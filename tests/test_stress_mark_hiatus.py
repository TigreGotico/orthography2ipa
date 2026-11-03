"""A written hiatus is two syllables, and the stress mark finds the right one.

The RAE/ASALE Ortografía (2010) counts two vowels in contact as one syllable
only when they form a diphthong: "se consideran siempre diptongos a efectos
ortográficos las combinaciones de vocal abierta (/a/, /e/, /o/) seguida o
precedida de vocal cerrada átona (/i/, /u/) [...] y de dos vocales cerradas
distintas" (p. 235). Every other pair is a hiatus: two equal vowels (leer),
two open vowels (tea-tro), and an open vowel next to a stressed closed one,
which always takes the accent (país, reír, prohíben, vehículo; Ort. 1999,
p. 46). A silent ⟨h⟩ between the vowels changes nothing: "Las palabras que
tienen h muda intercalada se separan como si dicha letra no existiera:
al- / cohol, [...] prohi- / bir". The passages are quoted from the summary
in papers/iberian/rae_ortografia_2010_nueva.pdf, pp. JMIM-8 and JMIM-16.

The stressed syllable then follows the accentuation rules (Navarro Tomás,
Manual de pronunciación española, §§ 155-156): the written accent wins;
without one a word "terminada en vocal o en las consonantes n, s" is llana,
and a word "terminada en cualquier consonante que no sea n ni s" is aguda.

The transcription cannot see the accent or the silent letter: ⟨país⟩ is
[pais] and ⟨ahorrábamos⟩ is [aoraβamos]. Each expected value below is
written by hand: the syllables and the stress follow the rules above (the
comment gives the written syllables, the stressed one in capitals), and the
segments follow the Castilian values the spec cites.
"""
from __future__ import annotations

import pytest

from orthography2ipa import G2P, get


def _ipa(lang: str, word: str) -> str:
    return G2P(lang).transcribe_word(word)


# Castilian segments, from the same sources the spec cites: ⟨c z⟩ before a
# front vowel /θ/, ⟨b v d g⟩ between continuants [β ð ɣ], a single ⟨r⟩
# between vowels [ɾ], ⟨rr⟩ and initial ⟨r⟩ [r], ⟨j⟩ /x/, ⟨h⟩ silent, a falling
# diphthong with [i̯ u̯] and a rising one with [j w].
SILENT_H_HIATUS = [
    ("ahorrábamos", "aoˈraβamos"),    # a-ho-RRÁ-ba-mos
    ("ahí", "aˈi"),                   # a-HÍ
    ("ahínco", "aˈinko"),             # a-HÍN-co
    ("prohíbe", "pɾoˈiβe"),           # pro-HÍ-be
    ("rehúso", "reˈuso"),             # re-HÚ-so
    ("vahído", "baˈiðo"),             # va-HÍ-do
    ("vehículo", "beˈikulo"),         # ve-HÍ-cu-lo
    ("retahíla", "retaˈila"),         # re-ta-HÍ-la
    ("alcohol", "alkoˈol"),           # al-co-HOL
    ("zanahoria", "θanaˈoɾja"),       # za-na-HO-ria
    ("cohete", "koˈete"),             # co-HE-te
    ("ahora", "aˈoɾa"),               # a-HO-ra
    ("almohada", "almoˈaða"),         # al-mo-HA-da
]

PLAIN_HIATUS = [
    ("paseo", "paˈseo"),              # pa-SE-o
    ("correo", "koˈreo"),             # co-RRE-o
    ("leer", "leˈeɾ"),                # le-ER
    ("creer", "kɾeˈeɾ"),              # cre-ER
    ("maíz", "maˈiθ"),                # ma-ÍZ
    ("país", "paˈis"),                # pa-ÍS
    ("reúne", "reˈune"),              # re-Ú-ne
    ("reír", "reˈiɾ"),                # re-ÍR
    ("oír", "oˈiɾ"),                  # o-ÍR
    ("poeta", "poˈeta"),              # po-E-ta
    ("teatro", "teˈatɾo"),            # te-A-tro
    ("cacao", "kaˈkao"),              # ca-CA-o
    ("aéreo", "aˈeɾeo"),              # a-É-re-o
    ("museo", "muˈseo"),              # mu-SE-o
    ("oeste", "oˈeste"),              # o-ES-te
]


@pytest.mark.parametrize("word,expected", SILENT_H_HIATUS)
def test_es_hiatus_across_a_silent_h(word, expected):
    assert _ipa("es-ES", word) == expected


@pytest.mark.parametrize("word,expected", PLAIN_HIATUS)
def test_es_plain_hiatus(word, expected):
    assert _ipa("es-ES", word) == expected


# Seseo: the American varieties read ⟨c z⟩ before a front vowel as /s/,
# which none of these words contains.
@pytest.mark.parametrize("lang", ["es-419", "es-AR", "es-MX"])
@pytest.mark.parametrize("word,expected", [
    ("ahorrábamos", "aoˈraβamos"),
    ("paseo", "paˈseo"),
    ("país", "paˈis"),
])
def test_es_varieties_inherit_the_hiatus(lang, word, expected):
    assert _ipa(lang, word) == expected


# Diphthongs and words without a vowel sequence. Each one is right before the
# change and must stay right. ⟨desahucio⟩ and ⟨ahumar⟩ keep the diphthong
# across the silent ⟨h⟩ (de-SAHU-cio, ahu-MAR). ⟨día⟩ ⟨búho⟩ ⟨actúa⟩ are a
# hiatus whose stress falls on the first vowel.
CONTROL = [
    ("baile", "ˈbai̯le"),              # BAI-le
    ("causa", "ˈkau̯sa"),              # CAU-sa
    ("peine", "ˈpei̯ne"),              # PEI-ne
    ("ciudad", "θjuˈðað"),            # ciu-DAD
    ("cuidado", "kwiˈðaðo"),          # cui-DA-do
    ("canción", "kanˈθjon"),          # can-CIÓN
    ("huir", "ˈwiɾ"),                 # HUIR
    ("quiero", "ˈkjeɾo"),             # QUIE-ro
    ("guion", "ˈɡjon"),               # GUION
    ("desahucio", "deˈsauθjo"),       # de-SAHU-cio
    ("ahumar", "auˈmaɾ"),             # ahu-MAR
    ("día", "ˈdia"),                  # DÍ-a
    ("búho", "ˈbuo"),                 # BÚ-ho
    ("actúa", "akˈtua"),              # ac-TÚ-a
    ("continúo", "kontiˈnuo"),        # con-ti-NÚ-o
    ("casa", "ˈkasa"),                # CA-sa
    ("cantaban", "kanˈtaβan"),        # can-TA-ban
    ("teléfono", "teˈlefono"),        # te-LÉ-fo-no
    ("útil", "ˈutil"),                # Ú-til
    ("ahijaría", "aixaˈɾia"),         # ahi-ja-RÍ-a
    ("acequia", "aˈθekja"),           # a-CE-quia
]


@pytest.mark.parametrize("word,expected", CONTROL)
def test_es_control_words_keep_their_stress(word, expected):
    assert _ipa("es-ES", word) == expected


# Galician writes /ɡ k/ before ⟨e i⟩ as the digraphs ⟨gu qu⟩ (RAG/ILG,
# Normas ortográficas e morfolóxicas do idioma galego, 23rd ed., p. 14, the
# table of "dígrafos que representan un único fonema": "gu [...] [g]", "qu
# [...] [k]"; § 1.2-1.3, p. 17). Their ⟨u⟩ is no vowel, so ⟨guiaban⟩ is
# guia-ban, with the rising diphthong ⟨ia⟩ that § 3.2.5 (p. 33) keeps in one
# syllable (la-/bial, cien-/cia). A word that ends in a vowel, ⟨-n⟩ or ⟨-s⟩
# and carries no accent is grave (§ 2.3, p. 24: "non se acentúan as palabras
# graves rematadas en vogal, vogal + n, vogal + s").
@pytest.mark.parametrize("word,expected", [
    ("guiaban", "ˈɡjaβaŋ"),           # GUIA-ban
    ("guiados", "ˈɡjaðos"),           # GUIA-dos
    ("guiamos", "ˈɡjamos"),           # GUIA-mos
    ("esquiaban", "esˈkjaβaŋ"),       # es-QUIA-ban
    ("esquiadores", "eskjaˈðoɾes"),   # es-quia-DO-res
])
def test_gl_digraph_u_is_not_a_nucleus(word, expected):
    assert _ipa("gl-ES", word) == expected


def test_es_falling_diphthong_keeps_its_glide():
    # The non-syllabic [i̯] of a falling diphthong is not a second nucleus.
    assert G2P("es-ES").transcribe_word("baile") == "ˈbai̯le"


def test_es_declares_the_rae_diphthongs():
    diphthongs = set(get("es-ES").stress.diphthongs)
    assert {"ai", "ia", "ui", "iu", "uái", "üe"} <= diphthongs
    assert not {"ae", "ea", "ee", "aí", "ía", "úo"} & diphthongs
