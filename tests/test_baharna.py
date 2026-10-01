"""Bahārna Arabic is not Bahrain's Gulf dialect, and the difference is segmental.

Holes (2016) distinguishes the B dialects of the Shiʿi sedentary communities from the
A dialects of the Sunni population. On the most salient variable the country spec
cannot express the B reading at all: ar-BH offers ⟨ث⟩ as [θ, t], while every B dialect
reads it [f]. These tests hold the reflexes to what Holes states, and hold out the one
reading that would make this spec describe the other community.
"""
import os

import pytest

import orthography2ipa
from orthography2ipa import get

DATA = os.path.join(os.path.dirname(orthography2ipa.__file__), "data")

BAHARNA, GULF = "ar-BH-x-baharna", "ar-BH"


def test_the_iso_code_reaches_the_spec_and_not_a_stub():
    spec = get("abv")
    assert spec.code == BAHARNA
    assert len(spec.graphemes) > 100, "resolved to something with no phonology"


def test_thaa_is_f_and_the_parent_cannot_say_so():
    """Holes 2016 §2.1.2.1 p.59: "All B dialects have /f/ for OA /ṯ/", e.g. ifnēn
    'two', falāfa 'three'. It is the one segmental member of his B-defining set."""
    assert get(BAHARNA).graphemes["ث"][0] == "f"
    assert "f" not in get(GULF).graphemes["ث"], (
        "if the Gulf table gains [f] this spec's central justification changes")


def test_theta_survives_because_a_second_source_disagrees():
    """Al-Tajir 1982 p.40 calls f a free variant rather than categorical, so the
    fricative is carried rather than dropped."""
    assert "θ" in get(BAHARNA).graphemes["ث"]


def test_the_emphatics_merge_to_the_stop_not_the_fricative():
    """Same sentence: "/ḍ/ for both OA /ḍ/ and /ḏ̣/". The Gulf parent merges both the
    other way, to [ðˤ], so this is a direction difference and not a finer reading."""
    for letter in ("ض", "ظ"):
        assert get(BAHARNA).graphemes[letter][0] == "dˤ", letter


def test_qaf_never_affricates_because_that_is_the_other_community():
    """In the A dialects /g/ < OA /q/ affricates to /ǧ/ before front vowels, which
    Holes calls "a saliently A feature" (§2.1.1.2 p.52). No B system has ǧ < q."""
    q = get(BAHARNA).graphemes["ق"]
    assert "dʒ" not in q, (
        "⟨ق⟩ reading [dʒ] is the ʿArab marker; this spec exists to distinguish the "
        "community that does not have it")
    assert set(q) == {"k", "ɡ", "q"}, q


def test_all_four_of_holes_systems_are_carried_rather_than_one_chosen():
    """B1 /k/, B2 retracted [ḳ]~[q], B3/B4 /g/ — which system a recording belongs to
    is a fact about the speaker, not about the spelling, so the lattice carries all."""
    assert len(get(BAHARNA).graphemes["ق"]) == 3
    assert get(BAHARNA).graphemes["ك"] == ["tʃ", "k"], "B1 affricates in any environment"
    assert get(BAHARNA).graphemes["ج"] == ["dʒ", "j"], "B4 has /y/ categorically"


def test_it_inherits_the_gulf_table_for_everything_it_does_not_change():
    """Only the reflexes Holes names differ; the rest is Bahrain's table."""
    b, g = get(BAHARNA).graphemes, get(GULF).graphemes
    changed = {k for k in set(b) | set(g) if b.get(k) != g.get(k)}
    assert changed == {"ث", "ذ", "ض", "ظ", "ق", "ك"}, sorted(changed)


def test_jim_is_declared_on_holes_and_not_inherited():
    """⟨ج⟩ reads the same in ar-BH, so this key changes nothing today and could look
    redundant. Both readings are Holes' own — /ǧ/ = [ʤ] for B1–B3 (p.61), /y/ < OA
    /ǧ/ "categorically" for B4 (p.62) — so the agreement is a coincidence and the key
    is declared to keep his reading if the Gulf table is ever corrected.

    This test exists to make that coincidence visible: if ar-BH's ⟨ج⟩ changes, this
    goes red and somebody decides deliberately, rather than the two drifting apart
    unnoticed."""
    import json
    import os

    raw = json.load(open(os.path.join(DATA, "ar-BH-x-baharna.json"), encoding="utf-8"))
    assert raw["graphemes"]["ج"] == ["dʒ", "j"], "declared locally on Holes"
    if get(GULF).graphemes["ج"] != ["dʒ", "j"]:
        pytest.fail(
            "ar-BH's ⟨ج⟩ has changed. The Baharna value is Holes' and stands on its "
            "own, but the coincidence this test recorded is gone — check whether the "
            "Gulf change should reach Baharna too, then update this test either way.")
