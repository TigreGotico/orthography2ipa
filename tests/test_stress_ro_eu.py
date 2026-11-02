"""Default stress placement for Romanian (ro-RO) and Standard Basque (eu).

Every expected position below is the stressed syllable the cited source
writes for that word, counted from the start of the word. The words are the
regular class each source describes; the lexically marked words the sources
also list are outside the default rule and are not asserted here.

Romanian: final stress on a consonant-final word, penultimate stress on any
other word, final stress on a word-final falling diphthong (Chițoran 2002:
75-77, tabulated in Alexei & Ulfsbjorninn 2022: 2-5, 18, 21; Franzén & Horne
1997: 75-77).

Basque: Batua takes the General Central [+2] accent, on the second syllable
counted from the left (Hualde 1994: 1559; Elordieta, Gaminde & Hualde 1998:
402). East of the Bidasoa the accent is penultimate [-2] (Hualde 2022: 92, 97).
"""
import unicodedata

import pytest

import orthography2ipa
from orthography2ipa.registry import get

_VOWELS = set("aeiouəɨɐɛɔ")
_NON_SYLLABIC = "̯"


def _stressed_syllable(ipa: str) -> int:
    """1-based syllable that the primary mark precedes: the syllabic vowels
    written before the mark, plus one. A vowel carrying U+032F is a glide."""
    assert "ˈ" in ipa, ipa
    head = ipa[:ipa.index("ˈ")]
    count = 0
    for i, ch in enumerate(head):
        if ch not in _VOWELS:
            continue
        j = i + 1
        while j < len(head) and unicodedata.combining(head[j]):
            j += 1
        if _NON_SYLLABIC not in head[i + 1:j]:
            count += 1
    return count + 1


ROMANIAN = [
    # Alexei & Ulfsbjorninn 2022: 2, Table 1a (after Chițoran 2002a: 75-77)
    ("mare", 1), ("nume", 1), ("femeie", 2), ("mașină", 2),
    ("bărbat", 2), ("mesaj", 2), ("animal", 3), ("magazin", 3),
    # Alexei & Ulfsbjorninn 2022: 4-5, Table 2a-i and 2b-i
    ("sare", 1), ("avere", 2), ("cămară", 2), ("căldare", 2),
    ("albastru", 2), ("căpăstru", 2), ("balon", 2), ("balcon", 2),
    ("mărunt", 2), ("argint", 2), ("asasin", 3), ("geamantan", 3),
    # Franzén & Horne 1997: 75-77
    ("copil", 2), ("burduf", 2), ("amurg", 2), ("balaur", 2),
    ("teorie", 3), ("băiețandru", 3),
    # Alexei & Ulfsbjorninn 2022: 6, examples (1): stressed derivational suffixes
    ("iepuraș", 3), ("puișor", 2), ("portar", 2), ("mărime", 2),
    ("singurătate", 4), ("obrăznicie", 4),
    # Alexei & Ulfsbjorninn 2022: 18, 21: a word-final falling diphthong is stressed
    ("gunoi", 2), ("pârâu", 2), ("birou", 2), ("liceu", 2),
]

BASQUE = [
    # Elordieta, Gaminde & Hualde 1998: 402 (young Donostia Batua speakers)
    ("gizon", 2), ("atal", 2), ("enbor", 2),
    ("mendia", 2), ("basoa", 2), ("gizona", 2), ("mutilla", 2),
    ("mendiak", 2), ("gizonak", 2),
    ("autobusa", 2), ("alarguna", 2), ("gizonena", 2), ("amarentzat", 2),
    ("txistularia", 2), ("alargunena", 2), ("gizonarena", 2),
    ("lagunarentzat", 2), ("txistulariari", 2), ("alargunenari", 2),
    ("gizonarentzako", 2), ("txistulariarena", 2), ("alargunarenari", 2),
    ("baserritarrarentzat", 2),
    # Hualde 1994: 1559, proposal (12-I)
    ("txakurra", 2), ("emakumea", 2), ("bertsolariarekin", 2),
]


@pytest.mark.parametrize("word,syllable", ROMANIAN)
def test_romanian_default_stress(word, syllable):
    ipa = orthography2ipa.transcribe(word, "ro-RO")
    assert _stressed_syllable(ipa) == syllable, ipa


@pytest.mark.parametrize("word,syllable", BASQUE)
def test_basque_batua_second_syllable(word, syllable):
    ipa = orthography2ipa.transcribe(word, "eu")
    assert _stressed_syllable(ipa) == syllable, ipa


def test_basque_mark_does_not_split_s_stop():
    # txistúlaria (Elordieta, Gaminde & Hualde 1998: 402), and /s/ + stop is
    # split between two syllables in Batua: i.ra.kas.le (Euskaltzaindia,
    # Euskara Batuaren Eskuliburua, 'azentua').
    assert orthography2ipa.transcribe("txistularia", "eu") == "tʃis̺ˈtulaɾia"


@pytest.mark.parametrize("code", ["eu-x-zuberera", "eu-x-lapurtera",
                                  "eu-x-nafarra-beherea",
                                  "eu-x-erronkariera"])
def test_eastern_basque_is_penultimate(code):
    # Hualde 2022: 92: "East of the Bidasoa river, the most common pattern is
    # penultimate accentuation, [–2]".
    assert get(code).stress.default_position == -2


def test_souletin_penultimate_word():
    # Zuberoan alhába 'daughter' (Hualde 2022: 97).
    ipa = orthography2ipa.transcribe("alhaba", "eu-x-zuberera")
    assert _stressed_syllable(ipa) == 2, ipa


def test_central_basque_dialect_keeps_second_syllable():
    # Gipuzkoan is the General Central [+2] system (Hualde 2022: 84, Table 2).
    assert get("eu-x-gipuzkera").stress.default_position == 2


@pytest.mark.parametrize("code,word", [("eu-x-bizkaiera", "gizona"),
                                       ("eu-x-nafarra-garaia", "mendia")])
def test_mixed_accent_dialect_prints_no_stress(code, word):
    # Bizkaia mixes the Western phrase-accent systems with Central ones
    # (Hualde 2022: 83, Table 1); Upper Navarre holds tonal Goizueta [+2H]
    # (Hualde 2022: 84, Table 2) and the [-2] Baztan Valley (Hualde 2022: 80,
    # note 5). Neither spec takes the Batua [+2] block.
    assert "ˈ" not in orthography2ipa.transcribe(word, code)
