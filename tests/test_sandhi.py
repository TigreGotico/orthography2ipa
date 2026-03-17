"""Tests for sandhi module."""
from orthography2ipa.sandhi import SandhiEngine
from orthography2ipa.types import SandhiRule


class TestSandhiEngine:
    def test_empty_rules_noop(self):
        engine = SandhiEngine(())
        assert engine.apply(["abc", "def"]) == ["abc", "def"]

    def test_single_word_noop(self):
        rules = (SandhiRule(
            id="TEST", name="test", left_context=r"z$",
            right_context=r"^[aeiou]", transform="z‿",
        ),)
        engine = SandhiEngine(rules)
        assert engine.apply(["lez"]) == ["lez"]

    def test_french_liaison_z(self):
        rules = (SandhiRule(
            id="FR_LIAISON_Z", name="z-liaison",
            left_context=r"z$", right_context=r"^[aeiou]",
            transform="z‿",
        ),)
        engine = SandhiEngine(rules)
        result = engine.apply(["lez", "ami"])
        assert result == ["lez‿", "ami"]

    def test_no_match_no_change(self):
        rules = (SandhiRule(
            id="FR_LIAISON_Z", name="z-liaison",
            left_context=r"z$", right_context=r"^[aeiou]",
            transform="z‿",
        ),)
        engine = SandhiEngine(rules)
        result = engine.apply(["lez", "pɑʁi"])
        assert result == ["lez", "pɑʁi"]

    def test_obligatory_filter(self):
        rules = (
            SandhiRule(
                id="OPT", name="optional",
                left_context=r"z$", right_context=r"^[a]",
                transform="z‿", obligatory=False,
            ),
            SandhiRule(
                id="OBL", name="obligatory",
                left_context=r"n$", right_context=r"^[a]",
                transform="n‿", obligatory=True,
            ),
        )
        engine = SandhiEngine(rules)
        result = engine.apply(["lez", "ami"], obligatory_only=True)
        assert result == ["lez", "ami"]  # optional rule skipped

    def test_sandhi_rule_frozen(self):
        rule = SandhiRule(id="X", name="x", left_context="a", right_context="b", transform="c")
        assert rule.id == "X"
        assert rule.obligatory is True
        assert rule.notes == ""

    def test_multiple_boundaries(self):
        rules = (SandhiRule(
            id="TEST", name="test", left_context=r"s$",
            right_context=r"^[aeiou]", transform="z",
        ),)
        engine = SandhiEngine(rules)
        result = engine.apply(["les", "amis", "ici"])
        assert result[0] == "lez"
        assert result[1] == "amiz"
