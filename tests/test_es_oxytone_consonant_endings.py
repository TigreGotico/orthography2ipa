"""Spanish: an unaccented word that ends in a consonant other than n or s is oxytone.

Navarro Tomás 1918, Manual de pronunciación española, § 156 p. 140:
"Se pronuncia aguda, con acento sobre la última sílaba, toda palabra de dos o
más sílabas escrita sin acento y terminada en cualquier consonante que no sea
n ni s". The examples on the same page include vivac and querub.

The stress is checked as the number of syllabic vowels before the primary
mark, so the test does not depend on how the consonants are realised.
"""
import pytest

from orthography2ipa.g2p import G2P

_VOWELS = set("aeiouɛɔ")


def _vowels_before_mark(code: str, word: str) -> int:
    ipa = G2P(code).transcribe_word(word)
    assert ipa.count("ˈ") == 1, ipa
    return sum(ch in _VOWELS for ch in ipa[: ipa.index("ˈ")])


# word, syllables (the stress falls on the last one)
OXYTONES = [
    ("vivac", 2),
    ("querub", 2),
    ("robot", 2),
    ("cenit", 2),
    ("coñac", 2),
    ("complot", 2),
    ("bistec", 2),
    ("zigzag", 2),
    ("islam", 2),
]


@pytest.mark.parametrize("code", ["es-ES", "es-419", "es-MX"])
@pytest.mark.parametrize("word,syllables", OXYTONES)
def test_final_consonant_other_than_n_s_is_oxytone(code, word, syllables):
    assert _vowels_before_mark(code, word) == syllables - 1


@pytest.mark.parametrize("word,expected", [
    ("robot", "roˈβot"),
    ("cenit", "θeˈnit"),
    ("vivac", "biˈβak"),
    ("coñac", "koˈɲak"),
    ("complot", "komˈplot"),
])
def test_es_es_oxytone_transcription(word, expected):
    assert G2P("es-ES").transcribe_word(word) == expected


# Controls: a final n or s keeps the penult, and a written accent wins.
@pytest.mark.parametrize("word,stressed_index", [
    ("joven", 0),
    ("lunes", 0),
    ("álbum", 0),
    ("fórceps", 0),
    ("déficit", 0),
])
def test_n_s_endings_and_written_accent_unchanged(word, stressed_index):
    assert _vowels_before_mark("es-ES", word) == stressed_index


def test_final_stress_endings_has_no_duplicate():
    from orthography2ipa.json_loader import load_json_spec
    endings = load_json_spec("es-ES").stress.final_stress_endings
    assert len(endings) == len(set(endings))
