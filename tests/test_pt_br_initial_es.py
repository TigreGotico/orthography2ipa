"""A word-initial pretonic ⟨e⟩ before a coda sibilant is [i] in pt-BR.

Carmo (2019: 811), north-western São Paulo state: the raising of a
word-initial pretonic /e/ before a coda sibilant applies in "99,5%
(1449/1457)", "como em [i]s.co.la e [i]s.fa.re.la". Barbosa & Albano (2004:
231) write todo o esplendor as "todʊɪspleⁿˈdoɾ". The spec writes the close
[i] for the near-close vowel, as BR_INITIAL_EN_RAISE does. The rule and its
full citation are BR_INITIAL_ES_RAISE in pt-BR.json.

The tests read only the first vowel of each word, the value the sources give.
"""
import pytest

from orthography2ipa import transcribe
from orthography2ipa.json_loader import load_json_spec


def _first_vowel(code, word):
    return transcribe(word, code).lstrip("ˈ")[0]


@pytest.mark.parametrize("word", [
    "escola", "esfarela", "esplendor", "estar", "estado", "esmola",
    "escrever", "Espanha",
])
def test_a_word_initial_pretonic_e_before_a_coda_sibilant_is_raised(word):
    assert _first_vowel("pt-BR", word) == "i"


@pytest.mark.parametrize("word", ["essencial", "Esaú"])
def test_a_sibilant_in_the_onset_keeps_the_vowel(word):
    assert _first_vowel("pt-BR", word) == "e"


@pytest.mark.parametrize("word", ["explicar", "extrair", "excluir"])
def test_an_ex_before_a_consonant_keeps_the_vowel(word):
    """No opened source counts ⟨ex⟩: Carmo (2019: 807, 815) gives only ⟨es⟩ examples."""
    assert _first_vowel("pt-BR", word) == "e"


@pytest.mark.parametrize("word", ["pestana", "festival"])
def test_a_pretonic_e_after_an_onset_keeps_the_vowel(word):
    """Carmo (2019) measures the word-initial vowel only."""
    assert transcribe(word, "pt-BR").lstrip("ˈ")[1] == "e"


@pytest.mark.parametrize("word", ["este", "esse", "estes"])
def test_a_stressed_e_keeps_the_vowel(word):
    assert _first_vowel("pt-BR", word) == "e"


def test_the_rule_stands_after_the_nasal_raise():
    ids = [r.id for r in load_json_spec("pt-BR").allophone_rules]
    assert ids.index("BR_INITIAL_EN_RAISE") < ids.index("BR_INITIAL_ES_RAISE")


@pytest.mark.parametrize("code", ["pt-BR-x-sp", "pt-BR-x-sul", "pt-BR-x-rj", "pt-BR-x-recife"])
def test_children_inherit_the_raising(code):
    """pt-BR-x-rj and pt-BR-x-recife write the coda as [ʃ]."""
    assert _first_vowel(code, "escola") == "i"


def test_uruguayan_portuguese_keeps_its_output():
    """pt-UY switches the rule off: no source on the border variety states it."""
    assert _first_vowel("pt-UY", "estar") == "e"
