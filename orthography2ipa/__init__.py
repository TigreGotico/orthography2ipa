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
    pairwise_distances,
    phonological_distance,
    segment_distance,
)
from orthography2ipa.phonetok import IPAPath, PhonetokTokenizer, Token, TokenKind
from orthography2ipa.registry import available_codes, available_families, get
from orthography2ipa.types import (
    AllophoneMap, Ancestor, AncestorRole, Grapheme2IPA, LanguageSpec,
    PositionalGrapheme2IPA,
)

__all__ = [
    "get",
    "available_codes",
    "available_families",
    "LanguageSpec",
    "Grapheme2IPA",
    "AllophoneMap",
    "Ancestor",
    "AncestorRole",
    "PositionalGrapheme2IPA",
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
]
__version__ = "0.1.0"
