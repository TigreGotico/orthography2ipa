"""syllabifier_plugin — Abstract interface for per-language syllabifiers.

The bundled :func:`orthography2ipa.stress.syllabify` is a naive
vowel-group splitter. Languages with a real syllabifier ship it as a
plugin — ``silabificador`` for Portuguese, ``pycotovia`` for Galician —
and stress detection (and the G2P engine) picks it up automatically.

Plugins are discovered via ``importlib.metadata`` entry points in the
``orthography2ipa.syllabify`` group; when several claim the same
language code the highest :attr:`SyllabifierPlugin.priority` wins.

Usage
─────
    # In a plugin's pyproject.toml:
    [project.entry-points."orthography2ipa.syllabify"]
    portuguese = "silabificador.plugin:PortugueseSyllabifier"
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
        """Dispatch precedence among plugins claiming the same code.

        Higher wins; ``50`` is the neutral default.
        """
        return 50
