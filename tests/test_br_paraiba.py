"""Distinguishing features of the Paraíba spec, pt-BR-x-paraiba.

Each expected form is the pt-BR reading of the word with the rule of the
cited source applied, in the spec's broad notation. Where the source prints
the word, the test uses its form. The rule notes in the spec hold the quotes.
The /t d/ and coda /S/ sources describe João Pessoa.
"""
from __future__ import annotations

import warnings

import pytest

from orthography2ipa import registry, transcribe

PARAIBA = "pt-BR-x-paraiba"


# /t d/ stay dental before [i]: palatalisation "em torno de 7% nas oclusivas
# antes de [i]" in the VALPB corpus, where "[t]ia e [d]ia" are the plain forms
# (Hora, Henrique & Amorim 2018: 280); the ALiB rates João Pessoa "baixa"
# (Battisti & Dornelles Filho 2015: 226).
@pytest.mark.parametrize("word, expected", [
    ("tia", "ˈtiɐ"),
    ("noite", "ˈnojti"),
    ("dentes", "ˈdẽtis"),  # and coda /S/ alveolar word-finally (2018: 283-284)
])
def test_t_d_stay_stops_before_i(word, expected):
    assert transcribe(word, PARAIBA) == expected


# After a coda [ʃ ʒ] the affricate is the more frequent form: "dentre os
# contextos precedentes, a fricativa palatal foi a que mais condicionou a taxa
# de produção das oclusivas dentais (56.4%)" (Hora, Henrique & Amorim 2018:
# 292). Gráfico 6 gives 3.7 % after a glide, 1.8 % after a pause and 3.1 % after
# a vowel, a liquid or a nasal, so those contexts keep the stop. mestre has
# ⟨tr⟩, not /t/ before [i], and keeps its cluster.
@pytest.mark.parametrize("word, expected", [
    ("desde", "ˈdeʒd͡ʒi"),
    ("desdizer", "deʒd͡ʒiˈze"),
    ("festival", "feʃt͡ʃiˈvaw"),
    ("tarde", "ˈtahdi"),
    ("noite", "ˈnojti"),
    ("tia", "ˈtiɐ"),
    ("dia", "ˈdiɐ"),
    ("verdade", "vehˈdadi"),
    ("mestre", "ˈmeʃtɾi"),
])
def test_t_d_before_i_are_affricates_only_after_a_palatal_coda(word, expected):
    assert transcribe(word, PARAIBA) == expected


# Coda /S/ is alveolar before other consonants and word-finally. Hora, Henrique
# & Amorim (2018: 284) give "ca[ʃ]ca", "me[ʒ]mo" and "doi[ʃ]" as stereotypes of
# Rio de Janeiro and Recife, and pessoenses produce the coda "como alveolar
# prioritariamente".
@pytest.mark.parametrize("word, expected", [
    ("casca", "ˈkaskɐ"),
    ("mesmo", "ˈmezmu"),
    ("dois", "ˈdojs"),
])
def test_coda_s_alveolar_elsewhere(word, expected):
    assert transcribe(word, PARAIBA) == expected


# Coda /S/ is palatal before /t d/: "é quase categórico o uso [ʃ, ʒ] antes das
# consoantes oclusivas dentais [t] e [d]" (Hora, Henrique & Amorim 2018: 283);
# "po[s]te e de[z]de se tornam po[ʃ]te e de[ʒ]de" (p. 280). Coda ⟨x⟩ shares the
# archiphoneme, so texto takes the palatal too.
@pytest.mark.parametrize("word, expected", [
    ("posto", "ˈpoʃtu"),
    ("texto", "ˈteʃtu"),
    ("desde", "ˈdeʒd͡ʒi"),  # /d/ is the affricate after the palatal coda
])
def test_coda_s_palatal_before_t_d(word, expected):
    assert transcribe(word, PARAIBA) == expected


# Coda /R/ is "[- vibrante] e [- anterior]" (Callou, Serra & Cunha 2015: 197),
# and João Pessoa deletes word-final /R/ in 95-97 % of tokens (p. 207).
@pytest.mark.parametrize("word, expected", [
    ("verde", "ˈvehdi"),
    ("mar", "ˈma"),
])
def test_coda_r_aspirate_and_final_r_deleted(word, expected):
    assert transcribe(word, PARAIBA) == expected


# Pretonic /o/ opens before a nasal stressed vowel (Mota & Lopes 2018: 215);
# in the Atlas Linguístico da Paraíba, pretonic /O/ lowers in 81 of the 98
# tokens that keep or lower it (Silva, Araújo & Viana 2018: 277).
def test_pretonic_o_opens_before_nasal_stressed_vowel():
    assert transcribe("fogão", PARAIBA) == "fɔˈɡɐ̃w̃"


# Pretonic /e/ opens before the low vowel [a] (Mota & Lopes 2018: 215:
# "diante da vogal baixa [a]").
def test_pretonic_e_opens_before_low_stressed_vowel():
    assert transcribe("pedaço", PARAIBA) == "pɛˈdasu"


# Every source studies pretonic vowels only, so a posttonic mid vowel keeps
# the pt-BR reading.
@pytest.mark.parametrize("word", ["pérola", "época", "abóbora", "cócegas"])
def test_posttonic_vowels_keep_the_pt_br_reading(word):
    assert transcribe(word, PARAIBA) == transcribe(word, "pt-BR")


@pytest.mark.parametrize("tag", [
    "pt-BR-x-paraiba", "pt-BR-x-pb", "pt-Latn-BR-x-paraiba", "PT-BR-X-PARAIBA",
])
def test_tags_resolve_to_the_spec_without_warning(tag):
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        assert registry.resolve(tag) == PARAIBA


def test_state_code_alias_reads_the_spec():
    assert registry.get("pt-BR-x-pb") is registry.get(PARAIBA)
    assert transcribe("posto", "pt-BR-x-pb") == "ˈpoʃtu"
