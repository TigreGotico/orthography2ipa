#!/usr/bin/env python3
"""Populate each spec's ``location`` from Glottolog's languoid coordinates.

Glottolog publishes a representative point for every languoid it catalogues, so a
spec that already carries a verified ``glottolog_code`` gets its coordinates for
free — no new research, no guessing.

What this does NOT do is invent a point. A spec with no glottocode, or whose
glottocode has no coordinates, is left with ``location: null``. Absence is honest;
a made-up point is not, and would silently corrupt every geographic comparison.

Usage::

    python scripts/gen_locations.py            # write locations
    python scripts/gen_locations.py --check    # fail if any spec is stale
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import os
import sys
import urllib.request

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_DATA = os.path.join(_ROOT, "orthography2ipa", "data")

LANGUOIDS_URL = (
    "https://raw.githubusercontent.com/glottolog/glottolog-cldf/"
    "master/cldf/languages.csv"
)


def load_glottolog() -> dict:
    """Return ``{glottocode: {lat, lon, name, level}}`` for coded languoids."""
    with urllib.request.urlopen(LANGUOIDS_URL, timeout=120) as fh:
        text = fh.read().decode("utf-8")

    table = {}
    for row in csv.DictReader(io.StringIO(text)):
        code = row.get("Glottocode") or row.get("ID")
        lat, lon = row.get("Latitude"), row.get("Longitude")
        if not (code and lat and lon):
            continue
        table[code] = {
            "lat": float(lat),
            "lon": float(lon),
            "name": row.get("Name", ""),
            "level": row.get("Level", ""),
        }
    return table


def location_for(spec: dict, glottolog: dict) -> dict | None:
    """The location a spec should carry, or None if we cannot honestly give it one."""
    code = spec.get("glottolog_code")
    if not code:
        return None
    entry = glottolog.get(code)
    if not entry:
        return None

    # Say what the point actually represents, so a consumer can judge it. A
    # family's point is a computed centroid and is much weaker evidence than a
    # single language's.
    if entry["level"] == "family":
        note = (f"Glottolog's computed centroid for the {entry['name']} family — "
                f"a summary of a whole clade's range, not a place anyone speaks.")
    else:
        note = f"Glottolog's representative point for {entry['name']}."

    return {
        "latitude": round(entry["lat"], 6),
        "longitude": round(entry["lon"], 6),
        "source": "glottolog",
        "notes": note,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="exit non-zero if any spec's location is stale")
    args = ap.parse_args()

    glottolog = load_glottolog()
    written = cleared = stale = 0
    no_code = no_coords = 0

    for name in sorted(os.listdir(_DATA)):
        if not name.endswith(".json"):
            continue
        path = os.path.join(_DATA, name)
        with open(path, encoding="utf-8") as fh:
            spec = json.load(fh)

        wanted = location_for(spec, glottolog)
        current = spec.get("location")

        if wanted is None:
            if not spec.get("glottolog_code"):
                no_code += 1
            else:
                no_coords += 1
            if current is not None:
                if args.check:
                    stale += 1
                else:
                    spec.pop("location", None)
                    cleared += 1
                    _write(path, spec)
            continue

        if current == wanted:
            continue
        if args.check:
            stale += 1
            print(f"stale: {spec['code']}", file=sys.stderr)
            continue
        spec["location"] = wanted
        written += 1
        _write(path, spec)

    if args.check:
        if stale:
            print(f"{stale} spec(s) have a stale location — "
                  f"run scripts/gen_locations.py", file=sys.stderr)
            return 1
        print("locations up to date")
        return 0

    print(f"wrote {written} location(s), cleared {cleared}")
    print(f"left null: {no_code} with no glottocode, "
          f"{no_coords} whose glottocode has no coordinates")
    return 0


def _write(path: str, spec: dict) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(spec, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


if __name__ == "__main__":
    raise SystemExit(main())
