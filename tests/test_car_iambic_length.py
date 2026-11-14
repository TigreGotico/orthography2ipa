"""Galibi Carib (`car`) — vowel length by weight-alternating footing.

Courtz (2008, *A Carib Grammar and Dictionary*, §2.3.1-2.3.2) describes an
Eastern Surinamese Carib stress system independent of the final-syllable
accent this spec marks (Hoff 1968, Western Surinamese Carib): "In words of
more than two syllables, even syllables except the word final syllable are
stressed, if the word initial syllable is light. If the word initial
syllable is heavy, odd syllables except the word final syllable are
stressed" (p. 27-28), and "All vowels may be pronounced a little longer ...
when stressed" (p. 31). A light syllable is open (no diphthong, no coda); a
heavy one has either.

Expected strings are worked out from that rule directly on the input
spelling, never read back from the engine. The wikipron gold
(``car_latn_narrow.tsv``) independently confirms the pattern: ``ajawa`` ->
``a j aː w a``, ``ajunu`` -> ``a j uː n u``, ``akami`` -> ``a k aː m i``,
``ainatone`` -> ``a j ɲ a d oː n e``, ``aipajawa`` ->
``a j h pʲ a j aː w a``.
"""
import pytest

import orthography2ipa as o2i


@pytest.fixture(scope="module")
def car():
    return o2i.G2P("car")


def strip_stress(s):
    return s.replace("ˈ", "").replace("ˌ", "")


@pytest.mark.parametrize("word,expected", [
    # a.ja.wa — light initial "a" (open, no coda/diphthong): the alternation
    # starts on the SECOND syllable, "ja", which is itself light so it
    # lengthens; "wa" is final and never a foot head.
    ("ajawa", "ajaːwa"),
    ("ajunu", "ajuːnu"),
    ("akami", "akaːmi"),
    # ai.na.to.ne — heavy initial "ai" (diphthong): the alternation starts
    # on the first syllable itself, but "ai" is already heavy so it is not
    # further lengthened; the next foot head is the third syllable "to".
    ("ainatone", "ainatoːne"),
    # ai.pa.ja.wa — same heavy-initial footing (1st, 3rd syllables); "ai"
    # stays unlengthened (already heavy), "ja" lengthens.
    ("aipajawa", "aipajaːwa"),
])
def test_iambic_length_matches_gold_pattern(car, word, expected):
    assert strip_stress(car.transcribe_word(word)) == expected


@pytest.mark.parametrize("word", [
    "tata",   # 2 syllables — Courtz's rule is stated for >2 syllables only
    "tuna",   # 2 syllables
    "apo",    # 2 syllables
])
def test_short_words_get_no_extra_length(car, word):
    assert "ː" not in car.transcribe_word(word)


def test_iambic_length_runs_before_the_final_stress_mark(car):
    """The Hoff-dialect accent mark still falls on the final syllable —
    the length is a separate fact from where the mark is written."""
    out = car.transcribe_word("ajawa")
    assert out.endswith("ˈwa")
    assert "aːˈ" in out
