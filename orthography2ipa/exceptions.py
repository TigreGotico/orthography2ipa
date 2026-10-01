"""Custom exception types for orthography2ipa.

Kept in a dedicated module so downstream consumers can catch them without
importing internal engine modules.
"""
from __future__ import annotations

from typing import Tuple

__all__ = ["StubSpecWarning", "UnmappedScriptError",
           "UnknownLanguageVariantError"]


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


class UnknownLanguageVariantError(KeyError):
    """Raised when a requested code names a variant the registry does not
    carry, and the caller did not pass ``fallback=True``.

    A ``KeyError`` subclass, because that is what :func:`registry.get` has
    always raised for a language it does not have: a caller already catching
    ``KeyError`` keeps working.

    The registry can usually find something close. Before
    ``ar-BH-x-baharna`` had a spec, asking for it returned the Bahraini Sunni
    table — 261 graphemes of confident Arabic — and nothing in the result said
    so. A private-use ``-x-`` subtag claims a named lect exists, so answering
    it with a sibling answers a different question. A region tag the registry
    does not carry is different: that is ordinary BCP-47 matching within one
    language, it is not refused, and it never raises this.

    Parameters
    ----------
    requested : str
        The code the caller asked for.
    substitute : str
        The registered code that would have answered it under
        ``fallback=True``.
    reason : str
        Which guess was refused: ``"unknown-variant"`` for an unregistered
        private-use subtag, ``"cross-language"`` when the nearest match
        changes the primary language.
    """

    def __init__(self, requested: str, substitute: str,
                 reason: str = "unknown-variant") -> None:
        self.requested = requested
        self.substitute = substitute
        self.reason = reason
        if reason == "cross-language":
            what = (f"the nearest registered spec is {substitute!r}, which is "
                    f"a different language")
        else:
            what = (f"this registry has no spec for that variant; the nearest "
                    f"is {substitute!r}")
        # KeyError renders its argument with repr(), so the whole sentence is
        # one string and reads as a sentence rather than as a quoted fragment.
        super().__init__(
            f"{requested!r}: {what}. Readings from {substitute!r} are that "
            f"spec's, not {requested!r}'s. Pass fallback=True to accept the "
            f"substitution, or name a registered code."
        )
