"""Quick top-1 / oracle PER on a random sample of a dataset row.

Usage: PYTHONPATH=. python scripts/rank_eval.py fr 5000 [dataset]
"""
from __future__ import annotations

import random
import sys

sys.path.insert(0, "scripts")

from benchmark import DATASETS, evaluate_words_oracle  # noqa: E402


def sample(lang, limit, dataset="wikipron", seed=20260810):
    pairs = DATASETS[dataset][0](lang, sys.maxsize)
    if limit and limit < len(pairs):
        random.Random(seed).shuffle(pairs)
        pairs = pairs[:limit]
    return pairs


if __name__ == "__main__":
    lang = sys.argv[1]
    limit = int(sys.argv[2])
    ds = sys.argv[3] if len(sys.argv) > 3 else "wikipron"
    pairs = sample(lang, limit, ds)
    n, covered, pers, per, wer, orc = evaluate_words_oracle(
        pairs, lang, strip_stress=True, broad=True)
    print(f"{lang} {ds} n={n} covered={covered} "
          f"PER={per:.4f} WER={wer:.4f} "
          f"oracle@5={orc.oracle_per[5]:.4f} "
          f"exact@1={orc.oracle_exact[1]:.4f} "
          f"exactX@5={orc.oracle_exact[5]:.4f}")
