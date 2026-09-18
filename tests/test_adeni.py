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
    assert sorted(raw["graphemes"]) == sorted(["ث", "ذ", "ج"])
    assert raw["quality"] == "research"
    assert raw["graphemes_base"] == PARENT


def test_qaf_and_kaf_are_left_to_the_parent():
    """The source lists both /q/ and /g/ in the inventory and does not say which the
    letter takes. That is the case a phone inventory cannot settle, so neither letter is
    declared here and both resolve to the parent's values."""
    path = os.path.join(os.path.dirname(o2i.__file__), "data", "acq.json")
    with open(path, encoding="utf-8") as fh:
        raw = json.load(fh)
    assert "ق" not in raw["graphemes"] and "ك" not in raw["graphemes"]
    assert get(ADEN).graphemes["ق"] == get(PARENT).graphemes["ق"]


def test_the_contradicted_letter_is_named_in_the_notes():
    """The source says Adeni lacks the emphatic fricative, which is the only value the
    parent gives for zaa — so the inherited reflex is one the source denies. It is not
    corrected, because a negative fact licenses no positive one, and the notes have to
    say so or the next reader will take the inheritance for a finding."""
    path = os.path.join(os.path.dirname(o2i.__file__), "data", "acq.json")
    with open(path, encoding="utf-8") as fh:
        raw = json.load(fh)
    assert "ظ" not in raw["graphemes"]
    assert "LACKS" in raw["notes"] and "no replacement" in raw["notes"].lower()
