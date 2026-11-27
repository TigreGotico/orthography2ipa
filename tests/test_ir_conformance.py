"""The IR conformance vectors of section 8.4 hold for the Python interpreter and Lua.

Each vector file embeds its IR, so a spec change does not make these tests
fail. ``scripts/gen_ir_vectors.py`` writes the files again.
"""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from orthography2ipa.ir import layout
from orthography2ipa.ir.interpreter import Interpreter

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import gen_ir_vectors  # noqa: E402
from ir_features import ablate, feature_names  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
DIR = REPO / "tests" / "conformance" / "ir-v1"
VECTORS = sorted(DIR.glob("*.jsonl"))
RUNNER = REPO / "scripts" / "ir_lua_conformance.lua"


def load(path):
    with path.open(encoding="utf-8") as f:
        head, *cases = [json.loads(line) for line in f]
    assert head["kind"] == "ir" and all(c["kind"] == "case" for c in cases)
    return head, cases


def text(cps):
    return "".join(map(chr, cps))


def test_the_vector_set_covers_every_spec():
    assert sorted(p.stem for p in VECTORS) == sorted(gen_ir_vectors.stems())
    for path in VECTORS:
        assert len(load(path)[1]) >= 1, path.stem


@pytest.mark.parametrize("path", VECTORS, ids=lambda p: p.stem)
def test_every_file_keeps_the_size_budget(path):
    head, *cases = path.read_text(encoding="utf-8").splitlines(keepends=True)
    assert len(head.encode()) <= gen_ir_vectors.IR_BUDGET
    if path.stem not in gen_ir_vectors.GOLDEN_SPECS:
        assert sum(len(c.encode()) for c in cases) <= gen_ir_vectors.CASE_BUDGET


def test_every_ir_feature_has_a_case_that_needs_it():
    found = json.loads((DIR / gen_ir_vectors.FEATURES).read_text(encoding="utf-8"))
    uncovered = [name for name in feature_names() if name not in found and name not in gen_ir_vectors.UNREACHABLE]
    weak = []
    for name, (file, index) in sorted(found.items()):
        head, cases = load(DIR / file)
        ir = layout.decode(head["ir"])
        case = cases[index]
        ablated = ablate(ir, name)
        if ablated is None or Interpreter(ablated).transcribe(text(case["input"]), width=1) == text(case["expect"]):
            weak.append(name)
    assert not uncovered and not weak, f"uncovered: {uncovered}; the case does not need: {weak}"


@pytest.mark.xfail(strict=True, reason="no case can show these features: see gen_ir_vectors.UNREACHABLE")
def test_every_unreachable_feature_has_a_case():
    found = json.loads((DIR / gen_ir_vectors.FEATURES).read_text(encoding="utf-8"))
    assert [name for name in gen_ir_vectors.UNREACHABLE if name not in found] == []


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
