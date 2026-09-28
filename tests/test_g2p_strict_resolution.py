"""``G2P`` can refuse a guessed spec, and says when it accepted one.

``registry.get(strict=True)`` and ``resolves_exactly`` already let a caller tell
"this code names a spec" from "something vaguely like it does". ``G2P`` did not
carry either: ``G2P(lang, strict=True)`` was a ``TypeError``, and the object
reported only the resolved code, so a caller who asked for a lect the tree does
not have could not find out that it had been substituted.

The default is unchanged. Every existing caller keeps the guess.
"""
import pytest

from orthography2ipa import G2P


def test_strict_refuses_a_guess():
    with pytest.raises(KeyError):
        G2P("ar-XX-x-nonsense", strict=True)


def test_strict_refuses_an_invented_region_variant():
    with pytest.raises(KeyError):
        G2P("pt-BR-x-nothing", strict=True)


def test_a_kept_region_fallback_is_not_a_guess():
    """``ar-SA`` is a curated default and ``pt`` a curated bare default: both
    name a spec deliberately, so strict must accept them."""
    assert G2P("ar-SA", strict=True).lang == "ar-SA-x-najd"
    assert G2P("pt", strict=True).lang == "pt-PT"


def test_an_exact_code_is_accepted_under_strict():
    assert G2P("ar-EG", strict=True).lang == "ar-EG"


def test_the_object_reports_what_was_asked_for():
    g = G2P("ar-XX-x-nonsense")
    assert g.requested == "ar-XX-x-nonsense"
    assert g.lang == "ar"
    assert g.substituted is True


def test_no_substitution_is_reported_when_the_code_named_a_spec():
    g = G2P("ar-EG")
    assert g.requested == "ar-EG"
    assert g.substituted is False


def test_a_curated_default_is_not_reported_as_a_substitution():
    """``pt`` -> ``pt-PT`` changes the code but names a spec deliberately, so it
    is not the silent-guess case this flag exists to expose."""
    g = G2P("pt")
    assert g.lang == "pt-PT"
    assert g.substituted is False


def test_the_default_still_guesses():
    assert G2P("ar-XX-x-nonsense").transcribe("كتاب")
