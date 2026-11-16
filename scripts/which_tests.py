#!/usr/bin/env python3
"""List the test files that assert on a given language spec.

The suite is a broad per-family layout (``test_celtic.py``, ``test_slavic.py``,
...) plus 18 ``test_cited_rules_*.py`` files that pin individual rules back to
their source citation, independently of the family file. A change to one
spec routinely has assertions in both: editing ``gd.json``'s pre-aspiration
rule broke ``test_cited_rules_germanic_celtic.py::test_gd_preasp_c_broad``
while ``tests/test_celtic.py`` stayed green, because the family file and the
cited-rules file assert different words. Nothing maps a spec to the tests
that constrain it, so a contributor who narrows a run to the family file (the
usual advice, since the full suite is expensive) never learns the other file
exists.

The mapping a `grep -rl '"gd"' tests/*.py` would give is the right shape but
tedious to remember and easy to get wrong on short codes. This script does the
grep and a bit more:

* it matches the language code as a **quoted token** (``"gd"``, ``'gd'``),
  which is how a code shows up as a function argument, a dict key, or a
  parametrize entry. A bare substring match on a two- or three-letter code
  (``br``, ``an``, ``ka``, ``is``, ``it``) matches inside unrelated words and
  drowns the real hits in noise;
* by default it also includes every spec that **inherits from** the given
  language (``parent`` or a ``*_base`` table reference, transitively), because
  editing a parent's table can move a child's output through inheritance even
  when no test names the parent directly. This can only add files, so
  ``--no-children`` is there for the rare case where a caller wants the exact
  match only.

False positives cost a contributor a few extra seconds of test time; a missed
file costs a CI failure after the PR looked green locally, which is the
failure mode this exists to prevent. The trade favours over-matching.

With ``--lang`` it reports one language. With ``--base`` (default
``origin/dev``) and no ``--lang`` it looks at which specs the diff against
that base touches, and reports the union of test files for all of them --
the form to run before pushing::

    python scripts/which_tests.py --lang gd
    python scripts/which_tests.py --base origin/dev

It always reports how many test files it searched, alongside the hits (or the
lack of them): "searched 214 test files, none reference ['pox']" tells a
reader the search ran; a bare "none" would not. If ``--repo`` does not point
at a checkout with a ``tests/`` directory and a spec directory, it exits
non-zero naming the path instead of reporting an empty, indistinguishable
"nothing found" -- the whole point of this tool is to prevent a contributor
from mistaking "the search did not run" for "there is nothing to run".
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import subprocess
import sys

_ROOT = os.path.join(os.path.dirname(__file__), "..")
SPEC_DIR = os.path.join(_ROOT, "orthography2ipa", "data")
TEST_DIR = os.path.join(_ROOT, "tests")


def spec_descendants(lang, repo=_ROOT):
    """*lang* and every spec that inherits its tables, directly or not.

    Mirrors ``scripts/check_board_not_reverting.py:spec_ancestors`` but walks
    the ``parent`` / ``*_base`` graph the other way: from a spec to the
    children that reference it, so editing a parent accounts for the children
    its tables move.
    """
    parent_of = {}
    for path in glob.glob(os.path.join(repo, "orthography2ipa", "data", "*.json")):
        code = os.path.splitext(os.path.basename(path))[0]
        try:
            with open(path, encoding="utf-8") as fh:
                spec = json.load(fh)
        except (OSError, ValueError):
            continue
        refs = {spec.get("parent")}
        refs |= {v for k, v in spec.items() if k.endswith("_base") and isinstance(v, str)}
        for ref in refs:
            if ref:
                parent_of.setdefault(ref, set()).add(code)

    seen, queue = set(), [lang]
    while queue:
        code = queue.pop()
        if code in seen:
            continue
        seen.add(code)
        queue += list(parent_of.get(code, ()))
    return seen


class RepoLayoutError(Exception):
    """*repo* does not look like an orthography2ipa checkout.

    Raised instead of silently searching nothing, so a wrong ``--repo`` (or a
    script copied outside the checkout) fails loudly rather than reporting
    "no test file references ..." -- a clean negative that is indistinguishable
    from a genuine all-clear on the one question this tool exists to answer.
    """


def validate_repo(repo):
    """Raise :class:`RepoLayoutError` unless *repo* has a ``tests/`` and a spec directory."""
    tests_dir = os.path.join(repo, "tests")
    spec_dir = os.path.join(repo, "orthography2ipa", "data")
    if not os.path.isdir(tests_dir):
        raise RepoLayoutError(
            f"no tests/ directory under {os.path.abspath(repo)!r} -- "
            "this does not look like an orthography2ipa checkout, "
            "pass --repo pointing at one"
        )
    if not os.path.isdir(spec_dir):
        raise RepoLayoutError(
            f"no orthography2ipa/data/ directory under {os.path.abspath(repo)!r} -- "
            "this does not look like an orthography2ipa checkout, "
            "pass --repo pointing at one"
        )


def matching_test_files(lang, include_children=True, repo=_ROOT):
    """Test files that reference *lang* as a quoted token.

    Returns a sorted list of paths relative to *repo*. Raises
    :class:`RepoLayoutError` if *repo* has no test suite to search, rather
    than returning an empty list indistinguishable from a real "nothing
    references this code".
    """
    validate_repo(repo)
    codes = spec_descendants(lang, repo=repo) if include_children else {lang}
    patterns = [re.compile(r"""(["'])""" + re.escape(code) + r"""\1""") for code in codes]

    test_files = sorted(glob.glob(os.path.join(repo, "tests", "*.py")))
    hits = []
    for path in test_files:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        if any(p.search(text) for p in patterns):
            hits.append(os.path.relpath(path, repo))
    return hits, len(test_files)


def changed_langs(base, head="HEAD", repo=_ROOT):
    """Language codes whose spec file the diff between *base* and *head* touches."""
    out = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...{head}", "--", "orthography2ipa/data/*.json"],
        cwd=repo, capture_output=True, text=True, check=True,
    ).stdout
    langs = set()
    for line in out.splitlines():
        line = line.strip()
        if line.endswith(".json"):
            langs.add(os.path.splitext(os.path.basename(line))[0])
    return langs


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--lang", default=None, help="language/spec code, e.g. gd")
    ap.add_argument("--base", default="origin/dev",
                    help="diff base to derive changed specs from when --lang is not given "
                         "(default origin/dev)")
    ap.add_argument("--head", default="HEAD", help="branch head to diff (default HEAD)")
    ap.add_argument("--repo", default=_ROOT, help="repository root (default the checkout)")
    ap.add_argument("--no-children", dest="children", action="store_false", default=True,
                    help="match the exact code only, not specs that inherit from it")
    args = ap.parse_args()

    try:
        validate_repo(args.repo)
    except RepoLayoutError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.lang:
        langs = {args.lang}
    else:
        langs = changed_langs(args.base, args.head, repo=args.repo)
        if not langs:
            print("no changed language specs found", file=sys.stderr)
            return 0

    files = set()
    total = 0
    for lang in sorted(langs):
        hits, total = matching_test_files(lang, include_children=args.children, repo=args.repo)
        files |= set(hits)

    if not files:
        print(f"searched {total} test files, none reference {sorted(langs)}", file=sys.stderr)
        return 0

    print(f"searched {total} test files, {len(files)} reference {sorted(langs)}:", file=sys.stderr)
    for path in sorted(files):
        print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
