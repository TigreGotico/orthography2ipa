"""A word-final chiado [ʃ] in Carioca takes the voicing of the next word.

Nanini (2022), on the post-vocalic /S/ of Copacabana, gives the voiced
palatal across a word boundary before a voiced consonant, "[ʒ] meus neto
[‘meuʒ‘nɛ.tʊ]" (p. 19), and the alveolar [z] before a vowel: "a realização
deste último nesse contexto é, categoricamente, a fricativa alveolar sonora
[z]" (p. 17), as in "mas era [‘mɐi’zɛɾɐ]" (p. 26). The rules and their full
citations are RJ_FINAL_SH_VOICING and RJ_FINAL_SH_PREVOCALIC_VOICE in
pt-BR-x-rj.json.

The tests read only the final sibilant of each word, the value the source
gives.
"""
import pytest

from orthography2ipa import transcribe


def _final_sibilants(phrase):
    """The last segment of each word of *phrase* in pt-BR-x-rj."""
    return [word[-1] for word in transcribe(phrase, "pt-BR-x-rj").split()]


@pytest.mark.parametrize("phrase", [
    "meus netos", "os dois", "as mesas", "os barcos", "mas não", "três vezes",
])
def test_final_sh_is_voiced_before_a_voiced_consonant(phrase):
    assert _final_sibilants(phrase)[0] == "ʒ"


@pytest.mark.parametrize("phrase", ["mas era", "dez anos", "os amigos", "dois homens"])
def test_final_sh_is_alveolar_before_a_vowel(phrase):
    assert _final_sibilants(phrase)[0] == "z"


@pytest.mark.parametrize("phrase", ["meus pais", "as casas", "os chefes", "os rios"])
def test_final_sh_stays_voiceless_before_a_voiceless_consonant(phrase):
    """The strong /r/ of this spec is the voiceless [χ] (os rios)."""
    assert _final_sibilants(phrase)[0] == "ʃ"


def test_a_word_alone_keeps_its_final_sh():
    assert transcribe("dois", "pt-BR-x-rj").endswith("ʃ")


def test_a_pause_blocks_the_voicing():
    assert _final_sibilants("dois. Era")[0] == "ʃ"
