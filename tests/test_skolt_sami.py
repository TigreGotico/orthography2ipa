"""Skolt Sami (`sms`) — orthography letters and the suprasegmental palatalisation mark.

Expected strings are written from the letter→phoneme inventory of the 1973
orthography (the same values NorthEuraLex and WikiPron independently
transcribe), not read back from the engine.
"""
import unicodedata

import pytest

import orthography2ipa as o2i


@pytest.fixture(scope="module")
def sms():
    return o2i.G2P("sms")


def strip_stress(s):
    return s.replace("ˈ", "").replace("ˌ", "")


@pytest.mark.parametrize("letter,ipa", [
    ("a", "ɑ"),      # open back unrounded, not the front /a/ that ⟨ä⟩ spells
    ("â", "ɐ"),
    ("ä", "a"),
    ("å", "ɔ"),
    ("e", "e"),
    ("i", "i"),
    ("o", "o"),
    ("õ", "ɘ"),
    ("u", "u"),
])
def test_vowel_letters(sms, letter, ipa):
    assert strip_stress(sms.transcribe_word(letter)) == ipa


@pytest.mark.parametrize("letter,ipa", [
    ("h", "x"),      # ⟨h⟩ is the velar fricative, word-initially too
    ("j", "ʝ"),      # ⟨j⟩ is the voiced palatal fricative, not the glide
    ("ǩ", "cç"),     # voiceless palatal affricate
    ("ǧ", "ɟʝ"),     # voiced palatal affricate
    ("đ", "ð"),
    ("ǥ", "ɣ"),
    ("c", "ts"),
    ("č", "tʃ"),
])
def test_consonant_letters(sms, letter, ipa):
    assert strip_stress(sms.transcribe_word(letter)) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("nj", "ɲ"),     # palatal nasal digraph
    ("lj", "ʎ"),     # palatal lateral digraph
    ("nnj", "ɲɲ"),   # its geminate, spelt with the doubled first letter
    ("llj", "ʎʎ"),
])
def test_palatal_sonorant_digraphs(sms, word, ipa):
    assert strip_stress(sms.transcribe_word(word)) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("aa", "ɑː"),
    ("ââ", "ɐː"),
    ("ää", "aː"),
    ("åå", "ɔː"),
    ("ee", "eː"),
    ("ii", "iː"),
    ("oo", "oː"),
    ("õõ", "ɘː"),
    ("uu", "uː"),
])
def test_doubled_vowel_letter_is_one_long_nucleus(sms, word, ipa):
    assert strip_stress(sms.transcribe_word(word)) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("cc", "tts"),
    ("čč", "ttʃ"),
    ("ǩǩ", "ccç"),
    ("ǧǧ", "ɟɟʝ"),
    ("ǯǯ", "ddʒ"),
    ("ʒʒ", "ddz"),
])
def test_geminate_affricates_double_the_first_element(sms, word, ipa):
    assert strip_stress(sms.transcribe_word(word)) == ipa


# The palatalisation mark is written with several codepoints in the wild: the
# 1973 standard uses U+02B9 MODIFIER LETTER PRIME, printed and machine-readable
# sources substitute U+00B4 ACUTE ACCENT or U+02CA MODIFIER LETTER ACUTE ACCENT.
PALATALISATION_MARKS = ["ʹ", "´", "ˊ"]


@pytest.mark.parametrize("mark", PALATALISATION_MARKS)
def test_mark_palatalises_the_following_consonant(sms, mark):
    assert strip_stress(sms.transcribe_word("čâ" + mark + "lmm")) == "tʃɐlʲmm"


@pytest.mark.parametrize("mark", PALATALISATION_MARKS)
def test_mark_is_never_silently_dropped(sms, mark):
    """Regression: every mark used for palatalisation must reach the output.

    An unmapped grapheme is deleted without trace, so the mark has to leave a
    ⟨ʲ⟩ behind rather than vanish.
    """
    assert "ʲ" in sms.transcribe_word("hâ" + mark + "dd")


@pytest.mark.parametrize("mark", PALATALISATION_MARKS)
def test_mark_before_a_vowel_letter_contributes_no_segment(sms, mark):
    assert strip_stress(sms.transcribe_word("pâ" + mark + "el")) == "pɐel"


@pytest.mark.parametrize("mark", ["'", "’"])
def test_apostrophe_is_a_declared_silent_grapheme(sms, mark):
    """The apostrophe of the dictionary quantity notation carries no segment.

    It must still be a declared key: an undeclared character is dropped
    silently, which hides the fact that the spec never accounted for it.
    """
    assert mark in o2i.get("sms").graphemes
    assert strip_stress(sms.transcribe_word("jiõg" + mark + "g")) == "ʝiɘɡɡ"


def test_every_orthographic_character_is_mapped(sms):
    """No letter of a real Skolt Sami word may fall through unmapped."""
    graphemes = o2i.get("sms").graphemes
    alphabet = "aâbcčʒǯdđefghijklmnŋoõpqrsštuvzž" + "åä" + "ǥǧǩ" + "".join(PALATALISATION_MARKS) + "'’"
    missing = [c for c in alphabet if c not in graphemes and c not in "q"]
    assert missing == [], missing


def test_palatalisation_mark_codepoints_are_distinct():
    """Guard against the Latin-lookalike confusion these marks invite."""
    names = {unicodedata.name(m) for m in PALATALISATION_MARKS}
    assert names == {
        "MODIFIER LETTER PRIME",
        "ACUTE ACCENT",
        "MODIFIER LETTER ACUTE ACCENT",
    }
