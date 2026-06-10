"""g2p_plugin — Abstract interface for language-specific G2P plugins.

Plugins provide sophisticated G2P logic that goes beyond the declarative
grapheme table approach.  They can handle complex morphophonology,
contextual rules, and external model inference (e.g., Arabic tashkeel).

Plugins are discovered via ``importlib.metadata`` entry points in the
``orthography2ipa.g2p`` group.

Usage
─────
    # In a plugin's pyproject.toml:
    [project.entry-points."orthography2ipa.g2p"]
    arabic = "orthography2ipa.plugins.arabic_g2p:ArabicG2PPlugin"

Lifecycle hooks
───────────────
Beyond the abstract transcription methods, a plugin can override three
defaulted hooks:

- :meth:`G2PPlugin.normalize` — pre-G2P text preparation (Unicode
  normalisation, diacritization such as Arabic tashkeel, number/date
  expansion). The engine calls it once on the full input text.
- :meth:`G2PPlugin.post_process` — post-G2P IPA adjustment with word
  context (pausal forms, cross-word assimilation, liaison).
- :attr:`G2PPlugin.priority` — dispatch tie-break when several plugins
  claim the same language code; the highest priority wins. Bundled
  plugins use the default ``50``; external distributions that improve
  on a bundled implementation should declare a higher value.
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

    @property
    def priority(self) -> int:
        """Dispatch precedence among plugins claiming the same code.

        Higher wins. ``50`` is the neutral default; external plugins
        that supersede a bundled one should return a higher value.
        """
        return 50

    @property
    def sentence_level(self) -> bool:
        """Whether the plugin owns the whole-sentence pipeline.

        ``True`` makes the engine hand the full normalized text to
        :meth:`transcribe` instead of driving :meth:`transcribe_word`
        per word — required when transcription quality depends on
        sentence-wide state the per-word path cannot carry (POS
        tagging, clitic joining). The plugin then owns context
        effects and sandhi itself.
        """
        return False
