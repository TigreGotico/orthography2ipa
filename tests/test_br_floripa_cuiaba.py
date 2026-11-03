"""Distinguishing features of the Florianópolis and Cuiabá specs.

Each expected form is read from the transcription the cited source prints,
rewritten in the spec's broad notation. The cited rule note in the spec holds
the quote and the page.

Lexical vowel quality is unmarked in the spelling, so most tests assert the
consonant the source describes and not the whole word.
"""
from __future__ import annotations

import pytest

from orthography2ipa import transcribe

FLORIPA = "pt-BR-x-floripa"
CUIABA = "pt-BR-x-cuiaba"


# Florianópolis: Dias (2010: 2) gives tipo [tipu]; Brescancini (2015: 76)
# gives fe[S]ta, and coda /S/ is palato-alveolar in 83 % of tokens (p. 82).
@pytest.mark.parametrize("word, expected", [("tipo", "ˈtipu"), ("tia", "ˈtiɐ"), ("dia", "ˈdiɐ")])
def test_floripa_t_d_stay_stops(word, expected):
    assert transcribe(word, FLORIPA) == expected


@pytest.mark.parametrize("word, expected", [("mas", "ˈmaʃ"), ("três", "ˈtɾeʃ"), ("paz", "ˈpaʃ")])
def test_floripa_word_final_s_palatal(word, expected):
    assert transcribe(word, FLORIPA) == expected


def test_floripa_preconsonantal_s_palatal():
    assert "ʃt" in transcribe("festa", FLORIPA)


# Brescancini (2015: 76): "[s] ou [S] antes de consoante surda ou pausa e [z] ou
# [Z] antes de consoante sonora" (me[Z]mo). The palatal coda voices before a
# voiced consonant and stays voiceless before a voiceless one.
@pytest.mark.parametrize("word, expected", [("mesmo", "ˈmeʒmu"), ("desde", "ˈdeʒdi"), ("Lisboa", "liʒˈboɐ")])
def test_floripa_palatal_coda_voices_before_voiced_consonant(word, expected):
    assert transcribe(word, FLORIPA) == expected


def test_floripa_plural_after_stop_is_raised_and_palatal():
    assert transcribe("dentes", FLORIPA) == "ˈdẽtiʃ"


# Cuiabá, Almeida (2004). /t d/ stops before [i] (pp. 151-152): sete [»sEti],
# dia [»dia], rede [»redi].
@pytest.mark.parametrize("word, expected", [("dia", "ˈdiɐ"), ("rede", "ˈredi"), ("gente", "ˈd͡ʒẽti")])
def test_cuiaba_t_d_stay_stops(word, expected):
    assert transcribe(word, CUIABA) == expected


def test_cuiaba_sete_ends_in_stop():
    assert transcribe("sete", CUIABA).endswith("ti")


# Affricates for the palatal fricatives (pp. 154-155): chegar [tSe»ga],
# chá [»tSa], já [»dZa], hoje [»odZi].
@pytest.mark.parametrize("word, expected", [
    ("chegar", "t͡ʃeˈɡa"), ("chá", "ˈt͡ʃa"), ("já", "ˈd͡ʒa"), ("hoje", "ˈod͡ʒi"),
])
def test_cuiaba_affricates(word, expected):
    assert transcribe(word, CUIABA) == expected


def test_cuiaba_x_is_affricate():
    assert transcribe("puxa", CUIABA).startswith("ˈput͡ʃ")


# Coda /S/ palatal (p. 153): mas [»maS], três [»tReS], dez [»dES],
# festas [»fEStaS]. A coda [ʃ] must not become an affricate.
@pytest.mark.parametrize("word, expected", [("mas", "ˈmaʃ"), ("três", "ˈtɾeʃ"), ("dez", "ˈdɛʃ")])
def test_cuiaba_coda_s_palatal(word, expected):
    assert transcribe(word, CUIABA) == expected


# Almeida (2004: 154): "O recuo do ponto de articulação também ocorre com a
# sonora [z] > [Z]": [»raZga] rasga, [»vaZa] várzea.
@pytest.mark.parametrize("word, expected", [("rasga", "ˈraʒɡɐ"), ("mesmo", "ˈmeʒmu"), ("desde", "ˈdeʒdi")])
def test_cuiaba_palatal_coda_voices_before_voiced_consonant(word, expected):
    assert transcribe(word, CUIABA) == expected


def test_cuiaba_festas_two_palatal_codas_no_affricate():
    got = transcribe("festas", CUIABA)
    assert got.count("ʃ") == 2 and "t͡ʃ" not in got


# Coda /l/ retroflex (p. 157): mal [»ma”], igual [i»gwa”], sinal [si»na”].
@pytest.mark.parametrize("word, expected", [("mal", "ˈmaɻ"), ("igual", "iˈɡwaɻ"), ("sinal", "siˈnaɻ")])
def test_cuiaba_coda_l_retroflex(word, expected):
    assert transcribe(word, CUIABA) == expected


# Strong /R/ is a trill (pp. 158-159): rapaz [ra»paS], burro [»buru].
@pytest.mark.parametrize("word, expected", [("rapaz", "raˈpaʃ"), ("burro", "ˈburu")])
def test_cuiaba_strong_r_trill(word, expected):
    assert transcribe(word, CUIABA) == expected


# Coda /R/ retroflex (p. 159): porto [»po”tu], curva [»ku”va].
@pytest.mark.parametrize("word", ["porto", "curva"])
def test_cuiaba_coda_r_retroflex(word):
    assert "ɻ" in transcribe(word, CUIABA)


# Word-final /R/ drops (p. 159): fazer [fa»ze], casar [ka»za]. A final /l/
# is not a rhotic and stays.
@pytest.mark.parametrize("word, expected", [("fazer", "faˈze"), ("casar", "kaˈza")])
def test_cuiaba_final_r_drops(word, expected):
    assert transcribe(word, CUIABA) == expected


# The strong /R/ is the trill (pp. 158-159) in every R-forte context, after a
# coda consonant too (Cristófaro Silva 2025: 240).
@pytest.mark.parametrize("word, expected", [("honra", "ˈõrɐ"), ("genro", "ˈd͡ʒẽru")])
def test_cuiaba_strong_r_after_coda_is_trill(word, expected):
    assert transcribe(word, CUIABA) == expected
