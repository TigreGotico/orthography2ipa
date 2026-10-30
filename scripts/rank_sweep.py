"""Per-word PER dump for one engine state, for win/loss sweeps.

Writes ``word\tper\thyp`` for every scorable word of a dataset row, so two
runs (before/after a spec change) can be diffed per word and per bucket.

Usage: PYTHONPATH=. python scripts/rank_sweep.py fr out.tsv [dataset]
"""
from __future__ import annotations

import sys

sys.path.insert(0, "scripts")

from benchmark import (DATASETS, _prosody_marks, levenshtein,  # noqa: E402
                       normalize)

from orthography2ipa import G2P  # noqa: E402


def dump(lang: str, path: str, dataset: str = "wikipron") -> None:
    pairs = DATASETS[dataset][0](lang, sys.maxsize)
    engine = G2P(lang)
    extra = _prosody_marks(lang)
    refs = {}
    for word, gold in pairs:
        refs.setdefault(word, []).append(gold)
    with open(path, "w", encoding="utf-8") as fh:
        for word, golds in refs.items():
            if " " in word:
                continue
            try:
                hyp = normalize(engine.transcribe_word(word), True, True,
                                extra_strip=extra)
            except Exception:
                continue
            if not hyp:
                continue
            gn = [normalize(g, True, True, extra_strip=extra) for g in golds]
            per = min(levenshtein(hyp, g) / max(len(g), 1) for g in gn)
            fh.write(f"{word}\t{per:.6f}\t{hyp}\t{gn[0]}\n")


if __name__ == "__main__":
    dump(sys.argv[1], sys.argv[2],
         sys.argv[3] if len(sys.argv) > 3 else "wikipron")
