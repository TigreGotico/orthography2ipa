"""Arabic varieties that are attested with a published description but not yet described here.

A lect with a grammar in print and no entry is invisible to a caller: the code resolves
to nothing, or to a neighbour that is a different variety. These entries give it a code
and a usable table while stating plainly that the table is the parent's and not the
variety's. ``quality`` is ``stub`` for exactly that reason, and these tests hold that
line: the entries must keep claiming a lect exists and must not start claiming to
describe one.
"""
import json
import os

import pytest

import orthography2ipa
from orthography2ipa.registry import get

DATA = os.path.join(os.path.dirname(orthography2ipa.__file__), "data")

ATTESTED = {
    "ar-YE-x-manakha": "ar-YE",
    "ar-YE-x-highland": "ar-YE",
    "ar-TR-x-cukurova": "ar-SY",
    "ar-TR-x-kinderib": "ar-IQ-x-qeltu",
    "ar-EG-x-fayyum": "ar-EG",
    "ar-SA-x-janubi": "ar-x-peninsular",
}


def _raw(code):
    with open(os.path.join(DATA, code + ".json"), encoding="utf-8") as fh:
        return json.load(fh)


@pytest.mark.parametrize("code,parent", sorted(ATTESTED.items()))
def test_the_code_reaches_a_table_it_can_use(code, parent):
    """The point of the entry: resolving must not land on nothing."""
    spec = get(code)
    assert spec.code == code
    assert len(spec.graphemes) > 100, "resolved to a spec with no phonology"


@pytest.mark.parametrize("code,parent", sorted(ATTESTED.items()))
def test_the_table_is_the_parents_and_nothing_is_invented(code, parent):
    """No reflex here was read from a source, so none may be asserted here."""
    raw = _raw(code)
    assert raw["graphemes"] == {}, (
        "a grapheme was declared for a variety whose description has not been read; "
        "either cite it in the notes or take it out")
    assert raw["allophones"] == {}
    assert raw["graphemes_base"] == parent
    assert get(code).graphemes == get(parent).graphemes, (
        "the effective table has diverged from the parent, so it is no longer the "
        "placeholder these notes describe")


@pytest.mark.parametrize("code,parent", sorted(ATTESTED.items()))
def test_it_says_what_it_is(code, parent):
    """A stub that reads like a description is worse than no entry at all."""
    raw = _raw(code)
    assert raw["quality"] == "stub"
    notes = raw["notes"]
    assert "NOT YET DESCRIBED HERE" in notes or "NOT AS A LANGUOID" in notes, notes[:200]
    assert "placeholder" in notes.lower() or "not a claim" in notes.lower(), notes[:200]


@pytest.mark.parametrize("code", sorted(c for c in ATTESTED if c != "ar-SA-x-janubi"))
def test_a_described_lect_names_where_its_description_is(code):
    """The claim these entries do make is that a published description exists."""
    sources = _raw(code)["sources"]
    assert sources, "attested means someone published it; say who"
    for s in sources:
        assert s.get("author") and s.get("year") and s.get("title"), s


def test_janubi_claims_a_label_rather_than_a_languoid():
    """It is a corpus label over villages that disagree with each other, so it cites
    no grammar and must not pretend to."""
    raw = _raw("ar-SA-x-janubi")
    assert raw["sources"] == []
    assert "NOT AS A LANGUOID" in raw["notes"]
    assert raw["parent"] == "ar-x-peninsular", (
        "parenting it to rijal-alma or tihama-qahtan would assert a grouping no "
        "source supports")
