#!/usr/bin/env python3
"""Find alphabetic characters that appear in a gating gold set's orthography
but that the RESOLVED spec cannot see at all.

enm shipped no grapheme entry for ⟨y⟩ anywhere — not in ``graphemes``, not in
``positional_graphemes`` — so the engine dropped it silently instead of
erroring (ymage -> maɡɛ, yong -> ɔnɡ). Grepping a spec's own JSON file for
its ``graphemes`` dict would have found this gap already, but it would ALSO
flag hundreds of false positives for every spec that inherits its grapheme
table from a parent through ``graphemes_base`` — a spec's own dict may hold
only overrides while the base carries the rest. The only trustworthy view is
the one the engine itself uses: ``orthography2ipa.get(lang)``, which returns
the spec with inheritance already resolved.

Even the resolved character surface is not the whole truth. A character can
be entirely absent from every grapheme/positional_graphemes/word_exceptions
key and still transcribe correctly, when the tokenizer handles it through
Unicode decomposition rather than a table lookup — Ancient Greek's accented
vowels (ά, έ, ί) are not grapheme keys, but λόγος still comes out ``loɡos``.
So "not a grapheme key" does not imply "dropped": this script additionally
transcribes the bare character in isolation and only reports a character as
a CONFIRMED drop when that isolated transcription comes back empty.
Everything else the resolved spec cannot see is reported as a CANDIDATE,
needing a human or a targeted gold check to confirm.

Usage::

    python scripts/check_unmapped_graphemes.py                     # every gating lang, every dataset
    python scripts/check_unmapped_graphemes.py --lang enm          # one language
    python scripts/check_unmapped_graphemes.py --dataset wikipron  # one dataset, every language it gates

Only gating languages whose gold is already cached under ``.benchmark_cache``
are scored — this avoids triggering a download for every registered dataset.
Network access is blocked for the duration of the run, so any dataset/lang
combination without a local cache hit is skipped, not fetched.

An unscoped run iterates every dataset in ``benchmark.DATASETS`` — some
register hundreds of languages — so it can take a long time even with
network blocked; narrow with ``--dataset``/``--lang``/``--limit`` (default
2000 gold rows per language) for a fast check, and treat a full run as a
periodic sweep rather than a per-PR gate.
"""
from __future__ import annotations

import argparse
import sys
import unicodedata
from collections import defaultdict
from typing import Dict, Set

sys.path.insert(0, __file__.rsplit("/scripts/", 1)[0])
sys.path.insert(0, __file__.rsplit("/check_unmapped_graphemes.py", 1)[0])

import benchmark  # noqa: E402
from orthography2ipa import get  # noqa: E402
from orthography2ipa.g2p import G2P  # noqa: E402


def _block_network(*_args, **_kwargs):
    raise RuntimeError("network access blocked: gold is not cached")


def _is_alpha(ch: str) -> bool:
    return unicodedata.category(ch).startswith("L")


def _known_characters(spec) -> Set[str]:
    """Every character the resolved spec's grapheme surface can see: the
    flat ``graphemes`` table, ``positional_graphemes`` keys, and
    ``word_exceptions`` keys (an exception entry proves the spec has some
    handling for the characters it spells, even without a generic rule)."""
    known: Set[str] = set()
    for key in spec.graphemes or {}:
        known.update(key.lower())
    for key in (spec.positional_graphemes or {}):
        known.update(str(key).lower())
    for key in (spec.word_exceptions or {}) or {}:
        known.update(key.lower())
    return known


def _cached_gold_words(dataset_name: str, loader, langs, limit: int = 2000):
    """Yield (lang, {orthographic words}) for every language in *langs*
    whose gold is already on disk. A network-requiring lang raises inside
    the blocked urlretrieve and is skipped."""
    for lang in langs:
        try:
            pairs = loader(lang, limit)
        except Exception:
            continue
        if not pairs:
            continue
        yield lang, {word for word, _ipa in pairs}


def check_language(lang: str, words: Set[str]) -> Dict[str, dict]:
    """Return {character: {"count": n, "confirmed": bool}} for characters
    the resolved spec cannot see."""
    try:
        spec = get(lang)
    except Exception:
        return {}
    known = _known_characters(spec)
    counts: Dict[str, int] = defaultdict(int)
    for word in words:
        for ch in word.lower():
            if _is_alpha(ch) and ch not in known:
                counts[ch] += 1
    if not counts:
        return {}

    engine = G2P(lang)
    flagged = {}
    for ch, count in counts.items():
        try:
            isolated = engine.transcribe_word(ch)
        except Exception:
            isolated = ""
        flagged[ch] = {"count": count, "confirmed": not bool(isolated.strip())}
    return flagged


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lang", help="restrict to one spec code")
    ap.add_argument("--dataset", help="restrict to one dataset name "
                     "(see benchmark.DATASETS); a full unscoped run iterates "
                     "every dataset and can take a long time even cache-only")
    ap.add_argument("--limit", type=int, default=2000,
                     help="max gold rows read per language (default 2000)")
    args = ap.parse_args()

    orig_urlretrieve = benchmark.urllib.request.urlretrieve
    benchmark.urllib.request.urlretrieve = _block_network
    try:
        per_lang: Dict[str, Dict[str, dict]] = {}
        for dataset_name, (loader, langs) in benchmark.DATASETS.items():
            if args.dataset and dataset_name != args.dataset:
                continue
            scoped_langs = ([args.lang] if args.lang in langs else []) if args.lang else langs
            for lang, words in _cached_gold_words(dataset_name, loader, scoped_langs,
                                                   limit=args.limit):
                if lang in per_lang:
                    continue  # already scored against another dataset's gold
                flagged = check_language(lang, words)
                if flagged:
                    per_lang[lang] = flagged
    finally:
        benchmark.urllib.request.urlretrieve = orig_urlretrieve

    confirmed_total = candidate_total = 0
    for lang in sorted(per_lang):
        confirmed = {c: d for c, d in per_lang[lang].items() if d["confirmed"]}
        candidates = {c: d for c, d in per_lang[lang].items() if not d["confirmed"]}
        if confirmed:
            print(f"\n{lang}: CONFIRMED dropped (isolated transcription is empty)")
            for ch, d in sorted(confirmed.items(), key=lambda kv: -kv[1]["count"]):
                print(f"  {ch!r}  n={d['count']}")
            confirmed_total += len(confirmed)
        if candidates:
            print(f"\n{lang}: candidates (unseen by the resolved spec, "
                  "but isolated transcription is non-empty -- needs confirmation)")
            for ch, d in sorted(candidates.items(), key=lambda kv: -kv[1]["count"]):
                print(f"  {ch!r}  n={d['count']}")
            candidate_total += len(candidates)

    print(f"\n{confirmed_total} confirmed drop(s), {candidate_total} candidate(s), "
          f"across {len(per_lang)} language(s) with any finding.")
    return 1 if confirmed_total else 0


if __name__ == "__main__":
    raise SystemExit(main())
