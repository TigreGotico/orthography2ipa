"""A word-final /S/ in Brazilian Portuguese takes the voicing of the next word.

Barbosa & Albano (2004: 229): "The archiphoneme /S/ surfaces either as a voiced
or as a voiceless alveolar fricative. As in most varieties, it tends to
assimilate the voicing of the following sound." Their transcribed passage
(p. 231) writes "kʊ̯aʊ̯ duz doɪ̯z ɛɾɐ u maɪ̯s fɔɾtʃɪ" for qual dos dois era o
mais forte, and "maɪ̯z u viaˈʒẽⁿt" for mais o viajante.

The tests read only the final sibilant of each word, the value the source
gives, and leave the rest of each word to the word-level rules.
"""
import pytest

from orthography2ipa import transcribe


def _final_sibilants(code, phrase):
    """The last segment of each word of *phrase*."""
    return [word[-1] for word in transcribe(phrase, code).split()]


@pytest.mark.parametrize("phrase, expected", [
    ("qual dos dois era o mais forte", {1: "z", 2: "z", 5: "s"}),
    ("mais o viajante", {0: "z"}),
])
def test_barbosa_albano_passage(phrase, expected):
    finals = _final_sibilants("pt-BR", phrase)
    assert {i: finals[i] for i in expected} == expected


@pytest.mark.parametrize("phrase", [
    "os dois", "as mesas", "os gatos", "as bocas", "os jogos", "mas não",
    "três vezes", "os lagos", "os ratos",
])
def test_final_s_is_voiced_before_a_voiced_consonant(phrase):
    assert _final_sibilants("pt-BR", phrase)[0] == "z"


@pytest.mark.parametrize("phrase", [
    "dez anos", "os amigos", "os hábitos", "dois homens", "as ilhas",
    "mais uma", "os índios",
])
def test_final_s_is_voiced_before_a_vowel(phrase):
    assert _final_sibilants("pt-BR", phrase)[0] == "z"


@pytest.mark.parametrize("phrase", [
    "mais forte", "os pés", "as casas", "dois sacos", "os chefes", "três tigres",
])
def test_final_s_stays_voiceless_before_a_voiceless_consonant(phrase):
    assert _final_sibilants("pt-BR", phrase)[0] == "s"


def test_a_pause_blocks_the_voicing():
    assert _final_sibilants("pt-BR", "dois. Era")[0] == "s"


def test_a_word_alone_keeps_its_final_s():
    assert transcribe("dois", "pt-BR").endswith("s")


def test_sao_paulo_inherits_the_rule():
    assert _final_sibilants("pt-BR-x-sp", "os dois") == ["z", "s"]


def test_a_voiceless_strong_rhotic_keeps_the_sibilant_voiceless():
    """pt-BR-x-sp writes the strong rhotic as the voiceless [x]: os ratos."""
    output = transcribe("os ratos", "pt-BR-x-sp")
    assert output.split()[1].lstrip("ˈ").startswith("x")
    assert output.split()[0] == "us"


def test_uruguayan_portuguese_keeps_its_output():
    """pt-UY switches the pt-BR rules off, as it does BR_CODA_S_VOICED."""
    assert _final_sibilants("pt-UY", "os dois") == ["s", "s"]
    assert _final_sibilants("pt-UY", "dez anos") == ["s", "s"]
