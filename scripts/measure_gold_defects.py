#!/usr/bin/env python3
"""Measure the gold-defect counts of ``docs/evaluation/gold_defects.md``.

The script reads the cached gold in ``.benchmark_cache/`` and writes
``benchmarks/gold_defects.json``. ``scripts/gen_doc_charts.py`` draws the
figure of the page from that file.

``pt_tl``
    The Portal (LUPo) rows of ``pt-TL-x-dili`` against ``pt-PT-x-lisboa`` in
    ``portuguese_pronunciation_lexicon.jsonl``. The first ``ipa_narrow``
    variant of each word is compared. Character substitutions are counted
    position by position over the shared words whose two transcriptions have
    the same length.
``fa``
    Counts of the classical and modern diagnostic symbols in the IPA column
    of the WikiPron file ``fas_arab_broad.tsv``.

Usage::

    python scripts/measure_gold_defects.py [--cache DIR]
"""

from __future__ import annotations

import argparse
import json
import os
from collections import Counter

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REPO_ROOT, "benchmarks", "gold_defects.json")
TOP_SUBSTITUTIONS = 6
FA_SYMBOLS = ("aː", "ɒː", "r", "ɾ", "w", "v", "q", "ɣ")


def pt_tl(path: str) -> dict:
    first = {"pt-TL-x-dili": {}, "pt-PT-x-lisboa": {}}
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            row = json.loads(raw)
            region = first.get(row["region"])
            if not row.get("phones") or region is None or row["word"] in region:
                continue
            region[row["word"]] = row["ipa_narrow"]
    dili, lisboa = first["pt-TL-x-dili"], first["pt-PT-x-lisboa"]
    shared = set(dili) & set(lisboa)
    equal = [w for w in shared if len(dili[w]) == len(lisboa[w])]
    subs = Counter((a, b) for w in equal for a, b in zip(lisboa[w], dili[w]) if a != b)
    return {"shared_words": len(shared),
            "identical_words": sum(dili[w] == lisboa[w] for w in shared),
            "equal_length_words": len(equal),
            "character_differences": sum(subs.values()),
            "substitutions": [{"lisboa": a, "dili": b, "count": n}
                              for (a, b), n in sorted(subs.items(), key=lambda kv: (-kv[1], kv[0]))
                              [:TOP_SUBSTITUTIONS]]}


def fa(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        ipa = "".join(line.rstrip("\n").split("\t")[1] for line in fh)
    return {s: ipa.count(s) for s in FA_SYMBOLS}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--cache", default=os.path.join(REPO_ROOT, ".benchmark_cache"))
    args = ap.parse_args()
    data = {"pt_tl": pt_tl(os.path.join(args.cache, "portuguese_pronunciation_lexicon.jsonl")),
            "fa": fa(os.path.join(args.cache, "fas_arab_broad.tsv"))}
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=1)
        fh.write("\n")
    print(f"wrote {os.path.relpath(OUT, REPO_ROOT)}: "
          f"{len(data['pt_tl']['substitutions'])} substitutions, {len(data['fa'])} symbols")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
