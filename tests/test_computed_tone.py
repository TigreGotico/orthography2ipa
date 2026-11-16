# -*- coding: utf-8 -*-
"""Tone computed from the shape of the syllable, over invented data.

The engine may not know that the system it is reading is Thai's, so these
tests state a small made-up one — two classes, one mark, three tones — and
check that the table alone decides the answer.
"""
import pytest

from orthography2ipa.tone import assign_computed_tones
from orthography2ipa.types import ToneRules


@pytest.fixture
def rules():
    return ToneRules(
        classes={"b": "low", "p": "high"},
        marks={"'": "acute"},
        tones={"flat": "˧", "up": "˦˥", "down": "˨˩"},
        table={
            "low": {"live": {"none": "flat"},
                    "dead_short": {"none": "up"},
                    "dead_long": {"none": "down"},
                    "any": {"acute": "up"}},
            "high": {"live": {"none": "up"},
                     "dead_short": {"none": "down"},
                     "dead_long": {"none": "down"},
                     "any": {"acute": "down"}},
        },
        dead_codas=("t",),
    )


def test_a_live_syllable_reads_its_class(rules):
    assert assign_computed_tones(("b", "a"), ("b", "aː"), rules) == "baː˧"
    assert assign_computed_tones(("p", "a"), ("p", "aː"), rules) == "paː˦˥"


def test_a_stop_coda_makes_the_syllable_dead(rules):
    assert assign_computed_tones(("b", "a", "t"), ("b", "aː", "t"),
                                 rules) == "baːt˨˩"
    assert assign_computed_tones(("b", "a", "t"), ("b", "a", "t"),
                                 rules) == "bat˦˥"


def test_a_short_vowel_with_no_coda_is_dead_and_a_long_one_is_live(rules):
    assert assign_computed_tones(("b", "a"), ("b", "a"), rules) == "ba˦˥"
    assert assign_computed_tones(("b", "a"), ("b", "aː"), rules) == "baː˧"


def test_a_sonorant_coda_leaves_the_syllable_live(rules):
    assert assign_computed_tones(("b", "a", "n"), ("b", "a", "n"),
                                 rules) == "ban˧"


def test_a_mark_overrides_the_shape_of_the_rime(rules):
    """The mark slot spells no segment of its own and still decides."""
    assert assign_computed_tones(("b", "'", "a"), ("b", "", "aː"),
                                 rules) == "baː˦˥"
    assert assign_computed_tones(("p", "'", "a"), ("p", "", "aː"),
                                 rules) == "paː˨˩"


def test_each_syllable_is_toned_on_its_own(rules):
    assert assign_computed_tones(
        ("b", "a", "n", "p", "a"), ("b", "a", "n", "p", "aː"),
        rules) == "ban˧paː˦˥"


def test_a_syllable_whose_onset_has_no_class_is_left_untoned(rules):
    assert assign_computed_tones(("k", "a"), ("k", "aː"), rules) == "kaː"


def test_a_reading_with_no_nucleus_comes_back_unchanged(rules):
    assert assign_computed_tones(("b",), ("b",), rules) == "b"


def test_an_onset_cluster_takes_the_class_of_the_letter_that_opens_it(rules):
    """One grapheme spelling a whole cluster is one onset, and the first
    of its letters that the table names is the one that decides."""
    assert assign_computed_tones(("br",), ("braː",), rules) == "braː˧"
