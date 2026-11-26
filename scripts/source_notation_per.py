#!/usr/bin/env python3
"""The pt-BR portuguese_unified rows scored with per-source notation folds.

A fold applies only to a gold reading from a source whose own rows show no
contrast for it. It changes the hypothesis into the notation of that source,
so the score counts the engine's errors and not the notation of the gold.
Counts are over the pt-BR Michaelis rows of the dataset, ``ipa_narrow``:

- ``michaelis_ã``: 0 of 1,530 words spelled with ⟨ã⟩ write [ɐ̃]. [ɐ̃] → [ã].
- ``michaelis_no_palatal``: 1 of 1,378 ⟨ti⟩ words and 0 of 982 ⟨di⟩ words
  write a palatal. [t͡ʃ d͡ʒ] → [t d] before [i ĩ ɪ j].
- ``michaelis_final_r``: 3,865 of 3,868 words in -ar, -er, -ir write the
  final r. In a verb, the final rhotic of the gold is not counted where the
  hypothesis ends without one. This fold accepts a cited optional deletion,
  not a notation: Callou, Moraes & Leite 1998 (DELTA 14, p. 66), "A perda do
  R é mais freqüente nos verbos ... Nos não-verbos, em que o R não carreia
  informação morfológica, o peso relativo é baixo". A reading from a row
  without the POS VERB keeps its r.

A word read by several sources takes the folds of the source of each reading.
The script prints the code-point PER of the board and the segment PER, each
unfolded and folded.

    python scripts/source_notation_per.py [--dataset portuguese_unified_corrected]
"""

import argparse
import json
import os
import re
import sys
import unicodedata
from typing import Dict, List, Set, Tuple

from benchmark import (  # noqa: E402
    DATASETS,
    _PT_UNIFIED_REGIONS,
    _PT_UNIFIED_URL,
    _fetch,
    _is_multiword,
    _prosody_marks,
    levenshtein,
    normalize,
    pt_unified_source,
    read_pt_unified_corrections,
    segments,
)

_NFD = lambda s: unicodedata.normalize("NFD", s)  # noqa: E731
_FRONT = "iĩɪj"
_PALATAL = re.compile(_NFD(f"(t͡ʃ|tʃ|ʧ|d͡ʒ|dʒ|ʤ)(?=[{_FRONT}]|[{_FRONT}]̃)"))
_RHOTIC_END = re.compile("[ɾrʁhχɹxɻ]$")

SOURCE_FOLDS = {"michaelis": ("michaelis_ã", "michaelis_no_palatal", "michaelis_final_r")}


def fold(hyp: str, gold: str, folds: Set[str]) -> Tuple[str, str]:
    """*hyp* and *gold* with the named *folds* applied, both in NFD."""
    hyp, gold = _NFD(hyp), _NFD(gold)
    if "michaelis_ã" in folds:
        hyp = hyp.replace(_NFD("ɐ̃"), _NFD("ã"))
    if "michaelis_no_palatal" in folds:
        hyp = _PALATAL.sub(lambda m: "t" if m.group(1)[0] in "tʧ" else "d", hyp)
    if "michaelis_final_r" in folds:
        bare_hyp, bare_gold = hyp.rstrip("ˈˌ "), gold.rstrip("ˈˌ ")
        if _RHOTIC_END.search(bare_gold) and not _RHOTIC_END.search(bare_hyp):
            gold = bare_gold[:-1]
    return hyp, gold


def reading_sources(lang: str) -> Dict[Tuple[str, str], Set[Tuple[str, str]]]:
    """``(word, reading)`` → the ``(source, pos)`` of each row that gives
    that reading, after the overlay."""
    region = _PT_UNIFIED_REGIONS[lang]
    overlay = {(r["word"], r["region"], r["source"], r["pos"], r["field"],
                r["original_reading"]): r["corrected_reading"]
               for r in read_pt_unified_corrections() if r["field"] == "ipa_narrow"}
    out: Dict[Tuple[str, str], Set[str]] = {}
    text = _fetch(_PT_UNIFIED_URL, "portuguese_pronunciation_lexicon.jsonl")
    for line in text.splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        source = pt_unified_source(row)
        if row.get("region") != region or source == "portal":
            continue
        ipa = (row.get("ipa_narrow") or "").strip()
        key = (row["word"], region, source, row.get("pos") or "", "ipa_narrow",
               row.get("ipa_narrow"))
        ipa = overlay.get(key, ipa)
        if ipa:
            out.setdefault((row["word"], ipa.strip()), set()).update(
                (src, row.get("pos") or "") for src in source.split("+"))
    return out


def score(pairs, lang: str, sources, folded: bool) -> Tuple[float, float]:
    """``(code-point PER, segment PER)`` of the rules on *pairs*."""
    from orthography2ipa import G2P, Pipeline

    engine = G2P(lang, pipeline=Pipeline(lexicon=None))
    extra = _prosody_marks(lang)
    refs: Dict[str, List[str]] = {}
    for word, gold in pairs:
        refs.setdefault(word, []).append(gold)
    cp_sum = covered = edits = total = 0
    for word, golds in refs.items():
        transcribe = engine.transcribe if _is_multiword(word) else engine.transcribe_word
        raw = transcribe(word)
        cp, seg = [], []
        for gold in golds:
            folds = set()
            if folded:
                for src, pos in sources.get((word, gold), ()):
                    folds.update(f for f in SOURCE_FOLDS.get(src, ())
                                 if f != "michaelis_final_r" or pos == "VERB")
            h, g = fold(raw, gold, folds)
            hn, gn = (normalize(x, True, True, extra_strip=extra) for x in (h, g))
            cp.append(levenshtein(hn, gn) / max(len(gn), 1))
            seg.append((levenshtein(segments(h), segments(g)), len(segments(g))))
        if normalize(raw, True, True, extra_strip=extra):
            covered += 1
            cp_sum += min(cp)
        cost, size = min(seg)
        edits += cost
        total += size
    return cp_sum / covered, edits / total


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dataset", default="portuguese_unified_corrected",
                    choices=["portuguese_unified", "portuguese_unified_corrected"])
    ap.add_argument("--write", action="store_true",
                    help="score both pt-BR rows and write benchmarks/notation_folds.json")
    args = ap.parse_args()
    lang = "pt-BR"
    sources = reading_sources(lang)
    rows = []
    for dataset in (["portuguese_unified", "portuguese_unified_corrected"]
                    if args.write else [args.dataset]):
        pairs = DATASETS[dataset][0](lang, sys.maxsize)
        words = len({w for w, _ in pairs})
        (cp, seg), (fcp, fseg) = (score(pairs, lang, sources, f) for f in (False, True))
        print(f"{dataset} {lang}: {words} words; code-point PER {cp:.4f} folded {fcp:.4f}; "
              f"segment PER {seg:.4f} folded {fseg:.4f}")
        rows.append({"lang": lang, "dataset": dataset, "words": words,
                     "per": round(cp, 4), "folded_per": round(fcp, 4),
                     "segment_per": round(seg, 4), "folded_segment_per": round(fseg, 4),
                     "folds": list(SOURCE_FOLDS["michaelis"])})
    if args.write:
        path = os.path.join(os.path.dirname(__file__), "..", "benchmarks", "notation_folds.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(rows, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print(f"wrote {len(rows)} rows to benchmarks/notation_folds.json")


if __name__ == "__main__":
    main()
