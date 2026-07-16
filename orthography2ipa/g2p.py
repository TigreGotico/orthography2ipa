"""g2p — Top-level grapheme→IPA engine.

One obvious call to transcribe text in any covered language::

    >>> import orthography2ipa
    >>> orthography2ipa.transcribe("olá mundo", "pt")
    'oˈla ˈmundo'

The :class:`G2P` engine composes the package's pieces into a
data-driven pipeline:

1. **normalize** — a caller-supplied callable (diacritization, number
   expansion); identity by default.
2. **word split** — :class:`~orthography2ipa.phonetok.PhonetokTokenizer`
   token stream grouped at whitespace/punctuation; punctuation marks
   pausal positions.
3. **per-word search** — greedy (``beam_width=1``) or beam expansion of
   IPA candidates. Beaming per word avoids the combinatorial blow-up of
   whole-sentence beams.
4. **stress** — when the spec declares
   :class:`~orthography2ipa.types.StressRules`, the stressed syllable is
   detected (per-language syllabifier plugins are honoured) and marked.
5. **sandhi** — the spec's cross-word rules via
   :class:`~orthography2ipa.sandhi.SandhiEngine`.
6. **dialect transform** — :func:`~orthography2ipa.transforms.apply_transform`
   profile, applied last.

The engine is intentionally self-contained: it never loads external
G2P implementations. Downstream engines (arbtok for Arabic, tugaphone
for Portuguese) *consume* this library — its spec data, tokenizer,
stress rules and base types — and own their richer pipelines.
"""
from __future__ import annotations

import logging
import unicodedata
from dataclasses import dataclass, replace
from typing import Callable, List, Optional, Set, Tuple

from orthography2ipa.exceptions import UnmappedScriptError
from orthography2ipa.features import (
    GraphemeFeatures,
    WordFeatures,
    build_word_features,
)
from orthography2ipa.inventory import phoneme_inventory
from orthography2ipa.inventory import tokenize as inventory_tokenize
from orthography2ipa.lexicon import get_lexicon
from orthography2ipa.markup import MarkupError, parse_markup
from orthography2ipa.phonetok import (
    Candidate,
    IPAPath,
    PhonetokTokenizer,
    SegmentSlot,
    Token,
    TokenKind,
    flat_contexts,
    lattice_confidence,
    lower_str,
    slot_confidence,
)
from orthography2ipa.allophony import compile_allophone_rescorer
from orthography2ipa.positional import resolve_branches
from orthography2ipa.rescorer import (
    LatticeRescorer, RescorerArg, apply_rescorers, normalize_rescorers,
)
from orthography2ipa.registry import get, resolve
from orthography2ipa.sandhi import SandhiEngine
from orthography2ipa.sentence import (
    Position,
    SentenceLattice,
    SentenceRescorer,
    SentenceRescorerArg,
    WordSlot,
    apply_sentence_rescorers,
    normalize_sentence_rescorers,
    span_position,
)
from orthography2ipa.stress import (
    _syllables_for, apply_stress_mark, detect_stress, detect_stress_by_weight,
    syllabify, syllabify_ipa,
)
from orthography2ipa.types import LanguageSpec

__all__ = [
    "G2P",
    "transcribe",
    "WordTranscription",
    "TranscriptionResult",
    "ConfidenceBreakdown",
    "WordFeatures",
    "GraphemeFeatures",
    "UnmappedScriptError",
    "MarkupError",
]

_log = logging.getLogger(__name__)

_PAUSE_PUNCTUATION = set(".,;:!?…")

#: Sentinel ``stressed_syll_idx`` for a prosodic clitic (a word listed in
#: ``stress.cliticless_words``). It leans on its host and bears no lexical
#: stress, so no syllable is "the stressed one". A negative index never equals
#: a real 0-based syllable index, so ``RescoreContext.is_stressed`` reads
#: ``False`` (not ``None``) for every syllable: stress-gated allophone rules
#: (e.g. north-western tonic-mid diphthongisation) are withheld, while
#: unstressed-gated reduction rules still apply. The stress mark itself is
#: suppressed separately in ``_transcribe_word`` (Vigário 2003, *The Prosodic
#: Word in European Portuguese*, on clitics as non-prosodic-words).
_CLITIC_NO_STRESS = -1

#: Vowels never collapse — ⟨ee⟩/⟨oo⟩ are real long vowels, not doubled letters.
#: Length and stress marks are not segments, so a run is identical across them.
_VOWEL_IPA = set("aeiouɑɐɒæɓəɘɛɜɞɤɪɨɯɵøœʊʉʌʏyɶ")


def _collapse_geminates(ipa: str) -> str:
    """Collapse a run of the same consonant to one — ``sʌmmə`` → ``sʌmə``.

    For a language whose orthographic doubling is not gemination (``spec.
    collapse_geminates``). Only identical adjacent CONSONANT segments merge; a
    doubled vowel letter is a long vowel and is left alone, and a length or
    stress mark riding between two identical consonants does not block the
    merge (there is none to ride in these orthographies, but the guard is cheap).
    """
    out: List[str] = []
    for ch in ipa:
        if (out and ch == out[-1] and ch not in _VOWEL_IPA
                and ch not in "ːˑ" and not ch.isspace()):
            continue
        out.append(ch)
    return "".join(out)


@dataclass(frozen=True)
class WordTranscription:
    """One word of a transcription, with its alternatives."""

    word: str
    """Orthographic surface form (as it appeared after normalization)."""

    ipa: str
    """Chosen IPA transcription."""

    candidates: Tuple[IPAPath, ...] = ()
    """Beam alternatives, best first. Empty for greedy search."""

    unmapped: Tuple[str, ...] = ()
    """Characters in :attr:`word` with no grapheme mapping in the spec's
    table (i.e. the tokenizer emitted an ``UNKNOWN`` token for them).
    Empty when every character mapped, including for words that are
    genuinely silent (pure punctuation) — those never reach this stage
    since punctuation is stripped during word splitting."""

    coverage: float = 1.0
    """Fraction of :attr:`word`'s characters that mapped to a grapheme,
    in ``[0.0, 1.0]``. ``1.0`` when :attr:`unmapped` is empty."""

    confidence: float = 1.0
    """Per-word confidence that :attr:`ipa` is the right pronunciation, in
    ``[0.0, 1.0]`` — a pure, deterministic read off the pronunciation
    lattice (Workstream B5). It is the ``[0, 1]``-normalised weakest-link
    of three lattice signals: the top-1 vs top-2 ``cost`` **margin** per
    slot (small margin = ambiguous), the **rarity** of each slot's winning
    candidate (a high-cost winner is a rare mapping), and this word's
    :attr:`coverage` (any unmapped grapheme sharply lowers it). An
    unambiguous, fully-mapped word scores near ``1.0``; a known-ambiguous
    word (e.g. English ⟨th⟩) scores clearly lower; a word with an OOV
    character scores low. It exists so a downstream specialized phonemizer
    can spend its expensive lexicon/rules only where the base engine is
    unsure and trust the fallback elsewhere. See :meth:`G2P.word_confidence`
    and ``docs/lattice.md`` for the exact formula. ``1.0`` is the neutral
    default for a word built without the lattice (e.g. a plain
    :class:`WordTranscription` constructed by a caller)."""


@dataclass(frozen=True)
class ConfidenceBreakdown:
    """Richer, per-signal view behind :attr:`WordTranscription.confidence`.

    Returned by :meth:`G2P.confidence_breakdown`. All fields are in
    ``[0.0, 1.0]`` and derived purely from the lattice; :attr:`value` is the
    single number surfaced on :class:`WordTranscription`."""

    value: float
    """The headline confidence: :attr:`lattice` × :attr:`coverage`."""

    lattice: float
    """Weakest-link (minimum) per-slot confidence, before folding coverage."""

    per_slot: Tuple[float, ...] = ()
    """Each grapheme slot's confidence, in surface order."""

    coverage: float = 1.0
    """The word's grapheme coverage (OOV signal); < 1 when characters were
    unmapped."""

    unmapped: Tuple[str, ...] = ()
    """The unmapped characters folded into :attr:`coverage`, if any."""


@dataclass(frozen=True)
class TranscriptionResult:
    """Detailed result of :meth:`G2P.transcribe_detailed`."""

    ipa: str
    """Full transcription — word IPAs joined with spaces."""

    words: Tuple[WordTranscription, ...] = ()
    """Per-word breakdown, in input order."""

    lang: str = ""
    """The resolved canonical language code used."""


@dataclass(frozen=True)
class _Word:
    """Internal: a word occurrence in the input."""

    surface: str
    pausal: bool = False  # followed by pause punctuation or end of text
    sentence_initial: bool = False
    sentence_final: bool = False
    #: IPA the caller forced with ``<phoneme ph="…">``, bypassing the rules.
    forced_ipa: Optional[str] = None



def _as_names(plugins: dict) -> dict:
    """Normalise a caller's ``{stage: name}`` / ``{stage: [names]}`` to tuples."""
    return {
        stage: ((names,) if isinstance(names, str) else tuple(names))
        for stage, names in plugins.items()
    }


class _StagePlugins:
    """The plugins this engine runs, resolved once, per stage.

    Resolution is lazy per stage and cached: a spec that names nothing pays
    nothing, and a spec that names something missing fails the first time that
    stage runs — loudly, with the name it wanted and the names it found.
    """

    def __init__(self, spec, declared: dict) -> None:
        self._spec = spec
        self._declared = declared
        self._cache: dict = {}

    def get(self, stage: str) -> list:
        if stage not in self._cache:
            from dataclasses import replace

            from orthography2ipa.registry import get_declared_plugins

            # The caller's choice overrides the spec's, so resolve against the
            # merged view rather than the spec's own block.
            merged = replace(self._spec, plugins=self._declared)
            self._cache[stage] = get_declared_plugins(stage, merged)
        return self._cache[stage]


class G2P:
    """Grapheme→IPA engine for one language.

    Parameters
    ----------
    lang : str
        Language code; resolved like :func:`orthography2ipa.get` (bare
        tags, ISO 639-3 aliases and nearest-match all work).
    expand_allophones : bool
        Enumerate surface variants: branch the beam over every allophone of
        each phoneme from ``spec.allophones`` (flat ``+0.5`` cost each). This
        *inflates* the search space with every variant; it does not pick the
        contextually-correct one. Use it to see all surface possibilities.
        Independent of :paramref:`apply_allophony` (the realisation path).
    apply_allophony : bool
        Apply the spec's declarative ``allophone_rules`` — the post-lexical
        ``phoneme → surface`` realisation pass (Workstream B8) — as a
        rescorer after phoneme selection and before stress/sandhi. Default
        ``True``, but a **no-op for every spec that declares no**
        ``allophone_rules`` (i.e. all shipped specs bar the pilots), so the
        default engine path stays byte-identical. Set ``False`` to force
        broad/phonemic output even for a spec that declares rules. See
        :mod:`orthography2ipa.allophony`.
    dialect_profile : Optional[str]
        ``DIALECT_PROFILES`` key applied to the final IPA
        (see :func:`orthography2ipa.apply_transform`).
    apply_sandhi : bool
        Apply the spec's cross-word sandhi rules (default).
    apply_stress : bool
        Insert stress marks when the spec declares stress rules
        (default).
    normalizer : Optional[Callable[[str], str]]
        Pre-G2P text preparation (diacritization, number expansion);
        identity when omitted.
    on_unmapped : str
        How to react when a word contains characters absent from the
        spec's grapheme table (e.g. feeding Hanzi to a pinyin-only spec,
        or precomposed Hangul to a compatibility-jamo spec). One of:

        - ``"ignore"`` (default): no behavior change — the word's
          uncovered characters silently contribute nothing to ``ipa``,
          exactly as before this option existed. Inspect
          :attr:`WordTranscription.unmapped` /
          :attr:`WordTranscription.coverage` via
          :meth:`transcribe_detailed` to detect this after the fact.
        - ``"log"``: same output as ``"ignore"``, plus a
          ``logging.warning`` emitted once per distinct ``(lang, word)``
          pair.
        - ``"raise"``: raises
          :class:`~orthography2ipa.exceptions.UnmappedScriptError`
          instead of returning a result for that word.
    """

    def __init__(
        self,
        lang: str,
        *,
        expand_allophones: bool = False,
        dialect_profile: Optional[str] = None,
        apply_sandhi: bool = True,
        apply_stress: bool = True,
        apply_allophony: bool = True,
        normalizer: Optional[Callable[[str], str]] = None,
        plugins: Optional[dict] = None,
        on_unmapped: str = "ignore",
        rescorer: RescorerArg = None,
        sentence_rescorer: SentenceRescorerArg = None,
        allow_undeclared_phonemes: bool = False,
    ) -> None:
        self.allow_undeclared_phonemes = allow_undeclared_phonemes
        if on_unmapped not in ("ignore", "log", "raise"):
            raise ValueError(
                "on_unmapped must be 'ignore', 'log' or 'raise', "
                f"got {on_unmapped!r}")
        self.lang: str = resolve(lang)
        self.spec: LanguageSpec = get(self.lang)
        # User rescorer(s) first, then — as the post-lexical stage — the
        # allophone rescorer compiled from the spec's ``allophone_rules``.
        # A spec with no rules (every shipped spec bar the pilots) compiles
        # to ``None``, so the chain is exactly the user's rescorer(s) and the
        # default path is byte-identical.
        self.apply_allophony = apply_allophony
        user_rescorers: Tuple[LatticeRescorer, ...] = normalize_rescorers(
            rescorer)
        allophone_rescorer = (
            compile_allophone_rescorer(self.spec.allophone_rules)
            if apply_allophony else None
        )
        self._allophone_rescorer = allophone_rescorer

        # Rescorers come from DECLARED plugins only — named by the spec or by the
        # caller. Discovery alone never contributes phonology: a rescorer changes
        # the transcription, and `pip install` must not.
        #
        # The spec's own allophone rules run last and keep the last word: they are
        # declared data a language owner wrote, and a plugin refines that phonology
        # rather than overruling it.
        self._rescorers: Tuple[LatticeRescorer, ...] = (
            user_rescorers
            + ((allophone_rescorer,) if allophone_rescorer is not None else ())
        )
        self._plugin_rescorers_resolved = False
        self.expand_allophones = expand_allophones
        self.dialect_profile = dialect_profile
        self.apply_sandhi = apply_sandhi
        self.apply_stress = apply_stress
        self.normalizer = normalizer

        # Which plugin this engine runs, per stage. The SPEC names the ones that
        # are intrinsic to the language; the CALLER overrides, which is how a
        # downstream engine composes its own pipeline — arbtok does not edit this
        # library's shipped ar.json to say it wants a diacritizer, it passes one.
        #
        # Either way it is a DECLARATION. What is never allowed is for discovery
        # alone to decide: `pip install` must not change a transcription.
        self.plugins = {**(self.spec.plugins or {}), **_as_names(plugins or {})}
        self._stage_plugins = _StagePlugins(self.spec, self.plugins)

        declared_rescorers = tuple(
            r
            for plugin in self._stage_plugins.get("rescore")
            for r in plugin.rescorers(self.lang)
        )
        if declared_rescorers:
            allophone_last = (
                (self._allophone_rescorer,)
                if self._allophone_rescorer is not None else ()
            )
            base = tuple(
                r for r in self._rescorers if r is not self._allophone_rescorer
            )
            self._rescorers = base + declared_rescorers + allophone_last

        self.on_unmapped = on_unmapped
        self._warned_unmapped: Set[Tuple[str, str]] = set()
        self._tokenizer = PhonetokTokenizer(self.spec)
        self._sandhi = (
            SandhiEngine(self.spec.sandhi_rules)
            if self.spec.sandhi_rules else None
        )
        # Sentence-scope (cross-word) rescorers are opt-in and caller-supplied
        # only (no spec field): an empty tuple means the sentence seam never
        # runs and transcribe() is byte-identical to before this seam existed.
        self._sentence_rescorers: Tuple[SentenceRescorer, ...] = (
            normalize_sentence_rescorers(sentence_rescorer))

    # ─── public API ──────────────────────────────────────────────────

    def _normalize(self, text: str) -> str:
        """What the input IS, canonically, before anything reads it.

        The declared `normalize` plugin runs first — diacritic restoration for an
        abjad, number expansion — and then the caller's own normalizer, which is
        the last word because the caller is closest to the text.
        """
        for plugin in self._stage_plugins.get("normalize"):
            text = plugin.normalize(text, self.lang)
        if self.normalizer is not None:
            text = self.normalizer(text)
        return text

    def transcribe(
        self,
        text: str,
        *,
        search: str = "greedy",
        beam_width: int = 8,
    ) -> str:
        """Transcribe *text* to IPA.

        ``search="greedy"`` takes the best candidate per word
        (equivalent to ``beam_width=1``); ``search="beam"`` runs a
        per-word beam of *beam_width* hypotheses and keeps the best
        path, with alternatives available via
        :meth:`transcribe_detailed`.
        """
        return self.transcribe_detailed(
            text, search=search, beam_width=beam_width).ipa

    def transcribe_detailed(
        self,
        text: str,
        *,
        search: str = "greedy",
        beam_width: int = 8,
    ) -> TranscriptionResult:
        """Transcribe *text*, returning per-word detail."""
        width = self._width(search, beam_width)
        words = self._split_words(text)
        if not words:
            return TranscriptionResult(ipa="", words=(), lang=self.lang)

        transcribed: List[WordTranscription] = [
            self._transcribe_word(w.surface, width, forced_ipa=w.forced_ipa)
            for w in words
        ]

        ipa_words = [wt.ipa for wt in transcribed]
        # Sentence-scope (cross-word) rescorers run first — they see the whole
        # utterance's word lattices, adjacency and phrase/utterance position —
        # then the spec's declarative sandhi pass runs exactly as before. When
        # no sentence rescorer is configured (the default) this branch is
        # skipped entirely, so the pipeline below is byte-identical.
        if self._sentence_rescorers:
            lattice = self._build_sentence_lattice(words, transcribed, width)
            ipa_words = apply_sentence_rescorers(
                lattice, self._sentence_rescorers)
        if self.apply_sandhi and self._sandhi is not None:
            ipa_words = self._sandhi.apply(ipa_words)

        # Cross-word phonology that needs code rather than a declarative rule: a
        # final /n/ that assimilates to the next onset, a case ending a pause
        # removes. The plugin sees each word's SPELLING as well as its IPA — whether
        # a word ends in a case ending is a fact about the page, and guessing it
        # from the last characters of the IPA confuses an ending with a stem.
        for plugin in self._stage_plugins.get("sandhi"):
            surfaces = [w.surface for w in words]
            # The pause has to be HANDED to the plugin: punctuation is stripped
            # during word splitting, so by now it is gone from the input — and a
            # pause is exactly what removes a case ending.
            pausal = [w.pausal for w in words]
            rewritten = plugin.apply(
                list(ipa_words), surfaces, pausal, self.lang)
            if len(rewritten) != len(ipa_words):
                raise ValueError(
                    f"the sandhi plugin {type(plugin).__name__} returned "
                    f"{len(rewritten)} words for {len(ipa_words)} — it rewrote the "
                    f"sentence, not its sandhi"
                )
            ipa_words = rewritten

        ipa = " ".join(w for w in ipa_words if w)
        if self.dialect_profile:
            from orthography2ipa.transforms import apply_transform
            # The spelling the transform reads is the words', normalized — which is
            # also the only spelling there is: a forced word contributes the text it
            # wrapped, and the markup itself is not part of the utterance.
            ipa = apply_transform(ipa, self.dialect_profile,
                                  ortho=" ".join(w.surface for w in words))

        final_words = tuple(
            WordTranscription(word=wt.word, ipa=iw, candidates=wt.candidates,
                              unmapped=wt.unmapped, coverage=wt.coverage,
                              confidence=wt.confidence)
            for wt, iw in zip(transcribed, ipa_words)
        )
        return TranscriptionResult(ipa=ipa, words=final_words,
                                   lang=self.lang)

    def sentence_lattice(
        self,
        text: str,
        *,
        search: str = "greedy",
        beam_width: int = 8,
    ) -> SentenceLattice:
        """The whole utterance as an ordered :class:`~orthography2ipa.sentence.SentenceLattice`.

        Unlike :meth:`transcribe_detailed` (which flattens to strings), this
        exposes every word's per-grapheme lattice
        (:meth:`ipa_lattice`) **in order**, with word boundaries and each
        word's phrase / utterance :class:`~orthography2ipa.sentence.Position`,
        so a downstream cross-word rule can see the entire utterance's ranked
        candidates and positional context — the object a
        :class:`~orthography2ipa.sentence.SentenceRescorer` consumes.

        This is a **read** method: it never applies sentence rescorers or the
        spec's sandhi pass, and never affects :meth:`transcribe`. Its
        :attr:`~orthography2ipa.sentence.SentenceLattice.ipa` is the
        per-word (post-stress, pre-cross-word) reading.
        """
        width = self._width(search, beam_width)
        words = self._split_words(text)
        if not words:
            return SentenceLattice(words=(), lang=self.lang)
        transcribed = [self._transcribe_word(w.surface, width,
                                             forced_ipa=w.forced_ipa)
                       for w in words]
        return self._build_sentence_lattice(words, transcribed, width)

    def _build_sentence_lattice(
        self,
        words: List["_Word"],
        transcribed: List[WordTranscription],
        width: int,
    ) -> SentenceLattice:
        """Assemble a :class:`SentenceLattice` from the split words and their
        per-word transcriptions, attaching each word's lattice and its
        phrase / utterance position."""
        phrase_pos, utt_pos = self._word_positions(words)
        word_slots = tuple(
            WordSlot(
                surface=w.surface,
                ipa=wt.ipa,
                slots=tuple(self.ipa_lattice(w.surface, beam_width=width)),
                index=i,
                phrase_position=phrase_pos[i],
                utterance_position=utt_pos[i],
                pausal=w.pausal,
            )
            for i, (w, wt) in enumerate(zip(words, transcribed))
        )
        return SentenceLattice(words=word_slots, lang=self.lang)

    @staticmethod
    def _word_positions(
        words: List["_Word"],
    ) -> Tuple[List[Position], List[Position]]:
        """Compute each word's (phrase_position, utterance_position).

        Phrases are the punctuation-bounded runs the tokenizer already marks:
        a word with ``pausal=True`` is phrase-final, and the word after it
        opens the next phrase. The utterance span is the whole word list.
        """
        n = len(words)
        # Phrase spans: split after every pausal word.
        phrase: List[Position] = [Position.MEDIAL] * n
        start = 0
        for i, w in enumerate(words):
            if w.pausal or i == n - 1:
                for j in range(start, i + 1):
                    phrase[j] = span_position(j, start, i + 1)
                start = i + 1
        utt = [span_position(i, 0, n) for i in range(n)]
        return phrase, utt

    def transcribe_word(
        self,
        word: str,
        *,
        search: str = "greedy",
        beam_width: int = 8,
    ) -> str:
        """Transcribe a single *word*."""
        return self._transcribe_word(
            word, self._width(search, beam_width)).ipa

    def candidates(self, word: str, *, beam_width: int = 8) -> List[IPAPath]:
        """All beam candidates for a single *word*, best first."""
        return self._tokenizer.ipa_beam(
            word, beam_width=beam_width,
            expand_allophones=self.expand_allophones)

    def ipa_lattice(
        self, word: str, *, beam_width: int = 8
    ) -> List[SegmentSlot]:
        """Structured pronunciation lattice for a single *word*.

        Returns one :class:`~orthography2ipa.phonetok.SegmentSlot` per
        GRAPHEME token, in surface order, with ranked ``-log P``
        candidates. Unlike
        :meth:`PhonetokTokenizer.ipa_lattice`, the engine additionally
        supplies **stress/syllable context**, so the stress-conditioned
        nucleus positions fire — the slots reflect the same positional +
        weight scoring the engine uses to pick a pronunciation.

        The lattice is the *pre-lexical* phoneme lattice: it is built
        before stress-mark insertion and cross-word sandhi (which act on
        the whole utterance), and before any ``word_exceptions`` override.
        Concatenating each slot's top candidate therefore matches the
        engine's chosen pronunciation up to those later stages — it is the
        object a downstream rescorer (B4) or confidence signal (B5) reads.
        """
        keep = 2 ** 31 if beam_width < 0 else beam_width
        g_tokens = self._tokenizer.grapheme_tokens(word)
        if not g_tokens:
            return []
        contexts = flat_contexts(g_tokens)

        stressed_syll_idx: Optional[int] = None
        sylls: List[str] = []
        if self.spec.stress is not None:
            sylls = _syllables_for(word, self.lang, self.spec.stress.diphthongs
                                   if self.spec.stress else ())
            if len(sylls) > 1:
                stressed_syll_idx = detect_stress(
                    word, self.spec.stress, syllables=sylls)
            else:
                stressed_syll_idx = 0
            if self._is_cliticless(word):
                stressed_syll_idx = _CLITIC_NO_STRESS
        syll_for_token = self._map_tokens_to_syllables(g_tokens, sylls)

        allophone_map = (
            self.spec.allophones if self.expand_allophones else None)

        slots: List[SegmentSlot] = []
        for tok_idx, ctx in enumerate(contexts):
            branches = resolve_branches(
                self.spec, ctx,
                weights_for=self._tokenizer.weights_for,
                allophone_map=allophone_map,
                syll_idx=syll_for_token[tok_idx],
                stressed_syll_idx=stressed_syll_idx)
            tok = g_tokens[tok_idx]
            slots.append(SegmentSlot(
                grapheme=tok.grapheme,
                span=(tok.position, tok.position + tok.length),
                candidates=tuple(
                    Candidate(ipa=ipa, cost=cost) for ipa, cost in branches),
            ))

        if self._rescorers:
            # Re-cost with the engine's stress context, then truncate. A
            # rescorer that empties a slot deletes it from the lattice.
            slots = [
                s for s in apply_rescorers(
                    slots, contexts, self._rescorers,
                    syll_for_token=syll_for_token,
                    stressed_syll_idx=stressed_syll_idx)
                if s.candidates
            ]

        return [
            SegmentSlot(grapheme=s.grapheme, span=s.span,
                        candidates=s.candidates[:keep])
            for s in slots
        ]

    def word_confidence(self, word: str, *, beam_width: int = 8) -> float:
        """Per-word confidence for *word*, in ``[0.0, 1.0]`` (Workstream B5).

        A pure, deterministic read off the pronunciation lattice: the
        weakest-link (minimum) per-slot confidence — combining each slot's
        top-1 vs top-2 ``cost`` margin (ambiguity) and its winner's absolute
        ``cost`` (rarity) — multiplied by the word's grapheme ``coverage``
        (OOV signal). ``1.0`` for an unambiguous, fully-mapped word; clearly
        lower for a known-ambiguous word; low when a character is OOV. This
        is the number surfaced as :attr:`WordTranscription.confidence`; a
        downstream engine uses it to decide where to spend effort. See
        :func:`orthography2ipa.phonetok.slot_confidence` and
        ``docs/lattice.md``.
        """
        return self.confidence_breakdown(word, beam_width=beam_width).value

    def confidence_breakdown(
        self, word: str, *, beam_width: int = 8
    ) -> ConfidenceBreakdown:
        """Full :class:`ConfidenceBreakdown` behind :meth:`word_confidence`.

        Exposes the per-slot confidences, the pre-coverage lattice
        confidence, and the coverage/unmapped OOV signal separately, for a
        downstream engine that wants to localise *which* position the base
        engine was unsure about. A lexicon-``word_exceptions`` override is a
        certain answer, so its lattice confidence is ``1.0`` (only coverage
        can lower it).
        """
        override = self._override_for(word)
        unmapped, coverage = self._unmapped_chars(word)
        if override is not None:
            slots: List[SegmentSlot] = []
            per_slot: Tuple[float, ...] = ()
            lattice = 1.0
        else:
            slots = self.ipa_lattice(word, beam_width=beam_width)
            per_slot = tuple(slot_confidence(s) for s in slots)
            lattice = lattice_confidence(slots)
        return ConfidenceBreakdown(
            value=lattice * coverage,
            lattice=lattice,
            per_slot=per_slot,
            coverage=coverage,
            unmapped=unmapped,
        )

    def features(self, text: str) -> List[WordFeatures]:
        """Per-word linguistic **feature view** for downstream ML / CRF G2P.

        A PURE READ over the shared pronunciation lattice and grapheme
        context — it never affects :meth:`transcribe`. Returns one
        :class:`~orthography2ipa.features.WordFeatures` per word (using the
        same normalizer + word split as :meth:`transcribe`), each holding a
        :class:`~orthography2ipa.features.GraphemeFeatures` per grapheme with
        phonological-class predicates, word-local neighbours, the ranked
        ``(ipa, cost)`` candidate lattice, top-1 / margin, and the per-word
        confidence signal (Workstream B5).

        It reuses :meth:`ipa_lattice` (candidates + stress context),
        :meth:`confidence_breakdown` (the confidence value) and
        :func:`~orthography2ipa.phonetok.flat_contexts` (predicates +
        neighbours) — no vowel logic is recomputed. Every record's
        :meth:`~orthography2ipa.features.GraphemeFeatures.as_dict` is a flat,
        JSON-able, CRF-consumable feature dict. See ``docs/features.md`` for
        the CRF-as-rescorer pattern and a worked example.
        """
        out: List[WordFeatures] = []
        for w in self._split_words(text):
            word = w.surface
            slots = self.ipa_lattice(word)
            confidence = self.confidence_breakdown(word).value
            g_tokens = self._tokenizer.grapheme_tokens(word)
            contexts = flat_contexts(g_tokens)
            out.append(build_word_features(
                word, slots, contexts, confidence,
                self.spec.code, self.spec.script))
        return out

    # ─── pipeline stages ─────────────────────────────────────────────

    @staticmethod
    def _width(search: str, beam_width: int) -> int:
        if search == "greedy":
            return 1
        if search == "beam":
            return beam_width
        raise ValueError(
            f"search must be 'greedy' or 'beam', got {search!r}")

    def _split_words(self, text: str) -> List[_Word]:
        """Parse the input into words, forced pronunciations included.

        Markup is read *before* normalization, so a ``normalize`` plugin — a
        diacritizer, a number expander — never sees a tag. It is handed the plain
        runs and nothing else, which is the only text it has any business
        rewriting: the caller who wrote ``ph`` has already said what that word is.
        """
        words: List[_Word] = []
        for chunk in parse_markup(text):
            if chunk.is_forced:
                words.append(_Word(surface=chunk.text.strip(),
                                   forced_ipa=self._check_forced(chunk.forced_ipa)))
            else:
                self._group_words(self._normalize(chunk.text), words)
        return self._flag(words)

    def _check_forced(self, ipa: str) -> str:
        """Hold forced IPA to the spec's declared inventory.

        A symbol the spec never declares has no vector in a TTS frontend's
        embedding table — it is built from the declared inventory before training
        — so a word carrying it is mispronounced permanently, and silently. Better
        to say so here, at the call site that asked for it.
        """
        ipa = ipa.strip()
        if self.allow_undeclared_phonemes:
            return ipa
        declared = phoneme_inventory(self.spec)
        outside = [t for t in inventory_tokenize(ipa, self.spec) if t not in declared]
        if outside:
            raise MarkupError(
                f"<phoneme ph={ipa!r}> uses {outside!r}, which the {self.spec.code} "
                f"spec does not declare.\n\n"
                f"A phoneme outside the inventory has no embedding at synthesis time, "
                f"so the word carrying it is mispronounced permanently and silently. "
                f"This is the usual shape of a loanword forced in its donor's "
                f"phonology: English 'meeting' is not [ˈmiːtɪŋ] in Arabic, it is "
                f"nativised, and /ɪ/ and /ŋ/ are not Arabic phonemes.\n\n"
                f"Give the nativised reading, or — if the phonology really does have "
                f"this sound — declare it in the spec, where it can be read, cited "
                f"and diffed."
            )
        return ipa

    def _flag(self, words: List[_Word]) -> List[_Word]:
        """Mark the edges of the utterance. The last word stands before a pause."""
        if not words:
            return []
        return [
            replace(w, pausal=w.pausal or i == len(words) - 1,
                    sentence_initial=i == 0,
                    sentence_final=i == len(words) - 1)
            for i, w in enumerate(words)
        ]

    def _group_words(self, text: str, words: List[_Word]) -> None:
        """Group a plain run's token stream into words, appending to *words*.

        It appends rather than returns because a pause is not confined to the run
        it is written in: punctuation opening a plain run falls *after* whatever
        preceded it, and what preceded it may be a forced word. Grouping each run
        in isolation would drop that pause, and a pause is exactly what strips a
        case ending.
        """
        tokens = self._tokenizer.tokenize(text)
        current: List[str] = []

        def flush():
            if current:
                words.append(_Word(surface="".join(current)))
                current.clear()

        for token in tokens:
            if token.kind in (TokenKind.BOS, TokenKind.EOS):
                continue
            if token.kind == TokenKind.WHITESPACE:
                flush()
            elif token.kind == TokenKind.PUNCTUATION:
                flush()
                if words and any(c in _PAUSE_PUNCTUATION
                                 for c in token.grapheme):
                    words[-1] = _Word(surface=words[-1].surface,
                                      pausal=True)
            else:
                # Reconstruct the *surface* span, not just the grapheme key.
                # A token may consume more characters than its grapheme names:
                # an abugida consonant followed by a virama has a 1-character
                # grapheme but a 2-character span. Joining grapheme keys alone
                # would drop the virama from the rebuilt word, and the word is
                # re-tokenised downstream — so the suppressed inherent vowel
                # would silently come back. For every token whose span equals
                # its grapheme (i.e. every non-abugida token) the tail is empty
                # and the rebuilt word is unchanged.
                tail = token.text_span(text)[len(token.grapheme):]
                current.append(token.grapheme + tail)
        flush()

    def _override_for(self, word: str) -> Optional[str]:
        """Whole-word IPA override for *word*, or ``None`` to fall to rules.

        Precedence — inline ``spec.word_exceptions`` > sidecar lexicon
        (caller-registered; see :mod:`orthography2ipa.lexicon`) > ``None``. Both are matched on the same
        language-aware lowercased key, so a lexicon hit rejoins the *identical*
        override pathway an inline exception uses (stress-mark insertion,
        cross-word sandhi and ``confidence == 1.0`` all apply unchanged). The
        lexicon is read lazily on first use per language (see
        :mod:`orthography2ipa.lexicon`); a language with no sidecar gets an
        empty map here, so its behaviour is byte-identical to before E3.
        """
        key = lower_str(word, self.spec.code)
        exceptions = self.spec.word_exceptions
        if exceptions:
            inline = exceptions.get(key)
            if inline is not None:
                return inline
        lex = get_lexicon(self.lang)
        if lex:
            hit = lex.get(unicodedata.normalize("NFC", key))
            if hit is not None:
                return hit
        return None

    def _cliticless_keys(self) -> frozenset:
        """The spec's ``stress.cliticless_words`` as a normalized lookup set.

        Cached per engine. Keyed exactly like :meth:`_override_for` — language-
        aware lowercased and NFC-normalized — so a form listed in the spec's
        input orthography matches the input word regardless of case or Unicode
        composition.
        """
        cached = getattr(self, "_cliticless_cache", None)
        if cached is None:
            forms = (self.spec.stress.cliticless_words
                     if self.spec.stress is not None else ())
            cached = frozenset(
                unicodedata.normalize("NFC", lower_str(f, self.spec.code))
                for f in forms
            )
            self._cliticless_cache = cached
        return cached

    def _is_cliticless(self, word: str) -> bool:
        """Whether *word* is a declared prosodic clitic that takes no stress.

        A clitic leans on an adjacent host and lives inside the host's stress
        domain, so no word stress is placed on it (Watson 2002, ch. 3). This is
        an orthographic-form test — it cannot tell a clitic homograph from a
        full-word one — matching the spec's ``stress.cliticless_words``.
        """
        keys = self._cliticless_keys()
        if not keys:
            return False
        return unicodedata.normalize(
            "NFC", lower_str(word, self.spec.code)) in keys

    def _transcribe_word(self, word: str, width: int,
                         forced_ipa: Optional[str] = None) -> WordTranscription:
        override = forced_ipa if forced_ipa is not None else self._override_for(word)
        paths: List[IPAPath] = []
        if override is not None:
            ipa = override
        else:
            if self.spec.has_positional_data():
                paths = self._positional_beam(word, width)
            else:
                paths = self._tokenizer.ipa_beam(
                    word, beam_width=width,
                    expand_allophones=self.expand_allophones,
                    rescorer=self._rescorers or None)
            ipa = paths[0].ipa if paths else word
            if self.spec.collapse_geminates and ipa:
                ipa = _collapse_geminates(ipa)
        # A forced reading is not re-stressed: `ph` is the pronunciation, mark and
        # all. A caller who wrote a mark has placed the stress, and one who wrote
        # none has said this word carries none — re-deriving it from the spelling
        # would overrule the very thing being forced.
        if (forced_ipa is None
                and self.apply_stress and self.spec.stress is not None and ipa
                and not self._is_cliticless(word)):
            if self.spec.stress.quantity_sensitive:
                # Weight is a property of the transcription, not the spelling —
                # a syllable is heavy because its vowel is long or it has a
                # coda. So this system reads the IPA we just produced, and no
                # orthographic syllabification is involved.
                idx = detect_stress_by_weight(ipa, self.spec.stress)
                # Mark the mark against the SAME division the weights were read
                # off. The naive `syllabify` cuts `saːliq` as `sa|ːliq`, which
                # would drop the mark inside the long vowel: `saˈːliq`.
                ipa = apply_stress_mark(
                    ipa, self.spec.stress, idx,
                    ipa_syllables=syllabify_ipa(
                        ipa, self.spec.stress.max_onset),
                )
            else:
                sylls = _syllables_for(word, self.lang, self.spec.stress.diphthongs
                                       if self.spec.stress else ())
                idx = detect_stress(word, self.spec.stress, syllables=sylls)
                ipa = apply_stress_mark(ipa, self.spec.stress, idx,
                                        syllables=sylls)
        unmapped, coverage = self._unmapped_chars(word)
        if unmapped:
            self._handle_unmapped(word, unmapped)
        # Per-word confidence (B5): a lexicon override is a certain answer
        # (lattice_conf = 1.0); otherwise read the lattice's weakest-link
        # slot confidence. Coverage folds the OOV signal in either case.
        lattice_conf = (
            1.0 if override is not None
            else lattice_confidence(self.ipa_lattice(word))
        )
        confidence = lattice_conf * coverage
        return WordTranscription(
            word=word,
            ipa=ipa,
            candidates=tuple(paths) if width > 1 else (),
            unmapped=unmapped,
            coverage=coverage,
            confidence=confidence,
        )

    def _unmapped_chars(self, word: str) -> Tuple[Tuple[str, ...], float]:
        """Return (unmapped_chars, coverage) for *word*.

        ``unmapped_chars`` are the surface characters of any ``UNKNOWN``
        token the tokenizer produced for *word* — characters the spec's
        grapheme table does not cover. ``coverage`` is the fraction of
        ``GRAPHEME``/``UNKNOWN`` characters that mapped successfully.
        Punctuation/whitespace never reach this method (already stripped
        by :meth:`_split_words`), so it is not part of the calculation.
        """
        tokens = self._tokenizer.tokenize(word)
        unmapped: List[str] = []
        total_chars = 0
        for tok in tokens:
            if tok.kind == TokenKind.GRAPHEME:
                total_chars += tok.length
            elif tok.kind == TokenKind.UNKNOWN:
                unmapped.append(tok.grapheme)
                total_chars += tok.length
        if total_chars == 0:
            return (), 1.0
        coverage = (total_chars - len(unmapped)) / total_chars
        return tuple(unmapped), coverage

    def _handle_unmapped(self, word: str, unmapped: Tuple[str, ...]) -> None:
        if self.on_unmapped == "raise":
            raise UnmappedScriptError(word, unmapped, self.lang)
        if self.on_unmapped == "log":
            key = (self.lang, word)
            if key not in self._warned_unmapped:
                self._warned_unmapped.add(key)
                _log.warning(
                    "%s: word %r has unmapped characters %r not covered "
                    "by the grapheme table",
                    self.lang, word, "".join(unmapped),
                )

    # ─── positional beam search ──────────────────────────────────────────

    def _positional_beam(self, word: str, width: int) -> List[IPAPath]:
        """Beam search using positional grapheme overrides where available.

        For each grapheme token the positional context is computed from:
        - word boundary (first / last grapheme)
        - neighbour grapheme class (vowel / consonant)
        - intervocalic (vowel on both sides)
        - nucleus_stressed / nucleus_unstressed for vowel graphemes,
          derived from the spec's StressRules applied to the ortho word.

        Positional candidates are tried in priority order (most specific
        first).  For beam search the positional candidate is ranked first
        (score 0) and base-grapheme alternatives are appended at higher
        scores so the beam space is preserved.
        """
        g_tokens = self._tokenizer.grapheme_tokens(word)
        if not g_tokens:
            return self._tokenizer.ipa_beam(
                word, beam_width=width,
                expand_allophones=self.expand_allophones)

        # Flat-run context views: all grapheme tokens of the word stay
        # mutual neighbours (word-splitting already stripped punctuation),
        # so positional resolution matches the engine's neighbour rules.
        contexts = flat_contexts(g_tokens)

        # Determine stressed syllable index once (reuse for all vowels)
        stressed_syll_idx: Optional[int] = None
        sylls: List[str] = []
        if self.spec.stress is not None:
            sylls = _syllables_for(word, self.lang, self.spec.stress.diphthongs
                                   if self.spec.stress else ())
            if len(sylls) > 1:
                stressed_syll_idx = detect_stress(
                    word, self.spec.stress, syllables=sylls)
            else:
                stressed_syll_idx = 0  # monosyllable → always stressed
            if self._is_cliticless(word):
                stressed_syll_idx = _CLITIC_NO_STRESS

        # Map each grapheme token index to its syllable index
        syll_for_token = self._map_tokens_to_syllables(g_tokens, sylls)

        allophone_map = self.spec.allophones if self.expand_allophones else None
        beam: List[Tuple[List[str], float]] = [([], 0.0)]

        # Pre-resolve every slot's branches (with the engine's stress
        # context). When a rescorer is configured the slots are re-costed
        # through it — the engine path, unlike the standalone tokenizer,
        # supplies syllable/stress context to the RescoreContext.
        per_token_branches: List[List[Tuple[str, float]]] = [
            resolve_branches(
                self.spec, ctx,
                weights_for=self._tokenizer.weights_for,
                allophone_map=allophone_map,
                syll_idx=syll_for_token[tok_idx],
                stressed_syll_idx=stressed_syll_idx)
            for tok_idx, ctx in enumerate(contexts)
        ]
        if self._rescorers:
            slots = [
                SegmentSlot(
                    grapheme=g_tokens[i].grapheme,
                    span=(g_tokens[i].position,
                          g_tokens[i].position + g_tokens[i].length),
                    candidates=tuple(
                        Candidate(ipa=ipa, cost=cost) for ipa, cost in br))
                for i, br in enumerate(per_token_branches)
            ]
            rescored = apply_rescorers(
                slots, contexts, self._rescorers,
                syll_for_token=syll_for_token,
                stressed_syll_idx=stressed_syll_idx)
            per_token_branches = [
                [(c.ipa, c.cost) for c in s.candidates] for s in rescored
            ]

        for branches in per_token_branches:
            if not branches:
                # Rescorer deleted this slot: it contributes no segment.
                continue
            beam = PhonetokTokenizer._expand_beam(beam, branches, width)

        paths = [
            IPAPath(segments=tuple(segs), score=sc)
            for segs, sc in beam
        ]
        paths.sort(key=lambda p: (p.score, p.ipa))
        return paths

    @staticmethod
    def _map_tokens_to_syllables(
        tokens: List[Token], sylls: List[str]
    ) -> List[int]:
        """Map each grapheme token index to its 0-based syllable index.

        Walks syllables left-to-right consuming grapheme characters to
        assign each token to a syllable.  Falls back to 0 on mismatch.
        """
        if not sylls:
            return [0] * len(tokens)
        syll_idx = 0
        syll_consumed = 0  # chars consumed from current syllable
        result: List[int] = []
        for token in tokens:
            result.append(syll_idx)
            syll_consumed += len(token.grapheme)
            while syll_idx < len(sylls) and syll_consumed >= len(sylls[syll_idx]):
                syll_consumed -= len(sylls[syll_idx])
                syll_idx += 1
                if syll_idx >= len(sylls):
                    break
        return result


def transcribe(
    text: str,
    lang: str,
    *,
    search: str = "greedy",
    beam_width: int = 8,
    dialect_profile: Optional[str] = None,
) -> str:
    """One-call convenience: transcribe *text* in *lang* to IPA.

    Equivalent to ``G2P(lang, ...).transcribe(text, ...)``; build a
    :class:`G2P` instance directly for repeated calls or the full
    option set.
    """
    engine = G2P(lang, dialect_profile=dialect_profile)
    return engine.transcribe(text, search=search, beam_width=beam_width)
