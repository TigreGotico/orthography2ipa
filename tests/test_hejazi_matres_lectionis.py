"""Hejazi Arabic (``ar-SA-x-hejaz``) matres lectionis cases the grapheme table is pinned to.

The sources and the gold counts are cited in the ``ar-SA-x-hejaz`` spec notes; this
file only pins the readings.
"""
import pytest

from orthography2ipa.g2p import G2P

AR_HEJAZ = G2P("ar-SA-x-hejaz")


@pytest.mark.parametrize("word, vowels", [("فوق", ("uː", "oː")), ("عليه", ("iː", "eː")), ("دود", ("uː", "oː"))])
def test_waw_and_ya_after_a_consonant_are_long_vowels(word, vowels):
    out = AR_HEJAZ.transcribe(word)
    assert any(v in out for v in vowels), out


@pytest.mark.parametrize("word, glide", [("ولد", "w"), ("يوم", "j")])
def test_waw_and_ya_word_initially_stay_glides(word, glide):
    assert AR_HEJAZ.transcribe(word).lstrip("ˈ").startswith(glide)


@pytest.mark.parametrize("word", ["بيوت", "بوية"])
def test_two_adjacent_letters_are_not_both_long_vowels(word):
    out = AR_HEJAZ.transcribe(word)
    assert "uːiː" not in out and "iːuː" not in out, out


@pytest.mark.parametrize("word, glide", [("قهوة", "w"), ("جمعية", "j")])
def test_waw_and_ya_before_a_final_ta_marbuta_are_glides(word, glide):
    out = AR_HEJAZ.transcribe(word)
    assert glide + "a" in out, out
