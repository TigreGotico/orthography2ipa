"""Tests for scripts/check_benchmark_regression.py.

Covers the false-green hole where build_scoreboard() catches every
loader exception (including transient network failures) and silently
skips affected rows: if enough datasets fail to load, the gate must
fail closed instead of reporting "no regressions detected" on an
empty comparison. Also covers the harness_version/limit compatibility
guard added alongside it.
"""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from benchmark import HARNESS_VERSION  # noqa: E402
import check_benchmark_regression as cbr  # noqa: E402


def _row(lang="pt-PT", dataset="wikipron", per=0.1, harness_version=HARNESS_VERSION,
         limit=300):
    return {
        "lang": lang,
        "dataset": dataset,
        "n": 300,
        "per": per,
        "exact_match": 0.8,
        "quality_tier": "research",
        "harness_version": harness_version,
        "limit": limit,
    }


class TestScoredRowFloor:
    def test_exits_nonzero_when_too_few_rows_scored(self):
        """Simulates a wholesale loader outage (e.g. transient network
        failure across every dataset): the current run scores far
        fewer rows than MIN_SCORED_ROWS, so the gate must fail closed
        rather than silently comparing zero rows and exiting 0."""
        current = [_row(lang=f"l{i}") for i in range(3)]
        with pytest.raises(SystemExit) as exc_info:
            cbr.check_scored_row_floor(current)
        assert exc_info.value.code != 0
        assert "scored" in str(exc_info.value.code).lower()

    def test_does_not_exit_when_enough_rows_scored(self):
        current = [_row(lang=f"l{i}") for i in range(cbr.MIN_SCORED_ROWS)]
        # should not raise
        cbr.check_scored_row_floor(current)


class TestHarnessAndLimitGuard:
    def test_exits_nonzero_on_harness_version_mismatch(self):
        baseline = {("pt-PT", "wikipron"): _row(harness_version="0.9")}
        current = [_row()]
        with pytest.raises(SystemExit) as exc_info:
            cbr.check_harness_and_limit(baseline, current, limit=300)
        assert exc_info.value.code != 0

    def test_exits_nonzero_on_limit_mismatch(self):
        baseline = {("pt-PT", "wikipron"): _row(limit=300)}
        current = [_row(limit=100)]
        with pytest.raises(SystemExit) as exc_info:
            cbr.check_harness_and_limit(baseline, current, limit=100)
        assert exc_info.value.code != 0

    def test_does_not_exit_when_consistent(self):
        baseline = {("pt-PT", "wikipron"): _row()}
        current = [_row()]
        cbr.check_harness_and_limit(baseline, current, limit=300)


class TestRegressionDetection:
    """Sanity check that real PER regressions are still caught (and
    that the new guards don't interfere with normal comparisons)."""

    def test_regression_detected(self):
        baseline = {("pt-PT", "wikipron"): _row(per=0.10)}
        current = [_row(per=0.20)]
        diff_rows, regressed_rows = cbr.compare(baseline, current, epsilon=0.005)
        assert len(regressed_rows) == 1
        assert regressed_rows[0]["status"] == "regressed"

    def test_no_regression_within_epsilon(self):
        baseline = {("pt-PT", "wikipron"): _row(per=0.10)}
        current = [_row(per=0.102)]
        diff_rows, regressed_rows = cbr.compare(baseline, current, epsilon=0.005)
        assert regressed_rows == []


class TestCompetitorDerivedGoldNeverGates:
    """A worse score against espeak-/epitran-derived or LLM gold measures
    increased DISAGREEMENT with a competitor, and diverging from a
    competitor may be exactly what the cited source demands — the same
    rule can_gate_promotion applies to tier promotion. Such rows report
    as `drifted` and never fail the gate."""

    def test_espeak_derived_regression_is_drift_not_failure(self):
        baseline = {("el", "vox_communis"):
                    _row(lang="el", dataset="vox_communis", per=0.20)}
        cur = _row(lang="el", dataset="vox_communis", per=0.30)
        cur["provenance"] = "espeak-derived"
        diff_rows, regressed_rows = cbr.compare(baseline, [cur], epsilon=0.005)
        assert regressed_rows == []
        assert diff_rows[0]["status"] == "drifted"

    def test_trusted_gold_still_gates(self):
        baseline = {("el", "wikipron"): _row(lang="el", per=0.10)}
        cur = _row(lang="el", per=0.20)
        cur["provenance"] = "crowd-scraped"
        diff_rows, regressed_rows = cbr.compare(baseline, [cur], epsilon=0.005)
        assert len(regressed_rows) == 1

    def test_missing_provenance_still_gates(self):
        baseline = {("el", "wikipron"): _row(lang="el", per=0.10)}
        cur = _row(lang="el", per=0.20)
        cur.pop("provenance", None)
        diff_rows, regressed_rows = cbr.compare(baseline, [cur], epsilon=0.005)
        assert len(regressed_rows) == 1
