"""Montenegrin Cyrillic reads through the cnr spec.

The alphabet is the table of the Pravopis (2010: 7). The expected value of a
Cyrillic word is the Latin spelling of the same word through the same spec.
The word pairs come from the Pravopis (2010: 7-9, 46-47) and from Unicode
document L2/15-169, PDF page 9.
"""
import string
import unicodedata
import warnings

import langcodes
import pytest
from linguatag.matching import DEFAULT_MAX_LANGUAGE_DISTANCE, lang_distance

from orthography2ipa import G2P, UnknownVariantWarning, get, resolve

ACUTE = "\u0301"
S_ACUTE = "с" + ACUTE
Z_ACUTE = "з" + ACUTE

# Each Cyrillic letter in the order of the Pravopis table, with its Latin letter.
ALPHABET = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "ђ": "đ", "е": "e",
    "ж": "ž", "з": "z", Z_ACUTE: "ź", "и": "i", "ј": "j", "к": "k", "л": "l",
    "љ": "lj", "м": "m", "н": "n", "њ": "nj", "о": "o", "п": "p", "р": "r",
    "с": "s", S_ACUTE: "ś", "т": "t", "ћ": "ć", "у": "u", "ф": "f", "х": "h",
    "ц": "c", "ч": "č", "џ": "dž", "ш": "š",
}

WORDS = [
    (S_ACUTE + "екира", "śekira"), (S_ACUTE + "евер", "śever"),
    (S_ACUTE + "еница", "śenica"), (S_ACUTE + "еме", "śeme"),
    ("пос́ећи", "pośeći"), ("гус́еница", "guśenica"), ("мус́", "muś"),
    (Z_ACUTE + "еница", "źenica"), ("из́ести", "iźesti"),
    ("из́елица", "iźelica"), ("коз́и", "koźi"), ("З́агора", "Źagora"),
    ("љубав", "ljubav"), ("Њујорк", "Njujork"), ("џем", "džem"),
    ("ЏЕМ", "DŽEM"), ("ЉЕТО", "LJETO"), ("ЊЕДРА", "NJEDRA"),
    ("рђа", "rđa"), ("прст", "prst"), ("крст", "krst"), ("смртан", "smrtan"),
    ("срп", "srp"), ("Подгорица", "Podgorica"), ("Никшић", "Nikšić"),
    ("Жабљак", "Žabljak"), ("расходовати", "rashodovati"),
    ("читај", "čitaj"), ("фонем", "fonem"), ("бизин", "bizin"),
]

TEXT = S_ACUTE + "екира љубав"
LATIN_TEXT = "śekira ljubav"


def latin_reading(text: str) -> str:
    reading = G2P("cnr").transcribe(text)
    assert reading
    return reading


def test_the_spec_holds_the_32_letters_of_the_alphabet():
    cyrillic = {key for key in get("cnr").graphemes
                if any("Ѐ" <= ch <= "ӿ" for ch in key)}
    assert len(ALPHABET) == 32
    assert cyrillic == set(ALPHABET)
    # Unicode has no precomposed form, so NFC keeps the two code points.
    assert unicodedata.normalize("NFC", S_ACUTE) == S_ACUTE
    assert unicodedata.normalize("NFC", Z_ACUTE) == Z_ACUTE
    written = unicodedata.normalize("NFC", " ".join(c for c, _ in WORDS)).lower()
    assert [letter for letter in ALPHABET if letter not in written] == []


@pytest.mark.parametrize("cyrillic,latin", ALPHABET.items())
def test_a_cyrillic_letter_carries_the_phonemes_of_its_latin_letter(cyrillic, latin):
    graphemes = get("cnr").graphemes
    assert graphemes[cyrillic] == graphemes[latin]


def test_the_two_new_letters_read_the_montenegrin_phonemes():
    assert G2P("cnr").transcribe(S_ACUTE + "екира") == "ɕɛkira"
    assert G2P("cnr").transcribe(Z_ACUTE + "еница") == "ʑɛnitsa"
    assert G2P("cnr").transcribe("љубав вода") == "ʎubav vɔda"


@pytest.mark.parametrize("cyrillic,latin", WORDS)
def test_a_cyrillic_word_reads_as_its_latin_spelling(cyrillic, latin):
    assert G2P("cnr").transcribe(cyrillic) == latin_reading(latin)


@pytest.mark.parametrize("tag", ["cnr", "cnr-ME", "cnr-Latn", "cnr-Cyrl-ME"])
def test_each_cnr_tag_reads_both_alphabets(tag):
    assert G2P(tag).transcribe(TEXT) == latin_reading(LATIN_TEXT)
    assert G2P(tag).transcribe(LATIN_TEXT) == latin_reading(LATIN_TEXT)


def regions():
    pairs = (a + b for a in string.ascii_uppercase for b in string.ascii_uppercase)
    return [r for r in pairs if langcodes.Language.get(f"und-{r}").is_valid()]


def test_every_region_reaches_the_spec_and_reads_cyrillic():
    # A Cyrillic cnr tag reaches cnr only through langcodes, which folds it
    # into sr: the distance is 9 and the limit is 10. Past the limit the wide
    # search picks sr, which has no letter for С́.
    tags = [f"cnr-Cyrl-{region}" for region in regions()]
    assert len(tags) >= 249
    expected = latin_reading(LATIN_TEXT)
    wrong = {}
    for tag in tags:
        reached = resolve(tag)
        reading = G2P(tag).transcribe(TEXT)
        distance = lang_distance(tag, "cnr")
        if (reached != "cnr" or reading != expected
                or distance > DEFAULT_MAX_LANGUAGE_DISTANCE):
            wrong[tag] = (reached, reading, distance)
    assert wrong == {}


@pytest.mark.parametrize("tag", [
    "cnr-Cyrl-x-a", "cnr-Cyrl-ME-x-a", "cnr-Cyrl-AL-x-a", "cnr-Cyrl-DE-x-a",
    "cnr-Cyrl-x-podgoric", "cnr-Cyrl-RS-x-a",
])
def test_a_private_use_tag_reaches_the_spec_and_reads_cyrillic(tag):
    with pytest.warns(UnknownVariantWarning):
        assert resolve(tag) == "cnr"
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UnknownVariantWarning)
        assert G2P(tag).transcribe(TEXT) == latin_reading(LATIN_TEXT)


@pytest.mark.parametrize("tag", ["CNR-CYRL", "cnr-cyrl-me", "CNR-Cyrl-XK"])
def test_a_tag_in_another_case_names_the_spec(tag):
    assert resolve(tag) == "cnr"


@pytest.mark.parametrize("text,latin", [
    ("С" + ACUTE + "екира", "Śekira"),
    ("С" + ACUTE + "ЕКИРА", "ŚEKIRA"),
    ("З" + ACUTE + "еница", "Źenica"),
    ("с\u0341екира", "śekira"),
    ("з\u0341еница", "źenica"),
])
def test_each_encoded_form_of_the_letters_reads_alike(text, latin):
    # U+0341 decomposes to U+0301.
    assert G2P("cnr").transcribe(text) == latin_reading(latin)


@pytest.mark.parametrize("spacing,spaced", [
    ("с\u00b4екира", "с екира"), ("з\u00b4еница", "з еница"),
])
def test_a_spacing_acute_is_not_the_letter(spacing, spaced):
    # U+00B4 is punctuation, as in the text layer of the Pravopis (2009: 8).
    # The library does not normalise text, so the caller maps it to U+0301.
    assert G2P("cnr").transcribe(spacing) == G2P("cnr").transcribe(spaced) != ""
