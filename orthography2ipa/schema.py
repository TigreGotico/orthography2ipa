"""Pydantic v2 validation models for orthography2ipa language specs.

These models mirror the JSON spec schema documented in ``data/SCHEMA.md`` and
the runtime dataclasses in :mod:`orthography2ipa.types`. They exist purely as a
validation layer: the runtime loader (:mod:`orthography2ipa.json_loader`) still
parses specs into the frozen dataclasses. The models here let tests and the
``orthography2ipa validate`` CLI assert that every ``data/*.json`` file is
structurally sound and free of unknown keys.

Validation is strict: every model sets ``extra='forbid'`` so unknown keys are
reported rather than silently ignored. Field validators enforce the constraints
the schema implies (non-empty codes/identifiers, ancestor weights in ``[0, 1]``,
plausible publication years).

Notes on intentional permissiveness:

- Grapheme and allophone IPA candidate lists may contain the empty string ``""``.
  An empty candidate is a meaningful value: a silent grapheme (silent ⟨h⟩,
  French word-final liaison consonants, the Indic virama deleting an inherent
  vowel). It is therefore allowed.
- A grapheme/allophone value of ``None`` is a deletion marker used during
  ``*_base`` inheritance and is allowed.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Literal, Optional, Tuple, Union

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    field_validator,
    model_validator,
)

from orthography2ipa.types import (
    AncestorRole,
    GraphemePosition,
    QualityTier,
    ScriptType,
)

# Grapheme / allophone candidate lists. ``None`` is the inheritance deletion
# marker; individual candidates may be empty strings (silent realisations).
IPACandidates = Optional[List[str]]


class _Strict(BaseModel):
    """Base config: forbid unknown keys, validate on assignment, use enum values."""

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        use_enum_values=True,
    )


class WeightedGraphemeModel(_Strict):
    """The weighted-object form of a grapheme value:
    ``{"ipa": [...], "weights": [...]}`` (see ``docs/candidate_scoring.md``).

    ``weights`` are candidate frequencies, one per ``ipa`` entry, and must
    be non-negative and sum to a positive value; the model enforces the
    length match so a malformed weighted spec fails validation rather than
    silently falling back to rank ordering at runtime."""

    ipa: List[str]
    weights: List[float]

    @field_validator("weights")
    @classmethod
    def _weights_valid(cls, v: List[float]) -> List[float]:
        if any(w < 0 for w in v):
            raise ValueError("candidate weights must be non-negative")
        if sum(v) <= 0:
            raise ValueError("candidate weights must sum to a positive value")
        return v

    @model_validator(mode="after")
    def _lengths_match(self) -> "WeightedGraphemeModel":
        if len(self.ipa) != len(self.weights):
            raise ValueError(
                f"weights length ({len(self.weights)}) must equal ipa "
                f"length ({len(self.ipa)})")
        return self


# A grapheme value is either a plain candidate list or the weighted object.
GraphemeValue = Optional[Union[List[str], WeightedGraphemeModel]]


class SourceModel(_Strict):
    """A bibliographic reference (``sources[]``). Mirrors ``LinguisticSource``."""

    id: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int
    title: str = Field(min_length=1)
    publisher: Optional[str] = None
    url: Optional[str] = None
    wikipedia_url: Optional[str] = None
    pages: Optional[str] = None
    notes: Optional[str] = None

    @field_validator("year")
    @classmethod
    def _plausible_year(cls, v: int) -> int:
        # Earliest modern descriptive phonologies + a generous future margin.
        if not (1500 <= v <= 2100):
            raise ValueError(f"implausible publication year: {v!r}")
        return v


class AncestorModel(_Strict):
    """A single ancestry link (``ancestors[]``). Mirrors ``Ancestor``."""

    code: str = Field(min_length=1)
    role: AncestorRole
    weight: float = 0.5
    notes: str = ""

    @field_validator("weight")
    @classmethod
    def _weight_in_range(cls, v: float) -> float:
        if not (0.0 <= v <= 1.0):
            raise ValueError(f"ancestor weight must be in [0.0, 1.0], got {v!r}")
        return v


class SandhiRuleModel(_Strict):
    """A cross-word-boundary phonological rule (``sandhi_rules[]``)."""

    id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    left_context: str
    right_context: str
    transform: str
    obligatory: bool = True
    notes: str = ""


class AllophoneRuleModel(_Strict):
    """A post-lexical phoneme→surface rewrite (``allophone_rules[]``).

    Mirrors :class:`~orthography2ipa.types.AllophoneRule`. Conditions are
    optional and ANDed; a bare-string ``phonemes`` is accepted."""

    id: str = Field(min_length=1)
    phonemes: Union[str, List[str]]
    surface: str
    word_initial: Optional[bool] = None
    word_final: Optional[bool] = None
    stress: Optional[Literal["stressed", "unstressed"]] = None
    syllable_position: Optional[Literal["onset", "coda", "nucleus"]] = None
    preceded_by: Optional[Literal[
        "vowel", "consonant", "front_vowel", "back_vowel", "palatal",
        "word_boundary"]] = None
    followed_by: Optional[Literal[
        "vowel", "consonant", "front_vowel", "back_vowel", "palatal",
        "word_boundary"]] = None
    preceded_by_phoneme: Optional[List[str]] = None
    followed_by_phoneme: Optional[List[str]] = None
    grapheme: Optional[List[str]] = None
    notes: str = ""


class TimeSpanModel(_Strict):
    """Attestation period (``timespan``). Mirrors ``TimeSpan``."""

    start_year: int
    end_year: Optional[int] = None

    @field_validator("end_year")
    @classmethod
    def _end_after_start(cls, v: Optional[int], info) -> Optional[int]:
        start = info.data.get("start_year")
        if v is not None and start is not None and v < start:
            raise ValueError(f"end_year {v} precedes start_year {start}")
        return v


class StressRulesModel(_Strict):
    """Declarative stress placement (``stress``). Mirrors ``StressRules``."""

    default_position: int = -2
    final_stress_endings: Optional[List[str]] = None
    penult_stress_endings: Optional[List[str]] = None
    marked_vowels: Optional[List[str]] = None
    stress_mark: str = "ˈ"
    notes: Optional[str] = None

    @field_validator("default_position")
    @classmethod
    def _position_from_end(cls, v: int) -> int:
        if v == 0 or not (-4 <= v <= 2):
            raise ValueError(
                f"default_position: negative values -1..-4 count from the end "
                f"(oxytone..4th-from-last); positive values 1..2 count from the "
                f"start (1=first syllable, 2=second); 0 is not valid; got {v!r}"
            )
        return v

    @field_validator("final_stress_endings", "penult_stress_endings",
                     "marked_vowels")
    @classmethod
    def _non_empty_entries(cls, v: Optional[List[str]]) -> Optional[List[str]]:
        if v is not None and any(not entry for entry in v):
            raise ValueError("stress rule entries must be non-empty strings")
        return v


class LanguageSpecModel(_Strict):
    """A complete language specification — one ``data/{code}.json`` file."""

    # ─── required ───────────────────────────────────────────────────
    code: str = Field(min_length=1)
    name: str = Field(min_length=1)
    family: str = Field(min_length=1)
    script: str = Field(min_length=1)

    # ─── core mappings (required per SCHEMA.md, but optional when a
    #     ``*_base`` inheritance key supplies them) ──────────────────
    graphemes: Optional[Dict[str, GraphemeValue]] = None
    allophones: Optional[Dict[str, IPACandidates]] = None

    # ─── positional overrides ───────────────────────────────────────
    positional_graphemes: Optional[
        Dict[str, Optional[Dict[GraphemePosition, List[str]]]]
    ] = None

    # ─── inheritance keys ───────────────────────────────────────────
    graphemes_base: Optional[str] = None
    allophones_base: Optional[str] = None
    positional_graphemes_base: Optional[str] = None

    # ─── ancestry ───────────────────────────────────────────────────
    parent: Optional[str] = None
    ancestors: Optional[List[AncestorModel]] = None

    # ─── metadata ───────────────────────────────────────────────────
    notes: Optional[str] = None
    quality: QualityTier = QualityTier.RESEARCH
    script_type: ScriptType = ScriptType.ALPHABET
    inherent_vowel: Optional[str] = None
    iso639_3: Optional[str] = None
    glottolog_code: Optional[str] = None
    wikidata_qid: Optional[str] = None
    phoible_id: Optional[str] = None
    wals_code: Optional[str] = None

    # ─── extended structures ────────────────────────────────────────
    sandhi_rules: Optional[List[SandhiRuleModel]] = None
    allophone_rules: Optional[List[AllophoneRuleModel]] = None
    stress: Optional[StressRulesModel] = None
    tone_inventory: Optional[Dict[str, str]] = None
    sources: Optional[List[SourceModel]] = None
    wikipedia: Optional[List[str]] = None
    urls: Optional[List[str]] = None
    timespan: Optional[TimeSpanModel] = None

    # ─── bundled-lexicon reference (consumed by load_lexicon) ────────
    lexicon_csv: Optional[str] = None

    # ─── whole-word overrides for a closed irregular set ─────────────
    word_exceptions: Optional[Dict[str, str]] = None

    @field_validator("graphemes", "allophones")
    @classmethod
    def _non_empty_keys(cls, v):
        if v is not None:
            for key in v:
                if not key:
                    raise ValueError("grapheme/allophone keys must be non-empty")
        return v


# ═══════════════════════════════════════════════════════════════════════════
# Validation helpers
# ═══════════════════════════════════════════════════════════════════════════

DATA_DIR = Path(__file__).parent / "data"


def validate_spec_file(path: Path) -> LanguageSpecModel:
    """Parse and validate a single spec JSON file.

    Raises
    ------
    json.JSONDecodeError
        If the file is not valid JSON.
    pydantic.ValidationError
        If the document violates the schema.
    """
    with Path(path).open(encoding="utf-8") as f:
        data = json.load(f)
    return LanguageSpecModel.model_validate(data)


def iter_spec_files() -> List[Path]:
    """Return all ``data/*.json`` spec files, sorted by code."""
    return sorted(DATA_DIR.glob("*.json"))


def validate_all(
    code: Optional[str] = None,
) -> Tuple[List[str], List[Tuple[str, Exception]]]:
    """Validate every spec (or one ``code``) against the schema.

    Returns
    -------
    (ok, failures)
        ``ok`` is the list of codes that validated. ``failures`` pairs each
        failing code with the raised exception.
    """
    if code is not None:
        files = [DATA_DIR / f"{code}.json"]
    else:
        files = iter_spec_files()

    ok: List[str] = []
    failures: List[Tuple[str, Exception]] = []
    for path in files:
        spec_code = path.name[: -len(".json")]
        try:
            validate_spec_file(path)
            ok.append(spec_code)
        except (ValidationError, json.JSONDecodeError, OSError) as exc:
            failures.append((spec_code, exc))
    return ok, failures


def format_failure(code: str, exc: Exception) -> str:
    """Render a validation failure as ``code.json: field.path — message`` lines."""
    lines: List[str] = []
    if isinstance(exc, ValidationError):
        for err in exc.errors():
            loc = ".".join(str(p) for p in err["loc"]) or "<root>"
            lines.append(f"{code}.json: {loc} — {err['msg']} [{err['type']}]")
    else:
        lines.append(f"{code}.json: {exc}")
    return "\n".join(lines)
