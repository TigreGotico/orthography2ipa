"""Regression test for scripts/benchmark.py's _expand_consonant_length()
missing decomposed diacritic-marked consonants before a length mark.

A diacritic-marked consonant preceding [ː] is not always a single
codepoint: dental [n̪] has no precomposed Unicode form, so it is written
as base [n] + combining bridge below (U+032A). Scanning the raw string
one codepoint at a time only looks at the codepoint immediately before
[ː] — for [n̪ː] that is the combining mark, not [n] — so the doubling
duplicates the diacritic and drops the base letter entirely
([n̪ː] -> [n̪̪] instead of the correct [n̪n̪]).
"""
import os
import sys
import unicodedata

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from benchmark import _expand_consonant_length  # noqa: E402


def test_decomposed_dental_consonant_length_doubles_whole_cluster():
    s = "n" + "̪" + "ː"  # n + combining bridge below + length mark
    result = _expand_consonant_length(s)
    expected = unicodedata.normalize("NFC", "n̪" + "n̪")
    assert unicodedata.normalize("NFC", result) == expected
    # the base letter must survive — it must not vanish, leaving only the
    # doubled diacritic behind.
    assert "n" in result


def test_precomposed_retroflex_consonant_length_still_works():
    # ṇ (LATIN SMALL LETTER N WITH DOT BELOW, a single precomposed
    # codepoint) already worked before the fix — must keep working.
    s = "ṇ" + "ː"
    result = _expand_consonant_length(s)
    assert unicodedata.normalize("NFC", result) == unicodedata.normalize(
        "NFC", "ṇṇ")


def test_plain_geminate_and_affricate_still_expand():
    assert _expand_consonant_length("lː") == "ll"
    assert _expand_consonant_length("tʃː") == "ttʃ"


def test_vowel_length_left_untouched():
    assert _expand_consonant_length("aː") == "aː"


def test_marked_vowel_length_left_untouched():
    # ɛ̌ (ɛ + combining caron, U+030C) followed by a length mark. The old
    # codepoint-at-a-time scan checked only the caron against
    # is_ipa_vowel() -- a diacritic is never a vowel letter -- so it
    # treated the cluster as a consonant and doubled the diacritic onto
    # itself: [ɛ̌ː] -> [ɛ̌̌], destroying the vowel. The walk-back must
    # instead resolve the whole cluster's base letter (ɛ, a vowel) and
    # leave marked vowel length untouched, same as plain [aː].
    s = "ɛ" + "̌" + "ː"  # ɛ + combining caron + length mark
    result = _expand_consonant_length(s)
    assert unicodedata.normalize("NFC", result) == unicodedata.normalize(
        "NFC", "ɛ̌ː")


def test_already_doubled_length_mark_triples_the_consonant():
    # A length mark that is itself already doubled is not deduplicated:
    # each [ː] seen doubles the preceding consonant again, so [lːː]
    # expands to [lll], not [ll].
    assert _expand_consonant_length("lːː") == "lll"
