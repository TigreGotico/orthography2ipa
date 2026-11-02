"""Every JSON key the spec loader reads is documented in ``data/SCHEMA.md``.

``orthography2ipa/json_loader.py`` builds a ``LanguageSpec`` from an explicit
list of keys, and a key it does not read is dropped at load time. The reverse
failure is quieter: a key the loader reads but ``SCHEMA.md`` never names is a
feature no spec author can find. This test reads the loader's source, collects
every string key it looks up, and requires each one to appear in
``SCHEMA.md`` as a code span (`` `key` ``).
"""
import ast
import re
from pathlib import Path

from orthography2ipa import json_loader
from orthography2ipa.types import FIELD_INHERITANCE

_ROOT = Path(__file__).resolve().parent.parent
_LOADER = _ROOT / "orthography2ipa" / "json_loader.py"
_SCHEMA = _ROOT / "orthography2ipa" / "data" / "SCHEMA.md"

# LanguageSpec fields the loader computes instead of reading from JSON.
_DERIVED_FIELDS = {"family_path", "grapheme_weights"}


def _string_constant(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def loader_keys() -> set:
    """The JSON keys ``json_loader.py`` reads, found by walking its AST.

    A key counts when it is the first argument of ``.get()``, a subscript
    (``raw["code"]``), or the left side of an ``in`` test. The one computed
    key, ``f"{field}_base"``, is expanded over the fields it is built from.
    """
    keys = set()
    for node in ast.walk(ast.parse(_LOADER.read_text(encoding="utf-8"))):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and node.func.attr == "get" and node.args):
            key = _string_constant(node.args[0])
        elif isinstance(node, ast.Subscript):
            key = _string_constant(node.slice)
        elif (isinstance(node, ast.Compare)
              and any(isinstance(op, ast.In) for op in node.ops)):
            key = _string_constant(node.left)
        elif isinstance(node, ast.JoinedStr):
            parts = [_string_constant(v) for v in node.values]
            if parts and parts[-1] == "_base":
                keys.update(f"{f}_base" for f in json_loader._BASE_MERGE_FIELDS)
            continue
        else:
            continue
        if key:
            keys.add(key)
    return keys


def documented_keys() -> set:
    return set(re.findall(r"`([A-Za-z_][A-Za-z0-9_]*)`",
                          _SCHEMA.read_text(encoding="utf-8")))


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


def test_every_loader_key_is_documented_in_schema():
    undocumented = sorted(loader_keys() - documented_keys())
    assert not undocumented, (
        f"json_loader.py reads these keys, and data/SCHEMA.md does not name "
        f"them as `key`: {undocumented}. Document each one in SCHEMA.md."
    )
