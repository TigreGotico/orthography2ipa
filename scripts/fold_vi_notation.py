#!/usr/bin/env python3
"""Attribute the Vietnamese ``vox_communis`` PER to transcription conventions.

The ``vi`` row of the VoxCommunis board sits near the bottom (PER 0.5596
over 2,475 words), which invites reading it as a defect in the Vietnamese
spec. It is not one. This script re-scores that row with the harness's own
``normalize()`` and ``levenshtein()``, then folds one notation difference at
a time out of BOTH sides and re-scores, so each convention gets a number
instead of an adjective.

It also counts the two ways the gold is not merely a different notation but
wrong about Vietnamese: it writes one tone letter for the two contrastive
tones ngang and huyền, and it places tone letters inside the rime.

Run it from the repository root::

    PYTHONPATH=. python scripts/fold_vi_notation.py

Nothing here feeds the board. Folding these conventions into ``normalize()``
would be wrong — it is the single scorer for every row, and tone-letter
placement is language-specific — so the row stays as scored and this script
is how the offset is quantified. See docs/languages/vi.md.
"""
from __future__ import annotations

import collections
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

LANG = "vi"
DATASET = "vox_communis"

#: Chao tone letters and the glottalisation mark the gold builds tones from.
TONE = re.compile("[˥˦˧˨˩ˀ]+")

#: Orthographic tone diacritic → traditional tone name. Vietnamese writes
#: every tone but ngang, which is the unmarked one.
TONE_MARK = {
    "̀": "huyền", "́": "sắc", "̉": "hỏi",
    "̃": "ngã", "̣": "nặng",
}

#: One fold per transcription convention, applied to gold and hypothesis
#: alike and CUMULATIVELY, in the order listed. Each entry is
#: (description, function).
FOLDS = [
    ("tone letters", lambda s: TONE.sub("", s)),
    ("vowel length ⟨ː⟩", lambda s: s.replace("ː", "")),
    ("unreleased-stop mark ⟨◌̚⟩", lambda s: s.replace("̚", "")),
    ("tie bar ⟨ŋ͡m k͡p⟩", lambda s: s.replace("͡", "")),
    ("⟨ɨ⟩ ~ ⟨ɯ⟩ for ⟨ư⟩", lambda s: s.replace("ɨ", "ɯ")),
    ("short vowels ⟨ă ɤ̆⟩ ~ ⟨a ə⟩",
     lambda s: s.replace("ă", "a").replace("ɤ̆", "ɤ").replace("ə", "ɤ")),
    ("palatal ⟨ɲ c⟩ ~ pre-velar ⟨ŋ k⟩ finals",
     lambda s: s.replace("ɲ", "ŋ").replace("c", "k")),
    ("vowel height ⟨ɛ ɔ⟩ ~ ⟨e o⟩",
     lambda s: s.replace("ɛ", "e").replace("ɔ", "o")),
]


def scored_pairs():
    """(word, normalized gold, normalized hypothesis) for every scored word."""
    from orthography2ipa import G2P

    engine = G2P(LANG)
    extra = B._prosody_marks(LANG)

    def norm(s):
        return B.normalize(s, True, False, extra_strip=extra)

    out = []
    for word, gold in B.load_vox_communis(LANG, 10 ** 9):
        try:
            hyp = engine.transcribe_word(word)
        except Exception:
            continue
        if hyp:
            out.append((word, norm(gold), norm(hyp)))
    return out


def per(rows, fold=lambda s: s):
    """Mean per-word PER after applying *fold* to both sides."""
    total = 0.0
    for _word, gold, hyp in rows:
        g, h = fold(gold), fold(hyp)
        total += B.levenshtein(h, g) / max(len(g), 1)
    return total / len(rows)


def compose(fns):
    """Apply *fns* left to right, re-composing so ⟨ɤ̆⟩ matches as one unit."""
    def folded(s):
        s = unicodedata.normalize("NFC", s)
        for fn in fns:
            s = unicodedata.normalize("NFC", fn(s))
        return s
    return folded


def tone_confusion(pairs):
    """Gold tone letters seen per orthographic tone category."""
    seen = collections.defaultdict(collections.Counter)
    for word, gold in pairs:
        name = "ngang"
        for ch in unicodedata.normalize("NFD", word.lower()):
            if ch in TONE_MARK:
                name = TONE_MARK[ch]
                break
        seen[name]["".join(TONE.findall(gold))] += 1
    return seen


def main():
    rows = scored_pairs()
    print(f"{DATASET} / {LANG}: {len(rows)} words scored\n")

    print("Cumulative notation folds (both sides):")
    print(f"  {'as scored':<44} {per(rows):.4f}")
    fns = []
    for name, fn in FOLDS:
        fns.append(fn)
        print(f"  + {name:<42} {per(rows, compose(fns)):.4f}")

    pairs = [(w, g) for w, g, _h in rows]
    print("\nGold tone letters per orthographic tone category:")
    merged = 0
    for name in ("ngang", "huyền", "sắc", "hỏi", "ngã", "nặng"):
        counter = tone_confusion(pairs)[name]
        total = sum(counter.values())
        top = ", ".join(f"{t or '(none)'}×{n}" for t, n in counter.most_common(3))
        print(f"  {name:<6} n={total:<5} {top}")
        if name in ("ngang", "huyền"):
            merged += counter["˨˨"]
    print(f"\n  ngang and huyền are contrastive (Kirby 2011: 386, ma/mà) but "
          f"share the\n  gold tone letter ˨˨ on {merged} of {len(rows)} words "
          f"({100 * merged / len(rows):.1f}%).")

    inside = sum(1 for _w, g, _h in rows
                 for m in [TONE.search(g)] if m and m.end() < len(g))
    toned = sum(1 for _w, g, _h in rows if TONE.search(g))
    print(f"  Tone letters placed inside the rime rather than after it: "
          f"{inside} of {toned}\n  toned words ({100 * inside / toned:.1f}%).")

    # Why two folds above move nothing. The tie bar never reaches the scorer,
    # and the mid/open vowel heights already agree on nearly every word.
    ties = sum(1 for _w, g, h in rows if "͡" in g or "͡" in h)
    heights = sum(
        1 for _w, g, h in rows
        if collections.Counter(c for c in g if c in "ɛɔeo")
        != collections.Counter(c for c in h if c in "ɛɔeo")
    )
    print(f"\n  Tie bars surviving normalize() on either side: {ties} of "
          f"{len(rows)} words.\n  Words whose ⟨ɛ ɔ e o⟩ content differs "
          f"between the two sides: {heights} of {len(rows)}.")


if __name__ == "__main__":
    main()
