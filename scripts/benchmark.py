#!/usr/bin/env python3
"""Benchmark the orthography2ipa G2P engine against gold pronunciation sets.

Self-contained evaluation harness for this library: it loads a gold
dataset, transcribes every word with :class:`orthography2ipa.G2P`, and
reports PER (phoneme error rate) and WER (word error rate). The
datasets, their sources and the methodology are documented in
``docs/benchmarks.md``.

Usage::

    python scripts/benchmark.py --dataset portuguese_unified --lang pt-PT
    python scripts/benchmark.py --dataset wikipron --lang gl --broad
    python scripts/benchmark.py --dataset mirandese_g2p --lang mwl
    python scripts/benchmark.py --list

Dataset access:

- ``cmudict`` needs the ``scriptconv`` package for ARPABET→IPA.
- ``wikipron`` and ``mirandese_g2p`` download TSVs directly (stdlib only).
- ``portuguese_unified`` downloads a JSONL gold file directly and samples it with
  a fixed seed (stdlib only).
  (It merges the former separate infopedia / wiktionary / Portal-lexicon
  golds; one region is scored per registered language tag.)
- ``hitz_basque_ipa`` pages the HiTZ/wikipedia_basque_ipa Hugging Face
  dataset through the datasets-server "rows" REST API (stdlib only,
  no full-parquet download).
- ``clup_dialect`` downloads a CSV gold file directly (stdlib only).
  (stdlib only).
- ``ipa_childes`` downloads per-language CSVs from the
  fdemelo/ipa-childes-split Hugging Face dataset directly (stdlib only).
- ``ipa_babylm`` downloads the dev-split CSVs of the
  phonemetransformers/IPA-BabyLM Hugging Face dataset directly (stdlib only).
- ``northeuralex`` and ``wold`` download ``cldf/forms.csv`` directly from the
  lexibank/northeuralex and lexibank/wold GitHub repositories (stdlib only).
- ``kaikki`` downloads per-language Wiktextract JSON-lines dumps directly
  from kaikki.org (stdlib only).

The scoreboard also reports **oracle PER@k** — the per-word minimum PER
over the engine's top-k readings — which splits ranking error (right
answer in the beam, ranked wrong) from model error (right answer absent
at any k). It is a lattice-quality diagnostic for THIS engine only and
is never valid input to a cross-system comparison: see
:class:`OracleResult` and ``docs/benchmarks.md``.

The committed ``--scoreboard`` scores the FULL gold set of every language
with NO cap (uniformly — no per-language limit juggling); the published
docs/scoreboard.md is full-dataset. ``--limit N`` still applies a uniform
cap for ad-hoc fast runs, and the CI regression gate re-scores at a fixed
uniform sample (see ``--ci-sample`` and check_benchmark_regression.py). A
few loaders keep an intrinsic, language-agnostic infrastructure bound that
``--limit`` cannot lift (e.g. ``hitz_basque_ipa`` pages the HF rows API and
stops at ``_HITZ_BASQUE_MAX_PARAGRAPHS`` rather than pulling the full
1.67M-row set) — these are documented in docs/benchmarks.md.

Where things live
-----------------

The module reads top to bottom as fetch -> load -> provenance -> score ->
render. Each section carries a ``# ─── name ───`` header:

``dataset loaders``
    One ``load_<name>(lang, limit) -> [GoldPair, ...]`` per gold source.
    Uniform signature on purpose: that is what lets :data:`DATASETS`
    register them all interchangeably. Each loader's docstring records
    where its IPA came from — that provenance is the reason to trust or
    distrust every number derived from it, so it belongs with the loader.
``DATASETS``
    The registry. Adding a gold set = write a loader + add one entry here
    + record its :data:`PROVENANCE` tier. Nothing else needs to change.
``provenance / reliability tiers``
    :data:`RELIABILITY_TIERS`, :data:`PROVENANCE`, and
    :func:`can_gate_promotion` — which golds are trustworthy enough to FAIL
    a build on, and which may only report drift. A gold that is another
    tool's output can never gate.
``metric``
    :func:`normalize` (the one comparison space every system is scored in),
    :func:`levenshtein`, :func:`align`, and the :func:`evaluate` family.
    ``compare_systems.py`` imports these so its numbers are directly
    comparable to the scoreboard's.
``build_scoreboard`` / ``write_scoreboard``
    Sweep every registered dataset/language, then render
    docs/scoreboard.md + benchmarks/results.json.
``lexicon-overlay report``
    The separate rules-only-vs-with-lexicon board (``--lexicon-report``);
    it writes its own docs page and never touches the main scoreboard.
"""
from __future__ import annotations

import argparse
import contextlib
import csv
import glob
import json
import os
import random
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from typing import (Callable, Dict, Iterator, List, Optional, Sequence,
                    Tuple)

#: A gold entry: (orthographic word or sentence, reference IPA). Every
#: ``load_*`` dataset loader returns a list of these, and every scoring
#: function consumes them — the one shape the whole harness is built on.
GoldPair = Tuple[str, str]

# the repository root precedes the installed package so that running the
# script from a checkout measures THAT checkout
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from orthography2ipa.vowels import is_ipa_vowel  # noqa: E402

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CACHE_DIR = os.path.join(os.path.dirname(__file__), "..", ".benchmark_cache")

HARNESS_VERSION = "1.1"

# Fixed seed for the bootstrap confidence-interval resampling below --
# never randomized, so the same per-word PER list always yields the same
# CI bounds across runs/machines.
BOOTSTRAP_SEED = 20260710
BOOTSTRAP_REPS = 1000

# Fixed seed for loaders that draw a random sample from a large gold file
# (portuguese_unified) instead of the alphabetical
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
# CI job (the 598k-row portuguese_unified gold alone takes the better part
# of an hour). So the CI regression gate re-scores
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
#: is a real segment. The Scandinavian pitch-accent digits ¹/² are stripped
#: too, but ONLY for a language whose spec declares a pitch accent
#: (``StressRules.accent2_mark`` — see :func:`_prosody_marks`): there they
#: are word-prosodic, not segmental, and the one gold set that writes them
#: (wikipron Swedish) marks them inconsistently — attested accent-2 trochees
#: like ⟨alla⟩ ⟨anka⟩ are left bare — so scoring them measures the
#: annotators' coverage, not G2P quality. For any other language the digits
#: stay: Yi (ycl) gold writes lexical TONE with the same superscripts
#: (²¹, ³³), and those are segments a G2P must produce.
_STRESS_MARKS = "ˈˌ'"
#: Tie bars are notation, not phonology: t͡s and ts are the same phoneme
#: string at every transcription tier, so they are stripped from BOTH
#: sides unconditionally (unlike the narrow diacritics below, which only
#: strip under --broad).
_TIE_BARS = "͜͡‿"

_NARROW_MARKS = "̝̞̪̺̻̼̘̙̯.·()"

#: Click accompaniment notation: a click's release/manner accompaniment
#: (velar ⟨k⟩, nasal ⟨ŋ⟩) is conventionally written either as a full IPA
#: letter immediately before the click letter (kǀ, ŋǃ) OR with the same
#: accompaniment carried by a dedicated superscript modifier letter in the
#: same slot (ᵏǀ, ᵑǃ) -- both are attested, interchangeable transcription
#: conventions for the SAME segment sequence, not a phonemic contrast (IPA
#: Chart 2015, superscript-modifier-letter convention; Ladefoged &
#: Maddieson, *The Sounds of the World's Languages*, 1996, ch.8 "Clicks",
#: pp.246-260, describing accompaniments transcribed either way with no
#: distinction implied). Folded ONLY when the modifier letter sits directly
#: next to one of the five IPA click letters (_CLICK_LETTERS), COMBINING
#: MARKS ON THE MODIFIER (e.g. a combining ring below for voicelessness,
#: ᵑ̊) allowed to ride along: ᵏ/ᵑ anywhere else (e.g. the common Bantuist
#: prenasalized-stop notation ᵑg/ᵐb) is a different, unrelated convention
#: and must not be touched. ʘ/ǀ/ǁ/ǃ/ǂ are five distinct click TYPES
#: (different active articulators) and are never folded into each other.
#: Applied AFTER the final whitespace join (some gold sets space-separate
#: phonemes, putting the modifier and its click letter on opposite sides
#: of a space -- e.g. "ᵑ ǂ" -- which must still fold).
_CLICK_LETTERS = "ǀǁǃǂʘ"
_CLICK_ACCOMPANIMENT_SUPERSCRIPTS = {"ᵏ": "k", "ᵑ": "ŋ"}
#: U+1DF06 (𝼆, "LATIN SMALL LETTER TURNED Y WITH BELT") is NOT a click
#: letter and is never folded into one. It is a ligature-style shorthand
#: for the voiceless palatal lateral fricative ʎ̥˔ (Unicode 13.0, 2021 --
#: analogous to how ɬ is a dedicated letter for the voiceless alveolar
#: lateral fricative). The Hadza wikipron alphabet-table rows write the
#: Hadza "tl" lateral affricate as bare 𝼆, while the corresponding word
#: rows write the SAME segment tie-barred as c͜ʎ̥˔ (see the "hts" registry
#: comment below) -- so the fold target is ʎ̥˔, not ǁ.
_NOTATIONAL_LETTER_ALIASES = {"𝼆": "ʎ̥˔"}

#: ASCII "g" (U+0067, keyboard Latin) vs the official IPA voiced velar
#: plosive ɡ (U+0261, LATIN SMALL LETTER SCRIPT G) — a Unicode confusable,
#: not a phonemic contrast (IPA Handbook, 1999, §"Consonants": the plosive
#: symbol is U+0261; ASCII "g" is a font-rendering/keyboard stand-in with
#: no distinct value anywhere in the Handbook's inventory). Several gold
#: sets (e.g. NorthEuraLex's CLDF Segments column) were keyed with the
#: plain ASCII letter, so a transcription that correctly emits ɡ was
#: being penalised for a typographic accident rather than an error. Folded
#: UNCONDITIONALLY (both strip_stress states, narrow and broad) because no
#: registered spec's own phoneme inventory contrasts "g" against "ɡ" —
#: verified against every data/*.json phonemes list before adding this.
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
    # Explicitly regional: the ⟨po⟩ file is European Portuguese and is
    # scored against the pt-PT spec (vowel reduction makes a higher PER
    # expected than pt-BR); the ⟨bz⟩ file is Brazilian. No bare "pt" row —
    # generic Portuguese defaults to pt-BR elsewhere in the registry.
    "pt-PT": "por_latn_po_broad.tsv",
    "pt-BR": "por_latn_bz_broad.tsv",
    "en": "eng_latn_us_broad.tsv",
    "en-GB": "eng_latn_uk_broad.tsv",
    # --- Semitic ---
    "ar": "ara_arab_broad.tsv",          # ~17.5k rows (MSA, broad)
    # Hebrew: Wiktionary headwords are UNPOINTED skeletons (a handful carry
    # niqqud), so — exactly like the undiacritized 'ar' gold above — short
    # vowels are orthographically absent from most inputs and a substantial
    # PER floor is expected. The file also mixes transcription traditions
    # (some rows are Tiberian-flavoured: ɔː, ə, ŋ); see data/he.json notes.
    "he": "heb_hebr_broad.tsv",          # ~6.8k rows (Hebrew script, broad)
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
    # Ukrainian and Belarusian: like Russian, WikiPron only scraped
    # NARROW transcriptions for these (no *_broad.tsv exists upstream);
    # the harness's default normalization strips narrow diacritics
    # before scoring, so they are comparable to the broad-tier golds.
    "uk": "ukr_cyrl_narrow.tsv",         # ~53k rows
    "be": "bel_cyrl_narrow.tsv",         # ~7k rows
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
    # --- registry sweep against the upstream CUNY-CL/wikipron scrape
    #     index (data/scrape/summary.tsv). Every language below has a
    #     broad WikiPron TSV with N>=200 AND a registered o2i spec that
    #     was NOT yet scored here. Each was smoke-checked: the engine
    #     produces non-empty output for the file's script (Han-script
    #     Chinese varieties, Uighur, Shan, Kashmiri, Sindhi, Saraiki,
    #     Sylheti, Dzongkha, Javanese, Mon, Aramaic, Bavarian, Scots,
    #     Tachelhit and Tuvinian had zero coverage and were left out).
    #     Same crowd-scraped Wiktionary tier as the rest of wikipron.
    "grc":       "grc_grek_broad.tsv",              # Ancient Greek (to 1453), ~198102 rows
    "ang":       "ang_latn_broad.tsv",              # Old English (ca. 450-1100), ~55835 rows
    "mt":        "mlt_latn_broad.tsv",              # Maltese, ~21208 rows
    "id":        "ind_latn_broad.tsv",              # Indonesian, ~18590 rows
    "th":        "tha_thai_broad.tsv",              # Thai, ~18319 rows
    "enm":       "enm_latn_broad.tsv",              # Middle English (1100-1500), ~18272 rows
    "sa":        "san_deva_broad.tsv",              # Sanskrit, ~17859 rows
    "fa":        "fas_arab_broad.tsv",              # Persian, ~10312 rows
    "izh":       "izh_latn_broad.tsv",              # Ingrian, ~9755 rows
    "my":        "mya_mymr_broad.tsv",              # Burmese, ~8288 rows
    "io":        "ido_latn_broad.tsv",              # Ido, ~7874 rows
    "ur":        "urd_arab_broad.tsv",              # Urdu, ~7709 rows
    "bn":        "ben_beng_rarh_broad.tsv",         # Bengali, ~7391 rows
    "km":        "khm_khmr_broad.tsv",              # Khmer, ~7108 rows
    "ms":        "msa_latn_broad.tsv",              # Malay (macrolanguage), ~6672 rows
    "sl":        "slv_latn_broad.tsv",              # Slovenian, ~5955 rows
    "nn":        "nno_latn_broad.tsv",              # Norwegian Nynorsk, ~5644 rows
    "se":        "sme_latn_broad.tsv",              # Northern Sami, ~5506 rows
    "bcl":       "bcl_latn_broad.tsv",              # Central Bikol, ~5432 rows
    "yi":        "yid_hebr_broad.tsv",              # Yiddish, ~5421 rows
    "te":        "tel_telu_broad.tsv",              # Telugu, ~5117 rows
    "yo":        "yor_latn_broad.tsv",              # Yoruba, ~4937 rows
    "mr":        "mar_deva_broad.tsv",              # Marathi, ~4872 rows
    "gu":        "guj_gujr_broad.tsv",              # Gujarati, ~4244 rows
    "egy":       "egy_latn_broad.tsv",              # Egyptian (Ancient), ~4177 rows
    "ceb":       "ceb_latn_broad.tsv",              # Cebuano, ~4100 rows
    "lb":        "ltz_latn_broad.tsv",              # Luxembourgish, ~4060 rows
    "bo":        "bod_tibt_broad.tsv",              # Tibetan, ~3621 rows
    "mn":        "mon_cyrl_broad.tsv",              # Mongolian, ~3563 rows
    "tg":        "tgk_cyrl_broad.tsv",              # Tajik, ~3269 rows
    "as":        "asm_beng_broad.tsv",              # Assamese, ~3223 rows
    "fo":        "fao_latn_broad.tsv",              # Faroese, ~3024 rows
    "szl":       "szl_latn_broad.tsv",              # Silesian, ~2925 rows
    "vot":       "vot_latn_broad.tsv",              # Votic, ~2915 rows
    "et":        "est_latn_broad.tsv",              # Estonian, ~2903 rows
    "csb":       "csb_latn_broad.tsv",              # Kashubian, ~2830 rows
    "dsb":       "dsb_latn_broad.tsv",              # Lower Sorbian, ~2484 rows
    "wa":        "wln_latn_broad.tsv",              # Walloon, ~2480 rows
    "ku":        "kmr_latn_broad.tsv",              # Northern Kurdish, ~2193 rows
    "ha":        "hau_latn_broad.tsv",              # Hausa, ~2176 rows
    "af":        "afr_latn_broad.tsv",              # Afrikaans, ~2171 rows
    "haw":       "haw_latn_broad.tsv",              # Hawaiian, ~2152 rows
    "got":       "got_goth_broad.tsv",              # Gothic, ~1837 rows
    "zu":        "zul_latn_broad.tsv",              # Zulu, ~1778 rows
    "aa":        "aar_latn_broad.tsv",              # Afar, ~1728 rows
    "kn":        "kan_knda_broad.tsv",              # Kannada, ~1713 rows
    "ht":        "hat_latn_broad.tsv",              # Haitian, ~1695 rows
    "za":        "zha_latn_broad.tsv",              # Zhuang, ~1691 rows
    "ny":        "nya_latn_broad.tsv",              # Nyanja, ~1624 rows
    "scn":       "scn_latn_broad.tsv",              # Sicilian, ~1599 rows
    "pa":        "pan_guru_broad.tsv",              # Panjabi, ~1586 rows
    "kl":        "kal_latn_broad.tsv",              # Kalaallisut, ~1581 rows
    "dv":        "div_thaa_broad.tsv",              # Dhivehi, ~1551 rows
    "ki":        "kik_latn_broad.tsv",              # Kikuyu, ~1420 rows
    "ps":        "pus_arab_broad.tsv",              # Pushto, ~1414 rows
    "no":        "nor_latn_broad.tsv",              # Norwegian, ~1331 rows
    "fy":        "fry_latn_broad.tsv",              # Western Frisian, ~1246 rows
    "hsb":       "hsb_latn_broad.tsv",              # Upper Sorbian, ~1130 rows
    "li":        "lim_latn_broad.tsv",              # Limburgan, ~1128 rows
    "ilo":       "ilo_latn_broad.tsv",              # Iloko, ~1049 rows
    "mi":        "mri_latn_broad.tsv",              # Maori, ~1005 rows
    "mww":       "mww_latn_broad.tsv",              # White Hmong (RPA), ~492 rows
    "nv":        "nav_latn_broad.tsv",              # Navajo, ~995 rows
    "ckb":       "ckb_arab_broad.tsv",              # Central Kurdish, ~981 rows
    "mh":        "mah_latn_broad.tsv",              # Marshallese, ~960 rows
    "pam":       "pam_latn_broad.tsv",              # Pampanga, ~926 rows
    "pms":       "pms_latn_broad.tsv",              # Piemontese, ~921 rows
    "kv":        "kpv_cyrl_broad.tsv",              # Komi-Zyrian, ~918 rows
    "ky":        "kir_cyrl_broad.tsv",              # Kirghiz, ~888 rows
    "nci":       "nci_latn_broad.tsv",              # Classical Nahuatl, ~886 rows
    "cop":       "cop_copt_broad.tsv",              # Coptic, ~881 rows
    "br":        "bre_latn_broad.tsv",              # Breton, ~874 rows
    "srn":       "srn_latn_broad.tsv",              # Sranan Tongo, ~849 rows
    "lij":       "lij_latn_broad.tsv",              # Ligurian, ~820 rows
    "stq":       "stq_latn_broad.tsv",              # Saterfriesisch, ~818 rows
    "gv":        "glv_latn_broad.tsv",              # Manx, ~785 rows
    "kk":        "kaz_cyrl_broad.tsv",              # Kazakh, ~774 rows
    "sc":        "srd_latn_broad.tsv",              # Sardinian, ~722 rows
    "guw":       "guw_latn_broad.tsv",              # Gun, ~681 rows
    "fax":       "fax_latn_broad.tsv",              # Fala, ~655 rows
    "kw":        "cor_latn_broad.tsv",              # Cornish, ~648 rows
    "krl":       "krl_latn_broad.tsv",              # Karelian, ~645 rows
    "lmo":       "lmo_latn_broad.tsv",              # Lombard, ~595 rows
    "iba":       "iba_latn_broad.tsv",              # Iban, ~584 rows
    "az":        "aze_latn_broad.tsv",              # Azerbaijani, ~513 rows
    "de-CH":     "gsw_latn_broad.tsv",              # Swiss German, ~511 rows
    "pdc":       "pdc_latn_broad.tsv",              # Pennsylvania German, ~510 rows
    "lt":        "lit_latn_broad.tsv",              # Lithuanian, ~507 rows
    "co":        "cos_latn_broad.tsv",              # Corsican, ~492 rows
    "nds":       "nds_latn_broad.tsv",              # Low German, ~492 rows
    "ia":        "ina_latn_broad.tsv",              # Interlingua (International Auxiliary Language Association), ~484 rows
    "ce":        "che_cyrl_broad.tsv",              # Chechen, ~480 rows
    "am":        "amh_ethi_broad.tsv",              # Amharic, ~478 rows
    "nup":       "nup_latn_broad.tsv",              # Nupe-Nupe-Tako, ~453 rows
    "tk":        "tuk_latn_broad.tsv",              # Turkmen, ~452 rows
    "vo":        "vol_latn_broad.tsv",              # Volapük, ~446 rows
    "jam":       "jam_latn_broad.tsv",              # Jamaican Creole English, ~415 rows
    "si":        "sin_sinh_broad.tsv",              # Sinhala, ~393 rows
    "war":       "war_latn_broad.tsv",              # Waray (Philippines), ~383 rows
    "tpw":       "tpw_latn_broad.tsv",              # Tupí, ~375 rows
    "sw":        "swa_latn_broad.tsv",              # Swahili (macrolanguage), ~370 rows
    "gn":        "gug_latn_broad.tsv",              # Paraguayan Guaraní, ~348 rows
    "uz":        "uzb_latn_broad.tsv",              # Uzbek, ~345 rows
    "xal":       "xal_cyrl_broad.tsv",              # Kalmyk, ~339 rows
    "mdf":       "mdf_cyrl_broad.tsv",              # Moksha, ~334 rows
    "non":       "non_latn_broad.tsv",              # Old Norse, ~318 rows
    "ban":       "ban_latn_broad.tsv",              # Balinese, ~300 rows
    "inh":       "inh_cyrl_broad.tsv",              # Ingush, ~300 rows
    "ppl":       "ppl_latn_broad.tsv",              # Pipil, ~283 rows
    "olo":       "olo_latn_broad.tsv",              # Livvi, ~278 rows
    "osx":       "osx_latn_broad.tsv",              # Old Saxon, ~273 rows
    "ace":       "ace_latn_broad.tsv",              # Achinese, ~272 rows
    "ee":        "ewe_latn_broad.tsv",              # Ewe, ~250 rows
    "sah":       "sah_cyrl_broad.tsv",              # Yakut, ~240 rows
    "cho":       "cho_latn_broad.tsv",              # Choctaw, ~235 rows
    "nrf":       "nrf_latn_broad.tsv",              # Jèrriais, ~234 rows
    "nap":       "nap_latn_broad.tsv",              # Neapolitan, ~231 rows
    "koi":       "koi_cyrl_broad.tsv",              # Komi-Permyak, ~229 rows
    "pag":       "pag_latn_broad.tsv",              # Pangasinan, ~229 rows
    "ba":        "bak_cyrl_broad.tsv",              # Bashkir, ~208 rows
    "ab":        "abk_cyrl_broad.tsv",              # Abkhazian, ~206 rows
    "kas":       "kas_arab_broad.tsv",              # Kashmiri (Perso-Arabic), ~751 rows
    "new":       "new_deva_narrow.tsv",             # Newar (Devanagari, narrow), ~416 rows
    "shn":       "shn_mymr_broad.tsv",              # Shan (Myanmar script), ~2607 rows
    # --- Arabic spoken dialects (ISO 639-3 codes → o2i lect) ---
    #     WikiPron scrapes six spoken Arabic dialects under their ISO 639-3
    #     codes; each maps onto an existing o2i ``ar-XX`` dialect spec (the
    #     registry alias table resolves the ISO code too). Like the MSA ``ar``
    #     row, these Wiktionary headwords are UNPOINTED consonantal skeletons —
    #     short vowels are orthographically absent, so a substantial PER floor
    #     from unvowelized input is expected (see the ``ar`` note above); the
    #     signal is consonant/long-vowel accuracy against the dialect spec, not
    #     a full-vowel score. Same crowd-scraped Wiktionary tier as the rest.
    "ar-EG":         "arz_arab_broad.tsv",          # Egyptian Arabic (arz), ~800 rows
    "ar-MA":         "ary_arab_broad.tsv",          # Moroccan Arabic (ary), ~2168 rows
    "ar-SY":         "apc_arab_broad.tsv",          # North Levantine (apc), ~618 rows
    "ar-JO":         "ajp_arab_broad.tsv",          # South Levantine (ajp), ~3182 rows
    "ar-x-gulf":     "afb_arab_broad.tsv",          # Gulf Arabic (afb), ~763 rows
    "ar-SA-x-hejaz": "acw_arab_broad.tsv",          # Hijazi Arabic (acw), ~2640 rows
    # --- new skeleton-tier specs, wired to their upstream WikiPron gold ---
    #     Each has a fresh skeleton spec added in this round (orthography kind,
    #     base grapheme inventory, cited ancestry). Smoke-checked to engage;
    #     scores are honest baselines for a first-pass grapheme map (conditioned
    #     allophony, tone and vowel length that the spelling does not recover are
    #     unencoded, so PER is high by construction). Same Wiktionary tier.
    "kix":       "kix_latn_broad.tsv",              # Khiamniungan Naga, ~4240 rows
    "sga":       "sga_latn_broad.tsv",              # Old Irish, ~3799 rows
    "yol":       "yol_latn_broad.tsv",              # Yola, ~2546 rows
    "liv":       "liv_latn_broad.tsv",              # Livonian, ~2516 rows
    "phl":       "phl_latn_broad.tsv",              # Phalura, ~2240 rows
    "hrx":       "hrx_latn_broad.tsv",              # Hunsrik, ~2108 rows
    "gmh":       "gmh_latn_broad.tsv",              # Middle High German, ~1724 rows
    "slr":       "slr_latn_broad.tsv",              # Salar, ~1724 rows
    "orv":       "orv_cyrl_broad.tsv",              # Old East Slavic, ~1612 rows
    "fro":       "fro_latn_broad.tsv",              # Old French, ~1057 rows
    "kaw":       "kaw_latn_broad.tsv",              # Kawi / Old Javanese, ~937 rows
    "sjs":       "sjs_latn_broad.tsv",              # Senhaja de Srair, ~865 rows
    "mak":       "mak_latn_broad.tsv",              # Makasar, ~834 rows
    "osp":       "osp_latn_broad.tsv",              # Old Spanish, ~681 rows
    "akk":       "akk_latn_broad.tsv",              # Akkadian, ~672 rows
    # --- wikipron-gap sweep: fresh skeleton/research specs wired to their
    #     upstream WikiPron gold. Each has a sourced grapheme map added in
    #     this round; scores are honest first-pass baselines (tone, vowel
    #     length and conditioned allophony the spelling does not recover are
    #     unencoded, so PER is high by construction). Same Wiktionary tier.
    #     Hard-script varieties (Han, Manchu, Tibetan, Canadian syllabics,
    #     Thai/Tai/Myanmar/Devanagari/Limbu/Hangul abugidas) got a spec but no
    #     row here: grapheme->IPA there is lexicon-dependent, cov-0 by design.
    "acm":        "acm_arab_broad.tsv",  # Mesopotamian Arabic, N=108
    "aii":        "aii_syrc_narrow.tsv",  # Assyrian Neo-Aramaic, N=7851
    "ale":        "ale_latn_broad.tsv",  # Aleut, N=121
    "aot":        "aot_latn_broad.tsv",  # Atong (India), N=181
    "apw":        "apw_latn_narrow.tsv",  # Western Apache, N=147
    "ayl":        "ayl_arab_broad.tsv",  # Libyan Arabic, N=166
    "bbl":        "bbl_geor_broad.tsv",  # Bats, N=421
    "bbn":        "bbn_latn_broad.tsv",  # Uneapa, N=194
    "bdq":        "bdq_latn_broad.tsv",  # Bahnar, N=198
    "bjb":        "bjb_latn_broad.tsv",  # Banggarla, N=136
    "bua":        "bua_cyrl_broad.tsv",  # Buriat, N=140
    "car":        "car_latn_narrow.tsv",  # Galibi Carib, N=447
    "chb":        "chb_latn_broad.tsv",  # Chibcha, N=121
    "cic":        "cic_latn_broad.tsv",  # Chickasaw, N=394
    "cnk":        "cnk_latn_broad.tsv",  # Khumi Chin, N=350
    "crk":        "crk_latn_narrow.tsv",  # Plains Cree, N=159
    "dlm":        "dlm_latn_broad.tsv",  # Dalmatian, N=180
    "dng":        "dng_cyrl_broad.tsv",  # Dungan, N=297
    "dum":        "dum_latn_broad.tsv",  # Middle Dutch (ca. 1050-1350), N=222
    "ett":        "ett_ital_broad.tsv",  # Etruscan, N=208
    "evn":        "evn_cyrl_broad.tsv",  # Evenki, N=153
    "fpe":        "fpe_latn_broad.tsv",  # Fernando Po Creole English, N=261
    "gml":        "gml_latn_broad.tsv",  # Middle Low German, N=175
    "gul":        "gul_latn_broad.tsv",  # Sea Island Creole English, N=304
    "gwc":        "gwc_arab_broad.tsv",  # Gawri, N=208
    "hil":        "hil_latn_broad.tsv",  # Hiligaynon, N=473
    # Hadza. 335 rows / 329 unique headwords, of which 52 are NOT words: the
    # scrape ingested the source's ALPHABET TABLE alongside its lexicon, so
    # ⟨cc⟩, ⟨Nq⟩, ⟨Tlh⟩ etc. appear as headwords glossed with the single
    # phoneme the letter spells. 26 of those 52 were transcribed in a
    # DIFFERENT notation from the same gold's word rows: the alphabet rows
    # write the clicks with superscript modifiers (ᵏǀ, ᵑǀʔ) and the "tl"
    # lateral affricate with U+1DF06 (𝼆), while every word row writes the
    # same segments with a tie bar (k͜ǀ, ŋ͜ǀˀ, c͜ʎ̥˔). `normalize` now folds
    # both notational variants together
    # (_CLICK_ACCOMPANIMENT_SUPERSCRIPTS for the clicks,
    # _NOTATIONAL_LETTER_ALIASES for 𝼆 -> ʎ̥˔, alongside the tie-bar strip
    # it already did), so the two conventions score as the same segments.
    "hts":        "hts_latn_broad.tsv",  # Hadza, N=335
    "huu":        "huu_latn_narrow.tsv",  # Murui Huitoto, N=440
    "kgp":        "kgp_latn_broad.tsv",  # Kaingang, N=107
    "kld":        "kld_latn_broad.tsv",  # Gamilaraay, N=516
    "klj":        "klj_latn_broad.tsv",  # Khalaj, N=155
    "kru":        "kru_deva_narrow.tsv",  # Kurukh, N=187
    "ktz":        "ktz_latn_broad.tsv",  # Juǀʼhoan, N=135
    "kwk":        "kwk_latn_broad.tsv",  # Kwakiutl, N=116
    "kxd":        "kxd_latn_broad.tsv",  # Brunei, N=365
    "lmy":        "lmy_latn_narrow.tsv",  # Lamboya, N=135
    "lou":        "lou_latn_broad.tsv",  # Louisiana Creole, N=262
    "lsi":        "lsi_latn_narrow.tsv",  # Lashi, N=141
    "lut":        "lut_latn_broad.tsv",  # Lushootseed, N=140
    "lzz":        "lzz_geor_broad.tsv",  # Laz, N=363
    "mch":        "mch_latn_narrow.tsv",  # Maquiritari, N=1746
    "mdh":        "mdh_latn_broad.tsv",  # Maguindanaon, N=205
    "mfe":        "mfe_latn_broad.tsv",  # Morisyen, N=233
    "mga":        "mga_latn_broad.tsv",  # Middle Irish (900-1200), N=501
    "mic":        "mic_latn_broad.tsv",  # Mi'kmaq, N=203
    "mqs":        "mqs_latn_broad.tsv",  # West Makian, N=791
    "mtq":        "mtq_latn_broad.tsv",  # Muong, N=194
    "ngh":        "ngh_latn_broad.tsv",  # Nǁng, N=325
    "nhg":        "nhg_latn_narrow.tsv",  # Tetelcingo Nahuatl, N=305
    "nhx":        "nhx_latn_broad.tsv",  # Isthmus-Mecayapan Nahuatl, N=146
    "niv":        "niv_cyrl_broad.tsv",  # Gilyak, N=627
    "nmy":        "nmy_latn_narrow.tsv",  # Namuyi, N=354
    "oji":        "oji_latn_broad.tsv",  # Ojibwa, N=136
    "ota":        "ota_arab_broad.tsv",  # Ottoman Turkish (1500-1928), N=209
    "pbv":        "pbv_latn_broad.tsv",  # Pnar, N=101
    "pcc":        "pcc_latn_broad.tsv",  # Bouyei, N=153
    "pjt":        "pjt_latn_narrow.tsv",  # Pitjantjatjara, N=125
    "pox":        "pox_latn_broad.tsv",  # Polabian, N=321
    "pqm":        "pqm_latn_broad.tsv",  # Malecite-Passamaquoddy, N=151
    "rgn":        "rgn_latn_broad.tsv",  # Romagnol, N=267
    "sce":        "sce_latn_broad.tsv",  # Dongxiang, N=169
    "sdc":        "sdc_latn_broad.tsv",  # Sassarese Sardinian, N=344
    "sia":        "sia_cyrl_broad.tsv",  # Akkala Sami, N=181
    "sid":        "sid_latn_broad.tsv",  # Sidamo, N=298
    "sjd":        "sjd_cyrl_broad.tsv",  # Kildin Sami, N=761
    "sms":        "sms_latn_broad.tsv",  # Skolt Sami, N=119
    "srs":        "srs_latn_broad.tsv",  # Sarsi, N=137
    "syc":        "syc_syrc_broad.tsv",  # Classical Syriac, N=133
    "tew":        "tew_latn_broad.tsv",  # Tewa (USA), N=106
    "tft":        "tft_latn_broad.tsv",  # Ternate, N=297
    "tkl":        "tkl_latn_narrow.tsv",  # Tokelau, N=340
    "tru":        "tru_syrc_broad.tsv",  # Turoyo, N=232
    "twf":        "twf_latn_broad.tsv",  # Northern Tiwa, N=135
    "tzm":        "tzm_tfng_broad.tsv",  # Central Atlas Tamazight, N=690
    "uby":        "uby_cyrl_narrow.tsv",  # Ubykh, N=1317
    "ulw":        "ulw_latn_broad.tsv",  # Ulwa, N=103
    "wau":        "wau_latn_broad.tsv",  # Waurá, N=146
    "wbk":        "wbk_latn_broad.tsv",  # Waigali, N=154
    "wiy":        "wiy_latn_broad.tsv",  # Wiyot, N=151
    "wlm":        "wlm_latn_broad.tsv",  # Middle Welsh, N=435
    "xsl":        "xsl_latn_narrow.tsv",  # South Slavey, N=304
    "ycl":        "ycl_latn_narrow.tsv",  # Lolopo, N=111
    "yrk":        "yrk_cyrl_narrow.tsv",  # Nenets, N=455
    "yux":        "yux_cyrl_narrow.tsv",  # Southern Yukaghir, N=255
    "zom":        "zom_latn_narrow.tsv",  # Zou, N=165
    "zza":        "zza_latn_narrow.tsv",  # Zaza, N=215
    # --- orthography wave 5: fresh cited grapheme maps wired to their
    #     upstream WikiPron gold. Scores are honest first-pass baselines.
    "ug":         "uig_arab_broad.tsv",  # Uyghur, N=2674
    "dz":         "dzo_tibt_broad.tsv",  # Dzongkha, N=243 (base-letter table only, see data/dz.json notes)
    # --- orthography wave 6: fresh cited grapheme maps wired to their
    #     upstream WikiPron gold. Scores are honest first-pass baselines.
    "skr":        "skr_arab_broad.tsv",           # Saraiki, Shahmukhi, N~348
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
_PT_UNIFIED_URL = (
    "https://huggingface.co/datasets/TigreGotico/"
    "portuguese-unified-pronunciation-lexicon"
    "/resolve/main/portuguese_pronunciation_lexicon.jsonl"
)
#: orthography2ipa language tag -> unified-dataset region tag. Only regions
#: with a matching o2i spec AND a usable row count are scored; the tiny
#: paulistano/paulista registers (~50 words each) and untagged "pt" rows
#: are deliberately left out.
_PT_UNIFIED_REGIONS: Dict[str, str] = {
    "pt-PT": "pt-PT",                       # Infopedia + Wiktionary EP, ~116k rows
    "pt-PT-x-lisbon": "pt-PT-x-lisboa",     # Portal lexicon Lisbon, ~62k rows
    "pt-BR": "pt-BR",                       # Wiktionary BR, ~3.6k rows
    "pt-BR-x-sp": "pt-BR-x-saopaulo",       # Portal lexicon Sao Paulo, ~92k rows
    "pt-BR-x-rj": "pt-BR-x-riodejaneiro",   # Portal lexicon Rio, ~64k rows
    "pt-BR-x-carioca": "pt-BR-x-carioca",   # Wiktionary carioca, ~566 words
    "pt-BR-x-caipira": "pt-BR-x-caipira",   # Wiktionary caipira, ~83 words
    "pt-AO": "pt-AO",                       # Portal lexicon Luanda, ~53k rows
    "pt-MZ": "pt-MZ-x-maputo",              # Portal lexicon Maputo, ~95k rows
    "pt-TL": "pt-TL-x-dili",                # Portal lexicon Dili, ~53k rows
}
_VOX_COMMUNIS_BASE = (
    "https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p"
    "/resolve/main/"
)
#: orthography2ipa language tag -> vox-communis TSV file name (without .tsv).
#: Direct matches are generated from the intersection of the dataset's 78
#: per-language files with the spec inventory; the alias entries map the
#: dataset's regionalised file names onto the spec that covers them. The
#: ``pt`` file is registered under pt-BR: Common Voice Portuguese is
#: predominantly Brazilian and the file itself is region-untagged (same
#: policy as the WikiPron generic-pt row).
_VOX_COMMUNIS_FILES: Dict[str, str] = {
    lang: lang for lang in (
        "ab", "am", "as", "ba", "be", "bg", "bn", "ca", "ckb", "cs", "cv",
        "cy", "dv", "el", "et", "eu", "fi", "gl", "gn", "ha", "hi", "hsb",
        "hu", "id", "ja", "ka", "kab", "kk", "ko", "ky", "lg", "lij", "lt",
        "mk", "ml", "mn", "mr", "mt", "myv", "nl", "or", "pl", "ru", "rw",
        "sah", "sk", "sl", "sq", "sr", "sw", "ta", "th", "tk", "tn", "tr",
        "tt", "ug", "uk", "uz", "vi", "yo",
    )
}
_VOX_COMMUNIS_FILES.update({
    "es": "es", "it": "it", "ro": "ro",       # bare tags resolve via registry
    "pt-BR": "pt",                            # region-untagged; see note above
    "sv": "sv-se", "hy": "hy-am",
    "fy": "fy-nl", "pa": "pa-in",
})
#: Non-speech / no-coverage placeholders in the ``phonemized_sentence``
#: phone tier. ``spn`` (MFA "spoken noise", reused by VoxCommunis as the
#: lexicon-miss marker) is the ONLY one that may be filtered.
#:
#: The obvious siblings — ``sil``, ``sp``, ``nsn``, ``noise`` — are
#: deliberately NOT listed, because in these files they occur almost
#: entirely as GENUINE transcriptions of real words, and filtering on the
#: phone string alone would silently delete them: Welsh ``sul`` → /sil/
#: (336 rows), Amharic ``ሲል`` → /sil/, Bulgarian ``сп`` → /sp/, Tamil
#: ``ஸ்ப்`` → /sp/, Korean ``실`` → /sil/, Punjabi ``ਸੀਲ`` → /sil/.
#:
#: 61 rows across seven files additionally have the marker on BOTH tiers
#: (word ``sil`` → phones ``sil``), which does look like an aligner
#: placeholder leaking into the orthography. Those are left in too: the
#: identity test is not safe either, because Turkish ``sil`` ("wipe",
#: imperative of *silmek*) is a real word genuinely pronounced [sil]. 61
#: rows out of ~2.6M is far below the noise floor of an
#: ``epitran-derived`` row, and no filter separates the leak from the real
#: word without a per-language lexicon.
#:
#: See :func:`load_vox_communis` for why ``spn`` in particular can never be
#: scored.
_VOX_COMMUNIS_NON_SPEECH = frozenset({"spn"})
# ``zh`` (Mandarin) is DELIBERATELY not registered here either, for exactly
# the reason spelled out for ``yue`` below and already recorded for the
# ipa-dict ``zh_*``/``yue`` files in docs/benchmarks.md ("Rejected
# candidates"): the o2i ``zh`` spec is a PINYIN spec, while
# ``zh-cn.tsv``'s ``aligned_sentence`` column is Han characters
# (``盘固 草 为 禾 本科 …``). Every single row therefore transcribes to the
# empty string, and the board carried a meaningless ``per: 1.0`` row for
# ``zh`` built entirely out of "hypothesis is empty, so the whole gold is a
# deletion". That is not a Mandarin score; it is the absence of a
# hanzi→pinyin front-end, measured in the units of a phone error rate. The
# registration comes back the day such a front-end exists.
#
# ``yue`` (Cantonese) is DELIBERATELY not registered here even though the
# upstream ``yue.tsv`` file exists and loads fine (12.8k rows, live-checked
# 2026-08). The `yue` spec is a genuine grapheme-inventory STUB (see
# orthography2ipa/g2p.py get('yue').notes): Cantonese is logographic and
# has no letter-to-sound mapping without a Jyutping/Yale romanisation step
# upstream of this library -- exactly like ``zh`` needs pinyin. The
# vox-communis ``yue.tsv`` ``sentence``/``aligned_sentence`` columns are raw
# Han characters, so every row transcribes to an empty hypothesis and the
# harness previously recorded a fake ``per: 1.0, n: 0`` row for it. That
# was dishonest (n=0 read as "loader is broken", not "this pairing can
# never score"); removing the registration until a Jyutping/Yale
# transliteration front-end exists is the honest fix.


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
    # Cusco, not the `qu` macrolanguage. `qu.json` is a declared structural
    # adstrate STUB with no phonology (no ⟨q⟩, no ⟨ch⟩, no ⟨ll⟩, no laryngeal
    # series), so scoring this corpus against it measured the stub, not a
    # Quechua spec. The corpus itself names its variety: 220 of its 1572
    # official-alphabet word types spell an aspirate or an ejective (⟨qhawariy⟩
    # ⟨q'illu⟩ ⟨sach'a⟩ ⟨mikhun⟩) and ⟨q⟩ is transcribed as a stop throughout —
    # both are Cusco-Collao, and both are exactly what Ayacucho (`quy`) lacks.
    # `quy` happens to score a little lower on this gold; taking that score
    # would be fitting the row to the gold against the corpus's own evidence.
    #
    # The row keeps a high PER floor that is notation, not error. espeak-ng's
    # `qu` voice (dictsource/qu_rules) is a plain letter-to-phoneme table: it
    # writes /i u/ as lax [ɪ ʊ] (2391 substitutions), ⟨ch⟩ with a retraction
    # diacritic as t̠ʃ (735), the tap as a trill r (536), and an ejective as the
    # ejective plus a spurious glottal stop, ⟨k'⟩ → kʼʔ (133, from the rule file's
    # own "q' → q`?"). It applies no uvular lowering at all, so every [ɑ ɛ ɔ]
    # this spec derives by rule is scored as an error (538). Where the two
    # disagree on a segment the cited source settles it: ⟨sh⟩ is /ʃ/ in Cusco,
    # which espeak renders as s+h. The corpus also mixes varieties, not just
    # orthographies — a 296-type subcorpus (corpus_id 358) is Ecuadorian
    # Highland Kichwa, a different Quechuan language mislabelled qu-PE
    # upstream: it has the perfect/gerund endings -shca/-shpa where Cusco has
    # -sqa/-spa, ñuca for Cusco ñuqa, ashcu for Cusco allqu, micuna where
    # Cusco has mikhuna. Neither `quz` nor `quy` can read Kichwa, which no
    # trivocalic Southern Quechua spec is meant to; it scores ~0.17 worse
    # than the official-alphabet Cusco-Collao corpus (1572 word types,
    # corpus_id 146) for every Southern Quechua spec. Splitting Kichwa out of
    # this IPA-CHILDES folder into its own row is future work (o2i #91), not
    # something this loader can decide.
    "quz": "qu-PE",
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
    "quz": "phonemizer (espeak-ng), qu",
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


# Lexibank/CLDF wordlist gold. Lexibank (github.com/lexibank) republishes
# published comparative wordlists/dictionaries as CLDF (Cross-Linguistic Data
# Format): one ``cldf/forms.csv`` per dataset, keyed by ``Language_ID`` (the
# dataset's own language code, resolved via ``cldf/languages.csv``), with a
# ``Value`` column (the word as originally recorded — real orthography or
# script) and a ``Segments`` column (space-separated IPA-ish segments, with
# ``+`` marking a morpheme boundary). Every row cites its source dictionary
# in the ``Source`` column, so this is compiled/cited lexicographic data, not
# phonemizer output — ``lexicon-derived``, the same tier as ``cmudict`` and
# ``portuguese_unified``.
#
# Candidates inspected and NOT wired:
#
# - `lexibank/ids` (Intercontinental Dictionary Series): ``Segments`` is
#   EMPTY on every one of its 437k rows (verified by scanning the whole
#   file) — there is no IPA column to score against at all.
# - `lexibank/abvd` (Austronesian Basic Vocabulary Database): same problem,
#   ``Segments`` empty on all 346k rows.
#
# 2026-08 audit wave — 21 more candidates inspected, NONE wired. Full verdicts
# and evidence in docs/benchmarks.md "Rejected candidates". Summary:
#
# - `uralex`: ``Segments`` empty on all sampled rows (same as ids/abvd).
# - `tuled`, `dravlex`, `chaconarawakan`, `felekesemitic`, `hantganbangime`,
#   `lundgrenomagoa`, `naganorgyalrongic`, `sagartst`, `savelyevturkic`,
#   `abrahammonpa`, `allenbai`, `bantubvd`, `chindialectsurvey`,
#   `birchallchapacuran`, `gravinachadic`, `kraftchadic`,
#   `luangthongkumkaren`, `marrisonnaga`, `mitterhoferbena`: ``Value`` is
#   itself an IPA/comparative-transcription string (tone marks, IPA-only
#   symbols, sense-index suffixes, or a fieldworker's normalized transcription
#   convention applied uniformly across many languages) — not each
#   language's own writing system, failing the "Form must be real
#   orthography, not transcription" rule this loader exists to enforce.
# - `robinsonap`: the one candidate whose ``Value`` genuinely reads as
#   practical orthography (real digraphs, e.g. ``ng``→``ŋ``). Still not
#   wired: all 13 languages resolve to `stub`-quality o2i specs with an
#   EMPTY grapheme table, so there is nothing for a gold row to exercise yet.
#
# Two datasets passed inspection and are wired: `northeuralex` (NorthEuraLex,
# Dellert et al. 2020) and `wold` (World Loanword Database, Haspelmath &
# Tadmor 2009), both real orthographic ``Value`` + populated ``Segments``.
_LEXIBANK_RAW_BASE = "https://raw.githubusercontent.com/lexibank/{repo}/master/cldf/"


def _lexibank_segments_to_ipa(segments: str) -> str:
    """Join a CLDF ``Segments`` string ("s ɛ m") into one IPA string,
    dropping the ``+`` morpheme-boundary marker (the only non-IPA token
    either wired Lexibank dataset's Segments column contains)."""
    return "".join(seg for seg in segments.split() if seg != "+")


def _load_lexibank(repo: str, language_id: str, limit: int) -> List[Tuple[str, str]]:
    """Shared CLDF ``forms.csv`` reader for the Lexibank datasets below:
    filters to one ``Language_ID``, pairs the original-orthography ``Value``
    with the IPA joined from ``Segments``, skips rows with no segments
    (unelicited/missing forms) and de-duplicates by (word, ipa).
    """
    url = _LEXIBANK_RAW_BASE.format(repo=repo) + "forms.csv"
    text = _fetch(url, f"lexibank_{repo}_forms.csv")
    pairs: List[Tuple[str, str]] = []
    seen = set()
    reader = csv.DictReader(text.splitlines())
    for row in reader:
        if row.get("Language_ID") != language_id:
            continue
        word = (row.get("Value") or "").strip()
        segments = (row.get("Segments") or "").strip()
        if not word or not segments:
            continue
        ipa = _lexibank_segments_to_ipa(segments)
        if not ipa:
            continue
        key = (word, ipa)
        if key in seen:
            continue
        seen.add(key)
        pairs.append((word, ipa))
        if len(pairs) >= limit:
            break
    return pairs


# orthography2ipa language tag -> NorthEuraLex Language_ID (its own code,
# which happens to equal the ISO 639-3 code for every language wired here).
# Restricted to languages whose o2i spec (a) is registered and (b) is a
# `stub`/`skeleton`-tier spec with a NON-EMPTY grapheme table that the
# gold can actually exercise — this loader targets the stub-promotion
# path, not already-`research`/`production` languages. Every entry was
# smoke-checked: the engine produces non-empty output for a large majority
# of the language's sampled forms (see docs/benchmarks.md).
#
# Excluded despite an ISO/registry match: `yux` (Southern Yukaghir) has a
# non-empty grapheme table but scored 0/913 non-empty — a script/transliteration
# mismatch between the spec's grapheme inventory and NorthEuraLex's Cyrillic
# orthography for this variety, not something a gold row can fix.
_NORTHEURALEX_LANGS: Dict[str, str] = {
    "liv": "liv",   # Livonian (skeleton)
    "sms": "sms",   # Skolt Sami (skeleton)
    "sjd": "sjd",   # Kildin Sami (skeleton)
    "yrk": "yrk",   # Tundra Nenets (skeleton)
    "bua": "bua",   # Buryat (skeleton)
    "evn": "evn",   # Evenki (skeleton)
    "niv": "niv",   # Nivkh (skeleton)
    "ale": "ale",   # Aleut (skeleton)
    "ain": "ain",   # Hokkaido Ainu (stub)
    # 2026-08 registration wave: 9 languages with ZERO gold anywhere and a
    # non-empty grapheme table, each verified against cldf/languages.csv
    # (not a naive ISO 639-3 lookup — two of these need a code translation,
    # see below) and smoke-checked at 100/100 non-empty engine output:
    "udm": "udm",   # Udmurt (research)
    "ady": "ady",   # Adyghe (research)
    # o2i `av` is the macrolanguage code; NEL's own Language_ID for Avar is
    # its ISO 639-3 code "ava" (languages.csv: avar1256, "Avar"), not "av".
    "av": "ava",    # Avar (research)
    "lbe": "lbe",   # Lak (research)
    # NEL's `dar` row is glottocode darg1241, "North-Central Dargwa" — the
    # same Akusha-based variety the o2i `dar` spec targets ("the literary
    # standard is based on the Akusha dialect ... this spec targets the
    # literary Akusha-based standard only"), not a different Dargwa lect.
    # This gold row completes `dar`'s promotion from `skeleton` to `research`
    # (sources + a documented stress exemption were already in place).
    "dar": "dar",   # Dargwa (research, promoted by this wave)
    "lez": "lez",   # Lezgian (research)
    # o2i `lv` is the ISO 639-1 code; NEL's own Language_ID for Latvian is
    # its ISO 639-3 code "lav" (languages.csv: latv1249, "Latvian").
    "lv": "lav",    # Latvian (research)
    "smn": "smn",   # Inari Sami (research)
    "vep": "vep",   # Veps (research)
    # 2026-08 "Siberian double-win" wave: 8 Uralic (+1 Yukaghir) REGISTRY STUBs
    # that were empty-grapheme placeholders with a cited PHOIBLE phoneme
    # inventory already in place; this wave adds cited Cyrillic orthographies
    # (Alhoniemi 1985, Kangasmaa-Minn 1998, Nikolaeva 1999, Riese 2001,
    # Helimski 1998, Wagner-Nagy 2018, Siegl 2013, Maslova 2003 — see each
    # spec's `sources`) and reconciles them against the existing PHOIBLE
    # inventories. Language_ID in cldf/languages.csv equals the o2i code for
    # all eight (no av->ava-style translation needed here); each smoke-checked
    # at 150/150 non-empty engine output on a NorthEuraLex sample.
    "mhr": "mhr",   # Meadow (Eastern) Mari (research)
    "mrj": "mrj",   # Hill (Western) Mari (research)
    "kca": "kca",   # Northern Khanty (research)
    "mns": "mns",   # Northern Mansi (research)
    "sel": "sel",   # Northern Selkup (research)
    "nio": "nio",   # Nganasan (research)
    "enf": "enf",   # Forest Enets (research)
    "ykg": "ykg",   # Northern Yukaghir (research)
    # 2026-08 Siberian double-win batch B: Paleosiberian/Tungusic/isolate stubs
    # promoted from empty REGISTRY STUBs to Cyrillic (mnc: Moellendorff Latin
    # romanization — see mnc.json notes) grapheme tables, each verified against
    # cldf/languages.csv (Language_ID == o2i code for all of these) and
    # smoke-checked for non-empty engine output. `bsk` (Burushaski) was
    # evaluated and deliberately excluded: its NEL Value column is Berger
    # (1998) scholarly transcription, not a community orthography — see
    # bsk.json notes.
    "ckt": "ckt",   # Chukchi (skeleton)
    "itl": "itl",   # Itelmen (skeleton)
    "ket": "ket",   # Ket (skeleton)
    "gld": "gld",   # Nanai (skeleton)
    "mnc": "mnc",   # Manchu, Moellendorff romanization (skeleton)
    "ddo": "ddo",   # Tsez (skeleton)
    "ess": "ess",   # Central Siberian Yupik (skeleton)
}


def load_northeuralex(lang: str, limit: int) -> List[Tuple[str, str]]:
    """NorthEuraLex (lexibank/northeuralex, Dellert et al. 2020): a
    100+-language comparative wordlist of Northern Eurasia, CLDF ``Value``
    (dictionary orthography) + ``Segments`` (IPA-ish phonemic transcription,
    cited per row to its source dictionary in ``Source``). See
    ``_NORTHEURALEX_LANGS`` for the wired subset and why."""
    return _load_lexibank("northeuralex", _NORTHEURALEX_LANGS[lang], limit)


# orthography2ipa language tag -> WOLD Language_ID (the dataset's own
# per-language folder/ID name, not an ISO code). Same stub-promotion
# selection discipline as `_NORTHEURALEX_LANGS`: smoke-checked, non-empty
# grapheme table, majority non-empty output.
#
# Excluded despite an ISO match: WOLD's own `KildinSaami` (`sjd`) romanizes
# the language differently from NorthEuraLex's Cyrillic forms (scored only
# 25/1473 non-empty) — NorthEuraLex's `sjd` row above is the one that
# actually exercises the spec's grapheme table for this language, so WOLD's
# duplicate entry is left out rather than wired at a token score.
_WOLD_LANGS: Dict[str, str] = {
    "car": "Kalina",       # Galibi Carib (skeleton)
    "arn": "Mapudungun",   # Mapudungun (stub)
    # 2026-08 gold-hunting wave 1: remaining WOLD languages cross-referenced
    # against the o2i spec registry. Of WOLD's other 39 languages, most
    # already have gold from wikipron/ipadict/etc (English, Dutch, Japanese,
    # Mandarin, Thai, Vietnamese, Indonesian, Hawaiian, White Hmong, Hausa,
    # Lower Sorbian, Kildin Saami, ...); several have NO registered o2i spec
    # at all (Kanuri `knc`, Zinacantan Tzotzil `tzz`, Malagasy `plt`, Old
    # High German, Selice Romani, Sakha have no ISO/spec match here); and the
    # rest resolve to `stub` specs with an EMPTY grapheme table (Archi,
    # Bezhta, Manange, Ket, Oroqen, Ceq Wong, Takia, Gurindji, Yaqui,
    # Qeqchi, Otomi, Saramaccan, Imbabura Quechua, Hup, Wichi) -- nothing for
    # a gold row to exercise yet, same reasoning as the Lexibank/robinsonap
    # rejection above. Only four had BOTH a non-empty grapheme table AND no
    # existing gold row anywhere in this registry; all four smoke-checked at
    # ~100% non-empty engine coverage on a 150-row sample:
    "gwd": "Gawwada",        # Gawwada (skeleton), coverage 150/150
    "irk": "Iraqw",          # Iraqw (skeleton), coverage 150/150
    "crs": "SeychellesCreole",   # Seychelles Creole (research), coverage 150/150
    "rif": "TarifiytBerber",     # Tarifiyt Berber (research), coverage 149/150
}


def load_wold(lang: str, limit: int) -> List[Tuple[str, str]]:
    """World Loanword Database (lexibank/wold, Haspelmath & Tadmor 2009): a
    41-language loanword-typology wordlist, CLDF ``Value`` (dictionary
    orthography) + ``Segments`` (IPA-ish transcription). See
    ``_WOLD_LANGS`` for the wired subset and why."""
    return _load_lexibank("wold", _WOLD_LANGS[lang], limit)


# ── kaikki.org (Wiktextract) ────────────────────────────────────────────────
#
# kaikki.org publishes machine-extracted per-language dumps of Wiktionary
# ("Wiktextract", Ylonen 2022) as JSON-lines: one object per dictionary
# entry, with a ``word`` (the headword as written) and a ``sounds`` list of
# ``{"ipa": "..."}`` objects (often several transcription variants per
# entry). Same crowd-scraped Wiktionary tier as ``wikipron`` -- this is a
# different extraction pipeline over the same underlying source, not an
# independent transcriber.
#
# 2026-08 gold-hunting wave 2: targeted at o2i specs with a non-empty
# grapheme table and ZERO gold anywhere else in this registry. Every
# wired language was downloaded, filtered to entries with a non-empty
# ``sounds[].ipa``, and hand-sampled (see docs/benchmarks.md) before
# wiring. Rejected: Tigrinya (only 28/933 entries carry ``ipa`` -- too
# thin to be a usable gold set).
#
# Tetum (`tet`) was checked against kaikki.org and REJECTED: the Tetum dump has
# 686 entries and exactly 3 of them carry a `sounds[].ipa`, an order of
# magnitude thinner than the Tigrinya set already rejected below. WikiPron has
# no Tetum scrape either (no `tet_latn_*.tsv` upstream), so the language's gold
# is the primary-source set mined from its own reference grammar instead.
#
# 2026-08 gold-hunting wave 3: re-ran the zero-gold sweep (it shrank a lot
# between waves) and checked kaikki.org coverage for the top-tier-by-speakers
# zero-gold languages. Added: `so` (Somali), `om` (Oromo), `ne` (Nepali),
# `kok` (Konkani). Re-checked: Tigrinya is UNCHANGED (still 28/933 -- stays
# rejected), and Sindhi (`sd`) / Santali (`sat`) were investigated and
# rejected -- see docs/benchmarks.md for both.
_KAIKKI_BASE = "https://kaikki.org/dictionary/{name}/kaikki.org-dictionary-{name}.jsonl"

# orthography2ipa language tag -> kaikki.org per-language dump directory name.
_KAIKKI_LANGS: Dict[str, str] = {
    "jv": "Javanese",   # Javanese (skeleton)
    "su": "Sundanese",  # Sundanese (skeleton)
    "lo": "Lao",        # Lao (skeleton)
    "xh": "Xhosa",      # Xhosa (skeleton)
    "so": "Somali",     # Somali (research)
    "om": "Oromo",      # Oromo (skeleton)
    "ne": "Nepali",     # Nepali (research)
    "kok": "Konkani",   # Konkani (research)
}

#: kaikki entries whose ``pos`` is one of these are dictionary metadata
#: (single-letter/digraph "character" glosses describing an orthographic
#: symbol, e.g. Xhosa ``hl`` -> /ɬ/), not words -- they would double-count
#: the same grapheme fact the spec's own table already encodes, so they are
#: excluded from the gold rather than scored as if they were lexical items.
_KAIKKI_EXCLUDED_POS = {"character"}

#: Wiktionary mixes scripts for some languages (kaikki's Javanese dump is
#: majority Aksara Jawa entries even though the o2i ``jv`` spec is Latin-only
#: romanization) -- restrict to the script the wired spec actually covers.
#: ``None`` means no filter (the dump is already single-script for that
#: language, verified during the smoke-check).
_KAIKKI_WORD_FILTER: Dict[str, "re.Pattern[str]"] = {
    "jv": re.compile(r"[A-Za-z'\-]+\Z"),
    # `so` and `om` specs are Latin-only (official orthographies), but their
    # kaikki dumps carry a handful of non-Latin/loanword entries -- restrict
    # to the script the spec actually covers, same rationale as `jv`.
    "so": re.compile(r"[A-Za-z'\-]+\Z"),
    "om": re.compile(r"[A-Za-z'\-]+\Z"),
}


def load_kaikki(lang: str, limit: int) -> List[Tuple[str, str]]:
    """kaikki.org (Wiktextract) per-language Wiktionary extract: pairs the
    entry ``word`` with the first non-empty ``sounds[].ipa`` transcription,
    stripping the slash/bracket transcription-type delimiters kaikki wraps
    around each variant. See ``_KAIKKI_LANGS`` for the wired subset and why."""
    name = _KAIKKI_LANGS[lang]
    word_filter = _KAIKKI_WORD_FILTER.get(lang)
    url = _KAIKKI_BASE.format(name=name)
    text = _fetch(url, f"kaikki_{name}.jsonl")
    pairs: List[Tuple[str, str]] = []
    seen = set()
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        if entry.get("pos") in _KAIKKI_EXCLUDED_POS:
            continue
        word = (entry.get("word") or "").strip()
        if not word or " " in word:
            continue
        if word_filter is not None and not word_filter.match(word):
            continue
        ipa = None
        for sound in entry.get("sounds") or []:
            raw = (sound.get("ipa") or "").strip()
            if raw:
                ipa = raw.strip("/[]")
                break
        if not ipa:
            continue
        key = (word, ipa)
        if key in seen:
            continue
        seen.add(key)
        pairs.append((word, ipa))
        if len(pairs) >= limit:
            break
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


def _fetch_file(url: str, name: str) -> str:
    """Download *url* to ``CACHE_DIR/name`` once and return the path. Binary
    safe, so archives can be cached the same way text files are."""
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
    return dest


def _fetch(url: str, name: str) -> str:
    with open(_fetch_file(url, name), encoding="utf-8", errors="replace") as fh:
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

    PROVENANCE — the upstream dataset regrew to ~1.8k rows with a per-row
    ``provenance_tier`` column. Rows tagged ``engine-verified-convention``
    are o2i-derived and are EXCLUDED here (circular). The remaining
    ``dicionario-headword`` rows take their headwords from the published
    Dicionário de Barranquenho (2025), but the near-zero PER o2i scores
    against them suggests their IPA column is itself o2i-aligned — treat
    every number from this dataset as agreement, not correctness, until
    upstream documents who produced the IPA. The row stays at the lowest
    reliability tier and can gate nothing.
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
        # The dataset renamed its IPA column from ``ipa_transcription`` to
        # ``ipa`` when it grew to 1.8k rows; accept both spellings so a
        # fresh (uncached) fetch never silently yields zero rows again.
        ipa = (row.get("ipa") or row.get("ipa_transcription") or "").strip()
        # Rows tagged ``engine-verified-convention`` were produced by running
        # o2i itself over the orthographic convention: scoring o2i against
        # them is circular, so they are excluded from the gold. The
        # ``navas-attested`` (human, Navas Sanchez-Elez) and
        # ``dicionario-headword`` tiers remain scorable.
        if (row.get("provenance_tier") or "").strip() == "engine-verified-convention":
            continue
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


def load_portuguese_unified(lang: str, limit: int) -> List[Tuple[str, str]]:
    """Portuguese unified pronunciation lexicon, one REGION per language tag
    (TigreGotico/portuguese-unified-pronunciation-lexicon on Hugging Face,
    ~598k rows / 122k words, CC BY-SA 4.0).

    Merges the three previous TigreGotico Portuguese golds into one
    convention-normalized dataset — Infopedia (Porto Editora dictionary),
    pt.wiktionary.org, and the Portal da Lingua Portuguesa 10-region
    lexicon — and REPLACES their separate loaders here. Each JSONL row is a
    word x region x source x POS tuple carrying both a broad phonemic and a
    narrow phonetic transcription normalized across sources.

    ``ipa_narrow`` is scored: it matches the transcription depth of the
    o2i pt specs and of the previous gold (explicit [ɐ ɨ ɾ ʀ ɫ]).
    Untagged plain-"pt" rows are excluded from every regional row: they are
    the pan-Portuguese subset and would dilute regional contrasts. See
    ``_PT_UNIFIED_REGIONS`` for the spec -> region mapping.

    PROVENANCE — classified ``lexicon-derived``: the bulk of the rows come
    from published-dictionary extractions (Infopedia) and the Portal's
    semi-automated lexicon; the Wiktionary minority is crowd-scraped. Both
    tiers may gate regressions, so the mixed classification is safe (only
    competitor-derived/LLM tiers are exempt from gating).

    SAMPLING — the file is grouped by word, so the first ``limit`` lines
    would be a biased alphabetical slice; the whole file is read and a
    fixed-seed (``SAMPLE_SEED``) random sample of up to ``limit`` WORDS is
    drawn, keeping all of a sampled word's variants for the chosen region.
    """
    region = _PT_UNIFIED_REGIONS[lang]
    text = _fetch(_PT_UNIFIED_URL, "portuguese_pronunciation_lexicon.jsonl")
    by_word: Dict[str, List[str]] = {}
    for line in text.strip().splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("region") != region:
            continue
        word = row.get("word")
        ipa = (row.get("ipa_narrow") or "").strip()
        if not word or not ipa:
            continue
        by_word.setdefault(word, []).append(ipa)
    words = sorted(by_word.items())
    rng = random.Random(SAMPLE_SEED)
    rng.shuffle(words)
    pairs: List[Tuple[str, str]] = []
    for word, variants in words[:limit]:
        for ipa in dict.fromkeys(variants):
            pairs.append((word, ipa))
    return pairs


def load_vox_communis(lang: str, limit: int) -> List[Tuple[str, str]]:
    """VoxCommunis parallel G2P pairs (fdemelo/vox-communis-parallel-g2p on
    Hugging Face, CC0): Common Voice utterances force-aligned by the
    VoxCommunis Corpus, with per-utterance phone strings whose lexicons came
    from Epitran, the XPF Corpus, Charsiu and custom dictionaries (manually
    corrected in part). One small TSV per language (~hundreds of rows).

    The ``phonemized_sentence`` column is space-separated phones with ``|``
    between words, aligned with the whitespace-tokenized
    ``aligned_sentence``; rows are split into word-level (word, IPA) pairs
    the same way ``load_ipa_childes`` does, skipping rows whose token counts
    do not match. Alignment artifacts (underscores, stray apostrophes) are
    stripped from the phone side.

    ``spn`` TOKENS ARE DROPPED. ``spn`` is the Montreal Forced Aligner's
    "spoken noise" symbol, which the VoxCommunis pipeline also emits for any
    word its lexicon could not cover: the phone tier records the literal
    three-character string ``spn`` in place of that word's phones. It is a
    coverage hole marker, not a transcription. Scoring it as gold is not
    merely noisy, it is unbounded: PER is normalised by the GOLD length, so
    a real 10-segment word scored against the 3-character ``spn`` yields a
    per-word PER above 3. Whole languages were driven past PER 1.0 by this
    alone (``ab`` 46.5% of tokens ``spn``, ``kk`` 59.4%, ``cv`` 31.3%,
    ``ba`` 15.1%, ``it`` 12.5%, ``sr`` 9.6% — measured over the cached
    TSVs, 2026-08). Dropping the token is the only honest reading: the
    dataset is telling us it has no gold for that word.

    ``spn`` is the ONLY token filtered. The obvious siblings do occur in
    these files, but as genuine transcriptions of real words — Welsh
    ``sul`` → /sil/ (336 rows), Amharic ``ሲል``, Bulgarian ``сп``, Tamil
    ``ஸ்ப்``, Korean ``실``, Punjabi ``ਸੀਲ`` — so filtering on the phone
    string would delete real gold. See ``_VOX_COMMUNIS_NON_SPEECH`` for
    the 61 identity rows (word and phones both ``sil``/``sp``) that are
    also left alone, and why.

    PROVENANCE — classified ``epitran-derived`` (the competitor tier): the
    phone tier's lexicons are built with Epitran — a scored competitor in
    docs/comparison.md — alongside XPF/Charsiu, so a disagreement here
    measures divergence from a competitor's output. Directional signal
    only; can never gate a regression or a tier promotion.
    """
    fname = _VOX_COMMUNIS_FILES[lang] + ".tsv"
    text = _fetch(_VOX_COMMUNIS_BASE + fname, f"vox_communis_{fname}")
    pairs: List[Tuple[str, str]] = []
    seen = set()
    reader = csv.DictReader(text.splitlines(), delimiter="\t")
    for row in reader:
        sentence = (row.get("aligned_sentence") or "").strip()
        ipa = (row.get("phonemized_sentence") or "").strip()
        if not sentence or not ipa:
            continue
        words = sentence.split()
        phones = ["".join(seg.split()) for seg in ipa.split("|")]
        phones = [p.replace("_", "").replace("'", "") for p in phones]
        if len(words) != len(phones):
            continue
        for word, phone in zip(words, phones):
            word = word.strip(".,;:!?\u00bf\u00a1\"'()")
            if not word or not phone or phone in _VOX_COMMUNIS_NON_SPEECH:
                continue
            key = word.lower()
            if key in seen:
                continue
            seen.add(key)
            pairs.append((word, phone))
            if len(pairs) >= limit:
                return pairs
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


# ─── sentence-level TTS gold (Arabic + Portuguese) ──────────────────────────
#
# Two sibling gold sets of full sentences, one TSV per lect, each row an
# orthographic sentence paired with a hand-written broad IPA transcription.
# They are LLM-authored (see the provenance note on ``arabic_tts`` /
# ``portuguese_tts`` in ``PROVENANCE`` and docs/benchmarks.md): every
# transcription was drafted by a language model, then engine-pinned and
# audited row-by-row against the cited phonological literature recorded in
# each row's ``notes`` column (docs/arabic-tts-gold.md,
# docs/portuguese-tts-gold.md). Citation-audited is not expert-authored, so
# the honest tier is ``llm-generated``: it has no error model and can gate no
# quality decision — a directional signal only.
#
# Both are sentence-level, so the scorer routes each row through
# ``engine.transcribe`` (see ``_is_multiword`` / ``evaluate_words``) and PER
# is computed over the whole sentence under the same normalization
# (stress-stripped, broad) as every other dataset. The lang tag scored under
# each file is simply the file stem (a registered spec code); a test asserts
# every stem resolves.
_ARABIC_TTS_DIR = os.path.join(
    os.path.dirname(__file__), "..", "orthography2ipa", "data", "gold",
    "arabic_tts",
)
_PORTUGUESE_TTS_DIR = os.path.join(
    os.path.dirname(__file__), "..", "orthography2ipa", "data", "gold",
    "portuguese_tts",
)


def _load_sentence_tts(directory: str, lang: str, limit: int) \
        -> List[Tuple[str, str]]:
    """Shared reader for the per-lect sentence-level TTS gold TSVs.

    Each file is ``<lang>.tsv`` with a header row and (at least) a
    ``sentence`` column (the scored input) and an ``ipa`` column (the gold).
    The Arabic files also carry an undiacritized ``raw`` column, which is
    ignored: o2i's Arabic input contract is fully-diacritized text, and the
    ``sentence`` column is the vocalized form. Punctuation carried by the
    sentence is not a phoneme and is stripped from the gold by
    :func:`normalize`.
    """
    path = os.path.join(directory, f"{lang}.tsv")
    pairs: List[Tuple[str, str]] = []
    with open(path, encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for row in reader:
            sentence = (row.get("sentence") or "").strip()
            ipa = (row.get("ipa") or "").strip()
            if not sentence or not ipa:
                continue
            pairs.append((sentence, ipa))
            if len(pairs) >= limit:
                break
    return pairs


def _sentence_tts_langs(directory: str) -> List[str]:
    return sorted(
        os.path.basename(p)[:-4]
        for p in glob.glob(os.path.join(directory, "*.tsv"))
    )


def load_arabic_tts(lang: str, limit: int) -> List[Tuple[str, str]]:
    """Arabic sentence-level TTS gold — one TSV per lect, 20 sentences each
    across 33 Arabic varieties (MSA + regional macro-lects + country/city
    dialects). Vocalized ``sentence`` column in, broad IPA ``ipa`` column as
    gold. LLM-authored, literature-audited: see docs/arabic-tts-gold.md and
    the ``arabic_tts`` provenance note.
    """
    return _load_sentence_tts(_ARABIC_TTS_DIR, lang, limit)


def load_portuguese_tts(lang: str, limit: int) -> List[Tuple[str, str]]:
    """Portuguese sentence-level TTS gold — one TSV per lect across European
    Portuguese standard + regional varieties. ``sentence`` column in, broad
    IPA ``ipa`` column as gold. LLM-authored, literature-audited: see
    docs/portuguese-tts-gold.md and the ``portuguese_tts`` provenance note.
    """
    return _load_sentence_tts(_PORTUGUESE_TTS_DIR, lang, limit)


_ARABIC_TTS_LANGS = _sentence_tts_langs(_ARABIC_TTS_DIR)
_PORTUGUESE_TTS_LANGS = _sentence_tts_langs(_PORTUGUESE_TTS_DIR)


# ─── gold20 — Salesteq/arabic-dialects-gold20 (Hugging Face) ────────────────
#
# A SIBLING gold set to ``arabic_tts`` above, published upstream as
# ``Salesteq/arabic-dialects-gold20`` on Hugging Face: 33 lects × 20
# sentences, same shape (vocalized ``sentence`` in, broad ``ipa`` gold),
# plus extra columns (``ipa_o2i`` engine draft, ``features``,
# ``fable_corrections``, ``verification``, ``judge_agreement``) this loader
# does not need and ignores. It is registered SEPARATELY, fetched at
# runtime (never vendored) and cached under CACHE_DIR, because the
# maintainer asked for this specific published dataset by URL — it is not a
# vendored copy of ``arabic_tts``, whose local TSVs have since been hand
# re-audited and diverge from the upstream file row-by-row (see e.g. the
# ar-EG-020 delta note in ``orthography2ipa/data/gold/arabic_tts/ar-EG.tsv``).
#
# PROVENANCE — semi-synthetic: every ``sentence``/``ipa`` pair was drafted
# by an LLM (the same Claude lineage that authored the o2i Arabic dialect
# specs this scores against — a near-circular relationship), then
# spot-checked by a native Arabic speaker who judged the set good. That
# spot-check is documented context, not a tier upgrade: there is still no
# lexicon and no rule system behind the gold, so a disagreement cannot be
# attributed to anything. Tier stays ``llm-generated`` — the same, lowest
# tier as ``arabic_tts``/``portuguese_tts``/``barranquenho_dict``/
# ``mirandese_dict``. It gates nothing and certifies nothing. It is
# registered anyway because for most of these Arabic dialects no other gold
# exists at all: this is better than the alternative of no signal, not
# because it clears any quality bar.
_GOLD20_ARABIC_BASE = (
    "https://huggingface.co/datasets/Salesteq/arabic-dialects-gold20"
    "/resolve/main/{lang}.tsv"
)
# Upstream file stems that are already valid orthography2ipa lect codes
# (verified 1:1 against orthography2ipa/data/*.json — every file here has a
# matching registered spec; nothing was force-mapped and nothing was
# rejected).
_GOLD20_ARABIC_LANGS = sorted([
    "ar", "arb",
    "ar-AE", "ar-BH", "ar-DZ", "ar-EG", "ar-IQ", "ar-IQ-x-qeltu", "ar-JO",
    "ar-KW", "ar-LB", "ar-LY", "ar-MA", "ar-MR", "ar-NG", "ar-OM", "ar-PS",
    "ar-QA", "ar-SA-x-hejaz", "ar-SA-x-najd", "ar-SA-x-qassim",
    "ar-SA-x-rijal-alma", "ar-SA-x-sharqiyya", "ar-SD", "ar-SY", "ar-TD",
    "ar-TN", "ar-YE",
    "ar-x-gulf", "ar-x-levantine", "ar-x-maghrebi", "ar-x-mashriqi",
    "ar-x-peninsular",
])


def load_gold20_arabic(lang: str, limit: int) -> List[Tuple[str, str]]:
    """Salesteq/arabic-dialects-gold20 (Hugging Face) — one TSV per lect, 20
    sentences each, 33 Arabic varieties. Vocalized ``sentence`` column in,
    broad IPA ``ipa`` column as gold; the ``ipa_o2i``/``features``/
    ``fable_corrections``/``verification``/``judge_agreement`` columns are
    ignored by the harness. Semi-synthetic (LLM-drafted by the same Claude
    lineage that authored the o2i Arabic dialect specs), spot-checked good by
    a native Arabic speaker; registered because for most of these dialects no
    other gold exists at all. See the ``gold20_arabic`` provenance note:
    ``llm-generated``, gates no quality decision.
    """
    fname = f"{lang}.tsv"
    text = _fetch(_GOLD20_ARABIC_BASE.format(lang=lang), f"gold20_arabic_{fname}")
    pairs: List[Tuple[str, str]] = []
    reader = csv.DictReader(text.splitlines(), delimiter="\t")
    for row in reader:
        sentence = (row.get("sentence") or "").strip()
        ipa = (row.get("ipa") or "").strip()
        if not sentence or not ipa:
            continue
        pairs.append((sentence, ipa))
        if len(pairs) >= limit:
            break
    return pairs


_PRIMARY_SOURCES_DIR = os.path.join(
    os.path.dirname(__file__), "..", "orthography2ipa", "data", "gold",
    "primary_sources",
)
_PRIMARY_SOURCES_ROWS = os.path.join(_PRIMARY_SOURCES_DIR, "rows.jsonl")


def read_primary_source_rows() -> List[Dict[str, object]]:
    """Every row of the primary-source gold, unfiltered.

    Rows carry their full provenance (source id, printed page, the source's
    own notation, broad/narrow, confidence); the benchmark loader below
    projects them down to the (word, ipa) pairs the harness scores, and the
    tests use this richer view.
    """
    rows: List[Dict[str, object]] = []
    with open(_PRIMARY_SOURCES_ROWS, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def load_primary_sources(lang: str, limit: int) -> List[Tuple[str, str]]:
    """Example transcriptions mined from the PRIMARY SOURCES the language
    specs themselves cite (grammars, phonology monographs, theses).

    Each row is one worked example printed by the linguist who described the
    variety — the orthographic form, the IPA as that source wrote it, and the
    printed page it came from. See the dataset README for the per-source row
    counts, the notation-normalization decisions, and the rows where a source
    contradicts a spec.

    The scored input word is the vocalized orthography where the row has one
    (Arabic: o2i's input contract is fully-diacritized text, and the sources
    print their examples in transcription, so the ḥarakāt are editor-supplied
    and flagged as such per row), otherwise the orthography as printed.
    """
    pairs: List[Tuple[str, str]] = []
    for row in read_primary_source_rows():
        if row.get("lang") != lang:
            continue
        word = row.get("orthography_vocalized") or row.get("orthography")
        ipa = row.get("ipa")
        if not word or not ipa:
            continue
        pairs.append((str(word), str(ipa)))
        if len(pairs) >= limit:
            break
    return pairs


def _primary_source_langs() -> List[str]:
    return sorted({
        str(row["lang"]) for row in read_primary_source_rows() if row.get("lang")
    })


# ─── alphacep/biggest-ru-book-cleanup (Russian) ────────────────────────────
#
# Notation: a Latin-letter segment code per Russian phoneme. Plain
# consonants are the code letter itself; a trailing ``j`` on a consonant
# marks palatalization (``tj`` = /tʲ/); vowels carry a trailing stress digit
# (``1`` = stressed, ``0`` = unstressed). Enumerated exhaustively over the
# cached ``dev`` split (1291 rows, 314 raw segment tokens before
# stripping, 48 distinct phoneme codes once trailing sentence punctuation
# is stripped from word/segment-group edges the same way
# ``load_vox_communis`` strips it) — every code below is one of those 48;
# none were guessed.
_ALPHACEP_RU_CONSONANTS: Dict[str, str] = {
    "b": "b", "c": "t͡s", "ch": "t͡ɕ", "d": "d", "f": "f", "g": "ɡ",
    "h": "x", "k": "k", "l": "ɫ", "m": "m", "n": "n", "p": "p", "r": "r",
    "s": "s", "sch": "ɕː", "sh": "ʂ", "t": "t", "v": "v", "z": "z",
    "zh": "ʐ", "j": "j",
}
_ALPHACEP_RU_VOWELS: Dict[str, str] = {
    "a": "a", "e": "e", "i": "i", "o": "o", "u": "u", "y": "ɨ",
}
#: Palatalization on ``ch``/``sch``/``zh``/``sh`` is not marked with a
#: trailing ``j`` in the source data (they are inherently soft/hard in
#: Russian and the annotation does not append ``j`` to them) — only the
#: single-letter and ``j``-final codes below take the ``Cj`` softening
#: pattern, confirmed against the segment inventory (``sch``, ``sh``, ``zh``
#: never co-occur with a trailing extra ``j``).
_ALPHACEP_RU_PALATALIZABLE = frozenset("bdfghklmnprstvz")

#: ``l`` is the one consonant whose palatalized counterpart is not the
#: plain IPA symbol plus ``ʲ``: Russian hard /ɫ/ (velarized "dark" l) and
#: soft /lʲ/ are two distinct places of articulation, not the same
#: consonant with an added secondary articulation — ``lj`` -> ``ɫʲ`` would
#: notate a velarized-AND-palatalized lateral that does not occur in
#: Russian. Every other ``Cj`` code keeps the generic base-IPA + ``ʲ``
#: rule.
_ALPHACEP_RU_PALATALIZED_OVERRIDES: Dict[str, str] = {"l": "lʲ"}

#: Punctuation the source data glues onto the edge of a word's phone group
#: (sentence punctuation, quotes, parens) — none of it is a phoneme.
_ALPHACEP_RU_PUNCT = ".,;:!?¡¿\"'()«»…-—:"


def _alphacep_ru_strip_punct(token: str) -> str:
    return token.strip(_ALPHACEP_RU_PUNCT)


def _alphacep_ru_segment_to_ipa(seg: str) -> Optional[str]:
    """Map one underscore-delimited segment code to IPA, or ``None`` if the
    segment is punctuation left over after group-level stripping (a stray
    quote/dash glued to an interior segment by the source annotation)."""
    seg = _alphacep_ru_strip_punct(seg)
    if not seg:
        return None
    if seg[-1].isdigit():
        base, stress = seg[:-1], seg[-1]
        ipa = _ALPHACEP_RU_VOWELS.get(base)
        if ipa is None:
            return None
        return ("ˈ" if stress == "1" else "") + ipa
    if (len(seg) >= 2 and seg[-1] == "j"
            and seg[:-1] in _ALPHACEP_RU_PALATALIZABLE):
        base = seg[:-1]
        override = _ALPHACEP_RU_PALATALIZED_OVERRIDES.get(base)
        if override is not None:
            return override
        base_ipa = _ALPHACEP_RU_CONSONANTS.get(base)
        if base_ipa is None:
            return None
        return base_ipa + "ʲ"
    return _ALPHACEP_RU_CONSONANTS.get(seg)


def load_alphacep_ru_book(lang: str, limit: int) -> List[Tuple[str, str]]:
    """alphacep/biggest-ru-book-cleanup (Hugging Face, dataset repo): a
    cleaned phone-level re-annotation of its5Q/biggest-ru-book (Russian
    audiobook TTS data). Rows are ``wav|sentence|phones``, where ``phones``
    is one underscore-joined segment group per whitespace-tokenized
    ``sentence`` word — rows are split into word-level (word, IPA) pairs the
    same way ``load_vox_communis`` does; a row whose word/group counts do
    not match is guarded against and skipped, though the cached ``dev``
    split has none. Only the cached ``dev`` split is read (fetched via
    ``huggingface_hub.hf_hub_download``, which resolves from the local HF
    cache and does not re-download a file already present there).

    PRODUCTION METHOD — this gold is MORPHOPHONEMIC / accentuator-driven,
    not a surface-phonetic transcription: it is grapheme-faithful (no
    vowel reduction — unstressed vowels keep their full quality, e.g.
    молчал → m_o0_l_ch_a1_l with an unreduced [o], never akanje [ɐ]/[ə]) and
    it writes genitive-ending ⟨г⟩ as [g] rather than the spoken [v]
    (298/300 его-suffix rows checked carry [g], confirming this is a fixed
    orthography-driven rule of the annotation pipeline, not a transcription
    error). o2i's Russian output is surface-phonetic (it reduces unstressed
    vowels and realizes genitive ⟨г⟩ as [v]), so PER against this gold will
    show systematic, EXPECTED disagreement on exactly those two phenomena —
    that is a notation mismatch between two legitimate conventions, not a
    model error, and it must not be "fixed" by adding akanje/г-devoicing
    exceptions to o2i to chase this one gold's convention.

    PROVENANCE — classified ``machine-generated``: the phone tier is an
    automatic accentuator/G2P annotation over its5Q/biggest-ru-book, not a
    hand-transcribed or lexicon-derived gold. Directional signal only; see
    ``docs/quality_tiers.md`` — this tier cannot gate a promotion.
    """
    if lang != "ru":
        return []
    from huggingface_hub import hf_hub_download
    path = hf_hub_download(
        repo_id="alphacep/biggest-ru-book-cleanup",
        filename="metadata-phones-ids.csv.dev",
        repo_type="dataset",
    )
    pairs: List[Tuple[str, str]] = []
    seen = set()
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.rstrip("\n")
            parts = line.split("|")
            if len(parts) < 3:
                continue
            sentence, phones_field = parts[1], parts[2]
            words = sentence.split()
            groups = phones_field.split()
            if len(words) != len(groups):
                continue
            for word, group in zip(words, groups):
                word = _alphacep_ru_strip_punct(word)
                if not word:
                    continue
                ipa_segs = [_alphacep_ru_segment_to_ipa(seg)
                            for seg in group.split("_")]
                ipa_segs = [s for s in ipa_segs if s]
                if not ipa_segs:
                    continue
                ipa = "".join(ipa_segs)
                key = word.lower()
                if key in seen:
                    continue
                seen.add(key)
                pairs.append((word, ipa))
                if len(pairs) >= limit:
                    return pairs
    return pairs


# ─── CoRuSS phonetic dictionary (Russian) ──────────────────────────────────
#
# Notation: the SPbU lab's own ASCII scheme, described by the corpus site as
# "analogous to the SAMPA set" but NOT X-SAMPA — the two disagree on most of
# the symbols that matter here (``Q`` is /ɨ/ not /ɒ/, ``C`` is /t͡ɕ/ not /ç/,
# ``D`` is voiced ⟨ц⟩ not /ð/, ``G`` is voiced ⟨ч⟩ not /ɣ/, ``h`` is /ɣ/ not
# /h/, ``I`` is a vowel-context diacritic not /ɪ/, and ``:`` marks a
# palatal environment rather than length). Running it through
# ``scriptconv.notation.xsampa_to_ipa`` would therefore mistranscribe the
# majority of its distinctive symbols, so the tables below are the corpus's
# own documented set, transcribed from the conventions page
# (https://russpeech.spbu.ru/transkrip.htm) and checked to cover every
# symbol that actually occurs in the archive.
#
# Vowels are written as a base letter plus up to three optional context
# diacritics, in this order: ``:`` after or between palatalized consonants,
# ``I`` before a palatalized consonant, ``#`` excessive duration. Consonants
# are their Latin transliteration plus an optional ``'`` for palatalization
# and an optional ``#``.
_CORUSS_VOWELS: Dict[str, str] = {
    "a": "a", "o": "o", "e": "ɛ", "i": "i", "u": "u", "Q": "ɨ", "@": "ə",
}
#: The ``:`` diacritic is a COARTICULATION mark, not a phoneme distinction,
#: for every vowel but ⟨э⟩: a fronted [ä]/[ö]/[ʉ] after a soft consonant is
#: the same phoneme as its plain counterpart and o2i does not notate the
#: fronting, so writing it into the gold would charge every soft-consonant
#: vowel token as an error. ⟨э⟩ is the exception, because the hard/soft
#: split there is the [ɛ] ~ [e] distinction o2i's own Russian inventory
#: makes (⟨это⟩ ˈɛtə vs ⟨лес⟩ ˈlʲes). ``I`` and ``#`` carry no phoneme
#: distinction at all and are dropped from every vowel.
_CORUSS_VOWELS_AFTER_SOFT: Dict[str, str] = {"e": "e"}
_CORUSS_CONSONANTS: Dict[str, str] = {
    "b": "b", "p": "p", "d": "d", "t": "t", "k": "k", "g": "ɡ", "f": "f",
    "v": "v", "s": "s", "z": "z", "m": "m", "n": "n", "r": "r", "j": "j",
    "l": "ɫ", "x": "x", "h": "ɣ", "c": "t͡s", "D": "d͡z", "C": "t͡ɕ",
    "G": "d͡ʑ", "S": "ʂ", "Z": "ʐ", "$": "ɕː",
}
#: Consonants that take the ``C'`` palatalization mark. The conventions
#: page is the criterion for what a symbol means, so ``c'``, ``S'`` and
#: ``C'`` (19 occurrences between them) are rejected as annotation slips:
#: ⟨ц ш ч⟩ are unpaired for palatalization in Russian, the page gives them
#: no palatalized form, and there is nothing to map them to that would not
#: be a guess. ``Z'`` goes the other way for the same reason — the page
#: DOES define it, as the voiced counterpart of ⟨щ⟩ — so it is honoured;
#: see _CORUSS_PALATALIZED_OVERRIDES.
_CORUSS_PALATALIZABLE = frozenset("bpdtkgfvszmnrlx")
#: Hard ⟨л⟩ is velarized /ɫ/ and soft ⟨ль⟩ is /lʲ/ — two distinct Russian
#: consonants, not one consonant plus a secondary articulation, so ``l'``
#: cannot go through the generic base + ``ʲ`` rule (``ɫʲ`` is not a Russian
#: segment). Same reasoning as ``load_alphacep_ru_book``.
#:
#: ``Z'`` takes the value the conventions page assigns it, voiced ⟨щ⟩
#: /ʑː/, rather than the palatalized ⟨ж⟩ its shape suggests (/ʐʲ/ is not a
#: Russian segment either way). Worth knowing about the gold: all 16 rows
#: that use it spell ⟨ж⟩ or ⟨з⟩ and none spell ⟨щ⟩. Three of them —
#: ⟨выезжать⟩, ⟨приезжай⟩, ⟨дождём⟩ — are the genuine old-Moscow long soft
#: /ʑː/ for ⟨зж⟩/⟨жд⟩; the rest (⟨живёт⟩, ⟨даже⟩, ⟨ружья⟩, ⟨ежедневно⟩ …)
#: are annotator readings that standard Russian would write with plain
#: /ʐ/. That is a property of this gold, recorded rather than corrected:
#: the loader's job is fidelity to the documented convention, and at ~0.1%
#: of rows it is far below the noise floor of a 0.35 PER anyway.
_CORUSS_PALATALIZED_OVERRIDES: Dict[str, str] = {"l": "lʲ", "Z": "ʑː"}

#: ``  word [transcription]  count`` — the per-file trailing tally line
#: (``1981/0``) has no bracket and simply fails to match.
_CORUSS_ROW = re.compile(r"^\s*(\S+)\s+\[([^\]]*)\]\s*\d*\s*$")
_CORUSS_CYRILLIC = frozenset("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
_CORUSS_VOWEL_LETTERS = frozenset("аеёиоуыэюя")


def _coruss_to_ipa(trans: str) -> Optional[str]:
    """Map one CoRuSS transcription to IPA, or ``None`` if it contains a
    symbol the conventions page does not define (annotation slips: stray
    ``+``, Latin ``O``/``U``/``V``/``w``, punctuation, single Cyrillic
    letters typed into the Latin field). Undefined symbols reject the whole
    row rather than being dropped from it — a silently shortened reference
    would score as a deletion error against a correct hypothesis."""
    out: List[str] = []
    i, n = 0, len(trans)
    while i < n:
        ch = trans[i]
        # Round brackets mark a weakly realized segment the annotator still
        # heard (⟨Брежнев⟩ [br'e:Zn'e:(f)] — a devoiced but present final
        # stop). The segment is real; only the bracket is notation.
        if ch in "()":
            i += 1
            continue
        if ch in _CORUSS_VOWELS:
            j = i + 1
            after_soft = j < n and trans[j] == ":"
            j += after_soft
            j += j < n and trans[j] == "I"
            j += j < n and trans[j] == "#"
            out.append(_CORUSS_VOWELS_AFTER_SOFT[ch] if after_soft
                       and ch in _CORUSS_VOWELS_AFTER_SOFT
                       else _CORUSS_VOWELS[ch])
            i = j
            continue
        if ch in _CORUSS_CONSONANTS:
            j = i + 1
            if j < n and trans[j] == "'":
                override = _CORUSS_PALATALIZED_OVERRIDES.get(ch)
                if override is None and ch not in _CORUSS_PALATALIZABLE:
                    return None
                out.append(override or _CORUSS_CONSONANTS[ch] + "ʲ")
                j += 1
            else:
                out.append(_CORUSS_CONSONANTS[ch])
            j += j < n and trans[j] == "#"
            i = j
            continue
        return None
    return "".join(out) or None


def _coruss_anchor_stress(word: str, ipa: str) -> str:
    """Move the orthographic stress mark onto the IPA.

    CoRuSS marks stress on the ORTHOGRAPHIC side only — ``+`` follows the
    stressed vowel letter — and leaves the transcription unmarked, so the
    mark has to be re-anchored to be comparable with o2i's ``ˈ``. It is
    placed before the IPA vowel at the same ordinal position as the marked
    orthographic vowel, and only when the two vowel counts agree: this is
    surface-phonetic transcription of colloquial speech, where a vowel is
    often simply gone (⟨Алекса+ндровна⟩ [l'iksan@] has four vowels for
    five letters), and there is no defensible way to say which vowel
    survived. Unanchorable rows keep an unmarked reference; the board
    strips stress from both sides anyway (``--keep-stress`` is off by
    default), so this only affects stress-aware reruns.
    """
    if word.count("+") != 1:
        return ipa
    letters = [c for c in word.lower() if c in _CORUSS_CYRILLIC or c == "+"]
    try:
        rank = sum(1 for c in letters[:letters.index("+")]
                   if c in _CORUSS_VOWEL_LETTERS)
    except ValueError:
        return ipa
    positions = [k for k, c in enumerate(ipa) if is_ipa_vowel(c)]
    if len(positions) != sum(1 for c in letters
                             if c in _CORUSS_VOWEL_LETTERS) or rank < 1:
        return ipa
    cut = positions[rank - 1]
    return ipa[:cut] + "ˈ" + ipa[cut:]


def load_coruss_ru(lang: str, limit: int) -> List[Tuple[str, str]]:
    """CoRuSS phonetic dictionary (Corpus of Russian Colloquial Speech, the
    phonetics lab of Saint Petersburg State University; Kachkovskaia et al.
    2016, "CoRuSS: a corpus of Russian spontaneous speech", LREC).

    The published dictionaries (``slovari.rar``, fetched once into
    ``CACHE_DIR``) hold one ``word [transcription] count`` row per attested
    realization, over three sub-corpora: ``READ`` (read speech), ``MONO``
    (monologues) and ``DICT``. A wordform realized several different ways
    contributes SEVERAL rows, and all of them are kept — the harness scores
    a hypothesis against the best of a word's references, so the corpus's
    pronunciation variation is used as multi-reference gold rather than
    being collapsed to an arbitrary winner.

    Rows are rejected, never patched, when the orthographic side is a
    cross-word coalescence (``если_они``, ``потому=что``: the conventions
    page defines these composite wordforms, and their transcriptions carry
    sandhi a word-level G2P cannot produce), a truncated fragment
    (``Инфо+рм-``), an unreadable legacy encoding (a handful of very
    high-variance filler words), or when the transcription contains a
    symbol the conventions page does not define.

    PRODUCTION METHOD — HUMAN-ANNOTATED and SURFACE-PHONETIC. The lab
    transcribed the acoustic signal directly, explicitly suppressing the
    transcriber's lexical and grammatical knowledge, so a row records what
    a speaker actually said in unscripted conversation, not what a
    dictionary says the word is. Colloquial speech reduces far harder than
    the careful speech behind a pronunciation lexicon: whole syllables
    disappear (⟨Александровна⟩ [l'iksan@], ⟨Волгоград⟩ [vodgrat]), and no
    G2P can or should predict that. PER against this gold is therefore a
    FLOOR on Russian error, and a much higher one than against a
    careful-speech reference — it must be read as the distance to
    spontaneous-speech surface forms, and compared only against other runs
    on this same dataset, never against a lexicon gold's number. Nothing
    here licenses adding reduction rules to o2i to close that gap: the
    variation is speaker- and context-specific, and fitting it would be
    gold-fitting.

    PROVENANCE — ``expert-human``: expert phonetic transcription by a
    university phonetics lab, from audio, with no engine in the loop.
    """
    if lang != "ru":
        return []
    import rarfile  # optional; skip the row when unavailable
    archive = _fetch_file(
        "https://russpeech.spbu.ru/SLOVARI/slovari.rar", "coruss_slovari.rar")
    pairs: List[Tuple[str, str]] = []
    seen = set()
    with rarfile.RarFile(archive) as rf:
        for name in sorted(n for n in rf.namelist() if not n.endswith("/")):
            text = rf.read(name).decode("cp1251", errors="replace")
            for line in text.splitlines():
                row = _CORUSS_ROW.match(line)
                if row is None:
                    continue
                word, trans = row.group(1), row.group(2)
                # ``^`` marks a secondary-stress vowel and is not part of
                # the spelling; ``+`` is kept for stress anchoring below.
                word = word.replace("^", "")
                if ("_" in word or "=" in word or word.endswith("-")
                        or word.startswith("-")):
                    continue
                spelling = word.replace("+", "").replace("-", "")
                if not spelling or not all(c in _CORUSS_CYRILLIC
                                           for c in spelling.lower()):
                    continue
                ipa = _coruss_to_ipa(trans)
                if ipa is None:
                    continue
                ipa = _coruss_anchor_stress(word, ipa)
                word = word.replace("+", "")
                if (word, ipa) in seen:
                    continue
                seen.add((word, ipa))
                pairs.append((word, ipa))
                if len(pairs) >= limit:
                    return pairs
    return pairs


#: A dataset loader: ``loader(lang, limit) -> [GoldPair, ...]``. ``limit``
#: is a row cap (``sys.maxsize`` for "no cap"); a loader that cannot serve
#: *lang* returns an empty list rather than raising.
DatasetLoader = Callable[[str, int], List[GoldPair]]

#: THE dataset registry: ``{name: (loader, [language, ...])}``. Every gold
#: set the harness can score is reachable from here and nowhere else — the
#: CLI's ``--dataset`` choices, ``build_scoreboard``'s sweep, and
#: ``compare_systems.LANGS``' dataset references all read this one table, so
#: registering a loader here is the whole job of adding a dataset. Every
#: entry must also have a ``PROVENANCE`` tier (enforced below): a gold with
#: no recorded provenance cannot be read honestly.
DATASETS: Dict[str, Tuple[DatasetLoader, List[str]]] = {
    "primary_sources": (load_primary_sources, _primary_source_langs()),
    "arabic_tts": (load_arabic_tts, _ARABIC_TTS_LANGS),
    "gold20_arabic": (load_gold20_arabic, _GOLD20_ARABIC_LANGS),
    "portuguese_tts": (load_portuguese_tts, _PORTUGUESE_TTS_LANGS),
    "ep_dialects": (load_ep_dialects, _EP_DIALECT_LANGS),
    "wikipron": (load_wikipron, sorted(_WIKIPRON_FILES)),
    "wikipron_ar_diacritized": (load_wikipron_ar_diacritized, ["ar"]),
    "mirandese_g2p": (load_mirandese, sorted(_MIRANDESE_DIALECTS)),
    "barranquenho_dict": (load_barranquenho_dict, ["ext-PT-x-barrancos"]),
    "mirandese_dict": (load_mirandese_dict, sorted(_MIRANDESE_DICT_DIALECTS)),
    "portuguese_unified": (load_portuguese_unified, sorted(_PT_UNIFIED_REGIONS)),
    "4catac": (load_4catac, sorted(_4CATAC_FILES)),
    "hitz_basque_ipa": (load_hitz_basque, ["eu"]),
    "clup_dialect": (load_clup_dialect, _CLUP_LANGS),
    "cmudict": (load_cmudict, ["en-US"]),
    "ipadict": (load_ipadict, sorted(_IPADICT_FILES)),
    "ipa_childes": (load_ipa_childes, sorted(_IPA_CHILDES_FOLDERS)),
    "vox_communis": (load_vox_communis, sorted(_VOX_COMMUNIS_FILES)),
    "ipa_babylm": (load_ipa_babylm, ["en-US"]),
    "northeuralex": (load_northeuralex, sorted(_NORTHEURALEX_LANGS)),
    "wold": (load_wold, sorted(_WOLD_LANGS)),
    "kaikki": (load_kaikki, sorted(_KAIKKI_LANGS)),
    "alphacep_ru_book": (load_alphacep_ru_book, ["ru"]),
    "coruss_ru": (load_coruss_ru, ["ru"]),
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
    # The transcriptions are the published examples of the phonologists and
    # dialectologists the specs cite — the most authoritative gold in the
    # harness, and the only one whose every row names the page it came from.
    # Still small-n, still bound by each source's own conventions (and by the
    # editor-supplied Arabic ḥarakāt: see the dataset README), so it diagnoses
    # rules rather than certifying a language on its own.
    "primary_sources": "expert-human",
    # Arabic + Portuguese sentence-level TTS gold. LLM-authored: every IPA
    # transcription was drafted by a large language model, then engine-pinned
    # and audited row-by-row against the phonological literature cited in each
    # row's `notes` column (docs/arabic-tts-gold.md, docs/portuguese-tts-gold.md).
    # Citation-auditing raises confidence but does NOT change the error model:
    # there is still no lexicon, no G2P, no rule system behind the gold, so a
    # disagreement cannot be attributed to anything. The honest tier is
    # `llm-generated` (never `expert-human`) — directional signal only, gates
    # no quality decision (docs/quality_tiers.md).
    "arabic_tts": "llm-generated",
    "gold20_arabic": "llm-generated",   # Salesteq/arabic-dialects-gold20 (HF):
    # semi-synthetic (same Claude lineage that authored the o2i Arabic dialect
    # specs — near-circular), native-speaker spot-checked but that raises
    # confidence, not tier: no lexicon/rules behind it, so it stays the
    # lowest, non-gating tier, same as its arabic_tts sibling.
    "portuguese_tts": "llm-generated",
    # phonetician / native-speaker / expert-annotator curated IPA
    "ep_dialects": "expert-human",       # TigreGotico team, manual, unvalidated, small-n
    "mirandese_g2p": "expert-human",     # TigreGotico/mirandese_g2p; native-speaker collected; small-n
    "4catac": "expert-human",            # expert annotators, IEC guidelines, consensus review
    "clup_dialect": "expert-human",      # U.Porto CLUP dialect archive; see note (IPA-column provenance undocumented, many rows n=1-17)
    # human lexicographers via dictionary notation conventions
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
    "portuguese_unified": "lexicon-derived",  # Infopedia + Portal lexicon + Wiktionary, convention-normalized
    # SAME crowd-scraped WikiPron ar gold; only the INPUT word is
    # machine-diacritized (text2tashkeel, ~2% DER), which adds a small
    # machine noise floor on top of the gold's own tier. Diagnostic for
    # the vowelized-Arabic rules; certifies nothing beyond the raw row.
    "wikipron_ar_diacritized": "crowd-scraped",
    # Portal da Língua Portuguesa scrape; semi-automated IPA, not hand-verified
    # A COMPETITOR'S OUTPUT reused as a reference. These phonemes come from the
    # espeak-ng-backed phonemizer, so this row measures AGREEMENT WITH ESPEAK,
    # not correctness — and espeak is a system we benchmark ourselves *against*
    # (docs/comparison.md). Diverging from it can mean we are right and it is
    # wrong, which would show here as a *worse* score. Quality also varies by
    # language. Never gate a quality decision on this row; judge any divergence
    # against a cited source instead. Kept because it is broad coverage and a
    # useful directional signal.
    # IPA-BabyLM: G2P+ (github.com/codebyzeb/g2p-plus) with the `phonemizer`
    # backend, language en-us — i.e. espeak-ng output. espeak output can
    # never qualify or block a spec: a disagreement measures divergence
    # from espeak, which may be exactly what the cited source demands.
    "ipa_babylm": "espeak-derived",
    # VoxCommunis lexicons are built with Epitran (a scored competitor),
    # XPF and Charsiu; partially hand-corrected, but not attributably so.
    "vox_communis": "epitran-derived",
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
    # Lexibank/CLDF wordlists: every row is compiled from, and cites, a
    # published source dictionary (the CLDF `Source` column) — human
    # lexicographers via a published notation, the same class of gold as
    # `cmudict`/`portuguese_unified`, not a phonemizer's own output.
    "northeuralex": "lexicon-derived",  # Dellert et al. 2020, NorthEuraLex
    "wold": "lexicon-derived",          # Haspelmath & Tadmor 2009, WOLD
    "kaikki": "crowd-scraped",          # kaikki.org Wiktextract (Wiktionary)
    # alphacep/biggest-ru-book-cleanup: automatic accentuator/G2P annotation
    # over its5Q/biggest-ru-book, not hand-transcribed or lexicon-derived.
    # Also morphophonemic (no vowel reduction, ⟨г⟩=[g]) rather than
    # surface-phonetic — see load_alphacep_ru_book's docstring.
    "alphacep_ru_book": "machine-generated",
    # CoRuSS: expert phonetic transcription of recorded speech by the SPbU
    # phonetics lab, no engine in the loop. Surface-phonetic and
    # colloquial, so its PER floor is far above a careful-speech gold's --
    # see load_coruss_ru's docstring.
    "coruss_ru": "expert-human",
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

#: Affricates whose long form doubles the FIRST element in doubled-letter
#: notation (Italian convention): [tʃː] and [ttʃ] are the same phoneme.
_AFFRICATE_LENGTH = {
    "tʃː": "ttʃ", "dʒː": "ddʒ", "tsː": "tts", "dzː": "ddz",
    "tɕː": "ttɕ", "dʑː": "ddʑ", "tʂː": "ttʂ", "dʐː": "ddʐ",
}


def _expand_consonant_length(s: str) -> str:
    """Canonicalize CONSONANT length to doubled-letter notation.

    [lː] and [ll] are the same phoneme string — two transcription
    conventions, not two pronunciations — so both sides score in one
    notation. Affricates double their first element ([tʃː] → [ttʃ]).
    VOWEL length is untouched: it is phonemic and single-notation
    (Finnish [aː] never appears as [aa] in the wired gold sets).
    """
    for long, doubled in _AFFRICATE_LENGTH.items():
        s = s.replace(long, doubled)
    out = []
    for i, ch in enumerate(s):
        if ch == "ː" and i > 0 and not is_ipa_vowel(s[i - 1]):
            out.append(s[i - 1])
        else:
            out.append(ch)
    return "".join(out)


def _prosody_marks(lang: str) -> str:
    """Extra per-language suprasegmental marks PER must not score.

    A spec that declares ``stress.accent2_mark`` (Scandinavian pitch accent)
    makes ¹/² prosody for that language, unscored on both sides — exactly
    like the universal stress marks. For every other language the digits are
    left alone (they are lexical tone in e.g. Yi gold).
    """
    try:
        from orthography2ipa import get
        st = get(lang).stress
    except Exception:
        return ""
    if st is not None and st.accent2_mark:
        return "¹²"
    return ""


def normalize(ipa: str, strip_stress: bool, broad: bool,
              extra_strip: str = "") -> str:
    s = unicodedata.normalize("NFC", ipa)
    for ch in extra_strip:
        s = s.replace(ch, "")
    s = s.replace("g", "ɡ")  # ASCII/IPA confusable fold — see _NARROW_MARKS comment
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
    for alt, canon in _NOTATIONAL_LETTER_ALIASES.items():
        s = s.replace(alt, canon)
    s = _expand_consonant_length(s)
    if broad:
        decomposed = unicodedata.normalize("NFD", s)
        s = unicodedata.normalize(
            "NFC", "".join(c for c in decomposed if c not in _NARROW_MARKS))
    # comparison is segmentation-free: some gold sets space-separate phonemes
    s = "".join(s.split())
    # Click-accompaniment superscript fold runs AFTER the whitespace join:
    # some gold sets space-separate phonemes, putting the modifier and its
    # click letter on opposite sides of a space (e.g. "ᵑ ǂ"), which must
    # still fold. Combining marks on the modifier (e.g. a combining ring
    # below for voicelessness, ᵑ̊) ride along with it via \1.
    for mod, letter in _CLICK_ACCOMPANIMENT_SUPERSCRIPTS.items():
        s = re.sub(mod + "([̀-ͯ]*)(?=[" + _CLICK_LETTERS + "])",
                   letter + r"\1", s)
    return s


def _is_multiword(entry: str) -> bool:
    """True if *entry* is a phrase/sentence rather than a single word.

    Whitespace is the signal: a gold set is either word-level (WikiPron,
    CMUdict, vox_communis) or sentence-level (4catac, the TTS gold
    sets), and the scorer must call the matching engine API for each.
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


#: Top-k cut-offs the oracle metric reports. ``1`` is computed too, purely
#: as a self-check: oracle@1 must equal the 1-best PER. That identity is
#: NOT guaranteed by construction — ``transcribe_word`` searches greedily
#: at width 1 while ``word_candidates`` runs a width-``max(k, 8)`` beam,
#: and a wider beam is free to find a cheaper path than the greedy one.
#: The two share every word-final stage, so they agree empirically on
#: every gold set measured; the run VERIFIES it rather than assuming it,
#: and aborts if it ever fails. See :func:`assert_oracle_self_check`.
ORACLE_KS: Tuple[int, ...] = (1, 3, 5)

#: The cut-offs published in the scoreboard row / docs table.
ORACLE_REPORT_KS: Tuple[int, ...] = (3, 5)


class OracleResult:
    """Top-k oracle PER for one dataset/language row.

    **Read this before using any number here.** Oracle PER@k is the
    per-word MINIMUM PER over the engine's top-*k* readings, aggregated
    exactly like the 1-best PER. It is a **lattice-quality diagnostic for
    orthography2ipa only**:

    - The gap ``per - oracle_per[k]`` is *ranking* error: the right
      transcription is inside the beam but is not ranked first, so a
      downstream rescorer (which is what actually consumes our lattice)
      could recover it. That gap is the rescoring headroom.
    - What remains at ``oracle_per[k]`` is *model* error: the right
      transcription is not in the lattice at all, and no amount of
      reranking will find it. Only new rules/data fix that.

    It MUST NEVER be used in a cross-system comparison or any "beats X"
    claim. espeak, epitran and every other system we benchmark against
    emit ONE pronunciation; setting their 1-best against our oracle@k
    would compare k guesses to one and is simply dishonest. This is why
    ``scripts/compare_systems.py`` does not read these fields, and why
    the CI regression gate (``benchmarks/results_ci_sample.json``) stays
    1-best.
    """

    __slots__ = ("oracle_per", "oracle_exact", "fallback_words",
                 "scored_words", "top1_mismatch")

    def __init__(self, oracle_per: Dict[int, float],
                 oracle_exact: Dict[int, float], fallback_words: int,
                 scored_words: int, top1_mismatch: int) -> None:
        #: mean oracle PER keyed by k (k=1 included as the self-check).
        self.oracle_per = oracle_per
        #: fraction of words where some top-k candidate EQUALS a gold,
        #: keyed by k. Read this before saying "the right answer is in
        #: the beam": ``oracle_per`` improving only means a NEARER wrong
        #: answer is in the beam, which is a much weaker statement, and
        #: empirically most of the PER-oracle gain is of that kind.
        self.oracle_exact = oracle_exact
        #: words scored with no candidate list available, so the oracle
        #: fell back to the 1-best hypothesis (sentence-level entries, and
        #: any word whose candidate call raised). Never a crash, always
        #: counted.
        self.fallback_words = fallback_words
        #: words that got a REAL candidate list (covered minus fallback).
        #: Zero means the whole row is fallback and its oracle columns
        #: carry no lattice signal at all — they merely echo the PER.
        self.scored_words = scored_words
        #: words whose candidate 0 did not equal the 1-best hypothesis.
        #: MUST be 0; anything else is an engine bug, not a metric quirk.
        self.top1_mismatch = top1_mismatch

    def __repr__(self) -> str:  # pragma: no cover — debugging aid
        return (f"OracleResult(oracle_per={self.oracle_per!r}, "
                f"oracle_exact={self.oracle_exact!r}, "
                f"fallback_words={self.fallback_words}, "
                f"scored_words={self.scored_words}, "
                f"top1_mismatch={self.top1_mismatch})")


def assert_oracle_self_check(dataset: str, lang: str, per: float,
                             covered: int, oracle: "OracleResult",
                             epsilon: float = 1e-9) -> None:
    """Abort the run if the oracle path and the 1-best path disagree.

    Candidate 0 of ``G2P.word_candidates`` is meant to be exactly what
    ``transcribe_word`` returns, so oracle@1 must equal the PER column.
    If it does not, the oracle columns describe a DIFFERENT engine than
    the PER column beside them, and every ranking-vs-model conclusion
    drawn from the row is wrong.

    This exits non-zero rather than printing a warning: a scoreboard is
    a committed artifact, and a run that writes a corrupted one while
    reporting success is worse than a run that fails. A warning above
    ``exit 0`` is a warning nobody reads.
    """
    problems = []
    if oracle.top1_mismatch:
        problems.append(
            f"{oracle.top1_mismatch}/{covered} words where "
            f"word_candidates()[0] != transcribe_word()")
    delta = abs(oracle.oracle_per.get(1, per) - per)
    if delta > epsilon:
        problems.append(
            f"oracle@1 {oracle.oracle_per[1]:.6f} != PER {per:.6f} "
            f"(delta {delta:.2e} > {epsilon:g})")
    if not problems:
        return
    for problem in problems:
        print(f"ENGINE BUG: {dataset} lang={lang}: {problem}",
              file=sys.stderr)
    sys.exit(
        f"ABORTING: the top-k oracle disagrees with the 1-best path, so "
        f"the scoreboard would be corrupt. Refusing to write it. Fix "
        f"G2P.word_candidates / transcribe_word, or rerun with --no-topk "
        f"to write 1-best columns only.")


def evaluate_words(pairs: Sequence[GoldPair], lang: str, strip_stress: bool,
                   broad: bool
                   ) -> Tuple[int, int, List[float], float, float]:
    """Like :func:`evaluate` but also returns the per-word PER list, so
    callers (e.g. :func:`bootstrap_per_ci`) can resample it. The point
    estimates returned here (``n``, ``covered``, ``per``, ``wer``) are
    computed the exact same way as :func:`evaluate` — byte-identical
    scoreboard numbers.
    """
    n, covered, pers, per, wer, _oracle = evaluate_words_oracle(
        pairs, lang, strip_stress, broad, oracle_ks=())
    return n, covered, pers, per, wer


def evaluate_words_oracle(pairs: Sequence[GoldPair], lang: str,
                          strip_stress: bool, broad: bool,
                          oracle_ks: Sequence[int] = ORACLE_KS,
                          expose_ambiguous_endings: bool = False
                          ) -> Tuple[int, int, List[float], float, float,
                                     Optional["OracleResult"]]:
    """:func:`evaluate_words` plus the top-k oracle PER.

    One scoring loop, one normalization, one distance function: passing
    an empty *oracle_ks* turns the oracle off and the 1-best numbers are
    byte-identical to the pre-oracle harness. Read :class:`OracleResult`
    for what the oracle numbers may and may not be used for.

    ``expose_ambiguous_endings`` defaults to **False**, which is the
    board's convention: injected alternatives stay out of the oracle
    columns (see the ``G2P`` call below). Pass ``True`` only to measure
    the injected movement itself — the separate reachability number that
    docs/benchmarks.md requires to be reported under its own heading and
    never folded into ranking error. It cannot change the 1-best numbers.

    Returns ``(n, covered, pers, per, wer, oracle_or_None)``.
    """
    from orthography2ipa import G2P

    # ``expose_ambiguous_endings=False``: the board's oracle columns are a
    # RANKING diagnostic (``PER - Oracle@k`` is defined as ranking error),
    # and a deliberately injected alternative — a list-valued
    # ``grammatical_endings`` entry — moves that gap by construction, since
    # adding candidates to a beam can only lower an oracle. Scoring with
    # them on would let any spec inflate its own headroom by declaring more
    # alternatives. The injected movement is real and worth reporting, but
    # as REACHABILITY and under its own heading: see docs/benchmarks.md,
    # "Injected alternatives do not count as ranking error". 1-best is
    # identical either way, so the PER columns are unaffected.
    engine = G2P(lang, expose_ambiguous_endings=expose_ambiguous_endings)
    # gold sets may carry several valid transcriptions per word
    # (dialect variants); score against all, keep the best
    refs: Dict[str, List[str]] = {}
    for word, gold in pairs:
        refs.setdefault(word, []).append(gold)

    extra = _prosody_marks(lang)
    pers: List[float] = []
    wrong, covered = 0, 0
    ks = sorted({int(k) for k in oracle_ks})
    oracle_sums: Dict[int, float] = {k: 0.0 for k in ks}
    oracle_exact_counts: Dict[int, int] = {k: 0 for k in ks}
    fallback_words = 0
    top1_mismatch = 0
    for word, golds in refs.items():
        try:
            # Pick the API that matches the entry's granularity. Several gold
            # sets are sentence-level (4catac, the TTS gold sets), and
            # transcribe_word() treats a whole sentence as ONE word: word
            # boundaries vanish, per-word stress collapses to a single mark,
            # and word-final rules (Catalan final-⟨r⟩ deletion, Danish schwa)
            # never fire. That is a harness artifact, not an engine error —
            # it cost Catalan ~7 and English ~16 PER points.
            transcribe = (engine.transcribe if _is_multiword(word)
                          else engine.transcribe_word)
            hyp = normalize(transcribe(word), strip_stress, broad,
                            extra_strip=extra)
        except Exception:
            continue
        if not hyp:
            continue
        covered += 1
        golds_norm = [normalize(x, strip_stress, broad, extra_strip=extra)
                      for x in golds]
        golds_set = set(golds_norm)

        def _score(h: str) -> float:
            """PER of hypothesis *h* against the best of this word's golds."""
            return min(levenshtein(h, g) / max(len(g), 1) for g in golds_norm)

        per = _score(hyp)
        pers.append(per)
        wrong += per > 0

        if ks:
            # Oracle: the same _score, over the engine's top-k readings
            # instead of only its first. Sentence-level gold entries have no
            # word-level candidate list (the beam is per WORD; composing a
            # sentence beam out of word beams would invent a ranking the
            # engine never produces), so they fall back to the 1-best.
            cands: List[str] = []
            if not _is_multiword(word):
                try:
                    cands = [
                        normalize(c, strip_stress, broad, extra_strip=extra)
                        for c in engine.word_candidates(word, k=max(ks))
                    ]
                except Exception:
                    cands = []
            if not cands:
                fallback_words += 1
                cands = [hyp]
            elif cands[0] != hyp:
                # Candidate 0 is meant to BE transcribe_word's answer. If it
                # is not, the two paths disagree and the oracle is measuring
                # a different engine than the 1-best column. Counted, never
                # silently smoothed over.
                top1_mismatch += 1
            best = float("inf")
            hit = False
            for i, k in enumerate(ks):
                lo = ks[i - 1] if i else 0
                for cand in cands[lo:k]:
                    best = min(best, _score(cand))
                    # EXACT oracle: some top-k candidate IS a gold, not
                    # merely closer to one. This is the number that
                    # supports the phrase "the right answer is in the
                    # beam"; the PER oracle only says "a nearer wrong
                    # answer is in the beam", which is a much weaker
                    # claim and empirically the common case.
                    hit = hit or cand in golds_set
                oracle_sums[k] += best
                oracle_exact_counts[k] += hit
    n = len(refs)
    per_sum = sum(pers)
    oracle = None
    if ks:
        oracle = OracleResult(
            oracle_per={k: (oracle_sums[k] / covered if covered else 1.0)
                        for k in ks},
            oracle_exact={k: (oracle_exact_counts[k] / covered
                              if covered else 0.0)
                          for k in ks},
            fallback_words=fallback_words,
            scored_words=covered - fallback_words,
            top1_mismatch=top1_mismatch,
        )
    return n, covered, pers, (per_sum / covered if covered else 1.0), \
        (wrong / covered if covered else 1.0), oracle


def evaluate(pairs: Sequence[GoldPair], lang: str, strip_stress: bool,
             broad: bool) -> Tuple[int, int, float, float]:
    """Score *pairs* and return just the point estimates
    ``(n, covered, per, wer)`` — :func:`evaluate_words` without the per-word
    PER list. Same numbers, one scoring loop; see :func:`evaluate_words_oracle`
    for the single implementation all three wrappers share."""
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


def _injected_alternatives(lang: str, exposed: bool) -> List[str]:
    """The injected alternatives this row's oracle EXCLUDED, or ``[]``.

    ``["<code> <ending>", ...]`` for every list-valued (ambiguous)
    ``grammatical_endings`` entry in *lang*'s spec — the readings the
    spec deliberately injects into the beam for a downstream rescorer.

    ``exposed`` is the ``expose_ambiguous_endings`` value the row was
    actually SCORED with, and it is a parameter rather than an assumption
    on purpose. The field is a claim about this measurement ("these
    readings are not in these numbers"), not about the spec, so when the
    scoring ran with exposure ON there is nothing to claim and the list
    is empty. Deriving it from the spec alone let the field keep
    asserting an exclusion that had stopped happening — which is exactly
    the failure a provenance field exists to prevent."""
    if exposed:
        return []
    try:
        from orthography2ipa import get
        spec = get(lang)
    except Exception:
        return []
    return [f"{spec.code} {ending}"
            for ending, value in sorted(
                (spec.grammatical_endings or {}).items())
            if isinstance(value, list)]


def build_scoreboard(limit: Optional[int], oracle: bool = False,
                     only_langs: Optional[Sequence[str]] = None,
                     only_datasets: Optional[Sequence[str]] = None,
                     expose_ambiguous_endings: bool = False,
                     ) -> List[dict]:
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

    ``oracle`` adds the top-k oracle PER columns (see
    :class:`OracleResult` for what they mean and what they must NOT be
    used for). It defaults to **OFF**, and every caller that wants it
    says so. The published ``--scoreboard`` run opts in; the CI
    regression gate (``check_benchmark_regression.py``) and the
    ``--ci-sample`` baseline do not, because they compare 1-best PER
    only and would otherwise pay ~1.6x for columns they never read.
    Defaulting to off is what keeps a future call site from silently
    inheriting that cost.

    ``expose_ambiguous_endings`` is the measurement convention, and the
    published board uses the default **False** (see
    :func:`evaluate_words_oracle`). It is threaded through rather than
    hardcoded so the row's ``oracle_injected_alternatives`` field can be
    derived from the flag the row was SCORED with — a provenance field
    that asserts an exclusion the run did not perform is worse than none.

    ``only_langs`` / ``only_datasets`` restrict the run to a subset. The
    full scoreboard is ~10M scored words and takes hours, so a targeted
    rerun is the practical way to refresh a handful of rows; the caller
    then MERGES the result into the committed set (see
    :func:`merge_scoreboard_rows`). A subset run scores each row exactly
    as the full run does — no row depends on which others ran with it.
    """
    effective = sys.maxsize if limit is None else limit
    rows: List[dict] = []
    for dataset_name, (loader, langs) in DATASETS.items():
        if only_datasets and dataset_name not in only_datasets:
            continue
        for lang in langs:
            if only_langs and lang not in only_langs:
                continue
            try:
                pairs = loader(lang, effective)
            except Exception as exc:
                print(f"skip {dataset_name} lang={lang}: {exc}",
                      file=sys.stderr)
                continue
            n, covered, pers, per, wer, oracle_res = evaluate_words_oracle(
                pairs, lang, strip_stress=True, broad=True,
                oracle_ks=ORACLE_KS if oracle else (),
                expose_ambiguous_endings=expose_ambiguous_endings,
            )
            if covered == 0:
                # A zero-coverage result is a broken loader, a dead upstream
                # or a spec with no scorable graphemes — never a real score.
                # Recording it would fabricate a per=1.0 row that looks like
                # a measurement (this exact failure silently produced stale
                # n=0 rows for tn/ug/yue). Loudly skip instead.
                print(f"REFUSING to record zero-coverage row: "
                      f"{dataset_name} lang={lang} (n={n}, covered=0) — "
                      f"investigate the loader or deregister the language",
                      file=sys.stderr)
                continue
            ci_low, ci_high = bootstrap_per_ci(pers)
            if oracle_res is not None:
                assert_oracle_self_check(dataset_name, lang, per, covered,
                                         oracle_res)
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
            if oracle_res is not None:
                # Diagnostic-only lattice-quality columns. NEVER compare
                # these to another system's 1-best (see OracleResult).
                for k in ORACLE_REPORT_KS:
                    rows[-1][f"oracle_per_top{k}"] = round(
                        oracle_res.oracle_per[k], 4)
                    rows[-1][f"oracle_exact_top{k}"] = round(
                        oracle_res.oracle_exact[k], 4)
                rows[-1]["oracle_fallback_words"] = oracle_res.fallback_words
                # Explicit, so no reader (or later edit) has to know that a
                # row's "n" happens to be `covered`: 0 means the row's
                # oracle columns carry no lattice signal.
                rows[-1]["oracle_scored_words"] = oracle_res.scored_words
                # Which injected alternatives this row's oracle EXCLUDES,
                # so the exclusion travels with the numbers instead of
                # living only in prose a later reader may not find.
                injected = _injected_alternatives(
                    lang, expose_ambiguous_endings)
                if injected:
                    rows[-1]["oracle_injected_alternatives"] = injected
    rows.sort(key=lambda r: (r["lang"], r["dataset"]))
    return rows


def merge_scoreboard_rows(old: List[dict], new: List[dict]) -> List[dict]:
    """Overlay freshly-scored *new* rows onto the committed *old* set.

    Keyed on ``(lang, dataset)`` — the scoreboard's identity. A new row
    REPLACES the old one wholesale (never a field-by-field patch: a row
    is one measurement, and half-refreshing one would mix two runs).
    Rows only in *old* are carried through untouched, which is what makes
    a per-language rerun safe when a full run is impractical.
    """
    merged = {(r["lang"], r["dataset"]): r for r in old}
    for row in new:
        merged[(row["lang"], row["dataset"])] = row
    return sorted(merged.values(), key=lambda r: (r["lang"], r["dataset"]))


def read_scoreboard_rows() -> List[dict]:
    """The committed scoreboard rows, or ``[]`` if none are written yet."""
    if not os.path.exists(SCOREBOARD_JSON):
        return []
    with open(SCOREBOARD_JSON, encoding="utf-8") as fh:
        return json.load(fh)


#: Indent used for benchmarks/results.json. It is 1, not the 2 every
#: sibling artifact uses, because that is how the file is committed:
#: ~80 commits touch it, and reformatting 8k lines to gain a space would
#: conflict with every one of them in flight for no measurement value.
#: Normalizing it to 2 is a standalone cleanup, not a rider on a
#: feature PR.
SCOREBOARD_JSON_INDENT = 1


def write_scoreboard(rows: List[dict]) -> None:
    os.makedirs(os.path.dirname(SCOREBOARD_JSON), exist_ok=True)
    with open(SCOREBOARD_JSON, "w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=SCOREBOARD_JSON_INDENT, ensure_ascii=False)
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
        "The `Oracle@3` / `Oracle@5` columns are the per-word MINIMUM PER "
        "over the engine's top-3 / top-5 readings, averaged like `PER`. "
        "They are an **orthography2ipa-only lattice-quality diagnostic** and "
        "**must never be used in a cross-system comparison or a \"beats X\" "
        "claim**: espeak, epitran and every other system benchmarked in "
        "[`docs/comparison.md`](comparison.md) emit ONE pronunciation, so "
        "setting their single answer against k of ours compares k guesses to "
        "one. `scripts/compare_systems.py` therefore does not read these "
        "columns, and the CI regression gate "
        "(`benchmarks/results_ci_sample.json`) stays 1-best.",
        "",
        "How to read the gap: `PER − Oracle@k` is **ranking error** — some "
        "reading in the top-k scores better than the one the engine ranked "
        "first, so a downstream rescorer reading our lattice could recover "
        "that much. That gap is the **rescoring headroom**, and it is an "
        "UPPER BOUND no real rescorer reaches: an oracle is allowed to pick "
        "the best candidate per word after seeing the answer. What is left "
        "at `Oracle@k` is **model error**: no better reading exists in the "
        "lattice, and only new rules or data can fix it.",
        "",
        "`Oracle@k` improving does NOT mean the correct transcription is in "
        "the beam — only that a CLOSER one is. The separate "
        "`OracleX@k` columns are the strict version: the fraction of words "
        "where some top-k candidate **equals** a gold exactly (compare "
        "against the `Exact match` column, which is the same measure at "
        "k=1). Most of the PER-oracle gain is closer-but-still-wrong "
        "readings, so quote `OracleX@k` for any \"the engine already "
        "knows the answer\" claim. It is phenomena-neutral either way: it "
        "says nothing about WHICH phonological phenomenon is wrong.",
        "",
        "Oracle cells EXCLUDE injected alternatives. A spec may declare a "
        "`grammatical_endings` value as an ordered candidate list, which "
        "deliberately puts a reading it cannot choose between into the beam "
        "for a downstream rescorer. Adding candidates can only lower an "
        "oracle, so scoring with them on would let a spec inflate its own "
        "`PER − Oracle@k` headroom — the gap this board defines as RANKING "
        "error — by declaring more alternatives. The run therefore scores "
        "with them off, and a row whose language declares any records them "
        "in `oracle_injected_alternatives` in "
        "[`benchmarks/results.json`](../benchmarks/results.json). `PER` and "
        "`Exact match` are unaffected either way: an injected alternative can "
        "never reach rank 1. The movement they do cause is reported "
        "separately, as reachability, in "
        "[`docs/benchmarks.md`](benchmarks.md).",
        "",
        "Oracle cells read `·` when the row has **not been rescored** since "
        "the oracle columns were added (most rows: a full scoreboard is "
        "~10M scored words, so rows are refreshed in batches), and `-` when "
        "the row is **sentence-level** and can never have an oracle: the "
        "beam is per WORD, and composing a sentence-level beam out of word "
        "beams would invent a ranking the engine never produces. The two "
        "are different states and are never merged into one blank.",
        "",
        "| Lang | Dataset | N | PER | Oracle@3 | Oracle@5 | OracleX@3 "
        "| OracleX@5 | 95% CI | Exact match | Quality tier | Provenance |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|",
    ]
    for row in rows:
        tier = row["quality_tier"] or "-"
        prov = row.get("provenance") or "-"
        # A row scored before the CI column existed carries nulls; a
        # merged board can hold both generations.
        lo, hi = row.get("per_ci_low"), row.get("per_ci_high")
        ci = "-" if lo is None or hi is None else f"[{lo:.4f}, {hi:.4f}]"
        # Three distinct states, three distinct markers:
        #   "·"  never rescored since the oracle columns landed
        #   "-"  rescored, but no word had a real candidate list
        #        (sentence-level gold: an oracle is impossible, not absent)
        #   n.nnnn  a real measurement
        # Collapsing the first two into one blank would let an unrescored
        # row read as "sentence-level, no ranking error", which is a
        # conclusion the data does not support.
        rescored = "oracle_per_top3" in row
        no_signal = row.get("oracle_scored_words") == 0

        def _oracle(field: str) -> str:
            if not rescored:
                return "·"
            if no_signal:
                return "-"
            v = row.get(field)
            return "·" if v is None else f"{v:.4f}"

        em = row.get("exact_match")
        lines.append(
            f"| {row['lang']} | {row['dataset']} | {row['n']} | "
            f"{row['per']:.4f} | {_oracle('oracle_per_top3')} "
            f"| {_oracle('oracle_per_top5')} "
            f"| {_oracle('oracle_exact_top3')} "
            f"| {_oracle('oracle_exact_top5')} | {ci} "
            f"| {'-' if em is None else f'{em:.4f}'} | {tier} | {prov} |"
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
# — for every language with a registered lexicon (none are bundled), so a regression
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
def _lexicon_disabled() -> Iterator[None]:
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


def _score_pairs(pairs: Sequence[GoldPair], lang: str) -> Tuple[int, float]:
    n, covered, _pers, per, _wer = evaluate_words(
        pairs, lang, strip_stress=True, broad=True)
    return covered, per


def build_lexicon_report(limit: Optional[int]) -> List[dict]:
    """Rules-only vs with-lexicon PER for every shipped lexicon language.

    For each registered lexicon (see ``orthography2ipa.register_lexicon``) and each wikipron gold tag that
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
        "optional caller-registered lexicon (never bundled) "
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
    ap.add_argument("--no-topk", action="store_true",
                    help="Skip the top-k oracle PER columns in "
                         "--scoreboard. The oracle is ON by default "
                         "(measured cost: ~1.6x the 1-best run); this is "
                         "an escape hatch for a fast ad-hoc rerun. The "
                         "oracle is a lattice-quality diagnostic for THIS "
                         "engine only and is never valid input to a "
                         "cross-system comparison.")
    ap.add_argument("--lexicon-report", action="store_true",
                    help="Score rules-only vs with-lexicon PER for every "
                         "language with a registered lexicon and "
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
        # 1-best only, deliberately (and by default): the regression gate
        # compares point-estimate PER and must never drift onto an oracle.
        rows = build_scoreboard(CI_SAMPLE_LIMIT, oracle=False)
        os.makedirs(os.path.dirname(CI_SAMPLE_JSON), exist_ok=True)
        with open(CI_SAMPLE_JSON, "w", encoding="utf-8") as fh:
            json.dump(rows, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"wrote {len(rows)} rows to "
              f"{os.path.relpath(CI_SAMPLE_JSON, REPO_ROOT)} "
              f"(CI regression sample, uniform limit={CI_SAMPLE_LIMIT})")
        return

    if args.scoreboard:
        # --lang/--dataset narrow the run to a subset and MERGE the result
        # into the committed scoreboard; without them the whole board is
        # rescored from scratch.
        subset = bool(args.lang or args.dataset)
        # The published scoreboard is the ONE caller that opts into the
        # oracle; build_scoreboard defaults it off so the CI gate and any
        # future call site never inherit the ~1.6x cost by accident.
        rows = build_scoreboard(
            args.limit, oracle=not args.no_topk,
            only_langs=[args.lang] if args.lang else None,
            only_datasets=[args.dataset] if args.dataset else None,
        )
        if subset:
            print(f"merging {len(rows)} rescored rows into the committed "
                  f"scoreboard", file=sys.stderr)
            rows = merge_scoreboard_rows(read_scoreboard_rows(), rows)
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
    n, covered, _pers, per, wer, oracle_res = evaluate_words_oracle(
        pairs, lang,
        strip_stress=not args.keep_stress,
        broad=not args.narrow,
        oracle_ks=() if args.no_topk else ORACLE_KS,
    )
    line = (f"{args.dataset} lang={lang} n={n} covered={covered} "
            f"PER={per:.4f} WER={wer:.4f}")
    if oracle_res is not None:
        line += "".join(f" oracle@{k}={oracle_res.oracle_per[k]:.4f}"
                        f"/x{oracle_res.oracle_exact[k]:.4f}"
                        for k in ORACLE_REPORT_KS)
        line += (f" (scored={oracle_res.scored_words} "
                 f"fallback={oracle_res.fallback_words})")
    print(line)


if __name__ == "__main__":
    main()
