"""Fill stub specs with cited phoneme inventories from PHOIBLE 2.0.

For every registry stub that claims no phonology, look up its language in
PHOIBLE (Moran & McCloy 2019, https://doi.org/10.5281/zenodo.2562766), pick one
inventory deterministically, and write:

  phonemes        non-marginal consonant/vowel segments
  allophones      phoneme -> surface allophones (PHOIBLE Allophones column)
  tone_inventory  tone segments, kept out of `phonemes`
  phoible_id      the chosen InventoryID
  sources         PHOIBLE citation + the per-inventory URL

The spelling side is untouched: graphemes stay empty and quality stays `stub`
(the skeleton tier starts at a non-empty grapheme inventory). This encodes the
"sounds are not a property of spelling" invariant: for an unwritten language a
cited inventory IS the complete honest phonological description.

Inventory choice, in order: a language-level match (no SpecificDialect) from
the most descriptive contributor first (spa, gm, ph, aa, ea, er, ra, saphon,
uz), UPSID last (it normalises inventories aggressively); ties broken by the
lowest InventoryID.

Input (download once, not bundled):
  ~/tmp/phoible.csv   https://github.com/phoible/dev  data/phoible.csv

Usage:
  python scripts/gen_phoible.py [--apply]
"""

import argparse
import csv
import glob
import json
import os
from collections import defaultdict

DATA = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa", "data")

SOURCE_PREFERENCE = ["spa", "gm", "ph", "aa", "ea", "er", "ra", "saphon", "uz", "upsid"]

PHOIBLE_SOURCE = {
    "id": "phoible2019",
    "author": "Moran, Steven; McCloy, Daniel (eds.)",
    "year": 2019,
    "title": "PHOIBLE 2.0 (doi:10.5281/zenodo.2562766)",
    "publisher": "Max Planck Institute for the Science of Human History",
    "url": "https://phoible.org/",
    
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    inventories = defaultdict(list)
    with open(os.path.expanduser("~/tmp/phoible.csv"), encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            inventories[(r["InventoryID"], r["ISO6393"], r["Glottocode"])].append(r)

    # index candidate inventories per ISO code
    by_iso = defaultdict(list)
    for (inv_id, iso, glottocode), rows in inventories.items():
        if iso and iso != "NA":
            by_iso[iso].append((inv_id, glottocode, rows))

    def rank(candidate):
        inv_id, _glottocode, rows = candidate
        src = rows[0]["Source"]
        dialect_free = all(r["SpecificDialect"] in ("NA", "") for r in rows)
        pref = SOURCE_PREFERENCE.index(src) if src in SOURCE_PREFERENCE else len(SOURCE_PREFERENCE)
        return (not dialect_free, pref, int(inv_id))

    updated, skipped_marginal_only, no_data = [], [], []
    for path in sorted(glob.glob(os.path.join(DATA, "*.json"))):
        with open(path, encoding="utf-8") as fh:
            spec = json.load(fh)
        if spec.get("quality") != "stub" or spec.get("clade"):
            continue
        if spec.get("phonemes") or spec.get("graphemes"):
            continue  # something already claims phonology; not ours to overwrite
        if "REGISTRY STUB" not in spec.get("notes", ""):
            continue  # only touch sweep-generated stubs
        iso = spec.get("iso639_3")
        if not iso or iso not in by_iso:
            no_data.append(spec["code"])
            continue
        inv_id, glottocode, rows = sorted(by_iso[iso], key=rank)[0]

        phonemes, tones, allophones = [], [], {}
        n_marginal = 0
        for r in rows:
            seg = r["Phoneme"]
            if r["Marginal"] == "TRUE":
                n_marginal += 1
                continue
            if r["SegmentClass"] == "tone":
                tones.append(seg)
                continue
            phonemes.append(seg)
            allo = [a for a in r["Allophones"].split() if a not in ("NA", "")]
            if allo and allo != [seg]:
                allophones[seg] = allo
        if not phonemes:
            skipped_marginal_only.append(spec["code"])
            continue

        spec["phonemes"] = phonemes
        if allophones:
            spec["allophones"] = allophones
        if tones:
            spec["tone_inventory"] = {t: "PHOIBLE tone segment" for t in tones}
        spec["phoible_id"] = str(inv_id)
        spec["sources"] = spec.get("sources", []) + [
            dict(
                PHOIBLE_SOURCE,
                url=f"https://phoible.org/inventories/view/{inv_id}",
                notes=f"Inventory {inv_id} ({rows[0]['Source']}), "
                      f"{len(phonemes)} non-marginal segments"
                      + (f", {n_marginal} marginal excluded" if n_marginal else "")
                      + (f", {len(tones)} tones" if tones else "") + ".",
            )
        ]
        spec["notes"] = spec["notes"].replace(
            "No orthography or phonology is claimed",
            "No orthography is claimed; the phoneme inventory follows the cited "
            "PHOIBLE inventory (which itself cites a published description)",
        )
        updated.append(spec["code"])
        if args.apply:
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(spec, fh, ensure_ascii=False, indent=1)
                fh.write("\n")

    print(f"updated: {len(updated)}  no PHOIBLE data: {len(no_data)}  "
          f"marginal-only: {len(skipped_marginal_only)}")
    if not args.apply:
        print("(dry run: pass --apply to write)")


if __name__ == "__main__":
    main()
