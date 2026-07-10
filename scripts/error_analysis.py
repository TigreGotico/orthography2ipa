#!/usr/bin/env python3
"""Diagnose why a language's transcriptions miss the gold reference.

Read-only microscope over ``scripts/benchmark.py``'s gold datasets and
alignment routine: for a language, runs the gold through
:class:`orthography2ipa.G2P` and reports three views onto where the
errors are, so language work (see the roadmap's per-language procedure)
starts from evidence instead of guesswork.

Reports:

- **Confusion pairs**: top-20 ``(gold_phoneme, hyp_phoneme)`` substitution/
  insertion/deletion pairs (``None`` marks an insertion or deletion),
  aligned via :func:`scripts.benchmark.align`, ranked by frequency.
- **Worst words**: top-20 words by per-word PER, gold vs hyp side by side.
- **Grapheme blame**: for each orthographic character/digraph the
  language's spec maps in its grapheme table, the mean PER of every
  scored word containing it (occurring at least 3 times), worst first.

Never writes to specs or any other file — pure read/report.

Usage::

    python scripts/error_analysis.py en
    python scripts/error_analysis.py en --dataset wikipron --limit 300
    python scripts/error_analysis.py en --json
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from benchmark import DATASETS, align, normalize, levenshtein  # noqa: E402

TOP_N = 20
MIN_GRAPHEME_OCCURRENCES = 3


def pick_dataset(lang: str, dataset: Optional[str] = None) -> str:
    """Return the dataset name to use for ``lang``: ``dataset`` if given
    (validated to cover ``lang``), else the first registered dataset
    (in ``DATASETS`` iteration order) whose language list covers ``lang``.
    """
    if dataset is not None:
        if dataset not in DATASETS:
            raise SystemExit(f"unknown dataset: {dataset}")
        _, langs = DATASETS[dataset]
        if lang not in langs:
            raise SystemExit(f"dataset {dataset!r} does not cover lang={lang!r}")
        return dataset
    for name, (_, langs) in DATASETS.items():
        if lang in langs:
            return name
    raise SystemExit(f"no registered dataset covers lang={lang!r}")


def _grapheme_keys(lang: str) -> List[str]:
    """Orthographic characters/digraphs the spec's grapheme map declares
    for ``lang``, longest-first so digraphs are checked before the
    single characters they contain."""
    from orthography2ipa import get

    spec = get(lang)
    keys = list(spec.graphemes.keys())
    keys.sort(key=len, reverse=True)
    return keys


def analyze(lang: str, dataset: str, limit: int) -> dict:
    """Run the gold dataset through the engine and build the three
    report sections. Returns a plain-data dict (JSON-serializable)."""
    from orthography2ipa import G2P

    loader, _ = DATASETS[dataset]
    pairs = loader(lang, limit)

    refs: Dict[str, List[str]] = {}
    for word, gold in pairs:
        refs.setdefault(word, []).append(gold)

    engine = G2P(lang)

    confusion: Dict[Tuple[Optional[str], Optional[str]], int] = defaultdict(int)
    worst_words: List[Tuple[float, str, str, str]] = []  # per, word, gold, hyp
    grapheme_pers: Dict[str, List[float]] = defaultdict(list)
    grapheme_keys = _grapheme_keys(lang)

    for word, golds in refs.items():
        try:
            raw_hyp = engine.transcribe_word(word)
        except Exception:
            continue
        hyp = normalize(raw_hyp, strip_stress=True, broad=True)
        if not hyp:
            continue

        best_per = None
        best_gold_norm = None
        for g in golds:
            gold_norm = normalize(g, strip_stress=True, broad=True)
            per = levenshtein(hyp, gold_norm) / max(len(gold_norm), 1)
            if best_per is None or per < best_per:
                best_per = per
                best_gold_norm = gold_norm

        worst_words.append((best_per, word, best_gold_norm, hyp))

        for gp, hp in align(best_gold_norm, hyp):
            if gp != hp:
                confusion[(gp, hp)] += 1

        lower_word = word.lower()
        for gk in grapheme_keys:
            if gk and gk in lower_word:
                # substring containment, not tokenization -- acceptable
                # for blame attribution, which is meant as a triage
                # signal, not ground truth.
                grapheme_pers[gk].append(best_per)

    worst_words.sort(key=lambda t: t[0], reverse=True)
    confusion_top = sorted(
        confusion.items(), key=lambda kv: kv[1], reverse=True)[:TOP_N]

    grapheme_blame = [
        (gk, sum(pers) / len(pers), len(pers))
        for gk, pers in grapheme_pers.items()
        if len(pers) >= MIN_GRAPHEME_OCCURRENCES
    ]
    grapheme_blame.sort(key=lambda t: t[1], reverse=True)

    return {
        "lang": lang,
        "dataset": dataset,
        "n_words": len(refs),
        "n_scored": len(worst_words),
        "confusion_pairs": [
            {"gold": gp, "hyp": hp, "count": count}
            for (gp, hp), count in confusion_top
        ],
        "worst_words": [
            {"word": w, "gold": g, "hyp": h, "per": round(per, 4)}
            for per, w, g, h in worst_words[:TOP_N]
        ],
        "grapheme_blame": [
            {"grapheme": gk, "mean_per": round(mean_per, 4), "n": n}
            for gk, mean_per, n in grapheme_blame
        ],
    }


def _fmt_phone(p: Optional[str]) -> str:
    return p if p else "∅"


def print_report(report: dict) -> None:
    print(f"=== {report['lang']} ({report['dataset']}, "
          f"n_words={report['n_words']}, n_scored={report['n_scored']}) ===")

    print(f"\n--- Top {TOP_N} phoneme confusion pairs (gold -> hyp) ---")
    for row in report["confusion_pairs"]:
        print(f"  {_fmt_phone(row['gold'])!r:>6} -> {_fmt_phone(row['hyp'])!r:<6} "
              f"x{row['count']}")

    print(f"\n--- Top {TOP_N} worst words ---")
    for row in report["worst_words"]:
        print(f"  {row['word']!r:<20} gold={row['gold']!r:<20} "
              f"hyp={row['hyp']!r:<20} PER={row['per']:.4f}")

    print(f"\n--- Per-grapheme blame (min {MIN_GRAPHEME_OCCURRENCES} occurrences) ---")
    for row in report["grapheme_blame"]:
        print(f"  {row['grapheme']!r:<8} mean_PER={row['mean_per']:.4f} "
              f"n={row['n']}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("lang")
    ap.add_argument("--dataset", default=None, choices=sorted(DATASETS))
    ap.add_argument("--limit", type=int, default=300)
    ap.add_argument("--json", action="store_true",
                    help="Emit all three sections as one JSON object")
    args = ap.parse_args()

    dataset = pick_dataset(args.lang, args.dataset)
    report = analyze(args.lang, dataset, args.limit)

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_report(report)


if __name__ == "__main__":
    main()
