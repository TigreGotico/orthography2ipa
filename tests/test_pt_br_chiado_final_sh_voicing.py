"""A word-final chiado [ʃ] takes the voicing of a following voiced consonant.

Barbosa & Albano (2004: 229): "The archiphoneme /S/ surfaces either as a
voiced or as a voiceless alveolar fricative. As in most varieties, it tends
to assimilate the voicing of the following sound." Brescancini (2015: 76)
for Florianópolis: "[s] ou [S] antes de consoante surda ou pausa e [z] ou [Z]
antes de consoante sonora". The place stays palatal because these specs write
the coda as [ʃ]. The rule is BR_FINAL_SH_VOICING in each spec.

Before a vowel the specs still write [ʃ], which no source supports. Brescancini
(2015: 76): "em fronteira de palavra diante de vogais é prevista a ocorrência
apenas de [z] (mai[z] atrasada)", with the voiced palato-alveolar also found in
Florianópolis. That case is a strict xfail that names issue #2052.

The tests read only the final sibilant of each word.
"""
import pytest

from orthography2ipa import transcribe

CHIADO = ["pt-BR-x-floripa", "pt-BR-x-norte", "pt-BR-x-recife", "pt-BR-x-cuiaba"]


def _final_sibilants(phrase, lang):
    """The last segment of each word of *phrase* in *lang*."""
    return [word[-1] for word in transcribe(phrase, lang).split()]


@pytest.mark.parametrize("lang", CHIADO)
@pytest.mark.parametrize("phrase", [
    "meus netos", "os dois", "as mesas", "os barcos", "mas não", "três vezes", "os rios",
])
def test_final_sh_is_voiced_before_a_voiced_consonant(phrase, lang):
    assert _final_sibilants(phrase, lang)[0] == "ʒ"


@pytest.mark.parametrize("lang", CHIADO)
@pytest.mark.parametrize("phrase", ["meus pais", "as casas", "os chefes", "os tios"])
def test_final_sh_stays_voiceless_before_a_voiceless_consonant(phrase, lang):
    assert _final_sibilants(phrase, lang)[0] == "ʃ"


@pytest.mark.xfail(strict=True, reason="a final sibilant before a vowel is voiced (Brescancini 2015: 76); "
                   "https://github.com/TigreGotico/orthography2ipa/issues/2052")
@pytest.mark.parametrize("lang", CHIADO)
@pytest.mark.parametrize("phrase", ["mas era", "dez anos", "os amigos", "dois homens"])
def test_final_sh_is_voiced_before_a_vowel(phrase, lang):
    assert _final_sibilants(phrase, lang)[0] in {"z", "ʒ"}


@pytest.mark.parametrize("lang", CHIADO)
def test_a_word_alone_keeps_its_final_sh(lang):
    assert transcribe("dois", lang).endswith("ʃ")


@pytest.mark.parametrize("lang", CHIADO)
def test_a_pause_blocks_the_voicing(lang):
    assert _final_sibilants("dois. Era", lang)[0] == "ʃ"


@pytest.mark.parametrize("lang", CHIADO)
def test_the_last_word_of_an_utterance_keeps_its_final_sh(lang):
    assert _final_sibilants("os dois", lang)[-1] == "ʃ"


@pytest.mark.parametrize("lang, phrase, expected", [
    ("pt-BR", "os dois", "uz ˈdojs"),
    ("pt-BR", "dez anos", "ˈdɛz ˈɐ̃nus"),
    ("pt-BR-x-rj", "os dois", "uʒ ˈdojʃ"),
    ("pt-BR-x-rj", "dez anos", "ˈdɛz ˈɐ̃nuʃ"),
])
def test_base_and_rio_are_unchanged(lang, phrase, expected):
    assert transcribe(phrase, lang) == expected
