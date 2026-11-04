"""Every ``iso639_3`` value is an ISO 639-3 code.

SCHEMA.md: "``iso639_3`` follows the same rule and stays ``null`` when ISO 639-3
has no code for the variety, so that a code belonging to a different language
is never claimed twice." The schema pattern ``^[a-z]{3}$`` also accepts an
ISO 639-2/B code, an ISO 639-5 collective code and a retired code, so the
values are checked against the SIL code table itself, vendored in
``tests/data`` so that the test does not reach the network.
"""
import json
import pathlib

import pytest

from orthography2ipa import get

TESTS = pathlib.Path(__file__).parent
DATA_DIR = TESTS.parent / "orthography2ipa" / "data"


def _codes(name):
    lines = (TESTS / "data" / name).read_text(encoding="utf-8").splitlines()
    return frozenset(x for x in lines if x and not x.startswith("#"))


ISO639_3 = _codes("iso639_3_codes.txt")
ISO639_5 = _codes("iso639_5_codes.txt")

# Declarations that hold a retired code. Each one waits on a key rename, which
# moves the spec and its declaration together. This set may only shrink.
KNOWN_INVALID = {
    "ajt": "ajt",
    "bbz": "bbz",
    "yol": "yol",
}


def _declarations():
    out = {}
    for path in sorted(DATA_DIR.glob("*.json")):
        spec = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(spec, dict) and spec.get("iso639_3") is not None:
            out[path.stem] = spec["iso639_3"]
    return out


DECLARED = _declarations()


def test_the_code_tables_are_read():
    assert len(ISO639_3) > 7900
    assert {"por", "bod", "twi", "vsn"} <= ISO639_3
    assert {"ber", "sla", "asw"} <= ISO639_5
    assert not ISO639_3 & ISO639_5
    assert len(DECLARED) > 7000


def test_every_declared_iso639_3_is_an_iso639_3_code():
    bad = {key: code for key, code in DECLARED.items()
           if code not in ISO639_3 and KNOWN_INVALID.get(key) != code}
    assert not bad, bad


def test_no_declared_iso639_3_is_an_iso639_5_code():
    bad = {key: code for key, code in DECLARED.items() if code in ISO639_5}
    assert not bad, bad


def test_known_invalid_declarations_are_still_present():
    stale = {key: code for key, code in KNOWN_INVALID.items()
             if DECLARED.get(key) != code or code in ISO639_3}
    assert not stale, f"remove from KNOWN_INVALID: {stale}"


# The individual code SIL lists for the variety the key and the glottocode
# name, where the spec declared the macrolanguage or the ISO 639-2/B code.
@pytest.mark.parametrize("key, code", [
    ("tw", "twi"),
    ("bxr", "bxr"),
    ("diq", "diq"),
    ("bo", "bod"),
    ("sc-x-campidanese", "sro"),
    ("sc-x-logudorese", "src"),
    ("vsn", "vsn"),
])
def test_declares_the_individual_code(key, code):
    assert get(key).iso639_3 == code
