"""Compare the Python reference interpreter with the Lua interpreter.

For each language code, the tool compiles the IR once with
``orthography2ipa.ir.compiler``, writes its canonical JSON, and runs the same
texts through ``Interpreter`` (Python) and ``interpreter.lua`` (LuaJIT, one
batch over stdin). Both read the same JSON file and no lexicon, as loom does.
It prints N in, N out, N identical, the mismatches and the speed of each side.

    python -I scripts/ir_lua_parity.py --lang pt-PT --corpus FILE
    python -I scripts/ir_lua_parity.py --dialect-corpus tests/data/ep_dialect_sentences.csv
    python -I scripts/ir_lua_parity.py --lang kab --data-ref 7.30.0 --expected FILE.json
    python -I scripts/ir_lua_parity.py --gold-langs --gold-cache DIR [--lang X ...]
    python -I scripts/ir_lua_parity.py --fuzz
    python -I scripts/ir_lua_parity.py --loom-host BIN --lang kab --data-ref 7.30.0 --expected FILE.json

With --loom-host, the Lua side is the real loom engine: the tool exports a
GGUF with orthography2ipa.export_to_loom and pipes the texts through the host
binary, one text per line. With --expected, it also counts the loom output
that equals the expected IPA.
"""
import argparse
import csv
import json
import random
import re
import subprocess
import sys
import tempfile
import time
import warnings
from pathlib import Path
from typing import List, Optional

warnings.simplefilter("ignore")

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from orthography2ipa import registry  # noqa: E402
from orthography2ipa.ir import layout, pattern  # noqa: E402
from orthography2ipa.ir.compiler import IRUnsupportedFeature, build_ir  # noqa: E402
from orthography2ipa.ir.interpreter import Interpreter  # noqa: E402

LUA = REPO / "orthography2ipa" / "ir" / "interpreter.lua"
CLI = REPO / "scripts" / "ir_lua_cli.lua"
LUAJIT = "luajit"


def _cps(text: str) -> str:
    return " ".join(str(ord(c)) for c in text)


def run_lua(ir_path: Path, texts: List[str], width: int):
    """IPA per text from the Lua interpreter, and its CPU seconds."""
    stdin = "".join(_cps(t) + "\n" for t in texts)
    proc = subprocess.run([LUAJIT, str(CLI), str(ir_path), str(width)], input=stdin,
                          capture_output=True, text=True, check=True)
    lines = proc.stdout.split("\n")[:-1] if proc.stdout else []
    if len(lines) == 1 and lines[0].startswith("E ") and len(texts) != 1:
        raise RuntimeError(f"lua refused the IR: {lines[0][2:]}")
    out = [line if line.startswith("E ") else "".join(chr(int(x)) for x in line.split()) for line in lines]
    m = re.search(r"in ([0-9.]+) s cpu", proc.stderr)
    return out, float(m.group(1)) if m else float("nan")


def run_loom(host: str, code: str, data_ref: Optional[str], texts: List[str], workdir: Path):
    """IPA per text from the loom engine, and its wall seconds."""
    from orthography2ipa.export_to_loom import export_to_loom
    if any("\n" in t or "\r" in t for t in texts):
        raise ValueError("the loom host reads one text per line")
    model = workdir / f"{code}.gguf"
    export_to_loom([code], model, data_ref=data_ref)
    t0 = time.perf_counter()
    proc = subprocess.run([host, str(model), "0"], input="".join(t + "\n" for t in texts),
                          capture_output=True, text=True, check=True)
    seconds = time.perf_counter() - t0
    model.unlink()
    return proc.stdout.split("\n")[:-1], seconds


def run_python(doc: dict, texts: List[str], width: int):
    it = Interpreter(doc)
    out = []
    t0 = time.process_time()
    for text in texts:
        try:
            out.append(it.transcribe(text, width=width))
        except Exception as exc:  # the reference raised: Lua must raise too
            out.append(f"E {type(exc).__name__}: {exc}")
    return out, time.process_time() - t0


def run(code: str, texts: List[str], workdir: Path, *, dialect: Optional[str] = None,
        data_ref: Optional[str] = None, width: int = 1, show: int = 50, source: str = "",
        loom_host: Optional[str] = None, expected: Optional[List[str]] = None) -> dict:
    label = code + (f" dialect={dialect}" if dialect else "") + (f" data_ref={data_ref}" if data_ref else "")
    label += f" [{source}]" if source else ""
    try:
        doc = layout.encode(build_ir(code, data_ref, dialect_profile=dialect))
    except IRUnsupportedFeature as exc:
        print(f"{label}: refused: {exc.feature}", flush=True)
        return {"label": label, "refused": exc.feature}
    ir_path = workdir / f"{code}-{dialect or 'none'}-{data_ref or 'head'}.json"
    ir_path.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
    doc = json.loads(ir_path.read_text(encoding="utf-8"))
    py, py_s = run_python(doc, texts, width)
    if loom_host:
        lua, lua_s = run_loom(loom_host, code, data_ref, texts, workdir)
        label += " [loom]"
    else:
        lua, lua_s = run_lua(ir_path, texts, width)
    ir_path.unlink()
    same = sum(a == b for a, b in zip(py, lua))
    py_err = sum(a.startswith("E ") for a in py)
    lua_err = sum(b.startswith("E ") for b in lua)
    bad = [(t, a, b) for t, a, b in zip(texts, py, lua) if a != b]
    rate = lambda s: len(texts) / s if s > 0 else float("inf")  # noqa: E731
    print(f"{label}: N in {len(texts)}, N out {len(lua)}, N identical {same}, mismatches {len(texts) - same}"
          f" (errors py {py_err} lua {lua_err}; python {rate(py_s):.0f} texts/s, lua {rate(lua_s):.0f} texts/s)",
          flush=True)
    for t, a, b in bad[:show]:
        print(f"  {t!r} | python {a!r} | lua {b!r}", flush=True)
    if expected is not None:
        hit = sum(a == b for a, b in zip(expected, lua))
        print(f"{label} against the expected IPA: N in {len(expected)}, N identical {hit}, "
              f"mismatches {len(expected) - hit}", flush=True)
        for t, a, b in [(t, a, b) for t, a, b in zip(texts, expected, lua) if a != b][:show]:
            print(f"  {t!r} | expected {a!r} | got {b!r}", flush=True)
    return {"label": label, "n_in": len(texts), "n_out": len(lua), "same": same,
            "py_errors": py_err, "lua_errors": lua_err, "py_s": py_s, "lua_s": lua_s}


def dialect_texts(path: Path) -> List[str]:
    with path.open(encoding="utf-8") as f:
        return [row["text"] for row in csv.DictReader(f)]


def gold_words(code: str, limit: int, cache: Optional[str]):
    """The words of the language's WikiPron gold set, else its word_exceptions."""
    if cache:
        sys.path.insert(0, str(REPO / "scripts"))
        import benchmark
        benchmark.CACHE_DIR = cache
        if code in benchmark._WIKIPRON_FILES and (Path(cache) / benchmark._WIKIPRON_FILES[code]).exists():
            words = [w for w, _ in benchmark.load_wikipron(code, limit)]
            return "wikipron", list(dict.fromkeys(words))
    return "word_exceptions", sorted(registry.get(code).word_exceptions or {})[:limit]


# ─── pattern fuzz: the generator of tests/test_ir.py TestPatternFuzz ─────────

def _random_pattern(rng, depth=0):
    atoms = ["a", "b", ".", "[ab]", "[^a]", "\\n", "^", "$"]
    kind = rng.randrange(7 if depth < 3 else 1)
    if kind == 0:
        return rng.choice(atoms)
    if kind == 1:
        return _random_pattern(rng, depth + 1) + _random_pattern(rng, depth + 1)
    if kind == 2:
        return _random_pattern(rng, depth + 1) + "|" + rng.choice(["", _random_pattern(rng, depth + 1)])
    if kind == 3:
        return "(" + _random_pattern(rng, depth + 1) + ")"
    if kind == 4:
        return "(?:" + _random_pattern(rng, depth + 1) + ")" + rng.choice("*+?")
    if kind == 5:
        return "(" + _random_pattern(rng, depth + 1) + ")" + rng.choice("*+?")
    return rng.choice(["(?=", "(?!"]) + _random_pattern(rng, depth + 1) + ")" + rng.choice(["", "+", "*"])


_FUZZ_LUA = r"""
package.path = arg[1] .. "/?.lua;" .. package.path
local M = require("interpreter")
local f = io.open(arg[2], "rb"); local cases = M.json_decode(f:read("*a")); f:close()
local P = M.pattern
local out = {}
for _, c in ipairs(cases) do
  local ng = P.group_count(c.node)
  for _, s in ipairs(c.texts) do
    local st, e, g = P.search(c.node, s, 0, ng)
    local parts = {}
    if st == nil then parts[1] = "none" else
      parts[1] = st .. " " .. e
      for k = 2, c.ngroups + 1 do parts[#parts + 1] = g[k] and (g[k][1] .. " " .. g[k][2]) or "-" end
    end
    out[#out + 1] = table.concat(parts, ",") .. "|" .. table.concat(P.sub(c.node, c.parts, s, c.strings), " ")
  end
end
io.write(table.concat(out, "\n"), "\n")
"""


def fuzz(workdir: Path, rounds: int = 4000) -> dict:
    """Every accepted pattern: Lua search and sub against re and pattern.py."""
    from orthography2ipa.ir.compile_patterns import PatternOutsideSubset, compile_pattern, compile_template
    rng = random.Random(2482)
    texts = ["".join(rng.choice("ab\n") for _ in range(rng.randrange(7))) for _ in range(40)]
    cases, expect = [], []
    for _ in range(rounds):
        text = _random_pattern(rng)
        try:
            rx = re.compile(text)
        except re.error:
            continue
        try:
            node = compile_pattern(text)
        except PatternOutsideSubset:
            continue
        ngroups = rx.groups
        template = "<" + "".join(f"\\{g}" for g in range(1, ngroups + 1)) + ">"
        tpl = compile_template(template)
        strings = [[ord(c) for c in p[1]] for p in tpl if p[0] == "lit"]
        parts, n = [], 0
        for p in tpl:
            if p[0] == "lit":
                parts.append(["lit", n])
                n += 1
            else:
                parts.append(p)
        cps = [[ord(c) for c in s] for s in texts]
        cases.append({"node": node, "parts": parts, "strings": strings, "ngroups": ngroups, "texts": cps})
        for s, c in zip(texts, cps):
            m = rx.search(s)
            got = pattern.search(node, c, 0, pattern.group_count(node))
            want = "none" if m is None else ",".join(
                [f"{m.start()} {m.end()}"] + [f"{m.start(g)} {m.end(g)}" if m.group(g) is not None else "-"
                                              for g in range(1, ngroups + 1)])
            ref = "none" if got is None else ",".join(
                [f"{got[0]} {got[1]}"] + [f"{sp[0]} {sp[1]}" if sp is not None else "-"
                                          for sp in got[2][1:ngroups + 1]])
            subbed = rx.sub(template, s)
            assert ref == want and "".join(map(chr, pattern.sub(node, parts, c, strings))) == subbed, (text, s)
            expect.append((text, s, want + "|" + " ".join(str(ord(ch)) for ch in subbed)))
    case_path = workdir / "fuzz-cases.json"
    case_path.write_text(json.dumps(cases), encoding="utf-8")
    driver = workdir / "fuzz.lua"
    driver.write_text(_FUZZ_LUA, encoding="utf-8")
    proc = subprocess.run([LUAJIT, str(driver), str(LUA.parent), str(case_path)],
                          capture_output=True, text=True, check=True)
    got = proc.stdout.split("\n")[:-1]
    case_path.unlink()
    driver.unlink()
    same = sum(a[2] == b for a, b in zip(expect, got))
    print(f"pattern fuzz: {len(cases)} accepted patterns, N in {len(expect)}, N out {len(got)}, "
          f"N identical {same}, mismatches {len(expect) - same}", flush=True)
    for (text, s, want), have in list(zip(expect, got)):
        if want != have:
            print(f"  {text!r} on {s!r} | re {want} | lua {have}", flush=True)
    return {"label": "pattern fuzz", "n_in": len(expect), "n_out": len(got), "same": same}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", action="append", default=[])
    ap.add_argument("--corpus")
    ap.add_argument("--dialect-corpus")
    ap.add_argument("--dialect", action="append", default=[])
    ap.add_argument("--data-ref")
    ap.add_argument("--expected", help="JSON list of [text, ipa] rows; the texts are the input")
    ap.add_argument("--gold-langs", action="store_true")
    ap.add_argument("--gold-cache", help="the board's .benchmark_cache directory")
    ap.add_argument("--limit", type=int, default=2000)
    ap.add_argument("--width", type=int, default=1)
    ap.add_argument("--show", type=int, default=50)
    ap.add_argument("--fuzz", action="store_true")
    ap.add_argument("--loom-host", help="the o2i_loom host binary: run the Lua side inside loom")
    ap.add_argument("--report")
    args = ap.parse_args()
    results = []
    with tempfile.TemporaryDirectory(prefix="ir-lua-parity-") as tmp:
        workdir = Path(tmp)
        if args.fuzz:
            results.append(fuzz(workdir))
        if args.expected:
            rows = json.loads(Path(args.expected).read_text(encoding="utf-8"))
            rows = rows["rows"] if isinstance(rows, dict) else rows
            for code in args.lang:
                results.append(run(code, [r[0] for r in rows], workdir, data_ref=args.data_ref,
                                   width=args.width, show=args.show, loom_host=args.loom_host,
                                   expected=[r[1] for r in rows]))
        elif args.dialect_corpus:
            from orthography2ipa.transforms import DIALECT_PROFILES
            texts = dialect_texts(Path(args.dialect_corpus))
            for profile in args.dialect or sorted(DIALECT_PROFILES):
                results.append(run("pt-PT", texts, workdir, dialect=profile, width=args.width, show=args.show))
            n = sum(r.get("n_in", 0) for r in results)
            same = sum(r.get("same", 0) for r in results)
            print(f"dialect total: N in {n}, N identical {same}, mismatches {n - same}")
        elif args.corpus:
            lines = [line for line in Path(args.corpus).read_text(encoding="utf-8").split("\n") if line]
            for code in args.lang:
                results.append(run(code, lines, workdir, data_ref=args.data_ref, width=args.width,
                                   show=args.show, loom_host=args.loom_host))
        elif args.gold_langs:
            for code in args.lang or registry.available_codes():
                try:
                    source, words = gold_words(code, args.limit, args.gold_cache)
                except Exception as exc:  # a spec that does not load
                    print(f"{code}: does not load: {exc}", flush=True)
                    continue
                if words:
                    result = run(code, words, workdir, width=args.width, show=args.show, source=source,
                                 loom_host=args.loom_host)
                    result["source"] = source
                    results.append(result)
    if args.report:
        Path(args.report).write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
