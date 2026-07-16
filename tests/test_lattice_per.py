"""lattice_per — pronunciation-fair PER against the candidate lattice."""
import pytest

from orthography2ipa.lattice_per import LatticePER, lattice_per, _segments


class TestSegmentation:
    def test_combining_marks_stay_with_their_base(self):
        assert _segments("es̻ pada") == ["e", "s̻", "p", "a", "d", "a"]

    def test_stress_and_boundary_marks_are_stripped(self):
        assert _segments("ˈla.ðɾɐ") == ["l", "a", "ð", "ɾ", "ɐ"]

    def test_whitespace_never_scores(self):
        assert _segments("a b") == _segments("ab")


class TestOracleAgainstTheLattice:
    def test_engine_final_reading_scores_zero(self):
        # The sandhi-applied reading is always admissible.
        r = lattice_per("es̻ pada", "ez bada", "eu")
        assert r.distance == 0.0
        assert r.per == 0.0

    def test_pre_sandhi_lattice_reading_scores_zero(self):
        # A lattice path the final reading rewrote is still a valid
        # pronunciation; single-reference PER would have charged it.
        r = lattice_per("es̻ bada", "ez bada", "eu")
        assert r.distance == 0.0
        assert r.top_distance > 0.0
        assert r.variant_credit > 0.0

    def test_wrong_segments_are_charged_on_every_reading(self):
        r = lattice_per("es baða", "ez bada", "eu")
        assert r.distance == 2.0  # s̻→s and d→ð wrong on all paths

    def test_oracle_never_exceeds_single_reference(self):
        for hyp in ("es̻ pada", "es̻ bada", "es baða", "totally ˈdifferent"):
            r = lattice_per(hyp, "ez bada", "eu")
            assert r.distance <= r.top_distance

    def test_empty_hypothesis_costs_all_deletions(self):
        r = lattice_per("", "ez bada", "eu")
        assert r.distance == r.ref_segments
        assert r.per == 1.0

    def test_result_carries_the_resolved_lect(self):
        assert lattice_per("a", "a", "eu").lang == "eu"


class TestWeightedCosts:
    def test_weighted_never_exceeds_unit(self):
        ref, hyp = "ez bada", "es baða"
        unit = lattice_per(hyp, ref, "eu").distance
        weighted = lattice_per(hyp, ref, "eu", weighted=True).distance
        assert weighted <= unit

    def test_close_segments_cost_less_than_distant_ones(self):
        # d→ð (one lenition step) must cost less than d→a (consonant→vowel).
        near = lattice_per("es̻ paða", "ez bada", "eu", weighted=True).distance
        far = lattice_per("es̻ paaa", "ez bada", "eu", weighted=True).distance
        assert 0 < near < far

    def test_diacritic_only_difference_is_a_near_match(self):
        # s̻ vs s is outside the feature table; the base-character fallback
        # prices it as a feature flip, not a full substitution.
        r = lattice_per("es pada", "ez bada", "eu", weighted=True)
        assert 0 < r.distance < 0.5


class TestResultShape:
    def test_is_a_frozen_dataclass_with_the_documented_fields(self):
        r = lattice_per("es̻ pada", "ez bada", "eu")
        assert isinstance(r, LatticePER)
        with pytest.raises(AttributeError):
            r.distance = 1.0
        assert r.hyp_segments == 6
        assert r.ref_segments == 6
