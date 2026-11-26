"""The IR conformance vectors of section 8.4 hold for the Python interpreter, the rules engine and Lua."""
import json
import shutil
import subprocess
import warnings
from pathlib import Path

import pytest

from orthography2ipa import G2P
from orthography2ipa.ir.interpreter import Interpreter

REPO = Path(__file__).resolve().parent.parent
VECTORS = sorted((REPO / "tests" / "conformance" / "ir-v1").glob("*.jsonl"))
RUNNER = REPO / "scripts" / "ir_lua_conformance.lua"


def load(path):
    with path.open(encoding="utf-8") as f:
        head, *cases = [json.loads(line) for line in f]
    assert head["kind"] == "ir" and all(c["kind"] == "case" for c in cases)
    return head, cases


def text(cps):
    return "".join(map(chr, cps))


def test_the_vector_set_covers_every_spec():
    assert len(VECTORS) == 22
    assert sum(len(load(p)[1]) for p in VECTORS) == 3881


@pytest.mark.parametrize("path", VECTORS, ids=lambda p: p.stem)
def test_python_interpreter_gives_every_expect(path):
    head, cases = load(path)
    try:
        it = Interpreter(head["ir"])
    except ValueError as exc:
        assert [c["expect_error"] for c in cases] == ["unsupported primitive version"]
        assert str(exc).startswith(cases[0]["expect_error"])
        return
    got = [[ord(c) for c in it.transcribe(text(case["input"]), width=1)] for case in cases]
    assert got == [case["expect"] for case in cases]


@pytest.mark.parametrize("path", [p for p in VECTORS if p.stem != "unknown-version"], ids=lambda p: p.stem)
def test_rules_engine_gives_every_expect(path):
    head, cases = load(path)
    engine = G2P(head["lang"])
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        got = [[ord(c) for c in engine.transcribe(text(case["input"]))] for case in cases]
    assert got == [case["expect"] for case in cases]


@pytest.mark.skipif(shutil.which("luajit") is None, reason="luajit is not installed")
def test_lua_interpreter_gives_every_expect():
    proc = subprocess.run(["luajit", str(RUNNER), *map(str, VECTORS)], capture_output=True, text=True)
    assert proc.stdout.splitlines()[-1] == "total: files 22, N in 3881, N pass 3881, N fail 0", proc.stdout
    assert proc.returncode == 0
