"""An unmarked stressed ⟨o⟩ in pt-PT-x-lisbon takes the open default of pt-PT.

The spec held a positional row for ⟨o⟩ with no `nucleus_stressed` or
`word_initial` key. A child row replaces the whole parent row, so a stressed
⟨o⟩ fell to the grapheme table and read [o]. No source gives Lisbon that close
default. The gold values are Infopédia rows, in its own notation.
"""
from __future__ import annotations

import re

import pytest

from orthography2ipa import G2P, get

SPEC = "pt-PT-x-lisbon"

INFOPEDIA_OPEN = {
    "porta": "ˈpɔrtɐ",
    "hora": "ˈɔrɐ",
    "nova": "ˈnɔvɐ",
    "corte": "ˈkɔrt(ə)",
    "escola": "(i)ʃˈkɔlɐ",
}

#: Words with no Lisbon feature, so the dialect and the standard agree.
SAME_AS_STANDARD = [
    "porta", "hora", "nova", "forte", "sol", "ovo", "operação", "casa", "bonito",
    "comida", "cidade", "amigo", "pá", "cama", "como", "sopa",
]


def stressed_vowel(ipa: str) -> str:
    """The back mid vowel after the last stress mark."""
    return re.search("[oɔ]", ipa.rsplit("ˈ", 1)[-1]).group()


def test_spec_rows_are_the_parent_rows() -> None:
    lisbon, standard = get(SPEC), get("pt-PT")
    for grapheme in ("a", "o"):
        assert lisbon.positional_graphemes[grapheme] == standard.positional_graphemes[grapheme]


@pytest.mark.parametrize("word,gold", INFOPEDIA_OPEN.items())
def test_stressed_o_matches_infopedia(word: str, gold: str) -> None:
    assert stressed_vowel(G2P(SPEC).transcribe_word(word)) == stressed_vowel(gold)


@pytest.mark.parametrize("word", SAME_AS_STANDARD)
def test_word_without_a_lisbon_feature_matches_the_standard(word: str) -> None:
    assert G2P(SPEC).transcribe_word(word) == G2P("pt-PT").transcribe_word(word)


@pytest.mark.parametrize("word,ipa", [
    ("coelho", "kuˈɐʎu"),
    ("fecho", "ˈfɐʃu"),
    ("leite", "ˈlɐjtɨ"),
    ("ouro", "ˈoɾu"),
    ("casa", "ˈkazɐ"),
    ("bonito", "buˈnitu"),
    ("melhor", "mɨˈʎɔɾ"),
])
def test_lisbon_features_stay(word: str, ipa: str) -> None:
    assert G2P(SPEC).transcribe_word(word) == ipa
