"""Asturian letter values, allophones and stress against the ALLA references.

Every expected transcription is built by hand from two books of the Academia
de la Llingua Asturiana: the *Normes Ortográfiques* (8th revised ed., 2021)
for letter values and accent rules, and the *Gramática de la Llingua
Asturiana* (3rd ed., 2001) for the phonetic variants. The citation for each
value is in the rule or grapheme note of ``orthography2ipa/data/ast.json``;
the comment on each case names the paragraph it rests on.

A word transcribed alone stands after a pause and before one, so the
word-initial and word-final variants apply.
"""
import pytest

from orthography2ipa import G2P


@pytest.fixture(scope="module")
def engines():
    return {code: G2P(code)
            for code in ("ast", "ast-x-occidental", "ast-x-oriental")}


def _check(engines, code, word, expected):
    assert engines[code].transcribe(word) == expected


# Normes §1.1.3: the "ch vaqueira" ⟨ḷḷ⟩ / ⟨l.l⟩ is [ʎ] outside the west and
# one of [t̺s̺, t's, ʈʂ, ʈ, ɖ] in the west. Both spellings are one sound, so
# the dot of ⟨l.l⟩ does not split the word.
CH_VAQUEIRA = [
    ("ast", "ḷḷobu", "ˈʎoβu"),
    ("ast", "l.lobu", "ˈʎoβu"),
    ("ast", "coḷḷar", "koˈʎaɾ"),
    ("ast", "Ḷḷuarca", "ˈʎwaɾka"),
    ("ast", "L.luarca", "ˈʎwaɾka"),
    ("ast-x-oriental", "ḷḷobu", "ˈʎoβu"),
    ("ast-x-oriental", "l.lobu", "ˈʎoβu"),
    ("ast-x-occidental", "ḷḷobu", "ˈt͡soβu"),
    ("ast-x-occidental", "l.lobu", "ˈt͡soβu"),
]


@pytest.mark.parametrize("code,word,expected", CH_VAQUEIRA)
def test_ch_vaqueira(engines, code, word, expected):
    _check(engines, code, word, expected)


def test_ch_vaqueira_decomposed_input(engines):
    # ⟨l⟩ + U+0323 COMBINING DOT BELOW is the same letter as U+1E37.
    assert engines["ast"].transcribe("ḷḷobu") == "ˈʎoβu"


# Normes §1.2.1.2: ⟨y⟩ is the phoneme /i/ in the enclitic pronoun ⟨-y⟩ and the
# conjunction ⟨y⟩; elsewhere it is /y/ (Gramática III.1.7: affricate after a
# pause, fricative between vowels).
LETTER_Y = [
    ("ast", "y", "i"),
    ("ast", "dio-y pan", "ˈdjo i ˈpaŋ"),
    ("ast", "fála-y", "ˈfala i"),
    ("ast", "dá-yla", "ˈda ila"),
    ("ast", "díxo-yos", "ˈdiʃo ʝos"),
    ("ast", "yo", "ˈɟ͡ʝo"),
    ("ast", "mayu", "ˈmaʝu"),
    ("ast", "mayo", "ˈmaʝo"),
    ("ast", "pioyu", "ˈpjoʝu"),
    ("ast", "paya", "ˈpaʝa"),
    ("ast", "díxoye", "ˈdiʃoʝe"),
    ("ast-x-occidental", "mayu", "ˈmaʝu"),
    ("ast-x-oriental", "paya", "ˈpaʝa"),
    ("ast-x-oriental", "y", "i"),
    ("ast-x-occidental", "dio-y", "ˈdjo i"),
]


@pytest.mark.parametrize("code,word,expected", LETTER_Y)
def test_letter_y(engines, code, word, expected):
    _check(engines, code, word, expected)


# An apostrophe joins the elided word to its host: one phonological word.
# ⟨qu'⟩ before a vowel is /k/ (Gramática III.2.1).
ELISION = [
    ("ast", "l'agua", "ˈlaɣwa"),
    ("ast", "l’agua", "ˈlaɣwa"),
    ("ast", "d'Uviéu", "duˈβjeu̯"),
    ("ast", "qu'entamar", "kentaˈmaɾ"),
    ("ast", "qu'amburó", "kambuˈɾo"),
    ("ast", "lleva'l", "ˈʎeβal"),
]


@pytest.mark.parametrize("code,word,expected", ELISION)
def test_elision(engines, code, word, expected):
    _check(engines, code, word, expected)


# Normes §1.2: five vowel phonemes /a e i o u/. Glides per Gramática II.2;
# diphthongs and triphthongs per Normes §1.6.
VOWELS = [
    ("ast", "corazón", "koɾaˈθoŋ"),
    ("ast", "Xixón", "ʃiˈʃoŋ"),
    ("ast", "Xosé", "ʃoˈse"),
    ("ast", "Uviéu", "uˈβjeu̯"),
    ("ast", "mieu", "ˈmjeu̯"),
    ("ast", "fueu", "ˈfweu̯"),
    ("ast", "llueu", "ˈʎweu̯"),
    ("ast", "güei", "ˈɣwei̯"),
    ("ast", "rei", "ˈrei̯"),
    ("ast", "llei", "ˈʎei̯"),
    ("ast-x-oriental", "corazón", "koɾaˈθoŋ"),
]


@pytest.mark.parametrize("code,word,expected", VOWELS)
def test_vowels_and_glides(engines, code, word, expected):
    _check(engines, code, word, expected)


# Normes §1.9.1.1-§1.9.1.3: unaccented words ending in a vowel, -n or -s are
# paroxytone, others oxytone; a diphthong takes the accent on its open vowel;
# an accent on the closed vowel marks a hiatus.
STRESS = [
    ("ast", "falen", "ˈfaleŋ"),
    ("ast", "señardá", "seɲaɾˈða"),
    ("ast", "caxón", "kaˈʃoŋ"),
    ("ast", "Avilés", "aβiˈles"),
    ("ast", "cáncer", "ˈkanθeɾ"),
    ("ast", "llápiz", "ˈʎapiθ"),
    ("ast", "cámbaru", "ˈkambaɾu"),
    ("ast", "mercar", "meɾˈkaɾ"),
    ("ast", "Enol", "eˈnol"),
    ("ast", "Tiuya", "ˈtjuʝa"),
    ("ast", "téunicu", "ˈteu̯niku"),
    ("ast", "caráuter", "kaˈɾau̯teɾ"),
    ("ast", "maíz", "maˈiθ"),
    ("ast", "feúcu", "feˈuku"),
    ("ast", "partíu", "paɾˈtiu"),
    ("ast", "fiína", "fiˈina"),
    ("ast", "teatru", "teˈatɾu"),
    ("ast", "real", "reˈal"),
]


@pytest.mark.parametrize("code,word,expected", STRESS)
def test_stress(engines, code, word, expected):
    _check(engines, code, word, expected)


# Gramática III.1: spirants (b d g), nasal place, final [ŋ], voicing of
# /s θ ʃ/ before a voiced consonant, the strong r after l n s (also Normes
# §1.7.19.1 b).
CONSONANTS = [
    ("ast", "cebera", "θeˈβeɾa"),
    ("ast", "cabra", "ˈkaβɾa"),
    ("ast", "llombu", "ˈʎombu"),
    ("ast", "rueda", "ˈrweða"),
    ("ast", "desdexase", "dezðeˈʃase"),
    ("ast", "llargu", "ˈʎaɾɣu"),
    ("ast", "fungar", "fuŋˈɣaɾ"),
    ("ast", "guetar", "ɣeˈtaɾ"),
    ("ast", "enmarcar", "emmaɾˈkaɾ"),
    ("ast", "concu", "ˈkoŋku"),
    ("ast", "mesmu", "ˈmezmu"),
    ("ast", "pazguatu", "paðˈɣwatu"),
    ("ast", "pexdegatu", "peʒðeˈɣatu"),
    ("ast", "Israel", "izraˈel"),
    ("ast", "alredor", "alreˈðoɾ"),
    ("ast", "home", "ˈome"),
    ("ast", "quexase", "keˈʃase"),
    ("ast", "muyyer", "muˈkʲeɾ"),
    ("ast-x-oriental", "ḥoguera", "hoˈɣeɾa"),
]


@pytest.mark.parametrize("code,word,expected", CONSONANTS)
def test_consonants(engines, code, word, expected):
    _check(engines, code, word, expected)


# Western final -o closes to [u] only when unstressed (Normes §1.4 treats the
# alternation under the unstressed final vowels).
OCCIDENTAL_FINAL_O = [
    ("ast-x-occidental", "falo", "ˈfalu"),
    ("ast-x-occidental", "yo", "ˈɟ͡ʝo"),
    ("ast-x-occidental", "dio", "ˈdjo"),
]


@pytest.mark.parametrize("code,word,expected", OCCIDENTAL_FINAL_O)
def test_occidental_final_o(engines, code, word, expected):
    _check(engines, code, word, expected)
