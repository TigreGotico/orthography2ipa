#!/usr/bin/env python3
"""Fail when a committed board disagrees with what a touched spec now
produces.

``tests/test_thin_row_marker.py::test_committed_scoreboard_is_in_sync_with_generator``
guards a narrower thing than its name suggests: it regenerates
``docs/evaluation/generated/scoreboard.md`` from ``benchmarks/results.json`` and checks the two
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
measured PER or stress columns — rounded to the same four decimals the board
stores — no longer match the committed values is stale, and the message names
the row, the field, both numbers, and the exact command to refresh it.

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
"handful" is a typical case, not a guarantee. A widely-inherited parent or
clade spec (``en-GB.json``, ``pt-PT.json``, ``iir.json``, a hub language
several dialects declare tables against) owns every row of every language
that inherits from it. An edit to ``iir.json`` and the other clade specs of
PR #1921 owned 178 rows in each board file, about 2.7 million word pairs,
and one CI job measured 152 of them in 45 minutes before it was cancelled.
This script never trades that honesty for speed: it does not sample, cap or
skip rows to hit a time budget, because a check that passes on a subset it
chose for itself is the same silent hole this PR exists to close, only moved
one level up. It splits the work instead. ``--plan-out`` writes the owned
rows to a plan file and assigns each row to one shard, balancing the shards
by the word count each row committed (:func:`assign_shards`). ``--shard``
measures one shard's rows and writes their results; CI runs the shards as
parallel jobs. ``--aggregate`` reads the plan and every shard's results and
gives the verdict. A planned row with no result (a shard that crashed, timed
out or never ran) is reported as unverified and fails the check, so a lost
shard can never read as a pass. Without any of these options the script
plans, measures and judges every owned row in one process. A harness or
engine change (:data:`_ENGINE_RE` in ``check_board_not_reverting.py``) can
move every row and is out of scope here — that is what the regression gate
and the reverting guard already cover between them.

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

    # the same check split into shards, as CI runs it
    python scripts/check_board_freshness.py --base origin/dev --plan-out plan.json
    python scripts/check_board_freshness.py --plan plan.json --shard 0 --results-out results/0.json
    python scripts/check_board_freshness.py --plan plan.json --aggregate results/
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
    CI_SAMPLE_JSON, DATASETS, evaluate_words, SCOREBOARD_JSON, StressTally,
)
from check_board_not_reverting import (  # noqa: E402
    PackageUnavailable, SPEC_DIR, spec_ancestors,
)

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

#: The board files this check verifies, keyed by their path in the repo,
#: each paired with the command that refreshes a stale row in it and the
#: files to commit afterwards. The full board is refreshed row-by-row
#: (``build_scoreboard`` merges a subset run into the committed set); the CI
#: sample has no such subsetting (``--ci-sample`` always rewrites the whole
#: file from a uniform-limit run), so its fix command is file-wide.
BOARD_FIXES: Dict[str, Tuple[str, str]] = {
    "benchmarks/results.json": (
        "python scripts/benchmark.py --scoreboard --lang {lang} "
        "--dataset {dataset}",
        "the regenerated benchmarks/results.json and "
        "docs/evaluation/generated/scoreboard.md."),
    "benchmarks/results_ci_sample.json": (
        "python scripts/benchmark.py --ci-sample  # rewrites the WHOLE "
        "sample file, no per-row subsetting",
        "the regenerated benchmarks/results_ci_sample.json."),
}

#: Word pairs one shard is planned to measure. The slowest rows a hosted CI
#: runner scored (``pt-BR/ipadict`` and the ``pt-BR-x-*``
#: ``portuguese_unified`` rows) ran at about 450 word pairs a second, so a
#: full shard takes about 15 minutes there.
SHARD_WORDS = 400_000

#: The most shards one plan asks for. At this cap even an edit that owned
#: every row of the full board (about 10.3 million word pairs) leaves each
#: shard under 25 minutes at the slowest measured rate, inside the shard
#: job's 45-minute limit.
MAX_SHARDS = 16


def board_paths() -> Dict[str, str]:
    """Each board file's repo path mapped to its path on disk. Read at call
    time, not import time, so a test can point a board somewhere else."""
    return {"benchmarks/results.json": SCOREBOARD_JSON,
            "benchmarks/results_ci_sample.json": CI_SAMPLE_JSON}


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


#: The measured row fields this check compares. A committed row that predates
#: a field does not carry it, and that field is not compared for it.
CHECKED_FIELDS = ("per", "stress_acc", "n_stress")


def rescore(row: dict) -> Tuple[Optional[dict], Optional[str]]:
    """Re-measure *row*'s PER and stress columns against the current
    checkout, at the SAME
    ``limit`` the row was committed at (``None`` = full gold, an integer =
    the deterministic prefix/fixed-seed-sample that limit produces), so a
    CI-sample row is compared against the identical word set it was scored
    on rather than a differently-sized rescoring of it.

    Returns ``({field: value}, None)`` for every :data:`CHECKED_FIELDS`
    entry on a real measurement, or ``(None, reason)`` when the gold could
    not be fetched in this environment. Raises on a
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
    stress = StressTally()
    n, covered, _pers, per, _wer = evaluate_words(
        pairs, lang, strip_stress=True, broad=True, stress=stress)
    if covered == 0:
        raise RuntimeError(
            f"{dataset} lang={lang}: loader returned {n} pairs but scored "
            f"0 of them — a broken loader or a spec that dropped this "
            f"language, not an environment limit")
    return {
        "per": round(per, 4),
        "stress_acc": (None if stress.accuracy is None
                       else round(stress.accuracy, 4)),
        "n_stress": stress.eligible,
    }, None


def assign_shards(weights: List[int], shard_words: int = SHARD_WORDS,
                  max_shards: int = MAX_SHARDS) -> Tuple[int, List[int]]:
    """Split rows of these *weights* (word pairs) into balanced shards.

    Returns ``(shard_count, shard_of_each_row)``. The count is the total
    weight over *shard_words*, rounded up and capped at *max_shards* and at
    the number of rows. Each row, heaviest first, goes to the shard with the
    least weight so far, so the slowest shard stays close to the mean.
    """
    if not weights:
        return 0, []
    count = min(len(weights), max_shards,
                max(1, -(-sum(weights) // shard_words)))
    loads = [0] * count
    shards = [0] * len(weights)
    for i in sorted(range(len(weights)), key=lambda i: -weights[i]):
        shard = min(range(count), key=loads.__getitem__)
        shards[i] = shard
        loads[shard] += weights[i]
    return count, shards


def plan(base: str, head: str = "HEAD", repo=REPO_ROOT,
         shard_words: int = SHARD_WORDS,
         max_shards: int = MAX_SHARDS) -> dict:
    """The rows this check must measure, each assigned to a shard.

    Returns a JSON-ready dict: the *base* ref, the commit *head* resolves to,
    the touched specs, the shard count, and for each board file the list of
    ``{"shard": k, "row": committed_row}`` entries it owns (``None`` when
    the board file does not exist). Raises :class:`PackageUnavailable` when
    board tags cannot be resolved to specs.
    """
    specs = touched_specs(base, head, repo=repo)
    boards: Dict[str, Optional[List[dict]]] = {}
    for rel_path, path in board_paths().items():
        if not os.path.exists(path):
            boards[rel_path] = None
            continue
        with open(path, encoding="utf-8") as fh:
            committed = json.load(fh)
        rows = owned_rows(committed, specs, repo=repo) if specs else []
        boards[rel_path] = [{"shard": 0, "row": row} for row in rows]
    entries = [e for rows in boards.values() for e in rows or ()]
    count, shards = assign_shards(
        [max(e["row"].get("n") or 0, 1) for e in entries],
        shard_words, max_shards)
    for entry, shard in zip(entries, shards):
        entry["shard"] = shard
    return {"base": base,
            "head": (git("rev-parse", head, repo=repo) or "").strip(),
            "specs": sorted(specs), "shards": count, "boards": boards}


def measure(tasks: List[Tuple[str, dict]]) -> List[dict]:
    """Rescore each ``(rel_path, row)`` task against the current checkout.

    Returns one result per task: the board, ``lang`` and ``dataset``, the
    skip reason (``None`` for a real measurement), and every
    :data:`CHECKED_FIELDS` entry whose committed value differs from the
    measured one, as ``[field, committed, measured]``.
    """
    _PROGRESS["outstanding"].extend(
        (rel_path, row["lang"], row["dataset"]) for rel_path, row in tasks)
    results = []
    for rel_path, row in tasks:
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
        result = {"board": rel_path, "lang": lang, "dataset": dataset,
                  "skip": reason, "stale": []}
        if reason is not None:
            print(f"SKIP {rel_path} {lang}/{dataset}: {reason} — cannot "
                  f"verify this row's freshness in this environment",
                  file=sys.stderr)
        else:
            result["stale"] = [
                [field, row[field], measured[field]]
                for field in CHECKED_FIELDS
                if field in row and measured[field] != row[field]]
        results.append(result)
    return results


def report_stale(rel_path: str, results: List[dict]) -> bool:
    """Print every stale field among *results* with its fix command.
    Returns whether any row was stale."""
    stale = [(r["lang"], r["dataset"], field, committed, measured)
             for r in results for field, committed, measured in r["stale"]]
    if not stale:
        return False
    fix_cmd, fix_note = BOARD_FIXES[rel_path]
    print(f"STALE BOARD ({rel_path}): the following committed rows no "
          f"longer match what the current spec produces:", file=sys.stderr)
    for lang, dataset, field, committed, measured in stale:
        print(f"  {lang}/{dataset}: committed {field}={committed} but the "
              f"current spec measures {measured}. Fix: "
              f"{fix_cmd.format(lang=lang, dataset=dataset)}",
              file=sys.stderr)
    print(f"then commit {fix_note}", file=sys.stderr)
    return True


def judge_board(rel_path: str, entries: Optional[List[dict]],
                results: Dict[Tuple[str, str, str], dict],
                specs: List[str]) -> int:
    """The verdict on one board file: 0 clean or nothing owned, 1 stale,
    unverifiable or incomplete. *results* maps ``(board, lang, dataset)``
    to that row's result, from however many shards measured them."""
    if entries is None:
        print(f"{rel_path} does not exist; nothing to verify")
        return 0
    if not entries:
        print(f"{rel_path}: touched spec(s) {specs} own no committed row; "
              f"nothing to rescore")
        return 0

    keys = [(rel_path, e["row"]["lang"], e["row"]["dataset"])
            for e in entries]
    missing = [key for key in keys if key not in results]
    got = [results[key] for key in keys if key in results]
    skipped = [r for r in got if r["skip"] is not None]
    verified = len(got) - len(skipped)

    rc = 0
    if missing:
        # A shard that crashed, timed out or never ran leaves its rows with
        # no result. They were never checked, and must never be folded into
        # a pass.
        print(f"UNVERIFIED {rel_path}: {len(missing)} of {len(entries)} "
              f"owned row(s) have no result, so this run never checked "
              f"them. A lost shard is NOT evidence the board is fresh:",
              file=sys.stderr)
        for _, lang, dataset in missing:
            print(f"  UNVERIFIED: {rel_path} {lang}/{dataset}",
                  file=sys.stderr)
        rc = 1

    if skipped and not verified:
        # Every measured row skipped: a run that verifies nothing must not
        # read as a pass just because it also found nothing stale. That is
        # the same "green either way" shape this whole check exists to
        # close — only here the blind spot would be the check itself.
        print(f"COULD NOT VERIFY {rel_path}: all {len(got)} measured "
              f"row(s) owned by the touched spec(s) were skipped, so this "
              f"run confirms NOTHING about this board's freshness. Reasons:",
              file=sys.stderr)
        for r in skipped:
            print(f"  {r['lang']}/{r['dataset']}: {r['skip']}",
                  file=sys.stderr)
        print("Rerun where this gold is reachable, or accept the risk "
              "explicitly rather than reading this as a pass.",
              file=sys.stderr)
        return 1

    if skipped:
        print(f"{rel_path}: {verified} of {len(entries)} owned row(s) "
              f"verified against the current checkout; {len(skipped)} "
              f"skipped (gold unavailable here, see stderr) and NOT "
              f"verified", file=sys.stderr)
    elif not missing:
        print(f"{rel_path}: {verified} row(s) owned by the touched spec(s) "
              f"match what the current checkout measures")

    if report_stale(rel_path, got):
        rc = 1
    return rc


def judge(planned: dict, results: List[dict]) -> int:
    """The verdict over every board file in *planned*, given the *results*
    of every shard that ran."""
    if not planned["specs"]:
        print("no orthography2ipa/data/*.json spec changed against "
              f"{planned['base']}; nothing this row-freshness check can "
              f"catch moved")
        return 0
    by_key: Dict[Tuple[str, str, str], dict] = {}
    for r in results:
        key = (r["board"], r["lang"], r["dataset"])
        if key in by_key:
            print(f"{r['board']} {r['lang']}/{r['dataset']} was measured "
                  f"by more than one shard; the plan and its results do "
                  f"not belong together", file=sys.stderr)
            return 1
        by_key[key] = r
    rc = 0
    for rel_path, entries in planned["boards"].items():
        rc = max(rc, judge_board(rel_path, entries, by_key,
                                 planned["specs"]))
    return rc


def _install_interrupt_report() -> None:
    _PROGRESS["verified"].clear()
    _PROGRESS["outstanding"].clear()
    # SIGTERM is what a CI job timeout (and `kill`) sends; SIGINT is
    # Ctrl-C. Both must report what was and was not reached rather than
    # letting the process vanish silently -- see _report_interrupted.
    signal.signal(signal.SIGTERM, _report_interrupted)
    signal.signal(signal.SIGINT, _report_interrupted)


def _report_package_unavailable(exc: PackageUnavailable) -> None:
    print(f"cannot import orthography2ipa: {exc}\n"
          f"the check cannot resolve board tags to specs without the "
          f"package installed", file=sys.stderr)


def _tasks(planned: dict, shard: Optional[int] = None
           ) -> List[Tuple[str, dict]]:
    return [(rel_path, e["row"])
            for rel_path, entries in planned["boards"].items()
            for e in entries or ()
            if shard is None or e["shard"] == shard]


def check(base: str, head: str = "HEAD", repo=REPO_ROOT) -> int:
    """Plan, measure and judge every owned row in this one process."""
    _install_interrupt_report()
    try:
        planned = plan(base, head, repo=repo)
    except PackageUnavailable as exc:
        _report_package_unavailable(exc)
        return 2
    return judge(planned, measure(_tasks(planned)))


def run_shard(planned: dict, shard: int, results_out: str,
              repo=REPO_ROOT) -> int:
    """Measure the rows *planned* assigns to *shard* and write their
    results to *results_out*. Returns 1 when one of them is stale."""
    head = (git("rev-parse", "HEAD", repo=repo) or "").strip()
    if head != planned["head"]:
        print(f"this checkout is {head or 'unknown'}, but the plan was made "
              f"on {planned['head']}; a shard must measure the commit its "
              f"plan describes", file=sys.stderr)
        return 1
    if not 0 <= shard < planned["shards"]:
        print(f"shard {shard} is outside the plan's {planned['shards']} "
              f"shard(s)", file=sys.stderr)
        return 1
    _install_interrupt_report()
    results = measure(_tasks(planned, shard))
    with open(results_out, "w", encoding="utf-8") as fh:
        json.dump({"head": head, "shard": shard, "results": results}, fh,
                  ensure_ascii=False, indent=1)
    skipped = sum(r["skip"] is not None for r in results)
    print(f"shard {shard} of {planned['shards']}: measured {len(results)} "
          f"row(s), {skipped} skipped; --aggregate gives the verdict over "
          f"every shard")
    stale = [report_stale(rel_path,
                          [r for r in results if r["board"] == rel_path])
             for rel_path in planned["boards"]]
    return int(any(stale))


def aggregate(planned: dict, results_dir: str) -> int:
    """Judge *planned* from every shard result file in *results_dir*."""
    results: List[dict] = []
    names = sorted(n for n in os.listdir(results_dir) if n.endswith(".json")) \
        if os.path.isdir(results_dir) else []
    for name in names:
        with open(os.path.join(results_dir, name), encoding="utf-8") as fh:
            shard_results = json.load(fh)
        if shard_results["head"] != planned["head"]:
            print(f"{name} measured {shard_results['head']}, but the plan "
                  f"was made on {planned['head']}", file=sys.stderr)
            return 1
        results.extend(shard_results["results"])
    print(f"read {len(names)} shard result file(s) of {planned['shards']} "
          f"planned, {len(results)} row result(s) for "
          f"{len(_tasks(planned))} planned row(s)")
    return judge(planned, results)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--base", default="origin/dev",
                    help="Branch/ref to diff against (default: origin/dev)")
    ap.add_argument("--head", default="HEAD")
    ap.add_argument("--plan-out", metavar="PATH",
                    help="Write the owned rows and their shards to PATH "
                         "and exit without measuring")
    ap.add_argument("--shard-words", type=int, default=SHARD_WORDS,
                    help="Word pairs planned per shard (default: "
                         "%(default)s)")
    ap.add_argument("--max-shards", type=int, default=MAX_SHARDS,
                    help="Most shards one plan asks for (default: "
                         "%(default)s)")
    ap.add_argument("--plan", metavar="PATH",
                    help="A plan written by --plan-out, for --shard or "
                         "--aggregate")
    ap.add_argument("--shard", type=int, metavar="K",
                    help="Measure only shard K of --plan")
    ap.add_argument("--results-out", metavar="PATH",
                    help="Where --shard writes its results")
    ap.add_argument("--aggregate", metavar="DIR",
                    help="Judge --plan from the shard results in DIR")
    args = ap.parse_args()

    if args.plan_out:
        try:
            planned = plan(args.base, args.head,
                           shard_words=args.shard_words,
                           max_shards=args.max_shards)
        except PackageUnavailable as exc:
            _report_package_unavailable(exc)
            sys.exit(2)
        with open(args.plan_out, "w", encoding="utf-8") as fh:
            json.dump(planned, fh, ensure_ascii=False, indent=1)
        loads = [0] * planned["shards"]
        for rel_path, entries in planned["boards"].items():
            for e in entries or ():
                loads[e["shard"]] += max(e["row"].get("n") or 0, 1)
        print(f"planned {len(_tasks(planned))} row(s) owned by "
              f"{len(planned['specs'])} touched spec(s) over "
              f"{planned['shards']} shard(s); word pairs per shard: {loads}")
        sys.exit(0)
    if args.shard is not None or args.aggregate:
        if not args.plan:
            ap.error("--shard and --aggregate need --plan")
        with open(args.plan, encoding="utf-8") as fh:
            planned = json.load(fh)
        if args.aggregate:
            sys.exit(aggregate(planned, args.aggregate))
        if not args.results_out:
            ap.error("--shard needs --results-out")
        sys.exit(run_shard(planned, args.shard, args.results_out))
    sys.exit(check(args.base, args.head))


if __name__ == "__main__":
    main()
