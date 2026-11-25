"""g2p — Top-level grapheme→IPA engine.

One obvious call to transcribe text in any covered language::

    >>> import orthography2ipa
    >>> orthography2ipa.transcribe("olá mundo", "pt")
    'ɔˈla ˈmũdu'

:class:`G2P` compiles its spec to the IR (``docs/ir/o2i-ir-v1.md``) and runs
it on :class:`~orthography2ipa.ir.interpreter.Interpreter`. The engine runs
around the interpreter what a spec cannot hold: the lexicon, the
``Pipeline`` steps and the declared plugins, which the interpreter calls
through its host hooks.

The engine is intentionally self-contained: it never loads external
G2P implementations. Downstream engines (arbtok for Arabic, tugaphone
for Portuguese) *consume* this library — its spec data, tokenizer,
stress rules and base types — and own their richer pipelines.
"""
from __future__ import annotations

import functools
import logging
import unicodedata
import warnings
from dataclasses import dataclass, replace
from functools import cached_property
from typing import Callable, Dict, FrozenSet, List, Optional, Set, Tuple

from orthography2ipa.exceptions import (StubSpecWarning,
                                         UnmappedGraphemeWarning,
                                         UnmappedScriptError)
from orthography2ipa.features import (
    GraphemeFeatures,
    WordFeatures,
    build_word_features,
)
from orthography2ipa.inventory import phoneme_inventory
from orthography2ipa.inventory import tokenize as inventory_tokenize
from orthography2ipa.ir import interpreter as ir_kinds
from orthography2ipa.lexicon import _process_lexicon, _warn_deprecated
from orthography2ipa.markup import Chunk, MarkupError, parse_markup
from orthography2ipa.phonetok import (
    Candidate,
    IPAPath,
    GraphemeContext,
    SegmentSlot,
    Token,
    TokenKind,
    flat_contexts,
    lattice_confidence,
    slot_confidence,
)
from orthography2ipa.phonetok import _PUNCT_RE as _WORD_PUNCT_RE
from orthography2ipa.pipeline import Pipeline, _check_mark, _cut_marked
from orthography2ipa.vowels import is_ipa_vowel
from orthography2ipa.rescorer import (
    LatticeRescorer, RescorerArg, apply_rescorers, normalize_rescorers,
)
from orthography2ipa.registry import _get_declared_plugins, get, resolve
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
from orthography2ipa.stress import plugin_syllables
from orthography2ipa.types import GraphemePosition, LanguageSpec

# The compiler reads the constants and helpers below.

#: Punctuation clinging to either end of a raw word, which a whole-word
#: lookup strips. An apostrophe is not clinging punctuation: it spells an
#: elision (Catalan ``d'`` ``l'``, English ``goin'`` ``'em``, Afrikaans
#: ``'n``) and stays part of the key.
_EDGE_PUNCT_CHAR = rf"(?:(?!['\u2019]){_WORD_PUNCT_RE.pattern[:-1]})"

#: Apostrophe-family marks ``word_internal_apostrophe`` governs: U+0027 and
#: U+2019, the two codepoints ``_EDGE_PUNCT_CHAR`` already treats as a letter-like mark.
_APOSTROPHES = frozenset("'\u2019")
#: Hyphens that join the words of a compound (ASCII, U+2010, U+2011).
_HYPHENS = frozenset("-\u2010\u2011")

__all__ = [
    "G2P",
    "transcribe",
    "WordTranscription",
    "TranscriptionResult",
    "ConfidenceBreakdown",
    "WordFeatures",
    "GraphemeFeatures",
    "StubSpecWarning",
    "UnmappedScriptError",
    "MarkupError",
]

_log = logging.getLogger(__name__)


def _vowel_runs(ipa: str) -> List[Tuple[int, int]]:
    """The ``(start, end)`` spans of the vowel runs in *ipa*: each run is a
    vowel character and every vowel or combining mark that follows it."""
    runs: List[Tuple[int, int]] = []
    for i, c in enumerate(ipa):
        if is_ipa_vowel(c):
            if runs and runs[-1][1] == i:
                runs[-1] = (runs[-1][0], i + 1)
            else:
                runs.append((i, i + 1))
        elif runs and runs[-1][1] == i and unicodedata.combining(c):
            runs[-1] = (runs[-1][0], i + 1)
    return runs


#: Positions that read a vowel letter in an unstressed syllable. A value
#: listed there is a reduction product of that letter.
_UNSTRESSED_POSITIONS = frozenset({
    GraphemePosition.FIRST_PRETONIC,
    GraphemePosition.PRETONIC,
    GraphemePosition.POSTTONIC,
    GraphemePosition.NUCLEUS_UNSTRESSED,
    GraphemePosition.NUCLEUS_UNSTRESSED_OPEN,
    GraphemePosition.NUCLEUS_UNSTRESSED_CLOSED,
})


#: Vowels never collapse — ⟨ee⟩/⟨oo⟩ are real long vowels, not doubled letters.
#: Length and stress marks are not segments, so a run is identical across them.
_VOWEL_IPA = set("aeiouɑɐɒæɔəɘɛɜɞɤɪɨɯɵøœʊʉʌʏyɶ")


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
    and ``docs/engine/lattice.md`` for the exact formula. ``1.0`` is the neutral
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



def _as_names(plugins: dict) -> dict:
    """Normalise a caller's ``{stage: name}`` / ``{stage: [names]}`` to tuples."""
    return {
        stage: ((names,) if isinstance(names, str) else tuple(names))
        for stage, names in plugins.items()
    }


#: The :class:`Pipeline` field that replaces the old argument of each stage.
_STAGE_FIELDS = {
    "normalize": "Pipeline(expand=...) or Pipeline(mark=...)",
    "rescore": "Pipeline(rescore=...)",
    "sandhi": "Pipeline(sandhi=...)",
}
_STAGE_FIELDS_TEXT = ", ".join(f"{field} for {stage!r}" for stage, field in _STAGE_FIELDS.items())


def _field_stages(pipeline: Pipeline, named: dict, normalizer, rescorer,
                  sentence_rescorer) -> Tuple[str, ...]:
    """The plugin stages that *pipeline*'s fields take over.

    Raises :class:`ValueError` when a caller also passes the old argument for a
    stage, because either order would silently drop one of the two.
    """
    pairs = (
        ("normalize", pipeline.expand is not None or pipeline.mark is not None,
         "normalizer=", normalizer is not None),
        ("rescore", bool(pipeline.rescore), "rescorer=", rescorer is not None),
        ("sandhi", pipeline.sandhi is not None, "sentence_rescorer=",
         sentence_rescorer is not None),
    )
    for stage, field_set, old, old_set in pairs:
        if field_set and (old_set or named.get(stage)):
            raise ValueError(
                f"{old} and plugins={{{stage!r}: ...}} cannot run with "
                f"{_STAGE_FIELDS[stage]}: pass the field")
    return tuple(stage for stage, field_set, *_ in pairs if field_set)


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
            # The caller's choice overrides the spec's, so resolve against the
            # merged view rather than the spec's own block.
            merged = replace(self._spec, plugins=self._declared)
            self._cache[stage] = _get_declared_plugins(stage, merged)
        return self._cache[stage]


class G2P:
    """Grapheme→IPA engine for one language.

    Parameters
    ----------
    lang : str
        Language code; resolved like :func:`orthography2ipa.get` (bare
        tags, ISO 639-3 aliases and nearest-match all work).
    spec : Optional[LanguageSpec]
        Run on this spec instead of the registry's. For a caller whose spec
        is a variation on a shipped one — a ``dataclasses.replace`` copy
        that teaches the stress rules one more written accent, say — this is
        the way to build the engine on it, because the engine compiles the
        spec to its IR and never reads the attribute again. A spec the
        compiler refuses raises
        :class:`~orthography2ipa.ir.compiler.IRUnsupportedFeature` at the
        first transcription. The engine never writes to the spec, so the
        registry's shared object is unaffected either way; *lang* is still
        resolved, and still names the language the result is reported under.
    expand_allophones : bool
        Enumerate surface variants: branch the beam over every allophone of
        each phoneme from ``spec.allophones``, at ``+0.5`` cost per rank after
        the first. This
        *inflates* the search space with every variant; it does not pick the
        contextually-correct one. Use it to see all surface possibilities.
        Independent of :paramref:`apply_allophony` (the realisation path).
    apply_allophony : bool
        Apply the spec's declarative ``allophone_rules`` — the post-lexical
        ``phoneme → surface`` realisation pass — as a rescorer after phoneme
        selection and the caller's rescorers, and before stress marks and
        sandhi. Default ``True``. A spec that declares no ``allophone_rules``
        gives the same output either way. Set ``False`` to force
        broad/phonemic output even for a spec that declares rules. See
        :mod:`orthography2ipa.allophony`.
    dialect_profile : Optional[str]
        ``DIALECT_PROFILES`` key applied to the sentence IPA that
        :meth:`transcribe` and :meth:`transcribe_detailed` return
        (see :func:`orthography2ipa.apply_transform`). The word methods do
        not apply it.
    apply_sandhi : bool
        Apply the spec's cross-word ``sandhi_rules`` (default). ``False``
        does not turn off ``Pipeline(sandhi=...)``.
    apply_stress : bool
        Insert stress marks when the spec declares stress rules
        (default).
    normalizer : Optional[Callable[[str], str]]
        Deprecated: use ``Pipeline(expand=...)`` or ``Pipeline(mark=...)``.
        Pre-G2P text preparation (diacritization, number expansion);
        identity when omitted.
    rescorer, sentence_rescorer, plugins
        Deprecated: use ``Pipeline(rescore=...)``, ``Pipeline(sandhi=...)``
        and the ``Pipeline`` field of each stage. Each old argument that is
        not ``None`` warns :class:`DeprecationWarning`. An old argument for a
        stage whose ``Pipeline`` field is also set raises :class:`ValueError`.
    pipeline : Optional[Pipeline]
        The steps for this engine alone: ``lexicon``, ``syllabifier``,
        ``expand``, ``mark``, ``rescore`` and ``sandhi`` (see
        :class:`~orthography2ipa.pipeline.Pipeline`). Another engine in the
        same process does not see them.
    on_unmapped : str
        How to react when a word contains characters absent from the
        spec's grapheme table (e.g. feeding Hanzi to a pinyin-only spec,
        or precomposed Hangul to a compatibility-jamo spec). One of:

        - ``"warn"`` (default): the uncovered characters contribute
          nothing to ``ipa``, and each uncovered letter or combining mark
          (Unicode category ``L*`` or ``M*``) and each uncovered digit
          (``N*``) emits
          :class:`~orthography2ipa.exceptions.UnmappedGraphemeWarning`
          once per engine and character. Punctuation, symbols and
          spaces do not warn, and a stub spec does not warn per
          character.
        - ``"ignore"``: the same output with no signal. Inspect
          :attr:`WordTranscription.unmapped` /
          :attr:`WordTranscription.coverage` via
          :meth:`transcribe_detailed` to detect this after the fact.
        - ``"log"``: the same output, plus a ``logging.warning`` emitted
          once per distinct ``(lang, word)`` pair.
        - ``"raise"``: raises
          :class:`~orthography2ipa.exceptions.UnmappedScriptError`
          instead of returning a result for that word.

        In every mode, an engine on a stub spec warns
        :class:`~orthography2ipa.exceptions.StubSpecWarning` once, when
        it is built.
    allow_undeclared_phonemes : bool
        Accept forced ``<phoneme ph="...">`` IPA that holds a segment
        outside the spec's declared inventory. Default ``False``: such a
        forced reading raises :class:`~orthography2ipa.markup.MarkupError`.
    expose_ambiguous_endings : bool
        Let a list-valued ``grammatical_endings`` entry add its lower-ranked
        readings to the beam (default). The 1-best output is the same either
        way. The benchmark scoreboard sets it ``False``, so that its oracle
        columns measure ranking error only.
    """

    def __init__(
        self,
        lang: str,
        *,
        spec: Optional[LanguageSpec] = None,
        expand_allophones: bool = False,
        dialect_profile: Optional[str] = None,
        apply_sandhi: bool = True,
        apply_stress: bool = True,
        apply_allophony: bool = True,
        normalizer: Optional[Callable[[str], str]] = None,
        plugins: Optional[dict] = None,
        pipeline: Optional[Pipeline] = None,
        on_unmapped: str = "warn",
        rescorer: RescorerArg = None,
        sentence_rescorer: SentenceRescorerArg = None,
        allow_undeclared_phonemes: bool = False,
        expose_ambiguous_endings: bool = True,
    ) -> None:
        for name, value, stage in (("normalizer", normalizer, "normalize"),
                                   ("rescorer", rescorer, "rescore"),
                                   ("sentence_rescorer", sentence_rescorer, "sandhi")):
            if value is not None:
                _warn_deprecated(f"G2P({name}=...)", _STAGE_FIELDS[stage])
        if plugins is not None:
            _warn_deprecated("G2P(plugins=...)", _STAGE_FIELDS_TEXT)
        self.allow_undeclared_phonemes = allow_undeclared_phonemes
        self.pipeline: Pipeline = pipeline or Pipeline()
        named = _as_names(plugins or {})
        field_stages = _field_stages(
            self.pipeline, named, normalizer, rescorer, sentence_rescorer)
        #: Whether a list-valued ``grammatical_endings`` entry adds its
        #: lower-ranked readings to the beam. The scoreboard turns it off: the
        #: board defines ``PER - Oracle@k`` as ranking error, and an injected
        #: alternative lowers an oracle by construction (see
        #: docs/evaluation/benchmarks.md, "Injected alternatives do not count
        #: as ranking error"). 1-best is unaffected.
        self.expose_ambiguous_endings = expose_ambiguous_endings
        if on_unmapped not in ("warn", "ignore", "log", "raise"):
            raise ValueError(
                "on_unmapped must be 'warn', 'ignore', 'log' or 'raise', "
                f"got {on_unmapped!r}")
        self.lang: str = resolve(lang)
        self.spec: LanguageSpec = get(self.lang) if spec is None else spec
        if self.spec.plugins:
            _warn_deprecated(f"the plugins field of the {self.spec.code} spec", _STAGE_FIELDS_TEXT)
        if self.spec.stress is not None and self.spec.stress.source == "plugin":
            _warn_deprecated(f'stress.source = "plugin" in the {self.spec.code} spec',
                             "the stress rules of the spec")
        if self.is_stub:
            warnings.warn(
                f"{self.lang}: this spec has no grapheme table; every "
                f"transcription is the empty string and word_confidence() is "
                f"0.0. Pass on_unmapped='raise' to get UnmappedScriptError "
                f"per word instead.",
                StubSpecWarning, stacklevel=2)
        self.apply_allophony = apply_allophony
        self.expand_allophones = expand_allophones
        self.dialect_profile = dialect_profile
        self.apply_sandhi = apply_sandhi
        self.apply_stress = apply_stress
        self.normalizer = normalizer

        # The spec names the plugins intrinsic to the language and the caller
        # overrides them, so a downstream engine composes its own pipeline.
        # Discovery alone never decides.
        self.plugins = {**(self.spec.plugins or {}), **named}
        for stage in field_stages:
            self.plugins.pop(stage, None)
        self._stage_plugins = _StagePlugins(self.spec, self.plugins)

        # Rescorers come from the caller and the declared plugins only: a
        # rescorer changes the transcription, and ``pip install`` must not.
        # They run as an IR hook, before the spec's allophone rules.
        self._host_rescorers: Tuple[LatticeRescorer, ...] = normalize_rescorers(
            self.pipeline.rescore or rescorer) + tuple(
            r for plugin in self._stage_plugins.get("rescore") for r in plugin.rescorers(self.lang))

        self.on_unmapped = on_unmapped
        self._warned_unmapped: Set[Tuple[str, str]] = set()
        self._warned_graphemes: Set[str] = set()
        # Sentence-scope (cross-word) rescorers are caller-supplied only; an
        # empty tuple means the sentence seam never runs.
        self._sentence_rescorers: Tuple[SentenceRescorer, ...] = (
            normalize_sentence_rescorers(sentence_rescorer))
        self._lattice_cache: Dict[Tuple[str, int], List[SegmentSlot]] = {}
        self._caller_spec = spec is not None
        self._ir_width = 1

    @cached_property
    def _interpreter(self):
        """The IR interpreter of this engine with its host hooks. Raises
        :class:`~orthography2ipa.ir.compiler.IRUnsupportedFeature` for a spec
        the compiler refuses."""
        from orthography2ipa.ir.cache import interpreter
        from orthography2ipa.ir.compiler import build_ir
        from orthography2ipa.ir.interpreter import Hooks, Interpreter
        options = dict(dialect_profile=self.dialect_profile, apply_stress=self.apply_stress,
                       apply_allophony=self.apply_allophony, apply_sandhi=self.apply_sandhi,
                       expand_allophones=self.expand_allophones)
        if not self.expose_ambiguous_endings:
            options["expose_ambiguous_endings"] = False
        if self.pipeline.fragments:
            options["fragments"] = self.pipeline.fragments
        if self._caller_spec or self.spec.plugins:
            # The host runs the declared plugins, so the IR is compiled
            # without them. A caller spec is compiled for this engine alone.
            it = Interpreter(build_ir(self.lang, spec=replace(self.spec, plugins=None), **options))
        else:
            it = interpreter(self.lang, **options)
        normalizers = [functools.partial(plugin.normalize, lang=self.lang)
                       for plugin in self._stage_plugins.get("normalize")]
        if self.normalizer is not None:
            normalizers.append(self.normalizer)
        sandhi = self.pipeline.sandhi
        self._sandhi_plugins = [sandhi] if sandhi is not None else self._stage_plugins.get("sandhi")
        hooks = Hooks(
            text=(lambda run: functools.reduce(lambda t, f: f(t), normalizers, run))
            if normalizers else None,
            rescore=self._ir_rescore if self._host_rescorers else None,
            syllables=self._ir_syllables if self.pipeline.syllabifier is not None else None,
            sandhi=self._ir_sandhi if self._sandhi_plugins or self._sentence_rescorers else None)
        return it if hooks == Hooks() else it.with_hooks(hooks)

    def _ir_rescore(self, word: str, tokens, slots, syllables, stressed):
        """Run the caller's rescorers on the beam slots of *word*. A cost
        crosses from integer micro-units to a float and back by
        ``round(cost * 1_000_000)``, the rule the compiler costs the IR by."""
        g_tokens = [Token(TokenKind.GRAPHEME, t.grapheme, t.readings, t.position, t.length)
                    for t in tokens]
        if syllables is not None:
            contexts = flat_contexts(g_tokens, self.spec.vowel_graphemes)
        else:
            # Without syllable context a gap in the word (an unknown
            # character) ends a run of neighbours, as on the tokenizer beam.
            contexts = []
            start = 0
            for i, tok in enumerate(g_tokens):
                if i and tok.position != g_tokens[i - 1].position + g_tokens[i - 1].length:
                    start = i
                if i == start:
                    run: list = []
                run.append(GraphemeContext(tok, i, run, i - start, self.spec.vowel_graphemes))
                contexts.append(run[-1])
        seg_slots = [SegmentSlot(grapheme=t.grapheme, span=(t.position, t.position + t.length),
                                 candidates=tuple(Candidate(ipa, cost / 1_000_000) for ipa, cost in slot))
                     for t, slot in zip(g_tokens, slots)]
        rescored = apply_rescorers(seg_slots, contexts, self._host_rescorers,
                                   syll_for_token=syllables, stressed_syll_idx=stressed)
        return [[(c.ipa, round(c.cost * 1_000_000)) for c in s.candidates] for s in rescored]

    def _ir_syllables(self, word: str) -> Optional[List[str]]:
        return plugin_syllables(word, self.lang, self.pipeline.syllabifier)

    def _ir_sandhi(self, ipa_words: List[str], surfaces: List[str],
                   pausal: List[bool]) -> List[str]:
        """The sentence rescorers, then the sandhi plugins."""
        if self._sentence_rescorers:
            words = [ir_kinds._Word(s, pausal=p) for s, p in zip(surfaces, pausal)]
            transcribed = [WordTranscription(word=s, ipa=ipa) for s, ipa in zip(surfaces, ipa_words)]
            lattice = self._build_sentence_lattice(words, transcribed, self._ir_width)
            ipa_words = apply_sentence_rescorers(lattice, self._sentence_rescorers)
        for plugin in self._sandhi_plugins:
            rewritten = plugin.apply(list(ipa_words), surfaces, pausal, self.lang)
            if len(rewritten) != len(ipa_words):
                raise ValueError(
                    f"the sandhi plugin {type(plugin).__name__} returned "
                    f"{len(rewritten)} words for {len(ipa_words)} — it rewrote the "
                    f"sentence, not its sandhi"
                )
            ipa_words = rewritten
        return list(ipa_words)

    def _ir_runs(self, text: str) -> List[Tuple[str, Optional[str]]]:
        """*text* after ``expand`` and ``mark``, as interpreter runs: a plain
        run, or a forced word with its checked IPA."""
        return [(chunk.text, self._check_forced(chunk.forced_ipa)) if chunk.is_forced
                else (chunk.text, None)
                for chunk in self._prepared(parse_markup(text))]

    def _ir_lexicon(self):
        lexicon = self.pipeline.lexicon
        return _process_lexicon(self.lang) or None if lexicon is None else lexicon

    def _transcribe_ir(self, it, text: str, width: int) -> TranscriptionResult:
        lexicon = self._ir_lexicon()
        self._ir_width = width
        result = it.transcribe_runs(self._ir_runs(text), width=width, lexicon=lexicon)
        words = tuple(self._ir_word(it, wr, width, lexicon) for wr in result.words)
        return TranscriptionResult(ipa=result.ipa, words=words, lang=self.lang)

    @staticmethod
    def _ir_surface(it, word: str) -> str:
        """*word* as the word views index it: S1, then NFC."""
        return unicodedata.normalize("NFC", it.prepare(word))

    def _ir_key(self, it, word: str, lexicon) -> str:
        """The spelling a word method transcribes: *word* itself when it has an
        override, as an override is looked up before S1, else its
        NFC surface."""
        return word if it._override_for(word, lexicon) is not None else self._ir_surface(it, word)

    def _ir_word(self, it, wr, width: int, lexicon) -> WordTranscription:
        """The :class:`WordTranscription` of the interpreter's word result *wr*."""
        unmapped, coverage = self._unmapped_chars(wr.word)
        if unmapped:
            self._handle_unmapped(wr.word, unmapped)
        override = wr.forced or it._override_for(wr.word, lexicon) is not None
        confidence = 1.0 if override else lattice_confidence(self.ipa_lattice(wr.word))
        candidates = tuple(IPAPath(segs, cost / 1_000_000) for segs, cost in wr.paths) if width > 1 else ()
        return WordTranscription(word=unicodedata.normalize("NFC", wr.word), ipa=wr.ipa, candidates=candidates,
                                 unmapped=unmapped, coverage=coverage,
                                 confidence=confidence * coverage)

    def _ir_words(self, it, text: str, lexicon):
        """The words of *text* as the interpreter groups them, the last one
        pausal, each surface in NFC."""
        words = it.words(self._ir_runs(text), lexicon)
        for w in words:
            w.surface = unicodedata.normalize("NFC", w.surface)
        return words

    def _ir_compound_elements(self, it, word: str, lexicon):
        """The elements of *word* when the spec stresses it as one
        hyphen-joined compound, or ``None``. An override for the whole
        spelling wins, as it does for any word."""
        if (it.stress is None or not it.stress["compound_last"]
                or not _HYPHENS.intersection(word)
                or it._override_for(word, lexicon) is not None):
            return None
        elements = it.words([(word, None)], lexicon)
        if len(elements) < 2 or not all(w.hyphen_joined for w in elements[1:]):
            return None
        return elements

    # ─── public API ──────────────────────────────────────────────────

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
        return self._transcribe_ir(self._interpreter, text, self._width(search, beam_width))


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
        it = self._interpreter
        lexicon = self._ir_lexicon()
        words = self._ir_words(it, text, lexicon)
        transcribed = [self._ir_word(it, it.transcribe_word(w.surface, width, lexicon, w.forced),
                                     width, lexicon) for w in words]
        return self._build_sentence_lattice(words, transcribed, width)

    def _build_sentence_lattice(
        self,
        words: List[ir_kinds._Word],
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
        words: List[ir_kinds._Word],
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

    @property
    def is_stub(self) -> bool:
        """Whether this engine's spec has no grapheme table at all.

        A clade node is not a stub (it is not a language); a language spec
        with neither ``graphemes`` nor ``positional_graphemes`` is, and every
        word it is given comes back empty. See
        :class:`~orthography2ipa.exceptions.StubSpecWarning`.
        """
        if self.spec.clade:
            return False
        return not self.spec.graphemes and not self.spec.positional_graphemes

    def transcribe_word(
        self,
        word: str,
        *,
        search: str = "greedy",
        beam_width: int = 8,
    ) -> str:
        """Transcribe a single *word*.

        A hyphen-joined word that the spec stresses as one compound
        (``compound_stress="last"``) is transcribed element by element and
        marked as :meth:`transcribe` marks it, but returned as one token,
        with no space between the elements.
        """
        width = self._width(search, beam_width)
        it = self._interpreter
        lexicon = self._ir_lexicon()
        elements = self._ir_compound_elements(it, word, lexicon)
        surfaces = [self._ir_key(it, word, lexicon)] if elements is None else [w.surface for w in elements]
        ipa_words = [self._ir_word(it, it.transcribe_word(w, width, lexicon), width, lexicon).ipa
                     for w in surfaces]
        if elements is not None:
            ipa_words = it._mark_compounds(elements, ipa_words)
        ipa = "".join(ipa_words)
        return unicodedata.normalize("NFC", ipa) if ipa else ipa

    def candidates(self, word: str, *, beam_width: int = 8) -> List[IPAPath]:
        """All beam candidates for a single *word*, best first."""
        it = self._interpreter
        width = 2 ** 31 if beam_width < 0 else beam_width
        return [IPAPath(segments=segs, score=cost / 1_000_000, graphemes=graphemes)
                for segs, cost, graphemes in it._word_paths(
                    self._ir_surface(it, word), width, context=False, allophony=False)]

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
        the whole utterance), and before any word-level override —
        ``word_exceptions`` or the ``grammatical_endings`` tail rewrite.
        Concatenating each slot's top candidate therefore matches the
        engine's chosen pronunciation up to those later stages — it is the
        object a downstream rescorer (B4) or confidence signal (B5) reads.
        """
        keep = 2 ** 31 if beam_width < 0 else beam_width
        cache_key = (word, keep)
        cached = self._lattice_cache.get(cache_key)
        if cached is not None:
            # SegmentSlot is frozen, so sharing the elements is safe; a fresh
            # list guards the cache against a caller that mutates the sequence.
            return list(cached)
        it = self._interpreter
        result = [
            SegmentSlot(grapheme=tok.grapheme, span=(tok.position, tok.position + tok.length),
                        candidates=tuple(Candidate(ipa=ipa, cost=cost / 1_000_000)
                                         for ipa, cost in cands[:keep]))
            for tok, cands in it.lattice(self._ir_surface(it, word))]
        self._lattice_cache[cache_key] = result
        return list(result)

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
        ``docs/engine/lattice.md``.
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
        override = self._interpreter._override_for(word, self._ir_lexicon())
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
        JSON-able, CRF-consumable feature dict. See ``docs/engine/lattice.md#feature-export-for-a-learned-model`` for
        the CRF-as-rescorer pattern and a worked example.
        """
        out: List[WordFeatures] = []
        it = self._interpreter
        for w in self._ir_words(it, text, self._ir_lexicon()):
            word = w.surface
            slots = self.ipa_lattice(word)
            confidence = self.confidence_breakdown(word).value
            g_tokens = [Token(TokenKind.GRAPHEME, t.grapheme, t.readings, t.position, t.length)
                        for t in it.grapheme_tokens(word)]
            contexts = flat_contexts(g_tokens, self.spec.vowel_graphemes)
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


    def _prepared(self, chunks: List[Chunk]) -> List[Chunk]:
        """*chunks* after the pipeline's ``expand`` and ``mark``."""
        expand, mark = self.pipeline.expand, self.pipeline.mark
        if expand is not None:
            chunks = [chunk if chunk.is_forced
                      else replace(chunk, text=expand(chunk.text))
                      for chunk in chunks]
        if mark is None:
            return chunks
        text = "".join(chunk.text for chunk in chunks)
        marked = mark(text)
        _check_mark(text, marked)
        return _cut_marked(marked, chunks)


    @cached_property
    def _declared_inventory(self) -> FrozenSet[str]:
        """The phoneme inventory of the spec and the pipeline lexicon."""
        return phoneme_inventory(self.spec, self.pipeline.lexicon)

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
        # The process-wide lexicon can change between calls; an engine's own
        # lexicon and its spec cannot, so their inventory is read once.
        declared = (phoneme_inventory(self.spec) if self.pipeline.lexicon is None
                    else self._declared_inventory)
        outside = [t for t in inventory_tokenize(ipa, self.spec) if t not in declared]
        if outside:
            raise MarkupError(
                f"<phoneme ph={ipa!r}> uses {outside!r}, which the {self.spec.code} "
                f"spec does not declare.\n\n"
                f"The inventory is every segment the spec's tables can emit, "
                f"allophones included. A symbol outside it has no embedding at "
                f"synthesis time, so the word carrying it is mispronounced "
                f"permanently and silently. This is the usual shape of a loanword "
                f"forced in its donor's phonology.\n\n"
                f"Give the nativised reading, or — if the phonology really does have "
                f"this sound — declare it in the spec, where it can be read, cited "
                f"and diffed."
            )
        return ipa


    def word_candidates(self, word: str, *, k: int = 5,
                        beam_width: Optional[int] = None) -> List[str]:
        """The top-*k* full transcriptions of *word*, best first.

        Unlike :meth:`candidates`, which exposes the RAW beam paths (no
        stress marks, no geminate collapse, no grammatical-ending
        rewrite, no lexicon override), every string returned here has
        been through the same word-final pipeline as
        :meth:`transcribe_word` — geminate collapse, grammatical-ending
        rewrite, stress marking, and the lexicon/``word_exceptions``
        override.

        Element 0 is normally ``transcribe_word(word)``, but that is an
        EMPIRICAL property, not a guarantee. :meth:`transcribe_word`
        defaults to ``search="greedy"``, which prunes to a single
        hypothesis at every step; this method runs a real beam of
        ``max(k, 8)``. A wider beam may reach a cheaper path that greedy
        pruning discarded, in which case element 0 is the BETTER reading
        and differs from :meth:`transcribe_word`. Pass
        ``beam_width=1`` to force the greedy path and make the identity
        hold by construction, at the cost of getting one candidate.

        The benchmark harness relies on the identity to make oracle@k
        comparable to the 1-best PER, so it re-checks it on every run
        and aborts on a mismatch rather than trusting it.

        Duplicates are collapsed (two beam paths often finalize to the
        same string once stress and geminate collapse have run), so the
        result may be shorter than *k*. A word with a lexicon or
        ``word_exceptions`` override has exactly ONE reading — the
        override — and the list has length 1: no beam is consulted. A
        hyphen-joined compound (``compound_stress="last"``) also has one
        reading, the one :meth:`transcribe_word` returns.

        *beam_width* defaults to ``max(k, 8)``; a beam narrower than *k*
        cannot produce *k* readings.

        Returns an EMPTY list for a word with no pronounceable output
        (every path finalized to an empty string) — the caller decides
        what that means rather than receiving a fabricated reading.
        """
        if k < 1:
            raise ValueError(f"k must be >= 1, got {k}")
        width = max(k, 8) if beam_width is None else beam_width
        it = self._interpreter
        lexicon = self._ir_lexicon()
        word = self._ir_key(it, word, lexicon)
        override = it._override_for(word, lexicon)
        if override is not None:
            return [unicodedata.normalize("NFC", it._finalize(word, override, None, collapse=False))]
        if self._ir_compound_elements(it, word, lexicon) is not None:
            compound = self.transcribe_word(word)
            return [compound] if compound else []
        paths = it._apply_ending(word, it._word_paths(word, width))
        out: List[str] = []
        for path in paths[:k] or [((word,), 0, ())]:
            final = unicodedata.normalize("NFC", it._finalize(word, "".join(path[0]), path, collapse=True))
            if final and final not in out:
                out.append(final)
        return out


    def _unmapped_chars(self, word: str) -> Tuple[Tuple[str, ...], float]:
        """Return (unmapped_chars, coverage) for *word*.

        ``unmapped_chars`` are the surface characters of any ``UNKNOWN``
        or ``DIGIT`` token the tokenizer produced for *word* — characters the
        spec's grapheme table does not cover, so the transcription drops them.
        ``coverage`` is the fraction of ``GRAPHEME``/``UNKNOWN``/``DIGIT``
        characters that mapped successfully.
        Punctuation/whitespace never reach this method (already stripped
        by the word split), so it is not part of the calculation.
        """
        it = self._interpreter
        unmapped: List[str] = []
        total_chars = 0
        for tok in it.tokenize(self._ir_surface(it, word)):
            if tok.kind == ir_kinds.WORD:
                total_chars += tok.length
            elif tok.kind == ir_kinds.UNKNOWN:
                unmapped.append(tok.grapheme)
                total_chars += tok.length
            elif tok.kind == ir_kinds.DIGIT:
                unmapped.extend(tok.grapheme)
                total_chars += tok.length
        if total_chars == 0:
            return (), 1.0
        coverage = (total_chars - len(unmapped)) / total_chars
        return tuple(unmapped), coverage

    def _handle_unmapped(self, word: str, unmapped: Tuple[str, ...]) -> None:
        if self.on_unmapped == "warn" and not self.is_stub:
            for ch in unmapped:
                if (unicodedata.category(ch)[0] not in "LMN"
                        or ch in self._warned_graphemes):
                    continue
                self._warned_graphemes.add(ch)
                warnings.warn(
                    f"{self.lang}: U+{ord(ch):04X} {ch!r} "
                    f"({unicodedata.name(ch, 'unnamed')}) has no grapheme "
                    f"mapping and is dropped from the transcription",
                    UnmappedGraphemeWarning, stacklevel=2)
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
