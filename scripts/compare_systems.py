#!/usr/bin/env python3
"""Compare orthography2ipa against other G2P systems on the same gold rows.

Runs the SAME gold word/IPA pairs used by ``scripts/benchmark.py`` through
four systems — orthography2ipa, espeak-ng, epitran, and gruut — and scores
every system with the exact same normalization and PER metric
(``benchmark.normalize`` / ``benchmark.levenshtein``), so the numbers are
directly comparable to the committed scoreboard.

Systems are optional. If a system's tool/library is unavailable, or a
language has no explicit voice/code mapping for it, that system's column
is reported as ``n/a`` for that row — the script never crashes because a
comparison target is missing.

- **espeak-ng**: shelled out via ``espeak-ng -q --ipa -v <voice> <word>``,
  one process per word (small gold slices; simplicity over throughput).
  Detected with ``shutil.which("espeak-ng")``.
- **epitran**: optional Python library (``pip install .[compare]``),
  imported lazily. Needs an ISO 639-3 + ISO 15924 script code per
  language (e.g. ``spa-Latn``).
- **gruut**: optional Python library (``pip install .[compare]``),
  imported lazily. Needs a gruut language code (e.g. ``es``).

Normalization (identical across all four systems, see ``benchmark.normalize``
and the stress/diacritic handling in ``espeak_agreement.py``):

1. NFC-normalize.
2. Strip stress/length marks (``benchmark._STRESS_MARKS``): primary/secondary
   stress and length marks are never scored — no system agrees on where to
   place them consistently enough for that to be a fair signal.
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
           "epitran": None, "gruut": None},
    "ca": {"dataset": ("4catac", "ca"), "espeak": "ca",
           "epitran": "cat-Latn", "gruut": None},
    "cy": {"dataset": ("wikipron", "cy"), "espeak": "cy",
           "epitran": "cym-Latn", "gruut": None},
    "ga": {"dataset": ("wikipron", "ga"), "espeak": "ga",
           "epitran": None, "gruut": None},
    "ro": {"dataset": ("wikipron", "ro"), "espeak": "ro",
           "epitran": "ron-Latn", "gruut": None},
}


# ─── espeak-ng ───────────────────────────────────────────────────────────────

def espeak_available() -> bool:
    return shutil.which("espeak-ng") is not None


def espeak_transcribe(word: str, voice: str) -> Optional[str]:
    """Transcribe *word* with espeak-ng, or ``None`` on any failure."""
    try:
        proc = subprocess.run(
            ["espeak-ng", "-q", "--ipa", "-v", voice, word],
            capture_output=True, text=True, timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if proc.returncode != 0:
        return None
    out = proc.stdout.strip()
    return out or None


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

    use_espeak = cfg["espeak"] is not None and espeak_available()
    use_epitran = cfg["epitran"] is not None
    use_gruut = cfg["gruut"] is not None

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

    o2i_per, o2i_n = _score(o2i_rows)
    espeak_per, espeak_n = _score(espeak_rows) if use_espeak else (None, 0)
    epitran_per, epitran_n = _score(epitran_rows) if use_epitran else (None, 0)
    gruut_per, gruut_n = _score(gruut_rows) if use_gruut else (None, 0)

    return {
        "lang": lang,
        "dataset": dataset_name,
        "n": len(words),
        "o2i_per": round(o2i_per, 4) if o2i_per is not None else None,
        "o2i_n": o2i_n,
        "espeak_per": round(espeak_per, 4) if espeak_per is not None else None,
        "espeak_n": espeak_n,
        "epitran_per": round(epitran_per, 4) if epitran_per is not None else None,
        "epitran_n": epitran_n,
        "gruut_per": round(gruut_per, 4) if gruut_per is not None else None,
        "gruut_n": gruut_n,
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


def write_comparison(rows: List[dict]) -> None:
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
        "**espeak-ng**, **epitran**, and **gruut** on the SAME gold rows "
        "used by [`docs/scoreboard.md`](scoreboard.md). Regenerate with:",
        "",
        "```bash",
        "pip install '.[compare]'  # epitran, gruut — dev-only extra",
        "PYTHONPATH=$PWD python scripts/compare_systems.py --scoreboard",
        "```",
        "",
        "Machine-readable form: "
        "[`benchmarks/comparison.json`](../benchmarks/comparison.json).",
        "",
        "## Coverage",
        "",
        "Not every gold language has a mapping for every competitor "
        "system: espeak-ng, epitran, and gruut each cover a different, "
        "smaller subset of languages than orthography2ipa's 350+ codes. "
        "A missing mapping, or a system that isn't installed, is reported "
        "as `n/a` for that row rather than skipped or faked — this table "
        "never crashes and never silently drops a system, it just says "
        "when it has nothing to compare.",
        "",
        "## Normalization",
        "",
        "Every system is scored with the identical normalization and PER "
        "metric orthography2ipa's own scoreboard uses "
        "(`scripts/benchmark.py:normalize`/`levenshtein`): NFC-normalize, "
        "strip stress/length marks, strip narrow-transcription diacritics "
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
        "gruut PER |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['lang']} | {row['dataset']} | {row['n']} | "
            f"{_fmt(row['o2i_per'])} | {_fmt(row['espeak_per'])} | "
            f"{_fmt(row['epitran_per'])} | {_fmt(row['gruut_per'])} |"
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
    os.makedirs(os.path.dirname(COMPARISON_MD), exist_ok=True)
    with open(COMPARISON_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--lang", default=None, choices=sorted(LANGS))
    ap.add_argument("--limit", type=int, default=100)
    ap.add_argument("--list", action="store_true",
                    help="List languages this harness can compare")
    ap.add_argument("--scoreboard", action="store_true",
                    help="Run every mapped language and write "
                         "docs/comparison.md + benchmarks/comparison.json")
    args = ap.parse_args()

    if args.scoreboard:
        rows = build_comparison(args.limit)
        write_comparison(rows)
        print(f"wrote {len(rows)} rows to "
              f"{os.path.relpath(COMPARISON_MD, REPO_ROOT)} and "
              f"{os.path.relpath(COMPARISON_JSON, REPO_ROOT)}")
        return

    if args.list or not args.lang:
        for lang, cfg in sorted(LANGS.items()):
            print(f"{lang:10} espeak={cfg['espeak']} "
                  f"epitran={cfg['epitran']} gruut={cfg['gruut']}")
        return

    row = compare_lang(args.lang, args.limit)
    print(f"lang={row['lang']} n={row['n']} "
          f"o2i={_fmt(row['o2i_per'])} espeak={_fmt(row['espeak_per'])} "
          f"epitran={_fmt(row['epitran_per'])} gruut={_fmt(row['gruut_per'])}")


if __name__ == "__main__":
    main()
