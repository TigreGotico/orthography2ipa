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

from dataclasses import dataclass
from typing import Callable, List, Optional, Tuple

from orthography2ipa.phonetok import IPAPath, PhonetokTokenizer, TokenKind
from orthography2ipa.registry import get, resolve
from orthography2ipa.sandhi import SandhiEngine
from orthography2ipa.stress import _syllables_for, apply_stress_mark, detect_stress
from orthography2ipa.types import LanguageSpec

__all__ = [
    "G2P",
    "transcribe",
    "WordTranscription",
    "TranscriptionResult",
]

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
    ) -> None:
        self.lang: str = resolve(lang)
        self.spec: LanguageSpec = get(self.lang)
        self.expand_allophones = expand_allophones
        self.dialect_profile = dialect_profile
        self.apply_sandhi = apply_sandhi
        self.apply_stress = apply_stress
        self.normalizer = normalizer
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
            WordTranscription(word=wt.word, ipa=iw, candidates=wt.candidates)
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
        paths = self._tokenizer.ipa_beam(
            word, beam_width=width,
            expand_allophones=self.expand_allophones)
        ipa = paths[0].ipa if paths else word
        if (self.apply_stress and self.spec.stress is not None and ipa):
            sylls = _syllables_for(word, self.lang)
            idx = detect_stress(word, self.spec.stress, syllables=sylls)
            ipa = apply_stress_mark(ipa, self.spec.stress, idx,
                                    syllables=sylls)
        return WordTranscription(
            word=word,
            ipa=ipa,
            candidates=tuple(paths) if width > 1 else (),
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
