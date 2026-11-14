#!/usr/bin/env python3
"""Reading order and navigation footers for ``docs/``.

``docs/index.md`` defines the order of the documentation set, and
``docs/languages/index.md`` defines the order of the per-language pages inside
it. The atlas pages follow ``docs/languages/a-z.md`` instead: they come right
after that index, in the order of its "Pages" table, so a new atlas page joins
the set when the atlas generator lists it. This module reads the three pages,
so the order lives in one place instead of being restated in every page.

Every page except ``docs/index.md``, ``docs/README.md`` and the :data:`STUBS`
ends with a footer:
a horizontal rule, then one line linking the previous page, the index, and the
next page, with relative links only.

Generators that write a page under ``docs/`` (the scoreboard, the comparison
table, the espeak agreement report, the spec diagnostics) append
:func:`footer` to their output, so a regenerated page keeps its place in the
set.

Run it to synchronize the hand-written pages after adding, removing, or
reordering one::

    python3 scripts/docs_nav.py --write
    python3 scripts/docs_nav.py --check
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(REPO_ROOT, "docs")
INDEX = "index.md"
LANGUAGES = "languages/index.md"
ATLAS_AZ = "languages/a-z.md"
# Pages that only point to a moved page, kept because other sites link them.
STUBS = {"benchmarks.md", "scoreboard.md"}
NOT_IN_ORDER = {INDEX, "README.md"} | STUBS

_TABLE_LINK = re.compile(r"^\| \[[^\]]+\]\(([^)]+)\)", re.M)
_ANY_LINK = re.compile(r"\]\((?!\.\.)([A-Za-z0-9._-]+\.md)\)")
_FOOTER = re.compile(r"\n*---\n\[[^\n]*\]\([^\n]*\)\s*$")


def _read(rel: str) -> str:
    with open(os.path.join(DOCS, rel), encoding="utf-8") as fh:
        return fh.read()


def atlas_pages(az_text: str | None = None) -> list[str]:
    """The atlas pages, in the order of the "Pages" table of ``a-z.md``.

    The atlas generator passes the text it is about to write as *az_text*,
    because the copy on disk does not list a page it has just added.
    """
    text = _read(ATLAS_AZ) if az_text is None else az_text
    _, found, rest = text.partition("\n## Pages\n")
    if not found:
        return []
    section = rest.split("\n## ", 1)[0]
    return ["languages/" + name for name in _TABLE_LINK.findall(section)]


def reading_order(az_text: str | None = None) -> list[str]:
    """Every page of the set, in reading order, as paths relative to ``docs/``.

    *az_text* replaces ``docs/languages/a-z.md`` as the list of atlas pages.
    """
    order: list[str] = []
    for target in _TABLE_LINK.findall(_read(INDEX)):
        if target.startswith("..") or "#" in target or target in order:
            continue
        order.append(target)

    atlas = atlas_pages(az_text)
    languages: list[str] = []
    for name in _ANY_LINK.findall(_read(LANGUAGES)):
        page = "languages/" + name
        if page != LANGUAGES and page not in languages and page not in atlas:
            languages.append(page)
    if ATLAS_AZ in languages:
        at = languages.index(ATLAS_AZ) + 1
        languages[at:at] = atlas
    else:
        languages += atlas
    at = order.index(LANGUAGES)
    order = order[: at + 1] + languages + order[at + 1 :]

    on_disk = {
        os.path.relpath(p, DOCS).replace(os.sep, "/")
        for p in glob.glob(os.path.join(DOCS, "**", "*.md"), recursive=True)
    } - NOT_IN_ORDER
    missing = sorted(on_disk - set(order))
    unknown = sorted(set(order) - on_disk)
    if missing or unknown:
        raise SystemExit(
            "docs/index.md does not match docs/ on disk.\n"
            "  not linked from an index: {}\n"
            "  linked but absent: {}".format(missing, unknown)
        )
    return order


def _label(rel: str) -> str:
    for line in _read(rel).splitlines():
        if line.startswith("# "):
            title = re.split(r"\s*[:—–]\s|\s*\(`", line[2:].strip())[0]
            return re.sub(r"\s*\(.*\)$", "", title.strip().rstrip(".")) or rel
    return rel


def footer(rel: str, order: list[str] | None = None) -> str:
    """The navigation footer for the page at ``rel``, relative to ``docs/``."""
    order = order or reading_order()
    at = order.index(rel)
    here = os.path.dirname(rel) or "."
    link = lambda text, target: "[{}]({})".format(
        text, os.path.relpath(target, here).replace(os.sep, "/")
    )
    parts = []
    if at:
        parts.append(link("← " + _label(order[at - 1]), order[at - 1]))
    parts.append(link("Home", INDEX))
    if at < len(order) - 1:
        parts.append(link(_label(order[at + 1]) + " →", order[at + 1]))
    return "\n\n---\n" + " · ".join(parts) + "\n"


def with_footer(text: str, rel: str, order: list[str]) -> str:
    """*text* with its footer replaced by the footer for ``rel``."""
    return _FOOTER.sub("", text.rstrip()) + footer(rel, order)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="rewrite the footers")
    mode.add_argument("--check", action="store_true",
                      help="exit 1 on a stale footer (the default)")
    args = ap.parse_args()

    order = reading_order()
    stale = []
    for rel in order:
        path = os.path.join(DOCS, rel)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        wanted = with_footer(text, rel, order)
        if wanted == text:
            continue
        stale.append(rel)
        if args.write:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(wanted)

    if not stale:
        print("{} pages, footers in order".format(len(order)))
        return 0
    verb = "rewrote" if args.write else "stale footer in"
    print("{} {} pages: {}".format(verb, len(stale), ", ".join(stale)))
    return 0 if args.write else 1


if __name__ == "__main__":
    sys.exit(main())
