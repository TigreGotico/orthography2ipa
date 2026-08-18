"""The stress mark is written at the stressed syllable's true onset.

``apply_stress_mark`` divides the transcription itself to find where the
stressed syllable begins. A vowel-group split alone hands every medial
consonant forward to the following nucleus, so the mark landed inside
clusters no language opens a syllable with — ⟨cantar⟩ came out ka-ˈntaɾ,
claiming an /nt/ onset. TTS training consumes this mark position, so a
mark inside the onset teaches the wrong boundary.
"""
import pytest

from orthography2ipa import G2P
from orthography2ipa.stress import apply_stress_mark, syllabify_for_mark


@pytest.mark.parametrize("lang,word,expected", [
    # A medial cluster that is no onset closes the preceding syllable.
    ("es-ES", "cantar", "kanˈtaɾ"),
    ("es-ES", "montaña", "monˈtaɲa"),
    ("oc", "montanha", "munˈtaɲɔ"),
    ("tet", "kintál", "kinˈtaːl"),
    ("it-IT", "Abbondanza", "abːonˈdantsa"),
    ("pl", "Abchaza", "apˈxaza"),
    # A geminate is heterosyllabic: its halves belong to different syllables.
    ("it-IT", "Abbagnale", "abːaɲˈɲale"),
    # A licit complex onset stays whole and keeps the mark before it.
    ("pt-PT", "cabra", "ˈkabɾɐ"),
    ("es-ES", "Alfredo", "alˈfɾeðo"),
    # A rise onto a glide is an onset: the mark stays before the whole cluster.
    ("es-ES", "Oviedo", "oˈβjeðo"),
    ("es-ES", "cambiar", "kamˈbjaɾ"),
    ("pt-PT", "mulher", "muˈʎɛɾ"),
    # The velar nasal opens no syllable, so it closes the one before it.
    ("id", "Angola", "aŋˈola"),
])
def test_mark_sits_at_the_onset(lang, word, expected):
    assert G2P(lang).transcribe_word(word) == expected


@pytest.mark.parametrize("lang,word,expected", [
    # A written accent names the stressed vowel; the mark stays on it.
    ("ca", "Califòrnia", "kəliˈfɔrniə"),
    ("pt-PT", "saúde", "sɐˈudɨ"),
    ("pt-PT", "família", "fɐˈmiliɐ"),
    ("es-ES", "Alcorcón", "alkoɾˈkon"),
])
def test_marked_vowel_is_the_accented_one(lang, word, expected):
    assert G2P(lang).transcribe_word(word) == expected


@pytest.mark.parametrize("lang,word,expected", [
    # A two-symbol affricate is ONE consonant, and a syllable boundary drawn
    # inside it would cut a phoneme in half — including when the stop is
    # lengthened and when it is ejective, aspirated or palatalized. Where the
    # boundary lands around it is a separate question; that it never lands
    # INSIDE it is what these pin.
    ("pl", "Adżaria", "aˈdʐarja"),
    ("it-IT", "Acceglio", "aˈtːʃeʎʎo"),
    ("bbl", "არწივ", "arˈtsʼiv"),
    ("bbl", "ცაცხო", "tsʰatsʰˈxɔ"),
    ("ru-x-northern", "Авиценна", "avʲɪˈtsʲenna"),
    # …but a geminate stop is two consonants and does divide.
    ("bbl", "ატტაჼ", "atʼˈtʼa"),
])
def test_the_mark_never_splits_an_affricate(lang, word, expected):
    assert G2P(lang).transcribe_word(word) == expected


@pytest.mark.parametrize("lang,word,expected", [
    # Greek opens words with clusters no sonority shape licenses (κτίριο,
    # πτώση, σμήνος) and declares no inventory, so it turns the judgement off
    # and the mark falls where the vowel groups put it.
    ("el", "χαρακτήρας", "xaɾaˈktiɾas"),
    # Khmer subscript consonants are onsets on the same grounds.
    ("km", "កម្រង", "kɑˈmrɔːŋ"),
    # Ibero-Romance declares its inventory, which has no /s/ + stop onset —
    # the shape the sibilant appendix would otherwise license for everyone.
    ("es-ES", "castigo", "kasˈtiɣo"),
    ("es-ES", "España", "esˈpaɲa"),
    ("ca", "castigo", "kəsˈtiɣu"),
    ("pt-PT", "castigo", "kɐʃˈtiɡu"),
])
def test_the_spec_decides_its_own_onsets(lang, word, expected):
    assert G2P(lang).transcribe_word(word) == expected


def test_a_rise_onto_a_glide_is_an_onset():
    """Judge-internal: the shape set the orthographic judge uses refuses an
    obstruent + /j/ onset, on continental Germanic evidence that is a MORPHEME
    boundary. A transcription shows no boundary, so the IPA judge licenses
    every rise onto a glide — which is what keeps ⟨Oviedo⟩ o-ˈβjeðo rather
    than oβ-ˈjeðo. Pinned against the judge because the whole judge is new:
    there is no earlier behaviour for it to differ from.
    """
    from orthography2ipa.stress import _IpaOnsetJudge, _OnsetJudge
    judge = _IpaOnsetJudge()
    for onset in ("βj", "tj", "fj", "ɾw", "hw", "bj"):
        assert judge.licit(onset), onset
    # a fall onto a glide is still no onset, and neither is a fall generally
    assert not judge.licit("jβ")
    assert not judge.licit("nt")
    assert _OnsetJudge._two_member is not _IpaOnsetJudge._two_member


def test_division_keeps_the_longest_licit_onset():
    rules = G2P("es-ES").spec.stress
    assert syllabify_for_mark("kantaɾ", rules) == ["kan", "taɾ"]
    assert syllabify_for_mark("alfɾeðo", rules) == ["al", "fɾe", "ðo"]
    assert syllabify_for_mark("oβjeðo", rules) == ["o", "βje", "ðo"]


def test_caller_supplied_division_wins():
    """A quantity-sensitive caller has already divided the transcription —
    that division is what its weights were read off — and it is used as given,
    never re-derived."""
    rules = G2P("es-ES").spec.stress
    assert apply_stress_mark(
        "kantaɾ", rules, -1, ipa_syllables=["ka", "ntaɾ"]) == "kaˈntaɾ"
