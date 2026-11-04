"""A word-final nasal takes the place of the next word's first consonant.

Navarro Tomás, Manual de pronunciación española (1918), § 87, p. 66: "En
contacto con estas mismas consonantes iniciales de palabra, la n final de una
palabra anterior se pronuncia también m": un buen baile [um bwem baile], en
pie [em pjé].

Lipski, "Reduction of Spanish Word-Final /s/ and /n/" (1986), p. 140 writes
velarization as n → ŋ / __ # [−cons], and pp. 146-147 give word-final
preconsonantal /n/ "the normal process of homorganic assimilation of nasal
consonants to following obstruents". Lipski, "Geographical and Social
Varieties of Spanish: An Overview" (2011), p. 7, names the velarizing areas:
Andalusia, the Canary Islands, all Caribbean and Central American dialects
and the Pacific coast of Colombia, Peru and Ecuador.
"""
import pytest

from orthography2ipa.g2p import G2P

NON_VELARIZING = ["es-ES", "es-MX", "es-AR", "es-CO", "es-AR-x-norte"]
VELARIZING = ["es-VE", "es-PR", "es-DO", "es-CU", "es-PA", "es-NI",
              "es-CO-x-costa", "es-ES-x-andalusia-w"]


@pytest.mark.parametrize("code", NON_VELARIZING + VELARIZING)
@pytest.mark.parametrize("text, expected", [
    ("un peso", "um ˈpeso"),
    ("en pie", "em ˈpje"),
    ("un buen baile", "um ˈbwem ˈbai̯le"),
    ("en la casa", "en la ˈkasa"),
])
def test_word_final_n_before_a_consonant_takes_its_place(code, text, expected):
    assert G2P(code).transcribe(text) == expected


@pytest.mark.parametrize("code", NON_VELARIZING)
def test_word_final_n_before_a_vowel_or_a_velar_stays_n(code):
    g2p = G2P(code)
    assert g2p.transcribe("un otro") == "un ˈotɾo"
    assert g2p.transcribe("un gato") == "un ˈɡato"


@pytest.mark.parametrize("code", VELARIZING)
@pytest.mark.parametrize("text, expected", [
    ("un otro", "uŋ ˈotɾo"),
    ("un gato", "uŋ ˈɡato"),
    ("pan", "ˈpaŋ"),
    ("tren. Pero", "ˈtɾeŋ ˈpeɾo"),
])
def test_velar_word_final_n_before_a_vowel_a_velar_or_a_pause(code, text, expected):
    assert G2P(code).transcribe(text) == expected


# The creoles keep the nasal: their notes give no source for the Castilian rule.
@pytest.mark.parametrize("code", ["cbk-PH", "pln"])
def test_creoles_keep_the_word_final_nasal(code):
    assert G2P(code).transcribe("un peso").startswith("un ")


def test_norte_keeps_the_lateral_apart_from_y():
    g2p = G2P("es-AR-x-norte")
    assert g2p.transcribe("calle") == "ˈkaʎe"
    assert g2p.transcribe("cayo") == "ˈkaʝo"
