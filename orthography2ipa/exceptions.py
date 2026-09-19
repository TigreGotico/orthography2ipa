"""Custom exception types for orthography2ipa.

Kept in a dedicated module so downstream consumers can catch them without
importing internal engine modules.
"""
from __future__ import annotations

from typing import Tuple

__all__ = ["StubSpecWarning", "UnmappedScriptError"]


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


class StubSpecWarning(UserWarning):
    """Emitted once when a :class:`~orthography2ipa.g2p.G2P` engine is built
    on a spec that has no grapheme table at all (``quality: stub`` with
    neither ``graphemes`` nor ``positional_graphemes``, and no base to
    inherit them from).

    Every transcription from such an engine is the empty string, and
    :meth:`~orthography2ipa.g2p.G2P.word_confidence` is ``0.0``. Before this
    warning existed that was the only signal, and a caller who did not ask
    for it got ``""`` back with nothing said (``azb``, ``lah``). The engine
    still builds, because 6219 of the 7670 registered codes are such stubs
    and the catalog, the distance metrics and the tests enumerate them;
    ``G2P(..., on_unmapped="raise")`` turns the per-word case into
    :class:`UnmappedScriptError`.
    """
