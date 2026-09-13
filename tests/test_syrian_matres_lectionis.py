"""Syrian Arabic (``ar-SY``) matres lectionis cases the grapheme table is pinned to.

The sources and the gold counts are cited in the ``ar-SY`` spec notes; this file
only pins the readings.
"""
import pytest

from orthography2ipa.g2p import G2P

AR_SY = G2P("ar-SY")


@pytest.mark.parametrize("word, vowel", [("تين", "iː"), ("جميل", "iː"), ("نور", "uː")])
def test_waw_and_ya_after_a_consonant_are_long_vowels(word, vowel):
    out = AR_SY.transcribe(word)
    assert vowel in out, out


@pytest.mark.parametrize("word, glide", [("ولد", "w"), ("يوم", "j")])
def test_waw_and_ya_word_initially_stay_glides(word, glide):
    assert AR_SY.transcribe(word).lstrip("ˈ").startswith(glide)
