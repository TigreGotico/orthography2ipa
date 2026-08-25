"""Mechanical diagnostic over every language spec.

The waves that moved a board row furthest did not refine a rule. They found a
spec that was never written for its language at all: a phoneme table borrowed
from an unrelated family, or a grapheme table so small that most of the gold
orthography was deleted silently before any rule could apply. Both conditions
are mechanical, so they can be found without reading a spec.

Two signals are computed here. The first is coverage: the characters that occur
on the orthographic side of a spec's own gold, minus the characters its resolved
grapheme table can consume. Every one of those is a character the engine drops.
The second is inheritance across a language-family boundary: a ``parent``,
``graphemes_base`` or ``allophones_base`` that points at a language from a
different family is a borrowed phonology until proven otherwise.

Supporting fields make a flagged row readable: whether a stress block is
reachable, whether the declared phoneme inventory agrees with what the spec
actually emits, and the board rows the spec is scored on.

Usage::

    PYTHONPATH=$PWD python3 scripts/spec_diagnostics.py            # report to docs/
    PYTHONPATH=$PWD python3 scripts/spec_diagnostics.py --langs gn,as --stdout
    PYTHONPATH=$PWD python3 scripts/spec_diagnostics.py --json out.json

Gold is read from the benchmark cache only. Networking is disabled, so a spec
whose dataset is not cached reports no coverage figure instead of downloading
several gigabytes.
"""
from __future__ import annotations

import argparse
import functools
import json
import os
import socket
import sys
import unicodedata
from typing import Dict, List, Optional, Sequence, Set, Tuple

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import orthography2ipa as o2i  # noqa: E402
from orthography2ipa.inventory import emission_inventory  # noqa: E402
from orthography2ipa.json_loader import _DATA_DIR as DATA_DIR  # noqa: E402

BASE_FIELDS = (
    "parent",
    "graphemes_base",
    "allophones_base",
    "positional_graphemes_base",
    "word_exceptions_base",
    "grammatical_endings_base",
)

#: Characters that carry no phonological content and are never expected in a
#: grapheme table. Word separators, digits and punctuation are tokenizer
#: business, so counting them as unmapped would drown the real signal.
#:
#: The apostrophe family (``'``, ``’``, ``‘``) is deliberately NOT in this set.
#: Several orthographies use it phonemically — Tarifit marks pharyngealisation
#: with a trailing ``’`` (Kossmann), and it is the standard ejective/glottal-stop
#: letter elsewhere — so treating it as punctuation made that entire phonemic
#: dimension invisible to this signal. The cost is the mirror case: a gold that
#: genuinely uses the apostrophe only as quotation punctuation will now show it
#: as an ordinary "unmapped" character if the grapheme table has no entry for
#: it. This script cannot tell the two uses apart, so a flagged apostrophe
#: should be read, not trusted blindly either way.
IGNORED_CATEGORIES = ("Zs", "Nd", "Cc", "Cf")
IGNORED_CHARS = set(" \t\n-\"“”.,;:!?()[]{}/\\|_=+*&%$#@~`^<>0123456789")


def _offline() -> None:
    """Fail any outbound connection. The benchmark loaders fall back to their
    cache when the file is already there and raise otherwise, which is exactly
    the behaviour wanted: never re-download, never write the shared cache."""

    class _NoNet(socket.socket):
        def connect(self, *a, **k):  # noqa: ANN002, ANN003
            raise OSError("spec_diagnostics runs offline; cache miss")

    socket.socket = _NoNet  # type: ignore[misc]


# --------------------------------------------------------------------------
# spec facts
# --------------------------------------------------------------------------

def _raw_specs() -> Dict[str, dict]:
    raw: Dict[str, dict] = {}
    for name in sorted(os.listdir(DATA_DIR)):
        if not name.endswith(".json"):
            continue
        path = os.path.join(DATA_DIR, name)
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
        raw[data.get("code") or name[:-5]] = data
    return raw


@functools.lru_cache(maxsize=None)
def _family_cached(code: str) -> Optional[str]:
    try:
        return o2i.get(code).family or None
    except Exception:
        return None


def _family(code: str, raw: Dict[str, dict]) -> Optional[str]:
    """Family of *code*, resolved through the loader so an inherited family is
    reported rather than a missing key on the child."""
    return _family_cached(code) or (raw.get(code) or {}).get("family")


@functools.lru_cache(maxsize=None)
def _family_path(code: str) -> Tuple[str, ...]:
    try:
        return tuple(o2i.get(code).family_path)
    except Exception:
        return ()


def _root_family(code: str, raw: Dict[str, dict]) -> Optional[str]:
    """Top-level family, which is the level a borrowed phonology shows up at.

    Comparing full paths would flag every dialect whose parent sits on a
    neighbouring branch of the same family, which is ordinary descent. A
    grapheme or allophone table taken across the root boundary is not.
    """
    path = _family_path(code)
    if path:
        return path[0]
    family = _family(code, raw)
    return family.split(" > ")[0] if family else None


def _chain(code: str, raw: Dict[str, dict]) -> List[Dict[str, Optional[str]]]:
    """Every inheritance edge the spec declares, with the family on each end."""
    spec = raw[code]
    own = _root_family(code, raw)
    links = []
    for field in BASE_FIELDS:
        target = spec.get(field)
        if not target:
            continue
        target_family = _family(target, raw)
        target_root = _root_family(target, raw)
        links.append({
            "field": field,
            "target": target,
            "target_family": target_family,
            "cross_family": bool(own and target_root and own != target_root),
        })
    return links


def _scan_gold(spec, pairs: Sequence[Tuple[str, str]], sample: int) \
        -> Tuple[Set[str], List[str], int, int]:
    """Run the shipped tokenizer over the gold orthography.

    The tokenizer is the authority on what the engine can consume, so the
    unmapped set is read from its own verdicts rather than guessed from the
    grapheme keys. That distinction matters: a character that only ever
    occurs inside a multigraph is still consumed, while a character with no
    reading at any length is deleted before a rule can see it.

    ``UNKNOWN`` is not the whole story, though: the tokenizer also silently
    swallows apostrophe-class characters (``'``, ``’``, ``‘``, quote marks) as
    ``PUNCTUATION`` unless a spec's grapheme table explicitly claims them —
    which is correct for languages that use them only as delimiters, and
    wrong for the ones that use them phonemically (Tarifit's pharyngealised
    ``’``, ejective and glottal-stop apostrophes elsewhere). Those tokens are
    scanned here too, so a phonemic apostrophe with no grapheme entry still
    counts as unmapped instead of vanishing before either signal sees it.

    Returns the gold character set, the unmapped characters, the number of gold
    words containing at least one unmapped character, and the words scanned.
    """
    from orthography2ipa.phonetok import PhonetokTokenizer, TokenKind

    tokenizer = PhonetokTokenizer(spec)
    gold: Set[str] = set()
    unmapped: Set[str] = set()
    hit_words = 0
    scanned = 0
    for word, _ipa in pairs[:sample]:
        word = unicodedata.normalize("NFC", word)
        if not word.strip():
            continue
        scanned += 1
        for char in word.lower():
            if char in IGNORED_CHARS or unicodedata.category(char) in IGNORED_CATEGORIES:
                continue
            gold.add(char)
        try:
            tokens = tokenizer.tokenize(word)
        except Exception:
            continue
        bad = {
            char
            for token in tokens
            if token.kind in (TokenKind.UNKNOWN, TokenKind.PUNCTUATION)
            for char in (token.grapheme or "").lower()
            if char not in IGNORED_CHARS
            and unicodedata.category(char) not in IGNORED_CATEGORIES
        }
        if bad:
            hit_words += 1
            unmapped |= bad
    return gold, sorted(unmapped), hit_words, scanned


def _signature(table: Optional[dict]) -> frozenset:
    """First reading of every key, which is what an author copies wholesale."""
    if not table:
        return frozenset()
    out = []
    for key, readings in table.items():
        if isinstance(readings, dict):
            readings = readings.get("ipa") or readings.get("candidates") or []
        if isinstance(readings, str):
            readings = [readings]
        out.append((key.lower(), readings[0] if readings else ""))
    return frozenset(out)


def _twin(code: str, raw: Dict[str, dict], field: str,
          signatures: Dict[str, frozenset]) -> Optional[Tuple[str, float]]:
    """The spec whose own *field* table most resembles this one's.

    A table copied from another language keeps almost every key/value pair of
    its source. When the closest match is a language the spec never declares as
    a base, the table was asserted rather than derived, which is the condition
    behind a spec that reads as plausible and scores as noise.
    """
    mine = signatures.get(code)
    if not mine or len(mine) < 8:
        return None
    declared = {raw[code].get(f) for f in BASE_FIELDS if raw[code].get(f)}
    declared |= {a.get("code") for a in raw[code].get("ancestors") or [] if a.get("code")}
    # Dialect siblings share a table by design (``pt-BR-x-sp`` against
    # ``pt-BR-x-rj``), so a match under the same primary subtag says nothing.
    stem = code.split("-")[0]
    script = raw[code].get("script")
    best: Optional[Tuple[str, float]] = None
    for other, sig in signatures.items():
        if other == code or other in declared or not sig or len(sig) < 8:
            continue
        if raw.get(other, {}).get("script") != script:
            continue
        if other.split("-")[0] == stem:
            continue
        ratio = len(mine & sig) / max(len(mine), len(sig))
        if best is None or ratio > best[1]:
            best = (other, round(ratio, 3))
    return best


def _phoneme_agreement(spec) -> Tuple[List[str], List[str]]:
    """``(declared but never emitted, emitted but never declared)``.

    A spec whose declared inventory is a borrowed phoneme list contradicts its
    own grapheme table on both sides at once.
    """
    declared = {p for p in (spec.phonemes or ())}
    if not declared:
        return [], []
    try:
        emitted = set(emission_inventory(spec))
    except Exception:
        return [], []
    return sorted(declared - emitted), sorted(emitted - declared)


# --------------------------------------------------------------------------
# gold
# --------------------------------------------------------------------------

def _board_rows() -> Dict[str, List[dict]]:
    path = os.path.join(ROOT, "benchmarks", "results.json")
    with open(path, encoding="utf-8") as handle:
        rows = json.load(handle)
    by_lang: Dict[str, List[dict]] = {}
    for row in rows:
        by_lang.setdefault(row["lang"], []).append(row)
    return by_lang


def _load_gold(dataset: str, lang: str) -> Optional[List[Tuple[str, str]]]:
    import benchmark

    entry = benchmark.DATASETS.get(dataset)
    if entry is None:
        return None
    try:
        return list(entry[0](lang, 10 ** 9))
    except Exception:
        return None


# --------------------------------------------------------------------------
# report
# --------------------------------------------------------------------------

def diagnose(codes: Optional[Sequence[str]] = None, sample: int = 5000) -> List[dict]:
    raw = _raw_specs()
    board = _board_rows()
    grapheme_sigs = {c: _signature(d.get("graphemes")) for c, d in raw.items()}
    allophone_sigs = {c: _signature(d.get("allophones")) for c, d in raw.items()}
    wanted = list(codes) if codes else sorted(raw)
    out = []
    for code in wanted:
        if code not in raw:
            continue
        try:
            spec = o2i.get(code)
        except Exception as exc:
            out.append({"code": code, "error": str(exc)})
            continue
        rows = board.get(code, [])
        gold: Set[str] = set()
        missing_set: Set[str] = set()
        datasets = []
        per_dataset: List[dict] = []
        hit_words = scanned = 0
        for row in rows:
            pairs = _load_gold(row["dataset"], code)
            if pairs is None:
                continue
            datasets.append(row["dataset"])
            chars, missing, hits, count = _scan_gold(spec, pairs, sample)
            gold |= chars
            missing_set |= set(missing)
            hit_words += hits
            scanned += count
            per_dataset.append({
                "dataset": row["dataset"],
                "gold_chars": len(chars),
                "unmapped_count": len(missing),
                "unmapped": missing,
                "affected_words": hits,
                "scanned_words": count,
                "affected_share": round(hits / count, 4) if count else None,
            })
        missing = sorted(missing_set)
        declared_unused, undeclared = _phoneme_agreement(spec)
        twin = _twin(code, raw, "graphemes", grapheme_sigs) if rows else None
        allophone_twin = _twin(code, raw, "allophones", allophone_sigs) if rows else None
        links = _chain(code, raw)
        out.append({
            "code": code,
            "name": raw[code].get("name"),
            "family": _family(code, raw),
            "quality": raw[code].get("quality"),
            "own_graphemes": len(raw[code].get("graphemes") or {}),
            "resolved_graphemes": len(spec.graphemes or {}),
            "chain": links,
            "cross_family": [l for l in links if l["cross_family"]],
            "stress": bool(raw[code].get("stress")),
            "stress_resolved": spec.stress is not None,
            "per_dataset": per_dataset,
            # These four are a UNION across every gold dataset the spec is
            # scored on. A language scored on several corpora can show a
            # combined count that exceeds any single dataset's own count, and
            # the word share becomes a blend across unrelated corpora (loanword
            # letters from one dataset merged with diacritic gaps from
            # another). Kept for the full table below; the two ranked sections
            # use `per_dataset` instead, because ranking off the union has
            # already misprioritised rows in the past.
            "combined_gold_chars": len(gold),
            "combined_unmapped_count": len(missing),
            "combined_unmapped": missing,
            "combined_affected_words": hit_words,
            "combined_scanned_words": scanned,
            "combined_affected_share": round(hit_words / scanned, 4) if scanned else None,
            "grapheme_twin": twin,
            "allophone_twin": allophone_twin,
            "twin_cross_family": bool(
                twin and _root_family(twin[0], raw)
                and _root_family(code, raw) != _root_family(twin[0], raw)),
            "declared_unused": declared_unused,
            "undeclared_emitted": undeclared,
            "datasets": datasets,
            "board_rows": len(rows),
            "n": sum(r.get("n") or 0 for r in rows),
            "per": min([r["per"] for r in rows], default=None),
            "worst_per": max([r["per"] for r in rows], default=None),
        })
    return out


def _fmt_chain(entry: dict) -> str:
    if not entry["chain"]:
        return "(standalone)"
    parts = []
    for link in entry["chain"]:
        mark = " CROSS-FAMILY" if link["cross_family"] else ""
        parts.append("{}={} [{}]{}".format(
            link["field"], link["target"], link["target_family"] or "?", mark))
    return "; ".join(parts)


def render(entries: List[dict], top: int = 20) -> str:
    scored = [e for e in entries if "error" not in e]
    lines = []
    lines.append("# Spec diagnostics")
    lines.append("")
    lines.append(
        "Regenerate with `PYTHONPATH=$PWD python3 scripts/spec_diagnostics.py`. "
        "Three mechanical signals separate a spec that is wrong from a spec "
        "that is merely imprecise: gold characters its grapheme table cannot "
        "consume, which the engine deletes before a rule can see them; "
        "inheritance that crosses a language-family boundary; and a table that "
        "matches another language almost pair for pair. None is proof on its "
        "own. Each points at a spec worth reading before any rule in it is "
        "refined."
    )
    lines.append("")

    with_gold = [e for e in scored if e["combined_gold_chars"]]
    flagged = [e for e in with_gold if e["combined_unmapped_count"]]
    lines.append(
        "Of {} specs, {} have a cached gold to measure against, and {} of those "
        "leave at least one gold character unmapped.".format(
            len(scored), len(with_gold), len(flagged))
    )
    lines.append("")
    lines.append(
        "A language scored on several gold datasets is reported here **per "
        "dataset**, not unioned. Unioning inflates the count (a character can "
        "be unmapped in one corpus only) and blends unrelated problems — one "
        "dataset's loanword letters with another's diacritic gaps — into a "
        "single misleading figure. The `combined_*` fields in the JSON output "
        "keep the union for reference, but every ranking below and every row "
        "you might prioritise off of is per dataset."
    )
    lines.append("")

    # Flatten to (spec, dataset) rows for ranking; the code-level `entry` is
    # still attached so chain/stress/twin context can be printed alongside.
    per_dataset_rows: List[Tuple[dict, dict]] = [
        (entry, ds) for entry in with_gold for ds in entry["per_dataset"]
        if ds["unmapped_count"]
    ]

    lines.append("## Ranked by unmapped gold characters (per dataset)")
    lines.append("")
    for entry, ds in sorted(per_dataset_rows, key=lambda p: -p[1]["unmapped_count"])[:top]:
        lines.append("- **{}** ({}) / `{}` — {} of {} gold characters unmapped, hitting {:.1%} of {} scanned words; own table {} graphemes, resolved {}; worst per {}; n {}".format(
            entry["code"], entry["name"], ds["dataset"], ds["unmapped_count"], ds["gold_chars"],
            ds["affected_share"] or 0.0, ds["scanned_words"],
            entry["own_graphemes"], entry["resolved_graphemes"],
            entry["worst_per"], entry["n"]))
        lines.append("  - unmapped: `{}`".format(" ".join(ds["unmapped"][:60])))
        lines.append("  - chain: {}".format(_fmt_chain(entry)))
        if not entry["stress_resolved"]:
            lines.append("  - no stress block reachable")
    lines.append("")

    lines.append("## Ranked by share of gold words that lose a character (per dataset)")
    lines.append("")
    lines.append(
        "The character count above treats a rare loan letter and a missing "
        "nasal vowel series alike. This ordering weights each spec/dataset pair "
        "by how much of that dataset's own gold the deletion actually touches."
    )
    lines.append("")
    for entry, ds in sorted(per_dataset_rows, key=lambda p: -(p[1]["affected_share"] or 0))[:top]:
        lines.append("- **{}** ({}) / `{}` — {:.1%} of {} scanned words lose at least one character; unmapped `{}`; worst per {}".format(
            entry["code"], entry["name"], ds["dataset"], ds["affected_share"] or 0.0,
            ds["scanned_words"], " ".join(ds["unmapped"][:30]),
            entry["worst_per"]))
    lines.append("")

    lines.append("## Tables asserted from another language")
    lines.append("")
    lines.append(
        "A spec's closest table twin among the specs it does not declare as a "
        "base. A ratio near 1 means the table was taken from that language "
        "rather than written for this one; the notes then describe a language "
        "the data never encodes."
    )
    lines.append("")

    def _twin_score(entry: dict) -> float:
        return max((entry["grapheme_twin"] or ("", 0))[1],
                   (entry["allophone_twin"] or ("", 0))[1])

    twins = [e for e in scored if _twin_score(e) >= 0.8]
    for entry in sorted(twins, key=lambda e: -_twin_score(e))[:top]:
        lines.append("- **{}** ({}, {}) — graphemes {}, allophones {}; declares {}; worst per {}{}".format(
            entry["code"], entry["name"], entry["family"] or "?",
            "{} {}".format(*entry["grapheme_twin"]) if entry["grapheme_twin"] else "none",
            "{} {}".format(*entry["allophone_twin"]) if entry["allophone_twin"] else "none",
            _fmt_chain(entry), entry["worst_per"],
            " — twin is a different family" if entry["twin_cross_family"] else ""))
    lines.append("")

    lines.append("## Ranked by cross-family inheritance")
    lines.append("")
    cross = [e for e in scored if e["cross_family"]]
    cross.sort(key=lambda e: (-len(e["cross_family"]), -(e["worst_per"] or 0),
                              -e["combined_unmapped_count"]))
    for entry in cross[:top]:
        lines.append("- **{}** ({}, {}) — {}; per {}; {} unmapped gold chars (union across datasets)".format(
            entry["code"], entry["name"], entry["family"] or "?",
            _fmt_chain(entry), entry["worst_per"], entry["combined_unmapped_count"]))
    lines.append("")

    lines.append("## Declared inventory contradicting emitted output")
    lines.append("")
    contra = [e for e in scored
              if len(e["declared_unused"]) >= 5 and len(e["undeclared_emitted"]) >= 5]
    contra.sort(key=lambda e: -(len(e["declared_unused"]) + len(e["undeclared_emitted"])))
    for entry in contra[:top]:
        lines.append("- **{}** ({}) — declares {} phonemes it never emits, emits {} it never declares; chain: {}".format(
            entry["code"], entry["name"], len(entry["declared_unused"]),
            len(entry["undeclared_emitted"]), _fmt_chain(entry)))
    lines.append("")

    lines.append("## Full table")
    lines.append("")
    lines.append(
        "Every spec that is scored on the board, plus any spec flagged by a "
        "signal above. Specs with neither a gold nor a flag carry no evidence "
        "either way and are left to the JSON output. `gold chars` and "
        "`unmapped` here are the union across every gold dataset the spec is "
        "scored on — use the per-dataset sections above before prioritising a "
        "row off this table."
    )
    lines.append("")
    lines.append("code | family | own graphemes | gold chars (union) | unmapped (union) | words hit (union) | stress | cross-family | twin | rows | n | per")
    lines.append("--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---")
    listed = [e for e in scored
              if e["combined_gold_chars"] or e["cross_family"] or _twin_score(e) >= 0.8]
    for entry in sorted(listed, key=lambda e: (-e["combined_unmapped_count"], e["code"])):
        lines.append("{} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {}".format(
            entry["code"], entry["family"] or "", entry["own_graphemes"],
            entry["combined_gold_chars"], entry["combined_unmapped_count"],
            "{:.1%}".format(entry["combined_affected_share"]) if entry["combined_affected_share"] else "",
            "yes" if entry["stress_resolved"] else "no",
            len(entry["cross_family"]),
            "{} {}".format(*entry["grapheme_twin"]) if entry["grapheme_twin"] else "",
            entry["board_rows"], entry["n"],
            entry["worst_per"] if entry["worst_per"] is not None else ""))
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--langs", help="comma-separated codes; default every spec")
    parser.add_argument("--out", default=os.path.join(ROOT, "docs", "spec_diagnostics.md"))
    parser.add_argument("--json", help="also write the raw per-spec records here")
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--sample", type=int, default=5000,
                        help="gold words scanned per dataset")
    parser.add_argument("--stdout", action="store_true", help="print instead of writing")
    args = parser.parse_args()

    _offline()
    codes = [c.strip() for c in args.langs.split(",")] if args.langs else None
    entries = diagnose(codes, args.sample)
    text = render(entries, args.top)
    if args.stdout:
        print(text)
    else:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(text)
        print("wrote {}".format(args.out))
    if args.json:
        with open(args.json, "w", encoding="utf-8") as handle:
            json.dump(entries, handle, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
