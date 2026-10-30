#!/usr/bin/env python3
"""Attribute the Thai PER gap between the two golds to tone-letter placement.

Thai spells tone (``tone_rules`` in ``data/th.json``), and both golds write
it. They put the Chao tone letter in different slots: ``wikipron`` writes it
after the whole syllable, as this spec does, and the epitran-derived
``vox_communis`` gold writes it on the nucleus, before the coda. This script
re-scores each row with the harness's own ``normalize()`` (broad, as the board scores) and
``levenshtein()``, then moves every run of tone letters to the end of the
transcription on BOTH sides and re-scores. That keeps tone identity and
order and removes placement only, so the second number is what the row
scores once the notation choice is taken out.

Placement is a notation choice of the gold, not a contrast the spelling
cannot signal, so the number is recorded as an ``audit`` entry and not as a
``valid_ceiling`` (T-2583).

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_th_notation.py

Nothing here feeds the board. See docs/languages/th.md.
"""
from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "th"
DATASETS = (("wikipron", B.load_wikipron),
            ("vox_communis", B.load_vox_communis))

#: Chao tone letters.
TONE = re.compile("[˥˦˧˨˩]+")


def scored_pairs(loader):
    """(word, normalized golds, normalized hypothesis) per scored word.

    A word with several gold transcriptions is scored once against the best
    of them, as the board does.
    """
    from orthography2ipa import G2P

    engine = G2P(LANG)
    extra = B._prosody_marks(LANG)

    def norm(s):
        return B.normalize(s, True, True, extra_strip=extra)

    refs = {}
    for word, gold in loader(LANG, 10 ** 9):
        refs.setdefault(word, []).append(gold)
    out = []
    for word, golds in refs.items():
        try:
            hyp = engine.transcribe_word(word)
        except Exception:
            continue
        if hyp:
            out.append((word, [norm(g) for g in golds], norm(hyp)))
    return out


def tone_to_end(s):
    """Move every tone-letter run to the end, keeping identity and order."""
    return TONE.sub("", s) + "".join(TONE.findall(s))


def per(rows, fold=lambda s: s):
    """Mean per-word PER after applying *fold* to both sides."""
    total = 0.0
    for _word, golds, hyp in rows:
        h = fold(hyp)
        total += min(B.levenshtein(h, fold(g)) / max(len(fold(g)), 1)
                     for g in golds)
    return total / len(rows)


def main():
    for name, loader in DATASETS:
        rows = scored_pairs(loader)
        golds = [g for _w, gs, _h in rows for g in gs]
        toned = sum(1 for g in golds if TONE.search(g))
        inside = sum(1 for g in golds if TONE.search(g) and not TONE.search(g[-1]))
        print(f"{name} / {LANG}: {len(rows)} words scored")
        print(f"  as scored                 {per(rows):.4f}")
        print(f"  + tone letters to the end {per(rows, tone_to_end):.4f}")
        print(f"  + tone letters removed    "
              f"{per(rows, lambda s: TONE.sub('', s)):.4f}")
        print(f"  gold transcriptions that do not end in a tone letter: "
              f"{inside} of {toned} toned transcriptions\n")


if __name__ == "__main__":
    main()
