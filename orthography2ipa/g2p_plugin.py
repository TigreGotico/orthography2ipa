"""g2p_plugin — Base interface for G2P engines built on this library.

:class:`G2PPlugin` and :class:`WordContext` are shared types that
*downstream* engines implement — arbtok (Arabic), tugaphone
(Portuguese). They give every engine in the ecosystem one call shape
and one context vocabulary.

orthography2ipa itself never discovers or dispatches to these
implementations: its own :class:`~orthography2ipa.g2p.G2P` engine is
purely data-driven. Component plugins that slot into that engine's own
logic use dedicated groups instead (``orthography2ipa.syllabify``).

Lifecycle hooks
───────────────
Beyond the abstract transcription methods, an engine can override two
defaulted hooks:

- :meth:`G2PPlugin.normalize` — pre-G2P text preparation (Unicode
  normalisation, diacritization such as Arabic tashkeel, number/date
  expansion), called once on the full input text.
- :meth:`G2PPlugin.post_process` — post-G2P IPA adjustment with word
  context (pausal forms, cross-word assimilation, liaison).
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional

__all__ = [
    "WordContext",
    "G2PPlugin",
]


@dataclass(frozen=True)
class WordContext:
    """Context for a word in a sentence, enabling sandhi/liaison.

    All fields default so existing call sites keep working; engines
    populate as much as they know.
    """

    prev_word_ipa: Optional[str] = None
    """IPA of the preceding word, if already transcribed."""

    next_word_ipa: Optional[str] = None
    """IPA of the following word, if already transcribed."""

    is_pausal: bool = False
    """The word stands before a pause — punctuation or end of input.

    Pausal position conditions e.g. Arabic tanwīn suppression and
    tāʾ marbūṭa realisation."""

    is_sentence_initial: bool = False
    """The word opens the sentence (conditions e.g. hamzat al-waṣl)."""

    prev_word: Optional[str] = None
    """Orthographic form of the preceding word."""

    next_word: Optional[str] = None
    """Orthographic form of the following word."""

    is_sentence_final: bool = False
    """The word closes the sentence."""

    word_index: int = 0
    """Zero-based position of the word in the sentence."""

    word_count: int = 1
    """Total number of words in the sentence."""

    lang: Optional[str] = None
    """Resolved BCP-47 code the transcription was requested for —
    lets a multi-dialect plugin pick the right variety."""


class G2PPlugin(ABC):
    """Abstract base for G2P plugins."""

    @abstractmethod
    def transcribe(self, text: str) -> str:
        """Transcribe a full sentence/phrase to IPA."""

    @abstractmethod
    def transcribe_word(
        self, word: str, context: Optional[WordContext] = None
    ) -> str:
        """Transcribe a single word, optionally with sentence context."""

    @property
    @abstractmethod
    def language_codes(self) -> List[str]:
        """BCP-47 codes this plugin handles."""

    def normalize(self, text: str) -> str:
        """Prepare *text* for transcription. Identity by default.

        Override for pre-G2P steps that need the full input: Unicode
        normalisation and diacritic reordering, auto-diacritization
        (Arabic tashkeel), number/date/abbreviation expansion.
        """
        return text

    def post_process(
        self, ipa: str, context: Optional[WordContext] = None
    ) -> str:
        """Adjust transcribed *ipa* with word context. Identity by default.

        Called per word after every word in the sentence has an IPA
        candidate, so ``context.prev_word_ipa``/``next_word_ipa`` are
        populated — the place for pausal forms and cross-word
        assimilation.
        """
        return ipa
