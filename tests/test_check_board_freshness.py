"""Tests for scripts/check_board_freshness.py.

``test_thin_row_marker.py::test_committed_scoreboard_is_in_sync_with_generator``
only checks that ``docs/scoreboard.md`` agrees with ``benchmarks/results.json``
-- it never asks whether either agrees with what the specs actually produce.
A pull request that edits a grapheme table (e.g. ``lmo``'s missing ``ü``
mapping) moves the true PER for every row scored against that spec; if the
board is not regenerated, the two files stay mutually consistent and that
test stays green while the numbers quietly lie. These tests cover the
pieces that catch that: resolving which committed rows a touched spec can
have moved, telling a real mismatch apart from an environment that simply
could not fetch a dataset's gold, and doing all of that for BOTH committed
board files -- the full board and the CI-sample baseline, which went stale
in the same PR #1425 incident this check exists to catch and which no
existing test covers above the sample's row cap.
"""
import os
import signal
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

import check_board_freshness as cbf  # noqa: E402


def _row(lang="lmo", dataset="wikipron", per=0.2917, limit=None):
    return {"lang": lang, "dataset": dataset, "per": per, "limit": limit}


class TestOwnedRows:
    def test_row_on_a_touched_spec_is_owned(self, monkeypatch):
        monkeypatch.setattr(cbf, "spec_ancestors", lambda lang, repo=None: {lang})
        rows = [_row("lmo")]
        assert cbf.owned_rows(rows, {"lmo"}) == rows

    def test_row_inheriting_from_a_touched_spec_is_owned(self, monkeypatch):
        """Editing pt-PT.json also moves pt-PT-x-lisbon, which inherits its
        tables from it."""
        monkeypatch.setattr(
            cbf, "spec_ancestors",
            lambda lang, repo=None: {"pt-PT-x-lisbon", "pt-PT"})
        rows = [_row("pt-PT-x-lisbon", "vox_communis")]
        assert cbf.owned_rows(rows, {"pt-PT"}) == rows

    def test_unrelated_row_is_not_owned(self, monkeypatch):
        monkeypatch.setattr(cbf, "spec_ancestors", lambda lang, repo=None: {lang})
        rows = [_row("de", "wikipron")]
        assert cbf.owned_rows(rows, {"lmo"}) == []


class TestRescore:
    def test_measures_the_current_spec(self, monkeypatch):
        monkeypatch.setattr(cbf, "DATASETS",
                            {"wikipron": (lambda lang, limit: ["pairs"],
                                          ["lmo"])})
        monkeypatch.setattr(cbf, "evaluate_words",
                            lambda pairs, lang, strip_stress, broad:
                            (10, 10, [], 0.2892, 0.5))
        per, reason = cbf.rescore(_row("lmo"))
        assert reason is None
        assert per == 0.2892

    def test_loader_failure_is_a_skip_not_a_crash(self, monkeypatch):
        def boom(lang, limit):
            raise OSError("no network in this sandbox")
        monkeypatch.setattr(cbf, "DATASETS", {"wikipron": (boom, ["lmo"])})
        per, reason = cbf.rescore(_row("lmo"))
        assert per is None
        assert "no network in this sandbox" in reason

    def test_zero_coverage_raises_rather_than_skips(self, monkeypatch):
        """A dataset that loads fine but scores nothing is a broken loader
        or a spec that dropped the language -- never an environment limit,
        so it must not be swallowed the way a fetch failure is."""
        monkeypatch.setattr(cbf, "DATASETS",
                            {"wikipron": (lambda lang, limit: ["pairs"],
                                          ["lmo"])})
        monkeypatch.setattr(cbf, "evaluate_words",
                            lambda pairs, lang, strip_stress, broad:
                            (10, 0, [], 1.0, 1.0))
        with pytest.raises(RuntimeError):
            cbf.rescore(_row("lmo"))

    def test_language_dropped_from_the_dataset_is_a_skip(self, monkeypatch):
        monkeypatch.setattr(cbf, "DATASETS",
                            {"wikipron": (lambda lang, limit: [], [])})
        per, reason = cbf.rescore(_row("lmo"))
        assert per is None
        assert "lmo" in reason


class TestCheckEndToEnd:
    """Exercises check() with git and the loaders stubbed out, matching the
    lmo/wikipron incident: a spec edit that moved the true PER without the
    board being regenerated. Both board files are always given real (if
    often empty) tmp_path files: check() looks at both unconditionally, and
    an un-stubbed CI_SAMPLE_JSON would otherwise still point at the real
    committed benchmarks/results_ci_sample.json."""

    def _stub(self, monkeypatch, tmp_path, touched, measured_per,
             results_rows='[{"lang": "lmo", "dataset": "wikipron", '
                          '"per": 0.2917, "limit": null}]',
             sample_rows="[]"):
        results = tmp_path / "results.json"
        results.write_text(results_rows)
        sample = tmp_path / "results_ci_sample.json"
        sample.write_text(sample_rows)
        monkeypatch.setattr(cbf, "SCOREBOARD_JSON", str(results))
        monkeypatch.setattr(cbf, "CI_SAMPLE_JSON", str(sample))
        monkeypatch.setattr(cbf, "touched_specs",
                            lambda base, head, repo=None: touched)
        monkeypatch.setattr(cbf, "spec_ancestors",
                            lambda lang, repo=None: {lang})
        monkeypatch.setattr(cbf, "DATASETS",
                            {"wikipron": (lambda lang, limit: ["pairs"],
                                          ["lmo"])})
        monkeypatch.setattr(cbf, "evaluate_words",
                            lambda pairs, lang, strip_stress, broad:
                            (406, 406, [], measured_per, 0.5))
        return results, sample

    def test_stale_row_fails_the_check(self, tmp_path, monkeypatch, capsys):
        self._stub(monkeypatch, tmp_path, {"lmo"}, 0.2892)
        assert cbf.check("origin/dev") == 1
        err = capsys.readouterr().err
        assert "lmo/wikipron" in err
        assert "0.2917" in err and "0.2892" in err
        assert "--lang lmo --dataset wikipron" in err

    def test_fresh_row_passes_the_check(self, tmp_path, monkeypatch):
        self._stub(monkeypatch, tmp_path, {"lmo"}, 0.2892,
                  results_rows='[{"lang": "lmo", "dataset": "wikipron", '
                               '"per": 0.2892, "limit": null}]')
        assert cbf.check("origin/dev") == 0

    def test_no_touched_specs_is_a_noop(self, tmp_path, monkeypatch):
        results = tmp_path / "results.json"
        results.write_text("[]")
        sample = tmp_path / "results_ci_sample.json"
        sample.write_text("[]")
        monkeypatch.setattr(cbf, "SCOREBOARD_JSON", str(results))
        monkeypatch.setattr(cbf, "CI_SAMPLE_JSON", str(sample))
        monkeypatch.setattr(cbf, "touched_specs",
                            lambda base, head, repo=None: set())
        assert cbf.check("origin/dev") == 0

    def test_all_owned_rows_skipping_is_a_failure_not_a_pass(
            self, tmp_path, monkeypatch, capsys):
        """A run that verified nothing must never look identical to a run
        that verified everything: if every owned row's gold is unreachable,
        that is reported as a failure, not folded into
        '0 row(s) ... match', which would read as a pass."""
        results = tmp_path / "results.json"
        results.write_text(
            '[{"lang": "lmo", "dataset": "wikipron", "per": 0.2917, '
            '"limit": null}, '
            '{"lang": "lmo", "dataset": "cmudict", "per": 0.10, '
            '"limit": null}]')
        sample = tmp_path / "results_ci_sample.json"
        sample.write_text("[]")
        monkeypatch.setattr(cbf, "SCOREBOARD_JSON", str(results))
        monkeypatch.setattr(cbf, "CI_SAMPLE_JSON", str(sample))
        monkeypatch.setattr(cbf, "touched_specs",
                            lambda base, head, repo=None: {"lmo"})
        monkeypatch.setattr(cbf, "spec_ancestors",
                            lambda lang, repo=None: {lang})

        def boom(lang, limit):
            raise OSError("no network in this sandbox")

        monkeypatch.setattr(cbf, "DATASETS", {
            "wikipron": (boom, ["lmo"]),
            "cmudict": (boom, ["lmo"]),
        })

        assert cbf.check("origin/dev") == 1
        err = capsys.readouterr().err
        assert "COULD NOT VERIFY" in err
        assert "lmo/wikipron" in err and "lmo/cmudict" in err

    def test_partial_skip_states_both_counts_and_still_passes(
            self, tmp_path, monkeypatch, capsys):
        """Some rows verified and matching, some skipped: the run may still
        exit 0, but the summary must name both counts so partial coverage
        is never mistaken for full coverage."""
        results = tmp_path / "results.json"
        results.write_text(
            '[{"lang": "lmo", "dataset": "wikipron", "per": 0.2892, '
            '"limit": null}, '
            '{"lang": "lmo", "dataset": "cmudict", "per": 0.10, '
            '"limit": null}]')
        sample = tmp_path / "results_ci_sample.json"
        sample.write_text("[]")
        monkeypatch.setattr(cbf, "SCOREBOARD_JSON", str(results))
        monkeypatch.setattr(cbf, "CI_SAMPLE_JSON", str(sample))
        monkeypatch.setattr(cbf, "touched_specs",
                            lambda base, head, repo=None: {"lmo"})
        monkeypatch.setattr(cbf, "spec_ancestors",
                            lambda lang, repo=None: {lang})

        def boom(lang, limit):
            raise OSError("no network in this sandbox")

        monkeypatch.setattr(cbf, "DATASETS", {
            "wikipron": (lambda lang, limit: ["pairs"], ["lmo"]),
            "cmudict": (boom, ["lmo"]),
        })
        monkeypatch.setattr(cbf, "evaluate_words",
                            lambda pairs, lang, strip_stress, broad:
                            (406, 406, [], 0.2892, 0.5))

        assert cbf.check("origin/dev") == 0
        err = capsys.readouterr().err
        assert "1 of 2" in err
        assert "1 skipped" in err


class TestCiSampleBoardIsAlsoChecked:
    """The CI-sample baseline (benchmarks/results_ci_sample.json) went stale
    in the exact same PR #1425 incident, and nothing generic caught it for a
    row above CI_SAMPLE_LIMIT (see the module docstring). check() must
    verify it independently of the full board -- a clean full board must
    never excuse a stale sample, or the reverse."""

    def _stub(self, monkeypatch, tmp_path, sample_rows, results_rows="[]",
             measured_per=0.2892, dataset_limit=None):
        results = tmp_path / "results.json"
        results.write_text(results_rows)
        sample = tmp_path / "results_ci_sample.json"
        sample.write_text(sample_rows)
        monkeypatch.setattr(cbf, "SCOREBOARD_JSON", str(results))
        monkeypatch.setattr(cbf, "CI_SAMPLE_JSON", str(sample))
        monkeypatch.setattr(cbf, "touched_specs",
                            lambda base, head, repo=None: {"lmo"})
        monkeypatch.setattr(cbf, "spec_ancestors",
                            lambda lang, repo=None: {lang})

        seen_limits = []

        def fake_loader(lang, limit):
            seen_limits.append(limit)
            return ["pairs"]

        monkeypatch.setattr(cbf, "DATASETS",
                            {"wikipron": (fake_loader, ["lmo"])})
        monkeypatch.setattr(cbf, "evaluate_words",
                            lambda pairs, lang, strip_stress, broad:
                            (406, 406, [], measured_per, 0.5))
        return results, sample, seen_limits

    def test_stale_sample_row_fails_even_with_a_clean_full_board(
            self, tmp_path, monkeypatch, capsys):
        """The full board matches; only the CI sample is stale (a row above
        the cap, so TestCiSampleMatchesFullBelowCap's n-based cross-check
        cannot fire on it)."""
        _, _, seen_limits = self._stub(
            monkeypatch, tmp_path,
            sample_rows='[{"lang": "lmo", "dataset": "wikipron", '
                        '"per": 0.2917, "limit": 1000}]',
            results_rows='[{"lang": "lmo", "dataset": "wikipron", '
                         '"per": 0.2892, "limit": null}]')

        assert cbf.check("origin/dev") == 1
        err = capsys.readouterr().err
        assert "results_ci_sample.json" in err
        assert "0.2917" in err and "0.2892" in err
        assert "--ci-sample" in err
        # The full board's loader call used the real limit (no cap); the
        # sample's used CI_SAMPLE_LIMIT -- proving the rescoring compared
        # the sample against an identically-capped re-run, not the full set.
        assert sys.maxsize in seen_limits
        assert 1000 in seen_limits

    def test_fresh_sample_row_passes(self, tmp_path, monkeypatch):
        self._stub(
            monkeypatch, tmp_path,
            sample_rows='[{"lang": "lmo", "dataset": "wikipron", '
                        '"per": 0.2892, "limit": 1000}]')
        assert cbf.check("origin/dev") == 0


class TestProgressAndInterruption:
    """A widely-inherited parent spec can own rows with hundreds of
    thousands of pairs; a slow run must show what it is doing, and a run
    killed mid-flight must never be mistaken for one that finished clean."""

    def test_each_row_is_announced_before_it_is_measured(
            self, tmp_path, monkeypatch, capsys):
        results = tmp_path / "results.json"
        results.write_text(
            '[{"lang": "lmo", "dataset": "wikipron", "per": 0.2892, '
            '"limit": null}]')
        sample = tmp_path / "results_ci_sample.json"
        sample.write_text("[]")
        monkeypatch.setattr(cbf, "SCOREBOARD_JSON", str(results))
        monkeypatch.setattr(cbf, "CI_SAMPLE_JSON", str(sample))
        monkeypatch.setattr(cbf, "touched_specs",
                            lambda base, head, repo=None: {"lmo"})
        monkeypatch.setattr(cbf, "spec_ancestors",
                            lambda lang, repo=None: {lang})
        monkeypatch.setattr(cbf, "DATASETS",
                            {"wikipron": (lambda lang, limit: ["pairs"],
                                          ["lmo"])})
        monkeypatch.setattr(cbf, "evaluate_words",
                            lambda pairs, lang, strip_stress, broad:
                            (406, 406, [], 0.2892, 0.5))

        assert cbf.check("origin/dev") == 0
        err = capsys.readouterr().err
        assert "rescoring benchmarks/results.json lmo/wikipron" in err

    def test_progress_tracks_verified_and_outstanding_rows(
            self, tmp_path, monkeypatch):
        """After a clean run every row started out outstanding and ends up
        verified -- nothing is left outstanding once check() returns."""
        results = tmp_path / "results.json"
        results.write_text(
            '[{"lang": "lmo", "dataset": "wikipron", "per": 0.2892, '
            '"limit": null}]')
        sample = tmp_path / "results_ci_sample.json"
        sample.write_text("[]")
        monkeypatch.setattr(cbf, "SCOREBOARD_JSON", str(results))
        monkeypatch.setattr(cbf, "CI_SAMPLE_JSON", str(sample))
        monkeypatch.setattr(cbf, "touched_specs",
                            lambda base, head, repo=None: {"lmo"})
        monkeypatch.setattr(cbf, "spec_ancestors",
                            lambda lang, repo=None: {lang})
        monkeypatch.setattr(cbf, "DATASETS",
                            {"wikipron": (lambda lang, limit: ["pairs"],
                                          ["lmo"])})
        monkeypatch.setattr(cbf, "evaluate_words",
                            lambda pairs, lang, strip_stress, broad:
                            (406, 406, [], 0.2892, 0.5))

        cbf.check("origin/dev")
        assert cbf._PROGRESS["outstanding"] == []
        assert ("benchmarks/results.json", "lmo", "wikipron") in \
            cbf._PROGRESS["verified"]

    def test_interrupted_reports_verified_and_outstanding_never_a_pass(
            self, capsys):
        """Simulates the signal handler firing mid-run: one row already
        measured, one row not yet reached. The report must name both and
        exit non-zero -- a kill must never look like a clean pass."""
        cbf._PROGRESS["verified"] = [
            ("benchmarks/results.json", "en-GB", "cmudict")]
        cbf._PROGRESS["outstanding"] = [
            ("benchmarks/results.json", "en-GB", "ipadict"),
            ("benchmarks/results.json", "en-GB", "wikipron")]
        try:
            with pytest.raises(SystemExit) as exc_info:
                cbf._report_interrupted(signal.SIGTERM, None)
        finally:
            cbf._PROGRESS["verified"] = []
            cbf._PROGRESS["outstanding"] = []

        assert exc_info.value.code != 0
        err = capsys.readouterr().err
        assert "en-GB/cmudict" in err
        assert "en-GB/ipadict" in err and "en-GB/wikipron" in err
        assert "NOT evidence the board is fresh" in err
