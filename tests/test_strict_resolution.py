"""Nearest-language guessing is refused by default, and a caller can opt in.

This file used to assert the opposite — "the guess is the default and stays it,
because callers depend on it". That was reversed by decision
``o2i-resolver-fallback`` on 2026-09-25, after the Baharna case: before
``ar-BH-x-baharna`` had a spec, ``get`` answered it with the Bahraini Sunni
table, 261 graphemes of confident Arabic, and nothing in the result said a
substitution had happened. A reviewer read a complete baseline column from the
wrong spec.

So the default is now the refusal and ``fallback=True`` is the opt-in. The
``strict=True`` parameter asked for what is now the default; it stays accepted,
so a caller written against it keeps working.

The boundary is narrower than "refuse everything the registry had to search
for": see ``test_unknown_variant_is_refused.py`` for the region fallback that is
deliberately kept, and for the declared ISO 639-3 code that crosses the primary
subtag by the spec's own declaration.
"""
import pytest

from orthography2ipa import get, resolve, resolves_exactly
from orthography2ipa.exceptions import UnknownLanguageVariantError


def test_a_registered_code_resolves_exactly():
    assert resolves_exactly("ar-EG")
    assert resolves_exactly("en-GB")


def test_an_alias_is_not_a_guess():
    """Aliases, case folding and the curated defaults name a spec deliberately;
    only the guess is refused."""
    assert resolves_exactly("arz")          # alias to ar-EG
    assert resolves_exactly("AR-eg")        # case folding
    assert get("arz", strict=True).code == get("ar-EG").code


def test_an_unregistered_code_does_not_resolve_exactly():
    assert not resolves_exactly("ar-XX-x-invented")


def test_the_default_refuses_an_invented_lect():
    """The reversal. What used to answer with a plausible neighbour now says so."""
    with pytest.raises(UnknownLanguageVariantError):
        get("ar-XX-x-invented")
    with pytest.raises(UnknownLanguageVariantError):
        resolve("ar-XX-x-invented")


def test_strict_still_means_what_it_meant():
    """It asked for the refusal, and the refusal is now the default, so a caller
    that passes it sees no change."""
    with pytest.raises(KeyError):
        get("ar-XX-x-invented", strict=True)


def test_the_guess_is_still_available_when_asked_for():
    """The substitution was not removed, only made deliberate: a caller who
    wants the nearest spec can still have it."""
    spec = get("ar-XX-x-invented", fallback=True)
    assert spec.graphemes
    assert resolve("ar-XX-x-invented", fallback=True) != "ar-XX-x-invented"
