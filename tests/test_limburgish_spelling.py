"""Limburgish (``li``) spelling-to-sound cases the grapheme table is pinned to.

The sources are cited in the ``li`` spec notes; this file only pins the readings.
"""
import pytest

from orthography2ipa.g2p import G2P

LI = G2P("li")


@pytest.mark.parametrize("word", ["Amboss", "Begenn", "Jannewaar", "Blitterswik"])
def test_doubled_consonant_letter_is_not_a_geminate(word):
    out = LI.transcribe(word)
    assert not any(c * 2 in out for c in "bdfklmnprst"), out


@pytest.mark.parametrize("word", ["Baasch", "Aïsch"])
def test_sch_is_the_postalveolar_fricative(word):
    out = LI.transcribe(word)
    assert "ʃ" in out and "sç" not in out, out


def test_g_before_a_back_vowel_is_the_velar_fricative():
    assert LI.transcribe("Gott").lstrip("ˈ").startswith("ɣ")


def test_g_before_a_front_vowel_is_the_palatal_fricative():
    assert LI.transcribe("gitaar").lstrip("ˈ").startswith("ʝ")
