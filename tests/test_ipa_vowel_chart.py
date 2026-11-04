"""Every vowel set that claims to be complete holds the whole IPA vowel chart.

The chart (International Phonetic Association, "The International Phonetic
Alphabet", revised to 2020, the Vowels quadrilateral) has 28 symbols. Read row
by row, front to back:

    close        i y   ɨ ʉ   ɯ u
    near-close   ɪ ʏ       ʊ
    close-mid    e ø   ɘ ɵ   ɤ o
    mid              ə
    open-mid     ɛ œ   ɜ ɞ   ʌ ɔ
    near-open    æ     ɐ
    open         a ɶ         ɑ ɒ

A symbol missing from a vowel set is read as a consonant: the scorer then
treats a long vowel as a long consonant and doubles it (``ʏː`` → ``ʏʏ``).
"""
import os
import sys

import pytest

from orthography2ipa.g2p import _VOWEL_IPA, _collapse_geminates
from orthography2ipa.phonetok import _NASAL_CARRIERS
from orthography2ipa.vowels import IPA_VOWEL_SYMBOLS, is_ipa_vowel

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from benchmark import _expand_consonant_length, normalize  # noqa: E402

CHART = ("i", "y", "ɨ", "ʉ", "ɯ", "u",
         "ɪ", "ʏ", "ʊ",
         "e", "ø", "ɘ", "ɵ", "ɤ", "o",
         "ə",
         "ɛ", "œ", "ɜ", "ɞ", "ʌ", "ɔ",
         "æ", "ɐ",
         "a", "ɶ", "ɑ", "ɒ")


def test_chart_has_28_distinct_symbols():
    assert len(set(CHART)) == 28


@pytest.mark.parametrize("vowel", CHART)
def test_is_ipa_vowel(vowel):
    assert is_ipa_vowel(vowel)
    assert vowel in IPA_VOWEL_SYMBOLS


@pytest.mark.parametrize("vowel", CHART)
def test_nasal_tilde_may_land_on_every_oral_vowel(vowel):
    assert vowel in _NASAL_CARRIERS


@pytest.mark.parametrize("vowel", CHART)
def test_doubled_vowel_never_collapses(vowel):
    assert vowel in _VOWEL_IPA
    assert _collapse_geminates(vowel + vowel) == vowel + vowel


def test_geminate_collapse_set_holds_only_vowels():
    assert _VOWEL_IPA == set(CHART)
    assert _collapse_geminates("ɓɓ") == "ɓ"


@pytest.mark.parametrize("vowel", CHART)
def test_scorer_keeps_vowel_length(vowel):
    assert _expand_consonant_length(vowel + "ː") == vowel + "ː"


def test_scorer_keeps_near_close_rounded_length_in_a_word():
    # A long [ʏː] survives normalisation; a long consonant still doubles.
    assert normalize("lʏːs", strip_stress=True, broad=True) == "lʏːs"
    assert normalize("lːʏs", strip_stress=True, broad=True) == "llʏs"
