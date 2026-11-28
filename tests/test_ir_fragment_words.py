"""A plugin fragment's ``words`` table is IR data that ranks after the exceptions and the lexicon."""
import dataclasses
import json
import subprocess
from pathlib import Path

import pytest
from gguf import GGUFReader

from orthography2ipa import G2P, Pipeline, get
from orthography2ipa.export_to_loom import export_to_loom
from orthography2ipa.export_to_loom import main as export_main
from orthography2ipa.ir import layout
from orthography2ipa.ir.compiler import build_ir
from orthography2ipa.ir.interpreter import Interpreter

LUA = Path(__file__).resolve().parent.parent / "scripts" / "ir_lua_cli.lua"


def fragment(**words):
    return {"ir_version": 1, "words": words}


def _lua(doc, text, tmp_path):
    ir = tmp_path / "ir.json"
    ir.write_text(json.dumps(doc), encoding="utf-8")
    proc = subprocess.run(["luajit", str(LUA), str(ir), "1"], input=" ".join(str(ord(c)) for c in text) + "\n",
                          capture_output=True, text=True, check=True)
    return "".join(chr(int(x)) for x in proc.stdout.split())


def test_a_fragment_word_overrides_the_rules():
    rules = G2P("pt-PT").transcribe("casa")
    engine = G2P("pt-PT", pipeline=Pipeline(fragments=(fragment(casa="ˈwx"),)))
    assert rules != "ˈwx"
    assert engine.transcribe("casa") == "ˈwx"
    assert engine.transcribe("Casa") == "ˈwx"


def test_the_exception_beats_the_fragment():
    spec = dataclasses.replace(get("pt-PT"), word_exceptions={"casa": "ˈeks"})
    engine = G2P("pt-PT", spec=spec, pipeline=Pipeline(fragments=(fragment(casa="ˈwx"),)))
    assert engine.transcribe("casa") == "ˈeks"


def test_the_runtime_lexicon_beats_the_fragment():
    engine = G2P("pt-PT", pipeline=Pipeline(lexicon={"casa": "ˈlɛx"}, fragments=(fragment(casa="ˈwx", mesa="ˈms"),)))
    assert engine.transcribe("casa") == "ˈlɛx"
    assert engine.transcribe("mesa") == "ˈms"


def test_a_later_fragment_wins_on_a_duplicate_key():
    engine = G2P("pt-PT", pipeline=Pipeline(fragments=(fragment(casa="ˈwɐn"), fragment(casa="ˈtu"))))
    assert engine.transcribe("casa") == "ˈtu"


@pytest.mark.parametrize("bad, name", [
    ({"ir_version": 1, "marks": {}}, "marks"),
    ({"ir_version": 1, "words": {}, "rescore": []}, "rescore"),
    ({"ir_version": 2, "words": {}}, "2"),
    ({"words": {}}, "None"),
    ({"ir_version": 1, "words": {"Casa": "x"}}, "Casa"),
    ({"ir_version": 1, "words": {"casa": 3}}, "casa"),
    ({"ir_version": 1, "words": {"casá": "x"}}, "casá"),
])
def test_a_bad_fragment_is_refused_by_name(bad, name):
    with pytest.raises(ValueError, match=name):
        build_ir("pt-PT", fragments=(bad,))


@pytest.mark.parametrize("code", ["pt-PT", "en-GB", "ar", "ko"])
def test_no_fragment_leaves_the_ir_byte_identical(code):
    plain = layout.encode(build_ir(code))
    assert layout.canonical_bytes(layout.encode(build_ir(code, fragments=()))) == layout.canonical_bytes(plain)
    assert "words" not in plain["word"]


def test_the_fragment_changes_the_revision():
    plain = layout.spec_revision(build_ir("kab"))
    with_words = layout.spec_revision(build_ir("kab", fragments=(fragment(a="b"),)))
    other = layout.spec_revision(build_ir("kab", fragments=(fragment(a="c"),)))
    assert len({plain, with_words, other}) == 3


def test_the_ir_cache_key_covers_the_fragments():
    from orthography2ipa.ir import cache
    base = cache.cache_key("kab", cache.DEFAULT_OPTIONS)
    assert cache.cache_key("kab", {**cache.DEFAULT_OPTIONS, "fragments": ()}) == base
    one = cache.cache_key("kab", {**cache.DEFAULT_OPTIONS, "fragments": (fragment(a="b"),)})
    two = cache.cache_key("kab", {**cache.DEFAULT_OPTIONS, "fragments": (fragment(a="c"),)})
    assert len({base, one, two}) == 3


def test_both_interpreters_give_the_same_output_for_a_fragment_word(tmp_path):
    doc = layout.encode(build_ir("pt-PT", fragments=(fragment(casa="ˈwx"),)))
    assert Interpreter(doc).transcribe("casa") == "ˈwx"
    assert _lua(doc, "casa", tmp_path) == "ˈwx"
    assert _lua(doc, "Casa mesa", tmp_path) == Interpreter(doc).transcribe("Casa mesa")


def test_the_exception_beats_the_fragment_in_both_interpreters(tmp_path):
    spec = dataclasses.replace(get("pt-PT"), word_exceptions={"casa": "ˈeks"})
    doc = layout.encode(build_ir("pt-PT", spec=spec, fragments=(fragment(casa="ˈwx"),)))
    assert Interpreter(doc).transcribe("casa") == "ˈeks"
    assert _lua(doc, "casa", tmp_path) == "ˈeks"


def test_the_ruleset_names_the_revision_with_the_fragment(tmp_path):
    frag = fragment(casa="ˈwx")
    path = tmp_path / "frag.json"
    path.write_text(json.dumps(frag), encoding="utf-8")
    out = tmp_path / "frag.gguf"
    export_main(["--langs", "pt-PT", "--out", str(out), "--fragment", str(path)])
    ruleset = GGUFReader(str(out)).fields["loom.phonemizer.ruleset"].contents()
    with_fragment = layout.spec_revision(build_ir("pt-PT", fragments=(frag,)))
    assert ruleset.endswith(f"; pt-PT={with_fragment}")
    assert with_fragment != layout.spec_revision(build_ir("pt-PT"))
