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
    SpellingDivergence,
    InventoryDistance,
    PhonologicalDistance,
    allophone_overlap,
    ancestry_similarity,
    feature_vector,
    full_distance,
    geographic_distance,
    grapheme_divergence,
    spelling_divergence,
    inventory_distance,
    orthographic_distance,
    pairwise_distances,
    phonological_distance,
    segment_distance,
    tone_distance,
)
from orthography2ipa.g2p import (
    ConfidenceBreakdown,
    G2P,
    TranscriptionResult,
    WordTranscription,
    transcribe,
)
from orthography2ipa.features import GraphemeFeatures, WordFeatures
from orthography2ipa.g2p_plugin import G2PPlugin, WordContext
from orthography2ipa.json_loader import load_lexicon
from orthography2ipa.lexicon import (
    available_lexicon_codes,
    get_lexicon,
    is_ipa_string,
    validate_lexicon_text,
)
from orthography2ipa.phonetok import (
    Candidate,
    GraphemeContext,
    IPAPath,
    PhonetokTokenizer,
    SegmentSlot,
    Token,
    TokenKind,
    TokenSequence,
)
from orthography2ipa.rescorer import LatticeRescorer, RescoreContext
from orthography2ipa.sentence import (
    Position,
    SentenceLattice,
    SentenceRescoreContext,
    SentenceRescorer,
    WordSlot,
)
from orthography2ipa.allophony import (
    AllophoneRescorer,
    compile_allophone_rescorer,
)
from orthography2ipa.registry import (
    ancestry_chain,
    available_codes,
    available_families,
    get,
    get_syllabifier,
    resolve,
)
from orthography2ipa.sandhi import SandhiEngine
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
from orthography2ipa.registry import get_rescorers, who_answers
from orthography2ipa.rescorer_plugin import RescorerPlugin
from orthography2ipa.inventory import (
    STRESS_MARKS,
    dead_allophone_rules,
    emission_inventory,
    phoneme_inventory,
    tokenize,
)
from orthography2ipa.underspecification import (
    is_underdetermined,
    mark_density,
    underdetermined_positions,
)
from orthography2ipa.stress import apply_stress_mark, detect_stress, syllabify
from orthography2ipa.syllabifier_plugin import SyllabifierPlugin
from orthography2ipa.script_distance import (
    SCRIPT_REGISTRY,
    ScriptFeatures,
    script_distance,
    script_distance_by_name,
)
from orthography2ipa.types import (
    AllophoneMap, AllophoneRule, Ancestor, AncestorRole, Grapheme2IPA,
    LanguageSpec, Location, OrthographyKind, OrthographyStandard,
    PositionalGrapheme2IPA, QualityTier,
    SandhiRule, ScriptType, StressRules,
)

__all__ = [
    "transcribe",
    "G2P",
    "ConfidenceBreakdown",
    "TranscriptionResult",
    "WordTranscription",
    "WordFeatures",
    "GraphemeFeatures",
    "get",
    "resolve",
    "ancestry_chain",
    "available_codes",
    "available_families",
    "load_lexicon",
    "get_lexicon",
    "available_lexicon_codes",
    "is_ipa_string",
    "validate_lexicon_text",
    "G2PPlugin",
    "WordContext",
    "SandhiEngine",
    "LanguageSpec",
    "Location",
    "OrthographyKind",
    "OrthographyStandard",
    "Grapheme2IPA",
    "AllophoneMap",
    "Ancestor",
    "AncestorRole",
    "PositionalGrapheme2IPA",
    "QualityTier",
    "ScriptType",
    "SandhiRule",
    "AllophoneRule",
    "AllophoneRescorer",
    "compile_allophone_rescorer",
    "StressRules",
    "get_rescorers",
    "who_answers",
    "RescorerPlugin",
    "emission_inventory",
    "phoneme_inventory",
    "tokenize",
    "dead_allophone_rules",
    "STRESS_MARKS",
    "is_underdetermined",
    "underdetermined_positions",
    "mark_density",
    "detect_stress",
    "apply_stress_mark",
    "syllabify",
    "SyllabifierPlugin",
    "get_syllabifier",
    "ScriptFeatures",
    "SCRIPT_REGISTRY",
    "script_distance",
    "script_distance_by_name",
    "PhonetokTokenizer",
    "Token",
    "TokenKind",
    "IPAPath",
    "Candidate",
    "SegmentSlot",
    "GraphemeContext",
    "TokenSequence",
    "LatticeRescorer",
    "RescoreContext",
    "Position",
    "WordSlot",
    "SentenceLattice",
    "SentenceRescorer",
    "SentenceRescoreContext",
    "segment_distance",
    "inventory_distance",
    "grapheme_divergence",
    "geographic_distance",
    "allophone_overlap",
    "phonological_distance",
    "ancestry_similarity",
    "full_distance",
    "pairwise_distances",
    "feature_vector",
    "InventoryDistance",
    "GraphemeDivergence",
    "SpellingDivergence",
    "spelling_divergence",
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
