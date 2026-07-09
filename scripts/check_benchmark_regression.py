#!/usr/bin/env python3
"""Fail CI when a PR worsens PER against the committed benchmark baseline.

Reuses :func:`scripts.benchmark.build_scoreboard` (no duplicated
loading/scoring logic) to re-run every registered gold dataset/language
combination against the current checkout, then compares each resulting
row's PER to the matching row already committed in
``benchmarks/results.json`` (written by ``scripts/benchmark.py
--scoreboard``, see PR #76).

A row regresses when its new PER exceeds the baseline PER by more than
an absolute epsilon (default ``0.005`` — small enough to catch a real
grapheme/allophone regression, large enough to absorb harness-level
float noise between runs).

Datasets that need packages not installable in a plain CI runner
(``portuguese_lexicon`` needs ``tugalex``, ``cmudict`` needs
``scriptconv``, both TigreGotico-internal) fail to load and are
skipped by ``build_scoreboard`` itself (catch-and-skip, matching PR
#76's existing behavior); this script does not treat those absences as
regressions, it only notes them. Baseline rows with no corresponding
new row (skipped dataset) are noted, not scored. New rows with no
baseline match (e.g. a language added since the baseline was
committed) are noted, not scored, since there is nothing to regress
against.

Usage::

    python scripts/check_benchmark_regression.py
    python scripts/check_benchmark_regression.py --epsilon 0.01 --limit 300
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Dict, List, Tuple

sys.path.insert(0, os.path.dirname(__file__))

from benchmark import build_scoreboard, REPO_ROOT, SCOREBOARD_JSON  # noqa: E402

DEFAULT_EPSILON = 0.005


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


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--epsilon", type=float, default=DEFAULT_EPSILON,
                     help=f"Max allowed absolute PER worsening vs. "
                          f"baseline before a row counts as a regression "
                          f"(default {DEFAULT_EPSILON}).")
    ap.add_argument("--limit", type=int, default=300,
                     help="Rows per dataset/lang to evaluate (passed "
                          "through to build_scoreboard).")
    ap.add_argument("--baseline", default=SCOREBOARD_JSON,
                     help="Path to the committed baseline JSON "
                          "(default benchmarks/results.json).")
    args = ap.parse_args()

    baseline = load_baseline(args.baseline)
    current = build_scoreboard(args.limit)

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
