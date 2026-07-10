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
from dataclasses import dataclass
from typing import Callable, List, Optional, Set, Tuple

from orthography2ipa.exceptions import UnmappedScriptError
from orthography2ipa.phonetok import (
    IPAPath,
    PhonetokTokenizer,
    Token,
    TokenKind,
    flat_contexts,
    lower_str,
)
from orthography2ipa.positional import resolve_branches
from orthography2ipa.registry import get, resolve
from orthography2ipa.sandhi import SandhiEngine
from orthography2ipa.stress import _syllables_for, apply_stress_mark, detect_stress, syllabify
from orthography2ipa.types import LanguageSpec

__all__ = [
    "G2P",
    "transcribe",
    "WordTranscription",
    "TranscriptionResult",
    "UnmappedScriptError",
]

_log = logging.getLogger(__name__)

_PAUSE_PUNCTUATION = set(".,;:!?…")


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


class G2P:
    """Grapheme→IPA engine for one language.

    Parameters
    ----------
    lang : str
        Language code; resolved like :func:`orthography2ipa.get` (bare
        tags, ISO 639-3 aliases and nearest-match all work).
    expand_allophones : bool
        Branch beam candidates over allophonic variants too.
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
        normalizer: Optional[Callable[[str], str]] = None,
        on_unmapped: str = "ignore",
    ) -> None:
        if on_unmapped not in ("ignore", "log", "raise"):
            raise ValueError(
                "on_unmapped must be 'ignore', 'log' or 'raise', "
                f"got {on_unmapped!r}")
        self.lang: str = resolve(lang)
        self.spec: LanguageSpec = get(self.lang)
        self.expand_allophones = expand_allophones
        self.dialect_profile = dialect_profile
        self.apply_sandhi = apply_sandhi
        self.apply_stress = apply_stress
        self.normalizer = normalizer
        self.on_unmapped = on_unmapped
        self._warned_unmapped: Set[Tuple[str, str]] = set()
        self._tokenizer = PhonetokTokenizer(self.spec)
        self._sandhi = (
            SandhiEngine(self.spec.sandhi_rules)
            if self.spec.sandhi_rules else None
        )

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
        width = self._width(search, beam_width)
        normalized = (self.normalizer(text) if self.normalizer is not None
                      else text)
        words = self._split_words(normalized)
        if not words:
            return TranscriptionResult(ipa="", words=(), lang=self.lang)

        transcribed: List[WordTranscription] = [
            self._transcribe_word(w.surface, width) for w in words
        ]

        ipa_words = [wt.ipa for wt in transcribed]
        if self.apply_sandhi and self._sandhi is not None:
            ipa_words = self._sandhi.apply(ipa_words)

        ipa = " ".join(w for w in ipa_words if w)
        if self.dialect_profile:
            from orthography2ipa.transforms import apply_transform
            ipa = apply_transform(ipa, self.dialect_profile,
                                  ortho=normalized)

        final_words = tuple(
            WordTranscription(word=wt.word, ipa=iw, candidates=wt.candidates,
                              unmapped=wt.unmapped, coverage=wt.coverage)
            for wt, iw in zip(transcribed, ipa_words)
        )
        return TranscriptionResult(ipa=ipa, words=final_words,
                                   lang=self.lang)

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
        """Group the token stream into words with pausal/position flags."""
        tokens = self._tokenizer.tokenize(text)
        words: List[_Word] = []
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
                current.append(token.grapheme)
        flush()

        if not words:
            return []
        flagged = [
            _Word(surface=w.surface, pausal=w.pausal or i == len(words) - 1,
                  sentence_initial=i == 0,
                  sentence_final=i == len(words) - 1)
            for i, w in enumerate(words)
        ]
        return flagged

    def _transcribe_word(self, word: str, width: int) -> WordTranscription:
        exceptions = self.spec.word_exceptions
        override = exceptions.get(lower_str(word, self.spec.code)) if exceptions else None
        paths: List[IPAPath] = []
        if override is not None:
            ipa = override
        else:
            if self.spec.has_positional_data():
                paths = self._positional_beam(word, width)
            else:
                paths = self._tokenizer.ipa_beam(
                    word, beam_width=width,
                    expand_allophones=self.expand_allophones)
            ipa = paths[0].ipa if paths else word
        if (self.apply_stress and self.spec.stress is not None and ipa):
            sylls = _syllables_for(word, self.lang)
            idx = detect_stress(word, self.spec.stress, syllables=sylls)
            ipa = apply_stress_mark(ipa, self.spec.stress, idx,
                                    syllables=sylls)
        unmapped, coverage = self._unmapped_chars(word)
        if unmapped:
            self._handle_unmapped(word, unmapped)
        return WordTranscription(
            word=word,
            ipa=ipa,
            candidates=tuple(paths) if width > 1 else (),
            unmapped=unmapped,
            coverage=coverage,
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
            sylls = _syllables_for(word, self.lang)
            if len(sylls) > 1:
                stressed_syll_idx = detect_stress(
                    word, self.spec.stress, syllables=sylls)
            else:
                stressed_syll_idx = 0  # monosyllable → always stressed

        # Map each grapheme token index to its syllable index
        syll_for_token = self._map_tokens_to_syllables(g_tokens, sylls)

        allophone_map = self.spec.allophones if self.expand_allophones else None
        beam: List[Tuple[List[str], float]] = [([], 0.0)]

        for tok_idx, ctx in enumerate(contexts):
            # Positional resolution (incl. E1 vowel-class positions) is the
            # SAME shared code the standalone tokenizer beam uses; the
            # engine additionally supplies stress/syllable context so the
            # nucleus positions fire.
            branches = resolve_branches(
                self.spec, ctx,
                weights_for=self._tokenizer.weights_for,
                allophone_map=allophone_map,
                syll_idx=syll_for_token[tok_idx],
                stressed_syll_idx=stressed_syll_idx)

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
