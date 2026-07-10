"""Tests for scripts/error_analysis.py.

Uses a tiny in-memory fixture dataset (monkeypatched loader, no
network) to golden-test the three report sections, plus property
tests on scripts.benchmark.align().
"""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from benchmark import align, levenshtein  # noqa: E402
import error_analysis  # noqa: E402


# ═══════════════════════════════════════════════════════════════════════════
# align() properties
# ═══════════════════════════════════════════════════════════════════════════

ALIGN_CASES = [
    ("", ""),
    ("a", ""),
    ("", "a"),
    ("kat", "kat"),
    ("kat", "kæt"),
    ("kat", "kaat"),
    ("kaat", "kat"),
    ("abc", "xyz"),
    ("ˈabɐ", "abɐ"),
    ("sjẽsjɐ", "siensiɐ"),
]


@pytest.mark.parametrize("a,b", ALIGN_CASES)
def test_align_reconstructs_both_strings(a, b):
    pairs = align(a, b)
    reconstructed_a = "".join(p[0] for p in pairs if p[0] is not None)
    reconstructed_b = "".join(p[1] for p in pairs if p[1] is not None)
    assert reconstructed_a == a
    assert reconstructed_b == b


@pytest.mark.parametrize("a,b", ALIGN_CASES)
def test_align_op_count_matches_levenshtein(a, b):
    pairs = align(a, b)
    ops = sum(1 for gp, hp in pairs if gp != hp)
    assert ops == levenshtein(a, b)


def test_align_identical_strings_all_matches():
    pairs = align("kat", "kat")
    assert pairs == [("k", "k"), ("a", "a"), ("t", "t")]


def test_align_pure_insertion():
    pairs = align("", "abc")
    assert pairs == [(None, "a"), (None, "b"), (None, "c")]


def test_align_pure_deletion():
    pairs = align("abc", "")
    assert pairs == [("a", None), ("b", None), ("c", None)]


# ═══════════════════════════════════════════════════════════════════════════
# error_analysis.py golden-output test on a tiny fixture dataset
# ═══════════════════════════════════════════════════════════════════════════

# A tiny synthetic gold set for a real registered language ("en"), chosen
# so the engine's output is known and errors are deterministic and small
# enough to hand-verify.
_FIXTURE_PAIRS = [
    ("cat", "kæt"),
    ("cat", "kat"),   # second reference for the same word (dialect variant)
    ("bad", "bad"),
    ("bad", "bæd"),
]


def _fake_loader(lang, limit):
    return _FIXTURE_PAIRS[:limit]


@pytest.fixture
def patched_dataset(monkeypatch):
    monkeypatch.setitem(
        error_analysis.DATASETS, "fixture_gold", (_fake_loader, ["en"]))
    yield "fixture_gold"


def test_pick_dataset_explicit(patched_dataset):
    assert error_analysis.pick_dataset("en", patched_dataset) == patched_dataset


def test_pick_dataset_rejects_uncovered_lang(patched_dataset):
    with pytest.raises(SystemExit):
        error_analysis.pick_dataset("pt-PT", patched_dataset)


def test_pick_dataset_rejects_unknown_dataset():
    with pytest.raises(SystemExit):
        error_analysis.pick_dataset("en", "not-a-real-dataset")


def test_pick_dataset_defaults_to_first_covering_dataset(patched_dataset):
    # "wikipron" (an already-registered dataset) also covers "en" and
    # iterates before "fixture_gold" was inserted, so the default without
    # an explicit --dataset must still resolve deterministically to
    # *some* dataset covering "en" -- not necessarily the fixture one.
    chosen = error_analysis.pick_dataset("en")
    _, langs = error_analysis.DATASETS[chosen]
    assert "en" in langs


def test_analyze_golden_output(patched_dataset):
    report = error_analysis.analyze("en", patched_dataset, limit=10)

    assert report["lang"] == "en"
    assert report["dataset"] == patched_dataset
    # two distinct words in the fixture ("cat", "bad")
    assert report["n_words"] == 2
    assert report["n_scored"] == 2

    # every section is present and JSON-serializable in shape
    assert set(report) == {
        "lang", "dataset", "n_words", "n_scored",
        "confusion_pairs", "worst_words", "grapheme_blame",
    }
    assert isinstance(report["confusion_pairs"], list)
    assert isinstance(report["worst_words"], list)
    assert isinstance(report["grapheme_blame"], list)

    # worst_words covers exactly the fixture's distinct words, each with
    # both a gold and hyp string and a PER in [0, 1]
    words_seen = {row["word"] for row in report["worst_words"]}
    assert words_seen == {"cat", "bad"}
    for row in report["worst_words"]:
        assert 0.0 <= row["per"] <= 1.0
        assert row["gold"]
        assert row["hyp"]

    # worst_words is sorted worst-first
    pers = [row["per"] for row in report["worst_words"]]
    assert pers == sorted(pers, reverse=True)

    # confusion pairs are (gold, hyp) tuples with a positive count each
    for row in report["confusion_pairs"]:
        assert "gold" in row and "hyp" in row
        assert row["count"] >= 1

    # grapheme_blame only reports graphemes seen at least 3 times; with
    # only two fixture words no grapheme reaches that floor
    assert report["grapheme_blame"] == []


def test_analyze_grapheme_blame_respects_min_occurrences(monkeypatch):
    # three words sharing the letter "a" so it clears the
    # MIN_GRAPHEME_OCCURRENCES floor and shows up in the blame report
    pairs = [
        ("cat", "kæt"),
        ("bat", "bæt"),
        ("mat", "mæt"),
    ]
    monkeypatch.setitem(
        error_analysis.DATASETS, "fixture_gold3", (lambda lang, limit: pairs[:limit], ["en"]))
    report = error_analysis.analyze("en", "fixture_gold3", limit=10)
    blamed = {row["grapheme"]: row for row in report["grapheme_blame"]}
    assert "a" in blamed
    assert blamed["a"]["n"] == 3
    assert 0.0 <= blamed["a"]["mean_per"] <= 1.0


def test_analyze_never_raises_on_untranscribable_word(monkeypatch):
    # a loader yielding an empty-string word must not crash analyze();
    # the engine either raises or returns empty and the row is skipped
    monkeypatch.setitem(
        error_analysis.DATASETS, "fixture_empty",
        (lambda lang, limit: [("", "kæt")], ["en"]))
    report = error_analysis.analyze("en", "fixture_empty", limit=10)
    assert report["n_words"] == 1
