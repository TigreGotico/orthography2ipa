"""Fill empty registry-stub specs with cited Latin-script orthographies from
the africa-g2p compilation (AfriSpeech).

For every o2i spec that is a `quality: "stub"` REGISTRY STUB with empty
`graphemes` (a PHOIBLE-derived `phonemes` inventory may be present and is
kept), and whose ISO 639-3 code has a matching rule file in
africa-g2p, import a `graphemes` map built from that file's grapheme -> IPA
table:

  - values are wrapped as single-candidate lists (o2i wants lists, africa-g2p
    stores single IPA strings)
  - multigraphs (prenasalized stops, palatalized/labialized series, affricates,
    diphthong nuclei -- the digraphs African Latin orthographies actually use)
    are kept: they describe real orthographic units, not enumerated n-grams
  - a derivable-key audit drops any 2-letter key whose IPA is the literal
    concatenation of its two single-letter neighbours' IPA *and* does not match
    a recognised multigraph class (prenasalized / affricate / palatalized /
    labialized / geminate / diphthong nucleus); such a key is noise, not a
    orthographic unit
  - non-Latin-script files (graphemes keyed by Arabic/Ethiopic/Vai/N'Ko/Coptic
    characters) are skipped -- never force an abjad/abugida through a Latin
    importer

africa-g2p is a compilation tool; it is never the cited linguistic authority.
The actual citation is the source africa-g2p names for that file: an Omniglot
chart (c) Simon Ager, or Hartell 1993 "Alphabets of Africa" (UNESCO/SIL). A
provenance note records that the mapping was extracted via africa-g2p.

Existing `phonemes` (PHOIBLE-derived) are left in place; orthography and
phonology can legitimately diverge (spelling encodes a written standard,
PHOIBLE encodes a spoken inventory) -- graphemes may map to IPA outside the
existing phoneme inventory.

Where an ISO code has two africa-g2p regional variants (dop, hau, ngb, sag,
sef, snk), one is chosen deterministically (see REGIONAL_VARIANT_PICK) and the
other is left unused -- both are real charts, but a spec holds one orthography.

Input (read-only, not bundled): the africa-g2p checkout's language rule files
  ~/AgentWorkspaces/ml/africa-g2p/src/africa_g2p/languages/{iso}.json
(or a scratch copy of that directory, see AFRICA_G2P_DIR).

Usage:
  python scripts/gen_africa_orthographies.py --dry-run
  python scripts/gen_africa_orthographies.py --apply
  python scripts/gen_africa_orthographies.py --apply --limit 10
"""

import argparse
import glob
import json
import os
import re
from urllib.parse import quote

DATA = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa", "data")
AFRICA_G2P_DIR = os.environ.get(
    "AFRICA_G2P_DIR",
    os.path.expanduser("~/AgentWorkspaces/ml/africa-g2p/src/africa_g2p/languages"),
)

# When an ISO code has more than one africa-g2p regional chart, pick the one
# that represents the national/standard variety.
REGIONAL_VARIANT_PICK = {
    "dop": "dop-benin",
    "hau": "hau-nigeria",
    "ngb": "ngb-zaire",
    "sag": "sag-central_african_republic",
    "sef": "sef-cote_d_ivoire",
    "snk": "snk-senegal",
}

NON_LATIN_RANGES = [
    (0x0600, 0x06FF),  # Arabic
    (0x0750, 0x077F),  # Arabic supplement
    (0x1200, 0x139F),  # Ethiopic
    (0xA500, 0xA63F),  # Vai
    (0x07C0, 0x07FF),  # N'Ko
    (0x2C80, 0x2CFF),  # Coptic
]

VOWELS = set("aeiouɛɔəɨɪʊ")

# Doubly-articulated (labial-velar) stops/nasal: a single segment in West
# African phonologies, not a consonant cluster (Ladefoged & Maddieson 1996,
# "The Sounds of the World's Languages", ch. 8).
LABIAL_VELAR_UNITS = {"kp", "gb", "ŋm", "mgb", "nkp"}


def is_non_latin_char(c):
    cp = ord(c)
    return any(lo <= cp <= hi for lo, hi in NON_LATIN_RANGES)


def is_non_latin_file(graphemes):
    for k in graphemes:
        if any(is_non_latin_char(c) for c in k):
            return True
    return False


def strip_tiebar(ipa):
    return ipa.replace("͡", "").replace("͜", "")


def is_recognised_multigraph(key, ipa, single_ipa):
    """Test 2/3 heuristics for the AGENTS.md 3-part multigraph test, applied to
    a 2-character key whose IPA happens to equal the literal concatenation of
    its parts' IPA (so test 1 alone does not save it)."""
    if key in LABIAL_VELAR_UNITS:
        return True
    if len(key) != 2:
        return True  # only audit simple 2-char combinations; longer/irregular ones are kept
    c1, c2 = key[0], key[1]
    # prenasalized stop: n/m/ŋ + consonant, e.g. mb, nd, ng, nz
    if c1 in ("m", "n") and c2 not in VOWELS:
        return True
    # geminate: same letter twice (length / gemination)
    if c1 == c2:
        return True
    # palatalized / labialized series: Cy, Cw
    if c2 in ("y", "w") and c1 not in VOWELS:
        return True
    # affricate spelled as two consonant letters with a tie bar or affricate char
    if "͡" in ipa or "͜" in ipa or any(a in ipa for a in ("tʃ", "dʒ", "ts", "dz")):
        return True
    # diphthong / vowel nucleus: both letters are vowels
    if c1 in VOWELS and c2 in VOWELS:
        return True
    return False


def audit_graphemes(graphemes):
    """Return (kept, dropped) where dropped is [(key, ipa, reason), ...]."""
    single = {k: v for k, v in graphemes.items() if len(k) == 1}
    kept, dropped = {}, []
    for key, ipa in graphemes.items():
        if len(key) <= 1:
            kept[key] = ipa
            continue
        parts_ipa = "".join(single.get(c, "\0") for c in key)
        if parts_ipa == ipa and "\0" not in parts_ipa:
            if is_recognised_multigraph(key, ipa, ipa):
                kept[key] = ipa
            else:
                dropped.append((key, ipa, "IPA == literal concatenation of parts, no recognised multigraph class"))
        else:
            kept[key] = ipa
    return kept, dropped


def shape_flags(graphemes):
    flags = []
    if len(graphemes) > 60:
        flags.append(f"large inventory ({len(graphemes)} keys)")
    singles = [k for k in graphemes if len(k) == 1]
    cons = [c for c in singles if c not in VOWELS]
    vows = [c for c in singles if c in VOWELS]
    if cons and vows:
        cxv = sum(1 for k in graphemes if len(k) == 2 and k[0] in cons and k[1] in vows)
        if cxv >= len(cons) * len(vows) * 0.8 and len(cons) * len(vows) > 8:
            flags.append(f"looks like a C x V block ({cxv} of {len(cons)}x{len(vows)} pairs present)")
    return flags


def build_source(africa_spec):
    src = africa_spec.get("source", "")
    m = re.match(r"Omniglot chart \(([^)]+)\), .*", src)
    if m:
        chart = m.group(1)
        return {
            "id": f"omniglot-{chart.replace('.xls', '')}",
            "author": "Ager, Simon",
            # Omniglot charts carry no per-page publication year; 2026 records
            # the retrieval/compilation year (via africa-g2p), not authorship date.
            "year": 2026,
            "title": f"Omniglot chart ({chart})",
            "publisher": "Omniglot",
            "url": "https://www.omniglot.com/",
            "notes": "Undated web chart; year is retrieval year, not publication year.",
        }
    m = re.match(r"Hartell 1993, Alphabets of Africa \(UNESCO\), p\. (\d+)", src)
    if m:
        page = m.group(1)
        return {
            "id": f"hartell1993-p{page}",
            "author": "Hartell, Rhonda L. (ed.)",
            "year": 1993,
            "title": f"Alphabets of Africa, p. {page}",
            "publisher": "UNESCO/SIL, Dakar",
            "url": None,
        }
    return None


def load_africa_specs():
    variants = {}
    for f in sorted(glob.glob(os.path.join(AFRICA_G2P_DIR, "*.json"))):
        base = os.path.basename(f)[:-5]
        iso = base.split("-")[0]
        variants.setdefault(iso, []).append(base)
    picked = {}
    for iso, files in variants.items():
        if len(files) == 1:
            picked[iso] = files[0]
        else:
            picked[iso] = REGIONAL_VARIANT_PICK.get(iso, sorted(files)[0])
    specs = {}
    for iso, base in picked.items():
        with open(os.path.join(AFRICA_G2P_DIR, base + ".json"), encoding="utf-8") as fh:
            specs[iso] = (base, json.load(fh))
    return specs, variants


def load_o2i_specs():
    specs = {}
    by_iso3 = {}
    for f in glob.glob(os.path.join(DATA, "*.json")):
        code = os.path.basename(f)[:-5]
        with open(f, encoding="utf-8") as fh:
            d = json.load(fh)
        specs[code] = (f, d)
        if d.get("iso639_3"):
            by_iso3.setdefault(d["iso639_3"], []).append(code)
    return specs, by_iso3


def is_registry_stub(d):
    return (
        d.get("quality") == "stub"
        and not d.get("graphemes")
        and "REGISTRY STUB" in d.get("notes", "")
    )


def check_resolvable(codes_no_spec):
    """For africa-g2p codes with no o2i data file at all: check if
    orthography2ipa.get(code) resolves via alias. Returns (resolved, unresolvable)."""
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    import orthography2ipa

    resolved, unresolvable = [], []
    for code in sorted(codes_no_spec):
        try:
            spec = orthography2ipa.get(code)
            resolved.append((code, spec.code if spec else None))
        except Exception:
            unresolvable.append(code)
    return resolved, unresolvable


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    africa_specs, all_variants = load_africa_specs()
    o2i_specs, by_iso3 = load_o2i_specs()

    targets = []
    for iso, (base, aspec) in africa_specs.items():
        candidates = set()
        if iso in o2i_specs:
            candidates.add(iso)
        candidates.update(by_iso3.get(iso, []))
        for code in candidates:
            path, d = o2i_specs[code]
            if is_registry_stub(d):
                targets.append((iso, base, aspec, code, path, d))

    if args.limit:
        targets = targets[: args.limit]

    imported, skipped_non_latin, dropped_stats, flagged = [], [], {}, []
    unverified_wikipedia = []

    for iso, base, aspec, code, path, d in sorted(targets, key=lambda t: t[3]):
        raw_graphemes = aspec.get("graphemes", {})
        if not raw_graphemes:
            continue
        if is_non_latin_file(raw_graphemes):
            skipped_non_latin.append((code, aspec.get("name"), base))
            continue

        kept, dropped = audit_graphemes(raw_graphemes)
        if dropped:
            dropped_stats[code] = dropped
        flags = shape_flags(kept)
        if flags:
            flagged.append((code, flags))

        d["graphemes"] = {k: [v] for k, v in sorted(kept.items())}
        d["script"] = "Latin"
        d["script_type"] = "alphabet"
        d["quality"] = "skeleton"

        source_entry = build_source(aspec)
        sources = d.get("sources", [])
        if source_entry:
            sources = sources + [source_entry]
        d["sources"] = sources

        provenance = (
            f"Orthography from {'Hartell 1993, Alphabets of Africa (UNESCO/SIL)' if source_entry and source_entry['id'].startswith('hartell') else 'an Omniglot chart (c) Simon Ager, https://www.omniglot.com/'}"
            f", extracted via the AfriSpeech/africa-g2p compilation ({base}.json). "
            f"africa-g2p is a compilation tool, not the linguistic authority; the citation above is the "
            f"original source it names."
        )
        if not d.get("wikipedia"):
            # Best-effort English Wikipedia URL by the common "<Name>_language"
            # naming convention (matches the majority of existing entries);
            # not verified to resolve -- flagged in the PR body for review.
            name = d.get("name", "").split(" (")[0].strip()
            if name:
                d["wikipedia"] = [
                    f"https://en.wikipedia.org/wiki/{quote(name.replace(' ', '_'))}_language"
                ]
                unverified_wikipedia.append(code)

        old_notes = d.get("notes", "")
        new_notes = (
            old_notes.replace(
                "REGISTRY STUB (not a modelled G2P target). ",
                "",
            ).replace(
                "No orthography or phonology is claimed: script is Zyyy (undetermined) until a cited description is encoded. ",
                "",
            )
        )
        d["notes"] = (new_notes + " " + provenance).strip()

        imported.append(code)
        if args.apply:
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(d, fh, ensure_ascii=False, indent=1)
                fh.write("\n")

    matched_isos = {t[0] for t in targets}
    no_spec = sorted(set(africa_specs) - set(o2i_specs) - set().union(*[set(v) for v in [by_iso3.get(i, []) for i in africa_specs]]) if False else
                      [iso for iso in africa_specs if iso not in o2i_specs and iso not in by_iso3])

    print(f"africa-g2p rule files (after regional-variant pick): {len(africa_specs)}")
    print(f"matched empty REGISTRY STUB o2i specs: {len(targets)}")
    print(f"imported: {len(imported)}")
    print(f"skipped (non-Latin script): {len(skipped_non_latin)}")
    for code, name, base in skipped_non_latin:
        print(f"  - {code} ({name}, {base})")
    total_dropped = sum(len(v) for v in dropped_stats.values())
    print(f"dropped keys (derivable-concatenation audit): {total_dropped} across {len(dropped_stats)} spec(s)")
    for code, items in dropped_stats.items():
        for key, ipa, reason in items:
            print(f"  - {code}: {key!r} -> {ipa!r} ({reason})")
    if flagged:
        print(f"flagged inventory shapes: {len(flagged)}")
        for code, flags in flagged:
            print(f"  - {code}: {'; '.join(flags)}")
    if unverified_wikipedia:
        print(f"unverified best-effort wikipedia URLs added (review before merge): {len(unverified_wikipedia)}")
        print("  " + ", ".join(unverified_wikipedia))

    print()
    print(f"africa-g2p ISO codes with NO o2i data file at all: {len(no_spec)}")
    if no_spec:
        resolved, unresolvable = check_resolvable(no_spec)
        print(f"  resolved via orthography2ipa.get() alias: {len(resolved)}")
        for code, resolved_code in resolved:
            print(f"    - {code} -> {resolved_code}")
        print(f"  UNRESOLVABLE (likely retired/merged ISO codes, or genuinely uncovered): {len(unresolvable)}")
        for code in unresolvable:
            print(f"    - {code}")

    if not args.apply:
        print("\n(dry run: pass --apply to write)")


if __name__ == "__main__":
    main()
