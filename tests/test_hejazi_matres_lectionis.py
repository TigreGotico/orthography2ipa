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


@pytest.mark.parametrize("word, expected", [("قَوِي", "ɡawiː"), ("حَيِي", "ħajiː")])
def test_final_ya_after_a_kasra_key_is_a_long_vowel(word, expected):
    # arb's keys َوِ and َيِ absorb the kasra, so a word-final ⟨ي⟩ after them
    # looked like it followed a vowel and read [j]. After a kasra, a final
    # ⟨ي⟩ is a long vowel, as ِي reads in عَلِي.
    assert AR_HEJAZ.transcribe(word).lstrip("ˈ") == expected


def test_a_kasra_key_plus_ya_is_long_medially_too():
    """After a kasra, ⟨ي⟩ is a long vowel wherever it stands.

    dev read قَوِيم as ɡaˈwijm, a glide, because the arb key َوِ takes the
    kasra. The positional keys read iː in both positions now.
    """
    assert AR_HEJAZ.transcribe("قَوِيم") == "ɡaˈwiːm"


def test_a_shadda_keeps_the_geminate_glide():
    """A shadda doubles the letter before the graphemes are read, so the
    doubled keys َوِيي and َيِيي carry the geminate. Without them the long
    reading would swallow it and ⟨قَوِيَّة⟩ would read ...wiːja, which also
    breaks the pinned ar-QA-005 arabic_tts row.
    """
    assert AR_HEJAZ.transcribe("قَوِيَّة") == "ɡaˈwijja"
    assert AR_HEJAZ.transcribe("عَرَبِيَّة") == "ʕaraˈbijja"
    assert AR_HEJAZ.transcribe("عَلِي").lstrip("ˈ") == "ʕaliː"

