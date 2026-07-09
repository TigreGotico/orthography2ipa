#!/usr/bin/env python3
"""Benchmark the orthography2ipa G2P engine against gold pronunciation sets.

Self-contained evaluation harness for this library: it loads a gold
dataset, transcribes every word with :class:`orthography2ipa.G2P`, and
reports PER (phoneme error rate) and WER (word error rate). The
datasets, their sources and the methodology are documented in
``docs/benchmarks.md``.

Usage::

    python scripts/benchmark.py --dataset portuguese_lexicon --lang pt-PT
    python scripts/benchmark.py --dataset wikipron --lang gl --broad
    python scripts/benchmark.py --dataset mirandese --lang mwl
    python scripts/benchmark.py --list

Dataset access:

- ``portuguese_lexicon`` needs the ``tugalex`` package
  (https://github.com/TigreGotico/tugalex), which wraps the
  TigreGotico/portuguese_phonetic_lexicon dataset on Hugging Face.
- ``cmudict`` needs the ``scriptconv`` package for ARPABET→IPA.
- ``wikipron`` and ``mirandese`` download TSVs directly (stdlib only).

Every run is capped (``--limit``, default 300) — gold sets are large
and a slice is enough for a stable reference number.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
import unicodedata
import urllib.request
from typing import Dict, List, Optional, Tuple

# the repository root precedes the installed package so that running the
# script from a checkout measures THAT checkout
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CACHE_DIR = os.path.join(os.path.dirname(__file__), "..", ".benchmark_cache")

HARNESS_VERSION = "1.0"
SCOREBOARD_MD = os.path.join(REPO_ROOT, "docs", "scoreboard.md")
SCOREBOARD_JSON = os.path.join(REPO_ROOT, "benchmarks", "results.json")

_STRESS_MARKS = "ˈˌ"
_NARROW_MARKS = "̝̞̪̘̙͜͡.·‿()"

_WIKIPRON_BASE = (
    "https://raw.githubusercontent.com/CUNY-CL/wikipron/master/data/scrape/tsv/"
)
_WIKIPRON_FILES = {
    # --- already wired ---
    "gl": "glg_latn_broad.tsv",
    "es": "spa_latn_la_broad.tsv",
    "pt": "por_latn_po_broad.tsv",
    "pt-BR": "por_latn_bz_broad.tsv",
    "en": "eng_latn_us_broad.tsv",
    "en-GB": "eng_latn_uk_broad.tsv",
    # --- Romance ---
    "it": "ita_latn_broad.tsv",          # ~90k rows
    "fr": "fra_latn_broad.tsv",          # ~98k rows
    "ro": "ron_latn_broad.tsv",          # ~9k rows
    "ast": "ast_latn_broad.tsv",         # ~4k rows
    "oc": "oci_latn_broad.tsv",          # ~750 rows
    # --- Germanic ---
    "de": "deu_latn_broad.tsv",          # ~60k rows
    "nl": "nld_latn_broad.tsv",          # ~59k rows
    "sv": "swe_latn_broad.tsv",          # ~6k rows
    "da": "dan_latn_broad.tsv",          # ~5k rows
    "nb": "nob_latn_broad.tsv",          # ~3k rows
    "is": "isl_latn_broad.tsv",          # ~11k rows
    # --- Celtic ---
    "cy": "cym_latn_nw_broad.tsv",       # ~17k rows (NW dialect)
    "ga": "gle_latn_broad.tsv",          # ~21k rows
    "gd": "gla_latn_broad.tsv",          # ~6k rows
    # --- Slavic ---
    "pl": "pol_latn_broad.tsv",          # ~157k rows
    "sk": "slk_latn_broad.tsv",          # ~16k rows
    "hr": "hbs_latn_broad.tsv",          # ~26k rows (hbs covers hr/bs/sr Latin)
    # --- Other Indo-European ---
    "el": "ell_grek_broad.tsv",          # ~20k rows
    "hy": "hye_armn_e_broad.tsv",        # ~18k rows (Eastern Armenian)
    "sq": "sqi_latn_broad.tsv",          # ~5k rows
    "tr": "tur_latn_broad.tsv",          # ~12k rows
    # --- Uralic / Basque ---
    "fi": "fin_latn_broad.tsv",          # ~173k rows
    "eu": "eus_latn_broad.tsv",          # ~20k rows
    # --- Other ---
    "tl": "tgl_latn_broad.tsv",          # ~28k rows
    "eo": "epo_latn_broad.tsv",          # ~41k rows
    # --- Indo-Aryan / Dravidian (native script) ---
    "hi": "hin_deva_broad.tsv",          # ~33k rows, Devanagari
    "ta": "tam_taml_broad.tsv",          # ~10k rows, Tamil script
    "ml": "mal_mlym_broad.tsv",          # ~10k rows, Malayalam script
}
_MIRANDESE_URL = (
    "https://huggingface.co/datasets/TigreGotico/mirandese_g2p"
    "/resolve/main/mwl_dataset.tsv"
)
_MIRANDESE_DIALECTS = {"mwl": "central", "mwl-x-sendim": "sendinese"}
_CMUDICT_URL = (
    "https://raw.githubusercontent.com/cmusphinx/cmudict/master/cmudict.dict"
)
# ipa-dict: open pronunciation dictionaries maintained by the open-dict-data project.
# Source per-language; always verify provenance via the Credits section of the README.
# https://github.com/open-dict-data/ipa-dict
_IPADICT_BASE = (
    "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/"
)
# Icelandic: from the Hjal project / "Pronunciation Dictionary for Icelandic"
# (Malfong.is), CC BY 3.0. ~60k entries. Human-curated by Icelandic linguists.
_IPADICT_FILES = {
    "is": "is.txt",
}


_FETCH_ATTEMPTS = 3
_FETCH_BACKOFF_SECONDS = 1.5


def _fetch(url: str, name: str) -> str:
    os.makedirs(CACHE_DIR, exist_ok=True)
    dest = os.path.join(CACHE_DIR, name)
    if not os.path.exists(dest):
        last_exc: Optional[Exception] = None
        for attempt in range(1, _FETCH_ATTEMPTS + 1):
            try:
                urllib.request.urlretrieve(url, dest)
                last_exc = None
                break
            except Exception as exc:  # transient network hiccups
                last_exc = exc
                if attempt < _FETCH_ATTEMPTS:
                    time.sleep(_FETCH_BACKOFF_SECONDS * attempt)
        if last_exc is not None:
            raise last_exc
    with open(dest, encoding="utf-8", errors="replace") as fh:
        return fh.read()


# ─── dataset loaders ────────────────────────────────────────────────────────

def load_portuguese_lexicon(lang: str, limit: int) -> List[Tuple[str, str]]:
    """Portal da Língua Portuguesa lexicon, one region per language tag.

    Loaded through ``tugalex``; the underlying data is the
    TigreGotico/portuguese_phonetic_lexicon dataset on Hugging Face
    (~617k entries scraped from the INESC-ID Portal da Língua
    Portuguesa, with per-region IPA).
    """
    from tugalex import TugaLexicon  # https://github.com/TigreGotico/tugalex

    lex = TugaLexicon()
    region = lex.lang_to_region(lang)
    ipa_map = lex.get_ipa_map(region=region)
    return list(ipa_map.items())[:limit]


def load_wikipron(lang: str, limit: int) -> List[Tuple[str, str]]:
    """WikiPron broad transcriptions (community-curated Wiktionary IPA)."""
    fname = _WIKIPRON_FILES[lang]
    text = _fetch(_WIKIPRON_BASE + fname, fname)
    pairs = []
    for line in text.strip().splitlines():
        parts = line.split("\t")
        if len(parts) == 2:
            pairs.append((parts[0], parts[1]))
        if len(pairs) >= limit:
            break
    return pairs


def load_mirandese(lang: str, limit: int) -> List[Tuple[str, str]]:
    """Mirandese gold set (TigreGotico/mirandese_g2p on Hugging Face)."""
    dialect = _MIRANDESE_DIALECTS[lang]
    text = _fetch(_MIRANDESE_URL, "mirandese_g2p.tsv")
    pairs = []
    for line in text.strip().splitlines()[1:]:
        parts = line.split("\t")
        if len(parts) == 3 and parts[0] == dialect:
            pairs.append((parts[1].strip(), parts[2].strip()))
        if len(pairs) >= limit:
            break
    return pairs


def load_cmudict(lang: str, limit: int) -> List[Tuple[str, str]]:
    """CMU Pronouncing Dictionary (en-US), ARPABET converted to IPA."""
    from scriptconv.notation import arpa_to_ipa  # TigreGotico/scriptconv

    text = _fetch(_CMUDICT_URL, "cmudict.dict")
    pairs, seen = [], set()
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith(";;;"):
            continue
        parts = line.split()
        word = parts[0].lower()
        if "(" in word or word in seen or len(parts) < 2:
            continue
        seen.add(word)
        pairs.append((word, arpa_to_ipa(" ".join(parts[1:]))))
        if len(pairs) >= limit:
            break
    return pairs


def load_ipadict(lang: str, limit: int) -> List[Tuple[str, str]]:
    """ipa-dict pronunciation dictionaries (open-dict-data/ipa-dict).

    Provenance is **per-language** — see ``_IPADICT_FILES`` docstrings and
    the project README Credits section before adding new languages. Each
    entry uses the format ``word TAB /IPA/`` with IPA enclosed in slashes.

    Currently wired languages:

    - ``is`` (Icelandic): from the Hjal project / "Pronunciation Dictionary
      for Icelandic" (malfong.is), CC BY 3.0, ~60k human-curated entries.
    """
    fname = _IPADICT_FILES[lang]
    text = _fetch(_IPADICT_BASE + fname, f"ipadict_{fname}")
    pairs = []
    for line in text.strip().splitlines():
        parts = line.split("\t")
        if len(parts) == 2:
            word = parts[0].strip().lower()
            ipa = parts[1].strip().strip("/")
            if word and ipa:
                pairs.append((word, ipa))
        if len(pairs) >= limit:
            break
    return pairs



# Dialect code mapping for ep_dialects dataset
# CSV dialect_code  →  orthography2ipa language tag
# ─────────────────────────────────────────────────────────────────────────────
# lisboa    → pt-PT-x-lisbon   (Lisbon prestige variety)
# north     → pt-PT-x-porto    (Porto/Baixo-Minho representative Northern EP)
# central   → pt-PT            (Coimbra-type conservative standard; the Centro-
#                               Litoral/Estremenho dialect is the closest match
#                               to the "ideal standard" PT-PT in the codebase)
# alentejo  → pt-PT-x-alentejo
# algarve   → pt-PT-x-algarve
# madeira   → pt-PT-x-madeira
# azores    → pt-PT-x-acores
_EP_DIALECT_MAP: Dict[str, str] = {
    "pt-PT-x-lisboa": "pt-PT-x-lisbon",
    "pt-PT-x-north": "pt-PT-x-porto",
    "pt-PT-x-central": "pt-PT",
    "pt-PT-x-alentejo": "pt-PT-x-alentejo",
    "pt-PT-x-algarve": "pt-PT-x-algarve",
    "pt-PT-x-madeira": "pt-PT-x-madeira",
    "pt-PT-x-azores": "pt-PT-x-acores",
}

_EP_DIALECT_GOLD_CSV = os.path.join(
    os.path.dirname(__file__), "..", "tests", "data", "ep_dialect_sentences.csv"
)


def load_ep_dialects(lang: str, limit: int) -> List[Tuple[str, str]]:
    """European Portuguese regional dialect gold set (sentence-level).

    Source: TigreGotico internal dialect research (DIALECT_PATTERNS.md +
    whitepaper5 IPA dialect transforms).  250 sentences across seven EP
    regional varieties, manually annotated IPA, pending external
    peer-validation.

    Dialect code mapping (CSV dialect_code → orthography2ipa tag):
        pt-PT-x-lisboa   → pt-PT-x-lisbon
        pt-PT-x-north    → pt-PT-x-porto
        pt-PT-x-central  → pt-PT   (Coimbra-type standard)
        pt-PT-x-alentejo → pt-PT-x-alentejo
        pt-PT-x-algarve  → pt-PT-x-algarve
        pt-PT-x-madeira  → pt-PT-x-madeira
        pt-PT-x-azores   → pt-PT-x-acores

    The ``lang`` parameter accepts **either** the CSV dialect_code (e.g.
    ``pt-PT-x-north``) or the mapped orthography2ipa tag (e.g.
    ``pt-PT-x-porto``); both forms work transparently.
    """
    # Build reverse map so callers can pass either key
    reverse_map = {v: k for k, v in _EP_DIALECT_MAP.items()}
    csv_key = reverse_map.get(lang, lang)  # normalise to CSV-side key

    pairs: List[Tuple[str, str]] = []
    with open(_EP_DIALECT_GOLD_CSV, encoding="utf-8") as fh:
        next(fh)  # skip header
        for row in csv.reader(fh):
            if len(row) != 3:
                continue
            dialect_code, text, ipa = row
            if dialect_code == csv_key:
                # Strip phonemic-transcription delimiters /…/ from gold IPA
                pairs.append((text.strip(), ipa.strip().strip("/")))
            if len(pairs) >= limit:
                break
    return pairs


_EP_DIALECT_LANGS = sorted(_EP_DIALECT_MAP.values())

DATASETS = {
    "ep_dialects": (load_ep_dialects, _EP_DIALECT_LANGS),
    "portuguese_lexicon": (load_portuguese_lexicon,
                           ["pt-PT", "pt-BR", "pt-AO", "pt-MZ", "pt-TL"]),
    "wikipron": (load_wikipron, sorted(_WIKIPRON_FILES)),
    "mirandese": (load_mirandese, sorted(_MIRANDESE_DIALECTS)),
    "cmudict": (load_cmudict, ["en-US"]),
    "ipadict": (load_ipadict, sorted(_IPADICT_FILES)),
}


# ─── metric ─────────────────────────────────────────────────────────────────

def normalize(ipa: str, strip_stress: bool, broad: bool) -> str:
    s = unicodedata.normalize("NFC", ipa)
    if strip_stress:
        for ch in _STRESS_MARKS:
            s = s.replace(ch, "")
    if broad:
        decomposed = unicodedata.normalize("NFD", s)
        s = unicodedata.normalize(
            "NFC", "".join(c for c in decomposed if c not in _NARROW_MARKS))
    # comparison is segmentation-free: some gold sets space-separate phonemes
    return "".join(s.split())


def levenshtein(a: str, b: str) -> int:
    if a == b:
        return 0
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        curr = [i]
        for j, cb in enumerate(b, 1):
            curr.append(min(prev[j] + 1, curr[j - 1] + 1,
                            prev[j - 1] + (ca != cb)))
        prev = curr
    return prev[-1]


def evaluate(pairs, lang: str, strip_stress: bool, broad: bool):
    from orthography2ipa import G2P

    engine = G2P(lang)
    # gold sets may carry several valid transcriptions per word
    # (dialect variants); score against all, keep the best
    refs: Dict[str, List[str]] = {}
    for word, gold in pairs:
        refs.setdefault(word, []).append(gold)

    per_sum, wrong, covered = 0.0, 0, 0
    for word, golds in refs.items():
        try:
            hyp = normalize(engine.transcribe_word(word),
                            strip_stress, broad)
        except Exception:
            continue
        if not hyp:
            continue
        covered += 1
        per = min(
            levenshtein(hyp, g) / max(len(g), 1)
            for g in (normalize(x, strip_stress, broad) for x in golds)
        )
        per_sum += per
        wrong += per > 0
    n = len(refs)
    return n, covered, (per_sum / covered if covered else 1.0), \
        (wrong / covered if covered else 1.0)


def _quality_tier(lang: str) -> Optional[str]:
    """Look up the spec quality tier for a language tag, if the tag has
    a registered spec. Returns ``None`` when no spec resolves (e.g. a
    dataset dialect key that isn't itself a registered language code)."""
    from orthography2ipa import get

    try:
        return get(lang).quality.value
    except Exception:
        return None


def build_scoreboard(limit: int) -> List[dict]:
    """Run every registered gold dataset/language combination and
    return deterministic scoreboard rows sorted by language tag."""
    rows: List[dict] = []
    for dataset_name, (loader, langs) in DATASETS.items():
        for lang in langs:
            try:
                pairs = loader(lang, limit)
            except Exception as exc:
                print(f"skip {dataset_name} lang={lang}: {exc}",
                      file=sys.stderr)
                continue
            n, covered, per, wer = evaluate(
                pairs, lang, strip_stress=True, broad=True,
            )
            rows.append({
                "lang": lang,
                "dataset": dataset_name,
                "n": covered,
                "per": round(per, 4),
                "exact_match": round(1.0 - wer, 4),
                "quality_tier": _quality_tier(lang),
                "harness_version": HARNESS_VERSION,
                "limit": limit,
            })
    rows.sort(key=lambda r: (r["lang"], r["dataset"]))
    return rows


def write_scoreboard(rows: List[dict]) -> None:
    os.makedirs(os.path.dirname(SCOREBOARD_JSON), exist_ok=True)
    with open(SCOREBOARD_JSON, "w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    lines = [
        "# Scoreboard",
        "",
        "Committed PER/exact-match results for every gold dataset/language "
        "combination registered in `scripts/benchmark.py`. Regenerate with:",
        "",
        "```bash",
        "PYTHONPATH=$PWD python scripts/benchmark.py --scoreboard",
        "```",
        "",
        "Machine-readable form: [`benchmarks/results.json`]"
        "(../benchmarks/results.json). Methodology and dataset provenance: "
        "[`docs/benchmarks.md`](benchmarks.md).",
        "",
        "| Lang | Dataset | N | PER | Exact match | Quality tier |",
        "|---|---|---:|---:|---:|---|",
    ]
    for row in rows:
        tier = row["quality_tier"] or "-"
        lines.append(
            f"| {row['lang']} | {row['dataset']} | {row['n']} | "
            f"{row['per']:.4f} | {row['exact_match']:.4f} | {tier} |"
        )
    lines.append("")
    os.makedirs(os.path.dirname(SCOREBOARD_MD), exist_ok=True)
    with open(SCOREBOARD_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dataset", choices=sorted(DATASETS))
    ap.add_argument("--lang", default=None)
    ap.add_argument("--limit", type=int, default=300)
    ap.add_argument("--keep-stress", action="store_true",
                    help="Compare stress marks too (stripped by default)")
    ap.add_argument("--narrow", action="store_true",
                    help="Keep narrow-transcription diacritics "
                         "(stripped by default)")
    ap.add_argument("--list", action="store_true",
                    help="List datasets and their languages")
    ap.add_argument("--scoreboard", action="store_true",
                    help="Run every registered gold dataset/language "
                         "combination and write docs/scoreboard.md + "
                         "benchmarks/results.json")
    args = ap.parse_args()

    if args.scoreboard:
        rows = build_scoreboard(args.limit)
        write_scoreboard(rows)
        print(f"wrote {len(rows)} rows to "
              f"{os.path.relpath(SCOREBOARD_MD, REPO_ROOT)} and "
              f"{os.path.relpath(SCOREBOARD_JSON, REPO_ROOT)}")
        return

    if args.list or not args.dataset:
        for name, (_, langs) in sorted(DATASETS.items()):
            print(f"{name:22} {', '.join(langs)}")
        return

    loader, langs = DATASETS[args.dataset]
    lang = args.lang or langs[0]
    if lang not in langs:
        sys.exit(f"{args.dataset} supports: {langs}")

    pairs = loader(lang, args.limit)
    n, covered, per, wer = evaluate(
        pairs, lang,
        strip_stress=not args.keep_stress,
        broad=not args.narrow,
    )
    print(f"{args.dataset} lang={lang} n={n} covered={covered} "
          f"PER={per:.4f} WER={wer:.4f}")


if __name__ == "__main__":
    main()
