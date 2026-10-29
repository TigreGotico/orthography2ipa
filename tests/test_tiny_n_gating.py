"""A row scored on fewer than ``THIN_ROW_N`` words has no confidence interval
and does not gate.

Resampling one word returns that word, so the old interval for ``ar-DZ``
/``primary_sources`` (one gold entry, PER 0.7143) read ``[0.7143, 0.7143]``.
"""
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import benchmark  # noqa: E402
import check_benchmark_regression as cbr  # noqa: E402

REPO = os.path.join(os.path.dirname(__file__), "..")


def _score(monkeypatch, pairs, provenance="expert-human"):
    monkeypatch.setitem(
        benchmark.DATASETS, "_tiny_n_ds", (lambda lang, limit: pairs, ["eo"]))
    monkeypatch.setitem(benchmark.PROVENANCE, "_tiny_n_ds", provenance)
    (row,) = benchmark.build_scoreboard(
        None, only_langs=["eo"], only_datasets=["_tiny_n_ds"])
    return row


def test_one_word_row_has_null_interval_and_does_not_gate(monkeypatch):
    row = _score(monkeypatch, [("saluton", "salutxn")])
    assert row["n"] == 1
    assert row["per_ci_low"] is None
    assert row["per_ci_high"] is None
    assert row["gating"] is False


def _mixed_pairs(count):
    """*count* distinct eo words; every other one is scored against a wrong
    gold, so the per-word PERs differ and a real interval has width."""
    from orthography2ipa import G2P

    g2p = G2P("eo")
    words = [c + v for c in "bdfgklmnprstvz" for v in "aeiou"][:count]
    return [(w, g2p.transcribe(w) if i % 2 else "x")
            for i, w in enumerate(words)]


def test_row_at_the_minimum_sample_has_an_interval_and_gates(monkeypatch):
    row = _score(monkeypatch, _mixed_pairs(benchmark.THIN_ROW_N))
    assert row["n"] == benchmark.THIN_ROW_N
    assert row["per_ci_low"] is not None and row["per_ci_high"] is not None
    assert row["per_ci_low"] < row["per"] < row["per_ci_high"]
    assert row["gating"] is True


def test_row_one_below_the_minimum_is_the_boundary(monkeypatch):
    row = _score(monkeypatch, _mixed_pairs(benchmark.THIN_ROW_N - 1))
    assert row["n"] == benchmark.THIN_ROW_N - 1
    assert row["per_ci_low"] is None
    assert row["gating"] is False


def test_row_gates_needs_both_a_trusted_tier_and_enough_words():
    n = benchmark.THIN_ROW_N
    assert benchmark.row_gates("expert-human", n) is True
    assert benchmark.row_gates("expert-human", n - 1) is False
    assert benchmark.row_gates("espeak-derived", n) is False


def test_regression_gate_reports_a_tiny_row_as_drifted_not_regressed():
    def row(per, n):
        return {"lang": "ar-DZ", "dataset": "primary_sources", "n": n,
                "per": per, "provenance": "expert-human",
                "harness_version": benchmark.HARNESS_VERSION,
                "limit": benchmark.CI_SAMPLE_LIMIT}

    baseline = {("ar-DZ", "primary_sources"): row(0.10, 1)}
    _, regressed = cbr.compare(baseline, [row(0.70, 1)], epsilon=0.005)
    assert regressed == []
    baseline = {("ar-DZ", "primary_sources"): row(0.10, benchmark.THIN_ROW_N)}
    _, regressed = cbr.compare(
        baseline, [row(0.70, benchmark.THIN_ROW_N)], epsilon=0.005)
    assert len(regressed) == 1


@pytest.mark.parametrize("name", ["results.json", "results_ci_sample.json"])
def test_committed_board_has_no_point_interval_below_the_minimum(name):
    with open(os.path.join(REPO, "benchmarks", name), encoding="utf-8") as fh:
        rows = json.load(fh)
    thin = [r for r in rows if r["n"] < benchmark.THIN_ROW_N]
    assert thin, "the board holds no thin row to check"
    bad = [(r["lang"], r["dataset"]) for r in thin
           if r["per_ci_low"] is not None or r["per_ci_high"] is not None
           or r.get("gating") is True]
    assert not bad, f"thin rows with an interval or a gating vote: {bad}"
