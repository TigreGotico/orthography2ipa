#!/usr/bin/env python3
"""What a spec scores when it omits what its script does not write.

Some scripts do not write some of what they are read as. Arabic and
Hebrew orthography leaves the short vowels out, Syriac leaves them out
unless the text is pointed, and no rule over the letters alone can put
them back. One answer to that is to emit nothing where the script writes
nothing, and this module measures what that answer scores.

The omission score is NOT a lower bound, and nothing here should be read
as one. Deleting a segment and guessing it wrong cost the same single
edit, so a spec that guesses the likeliest vowel beats omission whenever
the guess lands. Rows do come in below their omission score: Syriac
``aii`` scores 0.3758 against an omission score of 0.4928. What the
number gives is a reference point — how much of a row's error is the
unwritten material, and whether a spec is doing better or worse than
declining to guess.

It is defined the way the scorer measures PER, and by calling the
scorer's own code: normalise both sides with :func:`benchmark.normalize`,
take the character-level :func:`benchmark.levenshtein` against the gold,
divide by the gold length, and average over the covered words.

Measuring it any other way gives a different answer. The share of gold
SEGMENTS that are short vowels is not it, because PER counts CHARACTERS
and many consonants are written with more than one (pharyngealisation,
and the geminates that ``normalize`` expands). A share-based estimate
reads several points high.
"""
import argparse
import os
import sys
import unicodedata
from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from benchmark import (  # noqa: E402
    DATASETS,
    GoldPair,
    _prosody_marks,
    levenshtein,
    normalize,
)


@dataclass(frozen=True)
class OmissionResult:
    """An omission score and everything needed to check it.

    ``score`` is the PER; ``words`` is how many gold entries it averages
    over; ``gold_chars`` and ``removed_chars`` are the normalised
    character totals, so a reader can confirm the ratio by hand.
    """

    score: float
    words: int
    gold_chars: int
    removed_chars: int

    @property
    def removed_share(self) -> float:
        """Share of normalised gold characters that the segments hold.

        This is the pooled character share, NOT the omission score,
        which averages per-word ratios; the two differ whenever word
        lengths vary.
        """
        return self.removed_chars / self.gold_chars if self.gold_chars else 0.0


_MODIFIERS = "ːˑ\u02b0\u02b2\u02b7\u02e0\u02e4\u0303\u0329\u032f"


def segment_clusters(ipa: str) -> List[str]:
    """*ipa* split into segments: a base character with what modifies it.

    A length mark, a combining diacritic or a superscript modifier
    belongs to the character before it, so ``aː`` is ONE segment and not
    an ``a`` next to a length mark.
    """
    out: List[str] = []
    for ch in unicodedata.normalize("NFC", ipa):
        if out and (ch in _MODIFIERS or unicodedata.combining(ch)):
            out[-1] += ch
        else:
            out.append(ch)
    return out


def _is_modifier_only(segment: str) -> bool:
    return bool(segment) and all(ch in _MODIFIERS or unicodedata.combining(ch)
                                 for ch in segment)


def strip_segments(ipa: str, segments: Iterable[str]) -> str:
    """*ipa* without the segments listed in *segments*.

    Matching is by whole segment, so removing ``a`` leaves ``aː``
    standing. That distinction is the point in an abjad: Arabic and
    Hebrew write the LONG vowels and leave the short ones out, so a
    score that removed both would describe a script nobody reads.

    A listed segment that is only a modifier — a bare length mark, say —
    is removed from the segments that carry it instead, leaving the base
    behind. That is what a script which writes a vowel but not its
    length leaves a spec able to emit.
    """
    wanted = {unicodedata.normalize("NFC", s) for s in segments if s}
    drop_marks = "".join(sorted(m for m in wanted if _is_modifier_only(m)))
    out = []
    for cluster in segment_clusters(ipa):
        if cluster in wanted:
            continue
        for mark in drop_marks:
            cluster = cluster.replace(mark, "")
        if cluster and cluster not in wanted:
            out.append(cluster)
    return "".join(out)


def omission_score(pairs: Sequence[GoldPair], lang: str,
              segments: Iterable[str],
              strip_stress: bool = True, broad: bool = True) -> OmissionResult:
    """What a spec scores when it emits nothing for *segments*.

    *pairs* and *lang* are what the benchmark loaders return and take.
    Words carrying several gold transcriptions score against whichever
    gold is kindest, the same rule the scorer applies.
    """
    refs: Dict[str, List[str]] = {}
    for word, gold in pairs:
        refs.setdefault(word, []).append(gold)

    extra = _prosody_marks(lang)
    segments = list(segments)
    total, gold_chars, removed_chars, words = 0.0, 0, 0, 0
    for golds in refs.values():
        golds_norm = [normalize(g, strip_stress, broad, extra_strip=extra)
                      for g in golds]
        golds_norm = [g for g in golds_norm if g]
        if not golds_norm:
            continue
        # A spec emits ONE transcription, and the scorer then credits it
        # against whichever gold it is closest to. So the omitting spec
        # gets the better of both choices: which gold the unwritten
        # segments are stripped out of, and which gold it is scored
        # against. Stripping each gold and scoring it only against
        # itself misses the case where a variant spelling is nearer.
        best, best_ref, best_hyp = None, "", ""
        for gold in golds:
            hyp = normalize(strip_segments(gold, segments), strip_stress,
                            broad, extra_strip=extra)
            for ref in golds_norm:
                score = levenshtein(hyp, ref) / len(ref)
                if best is None or score < best:
                    best, best_ref, best_hyp = score, ref, hyp
        if best is None:
            continue
        words += 1
        total += best
        gold_chars += len(best_ref)
        removed_chars += max(0, len(best_ref) - len(best_hyp))
    return OmissionResult(score=total / words if words else 0.0, words=words,
                          gold_chars=gold_chars,
                          removed_chars=removed_chars)


def score_for_dataset(dataset: str, lang: str, segments: Iterable[str],
                      limit: int = sys.maxsize) -> OmissionResult:
    """:func:`omission_score` over a registered gold set."""
    loader, langs = DATASETS[dataset]
    if lang not in langs:
        raise SystemExit(f"{dataset} supports: {langs}")
    return omission_score(loader(lang, limit), lang, segments)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dataset", required=True, choices=sorted(DATASETS))
    ap.add_argument("--lang", required=True)
    ap.add_argument("--segments", required=True,
                    help="Space-separated segments the spec cannot emit, "
                         "e.g. 'a i u'")
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()

    res = score_for_dataset(args.dataset, args.lang, args.segments.split(),
                            sys.maxsize if args.limit is None else args.limit)
    print(f"{args.dataset} lang={args.lang} words={res.words} "
          f"gold_chars={res.gold_chars} removed_chars={res.removed_chars} "
          f"share={res.removed_share:.4f} omission_score={res.score:.4f}")


if __name__ == "__main__":
    main()
