"""g2p — Top-level grapheme→IPA engine.

One obvious call to transcribe text in any covered language::

    >>> import orthography2ipa
    >>> orthography2ipa.transcribe("olá mundo", "pt")
    'ɔˈla ˈmũdu'

The :class:`G2P` engine composes the package's pieces into a pipeline:

1. **normalize** — plugin :meth:`~orthography2ipa.g2p_plugin.G2PPlugin.normalize`
   hook or a caller-supplied callable (diacritization, number expansion).
2. **word split** — :class:`~orthography2ipa.phonetok.PhonetokTokenizer`
   token stream grouped at whitespace/punctuation; punctuation marks
   pausal positions.
3. **per-word search** — greedy (``beam_width=1``) or beam expansion of
   IPA candidates. Beaming per word avoids the combinatorial blow-up of
   whole-sentence beams.
4. **stress** — when the spec declares
   :class:`~orthography2ipa.types.StressRules`, the stressed syllable is
   detected (per-language syllabifier plugins are honoured) and marked.
5. **context pass** — every word's
   :class:`~orthography2ipa.g2p_plugin.WordContext` is rebuilt with its
   neighbours' IPA and handed to the plugin's ``post_process`` hook.
6. **sandhi** — the spec's cross-word rules via
   :class:`~orthography2ipa.sandhi.SandhiEngine`.
7. **dialect transform** — :func:`~orthography2ipa.transforms.apply_transform`
   profile, applied last.

Dispatch: a registered :class:`~orthography2ipa.g2p_plugin.G2PPlugin`
claiming the resolved language code is preferred (highest priority wins);
the data-driven pipeline is the fallback for every language with a spec.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, List, Optional, Tuple

from orthography2ipa.g2p_plugin import G2PPlugin, WordContext
from orthography2ipa.phonetok import IPAPath, PhonetokTokenizer, TokenKind
from orthography2ipa.registry import get, get_plugin, resolve
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
    """Beam alternatives, best first. Empty for greedy search and for
    plugin-produced words."""

    source: str = "engine"
    """Where the transcription came from: ``"engine"`` (data-driven
    pipeline) or ``"plugin:<ClassName>"``."""


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
    use_plugins : bool
        Dispatch to a registered G2P plugin when one claims the
        resolved code (default). ``False`` forces the data-driven
        pipeline.
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
        Text-preparation override. When omitted, the plugin's
        ``normalize`` hook is used (identity without a plugin).
    """

    def __init__(
        self,
        lang: str,
        *,
        use_plugins: bool = True,
        expand_allophones: bool = False,
        dialect_profile: Optional[str] = None,
        apply_sandhi: bool = True,
        apply_stress: bool = True,
        normalizer: Optional[Callable[[str], str]] = None,
    ) -> None:
        self.lang: str = resolve(lang)
        self.spec: LanguageSpec = get(self.lang)
        self.plugin: Optional[G2PPlugin] = (
            get_plugin(self.lang) if use_plugins else None
        )
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
        normalized = self._normalize(text)
        words = self._split_words(normalized)
        if not words:
            return TranscriptionResult(ipa="", words=(), lang=self.lang)

        if self.plugin is not None and self.plugin.sentence_level:
            return self._transcribe_sentence_level(normalized, words)

        transcribed: List[WordTranscription] = [
            self._transcribe_word(w.surface, width) for w in words
        ]

        # context pass: neighbours' IPA is known now
        if self.plugin is not None:
            transcribed = [
                WordTranscription(
                    word=wt.word,
                    ipa=self.plugin.post_process(
                        wt.ipa, self._context(words, transcribed, i)),
                    candidates=wt.candidates,
                    source=wt.source,
                )
                for i, wt in enumerate(transcribed)
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
            WordTranscription(word=wt.word, ipa=iw,
                              candidates=wt.candidates, source=wt.source)
            for wt, iw in zip(transcribed, ipa_words)
        )
        return TranscriptionResult(ipa=ipa, words=final_words,
                                   lang=self.lang)

    def _transcribe_sentence_level(
        self,
        normalized: str,
        words: List["_Word"],
    ) -> TranscriptionResult:
        """Hand the whole text to a sentence-level plugin.

        The plugin owns context effects and sandhi; the engine only
        applies the dialect transform and aligns word IPA best-effort
        (one IPA token per word when counts match).
        """
        ipa = self.plugin.transcribe(normalized)
        if self.dialect_profile:
            from orthography2ipa.transforms import apply_transform
            ipa = apply_transform(ipa, self.dialect_profile,
                                  ortho=normalized)
        source = f"plugin:{type(self.plugin).__name__}"
        parts = ipa.split()
        aligned = len(parts) == len(words)
        word_results = tuple(
            WordTranscription(
                word=w.surface,
                ipa=parts[i] if aligned else "",
                source=source,
            )
            for i, w in enumerate(words)
        )
        return TranscriptionResult(ipa=ipa, words=word_results,
                                   lang=self.lang)

    def transcribe_word(
        self,
        word: str,
        context: Optional[WordContext] = None,
        *,
        search: str = "greedy",
        beam_width: int = 8,
    ) -> str:
        """Transcribe a single *word*, optionally with sentence context."""
        if self.plugin is not None:
            return self.plugin.transcribe_word(word, context)
        wt = self._transcribe_word(
            word, self._width(search, beam_width))
        return wt.ipa

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

    def _normalize(self, text: str) -> str:
        if self.normalizer is not None:
            return self.normalizer(text)
        if self.plugin is not None:
            return self.plugin.normalize(text)
        return text

    def _split_words(self, text: str) -> List[_Word]:
        """Group the token stream into words with pausal/position flags."""
        tokens = self._tokenizer.tokenize(text)
        words: List[_Word] = []
        current: List[str] = []
        pausal = False

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
        if self.plugin is not None:
            return WordTranscription(
                word=word,
                ipa=self.plugin.transcribe_word(word),
                source=f"plugin:{type(self.plugin).__name__}",
            )
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
            source="engine",
        )

    def _context(
        self,
        words: List[_Word],
        transcribed: List[WordTranscription],
        index: int,
    ) -> WordContext:
        w = words[index]
        return WordContext(
            prev_word_ipa=transcribed[index - 1].ipa if index > 0 else None,
            next_word_ipa=(transcribed[index + 1].ipa
                           if index + 1 < len(transcribed) else None),
            is_pausal=w.pausal,
            is_sentence_initial=w.sentence_initial,
            prev_word=words[index - 1].surface if index > 0 else None,
            next_word=(words[index + 1].surface
                       if index + 1 < len(words) else None),
            is_sentence_final=w.sentence_final,
            word_index=index,
            word_count=len(words),
            lang=self.lang,
        )


def transcribe(
    text: str,
    lang: str,
    *,
    search: str = "greedy",
    beam_width: int = 8,
    dialect_profile: Optional[str] = None,
    use_plugins: bool = True,
) -> str:
    """One-call convenience: transcribe *text* in *lang* to IPA.

    Equivalent to ``G2P(lang, ...).transcribe(text, ...)``; build a
    :class:`G2P` instance directly for repeated calls or the full
    option set.
    """
    engine = G2P(lang, dialect_profile=dialect_profile,
                 use_plugins=use_plugins)
    return engine.transcribe(text, search=search, beam_width=beam_width)
