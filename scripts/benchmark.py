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
- ``infopedia_pt`` downloads a JSONL gold file directly (stdlib only).
- ``hitz_basque_ipa`` pages the HiTZ/wikipedia_basque_ipa Hugging Face
  dataset through the datasets-server "rows" REST API (stdlib only,
  no full-parquet download).
- ``clup_dialect`` downloads a CSV gold file directly (stdlib only).
- ``styletts2_phonemes`` downloads per-language JSON files directly
  (stdlib only).
- ``ipa_childes`` downloads per-language CSVs from the
  fdemelo/ipa-childes-split Hugging Face dataset directly (stdlib only).

Every run is capped (``--limit``, default 300) — gold sets are large
and a slice is enough for a stable reference number.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import random
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
SCOREBOARD_MD = os.path.join(REPO_ROOT, "docs", "scoreboard.md")
SCOREBOARD_JSON = os.path.join(REPO_ROOT, "benchmarks", "results.json")

_STRESS_MARKS = "ˈˌ"
_NARROW_MARKS = "̝̞̪̺̼̘̙͜͡.·‿()"

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
_MIRANDESE_DIALECTS = {"mwl": "central", "mwl-x-sendim": "sendinese"}
_INFOPEDIA_PT_URL = (
    "https://huggingface.co/datasets/TigreGotico/infopedia-pt-ipa"
    "/resolve/main/infopedia_pt_ipa.jsonl"
)
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
# - ko-KR: this repo's ko spec's grapheme table is keyed on individual
#   compatibility jamo (e.g. U+3131 "ㄱ"), while real Korean text --
#   including this dataset's -- is precomposed Hangul syllable blocks
#   (e.g. "아홉"), which neither match the compatibility-jamo graphemes
#   directly nor decompose into them under NFD (NFD splits a Hangul
#   syllable into *conjoining* jamo, U+11xx, a different Unicode block
#   from the *compatibility* jamo, U+31xx, the spec's grapheme table
#   uses). G2P('ko').transcribe_word(...) returns an empty string for
#   every real Hangul word, so scoring this row would not measure
#   phonological accuracy.
# - qu-PE, yue-CN: no corresponding spec exists in this repo at all.
_IPA_CHILDES_FOLDERS: Dict[str, str] = {
    "en-US": "en-US",
    "et": "et-EE",
    "hu": "hu-HU",
    "id": "id-ID",
    "sr": "sr-RS",
    "zh": "zh-CN",
}
_IPA_CHILDES_STEM_COLUMN = {"zh"}


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
    model), and only a bounded ``limit``-sized prefix of each (typically
    tens-of-thousands-of-rows) CSV is read.
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


def load_infopedia_pt(lang: str, limit: int) -> List[Tuple[str, str]]:
    """European Portuguese IPA lexicon (TigreGotico/infopedia-pt-ipa on
    Hugging Face), extracted from Infopédia (Porto Editora).

    Each JSONL row is ``{"word", "ipa", "pronunciations", "syllabification"}``;
    ``pronunciations`` carries every distinct IPA form found for the word
    (a handful of entries have more than one), so all of them are emitted
    as separate reference pairs and scored via the harness's standard
    multi-reference-per-word handling.
    """
    text = _fetch(_INFOPEDIA_PT_URL, "infopedia_pt_ipa.jsonl")
    pairs = []
    for line in text.strip().splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        word = row.get("word")
        variants = row.get("pronunciations") or [row.get("ipa")]
        for ipa in variants:
            if word and ipa:
                pairs.append((word, ipa))
        if len(pairs) >= limit:
            break
    return pairs


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

    Only a bounded sample (default ``limit`` pairs, e.g. ~300) is ever
    fetched, paging a few hundred paragraphs at a time -- never the full
    1.67M-row dataset.
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
    "portuguese_lexicon": (load_portuguese_lexicon,
                           ["pt-PT", "pt-BR", "pt-AO", "pt-MZ", "pt-TL"]),
    "wikipron": (load_wikipron, sorted(_WIKIPRON_FILES)),
    "mirandese": (load_mirandese, sorted(_MIRANDESE_DIALECTS)),
    "infopedia_pt": (load_infopedia_pt, ["pt-PT"]),
    "4catac": (load_4catac, sorted(_4CATAC_FILES)),
    "hitz_basque_ipa": (load_hitz_basque, ["eu"]),
    "clup_dialect": (load_clup_dialect, _CLUP_LANGS),
    "cmudict": (load_cmudict, ["en-US"]),
    "ipadict": (load_ipadict, sorted(_IPADICT_FILES)),
    "styletts2_phonemes": (load_styletts2_phonemes,
                           sorted(_STYLETTS2_PHONEMES_FILES)),
    "ipa_childes": (load_ipa_childes, sorted(_IPA_CHILDES_FOLDERS)),
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
#   machine-generated— a phonemizer's own output used as the reference (the
#                      biggest grain of salt). Scoring against it measures
#                      AGREEMENT WITH THAT TOOL, not correctness; comparing
#                      o2i to espeak on an espeak-derived gold is partly
#                      circular.
RELIABILITY_TIERS = (
    "expert-human",
    "lexicon-derived",
    "crowd-scraped",
    "machine-generated",
)

# Every key in DATASETS MUST appear here (a test enforces it, so a new
# dataset cannot be registered without an explicit, evidence-based
# reliability classification). Classifications are justified per-dataset in
# docs/benchmarks.md "Provenance and reliability".
PROVENANCE: Dict[str, str] = {
    # phonetician / native-speaker / expert-annotator curated IPA
    "ep_dialects": "expert-human",       # TigreGotico team, manual, unvalidated, small-n
    "mirandese": "expert-human",         # native-speaker collected; small-n
    "4catac": "expert-human",            # expert annotators, IEC guidelines, consensus review
    "clup_dialect": "expert-human",      # U.Porto CLUP dialect archive; see note (IPA-column provenance undocumented, many rows n=1-17)
    # human lexicographers via dictionary notation conventions
    "portuguese_lexicon": "lexicon-derived",  # Portal da Língua Portuguesa (tugalex)
    "infopedia_pt": "lexicon-derived",        # Infopédia (Porto Editora) dictionary extraction
    "cmudict": "lexicon-derived",             # CMU hand-curated ARPABET, mechanically mapped to IPA
    "ipadict": "lexicon-derived",             # only human `is` (Hjal/malfong) wired; project is mixed-provenance
    # community-scraped Wiktionary
    "wikipron": "crowd-scraped",
    # a phonemizer's own output reused as a reference — biggest grain of salt
    "styletts2_phonemes": "machine-generated",  # phonemizer/espeak-derived TTS phonemes (partly circular vs espeak)
    "ipa_childes": "machine-generated",         # CHILDES "G2P+" automatic phonemizer column
    "hitz_basque_ipa": "machine-generated",     # HiTZ ahoNT automatic phonemizer
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
                "provenance": PROVENANCE[dataset_name],
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
        "**machine-generated** (a phonemizer's own output — biggest grain of "
        "salt; agreement-with-tool, not correctness).",
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
