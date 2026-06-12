#!/usr/bin/env python3
"""Measure agreement between orthography2ipa and espeak-ng.

This is NOT an accuracy benchmark — there is no gold standard here.
It answers a deployment question: can orthography2ipa safely replace
espeak-ng as the phonemization front-end of a TTS model that was
TRAINED on espeak output?  Such a model maps phoneme symbols to
embedding IDs, so what matters is symbol-level compatibility with what
espeak produces, not linguistic correctness.

Three signals per language:

- **exact** — fraction of words whose transcriptions match exactly
  after minimal normalization (NFC; espeak language-switch flags
  removed).  The strictest drop-in signal.
- **segmental** — mean character-level similarity
  (1 − levenshtein/len) with stress marks stripped.  How close the
  phone sequences are when they differ.
- **oov-rate** — fraction of words whose orthography2ipa output
  contains a symbol espeak never emitted for that language.  Out-of-
  inventory symbols become unknown embedding IDs: each one is a hard
  failure for the TTS model, which makes this the most important
  number.  The symbols themselves are listed.

Word lists are vocabulary samples drawn from the gold datasets of
``scripts/benchmark.py`` (only the word column is used).

Usage::

    python scripts/espeak_agreement.py --lang pt-PT
    python scripts/espeak_agreement.py --lang en --limit 500
    python scripts/espeak_agreement.py --list
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import unicodedata
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, os.path.dirname(__file__))
import benchmark  # noqa: E402  — shared dataset loaders and metric helpers

# language tag → (wordlist loader, loader lang, espeak voice)
SOURCES: Dict[str, Tuple] = {
    "en-US": (benchmark.load_cmudict, "en-US", "en-us"),
    "en": (benchmark.load_wikipron, "en", "en-gb"),
    "en-GB": (benchmark.load_wikipron, "en-GB", "en-gb"),
    "es": (benchmark.load_wikipron, "es", "es"),
    "gl": (benchmark.load_wikipron, "gl", None),  # espeak has no Galician
    "pt": (benchmark.load_wikipron, "pt", "pt"),
    "pt-PT": (benchmark.load_portuguese_lexicon, "pt-PT", "pt"),
    "pt-BR": (benchmark.load_portuguese_lexicon, "pt-BR", "pt-br"),
    "pt-AO": (benchmark.load_portuguese_lexicon, "pt-AO", "pt"),
    "pt-MZ": (benchmark.load_portuguese_lexicon, "pt-MZ", "pt"),
    "pt-TL": (benchmark.load_portuguese_lexicon, "pt-TL", "pt"),
    "mwl": (benchmark.load_mirandese, "mwl", None),  # espeak has no Mirandese
}

_LANG_SWITCH = re.compile(r"\([a-z-]+\)")  # espeak (en)…(pt) switch flags


def espeak_batch(words: List[str], voice: str) -> List[str]:
    """Phonemize *words* with one espeak-ng process (one word per line)."""
    proc = subprocess.run(
        ["espeak-ng", "-q", "--ipa", "-v", voice],
        input="\n".join(words),
        capture_output=True,
        text=True,
        timeout=300,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"espeak-ng failed for voice {voice!r}: {proc.stderr.strip()}")
    lines = [ln.strip() for ln in proc.stdout.splitlines() if ln.strip()]
    if len(lines) != len(words):
        raise RuntimeError(
            f"espeak-ng returned {len(lines)} lines for {len(words)} words "
            f"(voice {voice!r}); refusing to misalign")
    return lines


def normalize(ipa: str, strip_stress: bool = False) -> str:
    s = unicodedata.normalize("NFC", ipa)
    s = _LANG_SWITCH.sub("", s)
    if strip_stress:
        for ch in "ˈˌ":
            s = s.replace(ch, "")
    return "".join(s.split())


def agreement(lang: str, limit: int) -> Optional[dict]:
    loader, loader_lang, voice = SOURCES[lang]
    if voice is None:
        return None
    words = [w for w, _ in loader(loader_lang, limit)]

    from orthography2ipa import G2P

    engine = G2P(lang)
    ours = [normalize(engine.transcribe_word(w)) for w in words]
    theirs = [normalize(e) for e in espeak_batch(words, voice)]

    espeak_symbols = set("".join(theirs))
    exact = sum(a == b for a, b in zip(ours, theirs))
    exact_nostress = sum(
        normalize(a, strip_stress=True) == normalize(b, strip_stress=True)
        for a, b in zip(ours, theirs))

    seg_sum = 0.0
    oov_words = 0
    oov_symbols: Dict[str, int] = {}
    for a, b in zip(ours, theirs):
        a_s = normalize(a, strip_stress=True)
        b_s = normalize(b, strip_stress=True)
        dist = benchmark.levenshtein(a_s, b_s)
        seg_sum += 1.0 - dist / max(len(a_s), len(b_s), 1)
        unknown = {ch for ch in a if ch not in espeak_symbols}
        if unknown:
            oov_words += 1
            for ch in unknown:
                oov_symbols[ch] = oov_symbols.get(ch, 0) + 1

    n = len(words)
    return {
        "lang": lang,
        "voice": voice,
        "n": n,
        "exact": exact / n if n else 0.0,
        "exact_nostress": exact_nostress / n if n else 0.0,
        "segmental": seg_sum / n if n else 0.0,
        "oov_rate": oov_words / n if n else 0.0,
        "oov_symbols": dict(
            sorted(oov_symbols.items(), key=lambda kv: -kv[1])),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--lang", choices=sorted(SOURCES))
    ap.add_argument("--limit", type=int, default=300)
    ap.add_argument("--list", action="store_true",
                    help="List languages and their espeak voices")
    args = ap.parse_args()

    if args.list or not args.lang:
        for lang, (_, _, voice) in sorted(SOURCES.items()):
            print(f"{lang:8} espeak voice: {voice or '— (none; skipped)'}")
        return

    result = agreement(args.lang, args.limit)
    if result is None:
        sys.exit(f"espeak-ng has no voice for {args.lang}; "
                 "nothing to compare against")
    print(f"lang={result['lang']} voice={result['voice']} n={result['n']} "
          f"exact={result['exact']:.3f} "
          f"exact-nostress={result['exact_nostress']:.3f} "
          f"segmental={result['segmental']:.3f} "
          f"oov-rate={result['oov_rate']:.3f}")
    if result["oov_symbols"]:
        print("out-of-inventory symbols (orthography2ipa → not in espeak "
              "output):")
        for ch, count in result["oov_symbols"].items():
            print(f"  {ch!r}  U+{ord(ch):04X}  in {count} words")


if __name__ == "__main__":
    main()
