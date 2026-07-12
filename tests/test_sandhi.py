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


# ─── Right-side (right_transform) sandhi ───────────────────────────────────

class TestRightTransform:
    """``SandhiRule.right_transform`` rewrites the RIGHT word of a boundary.

    A left-only rule set cannot state a process whose TARGET is the right word,
    such as Catalan phrase-level spirantization — a PROGRESSIVE
    (left-conditioned) continuant-spreading rule in which the following word's
    initial /b d ɡ/ lenites because the preceding word ends in a continuant:
    ``de decidir`` → [ðə ðəsiˈði]. Both halves of a boundary can fire — ``els
    dos`` voices the left ⟨-s⟩ AND lenites the right ⟨d-⟩ — so the sides
    resolve independently.
    """

    def test_right_transform_rewrites_the_following_word(self):
        engine = SandhiEngine((SandhiRule(
            id="SPIRANT_D", name="spirant-d",
            left_context="[aeiou]$", right_context="^d",
            right_transform="ð"),))
        assert engine.apply(["la", "dona"]) == ["la", "ðona"]
        # ... only when the left context matches
        assert engine.apply(["un", "dona"]) == ["un", "dona"]

    def test_left_and_right_both_fire_at_one_boundary(self):
        engine = SandhiEngine((
            SandhiRule(id="VOICE_S", name="voice-s", left_context="s$",
                       right_context="^[bd]", transform="z"),
            SandhiRule(id="SPIRANT_D", name="spirant-d", left_context="[sz]$",
                       right_context="^d", right_transform="ð"),
        ))
        assert engine.apply(["els", "dos"]) == ["elz", "ðos"]

    def test_left_only_rules_are_unchanged(self):
        """A rule set with no ``right_transform`` behaves exactly as before:
        the first matching rule wins and only the left word is rewritten."""
        engine = SandhiEngine((
            SandhiRule(id="A", name="a", left_context="s$", right_context="^a",
                       transform="z"),
            SandhiRule(id="B", name="b", left_context="s$", right_context="^a",
                       transform="ʃ"),   # never reached: A already fired
        ))
        assert engine.apply(["las", "amigas"]) == ["laz", "amigas"]

    def test_transform_none_leaves_the_left_word_alone(self):
        engine = SandhiEngine((SandhiRule(
            id="R", name="r", left_context="a$", right_context="^b",
            right_transform="β"),))
        assert engine.apply(["la", "bota"]) == ["la", "βota"]
