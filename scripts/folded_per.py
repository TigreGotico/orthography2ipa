#!/usr/bin/env python3
"""What a spec scores on the material its orthography does supply.

A script that leaves segments out gives a spec no way to write them. The
omission score in :mod:`omission_score` measures what declining to guess
them costs. This module measures the other half: fold those segments out
of BOTH sides and score what is left, so the number describes how well
the spec reads what IS written.

The two are different quantities and neither bounds the other. The
omission score compares a stripped gold against the gold. The folded PER
compares the SPEC'S OWN OUTPUT, stripped, against the gold, stripped, so
it needs the engine and the omission score does not.

It is defined the way the scorer measures PER, and by calling the
scorer's own code: transcribe each word, normalise both sides with
:func:`benchmark.normalize`, remove the segments from each, take the
character-level :func:`benchmark.levenshtein` against the gold, divide by
the folded gold length, and average over the covered words. A word with
several golds scores against whichever gold is kindest, the rule the
scorer applies.
"""

import argparse
import sys
from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence

from benchmark import (  # noqa: E402
    DATASETS,
    GoldPair,
    _is_multiword,
    _prosody_marks,
    levenshtein,
    normalize,
)
from omission_score import strip_segments


@dataclass(frozen=True)
class FoldedResult:
    """The folded PER and the counts a reader needs to trust it."""

    score: float
    words: int
    covered: int
    gold_chars: int
    removed_chars: int

    @property
    def removed_share(self) -> float:
        total = self.gold_chars + self.removed_chars
        return self.removed_chars / total if total else 0.0


def folded_per(pairs: Sequence[GoldPair], lang: str,
               segments: Iterable[str],
               strip_stress: bool = True, broad: bool = True) -> FoldedResult:
    """The spec's PER with *segments* folded out of hypothesis and gold."""
    from orthography2ipa import G2P

    engine = G2P(lang)
    refs: Dict[str, List[str]] = {}
    for word, gold in pairs:
        refs.setdefault(word, []).append(gold)

    extra = _prosody_marks(lang)
    segments = list(segments)
    total, gold_chars, removed_chars, covered = 0.0, 0, 0, 0
    for word, golds in refs.items():
        try:
            transcribe = (engine.transcribe if _is_multiword(word)
                          else engine.transcribe_word)
            hyp = normalize(transcribe(word), strip_stress, broad,
                            extra_strip=extra)
        except Exception:
            continue
        if not hyp:
            continue
        hyp = strip_segments(hyp, segments)
        golds_norm = [normalize(g, strip_stress, broad, extra_strip=extra)
                      for g in golds]
        folded = [strip_segments(g, segments) for g in golds_norm]
        pairs_ = [(f, g) for f, g in zip(folded, golds_norm) if f]
        if not pairs_:
            continue
        covered += 1
        best, best_ref = None, ""
        for ref, full in pairs_:
            score = levenshtein(hyp, ref) / len(ref)
            if best is None or score < best:
                best, best_ref, best_full = score, ref, full
        total += best
        gold_chars += len(best_ref)
        removed_chars += len(best_full) - len(best_ref)
    score = total / covered if covered else 0.0
    return FoldedResult(score, len(refs), covered, gold_chars, removed_chars)


def score_for_dataset(dataset: str, lang: str, segments: Iterable[str],
                      limit: int = sys.maxsize) -> FoldedResult:
    """:func:`folded_per` over a registered gold set."""
    loader, langs = DATASETS[dataset]
    if lang not in langs:
        raise SystemExit(f"{dataset} supports: {langs}")
    return folded_per(loader(lang, limit), lang, segments)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dataset", required=True, choices=sorted(DATASETS))
    ap.add_argument("--lang", required=True)
    ap.add_argument("--segments", required=True,
                    help="Space-separated segments the orthography does not "
                         "write, e.g. 'a i u'")
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()

    res = score_for_dataset(args.dataset, args.lang, args.segments.split(),
                            sys.maxsize if args.limit is None else args.limit)
    print(f"{args.dataset} lang={args.lang} words={res.words} "
          f"covered={res.covered} gold_chars={res.gold_chars} "
          f"removed_chars={res.removed_chars} "
          f"share={res.removed_share:.4f} folded_per={res.score:.4f}")


if __name__ == "__main__":
    main()
