"""An override key drops the spec's silent stress marks, in both interpreters."""
import json
import subprocess
from pathlib import Path

import pytest

from orthography2ipa.ir import layout
from orthography2ipa.ir.compiler import build_ir
from orthography2ipa.ir.interpreter import Interpreter

LUA = Path(__file__).resolve().parent.parent / "scripts" / "ir_lua_cli.lua"


@pytest.fixture(scope="module")
def ru_doc():
    doc = layout.encode(build_ir("ru"))
    return doc


def _lua(doc, text, tmp_path):
    ir = tmp_path / "ru.json"
    ir.write_text(json.dumps(doc), encoding="utf-8")
    proc = subprocess.run(["luajit", str(LUA), str(ir), "1"], input=" ".join(str(ord(c)) for c in text) + "\n",
                          capture_output=True, text=True, check=True)
    return "".join(chr(int(x)) for x in proc.stdout.split())


def test_python_finds_the_entry_of_the_unmarked_word(ru_doc):
    it = Interpreter(ru_doc)
    assert it.transcribe("его́") == it.transcribe("его") == "jɪˈvo"


def test_lua_finds_the_entry_of_the_unmarked_word(ru_doc, tmp_path):
    assert _lua(ru_doc, "его́", tmp_path) == _lua(ru_doc, "его", tmp_path) == "jɪˈvo"


def test_both_interpreters_find_a_hangul_exception_with_a_final_consonant(tmp_path):
    import dataclasses
    from orthography2ipa import get
    from orthography2ipa.ir.compiler import build_ir as build

    doc = layout.encode(build("ko", spec=dataclasses.replace(get("ko"), word_exceptions={"한국어": "WX"})))
    assert Interpreter(doc).transcribe("한국어") == "WX"
    assert _lua(doc, "한국어", tmp_path) == "WX"
