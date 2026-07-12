#!/usr/bin/env python3
"""Fail CI when a PR worsens PER against the committed benchmark baseline.

Reuses :func:`scripts.benchmark.build_scoreboard` (no duplicated
loading/scoring logic) to re-run every registered gold dataset/language
combination against the current checkout, then compares each resulting
row's PER to the matching row in the committed baseline.

FULL-vs-SAMPLE, never mixed. The PUBLISHED scoreboard
(``benchmarks/results.json`` / ``docs/scoreboard.md``) is FULL-dataset —
every gold word, no cap — and is far too slow to re-run in a CI job (the
617k-row ``portuguese_phonetic_lexicon`` and 102k-row ``infopedia_pt``
alone take the better part of an hour). So this gate does NOT compare
against the full scoreboard. It re-scores at a fixed, UNIFORM sample size
(``benchmark.CI_SAMPLE_LIMIT``, the SAME cap for every language — no
per-language juggling) and compares against a SEPARATE baseline committed
at that identical cap (``benchmarks/results_ci_sample.json``, written by
``scripts/benchmark.py --ci-sample``). Because both sides are sliced
identically, there is never a mixed-slice comparison producing spurious
"regressions". Refresh the sample baseline whenever the full scoreboard is
regenerated.

A row regresses when its new PER exceeds the baseline PER by more than
an absolute epsilon (default ``0.005`` — small enough to catch a real
grapheme/allophone regression, large enough to absorb harness-level
float noise between runs).

Datasets that need packages not installable in a plain CI runner
(``cmudict`` needs ``scriptconv``, TigreGotico-internal) fail to load and are
skipped by ``build_scoreboard`` itself (catch-and-skip, matching PR
#76's existing behavior); this script does not treat those absences as
regressions, it only notes them. Baseline rows with no corresponding
new row (skipped dataset) are noted, not scored. New rows with no
baseline match (e.g. a language added since the baseline was
committed) are noted, not scored, since there is nothing to regress
against.

Usage::

    python scripts/check_benchmark_regression.py
    python scripts/check_benchmark_regression.py --epsilon 0.01 --limit 500
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Dict, List, Tuple

sys.path.insert(0, os.path.dirname(__file__))

from benchmark import (  # noqa: E402
    build_scoreboard, CI_SAMPLE_JSON, CI_SAMPLE_LIMIT,
    HARNESS_VERSION,
)

DEFAULT_EPSILON = 0.005

# Absolute floor on successfully-scored rows in the current run. If the
# scoreboard collapses to (near-)zero rows — e.g. every dataset loader
# hit a transient network failure — build_scoreboard() silently skips
# the failing rows rather than raising, so a naive "any regressions?"
# check would find none and exit 0: a false green exactly when the gate
# is blind. This floor is well below the current committed baseline's
# row count (see benchmarks/results.json) but high enough that a
# wholesale loader outage cannot slip through unnoticed.
MIN_SCORED_ROWS = 20


def _row_key(row: dict) -> Tuple[str, str]:
    return (row["lang"], row["dataset"])


def load_baseline(path: str) -> Dict[Tuple[str, str], dict]:
    with open(path, encoding="utf-8") as fh:
        rows = json.load(fh)
    return {_row_key(r): r for r in rows}


def compare(
    baseline: Dict[Tuple[str, str], dict],
    current: List[dict],
    epsilon: float,
) -> Tuple[List[dict], List[dict]]:
    """Return (diff_rows, regressed_rows).

    ``diff_rows`` covers every key present in either baseline or
    current, each annotated with a ``status`` of ``ok``, ``regressed``,
    ``new`` (no baseline row) or ``missing`` (baseline row not
    reproduced this run, e.g. its dataset failed to load this time).
    """
    diff_rows: List[dict] = []
    regressed_rows: List[dict] = []

    current_by_key = {_row_key(r): r for r in current}
    all_keys = sorted(set(baseline) | set(current_by_key))

    for key in all_keys:
        lang, dataset = key
        base_row = baseline.get(key)
        cur_row = current_by_key.get(key)

        if base_row is None:
            diff_rows.append({
                "lang": lang, "dataset": dataset,
                "baseline_per": None, "new_per": cur_row["per"],
                "delta": None, "status": "new",
            })
            continue

        if cur_row is None:
            diff_rows.append({
                "lang": lang, "dataset": dataset,
                "baseline_per": base_row["per"], "new_per": None,
                "delta": None, "status": "missing",
            })
            continue

        delta = cur_row["per"] - base_row["per"]
        status = "regressed" if delta > epsilon else "ok"
        row = {
            "lang": lang, "dataset": dataset,
            "baseline_per": base_row["per"], "new_per": cur_row["per"],
            "delta": round(delta, 4), "status": status,
        }
        diff_rows.append(row)
        if status == "regressed":
            regressed_rows.append(row)

    return diff_rows, regressed_rows


def format_value(v) -> str:
    if v is None:
        return "-"
    return f"{v:.4f}"


def print_report(diff_rows: List[dict], epsilon: float) -> None:
    header = f"{'lang':<16}{'dataset':<20}{'baseline':>10}{'new':>10}{'delta':>10}  status"
    print(header)
    print("-" * len(header))
    for row in diff_rows:
        line = (
            f"{row['lang']:<16}{row['dataset']:<20}"
            f"{format_value(row['baseline_per']):>10}"
            f"{format_value(row['new_per']):>10}"
            f"{format_value(row['delta']):>10}  {row['status']}"
        )
        if row["status"] == "regressed":
            line += "  <-- REGRESSION"
        print(line)
    print("-" * len(header))
    print(f"epsilon={epsilon} (absolute PER worsening allowed vs. baseline)")


def check_scored_row_floor(current: List[dict]) -> None:
    """Fail loudly if too few rows were successfully scored this run.

    ``build_scoreboard`` catches every loader exception (including
    transient network failures) and silently drops the affected
    rows, so a wholesale outage (e.g. every dataset fails to load)
    would otherwise produce zero comparable rows and a false-green
    "no regressions detected" exit.
    """
    if len(current) < MIN_SCORED_ROWS:
        sys.exit(
            f"only {len(current)} row(s) were successfully scored this "
            f"run (minimum required: {MIN_SCORED_ROWS}) — this looks "
            f"like a wholesale dataset-loading failure (e.g. transient "
            f"network outage) rather than a real absence of gold data, "
            f"so the regression gate cannot trust its own comparison. "
            f"Failing closed instead of reporting a false green."
        )


def check_harness_and_limit(
    baseline: Dict[Tuple[str, str], dict],
    current: List[dict],
    limit: int,
) -> None:
    """Fail loudly on a harness/limit mismatch between baseline and
    current run, since either makes PER deltas incomparable:

    - a different ``harness_version`` means the scoring method itself
      changed, not just the code under test.
    - a different ``--limit`` slices a different-sized (and thus
      differently distributed) sample of each gold dataset, which can
      produce spurious mass "regressions" that are really just
      slice-size noise, not a real PER change.
    """
    baseline_versions = {
        r.get("harness_version") for r in baseline.values()
    }
    if baseline_versions - {HARNESS_VERSION}:
        sys.exit(
            f"baseline was generated with harness_version(s) "
            f"{sorted(v for v in baseline_versions if v)} but this "
            f"checkout's harness_version is {HARNESS_VERSION!r} — "
            f"regenerate the CI sample baseline "
            f"(scripts/benchmark.py --ci-sample) before comparing."
        )

    # ``None`` is a meaningful limit — it marks a full-dataset row. Keep it in
    # the set so a full baseline (results.json) compared against a sampled run
    # trips the mismatch instead of slipping through an empty set.
    baseline_limits = {r.get("limit") for r in baseline.values()}
    if baseline_limits and baseline_limits - {limit}:
        shown = sorted(
            ("full" if v is None else v) for v in baseline_limits
        ) if None in baseline_limits else sorted(baseline_limits)
        sys.exit(
            f"baseline was generated with limit(s) {shown} "
            f"but this run used --limit {'full' if limit is None else limit} — "
            f"a different slice size per dataset produces spurious PER deltas "
            f"unrelated to real regressions. Re-run with --limit matching the "
            f"baseline (or regenerate the baseline at the new limit)."
        )


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--epsilon", type=float, default=DEFAULT_EPSILON,
                     help=f"Max allowed absolute PER worsening vs. "
                          f"baseline before a row counts as a regression "
                          f"(default {DEFAULT_EPSILON}).")
    ap.add_argument("--limit", type=int, default=CI_SAMPLE_LIMIT,
                     help="Uniform rows per dataset/lang to evaluate "
                          "(passed through to build_scoreboard). Must match "
                          "the sample baseline's limit; defaults to "
                          f"benchmark.CI_SAMPLE_LIMIT ({CI_SAMPLE_LIMIT}).")
    ap.add_argument("--baseline", default=CI_SAMPLE_JSON,
                     help="Path to the committed CI sample baseline JSON "
                          "(default benchmarks/results_ci_sample.json). This "
                          "is the UNIFORM-sample baseline, NOT the full "
                          "published benchmarks/results.json.")
    args = ap.parse_args()

    baseline = load_baseline(args.baseline)
    current = build_scoreboard(args.limit)

    check_scored_row_floor(current)
    check_harness_and_limit(baseline, current, args.limit)

    diff_rows, regressed_rows = compare(baseline, current, args.epsilon)
    print_report(diff_rows, args.epsilon)

    new_rows = [r for r in diff_rows if r["status"] == "new"]
    missing_rows = [r for r in diff_rows if r["status"] == "missing"]
    if new_rows:
        print(f"\n{len(new_rows)} row(s) have no baseline match (new "
              f"language/dataset) — not scored for regression.")
    if missing_rows:
        print(f"{len(missing_rows)} baseline row(s) were not reproduced "
              f"this run (dataset failed to load, e.g. needs a "
              f"TigreGotico-internal package or network access not "
              f"available here) — skipped gracefully, not scored.")

    if regressed_rows:
        print(f"\n{len(regressed_rows)} row(s) regressed beyond "
              f"epsilon={args.epsilon}:")
        for row in regressed_rows:
            print(f"  {row['lang']} ({row['dataset']}): "
                  f"{row['baseline_per']:.4f} -> {row['new_per']:.4f} "
                  f"(delta +{row['delta']:.4f})")
        sys.exit(1)

    print("\nno regressions detected")
    sys.exit(0)


if __name__ == "__main__":
    main()
