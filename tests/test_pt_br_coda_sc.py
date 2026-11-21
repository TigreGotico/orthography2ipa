"""pt-BR reads ⟨sc⟩ before a front vowel and ⟨sç⟩ as one /s/, in every spec.

Vasilévski (2012: 55, Table 1) lists "sc /s/ fascinante" and "sç /s/ cresça"
as digraphs of the phoneme /s/, apart from "s |S| mosca, lesma", the coda
archiphoneme. A chiado spec palatalises the archiphoneme in a coda, so it must
leave the digraph alone. The expected value of each word is the same word
written with a plain ⟨c⟩ or ⟨ss⟩ for the /s/, which no rule of this file reads.
"""
import pytest

from orthography2ipa import transcribe

CHIADO = ["pt-BR-x-rj", "pt-BR-x-norte", "pt-BR-x-recife", "pt-BR-x-floripa", "pt-BR-x-cuiaba"]
FAMILY = ["pt-BR", "pt-BR-x-sp", "pt-BR-x-sul", "pt-BR-x-mg", *CHIADO]

PAIRS = [
    ("nascer", "nacer"),
    ("crescer", "krecer"),
    ("descer", "decer"),
    ("piscina", "picina"),
    ("disciplina", "diciplina"),
    ("nascimento", "nacimento"),
    ("fascinante", "facinante"),
    ("cresça", "creça"),
]


@pytest.mark.parametrize("code", FAMILY)
@pytest.mark.parametrize("word, plain", PAIRS)
def test_sc_is_one_s_like_a_plain_c(code, word, plain):
    assert transcribe(word, code) == transcribe(plain, code)


@pytest.mark.parametrize("code", CHIADO)
def test_a_chiado_sc_has_no_palatal(code):
    assert "ʃ" not in transcribe("nascer", code)
    assert "ʃ" not in transcribe("crescer", code)


@pytest.mark.parametrize("code", CHIADO)
def test_a_chiado_coda_s_before_a_k_stays_palatal(code):
    """⟨c⟩ is [k] before ⟨o a l r⟩, so there is no digraph and the coda keeps its value."""
    for word in ("escola", "escada", "esclarecer", "escrever"):
        assert "ʃ" in transcribe(word, code)


def test_the_rj_values():
    assert transcribe("nascer", "pt-BR-x-rj") == "naˈseh"
    assert transcribe("piscina", "pt-BR-x-rj") == "piˈsĩnɐ"
