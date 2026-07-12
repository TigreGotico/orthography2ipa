#!/usr/bin/env python3
"""Benchmark the orthography2ipa G2P engine against gold pronunciation sets.

Self-contained evaluation harness for this library: it loads a gold
dataset, transcribes every word with :class:`orthography2ipa.G2P`, and
reports PER (phoneme error rate) and WER (word error rate). The
datasets, their sources and the methodology are documented in
``docs/benchmarks.md``.

Usage::

    python scripts/benchmark.py --dataset portuguese_phonetic_lexicon --lang pt-PT
    python scripts/benchmark.py --dataset wikipron --lang gl --broad
    python scripts/benchmark.py --dataset mirandese_g2p --lang mwl
    python scripts/benchmark.py --list

Dataset access:

- ``cmudict`` needs the ``scriptconv`` package for ARPABET→IPA.
- ``wikipron`` and ``mirandese_g2p`` download TSVs directly (stdlib only).
- ``infopedia_pt`` downloads a JSONL gold file directly and samples it with
  a fixed seed (stdlib only).
- ``portuguese_phonetic_lexicon`` downloads the Portal da Língua Portuguesa
  CSV directly and samples it per region with a fixed seed (stdlib only).
- ``hitz_basque_ipa`` pages the HiTZ/wikipedia_basque_ipa Hugging Face
  dataset through the datasets-server "rows" REST API (stdlib only,
  no full-parquet download).
- ``clup_dialect`` downloads a CSV gold file directly (stdlib only).
- ``styletts2_phonemes`` downloads per-language JSON files directly
  (stdlib only).
- ``ipa_childes`` downloads per-language CSVs from the
  fdemelo/ipa-childes-split Hugging Face dataset directly (stdlib only).
- ``ipa_babylm`` downloads the dev-split CSVs of the
  phonemetransformers/IPA-BabyLM Hugging Face dataset directly (stdlib only).

The committed ``--scoreboard`` scores the FULL gold set of every language
with NO cap (uniformly — no per-language limit juggling); the published
docs/scoreboard.md is full-dataset. ``--limit N`` still applies a uniform
cap for ad-hoc fast runs, and the CI regression gate re-scores at a fixed
uniform sample (see ``--ci-sample`` and check_benchmark_regression.py). A
few loaders keep an intrinsic, language-agnostic infrastructure bound that
``--limit`` cannot lift (e.g. ``hitz_basque_ipa`` pages the HF rows API and
stops at ``_HITZ_BASQUE_MAX_PARAGRAPHS`` rather than pulling the full
1.67M-row set) — these are documented in docs/benchmarks.md.
"""
from __future__ import annotations

import argparse
import contextlib
import csv
import json
import os
import random
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from typing import Dict, List, Optional, Tuple

# the repository root precedes the installed package so that running the
# script from a checkout measures THAT checkout
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CACHE_DIR = os.path.join(os.path.dirname(__file__), "..", ".benchmark_cache")

HARNESS_VERSION = "1.1"

# Fixed seed for the bootstrap confidence-interval resampling below --
# never randomized, so the same per-word PER list always yields the same
# CI bounds across runs/machines.
BOOTSTRAP_SEED = 20260710
BOOTSTRAP_REPS = 1000

# Fixed seed for loaders that draw a random sample from a large gold file
# (infopedia_pt, portuguese_phonetic_lexicon) instead of the alphabetical
# head. Never randomized, so the same ``limit`` always selects the same
# words across runs/machines — an unbiased but fully reproducible slice.
SAMPLE_SEED = 20260711
SCOREBOARD_MD = os.path.join(REPO_ROOT, "docs", "scoreboard.md")
SCOREBOARD_JSON = os.path.join(REPO_ROOT, "benchmarks", "results.json")
LEXICON_SCOREBOARD_MD = os.path.join(REPO_ROOT, "docs", "lexicon_scoreboard.md")
LEXICON_SCOREBOARD_JSON = os.path.join(
    REPO_ROOT, "benchmarks", "lexicon_results.json")

# ── CI regression sample ────────────────────────────────────────────────────
# The committed scoreboard (SCOREBOARD_JSON) is FULL-dataset — every gold
# word of every language, no cap — which is far too slow to re-run inside a
# CI job (the 617k-row portuguese_phonetic_lexicon and 102k-row infopedia_pt
# alone take the better part of an hour). So the CI regression gate re-scores
# at a fixed, UNIFORM sample size — the SAME cap for every language, no
# per-language juggling — and compares against a SEPARATE baseline committed
# at that identical cap (never against the full scoreboard, so there is never
# a mixed-slice comparison). Generate/refresh it with
# ``scripts/benchmark.py --ci-sample``.
CI_SAMPLE_LIMIT = 1000
CI_SAMPLE_JSON = os.path.join(REPO_ROOT, "benchmarks", "results_ci_sample.json")

#: Stress marks stripped from BOTH sides when ``strip_stress`` is set.
#: U+02C8/U+02CC are the IPA primary/secondary marks. The ASCII apostrophe is
#: not IPA at all, but several expert gold sets (4catac) use it as the stress
#: mark — leaving it in made every stressed syllable in the gold an unmatched
#: character, which cost Catalan ~7 PER points of pure notation. The IPA
#: modifier apostrophe U+02BC is deliberately NOT here: it marks ejectives and
#: is a real segment.
_STRESS_MARKS = "ˈˌ'"
#: Tie bars are notation, not phonology: t͡s and ts are the same phoneme
#: string at every transcription tier, so they are stripped from BOTH
#: sides unconditionally (unlike the narrow diacritics below, which only
#: strip under --broad).
_TIE_BARS = "͜͡‿"

_NARROW_MARKS = "̝̞̪̺̼̘̙.·()"
#: Prosodic/orthographic punctuation carried by sentence-level gold sets
#: (phrase breaks, commas, full stops). None of it is a phoneme, so scoring it
#: as one penalises a transcription for text the engine correctly ignores.
_PUNCT_MARKS = "|‖,.;:!?¡¿\"«»—–-"

_WIKIPRON_BASE = (
    "https://raw.githubusercontent.com/CUNY-CL/wikipron/master/data/scrape/tsv/"
)
_WIKIPRON_FILES = {
    # --- Iberian ---
    # Catalan's only other gold (4catac) is 160 expert SENTENCES; this is its
    # sole word-level set. Small (176 rows) but it isolates grapheme->phoneme
    # accuracy from the sentence-level stress and sandhi the other gold mixes in.
    "ca": "cat_latn_broad.tsv",
    "an": "arg_latn_broad.tsv",          # Aragonese, ~1.3k rows
    "lad": "lad_latn_broad.tsv",         # Ladino, ~145 rows
    # --- already wired ---
    "gl": "glg_latn_broad.tsv",
    "es": "spa_latn_la_broad.tsv",
    "pt": "por_latn_po_broad.tsv",
    "pt-BR": "por_latn_bz_broad.tsv",
    "en": "eng_latn_us_broad.tsv",
    "en-GB": "eng_latn_uk_broad.tsv",
    # --- Semitic ---
    "ar": "ara_arab_broad.tsv",          # ~17.5k rows (MSA, broad)
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
    # Russian: WikiPron only scraped a NARROW transcription for Russian
    # (per upstream README: "some languages only have broad or narrow
    # transcriptions, e.g. Russian only has the latter"), so this is the
    # narrow file. The harness's default normalization already strips
    # narrow-transcription diacritics (see ``_NARROW_MARKS``) before
    # scoring, so it is directly comparable to the broad-tier gold sets
    # used for the other languages above.
    "ru": "rus_cyrl_narrow.tsv",         # ~ large, Cyrillic, narrow-only
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
# orthography2ipa language tag → the value of the dataset's ``dialect``
# column scored under it. The 218-entry ``mwl_dataset.tsv`` tags each row
# ``central`` (the Central norm the Mirandese orthography is built on),
# ``sendinese`` (Sendinês, the Sendim sub-dialect) or ``raiano`` (the
# Raiano/Northern sub-dialect, whose local variety this repo tags
# ``mwl-x-ifanes`` after Ifanês). Every row is scored under exactly one tag.
_MIRANDESE_DIALECTS = {
    "mwl": "central",
    "mwl-x-sendim": "sendinese",
    "mwl-x-ifanes": "raiano",
}
_BARRANQUENHO_DICT_URL = (
    "https://huggingface.co/datasets/TigreGotico/barranquenho-ipa-dict-synthetic"
    "/resolve/main/barranquenho_ipa_dictionary.csv"
)
_MIRANDESE_DICT_URL = (
    "https://huggingface.co/datasets/TigreGotico/mirandese-ipa-dict-synthetic"
    "/resolve/main/mirandese_phonemizer_dataset.csv"
)
# The synthetic Mirandese dict tags each entry with a ``dialect`` column.
# Values seen: "central", "sendinês", "raiano", and "all" (dialect-neutral
# forms shared by every variety). orthography2ipa language tag → the set of
# ``dialect`` values scored under it. "all"+"central" go to the Central norm
# (``mwl``, the standard the orthography is built on); "raiano" maps to
# ``mwl-x-ifanes`` (Ifanês IS the Northern/Raiano subdialect in this repo's
# spec set); "sendinês" to ``mwl-x-sendim``. Each row is scored under exactly
# one tag (no double-counting of the shared "all" rows across sub-dialects).
_MIRANDESE_DICT_DIALECTS: Dict[str, set] = {
    "mwl": {"central", "all"},
    "mwl-x-sendim": {"sendinês"},
    "mwl-x-ifanes": {"raiano"},
}
_INFOPEDIA_PT_URL = (
    "https://huggingface.co/datasets/TigreGotico/infopedia-pt-ipa"
    "/resolve/main/infopedia_pt_ipa.jsonl"
)
_PT_LEXICON_URL = (
    "https://huggingface.co/datasets/TigreGotico/portuguese_phonetic_lexicon"
    "/resolve/main/dataset.csv"
)
# TigreGotico/portuguese_phonetic_lexicon (~617k rows) scraped from the
# public Portal da Língua Portuguesa (INESC-ID). Its IPA is SEMI-AUTOMATED
# and community-scraped → classified ``crowd-scraped``. Each row carries a
# ``region_code`` for one of ten regional variants (dataset card mapping).
# orthography2ipa spec → the ONE region_code scored under it: the STANDARD
# metropolitan variant of that country/region. Each spec gets a single row.
_PT_LEXICON_REGIONS: Dict[str, str] = {
    "pt-PT": "lbx",   # Lisbon (Standard) — standard European Portuguese
    "pt-BR": "spx",   # São Paulo (Standard) — Brazilian standard
    "pt-AO": "lda",   # Luanda — Angolan Portuguese (only Angola code)
    "pt-MZ": "mpx",   # Maputo (Standard) — Mozambican Portuguese
    "pt-TL": "dli",   # Dili — Timorese Portuguese (only Timor code)
}
# region_codes deliberately NOT scored (each is a non-standard register, or a
# second Brazilian metropolitan norm, of a region already covered by its
# Standard code above; no distinct orthography2ipa spec exists for them, so
# scoring them would duplicate a spec's row or conflate registers):
#   lbn (Lisbon non-std), rjx/rjo (Rio std/non-std), spo (São Paulo non-std),
#   map (Maputo non-std).
_4CATAC_BASE = (
    "https://huggingface.co/datasets/projecte-aina/4catac/resolve/main/"
)
# 4catac file name  →  orthography2ipa language tag
# Balear     → ca-x-balear    (Balearic)
# Central    → ca             (Central/standard Catalan)
# Nord-Occ   → ca-x-occidental (Northwestern/Lleidatà; 4catac's "North-Western"
#                                accent — NOT ca-x-nord, which is Northern
#                                Catalan/Rossellonès, a distinct dialect spoken
#                                in France and not covered by this dataset)
# Val        → ca-x-valencia  (Valencian)
_4CATAC_FILES: Dict[str, str] = {
    "ca": "Projecte BSC frases - Central.tsv",
    "ca-x-balear": "Projecte BSC frases - Balear.tsv",
    "ca-x-occidental": "Projecte BSC frases - Nord-Occ.tsv",
    "ca-x-valencia": "Projecte BSC frases - Val.tsv",
}
_HITZ_BASQUE_ROWS_URL = (
    "https://datasets-server.huggingface.co/rows"
    "?dataset=HiTZ%2Fwikipedia_basque_ipa&config=default&split=train"
    "&offset={offset}&length={length}"
)
_HITZ_BASQUE_PAGE_SIZE = 100
# bound network calls even in the (unlikely) case word yield per
# paragraph is very low -- never let this loader crawl the full 1.67M rows
_HITZ_BASQUE_MAX_PARAGRAPHS = 500

_CLUP_URL = (
    "https://huggingface.co/datasets/TigreGotico/ArquivoDialetalCLUP_ipa"
    "/resolve/main/dataset.csv"
)
# ArquivoDialetalCLUP_ipa rows carry a "<locality>, <district>" region
# label per sentence. District → orthography2ipa dialect tag, using the
# same regional groupings as the existing pt-PT-x-* specs.  Districts
# with no matching spec (e.g. Leiria, split between the Estremadura and
# Beira Litoral dialect areas) are left unmapped and their rows dropped.
_CLUP_DISTRICT_MAP: Dict[str, str] = {
    "Braga": "pt-PT-x-minho",
    "Porto": "pt-PT-x-porto",
    "Viana do Castelo": "pt-PT-x-viana",
    "Terceira": "pt-PT-x-acores",
    "São Miguel": "pt-PT-x-acores",
    "Aveiro": "pt-PT-x-aveiro",
    "Lisboa": "pt-PT-x-lisbon",
    "Faro": "pt-PT-x-algarve",
    "Bragança": "pt-PT-x-trasosmontes",
    "Viseu": "pt-PT-x-beira",
    "Coimbra": "pt-PT-x-beira",
    "Vila Real": "pt-PT-x-trasosmontes",
    "Funchal": "pt-PT-x-madeira",
    "Portalegre": "pt-PT-x-alentejo",
    "Ribeira Brava": "pt-PT-x-madeira",
    "Porto Santo": "pt-PT-x-madeira",
}
# Locality-level overrides: rows whose exact locality has its own spec
# take precedence over the district-level mapping above.
_CLUP_LOCALITY_MAP: Dict[str, str] = {
    "Alfena, Porto": "pt-PT-x-alfena",
}
_CLUP_LANGS = sorted(set(_CLUP_DISTRICT_MAP.values()) | set(_CLUP_LOCALITY_MAP.values()))
_STYLETTS2_PHONEMES_BASE = (
    "https://huggingface.co/datasets/styletts2-community/"
    "multilingual-phonemes-10k-alpha/resolve/main/"
)
# orthography2ipa language tag → dataset config file name.
# All 15 of the dataset's single-language configs are wired (the
# ``en-xl`` config is a 100K-row scale-up of the same "en" language
# already covered by the ``en`` config here plus ``wikipron``/``cmudict``,
# so it is left out as redundant rather than a new gold source).
_STYLETTS2_PHONEMES_FILES: Dict[str, str] = {
    "en": "en.json",
    "ca": "ca.json",
    "de": "de.json",
    "es": "es.json",
    "el": "el.json",
    "fa": "fa.json",
    "fi": "fi.json",
    "fr": "fr.json",
    "it": "it.json",
    "pl": "pl.json",
    "pt": "pt.json",
    "ru": "ru.json",
    "sv": "sv.json",
    "uk": "uk.json",
}

_IPA_CHILDES_BASE = (
    "https://huggingface.co/datasets/fdemelo/ipa-childes-split/resolve/main/"
    "test/{folder}/data.csv"
)
# orthography2ipa language tag → dataset folder (test split only -- the
# dataset's "split" is train/test, and gold benchmark data is drawn from
# the held-out test portion, not train). Folder codes are the dataset's own
# IETF tags (langcodes-normalized, per the dataset card).
#
# lang column carries the CHILDES orthographic "gloss" (renamed
# ``sentence``), except for zh-CN: the dataset's own ``sentence`` column is
# Hanzi, but the zh spec in this repo models Pinyin syllables (its
# grapheme inventory is Pinyin initials/finals, not Hanzi), so zh-CN reads
# the dataset's ``stem`` column instead -- CHILDES's own Pinyin-with-tone-
# numbers romanization of the same utterance, which is what actually
# exercises the zh spec's grapheme table.
#
# Excluded despite a language-code match:
# - fa-IR: CHILDES Persian transcripts in this corpus are Fingilish (ad hoc
#   Latin transliteration, e.g. "piano kar kardam"), never Persian script;
#   the fa spec is Arabic-script only, so there is no clean grapheme match.
# - ja-JP: CHILDES Japanese transcripts here are romaji only (no kana/kanji
#   column in the dataset); the ja spec's grapheme table is hiragana, so
#   there is no clean grapheme match either.
# - ko-KR: WIRABLE NOW, pending verification — the ko spec reads Hangul
#   syllable blocks since the conjoining-jamo graphemes + canonical
#   decomposition landed. This corpus's Korean column still needs its own
#   check (phonemizer tool, romanization vs Hangul) before wiring.
# - yue-CN: the yue spec is a STUB with an empty grapheme inventory (Cantonese
#   is written in Chinese characters); the dataset's own romanized column is
#   Jyutping-with-tone-numbers, which the stub does not model either, so
#   G2P('yue') returns "" for every row.
_IPA_CHILDES_FOLDERS: Dict[str, str] = {
    "ca": "ca-ES",
    "cy": "cy-GB",
    "da": "da-DK",
    "de-DE": "de-DE",
    "en-GB": "en-GB",
    "en-US": "en-US",
    "es-ES": "es-ES",
    "et": "et-EE",
    "eu": "eu-ES",
    "fr-FR": "fr-FR",
    "ga": "ga-IE",
    "hr": "hr-HR",
    "hu": "hu-HU",
    "id": "id-ID",
    "is": "is-IS",
    "it-IT": "it-IT",
    "nb": "nb-NO",
    "nl": "nl-NL",
    "pl": "pl-PL",
    "pt-BR": "pt-BR",
    "pt-PT": "pt-PT",
    "qu": "qu-PE",
    "ro-RO": "ro-RO",
    "sr": "sr-RS",
    "sv": "sv-SE",
    "tr": "tr-TR",
    "zh": "zh-CN",
}
_IPA_CHILDES_STEM_COLUMN = {"zh"}

# The TOOL that produced each language's ``ipa_g2p_plus`` column, verbatim from
# the IPA-CHILDES dataset card's own per-language table
# (https://huggingface.co/datasets/phonemetransformers/IPA-CHILDES). The tool is
# NOT uniform across the corpus, so neither is the reliability of the gold: most
# languages were run through ``phonemizer`` (whose backend is espeak-ng), six
# through ``epitran``, Mandarin through ``pinyin_to_ipa`` and Cantonese through
# ``pingyam``. espeak and epitran are both systems this project benchmarks
# itself AGAINST (docs/comparison.md), so a row scored on their output measures
# agreement with a competitor, not correctness — hence the per-language tiers in
# ``_IPA_CHILDES_PROVENANCE`` below rather than one dataset-wide tier.
_IPA_CHILDES_TOOL: Dict[str, str] = {
    "ca": "phonemizer (espeak-ng), ca",
    "cy": "phonemizer (espeak-ng), cy",
    "da": "phonemizer (espeak-ng), da",
    "de-DE": "epitran, deu-Latn",
    "en-GB": "phonemizer (espeak-ng), en-gb",
    "en-US": "phonemizer (espeak-ng), en-us",
    "es-ES": "epitran, spa-Latn",
    "et": "phonemizer (espeak-ng), et",
    "eu": "phonemizer (espeak-ng), eu",
    "fr-FR": "phonemizer (espeak-ng), fr-fr",
    "ga": "phonemizer (espeak-ng), ga",
    "hr": "epitran, hrv-Latn",
    "hu": "epitran, hun-Latn",
    "id": "epitran, ind-Latn",
    "is": "phonemizer (espeak-ng), is",
    "it-IT": "phonemizer (espeak-ng), it",
    "nb": "phonemizer (espeak-ng), nb",
    "nl": "phonemizer (espeak-ng), nl",
    "pl": "phonemizer (espeak-ng), pl",
    "pt-BR": "phonemizer (espeak-ng), pt-br",
    "pt-PT": "phonemizer (espeak-ng), pt",
    "qu": "phonemizer (espeak-ng), qu",
    "ro-RO": "phonemizer (espeak-ng), ro",
    "sr": "epitran, srp-Latn",
    "sv": "phonemizer (espeak-ng), sv",
    "tr": "phonemizer (espeak-ng), tr",
    "zh": "pinyin_to_ipa, mandarin",
}

# Per-language reliability tier for ipa_childes, derived MECHANICALLY from
# _IPA_CHILDES_TOOL (a test enforces the mapping): phonemizer → espeak-derived,
# epitran → epitran-derived, anything else → machine-generated. Mandarin's
# pinyin_to_ipa is a deterministic Pinyin→IPA table rather than a G2P system we
# compete with, so it stays machine-generated.
_IPA_CHILDES_PROVENANCE: Dict[str, str] = {
    lang: (
        "espeak-derived" if tool.startswith("phonemizer")
        else "epitran-derived" if tool.startswith("epitran")
        else "machine-generated"
    )
    for lang, tool in _IPA_CHILDES_TOOL.items()
}


def load_ipa_childes(lang: str, limit: int) -> List[Tuple[str, str]]:
    """IPA-CHILDES split (fdemelo/ipa-childes-split on Hugging Face):
    a postprocessed version of IPA-CHILDES, the CHILDES child-language
    corpus with automatic phonemic transcriptions ("G2P+"). Sentence-level,
    CSV, one file per language/test-split. The ``ipa_g2p_plus`` column is
    pipe-(" | ")-delimited with one segment per orthographic word, aligned
    positionally with the whitespace-tokenized orthographic sentence, so
    rows are split into word-level (word, IPA) pairs the same way
    ``load_hitz_basque`` derives word pairs from paragraph-level text; rows
    whose token counts don't match are skipped rather than guessed at.
    Only the ``test`` split is used (held out from training the G2P+
    model). Under the full ``--scoreboard`` run (``limit`` unset) the whole
    test split is read and de-duplicated; ``--limit N`` reads only the first
    N de-duplicated pairs.
    """
    folder = _IPA_CHILDES_FOLDERS[lang]
    url = _IPA_CHILDES_BASE.format(folder=folder)
    text = _fetch(url, f"ipa_childes_{folder}.csv")
    text_col = "stem" if lang in _IPA_CHILDES_STEM_COLUMN else "sentence"
    pairs: List[Tuple[str, str]] = []
    seen = set()
    reader = csv.DictReader(text.splitlines())
    for row in reader:
        sentence = (row.get(text_col) or "").strip()
        ipa = (row.get("ipa_g2p_plus") or "").strip()
        if not sentence or not ipa:
            continue
        words = sentence.split()
        phones = [p.strip() for p in ipa.split(" | ")]
        if len(words) != len(phones):
            continue
        for word, phone in zip(words, phones):
            if not word or not phone:
                continue
            key = word.lower()
            if key in seen:
                continue
            seen.add(key)
            pairs.append((word, phone))
            if len(pairs) >= limit:
                break
        if len(pairs) >= limit:
            break
    return pairs


_IPA_BABYLM_BASE = (
    "https://huggingface.co/datasets/phonemetransformers/IPA-BabyLM/"
    "resolve/main/dev/{shard}.csv"
)
# Only the held-out ``dev`` split is read (never train_100M/train_10M — those
# are the LM pre-training portions). The two dataset configs, ``strict`` and
# ``strict-small``, differ ONLY in their train split; they share this dev split,
# so there is exactly one gold set here, not two.
#
# PROVENANCE — the IPA was produced by G2P+ (https://github.com/codebyzeb/
# g2p-plus), which is a wrapper: its backends are ``phonemizer`` and
# ``epitran``. The BabyLM conversion notebook (codebyzeb/babylm-ipa,
# prepare_babylm.ipynb) calls it as ``transcribe_utterances(..., 'phonemizer',
# language='en-us', ...)``, and G2P+'s phonemizer backend requires espeak-ng.
# So this gold is espeak output: espeak-derived, a COMPETITOR's transcription
# (docs/comparison.md). It can neither qualify nor block English.
#
# LICENCE — the dataset card declares none; the underlying BabyLM 2024 corpora
# (BNC, CHILDES, Gutenberg, OpenSubtitles, Simple Wikipedia, Switchboard) keep
# their own licences. Eval-only use.
_IPA_BABYLM_SHARDS = (
    "bnc_spoken",
    "childes",
    "gutenberg",
    "open_subtitles",
    "simple_wiki",
    "switchboard",
)
_BABYLM_WORD_BOUNDARY = "WORD_BOUNDARY"


def load_ipa_babylm(lang: str, limit: int) -> List[Tuple[str, str]]:
    """IPA-BabyLM (phonemetransformers/IPA-BabyLM on Hugging Face): the BabyLM
    2024 pre-training corpora phonemized with G2P+ (espeak-ng under the hood —
    see the provenance note above). English only.

    Sentence-level CSV with a ``text`` column and a ``phonemized_utterance``
    column of space-separated IPA segments with ``WORD_BOUNDARY`` markers
    between words. Rows are split into word-level (word, IPA) pairs by aligning
    the whitespace-tokenized text against the WORD_BOUNDARY-delimited phoneme
    groups; rows whose token counts disagree are skipped rather than guessed
    at, the same way ``load_ipa_childes`` does.
    """
    pairs: List[Tuple[str, str]] = []
    seen = set()
    for shard in _IPA_BABYLM_SHARDS:
        url = _IPA_BABYLM_BASE.format(shard=shard)
        text = _fetch(url, f"ipa_babylm_dev_{shard}.csv")
        reader = csv.DictReader(text.splitlines())
        for row in reader:
            sentence = (row.get("text") or "").strip()
            ipa = (row.get("phonemized_utterance") or "").strip()
            if not sentence or not ipa:
                continue
            words = sentence.split()
            phones = [
                "".join(group.split())
                for group in ipa.split(_BABYLM_WORD_BOUNDARY)
                if group.strip()
            ]
            if len(words) != len(phones):
                continue
            for word, phone in zip(words, phones):
                key = word.lower()
                if not word or not phone or key in seen:
                    continue
                seen.add(key)
                pairs.append((word, phone))
                if len(pairs) >= limit:
                    return pairs
    return pairs


_CMUDICT_URL = (
    "https://raw.githubusercontent.com/cmusphinx/cmudict/master/cmudict.dict"
)
# ipa-dict: open pronunciation dictionaries maintained by the open-dict-data project.
# https://github.com/open-dict-data/ipa-dict — MIT, third-party datasets keep
# their own licence (see the README Credits section, which is the ONLY
# authority on where each file's IPA came from).
#
# The project is MIXED-PROVENANCE: some files are human dictionaries, some are
# Wiktionary scrapes, several are the output of a rule script or phonemizer —
# and `en_UK` is literally espeak output. So this dataset carries a
# PER-LANGUAGE tier (``_IPADICT_PROVENANCE`` below), not a dataset-wide one.
# Every claim below is sourced from the ipa-dict README Credits (and, for
# en_UK, from the credited ipacards project's own CREDITS/`bin/`, which shell
# out to `espeak`).
_IPADICT_BASE = (
    "https://raw.githubusercontent.com/open-dict-data/ipa-dict/master/data/"
)

# orthography2ipa language tag → ipa-dict filename.
#
# Codes are mapped to the repo's registered specs (``available_codes()``);
# ipa-dict files with no corresponding spec, or whose orthography the spec
# cannot read, are NOT registered — see ``_IPADICT_UNWIRED`` for the list and
# the reason for each.
_IPADICT_FILES = {
    "ar": "ar.txt",
    "ko": "ko.txt",
    "de-DE": "de.txt",
    "en-GB": "en_UK.txt",
    "en-US": "en_US.txt",
    "eo": "eo.txt",
    "es-ES": "es_ES.txt",
    "es-MX": "es_MX.txt",
    "fa": "fa.txt",
    "fi": "fi.txt",
    "fr-FR": "fr_FR.txt",
    "is": "is.txt",
    "ja": "ja.txt",
    "jam": "jam.txt",
    "km": "km.txt",
    "ms": "ma.txt",          # ipa-dict `ma` = "Malay (Malaysian and Indonesian)"
    "nb": "nb.txt",
    "nl": "nl.txt",
    "or": "or.txt",
    "pt-BR": "pt_BR.txt",
    "ro-RO": "ro.txt",
    "sv": "sv.txt",
    "sw": "sw.txt",
    "vi": "vi_N.txt",        # Northern (Hanoi) = the standard the `vi` spec targets
}

# ipa-dict files deliberately NOT registered, with the reason. Kept as data so
# the gap is visible (and so a test can assert the two sets never overlap).
_IPADICT_UNWIRED: Dict[str, str] = {
    "fr_QC": "no Québécois French spec (`fr-QC`) is registered; the file is "
             "also qc-ipa script output over fr_FR ('highly experimental').",
    "tts": "Isan / Northeastern Thai (aakanee Isaan-English Dictionary). No "
           "`tts` spec is registered; the `th` (Thai) spec is a different "
           "language and must not be used as a stand-in.",
    "vi_C": "no Central-Vietnamese spec is registered (only `vi`).",
    "vi_S": "no Southern-Vietnamese spec is registered (only `vi`).",
    "yue": "UNTRANSCRIBABLE GOLD: the gold is Han script and the `yue` spec "
           "emits nothing for it (`G2P('yue')` returns '' for 水).",
    "zh_hans": "UNTRANSCRIBABLE GOLD: the gold is Han script. The `zh` spec is "
               "PINYIN/romanization (`OrthographyKind.ROMANIZATION`), so it "
               "cannot read it, and the Han-script `zh-Hani` spec emits nothing "
               "for Han characters (`G2P('zh-Hani')` returns '' for 一). "
               "Forcing either would measure nothing.",
    "zh_hant": "same as zh_hans (ipa-dict README: the codes differ only in "
               "written standard, not pronunciation) — untranscribable for the "
               "same reason.",
}

# PER-LANGUAGE provenance for ipa-dict, sourced from the README Credits.
# Overrides the dataset-wide fallback in ``PROVENANCE`` (see ``provenance_for``).
# A tier is never upgraded on a guess: where the Credits section names no
# source at all, the file is classified ``machine-generated`` and the note says
# the provenance is UNVERIFIED.
_IPADICT_PROVENANCE: Dict[str, str] = {
    # ─ human dictionaries / published lexicographic sources ─
    "is": "lexicon-derived",       # Hjal / "Pronunciation Dictionary for Icelandic" (malfong.is), CC BY 3.0
    "en-US": "lexicon-derived",    # cmudict-ipa (CMU hand-curated ARPABET) + syllabify stress, MIT
    "ja": "lexicon-derived",       # EDICT readings (EDRDG), CC BY-SA 3.0; only the kana entries are scorable (kanji entries transcribe to '' and drop out of `covered`)
    "jam": "lexicon-derived",      # "A Learner's Grammar of Jamaican" (Open Grammar Project), CC BY 4.0
    "km": "lexicon-derived",       # Khmer-English Dictionary (aakanee.com), CC BY-NC-SA 4.0
    "ro-RO": "lexicon-derived",    # MaRePhoR phonetic dictionary (UTCluj), CC BY-NC
    "sv": "lexicon-derived",       # Folkets lexikon (KTH), CC BY-SA 2.5
    # ─ Wiktionary community edits ─
    "ko": "crowd-scraped",         # Korean Wiktionary scrape (open-dict-data); Hangul readable since the conjoining-jamo graphemes landed
    "de-DE": "crowd-scraped",      # german-ipa-dict (@devio-at), built from Wiktionary, CC BY-SA
    # ─ tool output: a rule script / analyzer / phonemizer produced the IPA ─
    "ar": "machine-generated",     # Buckwalter Arabic Morphological Analyzer output
    "es-ES": "machine-generated",  # spanish-pronunciation-rules PHP script ("experimental")
    "es-MX": "machine-generated",  # same script; the file is near-identical to es_ES
    "fa": "machine-generated",     # Wiktionary + PersPred + "a great deal of guesswork"; README: "extremely experimental"
    "fi": "machine-generated",     # prosodic1b (rule-based) over the Kotus wordlist
    "nl": "machine-generated",     # INT: "automated conversion … no manual correction or revision"
    "or": "machine-generated",     # OdiaWikimedia Converter (IPA-Romanization) over Wikimedia dumps
    "vi": "machine-generated",     # vPhon converter over Ho Ngoc Duc's wordlist
    # ─ tool output, base source UNDOCUMENTED (never upgraded on a guess) ─
    "nb": "machine-generated",     # base generation method undocumented; expert-CORRECTED (Dr. E. Stranger-Johannessen) but not shown to be expert-authored
    "eo": "machine-generated",     # PROVENANCE UNVERIFIED: the Credits section names no source for Esperanto
    "fr-FR": "machine-generated",  # PROVENANCE UNVERIFIED: no source credited for French
    "ms": "machine-generated",     # PROVENANCE UNVERIFIED: no source credited for Malay
    "pt-BR": "machine-generated",  # PROVENANCE UNVERIFIED: no source credited for Brazilian Portuguese
    "sw": "machine-generated",     # PROVENANCE UNVERIFIED: no source credited for Swahili
    # ─ a COMPETITOR's output as the reference: cannot qualify OR block a language ─
    "en-GB": "espeak-derived",     # ipacards (@leoboiko): its CREDITS and bin/add-ipa-to-freq.py shell out to `espeak`
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


#: Arabic short-vowel / tanwīn / sukūn combining marks (harakat). Used to
#: strip word-FINAL case vowels (iʿrāb) from diacritized words — gold
#: pronunciations are pausal forms, which drop them.
_ARABIC_HARAKAT = "ًٌٍَُِْ"


def _strip_final_harakat(word: str) -> str:
    return word.rstrip(_ARABIC_HARAKAT)


def load_wikipron_ar_diacritized(lang: str, limit: int) -> List[Tuple[str, str]]:
    """The WikiPron Arabic gold with tashkeel RESTORED on the input side.

    0/3000 raw WikiPron Arabic words carry harakat, so the raw ``ar`` row
    scores the engine on unvocalized text it cannot vowelize — its PER is
    dominated by missing short vowels, not by rule errors. This row keeps
    the SAME gold IPA and diacritizes only the INPUT word with
    ``text2tashkeel`` (ONNX Arabic diacritizer, rawi default model,
    ~2% DER), then strips word-final harakat: the restored case endings
    (iʿrāb) are real, but WikiPron gold records pausal forms, which drop
    them. Diacritization is input NORMALIZATION and lives here in the
    harness — o2i itself does no normalization by design.

    ``text2tashkeel`` is an optional dependency: when it is not
    importable this loader raises and ``build_scoreboard`` catch-and-skips
    the row (the ``cmudict``/``scriptconv`` pattern). Results are cached
    to ``CACHE_DIR`` so scoreboard reruns are fast and deterministic for
    a given cache; delete the cache file to re-diacritize.
    """
    from text2tashkeel import Diacritizer  # optional; skip row if missing

    fname = "wikipron_ar_diacritized.tsv"
    dest = os.path.join(CACHE_DIR, fname)
    if not os.path.exists(dest):
        raw = load_wikipron(lang, sys.maxsize)
        dia = Diacritizer()
        rows = [(_strip_final_harakat(dia.diacritize(w)), ipa)
                for w, ipa in raw]
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(dest, "w", encoding="utf-8") as fh:
            fh.writelines(f"{w}\t{ipa}\n" for w, ipa in rows)
    pairs = []
    for line in open(dest, encoding="utf-8").read().strip().splitlines():
        parts = line.split("\t")
        if len(parts) == 2:
            pairs.append((parts[0], parts[1]))
        if len(pairs) >= limit:
            break
    return pairs


def load_mirandese(lang: str, limit: int) -> List[Tuple[str, str]]:
    """Mirandese HUMAN gold set (TigreGotico/mirandese_g2p on Hugging Face).

    218 ``dialect,word,ipa`` rows collected from native speakers of
    Mirandese (``mwl``) and its Sendinês/Raiano sub-dialects — the single
    most trustworthy signal for ``mwl`` in this scoreboard. Registered under
    the row id ``mirandese_g2p`` and classified ``expert-human`` (small-n,
    not externally peer-validated). Split by the ``dialect`` column per
    ``_MIRANDESE_DIALECTS``: central→``mwl``, sendinese→``mwl-x-sendim``,
    raiano→``mwl-x-ifanes``. Mirandese is Latin-script, so no special input
    contract applies. It is a SEPARATE source from any synthetic
    Mirandese IPA dictionary; see docs/benchmarks.md "Provenance".
    """
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


def load_barranquenho_dict(lang: str, limit: int) -> List[Tuple[str, str]]:
    """Barranquenho IPA dictionary (TigreGotico/barranquenho-ipa-dict-synthetic
    on Hugging Face) — 319 entries for the Barranquenho contact variety
    (``ext-PT-x-barrancos``), a Portuguese–Spanish border speech of Barrancos.

    PROVENANCE — this gold is **LLM-generated** (Claude, conditioned on the
    published *Convenção Ortográfica do Barranquenho* and descriptive research
    on the variety), NOT produced by a phonemizer, by orthography2ipa, or by
    any downstream o2i consumer — so scoring o2i against it is not circular.
    It is nonetheless machine-generated and unverified by human phoneticians:
    it is classified at the lowest reliability tier (``machine-generated``) and
    is directional only. See docs/benchmarks.md "Provenance and reliability".

    Each CSV row is ``barranquenho_orthography,ipa_transcription,part_of_speech,
    portuguese_equivalent,spanish_equivalent,phonological_notes``; only the
    first two columns are used. Barranquenho is Latin-script, so no special
    input contract applies. Malformed rows (missing orthography or IPA) are
    skipped.
    """
    del lang  # single language; kept for the uniform loader signature
    text = _fetch(_BARRANQUENHO_DICT_URL, "barranquenho_ipa_dict.csv")
    pairs: List[Tuple[str, str]] = []
    reader = csv.DictReader(text.splitlines())
    for row in reader:
        word = (row.get("barranquenho_orthography") or "").strip()
        ipa = (row.get("ipa_transcription") or "").strip()
        if not word or not ipa:
            continue
        pairs.append((word, ipa))
        if len(pairs) >= limit:
            break
    return pairs


def load_mirandese_dict(lang: str, limit: int) -> List[Tuple[str, str]]:
    """Mirandese IPA dictionary (TigreGotico/mirandese-ipa-dict-synthetic on
    Hugging Face) — 671 entries for Mirandese (``mwl``) and its sub-dialects,
    split by the dataset's ``dialect`` column (see ``_MIRANDESE_DICT_DIALECTS``
    for the value→tag mapping).

    PROVENANCE — this gold is **LLM-generated** (Claude, conditioned on the
    *Convenção Ortográfica da Língua Mirandesa* and descriptive research on the
    sub-dialects), NOT produced by a phonemizer, by orthography2ipa, or by any
    downstream o2i consumer — so scoring o2i against it is not circular. It is
    still machine-generated and unverified by human phoneticians: it is
    classified at the lowest reliability tier (``machine-generated``) and is
    directional only. It is a SEPARATE, complementary source from the existing
    ``mirandese`` gold (TigreGotico/mirandese_g2p, native-speaker collected).
    See docs/benchmarks.md "Provenance and reliability".

    Each CSV row is ``word,ipa,pos,english,portuguese,dialect,notes``; only
    ``word``, ``ipa`` and ``dialect`` are used. Mirandese is Latin-script, so
    no special input contract applies. Rows whose ``dialect`` value is not in
    the requested tag's set, or that are missing word/IPA, are skipped.
    """
    wanted = _MIRANDESE_DICT_DIALECTS[lang]
    text = _fetch(_MIRANDESE_DICT_URL, "mirandese_ipa_dict.csv")
    pairs: List[Tuple[str, str]] = []
    reader = csv.DictReader(text.splitlines())
    for row in reader:
        if (row.get("dialect") or "").strip() not in wanted:
            continue
        word = (row.get("word") or "").strip()
        ipa = (row.get("ipa") or "").strip()
        if not word or not ipa:
            continue
        pairs.append((word, ipa))
        if len(pairs) >= limit:
            break
    return pairs


def load_infopedia_pt(lang: str, limit: int) -> List[Tuple[str, str]]:
    """European Portuguese (``pt-PT``) IPA lexicon (TigreGotico/infopedia-pt-ipa
    on Hugging Face, 102,685 entries), extracted from a crawl of Infopédia
    (Porto Editora), a reputable published European-Portuguese dictionary.

    Each JSONL row is ``{"word", "ipa", "pronunciations", "syllabification"}``;
    ``pronunciations`` carries every distinct IPA form found for the word
    (a handful of entries have more than one), so all of them are emitted
    as separate reference pairs and scored via the harness's standard
    multi-reference-per-word handling.

    PROVENANCE — classified ``lexicon-derived``: a published dictionary, but
    the IPA transcriptions are Porto Editora's own and the METHODOLOGY BEHIND
    THEM IS UNDOCUMENTED/UNKNOWN (not stated to be hand-checked, nor which
    tooling produced them), so this is directional, not a peer-validated
    ground truth. See docs/benchmarks.md "Provenance and reliability".

    SAMPLING — 102k entries is far too many to score in full and the file is
    alphabetically ordered, so the first ``limit`` lines would be a biased
    all-"a…" slice. Instead the whole file is read and a fixed-seed
    (``SAMPLE_SEED``) random sample of up to ``limit`` WORDS is drawn (all of
    a sampled word's pronunciation variants are kept), giving an unbiased yet
    fully reproducible slice. Portuguese is Latin-script; no special contract.
    """
    del lang  # single language (pt-PT); kept for the uniform signature
    text = _fetch(_INFOPEDIA_PT_URL, "infopedia_pt_ipa.jsonl")
    words: List[Tuple[str, List[str]]] = []
    for line in text.strip().splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        word = row.get("word")
        variants = [v for v in (row.get("pronunciations") or [row.get("ipa")]) if v]
        if word and variants:
            words.append((word, variants))
    rng = random.Random(SAMPLE_SEED)
    rng.shuffle(words)
    pairs: List[Tuple[str, str]] = []
    for word, variants in words[:limit]:
        for ipa in variants:
            pairs.append((word, ipa))
    return pairs


def load_portuguese_phonetic_lexicon(lang: str, limit: int) -> List[Tuple[str, str]]:
    """Portuguese phonetic lexicon, ONE regional variant per language tag
    (TigreGotico/portuguese_phonetic_lexicon on Hugging Face, ~617k rows).

    Scraped from the public Portal da Língua Portuguesa (INESC-ID). This is a
    DIRECT stdlib CSV loader (columns ``word,phones,postag,region_code,…``);
    it lets the Lusophone family (``pt-PT``/``pt-BR``/``pt-AO``/``pt-MZ``/``pt-TL``)
    be scored with no extra package installed. See ``_PT_LEXICON_REGIONS`` for
    the spec→region_code mapping and the skipped register variants.

    PROVENANCE — classified ``crowd-scraped``: the Portal's IPA is
    SEMI-AUTOMATED (rule/tooling-generated, not hand-verified per entry), so
    it is directional only, never ground truth. See docs/benchmarks.md.

    The ``phones`` field flattens syllables with ``|`` (e.g. ``ˈkːa|zɐ``); the
    separator is stripped so the whole-word IPA is scored. Portuguese is
    Latin-script; no special input contract applies. The region's rows are read
    in full; when ``limit`` is set (ad-hoc runs and the CI sample) a fixed-seed
    (``SAMPLE_SEED``) random sample of up to ``limit`` words is drawn — unbiased
    but fully reproducible. Under the published ``--scoreboard`` run (``limit``
    unset) every row is scored. Duplicate words (same spelling) are
    de-duplicated, keeping the first pronunciation.
    """
    region = _PT_LEXICON_REGIONS[lang]
    text = _fetch(_PT_LEXICON_URL, "portuguese_phonetic_lexicon.csv")
    seen = set()
    candidates: List[Tuple[str, str]] = []
    reader = csv.DictReader(text.splitlines())
    for row in reader:
        if (row.get("region_code") or "").strip() != region:
            continue
        word = (row.get("word") or "").strip()
        ipa = (row.get("phones") or "").replace("|", "").strip()
        if not word or not ipa:
            continue
        key = word.lower()
        if key in seen:
            continue
        seen.add(key)
        candidates.append((word, ipa))
    rng = random.Random(SAMPLE_SEED)
    rng.shuffle(candidates)
    return candidates[:limit]


def load_4catac(lang: str, limit: int) -> List[Tuple[str, str]]:
    """4catac gold set (sentence-level, projecte-aina/4catac on Hugging
    Face): 160 Catalan sentences transcribed in IPA by expert annotators
    for four regional accents, one TSV per accent (``sentence`` TAB
    ``transcription``). See ``_4CATAC_FILES`` for the accent → language
    tag mapping.
    """
    fname = _4CATAC_FILES[lang]
    url = _4CATAC_BASE + urllib.parse.quote(fname)
    text = _fetch(url, f"4catac_{fname}")
    pairs = []
    for line in text.strip().splitlines()[1:]:
        parts = line.split("\t")
        if len(parts) == 2 and parts[0].strip() and parts[1].strip():
            pairs.append((parts[0].strip(), parts[1].strip()))
        if len(pairs) >= limit:
            break
    return pairs


def load_hitz_basque(lang: str, limit: int) -> List[Tuple[str, str]]:
    """HiTZ/wikipedia_basque_ipa: Basque Wikipedia paragraphs phonemized by
    ahoNT (a Basque text-processing/phonemization tool developed at HiTZ
    Zentroa / AhoLab, the University of the Basque Country's NLP research
    group), ~1.67M ``text``/``phonemes`` rows at PARAGRAPH level.

    This is a COMPLEMENTARY source to the existing ``wikipron`` "eu" entry,
    not a replacement: wikipron/eu is Wiktionary-sourced broad
    transcriptions, this is a much larger corpus phonemized by an
    automatic tool (ahoNT) rather than a human annotator. Per an explicit,
    dataset-specific decision, that is accepted here because the dataset
    is published by an academic/university NLP research center (HiTZ) --
    see docs/benchmarks.md for the full rationale; this is not a general
    exception to the "gold only from humans" rule.

    The dataset is paragraph-level, a different shape than this harness's
    word-level gold sets. Rows are paged through the Hugging Face
    datasets-server "rows" REST API (no full-parquet download, no
    ``datasets`` dependency needed); each paragraph's ``text`` and
    ``phonemes`` are whitespace-tokenized (ahoNT emits one phoneme token
    per source word with punctuation attached to the token, per the
    dataset card), tokens are paired positionally, and surrounding
    punctuation is stripped from both sides to yield single-word (word,
    IPA) pairs. The dataset's own apostrophe stress convention
    (``'a``/``'e``/... before the stressed vowel, per the dataset card)
    is normalized to the standard IPA stress mark (U+02C8) so the
    harness's default stress-stripping applies consistently across
    datasets. Following ``load_ep_dialects``'s precedent of scoring
    non-single-word/paragraph-derived gold spans through the same
    ``transcribe_word``/PER pipeline, single word-tokens (rather than
    whole sentences) are used as the scored unit here, since paragraph-
    level ahoNT stress placement is not verified to need sentence context,
    making the single-token span the safer/cleaner unit to isolate.

    This loader pages the datasets-server API and stops at
    ``_HITZ_BASQUE_MAX_PARAGRAPHS`` paragraphs -- an intrinsic bound that
    ``limit=None`` does NOT lift, so this is the one dataset the full-dataset
    scoreboard does not read end-to-end (never the full 1.67M-row set). The
    bound is disclosed in ``docs/benchmarks.md``.
    """
    import re

    # explicit punctuation set -- NOT a blanket \W match, since \W would
    # also swallow the dataset's apostrophe stress mark and IPA letters
    # that aren't ASCII word characters (ɾ, ʂ, ɲ, ...)
    _PUNCT = ".,;:!?¡¿\"“”«»()[]{}…—–-"
    punct_re = re.compile(
        r"^[" + re.escape(_PUNCT) + r"]+|[" + re.escape(_PUNCT) + r"]+$")
    pairs: List[Tuple[str, str]] = []
    seen = set()
    offset = 0
    paragraphs_seen = 0
    while len(pairs) < limit and paragraphs_seen < _HITZ_BASQUE_MAX_PARAGRAPHS:
        url = _HITZ_BASQUE_ROWS_URL.format(
            offset=offset, length=_HITZ_BASQUE_PAGE_SIZE)
        raw = _fetch(url, f"hitz_basque_rows_{offset}.json")
        data = json.loads(raw)
        rows = data.get("rows", [])
        if not rows:
            break
        for entry in rows:
            paragraphs_seen += 1
            row = entry.get("row", {})
            text, phonemes = row.get("text"), row.get("phonemes")
            if not text or not phonemes:
                continue
            words = text.split()
            phones = phonemes.split()
            if len(words) != len(phones):
                continue
            for w, p in zip(words, phones):
                word = punct_re.sub("", w)
                ipa = punct_re.sub("", p)
                # dataset-specific stress convention: apostrophe before the
                # stressed vowel (dataset card), not IPA's own U+02C8 mark
                # -- normalize so the harness's default stress-stripping
                # (which matches on U+02C8/U+02CC) also applies here.
                ipa = ipa.replace("'", "ˈ")
                if not word or not ipa or not word.isalpha():
                    continue
                key = word.lower()
                if key in seen:
                    continue
                seen.add(key)
                pairs.append((word, ipa))
                if len(pairs) >= limit:
                    break
            if len(pairs) >= limit:
                break
        offset += _HITZ_BASQUE_PAGE_SIZE
    return pairs


def load_clup_dialect(lang: str, limit: int) -> List[Tuple[str, str]]:
    """European Portuguese dialect archive gold set (sentence-level),
    TigreGotico/ArquivoDialetalCLUP_ipa on Hugging Face — IPA
    transcriptions of the Arquivo Dialetal do Centro de Linguística da
    Universidade do Porto (CLUP, https://cl.up.pt/arquivo/) interview
    corpus, spanning localities across mainland Portugal, the Azores
    and Madeira.

    Each CSV row is ``region,text,ipa`` where ``region`` is a
    ``"<locality>, <district>"`` label. Rows are grouped to an
    orthography2ipa dialect tag via ``_CLUP_LOCALITY_MAP`` (exact
    locality match) falling back to ``_CLUP_DISTRICT_MAP`` (district
    match); rows whose district has no corresponding spec are skipped.
    """
    text = _fetch(_CLUP_URL, "clup_dialect.csv")
    pairs = []
    reader = csv.reader(text.strip().splitlines())
    next(reader)  # skip header
    for row in reader:
        if len(row) != 3:
            continue
        region, sentence, ipa = row
        code = _CLUP_LOCALITY_MAP.get(region)
        if code is None:
            district = region.rsplit(",", 1)[-1].strip()
            code = _CLUP_DISTRICT_MAP.get(district)
        if code != lang or not sentence.strip() or not ipa.strip():
            continue
        pairs.append((sentence.strip(), ipa.strip()))
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


_IPADICT_VARIANT_RE = re.compile(r"/([^/]+)/")


def load_ipadict(lang: str, limit: int) -> List[Tuple[str, str]]:
    """ipa-dict pronunciation dictionaries (open-dict-data/ipa-dict).

    Provenance is **per-language**: the project mixes human dictionaries,
    Wiktionary scrapes and tool output in one repository, so every wired
    language carries its own tier in ``_IPADICT_PROVENANCE`` (surfaced per
    scoreboard row via :func:`provenance_for`) rather than inheriting a
    single dataset-wide tier. ``en-GB`` in particular is **espeak output**
    and can therefore neither qualify nor block a language
    (docs/quality_tiers.md). Consult the project README Credits section —
    never assume — before wiring another language.

    Each entry is ``word TAB /IPA/``. A word with several attested
    pronunciations lists them comma-separated (``est  /ɛst/, /ɛ/``); each
    variant is emitted as its own ``(word, ipa)`` pair, which is how the
    scorer consumes multiple valid golds per word (``evaluate_words``
    groups pairs by word and keeps the best-matching gold).

    ``limit`` caps the number of emitted pairs, matching every other loader.
    """
    fname = _IPADICT_FILES[lang]
    text = _fetch(_IPADICT_BASE + fname, f"ipadict_{fname}")
    pairs: List[Tuple[str, str]] = []
    for line in text.strip().splitlines():
        parts = line.split("\t")
        if len(parts) != 2:
            continue
        word = parts[0].strip().lower()
        if not word:
            continue
        variants = _IPADICT_VARIANT_RE.findall(parts[1])
        if not variants:  # tolerate an unslashed field
            variants = [parts[1].strip()]
        for variant in variants:
            ipa = variant.strip()
            if not ipa:
                continue
            pairs.append((word, ipa))
            if len(pairs) >= limit:
                return pairs
    return pairs



def load_styletts2_phonemes(lang: str, limit: int) -> List[Tuple[str, str]]:
    """StyleTTS2 community multilingual phonemes gold set (sentence-level,
    styletts2-community/multilingual-phonemes-10k-alpha on Hugging Face):
    ~10K ``text``/``phonemes`` sentence pairs per language, synthesized for
    TTS-phonemizer training/evaluation, one JSON file per language config.
    See ``_STYLETTS2_PHONEMES_FILES`` for the full set of wired languages.
    """
    fname = _STYLETTS2_PHONEMES_FILES[lang]
    text = _fetch(_STYLETTS2_PHONEMES_BASE + fname, f"styletts2_{fname}")
    data = json.loads(text)
    pairs = []
    for row in data:
        sentence = row.get("text")
        ipa = row.get("phonemes")
        if sentence and ipa:
            pairs.append((sentence.strip(), ipa.strip()))
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

    Source: TigreGotico internal EP-dialect annotation based on Cintra,
    L.F.L. (1971), "Nova
    proposta de classificação dos dialectos galego-portugueses", Boletim de
    Filologia 22:81–116.  250 sentences across seven EP regional varieties,
    manually annotated IPA, pending external peer-validation.

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
    "wikipron": (load_wikipron, sorted(_WIKIPRON_FILES)),
    "wikipron_ar_diacritized": (load_wikipron_ar_diacritized, ["ar"]),
    "mirandese_g2p": (load_mirandese, sorted(_MIRANDESE_DIALECTS)),
    "barranquenho_dict": (load_barranquenho_dict, ["ext-PT-x-barrancos"]),
    "mirandese_dict": (load_mirandese_dict, sorted(_MIRANDESE_DICT_DIALECTS)),
    "portuguese_phonetic_lexicon": (load_portuguese_phonetic_lexicon,
                                    sorted(_PT_LEXICON_REGIONS)),
    "infopedia_pt": (load_infopedia_pt, ["pt-PT"]),
    "4catac": (load_4catac, sorted(_4CATAC_FILES)),
    "hitz_basque_ipa": (load_hitz_basque, ["eu"]),
    "clup_dialect": (load_clup_dialect, _CLUP_LANGS),
    "cmudict": (load_cmudict, ["en-US"]),
    "ipadict": (load_ipadict, sorted(_IPADICT_FILES)),
    "styletts2_phonemes": (load_styletts2_phonemes,
                           sorted(_STYLETTS2_PHONEMES_FILES)),
    "ipa_childes": (load_ipa_childes, sorted(_IPA_CHILDES_FOLDERS)),
    "ipa_babylm": (load_ipa_babylm, ["en-US"]),
}


# ─── provenance / reliability tiers ─────────────────────────────────────────
#
# Reliable G2P "gold" barely exists. Almost every dataset wired here is
# semi-automated, dictionary-extracted, community-scraped, or a
# phonemizer's OWN output reused as a reference. A low PER against a
# machine-generated gold means "agrees with that tool", NOT "correct".
# Treat every scoreboard number as directional, never precise. The
# reliability tier below is surfaced per-row in docs/scoreboard.md and
# benchmarks/results.json so the caveat travels WITH the numbers.
#
# Tiers, most to least trustworthy (all still subject to notation
# conventions and small-n noise — see docs/benchmarks.md "Provenance and
# reliability"):
#
#   expert-human     — IPA curated by phoneticians, trained annotators, or
#                      native speakers. Still bound by the transcription
#                      conventions of the annotating team and, here, often
#                      small-n and/or not externally peer-validated.
#   lexicon-derived  — human lexicographers, but via a published
#                      dictionary's notation conventions and sometimes a
#                      mechanical notation transform (ARPABET→IPA,
#                      slashed-phonemic→IPA).
#   crowd-scraped    — Wiktionary community edits; uneven per language, and
#                      some entries are themselves editor-applied rule output
#                      rather than attested transcriptions.
#   machine-generated— some other tool's output used as the reference (a
#                      transliteration table, a research phonemizer we do not
#                      compete with). Scoring against it measures AGREEMENT
#                      WITH THAT TOOL, not correctness.
#
# A GOLD SET'S VALUE IS ITS ERROR MODEL. The three tiers below are ordered by
# how much a disagreement tells you:
#
#   espeak-derived   — the gold is espeak-ng's own output (directly, or via
#   epitran-derived    phonemizer/G2P+ which wrap it), or epitran's. Both are
#                      COMPETITORS we benchmark ourselves against
#                      (docs/comparison.md has espeak_per and epitran_per
#                      columns), so the row measures AGREEMENT WITH A
#                      COMPETITOR. It is still diagnostic — they are
#                      deterministic rule systems, so a disagreement can be
#                      traced to a rule and adjudicated against a cited source,
#                      and diverging from them may be exactly right. But it can
#                      never CERTIFY us: it can neither qualify a language for
#                      promotion nor block one (docs/quality_tiers.md).
#   llm-generated    — the gold was produced by a large language model. Worst
#                      of all: no lexicon, no G2P model, no rules — therefore
#                      NO ERROR MODEL. The output is plausible-looking IPA that
#                      can be confidently wrong with no systematic structure, so
#                      a disagreement is not even diagnostic: you cannot
#                      attribute it to anything. Certifies nothing, diagnoses
#                      nothing. Directional curiosity only; never gate on it.
RELIABILITY_TIERS = (
    "expert-human",
    "lexicon-derived",
    "crowd-scraped",
    "machine-generated",
    "espeak-derived",
    "epitran-derived",
    "llm-generated",
)

# Gold produced by a G2P system we ourselves benchmark AGAINST. The specific
# tool is recorded in the tier name (rather than one flat "competitor-derived"
# label) because the identity of the competitor is what a reader needs in order
# to interpret the row: an espeak-derived row on English and an epitran-derived
# row on Spanish are non-comparable evidence, and the circularity warning for
# each points at a different column of docs/comparison.md.
COMPETITOR_DERIVED_TIERS = frozenset({"espeak-derived", "epitran-derived"})

# Tiers that can never gate a quality decision: a competitor's output (measures
# agreement, not correctness) or an LLM's (no error model at all). A language
# whose only >=500-entry gold sits in one of these has NO usable gold and stays
# at `research`, and a poor score on one of these rows can equally never BLOCK a
# language that clears the bar on a trustworthy gold. See docs/quality_tiers.md.
NON_QUALIFYING_TIERS = COMPETITOR_DERIVED_TIERS | {"llm-generated"}


def can_gate_promotion(tier: str) -> bool:
    """Whether a scoreboard row on this tier may qualify (or block) a language
    for the `production` quality tier. False for competitor-derived and
    LLM-generated gold; see docs/quality_tiers.md."""
    if tier not in RELIABILITY_TIERS:
        raise ValueError(f"unknown reliability tier: {tier!r}")
    return tier not in NON_QUALIFYING_TIERS

# Every key in DATASETS MUST appear here (a test enforces it, so a new
# dataset cannot be registered without an explicit, evidence-based
# reliability classification). Classifications are justified per-dataset in
# docs/benchmarks.md "Provenance and reliability".
PROVENANCE: Dict[str, str] = {
    # phonetician / native-speaker / expert-annotator curated IPA
    "ep_dialects": "expert-human",       # TigreGotico team, manual, unvalidated, small-n
    "mirandese_g2p": "expert-human",     # TigreGotico/mirandese_g2p; native-speaker collected; small-n
    "4catac": "expert-human",            # expert annotators, IEC guidelines, consensus review
    "clup_dialect": "expert-human",      # U.Porto CLUP dialect archive; see note (IPA-column provenance undocumented, many rows n=1-17)
    # human lexicographers via dictionary notation conventions
    "infopedia_pt": "lexicon-derived",        # Infopédia (Porto Editora) dictionary extraction
    "cmudict": "lexicon-derived",             # CMU hand-curated ARPABET, mechanically mapped to IPA
    # ipa-dict is MIXED-PROVENANCE and is classified PER LANGUAGE in
    # PROVENANCE_BY_LANG below (human dictionaries, Wiktionary scrapes, rule
    # scripts, and — for en-GB — espeak output all live in the same project).
    # This dataset-wide value is only the fallback for a language with no
    # explicit classification, so it is the most pessimistic tier, never an
    # average: an unclassified ipa-dict file is not to be trusted. A test
    # forbids leaving a registered ipadict language unclassified.
    "ipadict": "machine-generated",
    # community-scraped Wiktionary
    "wikipron": "crowd-scraped",
    # SAME crowd-scraped WikiPron ar gold; only the INPUT word is
    # machine-diacritized (text2tashkeel, ~2% DER), which adds a small
    # machine noise floor on top of the gold's own tier. Diagnostic for
    # the vowelized-Arabic rules; certifies nothing beyond the raw row.
    "wikipron_ar_diacritized": "crowd-scraped",
    # Portal da Língua Portuguesa scrape; semi-automated IPA, not hand-verified
    "portuguese_phonetic_lexicon": "crowd-scraped",
    # A COMPETITOR'S OUTPUT reused as a reference. These phonemes come from the
    # espeak-ng-backed phonemizer, so this row measures AGREEMENT WITH ESPEAK,
    # not correctness — and espeak is a system we benchmark ourselves *against*
    # (docs/comparison.md). Diverging from it can mean we are right and it is
    # wrong, which would show here as a *worse* score. Quality also varies by
    # language. Never gate a quality decision on this row; judge any divergence
    # against a cited source instead. Kept because it is broad coverage and a
    # useful directional signal.
    "styletts2_phonemes": "espeak-derived",
    # IPA-BabyLM: G2P+ (github.com/codebyzeb/g2p-plus) with the `phonemizer`
    # backend, language en-us — i.e. espeak-ng output. Same circularity as
    # styletts2_phonemes; cannot qualify or block English.
    "ipa_babylm": "espeak-derived",
    # IPA-CHILDES is MIXED-PROVENANCE and is classified PER LANGUAGE in
    # PROVENANCE_BY_LANG below: its dataset card names a DIFFERENT phonemizing
    # tool per language (phonemizer/espeak for most, epitran for six,
    # pinyin_to_ipa for Mandarin). The dataset-wide value here is only the
    # fallback for an unclassified language and is deliberately pessimistic —
    # every classified language is either espeak- or epitran-derived, so an
    # unclassified one is assumed competitor-derived and cannot gate.
    "ipa_childes": "epitran-derived",
    "hitz_basque_ipa": "machine-generated",     # HiTZ ahoNT automatic phonemizer
    # LLM-generated (Claude, research-conditioned) IPA dictionaries. Not
    # circular (no G2P system produced them) but they have NO ERROR MODEL: an
    # LLM has no lexicon and no rules, so a disagreement cannot be attributed to
    # anything. Lowest tier; can never gate a promotion.
    "barranquenho_dict": "llm-generated",
    "mirandese_dict": "llm-generated",
}

# Per-LANGUAGE provenance overrides, for datasets that are not one source but a
# COLLECTION of independently-sourced files. A single dataset-wide tier lies
# about such a dataset: ipa-dict ships a human Icelandic dictionary, a
# Wiktionary-built German list, and espeak-generated British English side by
# side, and a row must carry the tier of the FILE it was scored against — a
# language cannot be promoted (or blocked) on a tier that belongs to somebody
# else's file. Keys are dataset names; values map language tag → tier.
PROVENANCE_BY_LANG: Dict[str, Dict[str, str]] = {
    "ipadict": _IPADICT_PROVENANCE,
    "ipa_childes": _IPA_CHILDES_PROVENANCE,
}


def provenance_for(dataset: str, lang: str) -> str:
    """Reliability tier of one scoreboard row.

    Returns the per-language tier when the dataset is mixed-provenance and
    the language is classified in ``PROVENANCE_BY_LANG``; otherwise the
    dataset-wide ``PROVENANCE`` tier. The fallback is deliberately the
    dataset's most pessimistic tier, so an unclassified language degrades
    to "distrust it" rather than silently inheriting a better one.
    """
    per_lang = PROVENANCE_BY_LANG.get(dataset)
    if per_lang and lang in per_lang:
        return per_lang[lang]
    return PROVENANCE[dataset]


# ─── metric ─────────────────────────────────────────────────────────────────

def normalize(ipa: str, strip_stress: bool, broad: bool) -> str:
    s = unicodedata.normalize("NFC", ipa)
    if strip_stress:
        for ch in _STRESS_MARKS:
            s = s.replace(ch, "")
    # Punctuation is not a phoneme. Sentence-level gold sets carry phrase
    # breaks and commas the engine never emits; counting them as segments
    # penalises a correct transcription for text it rightly ignored.
    for ch in _PUNCT_MARKS:
        s = s.replace(ch, "")
    for ch in _TIE_BARS:
        s = s.replace(ch, "")
    if broad:
        decomposed = unicodedata.normalize("NFD", s)
        s = unicodedata.normalize(
            "NFC", "".join(c for c in decomposed if c not in _NARROW_MARKS))
    # comparison is segmentation-free: some gold sets space-separate phonemes
    return "".join(s.split())


def _is_multiword(entry: str) -> bool:
    """True if *entry* is a phrase/sentence rather than a single word.

    Whitespace is the signal: a gold set is either word-level (WikiPron,
    CMUdict) or sentence-level (4catac, styletts2_phonemes), and the scorer
    must call the matching engine API for each.
    """
    return len(entry.split()) > 1


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


def align(a: str, b: str) -> List[Tuple[Optional[str], Optional[str]]]:
    """Character-level edit-distance alignment between ``a`` (e.g. gold)
    and ``b`` (e.g. hypothesis), with full backpointer traceback.

    Returns a list of ``(a_char_or_None, b_char_or_None)`` pairs in order:
    a substitution/match pair ``(ca, cb)``, an insertion (present only in
    ``b``) as ``(None, cb)``, or a deletion (present only in ``a``) as
    ``(ca, None)``. Dropping every ``None`` from each side of the returned
    pairs reconstructs ``a`` and ``b`` respectively. Uses the same edit
    costs as :func:`levenshtein` (unit cost per insertion/deletion/
    substitution) so alignments are consistent with the scored distance,
    but is not used by :func:`levenshtein` itself to keep that function's
    behavior byte-identical to its historical implementation.
    """
    n, m = len(a), len(b)
    # dp[i][j] = edit distance between a[:i] and b[:j]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        ca = a[i - 1]
        for j in range(1, m + 1):
            cb = b[j - 1]
            cost = 0 if ca == cb else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,       # deletion (a char unmatched)
                dp[i][j - 1] + 1,       # insertion (b char unmatched)
                dp[i - 1][j - 1] + cost,  # match/substitution
            )

    # traceback from (n, m) to (0, 0), preferring match/substitution ties
    pairs: List[Tuple[Optional[str], Optional[str]]] = []
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            ca, cb = a[i - 1], b[j - 1]
            cost = 0 if ca == cb else 1
            if dp[i][j] == dp[i - 1][j - 1] + cost:
                pairs.append((ca, cb))
                i, j = i - 1, j - 1
                continue
        if i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            pairs.append((a[i - 1], None))
            i -= 1
            continue
        if j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            pairs.append((None, b[j - 1]))
            j -= 1
            continue
        # unreachable for a well-formed dp table
        break
    pairs.reverse()
    return pairs


def evaluate_words(pairs, lang: str, strip_stress: bool, broad: bool):
    """Like :func:`evaluate` but also returns the per-word PER list, so
    callers (e.g. :func:`bootstrap_per_ci`) can resample it. The point
    estimates returned here (``n``, ``covered``, ``per``, ``wer``) are
    computed the exact same way as :func:`evaluate` — byte-identical
    scoreboard numbers.
    """
    from orthography2ipa import G2P

    engine = G2P(lang)
    # gold sets may carry several valid transcriptions per word
    # (dialect variants); score against all, keep the best
    refs: Dict[str, List[str]] = {}
    for word, gold in pairs:
        refs.setdefault(word, []).append(gold)

    pers: List[float] = []
    wrong, covered = 0, 0
    for word, golds in refs.items():
        try:
            # Pick the API that matches the entry's granularity. Several gold
            # sets are sentence-level (4catac, styletts2_phonemes), and
            # transcribe_word() treats a whole sentence as ONE word: word
            # boundaries vanish, per-word stress collapses to a single mark,
            # and word-final rules (Catalan final-⟨r⟩ deletion, Danish schwa)
            # never fire. That is a harness artifact, not an engine error —
            # it cost Catalan ~7 and English ~16 PER points.
            transcribe = (engine.transcribe if _is_multiword(word)
                          else engine.transcribe_word)
            hyp = normalize(transcribe(word), strip_stress, broad)
        except Exception:
            continue
        if not hyp:
            continue
        covered += 1
        per = min(
            levenshtein(hyp, g) / max(len(g), 1)
            for g in (normalize(x, strip_stress, broad) for x in golds)
        )
        pers.append(per)
        wrong += per > 0
    n = len(refs)
    per_sum = sum(pers)
    return n, covered, pers, (per_sum / covered if covered else 1.0), \
        (wrong / covered if covered else 1.0)


def evaluate(pairs, lang: str, strip_stress: bool, broad: bool):
    n, covered, _pers, per, wer = evaluate_words(
        pairs, lang, strip_stress, broad)
    return n, covered, per, wer


def bootstrap_per_ci(
    pers: List[float],
    reps: int = BOOTSTRAP_REPS,
    seed: int = BOOTSTRAP_SEED,
) -> Tuple[float, float]:
    """95% bootstrap confidence interval for the mean PER.

    Resamples ``pers`` (the per-word PER list) with replacement ``reps``
    times using a fixed-seed ``random.Random`` (never the global RNG),
    computes the mean of each resample, and returns the 2.5th/97.5th
    percentiles of the resulting distribution. Deterministic across runs
    given the same input list, seed and rep count. Returns ``(0.0, 0.0)``
    for an empty input (nothing to resample).
    """
    n = len(pers)
    if n == 0:
        return (0.0, 0.0)
    rng = random.Random(seed)
    means: List[float] = []
    for _ in range(reps):
        sample = [pers[rng.randrange(n)] for _ in range(n)]
        means.append(sum(sample) / n)
    means.sort()

    def _percentile(p: float) -> float:
        idx = p * (len(means) - 1)
        lo = int(idx)
        hi = min(lo + 1, len(means) - 1)
        frac = idx - lo
        return means[lo] + (means[hi] - means[lo]) * frac

    return (_percentile(0.025), _percentile(0.975))


def _quality_tier(lang: str) -> Optional[str]:
    """Look up the spec quality tier for a language tag, if the tag has
    a registered spec. Returns ``None`` when no spec resolves (e.g. a
    dataset dialect key that isn't itself a registered language code)."""
    from orthography2ipa import get

    try:
        return get(lang).quality.value
    except Exception:
        return None


def build_scoreboard(limit: Optional[int]) -> List[dict]:
    """Run every registered gold dataset/language combination and
    return deterministic scoreboard rows sorted by language tag.

    ``limit`` is the per-dataset row cap. Pass ``None`` (the default for
    the committed ``--scoreboard`` run) to score the ENTIRE gold set of
    every language with no truncation — the published scoreboard is
    full-dataset. A concrete integer is only for ad-hoc fast runs and for
    the CI regression sample (see ``check_benchmark_regression.py``); it
    is applied UNIFORMLY to every language (no per-language cap juggling).
    ``None`` is passed to the loaders as ``sys.maxsize`` so their
    ``len(pairs) >= limit`` / ``pairs[:limit]`` guards become no-ops.
    """
    effective = sys.maxsize if limit is None else limit
    rows: List[dict] = []
    for dataset_name, (loader, langs) in DATASETS.items():
        for lang in langs:
            try:
                pairs = loader(lang, effective)
            except Exception as exc:
                print(f"skip {dataset_name} lang={lang}: {exc}",
                      file=sys.stderr)
                continue
            n, covered, pers, per, wer = evaluate_words(
                pairs, lang, strip_stress=True, broad=True,
            )
            ci_low, ci_high = bootstrap_per_ci(pers)
            rows.append({
                "lang": lang,
                "dataset": dataset_name,
                "n": covered,
                "per": round(per, 4),
                "per_ci_low": round(ci_low, 4),
                "per_ci_high": round(ci_high, 4),
                "exact_match": round(1.0 - wer, 4),
                "quality_tier": _quality_tier(lang),
                "provenance": provenance_for(dataset_name, lang),
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
        "**Grain of salt — read this first.** Reliable G2P \"gold\" barely "
        "exists. Most datasets below are semi-automated, dictionary-extracted, "
        "community-scraped, or a phonemizer's OWN output reused as a reference. "
        "A low PER against a `machine-generated` gold means \"agrees with that "
        "tool\", NOT \"correct\". Absolute PER is noisy — read every number as "
        "**directional/relative**, and cross-reference the `95% CI` (a wide or "
        "degenerate interval, common on small-`N` rows, means the row cannot "
        "support a conclusion). Full per-dataset classification and the honest "
        "caveats: [`docs/benchmarks.md`](benchmarks.md) "
        "(\"Provenance and reliability\").",
        "",
        "`Provenance` legend (most → least trustworthy, all still subject to "
        "notation conventions and small-`N` noise): "
        "**expert-human** (phonetician / native-speaker / expert-annotator) > "
        "**lexicon-derived** (dictionary, human lexicographers) > "
        "**crowd-scraped** (Wiktionary) > "
        "**machine-generated** (some other tool's output; agreement-with-tool, "
        "not correctness) > "
        "**espeak-derived** / **epitran-derived** (a COMPETITOR's output: "
        "measures agreement with a system we benchmark ourselves against, so it "
        "can neither qualify a language for `production` nor block one) > "
        "**llm-generated** (an LLM's output: no lexicon, no rules, therefore no "
        "error model — a disagreement is not even diagnostic; never gate on "
        "it).",
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
        "The `95% CI` column is a bootstrap confidence interval on the "
        "mean PER (per-word PERs resampled with replacement, "
        f"{BOOTSTRAP_REPS} reps, fixed seed {BOOTSTRAP_SEED}) — see "
        "[`docs/benchmarks.md`](benchmarks.md).",
        "",
        "| Lang | Dataset | N | PER | 95% CI | Exact match | Quality tier "
        "| Provenance |",
        "|---|---|---:|---:|---:|---:|---|---|",
    ]
    for row in rows:
        tier = row["quality_tier"] or "-"
        prov = row.get("provenance") or "-"
        ci = f"[{row['per_ci_low']:.4f}, {row['per_ci_high']:.4f}]"
        lines.append(
            f"| {row['lang']} | {row['dataset']} | {row['n']} | "
            f"{row['per']:.4f} | {ci} | {row['exact_match']:.4f} | {tier} "
            f"| {prov} |"
        )
    lines.append("")
    os.makedirs(os.path.dirname(SCOREBOARD_MD), exist_ok=True)
    with open(SCOREBOARD_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


# ─── lexicon-overlay report (E3) ────────────────────────────────────────────
#
# The lexicon overlay (orthography2ipa/lexicon.py) is only honest if we can see
# how much of a language's accuracy comes from the *rules* versus the shipped
# sidecar TSV. This report re-scores the same gold twice — once with the
# lexicon disabled ("rules-only PER") and once with it on ("with-lexicon PER")
# — for every language that ships a data/lexicons/{code}.tsv, so a regression
# in rule quality can't hide behind lexicon coverage. It is a SEPARATE artifact
# from the main scoreboard (docs/scoreboard.md is left untouched): languages
# with no lexicon are byte-identical with or without this feature.

# wikipron gold tags to score per lexicon code (a lexicon file is named by the
# resolved spec code; several BCP-47 tags can resolve to it and have their own
# gold — e.g. both "en" (US) and "en-GB" (UK) resolve to the en-GB spec).
_LEXICON_REPORT_TAGS: Dict[str, List[str]] = {
    "en-GB": ["en", "en-GB"],
}


@contextlib.contextmanager
def _lexicon_disabled():
    """Temporarily force every G2P engine onto the rules-only path.

    Swaps ``get_lexicon`` (bound both in ``orthography2ipa.lexicon`` and, by
    ``from``-import, in ``orthography2ipa.g2p``) for a stub returning ``{}``,
    so ``_override_for`` sees no sidecar and falls straight to the beam. The
    inline ``word_exceptions`` path is untouched — this isolates the lexicon's
    contribution, not the whole override mechanism.
    """
    from orthography2ipa import lexicon as _lex
    from orthography2ipa import g2p as _g2p

    orig = _lex.get_lexicon
    stub = lambda code: {}  # noqa: E731 — trivial, local
    _lex.get_lexicon = stub
    _g2p.get_lexicon = stub
    try:
        yield
    finally:
        _lex.get_lexicon = orig
        _g2p.get_lexicon = orig


def _score_pairs(pairs, lang: str) -> Tuple[int, float]:
    n, covered, _pers, per, _wer = evaluate_words(
        pairs, lang, strip_stress=True, broad=True)
    return covered, per


def build_lexicon_report(limit: Optional[int]) -> List[dict]:
    """Rules-only vs with-lexicon PER for every shipped lexicon language.

    For each ``data/lexicons/{code}.tsv`` and each wikipron gold tag that
    resolves to it, reports PER on the full ``limit`` slice AND on just the
    subset of gold words the lexicon actually covers (where the overlay can
    possibly act) — the covered-subset delta is the honest measure of the
    lexicon's own accuracy versus the rules on the same words.
    """
    from orthography2ipa import lexicon as _lex

    rows: List[dict] = []
    for code in _lex.available_lexicon_codes():
        lex = _lex.get_lexicon(code)
        for tag in _LEXICON_REPORT_TAGS.get(code, [code]):
            if tag not in _WIKIPRON_FILES:
                continue
            try:
                pairs = load_wikipron(
                    tag, sys.maxsize if limit is None else limit)
            except Exception as exc:
                print(f"skip lexicon report {tag}: {exc}", file=sys.stderr)
                continue
            covered_pairs = [(w, g) for (w, g) in pairs if w.lower() in lex]

            with _lexicon_disabled():
                full_n, full_rules = _score_pairs(pairs, tag)
                sub_n, sub_rules = _score_pairs(covered_pairs, tag)
            full_cov, full_lex = _score_pairs(pairs, tag)
            sub_cov, sub_lex = _score_pairs(covered_pairs, tag)

            rows.append({
                "lexicon": code,
                "lang": tag,
                "gold": "wikipron",
                "lexicon_entries": len(lex),
                "n_full": full_cov,
                "per_rules_only_full": round(full_rules, 4),
                "per_with_lexicon_full": round(full_lex, 4),
                "n_covered": sub_cov,
                "per_rules_only_covered": round(sub_rules, 4),
                "per_with_lexicon_covered": round(sub_lex, 4),
                "limit": limit,
                "harness_version": HARNESS_VERSION,
            })
    rows.sort(key=lambda r: (r["lexicon"], r["lang"]))
    return rows


def write_lexicon_report(rows: List[dict]) -> None:
    os.makedirs(os.path.dirname(LEXICON_SCOREBOARD_JSON), exist_ok=True)
    with open(LEXICON_SCOREBOARD_JSON, "w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    lines = [
        "# Lexicon-overlay scoreboard",
        "",
        "Rules-only vs with-lexicon PER for every language that ships an "
        "optional sidecar lexicon (`orthography2ipa/data/lexicons/{code}.tsv` "
        "— see [`docs/data_model.md`](data_model.md) and "
        "[`orthography2ipa/lexicon.py`]). This keeps rule quality honest: the "
        "overlay must *improve* PER without letting the underlying grapheme "
        "rules rot behind lexicon coverage. Same gold, scored twice — once "
        "with `get_lexicon` stubbed to `{}` (rules-only) and once with the "
        "sidecar active. Regenerate with:",
        "",
        "```bash",
        "PYTHONPATH=$PWD python scripts/benchmark.py --lexicon-report",
        "```",
        "",
        "`PER (covered)` columns restrict scoring to the gold words the "
        "lexicon actually contains — where the overlay can act — so the "
        "covered-subset delta is the lexicon's own accuracy vs the rules on "
        "the *same* words. The `full` columns dilute that by every gold word "
        "outside the (deliberately capped, top-frequency) pilot lexicon; a "
        "full production lexicon belongs downstream (see "
        "[`docs/adding_a_language.md`](adding_a_language.md)).",
        "",
        "| Lexicon | Lang | Gold | Entries | N (full) | PER rules-only (full) "
        "| PER +lexicon (full) | N (covered) | PER rules-only (covered) "
        "| PER +lexicon (covered) |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for r in rows:
        lines.append(
            f"| {r['lexicon']} | {r['lang']} | {r['gold']} | "
            f"{r['lexicon_entries']} | {r['n_full']} | "
            f"{r['per_rules_only_full']:.4f} | {r['per_with_lexicon_full']:.4f} "
            f"| {r['n_covered']} | {r['per_rules_only_covered']:.4f} | "
            f"{r['per_with_lexicon_covered']:.4f} |"
        )
    lines.append("")
    os.makedirs(os.path.dirname(LEXICON_SCOREBOARD_MD), exist_ok=True)
    with open(LEXICON_SCOREBOARD_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dataset", choices=sorted(DATASETS))
    ap.add_argument("--lang", default=None)
    ap.add_argument("--limit", type=int, default=None,
                    help="Per-dataset row cap, applied UNIFORMLY to every "
                         "language. Omit to score the FULL gold set (the "
                         "committed --scoreboard is full-dataset); pass an "
                         "integer only for ad-hoc fast runs.")
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
    ap.add_argument("--ci-sample", action="store_true",
                    help="Write the CI regression baseline "
                         "benchmarks/results_ci_sample.json — every dataset/"
                         "language scored at the fixed uniform "
                         f"--limit {CI_SAMPLE_LIMIT} sample used by "
                         "check_benchmark_regression.py (NOT the full "
                         "published scoreboard).")
    ap.add_argument("--lexicon-report", action="store_true",
                    help="Score rules-only vs with-lexicon PER for every "
                         "language shipping a data/lexicons/{code}.tsv and "
                         "write docs/lexicon_scoreboard.md + "
                         "benchmarks/lexicon_results.json")
    args = ap.parse_args()

    if args.lexicon_report:
        rows = build_lexicon_report(args.limit)
        write_lexicon_report(rows)
        print(f"wrote {len(rows)} rows to "
              f"{os.path.relpath(LEXICON_SCOREBOARD_MD, REPO_ROOT)} and "
              f"{os.path.relpath(LEXICON_SCOREBOARD_JSON, REPO_ROOT)}")
        return

    if args.ci_sample:
        rows = build_scoreboard(CI_SAMPLE_LIMIT)
        os.makedirs(os.path.dirname(CI_SAMPLE_JSON), exist_ok=True)
        with open(CI_SAMPLE_JSON, "w", encoding="utf-8") as fh:
            json.dump(rows, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"wrote {len(rows)} rows to "
              f"{os.path.relpath(CI_SAMPLE_JSON, REPO_ROOT)} "
              f"(CI regression sample, uniform limit={CI_SAMPLE_LIMIT})")
        return

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

    pairs = loader(lang, sys.maxsize if args.limit is None else args.limit)
    n, covered, per, wer = evaluate(
        pairs, lang,
        strip_stress=not args.keep_stress,
        broad=not args.narrow,
    )
    print(f"{args.dataset} lang={lang} n={n} covered={covered} "
          f"PER={per:.4f} WER={wer:.4f}")


if __name__ == "__main__":
    main()
