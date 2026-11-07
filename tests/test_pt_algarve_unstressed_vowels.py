"""An unstressed ⟨e o⟩ in pt-PT-x-algarve takes the pt-PT values.

The spec has no positional row for ⟨e⟩ or ⟨o⟩, because no source gave one. The
one source that transcribes the Algarve writes [ɨ]. Brissos (2014, Journal of
Portuguese Linguistics 13(1), p. 79) gives Praia da Salema "[dɨb'uʎõ]/[dɨb'ʉʎõ]
'debulham'" and "[kɨɾ'yʒɐ] 'coruja'". `coruja` does not show [u], so the [u] of
⟨o⟩ is the parent default and no measured value.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, get

SPEC = "pt-PT-x-algarve"

#: Words with no Algarve feature, so the dialect and the standard agree.
SAME_AS_STANDARD = [
    "pedir", "menino", "telefone", "pessoa", "governo", "comida", "bonito",
    "árvore", "domicílio", "forte", "porta", "pedra", "ovo", "operação",
    "objetivo", "ocasião", "ocorrer",
]


def test_spec_rows_are_the_parent_rows() -> None:
    algarve, standard = get(SPEC), get("pt-PT")
    for grapheme in ("e", "o"):
        assert algarve.positional_graphemes[grapheme] == standard.positional_graphemes[grapheme]


def test_brissos_pretonic_e_is_central() -> None:
    assert G2P(SPEC).transcribe_word("debulham").startswith("dɨˈb")


def test_pretonic_o_takes_the_parent_default() -> None:
    assert G2P(SPEC).transcribe_word("coruja") == "kuˈɾyʒɐ"


@pytest.mark.parametrize("word", SAME_AS_STANDARD)
def test_word_without_an_algarve_feature_matches_the_standard(word: str) -> None:
    assert G2P(SPEC).transcribe_word(word) == G2P("pt-PT").transcribe_word(word)


@pytest.mark.parametrize("word,ipa", [
    ("pedir", "pɨˈdiɾ"),
    ("telefone", "tɨlɨˈfɔnɨ"),
    ("comida", "kuˈmidɐ"),
    ("árvore", "ˈaɾvuɾɨ"),
    ("porque", "ˈpuɾkɨ"),
])
def test_unstressed_value(word: str, ipa: str) -> None:
    assert G2P(SPEC).transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("tudo", "ˈtydu"),
    ("mudo", "ˈmudu"),
    ("mas", "ˈmaʒ"),
    ("leite", "ˈletɨ"),
    ("outro", "ˈotɾu"),
    ("bem", "ˈbẽj̃"),
    ("homens", "ˈɔmẽʒ"),
    ("o", "u"),
    ("os", "uʒ"),
])
def test_algarve_features_stay(word: str, ipa: str) -> None:
    assert G2P(SPEC).transcribe_word(word) == ipa
