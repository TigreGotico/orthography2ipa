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
import warnings

import langcodes
import pytest

from orthography2ipa import G2P, UnknownVariantWarning, get, resolve, resolves_exactly
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


# Each code is the spec whose ``iso639_3`` is the tag's language: for afb,
# ayl and ayp the one with no region or private use, which is also what
# the bare code names.
@pytest.mark.parametrize("tag,code", [
    ("aao-Arab", "aao"), ("abh-Arab", "abh"), ("abv-Arab", "abv-BH"),
    ("acm-Arab", "acm-IQ"), ("acq-Arab", "acq"), ("acw-Arab", "acw-SA"),
    ("acx-Arab", "acx-OM"), ("adf-Arab", "adf-OM"), ("aec-Arab", "aec-EG"),
    ("afb-Arab", "afb"), ("auz-Arab", "auz"), ("ayh-Arab", "ayh"),
    ("ayl-Arab", "ayl"), ("ayn-Arab", "ayn-YE"), ("ayp-Arab", "ayp"),
    ("mey-Arab", "mey-MR"), ("ssh-Arab", "ssh"),
])
def test_an_arabic_variety_in_arabic_script_names_its_own_spec(tag, code):
    # CLDR gives these varieties the likely script Arab, so the script
    # subtag adds nothing and the own-language spec is near enough.
    language = _language(tag)
    assert get(code).iso639_3 == language
    assert resolve(tag) == code == resolve(language)


@pytest.mark.parametrize("tag", [
    "bs-Cyrl-RS", "bs-Cyrl-ME", "bs-Cyrl-HR", "bs-Cyrl-XK", "bs-Cyrl-x-a",
])
def test_a_bosnian_cyrillic_tag_of_any_region_gives_bs(tag):
    # The bs spec reads both Bosnian alphabets, and CLDR 49 puts no rule from
    # bs to sr, so the tag stays Bosnian whatever its region.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        assert resolve(tag) == "bs"
    assert not resolves_exactly(tag)
    with pytest.raises(KeyError):
        get(tag, strict=True)


@pytest.mark.parametrize("tag", ["hr-Cyrl", "hr-Cyrl-HR"])
def test_a_croatian_cyrillic_tag_stays_unresolved(tag):
    # CLDR 49 languageMatching (UTS #35 section 4.4) has the rules hr => bs 4,
    # sh => bs 4, sh => hr 4 and sh => sr 4, and none from hr to sr, so
    # ``* => * 80`` keeps Croatian a language apart from Serbian. The hr spec
    # is Latin, which is 50 away from Cyrillic.
    assert resolve(tag) == tag
    assert not resolves_exactly(tag)
    with pytest.raises(KeyError):
        get(tag)


@pytest.mark.parametrize("tag", ["afa-Cyrl", "fat-Arab", "fat-Cyrl"])
def test_a_script_other_than_latin_is_not_dropped_to_fit_a_spec(tag):
    assert not resolves_exactly(tag)
    with pytest.raises(KeyError):
        get(tag)


def test_an_unresolved_tag_stays_unresolved():
    assert resolve("zh-HK") == "zh-HK"
    with pytest.raises(KeyError):
        get("zh-HK")


@pytest.mark.parametrize("tag", ["cdo-Hans", "cdo-Hans-CN"])
def test_min_dong_in_han_script_is_not_mandarin(tag):
    # Min Dong (cdo) is a member of the zh macrolanguage, but it is not
    # Mandarin, and the zh spec reads Mandarin pinyin. CLDR gives Hans as the
    # likely script of cdo, and the cdo spec declares Han script. It is a
    # stub with no graphemes, where the zh spec reads pinyin.
    assert resolve(tag) == "cdo"
    assert not get(tag).graphemes


def test_only_the_tag_with_no_region_names_the_cdo_spec_exactly():
    assert resolves_exactly("cdo-Hans")
    assert not resolves_exactly("cdo-Hans-CN")


# langcodes 3.5.1 still folds these individual languages into a
# macrolanguage, from CLDR aliases that CLDR 49 no longer has:
#   <languageAlias type="fat" replacement="ak" reason="macrolanguage"/>
#   <languageAlias type="mnk" replacement="man" reason="macrolanguage"/>
# Each tag names a language that has a spec of its own.
@pytest.mark.parametrize("tag,code", [
    ("fat-GH", "fat"), ("fat-Latn-GH", "fat"), ("FAT-gh", "fat"),
    ("mnk-GM", "mnk"), ("mnk-SN", "mnk"), ("mnk-Latn-GM", "mnk"),
])
def test_a_folded_tag_is_measured_as_requested(tag, code):
    assert langcodes.standardize_tag(tag, macro=True).split("-")[0] != code
    assert resolve(tag) == code


@pytest.mark.parametrize("tag", [
    "cnr-Cyrl", "cnr-Cyrl-BA", "cnr-Cyrl-HR", "cnr-Cyrl-ME", "cnr-Cyrl-RS",
    "cnr-Cyrl-XK",
])
def test_montenegrin_cyrillic_names_its_own_spec(tag):
    # An alias names the spec, so a strict lookup answers as well.
    assert resolve(tag) == "cnr"
    assert resolves_exactly(tag)
    assert get(tag, strict=True).code == "cnr"
    latin = G2P("cnr").transcribe("ljubav voda")
    assert latin
    assert G2P(tag).transcribe("љубав вода") == latin


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
