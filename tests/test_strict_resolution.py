"""A caller can refuse nearest-language guessing.

The guess is the default and stays it, because callers depend on it. What was missing
was any way to tell "this code names a spec" from "something vaguely like it does" —
the failure that handed a reviewer a complete, plausible baseline column from the wrong
spec, with nothing in the result saying a substitution had occurred.
"""
import pytest

from orthography2ipa import get, resolve, resolves_exactly


def test_a_registered_code_resolves_exactly():
    assert resolves_exactly("ar-EG")
    assert resolves_exactly("en-GB")


def test_an_alias_is_not_a_guess():
    """Aliases, case folding and the curated defaults name a spec deliberately;
    only closest_lang guesses, so only closest_lang is refused."""
    assert resolves_exactly("arz")          # alias to ar-EG
    assert resolves_exactly("AR-eg")        # case folding
    assert get("arz", strict=True).code == get("ar-EG").code


def test_an_unregistered_code_does_not_resolve_exactly():
    assert not resolves_exactly("ar-XX-x-invented")


def test_strict_refuses_where_the_default_guesses():
    """The case this exists for: the default answers with a plausible neighbour."""
    loose = get("ar-XX-x-invented")          # a guess, and it succeeds
    assert loose.code != "ar-XX-x-invented"
    with pytest.raises(KeyError):
        get("ar-XX-x-invented", strict=True)


def test_the_default_is_unchanged():
    """Every existing caller keeps the guess. A strict default would be a different
    library, and the point is to make the guess visible, not to remove it."""
    assert get("ar-XX-x-invented").graphemes
    assert resolve("ar-XX-x-invented") != "ar-XX-x-invented"
