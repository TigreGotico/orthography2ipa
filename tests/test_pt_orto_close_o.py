"""The stressed ⟨o⟩ of the words in ⟨-orto⟩ is close [o] in pt-PT.

Infopédia writes [o] in all 25 single words that end in ⟨-orto⟩. Cunha & Cintra
(Nova Gramática do Português Contemporâneo, 7th ed., pp. 197-198) state the
class of close-vowel nouns that open in the plural, and name `porto` and `corpo`.
The adjective lists of pp. 265-267 do not name `morto`, `torto` or `absorto`.

The same list holds the rest of the pp. 197-198 class, the words that p. 198 says
open in Portugal, and the adjectives of p. 267, where the library read [ɔ] and
Infopédia writes [o]. Their plurals keep the open vowel.

Verb forms with the same ending stay out of the list. Cunha & Cintra (pp. 429-431)
give the stem-stressed forms of such verbs the semi-open vowel. The gold values
below are Infopédia rows, in its own notation.
"""
from __future__ import annotations

import re

import pytest

from orthography2ipa import G2P, get

RULE_ID = "PT_LEX_CLOSE_O"

INFOPEDIA = {
    "porto": "ˈportu",
    "desporto": "dəʃˈportu",
    "aerodesporto": "ɐɛrɔdəʃˈportu",
    "aeroporto": "ɐɛrɔˈportu",
    "heliporto": "ɛliˈportu",
    "hidroporto": "idrɔˈportu",
    "vertiporto": "vərtiˈportu",
    "anteporto": "ɐ̃təˈportu",
    "angiporto": "ɐ̃ʒiˈportu",
    "morto": "ˈmortu",
    "natimorto": "nɐtiˈmortu",
    "semimorto": "səmiˈmortu",
    "remorto": "ʀəˈmortu",
    "torto": "ˈtortu",
    "retorto": "ʀəˈtortu",
    "boquitorto": "bukiˈtortu",
    "horto": "ˈortu",
    "aborto": "ɐˈbortu",
    "antiaborto": "ɐ̃tiɐˈbortu",
    "autoaborto": "awtɔɐˈbortu",
    "absorto": "ɐˈbsortu",
    "conforto": "kõˈfortu",
    "desconforto": "dəʃkõˈfortu",
    "reconforto": "ʀəkõˈfortu",
    "lorto": "ˈlortu",
}

#: The Cunha & Cintra words that join the list, with their Infopédia rows.
CUNHA_CINTRA = {
    "abrolho": "ɐˈbroʎu", "caroço": "kɐˈrosu", "escolho": "(i)ʃˈkoʎu",
    "esforço": "(i)ʃˈforsu", "sobrolho": "suˈbroʎu", "contorno": "kõˈtornu",
    "estorvo": "(i)ʃˈtorvu", "socorro": "suˈkoʀu", "corcovo": "kurˈkovu",
    "fogo": "ˈfoɡu", "poço": "ˈposu", "tijolo": "tiˈʒolu", "coro": "ˈkoru",
    "forno": "ˈfornu", "porco": "ˈporku", "corno": "ˈkornu", "tojo": "ˈtoʒu",
    "corpo": "ˈkorpu", "fosso": "ˈfosu", "posto": "ˈpoʃtu", "tordo": "ˈtordu",
    "corvo": "ˈkorvu", "imposto": "ĩˈpoʃtu", "povo": "ˈpovu", "despojo": "dəsˈpoʒu",
    "jogo": "ˈʒoɡu", "troco": "ˈtroku", "destroço": "dəʃˈtrosu", "miolo": "ˈmjolu",
    "almoço": "aɫˈmosu", "bolso": "ˈboɫsu", "sogro": "ˈsoɡru",
    "disposto": "diʃˈpoʃtu", "grosso": "ˈɡrosu", "chocho": "ˈʃoʃu", "chocha": "ˈʃoʃɐ",
    "fosco": "ˈfoʃku", "fosca": "ˈfoʃkɐ", "fofo": "ˈfofu", "fofa": "ˈfofɐ",
}

#: Page 267 keeps the close vowel of these in the feminine, and gives no plural.
KEEPS_CLOSE_IN_FEMININE = ("chocho", "fosco", "fofo")

#: Words of the lists that stay out, with the default open vowel. `foro` has the
#: Infopédia row [ˈfɔru]. `reforço`, `renovo` and `troço` have no row. The noun
#: sense of `rogo`, `toco` and `tomo` is not clearly the frequent one.
LIST_WORDS_LEFT_OUT = {
    "foro": "ˈfɔɾu",
    "reforço": "ʁɨˈfɔɾsu",
    "renovo": "ʁɨˈnɔvu",
    "troço": "ˈtɾɔsu",
    "rogo": "ˈʁɔɡu",
    "toco": "ˈtɔku",
    "tomo": "ˈtɔmu",
}

#: Forms outside the list, with the default open vowel. `torta` is an Infopédia
#: row. The other vowels stay a lead until a source covers them.
UNCHANGED = {
    "suporto": "suˈpɔɾtu",
    "transporto": "tɾɐ̃ʃˈpɔɾtu",
    "importo": "ĩˈpɔɾtu",
    "exporto": "eʃˈpɔɾtu",
    "comporto": "kõˈpɔɾtu",
    "mortos": "ˈmɔɾtuʃ",
    "morta": "ˈmɔɾtɐ",
    "desportos": "dɨʃˈpɔɾtuʃ",
    "torta": "ˈtɔɾtɐ",
}

#: Specs that inherit the list from pt-PT.
INHERITING = ["pt-PT", "pt-PT-x-alentejo", "pt-PT-x-algarve", "pt-AO", "pt-TL"]
#: Specs that switch the rule off for their own stressed mid-vowel process.
OWN_PROCESS = {
    "pt-PT-x-porto": "ˈmwɔɾtu",
    "pt-PT-x-braga": "ˈmwɔɾtu",
    "pt-PT-x-terceira": "ˈmwɔɾtu",
}


def stressed_rhyme(ipa: str) -> str:
    """The text from the stressed back mid vowel to the end, with ⟨r⟩ as [ɾ]."""
    syllable = ipa.rsplit("ˈ", 1)[-1]
    return re.search("[oɔ].*", syllable).group().replace("r", "ɾ").replace("ʀ", "ʁ")


@pytest.mark.parametrize("word,gold", INFOPEDIA.items())
def test_stressed_rhyme_matches_infopedia(word: str, gold: str) -> None:
    assert stressed_rhyme(G2P("pt-PT").transcribe_word(word)) == stressed_rhyme(gold)


@pytest.mark.parametrize("word,gold", CUNHA_CINTRA.items())
def test_list_word_matches_infopedia(word: str, gold: str) -> None:
    assert stressed_rhyme(G2P("pt-PT").transcribe_word(word)) == stressed_rhyme(gold)


@pytest.mark.parametrize("word", [w for w in {**INFOPEDIA, **CUNHA_CINTRA}
                                  if w.endswith("o") and w not in KEEPS_CLOSE_IN_FEMININE])
def test_plural_stays_open(word: str) -> None:
    assert stressed_rhyme(G2P("pt-PT").transcribe_word(word + "s")).startswith("ɔ")


@pytest.mark.parametrize("word", ["disposta", "grossa"])
def test_opening_feminine_stays_open(word: str) -> None:
    assert stressed_rhyme(G2P("pt-PT").transcribe_word(word)).startswith("ɔ")


@pytest.mark.parametrize("word,ipa", LIST_WORDS_LEFT_OUT.items())
def test_list_word_left_out_keeps_the_default(word: str, ipa: str) -> None:
    assert G2P("pt-PT").transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", UNCHANGED.items())
def test_form_outside_the_list_keeps_the_default(word: str, ipa: str) -> None:
    assert G2P("pt-PT").transcribe_word(word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("aeroporto", "ɐɨɾuˈpoɾtu"),
    ("autoaborto", "awtuɐˈboɾtu"),
    ("conforto", "kõˈfoɾtu"),
])
def test_rule_leaves_unstressed_o_alone(word: str, ipa: str) -> None:
    assert G2P("pt-PT").transcribe_word(word) == ipa


@pytest.mark.parametrize("spec", INHERITING)
@pytest.mark.parametrize("word,stressed", [
    ("desporto", "ˈpo"), ("morto", "ˈmo"), ("conforto", "ˈfo"),
])
def test_inheriting_spec_reads_the_close_vowel(spec: str, word: str, stressed: str) -> None:
    assert stressed in G2P(spec).transcribe_word(word)


@pytest.mark.parametrize("spec,ipa", OWN_PROCESS.items())
def test_spec_with_its_own_process_keeps_it(spec: str, ipa: str) -> None:
    assert G2P(spec).transcribe_word("morto") == ipa


def test_pt_br_list_stays_separate() -> None:
    pt_pt_words = next(r for r in get("pt-PT").allophone_rules if r.id == RULE_ID).word
    pt_br_words = next(r for r in get("pt-BR").allophone_rules if r.id == RULE_ID).word
    assert "desporto" in pt_pt_words
    assert "desporto" not in pt_br_words
