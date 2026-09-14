"""Libyan Arabic (``ayl``) matres lectionis cases the grapheme table is pinned to.

The sources and the gold counts are cited in the ``ayl`` spec notes; this file
only pins the readings.
"""
import pytest

from orthography2ipa.g2p import G2P

AYL = G2P("ayl")


@pytest.mark.parametrize("word, vowel", [("موس", "uː"), ("كوشة", "uː"), ("كيب", "iː")])
def test_waw_and_ya_after_a_consonant_are_long_vowels(word, vowel):
    out = AYL.transcribe(word)
    assert vowel in out, out


@pytest.mark.parametrize("word, glide", [("وصيف", "w"), ("ولد", "w"), ("يوم", "j")])
def test_waw_and_ya_word_initially_stay_glides(word, glide):
    assert AYL.transcribe(word).lstrip("ˈ").startswith(glide)


@pytest.mark.parametrize("word, expected", [("بيوت", "bjuːt"), ("بوية", "buːja")])
def test_two_adjacent_letters_are_not_both_long_vowels(word, expected):
    assert AYL.transcribe(word).lstrip("ˈ") == expected


@pytest.mark.parametrize("word, glide", [("قهوة", "w"), ("جلابية", "j")])
def test_waw_and_ya_before_a_final_ta_marbuta_are_glides(word, glide):
    out = AYL.transcribe(word)
    assert glide + "a" in out, out
