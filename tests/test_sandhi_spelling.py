"""A spec ``SandhiRule`` can condition on the spelling of the left and the right word.

``left_spelling`` and ``right_spelling`` compile to the ``sandhi_spelling``
primitive and read the word alone: in ⟨casa-mesa⟩ the right word reads ``mesa``.
``left_joined_spelling`` and ``right_joined_spelling`` compile to the
``sandhi_joined`` primitive and read the joined spelling, which adds the one word
before a hyphen: the right word of ⟨casa-mesa⟩ reads ``casa-mesa``
(docs/ir/o2i-ir-v1.md, 3.10.1).
"""
import dataclasses
import json
import subprocess
from pathlib import Path

import pytest

import orthography2ipa
from orthography2ipa.ir import layout
from orthography2ipa.ir.compiler import build_ir
from orthography2ipa.ir.interpreter import Interpreter
from orthography2ipa.sandhi import SandhiEngine
from pydantic import ValidationError

from orthography2ipa.schema import SandhiRuleModel
from orthography2ipa.types import SandhiRule

LUA = Path(__file__).resolve().parent.parent / "scripts" / "ir_lua_cli.lua"

#: Rewrites a final [ɐ] to A, the marker the tests look for.
FINAL = dict(id="T_FINAL", name="test", left_context="ɐ$", right_context="", transform="A")


def _spec(*rules):
    """pt-PT with only *rules* as its sandhi rules."""
    return dataclasses.replace(orthography2ipa.get("pt-PT"), sandhi_rules=tuple(rules))


def _lua(doc, text, tmp_path):
    ir = tmp_path / "ir.json"
    ir.write_text(json.dumps(doc), encoding="utf-8")
    proc = subprocess.run(["luajit", str(LUA), str(ir), "1"], input=" ".join(str(ord(c)) for c in text) + "\n",
                          capture_output=True, text=True, check=True)
    return "".join(chr(int(x)) for x in proc.stdout.split())


def both(rule, text, tmp_path):
    """The output of both interpreters for *text* under the one spec *rule*; they must agree."""
    doc = layout.encode(build_ir("pt-PT", spec=_spec(rule)))
    python, lua = Interpreter(doc).transcribe(text), _lua(doc, text, tmp_path)
    assert python == lua
    return python


@pytest.mark.parametrize("extra, text, expected", [
    ({}, "casa mesa", "ˈkazA ˈmezɐ"),
    ({"left_spelling": "^c"}, "casa mesa", "ˈkazA ˈmezɐ"),
    ({"left_spelling": "^c"}, "mesa casa", "ˈmezɐ ˈkazɐ"),
    ({"right_spelling": "^m"}, "casa mesa", "ˈkazA ˈmezɐ"),
    ({"right_spelling": "^m"}, "casa casa", "ˈkazɐ ˈkazɐ"),
    ({"left_spelling": "^c", "right_spelling": "^m"}, "casa casa", "ˈkazɐ ˈkazɐ"),
    ({"left_spelling": "^casa$"}, "Casa mesa", "ˈkazA ˈmezɐ"),
])
def test_a_spec_rule_reads_the_spelling_in_both_interpreters(extra, text, expected, tmp_path):
    assert both(SandhiRule(**FINAL, **extra), text, tmp_path) == expected


@pytest.mark.parametrize("extra, text, fires", [
    # The spelling of a word is the word alone, also after a hyphen.
    ({"right_spelling": "^mesa$"}, "casa-mesa", True),
    ({"left_spelling": "^casa$"}, "mesa-casa mesa", True),
    # The joined spelling adds the word before and a hyphen, and spans two words.
    ({"right_joined_spelling": "^casa-mesa$"}, "casa-mesa", True),
    ({"right_joined_spelling": "^casa-mesa$"}, "casa mesa", False),
    ({"right_joined_spelling": "^mesa$"}, "casa-mesa", False),
    ({"left_joined_spelling": "^mesa-casa$"}, "mesa-casa mesa", True),
    ({"left_joined_spelling": "^casa$"}, "mesa-casa mesa", False),
    ({"left_joined_spelling": "^casa$"}, "casa-mesa", True),
    ({"right_joined_spelling": "^casa-mesa-casa$"}, "casa-mesa-casa", False),
])
def test_the_joined_spelling_adds_the_word_before_a_hyphen(extra, text, fires, tmp_path):
    plain = both(SandhiRule(**{**FINAL, "transform": "ɐ"}), text, tmp_path)
    assert (both(SandhiRule(**FINAL, **extra), text, tmp_path) != plain) is fires


def test_a_long_hyphen_chain_matches_in_linear_depth(tmp_path):
    # Each spelling spans at most two words, so a pattern with a repetition
    # recurses no deeper on a 2000-character chain than on two words.
    rule = SandhiRule(**FINAL, left_spelling="^(?:.*a)?$", left_joined_spelling="^(?:.*-)?casa$",
                      right_joined_spelling="(?:.*-)?casa$")
    text = "-".join(["casa"] * 400)
    assert len(text) > 1990
    out = both(rule, text, tmp_path)
    assert out.count("A") == 399


def test_the_fields_compile_to_the_sandhi_spelling_primitives():
    rule = SandhiRule(**FINAL, left_spelling="^c", right_spelling="^m")
    ir = build_ir("pt-PT", spec=_spec(rule))
    assert {"left_spelling", "right_spelling"} <= ir["sandhi"][0].keys()
    assert "sandhi_spelling=1" in layout.manifest(ir)
    assert "sandhi_joined" not in layout.manifest(ir)
    joined = build_ir("pt-PT", spec=_spec(SandhiRule(**FINAL, left_joined_spelling="^c")))
    assert "left_joined_spelling" in joined["sandhi"][0]
    assert "sandhi_joined=1" in layout.manifest(joined)
    assert "sandhi_spelling" not in layout.manifest(build_ir("pt-PT", spec=_spec(SandhiRule(**FINAL))))


def test_a_rule_without_the_fields_keeps_its_ir():
    assert build_ir("pt-PT", spec=_spec(SandhiRule(**FINAL)))["sandhi"][0].keys() == {
        "left", "right", "obligatory", "left_out"}


@pytest.mark.parametrize("field", ["left_spelling", "right_spelling", "left_joined_spelling",
                                   "right_joined_spelling"])
def test_the_schema_refuses_a_spelling_that_is_not_a_regex(field):
    SandhiRuleModel.model_validate({**FINAL, field: "^c"})
    with pytest.raises(ValidationError, match="not a valid regex"):
        SandhiRuleModel.model_validate({**FINAL, field: "("})


def test_the_reference_engine_reads_the_spellings():
    rule = SandhiRule(id="T", name="t", left_context="$", right_context="^ɑ̃$", transform="t‿",
                      left_spelling="^cent$")
    engine = SandhiEngine((rule,))
    assert engine.apply(["sɑ̃", "ɑ̃"], spellings=["cent", "ans"]) == ["sɑ̃t‿", "ɑ̃"]
    assert engine.apply(["sɑ̃", "ɑ̃"], spellings=["sang", "ans"]) == ["sɑ̃", "ɑ̃"]
    assert engine.apply(["sɑ̃", "ɑ̃"]) == ["sɑ̃", "ɑ̃"]
    with pytest.raises(ValueError, match="spellings"):
        engine.apply(["sɑ̃", "ɑ̃"], spellings=["cent"])


def test_the_reference_engine_reads_the_joined_spellings():
    rule = SandhiRule(id="T", name="t", left_context="$", right_context="", transform="t",
                      left_joined_spelling="^(?!quatre-vingt$)", left_spelling="^vingt$")
    engine = SandhiEngine((rule,))
    words = ["vɛ̃", "dø"]
    assert engine.apply(words, spellings=["vingt", "deux"]) == ["vɛ̃t", "dø"]
    assert engine.apply(words, spellings=["vingt", "deux"],
                        joined_spellings=["quatre-vingt", "vingt-deux"]) == ["vɛ̃", "dø"]


def test_a_spelling_free_rule_runs_without_spellings():
    block = SandhiRule(id="B", name="b", left_context="$", right_context="", transform="",
                       right_spelling="^h")
    link = SandhiRule(id="L", name="l", left_context="t$", right_context="^a", transform="t‿")
    engine = SandhiEngine((block, link))
    assert engine.apply(["sɛt", "aʃ"]) == ["sɛt‿", "aʃ"]
    assert engine.apply(["sɛt", "aʃ"], spellings=["cette", "hache"]) == ["sɛt", "aʃ"]


def test_the_joined_rule_rewrites_the_word_of_its_boundary(tmp_path):
    # In casa-mesa-casa only the pair mesa-casa has the joined spelling
    # mesa-casa on its right, so only mesa, the left word of that pair, changes.
    rule = SandhiRule(**FINAL, right_joined_spelling="^mesa-casa$")
    plain = both(SandhiRule(**{**FINAL, "transform": "ɐ"}), "casa-mesa-casa", tmp_path)
    out = both(rule, "casa-mesa-casa", tmp_path)
    words, plain_words = out.split(" "), plain.split(" ")
    assert words[0] == plain_words[0] and words[2] == plain_words[2]
    assert words[1] == plain_words[1][:-1] + "A"


def test_existing_positional_arguments_keep_their_meaning():
    rule = SandhiRule("T", "test", "$", "^a", "t", None, False, "note")
    assert (rule.obligatory, rule.notes) == (False, "note")
    assert rule.left_spelling is None and rule.right_joined_spelling is None
