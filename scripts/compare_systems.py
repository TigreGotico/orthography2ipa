#!/usr/bin/env python3
"""Compare orthography2ipa against other G2P systems on the same gold rows.

Runs the SAME gold word/IPA pairs used by ``scripts/benchmark.py`` through
several systems — orthography2ipa, espeak-ng, epitran, gruut, pycotovia,
and ahotts-g2p — and scores every system with the exact same normalization
and PER metric (``benchmark.normalize`` / ``benchmark.levenshtein``), so
the numbers are directly comparable to the committed scoreboard.

Systems are optional. If a system's tool/library is unavailable, or a
language has no explicit voice/code mapping for it, that system's column
is reported as ``n/a`` for that row — the script never crashes because a
comparison target is missing.

- **espeak-ng**: shelled out via ``espeak-ng -q --ipa -v <voice> <word>``,
  one process per word (small gold slices; simplicity over throughput).
  Detected with ``shutil.which("espeak-ng")``. Catalan dialect voices
  (``ca``, ``ca-ba``, ``ca-nw``, ``ca-va`` — BSC's central/balear/
  north-western/valencian voices) are discovered at runtime via
  ``espeak-ng --voices=ca`` rather than hardcoded, so a missing voice
  degrades to an honest ``n/a``/generic-voice fallback instead of a
  fabricated dialect number; see ``discover_catalan_dialect_voices``.
- **epitran**: optional Python library (``pip install .[compare]``),
  imported lazily. Needs an ISO 639-3 + ISO 15924 script code per
  language (e.g. ``spa-Latn``).
- **gruut**: optional Python library (``pip install .[compare]``),
  imported lazily. Needs a gruut language code (e.g. ``es``).
- **pycotovia**: optional Python library (``pip install .[compare]``),
  a pure-Python port of Cotovia (Univ. de Vigo / GTM) covering Galician
  and Spanish. Imported lazily; ``pycotovia.phonemize`` output is passed
  through ``pycotovia.cotovia_to_ipa`` to get comparable IPA.
- **ahotts-g2p**: optional Python library (``pip install .[compare]``,
  imported as ``ahotts_g2p``), the pure-Python G2P port of AhoTTS
  (Aholab / HiTZ, Univ. of the Basque Country) covering Basque (``eu``)
  and Spanish (``es``). ``ahotts_g2p.phonemize`` emits its output in the
  StyleTTS2 single-character training convention, where the library's
  ``MULTI`` table folds a handful of IPA sequences onto single ASCII
  letters — affricates (``tʃ``→``C``, ``ts``→``V``, ``tʂ``→``P``),
  aspirates (``pʰ``→``H``, ``kʰ``→``K``, ``tʰ``→``T``), and **stress-
  marked vowels** (``ˈi``→``I`` … ``ˈu``→``U``). Scoring that folded form
  raw against IPA gold would charge ahotts-g2p a spurious error on every
  uppercase char, so ``ahotts_transcribe`` first UNFOLDS it back to
  standard IPA (the inverse of ``ahotts_g2p.phones.MULTI``, stress
  rendered as ``ˈ`` so the shared ``normalize`` strips it exactly as it
  does for every other system) BEFORE the shared normalize()/PER — all
  systems are therefore compared in one IPA space.

  (The separate ``pyahotts`` package is the *audio* port of AhoTTS: its
  only public API synthesizes WAV bytes and exposes no phoneme output, so
  it is not scorable and is intentionally NOT a comparison system here —
  ``ahotts-g2p`` is the text-level G2P port that supersedes it for this
  table.)
- **africa-g2p**: optional Python library covering ~400 African-language
  ISO 639-3 codes (AfriSpeech, rule-based G2P derived from Omniglot script charts and Hartell's
  *Alphabets of Africa*, UNESCO 1993). NOT published on PyPI — it is not
  part of the ``[compare]`` extra (which must stay pip-installable from
  PyPI); install it from a locally built wheel of the upstream checkout
  before running this script, e.g.::

      python -m pip wheel /path/to/africa-g2p --no-deps -w /tmp/afg2p-wheel
      python -m pip install /tmp/afg2p-wheel/africa_g2p-*.whl

  Imported lazily as ``africa_g2p``; a missing install degrades every
  ``africa_g2p`` column to ``n/a``, same as every other optional system.
  Wrapped via ``AfricaPipeline(lang=<iso639_3>, output="ipa").run(word)``;
  the library's own ``africa_g2p.loader.registry()`` is queried at import
  time so the set of covered codes is never hand-enumerated here.

Normalization (identical across all four systems, see ``benchmark.normalize``
and the stress/diacritic handling in ``espeak_agreement.py``):

1. NFC-normalize.
2. Strip stress marks (``benchmark._STRESS_MARKS`` == ``ˈˌ``): primary and
   secondary stress are never scored — no system agrees on where to place
   them consistently enough for that to be a fair signal. (The length
   mark ``ː`` is NOT in that set and is retained, exactly as
   ``benchmark.normalize`` treats it.)
3. Strip narrow-transcription diacritics (``benchmark._NARROW_MARKS``) via
   NFD decomposition — this is the same "broad" comparison mode
   ``benchmark.py --scoreboard`` uses by default.
4. Drop whitespace — segmentation-free comparison, since some systems
   space-separate phonemes and others don't.

PER is computed with ``benchmark.levenshtein(hyp, gold) / len(gold)``,
taking the best score against any gold variant for a word — exactly the
metric ``benchmark.evaluate`` uses for orthography2ipa.

Fair-comparison 2x2 (dictionary vs. rules)
-------------------------------------------

The main table above conflates two very different things espeak-ng ships
for a language: **letter-to-sound rules** (``dictsource/<lang>_rules``,
genuinely comparable to o2i's grapheme rules) and **hand-curated word-
exception lists** (``dictsource/<lang>_list``/``_listx``/``_extra`` —
a per-word lexicon espeak-ng ships and o2i, by hard rule, never bundles).
Scoring plain ``espeak`` against plain ``o2i`` therefore compares
"rules + dictionary" against "rules only" — not a fair fight. Two extra
optional columns isolate the dictionary's contribution:

- **``espeak_rules``**: espeak-ng run against a *rules-only* dictionary
  build — the exact same ``dictsource/<lang>_rules`` compiled, but with
  the ``_list``/``_listx``/``_extra`` word-exception files emptied before
  compiling. Inspecting the stripped list files (en, fr, de, nl, ca, sv,
  eu) showed they carry more than proper-noun/loanword exceptions: basic
  function words and numbers are hand-pronounced there too (English
  ``the``, ``of``, ``an``, ``and``, ``one``, ``two``; French ``le``,
  ``la``, ``les``, ``un``, ``une``, ``et``; German ``der``, ``die``,
  ``das``, ``und``, ``ein(e)``, ``zu``; Dutch ``de``, ``het``, ``een``,
  ``en``; Swedish ``en``, ``ett``, ``den``, ``det``, ``och``; Catalan
  ``el``, ``la``, ``els``, ``les``, ``de``, ``i``; Basque ``eta``) — so
  "rules-only" here means genuinely rules-only: those entries are
  stripped too, not just the proper-noun exceptions, and this column
  will visibly score WORSE than plain ``espeak`` on exactly those words.
  Build the stripped dictionaries with
  ``scripts/build_espeak_rules_only.sh`` (clones+builds espeak-ng from
  source into a scratch dir — GPL, never committed — and writes the
  compiled ``*_dict`` files to an output dir), then point this script at
  them::

      scripts/build_espeak_rules_only.sh en fr de nl ca sv eu
      ESPEAK_RULES_DATA_PATH=/path/to/rules-only-data \\
          PYTHONPATH=$PWD python scripts/compare_systems.py --scoreboard

  Without ``$ESPEAK_RULES_DATA_PATH`` set, ``espeak_rules`` is reported
  as ``n/a`` for every row, same as any other unavailable system.

- **``o2i_lex``**: orthography2ipa scored WITH a runtime lexicon built
  from espeak-ng's OWN word-exception list for that language — i.e. o2i
  gets the same per-word dictionary espeak-ng has, added via o2i's
  existing (unbundled) lexicon overlay capability
  (:mod:`orthography2ipa.lexicon`, ``register_lexicon``). The word list
  is extracted from ``dictsource/<lang>_list``/``_listx``/``_extra``
  (the words only — NOT the phoneme column, which is espeak-ng's
  internal ASCII notation, not IPA); each word's IPA is then obtained by
  actually running normal (non-stripped) ``espeak-ng --ipa -q`` on it,
  batched and cached to ``.o2i_lex_cache/<lang>.tsv`` (gitignored, never
  committed — GPL data lives only in that local cache, exactly like
  espeak-ng itself never ships in this repo). Set
  ``ESPEAK_DICTSOURCE_PATH`` to an espeak-ng checkout (or its
  ``dictsource/`` dir directly) to enable it::

      ESPEAK_DICTSOURCE_PATH=/path/to/espeak-ng \\
          PYTHONPATH=$PWD python scripts/compare_systems.py --scoreboard

  Without ``$ESPEAK_DICTSOURCE_PATH`` set, ``o2i_lex`` is ``n/a`` for
  every row.

Read together, the four columns ``o2i`` / ``o2i_lex`` / ``espeak`` /
``espeak_rules`` isolate what each system's RULES contribute versus what
its DICTIONARY contributes, on the same gold words.

Usage::

    python scripts/compare_systems.py --scoreboard
    python scripts/compare_systems.py --lang es --limit 50
    python scripts/compare_systems.py --list
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, os.path.dirname(__file__))
import benchmark  # noqa: E402  — shared dataset loaders, normalize(), levenshtein()

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
COMPARISON_MD = os.path.join(REPO_ROOT, "docs", "comparison.md")
COMPARISON_JSON = os.path.join(REPO_ROOT, "benchmarks", "comparison.json")

HARNESS_VERSION = "1.0"

# ─── fair-comparison 2x2 (dictionary vs. rules) ─────────────────────────────
#
# See the module docstring's "Fair-comparison 2x2" section for the full
# rationale. Both env vars point at GPL espeak-ng data that is built/cloned
# to a scratch location by the caller (``scripts/build_espeak_rules_only.sh``
# for the first one) — this repo never ships or commits any of it.

#: Directory of a *rules-only* compiled espeak-ng data set (word-exception
#: lists emptied, letter-to-sound rules intact) — see
#: ``scripts/build_espeak_rules_only.sh``. Unset => ``espeak_rules`` is
#: ``n/a`` everywhere.
ESPEAK_RULES_DATA_PATH = os.environ.get("ESPEAK_RULES_DATA_PATH")

#: An espeak-ng checkout (or its ``dictsource/`` dir) whose word-exception
#: list files are turned into a runtime o2i lexicon for the ``o2i_lex``
#: column. Unset => ``o2i_lex`` is ``n/a`` everywhere.
ESPEAK_DICTSOURCE_PATH = os.environ.get("ESPEAK_DICTSOURCE_PATH")

#: Where derived (word -> espeak IPA) lexicon TSVs are cached, keyed by o2i
#: language tag. GPL-derived data; gitignored, never committed.
O2I_LEX_CACHE_DIR = os.path.join(REPO_ROOT, ".o2i_lex_cache")

#: o2i language tag -> espeak-ng dictsource base language code, for the
#: languages this 2x2 currently covers (the "stronghold" rows). Extend as
#: more languages get an ``espeak`` voice mapping above AND a matching
#: dictsource file; a tag with no entry here just gets ``o2i_lex == n/a``.
DICTSOURCE_LANG: Dict[str, str] = {
    "en-US": "en",
    "en": "en",
    "fr": "fr",
    "de": "de",
    "nl": "nl",
    "ca": "ca",
    "ca-x-balear": "ca",
    "ca-x-occidental": "ca",
    "ca-x-valencia": "ca",
    "sv": "sv",
    "eu": "eu",
    "eu-wikipron": "eu",
}

# ─── language mapping ───────────────────────────────────────────────────────
#
# Each entry maps an orthography2ipa language tag to:
#   - a (loader, loader_lang, dataset_name) triple drawn from
#     benchmark.DATASETS, giving the SAME gold rows benchmark.py scores
#     orthography2ipa against;
#   - an espeak-ng voice (or None if espeak-ng has no matching voice);
#   - an epitran code, ISO 639-3 + ISO 15924 script (or None if epitran
#     has no published mapping for the language, or the language isn't
#     realistically epitran-compatible);
#   - a gruut language code (or None if gruut doesn't ship that language).
#
# A curated subset of DATASETS languages with reasonably confident
# third-party mappings — not every registered gold language, since most
# competitor systems only cover a fraction of orthography2ipa's language codes.
LANGS: Dict[str, dict] = {
    "en-US": {"dataset": ("cmudict", "en-US"), "espeak": "en-us",
               "epitran": "eng-Latn", "gruut": "en-us"},
    "en": {"dataset": ("wikipron", "en"), "espeak": "en-gb",
           "epitran": "eng-Latn", "gruut": "en-gb"},
    "es": {"dataset": ("wikipron", "es"), "espeak": "es",
           "epitran": "spa-Latn", "gruut": "es",
           "ahotts": {"lang": "es", "version": "classic"}},
    # sample_n: the unified pt gold is ~116k pt-PT words; epitran/gruut transcribe
    # word-by-word in-process and cannot batch, so a full pass is days of
    # wall clock. Scored on a fixed-seed (loader SAMPLE_SEED) sample of
    # 3000 — an EXPLICIT, row-flagged sample, not a silent cap.
    "pt-PT": {"dataset": ("portuguese_unified", "pt-PT"), "espeak": "pt",
              "epitran": "por-Latn", "gruut": "pt", "sample_n": 3000},
    "fr": {"dataset": ("wikipron", "fr"), "espeak": "fr-fr",
           "epitran": "fra-Latn", "gruut": "fr"},
    "de": {"dataset": ("wikipron", "de"), "espeak": "de",
           "epitran": "deu-Latn", "gruut": "de"},
    "it": {"dataset": ("wikipron", "it"), "espeak": "it",
           "epitran": "ita-Latn", "gruut": "it"},
    "nl": {"dataset": ("wikipron", "nl"), "espeak": "nl",
           "epitran": "nld-Latn", "gruut": "nl"},
    "sv": {"dataset": ("wikipron", "sv"), "espeak": "sv",
           "epitran": "swe-Latn", "gruut": "sv"},
    "ru": {"dataset": ("wikipron", "ru"), "espeak": "ru",
           "epitran": "rus-Cyrl", "gruut": "ru"},
    "pl": {"dataset": ("wikipron", "pl"), "espeak": "pl",
           "epitran": "pol-Latn", "gruut": None},
    "el": {"dataset": ("wikipron", "el"), "espeak": "el",
           "epitran": "ell-Grek", "gruut": None},
    "tr": {"dataset": ("wikipron", "tr"), "espeak": "tr",
           "epitran": "tur-Latn", "gruut": None},
    "fi": {"dataset": ("wikipron", "fi"), "espeak": "fi",
           "epitran": "fin-Latn", "gruut": None},
    "hi": {"dataset": ("wikipron", "hi"), "espeak": "hi",
           "epitran": "hin-Deva", "gruut": None},
    # Basque on the HiTZ expert-derived gold. NOTE: hitz_basque_ipa comes
    # from HiTZ/Aholab (UPV/EHU) — the same lab that authors AhoTTS — so
    # ahotts-g2p's number here is close to same-source and should be read
    # alongside the independent wikipron "eu-wikipron" row below.
    "eu": {"dataset": ("hitz_basque_ipa", "eu"), "espeak": "eu",
           "epitran": None, "gruut": None,
           "ahotts": {"lang": "eu", "version": "classic"}},
    # Basque on INDEPENDENT WikiPron (Wiktionary) gold — a fairer,
    # non-same-lab comparison point for ahotts-g2p on Basque. Uses the
    # ``g2p`` override so this distinct dataset row still drives the
    # ``eu`` orthography2ipa spec.
    "eu-wikipron": {"dataset": ("wikipron", "eu"), "g2p": "eu",
                     "espeak": "eu", "epitran": None, "gruut": None,
                     "ahotts": {"lang": "eu", "version": "classic"}},
    "ca": {"dataset": ("4catac", "ca"), "espeak": "ca",
           "epitran": "cat-Latn", "gruut": None},
    # Catalan dialect voices added to espeak-ng by the Barcelona
    # Supercomputing Center (BSC); matched 1:1 to the 4catac gold's four
    # regional accents. ca-x-occidental -> espeak's "ca-nw"
    # (Catalan_(North-western)) is a direct semantic match to 4catac's
    # "Nord-Occ" accent, not an approximation. The actual espeak voice
    # used per dialect is resolved at runtime (see
    # ``discover_catalan_dialect_voices``) and falls back to the generic
    # "ca" voice, clearly labeled, if a dialect voice isn't installed.
    "ca-x-balear": {"dataset": ("4catac", "ca-x-balear"), "espeak": "ca-ba",
                     "epitran": "cat-Latn", "gruut": None},
    "ca-x-occidental": {"dataset": ("4catac", "ca-x-occidental"),
                         "espeak": "ca-nw",
                         "epitran": "cat-Latn", "gruut": None},
    "ca-x-valencia": {"dataset": ("4catac", "ca-x-valencia"),
                       "espeak": "ca-va",
                       "epitran": "cat-Latn", "gruut": None},
    "gl": {"dataset": ("wikipron", "gl"), "espeak": None,
           "epitran": None, "gruut": None, "pycotovia": "gl"},
    "cy": {"dataset": ("wikipron", "cy"), "espeak": "cy",
           "epitran": "cym-Latn", "gruut": None},
    "ga": {"dataset": ("wikipron", "ga"), "espeak": "ga",
           "epitran": None, "gruut": None},
    "ro": {"dataset": ("wikipron", "ro"), "espeak": "ro",
           "epitran": "ron-Latn", "gruut": None},
    # ─── africa-g2p overlap ─────────────────────────────────────────────
    # Every o2i gold language (see benchmarks/results.json) whose ISO
    # 639-3 code africa-g2p's own registry() also covers. espeak-ng has
    # no matching voice for any of these on this machine's install
    # (checked via ``espeak-ng --voices``, never assumed); epitran/gruut
    # likewise have no published mapping, so those columns are honestly
    # ``None`` rather than guessed — africa-g2p is the only comparison
    # point for these rows today.
    "arb": {"dataset": ("arabic_tts", "arb"), "espeak": None,
            "epitran": None, "gruut": None},
    "cop": {"dataset": ("wikipron", "cop"), "espeak": None,
            "epitran": None, "gruut": None},
    "hts": {"dataset": ("wikipron", "hts"), "espeak": None,
            "epitran": None, "gruut": None},
    "kab": {"dataset": ("vox_communis", "kab"), "espeak": None,
            "epitran": None, "gruut": None},
    "ktz": {"dataset": ("wikipron", "ktz"), "espeak": None,
            "epitran": None, "gruut": None},
    "lad": {"dataset": ("wikipron", "lad"), "espeak": None,
            "epitran": None, "gruut": None},
    "mfe": {"dataset": ("wikipron", "mfe"), "espeak": None,
            "epitran": None, "gruut": None},
    "ngh": {"dataset": ("wikipron", "ngh"), "espeak": None,
            "epitran": None, "gruut": None},
    "nup": {"dataset": ("wikipron", "nup"), "espeak": None,
            "epitran": None, "gruut": None},
    "tzm": {"dataset": ("wikipron", "tzm"), "espeak": None,
            "epitran": None, "gruut": None},
}

#: africa-g2p's own registry of covered ISO 639-3 codes, loaded once
#: (empty if the library isn't installed) — used to gate ``africa_g2p``
#: columns per language so an unmapped code degrades to ``n/a`` instead
#: of raising.
def _africa_g2p_codes() -> set:
    try:
        from africa_g2p.loader import registry
    except ImportError:
        return set()
    try:
        return set(registry().keys())
    except Exception:
        return set()


AFRICA_G2P_CODES = _africa_g2p_codes()

for _tag, _cfg in LANGS.items():
    _cfg.setdefault("africa_g2p", _tag if _tag in AFRICA_G2P_CODES else None)


def apply_catalan_dialect_voices(langs: Dict[str, dict]) -> Dict[str, str]:
    """Mutate *langs*' Catalan dialect entries in place with the espeak
    voices actually discovered on this machine (see
    ``discover_catalan_dialect_voices``); return the resolved mapping so
    callers (and ``docs/comparison.md`` generation) can report exactly
    which voices were used, including any generic-``ca`` fallback."""
    voices = discover_catalan_dialect_voices()
    for tag, voice in voices.items():
        if tag in langs:
            langs[tag]["espeak"] = voice
    return voices


# ─── espeak-ng ───────────────────────────────────────────────────────────────

def espeak_available() -> bool:
    return shutil.which("espeak-ng") is not None


def discover_catalan_dialect_voices() -> Dict[str, Optional[str]]:
    """Discover which Catalan dialect voices ``espeak-ng`` actually has
    installed, by parsing ``espeak-ng --voices=ca`` — never hardcoded,
    since BSC's dialect voices (``ca-ba``, ``ca-nw``, ``ca-va``) may or
    may not be present depending on the espeak-ng build/version.

    Returns ``{o2i lang tag: espeak voice code or None}`` for the four
    LANGS Catalan entries. When a dialect-specific voice is missing but
    the generic ``ca`` voice is present, that dialect falls back to
    ``ca`` (documented, not faked as dialect-specific); when neither is
    present the dialect is ``None`` (n/a).
    """
    wanted = {
        "ca": "ca", "ca-x-balear": "ca-ba",
        "ca-x-occidental": "ca-nw", "ca-x-valencia": "ca-va",
    }
    if not espeak_available():
        return {tag: None for tag in wanted}
    try:
        proc = subprocess.run(
            ["espeak-ng", "--voices=ca"],
            capture_output=True, text=True, timeout=10,
        )
    except (OSError, subprocess.TimeoutExpired):
        return {tag: None for tag in wanted}
    available = set()
    for line in proc.stdout.splitlines()[1:]:
        parts = line.split()
        if len(parts) >= 2:
            available.add(parts[1])

    result: Dict[str, Optional[str]] = {}
    for tag, voice in wanted.items():
        if voice in available:
            result[tag] = voice
        elif "ca" in available:
            result[tag] = "ca"
        else:
            result[tag] = None
    return result


#: Words per espeak-ng subprocess in the batched path. espeak-ng emits one
#: IPA line per input line (empty output lines included), so alignment is
#: positional; the chunk bounds memory and keeps a single hung call from
#: stalling the whole language.
_ESPEAK_CHUNK = 500


def espeak_rules_available() -> bool:
    """``True`` when ``espeak-ng`` is installed AND ``ESPEAK_RULES_DATA_PATH``
    points at an existing rules-only compiled data directory (see
    ``scripts/build_espeak_rules_only.sh``)."""
    return (espeak_available() and bool(ESPEAK_RULES_DATA_PATH)
            and os.path.isdir(ESPEAK_RULES_DATA_PATH))


def _espeak_cmd(voice: str, data_path: Optional[str] = None,
                 word: Optional[str] = None) -> List[str]:
    cmd = ["espeak-ng"]
    if data_path:
        cmd.append(f"--path={data_path}")
    cmd += ["-q", "--ipa", "-v", voice]
    if word is not None:
        cmd += ["--", word]
    return cmd


def espeak_batch_transcribe(words: List[str], voice: str,
                            data_path: Optional[str] = None
                            ) -> Dict[str, Optional[str]]:
    """Transcribe *words* with espeak-ng, one subprocess per chunk of
    ``_ESPEAK_CHUNK`` instead of one per word — the difference between an
    uncapped full-gold run finishing in minutes and taking days.

    espeak-ng preserves line alignment: N input lines produce exactly N
    output lines (a word espeak drops yields an empty line, not a missing
    one). That invariant is CHECKED per chunk; on any mismatch the chunk
    falls back to the per-word path, so a batching surprise can degrade
    speed but never mis-attribute a transcription to the wrong word.
    Words containing a newline (impossible for gold entries, guarded
    anyway) also take the per-word path.
    """
    out: Dict[str, Optional[str]] = {}
    batchable = [w for w in words if "\n" not in w]
    for w in words:
        if "\n" in w:
            out[w] = espeak_transcribe(w, voice, data_path=data_path)
    for i in range(0, len(batchable), _ESPEAK_CHUNK):
        chunk = batchable[i:i + _ESPEAK_CHUNK]
        lines: Optional[List[str]] = None
        try:
            proc = subprocess.run(
                # NO --stdin flag: with it espeak-ng joins all input lines
                # into one utterance; reading piped stdin without it emits
                # one IPA line per input line (the alignment this relies on)
                _espeak_cmd(voice, data_path=data_path),
                input="\n".join(chunk) + "\n",
                capture_output=True, text=True,
                timeout=30 + len(chunk),
            )
            if proc.returncode == 0:
                candidate = proc.stdout.split("\n")
                # trailing newline → one empty trailing element
                if candidate and candidate[-1] == "":
                    candidate.pop()
                if len(candidate) == len(chunk):
                    lines = candidate
        except (OSError, subprocess.TimeoutExpired):
            lines = None
        if lines is None:
            for w in chunk:
                out[w] = espeak_transcribe(w, voice, data_path=data_path)
        else:
            for w, line in zip(chunk, lines):
                line = line.strip()
                out[w] = line or None
    return out


def espeak_transcribe(word: str, voice: str,
                       data_path: Optional[str] = None) -> Optional[str]:
    """Transcribe *word* with espeak-ng, or ``None`` on any failure.

    *data_path*, when given, is passed as ``--path=<data_path>`` so the
    caller can point espeak-ng at an alternate compiled data directory
    (e.g. the rules-only build for the ``espeak_rules`` column) instead of
    the machine's default install.
    """
    try:
        proc = subprocess.run(
            # "--" ends option parsing so a gold word starting with "-"
            # is treated as text, not misparsed as an espeak-ng flag
            _espeak_cmd(voice, data_path=data_path, word=word),
            capture_output=True, text=True, timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if proc.returncode != 0:
        return None
    out = proc.stdout.strip()
    return out or None


# Resolved once at import time against the local espeak-ng install; exposed
# so ``write_comparison``/tests can report exactly which voices were used.
CATALAN_DIALECT_VOICES: Dict[str, Optional[str]] = apply_catalan_dialect_voices(LANGS)


# ─── pycotovia (lazy, optional) ─────────────────────────────────────────────

def pycotovia_transcribe(word: str, lang: str) -> Optional[str]:
    try:
        import pycotovia
    except ImportError:
        return None
    try:
        raw = pycotovia.phonemize(word, lang=lang)
        ipa = pycotovia.cotovia_to_ipa(raw)
        return ipa or None
    except Exception:
        return None


# ─── ahotts-g2p (lazy, optional) ────────────────────────────────────────────

_ahotts_unfold_cache: Dict[str, str] = {}


def _ahotts_unfold_map() -> Dict[str, str]:
    """Inverse of ``ahotts_g2p.phones.MULTI`` (single folded char -> IPA
    sequence), with the stress apostrophe rendered as ``ˈ`` so the shared
    ``benchmark.normalize`` strips it just like every other system's
    stress marks. Built lazily and cached from the installed package so
    it never drifts from the library's own fold table."""
    if not _ahotts_unfold_cache:
        from ahotts_g2p.phones import MULTI
        for ipa_seq, single in MULTI.items():
            _ahotts_unfold_cache[single] = ipa_seq.replace("'", "ˈ")
    return _ahotts_unfold_cache


def ahotts_unfold_to_ipa(folded: str) -> str:
    """Convert ahotts-g2p's StyleTTS2 single-char output to standard IPA
    by expanding each folded char (uppercase affricate/aspirate/stressed
    vowel) back to its IPA sequence; all other chars pass through."""
    unfold = _ahotts_unfold_map()
    return "".join(unfold.get(ch, ch) for ch in folded)


def ahotts_transcribe(word: str, cfg: dict) -> Optional[str]:
    """Transcribe *word* with ahotts-g2p for ``cfg['lang']`` /
    ``cfg['version']``, unfolded to standard IPA (see
    ``ahotts_unfold_to_ipa``), or ``None`` if the library is absent or
    fails on the word."""
    try:
        import ahotts_g2p
    except ImportError:
        return None
    try:
        raw = ahotts_g2p.phonemize(
            word, lang=cfg["lang"], version=cfg["version"])
    except Exception:
        return None
    if not raw:
        return None
    return ahotts_unfold_to_ipa(raw) or None


# ─── africa-g2p (lazy, optional) ────────────────────────────────────────────

_africa_pipeline_cache: Dict[str, object] = {}


def africa_g2p_transcribe(word: str, lang: str) -> Optional[str]:
    """Transcribe *word* with africa-g2p's ``AfricaPipeline`` for the
    ISO 639-3 *lang* code, or ``None`` if the library is absent, the code
    isn't in its registry, or it fails on the word."""
    try:
        from africa_g2p import AfricaPipeline
    except ImportError:
        return None
    pipe = _africa_pipeline_cache.get(lang)
    if pipe is None:
        try:
            pipe = AfricaPipeline(lang=lang, output="ipa")
        except Exception:
            return None
        _africa_pipeline_cache[lang] = pipe
    try:
        return pipe.run(word) or None
    except Exception:
        return None


# ─── epitran (lazy, optional) ───────────────────────────────────────────────

_epitran_cache: Dict[str, object] = {}


def epitran_transcribe(word: str, code: str) -> Optional[str]:
    try:
        import epitran  # noqa: F401
    except ImportError:
        return None
    epi = _epitran_cache.get(code)
    if epi is None:
        try:
            epi = epitran.Epitran(code)
        except Exception:
            return None
        _epitran_cache[code] = epi
    try:
        return epi.transliterate(word) or None
    except Exception:
        return None


# ─── gruut (lazy, optional) ─────────────────────────────────────────────────

def gruut_transcribe(word: str, lang: str) -> Optional[str]:
    try:
        import gruut
    except ImportError:
        return None
    try:
        phonemes: List[str] = []
        for sentence in gruut.sentences(word, lang=lang):
            for gruut_word in sentence:
                if gruut_word.phonemes:
                    phonemes.extend(gruut_word.phonemes)
        return "".join(phonemes) or None
    except Exception:
        return None


# ─── o2i_lex: runtime lexicon built from espeak-ng's own wordlist ──────────
#
# See the module docstring's "Fair-comparison 2x2" section. GPL-derived
# data (espeak-ng's dictsource wordlists, and the IPA transcriptions
# derived from them) only ever lives under ``O2I_LEX_CACHE_DIR`` — a
# gitignored local cache, never the repo tree.

def _parse_espeak_wordlist_words(dictsource_dir: str, base_lang: str) -> List[str]:
    """Extract plain WORDS (not the phoneme column, which is espeak-ng's
    own internal ASCII phoneme notation — not IPA) from *base_lang*'s
    ``_list``/``_listx``/``_extra`` dictsource files under
    *dictsource_dir*.

    Skips: comments (``// ...``), blank lines, directive-only first
    tokens (``_lig``, ``?3``, ``$nounf`` — letter/ligature helper names
    and conditional/inflection directives, not words), and single-ASCII-
    letter entries (espeak-ng's "spell this letter" pronunciations, not
    real vocabulary words scored in any gold set here).
    """
    words = set()
    for suffix in ("list", "listx", "extra"):
        path = os.path.join(dictsource_dir, f"{base_lang}_{suffix}")
        if not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                line = line.split("//", 1)[0].strip()
                if not line:
                    continue
                tok = line.split()[0]
                if tok.startswith(("_", "?", "$")):
                    continue
                if len(tok) == 1:
                    continue
                if not any(ch.isalpha() for ch in tok):
                    continue
                words.add(tok.lower())
    return sorted(words)


def _resolve_dictsource_dir(base: str) -> Optional[str]:
    nested = os.path.join(base, "dictsource")
    if os.path.isdir(nested):
        return nested
    if os.path.isdir(base):
        return base
    return None


def build_espeak_lexicon_tsv(o2i_lang: str) -> Optional[str]:
    """Build (or reuse a cached) ``word<TAB>ipa`` lexicon TSV for
    *o2i_lang*, sourced from espeak-ng's OWN word-exception dictsource
    list and espeak-ng's OWN (normal, non-stripped) IPA transcription of
    each listed word — this scores o2i WITH espeak's dictionary
    knowledge, not espeak against itself.

    Returns ``None`` (=> ``o2i_lex`` is n/a for this language) when
    ``ESPEAK_DICTSOURCE_PATH`` is unset, *o2i_lang* has no
    ``DICTSOURCE_LANG`` mapping, espeak-ng isn't installed, or the
    wordlist is empty.
    """
    base_lang = DICTSOURCE_LANG.get(o2i_lang)
    if base_lang is None or not ESPEAK_DICTSOURCE_PATH or not espeak_available():
        return None
    dictsource_dir = _resolve_dictsource_dir(ESPEAK_DICTSOURCE_PATH)
    if dictsource_dir is None:
        return None
    os.makedirs(O2I_LEX_CACHE_DIR, exist_ok=True)
    cache_path = os.path.join(O2I_LEX_CACHE_DIR, f"{o2i_lang}.tsv")
    if os.path.isfile(cache_path) and os.path.getsize(cache_path) > 0:
        return cache_path
    words = _parse_espeak_wordlist_words(dictsource_dir, base_lang)
    if not words:
        return None
    voice = LANGS[o2i_lang]["espeak"] or base_lang
    ipa_by_word = espeak_batch_transcribe(words, voice)
    wrote_any = False
    with open(cache_path, "w", encoding="utf-8") as fh:
        for w in words:
            ipa = ipa_by_word.get(w)
            if ipa:
                fh.write(f"{w}\t{ipa}\n")
                wrote_any = True
    if not wrote_any:
        os.remove(cache_path)
        return None
    return cache_path


# ─── scoring ─────────────────────────────────────────────────────────────────

def _score(hyps_and_golds: List[Tuple[Optional[str], List[str]]]) -> Tuple[Optional[float], int]:
    """Mean PER over rows with a non-``None`` hypothesis, using
    ``benchmark.normalize``/``benchmark.levenshtein`` (broad, stress
    stripped — matching ``benchmark.py --scoreboard``'s default mode).
    Returns ``(per, covered)``; ``per`` is ``None`` when nothing scored."""
    per_sum, covered = 0.0, 0
    for hyp, golds in hyps_and_golds:
        if not hyp:
            continue
        hyp_n = benchmark.normalize(hyp, strip_stress=True, broad=True)
        if not hyp_n:
            continue
        covered += 1
        per_sum += min(
            benchmark.levenshtein(hyp_n, benchmark.normalize(g, True, True))
            / max(len(benchmark.normalize(g, True, True)), 1)
            for g in golds
        )
    if covered == 0:
        return None, 0
    return per_sum / covered, covered


def compare_lang(lang: str, limit: Optional[int]) -> dict:
    """Run *lang* through every available system on the same gold rows.
    Returns a row dict with per-system PER (or ``None`` == "n/a").

    ``limit=None`` scores the FULL gold set (the published run — same
    no-caps policy as ``benchmark.py --scoreboard``), except where the
    language config carries an explicit ``sample_n``: gold sets so large
    that per-word external systems make a full pass impractical (the
    617k-row Portal lexicon) are scored on a fixed-seed sample of that
    documented size, and the row says so (``sampled: true``) instead of
    hiding the cap.
    """
    cfg = LANGS[lang]
    dataset_name, loader_lang = cfg["dataset"]
    loader, _ = benchmark.DATASETS[dataset_name]
    sample_n = cfg.get("sample_n")
    if limit is None:
        effective = sample_n if sample_n is not None else sys.maxsize
    else:
        effective = limit
    pairs = loader(loader_lang, effective)
    if limit is None and sample_n is not None:
        print(f"note: {lang}/{dataset_name} scored on a fixed-seed sample "
              f"of {sample_n} (full set is impractical for the per-word "
              f"external systems); the row is flagged 'sampled'",
              file=sys.stderr)

    refs: Dict[str, List[str]] = {}
    for word, gold in pairs:
        refs.setdefault(word, []).append(gold)
    words = sorted(refs)

    import orthography2ipa
    from orthography2ipa import G2P
    g2p_code = cfg.get("g2p", lang)
    orthography2ipa.clear_lexicons()  # defensive: no leftover lexicon from a prior lang
    engine = G2P(g2p_code)

    o2i_rows: List[Tuple[Optional[str], List[str]]] = []
    espeak_rows: List[Tuple[Optional[str], List[str]]] = []
    espeak_rules_rows: List[Tuple[Optional[str], List[str]]] = []
    o2i_lex_rows: List[Tuple[Optional[str], List[str]]] = []
    epitran_rows: List[Tuple[Optional[str], List[str]]] = []
    gruut_rows: List[Tuple[Optional[str], List[str]]] = []
    pycotovia_rows: List[Tuple[Optional[str], List[str]]] = []
    ahotts_rows: List[Tuple[Optional[str], List[str]]] = []
    africa_g2p_rows: List[Tuple[Optional[str], List[str]]] = []

    use_espeak = cfg["espeak"] is not None and espeak_available()
    use_espeak_rules = cfg["espeak"] is not None and espeak_rules_available()
    use_epitran = cfg["epitran"] is not None
    use_gruut = cfg["gruut"] is not None
    use_pycotovia = cfg.get("pycotovia") is not None
    use_ahotts = cfg.get("ahotts") is not None
    use_africa_g2p = cfg.get("africa_g2p") is not None

    espeak_out: Dict[str, Optional[str]] = {}
    if use_espeak:
        espeak_out = espeak_batch_transcribe(words, cfg["espeak"])
    espeak_rules_out: Dict[str, Optional[str]] = {}
    if use_espeak_rules:
        espeak_rules_out = espeak_batch_transcribe(
            words, cfg["espeak"], data_path=ESPEAK_RULES_DATA_PATH)

    lexicon_tsv = build_espeak_lexicon_tsv(lang)
    use_o2i_lex = lexicon_tsv is not None

    for word in words:
        golds = refs[word]
        try:
            # Sentence-level gold entries (4catac) go through the
            # utterance API so cross-word sandhi and per-word dispatch
            # apply — the same multiword rule benchmark.evaluate_words
            # uses; transcribe_word on a whole sentence mis-scores it.
            transcribe = (engine.transcribe if len(word.split()) > 1
                          else engine.transcribe_word)
            o2i_rows.append((transcribe(word), golds))
        except Exception:
            o2i_rows.append((None, golds))

        if use_espeak:
            espeak_rows.append((espeak_out.get(word), golds))
        if use_espeak_rules:
            espeak_rules_rows.append((espeak_rules_out.get(word), golds))
        if use_epitran:
            epitran_rows.append((epitran_transcribe(word, cfg["epitran"]), golds))
        if use_gruut:
            gruut_rows.append((gruut_transcribe(word, cfg["gruut"]), golds))
        if use_pycotovia:
            pycotovia_rows.append(
                (pycotovia_transcribe(word, cfg["pycotovia"]), golds))
        if use_ahotts:
            ahotts_rows.append(
                (ahotts_transcribe(word, cfg["ahotts"]), golds))
        if use_africa_g2p:
            africa_g2p_rows.append(
                (africa_g2p_transcribe(word, cfg["africa_g2p"]), golds))

    if use_o2i_lex:
        # register_lexicon() calls get_lexicon.cache_clear() itself, so the
        # engine picks up the sidecar on the very next transcribe call —
        # no need for a fresh G2P instance.
        orthography2ipa.register_lexicon(g2p_code, lexicon_tsv)
        for word in words:
            golds = refs[word]
            try:
                transcribe = (engine.transcribe if len(word.split()) > 1
                              else engine.transcribe_word)
                o2i_lex_rows.append((transcribe(word), golds))
            except Exception:
                o2i_lex_rows.append((None, golds))
        orthography2ipa.clear_lexicons()

    o2i_per, o2i_n = _score(o2i_rows)
    o2i_lex_per, o2i_lex_n = (
        _score(o2i_lex_rows) if use_o2i_lex else (None, 0))
    espeak_per, espeak_n = _score(espeak_rows) if use_espeak else (None, 0)
    espeak_rules_per, espeak_rules_n = (
        _score(espeak_rules_rows) if use_espeak_rules else (None, 0))
    epitran_per, epitran_n = _score(epitran_rows) if use_epitran else (None, 0)
    gruut_per, gruut_n = _score(gruut_rows) if use_gruut else (None, 0)
    pycotovia_per, pycotovia_n = (
        _score(pycotovia_rows) if use_pycotovia else (None, 0))
    ahotts_per, ahotts_n = (
        _score(ahotts_rows) if use_ahotts else (None, 0))
    ahotts_version = cfg["ahotts"]["version"] if use_ahotts else None
    africa_g2p_per, africa_g2p_n = (
        _score(africa_g2p_rows) if use_africa_g2p else (None, 0))

    return {
        "lang": lang,
        "dataset": dataset_name,
        "n": len(words),
        "o2i_per": round(o2i_per, 4) if o2i_per is not None else None,
        "o2i_n": o2i_n,
        "o2i_lex_per": round(o2i_lex_per, 4) if o2i_lex_per is not None else None,
        "o2i_lex_n": o2i_lex_n,
        "espeak_per": round(espeak_per, 4) if espeak_per is not None else None,
        "espeak_n": espeak_n,
        "espeak_voice": cfg["espeak"],
        "espeak_rules_per": round(espeak_rules_per, 4) if espeak_rules_per is not None else None,
        "espeak_rules_n": espeak_rules_n,
        "epitran_per": round(epitran_per, 4) if epitran_per is not None else None,
        "epitran_n": epitran_n,
        "gruut_per": round(gruut_per, 4) if gruut_per is not None else None,
        "gruut_n": gruut_n,
        "pycotovia_per": round(pycotovia_per, 4) if pycotovia_per is not None else None,
        "pycotovia_n": pycotovia_n,
        "ahotts_per": round(ahotts_per, 4) if ahotts_per is not None else None,
        "ahotts_n": ahotts_n,
        "ahotts_version": ahotts_version,
        "africa_g2p_per": round(africa_g2p_per, 4) if africa_g2p_per is not None else None,
        "africa_g2p_n": africa_g2p_n,
        "harness_version": HARNESS_VERSION,
        "limit": limit if limit is not None else "full",
        "sampled": limit is None and sample_n is not None,
    }


def build_comparison(limit: Optional[int]) -> List[dict]:
    rows: List[dict] = []
    for lang in sorted(LANGS):
        try:
            rows.append(compare_lang(lang, limit))
        except Exception as exc:
            print(f"skip lang={lang}: {exc}", file=sys.stderr)
    rows.sort(key=lambda r: (r["lang"], r["dataset"]))
    return rows


def _fmt(per: Optional[float]) -> str:
    return f"{per:.4f}" if per is not None else "n/a"


_CATALAN_DIALECT_LABELS = {
    "ca": "central",
    "ca-x-balear": "balear",
    "ca-x-valencia": "valencian",
    "ca-x-occidental": "occidental (nord-occidental)",
}


def _catalan_dialect_table_lines(rows: List[dict],
                                  voices: Dict[str, Optional[str]]) -> List[str]:
    """Build the focused Catalan-dialect-vs-BSC-espeak markdown section
    from the subset of *rows* whose ``lang`` is one of the four 4catac
    dialect entries. Honest about voice availability: states plainly
    when a dialect voice fell back to the generic ``ca`` voice or was
    entirely unavailable, rather than presenting numbers as
    dialect-specific when they aren't."""
    dialect_rows = {r["lang"]: r for r in rows if r["lang"] in _CATALAN_DIALECT_LABELS}
    lines = [
        "## Catalan dialects vs espeak (BSC)",
        "",
        "The Barcelona Supercomputing Center (BSC) added Catalan dialect "
        "voices to espeak-ng (central, balearic, north-western, "
        "valencian). This table compares each o2i Catalan dialect spec "
        "against the matching espeak-ng dialect voice on the 4catac gold "
        "(expert human-annotated regional accents) — the same expert "
        "gold used for the `ca` row in the main table above.",
        "",
    ]
    dialect_voices_found = {t: v for t, v in voices.items()
                             if v not in (None, "ca")}
    if len(dialect_voices_found) == 3:
        lines.append(
            "All three BSC dialect voices (`ca-ba`, `ca-nw`, `ca-va`) were "
            "found on this machine's espeak-ng install; each dialect row "
            "below uses its own dialect-specific voice."
        )
    else:
        missing = [t for t, v in voices.items() if v in (None, "ca") and t != "ca"]
        if missing:
            lines.append(
                "Some BSC dialect voices were **not** found on this "
                "machine's espeak-ng install (`espeak-ng --voices=ca` "
                "listing). Affected dialects fall back to the generic "
                "`ca` voice, clearly labeled below — those rows do NOT "
                "reflect dialect-specific espeak output."
            )
        else:
            lines.append(
                "espeak-ng was unavailable in this run; all espeak "
                "columns below are `n/a`."
            )
    lines.append("")
    lines.append("| Dialect | o2i spec | espeak voice | N | o2i PER | espeak PER |")
    lines.append("|---|---|---|---:|---:|---:|")
    for tag, label in _CATALAN_DIALECT_LABELS.items():
        row = dialect_rows.get(tag)
        if row is None:
            lines.append(f"| {label} | {tag} | n/a | 0 | n/a | n/a |")
            continue
        voice = voices.get(tag)
        voice_label = voice if voice else "n/a"
        if voice == "ca" and tag != "ca":
            voice_label = "ca (fallback, no dialect voice found)"
        lines.append(
            f"| {label} | {tag} | {voice_label} | {row['n']} | "
            f"{_fmt(row['o2i_per'])} | {_fmt(row['espeak_per'])} |"
        )
    lines.append("")
    return lines


def write_comparison(rows: List[dict],
                      catalan_voices: Optional[Dict[str, Optional[str]]] = None) -> None:
    os.makedirs(os.path.dirname(COMPARISON_JSON), exist_ok=True)
    with open(COMPARISON_JSON, "w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    comparable = [r for r in rows if r["o2i_per"] is not None
                  and r["espeak_per"] is not None]
    wins = sum(1 for r in comparable if r["o2i_per"] < r["espeak_per"])

    lines = [
        "# Comparison to other G2P systems",
        "",
        "Committed cross-system comparison: orthography2ipa vs "
        "**espeak-ng**, **epitran**, **gruut**, **pycotovia** (Galician), "
        "and **ahotts-g2p** (Basque & Spanish) on the same gold "
        "datasets/loaders as [`docs/scoreboard.md`](scoreboard.md), using "
        "the FULL gold set of every mapped language (no cap — the same "
        "no-caps policy as the scoreboard; the one explicitly-flagged "
        "exception is the 617k-row Portal lexicon, scored on a "
        "fixed-seed sample and marked `sampled` in the JSON) — so the "
        "`o2i PER` column here matches the scoreboard's rows for the "
        "same language/dataset pair. Regenerate with:",
        "",
        "```bash",
        "pip install '.[compare]'  # epitran, gruut, pycotovia, "
        "ahotts-g2p — dev-only extra",
        "PYTHONPATH=$PWD python scripts/compare_systems.py --scoreboard",
        "```",
        "",
        "Machine-readable form: "
        "[`benchmarks/comparison.json`](../benchmarks/comparison.json).",
        "",
        "## Coverage",
        "",
        "Not every gold language has a mapping for every competitor "
        "system: espeak-ng, epitran, gruut, pycotovia, ahotts-g2p, and "
        "africa-g2p each cover a different, smaller subset of languages "
        "than orthography2ipa's 493 language codes. A missing mapping, or a system "
        "that isn't installed, is reported as `n/a` for that row rather "
        "than skipped or faked — this table never crashes and never "
        "silently drops a system, it just says when it has nothing to "
        "compare. `epitran`/`gruut`/`pycotovia`/`ahotts-g2p` are only "
        "installed via the dev-only `[compare]` extra; a committed run "
        "generated without them shows `n/a` in those columns for every "
        "row — that reflects the generating environment, not a claim "
        "those systems don't support the language.",
        "",
        "### ahotts-g2p output space (fairness)",
        "",
        "`ahotts-g2p` (Aholab / HiTZ AhoTTS G2P port; `eu`, `es`) emits "
        "its transcription in the StyleTTS2 single-character training "
        "convention, where the library's `MULTI` table folds affricates "
        "(`tʃ`→`C`, `ts`→`V`, `tʂ`→`P`), aspirates (`pʰ`→`H`, `kʰ`→`K`, "
        "`tʰ`→`T`) and **stress-marked vowels** (`ˈi`→`I` … `ˈu`→`U`) "
        "onto single ASCII letters — e.g. `kaixo`→`kajʃO`, "
        "`mundua`→`mundUa`, `etxea`→`eCEa`. Scoring that raw against IPA "
        "gold would charge a spurious error on every uppercase char, so "
        "the harness UNFOLDS it back to standard IPA (the inverse of "
        "`ahotts_g2p.phones.MULTI`, stress rendered as `ˈ` so the shared "
        "`normalize` strips it like every other system) BEFORE scoring: "
        "`kajʃO`→`kajʃˈo`, `mundUa`→`mundˈua`, `eCEa`→`etʃˈea`. All "
        "systems are thus compared in one IPA space. The two ahotts-g2p "
        "`version`s (`classic`/`modern`) produce near-identical output; "
        "the committed rows use `classic` (see the `ahotts_version` field "
        "in `benchmarks/comparison.json`). NOTE: the `eu` "
        "`hitz_basque_ipa` gold is authored by HiTZ/Aholab (UPV/EHU), the "
        "same lab behind AhoTTS, so ahotts-g2p's very low PER there is "
        "close to same-source; the independent `eu` `wikipron` "
        "(Wiktionary) row is the fairer external comparison point. The "
        "audio-only `pyahotts` package is NOT a comparison system here "
        "(no phoneme output); `ahotts-g2p` is the G2P port that "
        "supersedes it for this table.",
        "",
        "### africa-g2p coverage (honest limits)",
        "",
        "`africa-g2p` (Ghana NLP; rule-based G2P for ~400 African-language "
        "ISO 639-3 codes, derived from Hartell's *Alphabets of Africa*, "
        "UNESCO 1993) is not on PyPI, so it is not part of the `[compare]` "
        "extra — install it from a locally built wheel of the upstream "
        "checkout before regenerating this table (see the script's "
        "module docstring). Rows only appear for gold languages BOTH "
        "orthography2ipa and africa-g2p's own `registry()` cover; as of "
        "this run that intersection is small (10 languages: `arb`, "
        "`cop`, `hts`, `kab`, `ktz`, `lad`, `mfe`, `ngh`, `nup`, `tzm`) — "
        "most of africa-g2p's ~400 codes have no o2i gold registered yet, "
        "and most o2i gold languages are outside africa-g2p's coverage. "
        "None of these ten has a matching espeak-ng voice, epitran code, "
        "or gruut language on this machine either, so africa-g2p is "
        "currently the only comparison point for these rows — that is "
        "reported plainly rather than papered over with `n/a` silence.",
        "",
        "The `N` column is the number of unique gold words for that "
        "language/dataset pair; each system's own scored count can be "
        "slightly lower (a word it failed to transcribe is excluded from "
        "its PER, not counted as an error) — see the `*_n` fields in "
        "`benchmarks/comparison.json` for the exact per-system count.",
        "",
        "## Normalization",
        "",
        "Every system is scored with the identical normalization and PER "
        "metric orthography2ipa's own scoreboard uses "
        "(`scripts/benchmark.py:normalize`/`levenshtein`): NFC-normalize, "
        "strip stress marks (the length mark is retained), strip "
        "narrow-transcription diacritics "
        "(broad comparison), drop whitespace (segmentation-free), then "
        "score Levenshtein distance against the best-matching gold "
        "variant. No system is normalized differently or given a more "
        "forgiving metric.",
        "",
        "## Honesty",
        "",
        "This table includes languages where orthography2ipa **loses** to "
        "espeak-ng. Cherry-picking would make the comparison worthless.",
        "",
        "| Lang | Dataset | N | o2i PER | espeak PER | epitran PER | "
        "gruut PER | pycotovia PER | ahotts-g2p PER | africa-g2p PER |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['lang']} | {row['dataset']} | {row['n']} | "
            f"{_fmt(row['o2i_per'])} | {_fmt(row['espeak_per'])} | "
            f"{_fmt(row['epitran_per'])} | {_fmt(row['gruut_per'])} | "
            f"{_fmt(row.get('pycotovia_per'))} | "
            f"{_fmt(row.get('ahotts_per'))} | "
            f"{_fmt(row.get('africa_g2p_per'))} |"
        )
    lines.append("")
    if comparable:
        lines.append(
            f"**o2i beats espeak on {wins} of {len(comparable)} "
            "comparable languages.**"
        )
    else:
        lines.append(
            "No languages were comparable against espeak-ng in this run "
            "(espeak-ng unavailable or no overlapping mappings)."
        )
    lines.append("")
    lex_rows = [r for r in rows if r.get("o2i_lex_per") is not None
                or r.get("espeak_rules_per") is not None]
    lines.extend([
        "## Fair-comparison 2x2 (dictionary vs. rules)",
        "",
        "The table above conflates espeak-ng's letter-to-sound RULES with "
        "its hand-curated word-EXCEPTION list (o2i, by hard rule, ships no "
        "such list). This 2x2 isolates the dictionary's contribution on "
        "the same gold rows, for the languages where both extra columns "
        "are wired up (the `DICTSOURCE_LANG`-mapped subset — see the "
        "script's module docstring for how to enable `espeak_rules` via "
        "`scripts/build_espeak_rules_only.sh` and `o2i_lex` via "
        "`$ESPEAK_DICTSOURCE_PATH`):",
        "",
        "- `o2i` — orthography2ipa, rules only (unchanged from the main "
        "table).",
        "- `o2i_lex` — orthography2ipa + a runtime lexicon built from "
        "espeak-ng's OWN word-exception list, each word's IPA obtained "
        "from espeak-ng itself (o2i rules + espeak's dictionary).",
        "- `espeak` — espeak-ng, rules + its own word-exception dictionary "
        "(unchanged from the main table).",
        "- `espeak_rules` — espeak-ng with the word-exception dictionary "
        "emptied before compiling (rules only).",
        "",
        "| Lang | Dataset | N | o2i | o2i_lex | espeak | espeak_rules |",
        "|---|---|---:|---:|---:|---:|---:|",
    ])
    if lex_rows:
        for row in lex_rows:
            lines.append(
                f"| {row['lang']} | {row['dataset']} | {row['n']} | "
                f"{_fmt(row['o2i_per'])} | {_fmt(row.get('o2i_lex_per'))} | "
                f"{_fmt(row['espeak_per'])} | "
                f"{_fmt(row.get('espeak_rules_per'))} |"
            )
    else:
        lines.append(
            "| _(none)_ | | | | | | |"
        )
    lines.append("")
    lines.append(
        "Reading the four numbers together: `espeak - espeak_rules` is "
        "espeak-ng's dictionary contribution; `o2i_lex - o2i` is what the "
        "SAME dictionary is worth bolted onto o2i's rules. `o2i` vs "
        "`espeak_rules` is the fairest rules-only comparison; `o2i_lex` "
        "vs `espeak` is the fairest dictionary-included comparison."
    )
    lines.append("")
    lines.append(
        "**Licensing**: espeak-ng's dictsource word lists and the IPA "
        "derived from them are GPL. They are used here ONLY at comparison "
        "runtime — fetched/built into a local scratch cache "
        "(`$ESPEAK_RULES_DATA_PATH`, `.o2i_lex_cache/`), never committed "
        "to this repository and never shipped in orthography2ipa's own "
        "package or lexicons."
    )
    lines.append("")
    if catalan_voices is not None:
        lines.extend(_catalan_dialect_table_lines(rows, catalan_voices))
    os.makedirs(os.path.dirname(COMPARISON_MD), exist_ok=True)
    with open(COMPARISON_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--lang", default=None, choices=sorted(LANGS))
    ap.add_argument("--limit", type=int, default=None,
                    help="per-language gold cap for ad-hoc fast runs. "
                         "Default (unset) scores the FULL gold set — the "
                         "published comparison is uncapped, same no-caps "
                         "policy as benchmark.py --scoreboard (huge lexicons "
                         "with an explicit per-language sample_n are the "
                         "documented, visibly-flagged exception)")
    ap.add_argument("--list", action="store_true",
                    help="List languages this harness can compare")
    ap.add_argument("--scoreboard", action="store_true",
                    help="Run every mapped language and write "
                         "docs/comparison.md + benchmarks/comparison.json")
    args = ap.parse_args()

    if args.scoreboard:
        rows = build_comparison(args.limit)
        write_comparison(rows, catalan_voices=CATALAN_DIALECT_VOICES)
        print(f"wrote {len(rows)} rows to "
              f"{os.path.relpath(COMPARISON_MD, REPO_ROOT)} and "
              f"{os.path.relpath(COMPARISON_JSON, REPO_ROOT)}")
        return

    if args.list or not args.lang:
        for lang, cfg in sorted(LANGS.items()):
            print(f"{lang:10} espeak={cfg['espeak']} "
                  f"epitran={cfg['epitran']} gruut={cfg['gruut']} "
                  f"pycotovia={cfg.get('pycotovia')} "
                  f"ahotts={cfg.get('ahotts')} "
                  f"africa_g2p={cfg.get('africa_g2p')} "
                  f"dictsource_lang={DICTSOURCE_LANG.get(lang)}")
        return

    row = compare_lang(args.lang, args.limit)
    print(f"lang={row['lang']} n={row['n']} "
          f"o2i={_fmt(row['o2i_per'])} "
          f"o2i_lex={_fmt(row.get('o2i_lex_per'))} "
          f"espeak={_fmt(row['espeak_per'])} "
          f"espeak_rules={_fmt(row.get('espeak_rules_per'))} "
          f"epitran={_fmt(row['epitran_per'])} gruut={_fmt(row['gruut_per'])} "
          f"pycotovia={_fmt(row.get('pycotovia_per'))} "
          f"ahotts={_fmt(row.get('ahotts_per'))} "
          f"africa_g2p={_fmt(row.get('africa_g2p_per'))}")


if __name__ == "__main__":
    main()
