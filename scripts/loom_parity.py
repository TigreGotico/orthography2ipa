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
from orthography2ipa.export_to_loom import export_to_loom


def run_host(host: str, lang: str, texts: list, tmp: str) -> list:
    gguf = Path(tempfile.mkdtemp(dir=tmp)) / f"{lang}.gguf"
    export_to_loom([lang], gguf)
    out = subprocess.run([host, str(gguf), "0"], input="\n".join(texts) + "\n",
                         capture_output=True, text=True, check=True).stdout
    return out.split("\n")[:len(texts)]


def vectors(host: str, tmp: str) -> dict:
    cases = same = 0
    for path in sorted(glob.glob("tests/conformance/ir-v1/*.jsonl")):
        records = [json.loads(line) for line in open(path, encoding="utf-8")]
        rows = [r for r in records[1:] if "expect" in r]
        texts = ["".join(map(chr, r["input"])) for r in rows]
        got = run_host(host, records[0]["lang"], texts, tmp)
        cases += len(rows)
        same += sum(g == "".join(map(chr, r["expect"])) for g, r in zip(got, rows))
    return {"files": len(glob.glob("tests/conformance/ir-v1/*.jsonl")), "cases": cases, "identical": same}


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
        got = run_host(host, lect, texts, tmp)
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
