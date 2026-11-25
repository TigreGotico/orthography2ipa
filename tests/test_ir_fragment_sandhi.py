"""A plugin fragment's ``sandhi`` rules are IR rules with a spelling and a pause condition."""
import json
import subprocess
from pathlib import Path

import pytest
from gguf import GGUFReader

from orthography2ipa import G2P, Pipeline
from orthography2ipa.export_to_loom import export_to_loom
from orthography2ipa.ir import layout
from orthography2ipa.ir.compiler import build_ir
from orthography2ipa.ir.interpreter import Interpreter, IRVersionError

HERE = Path(__file__).resolve().parent
LUA = HERE.parent / "orthography2ipa" / "ir" / "interpreter.lua"
ARBTOK = json.loads((HERE / "data" / "arbtok_sandhi_fragment.json").read_text(encoding="utf-8"))


def fragment(*rules, unsupported=()):
    return {"ir_version": 1, "sandhi": list(rules), "unsupported": list(unsupported)}


def _lua(doc, text, tmp_path):
    ir = tmp_path / "ir.json"
    ir.write_text(json.dumps(doc), encoding="utf-8")
    proc = subprocess.run(["luajit", str(LUA), str(ir), "1"], input=" ".join(str(ord(c)) for c in text) + "\n",
                          capture_output=True, text=True, check=True)
    return "".join(chr(int(x)) for x in proc.stdout.split())


def both(frag, text, tmp_path):
    """The output of the Python and the Lua interpreter for *text*, which must agree."""
    doc = layout.encode(build_ir("pt-PT", fragments=(frag,)))
    python, lua = Interpreter(doc).transcribe(text), _lua(doc, text, tmp_path)
    assert python == lua
    return python


FINAL = {"left": "ɐ$", "left_out": "A"}


@pytest.mark.parametrize("rule, text, expected", [
    ({"pause": True, **FINAL}, "casa mesa", "ˈkazɐ ˈmezA"),
    ({"pause": True, **FINAL}, "casa", "ˈkazA"),
    ({"pause": True, **FINAL}, "casa, mesa", "ˈkazA ˈmezA"),
    ({"pause": True, **FINAL, "left_spelling": "^m"}, "casa mesa", "ˈkazɐ ˈmezA"),
    ({"pause": True, **FINAL, "left_spelling": "^m"}, "mesa casa", "ˈmezɐ ˈkazɐ"),
    ({**FINAL}, "casa mesa", "ˈkazA ˈmezɐ"),
    ({**FINAL}, "casa, mesa", "ˈkazɐ ˈmezɐ"),
    ({**FINAL, "right_spelling": "^m"}, "casa mesa", "ˈkazA ˈmezɐ"),
    ({**FINAL, "right_spelling": "^m"}, "casa casa", "ˈkazɐ ˈkazɐ"),
    ({**FINAL, "left_spelling": "^c"}, "casa mesa", "ˈkazA ˈmezɐ"),
    ({**FINAL, "left_spelling": "^c"}, "mesa casa", "ˈmezɐ ˈkazɐ"),
    ({"right": "^(ˈ?)m", "right_out": "\\1A"}, "casa mesa", "ˈkazɐ ˈAezɐ"),
])
def test_the_pause_and_spelling_conditions_in_both_interpreters(rule, text, expected, tmp_path):
    assert both(fragment(rule), text, tmp_path) == expected


def test_the_first_matching_pause_rule_wins(tmp_path):
    frag = fragment({"pause": True, **FINAL}, {"pause": True, "left": "ɐ$", "left_out": "B"})
    assert both(frag, "casa", tmp_path) == "ˈkazA"


def test_a_fragment_rule_runs_after_the_spec_rules():
    spec_rules = build_ir("ar")["sandhi"]
    merged = build_ir("ar", fragments=(fragment({"pause": True, **FINAL}),))["sandhi"]
    assert spec_rules and merged[:len(spec_rules)] == spec_rules and len(merged) == len(spec_rules) + 1


def test_the_spec_switch_does_not_turn_off_a_fragment_rule():
    engine = G2P("pt-PT", apply_sandhi=False, pipeline=Pipeline(fragments=(fragment({"pause": True, **FINAL}),)))
    assert engine.transcribe("casa") == "ˈkazA"


def test_the_arbtok_nun_rules_assimilate_before_r_j_l_and_b():
    engine = G2P("ar", pipeline=Pipeline(fragments=(ARBTOK,)))
    assert engine.transcribe("مِنْ رَبِّهِمْ، مِنْ بَيْتِكَ") == "ˈmir ˈrabbihim ˈmim ˈbajtik"
    assert engine.transcribe("مَنْ يَقُولُ مِنْ لَبَن") == "ˈmaj jaˈquːlu ˈmil ˈlaban"
    assert engine.transcribe("مِنْ مَسْجِد") == "ˈmin ˈmasdʒid"


@pytest.mark.parametrize("text, expected", [
    ("قَلَمٌ", "ˈqalam"),
    ("كِتَابٌ.", "kiˈtaːb"),
    ("قَاضٍ.", "ˈqɑːdˤ"),
    ("كِتَابًا", "kiˈtaːbaː"),
    ("مَدِينَةٌ", "maˈdiːna"),
    ("مَدِينَةً.", "maˈdiːna"),
    ("كَتَبَ.", "ˈkatab"),
    ("يَقُولُ،", "jaˈquːl"),
    ("بَيْتِكَ.", "ˈbajtik"),
    ("مَدْرَسَةُ.", "madˈrasa"),
    ("مَدْرَسَةِ.", "madˈrasa"),
    ("مُؤْمِن", "ˈmuʔmin"),
    ("هُوَ", "ˈhuwa"),
    ("نَحْنُ", "ˈnaħnu"),
    ("مَدْرَسَة", "ˈmadrasa"),
])
def test_the_arbtok_pause_rules_read_the_spelling_of_the_word(text, expected):
    """The gold is what ``arbtok.o2i_plugins.ArbtokSandhi`` returns for the same input."""
    assert G2P("ar", pipeline=Pipeline(fragments=(ARBTOK,))).transcribe(text) == expected


def test_a_word_inside_a_sentence_keeps_its_ending_until_a_pause():
    engine = G2P("ar", pipeline=Pipeline(fragments=(ARBTOK,)))
    assert engine.transcribe("قَلَمٌ كِتَابٌ") == "ˈqalamun kiˈtaːb"
    assert engine.transcribe("قَلَمٌ، كِتَابٌ.") == "ˈqalam kiˈtaːb"


@pytest.mark.parametrize("code", ["pt-PT", "en-GB", "ar", "ko"])
def test_no_fragment_leaves_the_ir_byte_identical(code):
    plain = layout.encode(build_ir(code))
    empty = layout.encode(build_ir(code, fragments=({"ir_version": 1},)))
    assert layout.canonical_bytes(empty) == layout.canonical_bytes(plain)
    assert not {"sandhi_spelling", "sandhi_pause"} & set(plain["primitives"])


def test_the_new_fields_have_their_own_semantics_versions():
    assert build_ir("kab", fragments=(fragment(FINAL),))["sandhi"][0].keys() == {"left", "right", "obligatory", "left_out"}
    primitives = lambda *rules: layout.manifest(build_ir("kab", fragments=(fragment(*rules),)))
    assert "sandhi_pause" not in primitives(FINAL) and "sandhi_spelling" not in primitives(FINAL)
    assert "sandhi_pause=1" in primitives({"pause": True, **FINAL})
    assert "sandhi_spelling=1" in primitives({**FINAL, "right_spelling": "^m"})


def test_the_revision_covers_the_rules():
    plain = layout.spec_revision(build_ir("kab"))
    one = layout.spec_revision(build_ir("kab", fragments=(fragment({"pause": True, **FINAL}),)))
    other = layout.spec_revision(build_ir("kab", fragments=(fragment({"pause": True, **FINAL, "left_out": "B"}),)))
    assert len({plain, one, other}) == 3


@pytest.mark.parametrize("field, version", [("sandhi_pause", 2), ("sandhi_spelling", 2)])
def test_both_interpreters_refuse_a_newer_condition(field, version, tmp_path):
    doc = layout.encode(build_ir("pt-PT", fragments=(fragment({"pause": True, **FINAL, "left_spelling": "^m"}),)))
    assert field in doc["primitives"]
    doc["primitives"][field] = version
    with pytest.raises(IRVersionError, match=field):
        Interpreter(doc)
    path = tmp_path / "ir.json"
    path.write_text(json.dumps(doc), encoding="utf-8")
    lua = subprocess.run(["luajit", str(LUA), str(path), "1"], input="99\n", capture_output=True, text=True)
    assert lua.stdout.startswith("E ") and f"unsupported primitive version: {field}" in lua.stdout


@pytest.mark.parametrize("field", ["sandhi_pause", "sandhi_spelling"])
def test_an_interpreter_without_the_condition_refuses_the_ir(field, monkeypatch):
    doc = layout.encode(build_ir("pt-PT", fragments=(fragment({"pause": True, **FINAL, "left_spelling": "^m"}),)))
    monkeypatch.delitem(layout.SEMANTICS, field)
    with pytest.raises(IRVersionError, match=field):
        Interpreter(doc)


@pytest.mark.parametrize("bad, name", [
    ({"ir_version": 1, "sandhi": [{"left": "a", "left_out": "", "mark": "x"}]}, "mark"),
    ({"ir_version": 1, "sandhi": [{"pause": True, "left": "a", "left_out": "", "right": "b"}]}, "right"),
    ({"ir_version": 1, "sandhi": [{"pause": True, "left": "a", "left_out": "", "right_spelling": "b"}]}, "right_spelling"),
    ({"ir_version": 1, "sandhi": [{"pause": 1, "left": "a", "left_out": ""}]}, "pause"),
    ({"ir_version": 1, "sandhi": [{"left": "a"}]}, "left_out"),
    ({"ir_version": 1, "sandhi": [{"pause": True, "left_out": "x"}]}, "needs a left pattern"),
    ({"ir_version": 1, "sandhi": [{"left": "a", "left_out": 3}]}, "left_out"),
    ({"ir_version": 1, "sandhi": [{"left": "(", "left_out": ""}]}, "unterminated"),
    ({"ir_version": 1, "sandhi": [{"left": "a(?=b)*", "left_out": ""}]}, "a\\(\\?=b\\)\\*"),
    ({"ir_version": 1, "sandhi": [{"left": "a", "left_out": "\\q"}]}, "template"),
    ({"ir_version": 1, "sandhi": [{"left": "a", "left_out": "", "left_spelling": "\\b"}]}, "left_spelling|\\\\b"),
    ({"ir_version": 1, "unsupported": [3]}, "unsupported"),
    ({"ir_version": 1, "rescore": []}, "rescore"),
    ({"ir_version": 2, "sandhi": []}, "2"),
])
def test_a_bad_fragment_is_refused_by_name(bad, name):
    with pytest.raises(ValueError, match=name):
        build_ir("pt-PT", fragments=(bad,))


def test_the_export_reports_the_unsupported_rules(tmp_path):
    out = tmp_path / "frag.gguf"
    meta = export_to_loom(["kab"], out, fragments=(fragment(unsupported=["b", "a"]), fragment(unsupported=["a", "c"])))
    assert meta["unsupported"] == ["a", "b", "c"]
    assert GGUFReader(str(out)).fields["o2i.unsupported"].contents() == ["a", "b", "c"]


def test_an_export_without_unsupported_rules_has_no_such_field(tmp_path):
    out = tmp_path / "plain.gguf"
    assert export_to_loom(["kab"], out, fragments=(fragment(),))["unsupported"] == []
    assert "o2i.unsupported" not in GGUFReader(str(out)).fields
