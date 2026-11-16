"""An unresolvable private-use subtag warns instead of resolving silently."""
import warnings

import pytest

import orthography2ipa as o2i
from orthography2ipa import registry
from orthography2ipa.registry import UnknownVariantWarning


@pytest.mark.parametrize("tag, chosen, discarded", [
    ("gmh-x-typo123", "gmh", "typo123"),
    # The default-region ruling: a bare tag goes to the region where the
    # language first appeared, so pt reads pt-PT.
    ("pt-x-doesnotexist", "pt-PT", "doesnotexist"),
    ("pt-TL-x-dili", "pt-TL", "dili"),
    ("en-gb-x-rp", "en-GB", "rp"),
    ("pt-PT-X-typo", "pt-PT", "typo"),
])
def test_resolve_warns_naming_subtag_and_spec(tag, chosen, discarded):
    with pytest.warns(UnknownVariantWarning) as rec:
        assert registry.resolve(tag) == chosen
    message = str(rec[0].message)
    assert repr(discarded) in message
    assert repr(chosen) in message


def test_get_warns():
    with pytest.warns(UnknownVariantWarning):
        spec = registry.get("pt-TL-x-dili")
    assert spec.code == "pt-TL"


def test_transcribe_warns():
    with pytest.warns(UnknownVariantWarning):
        o2i.transcribe("casa", "pt-x-doesnotexist")


def test_warning_is_a_user_warning_and_exported():
    assert issubclass(UnknownVariantWarning, UserWarning)
    assert o2i.UnknownVariantWarning is UnknownVariantWarning


@pytest.mark.parametrize("tag, chosen", [
    ("pt-BR-x-sp", "pt-BR-x-sp"),
    ("pt-BR-x-sao-paulo", "pt-BR-x-sp"),
    ("ar-sa-x-najd", "ars-SA"),
    ("ars-sa-x-qassim", "ars-SA-x-qassim"),
    ("pt", "pt-PT"),
    ("en-NZ", "en-GB"),
    ("PT-PT-X-PORTO", "pt-PT-x-porto"),
    ("eu-X-bizkaiera", "eu-biscayan"),
])
def test_resolvable_tags_stay_silent(tag, chosen):
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        assert registry.resolve(tag) == chosen
        registry.get(tag)


def test_strict_get_raises_without_warning():
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        with pytest.raises(KeyError):
            registry.get("pt-x-doesnotexist", strict=True)


def test_suite_turns_the_warning_into_an_error():
    with pytest.raises(UnknownVariantWarning):
        registry.resolve("gmh-x-typo123")


@pytest.mark.parametrize("tag", ["-X-", "-x-", "zzzz-x-nothing"])
def test_a_tag_that_resolves_to_no_spec_raises_keyerror_without_warning(tag):
    """No spec stands in, so there is no substitution to warn about."""
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        assert registry.resolve(tag) == tag
        with pytest.raises(KeyError):
            registry.get(tag)
