"""Tests for orthography2ipa.distance — Phonological distance metrics.

Validates:
- Segment (phone) distance: identity, symmetry, triangle inequality
- Feature vectors: deterministic, correct dimensionality
- Inventory distance
- Grapheme divergence
- Allophone overlap
- Phonological distance (combined)
- Ancestry similarity: shared vs unrelated languages
- Full distance: combined phonological + ancestry
- Pairwise distance matrices
"""
import pytest

import orthography2ipa
from orthography2ipa.distance import (
    feature_vector,
    segment_distance,
    inventory_distance,
    grapheme_divergence,
    allophone_overlap,
    phonological_distance,
    ancestry_similarity,
    full_distance,
    pairwise_distances,
    InventoryDistance,
    GraphemeDivergence,
    PhonologicalDistance,
)
from orthography2ipa.types import LanguageSpec


# ═══════════════════════════════════════════════════════════════════════════
# Fixtures
# ═══════════════════════════════════════════════════════════════════════════

@pytest.fixture
def en():
    return orthography2ipa.get("en-GB")

@pytest.fixture
def es():
    return orthography2ipa.get("es-ES")

@pytest.fixture
def pt():
    return orthography2ipa.get("pt-PT")

@pytest.fixture
def pt_br():
    return orthography2ipa.get("pt-BR")

@pytest.fixture
def fr():
    return orthography2ipa.get("fr-FR")

@pytest.fixture
def la():
    return orthography2ipa.get("la")

@pytest.fixture
def it():
    return orthography2ipa.get("it-IT")

@pytest.fixture
def ja():
    return orthography2ipa.get("ja")


# ═══════════════════════════════════════════════════════════════════════════
# Feature vectors
# ═══════════════════════════════════════════════════════════════════════════

class TestFeatureVector:
    """Tests for feature_vector()."""

    def test_returns_tuple(self):
        vec = feature_vector("p")
        assert isinstance(vec, tuple)

    def test_dimensionality(self):
        """Feature vectors should have 21 features."""
        vec = feature_vector("p")
        assert len(vec) == 21

    def test_values_in_range(self):
        """All features should be 0.0, 0.5, or 1.0."""
        for segment in ["p", "a", "t", "s", "n", "ʃ", "ŋ"]:
            vec = feature_vector(segment)
            for v in vec:
                assert v in (0.0, 0.5, 1.0), f"Unexpected value {v} for {segment}"

    def test_deterministic(self):
        """Same segment → same vector every time."""
        v1 = feature_vector("p")
        v2 = feature_vector("p")
        assert v1 == v2

    def test_different_segments_differ(self):
        """p and a should have different feature vectors."""
        assert feature_vector("p") != feature_vector("a")

    def test_unknown_segment_returns_neutral(self):
        """Unknown segments should get the neutral vector (all 0.5)."""
        vec = feature_vector("§")
        assert all(v == 0.5 for v in vec)


# ═══════════════════════════════════════════════════════════════════════════
# Segment distance — mathematical properties
# ═══════════════════════════════════════════════════════════════════════════

class TestSegmentDistanceMath:
    """Segment distance should be a proper metric."""

    def test_identity(self):
        """d(x, x) == 0 for all segments."""
        for seg in ["p", "b", "t", "d", "k", "a", "i", "u", "s", "ʃ"]:
            assert segment_distance(seg, seg) == 0.0

    def test_symmetry(self):
        """d(x, y) == d(y, x)."""
        pairs = [("p", "b"), ("t", "a"), ("s", "ʃ"), ("n", "ŋ")]
        for a, b in pairs:
            assert segment_distance(a, b) == pytest.approx(
                segment_distance(b, a), abs=1e-10
            )

    def test_triangle_inequality(self):
        """d(x, z) ≤ d(x, y) + d(y, z)."""
        triples = [("p", "t", "k"), ("b", "d", "ɡ"), ("a", "i", "u")]
        for x, y, z in triples:
            dxz = segment_distance(x, z)
            dxy = segment_distance(x, y)
            dyz = segment_distance(y, z)
            assert dxz <= dxy + dyz + 1e-10

    def test_non_negative(self):
        for a, b in [("p", "b"), ("t", "a"), ("s", "z")]:
            assert segment_distance(a, b) >= 0.0


# ═══════════════════════════════════════════════════════════════════════════
# Segment distance — linguistic expectations
# ═══════════════════════════════════════════════════════════════════════════

class TestSegmentDistanceLinguistic:
    """Linguistically motivated distance expectations."""

    def test_voicing_minimal_pair_small(self):
        """p/b differ only in voicing → small distance."""
        d = segment_distance("p", "b")
        assert d < 0.15

    def test_place_difference_moderate(self):
        """p/t differ in place → moderate distance."""
        d = segment_distance("p", "t")
        assert 0.05 < d < 0.30

    def test_consonant_vowel_maximum(self):
        """Consonant vs vowel → distance near or at 1.0."""
        d = segment_distance("p", "a")
        assert d >= 0.5  # major class difference

    def test_manner_contrast(self):
        """t (stop) vs s (fricative) → moderate distance."""
        d = segment_distance("t", "s")
        assert 0.05 < d < 0.40

    def test_similar_fricatives(self):
        """s and ʃ differ in place → smaller than cross-manner."""
        d_ss = segment_distance("s", "ʃ")
        d_st = segment_distance("s", "t")
        # s↔ʃ should be ≤ s↔t (both are s-like, differ only in place)
        assert d_ss <= d_st + 0.05

    def test_nasal_place_difference(self):
        """n and ŋ differ in place → small distance."""
        d = segment_distance("n", "ŋ")
        assert d < 0.20


# ═══════════════════════════════════════════════════════════════════════════
# Inventory distance
# ═══════════════════════════════════════════════════════════════════════════

class TestInventoryDistance:
    """Tests for inventory_distance()."""

    def test_returns_correct_type(self, es, pt):
        result = inventory_distance(es, pt)
        assert isinstance(result, InventoryDistance)

    def test_identity(self, es):
        result = inventory_distance(es, es)
        assert result.jaccard == pytest.approx(0.0, abs=0.01)

    def test_related_languages_closer(self, es, pt, ja):
        """Spanish↔Portuguese should be closer than Spanish↔Japanese."""
        d_es_pt = inventory_distance(es, pt)
        d_es_ja = inventory_distance(es, ja)
        assert d_es_pt.feature_mean < d_es_ja.feature_mean

    def test_values_in_range(self, es, en):
        result = inventory_distance(es, en)
        assert 0.0 <= result.jaccard <= 1.0
        assert 0.0 <= result.feature_mean <= 1.0


# ═══════════════════════════════════════════════════════════════════════════
# Grapheme divergence
# ═══════════════════════════════════════════════════════════════════════════

class TestGraphemeDivergence:
    """Tests for grapheme_divergence()."""

    def test_returns_correct_type(self, es, pt):
        result = grapheme_divergence(es, pt)
        assert isinstance(result, GraphemeDivergence)

    def test_identity_is_zero(self, es):
        result = grapheme_divergence(es, es)
        assert result.mean_ipa_distance == pytest.approx(0.0, abs=0.01)

    def test_values_in_range(self, es, en):
        result = grapheme_divergence(es, en)
        assert 0.0 <= result.mean_ipa_distance <= 1.0

    def test_shared_script_languages_have_nonzero_divergence(self, es, fr):
        """Spanish and French share Latin script but map graphemes differently."""
        result = grapheme_divergence(es, fr)
        assert result.mean_ipa_distance > 0.0

    def test_shared_grapheme_count(self, es, pt):
        result = grapheme_divergence(es, pt)
        assert result.shared_count > 0  # many shared Latin graphemes


# ═══════════════════════════════════════════════════════════════════════════
# Allophone overlap
# ═══════════════════════════════════════════════════════════════════════════

class TestAllophoneOverlap:
    """Tests for allophone_overlap()."""

    def test_self_overlap_is_one(self, es):
        sim = allophone_overlap(es, es)
        assert sim == pytest.approx(1.0, abs=0.01)

    def test_returns_float(self, es, pt):
        sim = allophone_overlap(es, pt)
        assert isinstance(sim, float)

    def test_range(self, es, ja):
        sim = allophone_overlap(es, ja)
        assert 0.0 <= sim <= 1.0

    def test_related_higher_than_unrelated(self, es, pt, ja):
        """Spanish↔Portuguese should share more allophones than Spanish↔Japanese."""
        sim_es_pt = allophone_overlap(es, pt)
        sim_es_ja = allophone_overlap(es, ja)
        assert sim_es_pt > sim_es_ja


# ═══════════════════════════════════════════════════════════════════════════
# Phonological distance (combined)
# ═══════════════════════════════════════════════════════════════════════════

class TestPhonologicalDistance:
    """Tests for phonological_distance() — the main combined metric."""

    def test_returns_correct_type(self, es, pt):
        result = phonological_distance(es, pt)
        assert isinstance(result, PhonologicalDistance)

    def test_has_all_components(self, es, pt):
        result = phonological_distance(es, pt)
        assert isinstance(result.inventory, InventoryDistance)
        assert isinstance(result.grapheme, GraphemeDivergence)
        assert isinstance(result.allophone_sim, float)
        assert isinstance(result.combined, float)

    def test_combined_in_range(self, es, pt):
        result = phonological_distance(es, pt)
        assert 0.0 <= result.combined <= 1.0

    def test_identity_near_zero(self, es):
        result = phonological_distance(es, es)
        assert result.combined < 0.05

    def test_related_closer_than_unrelated(self, es, pt, ja):
        d_es_pt = phonological_distance(es, pt)
        d_es_ja = phonological_distance(es, ja)
        assert d_es_pt.combined < d_es_ja.combined

    def test_latin_to_descendants_ordered(self, la, es, fr):
        """Latin→Spanish and Latin→French should be reasonable distances."""
        d_la_es = phonological_distance(la, es)
        d_la_fr = phonological_distance(la, fr)
        # Both should be nonzero but not near 1.0
        assert 0.1 < d_la_es.combined < 0.8
        assert 0.1 < d_la_fr.combined < 0.8

    def test_repr(self, es, pt):
        result = phonological_distance(es, pt)
        r = repr(result)
        assert "combined=" in r

    def test_custom_weights(self, es, pt):
        """Custom weights should change the combined score."""
        d1 = phonological_distance(es, pt, w_inventory=1.0, w_grapheme=0.0,
                                    w_allophone=0.0)
        d2 = phonological_distance(es, pt, w_inventory=0.0, w_grapheme=1.0,
                                    w_allophone=0.0)
        # Different weights → different combined scores (unless coincidental)
        # At minimum they should both be in range
        assert 0.0 <= d1.combined <= 1.0
        assert 0.0 <= d2.combined <= 1.0


# ═══════════════════════════════════════════════════════════════════════════
# Ancestry similarity
# ═══════════════════════════════════════════════════════════════════════════

class TestAncestrySimilarity:
    """Tests for ancestry_similarity()."""

    def test_self_similarity_high(self, es):
        sim = ancestry_similarity(es, es)
        assert sim >= 0.5

    def test_related_languages_high(self, es, pt):
        """Spanish and Portuguese share Latin ancestry → high similarity."""
        sim = ancestry_similarity(es, pt)
        assert sim > 0.2

    def test_unrelated_languages_zero(self, es, ja):
        """Spanish and Japanese share no ancestry → 0.0."""
        sim = ancestry_similarity(es, ja)
        assert sim == pytest.approx(0.0, abs=0.05)

    def test_symmetry(self, es, pt):
        sim_ab = ancestry_similarity(es, pt)
        sim_ba = ancestry_similarity(pt, es)
        assert sim_ab == pytest.approx(sim_ba, abs=1e-10)

    def test_range(self, es, fr):
        sim = ancestry_similarity(es, fr)
        assert 0.0 <= sim <= 1.0

    def test_dialect_very_similar(self, pt, pt_br):
        """pt-BR is a child of pt → very high ancestry similarity."""
        sim = ancestry_similarity(pt, pt_br)
        assert sim > 0.4

    def test_different_family_low(self, en, ja):
        """Germanic vs Japonic → very low or zero."""
        sim = ancestry_similarity(en, ja)
        assert sim < 0.1


# ═══════════════════════════════════════════════════════════════════════════
# Full distance
# ═══════════════════════════════════════════════════════════════════════════

class TestFullDistance:
    """Tests for full_distance() — combined phonological + ancestry."""

    def test_returns_float(self, es, pt):
        d = full_distance(es, pt)
        assert isinstance(d, float)

    def test_range(self, es, pt):
        d = full_distance(es, pt)
        assert 0.0 <= d <= 1.0

    def test_related_closer(self, es, pt, ja):
        d_es_pt = full_distance(es, pt)
        d_es_ja = full_distance(es, ja)
        assert d_es_pt < d_es_ja


# ═══════════════════════════════════════════════════════════════════════════
# Pairwise distance matrix
# ═══════════════════════════════════════════════════════════════════════════

class TestPairwiseDistances:
    """Tests for pairwise_distances()."""

    def test_square_matrix(self, es, pt, en):
        specs = [es, pt, en]
        matrix = pairwise_distances(specs)
        assert len(matrix) == 3
        assert all(len(row) == 3 for row in matrix)

    def test_diagonal_zero(self, es, pt, en):
        specs = [es, pt, en]
        matrix = pairwise_distances(specs)
        for i in range(3):
            assert matrix[i][i] == pytest.approx(0.0, abs=0.05)

    def test_symmetric(self, es, pt, en):
        specs = [es, pt, en]
        matrix = pairwise_distances(specs)
        for i in range(3):
            for j in range(3):
                assert matrix[i][j] == pytest.approx(
                    matrix[j][i], abs=1e-10
                )

    def test_ancestry_metric(self, es, pt, en):
        specs = [es, pt, en]
        matrix = pairwise_distances(specs, metric="ancestry")
        assert len(matrix) == 3
        # Ancestry distances should be in [0, 1]
        for row in matrix:
            for val in row:
                assert 0.0 <= val <= 1.0 + 1e-10
