"""An unresolvable private-use subtag warns instead of resolving silently."""
import warnings

import pytest

import orthography2ipa as o2i
from orthography2ipa import registry
from orthography2ipa.registry import UnknownVariantWarning


@pytest.mark.parametrize("tag, chosen, discarded", [
    ("gmh-x-typo123", "gmh", "typo123"),
    ("pt-x-doesnotexist", "pt-AO", "doesnotexist"),
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
    ("ar-sa-x-najd", "ar-SA-x-najd"),
    ("pt", "pt-PT"),
    ("en-NZ", "en-GB"),
    ("PT-PT-X-PORTO", "pt-PT-x-porto"),
    ("eu-X-bizkaiera", "eu-x-bizkaiera"),
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
