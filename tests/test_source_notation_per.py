"""Per-source notation folds of the pt-BR portuguese_unified rows."""
import os
import sys
import unicodedata

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from source_notation_per import fold  # noqa: E402

N = lambda s: unicodedata.normalize("NFD", s)  # noqa: E731
ALL = {"michaelis_ã", "michaelis_no_palatal", "michaelis_final_r"}


@pytest.mark.parametrize("hyp,gold,folds,expected", [
    ("ˈlejt͡ʃi", "ˈlejti", {"michaelis_no_palatal"}, ("ˈlejti", "ˈlejti")),
    ("siˈdad͡ʒi", "siˈdadi", {"michaelis_no_palatal"}, ("siˈdadi", "siˈdadi")),
    # Not before a front vowel: the palatal stays.
    ("ˈt͡ʃa", "ˈta", {"michaelis_no_palatal"}, ("ˈt͡ʃa", "ˈta")),
    ("kɐ̃ˈtaɾ", "kãˈtaɾ", {"michaelis_ã"}, ("kãˈtaɾ", "kãˈtaɾ")),
    ("kɐ̃ˈta", "kãˈtaɾ", {"michaelis_final_r"}, ("kɐ̃ˈta", "kãˈta")),
    # A final r in the hypothesis keeps the gold's r.
    ("kɐ̃ˈtaɾ", "kãˈtaɾ", {"michaelis_final_r"}, ("kɐ̃ˈtaɾ", "kãˈtaɾ")),
    # No folds: nothing changes.
    ("ˈlejt͡ʃi", "ˈlejti", set(), ("ˈlejt͡ʃi", "ˈlejti")),
])
def test_fold(hyp, gold, folds, expected):
    assert fold(hyp, gold, folds) == tuple(N(x) for x in expected)


def test_all_folds_together():
    assert fold("kɐ̃t͡ʃiˈla", "kãtiˈlaɾ", ALL) == (N("kãtiˈla"), N("kãtiˈla"))


def test_committed_unfolded_numbers_equal_the_board():
    import json
    root = os.path.join(os.path.dirname(__file__), "..", "benchmarks")
    folds = json.load(open(os.path.join(root, "notation_folds.json"), encoding="utf-8"))
    board = {(r["lang"], r["dataset"]): r["per"]
             for r in json.load(open(os.path.join(root, "results.json"), encoding="utf-8"))}
    assert folds
    for row in folds:
        assert round(board[(row["lang"], row["dataset"])], 4) == row["per"]
        assert row["folded_per"] < row["per"]


def test_the_scoreboard_marks_the_folded_rows_as_not_gated():
    import benchmark
    section = "\n".join(benchmark.notation_fold_section())
    assert "reported, not gated" in section
    assert "`michaelis_final_r`" in section
