"""Cited-rule tests for Eonavian (``gl-x-eonavia``).

Each test asserts one statement of the *Normas ortográficas del eonaviego*
(Academia de la Llingua Asturiana, Secretaría Llingüística del Navia-Eo,
3rd edition, 2025), on the example words the norms themselves give. The
section and printed page of each statement are in the spec's ``notes``.
"""

import pytest

from orthography2ipa.g2p import G2P

LANG = "gl-x-eonavia"


def ipa(word: str) -> str:
    return G2P(LANG).transcribe_word(word)


def bare(word: str) -> str:
    return ipa(word).replace("ˈ", "")


# ═══════════════════════════════════════════════════════════════════════════
# ⟨y⟩ = /ʝ/ — §1.1 (p. 15), §1.2.5 (p. 16)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("word,expected", [
    ("coyer", "koˈʝeɾ"),
    ("muyer", "muˈʝeɾ"),
    ("yelso", "ˈʝelso"),
    ("mayo", "ˈmaʝo"),
    ("paya", "ˈpaʝa"),
    ("oyo", "ˈoʝo"),
    ("coye", "ˈkoʝe"),
    ("díxoye", "ˈdiʃoʝe"),
])
def test_eonavian_y_is_a_palatal_fricative_onset(word, expected):
    """§1.2.5: "El fonema /ʝ/ represéntase por y". The letter opens a
    syllable, so an unaccented word in a vowel keeps paroxytone stress
    (§1.5.1): mayo is ma-yo, not one syllable with a vowel ⟨y⟩."""
    assert ipa(word) == expected


def test_eonavian_y_and_ll_stay_apart():
    """Note 1 to §1.2.5: a native speaker of the palatalising zone says
    coyello "estremando ben os dous sonidos", so /ʝ/ and /ʎ/ do not merge."""
    assert ipa("coyello") == "koˈʝeʎo"


def test_eonavian_conjunction_y_is_a_vowel():
    """§1.1 gives ⟨y⟩ the second value /i/, and §1.3.2 names the one word
    that uses it: the conjunction y."""
    assert bare("y") == "i"


# ═══════════════════════════════════════════════════════════════════════════
# ⟨j⟩ = /χ/ in unadapted loans — §1.2.6 (p. 17)
# ═══════════════════════════════════════════════════════════════════════════

def test_eonavian_j_in_a_loan_is_uvular():
    """§1.2.6: "El fonema /χ/ (grafiao como j) nun é propio del noso sistema
    llingüístico". The letter occurs only in a loan such as Castilian jefe,
    and it is read, not dropped."""
    assert bare("jefe") == "χefe"


# ═══════════════════════════════════════════════════════════════════════════
# Accented falling diphthongs — §1.3.2 (p. 17), §1.5.2 (p. 20)
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("word,expected", [
    ("penséi", "penˈsej"),
    ("cantái", "kanˈtaj"),
    ("cantéi", "kanˈtej"),
    ("calzóis", "kalˈθojs"),
    ("baxóu", "baˈʃow"),
    ("cantóu", "kanˈtow"),
    ("metéu", "meˈtew"),
    ("caráuter", "kaˈɾawteɾ"),
    ("chegóuye", "tʃeˈɣowʝe"),
])
def test_eonavian_accented_falling_diphthong_keeps_its_glide(word, expected):
    """§1.5.2 accents a diphthong on its more open vowel by the §1.5.1 stress
    rules (calzóis, baxóu, cantéi, caráuter), and §1.3.2 names penséi and
    cantái as diphthongs: the second letter is the glide. The vowel quality
    is that of the unaccented ⟨ei ou oi⟩, because §1.5.4.2 gives the accent a
    timbre value only in a few word pairs."""
    assert ipa(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("óso", "ˈɔso"),
    ("oso", "ˈoso"),
    ("pé", "ˈpɛ"),
    ("pe", "ˈpe"),
    ("coyémos", "koˈʝɛmos"),
    ("coyemos", "koˈʝemos"),
])
def test_eonavian_diacritic_accent_still_marks_the_open_vowel(word, expected):
    """Counter-case: in the pairs of §1.5.4.2 (p. 21) and in the P4 perfect
    coyémos, the accent does mark the open vowel /ɛ, ɔ/. The diphthong keys
    must not take that value away from a single accented vowel."""
    assert ipa(word) == expected
