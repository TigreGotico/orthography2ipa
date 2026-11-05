"""The nearest match keeps the language that the tag names.

RFC 5646 §2.2.1: "The primary language subtag is the first subtag in a
language tag and cannot be omitted". §2.1.1: "language tags and their
subtags, including private use and extensions, are to be treated as case
insensitive".

So a tag whose own language has a spec near enough resolves inside that
language, and an upper-case tag names the same spec as its lower-case form.
The expected languages below are the primary subtags of the tags, or for a
language with no spec of its own, the language that langcodes standardizes
the tag to.
"""
import langcodes
import pytest

from orthography2ipa import UnknownVariantWarning, get, resolve, resolves_exactly
from orthography2ipa.registry import available_json_codes


def _language(code: str) -> str:
    return code.split("-")[0].lower()


def _cyrillic_keys(code: str) -> int:
    return sum(any("\u0400" <= ch <= "\u04ff" for ch in key)
               for key in get(code).graphemes)


@pytest.mark.parametrize("tag", [
    "sr-Latn", "sr-Latn-RS", "sr-Latn-BA", "sr-Latn-ME", "sr-Latn-XK", "sr-ME",
    "hr-BA", "hr-Latn-BA", "cnr-RS", "cnr-BA",
    "sq-AL", "sw-CD", "rom-CH", "quz-PE", "bxr-RU", "ks-IN", "src-IT",
    "fat-GH", "jrb-US", "arb-TR", "mhr-RU",
])
def test_a_tag_resolves_inside_its_own_language(tag):
    assert _language(resolve(tag)) == _language(tag)


def test_an_unknown_variant_keeps_its_own_language():
    # arb has a spec of its own, so its unknown variant does not move to ar.
    with pytest.warns(UnknownVariantWarning):
        assert resolve("arb-x-zzz") == "arb"


@pytest.mark.parametrize("tag", ["sh", "hbs", "sh-Latn", "hbs-Latn-RS", "sh-ME"])
def test_a_language_with_no_spec_takes_its_standardized_language(tag):
    # langcodes standardizes sh and hbs to sr-Latn (the CLDR alias), and
    # Serbian has a spec.
    standardized = langcodes.standardize_tag(tag, macro=True)
    assert _language(standardized) == "sr"
    assert resolve(tag) == "sr"


def test_cnr_maximizes_to_serbian_but_is_not_chosen_for_it():
    # The reason for the rule: by distance alone cnr is nearer than sr.
    assert (langcodes.tag_distance("sr-Latn-RS", "cnr")
            < langcodes.tag_distance("sr-Latn-RS", "sr"))
    assert resolve("sr-Latn-RS") == "sr"


@pytest.mark.parametrize("tag,code", [
    ("aao-Arab", "ar"), ("acm-Arab", "ar"), ("cdo-Hans", "zh"),
    ("bs-Cyrl", "sr"), ("hr-Cyrl", "sr"), ("hr-Cyrl-HR", "sr"),
])
def test_with_no_own_spec_near_enough_the_old_target_stays(tag, code):
    # langcodes guesses Latn for aao and cdo, and the bs and hr specs read
    # Latin, so no own-language spec is near enough; the wide search runs.
    assert resolve(tag) == code
    assert not resolves_exactly(tag)


def test_an_unresolved_tag_stays_unresolved():
    assert resolve("zh-HK") == "zh-HK"
    with pytest.raises(KeyError):
        get("zh-HK")


@pytest.mark.parametrize("tag", [
    "cnr-Cyrl", "cnr-Cyrl-BA", "cnr-Cyrl-HR", "cnr-Cyrl-ME", "cnr-Cyrl-RS",
    "cnr-Cyrl-XK",
])
def test_montenegrin_cyrillic_reads_with_serbian(tag):
    # cnr reads the Latin alphabet only; sr reads Cyrillic.
    assert "Cyrillic" not in get("cnr").script
    assert any("Ѐ" <= ch <= "ӿ" for ch in get("sr").graphemes)
    assert resolve(tag) == "sr"
    assert resolves_exactly(tag)


@pytest.mark.parametrize("tag,code", [
    ("MNK", "mnk"), ("PNB-PK", "pnb-PK"), ("ALS", "als"), ("TL", "tl"),
    ("BCL", "bcl"), ("TWI", "tw"), ("EN-gb", "en-GB"),
])
def test_an_upper_case_tag_names_the_same_spec(tag, code):
    assert resolve(tag) == code == resolve(tag.lower())
    assert resolves_exactly(tag)


def test_every_registered_code_resolves_in_any_case():
    codes = available_json_codes()
    assert len(codes) > 5000
    wrong = [c for c in codes
             if resolve(c.upper()) != c or resolve(c.lower()) != c]
    assert not wrong, wrong[:20]
