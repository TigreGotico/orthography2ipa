"""Cited-rule tests for the three tone-writing Latin/Roman orthographies
whose specs were rebuilt from their published sources: Tewa (``tew``,
Martinez 1982 orthography with Sutton 2014 values), Lolopo / Yao'an Central
Yi (``ycl``, the Merrifield ``Loxrlavu`` orthography) and Namuyi Khatho
(``nmy``, the Pavlik 2017 / Li 2017 orthography).

Every test pins ONE claim the spec makes with a citation.

Read the scope of that honestly: MOST of the assertions below use words that
ARE in the WikiPron gold row the spec is scored against, so they pin the
spec's behaviour but cannot independently corroborate it.  Exactly ONE block
is held out -- ``MERRIFIELD_TABLE_3``, the five Lolopo example words printed
in Merrifield (2010) Table 3, none of which occurs in the ycl gold.  Those
five are the only assertions here that validate the rules against the
grammar rather than against the benchmark.

Counter-cases are included on purpose: a rule that fires everywhere is not a
rule.  ``ha`` must NOT nasalise where ``hi`` does, ``sah`` must NOT lose its
``h`` where ``seh`` does, and ``ddoleixr`` must NOT read its ``l`` as a tone
letter where ``anol`` does.
"""

import unicodedata as U

import pytest

from orthography2ipa.g2p import G2P


def ipa(code, word):
    """Transcribe *word*, dropping tie bars (notation, not phonology) and
    normalising to NFC so the expectations below can be written with
    ordinary precomposed characters."""
    out = G2P(code).transcribe_word(U.normalize("NFC", word))
    return U.normalize("NFC", out.replace("͡", ""))


# ---------------------------------------------------------------------------
# tew -- Rio Grande Tewa, Martinez (1982) orthography, Sutton (2014) values
# ---------------------------------------------------------------------------

def test_tew_ph_th_kh_are_fricatives_not_aspirates():
    """Sutton (2014): the Martinez digraphs are the FRICATIVES /f th x/.
    A naive Latin reading gives aspirated stops and is wrong."""
    assert ipa("tew", "pho") == "fò"
    assert ipa("tew", "thaa") == "θɑ̀ː"
    assert ipa("tew", "khowa") == "xòwɑ̀"


def test_tew_ay_and_ee_are_long_monophthongs():
    """The long-vowel digraphs are not the sum of their letters: <ay> is
    /e:/ and <ee> is /i:/ (Sutton 2014; Module:tew-IPA long_pairs)."""
    assert ipa("tew", "bay") == "bèː"
    assert ipa("tew", "dee") == "dìː"


def test_tew_ay_before_a_vowel_is_not_the_digraph():
    """COUNTER-CASE.  <ay> spells /e:/ only in a closed or final syllable;
    before a vowel the <y> is the next syllable's onset glide, so <khayeh>
    is [x\u0251\u0300j\u00ea] and not *[xe\u02d0...]."""
    assert ipa("tew", "khayêh") == "xɑ̀jê"


def test_tew_tone_diacritics_are_mapped():
    """Unmarked = low, acute = high, circumflex = falling (Sutton 2014)."""
    assert ipa("tew", "ko") == "kò"
    assert ipa("tew", "pó") == "pó"
    assert ipa("tew", "tây") == "têː"


def test_tew_word_initial_vowel_takes_epenthetic_glottal_stop():
    assert ipa("tew", "odo") == "ʔòdò"


def test_tew_coda_nasal_is_velar():
    """<m n n~> not followed by a vowel is /ŋ/ (Sutton 2014)."""
    assert ipa("tew", "kan") == "kɑ̀ŋ"
    assert ipa("tew", "kindi") == "kìŋdì"


def test_tew_final_h_is_silent_only_after_an_e_nucleus():
    """<teh> is [t\u00e8] -- and the counter-case: the rule is written for the
    <eh> rimes, so an <h> after another nucleus is still /h/."""
    assert ipa("tew", "teh") == "tè"
    assert ipa("tew", "sah") == "sɑ̀h"


def test_tew_nasal_vowels_are_written_and_mapped():
    """The Martinez orthography writes nasalisation with U+0327 under the
    vowel; it maps to /~/ on the vowel (Module:tew-IPA is_nasal_marks)."""
    assert ipa("tew", "a̧") == "ʔɑ̃̀"


def test_tew_lenition_is_recorded_but_not_applied():
    """Sutton's postlexical /b d g/ -> [v r g] lenitions are in the
    ``allophones`` map only: the transcriptions modelled are phonemic."""
    from orthography2ipa import get
    spec = get("tew")
    assert "v" in spec.allophones["b"]
    assert ipa("tew", "hada") == "hɑ̀dɑ̀"


# ---------------------------------------------------------------------------
# ycl -- Lolopo
#
# HELD OUT: the MERRIFIELD_TABLE_3 block immediately below, and only that
# block.  Every other assertion in this file (ycl, tew and nmy alike) uses a
# word that is also in the gold row.
# ---------------------------------------------------------------------------

#: Merrifield (2010) Table 3, "Lolo Syllable Structure".  The table's
#: ⟨ba⟩ row is omitted: it prints the phonetic form as [ba³³], which
#: contradicts Table 5 (⟨b⟩ = /p/, ⟨bb⟩ = /b/) and the ⟨bei⟩ = [pe³³] row
#: of the very same table.  Table 5 is the explicit statement, so the
#: internally inconsistent row is not used as a test oracle.
MERRIFIELD_TABLE_3 = [
    ("bei", "pe³³"),          # 'run'
    ("almeir", "ʔa⁵⁵me²¹"),   # 'rice'
    ("ddei", "de³³"),         # 'possessive'
    ("ngo", "ŋo³³"),          # 'I, me'
    ("altor", "ʔa⁵⁵tʰo²¹"),   # 'knife, sword'
]


@pytest.mark.parametrize("word,expected", MERRIFIELD_TABLE_3)
def test_ycl_merrifield_table_3_syllable_structure(word, expected):
    """Merrifield (2010) Table 3 gives these orthography/phonetic
    pairs.  They are not in the benchmark gold, so they test the rules and
    not the fit."""
    assert ipa("ycl", word) == expected


def test_ycl_doubled_letters_are_the_voiced_series():
    """Merrifield (2010) Table 5: voiced stops and affricates are written
    double, voiceless unaspirated single, voiceless aspirated single."""
    assert ipa("ycl", "bbi") == "bi³³"
    assert ipa("ycl", "bi") == "pi³³"
    assert ipa("ycl", "pi") == "pʰi³³"


def test_ycl_tone_letters_l_and_r():
    """Merrifield (2010) 2.1.1: syllable-final <l> is high 55, <r> is low
    21, an unmarked syllable is mid 33."""
    assert ipa("ycl", "bol") == "po⁵⁵"
    assert ipa("ycl", "hor") == "xo²¹"
    assert ipa("ycl", "lo") == "ɮo³³"


def test_ycl_l_before_a_vowel_is_an_onset_not_a_tone_letter():
    """COUNTER-CASE for the tone-letter reading of <l>.  In <ddoleixr> the
    <l> is the second syllable's onset, so the first syllable keeps its
    unmarked mid tone 33."""
    assert ipa("ycl", "ddoleixr") == "do³³ɮe̠ʔ²¹"


def test_ycl_x_marks_the_tight_throat_register():
    """Merrifield (2010) 2.1.3: tense (tight-throat) vowels are written
    with <x>, which raises mid 33 to 44 and high 55 to 66 and adds a
    final glottal stop to low 21."""
    assert ipa("ycl", "hax") == "xa̠⁴⁴"
    assert ipa("ycl", "doxl") == "to̠⁶⁶"
    assert ipa("ycl", "baxr") == "pa̠ʔ²¹"


def test_ycl_xl_before_a_vowel_is_not_the_tense_high_digraph():
    """COUNTER-CASE.  <vixlux> is [vi\u0320\u2074\u2074\u026a\u0264\u0320\u2074\u2074]: the <l> is the
    next syllable's onset and only the <x> is the register letter."""
    assert ipa("ycl", "vixlux") == (
        "vi̠⁴⁴ɮɤ̠⁴⁴")


def test_ycl_high_vowel_apicalises_after_a_sibilant():
    """<si> is [sz\u0329\u00b3\u00b3] while <mi> keeps its /i/ -- the apical rule is
    conditioned, not global."""
    assert ipa("ycl", "si") == "sz̩³³"
    assert ipa("ycl", "mi") == "mi³³"


# ---------------------------------------------------------------------------
# nmy -- Namuyi Khatho, Pavlik (2017) / Li (2017) orthography
# ---------------------------------------------------------------------------

def test_nmy_retroflex_and_dental_series_are_distinct():
    """<c ch dzh sh zh> are retroflex, <ts tsh dz s z> dental."""
    assert ipa("nmy", "chā") == "tʂʰa˧˩"
    assert ipa("nmy", "tshà") == "tsʰa˥˧"


def test_nmy_tone_diacritics_are_mapped():
    """Wiktionary:Namuyi entry guidelines: unmarked ˧, <a`> ˥˧, <a-> ˧˩,
    <a^> ˥, <a'> ˧˥; <a(breve)> is Li's low toneme 21."""
    assert ipa("nmy", "bi") == "bi˧"
    assert ipa("nmy", "vù") == "vu˥˧"
    assert ipa("nmy", "dā") == "da˧˩"
    assert ipa("nmy", "mâ") == "ma˥"
    assert ipa("nmy", "mŭ") == "mu˨"


def test_nmy_t_palatalises_before_i_but_not_before_a():
    """Guidelines: Pavlik's <ky khy> are written <ty thy>, and <t th>
    before /i/.  COUNTER-CASE: <t\u00f4> keeps its dental /t/."""
    assert ipa("nmy", "tī") == "tɕi˧˩"
    assert ipa("nmy", "tô") == "to˥"


def test_nmy_h_is_nasalised_before_every_vowel_but_a():
    """COUNTER-CASE pair from the gold itself: <hi> is [\u0266~\u0129˧] but <ha>
    is plain [\u0266a˧]."""
    assert ipa("nmy", "hi").startswith("ɦ̃")
    assert ipa("nmy", "ha") == "ɦa˧"


def test_nmy_preinitial_nasal_takes_the_place_of_its_onset():
    """/ɴ/ before a uvular, /ŋ/ before a velar."""
    assert ipa("nmy", "nxrŏ") == "ɴχɔ˨"
    assert ipa("nmy", "nkhî") == "ŋkʰi˥"


def test_nmy_u_before_a_vowel_is_the_on_glide():
    """<luò> is [lwoË¥Ë§]: the tone rides on the following nucleus."""
    assert ipa("nmy", "luò") == "lwo˥˧"


def test_nmy_ih_is_back_after_a_retroflex_onset():
    """<sih> is [sɨ] but <shih> is [ʂɯ] -- conditioned, not global."""
    assert ipa("nmy", "sìh") == "sɨ˥˧"
    assert ipa("nmy", "shìh") == "ʂɯ˥˧"


def test_nmy_word_initial_vowel_takes_epenthetic_glottal_stop():
    assert ipa("nmy", "â").startswith("ʔ")


def test_nmy_vowel_nasalisation_is_an_acknowledged_gap():
    """The orthography does not write Namuyi's contrastive vowel
    nasalisation, and the spec says so rather than guessing it."""
    from orthography2ipa import get
    assert "nasalisation" in get("nmy").notes.lower()
    assert "̃" not in ipa("nmy", "nga")
