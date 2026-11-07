"""Argentina and Uruguay merge ⟨ll⟩ and prevocalic ⟨y⟩ into one fricative, [ʃ] or [ʒ].

Lipski, "Dialects of Spanish and Portuguese" (Handbook of Dialectology,
ch. 30), p. 502: "In most of Argentina and Uruguay, /j/ has traditionally been
realized as a voiced fricative, [ʒ], but devoicing to [ʃ] has extended from
Buenos Aires and Montevideo to much of the remaining territory."

Lipski, "Geographical and Social Varieties of Spanish: An Overview", p. 5:
"In Latin America, the phoneme /ʎ/ is maintained in all regional and social
dialects of Paraguay and Bolivia, and in neighboring areas of northeastern and
northwestern Argentina."
"""
import pytest

from orthography2ipa.g2p import G2P

MERGED = ["es-AR", "es-UY", "es-AR-x-cordoba", "es-AR-x-cuyo",
          "es-AR-x-patagoni"]


@pytest.mark.parametrize("code", MERGED)
@pytest.mark.parametrize("word,expected", [
    ("yo", "ˈʃo"),
    ("mayo", "ˈmaʃo"),
    ("calle", "ˈkaʃe"),
    ("llena", "ˈʃena"),
])
def test_ll_and_y_are_the_rioplatense_fricative(code, word, expected):
    assert G2P(code).transcribe_word(word) == expected


@pytest.mark.parametrize("code", MERGED)
def test_cayo_and_callo_are_homophones(code):
    g = G2P(code)
    assert g.transcribe_word("cayo") == g.transcribe_word("callo")


@pytest.mark.parametrize("code", MERGED)
def test_y_outside_onset_stays_vocalic(code):
    g = G2P(code)
    assert g.transcribe("y") == "i"
    assert g.transcribe_word("hoy").endswith("i")


@pytest.mark.parametrize("code", ["es-AR-x-litoral", "es-AR-x-norte"])
def test_northern_argentina_keeps_the_lateral(code):
    g = G2P(code)
    assert g.transcribe_word("calle") == "ˈkaʎe"
    assert g.transcribe_word("cayo") == "ˈkaʝo"
