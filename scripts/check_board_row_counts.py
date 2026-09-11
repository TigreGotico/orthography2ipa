#!/usr/bin/env python3
"""Fail when a committed board row scored more words than its gold holds.

Every row in ``benchmarks/results.json`` carries an ``n`` — the number of
gold words that were actually scored for that language/dataset pair. That
number can never exceed the number of pairs the row's loader yields,
because scoring consumes the loader's output and drops from it (words the
spec cannot cover are counted but not scored, so ``n`` sits at or below
the pair count, never above it).

A row whose ``n`` is ABOVE its loader's current pair count is therefore
proof that the row was computed against a gold set that no longer exists.
That is exactly what happened when the ``vox_communis`` loader started
dropping the aligner's ``spn`` coverage-hole marker: the loader shed a
quarter of its pairs for some languages, the board kept scoring the old
count, and 26 rows silently published a PER measured against a gold set
the code had stopped producing. Nothing caught it, because the regression
gate is one-sided and a stale row that reads WORSE than reality never
trips it.

The check is deliberately one-directional. A row whose ``n`` is BELOW the
pair count is normal — Japanese scores 42.5k of 48.6k pairs because the
kana spec produces no hypothesis for a kanji-only word — so a lower bound
would fire on healthy rows. Only the upper bound is an impossibility.

``--tolerance`` absorbs the session-to-session drift of the loaders that
fetch a live snapshot (a re-fetch moves a 141k-row Catalan gold by a
handful of words). It defaults to 1%, which is two orders of magnitude
below the smallest real staleness this has caught.

Rows whose loader refuses the language outright are reported too. A board
row for a language its dataset no longer registers is unreachable by any
code path and can only be a fossil of a de-registration.

Usage::

    PYTHONPATH=$PWD python scripts/check_board_row_counts.py
    PYTHONPATH=$PWD python scripts/check_board_row_counts.py --tolerance 0.02
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from benchmark import DATASETS, SCOREBOARD_JSON  # noqa: E402

# Loading a live-snapshot gold needs the network, and some loaders need an
# optional package (e.g. `rarfile`) that is not installed in every
# environment. Neither is evidence the row is a fossil, so both are
# reported and skipped rather than counted as "no loader will serve them".
_OFFLINE_ERRORS = (OSError, ImportError)


def gold_size(dataset: str, lang: str) -> int:
    """Pair count the *dataset* loader currently yields for *lang*."""
    loader, _langs = DATASETS[dataset]
    return len(loader(lang, sys.maxsize))


def check_rows(rows, tolerance):
    """Return ``(stale, unreachable, skipped)`` for the committed *rows*.

    ``stale`` holds ``(row, gold_n)`` for every row scoring more words
    than its gold holds; ``unreachable`` holds ``(row, reason)`` for rows
    no loader will serve; ``skipped`` holds rows whose gold could not be
    fetched at all.
    """
    stale, unreachable, skipped = [], [], []
    for row in rows:
        dataset, lang = row["dataset"], row["lang"]
        if dataset not in DATASETS:
            unreachable.append((row, f"no dataset named {dataset!r}"))
            continue
        try:
            gold_n = gold_size(dataset, lang)
        except _OFFLINE_ERRORS as exc:
            skipped.append((row, str(exc)))
            continue
        except Exception as exc:
            unreachable.append((row, f"{type(exc).__name__}: {exc}"))
            continue
        if gold_n == 0:
            # A row scoring words against a zero-pair gold isn't drift,
            # it's a fossil — the loader no longer yields anything for
            # this language/dataset pair at all.
            unreachable.append((row, "loader now yields 0 pairs"))
            continue
        if row["n"] > gold_n * (1 + tolerance):
            stale.append((row, gold_n))
    return stale, unreachable, skipped


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--board", default=SCOREBOARD_JSON,
                    help="board file to check (default "
                         "benchmarks/results.json)")
    ap.add_argument("--tolerance", type=float, default=0.01,
                    help="fraction by which a row's n may exceed its "
                         "gold's current pair count before it counts as "
                         "stale (default 0.01)")
    ap.add_argument("--dataset", default=None,
                    help="check only this dataset")
    args = ap.parse_args()

    with open(args.board, encoding="utf-8") as fh:
        rows = json.load(fh)
    if args.dataset:
        rows = [r for r in rows if r["dataset"] == args.dataset]

    stale, unreachable, skipped = check_rows(rows, args.tolerance)

    if skipped:
        print(f"{len(skipped)} row(s) could not be checked (gold "
              f"unavailable here):")
        for row, reason in skipped:
            print(f"  {row['lang']} ({row['dataset']}): {reason}")

    if unreachable:
        print(f"\n{len(unreachable)} row(s) have no loader that will "
              f"serve them:")
        for row, reason in unreachable:
            print(f"  {row['lang']} ({row['dataset']}): n={row['n']} "
                  f"per={row['per']} — {reason}")

    if stale:
        print(f"\n{len(stale)} row(s) scored more words than their gold "
              f"holds (board is stale — regenerate them):")
        for row, gold_n in stale:
            print(f"  {row['lang']} ({row['dataset']}): board n={row['n']} "
                  f"but the loader now yields {gold_n} pairs "
                  f"({row['n'] / gold_n:.2f}x), per={row['per']}")

    if stale or unreachable:
        sys.exit(1)

    print(f"\n{len(rows) - len(skipped)} row(s) checked, none stale")
    sys.exit(0)


if __name__ == "__main__":
    main()
