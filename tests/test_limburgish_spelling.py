"""Limburgish (``li``) spelling-to-sound cases the grapheme table is pinned to.

The sources are cited in the ``li`` spec notes; this file only pins the readings.
"""
import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.vowels import is_ipa_vowel

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


# Tone accent. Spelling 2003, printed p. 27, §8 h-i: ⟨~⟩ after the vowel
# writes sleeptoon and ⟨\⟩ writes stoottoon, with the pairs haa~s
# 'handschoen' / haa\s 'haas' and be~rg 'berg' / be\rg 'bergen'. Hermans
# 2008, p. 40, gives the Roermond pair as Accent1 [ha:s] 'haas' and Accent2
# [ha:s] 'handschoen', so ⟨\⟩ is Accent 1 and ⟨~⟩ is Accent 2. Gussenhoven
# & Peters 2019, p. 498, write the classes ¹ and ²; Peters 2006, p. 119,
# writes the digit at the end of its syllable (/boːt²/, /ˈpoː²kər/).

def _segments(ipa):
    return "".join(c for c in ipa if c not in "ˈˌ¹²")


@pytest.mark.parametrize("sleeptoon, stoottoon, unmarked", [
    ("haa~s", "haa\\s", "haas"),
    ("be~rg", "be\\rg", "berg"),
    ("ze~ve", "ze\\ve", "zeve"),
    ("vae~r", "vae\\r", "vaer"),
])
def test_tone_signs_write_the_accent_class(sleeptoon, stoottoon, unmarked):
    accent2, accent1, bare = (LI.transcribe_word(w)
                              for w in (sleeptoon, stoottoon, unmarked))
    assert accent2.count("²") == 1 and "¹" not in accent2, accent2
    assert accent1.count("¹") == 1 and "²" not in accent1, accent1
    assert "¹" not in bare and "²" not in bare, bare
    assert _segments(accent2) == _segments(accent1) == _segments(bare)


@pytest.mark.parametrize("word, next_onset", [
    ("haa~s", ""),
    ("be\\rg", ""),
    ("vae~r", ""),
    ("ze~ve", "v"),
])
def test_accent_digit_closes_its_syllable(word, next_onset):
    out = LI.transcribe_word(word)
    digit = next(i for i, c in enumerate(out) if c in "¹²")
    assert out[digit + 1:digit + 2] == next_onset, out
    if next_onset:
        assert is_ipa_vowel(out[digit - 1]), out


# Stress. Peters 2006, p. 119: Hasselt 'Stress location is as in Standard
# Belgian Dutch'; Gussenhoven & Peters 2019, p. 497: the syllable with main
# stress is 'typically the final or penultimate'; Köhnlein 2015
# (Taalportaal): 'A syllable headed by a schwa never receives stress';
# Spelling 2003, p. 10: "e of ' = onbeklemtoonde klinker". The words are
# from Spelling 2003: sjoon p. 11, kómme p. 17, verlange p. 26.

def test_a_monosyllable_is_stressed():
    assert LI.transcribe_word("sjoon").startswith("ˈʃ")


def test_stress_falls_before_a_final_schwa_syllable():
    out = LI.transcribe_word("kómme")
    assert out.startswith("ˈk") and out.count("ˈ") == 1, out


def test_a_schwa_prefix_is_not_stressed():
    out = LI.transcribe_word("verlange")
    assert out.count("ˈ") == 1, out
    assert out.split("ˈ")[1].startswith("l"), out
