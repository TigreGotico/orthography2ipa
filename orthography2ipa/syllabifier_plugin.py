"""syllabifier_plugin — Abstract interface for per-language syllabifiers.

The bundled :func:`orthography2ipa.stress.syllabify` is a naive
vowel-group splitter. A language with a real syllabifier ships it as a
class that implements this interface — ``silabificador`` for Portuguese,
``pycotovia`` for Galician — and a caller passes an instance to one
engine. Nothing discovers a syllabifier, so installing a package changes
no transcription.

Usage
─────
    from orthography2ipa import G2P, Pipeline
    from orthography2ipa.syllabifiers import SilabificadorSyllabifier

    engine = G2P("pt-PT", pipeline=Pipeline(syllabifier=SilabificadorSyllabifier()))
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional

__all__ = [
    "SyllabifierPlugin",
]


class SyllabifierPlugin(ABC):
    """Abstract base for language-specific syllabifiers."""

    @abstractmethod
    def syllabify(self, word: str, lang: Optional[str] = None) -> List[str]:
        """Split an orthographic *word* into syllables.

        ``lang`` is the resolved BCP-47 code the request was made for,
        letting a multi-variety plugin adjust (e.g. pt-PT vs pt-BR).
        Joining the returned syllables must reproduce *word*.
        """

    @property
    @abstractmethod
    def language_codes(self) -> List[str]:
        """BCP-47 codes this syllabifier handles."""

    @property
    def priority(self) -> int:
        """Nothing reads this value: a caller names one syllabifier."""
        return 50
