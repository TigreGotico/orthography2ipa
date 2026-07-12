#!/usr/bin/env python3
"""Validate every ``glottolog_code`` in ``orthography2ipa/data/`` against Glottolog.

A regex cannot catch the two failure modes that actually occur:

1. **Dead / superseded languoids** — the code is well-formed and may even still
   render a page, but Glottolog has retired or merged it (e.g. ``nort2794``).
2. **Wrong level** — the code resolves, but to a *family* node rather than the
   language (e.g. Shona pointed at ``core1255`` "Core Shona", a family). Family
   nodes are only legitimate for a genuine macrolanguage or a proto-node.

This script queries Glottolog live and writes the resulting levels to
``tests/data/glottolog_levels.json``, which ``tests/test_catalog_crossrefs.py``
asserts against offline. Re-run it whenever a ``glottolog_code`` is added or
changed::

    python scripts/check_glottolog_codes.py            # report only
    python scripts/check_glottolog_codes.py --write    # refresh the snapshot

Codes whose spec legitimately points at a family node (macrolanguages such as
``cr``, ``kv``, ``kr``, ``din``, ``mg``, ``ik``, ``eml``, and the proto-nodes)
are recorded with their level in the snapshot, so the reviewer sees the level
rather than having to trust a comment.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys
import time
import urllib.error
import urllib.request

_DATA = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa", "data")
_SNAPSHOT = os.path.join(os.path.dirname(__file__), "..", "tests", "data",
                         "glottolog_levels.json")
_UA = {"User-Agent": "orthography2ipa glottolog check (openvoiceos@gmail.com)"}
_OK_LEVELS = ("language", "dialect")


def declared_codes() -> dict:
    """Map spec code -> glottolog_code for every spec that declares one."""
    out = {}
    for path in sorted(glob.glob(os.path.join(_DATA, "*.json"))):
        with open(path, encoding="utf-8") as fh:
            raw = json.load(fh)
        if isinstance(raw, dict) and raw.get("glottolog_code"):
            out[raw["code"]] = raw["glottolog_code"]
    return out


def languoid(gcode: str):
    """Return (name, level) for *gcode*, or None when it does not resolve."""
    url = f"https://glottolog.org/resource/languoid/id/{gcode}.json"
    req = urllib.request.Request(url, headers=_UA)
    for _ in range(3):
        try:
            data = json.load(urllib.request.urlopen(req))
            return data.get("name"), data.get("level")
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
            time.sleep(5)
        except Exception:
            time.sleep(5)
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true",
                    help="refresh tests/data/glottolog_levels.json")
    args = ap.parse_args()

    snapshot, dead, family = {}, [], []
    for code, gcode in declared_codes().items():
        info = languoid(gcode)
        if info is None:
            dead.append((code, gcode))
            continue
        name, level = info
        snapshot[gcode] = {"name": name, "level": level}
        if level not in _OK_LEVELS:
            family.append((code, gcode, name, level))
        time.sleep(0.3)

    for code, gcode in dead:
        print(f"DEAD    {code}: {gcode} does not resolve in Glottolog")
    for code, gcode, name, level in family:
        print(f"LEVEL   {code}: {gcode} is {name!r} at level {level!r} — "
              f"legitimate only for a macrolanguage or proto-node")

    if args.write:
        os.makedirs(os.path.dirname(_SNAPSHOT), exist_ok=True)
        with open(_SNAPSHOT, "w", encoding="utf-8") as fh:
            json.dump(dict(sorted(snapshot.items())), fh,
                      ensure_ascii=False, indent=2)
            fh.write("\n")
        print(f"wrote {len(snapshot)} languoids to {_SNAPSHOT}")

    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
