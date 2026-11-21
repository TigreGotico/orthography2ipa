"""A doubled consonant letter reads as one consonant in Portuguese.

Brazilian Portuguese has no geminate consonants: "consoantes geminadas não
ocorrem nessa língua", because "dois segmentos idênticos com a propriedade
[consonantal] não são permitidos" (Carvalho 2015: 44). Two native speakers
recorded by Assis (2007: 143) read the doubled letter of an English loan as
one consonant: hippie [ˈhipi], hobby [ˈhɔbɪ], lobby [ˈlɔbɪ]. Priberam gives
the same single consonant: lobby |lóbi|, hobby |óbi|. The rule notes in the
specs hold the citations.

A doubled letter only spells the consonant once, so a word with the doubled
letter reads like the same word with the letter written once.
"""
from __future__ import annotations

import pytest

from orthography2ipa import transcribe

PT_SPECS = [
    "pt-PT", "pt-BR", "pt-AO", "pt-MZ", "pt-PT-x-lisbon", "pt-PT-x-porto",
    "pt-BR-x-rj", "pt-BR-x-recife", "pt-BR-x-paraiba", "pt-UY",
]

# (doubled spelling, the same word with the letter written once)
PAIRS = [
    ("lobby", "loby"),
    ("Lotto", "Loto"),
    ("shopping", "shoping"),
    ("Uppsala", "Upsala"),
    ("hockey", "hokey"),
]


@pytest.mark.parametrize("lang", PT_SPECS)
@pytest.mark.parametrize("doubled, single", PAIRS)
def test_doubled_letter_reads_as_one_consonant(lang, doubled, single):
    assert transcribe(doubled, lang) == transcribe(single, lang)


# Priberam: lobby |lóbi|, hobby |óbi|; the ⟨h⟩ of a loan is silent in pt-PT.
@pytest.mark.parametrize("word, expected", [("lobby", "ˈlɔbi"), ("hobby", "ˈɔbi")])
def test_pt_pt_loan_reading(word, expected):
    assert transcribe(word, "pt-PT") == expected


# Carvalho (2015: 44): no two identical consonants in a row in pt-BR. The
# coda ⟨s⟩ and the ⟨c⟩ before ⟨e i⟩ of ⟨sc⟩ are both [s] in pt-BR, so the
# pair is one [s]. The final tap of the infinitive drops (BR_INFINITIVE_R).
@pytest.mark.parametrize("word, expected", [
    ("nascer", "naˈse"),
    ("crescer", "kɾeˈse"),
    ("adolescente", "adoleˈsẽt͡ʃi"),
])
def test_pt_br_sc_is_one_s(word, expected):
    assert transcribe(word, "pt-BR") == expected


# pt-PT keeps the coda [ʃ] of ⟨sc⟩, which is not the same consonant as the
# [s] after it, so the pair is not merged.
def test_pt_pt_sc_keeps_both_sibilants():
    assert transcribe("nascer", "pt-PT") == "nɐʃˈseɾ"
