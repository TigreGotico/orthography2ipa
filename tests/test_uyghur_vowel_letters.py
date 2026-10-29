"""Every vowel letter of the Uyghur Arabic alphabet (UEY) has a value in ug.

UEY writes eight vowels with eight letters: ⟨ا ە ې ى ۆ و ۇ ۈ⟩, ULY a e ë i ö o
u ü. A word-initial vowel sits on the hamza seat ⟨ئ⟩. The letter for /æ~ɛ/ is
ARABIC LETTER AE, U+06D5 ⟨ە⟩. It is not ARABIC LETTER HEH, U+0647 ⟨ه⟩, which
modern UEY does not use (the /h/ letter is U+06BE ⟨ھ⟩, and ⟨ه⟩ belongs to the
pre-1950s Perso-Arabic spelling). A spec keyed on U+0647 drops every ⟨ە⟩ that
is not on a hamza seat, so ⟨ئۇيغۇرچە⟩ came out *[ujʁurtʃ].

The expected values are the spec's own phoneme for each letter, applied by
hand to the ULY spellings that the Uyghur Arabic alphabet article gives beside
the UEY forms (Hesen, xelq, Qeshqer, Xoten, Uyghurche, -lær).
"""
import pytest

from orthography2ipa import get, transcribe


def _t(word):
    return transcribe(word, "ug")


@pytest.mark.parametrize("letter,expected", [
    ("ا", "ɑ"),   # ا  a
    ("ە", "ɛ"),   # ە  e
    ("ې", "e"),   # ې  ë
    ("ى", "i"),   # ى  i
    ("ۆ", "ø"),   # ۆ  ö
    ("و", "o"),   # و  o
    ("ۇ", "u"),   # ۇ  u
    ("ۈ", "y"),   # ۈ  ü
])
def test_each_vowel_letter_has_its_value(letter, expected):
    assert _t(letter) == expected
    assert _t("ئ" + letter) == expected


@pytest.mark.parametrize("word,expected", [
    ("ئۇيغۇرچە", "ujʁurtʃɛ"),   # Uyghurche
    ("ھەسەن", "hɛsɛn"),         # Hesen
    ("خەلق", "χɛlq"),           # xelq
    ("قەشقەر", "qɛʃqɛr"),       # Qeshqer
    ("خوتەن", "χotɛn"),         # Xoten
    ("لەر", "lɛr"),             # plural suffix -lær
])
def test_ae_inside_and_at_the_end_of_a_word(word, expected):
    assert _t(word) == expected


def test_heh_is_not_a_uyghur_vowel_letter():
    assert "ه" not in get("ug").graphemes
