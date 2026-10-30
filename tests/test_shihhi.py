"""Šiḥḥi Arabic, on the two reflexes Bernabela (2011) states and the parent cannot.

ar-OM reads ⟨ع⟩ as [ʕ] alone and ⟨ظ⟩ as [ðˤ] alone. Bernabela gives the glottal stop as
the primary reflex of Old Arabic ʕ and the plosive for the third interdental, so under
the parent neither reading is reachable.

The spec is deliberately partial: the sections stating qāf, jīm and kāf were missing from
the copy read, and those graphemes are left to the parent rather than guessed. These tests
hold that line too — a reflex appearing there later must come with a citation.
"""
import json
import os

import pytest

import orthography2ipa
from orthography2ipa import get

DATA = os.path.join(os.path.dirname(orthography2ipa.__file__), "data")
SHIHHI, OMANI = "ssh", "ar-OM"


def _raw():
    with open(os.path.join(DATA, "ssh.json"), encoding="utf-8") as fh:
        return json.load(fh)


def test_ayn_is_a_glottal_stop_and_the_parent_cannot_say_so():
    """§1.1.11 pp.26-27: "OA *ʕ has largely been lost, leaving the glottal stop ʔ as its
    primary reflex ... Word-initially it is always [ʔ]"."""
    assert get(SHIHHI).graphemes["ع"][0] == "ʔ"
    assert "ʔ" not in get(OMANI).graphemes["ع"], (
        "if ar-OM gains the glottal stop this spec's central justification changes")


def test_the_interdentals_are_plosives():
    """§1.1.10 p.26: the OA interdentals "have as their reflexes their plosive
    counterparts t, d and ḍ, respectively" — baħt, danab, ḍahr."""
    g = get(SHIHHI).graphemes
    assert g["ث"][0] == "t"
    assert g["ذ"][0] == "d"
    assert g["ظ"][0] == "dˤ"
    assert "dˤ" not in get(OMANI).graphemes["ظ"], "the parent has only the fricative here"


def test_the_fricatives_survive_because_the_source_says_they_are_heard():
    """"one may occasionally hear an interdental fricative being articulated, but this
    is probably due to the influence of MSA" — carried, not resolved."""
    g = get(SHIHHI).graphemes
    assert "θ" in g["ث"] and "ð" in g["ذ"] and "ðˤ" in g["ظ"]


def test_qaf_and_jim_are_left_to_the_parent_and_not_guessed():
    """The sections stating them were missing from the copy read. The thesis calls /g/ a
    marginal phoneme in Gulf loans, which suggests ⟨ق⟩ is not natively [ɡ] — suggestive,
    not sufficient, and deliberately not encoded."""
    raw = _raw()
    for letter in ("ق", "ج", "ك"):
        assert letter not in raw["graphemes"], (
            f"{letter} was declared without a citation; the source sections for it were "
            "not in the copy read")
    assert get(SHIHHI).graphemes["ق"] == get(OMANI).graphemes["ق"]


def test_it_changes_only_what_it_cites():
    b, o = get(SHIHHI).graphemes, get(OMANI).graphemes
    changed = {k for k in set(b) | set(o) if b.get(k) != o.get(k)}
    assert changed == {"ث", "ذ", "ظ", "ع"}, sorted(changed)


def test_it_says_it_is_partial():
    raw = _raw()
    assert raw["quality"] == "research", "not production while qaf and jim are uncited"
    assert "PARTIAL BY CONSTRUCTION" in raw["notes"]
    assert raw["sources"] and raw["sources"][0]["author"].startswith("Bernabela")


def test_it_is_not_a_stub_and_carries_what_a_described_spec_must():
    """A spec that declares reflexes is held to the repo's bar for a described one."""
    raw = _raw()
    assert raw["quality"] != "stub"
    assert raw.get("wikipedia"), "a non-stub spec must name a Wikipedia article"
