#!/usr/bin/env python3
"""Write ``docs/languages/leaders.md``, the board rows of the leader languages.

Every cell comes from the registry, the spec JSON or
``benchmarks/results.json``::

    python3 scripts/gen_leaders_doc.py --write
    python3 scripts/gen_leaders_doc.py --check
"""

from __future__ import annotations

import argparse
import json
import os
import sys

import linguatag
import orthography2ipa

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import docs_nav  # noqa: E402
from benchmark import GATING_CUTOFF_TIER, RELIABILITY_TIERS  # noqa: E402

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REL = "languages/leaders.md"
PATH = os.path.join(REPO_ROOT, "docs", REL)
RESULTS = os.path.join(REPO_ROOT, "benchmarks", "results.json")
DATA = os.path.join(REPO_ROOT, "orthography2ipa", "data")
SUBTAGS = os.path.join(os.path.dirname(linguatag.__file__), "data",
                       "language_subtags.json")
EXPLORER = "https://tigregotico.github.io/orthography2ipa/"

LEADERS = ("pt-PT", "pt-BR", "es-CO", "fr-FR", "it-IT", "de-DE", "nl-NL",
           "da-DK", "kab", "hi-IN", "bn-IN", "mwr")


def best_row(rows: list) -> dict | None:
    """The row on the most trusted provenance tier, then with the largest N,
    then first by dataset name."""
    if not rows:
        return None
    return min(rows, key=lambda r: (RELIABILITY_TIERS.index(r["provenance"]),
                                    -r["n"], r["dataset"]))


def _macrolanguage(code: str) -> str | None:
    with open(SUBTAGS, encoding="utf-8") as f:
        return json.load(f)["language"].get(code, {}).get("macrolanguage")


def _link(code: str) -> str:
    if os.path.exists(os.path.join(REPO_ROOT, "docs", "languages", code + ".md")):
        return f"[{code}.md]({code}.md)"
    return f"[`{code}` in the data explorer]({EXPLORER}#{code})"


def _tier(code: str) -> str:
    path = os.path.join(DATA, code + ".json")
    with open(path, encoding="utf-8") as f:
        return json.load(f).get("quality", "research")


def _board(rows: list) -> list:
    best = best_row([r for r in rows if r.get("gating")])
    mark = ""
    if best is None:
        best = best_row(rows)
        mark = " (does not gate)"
    if best is None:
        return ["not measured"] + [""] * 4
    return [f"`{best['dataset']}`", str(best["n"]), f"{best['per']:.4f}",
            f"{best['per_ci_low']:.4f}–{best['per_ci_high']:.4f}",
            best["provenance"] + mark]


def _row(tag: str, results: list) -> str:
    code = orthography2ipa.get(tag).code
    tier = _tier(code)
    own = os.path.exists(os.path.join(DATA, tag + ".json"))
    if own or code == tag:
        resolved = f"`{code}`"
    elif tier == "stub":
        member = (f" (a member of the {tag} macrolanguage)"
                  if _macrolanguage(code) == tag else "")
        resolved = f"unsupported: resolves to the `{code}` stub{member}, no phonology"
    else:
        resolved = f"`{code}` (no `{tag}` spec)"
    board = _board([r for r in results if r["lang"] == code])
    cells = [f"`{tag}`", resolved, tier, *board, _link(code)]
    return "| " + " | ".join(cells) + " |"


def render() -> str:
    with open(RESULTS, encoding="utf-8") as f:
        results = json.load(f)
    lines = [
        "# Leader languages",
        "",
        docs_nav.agent_hint(
            covers="the board row of each leader language tag",
            source="`benchmarks/results.json`, `orthography2ipa/data/*.json`",
            generated="yes, by `scripts/gen_leaders_doc.py`",
            verify="`python3 scripts/gen_leaders_doc.py --check`",
            see="`docs/benchmarks.md`, `docs/languages/a-z.md`"),
        "",
        "The table gives one board row for each leader language tag. The "
        "resolved spec is the code that `orthography2ipa.get(tag)` returns. "
        "A tag with no spec file of its own resolves to a broader spec, and "
        "the table names that spec. The scoreboard has no rule that marks "
        "one row as the primary row of a language. The best gold row is "
        "the gating row on the most trusted provenance tier, in the order "
        + ", ".join(RELIABILITY_TIERS[:RELIABILITY_TIERS.index(GATING_CUTOFF_TIER) + 1])
        + ", and then the row with the largest N. A tag with no gating row "
        "shows its best other row by the same rule, marked \"does not gate\". "
        "A tag with no row shows \"not measured\".",
        "",
        "| Tag | Resolved spec | Spec tier | Best gold dataset | N | PER "
        "| 95% CI | Provenance tier | Page |",
        "| :--- | :--- | :--- | :--- | ---: | ---: | :--- | :--- | :--- |",
        *(_row(tag, results) for tag in LEADERS),
    ]
    return "\n".join(lines) + docs_nav.footer(REL)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    text = render()
    if args.check:
        with open(PATH, encoding="utf-8") as f:
            if f.read() != text:
                print(f"{PATH} is stale: run scripts/gen_leaders_doc.py")
                return 1
        return 0
    with open(PATH, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
