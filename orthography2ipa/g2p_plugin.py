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
    """Context for a word in a sentence, enabling sandhi/liaison."""

    prev_word_ipa: Optional[str] = None
    next_word_ipa: Optional[str] = None
    is_pausal: bool = False
    is_sentence_initial: bool = False


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
