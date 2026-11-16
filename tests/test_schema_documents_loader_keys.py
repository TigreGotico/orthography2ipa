"""Every JSON key the spec loader reads is documented in ``data/SCHEMA.md``.

``orthography2ipa/json_loader.py`` builds a ``LanguageSpec`` from an explicit
list of keys, and a key it does not read is dropped at load time. The reverse
failure is quieter: a key the loader reads but ``SCHEMA.md`` never names is a
feature no spec author can find. This test reads the loader's source, collects
every string key it looks up, and requires each one to have a row in the
``SCHEMA.md`` table of the object it is read from. A key that only the prose of
another row names does not count, and neither does a row of the same name in
the table of another object.

``docs/specs/data_model.md`` groups the ``LanguageSpec`` fields in one table
for the Python reader, so every dataclass field must be in that table too.
"""
import ast
import dataclasses
import re
from pathlib import Path

from orthography2ipa import json_loader
from orthography2ipa.types import FIELD_INHERITANCE, LanguageSpec

_ROOT = Path(__file__).resolve().parent.parent
_LOADER = _ROOT / "orthography2ipa" / "json_loader.py"
_SCHEMA = _ROOT / "orthography2ipa" / "data" / "SCHEMA.md"
_DATA_MODEL = _ROOT / "docs" / "specs" / "data_model.md"

# LanguageSpec fields the loader computes instead of reading from JSON.
_DERIVED_FIELDS = {"family_path", "grapheme_weights"}

#: The loader variable a key is read from, mapped to the SCHEMA.md section
#: whose table documents that object. The inheritance tables hold names of
#: top-level fields, so they map to the top-level table.
_SECTION_OF = {
    "raw": "Fields",
    "base_field_langs": "Fields",
    "base_scalars": "Fields",
    "merged_base_fields": "Fields",
    "_resolved_overlay": "Fields",
    "raw_stress": "Stress Schema",
    "ar": "Allophone Rule Schema",
    "sr": "Sandhi Rule Schema",
    "s": "Sources Schema",
    "ancestor": "Ancestor Schema",
    "raw_loc": "Location Schema",
    "raw_timespan": "Timespan Schema",
    "raw_tone": "Tone Rules Schema",
    "raw_ortho": "Orthography Standard Schema",
    "raw_ceiling": "Valid Ceiling Schema",
    "raw_c": "Valid Ceiling Schema",
    "raw_a": "Audit Schema",
}

#: Variables that hold the value of one stress key. The row of that key lists
#: their keys as "Keys: `pairs` (...), ...".
_SUBKEYS_OF = {
    "raw_hiatus": ("Stress Schema", "closed_hiatus"),
    "raw_final": ("Stress Schema", "final_diphthongs"),
}

_ROW = re.compile(r"^\|\s*`([A-Za-z_][A-Za-z0-9_]*)`\s*\|(.*)$")


def _string_constant(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def loader_reads() -> set:
    """``(variable, key)`` for every JSON key ``json_loader.py`` reads.

    A key counts when it is the first argument of ``.get()``, a subscript
    (``raw["code"]``), or the left side of an ``in`` test. The variable is the
    source text of the object the key is read from. The one computed key,
    ``f"{field}_base"``, is expanded over the fields it is built from.
    """
    reads = set()
    for node in ast.walk(ast.parse(_LOADER.read_text(encoding="utf-8"))):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and node.func.attr == "get" and node.args):
            key, obj = _string_constant(node.args[0]), node.func.value
        elif isinstance(node, ast.Subscript):
            key, obj = _string_constant(node.slice), node.value
        elif (isinstance(node, ast.Compare)
              and any(isinstance(op, ast.In) for op in node.ops)):
            key, obj = _string_constant(node.left), node.comparators[0]
        elif isinstance(node, ast.JoinedStr):
            parts = [_string_constant(v) for v in node.values]
            if parts and parts[-1] == "_base":
                reads.update(("raw", f"{f}_base")
                             for f in json_loader._BASE_MERGE_FIELDS)
            continue
        else:
            continue
        if key:
            reads.add((ast.unparse(obj), key))
    return reads


def loader_keys() -> set:
    return {key for _, key in loader_reads()}


def schema_rows() -> dict:
    """Section heading to ``{key: rest of the row}``, for each table row of
    ``SCHEMA.md`` whose first cell is one code span."""
    sections, current = {}, None
    for line in _SCHEMA.read_text(encoding="utf-8").splitlines():
        heading = re.match(r"^## (.+?)\s*$", line)
        if heading:
            current = sections.setdefault(heading.group(1), {})
            continue
        row = _ROW.match(line)
        if row and current is not None:
            current[row.group(1)] = row.group(2)
    return sections


def data_model_table() -> str:
    """The rows of the field table under ``## `LanguageSpec``` in
    ``data_model.md``."""
    section = _DATA_MODEL.read_text(encoding="utf-8").split(
        "\n## `LanguageSpec`\n", 1)[1].split("\n#", 1)[0]
    return "\n".join(line for line in section.splitlines()
                     if line.startswith("|"))


def test_scan_finds_every_inherited_spec_field():
    """The AST scan sees every JSON field ``FIELD_INHERITANCE`` declares.

    ``FIELD_INHERITANCE`` is an independent list of the spec's fields. A scan
    that misses one of them is broken, and its silence would pass the main
    test for the wrong reason.
    """
    missing = set(FIELD_INHERITANCE) - _DERIVED_FIELDS - loader_keys()
    assert not missing, f"loader scan missed spec fields: {sorted(missing)}"


def test_scan_finds_the_computed_base_keys():
    keys = loader_keys()
    for key in ("graphemes_base", "allophones_base",
                "positional_graphemes_base", "word_exceptions_base",
                "grammatical_endings_base"):
        assert key in keys


def test_scan_reads_nested_keys_off_their_own_object():
    """The scan attributes a key to the object it is read from: ``source``
    is read off both the stress block and the location, and the two are
    documented in two tables."""
    reads = loader_reads()
    assert ("raw_stress", "source") in reads
    assert ("raw_loc", "source") in reads
    assert ("raw_hiatus", "pairs") in reads


def test_every_loader_variable_maps_to_a_schema_section():
    """A key read from an object this test does not map is checked against
    no table, so a new loader variable must be mapped first."""
    unmapped = sorted({obj for obj, _ in loader_reads()}
                      - set(_SECTION_OF) - set(_SUBKEYS_OF))
    assert not unmapped, (
        f"json_loader.py reads keys from {unmapped}. Map each one to its "
        f"SCHEMA.md section in _SECTION_OF or _SUBKEYS_OF.")


def test_every_mapped_section_exists_in_schema():
    wanted = set(_SECTION_OF.values()) | {s for s, _ in _SUBKEYS_OF.values()}
    missing = sorted(wanted - set(schema_rows()))
    assert not missing, f"SCHEMA.md has no section named {missing}"


def test_every_loader_key_has_a_row_in_its_schema_table():
    sections = schema_rows()
    missing = []
    for obj, key in sorted(loader_reads()):
        if obj in _SUBKEYS_OF:
            section, parent = _SUBKEYS_OF[obj]
            listed = re.search(r"Keys:(.*)",
                               sections.get(section, {}).get(parent, ""))
            if not listed or f"`{key}` (" not in listed.group(1):
                missing.append(f"{section} > {parent} > {key}")
        elif key not in sections.get(_SECTION_OF.get(obj), {}):
            missing.append(f"{_SECTION_OF.get(obj)} > {key}")
    assert not missing, (
        f"json_loader.py reads these keys, and data/SCHEMA.md has no table "
        f"row for them in the section of their object: {missing}.")


def test_every_spec_field_is_in_the_data_model_table():
    grouped = set(re.findall(r"`([A-Za-z_][A-Za-z0-9_]*)`", data_model_table()))
    missing = sorted(f.name for f in dataclasses.fields(LanguageSpec)
                     if f.name not in grouped)
    assert not missing, (
        f"docs/specs/data_model.md groups the LanguageSpec fields in one "
        f"table, and these fields are not in it: {missing}.")
