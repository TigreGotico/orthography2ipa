"""A word-initial pretonic ⟨en em⟩ is the raised nasal vowel in pt-BR.

Barbosa & Albano (2004: 231): "the sequence /eN/ is often pronounced as [ɪ̃],
in pre-stressed, word-initial position, as in the words ɪ̃ˈtɐ̃ʊ̯ and
ɪ̃ᵐbɾuʎavɐ". Their passages give envolto as [ĩvoʊ̯tʊ]. The spec writes the
close [ĩ] for the near-close vowel, as it writes [i] for the final [ɪ] of the
same source. Carmo (2019) measures the raising before a coda nasal at 79.2 %
(p. 811) and writes [i]ntupiu (p. 811), [i]ntortou (p. 816) and [i]nfaixou
(p. 808). The rule and its full citation are BR_INITIAL_EN_RAISE in pt-BR.json.

The other values come from the same sources: the diphthong of ⟨ão⟩ (Barbosa &
Albano 2004: 230, written [ɐ̃w̃] in this spec), the pretonic [ẽ] after an
onset in temporal [tẽᵐpoˈɾaʊ̯] (p. 229) and esplendor [isplẽⁿdor] (p. 231),
the stressed nasal [ẽ] (sento, p. 229), the nasal diphthong of a word-final
⟨-em⟩ (p. 230), and the blocked raising before a coda /R/ in erguer (Carmo
2019: 812).
"""
import pytest

from orthography2ipa import transcribe
from orthography2ipa.json_loader import load_json_spec


@pytest.mark.parametrize("word", ["então", "Então"])
def test_entao(word):
    assert transcribe(word, "pt-BR") == "ĩˈtɐ̃w̃"


@pytest.mark.parametrize("word", [
    "embrulhava", "envolto", "entupiu", "entortou", "enfaixou",
])
def test_a_word_initial_pretonic_en_em_is_raised(word):
    out = transcribe(word, "pt-BR")
    assert out.startswith("ĩ"), out


def test_a_pretonic_en_after_an_onset_keeps_the_mid_vowel():
    assert transcribe("temporal", "pt-BR").startswith("tẽ")


def test_a_word_medial_pretonic_en_keeps_the_mid_vowel():
    assert "plẽ" in transcribe("esplendor", "pt-BR")


@pytest.mark.parametrize("word", ["entre", "ênfase"])
def test_a_stressed_initial_en_keeps_the_mid_vowel(word):
    assert transcribe(word, "pt-BR").startswith("ˈẽ")


@pytest.mark.parametrize("word", ["enorme", "emoção"])
def test_an_initial_e_before_an_onset_nasal_is_oral(word):
    out = transcribe(word, "pt-BR")
    assert out[0] == "e" and out[1] != "̃", out


def test_an_initial_e_before_a_coda_r_is_not_raised():
    assert transcribe("erguer", "pt-BR").startswith("e")


def test_the_clitic_em_keeps_the_nasal_diphthong():
    assert transcribe("em", "pt-BR") == "ẽj̃"


def test_the_rule_stands_before_the_nasal_e_raise():
    ids = [r.id for r in load_json_spec("pt-BR").allophone_rules]
    assert ids.index("BR_INITIAL_EN_RAISE") < ids.index("PT_NASAL_E_RAISE")


@pytest.mark.parametrize("code", ["pt-BR-x-sp", "pt-BR-x-sul", "pt-BR-x-rj"])
def test_children_inherit_the_raising(code):
    assert transcribe("então", code).startswith("ĩ")
