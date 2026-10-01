#!/usr/bin/env python3
"""Fail when a committed board disagrees with what a touched spec now
produces.

``tests/test_thin_row_marker.py::test_committed_scoreboard_is_in_sync_with_generator``
guards a narrower thing than its name suggests: it regenerates
``docs/scoreboard.md`` from ``benchmarks/results.json`` and checks the two
agree with EACH OTHER. That catches a stale markdown render; it says nothing
about whether the numbers in ``results.json`` still describe what the specs
actually do. A pull request that edits a grapheme table moves the true PER for
every row scored against that spec, and if the board is not regenerated the
mutual-consistency check stays green while every affected row quietly lies —
this is exactly the failure PR #1425 hit on ``lmo``/``wikipron``.

This script closes that hole by rescoring, for real, only the rows a pull
request is capable of having moved: it diffs against *base* to find which
spec files under ``orthography2ipa/data/`` changed, resolves board language
tags to the spec they are scored against (inheritance included, so an edit to
``pt-PT.json`` also implicates ``pt-PT-x-lisbon``), and re-runs each such
row's own gold loader against the current checkout. A row whose freshly
measured PER — rounded to the same four decimals the board stores — no longer
matches the committed value is stale, and the message names the row, both
numbers, and the exact command to refresh it.

There are TWO committed board files and both are checked, independently,
against the same touched-spec set: the FULL, published board
(``benchmarks/results.json``) and the uniform-sample CI baseline
(``benchmarks/results_ci_sample.json``, every dataset/language capped at
``benchmark.CI_SAMPLE_LIMIT``). Checking only the full board would have missed
exactly the failure PR #1425 hit a second time: the sample file went stale
too, and nothing generic caught it — ``test_check_benchmark_regression.py``'s
``TestCiSampleMatchesFullBelowCap`` only fires when a row's ``n`` matches
between the two files (proving the CI run's cap never truncated it), so a row
whose sample genuinely is a subset (``n`` above the cap) has no cross-check at
all. Rescoring the sample directly closes that gap for every row, truncated
or not, rather than only the ones a coincidence of size happens to expose.
Doing so is only sound because each loader's truncation is DETERMINISTIC for a
fixed ``limit``: every loader either takes a stable prefix of a stable fetch
order, or (``portuguese_unified``) draws a fixed-seed
(``benchmark.SAMPLE_SEED``) ``random.Random`` sample — never the unseeded
global RNG — so re-running a capped loader at the same ``limit`` reproduces
the identical word set the committed sample was built from, and the PER
comparison is apples-to-apples rather than two different subsets compared as
if they were the same measurement. Each committed row's own ``limit`` field
says which cap it was built at (``None`` for the full board,
``CI_SAMPLE_LIMIT`` for the sample), so one rescoring path serves both files.

Rescoring is bounded by the diff, not the board: a spec-only PR pays for the
handful of rows it can have touched, never the full ~371-language board. But
"handful" is a typical case, not a guarantee — a widely-inherited PARENT
spec (``en-GB.json``, ``pt-PT.json``, a hub language several dialects
declare tables against) can own many rows across many datasets at once.
Editing ``en-GB.json`` alone owns 8 rows spanning ``cmudict``, ``ipadict``,
``wikipron``, ``ipa_babylm`` and ``ipa_childes`` — roughly half a million
word pairs — and measuring those took over five minutes in one run with no
completed row yet. This script never trades that honesty for speed: it does
not sample, cap or skip rows to hit a time budget, because a check that
passes on a subset it chose for itself is the same silent hole this PR
exists to close, only moved one level up. What it does instead is stay
loud while it works (see the per-row progress line below) and cheap to
interrupt safely, and the CI job wrapping it carries a generous but finite
``timeout-minutes`` so a genuine hang fails the build instead of tying up a
runner indefinitely. A harness or engine change (:data:`_ENGINE_RE` in
``check_board_not_reverting.py``) can move every row and is out of scope
here — that is what the regression gate and the reverting guard already
cover between them.

A dataset whose gold could not be fetched in this environment (no network, a
missing optional dependency) is reported and SKIPPED rather than failed: a
sandboxed rerun must never manufacture a false positive out of its own
limits. It is never silent about it — the language and dataset are named on
stderr so a reader can tell a real skip from a real match. A row that fetches
fine but scores zero covered words is a hard failure (a broken loader or a
spec that dropped a language cannot pass by looking like an unreachable
network), matching :func:`benchmark.build_scoreboard`'s own zero-coverage
refusal.

A skip is a genuine result only when it is partial: if SOME owned rows in a
board are verified, an unverified remainder is reported in the summary line
rather than folded into a silent pass. If EVERY owned row in a board skips,
that board's run has verified nothing about its freshness at all, and that is
reported as a failure rather than as the vacuous pass this whole check exists
to eliminate elsewhere — a run that confirms nothing must never render the
same as a run that confirmed everything. The two board files are judged
independently: the full board verifying fine never excuses the sample
skipping wholesale, or the reverse.

Before rescoring each row, its name is printed so a slow run shows what it
is currently doing rather than going silent. If the process is interrupted
(SIGTERM — a CI job timeout — or SIGINT/Ctrl-C) before it finishes, it
reports exactly which rows it had verified and which it never reached,
because a run that got killed partway through is not evidence the board is
fresh and must never be mistaken for one that finished clean.

Usage::

    python scripts/check_board_freshness.py --base origin/dev
"""
from __future__ import annotations

import argparse
import json
import os
import signal
import subprocess
import sys
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, os.path.dirname(__file__))

from benchmark import (  # noqa: E402
    CI_SAMPLE_JSON, DATASETS, evaluate_words, SCOREBOARD_JSON,
)
from check_board_not_reverting import (  # noqa: E402
    PackageUnavailable, SPEC_DIR, spec_ancestors,
)

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

#: The board files this check verifies, each paired with the command that
#: refreshes a stale row in it. The full board is refreshed row-by-row
#: (``build_scoreboard`` merges a subset run into the committed set); the CI
#: sample has no such subsetting (``--ci-sample`` always rewrites the whole
#: file from a uniform-limit run), so its fix command is file-wide.
BOARD_FILES: Tuple[Tuple[str, str], ...] = (
    (SCOREBOARD_JSON, "benchmarks/results.json"),
    (CI_SAMPLE_JSON, "benchmarks/results_ci_sample.json"),
)


#: Rows this run has finished (measured or determined unreachable) and rows
#: it has not started yet, both as ``(rel_path, lang, dataset)`` triples.
#: Module-level because the interrupt handler below has to read it from
#: wherever the run currently is when a signal arrives -- there is no
#: return value to thread it through at that point.
_PROGRESS: Dict[str, List[Tuple[str, str, str]]] = {
    "verified": [], "outstanding": [],
}


def _report_interrupted(signum, frame) -> None:
    """Print what this run did and did not get to before dying, then exit
    non-zero. A run killed mid-flight (a CI job timeout, Ctrl-C) must never
    be silent about which rows it never reached -- an operator watching a
    stalled job needs to know it stopped *checking*, not that it *passed*.
    """
    verified = _PROGRESS["verified"]
    outstanding = _PROGRESS["outstanding"]
    print(f"\nINTERRUPTED (signal {signum}) before finishing: "
          f"{len(verified)} row(s) verified, {len(outstanding)} row(s) "
          f"never reached. A timeout or interruption is NOT evidence the "
          f"board is fresh -- these rows were never checked:",
          file=sys.stderr)
    for rel_path, lang, dataset in outstanding:
        print(f"  UNVERIFIED: {rel_path} {lang}/{dataset}", file=sys.stderr)
    for rel_path, lang, dataset in verified:
        print(f"  verified:   {rel_path} {lang}/{dataset}", file=sys.stderr)
    sys.exit(1)


def git(*args, repo=REPO_ROOT) -> Optional[str]:
    proc = subprocess.run(("git", *args), cwd=repo, capture_output=True,
                          text=True)
    if proc.returncode != 0:
        return None
    return proc.stdout


def touched_specs(base: str, head: str = "HEAD", repo=REPO_ROOT) -> set:
    """Language codes whose own spec file differs between *base* and *head*."""
    merge_base = git("merge-base", base, head, repo=repo)
    if merge_base is None:
        sys.exit(f"cannot find a merge base between {base} and {head}")
    changed = (git("diff", "--name-only", merge_base.strip(), head,
                   repo=repo) or "").split()
    return {os.path.basename(p)[:-5] for p in changed
            if p.startswith(SPEC_DIR + "/") and p.endswith(".json")}


def owned_rows(rows: List[dict], specs: set, repo=REPO_ROOT
              ) -> List[dict]:
    """Committed *rows* whose scoring spec (or an ancestor of it) is in
    *specs*, i.e. the rows a change to those spec files can have moved."""
    owned = []
    cache: Dict[str, bool] = {}
    for row in rows:
        lang = row["lang"]
        if lang not in cache:
            cache[lang] = bool(spec_ancestors(lang, repo=repo) & specs)
        if cache[lang]:
            owned.append(row)
    return owned


def rescore(row: dict) -> Tuple[Optional[float], Optional[str]]:
    """Re-measure *row*'s PER against the current checkout, at the SAME
    ``limit`` the row was committed at (``None`` = full gold, an integer =
    the deterministic prefix/fixed-seed-sample that limit produces), so a
    CI-sample row is compared against the identical word set it was scored
    on rather than a differently-sized rescoring of it.

    Returns ``(per, None)`` on a real measurement, or ``(None, reason)``
    when the gold could not be fetched in this environment. Raises on a
    zero-coverage result — that is a real failure, not an environment
    limit, and callers must not swallow it the way a fetch failure is.
    """
    lang, dataset = row["lang"], row["dataset"]
    loader, langs = DATASETS[dataset]
    if lang not in langs:
        return None, f"{lang!r} is no longer registered under {dataset!r}"
    limit = row.get("limit")
    effective = sys.maxsize if limit is None else limit
    try:
        pairs = loader(lang, effective)
    except Exception as exc:  # noqa: BLE001 - environment-dependent fetch
        return None, f"gold unavailable ({exc!r})"
    n, covered, _pers, per, _wer = evaluate_words(
        pairs, lang, strip_stress=True, broad=True)
    if covered == 0:
        raise RuntimeError(
            f"{dataset} lang={lang}: loader returned {n} pairs but scored "
            f"0 of them — a broken loader or a spec that dropped this "
            f"language, not an environment limit")
    return round(per, 4), None


def check_board(path: str, rel_path: str, fix_cmd: str, fix_note: str,
                specs: set, repo=REPO_ROOT) -> int:
    """Verify one committed board *path* against *specs*. Returns an exit
    code: 0 clean/no-op, 1 stale or unverifiable, 2 the package could not be
    imported to resolve board tags at all."""
    if not os.path.exists(path):
        print(f"{rel_path} does not exist; nothing to verify")
        return 0
    with open(path, encoding="utf-8") as fh:
        committed = json.load(fh)

    try:
        rows = owned_rows(committed, specs, repo=repo)
    except PackageUnavailable as exc:
        print(f"cannot import orthography2ipa: {exc}\n"
              f"the check cannot resolve board tags to specs without the "
              f"package installed", file=sys.stderr)
        return 2

    if not rows:
        print(f"{rel_path}: touched spec(s) {sorted(specs)} own no "
              f"committed row; nothing to rescore")
        return 0

    stale, skipped = [], []
    _PROGRESS["outstanding"].extend(
        (rel_path, row["lang"], row["dataset"]) for row in rows)
    for row in rows:
        lang, dataset = row["lang"], row["dataset"]
        key = (rel_path, lang, dataset)
        # Printed BEFORE rescore() runs, and flushed, so a slow row (a
        # widely-inherited parent can own a row with hundreds of thousands
        # of pairs) shows what it is working on instead of going silent.
        print(f"rescoring {rel_path} {lang}/{dataset} "
              f"(limit={row.get('limit')})...", file=sys.stderr, flush=True)
        measured, reason = rescore(row)
        _PROGRESS["outstanding"].remove(key)
        _PROGRESS["verified"].append(key)
        if reason is not None:
            print(f"SKIP {rel_path} {lang}/{dataset}: {reason} — cannot "
                  f"verify this row's freshness in this environment",
                  file=sys.stderr)
            skipped.append((lang, dataset, reason))
            continue
        if measured != row["per"]:
            stale.append((lang, dataset, row["per"], measured))

    verified = len(rows) - len(skipped)

    if skipped and not verified:
        # Every owned row skipped: a run that verifies nothing must not
        # read as a pass just because it also found nothing stale. That is
        # the same "green either way" shape this whole check exists to
        # close — only here the blind spot would be the check itself.
        print(f"COULD NOT VERIFY {rel_path}: all {len(rows)} row(s) owned "
              f"by the touched spec(s) were skipped, so this run confirms "
              f"NOTHING about this board's freshness. Reasons:",
              file=sys.stderr)
        for lang, dataset, reason in skipped:
            print(f"  {lang}/{dataset}: {reason}", file=sys.stderr)
        print("Rerun where this gold is reachable, or accept the risk "
              "explicitly rather than reading this as a pass.",
              file=sys.stderr)
        return 1

    if skipped:
        print(f"{rel_path}: {verified} of {len(rows)} owned row(s) "
              f"verified against the current checkout; {len(skipped)} "
              f"skipped (gold unavailable here, see stderr) and NOT "
              f"verified", file=sys.stderr)
    else:
        print(f"{rel_path}: {verified} row(s) owned by the touched spec(s) "
              f"match what the current checkout measures")

    if not stale:
        return 0

    print(f"STALE BOARD ({rel_path}): the following committed rows no "
          f"longer match what the current spec produces:", file=sys.stderr)
    for lang, dataset, committed_per, measured_per in stale:
        print(f"  {lang}/{dataset}: committed per={committed_per} but the "
              f"current spec measures {measured_per}. Fix: "
              f"{fix_cmd.format(lang=lang, dataset=dataset)}",
              file=sys.stderr)
    print(f"then commit {fix_note}", file=sys.stderr)
    return 1


def check(base: str, head: str = "HEAD", repo=REPO_ROOT) -> int:
    _PROGRESS["verified"].clear()
    _PROGRESS["outstanding"].clear()
    # SIGTERM is what a CI job timeout (and `kill`) sends; SIGINT is
    # Ctrl-C. Both must report what was and was not reached rather than
    # letting the process vanish silently -- see _report_interrupted.
    signal.signal(signal.SIGTERM, _report_interrupted)
    signal.signal(signal.SIGINT, _report_interrupted)

    specs = touched_specs(base, head, repo=repo)
    if not specs:
        print("no orthography2ipa/data/*.json spec changed against "
              f"{base}; nothing this row-freshness check can catch moved")
        return 0

    rc = 0
    rc = max(rc, check_board(
        SCOREBOARD_JSON, "benchmarks/results.json",
        "python scripts/benchmark.py --scoreboard --lang {lang} "
        "--dataset {dataset}",
        "the regenerated benchmarks/results.json and docs/scoreboard.md.",
        specs, repo=repo))
    rc = max(rc, check_board(
        CI_SAMPLE_JSON, "benchmarks/results_ci_sample.json",
        "python scripts/benchmark.py --ci-sample  # rewrites the WHOLE "
        "sample file, no per-row subsetting",
        "the regenerated benchmarks/results_ci_sample.json.",
        specs, repo=repo))
    return rc


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--base", default="origin/dev",
                    help="Branch/ref to diff against (default: origin/dev)")
    ap.add_argument("--head", default="HEAD")
    args = ap.parse_args()
    sys.exit(check(args.base, args.head))


if __name__ == "__main__":
    main()
