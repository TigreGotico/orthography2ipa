#!/usr/bin/env python3
"""Fail when a pull request would revert board rows already merged on dev.

This repository squash-merges, and every wave regenerates the benchmark
board (``benchmarks/results.json``, ``benchmarks/results_ci_sample.json``,
``docs/scoreboard.md``) from whatever ``dev`` looked like when the branch
was cut. Rows the branch never touched keep the values they had at that
point. If other waves land meanwhile, those carried-over values are older
than ``dev``'s, and the squash writes them back over the merged results.
The regression gate never sees it: both sides are internally consistent,
so CI is green on the branch and green on ``dev``, and the damage exists
only in the interaction. A single stale branch has carried five merged
waves' worth of rows backwards at once, including one that had moved from
0.4351 to 0.0535.

The check is a three-way comparison, not a two-way diff, and that is what
makes it decidable. For every ``(lang, dataset)`` row it reads the value on
the merge target, on the branch head, and on the merge base the branch was
cut from:

* head equals target — nothing to say.
* head equals the MERGE BASE while the target has moved on — the branch is
  carrying the pre-existing value verbatim. It cannot be a rescore, because
  the branch never produced this number; it is the number the branch
  inherited. This is a REVERT and no declaration excuses it.
* head differs from both — the branch really did move this row, and the
  question is whether it is entitled to. See ownership below.

Ownership is read off the diff rather than taken on trust. A branch owns a
row if it edits that language's spec (``orthography2ipa/data/<lang>.json``)
or the spec of a language the row's language inherits from, or if the row
is new on both sides and therefore cannot displace anything.

Anything else — most importantly a harness or engine change that legitimately
moves hundreds of rows — has to be declared. A ``Board-Rows:`` line in the
pull request body or in a commit message on the branch names the rows, or
says ``all`` with a reason when a harness change rescored the whole board::

    Board-Rows: mr/wikipron, mr/vox_communis
    Board-Rows: all - stress placement reworked, every row rescored

Declaring ``all`` requires the diff to actually touch harness or engine code,
so it is not a free bypass; and it still does not license a REVERT, because a
row whose value is byte-identical to the merge base was not rescored by this
branch no matter what the branch claims. That asymmetry is the point: the
honest path (declare what you moved) is one line, and the silent path fails.

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

# A change anywhere in the package that is not a language spec, or to the
# harness itself, can move every row at once — that is the movement a
# `Board-Rows: all` declaration is allowed to cover.
_ENGINE_RE = re.compile(
    r"^(orthography2ipa/(?!data/).*\.py|orthography2ipa/data/[^/]+\.py"
    r"|scripts/(benchmark|_gold_build)\.py)$")

_DECLARATION_RE = re.compile(r"^\s*Board-Rows:\s*(.+?)\s*$", re.MULTILINE)


def git(*args, repo="."):
    """Run git in *repo* and return stdout, or None when the ref is absent."""
    proc = subprocess.run(("git", *args), cwd=repo, capture_output=True, text=True)
    if proc.returncode != 0:
        return None
    return proc.stdout


def read_board(rev, path, repo="."):
    """Rows of the board *path* at *rev*, keyed by ``(lang, dataset)``.

    A missing file reads as an empty board so that a branch adding one of
    the board files is compared as pure additions.
    """
    blob = git("show", f"{rev}:{path}", repo=repo)
    if blob is None:
        return {}
    if path.endswith(".md"):
        return _read_markdown(blob)
    return {(r["lang"], r["dataset"]): r for r in json.loads(blob)}


def _read_markdown(text):
    """Table rows of the scoreboard keyed by ``(lang, dataset)``.

    The row's whole rendered line is its value: the markdown is generated
    from the JSON, so any cell moving is the same event as the JSON row
    moving, and comparing the line needs no column schema.
    """
    rows = {}
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0] in ("Lang", "---") or set(cells[0]) <= {"-", ":"}:
            continue
        rows[(cells[0], cells[1])] = line.strip()
    return rows


def spec_ancestors(lang, repo="."):
    """*lang* and every language it inherits its tables from.

    Follows ``parent`` and the ``*_base`` table references, so editing
    ``pt-PT.json`` accounts for the movement it causes in ``pt-PT-x-lisbon``.
    """
    seen, queue = set(), [lang]
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


def classify(mb_rows, base_rows, head_rows, owns_lang, declared, engine_touched):
    """Split the rows that differ between head and target into verdicts.

    ``owns_lang`` answers whether the diff edits the spec of a language,
    or of one it inherits from. Returns ``(reverts, undeclared, allowed)``;
    each entry is ``(key, base_value, head_value)``.
    """
    declared_rows, declares_all, reason = declared
    reverts, undeclared, allowed = [], [], []
    for key in sorted(set(mb_rows) | set(base_rows) | set(head_rows)):
        base_v, head_v, mb_v = base_rows.get(key), head_rows.get(key), mb_rows.get(key)
        if head_v == base_v:
            continue
        if head_v == mb_v:
            reverts.append((key, base_v, head_v))
            continue
        if key not in mb_rows and key not in base_rows:
            allowed.append((key, base_v, head_v))
            continue
        if owns_lang(key[0]) or key in declared_rows:
            allowed.append((key, base_v, head_v))
        elif declares_all and engine_touched and reason:
            allowed.append((key, base_v, head_v))
        else:
            undeclared.append((key, base_v, head_v))
    return reverts, undeclared, allowed


def _per(value):
    if value is None:
        return "(absent)"
    if isinstance(value, dict):
        return f"per={value.get('per')} n={value.get('n')}"
    cells = [c.strip() for c in value.strip().strip("|").split("|")]
    return f"per={cells[3]} n={cells[2]}" if len(cells) > 3 else "present"


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

    changed = (git("diff", "--name-only", merge_base, head, repo=repo) or "").split()
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

    failed = False
    for path in (*BOARD_JSON, SCOREBOARD_MD):
        mb_rows = read_board(merge_base, path, repo=repo)
        base_rows = read_board(base, path, repo=repo)
        head_rows = read_board(head, path, repo=repo)
        reverts, undeclared, allowed = classify(
            mb_rows, base_rows, head_rows, owns_lang, declared, engine_touched)

        if reverts:
            failed = True
            print(f"\n{path}: {len(reverts)} row(s) would REVERT work already "
                  f"on {base}.")
            for key, base_v, head_v in reverts:
                if head_v is None:
                    what = f"{base} added this row; the branch predates it"
                elif base_v is None:
                    what = f"{base} removed this row; the branch would restore it"
                else:
                    what = (f"{base} has {_per(base_v)}, the branch carries "
                            f"{_per(head_v)} — the value it inherited when it "
                            f"was cut")
                print(f"  {key[0]} ({key[1]}): {what}, so the merge writes "
                      f"{base}'s newer result away.")
            print(f"  Fix: merge {base} into the branch, re-resolve the board "
                  f"files keeping {base}'s value for every row you did not "
                  f"rescore yourself, and regenerate docs/scoreboard.md.")

        if undeclared:
            failed = True
            print(f"\n{path}: {len(undeclared)} row(s) moved without ownership "
                  f"evidence or a Board-Rows declaration.")
            for key, base_v, head_v in undeclared:
                print(f"  {key[0]} ({key[1]}): {base} has {_per(base_v)}, this "
                      f"branch has {_per(head_v)} — no spec edit for {key[0]} "
                      f"in this diff.")
            print("  Fix: if the move is real, declare it — 'Board-Rows: "
                  "lang/dataset, ...' in the PR body, or 'Board-Rows: all - "
                  "<reason>' for a harness change that rescored everything. "
                  f"If it is not, keep {base}'s value.")

        if allowed:
            print(f"{path}: {len(allowed)} row(s) moved, all accounted for")

    if failed:
        return 1
    print(f"\nboard is not reverting anything on {base}")
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
