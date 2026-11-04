"""Specs outside Arabic are keyed by their ISO 639-3 individual code.

SCHEMA.md, "Minting a private-use lect code": a variety with an ISO 639-3
individual code of its own is keyed by that code, not by a private-use tag or
a retired code. Each code below is the SIL ISO 639-3 code table entry for the
variety the spec describes. Every key the spec had before keeps resolving to
it, and so does the bare ISO code, except an old key that is the code of
another language.
"""
import re

import pytest

from orthography2ipa import get, resolve, resolves_exactly
from orthography2ipa.json_loader import available_json_codes
from orthography2ipa.registry import UnknownVariantWarning

#: canonical key -> the keys it had before.
CANONICAL = {
    "haz-AF": ["fa-x-hazaragi"],
    "bar-AT": ["de-x-bavarian"],
    "pnb-PK": ["pa-PK"],
    "vsn": ["sa-x-vedic"],
    "tpn": ["tpw"],
    "ajg-BJ": [],
    "gej-TG": ["gen"],
    "cbk-PH": ["cbk-zam"],
    "cbk-PH-x-cavite": ["cbk-x-cavite"],
}

#: bare ISO 639-3 code -> the spec that declares it.
BARE = {
    "haz": "haz-AF", "bar": "bar-AT", "pnb": "pnb-PK", "vsn": "vsn",
    "tpn": "tpn", "ajg": "ajg-BJ", "gej": "gej-TG", "cbk": "cbk-PH",
    "twi": "tw",
}

#: Old keys that are the ISO 639-3 code of another language. ``aja`` is SIL
#: Aja (South Sudan); the spec it keyed is Aja (Benin), ``ajg``.
NOT_KEPT = ["aja"]

_PRIVATE_SUBTAG = re.compile(r"-x-(.+)$")


@pytest.mark.parametrize("key", sorted(CANONICAL))
def test_canonical_key_is_a_spec_and_resolves_to_itself(key):
    assert key in available_json_codes()
    assert resolve(key) == key
    assert resolves_exactly(key)
    spec = get(key)
    assert spec.code == key
    assert spec.iso639_3 == key.split("-")[0]
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


@pytest.mark.parametrize("code,spec", sorted(BARE.items()))
def test_bare_iso_code_resolves_to_its_declaring_spec(code, spec):
    assert resolve(code) == spec
    assert resolves_exactly(code)
    assert get(code).iso639_3 == code


@pytest.mark.parametrize("old", NOT_KEPT)
def test_another_languages_code_is_not_an_alias(old):
    assert old not in available_json_codes()
    assert not resolves_exactly(old)
    with pytest.raises(KeyError):
        get(old)


@pytest.mark.parametrize("child", ["cbk-PH-x-cavite", "cbk-x-ternate"])
def test_chavacano_children_take_the_canonical_parent(child):
    spec = get(child)
    assert spec.parent == "cbk-PH"
    parent = get("cbk-PH").graphemes
    assert {k: spec.graphemes.get(k) for k in parent} == dict(parent)


def test_pt_br_names_tupinamba_by_its_code():
    assert "tpn" in {a.code for a in get("pt-BR").ancestors}


@pytest.mark.parametrize("old,new", [("pa-PK", "pnb-PK"), ("tpw", "tpn"),
                                     ("gen", "gej-TG"), ("cbk-zam", "cbk-PH")])
def test_unknown_subtag_under_old_key_stays_on_its_spec(old, new):
    with pytest.warns(UnknownVariantWarning):
        assert resolve(f"{old}-x-zzz") == new
