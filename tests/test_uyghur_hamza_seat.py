"""The Uyghur hamza seat ⟨ئ⟩ is silent at the start of a word and /ʔ/ inside it.

UEY writes a vowel that has no consonant before it on the seat ⟨ئ⟩. The
Uyghur Arabic alphabet article states that the seat "also represents /ʔ/ but
it is usually ignored at the beginning of words. It still reads /ʔ/ in the
middle, such as سائەت /sɑʔæt/ hour". The expected values apply that statement
and the spec's own vowel phonemes by hand (the spec writes ⟨ە⟩ as /ɛ/).
"""
import pytest

from orthography2ipa import transcribe


def _t(word):
    return transcribe(word, "ug")


@pytest.mark.parametrize("word,expected", [
    ("سائەت", "sɑʔɛt"),     # saet, the article's own example
    ("ئائىت", "ɑʔit"),      # initial seat silent, medial seat /ʔ/
    ("مۇئەللىم", "muʔɛllim"),
])
def test_medial_seat_is_a_glottal_stop(word, expected):
    assert _t(word) == expected


@pytest.mark.parametrize("seat_vowel,expected", [
    ("ئا", "ɑ"), ("ئە", "ɛ"), ("ئې", "e"), ("ئى", "i"),
    ("ئۆ", "ø"), ("ئو", "o"), ("ئۇ", "u"), ("ئۈ", "y"),
])
def test_initial_seat_is_silent(seat_vowel, expected):
    assert _t(seat_vowel) == expected
    assert _t(seat_vowel + "ت") == expected + "t"


def test_initial_seat_before_a_whole_word():
    assert _t("ئۇيغۇر") == "ujʁur"
