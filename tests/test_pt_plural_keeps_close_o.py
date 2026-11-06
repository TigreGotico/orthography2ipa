"""Nouns that keep the close stressed ⟨o⟩ in the plural, and three that open it.

Cunha & Cintra (Nova Gramática do Português Contemporâneo, 7th ed., p. 198) say
that many nouns "conservam no plural o o fechado do singular". The gold values
are Infopédia rows, in its own notation. Infopédia has no plural rows, so the
plural vowel rests on that sentence.

Pages 197-198 put `olho`, `osso` and `ovo` in the class that opens in the plural.
A word-initial ⟨o⟩ takes the close first value of the `word_initial` row, so the
plurals read close until `PT_LEX_OPEN_O` names them. Infopédia writes [ɔ] in the
compounds below.
"""
from __future__ import annotations

import re

import pytest

from orthography2ipa import G2P

INFOPEDIA = {
    "acordo": "ɐˈkordu", "encosto": "ẽˈkoʃtu", "moço": "ˈmosu", "potro": "ˈpotru",
    "adorno": "ɐˈdornu", "engodo": "ẽˈɡodu", "reboco": "ʀəˈboku", "bojo": "ˈboʒu",
    "estojo": "(i)ʃˈtoʒu", "bolo": "ˈbolu", "ferrolho": "fəˈʀoʎu",
    "mosto": "ˈmoʃtu", "cachorro": "kɐˈʃoʀu", "globo": "ˈɡlobu", "namoro": "nɐˈmoru",
    "rolo": "ˈʀolu", "coco": "ˈkoku", "golfo": "ˈɡoɫfu", "piloto": "piˈlotu",
    "piolho": "ˈpjoʎu", "sopro": "ˈsopru", "consolo": "kõˈsolu", "poldro": "ˈpoɫdru",
    "dorso": "ˈdorsu", "logro": "ˈloɡru", "polvo": "ˈpoɫvu", "topo": "ˈtopu",
}

#: Words of the p. 198 list that stay out, with the default open vowel. The noun
#: sense of `gosto`, `colmo` and `morro` is not clearly the frequent one. Infopédia writes
#: [ɔ] in `molho` and `lobo`, and has no row for the other four.
LEFT_OUT = {
    "gosto": "ˈɡɔʃtu",
    "colmo": "ˈkɔɫmu",
    "morro": "ˈmɔʁu",
    "morros": "ˈmɔʁuʃ",
    "molho": "ˈmɔʎu",
    "lobo": "ˈlɔbu",
    "repolho": "ʁɨˈpɔʎu",
    "restolho": "ʁɨʃˈtɔʎu",
    "rosto": "ˈʁɔʃtu",
    "suborno": "suˈbɔɾnu",
}

#: The Infopédia compounds that show the open plural.
OPEN_COMPOUNDS = {
    "quatro-olhos": "kwaˈtrwɔʎuʃ",
    "lava-olhos": "lavɐˈɔʎuʃ",
    "quebra-ossos": "kɛbrɐˈɔsuʃ",
    "fios-de-ovos": "fiuʃˈdɔvuʃ",
}


def stressed_vowel(ipa: str) -> str:
    """The back mid vowel after the last stress mark."""
    return re.search("[oɔ]", ipa.rsplit("ˈ", 1)[-1]).group()


@pytest.mark.parametrize("word,gold", INFOPEDIA.items())
def test_singular_matches_infopedia(word: str, gold: str) -> None:
    assert stressed_vowel(G2P("pt-PT").transcribe_word(word)) == stressed_vowel(gold)


@pytest.mark.parametrize("word", INFOPEDIA)
def test_plural_keeps_the_close_vowel(word: str) -> None:
    assert stressed_vowel(G2P("pt-PT").transcribe_word(word + "s")) == "o"


@pytest.mark.parametrize("word,ipa", LEFT_OUT.items())
def test_word_left_out_keeps_the_default(word: str, ipa: str) -> None:
    assert G2P("pt-PT").transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("olhos", "ˈɔʎuʃ"), ("ossos", "ˈɔsuʃ"), ("ovos", "ˈɔvuʃ"),
])
def test_plural_opens(word: str, ipa: str) -> None:
    assert G2P("pt-PT").transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [("olho", "ˈoʎu"), ("osso", "ˈosu"), ("ovo", "ˈovu")])
def test_singular_stays_close(word: str, ipa: str) -> None:
    assert G2P("pt-PT").transcribe_word(word) == ipa


@pytest.mark.parametrize("word,gold", OPEN_COMPOUNDS.items())
def test_compound_matches_infopedia(word: str, gold: str) -> None:
    assert stressed_vowel(G2P("pt-PT").transcribe_word(word)) == stressed_vowel(gold)


@pytest.mark.parametrize("spec", ["pt-PT-x-alentejo", "pt-PT-x-lisbon", "pt-AO"])
def test_inheriting_spec_reads_the_open_plural(spec: str) -> None:
    assert stressed_vowel(G2P(spec).transcribe_word("olhos")) == "ɔ"
