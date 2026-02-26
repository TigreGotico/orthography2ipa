"""JSON-based language data loader for orthography2ipa.

Reads LanguageSpec definitions from JSON files, resolving inheritance
chains (``graphemes_base``, ``allophones_base``, ``positional_graphemes_base``)
and converting plain JSON values into typed Python objects (``Ancestor``,
``AncestorRole``, ``GraphemePosition``, ``LanguageSpec``).

Usage
-----
>>> from orthography2ipa.json_loader import load_json_spec, load_all_json_specs
>>> spec = load_json_spec("es-ES")
>>> specs = load_all_json_specs()

The JSON files live under ``orthography2ipa/data/`` organised by family.
See ``data/SCHEMA.md`` for the JSON schema reference.
"""
from __future__ import annotations

import json
import warnings
from pathlib import Path
from typing import Dict, List

from orthography2ipa.types import (
    Ancestor,
    AncestorRole,
    GraphemePosition,
    LanguageSpec,
)

# ═══════════════════════════════════════════════════════════════════════════
# Constants
# ═══════════════════════════════════════════════════════════════════════════

_DATA_DIR = Path(__file__).parent / "data"

# Map JSON string keys → GraphemePosition enum values
_POSITION_MAP: Dict[str, GraphemePosition] = {
    pos.value: pos for pos in GraphemePosition
}

# Map JSON string keys → AncestorRole enum values
_ROLE_MAP: Dict[str, AncestorRole] = {
    role.value: role for role in AncestorRole
}

_index: Dict[str, Path] = {}
_specs: Dict[str, LanguageSpec] = {}


def _index_files():
    global _index
    for lang_file in _DATA_DIR.glob("*.json"):
        lang_code = lang_file.name.split(".json")[0]
        _index[lang_code] = lang_file


# ═══════════════════════════════════════════════════════════════════════════
# Public API
# ═══════════════════════════════════════════════════════════════════════════

def load_json_spec(code: str) -> LanguageSpec:
    """Load a single ``LanguageSpec`` from JSON, resolving inheritance.

    Parameters
    ----------
    code : str
        BCP-47 or ISO 639 language code.

    Returns
    -------
    LanguageSpec
        Fully resolved, immutable language specification.

    Raises
    ------
    KeyError
        If the code is not found in any JSON file.
    ValueError
        If the JSON is malformed or contains invalid enum values.
    """
    global _specs

    # retrieve from cache
    if code in _specs:
        return _specs[code]

    # load json
    if code not in _index:
        raise KeyError(f"unsupported language: '{code}.json' not found. Available: {set(_index.keys())}")
    lang_file: Path = _index[code]
    with lang_file.open() as f:
        raw = json.load(f)

    # ensure all related languages also loaded
    parent_lang = raw.get("parent")
    parent_graphemes_lang = raw.get("graphemes_base")
    parent_positional_graphemes_lang = raw.get("positional_graphemes_base")
    parent_allophones_lang = raw.get("allophones_base")
    ancestors = raw.get("ancestors", [])
    ancestor_langs = [ancestor["code"] for ancestor in ancestors]
    for parent in (parent_lang, parent_graphemes_lang, parent_positional_graphemes_lang,
                   parent_allophones_lang, *ancestor_langs):
        if parent == code:
            continue  # TODO - error log, illegal
        if parent and parent not in _specs:
            try:
                _specs[parent] = load_json_spec(parent)
            except (KeyError, ValueError) as e:
                raise ValueError(f"Failed to load '{parent}' (requested by '{code}'): {e}")

    # merge parent data
    graphemes = raw.get("graphemes", {})
    allophones = raw.get("allophones", {})
    positional_graphemes = raw.get("positional_graphemes", {})
    if parent_graphemes_lang:
        graphemes = {
            **_specs[parent_graphemes_lang].graphemes,
            **raw.get("graphemes", {})
        }
    if parent_allophones_lang:
        allophones = {
            **_specs[parent_allophones_lang].allophones,
            **raw.get("allophones", {})
        }
    if parent_positional_graphemes_lang:
        positional_graphemes = {
            **_specs[parent_positional_graphemes_lang].positional_graphemes,
            **raw.get("positional_graphemes", {})
        }

    # parse ancestors
    try:
        ancestors = tuple(Ancestor(code=ancestor["code"],
                                   role=ancestor["role"],  # will auto cast to enum
                                   weight=ancestor.get("weight", 0.0),
                                   notes=ancestor.get("notes", ""))
                          for ancestor in ancestors)
    except Exception as e:
        raise ValueError(f"Failed to load ancestors for '{code}'") from e

    spec = LanguageSpec(
        code=raw["code"],
        name=raw["name"],
        family=raw["family"],
        script=raw["script"],
        graphemes=graphemes,
        allophones=allophones,
        positional_graphemes=positional_graphemes or {},  # will auto cast to enum
        parent=parent_lang,
        ancestors=ancestors,
        notes=raw.get("notes", ""),
    )

    _specs[code] = spec

    return spec


def load_all_json_specs() -> Dict[str, LanguageSpec]:
    """Load all LanguageSpecs from the data directory.

    Returns
    -------
    Dict[str, LanguageSpec]
        Mapping of language codes to their specs.
    """
    global _specs
    for code in _index:
        if code not in _specs:
            try:
                _specs[code] = load_json_spec(code)
            except (KeyError, ValueError) as e:
                # Log but don't crash — allows partial loading
                import warnings
                warnings.warn(f"Failed to load '{code}': {e}")
    return _specs


def available_json_codes() -> List[str]:
    """Return sorted list of all language codes with JSON data files."""
    return sorted(_index.keys())


_index_files()
