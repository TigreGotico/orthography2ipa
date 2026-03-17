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

import csv
import json
import warnings
from pathlib import Path
from typing import Dict, List, Optional

from orthography2ipa.types import (
    Ancestor,
    AncestorRole,
    GraphemePosition,
    LanguageSpec,
    LinguisticSource,
    QualityTier,
    SandhiRule,
    ScriptType,
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
    # Base specs (graphemes_base etc.) MUST be loadable — they provide data.
    # Ancestor-only references are best-effort (ancestors may be proto-languages
    # that exist only as stubs or not at all).
    _base_parents = {parent_graphemes_lang, parent_allophones_lang,
                     parent_positional_graphemes_lang}

    for parent in (parent_lang, parent_graphemes_lang, parent_positional_graphemes_lang,
                   parent_allophones_lang, *ancestor_langs):
        if parent == code:
            continue  # Skip self-reference cycles (parent == code); invalid per schema
        if parent and parent not in _specs:
            try:
                _specs[parent] = load_json_spec(parent)
            except (KeyError, ValueError) as e:
                is_base_dep = parent in _base_parents
                if is_base_dep:
                    # Base dependency is required for data inheritance — clear it
                    import warnings
                    warnings.warn(f"Could not load base '{parent}' (requested by '{code}'): {e}")
                    if parent == parent_graphemes_lang:
                        parent_graphemes_lang = None
                        raw["graphemes_base"] = None
                    elif parent == parent_allophones_lang:
                        parent_allophones_lang = None
                        raw["allophones_base"] = None
                    elif parent == parent_positional_graphemes_lang:
                        parent_positional_graphemes_lang = None
                        raw["positional_graphemes_base"] = None
                elif parent == parent_lang:
                    # Parent language is needed for ancestry but not data — tolerate
                    parent_lang = None
                # else: ancestor-only reference — silently skip

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

    # Parse sandhi rules
    sandhi_rules = ()
    raw_sandhi = raw.get("sandhi_rules", [])
    if raw_sandhi:
        sandhi_rules = tuple(
            SandhiRule(
                id=sr["id"],
                name=sr["name"],
                left_context=sr["left_context"],
                right_context=sr["right_context"],
                transform=sr["transform"],
                obligatory=sr.get("obligatory", True),
                notes=sr.get("notes", ""),
            )
            for sr in raw_sandhi
        )

    # Parse sources
    sources_raw = raw.get("sources", [])
    sources = tuple(
        LinguisticSource(
            id=s["id"],
            author=s["author"],
            year=s["year"],
            title=s["title"],
            publisher=s.get("publisher"),
            url=s.get("url"),
            pages=s.get("pages"),
            notes=s.get("notes"),
        )
        for s in sources_raw
    )

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
        quality=raw.get("quality", QualityTier.RESEARCH),
        script_type=raw.get("script_type", ScriptType.ALPHABET),
        inherent_vowel=raw.get("inherent_vowel"),
        iso639_3=raw.get("iso639_3"),
        sandhi_rules=sandhi_rules,
        tone_inventory=raw.get("tone_inventory"),
        sources=sources,
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


def load_lexicon(code: str) -> Optional[Dict[str, str]]:
    """Load the bundled IPA lexicon for a language code, if one exists.

    Reads the CSV file declared in the language's JSON ``lexicon_csv`` field.
    The CSV must have at minimum ``word`` and ``ipa`` columns; additional
    columns (``source``, ``pt_equivalent``) are ignored.

    Parameters
    ----------
    code : str
        BCP-47 language code (e.g. ``"ast-PT-x-rionor"``).

    Returns
    -------
    Dict[str, str] or None
        Mapping of orthographic word → best IPA string, or ``None`` if the
        language has no bundled lexicon or the file cannot be found.

    Examples
    --------
    >>> lex = load_lexicon("ast-PT-x-rionor")
    >>> lex["abajo"]
    'aˈbaʒo'
    """
    if code not in _index:
        return None
    lang_file: Path = _index[code]
    with lang_file.open() as f:
        raw = json.load(f)
    csv_rel = raw.get("lexicon_csv")
    if not csv_rel:
        return None
    csv_path = _DATA_DIR / csv_rel
    if not csv_path.exists():
        warnings.warn(
            f"lexicon_csv '{csv_rel}' declared for '{code}' but file not found at {csv_path}",
            stacklevel=2,
        )
        return None
    lexicon: Dict[str, str] = {}
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            word = row.get("word", "").strip().lower()
            ipa = row.get("ipa", "").strip()
            if word and ipa:
                lexicon[word] = ipa
    return lexicon


_index_files()
