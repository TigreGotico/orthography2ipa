"""Ancient Greek keeps the distinctions its own table declares.

`fold_diacritics` strips a mark before the grapheme table is consulted. That is right for
a mark the transcription does not encode and wrong for one the table gives a reading of
its own, because the reading then cannot be reached. Three marks were in the second
group: the rough breathing writes /h/, the macron writes contrastive vowel length, and
the iota subscript writes a diphthong offglide. With them folded, ἑπτά and ἐπτά — a
rough/smooth minimal pair — both came out [epta].

The smooth breathing stays folded and must: it marks the ABSENCE of /h/, so ἀ and α read
alike and nothing is lost.
"""
import pytest

from orthography2ipa import get, transcribe

ROUGH, MACRON, SUBSCRIPT, SMOOTH = "̔", "̄", "ͅ", "̓"


def test_the_segmental_marks_are_not_folded():
    folds = set(get("grc").fold_diacritics)
    for mark, what in ((ROUGH, "rough breathing, which writes /h/"),
                       (MACRON, "macron, which writes contrastive length"),
                       (SUBSCRIPT, "iota subscript, which writes an offglide")):
        assert mark not in folds, f"U+{ord(mark):04X} is folded: {what}"


def test_the_smooth_breathing_stays_folded():
    """It marks the absence of /h/, so folding it loses nothing."""
    assert SMOOTH in set(get("grc").fold_diacritics)
    assert get("grc").graphemes["ἀ"] == get("grc").graphemes["α"]


@pytest.mark.parametrize("rough,smooth", [("ἑπτά", "ἐπτά"), ("ὥρα", "ὦρα")])
def test_a_rough_smooth_pair_does_not_collapse(rough, smooth):
    """The pair is minimal in the breathing alone; the readings must differ."""
    a, b = transcribe(rough, "grc"), transcribe(smooth, "grc")
    assert a != b, f"{rough} and {smooth} both read {a!r}"
    assert "h" in a, f"{rough} read {a!r} with no /h/"


@pytest.mark.parametrize("word,expected", [("ἑπτά", "h"), ("ὡ", "h"), ("ἁ", "h")])
def test_the_rough_breathing_reaches_the_output(word, expected):
    assert expected in transcribe(word, "grc"), transcribe(word, "grc")


def test_length_and_the_offglide_survive():
    """The table declares these; folding made them unreachable."""
    assert transcribe("ᾱ", "grc") != transcribe("α", "grc"), "macron lost"
    assert "j" in transcribe("ᾳ", "grc"), f'ᾳ read {transcribe("ᾳ", "grc")!r}, no offglide'


def test_modern_greek_is_untouched():
    """el folds the same marks and is right to: it lost all three distinctions."""
    folds = set(get("el").fold_diacritics)
    for mark in (ROUGH, MACRON, SUBSCRIPT, SMOOTH):
        assert mark in folds, f"el should still fold U+{ord(mark):04X}"
