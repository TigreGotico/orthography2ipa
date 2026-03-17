"""script_distance — Typological distance between writing systems.

Measures how structurally different two scripts are based on their
typological classification, directionality, case system, vowel marking
strategy, and shared historical ancestry.

Usage
─────
    >>> from orthography2ipa.script_distance import script_distance_by_name
    >>> script_distance_by_name("Latin", "Cyrillic")   # ~0.15
    >>> script_distance_by_name("Latin", "Arabic")      # ~0.55
    >>> script_distance_by_name("Latin", "Hanzi")        # ~0.90
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

from orthography2ipa.types import ScriptType

__all__ = [
    "ScriptFeatures",
    "SCRIPT_REGISTRY",
    "script_distance",
    "script_distance_by_name",
]


@dataclass(frozen=True)
class ScriptFeatures:
    """Typological feature bundle for a writing system."""

    name: str
    script_type: ScriptType
    directionality: str  # "LTR", "RTL", "TTB"
    has_case: bool
    vowel_marking: str  # "full", "partial", "inherent", "none"
    unicode_block: str
    ancestor_scripts: Tuple[str, ...] = ()


# ═══════════════════════════════════════════════════════════════════════════
# Pre-built registry of major scripts
# ═══════════════════════════════════════════════════════════════════════════

SCRIPT_REGISTRY: Dict[str, ScriptFeatures] = {
    "Latin": ScriptFeatures(
        "Latin", ScriptType.ALPHABET, "LTR", True, "full",
        "Basic Latin", ("Etruscan", "Greek", "Phoenician"),
    ),
    "Cyrillic": ScriptFeatures(
        "Cyrillic", ScriptType.ALPHABET, "LTR", True, "full",
        "Cyrillic", ("Greek", "Phoenician"),
    ),
    "Greek": ScriptFeatures(
        "Greek", ScriptType.ALPHABET, "LTR", True, "full",
        "Greek", ("Phoenician",),
    ),
    "Armenian": ScriptFeatures(
        "Armenian", ScriptType.ALPHABET, "LTR", True, "full",
        "Armenian", ("Greek", "Phoenician"),
    ),
    "Georgian": ScriptFeatures(
        "Georgian", ScriptType.ALPHABET, "LTR", False, "full",
        "Georgian", ("Greek", "Phoenician"),
    ),
    "Arabic": ScriptFeatures(
        "Arabic", ScriptType.ABJAD, "RTL", False, "partial",
        "Arabic", ("Nabataean", "Aramaic", "Phoenician"),
    ),
    "Hebrew": ScriptFeatures(
        "Hebrew", ScriptType.ABJAD, "RTL", False, "partial",
        "Hebrew", ("Aramaic", "Phoenician"),
    ),
    "Devanagari": ScriptFeatures(
        "Devanagari", ScriptType.ABUGIDA, "LTR", False, "inherent",
        "Devanagari", ("Brahmi",),
    ),
    "Bengali": ScriptFeatures(
        "Bengali", ScriptType.ABUGIDA, "LTR", False, "inherent",
        "Bengali", ("Brahmi",),
    ),
    "Tamil": ScriptFeatures(
        "Tamil", ScriptType.ABUGIDA, "LTR", False, "inherent",
        "Tamil", ("Brahmi",),
    ),
    "Telugu": ScriptFeatures(
        "Telugu", ScriptType.ABUGIDA, "LTR", False, "inherent",
        "Telugu", ("Brahmi",),
    ),
    "Kannada": ScriptFeatures(
        "Kannada", ScriptType.ABUGIDA, "LTR", False, "inherent",
        "Kannada", ("Brahmi",),
    ),
    "Gurmukhi": ScriptFeatures(
        "Gurmukhi", ScriptType.ABUGIDA, "LTR", False, "inherent",
        "Gurmukhi", ("Brahmi",),
    ),
    "Thai": ScriptFeatures(
        "Thai", ScriptType.ABUGIDA, "LTR", False, "inherent",
        "Thai", ("Brahmi",),
    ),
    "Tibetan": ScriptFeatures(
        "Tibetan", ScriptType.ABUGIDA, "LTR", False, "inherent",
        "Tibetan", ("Brahmi",),
    ),
    "Ethiopic": ScriptFeatures(
        "Ethiopic", ScriptType.ABUGIDA, "LTR", False, "inherent",
        "Ethiopic", ("South Arabian",),
    ),
    "Hangul": ScriptFeatures(
        "Hangul", ScriptType.FEATURAL, "LTR", False, "full",
        "Hangul", (),
    ),
    "Hanzi": ScriptFeatures(
        "Hanzi", ScriptType.LOGOGRAPHIC, "LTR", False, "none",
        "CJK Unified", (),
    ),
    "Kana": ScriptFeatures(
        "Kana", ScriptType.SYLLABARY, "LTR", False, "full",
        "Hiragana", (),
    ),
    "Cherokee": ScriptFeatures(
        "Cherokee", ScriptType.SYLLABARY, "LTR", False, "full",
        "Cherokee", (),
    ),
    "IPA-reconstruction": ScriptFeatures(
        "IPA-reconstruction", ScriptType.RECONSTRUCTION, "LTR", False, "full",
        "IPA Extensions", (),
    ),
}


# ═══════════════════════════════════════════════════════════════════════════
# Script type distance matrix
# ═══════════════════════════════════════════════════════════════════════════

_SCRIPT_TYPE_DISTANCE: Dict[Tuple[ScriptType, ScriptType], float] = {}


def _init_type_distances() -> None:
    """Pre-compute pairwise distances between script types."""
    types = list(ScriptType)
    # Base distances (symmetric)
    raw = {
        (ScriptType.ALPHABET, ScriptType.ABJAD): 0.3,
        (ScriptType.ALPHABET, ScriptType.ABUGIDA): 0.4,
        (ScriptType.ALPHABET, ScriptType.SYLLABARY): 0.5,
        (ScriptType.ALPHABET, ScriptType.FEATURAL): 0.3,
        (ScriptType.ALPHABET, ScriptType.LOGOGRAPHIC): 0.9,
        (ScriptType.ALPHABET, ScriptType.MIXED): 0.7,
        (ScriptType.ABJAD, ScriptType.ABUGIDA): 0.4,
        (ScriptType.ABJAD, ScriptType.SYLLABARY): 0.6,
        (ScriptType.ABJAD, ScriptType.FEATURAL): 0.5,
        (ScriptType.ABJAD, ScriptType.LOGOGRAPHIC): 0.9,
        (ScriptType.ABJAD, ScriptType.MIXED): 0.7,
        (ScriptType.ABUGIDA, ScriptType.SYLLABARY): 0.4,
        (ScriptType.ABUGIDA, ScriptType.FEATURAL): 0.5,
        (ScriptType.ABUGIDA, ScriptType.LOGOGRAPHIC): 0.8,
        (ScriptType.ABUGIDA, ScriptType.MIXED): 0.6,
        (ScriptType.SYLLABARY, ScriptType.FEATURAL): 0.5,
        (ScriptType.SYLLABARY, ScriptType.LOGOGRAPHIC): 0.7,
        (ScriptType.SYLLABARY, ScriptType.MIXED): 0.4,
        (ScriptType.FEATURAL, ScriptType.LOGOGRAPHIC): 0.8,
        (ScriptType.FEATURAL, ScriptType.MIXED): 0.6,
        (ScriptType.LOGOGRAPHIC, ScriptType.MIXED): 0.3,
        # RECONSTRUCTION is a meta-script (IPA phonological notation).
        # Low distance to alphabets (both represent segments), moderate to others.
        (ScriptType.RECONSTRUCTION, ScriptType.ALPHABET): 0.1,
        (ScriptType.RECONSTRUCTION, ScriptType.ABJAD): 0.3,
        (ScriptType.RECONSTRUCTION, ScriptType.ABUGIDA): 0.3,
        (ScriptType.RECONSTRUCTION, ScriptType.SYLLABARY): 0.5,
        (ScriptType.RECONSTRUCTION, ScriptType.FEATURAL): 0.3,
        (ScriptType.RECONSTRUCTION, ScriptType.LOGOGRAPHIC): 0.8,
        (ScriptType.RECONSTRUCTION, ScriptType.MIXED): 0.6,
    }
    for a in types:
        _SCRIPT_TYPE_DISTANCE[(a, a)] = 0.0
    for (a, b), d in raw.items():
        _SCRIPT_TYPE_DISTANCE[(a, b)] = d
        _SCRIPT_TYPE_DISTANCE[(b, a)] = d


_init_type_distances()


# ═══════════════════════════════════════════════════════════════════════════
# Distance functions
# ═══════════════════════════════════════════════════════════════════════════

def script_distance(a: ScriptFeatures, b: ScriptFeatures) -> float:
    """Combined script distance in [0.0, 1.0].

    Components (weighted):
    - Script type distance (0.40)
    - Directionality mismatch (0.15)
    - Vowel marking similarity (0.15)
    - Case system mismatch (0.05)
    - Shared ancestor bonus (0.25)
    """
    if a.name == b.name:
        return 0.0

    # Script type distance
    type_d = _SCRIPT_TYPE_DISTANCE.get(
        (a.script_type, b.script_type), 0.5
    )

    # Directionality
    dir_d = 0.0 if a.directionality == b.directionality else 1.0

    # Vowel marking
    _vm_order = {"full": 0, "partial": 1, "inherent": 2, "none": 3}
    va = _vm_order.get(a.vowel_marking, 2)
    vb = _vm_order.get(b.vowel_marking, 2)
    vowel_d = abs(va - vb) / 3.0

    # Case
    case_d = 0.0 if a.has_case == b.has_case else 1.0

    # Shared ancestor bonus
    set_a = set(a.ancestor_scripts)
    set_b = set(b.ancestor_scripts)
    if set_a and set_b:
        shared = set_a & set_b
        union = set_a | set_b
        ancestor_sim = len(shared) / len(union)
    elif not set_a and not set_b:
        ancestor_sim = 0.0
    else:
        ancestor_sim = 0.0

    ancestor_d = 1.0 - ancestor_sim

    combined = (
        0.40 * type_d
        + 0.15 * dir_d
        + 0.15 * vowel_d
        + 0.05 * case_d
        + 0.25 * ancestor_d
    )
    return min(max(combined, 0.0), 1.0)


def script_distance_by_name(a: str, b: str) -> float:
    """Convenience: look up scripts by name and compute distance.

    Raises KeyError if a script name is not in SCRIPT_REGISTRY.
    """
    return script_distance(SCRIPT_REGISTRY[a], SCRIPT_REGISTRY[b])
