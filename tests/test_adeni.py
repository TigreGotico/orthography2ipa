"""Adeni Arabic: three cited reflexes, two of which the parent cannot express.

Each case is asserted against ar-YE as well. A spec that changed nothing would pass a
test that only looked at acq, and two of these three letters are exactly where the
parent disagrees.
"""
import json
import os

import pytest

import orthography2ipa as o2i
from orthography2ipa import get, transcribe

PARENT = "ar-YE"
ADEN = "acq"


@pytest.mark.parametrize("word,parent_ipa,aden_ipa,why", [
    ("ثَلَاثَة", "θaˈlaːθa", "taˈlaːta",
     "thala:thah 'three' -> tala:tah: the parent reads the interdental as a fricative "
     "alone and cannot produce this"),
    ("ذَاكِرَة", "ˈðaːkira", "ˈdaːkira",
     "dha:kirah 'a memory' -> da:kirah, likewise"),
    ("جَبَل", "ˈdʒabal", "ˈɡabal",
     "jabal 'a mountain' -> gabal: the parent already offers [g] among jim's values, so "
     "this one narrows rather than adds"),
])
def test_the_cited_reflexes(word, parent_ipa, aden_ipa, why):
    assert transcribe(word, PARENT) == parent_ipa, why
    assert transcribe(word, ADEN) == aden_ipa, why


def test_the_spec_declares_only_what_is_cited():
    path = os.path.join(os.path.dirname(o2i.__file__), "data", "acq.json")
    with open(path, encoding="utf-8") as fh:
        raw = json.load(fh)
    assert sorted(raw["graphemes"]) == sorted(["ث", "ذ", "ج", "ض", "ظ"])
    assert raw["quality"] == "research"
    assert raw["graphemes_base"] == PARENT


def _raw():
    path = os.path.join(os.path.dirname(o2i.__file__), "data", "acq.json")
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def test_qaf_and_kaf_are_left_to_the_parent():
    """The source lists both /q/ and /g/ in the inventory and does not say which the
    letter takes. That is the case a phone inventory cannot settle, so neither letter is
    declared here and both resolve to the parent's values."""
    path = os.path.join(os.path.dirname(o2i.__file__), "data", "acq.json")
    with open(path, encoding="utf-8") as fh:
        raw = json.load(fh)
    assert "ق" not in raw["graphemes"] and "ك" not in raw["graphemes"]
    assert get(ADEN).graphemes["ق"] == get(PARENT).graphemes["ق"]


def test_no_letter_emits_the_denied_phone_as_its_canonical_value():
    """The source says Adeni lacks the emphatic fricative. Both emphatics inherited it,
    and an earlier draft corrected neither while the notes named one of them.

    This asserts the property over every declared letter rather than over the two that
    happened to be noticed, so a third letter arriving with the same defect goes red.
    """
    denied = "ðˤ"
    for letter, values in _raw()["graphemes"].items():
        assert values[0] != denied, (
            f"{letter} emits the phone the source denies as its canonical reading")
    assert get(ADEN).graphemes["ض"][0] == "dˤ"
    assert get(ADEN).graphemes["ظ"][0] == "dˤ"


def test_the_inference_is_labelled_as_one():
    """dad is a reordering of values the parent already carries; zaa's stop is an
    inference, because the parent offers the fricative alone. The notes must keep those
    apart, or a later reader takes both for quotations."""
    notes = _raw()["notes"]
    assert "REORDERING" in notes and "INFERENCE" in notes
    assert "LACKS" in notes
