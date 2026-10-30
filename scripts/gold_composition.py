"""Gold composition diagnostic: how much of a row's gold is alphabet-chart
noise rather than running text.

See docs/gold_composition.md for the method and the resulting tables.

WikiPron (and several other crowd-scraped golds) is built by scraping
Wiktionary headwords, and for small languages a Wiktionary edition often
carries a full "letters of the alphabet" appendix as regular headwords —
single letters, digraph names, diacritic variants — sitting in the same
TSV as real words. A row's headline PER blends both: a spec that gets the
grapheme table right can score near-perfect on the alphabet-chart rows
while telling you nothing about how it handles running text, and a small
gold set (order 100 entries) can be dominated by exactly that.

This script does not touch any spec or any board file. It reads the
already-scored rows in benchmarks/results.json, reloads each row's gold
from the on-disk ``.benchmark_cache`` (never fetching new data — a cache
miss makes the row unmeasurable and it is skipped, reported separately),
splits the gold into a "trivial" and a "real-word" subset per the
definition below, and scores each subset with the harness's own
``evaluate_words`` so the numbers sit in the same space as the board.

Usage: PYTHONPATH=. python scripts/gold_composition.py
"""
from __future__ import annotations

import json
import sys
import unicodedata
from typing import Dict, List, Optional, Sequence, Tuple
from unittest import mock

sys.path.insert(0, "scripts")

from benchmark import (DATASETS, SCOREBOARD_JSON,  # noqa: E402
                       _is_multiword, evaluate_words)

import orthography2ipa as o2i  # noqa: E402

GoldPair = Tuple[str, str]

#: An entry's gold set is unreachable ("no cached data") when the loader
#: would need to hit the network. Blocking urlretrieve makes that failure
#: explicit and deterministic instead of silently downloading fresh data
#: (which would make this script's numbers depend on network access and,
#: worse, on whatever happens to be cached on the machine that ran it).
_NETWORK_BLOCKED = "gold_composition.py: refusing to fetch new data " \
    "(row has no cached gold)"

#: U+0640 ARABIC TATWEEL (also used for Syriac/other Arabic-script-family
#: orthographies) is an elongation/joining placeholder, not a letter. Some
#: wikipron scrapes carry it as a literal prefix character on entries pulled
#: from an inflection-table cell (e.g. tru/wikipron's "ـܢܐ", "ـܢܝ" — bound
#: SUFFIX forms from a declension table, not free-standing words). Any entry
#: containing it is a different flavour of "not running text" than the
#: alphabet-chart case above: it is caught here explicitly rather than by
#: the length/coverage heuristic, since a bound-affix headword need not be
#: short (nor does its word need to match anything in the spec's alphabet).
_TATWEEL = "ـ"

#: A short-word-set is only trustworthy evidence of an alphabet chart if it
#: covers a healthy chunk of the spec's own declared grapheme inventory.
#: Chosen empirically: real gold sets with a handful of coincidentally
#: short real words (French "à", "y", Chinese monosyllables) come nowhere
#: near this; the wikipron alphabet-chart rows found so far (kwk, and the
#: Hadza case from an earlier wave) cover 60-95% of their spec's alphabet.
#: Set below that band, not at it, so a partial chart still trips it.
ALPHABET_COVERAGE_THRESHOLD = 0.3


def _base_form(word: str) -> str:
    """Case- and mark-folded form used for the alphabet-chart comparison.

    NFD-decomposes and drops combining marks (Unicode category Mn) so a
    diacritic-marked alphabet-chart headword (e.g. Kwak'wala "A̱", a base
    letter plus a combining macron below) still compares equal to its
    bare letter for the purpose of counting how much of the declared
    alphabet a gold set's short entries cover. This is ONLY used for the
    alphabet-coverage test, never for scoring (which uses the harness's
    own :func:`benchmark.normalize`).
    """
    decomposed = unicodedata.normalize("NFD", word)
    stripped = "".join(
        c for c in decomposed if unicodedata.category(c) != "Mn")
    return unicodedata.normalize("NFC", stripped).casefold()


def classify_gold(lang: str, pairs: Sequence[GoldPair]
                   ) -> Tuple[List[GoldPair], List[GoldPair], dict]:
    """Split *pairs* into (trivial, real) and return composition stats.

    Definition of "trivial", in order of what was tried:

    A naive length cutoff ("<=2 characters is trivial") was rejected: many
    registered languages have short real words (monosyllabic content
    words, single-letter function words like French "y" or English "a"),
    and a fixed length threshold would misclassify those identically
    across every language regardless of how that language's words are
    actually shaped.

    Instead this uses a structural signal tied to the SPEC's own declared
    alphabet (:attr:`LanguageSpec.graphemes`, which already lists
    multi-character units like digraphs as first-class "letters"): an
    entry is a candidate "short form" if its :func:`_base_form` (case- and
    diacritic-folded) is <=2 characters. If the set of DISTINCT short
    forms in this row's gold covers at least
    :data:`ALPHABET_COVERAGE_THRESHOLD` of the spec's own base-form
    grapheme inventory, the row's short entries are treated as an
    alphabet chart and marked trivial; below that coverage they are left
    as ordinary (short) real words. Multiword/sentence-level entries are
    never trivial — an alphabet chart is word-level.

    Separately, any single-word entry containing :data:`_TATWEEL` is
    trivial as a **bound affix** (see the constant's docstring) regardless
    of length or alphabet coverage — this is a distinct failure shape from
    the alphabet chart above, not a special case of it, and is reported
    under its own ``n_bound_affix`` count so the two are never conflated.

    Nothing here strips or normalizes punctuation, apostrophes, or any
    other character beyond combining marks (:func:`_base_form`'s NFD/Mn
    fold, used ONLY to compare against the spec's alphabet). In
    particular an apostrophe-class character is never treated as
    ignorable: some orthographies use it for a real phoneme (e.g. a
    pharyngealization or glottalization marker), and silently folding it
    away would make exactly the kind of gold entry this script exists to
    flag disappear from view instead. Scoring itself runs through
    :func:`benchmark.evaluate_words`, the same normalization the board
    uses, unmodified.
    """
    try:
        spec = o2i.get(lang)
        alphabet = {_base_form(g) for g in spec.graphemes}
    except Exception:
        alphabet = set()

    n_single = n_two = n_bound_affix = 0
    short_forms: Dict[str, int] = {}
    bound_idx: List[int] = []
    per_pair_base: List[Optional[str]] = []
    for i, (word, _gold) in enumerate(pairs):
        if _is_multiword(word):
            per_pair_base.append(None)
            continue
        if _TATWEEL in word:
            n_bound_affix += 1
            bound_idx.append(i)
        base = _base_form(word)
        per_pair_base.append(base)
        if len(base) == 1:
            n_single += 1
        elif len(base) == 2:
            n_two += 1
        if len(base) <= 2:
            short_forms[base] = short_forms.get(base, 0) + 1

    covered = {b for b in short_forms if b in alphabet}
    coverage = len(covered) / len(alphabet) if alphabet else 0.0
    is_alphabet_chart = coverage >= ALPHABET_COVERAGE_THRESHOLD
    trivial_forms = set(short_forms) if is_alphabet_chart else set()
    bound_set = set(bound_idx)

    trivial: List[GoldPair] = []
    real: List[GoldPair] = []
    for i, ((word, gold), base) in enumerate(zip(pairs, per_pair_base)):
        if i in bound_set or (base is not None and base in trivial_forms):
            trivial.append((word, gold))
        else:
            real.append((word, gold))

    stats = {
        "n_total": len(pairs),
        "n_single_char": n_single,
        "n_two_char": n_two,
        "n_short_le2": sum(short_forms.values()),
        "n_bound_affix": n_bound_affix,
        "alphabet_size": len(alphabet),
        "alphabet_coverage": round(coverage, 4),
        "is_alphabet_chart": is_alphabet_chart,
        "n_trivial": len(trivial),
        "trivial_share": round(len(trivial) / len(pairs), 4) if pairs else 0.0,
    }
    return trivial, real, stats


#: Marker distinguishing a "too large to load in a practical sweep" skip
#: from a genuine no-cached-gold skip, so a caller can tell them apart.
TOO_LARGE = "too-large"


def score_row(lang: str, dataset: str, board_n: int, board_per: float,
              max_n: Optional[int] = None) -> Optional[dict]:
    """Score one board row's trivial/real split, or return ``None`` if it
    cannot be measured (see :data:`TOO_LARGE` / the network guard below).

    ``max_n`` skips the loader entirely for a row whose board-reported
    word count exceeds it, WITHOUT even reading the gold from disk. This
    is a deliberate, bounded simplification, not a sampling shortcut: a
    spec's declared alphabet has on the order of dozens of graphemes, so
    even in the worst case where every single alphabet entry appears
    verbatim as a headword, a gold set of ``max_n`` words has a trivial
    share bounded above by roughly ``alphabet_size / max_n`` — for
    ``max_n=5000`` and a generous 80-grapheme alphabet that is 1.6%, far
    under any threshold this page reports against. Skipping these rows
    trades a small, provably-irrelevant slice of the board for making a
    full sweep tractable; see docs/gold_composition.md for the count of
    rows this excludes on a given run.
    """
    if max_n is not None and board_n > max_n:
        return None
    loader = DATASETS[dataset][0]
    with mock.patch("urllib.request.urlretrieve",
                    side_effect=RuntimeError(_NETWORK_BLOCKED)):
        try:
            pairs = loader(lang, sys.maxsize)
        except RuntimeError as exc:
            if _NETWORK_BLOCKED in str(exc):
                return None
            raise
    if not pairs:
        return None

    trivial, real, stats = classify_gold(lang, pairs)
    if stats["n_trivial"] == 0:
        # Nothing flagged trivial: the split would just reproduce the
        # board number twice, which is not a finding.
        return {**stats, "lang": lang, "dataset": dataset,
                "board_n": board_n, "board_per": board_per,
                "trivial_per": None, "real_per": None, "gap": None}

    _, _, _, trivial_per, _ = evaluate_words(
        trivial, lang, strip_stress=True, broad=True)
    _, real_covered, _, real_per, _ = evaluate_words(
        real, lang, strip_stress=True, broad=True) if real else \
        (0, 0, [], None, None)

    gap = None if real_per is None else round(real_per - trivial_per, 4)
    return {
        **stats,
        "lang": lang,
        "dataset": dataset,
        "board_n": board_n,
        "board_per": board_per,
        "trivial_per": round(trivial_per, 4),
        "real_per": None if real_per is None else round(real_per, 4),
        "real_n": real_covered,
        "gap": gap,
    }


def build_report(start: int = 0, end: Optional[int] = None,
                 max_n: Optional[int] = None
                 ) -> Tuple[List[dict], List[Tuple[str, str]]]:
    """Score board rows ``board[start:end]``. Sliceable so a full 639-row
    sweep (which re-scores every trivial/real split with the harness's own
    G2P engine, and can take several minutes) can be run in batches."""
    with open(SCOREBOARD_JSON, encoding="utf-8") as fh:
        board = json.load(fh)
    board = board[start:end]

    rows: List[dict] = []
    skipped: List[Tuple[str, str]] = []
    for entry in board:
        lang, dataset = entry["lang"], entry["dataset"]
        try:
            result = score_row(lang, dataset, entry["n"], entry["per"],
                               max_n=max_n)
        except Exception as exc:  # loader/spec error unrelated to network
            skipped.append((lang, dataset))
            print(f"skip {dataset}/{lang}: {exc}", file=sys.stderr)
            continue
        if result is None:
            skipped.append((lang, dataset))
            continue
        rows.append(result)
    return rows, skipped


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, default=0)
    ap.add_argument("--end", type=int, default=None)
    ap.add_argument("--max-n", type=int, default=None,
                    help="Skip rows whose board 'n' exceeds this without "
                         "loading their gold (see score_row's docstring "
                         "for why that is a bounded, justified skip).")
    args = ap.parse_args()
    rows, skipped = build_report(args.start, args.end, max_n=args.max_n)
    flattering = sorted(
        (r for r in rows if r["gap"] is not None and r["trivial_share"] > 0),
        key=lambda r: r["gap"], reverse=True)
    print(json.dumps({
        "rows_scored": len(rows),
        "rows_skipped_no_cache": len(skipped),
        "most_flattered": flattering[:10],
        "rows": rows,
        "skipped": skipped,
    }, ensure_ascii=False, indent=1))
