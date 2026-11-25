"""The vowel test of vowels.py is phonematcher's ``is_vowel_phone``.

The first segment of a grapheme reading decides whether a letter such as
⟨y⟩ writes a nucleus. The segments below are the first segments of the
readings of every registered spec for which the vendored feature table said
"not a vowel" and phonematcher says "syllabic". Each is a vowel by the IPA
chart (a base vowel symbol under a diacritic or a tone mark) or a syllabic
consonant (a base consonant under a syllabicity mark). The oracle in
``_by_the_chart`` reads only the chart and the Unicode decomposition, so it
does not depend on either feature table.
"""
import unicodedata

import phonematcher
import pytest

from orthography2ipa import get
from orthography2ipa import vowels
from orthography2ipa.vowels import (
    IPA_VOWEL_SYMBOLS, SEMIVOWEL_MARGIN, SEMIVOWEL_NUCLEUS, SYLLABIC_MARKS,
    is_vowel_phone, place_class, semivowel_role,
)

FIRST_SEGMENTS = """
    a̘ a̟ a̤ a̰ e̘ e̝ e̞ e̠ e̤ i̘ i̠ i̤ l̩ m̩ n̩ o̘ o̝ o̞ o̠ o̤ o̰ r̩ u̘ u̠ v̩ à á â ã̀ ã́ ã̂ ã̄ ã̌
    ä æ̀ æ̂ æ̃̀ æ̃́ æ̃̂ æ̃̄ è é ê ì í î ò ó ô õ̀ õ̂ õ̌ ö̠ ù ú û ā ă ē ě ĩ̀ ĩ́ ĩ̂ ĩ̄ ĩ̌ ī ĭ ń̩ ŋ̍
    ō ũ̀ ũ̂ ũ̄ ũ̌ ū ŭ ǎ ǐ ǒ ǔ ǣ ǹ̩ ǽ ɑ̀ ɑ́ ɑ̂ ɑ̃̀ ɑ̃́ ɑ̃̂ ɑ̃̄ ɑ̄ ɑ̰ ɔ̀ ɔ́ ɔ̂ ɔ̃̀ ɔ̃́ ɔ̃̂ ɔ̃̄ ɔ̃̌
    ɔ̄ ɔ̌ ɔ̤ ɔ̰ ə̀ ə́ ə̂ ɚ ɛ̀ ɛ́ ɛ̂ ɛ̃̀ ɛ̃́ ɛ̃̂ ɛ̃̄ ɛ̃̌ ɛ̄ ɛ̌ ɛ̤ ɛ̰ ɤ̀ ɤ́ ɤ̄ ɤ̆ ɪ̀ ɪ́ ɪ̂ ɪ̃́ ɪ̞
    ɪ̰ ɵ̞ ɹ̩ ʊ̀ ʊ́ ʊ̂ ʊ̰ ʐ̩ ḁ ḛ ḭ ṍ ṳ ṵ ṷ ṹ ṽ̩ ẽ̀ ẽ́ ẽ̂ ẽ̄ ẽ̌ ị ụ ỹ
""".split()


def _by_the_chart(segment: str) -> bool:
    decomposed = unicodedata.normalize("NFD", segment)
    return decomposed[0] in IPA_VOWEL_SYMBOLS or any(c in SYLLABIC_MARKS for c in decomposed)


def test_the_vowel_test_is_phonematchers():
    assert vowels.is_vowel_phone is phonematcher.is_vowel_phone


@pytest.mark.parametrize("segment", FIRST_SEGMENTS)
def test_first_segment_is_a_vowel(segment):
    assert _by_the_chart(segment)
    assert is_vowel_phone(segment) is True
    assert semivowel_role("y", {"y": [segment]}) == SEMIVOWEL_NUCLEUS


def test_first_segment_list_is_complete():
    assert len(FIRST_SEGMENTS) == len(set(FIRST_SEGMENTS)) == 154


def test_wugniu_y_writes_a_syllabic_approximant_nucleus():
    graphemes = get("wuu-Latn-wugniu").graphemes
    assert graphemes["y"] == ["ɹ̩"]
    assert semivowel_role("y", graphemes) == SEMIVOWEL_NUCLEUS


@pytest.mark.parametrize("cluster", ["mp", "dr", "tr"])
def test_an_untied_cluster_is_two_segments_and_no_vowel(cluster):
    assert len(phonematcher.segments(cluster)) == 2
    assert not is_vowel_phone(cluster)
    assert semivowel_role("y", {"y": [cluster]}) == SEMIVOWEL_MARGIN


@pytest.mark.parametrize("vowel, place", [("a", "dorsal"), ("e", ""), ("i", "dorsal"),
                                          ("o", "dorsal"), ("u", "labial"), ("ɑ", "dorsal")])
def test_a_vowel_keeps_its_place_class(vowel, place):
    assert place_class(vowel) == place
