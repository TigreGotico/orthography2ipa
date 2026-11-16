"""Word-final /n/ is the velar [ŋ] where velarization is the rule.

Lipski, "Geographical and Social Varieties of Spanish: An Overview", p. 7:
"Velarization of phrase-final /n/ is the rule in Galicia and parts of
Asturias, Extremadura, Andalusia, the Canary Islands, all Caribbean and Central
American dialects, along the Pacific coast of Colombia, Peru, and Ecuador, and
sporadically in the Andean highlands. Word-final prevocalic nasals are
typically also velarized in these dialects, although with generally lower
rates than for phrase-final /n/ (Lipski 1986): un otro [uŋ.ˈo.tɾo]".

The Caribbean region of the same overview (p. 3, list (2)) includes the
Caribbean coast of Venezuela, where Maracaibo lies.
"""
import pytest

from orthography2ipa.g2p import G2P

VELARIZING = ["es-CO-x-pacifico", "es-EC-x-costa", "es-PE-x-lima", "es-HN",
              "es-SV", "es-GT", "es-CR", "es-ES-x-canarias",
              "es-VE-x-zulia"]


@pytest.mark.parametrize("code", VELARIZING)
def test_phrase_final_n_is_velar(code):
    assert G2P(code).transcribe("pan") == "ˈpaŋ"


@pytest.mark.parametrize("code", VELARIZING)
def test_prevocalic_word_final_n_is_velar(code):
    assert G2P(code).transcribe("un otro") == "uŋ ˈotɾo"


@pytest.mark.parametrize("code", VELARIZING)
def test_word_internal_n_before_vowel_stays_alveolar(code):
    out = G2P(code).transcribe_word("mano")
    assert out == "ˈmano", out


# Varieties the source does not name keep the alveolar nasal.
@pytest.mark.parametrize("code", ["es-ES", "es-CO", "es-MX", "es-AR"])
def test_non_velarizing_varieties_keep_n(code):
    assert G2P(code).transcribe("pan") == "ˈpan"


# Before a consonant of the next word the nasal takes that consonant's place.
# Lipski (1986, pp. 146-147): word-final preconsonantal /n/ follows "the normal
# process of homorganic assimilation of nasal consonants to following
# obstruents". Navarro Tomás (1918, § 87, p. 66): "la n final de una palabra
# anterior se pronuncia también m" before p and b: un buen baile [um bwem
# baile], en pie [em pjé].
@pytest.mark.parametrize("code", VELARIZING)
@pytest.mark.parametrize("text, expected", [
    ("un peso", "um ˈpeso"),
    ("en pie", "em ˈpje"),
    ("un buen baile", "um ˈbwem ˈbai̯le"),
    ("en la casa", "en la ˈkasa"),
    ("en chile", "en ˈtʃile"),
    ("un gato", "uŋ ˈɡato"),
])
def test_word_final_n_before_a_consonant_takes_its_place(code, text, expected):
    assert G2P(code).transcribe(text) == expected


@pytest.mark.parametrize("code", VELARIZING)
def test_word_final_n_before_a_pause_stays_velar(code):
    assert G2P(code).transcribe("tren. Pero") == "ˈtɾeŋ ˈpeɾo"
