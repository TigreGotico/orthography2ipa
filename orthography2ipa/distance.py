"""distance — Phonological distance metrics between languages.

Measures how "far apart" two languages are based on their phonological
inventories, grapheme-to-IPA mappings, and allophone systems.

Architecture
────────────
1. **Distinctive features**: Every IPA segment is decomposed into a
   binary/ternary feature vector covering place, manner, voicing,
   vowel quality, etc.  This is the foundation for all distance metrics.

2. **Segment distance**: The phonetic distance between any two IPA
   segments = normalised Hamming distance on their feature vectors.

3. **Inventory distance**: Comparison of two phoneme inventories using
   (a) Jaccard index on raw phoneme sets, (b) feature-weighted distance
   via optimal bipartite matching (Hungarian algorithm approximation).

4. **Grapheme divergence**: For languages sharing a script, measures
   how differently the same graphemes map to IPA.  High divergence =
   same letters, very different sounds (e.g. Latin ⟨c⟩=[k] vs French
   ⟨c⟩=[s,k]).

5. **Allophone overlap**: How much two languages' allophone systems
   share surface realisations.

6. **Combined phylogenetic distance**: Weighted combination providing
   a single scalar estimate of overall phonological relatedness.

Usage
─────
    >>> from orthography2ipa import get
    >>> from orthography2ipa.distance import (
    ...     segment_distance, inventory_distance, grapheme_divergence,
    ...     phonological_distance, feature_vector,
    ... )
    >>> segment_distance("p", "b")      # voicing difference only
    0.0625
    >>> segment_distance("p", "a")      # consonant vs vowel
    0.75
    >>> inventory_distance(get("es-ES"), get("pt-BR"))
    InventoryDistance(jaccard=0.23, ...)
    >>> phonological_distance(get("la"), get("it-IT"))
    PhonologicalDistance(combined=0.31, ...)
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Set, Tuple

from orthography2ipa.feats import NUM_FEATURES, phonetic_distance, vectorize_phones
from orthography2ipa.types import LanguageSpec

__all__ = [
    "Feature",
    "FeatureVector",
    #  "SegmentDistance",
    "InventoryDistance",
    "GraphemeDivergence",
    "PhonologicalDistance",
    "feature_vector",
    "segment_distance",
    "inventory_distance",
    "grapheme_divergence",
    "allophone_overlap",
    "phonological_distance",
    "pairwise_distances",
    "ancestry_similarity",
    "full_distance",
    "tone_distance",
    "orthographic_distance",
]

# ═══════════════════════════════════════════════════════════════════════════
# Distinctive feature system
# ═══════════════════════════════════════════════════════════════════════════
#
# We use 21-feature SPE/IPA system as the canonical source for phonetic feature vectors and segment distances.
#
#   - 21 distinctive features:
#       syllabic, sonorant, consonantal, continuant, delayed_release,
#       lateral, nasal, strident, voice, spread_glottis, constricted_glottis,
#       anterior, coronal, distributed, labial, high, low, back, round,
#       tense, long
#
#   - Linguistically weighted distance (major class features 7× heavier)
#   - Native diacritic/modifier handling (ː, ˤ, ˞, ̻)
#   - Vowel/consonant-aware scoring
#

Feature = str
FeatureVector = Tuple[float, ...]

_FEATURE_NAMES: Tuple[Feature, ...] = (
    "syllabic",  # 0
    "sonorant",  # 1
    "consonantal",  # 2
    "continuant",  # 3
    "delayed_release",  # 4
    "lateral",  # 5
    "nasal",  # 6
    "strident",  # 7
    "voice",  # 8
    "spread_glottis",  # 9
    "constricted_glottis",  # 10
    "anterior",  # 11
    "coronal",  # 12
    "distributed",  # 13
    "labial",  # 14
    "high",  # 15
    "low",  # 16
    "back",  # 17
    "round",  # 18
    "tense",  # 19
    "long",  # 20
    "click",  # 21
    "nasal_vowel",  # 22
)

_NEUTRAL: FeatureVector = tuple(0.5 for _ in range(NUM_FEATURES))


def _pm_vec_to_floats(vec: List) -> FeatureVector:
    """Convert True/False/None vector to 0.0/1.0/0.5 floats."""
    return tuple(
        1.0 if v is True else (0.0 if v is False else 0.5)
        for v in vec
    )


# ═══════════════════════════════════════════════════════════════════════════
# Feature lookup
# ═══════════════════════════════════════════════════════════════════════════

def feature_vector(segment: str) -> FeatureVector:
    """Return the 21-element distinctive feature vector for an IPA *segment*.

    handles composite phones (diacritics,  modifiers like ˤ ˞ ː) natively.
    Returns the neutral vector (all 0.5)
    if the segment is unknown, so distance calculations degrade gracefully.
    """
    if not segment or segment == "∅":
        return _NEUTRAL
    try:
        return _pm_vec_to_floats(vectorize_phones(segment))
    except (ValueError, KeyError):
        # Fallback: try stripping common combining marks
        stripped = segment
        for diac in ("̃", "̥", "̩", "̪", "̻", "̺", "̝", "̞", "̈", "̊", "̆",
                     "ʰ", "ʷ", "ʱ", "ˤ", "ˠ", "ʲ", "ˑ", "ː"):
            stripped = stripped.replace(diac, "")
        if stripped and stripped != segment:
            try:
                return _pm_vec_to_floats(vectorize_phones(stripped))
            except (ValueError, KeyError):
                pass
        return _NEUTRAL


def feature_names() -> Tuple[str, ...]:
    """Return the tuple of feature names (21 features)."""
    return _FEATURE_NAMES


# ═══════════════════════════════════════════════════════════════════════════
# Segment-level distance
# ═══════════════════════════════════════════════════════════════════════════

def segment_distance(seg_a: str, seg_b: str) -> float:
    """Phonetic distance between two IPA segments, normalised to [0.0, 1.0].

    Uses a weighted feature distance, which gives higher
    weight to major-class features (syllabic, sonorant, consonantal)
    and lower weight to minor features (strident, distributed, long).

    Vowel↔consonant mismatches always return 1.0.
    """
    if seg_a == seg_b:
        return 0.0
    if not seg_a or not seg_b or seg_a == "∅" or seg_b == "∅":
        return 1.0
    try:
        d = phonetic_distance(seg_a, seg_b)
        # returns 0–1 for vowels, 0–2 for consonants.
        # Normalise to [0, 1].
        return min(d, 1.0)
    except (ValueError, KeyError):
        # Fallback to feature-vector Hamming distance
        va = feature_vector(seg_a)
        vb = feature_vector(seg_b)
        diff = sum(abs(a - b) for a, b in zip(va, vb))
        return diff / NUM_FEATURES


# ═══════════════════════════════════════════════════════════════════════════
# Inventory-level distance
# ═══════════════════════════════════════════════════════════════════════════

def _extract_phonemes(spec: LanguageSpec) -> Set[str]:
    """Extract the set of unique IPA phonemes from a language spec."""
    phonemes: Set[str] = set()
    for ipa_list in spec.graphemes.values():
        for ipa in ipa_list:
            if ipa and ipa != "":
                phonemes.add(ipa)
    return phonemes


def _extract_allophones(spec: LanguageSpec) -> Set[str]:
    """Extract the set of all surface realisations."""
    phones: Set[str] = set()
    for allo_list in spec.allophones.values():
        for allo in allo_list:
            if allo and allo not in ("∅", ""):
                phones.add(allo)
    return phones


@dataclass(frozen=True)
class InventoryDistance:
    """Result of comparing two phoneme inventories."""
    jaccard: float
    """Jaccard distance (1 - |A∩B|/|A∪B|) on raw phoneme sets."""
    feature_mean: float
    """Mean minimum feature distance (for each phoneme in A, find closest
    in B; average over both directions)."""
    size_a: int
    """Number of phonemes in language A."""
    size_b: int
    """Number of phonemes in language B."""
    shared: int
    """Number of phonemes in common."""

    def __repr__(self) -> str:
        return (
            f"InventoryDistance(jaccard={self.jaccard:.3f}, "
            f"feature={self.feature_mean:.3f}, "
            f"shared={self.shared}/{max(self.size_a, self.size_b)})"
        )


def inventory_distance(spec_a: LanguageSpec, spec_b: LanguageSpec) -> InventoryDistance:
    """Compare the phoneme inventories of two languages."""
    set_a = _extract_phonemes(spec_a)
    set_b = _extract_phonemes(spec_b)

    shared = set_a & set_b
    union = set_a | set_b
    jaccard = 1.0 - (len(shared) / len(union)) if union else 0.0

    # Feature-based: mean minimum distance (asymmetric, then average)
    def _mean_min_dist(src: Set[str], tgt: Set[str]) -> float:
        if not src or not tgt:
            return 1.0
        total = 0.0
        for s in src:
            min_d = min(segment_distance(s, t) for t in tgt)
            total += min_d
        return total / len(src)

    fwd = _mean_min_dist(set_a, set_b)
    bwd = _mean_min_dist(set_b, set_a)

    return InventoryDistance(
        jaccard=jaccard,
        feature_mean=(fwd + bwd) / 2,
        size_a=len(set_a),
        size_b=len(set_b),
        shared=len(shared),
    )


# ═══════════════════════════════════════════════════════════════════════════
# Grapheme divergence
# ═══════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class GraphemeDivergence:
    """How differently two languages use the same graphemes."""
    shared_graphemes: int
    """Number of grapheme keys in common."""
    total_graphemes: int
    """Number of grapheme keys in the union."""
    mean_ipa_distance: float
    """Mean feature distance between IPA mappings of shared graphemes."""
    overlap_ratio: float
    """Fraction of shared graphemes (Jaccard on grapheme key sets)."""

    def __repr__(self) -> str:
        return (
            f"GraphemeDivergence(shared={self.shared_graphemes}/"
            f"{self.total_graphemes}, ipa_dist={self.mean_ipa_distance:.3f}, "
            f"overlap={self.overlap_ratio:.3f})"
        )


def grapheme_divergence(spec_a: LanguageSpec, spec_b: LanguageSpec) -> GraphemeDivergence:
    """Measure how differently two languages map shared graphemes to IPA."""
    keys_a = set(k.lower() for k in spec_a.graphemes)
    keys_b = set(k.lower() for k in spec_b.graphemes)
    shared = keys_a & keys_b
    union = keys_a | keys_b

    if not shared:
        return GraphemeDivergence(0, len(union), 1.0, 0.0)

    ga = {k.lower(): v for k, v in spec_a.graphemes.items()}
    gb = {k.lower(): v for k, v in spec_b.graphemes.items()}

    total_dist = 0.0
    for key in shared:
        ipa_a = ga[key]
        ipa_b = gb[key]
        # For each grapheme, compute mean pairwise feature distance
        # between the IPA sets
        if not ipa_a or not ipa_b:
            total_dist += 1.0
            continue
        # Minimum distance from each IPA in A to closest in B, averaged
        min_dists: List[float] = []
        for ia in ipa_a:
            if not ia:
                continue
            best = min((segment_distance(ia, ib) for ib in ipa_b if ib), default=1.0)
            min_dists.append(best)
        for ib in ipa_b:
            if not ib:
                continue
            best = min((segment_distance(ib, ia) for ia in ipa_a if ia), default=1.0)
            min_dists.append(best)
        total_dist += (sum(min_dists) / len(min_dists)) if min_dists else 1.0

    overlap = len(shared) / len(union) if union else 0.0

    return GraphemeDivergence(
        shared_graphemes=len(shared),
        total_graphemes=len(union),
        mean_ipa_distance=total_dist / len(shared),
        overlap_ratio=overlap,
    )


# ═══════════════════════════════════════════════════════════════════════════
# Allophone overlap
# ═══════════════════════════════════════════════════════════════════════════

def allophone_overlap(spec_a: LanguageSpec, spec_b: LanguageSpec) -> float:
    """Jaccard similarity (0–1) of the allophone surface-form inventories."""
    set_a = _extract_allophones(spec_a)
    set_b = _extract_allophones(spec_b)
    if not set_a and not set_b:
        return 1.0
    union = set_a | set_b
    shared = set_a & set_b
    return len(shared) / len(union) if union else 0.0


# ═══════════════════════════════════════════════════════════════════════════
# Combined phonological distance
# ═══════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class PhonologicalDistance:
    """Combined multi-metric phonological distance between two languages."""
    inventory: InventoryDistance
    grapheme: GraphemeDivergence
    allophone_sim: float
    combined: float
    """Weighted combination: 0.0 = identical, 1.0 = maximally different."""

    def __repr__(self) -> str:
        return (
            f"PhonologicalDistance(combined={self.combined:.3f}, "
            f"inv={self.inventory.feature_mean:.3f}, "
            f"graph={self.grapheme.mean_ipa_distance:.3f}, "
            f"allo={self.allophone_sim:.3f})"
        )


def phonological_distance(
        spec_a: LanguageSpec,
        spec_b: LanguageSpec,
        *,
        w_inventory: float = 0.40,
        w_grapheme: float = 0.30,
        w_allophone: float = 0.30,
) -> PhonologicalDistance:
    """Compute a combined phonological distance between two languages.

    Parameters
    ----------
    w_inventory, w_grapheme, w_allophone : float
        Weights for each component (should sum to 1.0).
    """
    inv = inventory_distance(spec_a, spec_b)
    gra = grapheme_divergence(spec_a, spec_b)
    allo = allophone_overlap(spec_a, spec_b)

    # Normalise allophone to distance (1 - similarity)
    allo_dist = 1.0 - allo

    combined = (
            w_inventory * inv.feature_mean
            + w_grapheme * gra.mean_ipa_distance
            + w_allophone * allo_dist
    )

    return PhonologicalDistance(
        inventory=inv,
        grapheme=gra,
        allophone_sim=allo,
        combined=combined,
    )


# ═══════════════════════════════════════════════════════════════════════════
# Pairwise distance matrix
# ═══════════════════════════════════════════════════════════════════════════

def pairwise_distances(
        specs: List[LanguageSpec],
        metric: str = "combined",
) -> List[List[float]]:
    """Compute a symmetric distance matrix for a list of languages.

    Parameters
    ----------
    specs : list of LanguageSpec
    metric : str
        "combined" (default), "inventory", "grapheme", "allophone",
        or "ancestry" (uses ancestry-weighted phylogenetic distance).

    Returns
    -------
    List[List[float]]
        Square distance matrix (0-indexed, same order as *specs*).
    """
    n = len(specs)
    matrix = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if metric == "ancestry":
                d = 1.0 - ancestry_similarity(specs[i], specs[j])
            else:
                pd = phonological_distance(specs[i], specs[j])
                if metric == "combined":
                    d = pd.combined
                elif metric == "inventory":
                    d = pd.inventory.feature_mean
                elif metric == "grapheme":
                    d = pd.grapheme.mean_ipa_distance
                elif metric == "allophone":
                    d = 1.0 - pd.allophone_sim
                else:
                    d = pd.combined
            matrix[i][j] = d
            matrix[j][i] = d

    return matrix


# ═══════════════════════════════════════════════════════════════════════════
# Ancestry-weighted phylogenetic distance
# ═══════════════════════════════════════════════════════════════════════════

def _build_ancestor_graph(
        code: str,
        _visited: Optional[Set[str]] = None,
        _registry: Optional[Dict[str, "LanguageSpec"]] = None,
) -> Dict[str, List[Tuple[str, float]]]:
    """Build a directed graph {code: [(ancestor_code, weight), ...]}
    by recursively following all ancestor links.

    Returns a graph covering the full ancestry of *code*.
    """
    from orthography2ipa.registry import get as _get

    if _visited is None:
        _visited = set()
    if _registry is None:
        _registry = {}

    if code in _visited:
        return _registry

    _visited.add(code)

    try:
        spec = _get(code)
    except KeyError:
        return _registry

    ancestors = spec.get_ancestors()
    if ancestors:
        _registry[code] = [(a.code, a.weight) for a in ancestors]
        for a in ancestors:
            _build_ancestor_graph(a.code, _visited, _registry)
    else:
        _registry[code] = []

    return _registry


def ancestry_similarity(
        spec_a: LanguageSpec,
        spec_b: LanguageSpec,
        max_depth: int = 10,
) -> float:
    """Compute ancestry-weighted similarity between two languages.

    Traces all ancestor paths for both languages, finds shared ancestors,
    and computes similarity as the sum of products of weights along the
    best connecting paths.

    Returns a value in [0.0, 1.0]:
    - 1.0: identical language
    - ~0.7-0.9: dialect of same language
    - ~0.4-0.7: same branch (e.g., two Romance languages)
    - ~0.2-0.4: same family, different branches
    - ~0.05-0.2: remote connection (substrate/adstrate only)
    - 0.0: no traceable connection
    """
    if spec_a.code == spec_b.code:
        return 1.0

    # Build weighted paths from each language to all reachable ancestors.
    paths_a = _trace_ancestry_weights(spec_a.code, max_depth)
    paths_b = _trace_ancestry_weights(spec_b.code, max_depth)

    # Check if A is a DIRECT parent of B or vice versa
    # (only applies when the path weight is high — not transitive traces)
    if spec_a.code in paths_b:
        direct_weight = paths_b[spec_a.code]
        # Also check shared-ancestor path; return whichever is higher
        shared = set(paths_a) & set(paths_b)
        shared_best = max(
            (paths_a[a] * paths_b[a] for a in shared), default=0.0
        )
        return max(direct_weight, shared_best)

    if spec_b.code in paths_a:
        direct_weight = paths_a[spec_b.code]
        shared = set(paths_a) & set(paths_b)
        shared_best = max(
            (paths_a[a] * paths_b[a] for a in shared), default=0.0
        )
        return max(direct_weight, shared_best)

    # Find shared ancestors and compute similarity through each
    shared = set(paths_a) & set(paths_b)
    if not shared:
        return 0.0

    # For each shared ancestor, the connection strength is
    # weight_A_to_ancestor * weight_B_to_ancestor
    # (product of the path weights = how strongly connected via this ancestor)
    # Take the maximum across all shared ancestors (best connection).
    best = 0.0
    for ancestor in shared:
        strength = paths_a[ancestor] * paths_b[ancestor]
        if strength > best:
            best = strength

    return min(best, 1.0)


def _trace_ancestry_weights(
        code: str,
        max_depth: int = 10,
) -> Dict[str, float]:
    """Trace all ancestry paths from *code*, returning {ancestor: max_weight}.

    The weight to an ancestor is the PRODUCT of weights along the path.
    If multiple paths reach the same ancestor, the maximum weight wins.
    """
    from orthography2ipa.registry import get as _get

    result: Dict[str, float] = {}
    # BFS with weight propagation
    # Queue: (code_to_visit, accumulated_weight, depth)
    queue: List[Tuple[str, float, int]] = [(code, 1.0, 0)]

    while queue:
        current, weight, depth = queue.pop(0)
        if depth > max_depth:
            continue

        try:
            spec = _get(current)
        except KeyError:
            continue

        ancestors = spec.get_ancestors()
        for a in ancestors:
            path_weight = weight * a.weight
            # Only keep the strongest path to each ancestor
            if a.code not in result or path_weight > result[a.code]:
                result[a.code] = path_weight
                queue.append((a.code, path_weight, depth + 1))

    return result


def full_distance(
        spec_a: LanguageSpec,
        spec_b: LanguageSpec,
        *,
        w_phonological: float = 0.60,
        w_ancestry: float = 0.40,
) -> float:
    """Combined phonological + ancestry distance.

    This is the most complete distance metric, combining:
    - Phonological distance (inventory, grapheme, allophone comparisons)
    - Ancestry-weighted phylogenetic distance (traces shared ancestors)

    Parameters
    ----------
    w_phonological, w_ancestry : float
        Weights (should sum to 1.0).

    Returns
    -------
    float
        Distance in [0.0, 1.0].
    """
    pd = phonological_distance(spec_a, spec_b)
    anc_sim = ancestry_similarity(spec_a, spec_b)
    return w_phonological * pd.combined + w_ancestry * (1.0 - anc_sim)


# ═══════════════════════════════════════════════════════════════════════════
# Tone distance
# ═══════════════════════════════════════════════════════════════════════════

def tone_distance(spec_a: LanguageSpec, spec_b: LanguageSpec) -> float:
    """Jaccard distance on tone inventories.

    Languages with no tones get distance 0.0 from each other,
    maximal distance (1.0) from tonal languages.
    """
    inv_a = spec_a.tone_inventory
    inv_b = spec_b.tone_inventory
    set_a = set(inv_a.keys()) if inv_a else set()
    set_b = set(inv_b.keys()) if inv_b else set()

    if not set_a and not set_b:
        return 0.0
    if not set_a or not set_b:
        return 1.0

    union = set_a | set_b
    shared = set_a & set_b
    return 1.0 - (len(shared) / len(union))


# ═══════════════════════════════════════════════════════════════════════════
# Orthographic distance (integrates script distance)
# ═══════════════════════════════════════════════════════════════════════════

def orthographic_distance(spec_a: LanguageSpec, spec_b: LanguageSpec) -> float:
    """Combined distance factoring in script difference.

    For same-script languages, this reduces to grapheme divergence.
    For cross-script languages, adds script typological distance.
    """
    from orthography2ipa.script_distance import SCRIPT_REGISTRY, script_distance_by_name

    gra = grapheme_divergence(spec_a, spec_b)

    # Try to get script distance
    try:
        s_dist = script_distance_by_name(spec_a.script, spec_b.script)
    except KeyError:
        s_dist = 0.0 if spec_a.script == spec_b.script else 0.5

    if s_dist == 0.0:
        return gra.mean_ipa_distance
    return 0.6 * s_dist + 0.4 * gra.mean_ipa_distance
