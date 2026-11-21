"""A stressed unmarked ⟨e⟩ of pt-BR is open in the word classes below.

The citations are in the notes of BR_SUFFIX_ELA_OPEN, BR_SUFFIX_ELAS_OPEN,
BR_SUFFIX_ECA_OPEN, BR_SUFFIX_ECAS_OPEN, BR_SUFFIX_ESE_OPEN, BR_LEX_OPEN_E
and BR_LEX_CLOSE_E_SUFFIX in pt-BR.json. The expected vowels come from these
sources, and none of them is the engine:

* WikiPron pt-BR (por_latn_bz_broad.tsv, the Wiktionary readings): sete
  [s ɛ t͡ʃ i], pele [p ɛ l i], segue [s ɛ ɡ i], janela [ʒ a n ɛ l a], aquela,
  tela, vela, panela, mortadela, boneca, careca, peteca, biblioteca, tese,
  diocese and maionese have only the open vowel. antiestrela, protoestrela,
  barrela, camela and enxaqueca have only the close vowel. estrela and seca
  list both vowels: the noun estrela and the adjective seca are close. The
  plurals of the close words follow their singular.
* Wiktionary pt-BR rows of the unified pronunciation lexicon: sete [ˈsɛtʃi]
  and pele [ˈpɛli].
* Cunha & Cintra (Nova Gramática do Português Contemporâneo, 7.ª ed., p. 429
  and p. 431, Obs. 1): the rhizotonic verb forms of the stem vowel ⟨e⟩ have
  'e semiaberto' in Brazil, unless the ⟨e⟩ is in ⟨ei⟩, before a nasal or
  before a palatal. cancelam and revelam are such forms.
* Barbosa & Albano (2004: 229) list /e/ and /ɛ/ as contrasting stressed
  vowels, so no rule gives the height of a word outside the lists.

The close controls pass before the rules exist. Each one fails when the rule
loses the condition that keeps it close.
"""
import re

import pytest

from orthography2ipa import G2P
from orthography2ipa.registry import get

CHILDREN = [
    "pt-BR-x-bahia", "pt-BR-x-caipira", "pt-BR-x-ce", "pt-BR-x-cuiaba",
    "pt-BR-x-floripa", "pt-BR-x-fluminen", "pt-BR-x-mg", "pt-BR-x-norte",
    "pt-BR-x-paraiba", "pt-BR-x-pr", "pt-BR-x-recife", "pt-BR-x-rj",
    "pt-BR-x-sp", "pt-BR-x-sul",
]
RULES = [
    "BR_LEX_CLOSE_E_SUFFIX", "BR_SUFFIX_ELA_OPEN", "BR_SUFFIX_ELAS_OPEN",
    "BR_SUFFIX_ECA_OPEN", "BR_SUFFIX_ECAS_OPEN", "BR_SUFFIX_ESE_OPEN",
    "BR_LEX_OPEN_E",
]
OPEN_WORDS = [
    "sete", "pele", "segue",
    "janela", "tela", "vela", "ela", "dela", "aquela", "panela", "mortadela",
    "janelas", "aquelas",
    "boneca", "careca", "peteca", "biblioteca", "bonecas",
    "tese", "diocese", "maionese",
    "cancelam", "revelam",
]
CLOSE_WORDS = [
    "estrela", "estrelas", "antiestrela", "antiestrelas", "protoestrela",
    "protoestrelas", "barrela", "barrelas", "camela", "camelas", "enxaqueca",
    "enxaquecas", "anurese", "seca", "secas",
    "mesa", "mesas", "cedo", "teve",
]


def stressed_vowel(word: str, lang: str = "pt-BR") -> str:
    ipa = G2P(lang, expose_ambiguous_endings=False).transcribe_word(word)
    return re.search(r"ˈ[^aeiouɛɔɐɪʊ]*([aeiouɛɔɐɪʊ])", ipa).group(1)


@pytest.mark.parametrize("word", OPEN_WORDS)
def test_stressed_e_is_open(word):
    assert stressed_vowel(word) == "ɛ"


@pytest.mark.parametrize("word", CLOSE_WORDS)
def test_stressed_e_stays_close(word):
    assert stressed_vowel(word) == "e"


@pytest.mark.parametrize("lang", CHILDREN)
@pytest.mark.parametrize("word", ["sete", "janela", "boneca", "tese"])
def test_children_read_the_open_vowel(lang, word):
    assert stressed_vowel(word, lang) == "ɛ"


@pytest.mark.parametrize("word", ["sete", "janela", "boneca", "tese"])
def test_uruguayan_portuguese_keeps_the_close_vowel(word):
    assert stressed_vowel(word, "pt-UY") == "e"


def test_uruguayan_portuguese_switches_every_rule_off():
    rules = {rule.id: rule for rule in get("pt-UY").allophone_rules}
    for rule_id in RULES:
        assert not rules[rule_id].phonemes


def test_close_exceptions_precede_the_open_suffix_rules():
    ids = [rule.id for rule in get("pt-BR").allophone_rules]
    for rule_id in RULES[1:6]:
        assert ids.index("BR_LEX_CLOSE_E_SUFFIX") < ids.index(rule_id)
