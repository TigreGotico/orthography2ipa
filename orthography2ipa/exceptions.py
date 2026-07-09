"""Custom exception types for orthography2ipa.

Kept in a dedicated module so downstream consumers can catch them without
importing internal engine modules.
"""
from __future__ import annotations

from typing import Tuple

__all__ = ["UnmappedScriptError"]


class UnmappedScriptError(ValueError):
    """Raised when a word contains characters absent from a spec's grapheme
    table, and the :class:`~orthography2ipa.g2p.G2P` engine was configured
    with ``on_unmapped="raise"``.

    Parameters
    ----------
    word : str
        The orthographic word that triggered the error.
    unmapped : Tuple[str, ...]
        The specific characters in *word* with no grapheme mapping.
    lang : str
        The resolved language code the transcription was attempted in.
    """

    def __init__(self, word: str, unmapped: Tuple[str, ...], lang: str) -> None:
        self.word = word
        self.unmapped = unmapped
        self.lang = lang
        super().__init__(
            f"{lang}: word {word!r} has unmapped characters "
            f"{''.join(unmapped)!r} not covered by the grapheme table"
        )
