#!/usr/bin/env python3
"""Count the Infopédia readings of a stressed plain ⟨a⟩ before an onset nasal.

The note of ``PT_STRESSED_A_BEFORE_NASAL`` in ``pt-PT.json`` states how often
Infopédia writes [ɐ] in that context. This script makes those numbers. It reads
the ``portuguese_unified`` file that ``scripts/benchmark.py`` caches, keeps the
``pt-PT`` rows that carry an Infopédia URL, and reads ``ipa_narrow``, because
``ipa_broad`` folds [ɐ] into [a].

A reading has the shape when it has a stress mark, then the onset of the
stressed syllable, then an oral [a] or [ɐ], then [m n ɲ], then a vowel or a
glide, so that the nasal opens the next syllable. The rule takes plain ⟨a⟩
only, so a word spelled with ⟨á â à ã⟩ is left out. Some rows hold two
readings split by a comma, and some words have more than one row, so the
script counts readings and distinct words.

Run it from the repository root::

    PYTHONPATH=$PWD python scripts/count_pt_stressed_a_nasal.py

``--examples N`` prints the first N readings that write [a].
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

REGION = "pt-PT"
VOWELS = "aɐæɑeɛiɪɨoɔøuʊəy"
SHAPE = re.compile(
    "[ˈ'][^" + VOWELS + "ˈ'ˌ.]*?([aɐ])(?!\u0303)\\.?[mnɲ][" + VOWELS + "jw]"
)
ACCENTED_A = re.compile("[áâàã]")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--examples", type=int, default=0,
                        help="print this many readings that write [a]")
    args = parser.parse_args()

    path = B._fetch_file(B._PT_UNIFIED_URL, "portuguese_pronunciation_lexicon.jsonl")
    lines = rows = 0
    readings_by_vowel = collections.Counter()
    iano_by_vowel = collections.Counter()
    words_by_vowel: dict[str, set[str]] = collections.defaultdict(set)
    iano_words_by_vowel: dict[str, set[str]] = collections.defaultdict(set)
    examples = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            lines += 1
            row = json.loads(line)
            if row.get("region") != REGION or not B.pt_unified_source(row).startswith("infopedia"):
                continue
            ipa = unicodedata.normalize("NFC", (row.get("ipa_narrow") or "").strip())
            word = row.get("word") or ""
            if not ipa or not word:
                continue
            rows += 1
            if ACCENTED_A.search(word):
                continue
            for reading in ipa.split(","):
                match = SHAPE.search(unicodedata.normalize("NFD", reading))
                if not match:
                    continue
                vowel = match.group(1)
                readings_by_vowel[vowel] += 1
                words_by_vowel[vowel].add(word)
                if word.endswith("iano"):
                    iano_by_vowel[vowel] += 1
                    iano_words_by_vowel[vowel].add(word)
                if vowel == "a" and len(examples) < args.examples:
                    examples.append(f"{word}\t{reading}")

    shape_readings = sum(readings_by_vowel.values())
    iano_readings = sum(iano_by_vowel.values())
    all_words = set().union(*words_by_vowel.values())
    iano_words = set().union(*iano_words_by_vowel.values())
    print(f"lines read: {lines}")
    print(f"Infopédia {REGION} rows with a narrow reading: {rows}")
    print(f"readings with the shape: {shape_readings}, "
          f"[ɐ] {readings_by_vowel['ɐ']}, [a] {readings_by_vowel['a']}")
    print(f"-iano readings with the shape: {iano_readings}, "
          f"[ɐ] {iano_by_vowel['ɐ']}, [a] {iano_by_vowel['a']}")
    print(f"words with the shape: {len(all_words)}, [ɐ] in {len(words_by_vowel['ɐ'])}, "
          f"[a] in {len(words_by_vowel['a'])}")
    print(f"-iano words with the shape: {len(iano_words)}, [ɐ] in {len(iano_words_by_vowel['ɐ'])}, "
          f"[a] in {len(iano_words_by_vowel['a'])}")
    for example in examples:
        print(example)


if __name__ == "__main__":
    main()
