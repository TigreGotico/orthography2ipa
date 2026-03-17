"""orthography2ipa - Linguistically motivated grapheme→IPA and allophone maps.

Quick start::

    >>> import orthography2ipa
    >>> en = orthography2ipa.get("en-GB")
    >>> en.graphemes["th"]
    ['θ', 'ð']
    >>> en.allophones["t"]
    ['t', 'tʰ', 'ɾ', 'ʔ', 't̚']

    >>> pt = orthography2ipa.get("pt-BR")
    >>> pt.graphemes["lh"]
    ['ʎ']
"""
from orthography2ipa.distance import (
    GraphemeDivergence,
    InventoryDistance,
    PhonologicalDistance,
    allophone_overlap,
    ancestry_similarity,
    feature_vector,
    full_distance,
    grapheme_divergence,
    inventory_distance,
    orthographic_distance,
    pairwise_distances,
    phonological_distance,
    segment_distance,
    tone_distance,
)
from orthography2ipa.json_loader import load_lexicon
from orthography2ipa.phonetok import IPAPath, PhonetokTokenizer, Token, TokenKind
from orthography2ipa.registry import available_codes, available_families, get
from orthography2ipa.transforms import (
    DIALECT_PROFILES,
    DialectTransform,
    IPAChainShift,
    IPALexicalRule,
    IPARule,
    apply_transform,
    available_profiles,
    debias_lisbon,
    load_clup_profile,
)
from orthography2ipa.script_distance import (
    SCRIPT_REGISTRY,
    ScriptFeatures,
    script_distance,
    script_distance_by_name,
)
from orthography2ipa.types import (
    AllophoneMap, Ancestor, AncestorRole, Grapheme2IPA, LanguageSpec,
    PositionalGrapheme2IPA, QualityTier, SandhiRule, ScriptType,
)

__all__ = [
    "get",
    "available_codes",
    "available_families",
    "load_lexicon",
    "LanguageSpec",
    "Grapheme2IPA",
    "AllophoneMap",
    "Ancestor",
    "AncestorRole",
    "PositionalGrapheme2IPA",
    "QualityTier",
    "ScriptType",
    "SandhiRule",
    "ScriptFeatures",
    "SCRIPT_REGISTRY",
    "script_distance",
    "script_distance_by_name",
    "PhonetokTokenizer",
    "Token",
    "TokenKind",
    "IPAPath",
    "segment_distance",
    "inventory_distance",
    "grapheme_divergence",
    "allophone_overlap",
    "phonological_distance",
    "ancestry_similarity",
    "full_distance",
    "pairwise_distances",
    "feature_vector",
    "InventoryDistance",
    "GraphemeDivergence",
    "PhonologicalDistance",
    # transforms
    "apply_transform",
    "debias_lisbon",
    "available_profiles",
    "DIALECT_PROFILES",
    "DialectTransform",
    "IPARule",
    "IPAChainShift",
    "IPALexicalRule",
    "load_clup_profile",
]
from orthography2ipa.version import VERSION_STR
__version__ = VERSION_STR
