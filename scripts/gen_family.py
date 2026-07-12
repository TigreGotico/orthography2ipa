#!/usr/bin/env python3
"""Regenerate the ``family`` field of every language spec from Glottolog.

``family`` is a **curated mapping onto** each spec's Glottolog classification path — not a
verbatim slice of it. Glottolog has no ``Romance`` node (Portuguese sits under
``Italic > Latino-Faliscan > Latinic > Imperial Latin > Romance …`` only via nodes whose names are
unusable as labels: ``Shifted Western Romance``, ``Southwestern Shifted Romance``, …). So we pick,
out of that path, the deepest node belonging to a controlled vocabulary of traditional branch and
sub-branch names, and render:

    "<top-level family> > <branch> > <sub-branch>"

dropping any level that does not apply. Examples::

    pt-PT   Indo-European > Romance > Ibero-Romance
    fr-FR   Indo-European > Romance > Gallo-Romance
    de-DE   Indo-European > Germanic > West Germanic
    ru      Indo-European > Slavic > East Slavic
    arb     Afro-Asiatic > Semitic > Central Semitic
    tr      Turkic

The CLI's ``--family`` filter matches *any* step of the path, so ``--family Romance`` and
``--family Ibero-Romance`` both work.

Specs with no ``glottolog_code`` (reconstructed proto-nodes, contact nodes) inherit ``family`` from
their o2i parent, or take a value from ``MANUAL`` below.

Usage:  python scripts/gen_family.py [--check]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "orthography2ipa" / "data"
LANGUAGES_CSV = "https://raw.githubusercontent.com/glottolog/glottolog-cldf/master/cldf/languages.csv"
VALUES_CSV = "https://raw.githubusercontent.com/glottolog/glottolog-cldf/master/cldf/values.csv"

# Traditional branch names, as they appear in Glottolog.
BRANCH = {
    "Romance", "Germanic", "Slavic", "Balto-Slavic", "Celtic", "Indo-Aryan", "Iranian",
    "Indo-Iranian", "Italic", "Armenic", "Albanian", "Greek", "Graeco-Phrygian", "Semitic",
    "Berber", "Cushitic", "Chadic", "Egyptian", "Omotic", "Turkic", "Mongolic", "Tungusic",
    "Dravidian", "Uralic", "Finnic", "Saami", "Sinitic", "Bodic", "Burmish", "Japonic",
    "Koreanic", "Kartvelian", "Mayan", "Quechuan", "Aymaran", "Tupian", "Uto-Aztecan",
    "Araucanian",
}

# Sub-branches: Glottolog node name -> traditional label. The deepest match on the path wins.
SUB = {
    # Romance
    "West Ibero-Romance": "Ibero-Romance", "Castilic": "Ibero-Romance",
    "Galician Romance": "Ibero-Romance", "Macro-Portuguese": "Ibero-Romance",
    "Spanish": "Ibero-Romance", "Asturo-Leonese": "Ibero-Romance",
    "Gallo-Rhaetian": "Gallo-Romance", "Oil": "Gallo-Romance",
    "Occitano-Romance": "Occitano-Romance",
    "Italo-Dalmatian": "Italo-Romance", "Italian Romance": "Italo-Romance",
    "Eastern Romance": "Eastern Romance", "Southern Romance": "Southern Romance",
    # Germanic
    "West Germanic": "West Germanic", "North Germanic": "North Germanic",
    "East Germanic": "East Germanic",
    # Slavic
    "West Slavic": "West Slavic", "East Slavic": "East Slavic", "South Slavic": "South Slavic",
    # Semitic
    "Central Semitic": "Central Semitic", "West Semitic": "West Semitic",
    "East Semitic": "East Semitic", "Ethiosemitic": "Ethiosemitic",
    # Celtic
    "Goidelic": "Goidelic", "Brythonic": "Brythonic",
    # Iranian
    "Southwestern Iranian": "Western Iranian", "Western Iranian": "Western Iranian",
    "Eastern Iranian": "Eastern Iranian",
}

# Specs with no glottocode whose family cannot be inherited from a parent.
MANUAL = {
    "khi": "Khoe-Kwadi",
    "eo": "Constructed",
    "xaq": "Basque",
    "eu": "Basque",
    # Romance varieties whose o2i parent is a Vulgar Latin stage: inheriting the Latin node's
    # "Italic" branch would mislabel them.
    "roa-x-galaicopt": "Indo-European > Romance > Ibero-Romance",
    "it-IT-x-abruzzo": "Indo-European > Romance > Italo-Romance",
    "it-IT-x-calabria": "Indo-European > Romance > Italo-Romance",
    "it-IT-x-puglia": "Indo-European > Romance > Italo-Romance",
    # orphan: parent is null (see docs/glottolog_audit.md 3a); parent not rewired here
    "pt-PT-x-lisbon": "Indo-European > Romance > Ibero-Romance",
    # reconstructed proto-nodes with no parent and no Glottolog node of their own
    "brx-x-proto-boro-garo": "Sino-Tibetan",
    "kha-x-proto-mon-khmer": "Austroasiatic",
    "sat-x-proto-munda": "Austroasiatic",
    "xpa": "Afro-Asiatic > Semitic > Central Semitic",
}


def load_glottolog():
    import csv
    csv.field_size_limit(10 ** 7)
    G, CLASS = {}, {}
    with urllib.request.urlopen(LANGUAGES_CSV) as fh:
        for r in csv.DictReader(l.decode() for l in fh):
            G[r["ID"]] = {"name": r["Name"], "level": r["Level"], "family_id": r["Family_ID"]}
    with urllib.request.urlopen(VALUES_CSV) as fh:
        for r in csv.DictReader(l.decode() for l in fh):
            if r["Parameter_ID"] == "classification":
                CLASS[r["Language_ID"]] = [x for x in r["Value"].split("/") if x]
    return G, CLASS


def family_from_code(gc, G, CLASS):
    v = G.get(gc)
    if not v:
        return None
    top = G[v["family_id"]]["name"] if v["family_id"] else (
        v["name"] if v["level"] == "family" else None)
    if not top:
        return "Isolate"          # Glottolog gives it no family: a true isolate
    # the node's OWN name is a candidate too, else a spec whose code *is* the branch node
    # (e.g. sla -> slav1255 "Slavic") would pick up the branch *above* it.
    path = [G[c]["name"] for c in CLASS.get(gc, []) if c in G] + [v["name"]]
    branch = sub = None
    for n in path:
        if n in BRANCH and n != top:
            branch = n
        if n in SUB:
            sub = SUB[n]
    return " > ".join(x for x in (top, branch, sub) if x)


def build(specs, G, CLASS):
    out = {}

    def resolve(code, seen=frozenset()):
        if code in seen:
            return None
        if code in MANUAL:
            return MANUAL[code]
        gc = specs[code].get("glottolog_code")
        if gc:
            f = family_from_code(gc, G, CLASS)
            if f:
                return f
        p = specs[code].get("parent")
        return resolve(p, seen | {code}) if p and p in specs else None

    for code in specs:
        f = resolve(code)
        if not f:
            raise SystemExit(f"cannot resolve family for {code}")
        out[code] = f
    return out


def set_field(raw, key, value):
    jv = json.dumps(value, ensure_ascii=False)
    pat = re.compile(
        r'^(\s*)"%s"\s*:\s*(?:"(?:[^"\\]|\\.)*"|null)\s*(,?)\s*$' % re.escape(key), re.M)
    return pat.sub(lambda m: f'{m.group(1)}"{key}": {jv}{m.group(2)}', raw, count=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="exit non-zero if any spec's family is stale")
    args = ap.parse_args()

    paths = sorted(DATA.glob("*.json"))
    specs = {}
    for p in paths:
        d = json.loads(p.read_text(encoding="utf-8"))
        specs[d["code"]] = d
        d["_path"] = p

    G, CLASS = load_glottolog()
    fam = build(specs, G, CLASS)

    stale = [c for c in specs if specs[c]["family"] != fam[c]]
    if args.check:
        for c in stale:
            print(f"STALE {c}: {specs[c]['family']!r} -> {fam[c]!r}")
        print(f"{len(stale)} stale of {len(specs)}")
        return 1 if stale else 0

    for c in stale:
        p = specs[c]["_path"]
        p.write_text(set_field(p.read_text(encoding="utf-8"), "family", fam[c]), encoding="utf-8")
    print(f"updated {len(stale)} of {len(specs)} specs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
