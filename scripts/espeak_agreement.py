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
import json
import os
import re
import subprocess
import sys
import unicodedata
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, os.path.dirname(__file__))
import benchmark  # noqa: E402  — shared dataset loaders and metric helpers

# language tag → (wordlist loader, loader lang, espeak voice)
#
# Coverage is the overlap between this repo's registered gold-dataset
# languages (``scripts/benchmark.py``'s ``DATASETS``) and espeak-ng's own
# voice list (``espeak-ng --voices``): a language needs a wordlist loader
# to draw a sample from AND an espeak-ng voice to compare against.
# Languages with a loader but no espeak-ng voice keep a ``None`` voice —
# ``agreement()`` returns ``None`` for those and they are skipped in the
# scoreboard, not reported as zero.
SOURCES: Dict[str, Tuple] = {
    "en-US": (benchmark.load_cmudict, "en-US", "en-us"),
    "en": (benchmark.load_wikipron, "en", "en-gb"),
    "en-GB": (benchmark.load_wikipron, "en-GB", "en-gb"),
    "es": (benchmark.load_wikipron, "es", "es"),
    "gl": (benchmark.load_wikipron, "gl", None),  # espeak has no Galician
    "pt": (benchmark.load_wikipron, "pt", "pt"),
    "pt-PT": (benchmark.load_portuguese_phonetic_lexicon, "pt-PT", "pt"),
    "pt-BR": (benchmark.load_portuguese_phonetic_lexicon, "pt-BR", "pt-br"),
    "pt-AO": (benchmark.load_portuguese_phonetic_lexicon, "pt-AO", "pt"),
    "pt-MZ": (benchmark.load_portuguese_phonetic_lexicon, "pt-MZ", "pt"),
    "pt-TL": (benchmark.load_portuguese_phonetic_lexicon, "pt-TL", "pt"),
    "mwl": (benchmark.load_mirandese, "mwl", None),  # espeak has no Mirandese
    "mwl-x-sendim": (benchmark.load_mirandese, "mwl-x-sendim", None),
    # --- wikipron-sourced, espeak-ng voice available ---
    "it": (benchmark.load_wikipron, "it", "it"),
    "fr": (benchmark.load_wikipron, "fr", "fr-fr"),
    "ro": (benchmark.load_wikipron, "ro", "ro"),
    "ast": (benchmark.load_wikipron, "ast", None),  # espeak has no Asturian
    "oc": (benchmark.load_wikipron, "oc", None),  # espeak has no Occitan
    "de": (benchmark.load_wikipron, "de", "de"),
    "nl": (benchmark.load_wikipron, "nl", "nl"),
    "sv": (benchmark.load_wikipron, "sv", "sv"),
    "da": (benchmark.load_wikipron, "da", "da"),
    "nb": (benchmark.load_wikipron, "nb", "nb"),
    "is": (benchmark.load_wikipron, "is", "is"),
    "cy": (benchmark.load_wikipron, "cy", "cy"),
    "ga": (benchmark.load_wikipron, "ga", "ga"),
    "gd": (benchmark.load_wikipron, "gd", "gd"),
    "pl": (benchmark.load_wikipron, "pl", "pl"),
    "sk": (benchmark.load_wikipron, "sk", "sk"),
    "hr": (benchmark.load_wikipron, "hr", "hr"),
    "ru": (benchmark.load_wikipron, "ru", "ru"),
    "el": (benchmark.load_wikipron, "el", "el"),
    "hy": (benchmark.load_wikipron, "hy", "hy"),
    "sq": (benchmark.load_wikipron, "sq", "sq"),
    "tr": (benchmark.load_wikipron, "tr", "tr"),
    "fi": (benchmark.load_wikipron, "fi", "fi"),
    "eu": (benchmark.load_wikipron, "eu", "eu"),
    "tl": (benchmark.load_wikipron, "tl", None),  # espeak has no Tagalog
    "eo": (benchmark.load_wikipron, "eo", "eo"),
    "hi": (benchmark.load_wikipron, "hi", "hi"),
    "ta": (benchmark.load_wikipron, "ta", "ta"),
    "ml": (benchmark.load_wikipron, "ml", "ml"),
    # --- 4catac-sourced (Catalan regional accents) ---
    "ca": (benchmark.load_4catac, "ca", "ca"),
    "ca-x-balear": (benchmark.load_4catac, "ca-x-balear", "ca-ba"),
    "ca-x-occidental": (benchmark.load_4catac, "ca-x-occidental", "ca-nw"),
    "ca-x-valencia": (benchmark.load_4catac, "ca-x-valencia", "ca-va"),
    # --- ep_dialects-sourced (European Portuguese regional accents);
    # espeak-ng has no per-region EP voice, so all compare against its
    # single Portuguese voice ---
    "pt-PT-x-acores": (benchmark.load_ep_dialects, "pt-PT-x-acores", "pt"),
    "pt-PT-x-alentejo": (benchmark.load_ep_dialects, "pt-PT-x-alentejo", "pt"),
    "pt-PT-x-algarve": (benchmark.load_ep_dialects, "pt-PT-x-algarve", "pt"),
    "pt-PT-x-lisbon": (benchmark.load_ep_dialects, "pt-PT-x-lisbon", "pt"),
    "pt-PT-x-madeira": (benchmark.load_ep_dialects, "pt-PT-x-madeira", "pt"),
    "pt-PT-x-porto": (benchmark.load_ep_dialects, "pt-PT-x-porto", "pt"),
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


REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AGREEMENT_MD = os.path.join(REPO_ROOT, "docs", "espeak_agreement.md")
AGREEMENT_JSON = os.path.join(REPO_ROOT, "benchmarks", "espeak_agreement.json")


def build_agreement_scoreboard(limit: int) -> List[dict]:
    """Run every SOURCES language with an espeak-ng voice and return
    deterministic rows sorted by language tag."""
    rows: List[dict] = []
    for lang, (_, _, voice) in sorted(SOURCES.items()):
        if voice is None:
            continue
        try:
            result = agreement(lang, limit)
        except Exception as exc:
            print(f"skip lang={lang}: {exc}", file=sys.stderr)
            continue
        if result is None:
            continue
        result["limit"] = limit
        rows.append(result)
    return rows


def write_agreement_scoreboard(rows: List[dict]) -> None:
    os.makedirs(os.path.dirname(AGREEMENT_JSON), exist_ok=True)
    with open(AGREEMENT_JSON, "w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    lines = [
        "# espeak-ng agreement",
        "",
        "Committed symbol-level agreement between orthography2ipa and "
        "espeak-ng, for every language where this repo has both a gold-"
        "dataset wordlist and espeak-ng has a voice. This is NOT an "
        "accuracy benchmark — see `docs/benchmarks.md` for what it means "
        "and does not mean. Regenerate with:",
        "",
        "```bash",
        "PYTHONPATH=$PWD python scripts/espeak_agreement.py --scoreboard",
        "```",
        "",
        "Machine-readable form: [`benchmarks/espeak_agreement.json`]"
        "(../benchmarks/espeak_agreement.json).",
        "",
        "| Lang | espeak voice | N | Exact | Exact (no stress) | "
        "Segmental | OOV rate |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['lang']} | {row['voice']} | {row['n']} | "
            f"{row['exact']:.4f} | {row['exact_nostress']:.4f} | "
            f"{row['segmental']:.4f} | {row['oov_rate']:.4f} |"
        )
    lines.append("")
    os.makedirs(os.path.dirname(AGREEMENT_MD), exist_ok=True)
    with open(AGREEMENT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--lang", choices=sorted(SOURCES))
    ap.add_argument("--limit", type=int, default=300)
    ap.add_argument("--list", action="store_true",
                    help="List languages and their espeak voices")
    ap.add_argument("--scoreboard", action="store_true",
                    help="Run every SOURCES language with an espeak-ng "
                         "voice and write docs/espeak_agreement.md + "
                         "benchmarks/espeak_agreement.json")
    args = ap.parse_args()

    if args.scoreboard:
        rows = build_agreement_scoreboard(args.limit)
        write_agreement_scoreboard(rows)
        print(f"wrote {len(rows)} rows to "
              f"{os.path.relpath(AGREEMENT_MD, REPO_ROOT)} and "
              f"{os.path.relpath(AGREEMENT_JSON, REPO_ROOT)}")
        return

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
