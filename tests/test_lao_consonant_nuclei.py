"""A bare Lao ⟨ວ⟩ between an unvowelled onset and a closing consonant is the nucleus.

The expected strings are the Kaikki Lao gold (``pʰ uː ə̯ k̚`` for ⟨ພວກ⟩) with the
gold's offglide mark ⟨ə̯⟩ written ⟨ə⟩, which is how this spec already writes
the vowel ⟨ົວ⟩ /uːə/. Tone letters are not part of the comparison. ⟨ກວດ⟩ is not a gold row: its
value composes the onset ⟨ກ⟩ /k/ and the coda ⟨ດ⟩ /t̚/ with the same nucleus.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest  # noqa: E402

from orthography2ipa import G2P  # noqa: E402


@pytest.fixture(scope="module")
def lo():
    return G2P("lo")


@pytest.mark.parametrize("word, expected", [
    ("ພວກ", "pʰuːək̚"),
    ("ກວດ", "kuːət̚"),
    ("ຫລວງ", "luːəŋ"),
    ("ຂວດ", "kʰuːət̚"),
    ("ມວຍ", "muːəj"),
    ("ສວນ", "suːən"),
    ("ນວດ", "nuːət̚"),
])
def test_bare_wo_between_consonants_is_the_nucleus(lo, word, expected):
    assert lo.transcribe_word(word) == expected


@pytest.mark.xfail(
    strict=True,
    reason="a key ending in the combining semivowel sign is read as a bare "
           "mark, so the letter after ⟨ຫຼ⟩ is not tested for a nucleus")
@pytest.mark.parametrize("word, expected", [
    ("ຫຼວງ", "luːəŋ"),
    ("ທາງຫຼວງ", "tʰaːŋluːəŋ"),
])
def test_wo_after_ho_nam_with_subscript_lo_is_the_nucleus(lo, word, expected):
    assert lo.transcribe_word(word) == expected


@pytest.mark.parametrize("word, expected", [
    ("ວັນ", "ʋan"),
    ("ແຫວນ", "ʋɛːn"),
    ("ສະແຫວງ", "saʔʋɛːŋ"),
])
def test_wo_that_is_an_onset_or_has_its_own_vowel_is_unchanged(lo, word, expected):
    assert lo.transcribe_word(word) == expected

