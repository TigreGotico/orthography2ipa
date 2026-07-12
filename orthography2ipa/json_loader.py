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
    AllophoneRule,
    Ancestor,
    AncestorRole,
    FIELD_INHERITANCE,
    GraphemePosition,
    InheritanceMode,
    LanguageSpec,
    LinguisticSource,
    Location,
    OrthographyKind,
    OrthographyStandard,
    QualityTier,
    SandhiRule,
    ScriptType,
    StressRules,
    TimeSpan,
)
from orthography2ipa.weights import split_weighted_graphemes

# Fields resolved via the ``{field}_base`` JSON key + ``{**base, **own}``
# dict merge (graphemes, allophones, positional_graphemes).
_BASE_MERGE_FIELDS: tuple = tuple(
    f for f, mode in FIELD_INHERITANCE.items() if mode is InheritanceMode.BASE_MERGE
)

# Fields resolved via id-keyed overlay (sandhi_rules). These have no
# dedicated ``{field}_base`` JSON key of their own — the schema doesn't
# declare one per rule-bearing field — so they inherit through the same
# structural base edge as ``graphemes`` (the primary data-inheritance
# pointer), falling back to the ancestry ``parent`` when no explicit
# ``graphemes_base`` is set (e.g. Arabic dialects that only set
# ``graphemes_base`` and leave ``parent`` empty).
_OVERLAY_BY_ID_FIELDS: tuple = tuple(
    f for f, mode in FIELD_INHERITANCE.items() if mode is InheritanceMode.OVERLAY_BY_ID
)


def _nearest_data_ancestor(code: Optional[str]) -> Optional[str]:
    """Return the nearest ancestor of *code* (itself included) that can carry
    data, skipping classification-only clade nodes.

    A clade (``Romance``, ``West Germanic``) has no phonology and must never
    act as a data-inheritance source. Splicing one into the ancestry chain
    between a spec and its data-bearing parent would otherwise silently strip
    the spec's inherited ``sandhi_rules`` / ``allophone_rules``; walking
    through clades keeps the inheritance edge pointing at the same language it
    pointed at before the clade existed.
    """
    seen = set()
    while code and code in _specs and code not in seen:
        seen.add(code)
        spec = _specs[code]
        if not spec.clade:
            return code
        code = spec.parent
    return None


def _derive_family_path(parent_code: Optional[str]) -> "Tuple[str, ...]":
    """Return the classification path implied by *parent_code*'s chain.

    The path is the names of the clade nodes on the ancestry chain, broadest
    first. Each spec's own ``family_path`` already holds its ancestors' clades,
    so one step of recursion is enough.
    """
    from typing import Tuple  # noqa: F401 — used in annotation only
    if not parent_code or parent_code not in _specs:
        return ()
    parent = _specs[parent_code]
    if parent.clade:
        return parent.family_path + (parent.name,)
    return parent.family_path


def _overlay_by_id(base_items: tuple, own_items: tuple) -> tuple:
    """Merge two sequences of id-keyed objects (``.id`` attribute).

    The base sequence's order and members are inherited in full; any own
    item whose ``id`` matches a base item replaces it in-place (same
    position), and any own item with a new ``id`` is appended. This avoids
    both silently dropping the base's rules (a blind own-only read) and
    silently duplicating a rule the leaf re-declares to override it (a
    blind concatenation).
    """
    merged: List = list(base_items)
    index = {item.id: i for i, item in enumerate(merged)}
    for item in own_items:
        if item.id in index:
            merged[index[item.id]] = item
        else:
            index[item.id] = len(merged)
            merged.append(item)
    return tuple(merged)

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
# Helpers
# ═══════════════════════════════════════════════════════════════════════════

def _parse_wikipedia(raw: object) -> "Tuple[str, ...]":
    """Normalise the JSON ``wikipedia`` field to a tuple of strings.

    Accepts:
    - ``None`` / missing → ``()``
    - ``"https://…"`` (legacy single string) → ``("https://…",)``
    - ``["https://…", …]`` (list) → tuple of those strings
    """
    from typing import Tuple  # noqa: F401 — used in annotation only
    if raw is None:
        return ()
    if isinstance(raw, str):
        return (raw,)
    return tuple(raw)


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

    # Normalise the two accepted grapheme JSON shapes (plain list and the
    # weighted-object ``{"ipa": [...], "weights": [...]}`` form) into one
    # internal representation: plain IPA lists in ``raw["graphemes"]`` (so
    # the base-merge below and every downstream consumer keep seeing plain
    # ``list[str]``) plus a sparse own-only weights table. Weights are NOT
    # inherited (FIELD_INHERITANCE) — they come from this spec's own file
    # only — so a child pulling graphemes via ``graphemes_base`` keeps the
    # parent's IPA lists but its own (absent) weights, i.e. rank ordering.
    own_graphemes_plain, own_grapheme_weights = split_weighted_graphemes(
        raw.get("graphemes", {}) or {}
    )
    raw["graphemes"] = own_graphemes_plain

    # ensure all related languages also loaded
    parent_lang = raw.get("parent")
    # base_field_langs[field] = the code declared in the JSON's
    # "{field}_base" key, driven by FIELD_INHERITANCE's BASE_MERGE fields
    # rather than a hand-listed set of 3 — a new BASE_MERGE field picked up
    # automatically here.
    base_field_langs: Dict[str, Optional[str]] = {
        field: raw.get(f"{field}_base") for field in _BASE_MERGE_FIELDS
    }
    ancestors = raw.get("ancestors", [])
    ancestor_langs = [ancestor["code"] for ancestor in ancestors]
    # Base specs (graphemes_base etc.) MUST be loadable — they provide data.
    # Ancestor-only references are best-effort (ancestors may be proto-languages
    # that exist only as stubs or not at all).
    _base_parents = {v for v in base_field_langs.values() if v}

    for parent in (parent_lang, *base_field_langs.values(), *ancestor_langs):
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
                    for field, lang in list(base_field_langs.items()):
                        if lang == parent:
                            base_field_langs[field] = None
                            raw[f"{field}_base"] = None
                elif parent == parent_lang:
                    # Parent language is needed for ancestry but not data — tolerate
                    parent_lang = None
                # else: ancestor-only reference — silently skip

    # merge base_merge fields (graphemes, allophones, positional_graphemes)
    merged_base_fields: Dict[str, dict] = {}
    for field in _BASE_MERGE_FIELDS:
        own_value = raw.get(field, {}) or {}
        base_lang = base_field_langs.get(field)
        if base_lang and base_lang in _specs:
            merged_base_fields[field] = {
                **getattr(_specs[base_lang], field),
                **own_value,
            }
        else:
            merged_base_fields[field] = own_value
    graphemes = merged_base_fields["graphemes"]
    allophones = merged_base_fields["allophones"]
    positional_graphemes = merged_base_fields["positional_graphemes"]

    # parse ancestors
    try:
        ancestors = tuple(Ancestor(code=ancestor["code"],
                                   role=ancestor["role"],  # will auto cast to enum
                                   weight=ancestor.get("weight", 0.0),
                                   notes=ancestor.get("notes", ""))
                          for ancestor in ancestors)
    except Exception as e:
        raise ValueError(f"Failed to load ancestors for '{code}'") from e

    # Parse sandhi rules (OVERLAY_BY_ID — see _overlay_by_id / FIELD_INHERITANCE)
    own_sandhi_rules = ()
    raw_sandhi = raw.get("sandhi_rules", [])
    if raw_sandhi:
        own_sandhi_rules = tuple(
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

    # Parse allophone rules (OVERLAY_BY_ID, like sandhi_rules — see
    # AllophoneRule / FIELD_INHERITANCE). Each entry is a declarative
    # phoneme→surface rewrite; unknown keys are ignored so the schema can
    # grow without breaking older data.
    own_allophone_rules: tuple = ()
    raw_allophone = raw.get("allophone_rules", [])
    if raw_allophone:
        own_allophone_rules = tuple(
            AllophoneRule(
                id=ar["id"],
                phonemes=ar["phonemes"],
                surface=ar["surface"],
                word_initial=ar.get("word_initial"),
                word_final=ar.get("word_final"),
                stress=ar.get("stress"),
                syllable_position=ar.get("syllable_position"),
                preceded_by=ar.get("preceded_by"),
                followed_by=ar.get("followed_by"),
                preceded_by_phoneme=tuple(ar.get("preceded_by_phoneme", ())),
                followed_by_phoneme=tuple(ar.get("followed_by_phoneme", ())),
                grapheme=(tuple(ar["grapheme"])
                          if ar.get("grapheme") else None),
                notes=ar.get("notes", ""),
            )
            for ar in raw_allophone
        )

    # Resolve every OVERLAY_BY_ID field through the same structural base edge
    # (graphemes_base, else ancestry parent), id-keyed so a child overrides a
    # single inherited rule by id and appends new ones.
    _own_overlay = {
        "sandhi_rules": own_sandhi_rules,
        "allophone_rules": own_allophone_rules,
    }
    _resolved_overlay = dict(_own_overlay)
    overlay_base_lang = (base_field_langs.get("graphemes")
                         or _nearest_data_ancestor(parent_lang))
    if overlay_base_lang and overlay_base_lang in _specs:
        for field in _OVERLAY_BY_ID_FIELDS:
            _resolved_overlay[field] = _overlay_by_id(
                getattr(_specs[overlay_base_lang], field),
                _own_overlay[field],
            )
    sandhi_rules = _resolved_overlay["sandhi_rules"]
    allophone_rules = _resolved_overlay["allophone_rules"]

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
            wikipedia_url=s.get("wikipedia_url"),
            pages=s.get("pages"),
            notes=s.get("notes"),
        )
        for s in sources_raw
    )

    # Parse timespan
    timespan: Optional[TimeSpan] = None
    raw_timespan = raw.get("timespan")
    if raw_timespan and isinstance(raw_timespan, dict):
        timespan = TimeSpan(
            start_year=int(raw_timespan["start_year"]),
            end_year=int(raw_timespan["end_year"]) if raw_timespan.get("end_year") is not None else None,
        )

    # Parse the representative point for where the language is spoken
    location: Optional[Location] = None
    raw_loc = raw.get("location")
    if raw_loc and isinstance(raw_loc, dict):
        location = Location(
            latitude=float(raw_loc["latitude"]),
            longitude=float(raw_loc["longitude"]),
            source=raw_loc.get("source"),
            notes=raw_loc.get("notes", "") or "",
        )

    # Parse the official orthography standard, when the language has one
    orthography_standard: Optional[OrthographyStandard] = None
    raw_ortho = raw.get("orthography_standard")
    if raw_ortho and isinstance(raw_ortho, dict):
        orthography_standard = OrthographyStandard(
            name=raw_ortho["name"],
            authority=raw_ortho.get("authority"),
            year=int(raw_ortho["year"]) if raw_ortho.get("year") is not None else None,
            url=raw_ortho.get("url"),
            notes=raw_ortho.get("notes", "") or "",
        )

    # Parse stress rules (own-file only — not inherited through ancestry)
    stress: Optional[StressRules] = None
    raw_stress = raw.get("stress")
    if raw_stress and isinstance(raw_stress, dict):
        stress = StressRules(
            default_position=int(raw_stress.get("default_position", -2)),
            final_stress_endings=tuple(raw_stress.get("final_stress_endings", ())),
            penult_stress_endings=tuple(raw_stress.get("penult_stress_endings", ())),
            marked_vowels=tuple(raw_stress.get("marked_vowels", ())),
            stress_mark=raw_stress.get("stress_mark", "ˈ"),
            notes=raw_stress.get("notes", "") or "",
        )

    # Derive the classification path from the ancestry chain. The chain is
    # walked through ``parent``; a spec that declares its genetic parent only
    # in ``ancestors`` (PARENT role) is classified through that instead, so a
    # spec never has to be re-parented just to be classifiable.
    classification_parent = parent_lang
    if not classification_parent:
        for ancestor in ancestors:
            if ancestor.role is AncestorRole.PARENT:
                classification_parent = ancestor.code
                break
    if classification_parent and classification_parent not in _specs:
        try:
            _specs[classification_parent] = load_json_spec(classification_parent)
        except (KeyError, ValueError):
            classification_parent = None
    family_path = _derive_family_path(classification_parent)
    # An explicit ``family`` string wins over the derived path: it is the
    # escape hatch for groupings that are not genetic clades (creoles,
    # constructed languages, isolates, unclassified languages).
    family = raw.get("family") or " > ".join(family_path)

    spec = LanguageSpec(
        code=raw["code"],
        name=raw["name"],
        family=family,
        family_path=family_path,
        clade=bool(raw.get("clade", False)),
        script=raw["script"],
        graphemes=graphemes,
        phonemes=tuple(raw.get("phonemes") or ()),
        orthography_kind=OrthographyKind(raw.get("orthography_kind") or "native"),
        allophones=allophones,
        positional_graphemes=positional_graphemes or {},  # will auto cast to enum
        parent=parent_lang,
        ancestors=ancestors,
        notes=raw.get("notes", ""),
        quality=raw.get("quality", QualityTier.RESEARCH),
        script_type=raw.get("script_type", ScriptType.ALPHABET),
        inherent_vowel=raw.get("inherent_vowel"),
        iso639_3=raw.get("iso639_3"),
        glottolog_code=raw.get("glottolog_code"),
        wikidata_qid=raw.get("wikidata_qid"),
        phoible_id=raw.get("phoible_id"),
        wals_code=raw.get("wals_code"),
        sandhi_rules=sandhi_rules,
        allophone_rules=allophone_rules,
        tone_inventory=raw.get("tone_inventory"),
        sources=sources,
        wikipedia=_parse_wikipedia(raw.get("wikipedia")),
        urls=tuple(raw.get("urls") or ()),
        orthography_standard=orthography_standard,
        location=location,
        timespan=timespan,
        stress=stress,
        word_exceptions=raw.get("word_exceptions"),
        grapheme_weights=own_grapheme_weights or None,
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
