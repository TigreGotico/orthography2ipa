"""Command-line interface for orthography2ipa.

Subcommands
-----------
- ``info``       — show a language specification
- ``transcribe`` — tokenise and transcribe a word/phrase to IPA
- ``distance``   — compute phonological distance between two languages
- ``list``       — list available language codes or families
"""
from __future__ import annotations

import argparse
import json
import sys
from typing import List, Optional


def _build_parser() -> argparse.ArgumentParser:
    """Build the top-level argument parser with subcommands."""
    parser = argparse.ArgumentParser(
        prog="orthography2ipa",
        description="Grapheme-to-IPA mappings and phonological tools for 310+ languages.",
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
        "transcribe", help="Transcribe text to IPA candidates.",
    )
    p_trans.add_argument("code", help="Language code.")
    p_trans.add_argument("text", help="Word or phrase to transcribe.")
    p_trans.add_argument(
        "--beam", type=int, default=4,
        help="Beam width for IPA path expansion (default: 4).",
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

    return parser


# ---- subcommand handlers ------------------------------------------------- #


def _cmd_list(args: argparse.Namespace) -> None:
    """Handle the ``list`` subcommand."""
    from orthography2ipa import available_codes, available_families

    if args.families or args.family:
        families = available_families()
        if args.family:
            key = args.family
            # case-insensitive match
            for k in families:
                if k.lower() == key.lower():
                    families = {k: families[k]}
                    break
            else:
                print(f"Unknown family: {key}", file=sys.stderr)
                sys.exit(1)
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
    from orthography2ipa import get
    from orthography2ipa.phonetok import PhonetokTokenizer

    spec = get(args.code)
    if spec is None:
        print(f"Unknown language code: {args.code}", file=sys.stderr)
        sys.exit(1)

    tok = PhonetokTokenizer(spec)
    words = args.text.strip().split()

    results: List[dict] = []
    for word in words:
        paths = tok.ipa_beam(word, beam_width=args.beam)
        results.append({
            "word": word,
            "ipa": [{"transcription": p.ipa, "score": round(p.score, 4)} for p in paths],
        })

    if args.as_json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    else:
        for r in results:
            print(f"{r['word']}:")
            for p in r["ipa"]:
                print(f"  /{p['transcription']}/  (score: {p['score']})")


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
        print(f"  grapheme:   {dist.grapheme.mean_ipa_distance:.4f}")
        print(f"  allophone:  {dist.allophone_sim:.4f}")


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
    }

    if args.command in handlers:
        handlers[args.command](args)
    else:
        parser.print_help()
        sys.exit(0)


if __name__ == "__main__":
    main()
