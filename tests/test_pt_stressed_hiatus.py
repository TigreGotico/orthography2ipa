"""A tonic ⟨í ú⟩ after a vowel is a hiatus, and the stress mark sits on it.

The Acordo Ortográfico 1990, Base X, 1.º writes the acute on a tonic ⟨i u⟩
"quando antecedidas de uma vogal com que não formam ditongo": juízes, ruína,
ciúme, miúdo, saída, baú. The accent marks the stress and the hiatus at once.

The Portuguese grapheme table writes every diphthong with a glide (⟨ui⟩ is
[uj]), so an IPA [ui] or [iu] in a transcription comes only from such a hiatus.
The specs declare ``ipa_diphthongs`` empty for that reason: the orthographic
⟨ui⟩ and ⟨iu⟩ entries of ``diphthongs`` would merge the IPA pair into one
syllable, and the mark would land a syllable early (ˈpɾuibɨ for ⟨proíbe⟩).
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, get
from orthography2ipa.stress import syllabify_for_mark
from orthography2ipa.types import StressRules


def _ipa(lang: str, word: str) -> str:
    return G2P(lang).transcribe_word(word)


# Expected forms: stress on the accented vowel (AO90 Base X, 1.º), pretonic
# ⟨o⟩ → [u], ⟨a⟩ → [ɐ], ⟨e⟩ → [ɨ] and final ⟨e⟩ → [ɨ], ⟨a⟩ → [ɐ] in EP.
EP_HIATUS = [
    ("proíbe", "pɾuˈibɨ"),
    ("juízes", "ʒuˈizɨʃ"),
    ("atribuído", "ɐtɾibuˈidu"),
    ("contribuí", "kõtɾibuˈi"),
    ("viúva", "viˈuvɐ"),
    ("saída", "sɐˈidɐ"),
    ("baú", "bɐˈu"),
    ("reúne", "ʁɨˈunɨ"),
]


@pytest.mark.parametrize("lang", ["pt-PT", "pt-PT-x-lisbon"])
@pytest.mark.parametrize("word,expected", EP_HIATUS)
def test_ep_stress_lands_on_the_accented_hiatus_vowel(lang, word, expected):
    assert _ipa(lang, word) == expected


# Brazilian Portuguese keeps the pretonic ⟨a⟩ as [a], so the IPA pair is [ai]
# or [au], which the orthographic ⟨ai⟩ ⟨au⟩ entries also merged.
BR_HIATUS = [
    ("saída", "saˈidɐ"),
    ("país", "paˈis"),
    ("baú", "baˈu"),
]


@pytest.mark.parametrize("word,expected", BR_HIATUS)
def test_br_stress_lands_on_the_accented_hiatus_vowel(word, expected):
    assert _ipa("pt-BR", word) == expected


# A falling diphthong written without an accent stays one nucleus: the glide
# keeps it out of the vowel run, so the empty IPA list cannot split it.
@pytest.mark.parametrize("lang", ["pt-PT", "pt-PT-x-lisbon", "pt-BR"])
@pytest.mark.parametrize("word,expected", [
    ("fui", "ˈfuj"),
    ("foi", "ˈfoj"),
])
def test_unaccented_diphthong_stays_one_syllable(lang, word, expected):
    assert _ipa(lang, word) == expected


@pytest.mark.parametrize("lang", ["pt-PT", "pt-PT-x-lisbon"])
def test_muito_and_cuidado_keep_the_diphthong_syllable_stressed(lang):
    assert _ipa(lang, "muito").startswith("ˈm")
    assert _ipa(lang, "cuidado").endswith("ˈdadu")


def test_portuguese_specs_declare_an_empty_ipa_list():
    assert get("pt-PT").stress.ipa_diphthongs == ()
    assert get("pt-BR").stress.ipa_diphthongs == ()


def test_undeclared_ipa_list_falls_back_to_the_orthographic_one():
    assert get("ca").stress.ipa_diphthongs is None
    rules = StressRules(diphthongs=("ui",))
    assert syllabify_for_mark("pɾuibɨ", rules) == ["pɾui", "bɨ"]


def test_declared_empty_ipa_list_makes_every_vowel_a_nucleus():
    rules = StressRules(diphthongs=("ui",), ipa_diphthongs=())
    assert syllabify_for_mark("pɾuibɨ", rules) == ["pɾu", "i", "bɨ"]
    assert syllabify_for_mark("fuj", rules) == ["fuj"]


def test_declared_ipa_list_is_read_instead_of_the_orthographic_one():
    rules = StressRules(diphthongs=("ui",), ipa_diphthongs=("iə",))
    assert syllabify_for_mark("pɾuibɨ", rules) == ["pɾu", "i", "bɨ"]
    assert syllabify_for_mark("biəɾ", rules) == ["biəɾ"]
