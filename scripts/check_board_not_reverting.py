#!/usr/bin/env python3
"""Fail when merging a pull request would carry benchmark board rows backwards.

The board (``benchmarks/results.json``, ``benchmarks/results_ci_sample.json``,
``docs/scoreboard.md``) is regenerated whole, but a branch only rescores the
rows it worked on; every other row is a copy of the merge target as it stood
when the branch was cut. That staleness is not by itself a problem: the merge
is a three-way merge, so rows the branch never edited keep the target's newer
values and the stale copy never reaches the target.

What does reach the target is a branch that edited the board *and* took its own
side for rows it did not measure — most often by merging the target in and
resolving the conflicted board file by keeping its own file wholesale, but also
by a textual hunk that swallows neighbouring rows. Then the merge really does
write the older number back. Nothing else notices: both sides are internally
consistent, so the regression gate is green on the branch and green on the
target, and the loss exists only in the interaction.

So the check is run on the merge RESULT rather than on the branch's file. It
merges head into the target with ``git merge-tree`` and compares the resulting
board against the target's, row by row, keyed on ``(lang, dataset)``:

* the merged row equals the target's — nothing to say.
* the merged row is a value the target already carried and moved past, for a
  language whose spec the branch does not touch — the merge puts an old number
  back. Prose cannot excuse that; only a spec edit for the language can, since
  that is the one piece of evidence a stale copy cannot produce.
* the merged row is a number neither side has had — the branch really moved
  this row, and the question is whether it is entitled to. See ownership below.

Ownership is read off the diff. A branch owns a row if it edits that language's
spec, or the spec of a language the row's language inherits from, or if the row
is new on both sides and therefore displaces nothing. Board language tags are
resolved to a spec the way the benchmark harness resolves them, so ``de`` is
owned by an edit to ``de-DE.json``. Re-keying a dataset onto a better-fitting
spec shows up as one row dropped and one added, and the branch owns both.

Anything else — most importantly a harness or engine change that legitimately
moves hundreds of rows — has to be declared. A ``Board-Rows:`` line in the pull
request body or in a commit message on the branch names the rows, or says
``all`` with a reason when a harness change rescored the whole board::

    Board-Rows: mr/wikipron, mr/vox_communis
    Board-Rows: all - stress placement reworked, every row rescored

Declaring ``all`` requires the diff to actually touch harness or engine code, so
it is not a free bypass.

Usage::

    python scripts/check_board_not_reverting.py --base origin/dev
    python scripts/check_board_not_reverting.py --base origin/dev --body-file pr.md
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys

BOARD_JSON = ("benchmarks/results.json", "benchmarks/results_ci_sample.json")
SCOREBOARD_MD = "docs/scoreboard.md"
SPEC_DIR = "orthography2ipa/data"

#: How far back down the target's history a board value is still recognised as
#: one the target already moved past. This is the last sixty board-touching
#: commits, which is roughly a week of dev — so the guarantee is bounded by
#: how stale a branch is: a branch cut further back than that can carry a row
#: backwards without the guard recognising the value as one dev moved past.
HISTORY_DEPTH = 60

#: Fields that carry a measurement. Provenance and tier move for reasons that
#: have nothing to do with rescoring, and comparing them produces findings no
#: one can act on.
SCORED_FIELDS = ("n", "per", "per_ci_low", "per_ci_high", "exact_match",
                 "oracle_per_top3", "oracle_exact_top3", "oracle_per_top5",
                 "oracle_exact_top5", "oracle_scored_words",
                 "oracle_fallback_words")

#: The thin-row marker appended to the N column when a row falls below
#: THIN_ROW_N scored words. This is a RENDERING ANNOTATION, not a value
#: change: the underlying N value is unchanged, and a row gaining this marker
#: should not be flagged as movement. This constant MUST be kept in sync with
#: the one in scripts/benchmark.py; when benchmark.py is updated to define or
#: import THIN_ROW_MARK, ensure it uses the same symbol to prevent drift.
THIN_ROW_MARK = "†"

# A change anywhere in the package that is not a language spec, or to the
# harness itself, can move every row at once — that is the movement a
# `Board-Rows: all` declaration is allowed to cover.
_ENGINE_RE = re.compile(
    r"^(orthography2ipa/(?!data/).*\.py|orthography2ipa/data/[^/]+\.py"
    r"|scripts/(benchmark|_gold_build)\.py)$")

_DECLARATION_RE = re.compile(r"^\s*Board-Rows:\s*(.+?)\s*$", re.MULTILINE)


def git(*args, repo="."):
    """Run git in *repo* and return stdout, or None when the command fails."""
    proc = subprocess.run(("git", *args), cwd=repo, capture_output=True, text=True)
    if proc.returncode != 0:
        return None
    return proc.stdout


def merge_tree(base, head, repo="."):
    """The tree of merging *head* into *base*, or None when git cannot.

    Conflicts elsewhere in the tree still yield a usable tree: the board
    files are read out of it individually and a board file that did not
    merge is recognised by its conflict markers.
    """
    proc = subprocess.run(("git", "merge-tree", "--write-tree", base, head),
                          cwd=repo, capture_output=True, text=True)
    tree = proc.stdout.split("\n", 1)[0].strip()
    return tree or None


def read_board(rev, path, repo="."):
    """Rows of the board *path* at *rev*, keyed by ``(lang, dataset)``.

    A missing file reads as an empty board so that a branch adding one of the
    board files is compared as pure additions. A file that failed to merge
    reads as None, which the caller reports and skips.
    """
    blob = git("show", f"{rev}:{path}", repo=repo)
    if blob is None:
        return {}
    if "<<<<<<<" in blob:
        return None
    if path.endswith(".md"):
        return _read_markdown(blob)
    try:
        rows = json.loads(blob)
    except ValueError:
        return None
    return {(r["lang"], r["dataset"]): r for r in rows}


def _read_markdown(text):
    """Table rows of the scoreboard as ``{header: cell}`` dicts.

    The markdown is generated from the JSON, so a cell moving is the same
    event as the JSON row moving; keeping the cells under their column
    headers lets a difference be named rather than just shown.

    The thin-row marker (†) is stripped from the N cell before storing,
    since it is a rendering annotation, not a value change: a row that
    gains the marker due to having fewer than THIN_ROW_N scored words still
    has the same underlying N value.
    """
    rows, headers = {}, []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if set("".join(cells)) <= {"-", ":", " "}:
            continue
        if not headers:
            headers = cells
            continue
        if len(cells) < 2:
            continue
        row = dict(zip(headers, cells))
        # Strip the thin-row marker from the N cell if present, since it is
        # a rendering-only annotation and not a value change.
        if "N" in row and row["N"].endswith(THIN_ROW_MARK):
            row["N"] = row["N"][:-len(THIN_ROW_MARK)]
        rows[(cells[0], cells[1])] = row
    return rows


class PackageUnavailable(RuntimeError):
    """The ``orthography2ipa`` package could not be imported to resolve a tag.

    Raised instead of silently guessing, because a check that blocks work
    must never fail in the direction of blaming the contributor: a bare tag
    like ``de`` would otherwise be treated as its own (nonexistent) spec and
    a legitimate wave touching ``de-DE.json`` would be reported as unowned.
    """


def spec_code(lang, repo="."):
    """The spec a board language tag is scored against.

    A tag with its own spec file is its own spec; the rest are resolved
    through the registry the way the benchmark harness resolves them, so
    ``de`` lands on ``de-DE`` and ``pt-BR-x-carioca`` on ``pt-BR``. Raises
    ``PackageUnavailable`` when the package cannot be imported to do that
    resolution, rather than returning *lang* as if it were its own spec.
    """
    if os.path.exists(os.path.join(repo, SPEC_DIR, f"{lang}.json")):
        return lang
    try:
        from orthography2ipa import get
    except ImportError as exc:
        raise PackageUnavailable(
            f"could not import orthography2ipa to resolve board tag {lang!r}: "
            f"{exc}") from exc
    return get(lang).code


def spec_ancestors(lang, repo="."):
    """*lang*'s spec and every spec it inherits its tables from.

    Follows ``parent`` and the ``*_base`` table references, so editing
    ``pt-PT.json`` accounts for the movement it causes in ``pt-PT-x-lisbon``.
    """
    seen, queue = set(), [spec_code(lang, repo=repo)]
    while queue:
        code = queue.pop()
        if code in seen:
            continue
        seen.add(code)
        try:
            with open(os.path.join(repo, SPEC_DIR, f"{code}.json"), encoding="utf-8") as fh:
                spec = json.load(fh)
        except (OSError, ValueError):
            continue
        refs = [spec.get("parent")]
        refs += [v for k, v in spec.items() if k.endswith("_base") and isinstance(v, str)]
        queue += [r for r in refs if r]
    return seen


def parse_declaration(*texts):
    """Rows and reasons declared by ``Board-Rows:`` lines in *texts*.

    Returns ``(rows, declares_all, reason)`` where ``rows`` is a set of
    ``(lang, dataset)`` keys.
    """
    rows, declares_all, reason = set(), False, ""
    for text in texts:
        for value in _DECLARATION_RE.findall(text or ""):
            parts = re.split(r"\s[-–—]\s", value, 1)
            body, why = parts[0], parts[1] if len(parts) > 1 else ""
            if body.strip().lower() == "all":
                declares_all = True
                reason = reason or why.strip()
                continue
            for item in body.replace(",", " ").split():
                lang, sep, dataset = item.partition("/")
                if sep:
                    rows.add((lang, dataset))
    return rows, declares_all, reason


def scored(row):
    """The comparable part of a row: its measurements, in a stable order."""
    if row is None:
        return None
    keys = [k for k in SCORED_FIELDS if k in row] or sorted(row)
    return {k: row[k] for k in keys}


def classify(base_rows, merged_rows, owns_lang, superseded, declared,
             engine_touched):
    """Split the rows the merge would change into verdicts.

    *base_rows* is the merge target's board and *merged_rows* the board the
    merge would produce. ``owns_lang`` answers whether the diff edits the spec
    of a language, or of one it inherits from; ``superseded`` answers whether a
    value the merge would install is one the target itself already moved past.
    Returns ``(reverts, undeclared, allowed)``; each entry is
    ``(key, base_value, merged_value)``.
    """
    declared_rows, declares_all, reason = declared
    reverts, undeclared, allowed = [], [], []
    # A dataset the branch re-keyed: it added a row for a language whose spec
    # it edits, and that row scores gold the dataset previously contributed
    # under another tag. The old tag's row disappearing is the same event.
    rekeyed = {ds for lang, ds in merged_rows
               if (lang, ds) not in base_rows and owns_lang(lang)}
    for key in sorted(set(base_rows) | set(merged_rows)):
        base_v, merged_v = base_rows.get(key), merged_rows.get(key)
        if scored(merged_v) == scored(base_v):
            continue
        if not owns_lang(key[0]) and superseded(key, merged_v):
            reverts.append((key, base_v, merged_v))
            continue
        if base_v is None:
            allowed.append((key, base_v, merged_v))
            continue
        if merged_v is None and key[1] in rekeyed:
            allowed.append((key, base_v, merged_v))
        elif owns_lang(key[0]) or key in declared_rows:
            allowed.append((key, base_v, merged_v))
        elif declares_all and engine_touched and reason:
            allowed.append((key, base_v, merged_v))
        else:
            undeclared.append((key, base_v, merged_v))
    return reverts, undeclared, allowed


def superseded_values(base, path, keys, repo=".", depth=HISTORY_DEPTH):
    """For each of *keys*, the values *path* has already carried on *base*.

    Walks the target's own history of the board file. A value the merge would
    install that appears here is one the target measured and then moved past:
    whatever the branch believes, it is putting an old number back.
    """
    revs = (git("log", f"-n{depth}", "--format=%H", base, "--", path,
                repo=repo) or "").split()
    seen = {key: [] for key in keys}
    for rev in revs[1:]:
        rows = read_board(rev, path, repo=repo) or {}
        for key in keys:
            value = scored(rows.get(key))
            if value is not None and value not in seen[key]:
                seen[key].append(value)
    return seen


def _delta(base_v, merged_v, base):
    """Prose naming what the merge would do to one row."""
    if merged_v is None:
        return f"the merge drops the row {base} has"
    if base_v is None:
        return f"the merge adds a row {base} does not have"
    fields = [k for k in scored(base_v)
              if base_v.get(k) != merged_v.get(k)] or ["the row"]
    return ", ".join(f"{k} {base_v.get(k)} -> {merged_v.get(k)}" for k in fields)


def check(base, head, repo=".", body=""):
    """Run the guard over every board file. Returns the process exit code."""
    merge_base = git("merge-base", base, head, repo=repo)
    if merge_base is None:
        print(f"cannot find a merge base between {base} and {head}", file=sys.stderr)
        return 2
    merge_base = merge_base.strip()
    head_sha = (git("rev-parse", head, repo=repo) or "").strip()
    if merge_base == head_sha:
        print(f"{head} is already contained in {base}, nothing to compare")
        return 0

    changed = set((git("diff", "--name-only", merge_base, head, repo=repo) or "").split())
    boards = [p for p in (*BOARD_JSON, SCOREBOARD_MD) if p in changed]
    if not boards:
        print("the branch does not touch the board; the merge cannot move a row")
        return 0

    merged = merge_tree(base, head, repo=repo)
    if merged is None:
        print(f"{head} and {base} cannot be merged automatically; "
              f"resolve the merge first")
        return 0

    touched_specs = {os.path.basename(p)[:-5] for p in changed
                     if p.startswith(SPEC_DIR + "/") and p.endswith(".json")}
    engine_touched = any(_ENGINE_RE.match(p) for p in changed)
    messages = git("log", "--format=%B", f"{merge_base}..{head}", repo=repo) or ""
    declared = parse_declaration(body, messages)

    owned_cache = {}

    def owns_lang(lang):
        if lang not in owned_cache:
            owned_cache[lang] = bool(spec_ancestors(lang, repo=repo) & touched_specs)
        return owned_cache[lang]

    try:
        return _run(boards, base, merged, owns_lang, declared, engine_touched, repo=repo)
    except PackageUnavailable as exc:
        print(f"cannot import orthography2ipa: {exc}\n"
              f"the guard cannot resolve board tags to specs without the "
              f"package, so it cannot judge row ownership here; run it with "
              f"PYTHONPATH including the repo root", file=sys.stderr)
        return 2


def _run(boards, base, merged, owns_lang, declared, engine_touched, repo="."):
    """The classification pass over every board file, once ownership can be
    resolved. Split out so a ``PackageUnavailable`` raised while resolving a
    tag is caught in one place rather than guessed at per call site."""
    failed = False
    for path in boards:
        merged_rows = read_board(merged, path, repo=repo)
        if merged_rows is None:
            print(f"{path}: conflicted, resolve the merge first")
            continue
        base_rows = read_board(base, path, repo=repo) or {}
        candidates = [key for key in set(base_rows) | set(merged_rows)
                      if scored(merged_rows.get(key)) != scored(base_rows.get(key))
                      and merged_rows.get(key) is not None
                      and not owns_lang(key[0])]
        history = superseded_values(base, path, candidates, repo=repo)

        def superseded(key, value, history=history):
            return value is not None and scored(value) in history.get(key, ())

        reverts, undeclared, allowed = classify(
            base_rows, merged_rows, owns_lang, superseded, declared, engine_touched)

        if reverts:
            failed = True
            print(f"\n{path}: merging would carry {len(reverts)} row(s) on "
                  f"{base} backwards.")
            for key, base_v, merged_v in reverts:
                print(f"  {key[0]} ({key[1]}): {_delta(base_v, merged_v, base)} "
                      f"— a value {base} already carried and moved past, and "
                      f"this diff does not touch {key[0]}'s spec.")
            print(f"  Fix: merge {base} into the branch and resolve the board "
                  f"files keeping {base}'s value for every row you did not "
                  f"rescore yourself, then regenerate docs/scoreboard.md.")

        if undeclared:
            failed = True
            print(f"\n{path}: merging would move {len(undeclared)} row(s) "
                  f"without ownership evidence or a Board-Rows declaration.")
            for key, base_v, merged_v in undeclared:
                print(f"  {key[0]} ({key[1]}): {_delta(base_v, merged_v, base)} "
                      f"— no spec edit for {key[0]} in this diff.")
            print("  Fix: if the move is real, declare it — 'Board-Rows: "
                  "lang/dataset, ...' in the PR body, or 'Board-Rows: all - "
                  "<reason>' for a harness change that rescored everything. "
                  f"If it is not, keep {base}'s value.")

        if allowed:
            print(f"{path}: {len(allowed)} row(s) moved, all accounted for")

    if failed:
        return 1
    print(f"\nmerging this branch does not carry {base} backwards")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--base", default="origin/dev", help="merge target (default origin/dev)")
    ap.add_argument("--head", default="HEAD", help="branch head to check (default HEAD)")
    ap.add_argument("--repo", default=".", help="repository to check (default .)")
    ap.add_argument("--body-file", default=None,
                    help="file holding the pull request body, read for a "
                         "Board-Rows declaration (the PR_BODY environment "
                         "variable is read too)")
    args = ap.parse_args()

    body = os.environ.get("PR_BODY", "")
    if args.body_file:
        with open(args.body_file, encoding="utf-8") as fh:
            body += "\n" + fh.read()
    sys.exit(check(args.base, args.head, repo=args.repo, body=body))


if __name__ == "__main__":
    main()
