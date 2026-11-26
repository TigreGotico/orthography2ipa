"""A spec ``SandhiRule`` can condition on the spelling of the left and the right word.

The fields are ``left_spelling`` and ``right_spelling``. They compile to the
``sandhi_spelling`` primitive (docs/ir/o2i-ir-v1.md, 3.10.1), and a word after a
hyphen reads from the start of its compound.
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

LUA = Path(__file__).resolve().parent.parent / "orthography2ipa" / "ir" / "interpreter.lua"

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
    # The second word of a compound reads the compound: "casa-mesa".
    ({"right_spelling": "^mesa$"}, "casa-mesa", False),
    ({"right_spelling": "^casa-mesa$"}, "casa-mesa", True),
    ({"right_spelling": "^casa-mesa$"}, "casa mesa", False),
    # The left word reads the compound up to itself: "mesa-casa" in "mesa-casa mesa".
    ({"left_spelling": "^casa$"}, "mesa-casa mesa", False),
    ({"left_spelling": "-casa$"}, "mesa-casa mesa", True),
    ({"left_spelling": "^casa$"}, "casa-mesa", True),
])
def test_a_word_after_a_hyphen_reads_from_the_start_of_its_compound(extra, text, fires, tmp_path):
    plain = both(SandhiRule(**{**FINAL, "transform": "ɐ"}), text, tmp_path)
    assert (both(SandhiRule(**FINAL, **extra), text, tmp_path) != plain) is fires


def test_the_fields_compile_to_the_sandhi_spelling_primitive():
    rule = SandhiRule(**FINAL, left_spelling="^c", right_spelling="^m")
    ir = build_ir("pt-PT", spec=_spec(rule))
    assert {"left_spelling", "right_spelling"} <= ir["sandhi"][0].keys()
    assert "sandhi_spelling=2" in layout.manifest(ir)
    assert "sandhi_spelling" not in layout.manifest(build_ir("pt-PT", spec=_spec(SandhiRule(**FINAL))))


def test_a_rule_without_the_fields_keeps_its_ir():
    assert build_ir("pt-PT", spec=_spec(SandhiRule(**FINAL)))["sandhi"][0].keys() == {
        "left", "right", "obligatory", "left_out"}


@pytest.mark.parametrize("field", ["left_spelling", "right_spelling"])
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
