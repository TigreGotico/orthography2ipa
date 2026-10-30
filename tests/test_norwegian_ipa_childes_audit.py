"""The nb/ipa_childes row: velar softening is word-initial only, then notation folds.

⟨k g⟩ before a front vowel are [ç j] word-initially and [k ɡ] inside a word;
the gold agrees on 72 of 75 and 40 of 43 medial words. The rest is espeak's
notation, folded 0.3550 to 0.1033, the last fold being the gold's own error
on final ⟨-e⟩. No `valid_ceiling` for this row.
"""
import pytest

from orthography2ipa import G2P, json_loader


def test_ipa_childes_is_an_audit_not_a_ceiling():
    spec = json_loader.load_json_spec("nb")
    assert "ipa_childes" not in (spec.valid_ceiling or {})
    entry = spec.audit["ipa_childes"]
    assert entry.conclusion == "at_ceiling_documented"
    for number in ("0.3550", "0.1033", "2008", "72", "40", "599"):
        assert number in entry.measured, number
    assert "fold_nb_notation.py" in entry.measured


@pytest.mark.parametrize("word, expected", [
    ("kake", "ˈkɑːkə"),
    ("leke", "ˈleːkə"),
    ("frøken", "ˈfrøːkən"),
    ("dagen", "ˈdɑːɡən"),
    ("hage", "ˈhɑːɡə"),
    ("kino", "ˈçiːnɔ"),       # word-initial: palatal
    ("kylling", "ˈçʏlːɪŋ"),
    ("gi", "ˈjiː"),
    ("gynge", "ˈjʏŋə"),
])
def test_velar_softening_is_word_initial_only(word, expected):
    assert G2P("nb").transcribe_word(word) == expected


def test_final_e_stays_schwa_whatever_the_gold_says():
    for word in ("alle", "lite", "kake"):
        assert G2P("nb").transcribe_word(word).endswith("ə"), word
