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


@pytest.mark.parametrize("word, expected", [("بيوت", "bjuːt"), ("بوية", "buːja")])
def test_two_adjacent_letters_are_not_both_long_vowels(word, expected):
    assert GULF.transcribe(word).lstrip("ˈ") == expected


@pytest.mark.parametrize("word, glide", [("قهوة", "w"), ("جمعية", "j")])
def test_waw_and_ya_before_a_final_ta_marbuta_are_glides(word, glide):
    out = GULF.transcribe(word)
    assert glide + "a" in out, out


@pytest.mark.parametrize("word, expected", [("قَوِي", "ɡawiː"), ("حَيِي", "ħajiː")])
def test_final_ya_after_a_kasra_key_is_a_long_vowel(word, expected):
    # arb's keys َوِ and َيِ absorb the kasra, so a word-final ⟨ي⟩ after them
    # looked like it followed a vowel and read [j]. After a kasra, a final
    # ⟨ي⟩ is a long vowel, as ِي reads in عَلِي.
    assert GULF.transcribe(word).lstrip("ˈ") == expected


def test_a_kasra_key_plus_ya_is_long_medially_too():
    """After a kasra, ⟨ي⟩ is a long vowel wherever it stands.

    dev read قَوِيم as ɡaˈwijm, a glide, because the arb key َوِ takes the
    kasra. The positional keys read iː in both positions now.
    """
    assert GULF.transcribe("قَوِيم") == "ɡaˈwiːm"


def test_a_shadda_keeps_the_geminate_glide():
    """A shadda doubles the letter before the graphemes are read, so the
    doubled keys َوِيي and َيِيي carry the geminate. Without them the long
    reading would swallow it and ⟨قَوِيَّة⟩ would read ...wiːja, which also
    breaks the pinned ar-QA-005 arabic_tts row.
    """
    assert GULF.transcribe("قَوِيَّة") == "ɡaˈwijja"
    assert GULF.transcribe("عَرَبِيَّة") == "ʕaraˈbijja"
    assert GULF.transcribe("عَلِي").lstrip("ˈ") == "ʕaliː"


@pytest.mark.parametrize("child", ["ar-AE", "ar-BH", "ar-KW", "ar-QA",
                                   "ar-SA-x-sharqiyya", "ar-SA-x-dawasir"])
def test_gulf_children_inherit_the_final_ya_keys(child):
    assert G2P(child).transcribe("قَوِي").lstrip("ˈ") == "ɡawiː"

