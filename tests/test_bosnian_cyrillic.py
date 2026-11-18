"""Bosnian Cyrillic reads through the bs spec.

The alphabet is the 30-letter Bosnian Cyrillic repertoire of the ICANN
reference LGR for bs-Cyrl and of the CLDR bs_Cyrl exemplar characters. Each
letter pairs with its Latin letter as in the alphabet table of the
bosnian_wiki source. The expected value of a Cyrillic word is the Latin
spelling of the same word through the same spec.
"""
import pytest

from orthography2ipa import G2P, get, resolve, resolves_exactly

# The CLDR bs_Cyrl exemplar characters, in their order, with the Latin letter.
ALPHABET = {
    "а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "ђ": "đ", "е": "e",
    "ж": "ž", "з": "z", "и": "i", "ј": "j", "к": "k", "л": "l", "љ": "lj",
    "м": "m", "н": "n", "њ": "nj", "о": "o", "п": "p", "р": "r", "с": "s",
    "т": "t", "ћ": "ć", "у": "u", "ф": "f", "х": "h", "ц": "c", "ч": "č",
    "џ": "dž", "ш": "š",
}

# Each pair spells one word letter for letter in the two alphabets.
WORDS = [
    ("Сарајево", "Sarajevo"), ("хљеб", "hljeb"), ("џамија", "džamija"),
    ("ћуприја", "ćuprija"), ("ђак", "đak"), ("њива", "njiva"),
    ("жена", "žena"), ("чаша", "čaša"), ("цвијет", "cvijet"),
    ("кафа", "kafa"), ("музика", "muzika"), ("грах", "grah"),
    ("прст", "prst"), ("шљива", "šljiva"), ("дом", "dom"), ("лист", "list"),
]


def latin_reading(text: str) -> str:
    reading = G2P("bs").transcribe(text)
    assert reading
    return reading


def test_the_spec_holds_the_30_letters_of_the_alphabet():
    cyrillic = {key for key in get("bs").graphemes
                if any("Ѐ" <= ch <= "ӿ" for ch in key)}
    assert len(ALPHABET) == 30
    assert cyrillic == set(ALPHABET)
    written = " ".join(c for c, _ in WORDS).lower()
    assert [letter for letter in ALPHABET if letter not in written] == []


@pytest.mark.parametrize("cyrillic,latin", WORDS)
def test_a_cyrillic_word_reads_as_its_latin_spelling(cyrillic, latin):
    assert G2P("bs").transcribe(cyrillic) == latin_reading(latin)


@pytest.mark.parametrize("tag", ["bs-Cyrl", "bs-Cyrl-BA"])
def test_a_bosnian_cyrillic_tag_names_the_bs_spec(tag):
    # These are the Bosnian Cyrillic locales of CLDR. Without the alias the
    # nearest match picks sr, which reads [v] and [ɛ ɔ], not [ʋ] and [e o].
    assert resolve(tag) == "bs"
    assert resolves_exactly(tag)
    assert get(tag, strict=True).code == "bs"
    assert G2P(tag).transcribe("љубав вода") == "ʎubaʋ ʋoda"
    assert G2P(tag).transcribe("љубав вода") == latin_reading("ljubav voda")
