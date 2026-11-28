"""Run the IR parity tools on a fixed sample of languages and fail on a defect.

The tool:

1. runs scripts/ir_parity.py --golden on tests/data/ir_golden_ci.json, the
   recorded rules-engine output of every 15th WikiPron code and pt-PT.
   Any mismatch or interpreter error fails the run.
2. when orthography2ipa/ir/interpreter.lua and scripts/ir_lua_parity.py
   exist, runs the Lua parity tool (Python IR against Lua IR) on the
   codes of the golden file and kab. It downloads the WikiPron files into
   the benchmark cache; kab reads the sentences of its shipped gold TSV.
   Any difference or error fails the run, because both sides read the
   same IR.

    python -I scripts/ir_parity_ci.py [--limit 300] [--out DIR]
"""
import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path
from typing import List

REPO = Path(__file__).resolve().parent.parent
GOLDEN = REPO / "tests" / "data" / "ir_golden_ci.json"


def inputs(codes: List[str], args) -> List[List[str]]:
    """The tool arguments for each group of codes. A code with a WikiPron
    gold set reads it from the cache; any other code reads the sentences of
    its shipped gold TSV (orthography2ipa/data/gold/*/CODE.tsv)."""
    sys.path.insert(0, str(REPO / "scripts"))
    import benchmark
    benchmark.CACHE_DIR = str(args.cache)
    wikipron = [code for code in codes if code in benchmark._WIKIPRON_FILES]
    for code in wikipron:
        benchmark.load_wikipron(code, 1)
    groups = [["--gold-langs", "--gold-cache", str(args.cache), "--limit", str(args.limit),
               *[arg for code in wikipron for arg in ("--lang", code)]]]
    for code in sorted(set(codes) - set(wikipron)):
        tsv = next((REPO / "orthography2ipa" / "data" / "gold").glob(f"*/{code}.tsv"), None)
        if tsv is None:
            raise SystemExit(f"{code}: no WikiPron gold and no shipped gold TSV")
        with tsv.open(encoding="utf-8") as f:
            texts = [row["sentence"] for row in csv.DictReader(f, delimiter="\t")][:args.limit]
        corpus = args.out / f"{code}.txt"
        corpus.write_text("\n".join(texts) + "\n", encoding="utf-8")
        groups.append(["--corpus", str(corpus), "--lang", code])
    return groups


def run_tool(script: str, groups: List[List[str]], out: Path) -> list:
    results = []
    for n, group in enumerate(groups):
        report = out / f"{Path(script).stem}-{n}.json"
        cmd = [sys.executable, "-I", str(REPO / "scripts" / script), *group, "--report", str(report)]
        print("+", " ".join(cmd), flush=True)
        subprocess.run(cmd, check=True, cwd=REPO)
        results += json.loads(report.read_text(encoding="utf-8"))
    return results


def python_failures(results: list) -> List[str]:
    return [f"{r['code']}: refused {r['refused']}" if "refused" in r else
            f"{r['label']}: N in {r['n']}, N identical {r['same']}, errors {sum(r['errors'].values())}"
            for r in results if "refused" in r or r["same"] != r["n"] or r["errors"]]


def lua_failures(results: list) -> List[str]:
    return [f"{r['label']}: N in {r['n_in']}, N out {r['n_out']}, N identical {r['same']}, "
            f"errors py {r['py_errors']} lua {r['lua_errors']}"
            for r in results if "refused" not in r
            and (r["same"] != r["n_in"] or r["n_out"] != r["n_in"] or r["py_errors"] or r["lua_errors"])]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--limit", type=int, default=300)
    ap.add_argument("--cache", type=Path, default=REPO / ".benchmark_cache")
    ap.add_argument("--out", type=Path, default=REPO / "ir-parity-reports")
    args = ap.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    golden = sorted(json.loads(GOLDEN.read_text(encoding="utf-8")))
    print(f"golden: {len(golden)} codes: {' '.join(golden)}", flush=True)

    failures: List[str] = []
    results = run_tool("ir_parity.py", [["--golden", str(GOLDEN)]], args.out)
    print(f"python parity: {len(golden)} codes in, {len(results)} results out")
    if len(results) != len(golden):
        failures.append(f"python parity: {len(golden)} codes in, {len(results)} results out")
    failures += python_failures(results)

    if (REPO / "orthography2ipa" / "ir" / "interpreter.lua").exists() \
            and (REPO / "scripts" / "ir_lua_parity.py").exists():
        codes = golden + ["kab"]
        results = run_tool("ir_lua_parity.py", inputs(codes, args), args.out)
        print(f"lua parity: {len(codes)} codes in, {len(results)} results out")
        if len(results) != len(codes):
            failures.append(f"lua parity: {len(codes)} codes in, {len(results)} results out")
        failures += lua_failures(results)
    else:
        print("lua parity: no interpreter.lua in this tree, step skipped")

    for failure in failures:
        print(f"FAIL {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
