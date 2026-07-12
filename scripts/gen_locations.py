#!/usr/bin/env python3
"""Populate each spec's ``location`` from Glottolog, or from a Wikidata PLACE.

Two sources, in that order of preference:

1. **Glottolog.** It publishes a representative point for every languoid it
   catalogues, so a spec that carries a verified ``glottolog_code`` gets its
   coordinates for free — no new research, no guessing.
2. **A Wikidata place.** Glottolog does not catalogue Portuense, Paisa, or the
   Aragonese of the Bielsa valley — and dialects are exactly where geography
   matters most, a continuum being a geographic object. Those specs are anchored
   in ``scripts/dialect_places.py`` to a PLACE (a valley, a city, a region) whose
   coordinate is read from that item's Wikidata P625 here. No latitude is ever
   typed by hand, so a mistake can only ever be the wrong PLACE — never a
   transposed or invented point — and ``--check`` catches that by verifying each
   item's label and country (P17) against what the entry claims.

What this does NOT do is invent a point. A spec that is neither catalogued nor
anchored is left with ``location: null``; ``dialect_places.UNLOCATABLE`` records
WHY for the deliberate ones (proto-languages with contested homelands, clade
nodes, a supraregional literary koine). Absence is honest; a made-up point is not,
and would silently corrupt every geographic comparison.

Usage::

    python scripts/gen_locations.py            # write locations
    python scripts/gen_locations.py --check    # fail if any spec is stale or unsound
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import math
import os
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dialect_places import PLACES, UNLOCATABLE  # noqa: E402

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_DATA = os.path.join(_ROOT, "orthography2ipa", "data")

LANGUOIDS_URL = (
    "https://raw.githubusercontent.com/glottolog/glottolog-cldf/"
    "master/cldf/languages.csv"
)
WIKIDATA_API = "https://www.wikidata.org/w/api.php"
_UA = {"User-Agent": "orthography2ipa-gen-locations/1.0 "
                     "(https://github.com/TigreGotico/orthography2ipa)"}

# A point further than this from every other spec that shares its parent is
# reported for human eyes. It is a smell detector, not a rule: colonial varieties
# ARE legitimately an ocean away from their parent, so the check compares a spec
# against its SIBLINGS, and only prints.
_OUTLIER_KM = 3000.0


def load_wikidata_places() -> dict:
    """Return ``{qid: {lat, lon, label, country}}`` for every anchored place.

    The coordinate comes from P625 and the country from P17 — both read live, so
    the repo stores a Wikidata item id, never a hand-typed number.
    """
    qids = sorted({e["qid"] for e in PLACES.values()})
    out: dict[str, dict] = {}
    for i in range(0, len(qids), 40):
        chunk = qids[i:i + 40]
        url = (f"{WIKIDATA_API}?action=wbgetentities&format=json"
               f"&props=labels|claims&languages=en|mul&ids={'|'.join(chunk)}")
        req = urllib.request.Request(url, headers=_UA)
        with urllib.request.urlopen(req, timeout=120) as fh:
            data = json.load(fh)
        for qid, entity in data.get("entities", {}).items():
            claims = entity.get("claims", {})
            coord = claims.get("P625")
            if not coord:
                continue
            value = coord[0]["mainsnak"].get("datavalue", {}).get("value", {})
            # An item can carry several P17s — the modern state plus every empire
            # that ever held the place. Keep them all; the check asks only that the
            # expected country be AMONG them.
            countries = []
            for snak in claims.get("P17", []):
                cid = snak["mainsnak"].get("datavalue", {}).get("value", {}).get("id")
                if cid:
                    countries.append(cid)
            out[qid] = {
                "lat": value["latitude"],
                "lon": value["longitude"],
                "label": _label(entity),
                "country_qids": countries,
            }
    # Resolve the country ids to labels in one more call, so the entry's plain-English
    # ``country`` can be verified without anyone memorising QIDs.
    cids = sorted({c for e in out.values() for c in e["country_qids"]})
    labels = {}
    for i in range(0, len(cids), 40):
        chunk = cids[i:i + 40]
        url = (f"{WIKIDATA_API}?action=wbgetentities&format=json"
               f"&props=labels&languages=en|mul&ids={'|'.join(chunk)}")
        req = urllib.request.Request(url, headers=_UA)
        with urllib.request.urlopen(req, timeout=120) as fh:
            data = json.load(fh)
        for qid, entity in data.get("entities", {}).items():
            labels[qid] = _label(entity)
    for entry in out.values():
        entry["countries"] = [labels.get(c, "") for c in entry["country_qids"]]
    return out


def _label(entity: dict) -> str:
    """The item's English name. Wikidata increasingly stores a language-neutral
    ``mul`` label instead of an ``en`` one, so accept either."""
    labels = entity.get("labels", {})
    for lang in ("en", "mul"):
        if lang in labels:
            return labels[lang]["value"]
    return ""


def verify_places(places: dict) -> list[str]:
    """Identity check. A Wikidata item that RESOLVES is not thereby the right item.

    Every anchored place must still carry the label the entry expects and sit in
    the country the entry expects — so a mistyped QID, or an item that has been
    merged away under us, is caught loudly rather than becoming a plausible-looking
    coordinate in the wrong country.
    """
    problems = []
    for code, entry in sorted(PLACES.items()):
        got = places.get(entry["qid"])
        if not got:
            problems.append(f"{code}: {entry['qid']} has no P625 coordinate")
            continue
        if got["label"] != entry["label"]:
            problems.append(f"{code}: {entry['qid']} is '{got['label']}', "
                            f"the entry expects '{entry['label']}'")
        want_country = entry.get("country")
        if want_country and want_country not in got.get("countries", []):
            problems.append(f"{code}: {entry['qid']} is in "
                            f"{got.get('countries')!r}, the entry expects "
                            f"{want_country!r}")
    return problems


def report_shared_points(located: dict) -> list[str]:
    """Flag Glottolog points shared by several specs.

    Glottolog-CLDF hands a dialect its parent languoid's coordinates, so two specs
    landing on the SAME point means at most one of them is really there. Where the
    shared point is also the wrong country (Cuban Spanish in Aragón) an anchor in
    ``dialect_places`` overrides it. This report keeps any remaining sharers — and
    any that appear as Glottolog grows — visible instead of silently plausible.

    Proto-language/clade pairs are exempt: a family node and its reconstructed
    proto-language genuinely ARE the same point, by construction.
    """
    groups: dict[tuple, list[str]] = {}
    for code, loc in located.items():
        if loc["source"] != "glottolog":
            continue
        groups.setdefault((loc["latitude"], loc["longitude"]), []).append(code)

    flagged = []
    for point, codes in sorted(groups.items()):
        if len(codes) < 2:
            continue
        if all(c.startswith("x-clade-") or "proto" in c or len(c) == 3
               for c in codes):
            continue
        flagged.append(f"{', '.join(sorted(codes))} all sit on {point} — "
                       f"Glottolog gave a dialect its parent's coordinates")
    return flagged


def _haversine(a: dict, b: dict) -> float:
    lat1, lon1, lat2, lon2 = map(math.radians, (a["latitude"], a["longitude"],
                                                b["latitude"], b["longitude"]))
    h = (math.sin((lat2 - lat1) / 2) ** 2
         + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2)
    return 2 * 6371.0088 * math.asin(math.sqrt(h))


def report_outliers(located: dict, parents: dict) -> list[str]:
    """Flag any spec implausibly far from every sibling under the same parent.

    This is what catches a transposed lat/lon or a wrong-country item: an Aragonese
    valley that lands outside Aragón, or a Portuguese dialect that lands in Brazil,
    is thousands of kilometres from its nearest sibling. It prints; it does not fail,
    because some distances are real (Brazilian and European Portuguese are one such
    pair, and so the check is sibling-based rather than parent-based).
    """
    by_parent: dict[str, list[str]] = {}
    for code in located:
        by_parent.setdefault(parents.get(code) or "", []).append(code)

    flagged = []
    for parent, codes in sorted(by_parent.items()):
        if len(codes) < 2:
            continue
        for code in sorted(codes):
            nearest = min(_haversine(located[code], located[other])
                          for other in codes if other != code)
            if nearest > _OUTLIER_KM:
                flagged.append(f"{code}: {nearest:.0f} km from its nearest sibling "
                               f"under '{parent}' — verify it is the right place")
    return flagged


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


def location_for(spec: dict, glottolog: dict, places: dict) -> dict | None:
    """The location a spec should carry, or None if we cannot honestly give it one.

    An explicit anchor WINS over Glottolog: an anchor is only ever added where
    Glottolog has no point, or where its point is its parent languoid's and so
    describes a different place entirely (see ``dialect_places``).
    """
    anchored = _place_location(spec["code"], places)
    if anchored:
        return anchored

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


def _place_location(code: str, places: dict) -> dict | None:
    """The location of a dialect anchored to a Wikidata place, if it is anchored."""
    entry = PLACES.get(code)
    if not entry:
        return None
    got = places.get(entry["qid"])
    if not got:
        return None
    return {
        "latitude": round(got["lat"], 6),
        "longitude": round(got["lon"], 6),
        "source": "wikidata",
        "notes": f"{entry['note']} [Wikidata {entry['qid']} P625]",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="exit non-zero if any spec's location is stale or unsound")
    args = ap.parse_args()

    glottolog = load_glottolog()
    places = load_wikidata_places()

    problems = verify_places(places)
    for problem in problems:
        print(f"WRONG PLACE: {problem}", file=sys.stderr)

    written = cleared = stale = 0
    unlocated = []
    located: dict[str, dict] = {}
    parents: dict[str, str] = {}

    for name in sorted(os.listdir(_DATA)):
        if not name.endswith(".json"):
            continue
        path = os.path.join(_DATA, name)
        with open(path, encoding="utf-8") as fh:
            spec = json.load(fh)

        wanted = location_for(spec, glottolog, places)
        current = spec.get("location")
        parents[spec["code"]] = spec.get("parent")

        if wanted is None:
            unlocated.append(spec["code"])
            if current is not None:
                if args.check:
                    stale += 1
                else:
                    spec.pop("location", None)
                    cleared += 1
                    _write(path, spec)
            continue

        located[spec["code"]] = wanted
        if current == wanted:
            continue
        if args.check:
            stale += 1
            print(f"stale: {spec['code']}", file=sys.stderr)
            continue
        spec["location"] = wanted
        written += 1
        _write(path, spec)

    for flag in report_shared_points(located):
        print(f"SHARED GLOTTOLOG POINT: {flag}", file=sys.stderr)

    flagged = report_outliers(located, parents)
    for flag in flagged:
        print(f"FAR FROM SIBLINGS: {flag}", file=sys.stderr)

    if args.check:
        if problems:
            print(f"{len(problems)} anchored place(s) are not the item the entry "
                  f"claims", file=sys.stderr)
        if stale:
            print(f"{stale} spec(s) have a stale location — "
                  f"run scripts/gen_locations.py", file=sys.stderr)
        if problems or stale:
            return 1
        print(f"locations up to date ({len(located)} located, "
              f"{len(unlocated)} null)")
        return 0

    print(f"wrote {written} location(s), cleared {cleared}")
    print(f"{len(located)} located; {len(unlocated)} left null, "
          f"of which {sum(1 for c in unlocated if c in UNLOCATABLE)} deliberately "
          f"(see dialect_places.UNLOCATABLE)")
    unexplained = [c for c in unlocated if c not in UNLOCATABLE]
    if unexplained:
        print(f"no location and no recorded reason: {', '.join(unexplained)}")
    return 0


def _write(path: str, spec: dict) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(spec, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


if __name__ == "__main__":
    raise SystemExit(main())
