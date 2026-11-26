"""The IR conformance vectors of section 8.4 hold for the Python interpreter and Lua.

Each vector file embeds its IR, so a spec change does not make these tests
fail. ``scripts/gen_ir_vectors.py --lang X`` writes the file of one spec again.
"""
import json
import shutil
import subprocess
from pathlib import Path

import pytest

from orthography2ipa.ir.interpreter import Interpreter

REPO = Path(__file__).resolve().parent.parent
VECTORS = sorted((REPO / "tests" / "conformance" / "ir-v1").glob("*.jsonl"))
RUNNER = REPO / "scripts" / "ir_lua_conformance.lua"
CODES = [*json.loads((REPO / "tests" / "data" / "ir_golden_ci.json").read_text(encoding="utf-8")), "kab"]


def load(path):
    with path.open(encoding="utf-8") as f:
        head, *cases = [json.loads(line) for line in f]
    assert head["kind"] == "ir" and all(c["kind"] == "case" for c in cases)
    return head, cases


def text(cps):
    return "".join(map(chr, cps))


def test_the_vector_set_covers_every_spec():
    assert sorted(p.stem for p in VECTORS) == sorted([*CODES, "unknown-version"])
    for path in VECTORS:
        assert len(load(path)[1]) >= (1 if path.stem == "unknown-version" else 20), path.stem


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


@pytest.mark.skipif(shutil.which("luajit") is None, reason="luajit is not installed")
def test_lua_interpreter_gives_every_expect():
    proc = subprocess.run(["luajit", str(RUNNER), *map(str, VECTORS)], capture_output=True, text=True)
    n = sum(len(load(p)[1]) for p in VECTORS)
    assert proc.stdout.splitlines()[-1] == f"total: files {len(VECTORS)}, N in {n}, N pass {n}, N fail 0", proc.stdout
    assert proc.returncode == 0
