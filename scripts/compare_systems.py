#!/usr/bin/env python3
"""Compare orthography2ipa against other G2P systems on the same gold rows.

Runs the SAME gold word/IPA pairs used by ``scripts/benchmark.py`` through
several systems — orthography2ipa, espeak-ng, epitran, gruut, pycotovia,
and pyahotts — and scores every system with the exact same normalization
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
- **pyahotts**: optional Python library (``pip install .[compare]``), a
  pure-Python port of AhoTTS (Aholab, Univ. of the Basque Country).
  Its only public API (``AhoTTS.get_tts``) synthesizes audio (WAV bytes)
  and exposes no text-level phoneme/IPA output, so there is nothing to
  score against gold IPA transcriptions — ``pyahotts_transcribe`` always
  returns ``None`` and the column is reported ``n/a`` for every row. This
  is documented rather than silently dropped: the library is real and
  installable, it simply doesn't expose the output this harness compares.

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
# competitor systems only cover a fraction of orthography2ipa's 350+ codes.
LANGS: Dict[str, dict] = {
    "en-US": {"dataset": ("cmudict", "en-US"), "espeak": "en-us",
               "epitran": "eng-Latn", "gruut": "en-us"},
    "en": {"dataset": ("wikipron", "en"), "espeak": "en-gb",
           "epitran": "eng-Latn", "gruut": "en-gb"},
    "es": {"dataset": ("wikipron", "es"), "espeak": "es",
           "epitran": "spa-Latn", "gruut": "es"},
    "pt-PT": {"dataset": ("portuguese_lexicon", "pt-PT"), "espeak": "pt",
              "epitran": "por-Latn", "gruut": "pt"},
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
    "eu": {"dataset": ("hitz_basque_ipa", "eu"), "espeak": "eu",
           "epitran": None, "gruut": None, "pyahotts": "eu"},
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
}


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


def espeak_transcribe(word: str, voice: str) -> Optional[str]:
    """Transcribe *word* with espeak-ng, or ``None`` on any failure."""
    try:
        proc = subprocess.run(
            # "--" ends option parsing so a gold word starting with "-"
            # is treated as text, not misparsed as an espeak-ng flag
            ["espeak-ng", "-q", "--ipa", "-v", voice, "--", word],
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


# ─── pyahotts (lazy, optional) ──────────────────────────────────────────────

def pyahotts_transcribe(word: str, lang: str) -> Optional[str]:
    """Always ``None``: pyahotts's only public API (``AhoTTS.get_tts``)
    synthesizes audio and exposes no text-level phoneme/IPA output, so
    there is nothing to score against gold IPA transcriptions. Kept as a
    real function (rather than omitted) so the ``n/a`` in the comparison
    table is a documented, tested outcome, not a silent gap."""
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


def compare_lang(lang: str, limit: int) -> dict:
    """Run *lang* through every available system on the same gold rows.
    Returns a row dict with per-system PER (or ``None`` == "n/a")."""
    cfg = LANGS[lang]
    dataset_name, loader_lang = cfg["dataset"]
    loader, _ = benchmark.DATASETS[dataset_name]
    pairs = loader(loader_lang, limit)

    refs: Dict[str, List[str]] = {}
    for word, gold in pairs:
        refs.setdefault(word, []).append(gold)
    words = sorted(refs)

    from orthography2ipa import G2P
    engine = G2P(lang)

    o2i_rows: List[Tuple[Optional[str], List[str]]] = []
    espeak_rows: List[Tuple[Optional[str], List[str]]] = []
    epitran_rows: List[Tuple[Optional[str], List[str]]] = []
    gruut_rows: List[Tuple[Optional[str], List[str]]] = []
    pycotovia_rows: List[Tuple[Optional[str], List[str]]] = []
    pyahotts_rows: List[Tuple[Optional[str], List[str]]] = []

    use_espeak = cfg["espeak"] is not None and espeak_available()
    use_epitran = cfg["epitran"] is not None
    use_gruut = cfg["gruut"] is not None
    use_pycotovia = cfg.get("pycotovia") is not None
    use_pyahotts = cfg.get("pyahotts") is not None

    for word in words:
        golds = refs[word]
        try:
            o2i_rows.append((engine.transcribe_word(word), golds))
        except Exception:
            o2i_rows.append((None, golds))

        if use_espeak:
            espeak_rows.append((espeak_transcribe(word, cfg["espeak"]), golds))
        if use_epitran:
            epitran_rows.append((epitran_transcribe(word, cfg["epitran"]), golds))
        if use_gruut:
            gruut_rows.append((gruut_transcribe(word, cfg["gruut"]), golds))
        if use_pycotovia:
            pycotovia_rows.append(
                (pycotovia_transcribe(word, cfg["pycotovia"]), golds))
        if use_pyahotts:
            pyahotts_rows.append(
                (pyahotts_transcribe(word, cfg["pyahotts"]), golds))

    o2i_per, o2i_n = _score(o2i_rows)
    espeak_per, espeak_n = _score(espeak_rows) if use_espeak else (None, 0)
    epitran_per, epitran_n = _score(epitran_rows) if use_epitran else (None, 0)
    gruut_per, gruut_n = _score(gruut_rows) if use_gruut else (None, 0)
    pycotovia_per, pycotovia_n = (
        _score(pycotovia_rows) if use_pycotovia else (None, 0))
    pyahotts_per, pyahotts_n = (
        _score(pyahotts_rows) if use_pyahotts else (None, 0))

    return {
        "lang": lang,
        "dataset": dataset_name,
        "n": len(words),
        "o2i_per": round(o2i_per, 4) if o2i_per is not None else None,
        "o2i_n": o2i_n,
        "espeak_per": round(espeak_per, 4) if espeak_per is not None else None,
        "espeak_n": espeak_n,
        "espeak_voice": cfg["espeak"],
        "epitran_per": round(epitran_per, 4) if epitran_per is not None else None,
        "epitran_n": epitran_n,
        "gruut_per": round(gruut_per, 4) if gruut_per is not None else None,
        "gruut_n": gruut_n,
        "pycotovia_per": round(pycotovia_per, 4) if pycotovia_per is not None else None,
        "pycotovia_n": pycotovia_n,
        "pyahotts_per": round(pyahotts_per, 4) if pyahotts_per is not None else None,
        "pyahotts_n": pyahotts_n,
        "harness_version": HARNESS_VERSION,
        "limit": limit,
    }


def build_comparison(limit: int) -> List[dict]:
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
        "and **pyahotts** (Basque) on the same gold datasets/loaders as "
        "[`docs/scoreboard.md`](scoreboard.md), using the same default "
        "`--limit` — so the `o2i PER` column here matches the "
        "scoreboard's rows for the same language/dataset pair. "
        "Regenerate with:",
        "",
        "```bash",
        "pip install '.[compare]'  # epitran, gruut, pycotovia, "
        "pyahotts — dev-only extra",
        "PYTHONPATH=$PWD python scripts/compare_systems.py --scoreboard",
        "```",
        "",
        "Machine-readable form: "
        "[`benchmarks/comparison.json`](../benchmarks/comparison.json).",
        "",
        "## Coverage",
        "",
        "Not every gold language has a mapping for every competitor "
        "system: espeak-ng, epitran, gruut, pycotovia, and pyahotts each "
        "cover a different, smaller subset of languages than "
        "orthography2ipa's 350+ codes. A missing mapping, or a system "
        "that isn't installed, is reported as `n/a` for that row rather "
        "than skipped or faked — this table never crashes and never "
        "silently drops a system, it just says when it has nothing to "
        "compare. `epitran`/`gruut`/`pycotovia`/`pyahotts` are only "
        "installed via the dev-only `[compare]` extra; a committed run "
        "generated without them shows `n/a` in those columns for every "
        "row — that reflects the generating environment, not a claim "
        "those systems don't support the language. `pyahotts` is `n/a` "
        "for every row regardless of installation: its only public API "
        "synthesizes audio and exposes no text-level phoneme output, so "
        "there is nothing to compare against gold IPA (see the harness "
        "module docstring).",
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
        "gruut PER | pycotovia PER | pyahotts PER |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['lang']} | {row['dataset']} | {row['n']} | "
            f"{_fmt(row['o2i_per'])} | {_fmt(row['espeak_per'])} | "
            f"{_fmt(row['epitran_per'])} | {_fmt(row['gruut_per'])} | "
            f"{_fmt(row.get('pycotovia_per'))} | "
            f"{_fmt(row.get('pyahotts_per'))} |"
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
    if catalan_voices is not None:
        lines.extend(_catalan_dialect_table_lines(rows, catalan_voices))
    os.makedirs(os.path.dirname(COMPARISON_MD), exist_ok=True)
    with open(COMPARISON_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--lang", default=None, choices=sorted(LANGS))
    ap.add_argument("--limit", type=int, default=300,
                    help="matches benchmark.py --scoreboard's default so "
                         "rows draw from the same gold slice")
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
                  f"pyahotts={cfg.get('pyahotts')}")
        return

    row = compare_lang(args.lang, args.limit)
    print(f"lang={row['lang']} n={row['n']} "
          f"o2i={_fmt(row['o2i_per'])} espeak={_fmt(row['espeak_per'])} "
          f"epitran={_fmt(row['epitran_per'])} gruut={_fmt(row['gruut_per'])} "
          f"pycotovia={_fmt(row.get('pycotovia_per'))} "
          f"pyahotts={_fmt(row.get('pyahotts_per'))}")


if __name__ == "__main__":
    main()
