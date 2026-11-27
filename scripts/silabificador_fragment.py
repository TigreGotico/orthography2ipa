"""Write a plugin fragment with the syllable tables of silabificador.

The tool reads the data of an installed ``silabificador`` and writes the
``syllable`` part of an IR fragment (docs/ir/o2i-ir-v1.md, 3.5 and 3.7.6).
The S5 written splitter applies the tables. The stress tables of
silabificador are not in the fragment.

    python scripts/silabificador_fragment.py OUT.json
"""
import argparse
import json

from silabificador import morphology, phonotactics


def fragment() -> dict:
    """The fragment of the installed silabificador data."""
    stems = {stem: list(offsets) for stem, offsets in morphology.LISTED_STEMS.items()}
    # _UO_IDADE is (?<=[^gq]u)idades?$. The IR pattern subset has a lookbehind
    # of one codepoint only, so the match starts two chars early.
    assert morphology._UO_IDADE.pattern == r"(?<=[^gq]u)idades?$"
    return {
        "ir_version": 1,
        "syllable": {
            "heterosyllabic_pairs": ["rr", "ss", "sc", "sç", "xc"],
            "hiatus": {
                "glides": sorted(phonotactics.GLIDE_CAPABLE),
                "before": sorted(phonotactics.HIATUS_BEFORE),
                "codas": sorted(phonotactics.HIATUS_CODAS),
                "diphthong_words": sorted(phonotactics.AO_DIPHTHONG_WORDS),
            },
            "stem_cuts": dict(sorted(stems.items())),
            "prefix_boundaries": [
                {"prefix": prefix, "onset": sorted(morphology._LIQUIDS), "stems": list(found)}
                for prefix, found in sorted(morphology.LATINATE_PREFIX_STEMS.items())],
            "seams": {
                "suffixes": [{"pattern": "[^gq]uidades?$", "cut": 2}],
                "stems": list(morphology.VOWEL_FINAL_STEMS),
                "next": ["i"],
            },
            "onsets": {
                "complex": sorted(phonotactics.COMPLEX_ONSETS),
                "max_onset": 2,
                "digraphs": sorted(phonotactics.CONSONANT_DIGRAPHS | {"gu", "gü", "qu", "qü"}),
            },
            "foreign": {
                "units": sorted(phonotactics.FOREIGN_DIGRAPHS | phonotactics.FOREIGN_TETRAGRAPHS),
                "pattern": phonotactics.FOREIGN_MARKS.pattern,
                "nuclei": ["ee", "oo", "ou"],
                "final_nuclei": {"eau": ["", "s", "x"], "eu": ["r", "rs"]},
            },
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("out")
    args = parser.parse_args()
    with open(args.out, "w", encoding="utf-8") as handle:
        json.dump(fragment(), handle, ensure_ascii=False, indent=1, sort_keys=True)
        handle.write("\n")


if __name__ == "__main__":
    main()
