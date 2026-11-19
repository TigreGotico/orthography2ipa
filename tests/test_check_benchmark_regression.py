"""Tests for scripts/check_benchmark_regression.py.

Covers the false-green hole where build_scoreboard() catches every
loader exception (including transient network failures) and silently
skips affected rows: if enough datasets fail to load, the gate must
fail closed instead of reporting "no regressions detected" on an
empty comparison. Also covers the harness_version/limit compatibility
guard added alongside it.
"""
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from benchmark import (  # noqa: E402
    CI_SAMPLE_JSON, CI_SAMPLE_LIMIT, HARNESS_VERSION, SCOREBOARD_JSON,
)
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


class TestStressRegression:
    """A stress_acc drop beyond the same epsilon fails like a PER rise."""

    def _rows(self, base_stress, new_stress, per=0.10):
        base = _row(per=per)
        base["stress_acc"] = base_stress
        cur = _row(per=per)
        cur["stress_acc"] = new_stress
        return {("pt-PT", "wikipron"): base}, [cur]

    def test_stress_drop_beyond_epsilon_regresses(self):
        baseline, current = self._rows(0.90, 0.88)
        _diff, regressed = cbr.compare(baseline, current, epsilon=0.005)
        assert len(regressed) == 1
        assert regressed[0]["stress_delta"] == -0.02

    def test_stress_drop_within_epsilon_is_ok(self):
        baseline, current = self._rows(0.90, 0.897)
        _diff, regressed = cbr.compare(baseline, current, epsilon=0.005)
        assert regressed == []

    def test_stress_gain_is_ok(self):
        baseline, current = self._rows(0.80, 0.95)
        _diff, regressed = cbr.compare(baseline, current, epsilon=0.005)
        assert regressed == []

    @pytest.mark.parametrize("base, new", [(None, 0.5), (0.9, None)])
    def test_null_stress_on_either_side_is_not_compared(self, base, new):
        baseline, current = self._rows(base, new)
        diff, regressed = cbr.compare(baseline, current, epsilon=0.005)
        assert regressed == []
        assert diff[0]["stress_delta"] is None

    def test_baseline_without_the_field_is_not_compared(self):
        baseline = {("pt-PT", "wikipron"): _row()}
        cur = _row()
        cur["stress_acc"] = 0.1
        _diff, regressed = cbr.compare(baseline, [cur], epsilon=0.005)
        assert regressed == []

    def test_competitor_gold_stress_drop_is_drift(self):
        baseline, current = self._rows(0.90, 0.50)
        current[0]["provenance"] = "espeak-derived"
        diff, regressed = cbr.compare(baseline, current, epsilon=0.005)
        assert regressed == []
        assert diff[0]["status"] == "drifted"


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


class TestCiSampleMatchesFullBelowCap:
    """This gate is one-sided by design (see the module docstring): it
    only fails on a PER *increase*, so an IMPROVEMENT that only lands in
    ``results.json`` never trips it, and the committed
    ``results_ci_sample.json`` baseline goes stale silently. A PR shipped
    with the two files disagreeing while this job stayed green.

    The uniform ``CI_SAMPLE_LIMIT`` gives one case that is mechanically
    checkable without re-running any loader: when a row's covered-word
    count (``n``) agrees between the full board and the CI sample, both
    runs necessarily scored the identical, un-truncated word set (the CI
    run never hit its cap), so the two files must report the identical
    PER by construction. A mismatch there is not sampling variance, it is
    a stale baseline.

    Rows where ``n`` disagrees between the two files are excluded on
    purpose: that mismatch means the CI run's raw extraction WAS capped
    at ``CI_SAMPLE_LIMIT`` even though the covered count that survived
    scoring happens to be below it (some gold entries get filtered out
    after extraction), so the sample is a genuine, expected subset of a
    larger dataset rather than an identical rescoring of it.
    """

    def test_full_and_ci_sample_agree_when_n_matches(self):
        with open(SCOREBOARD_JSON, encoding="utf-8") as fh:
            full_rows = json.load(fh)
        with open(CI_SAMPLE_JSON, encoding="utf-8") as fh:
            ci_rows = json.load(fh)
        full = {(r["lang"], r["dataset"]): r for r in full_rows}

        violations = []
        for crow in ci_rows:
            key = (crow["lang"], crow["dataset"])
            frow = full.get(key)
            if frow is None:
                continue
            if crow["n"] >= CI_SAMPLE_LIMIT or crow["n"] != frow["n"]:
                continue
            for field in ("per", "stress_acc", "n_stress"):
                if field in crow and field in frow \
                        and crow[field] != frow[field]:
                    violations.append(
                        (key, field, frow["n"], frow[field], crow[field]))

        assert violations == [], (
            "results_ci_sample.json disagrees with results.json on a row "
            "whose sample was never truncated (same n, below "
            f"CI_SAMPLE_LIMIT={CI_SAMPLE_LIMIT}), so the sample IS the "
            "full set and must match exactly: "
            f"{violations}")


class TestBaselineFromBaseBranch:
    """A pull request that regenerates the board commits its own
    results_ci_sample.json, so the gate reads the base branch's copy (#2106)."""

    @staticmethod
    def _git(repo, *args):
        import subprocess
        subprocess.run(("git", "-c", "user.name=t", "-c", "user.email=t@t",
                        *args), cwd=repo, check=True, capture_output=True)

    def _repo_with_moved_sample(self, tmp_path, base_per, head_per):
        """A repo whose committed sample holds *base_per*, and whose working
        copy holds *head_per*: the board a pull request regenerated."""
        sample = tmp_path / "benchmarks" / "results_ci_sample.json"
        sample.parent.mkdir()
        self._git(tmp_path, "init", "-q")
        sample.write_text(json.dumps([_row(per=base_per, limit=300)]))
        self._git(tmp_path, "add", ".")
        self._git(tmp_path, "commit", "-qm", "base")
        sample.write_text(json.dumps([_row(per=head_per, limit=300)]))
        return sample

    def test_reads_the_committed_copy_not_the_checkout(self, tmp_path):
        sample = self._repo_with_moved_sample(tmp_path, 0.10, 0.20)
        base = cbr.load_baseline_at("HEAD", str(sample), str(tmp_path))
        assert base[("pt-PT", "wikipron")]["per"] == 0.10
        assert cbr.load_baseline(str(sample))[("pt-PT", "wikipron")]["per"] == 0.20

    def test_unreadable_ref_fails_closed(self, tmp_path):
        sample = self._repo_with_moved_sample(tmp_path, 0.10, 0.20)
        with pytest.raises(SystemExit) as exc_info:
            cbr.load_baseline_at("no-such-ref", str(sample), str(tmp_path))
        assert "no-such-ref" in str(exc_info.value.code)

    def _run_main(self, monkeypatch, capsys, sample, base, current, body=""):
        """Run main() with --base-ref against a scored run of *current*,
        where the base branch's sample is *base*."""
        monkeypatch.setattr(cbr, "build_scoreboard", lambda limit: current)
        monkeypatch.setattr(cbr, "load_baseline_at", lambda ref: base)
        monkeypatch.setattr(cbr, "MIN_SCORED_ROWS", 1)
        monkeypatch.setenv("PR_BODY", body)
        monkeypatch.setattr(sys, "argv", [
            "check_benchmark_regression.py", "--limit", "300",
            "--baseline", str(sample), "--base-ref", "origin/dev"])
        with pytest.raises(SystemExit) as exc_info:
            cbr.main()
        return exc_info.value.code, capsys.readouterr().out

    def test_regenerated_board_does_not_hide_a_regression(
            self, tmp_path, monkeypatch, capsys):
        # The checkout's sample says 0.20, the same as the run: on its own
        # numbers the pull request regresses nothing. The base says 0.10.
        sample = tmp_path / "results_ci_sample.json"
        sample.write_text(json.dumps([_row(per=0.20)]))
        code, out = self._run_main(
            monkeypatch, capsys, sample,
            base={("pt-PT", "wikipron"): _row(per=0.10)},
            current=[_row(per=0.20)])
        assert code == 1
        assert "pt-PT (wikipron): PER 0.1000 -> 0.2000 (delta +0.1000)" in out

    def test_declared_row_reports_and_passes(
            self, tmp_path, monkeypatch, capsys):
        sample = tmp_path / "results_ci_sample.json"
        sample.write_text(json.dumps([_row(per=0.20)]))
        code, out = self._run_main(
            monkeypatch, capsys, sample,
            base={("pt-PT", "wikipron"): _row(per=0.10)},
            current=[_row(per=0.20)],
            body="Board-Rows: pt-PT/wikipron - the cited rule costs PER")
        assert code == 0
        assert "1 row(s) got worse and are declared on a Board-Rows line" in out

    def test_board_rows_all_declares_nothing(
            self, tmp_path, monkeypatch, capsys):
        sample = tmp_path / "results_ci_sample.json"
        sample.write_text(json.dumps([_row(per=0.20)]))
        code, _ = self._run_main(
            monkeypatch, capsys, sample,
            base={("pt-PT", "wikipron"): _row(per=0.10)},
            current=[_row(per=0.20)],
            body="Board-Rows: all - every row rescored")
        assert code == 1

    def test_incomparable_base_falls_back_to_the_checkout(
            self, tmp_path, monkeypatch, capsys):
        # A pull request that bumps the harness version cannot be compared
        # with a base sample scored by the old harness.
        sample = tmp_path / "results_ci_sample.json"
        sample.write_text(json.dumps([_row(per=0.20)]))
        code, out = self._run_main(
            monkeypatch, capsys, sample,
            base={("pt-PT", "wikipron"): _row(per=0.10, harness_version="0.9")},
            current=[_row(per=0.20)])
        assert code == 0
        assert "cannot be compared with this run" in out


class TestDeclaredRows:
    def test_declared_regression_is_not_a_failure(self):
        baseline = {("pt-PT", "wikipron"): _row(per=0.10)}
        diff_rows, regressed_rows = cbr.compare(
            baseline, [_row(per=0.20)], epsilon=0.005,
            declared={("pt-PT", "wikipron")})
        assert regressed_rows == []
        assert [r["status"] for r in diff_rows] == ["declared"]

    def test_declaring_another_row_still_gates(self):
        baseline = {("pt-PT", "wikipron"): _row(per=0.10)}
        _, regressed_rows = cbr.compare(
            baseline, [_row(per=0.20)], epsilon=0.005,
            declared={("pt-BR", "wikipron")})
        assert [r["status"] for r in regressed_rows] == ["regressed"]
