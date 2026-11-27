"""Run the conformance vectors and the bundled gold sentences through a loom host.

    python scripts/loom_parity.py HOST LOOM_COMMIT [--out benchmarks/loom_parity.json]

HOST is a build of scripts/loom_host. The result counts the texts where the loom
output equals the Python output byte for byte.
"""
import argparse
import collections
import glob
import json
import subprocess
import tempfile
from pathlib import Path

import orthography2ipa as o2i
from orthography2ipa import export_to_loom as loom


def run_host(host: str, lang: str, texts: list, tmp: str, ir: dict = None) -> subprocess.CompletedProcess:
    """Export *lang* and run *texts* through *host*. *ir* replaces the compiled IR."""
    gguf = Path(tempfile.mkdtemp(dir=tmp)) / f"{lang}.gguf"
    compile_irs = loom.compile_irs
    if ir is not None:
        loom.compile_irs = lambda langs, rev=None, fragments=(): {lang: ir}
    try:
        loom.export_to_loom([lang], gguf)
    finally:
        loom.compile_irs = compile_irs
    return subprocess.run([host, str(gguf), "0"], input="\n".join(texts) + "\n",
                          capture_output=True, text=True)


def outputs(proc: subprocess.CompletedProcess, n: int) -> list:
    if proc.returncode != 0:
        raise RuntimeError(f"host exited {proc.returncode}: {proc.stderr[-300:]}")
    return proc.stdout.split("\n")[:n]


def vectors(host: str, tmp: str) -> dict:
    """Run each vector file on its own IR. An error case passes when the host
    stops with the expected message."""
    paths = sorted(glob.glob("tests/conformance/ir-v1/*.jsonl"))
    cases = same = errors = errors_same = 0
    error_files = set()
    for path in paths:
        records = [json.loads(line) for line in open(path, encoding="utf-8")]
        head, rows = records[0], records[1:]
        runs = [r for r in rows if "expect" in r]
        if runs:
            texts = ["".join(map(chr, r["input"])) for r in runs]
            got = outputs(run_host(host, head["lang"], texts, tmp, head["ir"]), len(texts))
            cases += len(runs)
            same += sum(g == "".join(map(chr, r["expect"])) for g, r in zip(got, runs))
        for row in (r for r in rows if "expect_error" in r):
            proc = run_host(host, head["lang"], ["".join(map(chr, row["input"]))], tmp, head["ir"])
            errors += 1
            error_files.add(path)
            errors_same += proc.returncode != 0 and row["expect_error"] in proc.stderr
    return {"files": len(paths), "cases": cases, "identical": same,
            "error_files": len(error_files), "error_cases": errors, "error_cases_refused": errors_same}


def gold(host: str, tmp: str) -> dict:
    by_lect = collections.defaultdict(set)
    for path in glob.glob("orthography2ipa/data/gold/*.jsonl"):
        for line in open(path, encoding="utf-8"):
            row = json.loads(line)
            text = row["sentence"].replace("\n", " ").strip()
            if text:
                by_lect[row["lect"]].add(text)
    texts_n = same = 0
    for lect, texts in sorted(by_lect.items()):
        texts = sorted(texts)
        got = outputs(run_host(host, lect, texts, tmp), len(texts))
        texts_n += len(texts)
        same += sum(g == o2i.transcribe(t, lect) for g, t in zip(got, texts))
    return {"lects": len(by_lect), "sentences": texts_n, "identical": same}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("host")
    ap.add_argument("loom_commit")
    ap.add_argument("--out", default="benchmarks/loom_parity.json")
    args = ap.parse_args()
    with tempfile.TemporaryDirectory() as tmp:
        result = {"orthography2ipa": o2i.__version__, "loom_commit": args.loom_commit,
                  "vectors": vectors(args.host, tmp), "gold": gold(args.host, tmp)}
    Path(args.out).write_text(json.dumps(result, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
