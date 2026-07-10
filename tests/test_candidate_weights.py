"""Tests for per-spec candidate weights (E2 layer 1).

Covers the shared weight→cost helper, loader normalisation of the two
JSON grapheme shapes, byte-identical plain-list behaviour in both beam
paths (phonetok and the g2p positional beam), and the own-only
inheritance decision.
"""
from __future__ import annotations

import math
import warnings

import pytest

from orthography2ipa.registry import get
from orthography2ipa.phonetok import PhonetokTokenizer, Token, TokenKind
from orthography2ipa.types import (
    FIELD_INHERITANCE,
    InheritanceMode,
    LanguageSpec,
)
from orthography2ipa.weights import (
    WEIGHT_FLOOR,
    candidate_base_costs,
    normalize_grapheme_value,
    split_weighted_graphemes,
)


def _graph_token(grapheme: str, ipa) -> Token:
    return Token(kind=TokenKind.GRAPHEME, grapheme=grapheme,
                 ipa=tuple(ipa), position=0, length=len(grapheme))


# ── candidate_base_costs ───────────────────────────────────────────────

class TestCandidateBaseCosts:
    def test_plain_is_rank(self):
        assert candidate_base_costs(["k", "s"], None) == [0.0, 1.0]
        assert candidate_base_costs(["a", "b", "c"]) == [0.0, 1.0, 2.0]

    def test_empty(self):
        assert candidate_base_costs([], None) == []

    def test_weighted_is_neg_log_prob(self):
        costs = candidate_base_costs(["k", "s"], [0.9, 0.1])
        assert costs == [-math.log(0.9), -math.log(0.1)]

    def test_weights_normalised_over_sum(self):
        # Unnormalised weights (sum=4) still yield a proper distribution.
        costs = candidate_base_costs(["a", "b"], [3, 1])
        assert costs == [-math.log(0.75), -math.log(0.25)]

    def test_lower_weight_costs_more(self):
        costs = candidate_base_costs(["a", "b"], [0.7, 0.3])
        assert costs[1] > costs[0]

    def test_zero_weight_floored_not_infinite(self):
        costs = candidate_base_costs(["a", "b"], [1.0, 0.0])
        assert costs[1] == pytest.approx(-math.log(WEIGHT_FLOOR))
        assert math.isfinite(costs[1])

    def test_wrong_length_falls_back_to_rank(self):
        with pytest.warns(UserWarning):
            costs = candidate_base_costs(["a", "b"], [0.9], grapheme="x")
        assert costs == [0.0, 1.0]

    def test_negative_weight_falls_back_to_rank(self):
        with pytest.warns(UserWarning):
            costs = candidate_base_costs(["a", "b"], [1.0, -0.5])
        assert costs == [0.0, 1.0]

    def test_all_zero_falls_back_to_rank(self):
        with pytest.warns(UserWarning):
            costs = candidate_base_costs(["a", "b"], [0.0, 0.0])
        assert costs == [0.0, 1.0]


# ── normalisation of the two JSON shapes ───────────────────────────────

class TestNormalisation:
    def test_plain_list_shape(self):
        assert normalize_grapheme_value(["k", "s"]) == (["k", "s"], None)

    def test_weighted_object_shape(self):
        assert normalize_grapheme_value(
            {"ipa": ["k", "s"], "weights": [0.9, 0.1]}
        ) == (["k", "s"], [0.9, 0.1])

    def test_object_without_weights(self):
        assert normalize_grapheme_value({"ipa": ["k"]}) == (["k"], None)

    def test_none_passthrough(self):
        assert normalize_grapheme_value(None) == (None, None)

    def test_both_shapes_yield_same_ipa(self):
        plain, _ = normalize_grapheme_value(["k", "s"])
        obj, _ = normalize_grapheme_value(
            {"ipa": ["k", "s"], "weights": [0.9, 0.1]})
        assert plain == obj

    def test_split_is_sparse(self):
        graphemes, weights = split_weighted_graphemes({
            "c": ["k", "s"],
            "th": {"ipa": ["θ", "ð"], "weights": [0.7, 0.3]},
        })
        assert graphemes == {"c": ["k", "s"], "th": ["θ", "ð"]}
        # Only the weighted grapheme appears in the weights table.
        assert weights == {"th": [0.7, 0.3]}

    def test_split_preserves_null(self):
        graphemes, weights = split_weighted_graphemes({"x": None})
        assert graphemes == {"x": None}
        assert weights == {}


# ── byte-identical plain behaviour in the phonetok beam ────────────────

class TestPlainBranchesUnchanged:
    def test_ipa_branches_plain_costs_are_rank(self):
        tok = _graph_token("c", ["k", "s"])
        branches = PhonetokTokenizer._ipa_branches(tok, None, None)
        # (ipa, cost): first candidate cost 0.0, alternative cost 1.0.
        assert dict(branches) == {"k": 0.0, "s": 1.0}

    def test_ipa_branches_weighted_costs_are_neg_log(self):
        tok = _graph_token("c", ["k", "s"])
        branches = PhonetokTokenizer._ipa_branches(tok, None, [0.1, 0.9])
        assert dict(branches) == {"k": -math.log(0.1), "s": -math.log(0.9)}

    def test_weighted_beam_order_follows_weights(self):
        # Synthetic single-grapheme spec: 'z' → [x, y] with y favoured.
        spec = LanguageSpec(
            code="zz", name="Synthetic", family="test", script="Latin",
            graphemes={"z": ["x", "y"]},
            allophones={},
            grapheme_weights={"z": [0.1, 0.9]},
        )
        tok = PhonetokTokenizer(spec)
        paths = tok.ipa_beam("z", beam_width=4)
        # Higher-weight candidate 'y' wins despite being declared second.
        assert paths[0].ipa == "y"
        assert paths[1].ipa == "x"

    def test_plain_beam_order_is_declaration_order(self):
        spec = LanguageSpec(
            code="zz", name="Synthetic", family="test", script="Latin",
            graphemes={"z": ["x", "y"]}, allophones={},
        )
        tok = PhonetokTokenizer(spec)
        paths = tok.ipa_beam("z", beam_width=4)
        assert paths[0].ipa == "x"

    def test_weights_for_returns_none_when_absent(self):
        spec = LanguageSpec(
            code="zz", name="Synthetic", family="test", script="Latin",
            graphemes={"z": ["x", "y"]}, allophones={},
        )
        tok = PhonetokTokenizer(spec)
        assert tok.weights_for("z") is None


# ── inheritance: own-only weights, byte-identical children ─────────────

class TestInheritance:
    def test_manifest_decision_is_not_inherited(self):
        assert (FIELD_INHERITANCE["grapheme_weights"]
                is InheritanceMode.NOT_INHERITED)

    def test_weighted_parent_has_weights(self):
        # en-GB is the pilot: it declares weighted graphemes.
        spec = get("en-GB")
        assert spec.grapheme_weights
        assert "er" in spec.grapheme_weights

    def test_child_inherits_plain_ipa_not_weights(self):
        # en-US pulls graphemes from en-GB via graphemes_base but must NOT
        # inherit the weights — it keeps rank ordering (byte-identical to
        # before weights existed).
        parent = get("en-GB")
        child = get("en-US")
        # Same inherited IPA list…
        assert child.graphemes["er"] == parent.graphemes["er"]
        # …but no weights on the child.
        assert not child.grapheme_weights
        tok = PhonetokTokenizer(child)
        assert tok.weights_for("er") is None

    def test_child_override_replaces_ipa_and_weights_together(self):
        # A child spec that re-declares 'z' as a plain list overrides both
        # the parent's ipa and (absence of) weights. Modelled directly on
        # LanguageSpec since weights are own-only: a child's own file, not
        # its parent's, is the sole source of its weights.
        child = LanguageSpec(
            code="zz-child", name="Child", family="test", script="Latin",
            graphemes={"z": ["x", "y"]}, allophones={},
            # no grapheme_weights → rank ordering, regardless of any parent
        )
        tok = PhonetokTokenizer(child)
        assert tok.weights_for("z") is None
        assert tok.ipa_beam("z", beam_width=2)[0].ipa == "x"


# ── pydantic schema accepts weighted form, rejects malformed ───────────

class TestSchemaValidation:
    def _spec(self, graphemes):
        from orthography2ipa.schema import LanguageSpecModel
        return LanguageSpecModel(
            code="zz", name="Z", family="test", script="Latin",
            graphemes=graphemes, allophones={"a": ["a"]},
        )

    def test_accepts_plain_and_weighted(self):
        m = self._spec({
            "a": ["a"],
            "th": {"ipa": ["θ", "ð"], "weights": [0.7, 0.3]},
        })
        assert m.graphemes["th"].weights == [0.7, 0.3]

    def test_rejects_length_mismatch(self):
        import pydantic
        with pytest.raises(pydantic.ValidationError):
            self._spec({"th": {"ipa": ["θ", "ð"], "weights": [1.0]}})

    def test_rejects_negative_weight(self):
        import pydantic
        with pytest.raises(pydantic.ValidationError):
            self._spec({"th": {"ipa": ["θ", "ð"], "weights": [1.0, -0.1]}})

    def test_rejects_zero_sum(self):
        import pydantic
        with pytest.raises(pydantic.ValidationError):
            self._spec({"th": {"ipa": ["θ", "ð"], "weights": [0.0, 0.0]}})


# ── forcing-function test still green ──────────────────────────────────

def test_no_malformed_weights_in_shipped_specs():
    """Every shipped spec's weights are well-formed (length matches, sum>0,
    non-negative) so no warning fires at load time."""
    from orthography2ipa.json_loader import (
        available_json_codes, load_json_spec,
    )
    for code in available_json_codes():
        try:
            spec = load_json_spec(code)
        except Exception:
            continue
        for grapheme, weights in (spec.grapheme_weights or {}).items():
            ipa = spec.graphemes.get(grapheme, [])
            assert len(weights) == len(ipa), (
                f"{code}: weights/ipa length mismatch for {grapheme!r}")
            assert all(w >= 0 for w in weights), (
                f"{code}: negative weight for {grapheme!r}")
            assert sum(weights) > 0, (
                f"{code}: zero weight sum for {grapheme!r}")
