"""Spanish /b d ɡ/ are fricatives everywhere except after a pause and a nasal.

Navarro Tomás 1918, Manual de pronunciación española:

- § 82 p. 63: "Se pronuncia, pues, fricativa toda b que no se halle en
  posición inicial absoluta ni precedida de m o n." Examples on pp. 63-64:
  la boca, pobreza, abrigo, arboleda, estorbo, alba, esbelto, el bollo,
  las bocas, por bailar.
- § 101 p. 75: the stop [d] occurs "cuando va en posición inicial absoluta o
  en contacto con una n o l precedentes. … En todo otro caso la d ortográfica
  toma el sonido đ". Stops: falda, toldo, conde, mundo, un día, el domingo.
  Fricatives (§ 102 pp. 76-77): madre, piedra, cuadro, perdón, tu dinero,
  lo dicho.
- § 128 p. 108: the stop [ɡ] occurs in absolute initial position and after a
  nasal (tengo, un grado). § 129 p. 109: "Resulta, pues, normalmente fricativa
  toda g ortográfica … que en la pronunciación no se halle inicial absoluta ni
  precedida de n": cargo, colgar, siglo, alegre, rasguño.

Michnowicz 2012, p. 107, for Yucatán: "in YS /b d g/ are produced as stops in
contexts where standard varieties of Spanish would employ fricative or
approximant variants, such as intervocalically".
"""
import pytest

from orthography2ipa.g2p import G2P


@pytest.mark.parametrize("word,expected", [
    # b after a consonant other than a nasal, and before a consonant
    ("alba", "ˈalβa"),
    ("arboleda", "aɾβoˈleða"),
    ("estorbo", "esˈtoɾβo"),
    ("pobreza", "poˈβɾeθa"),
    ("abrigo", "aˈβɾiɣo"),
    ("cabra", "ˈkaβɾa"),
    ("barba", "ˈbaɾβa"),
    ("árbol", "ˈaɾβol"),
    # d after a consonant other than a nasal or l, and before a consonant
    ("madre", "ˈmaðɾe"),
    ("piedra", "ˈpjeðɾa"),
    ("cuadro", "ˈkwaðɾo"),
    ("perdón", "peɾˈðon"),
    ("verde", "ˈbeɾðe"),
    # g after a consonant other than a nasal, and before a consonant
    ("cargo", "ˈkaɾɣo"),
    ("colgar", "kolˈɣaɾ"),
    ("siglo", "ˈsiɣlo"),
    ("alegre", "aˈleɣɾe"),
    ("algo", "ˈalɣo"),
])
def test_word_internal_spirant(word, expected):
    assert G2P("es-ES").transcribe_word(word) == expected


@pytest.mark.parametrize("word,segment", [
    ("esbelto", "sβ"),
    ("desde", "sð"),
    ("rasguño", "sɣ"),
    ("vergüenza", "ɾɣw"),
])
def test_spirant_after_s_and_r(word, segment):
    assert segment in G2P("es-ES").transcribe_word(word).replace("ˈ", "")


@pytest.mark.parametrize("word,expected", [
    ("hombre", "ˈombɾe"),
    ("falda", "ˈfalda"),
    ("caldo", "ˈkaldo"),
    ("toldo", "ˈtoldo"),
    ("conde", "ˈkonde"),
    ("mundo", "ˈmundo"),
    ("tengo", "ˈteŋɡo"),
])
def test_stop_after_nasal_and_d_after_l(word, expected):
    assert G2P("es-ES").transcribe_word(word) == expected


@pytest.mark.parametrize("phrase,expected", [
    ("la boca", "la ˈβoka"),
    ("su boda", "su ˈβoða"),
    ("las bocas", "las ˈβokas"),
    ("tu dinero", "tu ðiˈneɾo"),
    ("lo dicho", "lo ˈðitʃo"),
    ("la guerra", "la ˈɣera"),
])
def test_cross_word_spirant(phrase, expected):
    assert G2P("es-ES").transcribe(phrase) == expected


@pytest.mark.parametrize("phrase,expected", [
    ("un día", "un ˈdia"),
    ("el domingo", "el doˈmiŋɡo"),
    ("un grado", "uŋ ˈɡɾaðo"),
    ("con gusto", "koŋ ˈɡusto"),
])
def test_cross_word_stop_after_nasal_and_d_after_l(phrase, expected):
    assert G2P("es-ES").transcribe(phrase) == expected


def test_pause_keeps_the_initial_stop():
    out = G2P("es-ES").transcribe("la casa. Bueno, vamos")
    assert out.split()[-2:] == ["ˈbweno", "ˈbamos"], out


def test_es_419_inherits_the_rule():
    assert G2P("es-419").transcribe("cuando vas a viajar") == "ˈkwando ˈβas a βjaˈxaɾ"


@pytest.mark.parametrize("text,expected", [
    ("cabra", "ˈkabɾa"),
    ("lobo", "ˈlobo"),
    ("la boca", "la ˈboka"),
    ("los dedos", "los ˈdedos"),
])
def test_yucatan_keeps_the_occlusives(text, expected):
    assert G2P("es-MX-x-yucatan").transcribe(text) == expected
