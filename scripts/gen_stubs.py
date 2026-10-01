"""Generate stub specs for every living ISO 639-3 language missing from the registry.

Each stub follows the documented `stub` tier (docs/quality_tiers.md): code, name,
script and a resolvable clade chain, no phonology claimed. Classification,
coordinates and languoid levels come from Glottolog (CLDF export). Isolates get
an authored ``family: "Isolate"`` per the existing convention (xib, ecr, ecy).

Inputs (download once, not bundled):
  ~/tmp/iso-639-3.tab            https://iso639-3.sil.org/ (tab export)
  ~/tmp/glottolog_languages.csv  glottolog-cldf cldf/languages.csv

Usage:
  python scripts/gen_stubs.py --dry-run
  python scripts/gen_stubs.py --apply
"""

import argparse
import csv
import glob
import json
import os

DATA = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa", "data")
SNAPSHOT = os.path.join(os.path.dirname(__file__), "..", "tests", "data", "glottolog_levels.json")

GLOTTOLOG_SOURCE = {
    "id": "glottolog2024",
    "author": "Hammarström, Harald; Forkel, Robert; Haspelmath, Martin; Bank, Sebastian",
    "year": 2024,
    "title": "Glottolog 5.0",
    "publisher": "Max Planck Institute for Evolutionary Anthropology",
    "url": "https://glottolog.org/",
}


def load_existing():
    specs = {}
    for f in glob.glob(os.path.join(DATA, "*.json")):
        code = os.path.basename(f)[:-5]
        with open(f, encoding="utf-8") as fh:
            specs[code] = json.load(fh)
    return specs


def covered_iso(specs):
    """ISO 639-3 codes already represented by any spec (via iso639_3 or code base)."""
    covered = set()
    for code, s in specs.items():
        if s.get("iso639_3"):
            covered.add(s["iso639_3"])
        covered.add(code.split("-")[0])
    return covered


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="cap number of stubs (0 = all)")
    args = ap.parse_args()

    specs = load_existing()
    covered = covered_iso(specs)
    existing_glottocodes = {s.get("glottolog_code") for s in specs.values() if s.get("glottolog_code")}

    with open(os.path.expanduser("~/tmp/iso-639-3.tab"), encoding="utf-8") as fh:
        iso_rows = [r for r in csv.DictReader(fh, delimiter="\t")]
    # part1 alias coverage (a spec named `pt` covers iso639-3 `por`)
    for r in iso_rows:
        if r["Part1"] and r["Part1"] in covered:
            covered.add(r["Id"])

    glotto = {}
    families = {}
    by_glottocode = {}
    with open(os.path.expanduser("~/tmp/glottolog_languages.csv"), encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            by_glottocode[r["Glottocode"]] = r
            # language-level rows win; dialect-level rows are the fallback for the
            # ISO codes Glottolog demotes to dialects (Chakavian, Deccan, ...)
            if r["ISO639P3code"] and (
                r["Level"] == "language" or r["ISO639P3code"] not in glotto
            ):
                glotto[r["ISO639P3code"]] = r
            if r["Level"] == "family":
                families[r["Glottocode"]] = r
    spec_by_glottocode = {
        s["glottolog_code"]: c for c, s in specs.items() if s.get("glottolog_code")
    }

    # fil (Filipino) shadows the existing Tagalog spec in code resolution: the
    # loader's BCP-47 normalisation maps tl onto fil, so a fil spec would hijack
    # get("tl"). Tagalog coverage stands in for it.
    ALIAS_COLLISIONS = {"fil"}

    targets = [
        r for r in iso_rows
        if r["Scope"] == "I" and r["Language_Type"] == "L"
        and r["Id"] not in covered and r["Id"] not in ALIAS_COLLISIONS
    ]
    if args.limit:
        targets = targets[: args.limit]

    new_specs, new_clades, skipped = {}, {}, []
    snapshot_add = {}

    for r in targets:
        iso = r["Id"]
        g = glotto.get(iso)
        if g is None:
            skipped.append((iso, r["Ref_Name"], "no Glottolog language-level languoid"))
            continue
        stub = {
            "code": iso,
            "name": r["Ref_Name"],
            "script": "Zyyy",
            "quality": "stub",
            "graphemes": {},
            "allophones": {},
            "notes": (
                "REGISTRY STUB (not a modelled G2P target). Placed so the ancestry "
                "graph covers every living ISO 639-3 language. No orthography or "
                "phonology is claimed: script is Zyyy (undetermined) until a cited "
                "description is encoded. Classification and coordinates follow Glottolog."
            ),
            "iso639_3": iso,
            "sources": [GLOTTOLOG_SOURCE],
            "urls": [f"https://glottolog.org/resource/languoid/id/{g['Glottocode']}"],
        }
        if g["Level"] != "family":
            stub["glottolog_code"] = g["Glottocode"]
        else:
            # Glottolog sometimes pins an ISO code on a family node (jya, chm, ...);
            # glottolog_code may only point at a language, so leave it out.
            stub["notes"] += (
                " No glottolog_code: Glottolog assigns this ISO code to a "
                "family-level node, which the field may not point at."
            )
        if g["Latitude"]:
            stub["location"] = {
                "latitude": round(float(g["Latitude"]), 4),
                "longitude": round(float(g["Longitude"]), 4),
                "source": "glottolog",
                "notes": "Glottolog's representative point.",
            }
        fid = g["Family_ID"]
        if g["Level"] == "dialect":
            # Family_ID on a dialect row is its containing language. Parent the
            # stub to that language's spec when one exists; otherwise climb to
            # the language row and use its real family.
            lang = by_glottocode.get(g["Language_ID"])
            if g["Language_ID"] in spec_by_glottocode:
                stub["parent"] = spec_by_glottocode[g["Language_ID"]]
                new_specs[iso] = stub
                if g["Glottocode"] not in existing_glottocodes:
                    snapshot_add[g["Glottocode"]] = {"name": g["Name"], "level": "dialect"}
                continue
            if lang is None:
                skipped.append((iso, r["Ref_Name"], "dialect with unresolvable language"))
                continue
            fid = lang["Family_ID"]
            g = dict(g, Is_Isolate=lang["Is_Isolate"])
        if g["Is_Isolate"] == "true" or not fid:
            stub["family"] = "Isolate"
        else:
            clade = f"x-clade-{fid}"
            stub["parent"] = clade
            if clade not in specs and clade not in new_clades:
                fam = families[fid]
                new_clades[clade] = {
                    "code": clade,
                    "name": fam["Name"],
                    "script": "Zyyy",
                    "quality": "stub",
                    "clade": True,
                    "graphemes": {},
                    "allophones": {},
                    "notes": (
                        f"Classification-only clade node for the {fam['Name']} family. "
                        "Carries no phonology: it is never a data-inheritance source, "
                        "only a step in the ancestry chain from which `family` is derived."
                    ),
                    "glottolog_code": fid,
                    "sources": [GLOTTOLOG_SOURCE],
                    "urls": [f"https://glottolog.org/resource/languoid/id/{fid}"],
                }
                snapshot_add[fid] = {"name": fam["Name"], "level": "family"}
        if g["Glottocode"] not in existing_glottocodes:
            snapshot_add[g["Glottocode"]] = {"name": g["Name"], "level": g["Level"]}
        new_specs[iso] = stub

    print(f"targets: {len(targets)}  stubs: {len(new_specs)}  "
          f"new clades: {len(new_clades)}  skipped: {len(skipped)}")
    for iso, name, why in skipped[:20]:
        print(f"  skip {iso} ({name}): {why}")
    if len(skipped) > 20:
        print(f"  ... and {len(skipped) - 20} more (see gen_stubs_skipped.tsv)")

    if not args.apply:
        return

    for code, spec in {**new_clades, **new_specs}.items():
        path = os.path.join(DATA, f"{code}.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(spec, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
    with open(SNAPSHOT, encoding="utf-8") as fh:
        snap = json.load(fh)
    snap.update(snapshot_add)
    with open(SNAPSHOT, "w", encoding="utf-8") as fh:
        json.dump(snap, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    with open(os.path.expanduser("~/tmp/gen_stubs_skipped.tsv"), "w", encoding="utf-8") as fh:
        fh.write("\n".join("\t".join(s) for s in skipped))

    # Prune stubs the loader's BCP-47 normalisation already resolves to another
    # spec (macrolanguage variants: zsm→ms, cmn→zh, npi→ne, ...). Those codes
    # are covered, and a stub file would shadow the covering spec.
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    import orthography2ipa as o2i
    pruned = []
    for code in list(new_specs):
        try:
            resolved = o2i.get(code).code
        except Exception:
            resolved = code
        if resolved != code:
            os.remove(os.path.join(DATA, f"{code}.json"))
            pruned.append((code, resolved))
    print(f"pruned {len(pruned)} alias-covered stubs: "
          + ", ".join(f"{c}→{r}" for c, r in pruned))
    print("applied.")


if __name__ == "__main__":
    main()
