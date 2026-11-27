"""A plugin fragment with ``langs`` enters only the IR of the languages it names."""
import json
import re
import subprocess

import pytest
from gguf import GGUFReader

from orthography2ipa import G2P, Pipeline
from orthography2ipa.export_to_loom import export_to_loom
from orthography2ipa.ir import layout
from orthography2ipa.ir.compiler import build_ir
from orthography2ipa.ir.interpreter import Interpreter

PT_CASA = {"ir_version": 1, "langs": ["pt-PT"], "words": {"casa": "ˈwx"},
           "sandhi": [{"pause": True, "left": "x$", "left_out": "q"}]}


def _driver_ir(reader, code):
    driver = reader.fields["model.driver_script"].contents()
    body = re.search(r'^  \["%s"\] = \[(=*)\[(.*?)\]\1\]' % re.escape(code), driver, flags=re.M | re.S)
    return body.group(2)


def _lua(reader, text, lang, tmp_path):
    driver = tmp_path / "driver.lua"
    driver.write_text(reader.fields["model.driver_script"].contents(), encoding="utf-8")
    call = "dofile(%r); io.write(table.concat(infer{text = {%s}, lang = %d}, ' '))" % (
        str(driver), ", ".join(str(ord(c)) for c in text), lang)
    proc = subprocess.run(["luajit", "-e", call], capture_output=True, text=True, check=True)
    return "".join(chr(int(x)) for x in proc.stdout.split())


def _python(code, text):
    return Interpreter(json.loads(json.dumps(layout.encode(build_ir(code, fragments=(PT_CASA,)))))).transcribe(text)


@pytest.fixture(scope="module")
def exported(tmp_path_factory):
    out = tmp_path_factory.mktemp("loom") / "two.gguf"
    export_to_loom(["kab", "pt-PT"], out, fragments=(PT_CASA,))
    return GGUFReader(str(out))


def test_a_language_outside_the_scope_gets_no_fragment_data(exported):
    def carried(code, fragments=()):
        return json.dumps(layout.encode(build_ir(code, fragments=fragments)), ensure_ascii=False,
                          separators=(",", ":"))
    assert _driver_ir(exported, "kab") == carried("kab")
    assert _driver_ir(exported, "pt-PT") != carried("pt-PT")
    assert _driver_ir(exported, "pt-PT") == carried("pt-PT", (PT_CASA,))
    assert build_ir("kab", fragments=(PT_CASA,)) == build_ir("kab")


def test_the_language_in_the_scope_gets_the_words_and_rules():
    ir = build_ir("pt-PT", fragments=(PT_CASA,))
    assert ir["word"]["words"] == [("casa", "ˈwx")]
    assert len(ir["sandhi"]) == len(build_ir("pt-PT").get("sandhi", ())) + 1


def test_a_code_in_langs_matches_by_resolution():
    assert build_ir("pt-PT", fragments=({**PT_CASA, "langs": ["pt"]},)) == build_ir("pt-PT", fragments=(PT_CASA,))


def test_a_fragment_without_langs_applies_to_every_language():
    everywhere = {k: v for k, v in PT_CASA.items() if k != "langs"}
    assert build_ir("kab", fragments=(everywhere,))["word"]["words"] == [("casa", "ˈwx")]


def test_both_interpreters_read_the_table_only_in_the_scope(exported, tmp_path):
    for lang, code in ((0, "kab"), (1, "pt-PT")):
        assert _lua(exported, "casa", lang, tmp_path) == _python(code, "casa")
    assert _python("pt-PT", "casa") == "ˈwq"
    assert _python("kab", "casa") == G2P("kab").transcribe("casa") != "ˈwq"


def test_the_pipeline_applies_the_same_scope():
    pipeline = Pipeline(fragments=(PT_CASA,))
    assert G2P("pt-PT", pipeline=pipeline).transcribe("casa") == "ˈwq"
    assert G2P("kab", pipeline=pipeline).transcribe("casa") == G2P("kab").transcribe("casa")


@pytest.mark.parametrize("langs", [[], "pt-PT", [1]])
def test_a_bad_langs_is_refused(langs):
    with pytest.raises(ValueError, match="fragment langs"):
        build_ir("kab", fragments=({**PT_CASA, "langs": langs},))


def test_an_out_of_scope_fragment_is_still_checked():
    with pytest.raises(ValueError, match="lowercase NFC"):
        build_ir("kab", fragments=({**PT_CASA, "words": {"Casa": "x"}},))
