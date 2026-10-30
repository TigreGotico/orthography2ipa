"""Every ISO 639-3 member of the Arabic macrolanguage has an entry.

A variety with no entry is invisible twice over: the code resolves to nothing, and
nothing in the registry records that the language was ever considered. That is worse
than a stub, which at least says what it does not know.

This was found by enumerating the macrolanguage rather than by reading the file list:
of the 31 codes below, `bbz` (Babalia Creole) and `sqr` (Siculo) had no spec declaring
them and the other 29 did. No existing test could see it, because every one of them
starts from the specs that exist.
"""
import glob
import json
import os

import pytest

import orthography2ipa
from orthography2ipa.registry import get

DATA = os.path.join(os.path.dirname(orthography2ipa.__file__), "data")

# The individual languages ISO 639-3 lists under the Arabic macrolanguage [ara],
# read from the SIL registry at iso639-3.sil.org (2026-09-18 release) and typed here
# rather than fetched: a test that reaches the network fails for reasons that are not
# about this repo. The point of the check is that it enumerates from OUTSIDE the spec
# directory, so the source of the list is what makes it auditable — if this literal is
# not current, the check silently stops covering whatever ISO added.
#
# 31 codes: 29 members of [ara] proper, plus arb Standard Arabic and sqr Siculo, which
# carry their own codes. The Judeo-Arabic varieties (jrb and its members ajt, aju, jye,
# yhd, yud) sit under their own macrolanguage and are covered by the inheritance test
# instead.
ARA_MEMBERS = [
    "aao", "abh", "abv", "acm", "acq", "acw", "acx", "acy", "adf", "aeb", "aec",
    "afb", "ajp", "apc", "apd", "arb", "arq", "ars", "ary", "arz", "auz", "avl",
    "ayh", "ayl", "ayn", "ayp", "bbz", "pga", "shu", "sqr", "ssh",
]


def _declared():
    out = {}
    for path in glob.glob(os.path.join(DATA, "*.json")):
        with open(path, encoding="utf-8") as fh:
            iso = json.load(fh).get("iso639_3")
        if iso:
            out.setdefault(iso, []).append(os.path.basename(path)[: -len(".json")])
    return out


def test_every_arabic_macrolanguage_member_has_an_entry():
    declared = _declared()
    assert len(declared) > 900, f"only {len(declared)} codes read -- the scan found nothing"
    missing = [c for c in ARA_MEMBERS if c not in declared]
    assert not missing, (
        "these ISO 639-3 Arabic languages have no spec declaring their code:\n  "
        + "\n  ".join(missing)
        + "\nA language with no entry is invisible: the code resolves to nothing and "
          "nothing records that it was considered. A stub with an honest note is the "
          "minimum.")


@pytest.mark.parametrize("code", ["bbz", "sqr"])
def test_the_two_added_here_reach_a_table_and_claim_nothing(code):
    spec = get(code)
    assert spec.code == code
    assert len(spec.graphemes) > 100, "resolves to a spec with no phonology"
    with open(os.path.join(DATA, code + ".json"), encoding="utf-8") as fh:
        raw = json.load(fh)
    assert raw["quality"] == "stub"
    assert not raw["graphemes"], "no reflex may be declared without a citation"
    assert spec.graphemes == get(raw["graphemes_base"]).graphemes
    assert "NOT DESCRIBED HERE" in raw["notes"]


def test_each_states_why_its_parent_is_weak():
    """Both parents are chosen on grounds weaker than description, and the notes say
    so rather than letting a reader infer agreement from the inheritance."""
    with open(os.path.join(DATA, "bbz.json"), encoding="utf-8") as fh:
        _bbz = json.load(fh)
    assert "CREOLE" in _bbz["notes"]
    assert _bbz["parent"] != _bbz["graphemes_base"], (
        "bbz's note disclaims the descent its parent would assert; the classification "
        "must stay off the graphemes base")
    with open(os.path.join(DATA, "sqr.json"), encoding="utf-8") as fh:
        assert "A GROUPING, NOT A DESCRIPTION" in json.load(fh)["notes"]
