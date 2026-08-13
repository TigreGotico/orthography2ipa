#!/usr/bin/env python3
"""Compare orthography2ipa against other G2P systems on the same gold rows.

Runs the SAME gold word/IPA pairs used by ``scripts/benchmark.py`` through
several systems — orthography2ipa, espeak-ng, epitran, gruut, pycotovia,
ahotts-g2p, africa-g2p, and the o2i-downstream family (arbtok, tugaphone,
g2p_barranquenho, mwl_phonemizer) — and scores every system with the exact
same normalization
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
- **o2i-downstream family** (arbtok, tugaphone, g2p_barranquenho,
  mwl_phonemizer): TigreGotico repos built directly on this repo's own
  ``orthography2ipa.G2P`` lattice, imported lazily and scored under the
  SAME lazy-import + n/a-degrade discipline as every optional system
  above. Because they share o2i's lattice, they ALSO share o2i's
  same-source exposure on gold drafted from the same knowledge that
  informed o2i's own rules (see ``_O2I_SAME_SOURCE_DATASETS`` and the
  module note by ``arbtok_transcribe`` for the full per-engine lexicon
  audit — arbtok's tiny closed-class ``WORD_EXCEPTIONS``, tugaphone's
  always-on ``tugalex`` lexicon excluded from ranking like stock
  ``espeak``, g2p_barranquenho and mwl_phonemizer both lexicon-free by
  default). They are wired in anyway because a family member can still
  be a real comparison point against a gold that is genuinely
  independent of o2i (e.g. mwl_phonemizer vs. the native-speaker
  ``mirandese_g2p`` gold, or arbtok vs. the diacritized-WikiPron ``ar``
  gold below) — and because "n/a" on a row that HAS a downstream engine
  is itself information the owner asked not to drop.

Normalization (identical across every system above, see ``benchmark.normalize``
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

Where things live
-----------------

The module reads top to bottom as config -> engines -> policy -> rendering.
Each section below carries a ``# ─── name ───`` header:

``fair-comparison 2x2`` / ``language mapping``
    Environment knobs, and ``LANGS`` — the one table mapping an o2i language
    tag to its gold dataset and to each system's per-language code. Adding a
    language is an edit here and nowhere else.
``espeak-ng`` … ``gruut``
    One section per comparison engine: a ``<name>_transcribe(word, cfg)``
    function that returns IPA or ``None``, plus whatever instance cache and
    availability check that engine needs. Every one degrades to ``None``
    rather than raising, so a missing library is an ``n/a`` cell.
``o2i_lex``
    Builds the runtime lexicon for the ``o2i_lex`` column from espeak-ng's
    own wordlist.
``scoring``
    ``_score`` — the shared PER metric, identical for every system.
``same-source policy``
    Which systems must be REFUSED a number on which datasets, and why.
``running the comparison``
    ``PER_WORD_ENGINES`` (the engine registry), the per-language/per-dataset
    passes, and ``_build_row`` — which defines the committed
    ``benchmarks/comparison.json`` schema.
``board persistence``
    Build the full board, merge a partial rerun into the committed one,
    read it back.
``rendering`` / ``ranking policy``
    Everything that turns rows into ``docs/comparison.md``, and the rules
    for what may be called a winner (lexicon-free only).
"""
from __future__ import annotations

import argparse
import importlib.metadata
import json
import logging
import os
import shutil
import subprocess
import sys
from typing import Any, Dict, List, NamedTuple, Optional, Sequence, Tuple

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
    "es": "es",
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
    # o2i's separate "en-GB" spec/gold (a DIFFERENT wikipron pull than the
    # "en" row above — see wikipron's own "en" vs "en-GB" locale split in
    # benchmark.py's DATASETS; the two gold sets are similar size but not
    # identical rows, which is why espeak's PER differs by several points
    # between the "en" and "en-GB" rows on this board — not measurement
    # noise, two different gold files).
    "en-GB": {"dataset": ("wikipron", "en-GB"), "espeak": "en-gb",
              "epitran": "eng-Latn", "gruut": "en-gb"},
    "es": {"dataset": ("wikipron", "es"), "espeak": "es",
           "epitran": "spa-Latn", "gruut": "es",
           "ahotts": {"lang": "es", "version": "classic"},
           # Cotovia's own Spanish mode (pycotovia.Phonemizer(lang="es"))
           # — Cotovia is a Galician/Spanish system per Univ. de Vigo/GTM,
           # so this row is its Spanish-mode showing, alongside the
           # Galician "gl" row's native-mode showing.
           "pycotovia": "es"},
    # sample_n: the unified pt gold is ~116k pt-PT words; epitran/gruut transcribe
    # word-by-word in-process and cannot batch, so a full pass is days of
    # wall clock. Scored on a fixed-seed (loader SAMPLE_SEED) sample of
    # 3000 — an EXPLICIT, row-flagged sample, not a silent cap.
    "pt-PT": {"dataset": ("portuguese_unified", "pt-PT"), "espeak": "pt",
              "epitran": "por-Latn", "gruut": "pt", "sample_n": 3000,
              # tugaphone: not o2i-same-source (portuguese_unified is
              # independent of o2i's own gold-generation, unlike
              # portuguese_tts) but its curated tugalex lexicon is always
              # on — see the "lexicon disposition" note above
              # arbtok_transcribe/tugaphone_transcribe/etc.
              "tugaphone": "pt-PT"},
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
    # Mirandese (mwl): scored against ``mirandese_g2p`` — a native-speaker,
    # human-collected gold that is a SEPARATE source from o2i (see
    # benchmark.load_mirandese's docstring), so this row is a real
    # comparison for BOTH o2i and mwl_phonemizer, not same-source. o2i's
    # own ``mwl`` spec is what mwl_phonemizer's lattice stage runs on, so
    # the two will tend to agree on cases the shared lattice handles the
    # same way — that is expected, not a bug; mwl_phonemizer's own stages
    # (dialect selection, syllabification, punctuation handling) are what
    # can still diverge it from raw o2i.
    "mwl": {"dataset": ("mirandese_g2p", "mwl"), "espeak": None,
            "epitran": None, "gruut": None, "mwl_phonemizer": "mwl"},
    # Barranquenho (ext-PT-x-barrancos): the ONLY registered gold,
    # ``barranquenho_dict``, is documented same-source for o2i (see
    # ``_O2I_SAME_SOURCE_DATASETS`` above) — its own loader docstring says
    # the IPA column "suggests their IPA column is itself o2i-aligned:
    # treat every number from this dataset as agreement, not correctness".
    # g2p_barranquenho is built directly on o2i's own
    # ext-PT-x-barrancos spec, so it inherits the exact same exposure —
    # wired in and correctly flagged same-source (see
    # ``_same_source_flags``'s "barranquenho" key) rather than silently
    # dropped or, worse, presented as a real comparison.
    "ext-PT-x-barrancos": {"dataset": ("barranquenho_dict", "ext-PT-x-barrancos"),
                            "espeak": None, "epitran": None, "gruut": None,
                            "barranquenho": "ext-PT-x-barrancos"},
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
            "epitran": None, "gruut": None,
            # arbtok: same-source on this row (arabic_tts is in
            # _ARBTOK_SAME_SOURCE_DATASETS, same as o2i itself — see the
            # module note by arbtok_transcribe). Kept wired in anyway so a
            # genuinely independent Arabic gold (if one lands — see
            # scripts/benchmark.py's Arabic-gold provenance notes) scores
            # both o2i and arbtok for real, without further code changes.
            "arbtok": "arb"},
    # INDEPENDENT Arabic gold: benchmark.load_wikipron_ar_diacritized's IPA
    # column is WikiPron/Wiktionary's own — not o2i-lineage, not
    # machine-pinned to o2i output like arabic_tts/gold20_arabic are — so
    # THIS row, unlike "arb" above, is a real comparison point for both
    # o2i and arbtok. See that loader's docstring for why the row exists
    # at all: raw WikiPron Arabic headwords carry NO harakat (0/3000
    # sampled), so scoring against them unmodified would measure "can't
    # vowelize unvocalized text", not phonemization quality; the loader
    # restores harakat on the INPUT (not the gold) with text2tashkeel
    # before scoring. Caveat, disclosed rather than hidden: text2tashkeel
    # is itself a TigreGotico tool, and arbtok's own default pipeline
    # (``diacritize=True``) uses the SAME diacritizer internally — so a
    # diacritization error the two share is not this row's independence
    # signal, only the underlying IPA gold's is. Still a strictly fairer,
    # strictly more independent comparison than "arb" above.
    # C4 reproducibility: the diacritized INPUT text is cached to a TSV
    # by benchmark.load_wikipron_ar_diacritized (CACHE_DIR-scoped, not
    # committed to this repo — it is a derived artifact of a specific
    # text2tashkeel model run, not gold data). Pin the model version
    # actually used to generate the currently-committed board's cache
    # here rather than leaving it silently unpinned: text2tashkeel
    # 0.3.0a1 (rawi default model), recorded at generation time via
    # ``importlib.metadata.version("text2tashkeel")``. Delete the cached
    # TSV to force re-diacritization if this version note and the
    # installed version drift apart.
    # sample_n: raw wikipron ``ar`` is ~17.5k words and arbtok/o2i score
    # in-process, per-word (arbtok additionally runs the ONNX diacritizer
    # on every word for the raw-wikipron and diacritized rows) — a full
    # pass is impractical wall clock, same rationale as pt-PT above. An
    # EXPLICIT, row-flagged sample of 3000, not a silent cap.
    "ar": {"dataset": ("wikipron_ar_diacritized", "ar"), "espeak": None,
           "epitran": None, "gruut": None, "arbtok": "ar", "sample_n": 3000},
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


#: Written by ``scripts/build_espeak_rules_only.sh`` into the rules-only
#: output dir: one ``lang<TAB>stripped_exception_lines`` row per language the
#: build ACTUALLY stripped and recompiled.
ESPEAK_RULES_MANIFEST = "rules_only_manifest.tsv"


def read_espeak_rules_manifest(root: str) -> Optional[Dict[str, int]]:
    """``{dictsource_lang: stripped_exception_lines}`` for a rules-only build,
    or ``None`` when the directory carries no manifest at all."""
    path = os.path.join(root, ESPEAK_RULES_MANIFEST)
    if not os.path.isfile(path):
        return None
    out: Dict[str, int] = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) >= 2:
                try:
                    out[parts[0]] = int(parts[1])
                except ValueError:
                    continue
    return out


def _dictsource_lang_for(lang: str, voice: Optional[str]) -> Optional[str]:
    """The espeak-ng ``dictsource/<x>_rules`` language behind a board row."""
    mapped = DICTSOURCE_LANG.get(lang)
    if mapped:
        return mapped
    if voice:
        # "ca-ba" -> "ca"; a plain voice name is already the dictsource lang
        return voice.split("-", 1)[0]
    return None


def assert_espeak_rules_built_for(lang: str, voice: Optional[str]) -> str:
    """Verify PER LANGUAGE that ``$ESPEAK_RULES_DATA_PATH`` really is a
    rules-only build for *lang*, and raise if it is not.

    The build script copies espeak-ng's STOCK compiled data for every
    language and then recompiles only the ones it was asked for, so a
    directory being present says nothing about the language being scored.
    Before this check, running the board for a language the build had not
    stripped scored **stock espeak-ng in both the ``espeak`` and the
    ``espeak_rules`` column** and published the two identical numbers as if
    they were a rules-vs-dictionary contrast. That is worse than no number,
    so it is an exception rather than a silent ``n/a``: a fabricated
    comparison cannot be distinguished from a real one after the fact.

    Two independent gates, because either alone can be fooled:

    1. the build manifest must list the language (a directory with no
       manifest predates this check and cannot be trusted at all); and
    2. if the manifest says exception lines were stripped, the compiled
       ``<lang>_dict`` must actually DIFFER from the installed stock one —
       proof the strip-and-recompile took effect. A manifest entry with
       zero stripped lines is a legitimate no-op (some languages ship no
       ``_list``/``_listx``/``_extra`` at all) and is allowed through.

    Returns the resolved dictsource language on success.
    """
    root = ESPEAK_RULES_DATA_PATH or ""
    ds_lang = _dictsource_lang_for(lang, voice)
    remedy = (f"rebuild with: scripts/build_espeak_rules_only.sh "
              f"{ds_lang or lang}   (then re-point $ESPEAK_RULES_DATA_PATH "
              f"at the output dir)")
    if ds_lang is None:
        raise RuntimeError(
            f"espeak_rules: no dictsource language known for '{lang}' — add "
            f"it to DICTSOURCE_LANG before scoring the column for this row")

    manifest = read_espeak_rules_manifest(root)
    if manifest is None:
        raise RuntimeError(
            f"espeak_rules: $ESPEAK_RULES_DATA_PATH ({root}) has no "
            f"{ESPEAK_RULES_MANIFEST}, so there is no evidence any language "
            f"in it is rules-only. {remedy}")
    if ds_lang not in manifest:
        raise RuntimeError(
            f"espeak_rules: '{lang}' needs dictsource language '{ds_lang}', "
            f"which this rules-only build did NOT strip (manifest lists: "
            f"{', '.join(sorted(manifest)) or 'nothing'}). Scoring it would "
            f"report STOCK espeak-ng in the espeak_rules column. {remedy}")

    if manifest[ds_lang] > 0:
        built = os.path.join(root, "espeak-ng-data", f"{ds_lang}_dict")
        stock = _stock_espeak_dict(ds_lang)
        # Gate 2 can only compare what it can find. When either side is
        # missing it proves nothing, and a check that quietly proves nothing
        # is how the fabricated es row survived review in the first place —
        # so say so out loud, and let a caller demand it actually ran.
        if not os.path.isfile(built):
            _rules_gate_inconclusive(
                f"espeak_rules: cannot verify '{ds_lang}' — the manifest says "
                f"{manifest[ds_lang]} exception lines were stripped but "
                f"{built} does not exist, so the "
                f"differs-from-stock check did not run. {remedy}")
        elif stock is None:
            _rules_gate_inconclusive(
                f"espeak_rules: cannot verify '{ds_lang}' — no INSTALLED "
                f"{ds_lang}_dict could be located to compare {built} against, "
                f"so the differs-from-stock check did not run. The manifest "
                f"gate still passed. Set $ESPEAK_RULES_STRICT=1 to treat this "
                f"as an error.")
        elif _file_digest(built) == _file_digest(stock):
            raise RuntimeError(
                f"espeak_rules: {built} is byte-identical to the stock "
                f"{stock} even though the manifest says "
                f"{manifest[ds_lang]} exception lines were stripped — the "
                f"recompile did not take effect. {remedy}")
    return ds_lang


#: When set, an INCONCLUSIVE differs-from-stock check is an error rather than
#: a warning. Off by default so a machine whose espeak-ng install layout this
#: script cannot introspect can still produce the (manifest-gated) column.
ESPEAK_RULES_STRICT = bool(os.environ.get("ESPEAK_RULES_STRICT"))


def _rules_gate_inconclusive(message: str) -> None:
    """Report that the differs-from-stock gate could not be evaluated.

    Raises under ``$ESPEAK_RULES_STRICT``, warns loudly otherwise. Never
    silent: the whole point of the gate is that an unverified
    ``espeak_rules`` number is indistinguishable from a fabricated one.
    """
    if ESPEAK_RULES_STRICT:
        raise RuntimeError(message)
    print(f"WARNING: {message}", file=sys.stderr)


def _file_digest(path: str) -> str:
    import hashlib
    with open(path, "rb") as fh:
        return hashlib.md5(fh.read()).hexdigest()


def _stock_espeak_dict(ds_lang: str) -> Optional[str]:
    """Path to the INSTALLED (stock) compiled dictionary for *ds_lang*, or
    ``None`` when the install layout cannot be located."""
    exe = shutil.which("espeak-ng")
    if not exe:
        return None
    prefix = os.path.dirname(os.path.dirname(os.path.realpath(exe)))
    roots = []
    # espeak-ng itself is the authority: `--version` prints "Data at: <dir>".
    # Ask it first, then fall back to the usual install layouts.
    try:
        proc = subprocess.run([exe, "--version"], capture_output=True,
                              text=True, timeout=10)
        for chunk in (proc.stdout or "").split("Data at:")[1:]:
            roots.append(chunk.strip().splitlines()[0].strip())
    except (OSError, subprocess.TimeoutExpired, IndexError):
        pass
    roots += [os.environ.get("ESPEAK_DATA_PATH", ""),
              os.path.join(prefix, "share", "espeak-ng-data"),
              "/usr/share/espeak-ng-data",
              "/usr/local/share/espeak-ng-data"]
    for root in roots:
        if not root:
            continue
        candidate = os.path.join(root, f"{ds_lang}_dict")
        if os.path.isfile(candidate):
            return candidate
    return None


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


# ─── o2i-downstream family (arbtok, tugaphone, g2p_barranquenho,
#     mwl_phonemizer) — lazy, optional ────────────────────────────────────────
#
# All four are TigreGotico repos built directly on this repo's own lattice
# (orthography2ipa.G2P), so they are never a truly independent comparison
# point against o2i-lineage gold — see the ``_O2I_SAME_SOURCE_DATASETS``
# additions below for exactly which rows that applies to. They are wired in
# anyway (owner directive: "dont forget our downstream in benchmarks too")
# because a family member can still legitimately be compared against a
# GENUINELY independent gold (e.g. mwl_phonemizer vs. the native-speaker
# ``mirandese_g2p`` set) or against each other, and because "n/a" on a row
# that has a downstream engine is itself information.
#
# Per-engine lexicon disposition (the espeak discipline, audited per package
# rather than assumed):
#
# - **arbtok** — audit correction: arbtok's DEFAULT configuration is NOT
#   lexicon-free. ``ArbtokG2PPlugin.__init__`` defaults to
#   ``lexicon=DEFAULT_LEXICON`` (``hf://TigreGotico/arabic-stem-lexicon``,
#   145,890 entries) AND ``dialect_lexicon=True`` (a per-lect closed-class
#   function-word lexicon) both ON. The RANKED ``arbtok`` column
#   therefore constructs the plugin explicitly with both disabled
#   (``lexicon=None, dialect_lexicon=False`` — see
#   ``arbtok_transcribe``), leaving only the rule path plus
#   ``arbtok.dialects.WORD_EXCEPTIONS`` — a 22-entry closed set of
#   MSA/Classical demonstrative-pronoun irregular readings (silent
#   letters) with no independent toggle, small enough to stay in the same
#   audited-acceptable category as pycotovia's closed function-word
#   table. The STOCK (default-configured, lexicon-backed) number is
#   reported separately and purely informationally as ``arbtok_stock``
#   (board column "arbtok (lexicon)") — never ranked, exactly like stock
#   ``espeak``/``gruut``/``tugaphone``.
# - **tugaphone** — ``TugaPhonemizer`` always registers the curated
#   ``tugalex`` lexicon for the target lect before phonemizing
#   (``lattice_core._ensure_lexicon``, called unconditionally from
#   ``phonemize_sentence``); there is no public toggle to disable it. Same
#   disposition as stock ``espeak``: reported "(lexicon)", left on the board
#   for information, excluded from the lexicon-free Winner/leaderboard
#   ranking (see ``_LEXICON_EXCLUDED_FROM_RANKING`` below) rather than
#   silently ranked with an undisclosed lexicon on.
# - **g2p_barranquenho** — no bundled per-word lexicon; ``transcribe()`` is
#   pure lattice + rule stages. Lexicon-free, scored as-is.
# - **mwl_phonemizer** — ``MirandesePhonemizer`` carries an optional
#   native-speaker lexicon overlay and CRF corrector, both OFF by default
#   (``use_crf=False``) and the overlay only consulted when
#   ``phonemize(..., lookup=True)``. The module-level ``phonemize()``
#   convenience function used here calls neither, so scoring is pure lattice
#   output — lexicon-free by construction, no extra flag needed.


def _installed_version(dist_name: str) -> Optional[str]:
    """The installed distribution version for *dist_name* (e.g.
    ``"arbtok"``), or ``None`` if it is not installed / not resolvable as
    a distribution (editable/local checkouts still report a version via
    their build backend — this is NOT a proxy for "installed from
    PyPI"). Recorded per row (``<system>_version``, same pattern as
    ``ahotts_version``) so a committed board number is reproducible
    against a known engine version, not silently unpinned."""
    try:
        return importlib.metadata.version(dist_name)
    except importlib.metadata.PackageNotFoundError:
        return None


#: One constructed plugin per Arabic variety. ``ArbtokG2PPlugin`` loads
#: model/lexicon files on construction, so building one per word would cost
#: seconds per word instead of seconds per language. Two separate caches
#: because the two columns are two DIFFERENT configurations of the same
#: class: lexicon-free (ranked) and stock/lexicon-backed (informational).
_arbtok_plugin_cache: Dict[str, object] = {}
_arbtok_stock_plugin_cache: Dict[str, object] = {}


def arbtok_transcribe(word: str, lang: str) -> Optional[str]:
    """Transcribe *word* with arbtok's ``ArbtokG2PPlugin`` for the Arabic
    *lang* variety, LEXICON-FREE (``lexicon=None, dialect_lexicon=False``),
    or ``None`` if the library is absent or fails on the word.

    Audit correction: arbtok's DEFAULTS are NOT lexicon-free —
    ``ArbtokG2PPlugin.__init__`` defaults ``lexicon=DEFAULT_LEXICON``
    (``hf://TigreGotico/arabic-stem-lexicon``, 145,890 entries) and
    ``dialect_lexicon=True`` (a per-lect closed-class function-word
    lexicon). This is the fair-comparison RANKED column — the espeak
    discipline applied correctly this time: both bundled lexicons
    disabled, so only the rule path plus the 22-entry
    ``WORD_EXCEPTIONS`` closed set (not independently toggleable, and
    small enough to stay audited-acceptable — see the module note above)
    remain. The full-lexicon STOCK number is reported separately, purely
    informationally, by ``arbtok_stock_transcribe`` below."""
    try:
        from arbtok.plugin import ArbtokG2PPlugin
    except ImportError:
        return None
    plugin = _arbtok_plugin_cache.get(lang)
    if plugin is None:
        try:
            plugin = ArbtokG2PPlugin(lang=lang, lexicon=None,
                                      dialect_lexicon=False)
        except Exception:
            return None
        _arbtok_plugin_cache[lang] = plugin
    try:
        return plugin.transcribe(word) or None
    except Exception:
        return None


def arbtok_stock_transcribe(word: str, lang: str) -> Optional[str]:
    """Transcribe *word* with arbtok's STOCK (default-configured)
    ``ArbtokG2PPlugin`` — the full 145,890-entry stem lexicon and the
    per-lect dialect lexicon both ON, exactly as a caller gets with no
    arguments. Informational only (see the ``(lexicon)`` column
    disposition below the module docstring); never ranked.

    C3: an HF lexicon fetch failure must never silently degrade to a
    bare-lattice result that LOOKS like a real, lexicon-backed score (a
    fetch failure scoring identically to "no lexicon configured" would
    be indistinguishable from a genuine lexicon-free run — a lie by
    omission).

    C3 correction (round 2): ``arbtok.lexicon.LexiconUnavailable`` does
    NOT propagate out of ``ArbtokG2PPlugin.transcribe`` — arbtok's own
    ``_diacritize`` wraps diacritizer construction AND every diacritize
    call in a blanket ``except Exception: return text`` (arbtok/
    plugin.py), so a broken lexicon degrades to bare-lattice output
    INSIDE arbtok itself before this function ever sees an exception. An
    ``except LexiconUnavailable: raise`` here was therefore dead code —
    unreachable, confirmed by a reviewer probe with a broken lexicon path
    that returned bare-lattice output with no raise. Fixed harness-side,
    since arbtok's own swallow is by design and not something to patch
    around: PRE-FLIGHT the lexicon directly, bypassing arbtok's
    diacritizer entirely, once per cached plugin, BEFORE any word is
    scored — ``StemLexicon(DEFAULT_LEXICON).entries`` raises
    ``LexiconUnavailable`` on its own fetch/parse failure with no
    swallowing anywhere in its own path (see
    ``arbtok.lexicon.StemLexicon.entries``). This still lets the run
    crash on a fetch failure instead of silently publishing a
    lexicon-labeled number that is secretly lexicon-free."""
    try:
        from arbtok.plugin import ArbtokG2PPlugin
        from arbtok.lexicon import LexiconUnavailable, StemLexicon
    except ImportError:
        return None
    plugin = _arbtok_stock_plugin_cache.get(lang)
    if plugin is None:
        StemLexicon().entries  # pre-flight: raises LexiconUnavailable, uncaught
        plugin = ArbtokG2PPlugin(lang=lang)  # stock defaults
        _arbtok_stock_plugin_cache[lang] = plugin
    try:
        return plugin.transcribe(word) or None
    except LexiconUnavailable:
        raise
    except Exception:
        return None


#: One ``TugaPhonemizer`` for the whole run — it takes the dialect per CALL
#: (``phonemize_sentence(..., lang=...)``), so unlike the arbtok caches this
#: needs no per-language keying.
_tugaphone_instance: Optional[Any] = None


def tugaphone_transcribe(word: str, lang: str) -> Optional[str]:
    """Transcribe *word* with tugaphone's ``TugaPhonemizer`` for the
    Portuguese *lang* dialect, or ``None`` if the library is absent or fails
    on the word."""
    try:
        from tugaphone import TugaPhonemizer
    except ImportError:
        return None
    global _tugaphone_instance
    if _tugaphone_instance is None:
        _tugaphone_instance = TugaPhonemizer()
    try:
        return _tugaphone_instance.phonemize_sentence(word, lang=lang) or None
    except Exception:
        return None


def barranquenho_transcribe(word: str, lang: str) -> Optional[str]:
    """Transcribe *word* with g2p_barranquenho's ``transcribe``, or ``None``
    if the library is absent or fails on the word. *lang* is accepted for a
    uniform call signature but unused — g2p_barranquenho scores a single
    fixed variety (``ext-PT-x-barrancos``)."""
    try:
        from g2p_barranquenho import transcribe
    except ImportError:
        return None
    try:
        phones = transcribe(word)
        return "".join(phones) if phones else None
    except Exception:
        return None


def mwl_transcribe(word: str, lang: str) -> Optional[str]:
    """Transcribe *word* with mwl_phonemizer's module-level ``phonemize()``
    for the Mirandese *lang* dialect (lattice-only: no lexicon overlay, no
    CRF — see the module disposition note above), or ``None`` if the
    library is absent or fails on the word."""
    try:
        from mwl_phonemizer import phonemize
    except ImportError:
        return None
    try:
        return phonemize(word, dialect=lang) or None
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


#: One ``TextProcessor`` per language, with its lexicon lookup disabled
#: (``settings.lookup_phonemes = None``) so every word falls through to
#: gruut's OWN g2p fallback model (a CRF/FST trained for out-of-lexicon
#: words) instead of a dictionary hit — gruut's ``gruut_rules_only``
#: column, the same "rules only, dictionary emptied" idea as
#: ``espeak_rules``/``build_espeak_rules_only.sh``, applied to gruut's
#: bundled lexicon.db rather than espeak-ng's dictsource. Built lazily
#: and cached per language: constructing a ``TextProcessor`` loads the
#: language's model files, so building thousands of them (per word) would
#: be a needless multi-second penalty per word instead of per language.
_GRUUT_RULES_ONLY_PROCESSORS: Dict[str, object] = {}


def gruut_rules_only_available(lang: str) -> bool:
    try:
        import gruut  # noqa: F401
    except ImportError:
        return False
    return True


def gruut_rules_only_transcribe(word: str, lang: str) -> Optional[str]:
    """Like :func:`gruut_transcribe`, but with gruut's bundled
    dictionary lookup disabled so every word goes through its g2p
    fallback model — see ``_GRUUT_RULES_ONLY_PROCESSORS``."""
    try:
        from gruut.text_processor import TextProcessor
    except ImportError:
        return None
    try:
        proc = _GRUUT_RULES_ONLY_PROCESSORS.get(lang)
        if proc is None:
            proc = TextProcessor(default_lang=lang)
            settings = proc.get_settings(lang)
            # The gate this column exists for: without this, gruut_rules_only
            # would silently be IDENTICAL to gruut (dictionary hits for every
            # in-lexicon word) — the same fabrication risk
            # assert_espeak_rules_built_for guards against for espeak_rules.
            settings.lookup_phonemes = None
            _GRUUT_RULES_ONLY_PROCESSORS[lang] = proc
        graph, root = proc(word, lang=lang)
        phonemes: List[str] = []
        for sentence in proc.sentences(graph, root):
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


# ─── same-source policy ─────────────────────────────────────────────────────
#
# WHY THIS SECTION EXISTS: several registered golds were themselves produced
# by one of the systems on this board (or by o2i, or by a downstream built on
# o2i). Scoring a system against its own output is tautological — it scores
# near 0 by construction, not because it is accurate. Every rule below
# decides, per (dataset, language), which system must be REFUSED a number on
# that row. The cell then renders as "same-source" rather than "n/a", because
# "system unavailable" and "this number would be a lie" are different facts
# and the reader is entitled to know which one applies.

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

#: gruut's bundled ``en-US`` lexicon (``gruut_lang_en/lexicon.db``,
#: 124,392 distinct words) is CMUdict-derived: it covers 98.2% of both
#: ``cmudict`` and ``ipadict``'s gold words by direct measurement (see the
#: coverage numbers this module can recompute against the installed
#: lexicon.db). For those two rows gruut is not doing G2P — it is a
#: lookup into a lexicon built from the SAME source the gold is drawn
#: from, so its low PER there measures lexicon agreement, not phonemizer
#: accuracy. gruut's independent ``en``/``en-GB`` ``wikipron`` rows are
#: NOT in this set (~44%/~43% lexicon coverage by the same measurement —
#: mostly real G2P on the uncovered majority) and stay a real comparison.
_GRUUT_SAME_SOURCE_DATASETS = frozenset({"cmudict", "ipadict"})

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
    # barranquenho_dict joins per this docstring's own instruction above:
    # load_barranquenho_dict's docstring documents its IPA column as itself
    # o2i-aligned, so scoring o2i (or g2p_barranquenho, which is built
    # directly on o2i's ext-PT-x-barrancos spec) against it is circular.
    "barranquenho_dict",
})

#: arbtok is built directly on o2i's own Arabic lattice AND its
#: code-switched-Arabic gold text is machine-pinned to o2i's own output
#: (see docs/benchmarks.md "Provenance"), so it shares o2i's same-source
#: exposure 1:1 — same datasets, same reason.
_ARBTOK_SAME_SOURCE_DATASETS = _O2I_SAME_SOURCE_DATASETS

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
        "gruut": dataset_name in _GRUUT_SAME_SOURCE_DATASETS,
        "o2i": dataset_name in _O2I_SAME_SOURCE_DATASETS,
        "arbtok": dataset_name in _ARBTOK_SAME_SOURCE_DATASETS,
        "arbtok_stock": dataset_name in _ARBTOK_SAME_SOURCE_DATASETS,
        "barranquenho": dataset_name in _O2I_SAME_SOURCE_DATASETS,
        # tugaphone and mwl_phonemizer are likewise built directly on o2i's
        # own lattice (TugaPhonemizer/MirandesePhonemizer both instantiate
        # orthography2ipa.G2P internally), so they inherit the exact same
        # circularity exposure on the o2i-lineage-gold datasets as arbtok
        # and g2p_barranquenho do — see _O2I_SAME_SOURCE_DATASETS.
        "tugaphone": dataset_name in _O2I_SAME_SOURCE_DATASETS,
        "mwl_phonemizer": dataset_name in _O2I_SAME_SOURCE_DATASETS,
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


# ─── running the comparison ─────────────────────────────────────────────────

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


#: A hypothesis/gold-variants pair, as consumed by :func:`_score`. One per
#: scored word, per system.
ScoredPairs = List[Tuple[Optional[str], List[str]]]


class PerWordEngine(NamedTuple):
    """One optional comparison engine that is called ONE WORD AT A TIME.

    This registry exists so adding or auditing a comparison engine is a
    ONE-LINE change in one place. Before it, every engine was spelled out
    five separate times inside ``_compare_lang_dataset`` (a result list, an
    availability gate, a per-word call, a scoring line, and a set of row
    keys); forgetting one of the five silently produced a missing or
    mis-gated column rather than an error.

    Deliberately NOT in this registry, because each is genuinely special
    rather than merely repetitive — folding them in would hide the very
    policy that makes them special:

    - ``o2i`` and ``o2i_lex`` — the system under test, not a comparison
      target; driven by an in-process ``G2P`` instance with sentence-vs-word
      dispatch, and ``o2i_lex`` needs a lexicon registered around its pass.
    - ``espeak`` and ``espeak_rules`` — batched through one subprocess per
      chunk (see :func:`espeak_batch_transcribe`), so their results are
      precomputed for all words at once rather than word by word.

    Fields:

    ``key``
        Row-key prefix (``<key>_per`` / ``<key>_n`` / ``<key>_same_source``)
        and the column key in ``_SYSTEMS``.
    ``cfg_key``
        Which ``LANGS`` entry key holds this engine's per-language config.
        ``None`` in that entry means "no mapping for this language" => the
        column is ``n/a``. Note ``arbtok_stock`` shares ``arbtok``'s
        mapping: it is the same language, just the default-configured
        (lexicon-backed) plugin.
    ``transcribe_name``
        The module-level function name to call as ``fn(word, cfg_value)``.
        Resolved BY NAME at call time, not captured as a function object,
        so ``monkeypatch.setattr(compare_systems, "gruut_transcribe", ...)``
        still takes effect — capturing the object here would silently
        bypass every test double and every future patch.
    ``same_source_key``
        Key into :func:`_same_source_flags` that suppresses this engine when
        the gold IS its own output. ``None`` means the engine can never be
        same-source, which is a POLICY claim, not an omission — see the
        per-engine reasons at each registry entry below.
    ``available_name``
        Name of an extra runtime availability predicate called as
        ``fn(cfg_value)``, beyond "the language has a mapping at all".
        Resolved by name at call time for the same reason
        ``transcribe_name`` is.
    ``deferred``
        Run in a SEPARATE pass after the o2i pass has finished, instead of
        interleaved into it. Only ``tugaphone`` needs this, and the reason
        is a real measured contamination bug — see :func:`_run_deferred`.
    """

    key: str
    cfg_key: str
    transcribe_name: str
    same_source_key: Optional[str] = None
    available_name: Optional[str] = None
    deferred: bool = False


#: Every per-word comparison engine, in the order they are called for each
#: word. That relative order is preserved from the pre-registry code.
#:
#: One ordering change IS made here, deliberately: o2i now runs as ONE
#: COMPLETE PASS before this loop, where the pre-registry code interleaved it
#: word by word with the engines below. Numerically inert today — of the
#: engines here only tugaphone mutates the process-global o2i lexicon
#: registry, and it is already ``deferred`` for exactly that reason (see
#: :func:`_run_deferred`) — and it removes the contamination surface
#: entirely rather than relying on one engine staying correctly flagged.
PER_WORD_ENGINES: List[PerWordEngine] = [
    PerWordEngine("epitran", "epitran", "epitran_transcribe",
                  same_source_key="epitran"),
    PerWordEngine("gruut", "gruut", "gruut_transcribe",
                  same_source_key="gruut"),
    # never same-source: gruut_rules_only bypasses the bundled lexicon
    # lookup entirely (see gruut_rules_only_transcribe), so it stays a real
    # comparison even on cmudict/ipadict — those rows get gruut_rules_per
    # while gruut_per itself is suppressed as same-source.
    PerWordEngine("gruut_rules", "gruut", "gruut_rules_only_transcribe",
                  available_name="gruut_rules_only_available"),
    # never same-source: no registered gold is Cotovia-derived.
    PerWordEngine("pycotovia", "pycotovia", "pycotovia_transcribe"),
    PerWordEngine("ahotts", "ahotts", "ahotts_transcribe",
                  same_source_key="ahotts"),
    # never same-source: no registered gold is africa-g2p-derived.
    PerWordEngine("africa_g2p", "africa_g2p", "africa_g2p_transcribe"),
    PerWordEngine("arbtok", "arbtok", "arbtok_transcribe",
                  same_source_key="arbtok"),
    PerWordEngine("arbtok_stock", "arbtok", "arbtok_stock_transcribe",
                  same_source_key="arbtok_stock"),
    PerWordEngine("tugaphone", "tugaphone", "tugaphone_transcribe",
                  same_source_key="tugaphone", deferred=True),
    PerWordEngine("barranquenho", "barranquenho", "barranquenho_transcribe",
                  same_source_key="barranquenho"),
    PerWordEngine("mwl_phonemizer", "mwl_phonemizer", "mwl_transcribe",
                  same_source_key="mwl_phonemizer"),
]


def _engine_enabled(spec: PerWordEngine, cfg: dict,
                    same_source: Dict[str, bool]) -> bool:
    """Whether *spec* produces a real number for this row, rather than
    ``n/a`` (no language mapping / library absent) or a same-source
    refusal."""
    cfg_value = cfg.get(spec.cfg_key)
    if cfg_value is None:
        return False
    if spec.same_source_key and same_source[spec.same_source_key]:
        return False
    if (spec.available_name is not None
            and not globals()[spec.available_name](cfg_value)):
        return False
    return True


def _load_gold_refs(lang: str, cfg: dict, dataset_name: str, loader_lang: str,
                    limit: Optional[int]) -> Dict[str, List[str]]:
    """``{word: [gold variant, ...]}`` for one (language, dataset) pair.

    An explicit per-language ``sample_n`` applies ONLY on an uncapped run
    (``limit is None``) and is announced on stderr, because a silently
    sampled row published next to full-set rows would be indistinguishable
    from one — the row itself is flagged ``sampled`` for the same reason.
    """
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
    return refs


def _o2i_pass(engine: Any, words: Sequence[str],
              refs: Dict[str, List[str]]) -> ScoredPairs:
    """Transcribe every word with the o2i *engine*, degrading a per-word
    failure to ``None`` (scored as "not covered") rather than losing the
    whole language to one bad word."""
    out: ScoredPairs = []
    for word in words:
        golds = refs[word]
        try:
            # Sentence-level gold entries (4catac) go through the
            # utterance API so cross-word sandhi and per-word dispatch
            # apply — the same multiword rule benchmark.evaluate_words
            # uses; transcribe_word on a whole sentence mis-scores it.
            transcribe = (engine.transcribe if len(word.split()) > 1
                          else engine.transcribe_word)
            out.append((transcribe(word), golds))
        except Exception:
            out.append((None, golds))
    return out


def _run_deferred(spec: PerWordEngine, cfg: dict, words: Sequence[str],
                  refs: Dict[str, List[str]], o2i_module: Any) -> ScoredPairs:
    """Run a ``deferred`` engine in its OWN pass, then clear the lexicon
    registry.

    POLICY, and the bug this prevents: ``tugaphone_transcribe`` ->
    ``TugaPhonemizer.phonemize_sentence`` -> ``tugaphone.lattice_core.
    _ensure_lexicon()`` calls ``orthography2ipa.register_lexicon(lect, ...)``
    — a PROCESS-GLOBAL mutation keyed on the SAME lect code o2i's own engine
    uses. Interleaving tugaphone into the o2i loop (the original bug) meant
    every o2i score from word 2 onward was secretly o2i+tugalex, not bare
    o2i — measured contamination: pt-PT/ep_dialects o2i PER dropped from
    0.1185 (clean) to 0.1072 (with tugalex leaking in). Running strictly
    AFTER the o2i pass has collected every entry, and clearing the registry
    immediately after, keeps the mutation out of o2i's scoring.
    """
    fn = globals()[spec.transcribe_name]
    cfg_value = cfg[spec.cfg_key]
    out: ScoredPairs = [(fn(word, cfg_value), refs[word]) for word in words]
    o2i_module.clear_lexicons()
    return out


def _o2i_lex_pass(o2i_module: Any, engine: Any, g2p_code: str,
                  lexicon_tsv: str, words: Sequence[str],
                  refs: Dict[str, List[str]]) -> ScoredPairs:
    """Re-score every word with espeak-ng's own wordlist registered as an
    o2i lexicon — the ``o2i_lex`` half of the fair-comparison 2x2 (see the
    module docstring). The registry is cleared again afterwards so the
    overlay cannot leak into the next language."""
    # register_lexicon() calls get_lexicon.cache_clear() itself, so the
    # engine picks up the sidecar on the very next transcribe call —
    # no need for a fresh G2P instance.
    o2i_module.register_lexicon(g2p_code, lexicon_tsv)
    out = _o2i_pass(engine, words, refs)
    o2i_module.clear_lexicons()
    return out


def _r(per: Optional[float]) -> Optional[float]:
    """Round a PER for the committed board, preserving ``None`` ("n/a")."""
    return round(per, 4) if per is not None else None


def _compare_lang_dataset(lang: str, cfg: dict, dataset_name: str,
                           loader_lang: str, limit: Optional[int]) -> dict:
    """Score *lang* against ONE gold dataset (see ``compare_lang`` for the
    multi-dataset iteration this backs).

    Runs, in this order: the o2i pass, then every enabled interleaved
    per-word engine (:data:`PER_WORD_ENGINES`), then the deferred engines,
    then the ``o2i_lex`` pass. The espeak columns are precomputed in batch
    before any of it. Returns one board row — see :func:`_build_row` for
    the key schema.
    """
    same_source = _same_source_flags(dataset_name, loader_lang)
    refs = _load_gold_refs(lang, cfg, dataset_name, loader_lang, limit)
    words = sorted(refs)

    import orthography2ipa
    from orthography2ipa import G2P
    g2p_code = cfg.get("g2p", lang)
    orthography2ipa.clear_lexicons()  # defensive: no leftover lexicon from a prior lang
    engine = G2P(g2p_code)

    # Every LANGS entry MUST declare these three explicitly, even as None.
    # The engine registry reads config keys with .get(), so a typo'd or
    # omitted key would quietly become an n/a column instead of an error —
    # and a silently-missing comparison is the exact failure mode this
    # harness refuses everywhere else (see assert_espeak_rules_built_for).
    # The pre-registry code got this for free by indexing these three
    # directly; keep it raising, but say what is wrong.
    missing = [k for k in ("espeak", "epitran", "gruut") if k not in cfg]
    if missing:
        raise KeyError(
            f"LANGS['{lang}'] is missing required key(s) {missing} — declare "
            f"them explicitly (None means 'this language has no mapping for "
            f"that system')")

    # ── espeak / espeak_rules: batched, so precomputed for all words ──
    use_espeak = (cfg.get("espeak") is not None and espeak_available()
                  and not same_source["espeak"])
    use_espeak_rules = (cfg.get("espeak") is not None
                        and espeak_rules_available()
                        and not same_source["espeak_rules"])
    if use_espeak_rules:
        # Raises rather than degrading to n/a: see assert_espeak_rules_built_for.
        assert_espeak_rules_built_for(lang, cfg["espeak"])
    espeak_out: Dict[str, Optional[str]] = (
        espeak_batch_transcribe(words, cfg["espeak"]) if use_espeak else {})
    espeak_rules_out: Dict[str, Optional[str]] = (
        espeak_batch_transcribe(words, cfg["espeak"],
                                data_path=ESPEAK_RULES_DATA_PATH)
        if use_espeak_rules else {})

    lexicon_tsv = build_espeak_lexicon_tsv(lang)

    # ── the passes ──
    enabled = [s for s in PER_WORD_ENGINES
               if _engine_enabled(s, cfg, same_source)]
    interleaved = [s for s in enabled if not s.deferred]
    results: Dict[str, ScoredPairs] = {s.key: [] for s in enabled}

    results["o2i"] = _o2i_pass(engine, words, refs)
    for word in words:
        golds = refs[word]
        for spec in interleaved:
            fn = globals()[spec.transcribe_name]
            results[spec.key].append((fn(word, cfg[spec.cfg_key]), golds))

    for spec in (s for s in enabled if s.deferred):
        results[spec.key] = _run_deferred(spec, cfg, words, refs,
                                          orthography2ipa)

    if lexicon_tsv is not None:
        results["o2i_lex"] = _o2i_lex_pass(orthography2ipa, engine, g2p_code,
                                           lexicon_tsv, words, refs)

    results["espeak"] = [(espeak_out.get(w), refs[w]) for w in words] \
        if use_espeak else []
    results["espeak_rules"] = [(espeak_rules_out.get(w), refs[w])
                               for w in words] if use_espeak_rules else []

    # ── score every collected pass ──
    #: {system key: (PER or None, words covered)}; an engine that never ran
    #: is absent, and reads back as the (None, 0) "n/a" default.
    scores: Dict[str, Tuple[Optional[float], int]] = {
        key: _score(pairs, lang=lang) if pairs else (None, 0)
        for key, pairs in results.items()
    }
    ran = {s.key for s in enabled}
    return _build_row(lang, cfg, dataset_name, loader_lang, limit, words,
                      same_source, scores, ran)


def _build_row(lang: str, cfg: dict, dataset_name: str, loader_lang: str,
               limit: Optional[int], words: Sequence[str],
               same_source: Dict[str, bool],
               scores: Dict[str, Tuple[Optional[float], int]],
               ran: set) -> dict:
    """Assemble one comparison board row.

    Written out key by key ON PURPOSE rather than generated from
    :data:`PER_WORD_ENGINES`: this dict IS the committed
    ``benchmarks/comparison.json`` schema, its key ORDER is the file's key
    order, and the per-engine key sets are deliberately irregular.
    Generating it would hide those distinctions behind a loop and make a
    schema change invisible in review. The irregularities, precisely:

    - only engines in ``_SAME_SOURCE_SYSTEMS`` carry ``_same_source``;
    - five engines carry a ``_version``, and they do NOT all get it the same
      way: ``ahotts_version`` is read from the ``LANGS`` config (it names
      which AhoTTS model generation was scored, not an installed package),
      while ``arbtok``/``tugaphone``/``barranquenho``/``mwl_phonemizer``
      read theirs from :func:`_installed_version`. The other engines record
      no version at all;
    - ``arbtok_version`` covers BOTH arbtok columns, since they are one
      installed package configured two ways.

    The distribution names below are written out here rather than carried on
    :class:`PerWordEngine`, because this asymmetry is the whole point: a
    registry field could not express "ahotts reads from config, not pip"
    without a special case anyway.
    """
    def per(key: str) -> Optional[float]:
        return _r(scores.get(key, (None, 0))[0])

    def n(key: str) -> int:
        return scores.get(key, (None, 0))[1]

    def version(key: str, dist: str) -> Optional[str]:
        return _installed_version(dist) if key in ran else None

    return {
        "lang": lang,
        "dataset": dataset_name,
        "n": len(words),
        "o2i_per": per("o2i"),
        "o2i_n": n("o2i"),
        "o2i_same_source": same_source["o2i"],
        "o2i_lex_per": per("o2i_lex"),
        "o2i_lex_n": n("o2i_lex"),
        "espeak_per": per("espeak"),
        "espeak_n": n("espeak"),
        "espeak_voice": cfg.get("espeak"),
        "espeak_same_source": same_source["espeak"],
        "espeak_rules_per": per("espeak_rules"),
        "espeak_rules_n": n("espeak_rules"),
        "espeak_rules_same_source": same_source["espeak_rules"],
        "epitran_per": per("epitran"),
        "epitran_n": n("epitran"),
        "epitran_same_source": same_source["epitran"],
        "gruut_per": per("gruut"),
        "gruut_n": n("gruut"),
        "gruut_same_source": same_source["gruut"],
        "gruut_rules_per": per("gruut_rules"),
        "gruut_rules_n": n("gruut_rules"),
        "pycotovia_per": per("pycotovia"),
        "pycotovia_n": n("pycotovia"),
        "ahotts_per": per("ahotts"),
        "ahotts_n": n("ahotts"),
        "ahotts_version": (cfg["ahotts"]["version"]
                            if "ahotts" in ran else None),
        "ahotts_same_source": same_source["ahotts"],
        "africa_g2p_per": per("africa_g2p"),
        "africa_g2p_n": n("africa_g2p"),
        "arbtok_per": per("arbtok"),
        "arbtok_n": n("arbtok"),
        "arbtok_same_source": same_source["arbtok"],
        "arbtok_stock_per": per("arbtok_stock"),
        "arbtok_stock_n": n("arbtok_stock"),
        "arbtok_stock_same_source": same_source["arbtok_stock"],
        # one version for BOTH arbtok columns: they are the same installed
        # package, configured two different ways.
        "arbtok_version": (_installed_version("arbtok")
                            if ({"arbtok", "arbtok_stock"} & ran) else None),
        "tugaphone_per": per("tugaphone"),
        "tugaphone_n": n("tugaphone"),
        "tugaphone_same_source": same_source["tugaphone"],
        "tugaphone_version": version("tugaphone", "tugaphone"),
        "barranquenho_per": per("barranquenho"),
        "barranquenho_n": n("barranquenho"),
        "barranquenho_same_source": same_source["barranquenho"],
        "barranquenho_version": version("barranquenho", "g2p_barranquenho"),
        "mwl_phonemizer_per": per("mwl_phonemizer"),
        "mwl_phonemizer_n": n("mwl_phonemizer"),
        "mwl_phonemizer_same_source": same_source["mwl_phonemizer"],
        "mwl_phonemizer_version": version("mwl_phonemizer", "mwl_phonemizer"),
        "provenance_tier": _provenance_tier_or_none(dataset_name, loader_lang),
        "harness_version": HARNESS_VERSION,
        "limit": limit if limit is not None else "full",
        "sampled": limit is None and cfg.get("sample_n") is not None,
    }


# ─── board persistence: build, merge, read ──────────────────────────────────

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


# ─── rendering: docs/comparison.md ──────────────────────────────────────────

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
            f"{_cell(row, 'o2i')} | {_cell(row, 'espeak')} |"
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
    scoreboard_by_key = {(r["lang"], r["dataset"]): r for r in scoreboard_rows}
    stale = []       # genuine drift: same word set, different engine output
    sampled_diff = []  # different SAMPLE SIZES, not drift — see below
    for row in rows:
        key = (row["lang"], row["dataset"])
        sb_row = scoreboard_by_key.get(key)
        if sb_row is None:
            continue
        sb_per = sb_row.get("per")
        o2i_per = row["o2i_per"]
        if sb_per is None or o2i_per is None:
            if sb_per != o2i_per:
                stale.append((row["lang"], row["dataset"], o2i_per, sb_per))
            continue
        if abs(sb_per - o2i_per) <= _SCOREBOARD_DRIFT_TOLERANCE:
            continue
        # A `sampled` comparison row (see LANGS' `sample_n`, e.g. pt-PT)
        # scores a fixed-seed SUBSET of the gold, while
        # scripts/benchmark.py's scoreboard runs the FULL gold — same
        # seed, different LIMIT, so the two draw a different-sized word
        # set from the same source and land on different PERs even when
        # both are freshly regenerated. That is sample-size variance, not
        # one board being stale relative to the other, and re-running
        # either script will not make the numbers converge.
        bench_n = sb_row.get("n")
        if row.get("sampled") and bench_n is not None and bench_n != row["n"]:
            sampled_diff.append((row["lang"], row["dataset"], o2i_per,
                                  row["n"], sb_per, bench_n))
        else:
            stale.append((row["lang"], row["dataset"], o2i_per, sb_per))

    if not stale and not sampled_diff:
        return (
            "The `o2i PER` column here matches "
            "[`benchmarks/results.json`](../benchmarks/results.json)'s "
            "`per` for every shared language/dataset pair in this run."
        )

    parts = []
    if not stale:
        parts.append(
            "The `o2i PER` column here matches "
            "[`benchmarks/results.json`](../benchmarks/results.json)'s "
            "`per` for every shared language/dataset pair that used the "
            "same word count."
        )
    else:
        stale.sort()
        listed = "; ".join(
            f"`{lang}`/`{dataset}` (here {_fmt(o2i_per)}, results.json "
            f"{_fmt(sb_per)})"
            for lang, dataset, o2i_per, sb_per in stale
        )
        parts.append(
            f"The `o2i PER` column here matches "
            f"[`benchmarks/results.json`](../benchmarks/results.json)'s "
            f"`per` for most shared language/dataset pairs, EXCEPT the "
            f"{len(stale)} listed below — those `benchmarks/results.json` "
            f"rows are stale (a prior PR changed the engine but did not "
            f"regenerate every affected row there; see e.g. PR #802's "
            f"`ca`/`4catac`-only regeneration). The numbers in THIS table "
            f"reflect the current engine via a live run; "
            f"`benchmarks/results.json` needs a matching regeneration for: "
            f"{listed}."
        )
    if sampled_diff:
        sampled_diff.sort()
        listed2 = "; ".join(
            f"`{lang}`/`{dataset}` (here {_fmt(o2i_per)} on {n} sampled "
            f"words, results.json {_fmt(sb_per)} on the full {bench_n})"
            for lang, dataset, o2i_per, n, sb_per, bench_n in sampled_diff
        )
        parts.append(
            f"{len(sampled_diff)} more row(s) differ for a DIFFERENT "
            f"reason — not staleness: this board's `sample_n` config "
            f"scores a fixed-seed SUBSET of the gold, while "
            f"`benchmarks/results.json` scores the FULL gold. Same seed, "
            f"different sample size, so a different PER is expected and "
            f"regenerating either side will not reconcile them: {listed2}."
        )
    return " ".join(parts)


def _espeak_rules_coverage_note(rows: List[dict]) -> str:
    """Name every row that has a stock ``espeak`` number (so it COULD, in
    principle, also carry an ``espeak-rules-only`` one) but no
    ``espeak_rules_per`` in this run — instead of letting those cells sit
    as silent ``n/a``.

    The ``espeak-rules-only`` column is a permanent part of this board
    (see the module docstring's "Fair-comparison 2x2" section and
    ``scripts/build_espeak_rules_only.sh``), but populating it requires a
    locally-built rules-only espeak-ng data dir
    (``$ESPEAK_RULES_DATA_PATH``) and a live re-measurement — rows that
    have not been re-measured yet (most commonly the large ones, 200k+
    gold words, deferred because a full engine + espeak pass over them is
    expensive) stay ``n/a`` there honestly rather than getting a
    fabricated or copied-from-a-PR-body number.
    """
    missing = [
        (r["lang"], r["dataset"], r["n"])
        for r in rows
        if r.get("espeak_per") is not None
        and not r.get("espeak_same_source")
        and r.get("espeak_rules_per") is None
        and not r.get("espeak_rules_same_source")
    ]
    if not missing:
        return (
            "Every row with a stock `espeak` number also carries an "
            "`espeak-rules-only` one in this run."
        )
    missing.sort(key=lambda t: (-t[2], t[0], t[1]))
    listed = "; ".join(
        f"`{lang}`/`{dataset}` (n={n})" for lang, dataset, n in missing
    )
    return (
        f"{len(missing)} row(s) have a stock `espeak` number but no "
        f"`espeak-rules-only` one yet in this run — deferred, not "
        f"fabricated (see `scripts/build_espeak_rules_only.sh`): "
        f"{listed}."
    )


#: Human-readable names for every ``LANGS`` key, for the leaderboard
#: lines and ``### <lang>`` table headings — bare ISO codes like `hts`
#: or `ktz` mean nothing to a reader who doesn't already know o2i's
#: registry. The obscure codes' names are copied VERBATIM from each
#: language's own orthography2ipa spec file's ``"name"`` field
#: (``orthography2ipa/data/<code>.json``) rather than guessed; the
#: common European languages use their standard English names.
#: ``eu-wikipron`` is not a distinct language — see the note on it below.
_LANG_DISPLAY_NAMES: Dict[str, str] = {
    "arb": "Classical Arabic",
    "ca": "Catalan",
    "ca-x-balear": "Balearic Catalan",
    "ca-x-occidental": "North-Western Catalan",
    "ca-x-valencia": "Valencian",
    "cop": "Coptic (Sahidic)",
    "cy": "Welsh",
    "de": "German",
    "el": "Modern Greek",
    "en": "English",
    "en-GB": "British English (RP)",
    "en-US": "American English (General American)",
    "es": "Spanish",
    "eu": "Basque (Euskara)",
    "eu-wikipron": "Basque (Euskara), wikipron-primary variant",
    "fi": "Finnish",
    "fr": "French",
    "ga": "Irish",
    "gl": "Galician",
    "hi": "Hindi",
    "hts": "Hadza",
    "it": "Italian",
    "kab": "Kabyle",
    "ktz": "Juǀʼhoan",
    "lad": "Ladino (Judeo-Spanish)",
    "mfe": "Morisyen",
    "ngh": "Nǁng",
    "nl": "Dutch",
    "nup": "Nupe",
    "pl": "Polish",
    "pt-PT": "European Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "sv": "Swedish",
    "tr": "Turkish",
    "tzm": "Central Atlas Tamazight",
}


def _lang_heading(lang: str) -> str:
    """The display name for a ``### <lang>`` heading / leaderboard bullet
    — bare code with its name in parens, or just the code if unnamed."""
    name = _LANG_DISPLAY_NAMES.get(lang)
    return f"{lang} ({name})" if name else lang


#: (field prefix, column label) for every comparison system, in table
#: column order. ``o2i`` is always first and always shown; the rest are
#: dropped per-language-group when every row in that group is ``n/a`` for
#: them (see ``_group_present_systems``).
#: Column labels. ``espeak``/``gruut`` are marked ``(lexicon)`` because
#: their stock number includes a bundled per-word exception dictionary o2i,
#: by hard rule, never ships — see the "Ranking policy: lexicon-free only"
#: section of the module docstring and the "How to read this" doc section.
#: They stay ON the board for information; they are simply never ranked
#: (see ``_RULES_ONLY_SUBSTITUTES``/``_rules_only_values``/``_winner``).
# ─── ranking policy: what may be called a winner ────────────────────────────
#
# WHY THIS SECTION EXISTS: the board shows more columns than it RANKS. The
# owner directive is "anything with a lexicon doesn't count as a winner", so
# the Winner column and the leaderboard rank over a LEXICON-FREE view of each
# row, while lexicon-backed columns stay visible for information. The three
# mechanisms, in the order a reader meets them:
#
#   _RULES_ONLY_SUBSTITUTES        a lexicon-backed system is ranked via its
#                                  rules-only twin (espeak -> espeak_rules),
#                                  never via its stock number.
#   _LEXICON_EXCLUDED_FROM_RANKING a lexicon-backed system with NO rules-only
#                                  twin is dropped from ranking outright.
#   _LEXICON_BACKED_INFORMATIONAL_COLUMNS
#                                  whichever excluded column would have won
#                                  is still named in an aside, so nothing is
#                                  silently buried.
#
# Ties, and the "no system is usable" escape hatch, live here too.

_SYSTEMS: List[Tuple[str, str]] = [
    ("o2i", "o2i"),
    ("espeak", "espeak (lexicon)"),
    ("espeak_rules", "espeak rules-only"),
    ("epitran", "epitran"),
    ("gruut", "gruut (lexicon)"),
    ("gruut_rules", "gruut rules-only"),
    ("pycotovia", "pycotovia"),
    ("ahotts", "ahotts-g2p"),
    ("africa_g2p", "africa-g2p"),
    # o2i-downstream family (arbtok, tugaphone, g2p_barranquenho,
    # mwl_phonemizer) — see the lexicon-disposition note by
    # arbtok_transcribe/tugaphone_transcribe/barranquenho_transcribe/
    # mwl_transcribe for the audit behind each one's ranking treatment.
    ("arbtok", "arbtok"),
    ("arbtok_stock", "arbtok (lexicon)"),
    ("tugaphone", "tugaphone (lexicon)"),
    ("barranquenho", "g2p_barranquenho"),
    ("mwl_phonemizer", "mwl_phonemizer"),
]

#: Systems whose cell can legitimately read ``same-source`` instead of a
#: number or ``n/a`` — see ``_cell``.
_SAME_SOURCE_SYSTEMS = {"o2i", "espeak", "espeak_rules", "epitran", "ahotts",
                         "gruut", "arbtok", "arbtok_stock", "barranquenho",
                         "tugaphone", "mwl_phonemizer"}

#: Family systems with an always-on lexicon and no public toggle to
#: disable it — ``tugaphone`` (audited: no toggle exists at all — see the
#: module note by ``tugaphone_transcribe``) — plus ``arbtok_stock``, the
#: PURELY INFORMATIONAL duplicate of the ``arbtok`` column with arbtok's
#: default (lexicon-backed) configuration; the RANKED ``arbtok`` column
#: is a separate, genuinely lexicon-free run (``lexicon=None,
#: dialect_lexicon=False`` — see ``arbtok_transcribe``), so
#: ``arbtok_stock`` is excluded here rather than substituted. Shown on
#: the board with a real PER for information; NEVER contributes to the
#: lexicon-free Winner/leaderboard ranking, the same treatment stock
#: ``espeak``/``gruut`` get via ``_RULES_ONLY_SUBSTITUTES`` — but unlike
#: those two, there is no ``_rules``-suffixed variant to substitute in,
#: so both members here are dropped from ``_rules_only_values`` outright.
_LEXICON_EXCLUDED_FROM_RANKING = {"tugaphone", "arbtok_stock"}

#: Two PERs within this margin of each other count as a tie for the
#: winner column, not a spurious four-decimal-place "win".
_WINNER_TIE_TOLERANCE = 0.001


def _system_value(row: dict, key: str) -> Optional[float]:
    """The comparable PER for system *key* on *row*, or ``None`` if it is
    unavailable OR same-source (a same-source cell is refused as a
    comparison point, not a real number — see ``_cell``)."""
    if key in _SAME_SOURCE_SYSTEMS and row.get(f"{key}_same_source"):
        return None
    return row.get(f"{key}_per")


def _row_has_system_data(row: dict, key: str) -> bool:
    """Whether *row* has ANYTHING to show for system *key* — a real PER
    or an honest ``same-source`` refusal both count; only a bare ``n/a``
    does not. Used to decide whether a language group's table needs the
    column at all."""
    if key in _SAME_SOURCE_SYSTEMS and row.get(f"{key}_same_source"):
        return True
    return row.get(f"{key}_per") is not None


def _group_present_systems(rows: List[dict]) -> List[Tuple[str, str]]:
    """The subset of ``_SYSTEMS`` (excluding ``o2i``, always shown) that
    has real data in at least one row of this language group — the
    per-group column omission that keeps a group with only 2 comparators
    from being buried in a wall of ``n/a``."""
    return [
        (key, label) for key, label in _SYSTEMS[1:]
        if any(_row_has_system_data(r, key) for r in rows)
    ]


def _row_cell(row: dict, key: str) -> str:
    if key in _SAME_SOURCE_SYSTEMS:
        return _cell(row, key)
    return _fmt(row.get(f"{key}_per"))


#: Bare-PER threshold above which NO system is doing usefully accurate
#: work on a gold — naming a "winner" among several systems all scoring
#: worse than this is misleading precision, so the winner cell instead
#: says so plainly. 0.8 is deliberately generous (PER can exceed 1.0):
#: this only fires on genuinely unusable rows, e.g. some `vox_communis`
#: rows where every system's PER sits above 1.0.
_NO_SYSTEM_USABLE_THRESHOLD = 0.8

#: {system key with a "*_rules" variant: that variant's key} — the
#: substitution B2's rules-only ranking applies. A system not in this map
#: has no rules-only column and keeps its normal value in that ranking
#: (documented per-engine in the doc's methodology section: pycotovia and
#: ahotts-g2p are rule-grade already with no general-purpose lexicon to
#: strip, epitran is a mapping table rather than a lexicon lookup for the
#: languages this board scores).
_RULES_ONLY_SUBSTITUTES = {"espeak": "espeak_rules", "gruut": "gruut_rules"}


def _rules_only_values(row: dict) -> Dict[str, float]:
    """*row*'s comparable PERs in the LEXICON-FREE world — the world the
    Winner column and the leaderboard actually rank over (owner
    directive: "anything with a lexicon doesn't count as a winner").
    Every system in ``_RULES_ONLY_SUBSTITUTES`` (currently ``espeak``,
    ``gruut``) is replaced by its rules-only variant, dropped entirely
    if that variant has no number — this NEVER silently falls back to
    the lexicon-backed stock number, which would defeat the point and
    let a lexicon sneak back into the ranking. Every other system
    (``epitran``, ``pycotovia``, ``ahotts``, ``africa_g2p``) keeps its
    normal :func:`_system_value`, because each is audited lexicon-free
    already — see the per-engine disposition in the module docstring /
    "How to read this" doc section:

    - ``epitran`` — a rule/mapping-based transliterator for the
      languages this board scores, not a lexicon lookup.
    - ``pycotovia`` — audited: its lexicon is closed to a small, fixed,
      rule-grade function-word stress table, not a general word
      dictionary.
    - ``ahotts`` — audited: its HDIC dictionary hits only 1.5% of the
      `eu` wikipron gold and 2.6% of `hitz_basque_ipa`, so it is
      effectively lexicon-free for ranking purposes; this is an explicit
      documented exception, not an oversight.
    - ``africa_g2p`` — rule-based G2P, no bundled per-word dictionary.

    The standalone ``espeak_rules``/``gruut_rules`` keys are skipped
    here since they are already represented via the substitution. When a
    ``transphone``-style lexicon-backed tokenizer column lands, it joins
    ``_RULES_ONLY_SUBSTITUTES`` (or is dropped from ranking entirely if
    it has no rules-only variant) rather than being ranked as-is."""
    out: Dict[str, float] = {}
    for key, _label in _SYSTEMS:
        if key in ("espeak_rules", "gruut_rules"):
            continue
        if key in _LEXICON_EXCLUDED_FROM_RANKING:
            continue
        if key in _RULES_ONLY_SUBSTITUTES:
            v = _system_value(row, _RULES_ONLY_SUBSTITUTES[key])
        else:
            v = _system_value(row, key)
        if v is not None:
            out[key] = v
    return out


def _lexicon_free_label(key: str) -> str:
    """The display label for *key* AS RANKED in the lexicon-free world:
    a system in ``_RULES_ONLY_SUBSTITUTES`` is ranked under its
    rules-only variant's label (e.g. ``espeak`` ranks as "espeak
    rules-only"), never under its lexicon-backed stock label — the
    stock label must never appear as a ranking winner."""
    labels = dict(_SYSTEMS)
    if key in _RULES_ONLY_SUBSTITUTES:
        return labels[_RULES_ONLY_SUBSTITUTES[key]]
    return labels[key]


def _labeled_lexicon_free_values(row: dict) -> Dict[str, float]:
    """:func:`_rules_only_values` re-keyed by display label (via
    :func:`_lexicon_free_label`) for callers that rank by name, e.g.
    :func:`_winner`."""
    return {_lexicon_free_label(k): v for k, v in _rules_only_values(row).items()}


#: Every lexicon-backed value this board reports PURELY informationally
#: (never ranked) — {the row field it lives in: the bare engine name for
#: the aside prose}. Covers two distinct shapes: ``espeak``/``gruut``
#: (a stock lexicon-backed column that has a SEPARATE ranked rules-only
#: substitute, e.g. ``espeak_rules``) and ``tugaphone``/``arbtok_stock``
#: (a column excluded from ranking outright — either because there is no
#: public toggle to strip the lexicon at all (tugaphone), or because it
#: duplicates a SEPARATE already-lexicon-free ranked column under a
#: different key (``arbtok_stock`` vs the ranked ``arbtok``)). C6: this
#: dict is the single source of truth for "which columns can win an
#: informational aside" — adding a new lexicon-backed system here is
#: enough, no separate case needed per call site.
_LEXICON_BACKED_INFORMATIONAL_COLUMNS: Dict[str, str] = {
    "espeak": "espeak",
    "gruut": "gruut",
    "tugaphone": "tugaphone",
    "arbtok_stock": "arbtok",
}


def _lexicon_backed_informational_note(row: dict, ranked_best: float) -> str:
    """Informational note naming a LEXICON-BACKED stock value (see
    ``_LEXICON_BACKED_INFORMATIONAL_COLUMNS``) that would have won had it
    been ranked — never silently dropped, just never counted. Empty
    string when no lexicon-backed stock value beats *ranked_best* (the
    actual, lexicon-free winner)."""
    candidates = []
    for key, label in _LEXICON_BACKED_INFORMATIONAL_COLUMNS.items():
        v = row.get(f"{key}_per")  # stock (lexicon-backed) value, raw
        if key in _SAME_SOURCE_SYSTEMS and row.get(f"{key}_same_source"):
            continue  # a same-source cell is not a real number to cite
        if v is not None and v < ranked_best - _WINNER_TIE_TOLERANCE:
            candidates.append((v, label))
    if not candidates:
        return ""
    v, label = min(candidates)
    return f" ({label} with its lexicon scores {v:.4f} — informational)"


def _ranked_winners(values: Dict[str, float]) -> List[str]:
    """Every key in *values* within ``_WINNER_TIE_TOLERANCE`` of the best
    (lowest) value — a single-element list is an outright win, more than
    one is a tie."""
    if not values:
        return []
    best = min(values.values())
    return [k for k, v in values.items() if v - best <= _WINNER_TIE_TOLERANCE]


def _winner(row: dict) -> str:
    """The name of the best (lowest-PER) system on *row*, RANKED OVER THE
    LEXICON-FREE WORLD ONLY (owner directive: a lexicon-backed stock
    value never counts as a winner — see :func:`_rules_only_values`).
    Names every system tied for best when two or more are within
    ``_WINNER_TIE_TOLERANCE`` of it (``tie (o2i, espeak rules-only)``,
    never a bare ``tie``). Same-source cells never win — they are not
    real comparisons. When even the best PER exceeds
    ``_NO_SYSTEM_USABLE_THRESHOLD``, says so instead of naming a
    "winner" among systems that are all effectively failing this gold.

    A lexicon-backed stock value (``espeak``/``gruut``) that would have
    scored lowest of all is NOT surfaced here — it stays visible in its
    own table column (marked ``(lexicon)``), and the leaderboard line
    for this row's language adds an informational aside about it (see
    :func:`_lexicon_backed_informational_note`); the Winner cell itself
    only ever names a lexicon-free result."""
    values = _labeled_lexicon_free_values(row)
    if not values:
        return "n/a"
    winners = _ranked_winners(values)
    if min(values.values()) > _NO_SYSTEM_USABLE_THRESHOLD:
        return "no system is usable on this gold"
    return f"tie ({', '.join(sorted(winners))})" if len(winners) > 1 else winners[0]


def _winner_label_str(winners: List[str]) -> str:
    """``X`` for an outright win, ``tie (A, B)`` for two or more within
    ``_WINNER_TIE_TOLERANCE`` — the exact same rendering rule
    :func:`_winner` uses for the table's Winner column, so the
    leaderboard line and the Winner cell can never contradict each
    other on the same row."""
    return f"tie ({', '.join(sorted(winners))})" if len(winners) > 1 else winners[0]


def _leaderboard_line(lang: str, primary_row: dict,
                       other_rows: Optional[List[dict]] = None) -> str:
    """One human-readable leaderboard line for *lang*'s primary gold row:
    who wins, and where o2i lands relative to them. RANKED OVER THE
    LEXICON-FREE WORLD ONLY (see :func:`_winner`/:func:`_rules_only_values`
    — a lexicon-backed espeak/gruut stock value never counts as a
    winner), and TIE-AWARE via :func:`_ranked_winners`/
    ``_WINNER_TIE_TOLERANCE`` — the exact same tie rule the table's
    Winner column uses, so the two can never disagree about whether a
    row is a tie (a bare ``sorted(...)[0]`` here previously called a
    within-tolerance row an outright "o2i #1" while the Winner column
    correctly rendered "tie (..., o2i)" for the identical row). When a
    lexicon-backed stock value would have scored lowest of all systems,
    an informational aside names it and its score
    (:func:`_lexicon_backed_informational_note`) — visible, never
    hidden, just not ranked. Kept short and scannable — this is the
    summary a reader checks first, before the per-language tables
    below."""
    disp = _lang_heading(lang)
    values = _rules_only_values(primary_row)
    if not values:
        # C-plausible: don't flatly say "no comparable systems" when a
        # NON-primary registered dataset for this language DOES have a
        # real (non-same-source) comparison — that reads as contradicting
        # the per-language table right below it. Point there instead.
        if other_rows and any(
                _rules_only_values(r) for r in other_rows
                if r is not primary_row):
            return (f"**{disp}** — primary gold has no comparable "
                    f"systems (same-source); see the per-language table "
                    f"below for a comparison on a secondary gold")
        return f"**{disp}** — no comparable systems for this gold"
    labeled = {_lexicon_free_label(k): v for k, v in values.items()}
    ranked = sorted(values.items(), key=lambda kv: kv[1])
    winner_val = ranked[0][1]
    tie_winners = _ranked_winners(labeled)
    aside = _lexicon_backed_informational_note(primary_row, winner_val)
    if "o2i" not in values:
        winner_str = _winner_label_str(tie_winners)
        if primary_row.get("o2i_same_source"):
            return (f"**{disp}** — o2i not scored: this gold was drafted "
                     f"by o2i's own lineage — see same-source "
                     f"({winner_str} #1 among the rest){aside}")
        return (f"**{disp}** — {winner_str} #1 "
                f"(o2i not scored on this gold){aside}")
    if min(values.values()) > _NO_SYSTEM_USABLE_THRESHOLD:
        return f"**{disp}** — no system is usable on this gold"
    if "o2i" in tie_winners:
        if len(tie_winners) == 1:
            if len(ranked) > 1:
                runner_up = _lexicon_free_label(ranked[1][0])
                return f"**{disp}** — o2i #1 (beats {runner_up}){aside}"
            return f"**{disp}** — o2i #1{aside}"
        return f"**{disp}** — {_winner_label_str(tie_winners)} #1{aside}"
    winner_str = _winner_label_str(tie_winners)
    o2i_rank = next(i for i, (k, _v) in enumerate(ranked, 1) if k == "o2i")
    return f"**{disp}** — {winner_str} #1, o2i #{o2i_rank}{aside}"


def _leaderboard_summary(rows: List[dict]) -> List[str]:
    """The compact per-language standings block that opens the doc, built
    from each language's configured PRIMARY gold row (``_primary_rows``)
    — one line per language, not one per table row."""
    primary = _primary_rows(rows)
    by_lang = {r["lang"]: r for r in primary}
    all_rows_by_lang: Dict[str, List[dict]] = {}
    for r in rows:
        all_rows_by_lang.setdefault(r["lang"], []).append(r)
    lines = ["## Leaderboard", "", (
        "One line per language: the best system on its primary gold, "
        "and where o2i lands. **Ranking policy: lexicon-free only** — "
        "a system's bundled per-word exception dictionary/lexicon never "
        "counts toward \"winner\", on the fair-comparison principle that "
        "o2i, by hard rule, ships no such lexicon of its own (see "
        "\"How to read this\" below for the full rationale and the "
        "per-engine disposition)."
    ), "", (
        "- **same-source** — the gold IS that system's own output; "
        "excluded from ranking, never a \"winner\"."
    ), (
        "- **n/a** — the system has no mapping, or isn't installed, for "
        "this language."
    ), (
        "- **(lexicon)** — a lexicon-backed stock value: shown on the "
        "board for information, never ranked. Its rules-only sibling "
        "column (or the engine's own audited-lexicon-free stock value) "
        "is what actually competes for \"winner\"."
    ), (
        "- **tie** — two or more systems within "
        f"{_WINNER_TIE_TOLERANCE} PER of the best; named, never a bare "
        "\"tie\"."
    ), (
        "- **rules-only** — the system with its bundled dictionary/"
        "lexicon disabled, scored on rules alone (see \"How to read "
        "this\" below)."
    ), (
        "- **#N** — N-th place by PER on that row, RANKED OVER THE "
        "LEXICON-FREE WORLD; `#1` is the winner."
    ), (
        "- **\"... with its lexicon scores N — informational\"** — a "
        "lexicon-backed stock value that would have scored lowest of "
        "all systems on this row, named so it is never hidden — just "
        "not counted as the winner."
    ), ""]
    for lang in sorted(by_lang):
        lines.append(f"- {_leaderboard_line(lang, by_lang[lang], all_rows_by_lang.get(lang))}")
    lines.append("")
    return lines


#: {system key: (repo name, one-line "what it adds over base o2i")} for
#: the o2i-downstream family section below. Order is display order.
_O2I_FAMILY_REPOS: List[Tuple[str, str, str]] = [
    ("arbtok", "arbtok",
     "Arabic diacritization, dialect lexicons, nativized loanwords, and "
     "code-switch handling on top of the shared `ar`/`arb` lattice "
     "(the RANKED `arbtok` column below runs with both bundled "
     "lexicons off for a fair lexicon-free comparison — see `arbtok "
     "(lexicon)` for the full-featured stock number)"),
    ("tugaphone", "tugaphone",
     "the curated `tugalex` pronunciation lexicon, sense-based homograph "
     "marking, and cross-dialect contact-language handling on top of the "
     "Portuguese-family lattice"),
    ("barranquenho", "g2p_barranquenho",
     "the Barranquenho (Spanish/Portuguese contact variety) rule layer "
     "on top of the `ext-PT-x-barrancos` lattice"),
    ("mwl_phonemizer", "mwl_phonemizer",
     "Mirandese dialect selection, an optional native-speaker lexicon "
     "overlay, and CRF correction on top of the `mwl` lattice"),
]


#: {row field: display name} for the family-version pin sentence below —
#: parallel to the espeak-ng version pin in the "Rules-only columns"
#: section ("espeak-ng 1.52.0 pinned").
_FAMILY_VERSION_FIELDS: List[Tuple[str, str]] = [
    ("arbtok_version", "arbtok"),
    ("tugaphone_version", "tugaphone"),
    ("barranquenho_version", "g2p_barranquenho"),
    ("mwl_phonemizer_version", "mwl_phonemizer"),
]


def _family_versions_note(rows: List[dict]) -> str:
    """One sentence naming the exact PyPI-published version of each o2i
    family engine the COMMITTED rows were actually produced with —
    reproducibility parallel to the espeak-ng version pin ("espeak-ng
    1.52.0 pinned") in the "Rules-only columns" section below. Reads the
    version straight off the rows themselves (``<system>_version``, set
    at scoring time via ``importlib.metadata.version()`` — see
    ``_installed_version``), so it can never drift out of sync with what
    actually produced the committed numbers. Empty string if no row
    carries any family version yet (e.g. none of the family systems were
    installed when the board was last regenerated)."""
    versions: Dict[str, str] = {}
    for row in rows:
        for field, label in _FAMILY_VERSION_FIELDS:
            v = row.get(field)
            if v and label not in versions:
                versions[label] = v
    if not versions:
        return ""
    parts = ", ".join(f"{label} {versions[label]}"
                       for _field, label in _FAMILY_VERSION_FIELDS
                       if label in versions)
    return (f"*Versions pinned: the family rows above were produced with "
            f"{parts} — every one of these exact versions is published "
            f"on PyPI as a pre-release alpha (verified with `pip index "
            f"versions <pkg> --pre`), so the number is reproducible from "
            f"a plain `pip install --pre <pkg>==<version>` even on "
            f"generating environments that installed a local/editable "
            f"checkout at the same version instead.*")


def _o2i_family_section(rows: List[dict]) -> List[str]:
    """A dedicated, FIRST-CLASS section for the o2i-downstream family
    (owner directive: "arbtok tugaphone and all o2i downstreams need to
    show in docs as first class, they show how o2i can be improved
    further") — distinct from the "other G2P systems" framing the rest of
    this document uses for espeak/epitran/gruut/etc., which are genuinely
    external projects o2i is compared AGAINST. The family is not that: it
    is built directly on o2i's own lattice, so a family member's win over
    bare o2i is not a competitor beating this project — it is a
    downstream feature (a lexicon, a dialect rule, a normalization pass)
    o2i itself does not yet carry, made visible as measured headroom.
    Measurement rigor is unchanged from the rest of the document: same
    same-source labels, same lexicon-ranking exclusion for tugaphone, same
    honest numbers whichever way they land — only the FRAMING differs."""
    lines = [
        "## The o2i family",
        "",
        "orthography2ipa is a shared lattice — a grapheme table plus "
        "allophone/sandhi rules per language variety — that several "
        "TigreGotico projects build directly on top of, adding what the "
        "shared lattice deliberately leaves to the caller (lexicons, "
        "diacritization, dialect selection, normalization). These are "
        "FIRST-CLASS to this board, not \"other G2P systems\" being "
        "compared against o2i as competitors:",
        "",
    ]
    version_note = _family_versions_note(rows)
    if version_note:
        lines.extend([version_note, ""])
    for key, repo, delta in _O2I_FAMILY_REPOS:
        lines.append(
            f"- **[{repo}](https://github.com/TigreGotico/{repo})** — adds "
            f"{delta}.")
    lines.extend([
        "",
        "**Reading a family row: headroom, not a loss.** Where a family "
        "system's PER beats bare o2i's on a row that is NOT `same-source` "
        "(see below — same-source rows are refused as a comparison "
        "point, exactly like every other system on this board), that gap "
        "is a concrete demonstration of what the shared `orthography2ipa` "
        "specs could still absorb into the base lattice — a diacritizer "
        "pass, a closed-class lexicon, a dialect rule — not evidence o2i "
        "\"lost\" to a competitor. Where a family row instead ties o2i "
        "exactly, that is equally informative: it means the family "
        "member's extra stages are not (yet, or not on this gold) adding "
        "anything the base lattice does not already do on its own.",
        "",
        "**Measurement stays unchanged.** Every family row is scored "
        "under the exact same discipline as every other system on this "
        "board: the SAME `same-source` refusal when a family engine "
        "would be scored against gold drawn from o2i's own lineage (see "
        "\"How to read this\" below — all four family engines are built "
        "on o2i's lattice, so they inherit o2i's own same-source exposure "
        "1:1); the SAME lexicon-vs-rules-only discipline — g2p_barranquenho "
        "and mwl_phonemizer's lexicon-free DEFAULT configuration are "
        "ranked normally; arbtok's DEFAULT is lexicon-backed (a "
        "145,890-entry stem lexicon plus a per-lect dialect lexicon, "
        "both on), so the ranked `arbtok` column is a deliberately "
        "NON-default configuration (`lexicon=None, "
        "dialect_lexicon=False`) leaving only the rule path plus a "
        "22-entry closed demonstrative-pronoun exception table with no "
        "independent toggle, while the unmodified stock number is shown "
        "separately as the informational `arbtok (lexicon)` column; "
        "tugaphone's always-on `tugalex` lexicon has no public disable "
        "switch at all, so it is excluded from the lexicon-free "
        "Winner/leaderboard ranking the same way — and the SAME honest "
        "reporting either way, a family engine beating o2i is reported "
        "as loudly as a tie.",
        "",
    ])
    return lines


def _render_language_tables(rows: List[dict]) -> List[str]:
    """The main comparison table, split into one sub-table per language
    under a ``### <lang>`` heading, one row per registered gold dataset.
    Columns a language group has nothing but ``n/a`` for are dropped."""
    by_lang: Dict[str, List[dict]] = {}
    for r in rows:
        by_lang.setdefault(r["lang"], []).append(r)

    lines = ["## Results by language", ""]
    for lang in sorted(by_lang):
        group = sorted(by_lang[lang], key=lambda r: r["dataset"])
        lines.append(f"### {_lang_heading(lang)}")
        lines.append("")
        present = _group_present_systems(group)
        header = ["Dataset", "N", "o2i"] + [label for _, label in present] \
            + ["Winner"]
        lines.append("| " + " | ".join(header) + " |")
        lines.append("|" + "---|" * len(header))
        for row in group:
            cells = [row["dataset"], str(row["n"]), _cell(row, "o2i")]
            cells += [_row_cell(row, key) for key, _ in present]
            cells.append(_winner(row))
            lines.append("| " + " | ".join(cells) + " |")
        lines.append("")
    return lines


def _fair_comparison_2x2_lines(rows: List[dict]) -> List[str]:
    """The dictionary-vs-rules 2x2 section: isolates espeak-ng's
    word-exception dictionary from its letter-to-sound rules on the same
    gold rows, for the ``DICTSOURCE_LANG``-mapped language subset."""
    lex_rows = [r for r in rows if r.get("o2i_lex_per") is not None
                or r.get("espeak_rules_per") is not None]
    rules_beats_stock = [
        r for r in rows
        if r.get("espeak_per") is not None and r.get("espeak_rules_per") is not None
        and not r.get("espeak_same_source") and not r.get("espeak_rules_same_source")
    ]
    n_rules_wins = sum(1 for r in rules_beats_stock
                        if r["espeak_rules_per"] < r["espeak_per"])
    lines = [
        "## Fair-comparison 2x2 (dictionary vs. rules)",
        "",
        "The table above conflates espeak-ng's letter-to-sound RULES with "
        "its hand-curated word-EXCEPTION list (o2i, by hard rule, ships no "
        "such list). This 2x2 isolates the dictionary's contribution on "
        "the same gold rows, for the languages where both extra columns "
        "are wired up (the `DICTSOURCE_LANG`-mapped subset — see the "
        "script's module docstring for how to enable `espeak_rules` via "
        "`scripts/build_espeak_rules_only.sh` and `o2i_lex` via "
        "`$ESPEAK_DICTSOURCE_PATH`). The dictionary is not a one-way "
        f"upgrade: across every row with both numbers, espeak-ng's "
        f"rules-only column actually BEATS stock (dictionary-included) "
        f"espeak-ng on {n_rules_wins} of {len(rules_beats_stock)} rows — "
        f"the word-exception list sometimes makes espeak-ng WORSE (e.g. "
        f"letter-spelling acronyms getting a dictionary hit that is "
        f"wrong for the gold's convention), not always better.",
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
    ]
    if lex_rows:
        for row in lex_rows:
            lines.append(
                f"| {row['lang']} | {row['dataset']} | {row['n']} | "
                f"{_cell(row, 'o2i')} | {_fmt(row.get('o2i_lex_per'))} | "
                f"{_cell(row, 'espeak')} | "
                f"{_cell(row, 'espeak_rules')} |"
            )
    else:
        lines.append("| _(none)_ | | | | | | |")
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
    return lines


def _details_block_lines(rows: List[dict], scoreboard_note: str,
                          espeak_rules_note: str,
                          gold_comparable: List[dict], gold_wins: int,
                          agreement_comparable: List[dict],
                          agreement_wins: int) -> List[str]:
    """The bottom-of-doc collapsible block: coverage caveats, per-tier
    win tallies, staleness/coverage notes, and the regen commands — all
    kept, none deleted, just moved out from between the title and the
    table so a reader hits data before methodology."""
    lines = [
        "<details>",
        "<summary>Coverage, staleness notes, and how to regenerate this "
        "table</summary>",
        "",
        "### Coverage",
        "",
        "Not every gold language has a mapping for every competitor "
        "system: espeak-ng, epitran, gruut, pycotovia, ahotts-g2p, and "
        "africa-g2p each cover a different, smaller subset of languages "
        "than orthography2ipa's 493 language codes. "
        "`epitran`/`gruut`/`pycotovia`/`ahotts-g2p` are only installed "
        "via the dev-only `[compare]` extra; a committed run generated "
        "without them shows `n/a` in those columns for every row — that "
        "reflects the generating environment, not a claim those systems "
        "don't support the language.",
        "",
        "**`eu-wikipron` is not a 37th language.** It is the SAME Basque "
        "spec as `eu`, registered as a separate board entry only so its "
        "independent `wikipron` gold can be the language's PRIMARY row "
        "for the leaderboard, instead of `eu`'s primary "
        "`hitz_basque_ipa` — which comes from HiTZ/Aholab, the same lab "
        "behind `ahotts-g2p`, and is close to same-source for that "
        "system (see the ahotts-g2p note below). Both entries score the "
        "identical set of gold datasets; only which one is PRIMARY "
        "differs.",
        "",
        "**ahotts-g2p output space.** `ahotts-g2p` (Aholab / HiTZ AhoTTS "
        "G2P port; `eu`, `es`) emits its transcription in the StyleTTS2 "
        "single-character training convention: the library's `MULTI` "
        "table folds affricates (`tʃ`→`C`, `ts`→`V`, `tʂ`→`P`), "
        "aspirates (`pʰ`→`H`, `kʰ`→`K`, `tʰ`→`T`) and **stress-marked "
        "vowels** (`ˈi`→`I` … `ˈu`→`U`) onto single ASCII letters. "
        "Scoring that raw against IPA gold would charge a spurious error "
        "on every uppercase char, so the harness UNFOLDS it back to "
        "standard IPA (the inverse of `ahotts_g2p.phones.MULTI`) before "
        "scoring. The two ahotts-g2p `version`s (`classic`/`modern`) "
        "produce near-identical output; the committed rows use "
        "`classic` (see the `ahotts_version` field in "
        "`benchmarks/comparison.json`). The `eu` `hitz_basque_ipa` gold "
        "is authored by HiTZ/Aholab, the same lab behind AhoTTS, so "
        "ahotts-g2p's very low PER there is close to same-source — the "
        "independent `eu` `wikipron` (Wiktionary) row is the fairer "
        "comparison. The audio-only `pyahotts` package is NOT a "
        "comparison system here (no phoneme output).",
        "",
        "**africa-g2p coverage.** `africa-g2p` (Ghana NLP; rule-based "
        "G2P for ~400 African-language ISO 639-3 codes) is not on PyPI, "
        "so it is not part of the `[compare]` extra — install it from a "
        "locally built wheel of the upstream checkout before "
        "regenerating this table (see the script's module docstring). "
        "Rows only appear for gold languages BOTH orthography2ipa and "
        "africa-g2p's own `registry()` cover — 10 languages as of this "
        "run: `arb`, `cop`, `hts`, `kab`, `ktz`, `lad`, `mfe`, `ngh`, "
        "`nup`, `tzm`. None of these ten has a matching espeak-ng voice, "
        "epitran code, or gruut language on this machine either, so "
        "africa-g2p is currently the only comparison point for these "
        "rows.",
        "",
        "### Staleness",
        "",
        scoreboard_note,
        "",
        "**espeak-rules-only coverage.** `espeak-rules-only` (the "
        "`espeak_rules_per` field) is a permanent column on this board: "
        "espeak-ng compiled from its own letter-to-sound rules with "
        "every per-language word-exception list "
        "(`_list`/`_listx`/`_extra`) emptied first — see "
        "`scripts/build_espeak_rules_only.sh`. " + espeak_rules_note,
        "",
        "### Win tallies",
        "",
        "Counted over distinct LANGUAGES (one row per language: its "
        "configured primary gold dataset — see `_primary_rows`), never "
        "over table rows, split by whether the primary gold is an "
        "independent reference or another tool's/LLM's output:",
        "",
    ]
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
            f"agreement with the generating tool, not accuracy): o2i "
            f"beats espeak on {agreement_wins} of "
            f"{len(agreement_comparable)} comparable languages."
        )
    else:
        lines.append(
            "- **Agreement-tier**: no language's primary gold was "
            "espeak-comparable in this run."
        )
    lines.extend([
        "",
        "### Regenerate",
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
        "</details>",
        "",
    ])
    return lines


def write_comparison(
        rows: List[dict],
        catalan_voices: Optional[Dict[str, Optional[str]]] = CATALAN_DIALECT_VOICES,
) -> None:
    """Write the comparison board (JSON) and the rendered document (Markdown).

    *catalan_voices* defaults to the resolved :data:`CATALAN_DIALECT_VOICES`
    rather than to ``None`` because the document is rewritten WHOLE on every
    call, including a single-language ``--lang`` refresh that rescored none of
    the Catalan rows. With a ``None`` default, any caller that simply did not
    think about Catalan silently DELETED the committed "Catalan dialects vs
    espeak (BSC)" section from the published document — a partial rerun must
    never be able to drop a section it did not touch. Pass ``None`` explicitly
    to suppress the section on purpose.
    """
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
    espeak_rules_note = _espeak_rules_coverage_note(rows)

    lines = [
        "# Comparison to other G2P systems",
        "",
        "This table shows how well orthography2ipa (o2i) predicts IPA "
        "pronunciation compared to eleven other G2P systems (including the "
        "four o2i-downstream family engines — arbtok, tugaphone, "
        "g2p_barranquenho, mwl_phonemizer), on the same gold word lists, "
        "language by language.",
        "",
        "Every number is a **PER (Phoneme Error Rate)**: lower is "
        "better, `0.0000` is a perfect match, and it CAN exceed `1.0` "
        "when a system's output is much longer or shorter than the gold "
        "(more edits than the gold has phonemes).",
        "",
    ]
    lines.extend(_leaderboard_summary(rows))
    lines.extend(_o2i_family_section(rows))
    lines.extend(_render_language_tables(rows))
    lines.extend([
        "## How to read this",
        "",
        "**Systems compared.** o2i vs **espeak-ng**, **espeak-ng "
        "rules-only**, **epitran**, **gruut**, **gruut rules-only**, "
        "**pycotovia** (Galician & Spanish), **ahotts-g2p** "
        "(Basque & Spanish), and "
        "**africa-g2p** (10 African-language rows) — seven systems, two "
        "of which (espeak-ng, gruut) also get a rules-only column. Each "
        "system covers a different subset of languages. A missing "
        "mapping, or a system not installed in the generating "
        "environment, shows as `n/a` — never skipped, never faked.",
        "",
        "**Rules-only columns, and why only two engines have one.** A "
        "\"rules-only\" column runs the SAME engine with its bundled "
        "dictionary/lexicon disabled, so it can only fall back on its "
        "own letter-to-sound rules or g2p model — the fair comparison "
        "against o2i, which by hard rule ships no word-exception list "
        "of its own. Disposition per engine:",
        "",
        "- **espeak-ng** — `espeak_rules`: its dictsource "
        "`_list`/`_listx`/`_extra` word-exception files emptied before "
        "compiling (`scripts/build_espeak_rules_only.sh`, espeak-ng "
        "1.52.0 pinned). Every number is verified before publishing: the "
        "build's manifest must list the language AND the compiled "
        "dictionary must differ from the stock one by md5 "
        "(`assert_espeak_rules_built_for`) — an earlier version of this "
        "board published a stock-vs-stock \"comparison\" for `es` "
        "because that check did not exist yet.",
        "- **gruut** — `gruut_rules`: its bundled lexicon lookup "
        "(`TextProcessorSettings.lookup_phonemes`) disabled at runtime "
        "so every word falls through to gruut's own g2p fallback model "
        "instead of a dictionary hit. This exists because gruut's "
        "`en-US` lexicon (124,392 words) turned out to be CMUdict-"
        "derived and covers 98.2% of both the `cmudict` and `ipadict` "
        "gold sets — see the same-source note below for those two rows.",
        "- **epitran** is a rule/mapping-based transliterator for the "
        "languages this board scores, not a lexicon lookup, so there is "
        "no dictionary to strip; the `es`/`gl` gold it is scored against "
        "uses a BROAD transcription convention (no ð/β/ɣ/θ allophone "
        "diacritics, glide notation folded) rather than the narrow one "
        "o2i and espeak-ng target — see the note on that below.",
        "- **pycotovia** — audited: its lexicon is closed to function-"
        "word stress tables (a small, fixed, rule-grade set, not a "
        "general word dictionary), so there is no general-purpose "
        "lexicon to disable and no rules-only column is needed.",
        "- **ahotts-g2p** — audited: it ships an HDIC dictionary "
        "(1,990 expansion entries; 103 TF_MRK words whose phonetic "
        "transcription is supplied directly by the dictionary; 1,065 "
        "per-word allophone-exception and 293 stress-marked entries), "
        "but those entries hit only 1.5% of the `eu` wikipron gold "
        "and 2.6% of `hitz_basque_ipa`, so a rules-only column would "
        "move the number by a fraction of a percent — recorded here "
        "rather than given a column.",
        "",
        "**Ranking policy: lexicon-free only.** Anything with a "
        "lexicon does not count as a winner. The Winner column and the "
        "leaderboard rank over LEXICON-FREE values only: each engine's "
        "rules-only variant where one exists (`espeak_rules`, "
        "`gruut_rules`), its stock value where the engine is audited "
        "lexicon-free (epitran's rule/mapping tables, pycotovia's "
        "closed function-word stress table, africa-g2p's rule-based "
        "G2P), and ahotts-g2p's stock value — its HDIC dictionary hits "
        "only 1.5%/2.6% of the `eu`/`hitz_basque_ipa` gold, an explicit "
        "documented exception, not an oversight (see the per-engine "
        "disposition above). A lexicon-BACKED stock value — plain "
        "`espeak`, plain `gruut`, and (once it lands) a "
        "`transphone`-style tokenizer column — is EXCLUDED from ranking "
        "entirely, on the fair-comparison principle that o2i, by hard "
        "rule, ships no bundled word-exception lexicon of its own: "
        "ranking o2i's rules against another system's rules-plus-"
        "dictionary is not a fair fight (see the module docstring's "
        "\"Fair-comparison 2x2\" section, which this policy generalizes "
        "from a side table into the primary ranking). This is a "
        "deliberate ranking policy, not hidden data — the lexicon-"
        "backed columns stay right there on the board, marked "
        "`(lexicon)`, for anyone who wants the dictionary-included "
        "picture; the leaderboard just also names, as an informational "
        "aside, whenever a lexicon-backed value would have scored "
        "lowest of all (`espeak with its lexicon scores N — "
        "informational`) — visible, never counted.",
        "",
        "**Symmetric alternative (not implemented).** The fair-"
        "comparison principle cuts both ways: a lexicon-BACKED ranking "
        "tier is equally possible, PROVIDED o2i is given the same "
        "per-word lexicon the competitor ships (exactly what `o2i_lex` "
        "in the \"Fair-comparison 2x2\" section below already does for "
        "espeak-ng's dictionary, on the languages that 2x2 covers). That "
        "tier is not wired into the Winner column or leaderboard today "
        "— extending it to every lexicon-backed system/language pair on "
        "this board, and rendering it as a second ranked tier rather "
        "than a side table, is future work.",
        "",
        "**Winner column.** The lowest PER on the row IN THE LEXICON-"
        "FREE WORLD (see \"Ranking policy\" above), by name; ties "
        f"(within {_WINNER_TIE_TOLERANCE} PER) name every system tied "
        "for best rather than a bare `tie`. `same-source` cells never "
        "win — they are not real comparisons. When even the best PER on "
        "a row exceeds "
        f"{_NO_SYSTEM_USABLE_THRESHOLD}, the cell says "
        "\"no system is usable on this gold\" instead of naming a "
        "misleadingly precise \"winner\" among systems that are all "
        "failing it.",
        "",
        "**`same-source` cells.** A cell reads `same-source` (never "
        "`n/a`) when the gold dataset IS that system's own output — "
        "e.g. scoring `espeak` against `ipa_babylm` (espeak-derived), "
        "`ahotts-g2p` against `hitz_basque_ipa` (HiTZ's own phonemizer "
        "output, same lab as AhoTTS), or `gruut` (dictionary lookup, "
        "not `gruut_rules`) against `cmudict`/`ipadict` (gruut's `en-US` "
        "lexicon is CMUdict-derived — see above). Scoring a system "
        "against its own generator would score near-zero by "
        "construction, not because it is accurate, so that comparison "
        "is refused. The same rule applies to o2i itself on "
        "`arabic_tts`, `portuguese_tts`, and `gold20_arabic` — gold "
        "drafted by the same Claude lineage that wrote orthography2ipa's "
        "own Arabic/Portuguese specs.",
        "",
        "**epitran's `es`/`gl` gold uses a broad transcription "
        "convention.** The wikipron gold rows for `es` and `gl` (and "
        "epitran's own output) are scored in the BROAD IPA convention — "
        "no allophonic diacritics (`ð β ɣ θ` etc.) and glide notation "
        "folded (`j w i̯ u̯` → `i u`) — rather than the narrower "
        "transcription o2i and espeak-ng aim for. #867 measured this "
        "directly: folding tier symbols out of both sides on `es`/"
        "`wikipron` moved o2i's PER from 0.0172 to 0.0090, and folding "
        "glide notation too moved it from 0.0099 to 0.0086 — most of a "
        "PER change on this row is notation converging, not an audible "
        "accuracy change. Read a narrow-vs-broad PER gap here as a "
        "convention difference, not a correctness gap.",
        "",
        "**Machine-generated gold measures agreement, not accuracy.** "
        "Some gold datasets are themselves another phonemizer's or an "
        "LLM's output (see each dataset's `provenance_tier` in "
        "`benchmarks/comparison.json`). A win on one of those rows shows "
        "how much a system agrees with the tool that generated the gold "
        "— it is not a correctness claim.",
        "",
        "**Normalization.** Every system is scored with the identical "
        "normalization and PER metric orthography2ipa's own scoreboard "
        "uses (`scripts/benchmark.py:normalize`/`levenshtein`): "
        "NFC-normalize, strip stress marks (length marks stay), strip "
        "narrow-transcription diacritics, drop whitespace, then score "
        "Levenshtein distance against the best-matching gold variant. No "
        "system gets a more forgiving metric.",
        "",
        "**Honesty.** This table includes languages where o2i **loses** "
        "to espeak-ng. Cherry-picking would make the comparison "
        "worthless. Every gold dataset a language has gets its own row — "
        "not just the flattering one — so a system winning on one gold "
        "and losing on another for the SAME language is visible here.",
        "",
        "**N** is the number of unique gold words for that "
        "language/dataset pair. A system's own scored count can be "
        "slightly lower — a word it failed to transcribe is excluded "
        "from its PER, not counted as an error — see the `*_n` fields in "
        "`benchmarks/comparison.json` for the exact per-system count. "
        "`N` can also differ from a PREVIOUS run of this same row for "
        "two unrelated reasons: `wikipron` gold is fetched live from its "
        "upstream GitHub repository and cached — a re-run against an "
        "empty cache picks up whatever Wiktionary-derived content is "
        "current upstream at fetch time, which drifts over time "
        "independent of any change here — `cy`/`wikipron`'s `N` in this "
        "regen (see the table above) differs from the previously "
        "committed board for exactly this reason, not an o2i or harness "
        "change; and a `sampled` row (below) "
        "draws a fixed-seed SUBSET whose exact size can differ slightly "
        "from run to run of the loader's own filtering, not from "
        "resampling.",
        "",
    ])
    lines.extend(_robustness_section(rows))
    lines.extend(_fair_comparison_2x2_lines(rows))
    if catalan_voices is not None:
        lines.extend(_catalan_dialect_table_lines(rows, catalan_voices))
    lines.extend(_details_block_lines(rows, scoreboard_note, espeak_rules_note,
                                       gold_comparable, gold_wins,
                                       agreement_comparable, agreement_wins))
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
                  f"arbtok={cfg.get('arbtok')} "
                  f"tugaphone={cfg.get('tugaphone')} "
                  f"barranquenho={cfg.get('barranquenho')} "
                  f"mwl_phonemizer={cfg.get('mwl_phonemizer')} "
                  f"dictsource_lang={DICTSOURCE_LANG.get(lang)}")
        return

    for row in compare_lang(args.lang, args.limit):
        print(f"lang={row['lang']} dataset={row['dataset']} n={row['n']} "
              f"o2i={_fmt(row['o2i_per'])} "
              f"o2i_lex={_fmt(row.get('o2i_lex_per'))} "
              f"espeak={_cell(row, 'espeak')} "
              f"espeak_rules={_cell(row, 'espeak_rules')} "
              f"epitran={_cell(row, 'epitran')} gruut={_cell(row, 'gruut')} "
              f"gruut_rules={_fmt(row.get('gruut_rules_per'))} "
              f"pycotovia={_fmt(row.get('pycotovia_per'))} "
              f"ahotts={_cell(row, 'ahotts')} "
              f"africa_g2p={_fmt(row.get('africa_g2p_per'))} "
              f"arbtok={_cell(row, 'arbtok')} "
              f"tugaphone={_cell(row, 'tugaphone')} "
              f"barranquenho={_cell(row, 'barranquenho')} "
              f"mwl_phonemizer={_cell(row, 'mwl_phonemizer')}")


if __name__ == "__main__":
    main()
