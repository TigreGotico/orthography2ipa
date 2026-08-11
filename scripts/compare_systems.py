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
import logging
import os
import shutil
import subprocess
import sys
from typing import Dict, List, Optional, Sequence, Tuple

sys.path.insert(0, os.path.dirname(__file__))
import benchmark  # noqa: E402  — shared dataset loaders, normalize(), levenshtein()

# epitran logs a WARNING (e.g. "lex_lookup (from flite) is not installed")
# on every per-word transliterate() call for some backends — harmless (it
# just means a fallback path is used) but at hundreds of thousands of
# words per run (e.g. the vox_communis datasets now scored per language,
# not just the one primary dataset) that's hundreds of thousands of log
# lines slowing the run down for no diagnostic value here.
logging.getLogger("epitran").setLevel(logging.ERROR)

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

def _score(hyps_and_golds: List[Tuple[Optional[str], List[str]]],
           lang: str = "") -> Tuple[Optional[float], int]:
    """Mean PER over rows with a non-``None`` hypothesis, using
    ``benchmark.normalize``/``benchmark.levenshtein`` (broad, stress
    stripped — matching ``benchmark.py --scoreboard``'s default mode).
    Returns ``(per, covered)``; ``per`` is ``None`` when nothing scored."""
    extra = benchmark._prosody_marks(lang) if lang else ""
    per_sum, covered = 0.0, 0
    for hyp, golds in hyps_and_golds:
        if not hyp:
            continue
        hyp_n = benchmark.normalize(hyp, strip_stress=True, broad=True, extra_strip=extra)
        if not hyp_n:
            continue
        covered += 1
        per_sum += min(
            benchmark.levenshtein(
                hyp_n, benchmark.normalize(g, True, True, extra_strip=extra))
            / max(len(benchmark.normalize(g, True, True,
                                          extra_strip=extra)), 1)
            for g in golds
        )
    if covered == 0:
        return None, 0
    return per_sum / covered, covered


#: Datasets whose gold IS a competitor system's own output — scoring that
#: system against its own generator's output is tautological (it scores
#: ~0 by construction, not because it is accurate). Rather than silently
#: reporting ``n/a`` (which reads as "system unavailable"), these cells are
#: flagged ``same_source`` and rendered as ``same-source`` in the docs — a
#: different, honest reason for having no comparable number.
#:
#: - espeak/espeak_rules are excluded wherever ``benchmark.provenance_for``
#:   tags the dataset+language ``espeak-derived``.
#: - epitran is excluded wherever the tier is ``epitran-derived``.
#: - ahotts-g2p is excluded on ``hitz_basque_ipa`` specifically: that gold
#:   is HiTZ/Aholab's own ahoNT automatic phonemizer output — the same lab
#:   that authors AhoTTS (see the module docstring's ahotts-g2p section).
_AHOTTS_SAME_SOURCE_DATASETS = frozenset({"hitz_basque_ipa"})

#: Datasets whose gold text was drafted by the SAME Claude lineage that
#: authored orthography2ipa's own dialect specs (see benchmark.py's
#: ``load_arabic_tts``/``load_portuguese_tts``/gold20 provenance notes,
#: which call this relationship "near-circular"). This is not the general
#: ``llm-generated`` tier as a whole — Claude drafted every dataset in
#: that tier, ``mirandese_dict`` and ``barranquenho_dict`` included, so
#: "which LLM" does not distinguish them. What distinguishes them is
#: whether o2i's OWN output fed back into the gold:
#: ``load_mirandese_dict``'s docstring documents that it was "NOT produced
#: by a phonemizer, by orthography2ipa, or by any downstream o2i
#: consumer — so scoring o2i against it is not circular", so it stays
#: OUT of this set. ``barranquenho_dict`` is the opposite case:
#: ``load_barranquenho_dict``'s docstring says the near-zero PER o2i
#: scores against it "suggests their IPA column is itself o2i-aligned —
#: treat every number from this dataset as agreement, not correctness".
#: It has no ``LANGS`` entry today so no row ever reaches this function
#: for it, but if it ever gains one it MUST join this set — the loader's
#: own documentation already calls the comparison circular. Only the
#: three datasets below currently have both a ``LANGS`` entry and a
#: documented near-circular relationship with o2i's own rules, so only
#: they get o2i flagged same-source: scoring o2i against a gold drafted
#: with the same knowledge that went into o2i's own rules measures
#: self-agreement, not correctness.
_O2I_SAME_SOURCE_DATASETS = frozenset({
    "arabic_tts", "portuguese_tts", "gold20_arabic",
})

#: Provenance tiers produced by a process independent of any G2P system —
#: a genuine external reference, not another tool's (or o2i's own) output.
#: These are the only tiers a "beats espeak" claim can be made from without
#: a qualifier. See benchmark.RELIABILITY_TIERS for the full tier order.
_GOLD_TIERS = frozenset({"expert-human", "lexicon-derived", "crowd-scraped"})

#: The remaining tiers: the reference IS another tool's output (or an
#: LLM's, with no error model at all). A row on one of these measures
#: agreement with whatever produced the reference, not correctness — see
#: "Machine-generated-reference rows are agreement, not accuracy" below.
#: ``machine-generated`` is included here (not just the competitor/LLM
#: tiers) because in this harness's registered datasets it is ALSO always
#: another automatic phonemizer's output (e.g. HiTZ's ahoNT for
#: ``hitz_basque_ipa``) rather than a human- or corpus-derived reference.
_AGREEMENT_TIERS = frozenset({
    "machine-generated", "espeak-derived", "epitran-derived", "llm-generated",
})


def _primary_rows(rows: List[dict]) -> List[dict]:
    """One row per language: the row for that language's CONFIGURED
    primary dataset (``LANGS[lang]["dataset"]``), which is always first in
    ``compare_lang``'s output. Used for the top-line aggregate so a
    language with many registered golds (see ``_robustness_section``
    instead for the full multi-gold breakdown) is counted exactly once —
    counting every row would let languages with more registered datasets
    dominate the aggregate."""
    primary_by_lang = {
        lang: cfg["dataset"][0] for lang, cfg in LANGS.items()
    }
    out = []
    for r in rows:
        if primary_by_lang.get(r["lang"]) == r["dataset"]:
            out.append(r)
    return out


def _comparable_and_wins(rows: List[dict]) -> Tuple[List[dict], int]:
    """espeak-comparable rows (both PERs present, neither same-source) from
    *rows*, and how many of them o2i wins on."""
    comparable = [
        r for r in rows
        if r["o2i_per"] is not None and r["espeak_per"] is not None
        and not r.get("espeak_same_source") and not r.get("o2i_same_source")
    ]
    wins = sum(1 for r in comparable if r["o2i_per"] < r["espeak_per"])
    return comparable, wins


def _same_source_flags(dataset_name: str, loader_lang: str) -> Dict[str, bool]:
    """Which comparison systems would be scored against their OWN output
    for this ``(dataset, loader_lang)`` pair — see
    ``_AHOTTS_SAME_SOURCE_DATASETS``/``_O2I_SAME_SOURCE_DATASETS`` above
    for the full rules.

    Datasets with no registered ``PROVENANCE`` entry (only possible in
    tests, which register throwaway fake datasets — every real dataset in
    ``benchmark.DATASETS`` is enforced to have one) are treated as
    non-same-source rather than raising.
    """
    try:
        tier = benchmark.provenance_for(dataset_name, loader_lang)
    except KeyError:
        tier = None
    return {
        "espeak": tier == "espeak-derived",
        "espeak_rules": tier == "espeak-derived",
        "epitran": tier == "epitran-derived",
        "ahotts": dataset_name in _AHOTTS_SAME_SOURCE_DATASETS,
        "o2i": dataset_name in _O2I_SAME_SOURCE_DATASETS,
    }


def _provenance_tier_or_none(dataset_name: str, loader_lang: str) -> Optional[str]:
    try:
        return benchmark.provenance_for(dataset_name, loader_lang)
    except KeyError:
        return None


def _datasets_for_loader_lang(loader_lang: str) -> List[str]:
    """Every ``benchmark.DATASETS`` name whose language list includes
    *loader_lang*, sorted for deterministic row order."""
    return sorted(
        name for name, (_loader, langs) in benchmark.DATASETS.items()
        if loader_lang in langs
    )


def compare_lang(lang: str, limit: Optional[int]) -> List[dict]:
    """Run *lang* through every available system on EVERY registered gold
    dataset for its underlying language — not just the one dataset picked
    for the main scoreboard row. Returns a list of row dicts (one per
    matching dataset), each with per-system PER (or ``None`` == "n/a", or
    flagged ``*_same_source`` when a system's own output IS the gold — see
    ``_same_source_flags``).

    The language's configured ``dataset`` entry is always first in the
    returned list (keeping existing single-row consumers/ordering
    unaffected); any additional datasets ``benchmark.DATASETS`` registers
    for the same loader language follow, sorted by name.
    """
    cfg = LANGS[lang]
    primary_dataset, loader_lang = cfg["dataset"]
    dataset_names = [primary_dataset] + [
        d for d in _datasets_for_loader_lang(loader_lang) if d != primary_dataset
    ]
    return [
        _compare_lang_dataset(lang, cfg, dataset_name, loader_lang, limit)
        for dataset_name in dataset_names
    ]


def _compare_lang_dataset(lang: str, cfg: dict, dataset_name: str,
                           loader_lang: str, limit: Optional[int]) -> dict:
    """Score *lang* against ONE gold dataset (see ``compare_lang`` for the
    multi-dataset iteration this backs)."""
    loader, _ = benchmark.DATASETS[dataset_name]
    same_source = _same_source_flags(dataset_name, loader_lang)
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

    use_espeak = (cfg["espeak"] is not None and espeak_available()
                  and not same_source["espeak"])
    use_espeak_rules = (cfg["espeak"] is not None and espeak_rules_available()
                         and not same_source["espeak_rules"])
    use_epitran = cfg["epitran"] is not None and not same_source["epitran"]
    use_gruut = cfg["gruut"] is not None
    use_pycotovia = cfg.get("pycotovia") is not None
    use_ahotts = cfg.get("ahotts") is not None and not same_source["ahotts"]
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

    o2i_per, o2i_n = _score(o2i_rows, lang=lang)
    o2i_lex_per, o2i_lex_n = (
        _score(o2i_lex_rows, lang=lang) if use_o2i_lex else (None, 0))
    espeak_per, espeak_n = _score(espeak_rows, lang=lang) if use_espeak else (None, 0)
    espeak_rules_per, espeak_rules_n = (
        _score(espeak_rules_rows, lang=lang) if use_espeak_rules else (None, 0))
    epitran_per, epitran_n = _score(epitran_rows, lang=lang) if use_epitran else (None, 0)
    gruut_per, gruut_n = _score(gruut_rows, lang=lang) if use_gruut else (None, 0)
    pycotovia_per, pycotovia_n = (
        _score(pycotovia_rows, lang=lang) if use_pycotovia else (None, 0))
    ahotts_per, ahotts_n = (
        _score(ahotts_rows, lang=lang) if use_ahotts else (None, 0))
    ahotts_version = cfg["ahotts"]["version"] if use_ahotts else None
    africa_g2p_per, africa_g2p_n = (
        _score(africa_g2p_rows, lang=lang) if use_africa_g2p else (None, 0))

    return {
        "lang": lang,
        "dataset": dataset_name,
        "n": len(words),
        "o2i_per": round(o2i_per, 4) if o2i_per is not None else None,
        "o2i_n": o2i_n,
        "o2i_same_source": same_source["o2i"],
        "o2i_lex_per": round(o2i_lex_per, 4) if o2i_lex_per is not None else None,
        "o2i_lex_n": o2i_lex_n,
        "espeak_per": round(espeak_per, 4) if espeak_per is not None else None,
        "espeak_n": espeak_n,
        "espeak_voice": cfg["espeak"],
        "espeak_same_source": same_source["espeak"],
        "espeak_rules_per": round(espeak_rules_per, 4) if espeak_rules_per is not None else None,
        "espeak_rules_n": espeak_rules_n,
        "espeak_rules_same_source": same_source["espeak_rules"],
        "epitran_per": round(epitran_per, 4) if epitran_per is not None else None,
        "epitran_n": epitran_n,
        "epitran_same_source": same_source["epitran"],
        "gruut_per": round(gruut_per, 4) if gruut_per is not None else None,
        "gruut_n": gruut_n,
        "pycotovia_per": round(pycotovia_per, 4) if pycotovia_per is not None else None,
        "pycotovia_n": pycotovia_n,
        "ahotts_per": round(ahotts_per, 4) if ahotts_per is not None else None,
        "ahotts_n": ahotts_n,
        "ahotts_version": ahotts_version,
        "ahotts_same_source": same_source["ahotts"],
        "africa_g2p_per": round(africa_g2p_per, 4) if africa_g2p_per is not None else None,
        "africa_g2p_n": africa_g2p_n,
        "provenance_tier": _provenance_tier_or_none(dataset_name, loader_lang),
        "harness_version": HARNESS_VERSION,
        "limit": limit if limit is not None else "full",
        "sampled": limit is None and sample_n is not None,
    }


def build_comparison(limit: Optional[int],
                     only_langs: Optional[Sequence[str]] = None) -> List[dict]:
    """Score every mapped language against the external systems.

    ``only_langs`` restricts the run to a subset, exactly as
    ``benchmark.build_scoreboard``'s ``only_langs`` does. A full pass runs
    every external system over every gold row of 33 languages and takes
    hours, so a targeted rerun is the practical way to refresh a handful of
    rows; the caller then MERGES the result into the committed set (see
    :func:`merge_comparison_rows`). No row depends on which others ran with
    it, so a subset row is scored identically to a full-run row.
    """
    rows: List[dict] = []
    for lang in sorted(LANGS):
        if only_langs is not None and lang not in only_langs:
            continue
        try:
            rows.extend(compare_lang(lang, limit))
        except Exception as exc:
            print(f"skip lang={lang}: {exc}", file=sys.stderr)
    rows.sort(key=lambda r: (r["lang"], r["dataset"]))
    return rows


def merge_comparison_rows(old: List[dict], new: List[dict]) -> List[dict]:
    """Overlay freshly-scored *new* rows onto the committed *old* set.

    Keyed on ``(lang, dataset)``, the comparison board's identity, and a new
    row REPLACES the old one wholesale rather than patching it field by
    field: a row is one live run against espeak-ng/epitran/gruut, and
    half-refreshing one would silently mix two runs' numbers. Rows only in
    *old* are carried through untouched, which is what makes ``--lang``
    safe. Mirrors :func:`benchmark.merge_scoreboard_rows`.
    """
    merged = {(r["lang"], r["dataset"]): r for r in old}
    for row in new:
        merged[(row["lang"], row["dataset"])] = row
    return sorted(merged.values(), key=lambda r: (r["lang"], r["dataset"]))


def read_comparison_rows() -> List[dict]:
    """The committed comparison rows, or ``[]`` if none are written yet."""
    if not os.path.exists(COMPARISON_JSON):
        return []
    with open(COMPARISON_JSON, encoding="utf-8") as fh:
        return json.load(fh)


def _fmt(per: Optional[float]) -> str:
    return f"{per:.4f}" if per is not None else "n/a"


def _cell(row: dict, system: str) -> str:
    """Format one system's cell for *row*, distinguishing an honestly
    tautological ``same-source`` comparison (the system's own output IS
    the gold — see ``_same_source_flags``) from a plain ``n/a`` (the
    system is unavailable or has no mapping for this language)."""
    if row.get(f"{system}_same_source"):
        return "same-source"
    return _fmt(row.get(f"{system}_per"))


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


def _robustness_section(rows: List[dict]) -> List[str]:
    """For every language scored against espeak on 2+ datasets, report the
    win/loss split — the mandatory honesty check: a language that beats
    espeak on one gold and loses on another must show BOTH, not just the
    flattering row. Languages with only one espeak-comparable dataset (or
    none) are skipped — there is nothing to reconcile."""
    by_lang: Dict[str, List[dict]] = {}
    for r in rows:
        if (r.get("espeak_same_source") or r.get("o2i_same_source")
                or r.get("espeak_per") is None):
            continue
        by_lang.setdefault(r["lang"], []).append(r)

    lines = ["## Robustness across golds", ""]
    lines.append(
        "A system winning on one gold and losing on another for the SAME "
        "language is real signal, not noise to average away. Every "
        "language with 2+ espeak-comparable gold datasets is listed "
        "below with its exact win/loss split (same-source cells excluded "
        "— they are never comparable, see above)."
    )
    lines.append("")
    multi = {lang: rs for lang, rs in by_lang.items() if len(rs) >= 2}
    if not multi:
        lines.append(
            "No language in this run had 2+ espeak-comparable gold "
            "datasets."
        )
        lines.append("")
        return lines
    for lang in sorted(multi):
        rs = sorted(multi[lang], key=lambda r: r["dataset"])
        wins = [r["dataset"] for r in rs if r["o2i_per"] < r["espeak_per"]]
        losses = [r["dataset"] for r in rs if r["o2i_per"] >= r["espeak_per"]]
        verdict = ("wins on all golds" if not losses else
                    "loses on all golds" if not wins else
                    "MIXED — wins on some golds, loses on others")
        lines.append(f"- **`{lang}`** ({verdict}):")
        for r in rs:
            outcome = "o2i wins" if r["dataset"] in wins else "o2i loses"
            lines.append(
                f"  - `{r['dataset']}` (n={r['n']}, tier="
                f"{r.get('provenance_tier') or '?'}): o2i "
                f"{_fmt(r['o2i_per'])} vs espeak {_fmt(r['espeak_per'])} "
                f"— {outcome}"
            )
    lines.append("")
    return lines


#: How far a fresh `o2i_per` may drift from `benchmarks/results.json`'s
#: `per` for the same (lang, dataset) before it counts as a disagreement
#: worth naming rather than rounding noise.
_SCOREBOARD_DRIFT_TOLERANCE = 0.002


def _scoreboard_staleness_note(rows: List[dict]) -> str:
    """Compare this run's freshly-computed `o2i_per` against the committed
    `benchmarks/results.json` for every shared (lang, dataset) pair and
    report the truth, instead of asserting a static "matches the
    scoreboard" claim that silently goes stale the next time an engine
    change updates compare_systems.py's numbers without a matching
    scripts/benchmark.py --scoreboard regeneration for that row (this is
    exactly what happened to `ca`/`ipa_childes` and `ca`/`vox_communis`
    after PR #802, which only regenerated `ca`/`4catac`).
    """
    try:
        with open(benchmark.SCOREBOARD_JSON, encoding="utf-8") as fh:
            scoreboard_rows = json.load(fh)
    except (OSError, json.JSONDecodeError):
        return (
            "`benchmarks/results.json` could not be read in this run — "
            "the match claim below is unverified."
        )
    scoreboard_per = {
        (r["lang"], r["dataset"]): r.get("per") for r in scoreboard_rows
    }
    stale = []
    for row in rows:
        key = (row["lang"], row["dataset"])
        if key not in scoreboard_per:
            continue
        sb_per = scoreboard_per[key]
        o2i_per = row["o2i_per"]
        if sb_per is None or o2i_per is None:
            if sb_per != o2i_per:
                stale.append((row["lang"], row["dataset"], o2i_per, sb_per))
            continue
        if abs(sb_per - o2i_per) > _SCOREBOARD_DRIFT_TOLERANCE:
            stale.append((row["lang"], row["dataset"], o2i_per, sb_per))

    if not stale:
        return (
            "The `o2i PER` column here matches "
            "[`benchmarks/results.json`](../benchmarks/results.json)'s "
            "`per` for every shared language/dataset pair in this run."
        )
    stale.sort()
    listed = "; ".join(
        f"`{lang}`/`{dataset}` (here {_fmt(o2i_per)}, results.json "
        f"{_fmt(sb_per)})"
        for lang, dataset, o2i_per, sb_per in stale
    )
    return (
        f"The `o2i PER` column here matches "
        f"[`benchmarks/results.json`](../benchmarks/results.json)'s `per` "
        f"for most shared language/dataset pairs, EXCEPT the "
        f"{len(stale)} listed below — those `benchmarks/results.json` "
        f"rows are stale (a prior PR changed the engine but did not "
        f"regenerate every affected row there; see e.g. PR #802's "
        f"`ca`/`4catac`-only regeneration). The numbers in THIS table "
        f"reflect the current engine via a live run; "
        f"`benchmarks/results.json` needs a matching regeneration for: "
        f"{listed}."
    )


def write_comparison(rows: List[dict],
                      catalan_voices: Optional[Dict[str, Optional[str]]] = None) -> None:
    os.makedirs(os.path.dirname(COMPARISON_JSON), exist_ok=True)
    with open(COMPARISON_JSON, "w", encoding="utf-8") as fh:
        json.dump(rows, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    primary = _primary_rows(rows)
    gold_primary = [r for r in primary if r.get("provenance_tier") in _GOLD_TIERS]
    agreement_primary = [r for r in primary
                          if r.get("provenance_tier") in _AGREEMENT_TIERS]
    gold_comparable, gold_wins = _comparable_and_wins(gold_primary)
    agreement_comparable, agreement_wins = _comparable_and_wins(agreement_primary)
    scoreboard_note = _scoreboard_staleness_note(rows)

    lines = [
        "# Comparison to other G2P systems",
        "",
        "Committed cross-system comparison: orthography2ipa vs "
        "**espeak-ng**, **epitran**, **gruut**, **pycotovia** (Galician), "
        "and **ahotts-g2p** (Basque & Spanish) on the same gold "
        "datasets/loaders as [`docs/scoreboard.md`](scoreboard.md), using "
        "the FULL gold set of every mapped language (no cap — the same "
        "no-caps policy as the scoreboard; the one explicitly-flagged "
        "exception is `pt-PT`, whose 598k-row `portuguese_unified` "
        "('Portal lexicon') made a per-word-external-system full pass "
        "impractical, so its config sets a `sample_n` — and because "
        "`sample_n` is a per-LANGUAGE cap, not a per-dataset one, it "
        "now applies to every dataset registered for `pt-PT`, not just "
        "`portuguese_unified`; all of them are marked `sampled` in the "
        "JSON). "
        + scoreboard_note + " Regenerate with:",
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
        "**Every gold dataset a language has, not one.** Earlier versions "
        "of this table picked a single 'battleground' gold per language. "
        "Multiple rows per language are now committed — one per "
        "registered gold dataset for that language — so a system winning "
        "on one gold and losing on another for the SAME language is "
        "visible here, not hidden by picking the flattering row.",
        "",
        "**`same-source` cells**: a cell reads `same-source` (never "
        "`n/a`) when the gold dataset IS that system's own output — "
        "e.g. scoring `espeak` against `ipa_babylm` (espeak-derived) or "
        "`ahotts-g2p` against `hitz_basque_ipa` (HiTZ's own ahoNT "
        "phonemizer output, same lab as AhoTTS). Scoring a system "
        "against its own generator is tautological — it would score "
        "near-zero by construction, not because it is accurate — so "
        "that comparison is refused rather than reported. The same rule "
        "applies to **o2i itself**: `arabic_tts`, `portuguese_tts` and "
        "`gold20_arabic` were drafted by the same Claude lineage that "
        "authored orthography2ipa's own Arabic/Portuguese dialect specs "
        "(near-circular per the datasets' provenance notes in "
        "`scripts/benchmark.py`) — a spec author's own generated gold "
        "measures self-agreement with the spec, not correctness, so the "
        "`o2i PER` cell on those rows also reads `same-source`.",
        "",
        "**Machine-generated-reference rows are agreement, not "
        "accuracy.** Rows whose gold is itself another phonemizer's or "
        "an LLM's output (see each dataset's `provenance_tier` in "
        "`benchmarks/comparison.json`, and `docs/scoreboard.md`'s "
        "provenance legend) measure how much a system agrees with the "
        "tool that generated the gold — not whether either is correct. "
        "A win on such a row is not a claim of accuracy.",
        "",
        "| Lang | Dataset | N | o2i PER | espeak PER | epitran PER | "
        "gruut PER | pycotovia PER | ahotts-g2p PER | africa-g2p PER |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['lang']} | {row['dataset']} | {row['n']} | "
            f"{_cell(row, 'o2i')} | {_cell(row, 'espeak')} | "
            f"{_cell(row, 'epitran')} | {_fmt(row['gruut_per'])} | "
            f"{_fmt(row.get('pycotovia_per'))} | "
            f"{_cell(row, 'ahotts')} | "
            f"{_fmt(row.get('africa_g2p_per'))} |"
        )
    lines.append("")
    lines.append(
        "Counted over distinct LANGUAGES (one row per language: its "
        "configured primary gold dataset — see `_primary_rows`), never "
        "over table rows, and split by whether that primary gold is an "
        "independent reference or another tool's/LLM's output:"
    )
    lines.append("")
    if gold_comparable:
        lines.append(
            f"- **Gold-tier** (expert-human / lexicon-derived / "
            f"crowd-scraped primary gold): o2i beats espeak on "
            f"{gold_wins} of {len(gold_comparable)} comparable languages."
        )
    else:
        lines.append(
            "- **Gold-tier**: no language's primary gold was "
            "espeak-comparable in this run."
        )
    if agreement_comparable:
        lines.append(
            f"- **Agreement-tier** (machine-generated / espeak-derived / "
            f"epitran-derived / llm-generated primary gold — measures "
            f"agreement with the generating tool, not accuracy; see "
            f"\"Honesty\" above): o2i beats espeak on {agreement_wins} of "
            f"{len(agreement_comparable)} comparable languages."
        )
    else:
        lines.append(
            "- **Agreement-tier**: no language's primary gold was "
            "espeak-comparable in this run."
        )
    lines.append("")
    lines.extend(_robustness_section(rows))
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
                f"{_cell(row, 'espeak')} | "
                f"{_cell(row, 'espeak_rules')} |"
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
        # --lang narrows the run to one language and MERGES the result into
        # the committed board; without it the whole board is rescored from
        # scratch. Before this was wired up, --scoreboard silently IGNORED
        # --lang and rebuilt all 33 languages — hours of espeak-ng and
        # epitran subprocesses — which in practice meant a one-language
        # refresh was never run and rows went stale instead.
        rows = build_comparison(
            args.limit, only_langs=[args.lang] if args.lang else None)
        if args.lang:
            print(f"merging {len(rows)} rescored rows into the committed "
                  f"comparison board", file=sys.stderr)
            rows = merge_comparison_rows(read_comparison_rows(), rows)
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

    for row in compare_lang(args.lang, args.limit):
        print(f"lang={row['lang']} dataset={row['dataset']} n={row['n']} "
              f"o2i={_fmt(row['o2i_per'])} "
              f"o2i_lex={_fmt(row.get('o2i_lex_per'))} "
              f"espeak={_cell(row, 'espeak')} "
              f"espeak_rules={_cell(row, 'espeak_rules')} "
              f"epitran={_cell(row, 'epitran')} gruut={_fmt(row['gruut_per'])} "
              f"pycotovia={_fmt(row.get('pycotovia_per'))} "
              f"ahotts={_cell(row, 'ahotts')} "
              f"africa_g2p={_fmt(row.get('africa_g2p_per'))}")


if __name__ == "__main__":
    main()
