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


def test_every_spec_field_is_parsed_by_the_loader():
    """Forcing function: a field declared on LanguageSpec must actually be read
    from the spec JSON.

    ``glottolog_code`` was declared on the dataclass, validated in the schema
    and given an inheritance decision, yet json_loader never passed it to the
    constructor — so every spec resolved it to None and the field was inert.
    The FIELD_INHERITANCE manifest test cannot catch that: it only cross-checks
    the dataclass against the manifest, never against the loader. This closes
    the gap by asserting the loader's ``LanguageSpec(...)`` call names every
    field.
    """
    import ast
    import dataclasses
    from orthography2ipa.types import LanguageSpec

    loader = os.path.join(os.path.dirname(__file__), "..", "orthography2ipa", "json_loader.py")
    with open(loader, encoding="utf-8") as fh:
        tree = ast.parse(fh.read())

    passed = set()
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == "LanguageSpec"):
            passed |= {kw.arg for kw in node.keywords if kw.arg}

    declared = {f.name for f in dataclasses.fields(LanguageSpec)}
    missing = sorted(declared - passed)
    assert not missing, (
        f"declared on LanguageSpec but never parsed by json_loader: {missing} — "
        "the field would silently resolve to its default for every spec"
    )


def test_new_crossref_fields_parse_from_a_synthetic_spec(tmp_path, monkeypatch):
    """The three new ids have no data in-tree yet, so exercise their parse path
    against a synthetic spec rather than relying on a round-trip over real
    specs, which would vacuously pass while nothing declares them."""
    from pathlib import Path

    from orthography2ipa import json_loader

    (tmp_path / "xx.json").write_text(json.dumps({
        "code": "xx",
        "name": "Test",
        "family": "Test",
        "script": "Latin",
        "graphemes": {"a": ["a"]},
        "glottolog_code": "test1234",
        "wikidata_qid": "Q1321",
        "phoible_id": "2175",
        "wals_code": "spa",
        "urls": ["https://glottolog.org/resource/languoid/id/test1234"],
    }), encoding="utf-8")

    monkeypatch.setattr(json_loader, "_DATA_DIR", Path(tmp_path))
    monkeypatch.setitem(json_loader._index, "xx", tmp_path / "xx.json")
    spec = json_loader.load_json_spec("xx")

    assert spec.glottolog_code == "test1234"
    assert spec.wikidata_qid == "Q1321"
    assert spec.phoible_id == "2175"
    assert spec.wals_code == "spa"
    assert spec.urls == ("https://glottolog.org/resource/languoid/id/test1234",)


def test_malformed_cross_reference_ids_are_rejected():
    """A typo'd identifier is exactly the error a linked-data hub field invites,
    so the schema must reject it rather than store it verbatim."""
    import pytest
    from pydantic import ValidationError

    from orthography2ipa.schema import LanguageSpecModel

    base = dict(code="xx", name="Test", family="Test", script="Latin",
                graphemes={"a": ["a"]})
    for bad in ({"wikidata_qid": "banana"}, {"wikidata_qid": "Q0"},
                {"glottolog_code": "!!"}, {"iso639_3": "spanish"},
                {"phoible_id": ""}, {"wals_code": ""}):
        with pytest.raises(ValidationError):
            LanguageSpecModel(**base, **bad)

    # …and well-formed ids are accepted.
    ok = LanguageSpecModel(**base, wikidata_qid="Q1321", glottolog_code="stan1288",
                           iso639_3="spa", phoible_id="2175", wals_code="spa")
    assert ok.wikidata_qid == "Q1321"


def test_orthography_standard_is_a_first_class_field():
    """An official published spelling norm is the primary authority for what a
    grapheme is, so it must be reachable on the spec — not buried in `urls`."""
    pt = o2i.get("pt-PT")
    assert pt.orthography_standard is not None
    assert pt.orthography_standard.year == 1990
    assert "Acordo Ortográfico" in pt.orthography_standard.name
    assert pt.orthography_standard.url

    gl = o2i.get("gl")
    assert gl.orthography_standard is not None
    assert "Real Academia Galega" in gl.orthography_standard.authority

    # A language with no official norm (or a dialect following its parent's)
    # simply has none — the field is not fabricated.
    assert o2i.get("roa-x-galaicopt").orthography_standard is None


# ── Glottolog languoid guard ────────────────────────────────────────────────
# A regex over `glottolog_code` cannot catch the two failure modes that occur
# in practice: a SUPERSEDED languoid (well-formed, may still render a page, but
# retired by Glottolog) and a WRONG-LEVEL languoid (resolves, but to a *family*
# node rather than the language — e.g. Shona pointed at "Core Shona").
# `scripts/check_glottolog_codes.py` queries Glottolog and snapshots each
# declared code's level into tests/data/glottolog_levels.json; these tests
# assert against that snapshot offline. Re-run the script with --write when a
# glottolog_code is added or changed.

_GLOTTOLOG_LEVELS = os.path.join(os.path.dirname(__file__), "data",
                                 "glottolog_levels.json")

# Specs whose spec code IS a macrolanguage or a family/proto node: a family
# languoid is the correct answer for them, not a defect.
_FAMILY_LEVEL_OK = {
    # ISO 639-3 macrolanguages: the language-level languoid does not exist,
    # so the family node IS the correct answer.
    "cr", "din", "eml", "ik", "kr", "kv", "mg", "ff", "ps", "ay", "qu", "sq",
    "nah", "sc",
    # Family / grouping / proto specs — these ARE family nodes by design.
    "afa", "ber", "iir", "ira", "khi", "nic", "sla", "xbr",
    "ta-x-proto-dravidian", "mni-x-proto-kuki-chin",
    # Dialect-group nodes whose Glottolog counterpart is a subfamily.
    "ber-x-kabyle-atlas", "de-x-alemannic", "gem-x-ingvaeonic",
    "roa-x-galaicopt",
    # Reconstructed stages and regional Latin/Arabic groupings. Glottolog has no
    # language-level node for a proto-stage or a dialect continuum's ancestor —
    # the subfamily IS the node, so a family languoid is the only correct answer.
    "sat-x-proto-munda", "kha-x-proto-mon-khmer", "gem-x-northwest",
    "la-x-hispania", "la-x-italia", "la-x-galloitalic", "la-x-balkans",
    "ar-x-peninsular", "ar-x-maghrebi",
}


def _glottolog_snapshot():
    with open(_GLOTTOLOG_LEVELS, encoding="utf-8") as fh:
        return json.load(fh)


def _declared_glottolog_codes():
    declared = {}
    for path in glob.glob(os.path.join(_DATA, "*.json")):
        with open(path) as fh:
            raw = json.load(fh)
        if isinstance(raw, dict) and raw.get("glottolog_code"):
            declared[raw["code"]] = raw["glottolog_code"]
    return declared


def test_every_glottolog_code_resolves_to_a_known_languoid():
    """No dead or superseded codes: every declared code is in the snapshot.

    A code absent from the snapshot either did not resolve in Glottolog or was
    never checked — run `python scripts/check_glottolog_codes.py --write`.
    """
    snapshot = _glottolog_snapshot()
    unknown = {code: gcode
               for code, gcode in _declared_glottolog_codes().items()
               if gcode not in snapshot}
    assert not unknown, (
        f"glottolog_code(s) not verified against Glottolog: {unknown}. "
        f"Run: python scripts/check_glottolog_codes.py --write"
    )


def test_glottolog_code_level_is_a_language_not_a_family():
    """A modern single language must not be pinned to a family node.

    Family-level languoids are legitimate only for the macrolanguage and
    family/proto specs listed in `_FAMILY_LEVEL_OK` or already carrying a
    family-node spec code.
    """
    snapshot = _glottolog_snapshot()
    offenders = []
    for code, gcode in _declared_glottolog_codes().items():
        if code in _FAMILY_LEVEL_OK:
            continue
        spec = o2i.get(code)
        if getattr(spec, "clade", False) or code.startswith("x-clade-"):
            # A clade IS a family. Pointing it at a family-level languoid is not
            # the bug this test hunts — it is the only correct answer.
            continue
        if spec.script_type is not None and str(
                getattr(spec.script_type, "value", spec.script_type)
        ) == "reconstruction":
            continue  # proto/reconstruction node: a family languoid is correct
        level = snapshot.get(gcode, {}).get("level")
        if level is not None and level not in ("language", "dialect"):
            offenders.append((code, gcode, snapshot[gcode]["name"], level))
    assert not offenders, (
        "glottolog_code points at a family node rather than the language: "
        f"{offenders}"
    )
