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
from orthography2ipa.phonetok import IPAPath, PhonetokTokenizer, Token, TokenKind
from orthography2ipa.registry import get, resolve
from orthography2ipa.sandhi import SandhiEngine
from orthography2ipa.stress import _syllables_for, apply_stress_mark, detect_stress, syllabify
from orthography2ipa.types import GraphemePosition, LanguageSpec

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
        override = exceptions.get(word.lower()) if exceptions else None
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

    _VOWEL_CHARS = frozenset(
        "aeiouáéíóúàèìòùâêîôûãõäëïöüåæøAEIOUÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÄËÏÖÜÅÆØ"
    )

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

        n = len(g_tokens)

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

        for tok_idx, token in enumerate(g_tokens):
            grapheme = token.grapheme
            next_tok = g_tokens[tok_idx + 1] if tok_idx + 1 < n else None
            prev_tok = g_tokens[tok_idx - 1] if tok_idx > 0 else None

            # Determine applicable positions (most-specific first)
            positions = self._positions_for_token(
                grapheme, tok_idx, n, prev_tok, next_tok,
                syll_for_token[tok_idx], stressed_syll_idx,
            )

            # Build branch list: positional candidates ranked first
            branches = self._positional_branches(
                grapheme, token, positions, allophone_map)

            beam = PhonetokTokenizer._expand_beam(beam, branches, width)

        paths = [
            IPAPath(segments=tuple(segs), score=sc)
            for segs, sc in beam
        ]
        paths.sort(key=lambda p: (p.score, p.ipa))
        return paths

    def _positions_for_token(
        self,
        grapheme: str,
        tok_idx: int,
        n: int,
        prev_tok: Optional[Token],
        next_tok: Optional[Token],
        syll_idx: int,
        stressed_syll_idx: Optional[int],
    ) -> List[GraphemePosition]:
        """Return ordered list of positions to try (most specific first)."""
        pos: List[GraphemePosition] = []
        is_vowel = grapheme[0].lower() in self._VOWEL_CHARS

        # 1. before_X (most specific)
        if next_tok is not None:
            nc = next_tok.grapheme[0].lower()
            if nc == 'a':
                pos.append(GraphemePosition.BEFORE_A)
            elif nc == 'e':
                pos.append(GraphemePosition.BEFORE_E)
            elif nc == 'i':
                pos.append(GraphemePosition.BEFORE_I)
            elif nc == 'o':
                pos.append(GraphemePosition.BEFORE_O)
            elif nc == 'u':
                pos.append(GraphemePosition.BEFORE_U)

        # 2. word boundary
        if tok_idx == 0:
            pos.append(GraphemePosition.WORD_INITIAL)
        if tok_idx == n - 1:
            pos.append(GraphemePosition.WORD_FINAL)

        # 3. intervocalic (consonants between two vowels)
        prev_is_v = (prev_tok is not None
                     and prev_tok.grapheme[0].lower() in self._VOWEL_CHARS)
        next_is_v = (next_tok is not None
                     and next_tok.grapheme[0].lower() in self._VOWEL_CHARS)
        if prev_is_v and next_is_v:
            pos.append(GraphemePosition.INTERVOCALIC)

        # 4. nucleus_stressed / nucleus_unstressed for vowels
        if is_vowel and stressed_syll_idx is not None:
            if syll_idx == stressed_syll_idx:
                pos.append(GraphemePosition.NUCLEUS_STRESSED)
            else:
                pos.append(GraphemePosition.NUCLEUS_UNSTRESSED)
                if syll_idx < stressed_syll_idx:
                    pos.append(GraphemePosition.PRETONIC)
                else:
                    pos.append(GraphemePosition.POSTTONIC)

        # 5. after/before vowel / consonant context
        if prev_is_v:
            pc = prev_tok.grapheme[0].lower()
            if pc == 'a':
                pos.append(GraphemePosition.AFTER_A)
            elif pc == 'e':
                pos.append(GraphemePosition.AFTER_E)
            elif pc == 'i':
                pos.append(GraphemePosition.AFTER_I)
            elif pc == 'o':
                pos.append(GraphemePosition.AFTER_O)
            elif pc == 'u':
                pos.append(GraphemePosition.AFTER_U)
            pos.append(GraphemePosition.AFTER_VOWEL)
        elif prev_tok is not None:
            pos.append(GraphemePosition.AFTER_CONSONANT)
        if next_is_v:
            pos.append(GraphemePosition.BEFORE_VOWEL)
        elif next_tok is not None:
            pos.append(GraphemePosition.BEFORE_CONSONANT)

        # 6. nucleus fallback for vowels
        if is_vowel:
            pos.append(GraphemePosition.NUCLEUS)

        pos.append(GraphemePosition.DEFAULT)
        return pos

    def _positional_branches(
        self,
        grapheme: str,
        token: Token,
        positions: List[GraphemePosition],
        allophone_map: Optional[dict],
    ) -> List[Tuple[str, float]]:
        """Return (ipa, cost) branches, positional winner ranked first."""
        spec = self.spec
        pg = spec.positional_graphemes.get(grapheme)

        positional_candidates: Optional[List[str]] = None
        if pg:
            for pos in positions:
                if pos in pg:
                    positional_candidates = pg[pos]
                    break

        # Base candidates from flat graphemes table (already in token.ipa)
        base_candidates = list(token.ipa)

        if positional_candidates is None:
            # No positional override: fall back to flat table
            candidates = base_candidates
        else:
            # Merge: positional first, then base alternatives not already included
            seen = set(positional_candidates)
            extra = [c for c in base_candidates if c not in seen]
            candidates = list(positional_candidates) + extra

        # Build (ipa, cost) list
        branches: List[Tuple[str, float]] = []
        for rank, phoneme in enumerate(candidates):
            base_cost = float(rank)
            if allophone_map and phoneme in allophone_map:
                allophones = allophone_map[phoneme]
                for a_rank, allophone in enumerate(allophones):
                    branches.append((allophone, base_cost + 0.5 * a_rank))
            else:
                branches.append((phoneme, base_cost))

        # Deduplicate (keep lowest cost)
        seen_ipa: dict = {}
        for ipa, cost in branches:
            if ipa not in seen_ipa or cost < seen_ipa[ipa]:
                seen_ipa[ipa] = cost
        return sorted(seen_ipa.items(), key=lambda x: (x[1], x[0]))

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
