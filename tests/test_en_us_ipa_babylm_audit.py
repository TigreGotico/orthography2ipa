"""The en-US/ipa_babylm row: three measured rules, six notation folds, a lexical floor.

Word-final ⟨s⟩ after a tense or r-coloured vowel is [z], word-final ⟨y⟩ in a
monosyllable is [aɪ], and I/is/as/was/has/his are whole-word exceptions; the
gold agrees on the words it holds. The rest is espeak's notation (folded
0.3602 to 0.2926) and the vowel readings English spelling does not signal,
counted as 61.9% of the remaining edits. No `valid_ceiling`.
"""
import pytest

from orthography2ipa import G2P, json_loader


def test_ipa_babylm_is_an_audit_not_a_ceiling():
    spec = json_loader.load_json_spec("en-US")
    assert "ipa_babylm" not in (spec.valid_ceiling or {})
    entry = spec.audit["ipa_babylm"]
    assert entry.conclusion == "at_ceiling_documented"
    for number in ("0.3602", "0.2926", "8072", "61.9%", "320", "338"):
        assert number in entry.measured, number
    assert "fold_en_us_notation.py" in entry.measured


@pytest.mark.parametrize("word, expected", [
    ("days", "ˈdeɪz"),
    ("goes", "ˈɡoʊz"),
    ("sees", "ˈsiz"),
    ("cars", "ˈkɑɹz"),
    ("years", "ˈjɪəɹz"),
    ("hers", "ˈhɝz"),
    ("this", "ˈθɪs"),      # a lax vowel keeps [s]
    ("bus", "ˈbʌs"),
    ("gas", "ˈɡæs"),
])
def test_final_s_voices_after_a_tense_or_r_coloured_vowel(word, expected):
    assert G2P("en-US").transcribe_word(word) == expected


@pytest.mark.parametrize("word, expected", [
    ("my", "ˈmaɪ"),
    ("why", "ˈwaɪ"),
    ("try", "ˈtɹaɪ"),
    ("sky", "ˈskaɪ"),
    ("happy", "ˈhæpi"),    # another vowel letter: the [i] ending stays
    ("city", "ˈsɪti"),
])
def test_final_y_in_a_monosyllable_is_a_diphthong(word, expected):
    assert G2P("en-US").transcribe_word(word) == expected


@pytest.mark.parametrize("word, expected", [
    ("I", "ˈaɪ"),
    ("I'm", "ˈaɪm"),
    ("I’m", "ˈaɪm"),
    ("is", "ˈɪz"),
    ("was", "ˈwʌz"),
    ("his", "ˈhɪz"),
])
def test_the_whole_word_exceptions(word, expected):
    assert G2P("en-US").transcribe_word(word) == expected
