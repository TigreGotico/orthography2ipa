"""Gulf Arabic (``ar-x-gulf``) matres lectionis cases the grapheme table is pinned to.

The sources and the gold counts are cited in the ``ar-x-gulf`` spec notes; this
file only pins the readings.
"""
import pytest

from orthography2ipa.g2p import G2P

GULF = G2P("ar-x-gulf")


@pytest.mark.parametrize("word, vowels", [("تيلة", ("iː", "eː")), ("بوك", ("uː", "oː")), ("موج", ("uː", "oː"))])
def test_waw_and_ya_after_a_consonant_are_long_vowels(word, vowels):
    out = GULF.transcribe(word)
    assert any(v in out for v in vowels), out


@pytest.mark.parametrize("word, glide", [("ولد", "w"), ("يوم", "j")])
def test_waw_and_ya_word_initially_stay_glides(word, glide):
    assert GULF.transcribe(word).lstrip("ˈ").startswith(glide)
