"""Arabic dialect specs are keyed by their ISO 639-3 individual code.

SCHEMA.md, "Minting a private-use lect code": a variety with an ISO 639-3
individual code of its own is keyed by that code, not by a private-use tag.
Each code below is the SIL ISO 639-3 code table entry for the variety the
spec describes. Every key the spec had before keeps resolving to it, and so
does the bare ISO code.
"""
import re

import pytest

from orthography2ipa import get, resolve, resolves_exactly
from orthography2ipa.registry import UnknownVariantWarning
from orthography2ipa.json_loader import available_json_codes

#: canonical key -> the keys it had before.
CANONICAL = {
    "arz-EG": ["ar-EG"],
    "arz-EG-x-fayyum": ["ar-EG-x-fayyum"],
    "aec-EG": ["ar-EG-x-saidi"],
    "avl-EG": ["ar-EG-x-bedawi"],
    "ary-MA": ["ar-MA"],
    "arq-DZ": ["ar-DZ"],
    "aeb-TN": ["ar-TN"],
    "mey-MR": ["ar-MR"],
    "apd-SD": ["ar-SD"],
    "shu-TD": ["ar-TD"],
    "shu-NG": ["ar-NG"],
    "acx-OM": ["ar-OM"],
    "adf-OM": ["ar-OM-x-dhofari"],
    "ayn-YE": ["ar-YE"],
    "ayn-YE-x-highland": ["ar-YE-x-highland"],
    "ayn-YE-x-manakha": ["ar-YE-x-manakha"],
    "acm-IQ": ["ar-IQ"],
    "apc": ["ar-x-levantine"],
    "apc-SY": ["ar-SY"],
    "apc-LB": ["ar-LB"],
    "apc-JO": ["ar-JO"],
    "apc-PS": ["ar-PS"],
    "apc-TR-x-cukurova": ["ar-TR-x-cukurova"],
    "afb": ["ar-x-gulf"],
    "afb-KW": ["ar-KW"],
    "afb-QA": ["ar-QA"],
    "afb-AE": ["ar-AE"],
    "afb-BH": ["ar-BH"],
    "afb-SA-x-sharqiya": ["ar-SA-x-sharqiyya"],
    "afb-SA-x-dawasir": ["ar-SA-x-dawasir"],
    "abv-BH": ["ar-BH-x-baharna"],
    "ars-SA": ["ar-SA-x-najd", "ar-x-najdi", "ar-SA"],
    "ars-SA-x-qassim": ["ar-SA-x-qassim"],
    "ars-SA-x-shamali": ["ar-SA-x-shamali"],
    "acw-SA": ["ar-SA-x-hejaz", "ar-x-hejazi", "ar-x-hijazi"],
}

#: bare ISO 639-3 code -> canonical key. ``ajp`` is retired into ``apc``.
BARE = {
    "arz": "arz-EG", "aec": "aec-EG", "avl": "avl-EG", "ary": "ary-MA",
    "arq": "arq-DZ", "aeb": "aeb-TN", "mey": "mey-MR", "apd": "apd-SD",
    "shu": "shu-TD", "acx": "acx-OM", "adf": "adf-OM", "ayn": "ayn-YE",
    "acm": "acm-IQ", "apc": "apc", "afb": "afb", "abv": "abv-BH",
    "ars": "ars-SA", "acw": "acw-SA", "ajp": "apc-JO",
}

#: specs whose ``iso639_3`` names their variety, read off the SIL table.
DECLARED = {
    "afb-AE": "afb", "afb-BH": "afb", "apc-JO": "apc", "apc-PS": "apc",
    "ar-IQ-x-qeltu": "ayp",
    "ar-SA-x-rijal-alma": None, "ar-SA-x-tihama-qahtan": None,
}

_PRIVATE_SUBTAG = re.compile(r"-x-(.+)$")


@pytest.mark.parametrize("key", sorted(CANONICAL))
def test_canonical_key_is_a_spec_and_resolves_to_itself(key):
    assert key in available_json_codes()
    assert resolve(key) == key
    assert resolves_exactly(key)
    spec = get(key)
    assert spec.code == key
    # A declared code names the key's own language subtag.
    assert spec.iso639_3 in (None, key.split("-")[0])
    # BCP 47 limits a private-use subtag to 1 to 8 characters.
    match = _PRIVATE_SUBTAG.search(key)
    if match:
        assert all(1 <= len(part) <= 8 for part in match.group(1).split("-"))


@pytest.mark.parametrize("old,new", sorted(
    (old, new) for new, olds in CANONICAL.items() for old in olds))
def test_old_key_resolves_exactly_to_canonical(old, new):
    assert old not in available_json_codes()
    assert resolve(old) == new
    assert resolves_exactly(old)
    assert get(old).code == new


@pytest.mark.parametrize("code,new", sorted(BARE.items()))
def test_bare_iso_code_resolves_to_canonical(code, new):
    assert resolve(code) == new
    assert resolves_exactly(code)


@pytest.mark.parametrize("key,code", sorted(DECLARED.items()))
def test_declaration_names_the_variety(key, code):
    assert get(key).iso639_3 == code


def test_official_tags_do_not_reach_standard_arabic():
    assert {resolve(key) for key in CANONICAL} == set(CANONICAL)
    assert "ar" not in {resolve(key) for key in CANONICAL}


@pytest.mark.parametrize("old,new", sorted(
    (old, new) for new, olds in CANONICAL.items() for old in olds
    if re.fullmatch(r"ar-[A-Z]{2}", old) and old not in ("ar-EG", "ar-SA")))
def test_unknown_subtag_under_old_key_stays_on_its_spec(old, new):
    # The nearest match for an unregistered variant of an old key is the spec
    # the old key names, not a sibling that happens to keep an ``ar-`` key.
    # ``ar-EG`` is left out: EG is the likely region of ``ar``, so its variant
    # ties with ``ar`` and goes there. ``ar-SA`` is a region default, not a key.
    with pytest.warns(UnknownVariantWarning):
        assert resolve(f"{old}-x-zzz") == new
