"""Egyptian Arabic (``ar-EG``) matres lectionis cases the grapheme table is pinned to.

The sources and the gold counts are cited in the ``ar-EG`` spec notes; this file
only pins the readings.
"""
import pytest

from orthography2ipa.g2p import G2P

AR_EG = G2P("ar-EG")


@pytest.mark.parametrize("word, vowel", [("جيم", "iː"), ("سين", "iː"), ("توت", "uː"), ("روح", "uː")])
def test_waw_and_ya_after_a_consonant_are_long_vowels(word, vowel):
    out = AR_EG.transcribe(word)
    assert vowel in out, out


@pytest.mark.parametrize("word, glide", [("ولد", "w"), ("يوم", "j")])
def test_waw_and_ya_word_initially_stay_glides(word, glide):
    assert AR_EG.transcribe(word).lstrip("ˈ").startswith(glide)


@pytest.mark.parametrize("word, expected", [("بيوت", "bjuːt"), ("بوية", "buːja")])
def test_two_adjacent_letters_are_not_both_long_vowels(word, expected):
    assert AR_EG.transcribe(word).lstrip("ˈ") == expected


@pytest.mark.parametrize("word, glide", [("قهوة", "w"), ("جمعية", "j")])
def test_waw_and_ya_before_a_final_ta_marbuta_are_glides(word, glide):
    out = AR_EG.transcribe(word)
    assert glide + "a" in out, out


@pytest.mark.parametrize("word, expected", [("قَوِي", "ʔawiː"), ("حَيِي", "ħajiː")])
def test_final_ya_after_a_kasra_key_is_a_long_vowel(word, expected):
    # The inherited keys َوِ and َيِ absorb the kasra, so the next ⟨ي⟩ looks
    # like it follows a vowel and would read [j]. After a kasra, a final ⟨ي⟩
    # is a long vowel, as ِي reads in عَلِي.
    assert AR_EG.transcribe(word).lstrip("ˈ") == expected


def test_medial_ya_after_a_kasra_key_stays_a_glide():
    assert AR_EG.transcribe("قَوِيَّة").lstrip("ˈ") == "ʔaˈwijja".lstrip("ˈ")
    assert AR_EG.transcribe("عَلِي").lstrip("ˈ") == "ʕaliː"
