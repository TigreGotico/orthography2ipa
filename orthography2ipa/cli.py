"""Command-line interface for orthography2ipa.

Subcommands
-----------
- ``info``       — show a language specification
- ``transcribe`` — tokenise and transcribe a word/phrase to IPA
- ``distance``   — compute phonological distance between two languages
- ``list``       — list available language codes or families
- ``validate``   — validate language spec JSON files against the schema
"""
from __future__ import annotations

import argparse
import json
import sys
from typing import List, Optional


def _language_count() -> int:
    """Number of catalogued languages (clade-only helper nodes excluded),
    computed from the registry so the help text never goes stale."""
    from orthography2ipa.registry import available_codes

    return len(available_codes())


def _build_parser() -> argparse.ArgumentParser:
    """Build the top-level argument parser with subcommands."""
    parser = argparse.ArgumentParser(
        prog="orthography2ipa",
        description=(
            f"Grapheme-to-IPA mappings and phonological tools for "
            f"{_language_count()} languages."
        ),
    )
    parser.add_argument(
        "--version", action="store_true", help="Print version and exit."
    )
    sub = parser.add_subparsers(dest="command")

    # --- list ---
    p_list = sub.add_parser("list", help="List available language codes or families.")
    p_list.add_argument(
        "--families", action="store_true",
        help="Group codes by language family.",
    )
    p_list.add_argument(
        "--family", type=str, default=None,
        help="Filter codes to a single family (e.g. Romance).",
    )
    p_list.add_argument(
        "--json", action="store_true", dest="as_json",
        help="Output as JSON.",
    )

    # --- info ---
    p_info = sub.add_parser("info", help="Show details for a language code.")
    p_info.add_argument("code", help="BCP-47 or ISO-639-3 language code.")
    p_info.add_argument(
        "--json", action="store_true", dest="as_json",
        help="Output full spec as JSON.",
    )
    p_info.add_argument(
        "--graphemes", action="store_true",
        help="Print only the grapheme→IPA map.",
    )
    p_info.add_argument(
        "--allophones", action="store_true",
        help="Print only the allophone map.",
    )

    # --- transcribe ---
    p_trans = sub.add_parser(
        "transcribe", help="Transcribe text to IPA.",
    )
    p_trans.add_argument("code", help="Language code.")
    p_trans.add_argument("text", help="Word or phrase to transcribe.")
    p_trans.add_argument(
        "--search", choices=("greedy", "beam"), default="greedy",
        help="Candidate search: best path per word (greedy, default) "
             "or keep a beam of alternatives (beam).",
    )
    p_trans.add_argument(
        "--beam-width", "--beam", type=int, default=8, dest="beam_width",
        help="Beam width for --search beam (default: 8).",
    )
    p_trans.add_argument(
        "--dialect-profile", default=None,
        help="Dialect transform profile applied to the final IPA.",
    )
    p_trans.add_argument(
        "--json", action="store_true", dest="as_json",
        help="Output as JSON.",
    )

    # --- distance ---
    p_dist = sub.add_parser(
        "distance", help="Compute phonological distance between two languages.",
    )
    p_dist.add_argument("code1", help="First language code.")
    p_dist.add_argument("code2", help="Second language code.")
    p_dist.add_argument(
        "--json", action="store_true", dest="as_json",
        help="Output as JSON.",
    )

    # --- validate ---
    p_val = sub.add_parser(
        "validate",
        help="Validate language spec JSON files against the schema.",
    )
    p_val.add_argument(
        "code", nargs="?", default=None,
        help="Validate a single language code (default: all specs).",
    )
    p_val.add_argument(
        "--json", action="store_true", dest="as_json",
        help="Output the validation report as JSON.",
    )

    return parser


# ---- subcommand handlers ------------------------------------------------- #


def _cmd_list(args: argparse.Namespace) -> None:
    """Handle the ``list`` subcommand."""
    from orthography2ipa import available_codes, available_families

    if args.families or args.family:
        families = available_families()
        if args.family:
            # ``family`` is a Glottolog classification path — "Indo-European >
            # Romance". Match the whole path or any single step of it, so both
            # the branch ("Romance") and the stock it sits in ("Indo-European",
            # which selects every family beneath it) are usable filters.
            key = args.family.strip().lower()
            matched = {
                k: v for k, v in families.items()
                if k.lower() == key
                or key in [step.strip().lower() for step in k.split(">")]
            }
            if not matched:
                print(f"Unknown family: {args.family}", file=sys.stderr)
                sys.exit(1)
            families = matched
        if args.as_json:
            print(json.dumps(families, ensure_ascii=False, indent=2))
        else:
            for fam, codes in sorted(families.items()):
                print(f"{fam}: {', '.join(sorted(codes))}")
    else:
        codes = sorted(available_codes())
        if args.as_json:
            print(json.dumps(codes, ensure_ascii=False, indent=2))
        else:
            for c in codes:
                print(c)


def _cmd_info(args: argparse.Namespace) -> None:
    """Handle the ``info`` subcommand."""
    from orthography2ipa import get

    spec = get(args.code)
    if spec is None:
        print(f"Unknown language code: {args.code}", file=sys.stderr)
        sys.exit(1)

    if args.as_json:
        from dataclasses import asdict
        print(json.dumps(asdict(spec), ensure_ascii=False, indent=2, default=str))
        return

    if args.graphemes:
        for g, ipas in sorted(spec.graphemes.items()):
            print(f"  {g!r:>8} → {', '.join(ipas)}")
        return

    if args.allophones:
        for ph, allos in sorted(spec.allophones.items()):
            print(f"  {ph:>6} → {', '.join(allos)}")
        return

    # default: summary
    print(f"Code:    {spec.code}")
    print(f"Name:    {spec.name}")
    print(f"Family:  {spec.family}")
    print(f"Script:  {spec.script}")
    print(f"Quality: {spec.quality.value if hasattr(spec.quality, 'value') else spec.quality}")
    print(f"Graphemes:  {len(spec.graphemes)}")
    print(f"Allophones: {len(spec.allophones)}")
    if spec.ancestors:
        ancs = ", ".join(
            f"{a.code} ({a.role.value if hasattr(a.role, 'value') else a.role})"
            for a in spec.ancestors
        )
        print(f"Ancestors:  {ancs}")
    if spec.tone_inventory:
        print(f"Tones:      {len(spec.tone_inventory)}")
    if spec.sources:
        print(f"Sources:    {len(spec.sources)}")


def _cmd_transcribe(args: argparse.Namespace) -> None:
    """Handle the ``transcribe`` subcommand."""
    from orthography2ipa.g2p import G2P

    try:
        engine = G2P(args.code, dialect_profile=args.dialect_profile)
    except KeyError as exc:
        print(f"Unknown language code: {exc}", file=sys.stderr)
        sys.exit(1)

    result = engine.transcribe_detailed(
        args.text, search=args.search, beam_width=args.beam_width)

    if args.as_json:
        payload = {
            "lang": result.lang,
            "ipa": result.ipa,
            "words": [
                {
                    "word": w.word,
                    "ipa": w.ipa,
                    "candidates": [
                        {"transcription": p.ipa, "score": round(p.score, 4)}
                        for p in w.candidates
                    ],
                }
                for w in result.words
            ],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"/{result.ipa}/")
        if args.search == "beam":
            for w in result.words:
                print(f"{w.word}:")
                for p in w.candidates:
                    print(f"  /{p.ipa}/  (score: {round(p.score, 4)})")


def _cmd_distance(args: argparse.Namespace) -> None:
    """Handle the ``distance`` subcommand."""
    from orthography2ipa import get
    from orthography2ipa.distance import phonological_distance

    s1 = get(args.code1)
    s2 = get(args.code2)
    if s1 is None:
        print(f"Unknown language code: {args.code1}", file=sys.stderr)
        sys.exit(1)
    if s2 is None:
        print(f"Unknown language code: {args.code2}", file=sys.stderr)
        sys.exit(1)

    dist = phonological_distance(s1, s2)

    if args.as_json:
        from dataclasses import asdict
        print(json.dumps(asdict(dist), ensure_ascii=False, indent=2, default=str))
    else:
        print(f"{s1.name} ({s1.code}) ↔ {s2.name} ({s2.code})")
        print(f"  combined:   {dist.combined:.4f}")
        print(f"  inventory:  {dist.inventory.feature_mean:.4f}")
        print(f"  allophone:  {dist.allophone_sim:.4f}")
        print(f"  grapheme:   {dist.grapheme.mean_ipa_distance:.4f}"
              f"   (orthography — not part of combined)")


def _cmd_validate(args: argparse.Namespace) -> None:
    """Handle the ``validate`` subcommand.

    Validates every spec (or a single ``code``) against the pydantic schema.
    Exits non-zero if any spec fails.
    """
    from orthography2ipa.schema import format_failure, validate_all

    ok, failures = validate_all(args.code)

    if args.as_json:
        print(json.dumps({
            "ok": ok,
            "failures": {code: format_failure(code, exc) for code, exc in failures},
            "passed": len(ok),
            "failed": len(failures),
        }, ensure_ascii=False, indent=2))
    else:
        for code, exc in failures:
            print(format_failure(code, exc), file=sys.stderr)
        print(f"{len(ok)} valid, {len(failures)} invalid "
              f"({len(ok) + len(failures)} specs checked)")

    if failures:
        sys.exit(1)


def main(argv: Optional[List[str]] = None) -> None:
    """CLI entry point."""
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.version:
        from orthography2ipa.version import VERSION_STR
        print(f"orthography2ipa {VERSION_STR}")
        return

    handlers = {
        "list": _cmd_list,
        "info": _cmd_info,
        "transcribe": _cmd_transcribe,
        "distance": _cmd_distance,
        "validate": _cmd_validate,
    }

    if args.command in handlers:
        handlers[args.command](args)
    else:
        parser.print_help()
        sys.exit(0)


if __name__ == "__main__":
    main()
