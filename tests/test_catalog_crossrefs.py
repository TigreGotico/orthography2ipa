"""Cross-reference catalog identifiers on a LanguageSpec.

Each spec may carry standard ids into external knowledge bases so it is a
node in the linked-data graph rather than an island: Glottolog (genealogy),
ISO 639-3, Wikidata (the hub that resolves all the others), PHOIBLE (attested
phoneme inventories) and WALS (typology).
"""
import json
import glob
import os

import orthography2ipa as o2i
from orthography2ipa.types import FIELD_INHERITANCE, InheritanceMode

_DATA = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa", "data")

CROSSREF_FIELDS = ("glottolog_code", "iso639_3", "wikidata_qid", "phoible_id", "wals_code")


def test_crossref_fields_are_own_only_never_inherited():
    """An identifier belongs to exactly one language — a dialect must never
    inherit its parent's Glottolog/Wikidata/PHOIBLE id."""
    for field in CROSSREF_FIELDS:
        assert FIELD_INHERITANCE[field] is InheritanceMode.OWN_ONLY


def test_glottolog_code_in_json_is_actually_loaded():
    """A glottolog_code declared in a spec's JSON must reach the loaded spec."""
    declared = {}
    for path in glob.glob(os.path.join(_DATA, "*.json")):
        with open(path, encoding="utf-8") as fh:
            raw = json.load(fh)
        if raw.get("glottolog_code"):
            declared[raw["code"]] = raw["glottolog_code"]

    assert declared, "expected some specs to declare a glottolog_code"
    for code, expected in declared.items():
        assert o2i.get(code).glottolog_code == expected


def test_crossref_fields_round_trip_from_json():
    """Every cross-reference id declared in JSON reaches the loaded spec."""
    for path in glob.glob(os.path.join(_DATA, "*.json")):
        with open(path, encoding="utf-8") as fh:
            raw = json.load(fh)
        spec = o2i.get(raw["code"])
        for field in CROSSREF_FIELDS:
            if raw.get(field):
                assert getattr(spec, field) == raw[field]
