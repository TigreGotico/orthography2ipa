"""Tests for temporal distance metrics and TimeSpan data model."""
from __future__ import annotations

import math
from unittest.mock import MagicMock

import pytest

from orthography2ipa.distance import (
    _temporal_decay,
    ancestry_similarity,
    temporal_distance,
    weighted_full_distance,
)
from orthography2ipa.types import LanguageSpec, TimeSpan


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def _make_spec(code: str, start: int, end: int | None = None) -> LanguageSpec:
    """Minimal LanguageSpec with only timespan set."""
    return LanguageSpec(
        code=code,
        name=code,
        family="Test",
        script="Latin",
        graphemes={},
        allophones={},
        timespan=TimeSpan(start_year=start, end_year=end),
    )


def _make_spec_no_timespan(code: str = "xx") -> LanguageSpec:
    return LanguageSpec(
        code=code,
        name=code,
        family="Test",
        script="Latin",
        graphemes={},
        allophones={},
        timespan=None,
    )


# ─────────────────────────────────────────────────────────────────────────────
# TimeSpan dataclass
# ─────────────────────────────────────────────────────────────────────────────

class TestTimeSpan:
    def test_historical(self):
        ts = TimeSpan(start_year=450, end_year=1150)
        assert ts.start_year == 450
        assert ts.end_year == 1150

    def test_living(self):
        ts = TimeSpan(start_year=1500, end_year=None)
        assert ts.end_year is None

    def test_bce(self):
        ts = TimeSpan(start_year=-500, end_year=200)
        assert ts.start_year == -500

    def test_frozen(self):
        ts = TimeSpan(start_year=1000, end_year=1200)
        with pytest.raises((AttributeError, TypeError)):
            ts.start_year = 999  # type: ignore[misc]


# ─────────────────────────────────────────────────────────────────────────────
# temporal_distance()
# ─────────────────────────────────────────────────────────────────────────────

class TestTemporalDistance:
    def test_missing_both_returns_none(self):
        a = _make_spec_no_timespan("a")
        b = _make_spec_no_timespan("b")
        assert temporal_distance(a, b) is None

    def test_missing_one_returns_none(self):
        a = _make_spec("a", 450, 1150)
        b = _make_spec_no_timespan("b")
        assert temporal_distance(a, b) is None
        assert temporal_distance(b, a) is None

    def test_identical_intervals_zero_distance(self):
        a = _make_spec("a", 450, 1150)
        b = _make_spec("b", 450, 1150)
        assert temporal_distance(a, b) == pytest.approx(0.0)

    def test_full_overlap_within_larger(self):
        # a=[400, 1200], b=[500, 1000] — b fully inside a
        a = _make_spec("a", 400, 1200)
        b = _make_spec("b", 500, 1000)
        d = temporal_distance(a, b)
        assert d is not None
        assert 0.0 < d < 1.0

    def test_no_overlap_gives_max_distance(self):
        a = _make_spec("a", 450, 1150)  # 450–1150
        b = _make_spec("b", 1600, 2025)  # 1600–2025 — no overlap
        d = temporal_distance(a, b)
        assert d == pytest.approx(1.0)

    def test_partial_overlap_between_zero_and_one(self):
        a = _make_spec("a", 400, 800)
        b = _make_spec("b", 600, 1000)
        d = temporal_distance(a, b)
        # overlap = 800-600=200, union = 1000-400=600, jaccard=200/600≈0.333
        assert d is not None
        assert d == pytest.approx(1.0 - 200.0 / 600.0)

    def test_living_language_uses_reference_year(self):
        a = _make_spec("a", 1500, None)  # living
        b = _make_spec("b", 1600, None)  # living, starts later
        d = temporal_distance(a, b, reference_year=2025)
        # overlap = 2025-1600=425, union = 2025-1500=525
        assert d == pytest.approx(1.0 - 425.0 / 525.0)

    def test_symmetry(self):
        a = _make_spec("a", 450, 1150)
        b = _make_spec("b", 1000, 1500)
        assert temporal_distance(a, b) == pytest.approx(temporal_distance(b, a))

    def test_adjacent_no_overlap(self):
        # ofs ends at 1500, fy starts at 1500 — single point, no interval overlap
        ofs = _make_spec("ofs", 1150, 1500)
        fy = _make_spec("fy", 1500, 2025)
        d = temporal_distance(ofs, fy)
        assert d == pytest.approx(1.0)


# ─────────────────────────────────────────────────────────────────────────────
# _temporal_decay()
# ─────────────────────────────────────────────────────────────────────────────

class TestTemporalDecay:
    def test_no_gap_returns_one(self):
        anc = _make_spec("anc", 500, 1000)
        desc = _make_spec("desc", 1000, 2000)  # starts where ancestor ends
        assert _temporal_decay(anc, desc) == pytest.approx(1.0)

    def test_halflife_decay(self):
        anc = _make_spec("anc", 0, 0)
        desc = _make_spec("desc", 1000, 2000)  # 1000-year gap
        decay = _temporal_decay(anc, desc, decay_halflife=1000.0)
        assert decay == pytest.approx(math.exp(-1.0), rel=1e-6)

    def test_zero_halflife_edge_case(self):
        # Large gap → near-zero decay
        anc = _make_spec("anc", -2000, -1000)
        desc = _make_spec("desc", 1500, 2025)
        decay = _temporal_decay(anc, desc, decay_halflife=1000.0)
        assert 0.0 < decay < 0.1

    def test_missing_ancestor_timespan_returns_one(self):
        anc = _make_spec_no_timespan("anc")
        desc = _make_spec("desc", 1500, 2025)
        assert _temporal_decay(anc, desc) == pytest.approx(1.0)

    def test_missing_descendant_timespan_returns_one(self):
        anc = _make_spec("anc", 500, 1000)
        desc = _make_spec_no_timespan("desc")
        assert _temporal_decay(anc, desc) == pytest.approx(1.0)

    def test_overlap_negative_gap_returns_one(self):
        # Ancestor still active when descendant starts — no decay
        anc = _make_spec("anc", 500, 1500)
        desc = _make_spec("desc", 1000, 2000)
        assert _temporal_decay(anc, desc) == pytest.approx(1.0)


# ─────────────────────────────────────────────────────────────────────────────
# ancestry_similarity() with temporal_decay
# ─────────────────────────────────────────────────────────────────────────────

class TestAncestryTemporalDecay:
    def test_temporal_decay_reduces_ancient_similarity(self):
        """ancestry to a 1300-year-old ancestor should drop with temporal_decay=True."""
        from orthography2ipa.json_loader import load_json_spec
        fy = load_json_spec("fy")
        gem = load_json_spec("gem")
        plain = ancestry_similarity(fy, gem)
        decayed = ancestry_similarity(fy, gem, temporal_decay=True)
        assert decayed < plain

    def test_temporal_decay_false_unchanged(self):
        from orthography2ipa.json_loader import load_json_spec
        fy = load_json_spec("fy")
        ofs = load_json_spec("ofs")
        plain = ancestry_similarity(fy, ofs, temporal_decay=False)
        plain2 = ancestry_similarity(fy, ofs)
        assert plain == pytest.approx(plain2)

    def test_same_language_always_one(self):
        from orthography2ipa.json_loader import load_json_spec
        fy = load_json_spec("fy")
        assert ancestry_similarity(fy, fy, temporal_decay=True) == pytest.approx(1.0)


# ─────────────────────────────────────────────────────────────────────────────
# weighted_full_distance() with temporal component
# ─────────────────────────────────────────────────────────────────────────────

class TestWeightedFullDistanceTemporal:
    def test_default_temporal_weight_zero_backward_compat(self):
        """w_temporal=0 (default) must reproduce pre-temporal behaviour."""
        from orthography2ipa.json_loader import load_json_spec
        fy = load_json_spec("fy")
        nds = load_json_spec("nds")
        wd = weighted_full_distance(fy, nds)
        # temporal field present but weight=0 → combined identical to old formula
        assert wd.temporal is not None  # data present
        assert wd.weights[4] == 0.0    # w_temporal

    def test_temporal_weight_changes_combined(self):
        from orthography2ipa.json_loader import load_json_spec
        ang = load_json_spec("ang")
        nds = load_json_spec("nds")
        wd_no_temp = weighted_full_distance(ang, nds, w_temporal=0.0)
        wd_with_temp = weighted_full_distance(ang, nds, w_temporal=0.3)
        assert wd_with_temp.combined != pytest.approx(wd_no_temp.combined)

    def test_temporal_none_when_data_missing(self):
        """Languages without timespan produce temporal=None, w_temporal excluded."""
        from orthography2ipa.json_loader import load_json_spec
        # Find two languages without timespan
        from orthography2ipa.json_loader import load_all_json_specs
        specs = load_all_json_specs()
        no_ts = [s for s in specs.values() if s.timespan is None]
        if len(no_ts) < 2:
            pytest.skip("Not enough languages without timespan for this test")
        a, b = no_ts[0], no_ts[1]
        wd = weighted_full_distance(a, b, w_temporal=0.2)
        assert wd.temporal is None

    def test_weights_tuple_length_five(self):
        from orthography2ipa.json_loader import load_json_spec
        fy = load_json_spec("fy")
        nds = load_json_spec("nds")
        wd = weighted_full_distance(fy, nds)
        assert len(wd.weights) == 5


# ─────────────────────────────────────────────────────────────────────────────
# JSON round-trip
# ─────────────────────────────────────────────────────────────────────────────

class TestJsonRoundTrip:
    def test_ang_timespan_loaded(self):
        from orthography2ipa.json_loader import load_json_spec
        ang = load_json_spec("ang")
        assert ang.timespan is not None
        assert ang.timespan.start_year == 450
        assert ang.timespan.end_year == 1150

    def test_fy_living_timespan(self):
        from orthography2ipa.json_loader import load_json_spec
        fy = load_json_spec("fy")
        assert fy.timespan is not None
        assert fy.timespan.end_year is None

    def test_gem_bce_timespan(self):
        from orthography2ipa.json_loader import load_json_spec
        gem = load_json_spec("gem")
        assert gem.timespan is not None
        assert gem.timespan.start_year < 0  # BCE
