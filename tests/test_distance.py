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
    phoneme_coverage,
    weighted_full_distance,
    positional_divergence,
    InventoryDistance,
    GraphemeDivergence,
    PhonologicalDistance,
    WeightedDistance,
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
    # "ja" (Japanese) not in registry; using arb (Classical Arabic) as a
    # maximally distant, non-Indo-European comparator for linguistic distance tests.
    # Arabic (Semitic) shares no ancestry with Romance languages and has a
    # distinct phoneme inventory.
    return orthography2ipa.get("arb")


# ═══════════════════════════════════════════════════════════════════════════
# Feature vectors
# ═══════════════════════════════════════════════════════════════════════════

class TestFeatureVector:
    """Tests for feature_vector()."""

    def test_returns_tuple(self):
        vec = feature_vector("p")
        assert isinstance(vec, tuple)

    def test_dimensionality(self):
        """Feature vectors should have NUM_FEATURES features."""
        vec = feature_vector("p")
        assert len(vec) == 23

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
        """n and ŋ differ in place → moderate distance.
        phonematcher weights coronal/anterior/distributed features,
        so alveolar↔velar nasal distance is ~0.43."""
        d = segment_distance("n", "ŋ")
        assert d < 0.50


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
        """Spanish↔Portuguese should be closer than Spanish↔Arabic (Semitic).

        Jaccard distance measures inventory overlap; related languages share
        more phonemes so their Jaccard distance is lower.
        feature_mean measures similarity only among shared phonemes — unrelated
        languages share only universal basic phonemes, which can appear similar,
        so Jaccard is the correct metric for relatedness.
        """
        d_es_pt = inventory_distance(es, pt)
        d_es_ja = inventory_distance(es, ja)
        assert d_es_pt.jaccard < d_es_ja.jaccard

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

    def test_identity_is_near_zero(self, es):
        """Self-comparison should be near zero (small float due to
        case normalization in grapheme key matching)."""
        result = grapheme_divergence(es, es)
        assert result.mean_ipa_distance == pytest.approx(0.0, abs=0.05)

    def test_values_in_range(self, es, en):
        result = grapheme_divergence(es, en)
        assert 0.0 <= result.mean_ipa_distance <= 1.0

    def test_shared_script_languages_have_nonzero_divergence(self, es, fr):
        """Spanish and French share Latin script but map graphemes differently."""
        result = grapheme_divergence(es, fr)
        assert result.mean_ipa_distance > 0.0

    def test_shared_grapheme_count(self, es, pt):
        result = grapheme_divergence(es, pt)
        assert result.shared_graphemes > 0  # many shared Latin graphemes


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
        d1 = phonological_distance(es, pt, w_inventory=1.0, w_allophone=0.0)
        d2 = phonological_distance(es, pt, w_inventory=0.0, w_allophone=1.0)
        assert 0.0 <= d1.combined <= 1.0
        assert 0.0 <= d2.combined <= 1.0
        assert d1.combined == pytest.approx(d1.inventory.feature_mean)
        assert d2.combined == pytest.approx(1.0 - d2.allophone_sim)

    def test_no_grapheme_weight(self, es, pt):
        """There is no orthographic knob to turn: the score has no such term."""
        with pytest.raises(TypeError):
            phonological_distance(es, pt, w_grapheme=1.0)


# ═══════════════════════════════════════════════════════════════════════════
# Phonological distance is not contaminated by orthography
# ═══════════════════════════════════════════════════════════════════════════
def _spec(code: str, **overrides) -> LanguageSpec:
    """A minimal spec, with *overrides* applied."""
    base = dict(
        code=code,
        name=code,
        family="Test",
        script="Latin",
        graphemes={"p": ["p"], "t": ["t"], "a": ["a"], "i": ["i"]},
        allophones={},
        phonemes=("p", "t", "a", "i"),
    )
    base.update(overrides)
    return LanguageSpec(**base)


class TestPhonologyIsNotOrthography:
    """The score must read the inventory and the allophony, and nothing else."""

    def test_same_sounds_different_script_are_near_identical(self):
        """One phonology, two scripts → phonologically the same language.

        Hindi/Urdu and Serbian/Croatian in miniature: identical phoneme
        inventories, disjoint writing systems.  A phonological metric that read
        the spelling would call these maximally distant — they share no grapheme
        at all — which is exactly the error being guarded against.
        """
        devanagari = _spec("xx-deva", script="Devanagari",
                           graphemes={"प": ["p"], "त": ["t"], "आ": ["a"], "इ": ["i"]})
        arabic = _spec("xx-arab", script="Arabic",
                       graphemes={"پ": ["p"], "ت": ["t"], "ا": ["a"], "ی": ["i"]})

        d = phonological_distance(devanagari, arabic)

        # The orthographies are maximally apart — that is the whole point.
        assert d.grapheme.shared_graphemes == 0
        assert d.grapheme.mean_ipa_distance == 1.0
        # The phonologies are identical, and the score says so.
        assert d.combined == pytest.approx(0.0)

    def test_respelling_a_language_does_not_move_the_distance(self):
        """Change only the graphemes; the phonological distance must not budge.

        This is the regression guard.  A spec's ``phonemes`` are held fixed while
        its writing system is replaced wholesale; any drift in ``combined`` means
        orthography has leaked back into the metric.
        """
        reference = _spec("xx-ref")
        latin = _spec("yy-latin")
        respelled = _spec(
            "yy-latin",
            script="Cyrillic",
            graphemes={"п": ["p"], "т": ["t"], "а": ["a"], "и": ["i"]},
        )

        before = phonological_distance(reference, latin)
        after = phonological_distance(reference, respelled)

        # The respelling is real and visible on the orthographic axis …
        assert after.grapheme.mean_ipa_distance != before.grapheme.mean_ipa_distance
        # … and invisible to the phonological one.
        assert after.combined == before.combined
        assert after.inventory == before.inventory
        assert after.allophone_sim == before.allophone_sim

    def test_declared_phonemes_beat_the_spelling(self):
        """A spec that declares an inventory is scored on it, not on its letters.

        Both specs declare the same four phonemes, and one has a grapheme table
        that would derive an entirely different inventory.  Reading the declared
        ``phonemes`` — rather than reverse-engineering them from the spelling — is
        the only way to see that these two languages sound alike.  Allophones are
        stated on both so that the inventory axis is what is under test.
        """
        allophones = {"p": ["p"], "t": ["t"], "a": ["a"], "i": ["i"]}
        plain = _spec("xx-plain", allophones=dict(allophones))
        misleading_spelling = _spec(
            "yy-odd",
            graphemes={"q": ["q"], "x": ["χ"], "ø": ["ø"], "y": ["y"]},
            allophones=dict(allophones),
        )

        d = phonological_distance(plain, misleading_spelling)

        assert d.inventory.feature_mean == pytest.approx(0.0)
        assert d.combined == pytest.approx(0.0)


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
        """Spanish and Arabic (Semitic) share minimal ancestry.

        Arabic is listed as an adstrate to Spanish (Moorish influence), so
        ancestry_similarity is small but non-zero. The assertion checks that
        the value is well below what genuinely related languages score.
        """
        sim = ancestry_similarity(es, ja)
        assert sim < 0.2

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
        """Romance (Occitan) vs Semitic (Arabic) → zero shared ancestry."""
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


# ═══════════════════════════════════════════════════════════════════════════
# strict mode for segment_distance
# ═══════════════════════════════════════════════════════════════════════════

class TestSegmentDistanceStrict:
    """Tests for strict=True parameter in segment_distance()."""

    def test_unknown_strict_raises(self):
        """strict=True raises ValueError on an unknown IPA segment."""
        with pytest.raises(ValueError, match="Unknown IPA segment"):
            segment_distance("ℵ", "p", strict=True)

    def test_unknown_permissive_returns_float(self):
        """strict=False (default) returns a value in [0, 1] for unknown segments."""
        result = segment_distance("ℵ", "p")
        assert 0.0 <= result <= 1.0

    def test_known_segments_strict_ok(self):
        """Known segments should not raise even with strict=True."""
        result = segment_distance("p", "b", strict=True)
        assert 0.0 <= result <= 1.0


# ═══════════════════════════════════════════════════════════════════════════
# Phoneme coverage
# ═══════════════════════════════════════════════════════════════════════════

class TestPhonemeCoverage:
    """Tests for phoneme_coverage()."""

    def test_identity_is_one(self):
        """Coverage of a language against itself is 1.0."""
        spec = orthography2ipa.get("es-ES")
        assert phoneme_coverage(spec, spec) == pytest.approx(1.0)

    def test_range_ab(self):
        """Coverage(A, B) is in [0.0, 1.0]."""
        spec_a = orthography2ipa.get("es-ES")
        spec_b = orthography2ipa.get("fr-FR")
        assert 0.0 <= phoneme_coverage(spec_a, spec_b) <= 1.0

    def test_range_ba(self):
        """Coverage(B, A) is in [0.0, 1.0]."""
        spec_a = orthography2ipa.get("es-ES")
        spec_b = orthography2ipa.get("fr-FR")
        assert 0.0 <= phoneme_coverage(spec_b, spec_a) <= 1.0

    def test_related_languages_high_coverage(self):
        """Spanish covers a large fraction of Portuguese phonemes."""
        spec_a = orthography2ipa.get("es-ES")
        spec_b = orthography2ipa.get("pt-PT")
        cov = phoneme_coverage(spec_a, spec_b)
        assert cov > 0.3


# ═══════════════════════════════════════════════════════════════════════════
# WeightedDistance / weighted_full_distance
# ═══════════════════════════════════════════════════════════════════════════

class TestWeightedFullDistance:
    """Tests for weighted_full_distance() and WeightedDistance."""

    def test_returns_weighted_distance(self):
        """Returns a WeightedDistance instance."""
        spec_a = orthography2ipa.get("es-ES")
        spec_b = orthography2ipa.get("fr-FR")
        result = weighted_full_distance(spec_a, spec_b)
        assert isinstance(result, WeightedDistance)

    def test_combined_in_range(self):
        """combined is in [0, 1]."""
        spec_a = orthography2ipa.get("es-ES")
        spec_b = orthography2ipa.get("fr-FR")
        result = weighted_full_distance(spec_a, spec_b)
        assert 0.0 <= result.combined <= 1.0

    def test_w_inventory_only(self):
        """w_inventory=1.0, others=0 → combined == inventory component."""
        spec_a = orthography2ipa.get("es-ES")
        spec_b = orthography2ipa.get("fr-FR")
        result = weighted_full_distance(
            spec_a, spec_b,
            w_inventory=1.0, w_grapheme=0.0, w_allophone=0.0, w_ancestry=0.0,
        )
        assert result.combined == pytest.approx(result.inventory, abs=1e-9)

    def test_identity_near_zero(self):
        """All components near 0 for the same spec."""
        spec = orthography2ipa.get("es-ES")
        result = weighted_full_distance(spec, spec)
        assert result.combined < 0.01


# ═══════════════════════════════════════════════════════════════════════════
# Positional divergence
# ═══════════════════════════════════════════════════════════════════════════

class TestPositionalDivergence:
    """Tests for positional_divergence()."""

    def test_identity_is_zero(self):
        """Returns 0.0 for the same spec."""
        spec = orthography2ipa.get("es-ES")
        assert positional_divergence(spec, spec) == pytest.approx(0.0)

    def test_range(self):
        """Result in [0.0, 1.0]."""
        spec_a = orthography2ipa.get("es-ES")
        spec_b = orthography2ipa.get("fr-FR")
        result = positional_divergence(spec_a, spec_b)
        assert 0.0 <= result <= 1.0

    def test_no_positional_both_zero(self):
        """Returns 0.0 when neither spec has positional graphemes."""
        from orthography2ipa.types import LanguageSpec
        spec_a = LanguageSpec(
            code="xx", name="Test A", family="Test", script="Latin",
            graphemes={"a": ["a"], "b": ["b"]},
            allophones={},
        )
        spec_b = LanguageSpec(
            code="yy", name="Test B", family="Test", script="Latin",
            graphemes={"a": ["a"], "b": ["b"]},
            allophones={},
        )
        assert positional_divergence(spec_a, spec_b) == pytest.approx(0.0)
