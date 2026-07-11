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

import functools
from dataclasses import dataclass, replace
from typing import Dict, List, Optional, Set, Tuple

from orthography2ipa.feats import NUM_FEATURES, phonetic_distance, vectorize_phones
from orthography2ipa.types import Ancestor, LanguageSpec, WeightedDistance

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
    "phoneme_coverage",
    "weighted_full_distance",
    "positional_divergence",
    "temporal_distance",
    "WeightedDistance",
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

def segment_distance(seg_a: str, seg_b: str, strict: bool = False) -> float:
    """Phonetic distance between two IPA segments, normalised to [0.0, 1.0].

    Uses a weighted feature distance, which gives higher
    weight to major-class features (syllabic, sonorant, consonantal)
    and lower weight to minor features (strident, distributed, long).

    Vowel↔consonant mismatches always return 1.0.

    Parameters
    ----------
    seg_a, seg_b : str
        IPA segments to compare.
    strict : bool
        If ``True``, raise ``ValueError`` when a segment produces an
        all-0.5 (unknown) feature vector.  Default is ``False`` (degrade
        gracefully).

    Raises
    ------
    ValueError
        If ``strict=True`` and either segment is unknown.
    """
    if seg_a == seg_b:
        return 0.0
    if not seg_a or not seg_b or seg_a == "∅" or seg_b == "∅":
        return 1.0
    if strict:
        for seg in (seg_a, seg_b):
            vec = feature_vector(seg)
            if all(v == 0.5 for v in vec):
                raise ValueError(f"Unknown IPA segment: {seg!r}")
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

def _data_ancestors(spec: LanguageSpec) -> Tuple[Ancestor, ...]:
    """Return *spec*'s ancestors with classification-only clade nodes skipped.

    A clade (``Romance``, ``West Germanic``) is a step in the classification
    chain, not a language: it has no phonology, so it contributes nothing to a
    genealogical distance. Each clade ancestor is therefore replaced by the
    nearest data-bearing ancestor above it (dropped when there is none), which
    keeps ancestry weights identical to a graph with no clade nodes in it.
    """
    from orthography2ipa.registry import get as _get

    resolved: List[Ancestor] = []
    for ancestor in spec.get_ancestors():
        code: Optional[str] = ancestor.code
        seen: Set[str] = set()
        while code and code not in seen:
            seen.add(code)
            try:
                candidate = _get(code)
            except KeyError:
                code = None
                break
            if not candidate.clade:
                break
            code = candidate.parent
        if code and code != ancestor.code:
            resolved.append(replace(ancestor, code=code))
        elif code:
            resolved.append(ancestor)
    return tuple(resolved)


def _build_ancestor_graph(
        code: str,
        _visited: Optional[Set[str]] = None,
        _registry: Optional[Dict[str, List[Tuple[str, float]]]] = None,
        _path: Optional[List[str]] = None,
) -> Dict[str, List[Tuple[str, float]]]:
    """Build a directed graph {code: [(ancestor_code, weight), ...]}
    by recursively following all ancestor links.

    Returns a graph covering the full ancestry of *code*.

    Raises
    ------
    ValueError
        If a circular ancestry reference is detected.
    """
    from orthography2ipa.registry import get as _get

    if _visited is None:
        _visited = set()
    if _registry is None:
        _registry = {}
    if _path is None:
        _path = []

    if code in _path:
        raise ValueError(f"Circular ancestry detected: {code!r} already visited")

    if code in _visited:
        return _registry

    _visited.add(code)
    _path = _path + [code]

    try:
        spec = _get(code)
    except KeyError:
        return _registry

    ancestors = _data_ancestors(spec)
    if ancestors:
        _registry[code] = [(a.code, a.weight) for a in ancestors]
        for a in ancestors:
            _build_ancestor_graph(a.code, _visited, _registry, _path)
    else:
        _registry[code] = []

    return _registry


@functools.lru_cache(maxsize=256)
def _get_ancestry_weights_by_code(code: str) -> Dict[str, float]:
    """Return the ancestry weight map for *code*, cached by language code.

    Delegates to ``_trace_ancestry_weights`` with a default max_depth of 10.
    """
    return _trace_ancestry_weights(code)


def _get_ancestry_weights(spec: LanguageSpec) -> Dict[str, float]:
    """Return the ancestry weight map for *spec*.

    Thin wrapper over the cached ``_get_ancestry_weights_by_code``.
    """
    return _get_ancestry_weights_by_code(spec.code)


def _temporal_decay(
        ancestor_spec: LanguageSpec,
        descendant_spec: LanguageSpec,
        decay_halflife: float = 1000.0,
) -> float:
    """Exponential weight multiplier based on temporal gap between ancestor and descendant.

    Returns 1.0 when either language lacks timespan data (no penalty applied).
    Uses the gap between ancestor's end (or start if no end) and descendant's
    start to compute: ``exp(-gap / halflife)``.

    Parameters
    ----------
    ancestor_spec : LanguageSpec
        The ancestor language.
    descendant_spec : LanguageSpec
        The descendant language.
    decay_halflife : float
        Years for weight to decay to ~0.37 (exp(-1)).  Default 1000 years.

    Returns
    -------
    float
        Multiplier in (0.0, 1.0].
    """
    import math
    if ancestor_spec.timespan is None or descendant_spec.timespan is None:
        return 1.0
    anc_end = ancestor_spec.timespan.end_year if ancestor_spec.timespan.end_year is not None \
        else ancestor_spec.timespan.start_year
    gap = descendant_spec.timespan.start_year - anc_end
    if gap <= 0:
        return 1.0
    return math.exp(-gap / decay_halflife)


def ancestry_similarity(
        spec_a: LanguageSpec,
        spec_b: LanguageSpec,
        max_depth: int = 10,
        temporal_decay: bool = False,
        decay_halflife: float = 1000.0,
) -> float:
    """Compute ancestry-weighted similarity between two languages.

    Traces all ancestor paths for both languages, finds shared ancestors,
    and computes similarity as the sum of products of weights along the
    best connecting paths.

    Parameters
    ----------
    spec_a, spec_b : LanguageSpec
        Languages to compare.
    max_depth : int
        Maximum recursion depth for ancestry tracing.
    temporal_decay : bool
        If ``True`` and ``timespan`` data is available, multiply each ancestor
        weight by an exponential decay factor based on the temporal gap between
        the ancestor's era and the descendant.  Default ``False`` (static weights).
    decay_halflife : float
        Years for weight to decay to ~0.37 when ``temporal_decay=True``.

    Returns a value in [0.0, 1.0]:
    - 1.0: identical language
    - ~0.7-0.9: dialect of same language
    - ~0.4-0.7: same branch (e.g., two Romance languages)
    - ~0.2-0.4: same family, different branches
    - ~0.05-0.2: remote connection (substrate/adstrate only)
    - 0.0: no traceable connection
    """
    from orthography2ipa.registry import get as _get

    if spec_a.code == spec_b.code:
        return 1.0

    # Build weighted paths from each language to all reachable ancestors.
    if temporal_decay:
        paths_a = _trace_ancestry_weights_temporal(spec_a, decay_halflife=decay_halflife)
        paths_b = _trace_ancestry_weights_temporal(spec_b, decay_halflife=decay_halflife)
    else:
        paths_a = _get_ancestry_weights(spec_a)
        paths_b = _get_ancestry_weights(spec_b)

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

        ancestors = _data_ancestors(spec)
        for a in ancestors:
            path_weight = weight * a.weight
            # Only keep the strongest path to each ancestor
            if a.code not in result or path_weight > result[a.code]:
                result[a.code] = path_weight
                queue.append((a.code, path_weight, depth + 1))

    return result


def _trace_ancestry_weights_temporal(
        spec: LanguageSpec,
        max_depth: int = 10,
        decay_halflife: float = 1000.0,
) -> Dict[str, float]:
    """Like ``_trace_ancestry_weights`` but multiplies each path weight by
    a temporal decay factor based on the gap between ancestor and descendant.

    Parameters
    ----------
    spec : LanguageSpec
        Starting language.
    max_depth : int
        Maximum recursion depth.
    decay_halflife : float
        Years for weight to halve (exponential decay).

    Returns
    -------
    Dict[str, float]
        Mapping of ancestor code → temporally-decayed max path weight.
    """
    from orthography2ipa.registry import get as _get

    result: Dict[str, float] = {}
    # Queue: (code_to_visit, accumulated_weight, depth, last_spec_with_timespan)
    queue: List[Tuple[str, float, int, LanguageSpec]] = [(spec.code, 1.0, 0, spec)]

    while queue:
        current, weight, depth, descendant_spec = queue.pop(0)
        if depth > max_depth:
            continue
        try:
            current_spec = _get(current)
        except KeyError:
            continue

        ancestors = _data_ancestors(current_spec)
        for a in ancestors:
            try:
                anc_spec = _get(a.code)
            except KeyError:
                anc_spec = None

            decay = _temporal_decay(anc_spec, descendant_spec, decay_halflife) if anc_spec else 1.0
            path_weight = weight * a.weight * decay
            if a.code not in result or path_weight > result[a.code]:
                result[a.code] = path_weight
                next_descendant = anc_spec if anc_spec else descendant_spec
                queue.append((a.code, path_weight, depth + 1, next_descendant))

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


# ═══════════════════════════════════════════════════════════════════════════
# Phoneme coverage (asymmetric)
# ═══════════════════════════════════════════════════════════════════════════

def phoneme_coverage(spec_native: LanguageSpec, spec_target: LanguageSpec) -> float:
    """Asymmetric: fraction of spec_target's phonemes already in spec_native's inventory.

    Parameters
    ----------
    spec_native : LanguageSpec
        The learner's native language.
    spec_target : LanguageSpec
        The language being acquired.

    Returns
    -------
    float
        1.0 = spec_native covers all of spec_target's phonemes (easy transfer).
        0.0 = no shared phonemes (hard transfer).
    """
    native_phones = _extract_phonemes(spec_native)
    target_phones = _extract_phonemes(spec_target)
    if not target_phones:
        return 1.0
    return len(native_phones & target_phones) / len(target_phones)


# ═══════════════════════════════════════════════════════════════════════════
# Weighted full distance
# ═══════════════════════════════════════════════════════════════════════════

def weighted_full_distance(
        spec_a: LanguageSpec,
        spec_b: LanguageSpec,
        *,
        w_inventory: float = 0.25,
        w_grapheme: float = 0.20,
        w_allophone: float = 0.15,
        w_ancestry: float = 0.40,
        w_temporal: float = 0.0,
        reference_year: int = 2025,
) -> "WeightedDistance":
    """Single configurable entry point combining all distance components.

    Parameters
    ----------
    spec_a, spec_b : LanguageSpec
        Languages to compare.
    w_inventory, w_grapheme, w_allophone, w_ancestry : float
        Component weights; need not sum to 1.0 (normalised internally).
    w_temporal : float
        Weight for temporal distance.  Default ``0.0`` (disabled) to preserve
        backward compatibility.  Set to a positive value to include
        :func:`temporal_distance` in the combined score.  If timespan data is
        missing for either language, this component is excluded and the
        remaining weights are renormalised.
    reference_year : int
        Passed to :func:`temporal_distance` for living languages.

    Returns
    -------
    WeightedDistance
        Frozen dataclass with per-component scores and the weighted ``combined``
        value in [0.0, 1.0].
    """
    inv = inventory_distance(spec_a, spec_b)
    gra = grapheme_divergence(spec_a, spec_b)
    allo = allophone_overlap(spec_a, spec_b)
    anc = ancestry_similarity(spec_a, spec_b)
    temp = temporal_distance(spec_a, spec_b, reference_year=reference_year)

    # If temporal data is unavailable, exclude it from the combined score
    effective_w_temporal = w_temporal if temp is not None else 0.0
    total_w = w_inventory + w_grapheme + w_allophone + w_ancestry + effective_w_temporal
    combined = (
        w_inventory * inv.feature_mean
        + w_grapheme * gra.mean_ipa_distance
        + w_allophone * (1.0 - allo)
        + w_ancestry * (1.0 - anc)
        + effective_w_temporal * (temp if temp is not None else 0.0)
    ) / total_w
    return WeightedDistance(
        inventory=inv.feature_mean,
        grapheme=gra.mean_ipa_distance,
        allophone=allo,
        ancestry=anc,
        temporal=temp,
        combined=combined,
        weights=(w_inventory, w_grapheme, w_allophone, w_ancestry, w_temporal),
    )


# ═══════════════════════════════════════════════════════════════════════════
# Temporal distance
# ═══════════════════════════════════════════════════════════════════════════

def temporal_distance(
        spec_a: LanguageSpec,
        spec_b: LanguageSpec,
        reference_year: int = 2025,
) -> Optional[float]:
    """Jaccard-interval distance between two languages' attestation periods.

    Returns ``None`` if either language lacks a :class:`~orthography2ipa.types.TimeSpan`.

    The metric is based on the Jaccard index of the two time intervals.
    Living languages (``end_year=None``) are treated as ongoing to
    ``reference_year``.

    Distance values:
    - ``0.0``: intervals are identical.
    - ``(0, 1)``: partial temporal overlap (higher = less overlap).
    - ``1.0``: no temporal overlap (languages lived in completely different eras).

    Parameters
    ----------
    spec_a, spec_b : LanguageSpec
        Languages to compare.
    reference_year : int
        Year to treat as the current end for living languages.  Default 2025.

    Returns
    -------
    Optional[float]
        Temporal distance in [0.0, 1.0], or ``None`` if data is missing.

    Examples
    --------
    >>> from orthography2ipa.types import TimeSpan, LanguageSpec
    >>> # Languages with full overlap → distance 0.0
    >>> # Languages in different eras → distance 1.0
    """
    if spec_a.timespan is None or spec_b.timespan is None:
        return None

    start_a = spec_a.timespan.start_year
    end_a = spec_a.timespan.end_year if spec_a.timespan.end_year is not None else reference_year
    start_b = spec_b.timespan.start_year
    end_b = spec_b.timespan.end_year if spec_b.timespan.end_year is not None else reference_year

    overlap = max(0, min(end_a, end_b) - max(start_a, start_b))
    union_span = max(end_a, end_b) - min(start_a, start_b)

    if union_span <= 0:
        return 0.0

    jaccard = overlap / union_span
    return 1.0 - jaccard


# ═══════════════════════════════════════════════════════════════════════════
# Positional divergence
# ═══════════════════════════════════════════════════════════════════════════

def positional_divergence(spec_a: LanguageSpec, spec_b: LanguageSpec) -> float:
    """Measures how differently two specs use positional grapheme overrides.

    Returns 0.0 when neither spec has positional graphemes or when specs are
    identical.  Returns a float in [0.0, 1.0].

    Parameters
    ----------
    spec_a, spec_b : LanguageSpec
        Languages to compare.

    Returns
    -------
    float
        0.0 = identical positional usage; 1.0 = maximally different.
    """
    def _get_positional_mappings(spec: LanguageSpec) -> Dict[str, Dict[str, str]]:
        """Return {grapheme: {position_value: ipa_candidates}} for positional graphemes."""
        result: Dict[str, Dict[str, str]] = {}
        for grapheme, pos_map in spec.positional_graphemes.items():
            entry: Dict[str, str] = {}
            for pos, ipa_list in pos_map.items():
                pos_key = pos.value if hasattr(pos, "value") else str(pos)
                entry[pos_key] = ipa_list[0] if ipa_list else ""
            if entry:
                result[grapheme] = entry
        return result

    pos_a = _get_positional_mappings(spec_a)
    pos_b = _get_positional_mappings(spec_b)

    if not pos_a and not pos_b:
        return 0.0

    all_graphemes = set(pos_a) | set(pos_b)
    if not all_graphemes:
        return 0.0

    total_divergence = 0.0
    for g in all_graphemes:
        if g in pos_a and g not in pos_b:
            total_divergence += 1.0
        elif g in pos_b and g not in pos_a:
            total_divergence += 1.0
        else:
            # Both have positional overrides for this grapheme
            positions = set(pos_a[g]) | set(pos_b[g])
            for pos in positions:
                ipa_a = pos_a[g].get(pos)
                ipa_b = pos_b[g].get(pos)
                if ipa_a is None or ipa_b is None:
                    total_divergence += 1.0 / len(positions)
                else:
                    total_divergence += segment_distance(ipa_a, ipa_b) / len(positions)

    return min(1.0, total_divergence / len(all_graphemes))


# ═══════════════════════════════════════════════════════════════════════════
# Spelling divergence — the inverse of grapheme divergence
# ═══════════════════════════════════════════════════════════════════════════

@dataclass(frozen=True)
class SpellingDivergence:
    """How differently two orthographies WRITE the same sounds."""

    shared_phonemes: int
    """Number of phonemes both orthographies can spell."""
    total_phonemes: int
    """Number of phonemes in the union of the two inverted maps."""
    mean_distance: float
    """Mean spelling distance over the shared phonemes (0 = spelled identically)."""
    identical_spellings: int
    """Shared phonemes the two orthographies spell exactly alike."""
    disjoint_spellings: int
    """Shared phonemes for which the two share no spelling at all."""


def _invert_graphemes(spec: LanguageSpec) -> Dict[str, Set[str]]:
    """Invert a spec's grapheme map into ``phoneme -> {graphemes that write it}``.

    ``graphemes`` answers "how is this written pronounced?"; the inverse answers
    "how is this sound written?". A grapheme with several candidates contributes
    to each of them, and a phoneme is routinely spelled several ways.
    """
    inverted: Dict[str, Set[str]] = {}
    for grapheme, ipas in (spec.graphemes or {}).items():
        for ipa in (ipas or ()):
            if not ipa:
                continue  # a silent grapheme spells no phoneme
            inverted.setdefault(ipa, set()).add(grapheme.lower())
    return inverted


def spelling_divergence(
        spec_a: LanguageSpec, spec_b: LanguageSpec) -> SpellingDivergence:
    """Measure how differently two orthographies spell the same phonemes.

    This is the INVERSE of :func:`grapheme_divergence`, and the two answer
    genuinely different questions:

    - :func:`grapheme_divergence` — *reading*: given the same TEXT, do these two
      sound alike?  (``j`` is /ʒ/ in Portuguese and /x/ in Spanish.)
    - :func:`spelling_divergence` — *spelling*: given the same SOUND, do these
      two write it alike?

    Orthography and phonology are orthogonal, and only this function can see it.
    Reintegrationist and RAG Galician are the same language with the same
    phonology: both spell /ɲ/ with a grapheme that maps to /ɲ/, so their
    *reading* divergence is nil and their graphemes are not even shared — yet one
    writes ``nh`` (as Portuguese does) and the other ``ñ`` (as Castilian does).
    That difference is invisible to every other metric here.

    Returns 1.0 (maximal divergence) when the two share no phoneme at all.
    """
    inv_a = _invert_graphemes(spec_a)
    inv_b = _invert_graphemes(spec_b)
    shared = set(inv_a) & set(inv_b)
    union = set(inv_a) | set(inv_b)
    if not shared:
        return SpellingDivergence(0, len(union), 1.0, 0, 0)

    distances: List[float] = []
    identical = 0
    disjoint = 0
    for phoneme in shared:
        spellings_a, spellings_b = inv_a[phoneme], inv_b[phoneme]
        overlap = spellings_a & spellings_b
        # Jaccard distance over the sets of graphemes that write this phoneme:
        # 0.0 when both orthographies spell it exactly the same way, 1.0 when
        # they share no spelling for it at all.
        distance = 1.0 - len(overlap) / len(spellings_a | spellings_b)
        distances.append(distance)
        if distance == 0.0:
            identical += 1
        elif not overlap:
            disjoint += 1

    return SpellingDivergence(
        shared_phonemes=len(shared),
        total_phonemes=len(union),
        mean_distance=sum(distances) / len(distances),
        identical_spellings=identical,
        disjoint_spellings=disjoint,
    )
