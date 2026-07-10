"""Tests for orthography2ipa.json_loader — manifest-driven inheritance.

Covers the OVERLAY_BY_ID resolution of ``sandhi_rules`` through the same
structural base edge used by ``graphemes_base`` / ``parent`` (see
``FIELD_INHERITANCE`` in ``orthography2ipa/types.py``).
"""
from orthography2ipa.json_loader import _overlay_by_id, load_json_spec
from orthography2ipa.types import SandhiRule


def _rule(id_, transform="x"):
    return SandhiRule(
        id=id_, name=id_, left_context="a$", right_context="^a", transform=transform,
    )


class TestOverlayById:
    def test_base_only_rules_are_inherited(self):
        base = (_rule("A"), _rule("B"))
        assert _overlay_by_id(base, ()) == base

    def test_own_rule_with_new_id_is_appended(self):
        base = (_rule("A"),)
        own = (_rule("B"),)
        merged = _overlay_by_id(base, own)
        assert [r.id for r in merged] == ["A", "B"]

    def test_own_rule_with_matching_id_overrides_in_place_no_duplicate(self):
        """A leaf spec re-declaring a base rule's id (e.g. ar.json
        re-declaring arb.json's AR_SUN_ASSIMILATION) must replace it at the
        same position, not duplicate it."""
        base = (_rule("A", transform="base"), _rule("B"))
        own = (_rule("A", transform="override"),)
        merged = _overlay_by_id(base, own)
        assert [r.id for r in merged] == ["A", "B"]
        assert merged[0].transform == "override"


class TestSandhiRulesInheritance:
    """End-to-end: sandhi_rules now actually inherits through the JSON
    loader, closing the gap where pt-PT-x-* dialects and other
    graphemes_base descendants never saw their base's cross-word rules."""

    def test_pt_dialect_inherits_base_sandhi_rules(self):
        base = load_json_spec("pt-PT")
        dialect = load_json_spec("pt-PT-x-lisbon")
        assert dialect.sandhi_rules  # previously empty before the manifest fix
        assert {r.id for r in dialect.sandhi_rules} == {r.id for r in base.sandhi_rules}

    def test_ar_inherits_arb_sandhi_rules_without_duplication(self):
        base = load_json_spec("arb")
        leaf = load_json_spec("ar")
        base_ids = {r.id for r in base.sandhi_rules}
        leaf_ids = [r.id for r in leaf.sandhi_rules]
        # every arb rule id appears, and each id appears exactly once
        assert base_ids <= set(leaf_ids)
        assert len(leaf_ids) == len(set(leaf_ids))
