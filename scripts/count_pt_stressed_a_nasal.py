#!/usr/bin/env python3
"""Count the Infopédia readings of a stressed plain ⟨a⟩ before an onset nasal.

The note of ``PT_STRESSED_A_BEFORE_NASAL`` in ``pt-PT.json`` states how often
Infopédia writes [ɐ] in that context. This script makes those numbers. It reads
the ``portuguese_unified`` file at a pinned Hugging Face commit, checks its
sha256, keeps the ``pt-PT`` rows that carry an Infopédia URL, and reads
``ipa_narrow``, because ``ipa_broad`` folds [ɐ] into [a].

A reading counts when the spelling and the transcription agree on the
context:

- The stressed element is the last hyphen element of the word, because the
  last stress mark of a compound reading falls on it. It spells no ⟨á â à ã⟩.
- That element spells a plain ⟨a⟩, then ⟨m n nh⟩, then a vowel letter.
- After the last stress mark, the reading has the onset of the stressed
  syllable, then an oral [a] or [ɐ], then [m n ɲ], then a vowel or a glide.
- The spelled ⟨a⟩ is the stressed vowel: the vowel letters after it make as
  many groups as the reading has nuclei after the stressed vowel.

Some rows hold two readings split by a comma, and some words have more than
one row, so the script counts readings and distinct words. It prints how many
lines, rows and readings it read and how many readings it kept.

Run it from the repository root::

    PYTHONPATH=$PWD python scripts/count_pt_stressed_a_nasal.py

``--examples N`` prints the first N readings that write [a].
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import benchmark as B  # noqa: E402

REVISION = "a8e0934f290e36049bb3edfd616163d121c56a0c"
SHA256 = "0b4d5e86a94762fc9037f6b415f9100647acd5de2fefa3b47f57086233cc2027"
URL = B._PT_UNIFIED_URL.replace("/resolve/main/", f"/resolve/{REVISION}/")
CACHE_NAME = f"portuguese_pronunciation_lexicon-{REVISION[:12]}.jsonl"

REGION = "pt-PT"
IPA_VOWELS = "aɐæɑeɛiɪɨoɔøuʊəy"
STRESS = "ˈ'"
SHAPE = re.compile(
    "[" + STRESS + "][^" + IPA_VOWELS + STRESS + "ˌ.]*?([aɐ])(?!̃)\\.?[mnɲ]"
    "[" + IPA_VOWELS + "jw]"
)
IPA_NUCLEUS = re.compile("[" + IPA_VOWELS + "]+")
ACCENTED_A = re.compile("[áâàã]")
VOWEL_LETTERS = "aeiouáéíóúâêôãõàüy"
SPELLED_CONTEXT = re.compile("a(?=(?:nh|m|n)[" + VOWEL_LETTERS + "])")
LETTER_GROUP = re.compile("[" + VOWEL_LETTERS + "]+")


def file_sha256(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def stressed_vowel(reading: str) -> tuple[str, int] | None:
    """The stressed [a] or [ɐ] of *reading* and the nuclei after it, or None."""
    reading = unicodedata.normalize("NFD", reading)
    last_mark = max(reading.rfind(mark) for mark in STRESS)
    match = SHAPE.match(reading, last_mark) if last_mark >= 0 else None
    if not match:
        return None
    return match.group(1), len(IPA_NUCLEUS.findall(reading[match.end(1):]))


def spells_stressed_a(word: str, nuclei_after: int) -> bool:
    """True when the stressed element of *word* spells the stressed vowel as a
    plain ⟨a⟩ before ⟨m n nh⟩ and a vowel letter."""
    element = word.lower().split("-")[-1]
    if ACCENTED_A.search(element):
        return False
    return any(len(LETTER_GROUP.findall(element[m.start() + 1:])) == nuclei_after
               for m in SPELLED_CONTEXT.finditer(element))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--examples", type=int, default=0,
                        help="print this many readings that write [a]")
    args = parser.parse_args()

    path = B._fetch_file(URL, CACHE_NAME)
    digest = file_sha256(path)
    if digest != SHA256:
        sys.exit(f"{path}: sha256 {digest}, expected {SHA256}")

    lines = rows = readings = 0
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
            for reading in ipa.split(","):
                readings += 1
                found = stressed_vowel(reading)
                if not found or not spells_stressed_a(word, found[1]):
                    continue
                vowel = found[0]
                readings_by_vowel[vowel] += 1
                words_by_vowel[vowel].add(word)
                if word.endswith("iano"):
                    iano_by_vowel[vowel] += 1
                    iano_words_by_vowel[vowel].add(word)
                if vowel == "a" and len(examples) < args.examples:
                    examples.append(f"{word}\t{reading}")

    kept = sum(readings_by_vowel.values())
    iano_kept = sum(iano_by_vowel.values())
    all_words = set().union(*words_by_vowel.values())
    iano_words = set().union(*iano_words_by_vowel.values())
    print(f"dataset: {URL}")
    print(f"sha256: {digest}")
    print(f"lines read: {lines}")
    print(f"Infopédia {REGION} rows with a narrow reading: {rows}")
    print(f"readings in: {readings}, readings out: {kept}, "
          f"[ɐ] {readings_by_vowel['ɐ']}, [a] {readings_by_vowel['a']}")
    print(f"-iano readings out: {iano_kept}, "
          f"[ɐ] {iano_by_vowel['ɐ']}, [a] {iano_by_vowel['a']}")
    print(f"words out: {len(all_words)}, [ɐ] in {len(words_by_vowel['ɐ'])}, "
          f"[a] in {len(words_by_vowel['a'])}")
    print(f"-iano words out: {len(iano_words)}, [ɐ] in {len(iano_words_by_vowel['ɐ'])}, "
          f"[a] in {len(iano_words_by_vowel['a'])}")
    for example in examples:
        print(example)


if __name__ == "__main__":
    main()
