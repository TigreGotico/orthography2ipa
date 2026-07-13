#!/usr/bin/env python3
"""Authoring helper for the Arabic TTS gold set: takes a python file defining
ROWS = [(sentence, gloss_en, shape_tags, notes), ...] and a lect code,
computes raw / o2i IPA / auto feature tags, and (re)writes the lect's gold
TSV. Complements scripts/arabic_tts_gold.py (checklist/draft/validate) —
see docs/arabic-tts-gold.md for the full procedure."""
import csv, importlib.util, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from arabic_tts_gold import FIELDS, FEATURES, GOLD_DIR, strip_tashkeel, diacritization_gaps

def build(lect, rows_py):
    import orthography2ipa
    spec = importlib.util.spec_from_file_location("rows", rows_py)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    GOLD_DIR.mkdir(parents=True, exist_ok=True)
    out = GOLD_DIR / f"{lect}.tsv"
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(FIELDS)
        for i, (sentence, gloss, shape, notes) in enumerate(mod.ROWS, 1):
            raw = strip_tashkeel(sentence)
            ipa = orthography2ipa.transcribe(sentence, lect)
            feats = [t for t, (_, p) in FEATURES.items() if p(raw, ipa)] + list(shape)
            gaps = diacritization_gaps(sentence)
            if gaps:
                print(f"  WARN {lect}-{i:03d} bare consonants: {gaps}")
            w.writerow([f"{lect}-{i:03d}", sentence, raw, ipa, gloss, ";".join(feats), notes])
            print(f"{lect}-{i:03d} {ipa}")
    print("wrote", out)

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
