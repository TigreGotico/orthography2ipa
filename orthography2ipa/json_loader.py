"""Load ``LanguageSpec`` objects from the JSON files in ``data/``.

Resolves the ``*_base`` inheritance edges. ``data/SCHEMA.md`` is the schema.
"""
from __future__ import annotations

import json
import warnings
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from orthography2ipa.types import (
    AllophoneRule,
    Ancestor,
    AncestorRole,
    AuditConclusion,
    AuditRecord,
    ClosedHiatus,
    FinalDiphthongs,
    FIELD_INHERITANCE,
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
    ToneRules,
    TimeSpan,
    ValidCeiling,
)
from orthography2ipa.positional import normalize_ending_value
from orthography2ipa.version import VERSION_MAJOR
from orthography2ipa.weights import split_weighted_graphemes

_BASE_SCALAR_FIELDS: tuple = tuple(
    f for f, mode in FIELD_INHERITANCE.items()
    if mode is InheritanceMode.BASE_SCALAR
)

_BASE_MERGE_FIELDS: tuple = tuple(
    f for f, mode in FIELD_INHERITANCE.items() if mode is InheritanceMode.BASE_MERGE
)

# Id-keyed fields have no ``*_base`` key: they follow ``graphemes_base``,
# else the nearest data ancestor on ``inherits``.
_OVERLAY_BY_ID_FIELDS: tuple = tuple(
    f for f, mode in FIELD_INHERITANCE.items() if mode is InheritanceMode.OVERLAY_BY_ID
)


def _nearest_data_ancestor(code: Optional[str]) -> Optional[str]:
    """The nearest non-clade spec on the ``inherits`` chain of *code*, itself included."""
    seen = set()
    while code and code in _specs and code not in seen:
        seen.add(code)
        spec = _specs[code]
        if not spec.clade:
            return code
        code = spec.inherits
    return None


def _derive_family_path(parent_code: Optional[str]) -> Tuple[str, ...]:
    """Return the classification path implied by *parent_code*'s chain.

    The path is the names of the clade nodes on the ancestry chain, broadest
    first. Each spec's own ``family_path`` already holds its ancestors' clades,
    so one step of recursion is enough.
    """
    if not parent_code or parent_code not in _specs:
        return ()
    parent = _specs[parent_code]
    if parent.clade:
        return parent.family_path + (parent.name,)
    return parent.family_path


def _overlay_by_id(base_items: tuple, own_items: tuple) -> tuple:
    """*base_items* with each own item replacing the base item of its ``id`` in
    place, and own items with a new ``id`` appended."""
    merged: List = list(base_items)
    index = {item.id: i for i, item in enumerate(merged)}
    for item in own_items:
        if item.id in index:
            merged[index[item.id]] = item
        else:
            index[item.id] = len(merged)
            merged.append(item)
    return tuple(merged)


_DATA_DIR = Path(__file__).parent / "data"
_index: Dict[str, Path] = {}
_specs: Dict[str, LanguageSpec] = {}


def _index_files():
    for lang_file in _DATA_DIR.glob("*.json"):
        lang_code = lang_file.name.split(".json")[0]
        _index[lang_code] = lang_file


def _parse_wikipedia(raw: object) -> Tuple[str, ...]:
    """The ``wikipedia`` field, a string or a list, as a tuple."""
    if raw is None:
        return ()
    if isinstance(raw, str):
        return (raw,)
    return tuple(raw)


def load_json_spec(code: str) -> LanguageSpec:
    """Load the spec of the file key *code*, resolving inheritance.

    Raises ``KeyError`` for an unknown key and ``ValueError`` for bad data.
    """
    if code in _specs:
        return _specs[code]

    if code not in _index:
        raise KeyError(f"unsupported language: '{code}.json' not found. Available: {set(_index.keys())}")
    lang_file: Path = _index[code]
    with lang_file.open() as f:
        raw = json.load(f)

    # Weights are not inherited: a child keeps the base IPA lists in rank order.
    own_graphemes_plain, own_grapheme_weights = split_weighted_graphemes(
        raw.get("graphemes", {}) or {}
    )
    raw["graphemes"] = own_graphemes_plain

    if "parent" in raw:
        if "inherits" in raw:
            raise ValueError(f"spec '{code}' sets both 'parent' and 'inherits'; keep 'inherits'")
        warnings.warn(
            f"the 'parent' key of spec '{code}' is deprecated and will be removed in "
            f"{VERSION_MAJOR + 1}.0.0; rename it to 'inherits'.",
            DeprecationWarning,
            stacklevel=2,
        )
        raw["inherits"] = raw.pop("parent")

    parent_lang = raw.get("inherits")
    base_field_langs: Dict[str, Optional[str]] = {
        field: raw.get(f"{field}_base") for field in _BASE_MERGE_FIELDS
    }
    # Positional graphemes refine the grapheme table, so they follow
    # ``graphemes_base`` by default. ``allophones_base`` has no default.
    if base_field_langs.get("positional_graphemes") is None:
        base_field_langs["positional_graphemes"] = base_field_langs.get("graphemes")

    ancestors = raw.get("ancestors", [])
    ancestor_langs = [ancestor["code"] for ancestor in ancestors]
    # A base spec must load; an ancestor-only reference may be missing.
    _base_parents = {v for v in base_field_langs.values() if v}

    for parent in (parent_lang, *base_field_langs.values(), *ancestor_langs):
        if parent == code:
            continue
        if parent and parent not in _specs:
            try:
                _specs[parent] = load_json_spec(parent)
            except (KeyError, ValueError) as e:
                if parent in _base_parents:
                    warnings.warn(f"Could not load base '{parent}' (requested by '{code}'): {e}")
                    for field, lang in list(base_field_langs.items()):
                        if lang == parent:
                            base_field_langs[field] = None
                            raw[f"{field}_base"] = None
                elif parent == parent_lang:
                    parent_lang = None

    merged_base_fields: Dict[str, dict] = {}
    for field in _BASE_MERGE_FIELDS:
        own_value = raw.get(field, {}) or {}
        base_lang = base_field_langs.get(field)
        if base_lang and base_lang in _specs:
            merged_base_fields[field] = {
                **(getattr(_specs[base_lang], field) or {}),
                **own_value,
            }
        else:
            merged_base_fields[field] = own_value
    # BASE_SCALAR fields follow graphemes_base, transitively.
    base_scalars: Dict[str, object] = {}
    _grapheme_base_lang = base_field_langs.get("graphemes")
    for field in _BASE_SCALAR_FIELDS:
        if field in raw:
            base_scalars[field] = raw[field]
        elif _grapheme_base_lang and _grapheme_base_lang in _specs:
            base_scalars[field] = getattr(_specs[_grapheme_base_lang], field)

    graphemes = merged_base_fields["graphemes"]
    allophones = merged_base_fields["allophones"]
    positional_graphemes = merged_base_fields["positional_graphemes"]

    # Fail at load, not on the first word that ends that way.
    for ending, value in (merged_base_fields["grammatical_endings"] or {}).items():
        try:
            normalize_ending_value(value)
        except ValueError as e:
            raise ValueError(
                f"'{code}': grammatical_endings[{ending!r}]: {e}") from e

    try:
        ancestors = tuple(Ancestor(code=ancestor["code"],
                                   role=ancestor["role"],
                                   weight=ancestor.get("weight", 0.0),
                                   notes=ancestor.get("notes", ""))
                          for ancestor in ancestors)
    except Exception as e:
        raise ValueError(f"Failed to load ancestors for '{code}'") from e

    own_sandhi_rules = ()
    raw_sandhi = raw.get("sandhi_rules", [])
    if raw_sandhi:
        own_sandhi_rules = tuple(
            SandhiRule(
                id=sr["id"],
                name=sr["name"],
                left_context=sr["left_context"],
                right_context=sr["right_context"],
                transform=sr.get("transform"),
                right_transform=sr.get("right_transform"),
                obligatory=sr.get("obligatory", True),
                notes=sr.get("notes", ""),
            )
            for sr in raw_sandhi
        )

    # Unknown keys are ignored.
    own_allophone_rules: tuple = ()
    raw_allophone = raw.get("allophone_rules", [])
    if raw_allophone:
        own_allophone_rules = tuple(
            AllophoneRule(
                id=ar["id"],
                phonemes=ar["phonemes"],
                surface=ar.get("surface", ""),
                append=ar.get("append", ""),
                word_initial=ar.get("word_initial"),
                word_final=ar.get("word_final"),
                stress=ar.get("stress"),
                syllable_position=ar.get("syllable_position"),
                preceded_by=ar.get("preceded_by"),
                followed_by=ar.get("followed_by"),
                preceded_by_2=ar.get("preceded_by_2"),
                followed_by_2=ar.get("followed_by_2"),
                preceded_by_3=ar.get("preceded_by_3"),
                followed_by_3=ar.get("followed_by_3"),
                preceded_by_phoneme=tuple(ar.get("preceded_by_phoneme", ())),
                followed_by_phoneme=tuple(ar.get("followed_by_phoneme", ())),
                preceded_by_grapheme=tuple(
                    ar.get("preceded_by_grapheme", ())),
                followed_by_grapheme=tuple(
                    ar.get("followed_by_grapheme", ())),
                followed_by_grapheme_not=tuple(
                    ar.get("followed_by_grapheme_not", ())),
                word_contains_grapheme=tuple(
                    ar.get("word_contains_grapheme", ())),
                word_contains_grapheme_not=tuple(
                    ar.get("word_contains_grapheme_not", ())),
                preceded_by_phoneme_2=tuple(ar.get("preceded_by_phoneme_2", ())),
                followed_by_phoneme_2=tuple(ar.get("followed_by_phoneme_2", ())),
                followed_by_phoneme_3=tuple(ar.get("followed_by_phoneme_3") or ()),
                preceded_by_surface_phoneme_2=tuple(
                    ar.get("preceded_by_surface_phoneme_2", ())),
                requires_other_nucleus=ar.get("requires_other_nucleus"),
                followed_by_nucleus=ar.get("followed_by_nucleus"),
                grapheme=(tuple(ar["grapheme"])
                          if ar.get("grapheme") else None),
                word=(tuple(ar["word"])
                      if ar.get("word") else None),
                notes=ar.get("notes", ""),
                mutates_neighbor=ar.get("mutates_neighbor"),
                mutates_neighbor_side=ar.get("mutates_neighbor_side"),
            )
            for ar in raw_allophone
        )

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

    sources_raw = raw.get("sources", [])
    sources = tuple(
        LinguisticSource(
            id=s["id"],
            author=s["author"],
            year=s["year"],
            title=s["title"],
            publisher=s.get("publisher"),
            url=s.get("url"),
            doi=s.get("doi"),
            wikipedia_url=s.get("wikipedia_url"),
            pages=s.get("pages"),
            notes=s.get("notes"),
        )
        for s in sources_raw
    )

    timespan: Optional[TimeSpan] = None
    raw_timespan = raw.get("timespan")
    if raw_timespan and isinstance(raw_timespan, dict):
        timespan = TimeSpan(
            start_year=int(raw_timespan["start_year"]),
            end_year=int(raw_timespan["end_year"]) if raw_timespan.get("end_year") is not None else None,
        )

    location: Optional[Location] = None
    raw_loc = raw.get("location")
    if raw_loc and isinstance(raw_loc, dict):
        location = Location(
            latitude=float(raw_loc["latitude"]),
            longitude=float(raw_loc["longitude"]),
            source=raw_loc.get("source"),
            notes=raw_loc.get("notes", "") or "",
        )

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

    # A fold is measured against one gold, so ceilings are keyed by dataset.
    valid_ceiling: Optional[Dict[str, ValidCeiling]] = None
    raw_ceiling = raw.get("valid_ceiling")
    if raw_ceiling:
        if not isinstance(raw_ceiling, dict):
            raise ValueError(
                f"{code}: valid_ceiling must be an object mapping dataset "
                f"name -> {{per, folded, citation}}")
        if "per" in raw_ceiling or "folded" in raw_ceiling:
            raise ValueError(
                f"{code}: valid_ceiling uses the old language-scoped shape "
                f"(bare per/folded/citation). A fold is measured against one "
                f"gold's notation conventions, so it must be keyed by "
                f"dataset name, e.g. {{\"wikipron\": {{\"per\": ..., "
                f"\"folded\": ..., \"citation\": ...}}}} (issue #1350)")
        valid_ceiling = {
            dataset_name: ValidCeiling(
                per=float(raw_c["per"]),
                folded=raw_c["folded"],
                citation=raw_c["citation"],
            )
            for dataset_name, raw_c in raw_ceiling.items()
        }

    audit: Optional[Dict[str, AuditRecord]] = None
    raw_audit = raw.get("audit")
    if raw_audit:
        if not isinstance(raw_audit, dict):
            raise ValueError(
                f"{code}: audit must be an object mapping dataset "
                f"name -> {{conclusion, measured, reference}}")
        audit = {
            dataset_name: AuditRecord(
                conclusion=AuditConclusion(raw_a["conclusion"]),
                measured=raw_a["measured"],
                reference=raw_a["reference"],
            )
            for dataset_name, raw_a in raw_audit.items()
        }

    # Stress (BASE_BLOCK): the own block wins whole. Else the block of
    # graphemes_base, else of the nearest data ancestor when the child's
    # iso639_3 is unset or the same (el-CY under el, not aoa under pt-PT).
    # ``"stress": false`` takes no block.
    stress: Optional[StressRules] = None
    raw_tone = raw.get("tone_rules")
    tone_rules = None
    if raw_tone and isinstance(raw_tone, dict):
        tone_rules = ToneRules(
            classes=dict(raw_tone.get("classes") or {}),
            marks=dict(raw_tone.get("marks") or {}),
            tones=dict(raw_tone.get("tones") or {}),
            table={k: {s: dict(m) for s, m in v.items()}
                   for k, v in (raw_tone.get("table") or {}).items()},
            dead_codas=tuple(raw_tone.get("dead_codas") or ()),
            no_mark=raw_tone.get("no_mark", "none"),
            notes=raw_tone.get("notes"),
        )

    raw_stress = raw.get("stress")
    if raw_stress and isinstance(raw_stress, dict):
        raw_hiatus = raw_stress.get("closed_hiatus")
        raw_final = raw_stress.get("final_diphthongs")
        stress = StressRules(
            default_position=int(raw_stress.get("default_position", -2)),
            final_stress_endings=tuple(raw_stress.get("final_stress_endings", ())),
            penult_stress_endings=tuple(raw_stress.get("penult_stress_endings", ())),
            antepenult_stress_endings=tuple(
                raw_stress.get("antepenult_stress_endings", ())),
            unstressed_prefixes=tuple(
                raw_stress.get("unstressed_prefixes", ())),
            schwa_rimes=tuple(raw_stress.get("schwa_rimes", ())),
            marked_vowels=tuple(raw_stress.get("marked_vowels", ())),
            stress_mark=raw_stress.get("stress_mark", "ˈ"),
            accent2_mark=raw_stress.get("accent2_mark", ""),
            accent2_final_letters=tuple(raw_stress.get("accent2_final_letters", ())),
            diphthongs=tuple(raw_stress.get("diphthongs", ())),
            ipa_diphthongs=(tuple(raw_stress["ipa_diphthongs"])
                            if "ipa_diphthongs" in raw_stress else None),
            closed_hiatus=(ClosedHiatus(
                pairs=tuple(raw_hiatus.get("pairs", ())),
                onsets=tuple(raw_hiatus.get("onsets", ())),
                codas=tuple(raw_hiatus.get("codas", ())),
                atonic_onsets=tuple(raw_hiatus.get("atonic_onsets", ())))
                if raw_hiatus else None),
            final_diphthongs=(FinalDiphthongs(
                diphthongs=tuple(raw_final.get("diphthongs", ())),
                finals=tuple(raw_final.get("finals", ())))
                if raw_final else None),
            tonic_after_diphthong=tuple(
                raw_stress.get("tonic_after_diphthong", ())),
            vowel_letters=tuple(raw_stress.get("vowel_letters", ())),
            quantity_sensitive=bool(raw_stress.get("quantity_sensitive", False)),
            superheavy_final_attracts=bool(
                raw_stress.get("superheavy_final_attracts", True)),
            max_onset=int(raw_stress.get("max_onset", 1)),
            max_onset_declared="max_onset" in raw_stress,
            onset_clusters=tuple(raw_stress.get("onset_clusters", ())),
            constrain_mark_onsets=bool(
                raw_stress.get("constrain_mark_onsets", True)),
            cliticless_words=tuple(raw_stress.get("cliticless_words", ())),
            coda_liquid_capture=bool(
                raw_stress.get("coda_liquid_capture", False)),
            secondary_stress=str(raw_stress.get("secondary_stress", "") or ""),
            compound_stress=str(raw_stress.get("compound_stress", "") or ""),
            iambic_length=bool(raw_stress.get("iambic_length", False)),
            source=str(raw_stress.get("source", "rules")),
            notes=raw_stress.get("notes", "") or "",
        )
    elif raw_stress is not False:
        stress_base = base_field_langs.get("graphemes")
        if not stress_base:
            data_parent = _nearest_data_ancestor(parent_lang)
            if data_parent and raw.get("iso639_3") in (
                    None, _specs[data_parent].iso639_3):
                stress_base = data_parent
        if stress_base and stress_base in _specs:
            stress = _specs[stress_base].stress

    # With no ``inherits``, the PARENT-role ancestor classifies the spec.
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
    # An explicit ``family`` names a grouping that is not a clade.
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
        positional_graphemes=positional_graphemes or {},
        inherits=parent_lang,
        ancestors=ancestors,
        notes=raw.get("notes", ""),
        quality=raw.get("quality", QualityTier.RESEARCH),
        script_type=raw.get("script_type", ScriptType.ALPHABET),
        inherent_vowel=raw.get("inherent_vowel"),
        plugins={
            stage: ((names,) if isinstance(names, str) else tuple(names))
            for stage, names in (raw.get("plugins", {}) or {}).items()
        },
        optional_marks=tuple(raw.get("optional_marks", ()) or ()),
        fold_diacritics=tuple(raw.get("fold_diacritics", ()) or ()),
        vowel_graphemes=tuple(raw.get("vowel_graphemes", ()) or ()),
        dependent_vowels=tuple(raw.get("dependent_vowels", ()) or ()),
        preposed_vowels=tuple(raw.get("preposed_vowels", ()) or ()),
        trailing_vowel_axis_digraphs=tuple(
            raw.get("trailing_vowel_axis_digraphs", ()) or ()),
        prevocalic_glide_backoff=tuple(
            raw.get("prevocalic_glide_backoff", ()) or ()),
        coda_no_inherent_vowel=bool(raw.get("coda_no_inherent_vowel", False)),
        consonant_nuclei=raw.get("consonant_nuclei"),
        codas=tuple(raw.get("codas") or ()),
        inherent_vowel_final=raw.get("inherent_vowel_final"),
        virama_final_vowel=raw.get("virama_final_vowel"),
        consonant_marks=tuple(raw.get("consonant_marks", ()) or ()),
        collapse_geminates=bool(raw.get("collapse_geminates", False)),
        doubled_letters_geminate=bool(
            raw.get("doubled_letters_geminate", True)),
        constrain_onsets=bool(base_scalars.get("constrain_onsets", False)),
        word_internal_apostrophe=bool(
            base_scalars.get("word_internal_apostrophe", False)),
        apostrophe_elision=bool(base_scalars.get("apostrophe_elision", False)),
        iso639_3=raw.get("iso639_3"),
        phoible_id=raw.get("phoible_id"),
        wals_code=raw.get("wals_code"),
        sandhi_rules=sandhi_rules,
        allophone_rules=allophone_rules,
        allophone_passes=int(raw.get("allophone_passes", 1)),
        tone_rules=tone_rules,
        tone_inventory=raw.get("tone_inventory"),
        tone_marks_syllable_final=bool(
            raw.get("tone_marks_syllable_final", False)),
        sources=sources,
        wikipedia=_parse_wikipedia(raw.get("wikipedia")),
        urls=tuple(raw.get("urls") or ()),
        orthography_standard=orthography_standard,
        location=location,
        timespan=timespan,
        valid_ceiling=valid_ceiling,
        audit=audit,
        stress=stress,
        word_exceptions=merged_base_fields["word_exceptions"] or None,
        grammatical_endings=merged_base_fields["grammatical_endings"] or None,
        grapheme_weights=own_grapheme_weights or None,
    )

    _specs[code] = spec
    return spec


def load_all_json_specs() -> Dict[str, LanguageSpec]:
    """Load every spec in the data directory; a bad file only warns."""
    for code in _index:
        if code not in _specs:
            try:
                _specs[code] = load_json_spec(code)
            except (KeyError, ValueError) as e:
                warnings.warn(f"Failed to load '{code}': {e}")
    return _specs


def available_json_codes() -> List[str]:
    """Return sorted list of all language codes with JSON data files."""
    return sorted(_index.keys())

_index_files()
