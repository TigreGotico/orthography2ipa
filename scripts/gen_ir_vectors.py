"""Write the IR conformance vectors of section 8.4 into tests/conformance/ir-v1/.

For each spec of SPECS, the tool compiles the IR with
``orthography2ipa.ir.compiler``, runs a fixed sample of the spec's gold data
through the Python reference interpreter, and writes ``<lang>.jsonl``: one
``ir`` line, then one ``case`` line per input. The sample is the first
SAMPLE sorted distinct words of ``tests/data/ir_golden_ci.json``, or the
first SAMPLE sentences of the shipped gold TSV for a code with no golden
rows. Every file also holds an empty input. pt-PT also holds ⟨os jogos⟩.
``pt-PT-syllable.jsonl`` holds the pt-PT IR with the fragment
``tests/data/ir_fragment_syllable.json``, and for each word of its list one
``case`` line and one ``syllables`` line, the written syllables of S5.
``unknown-version.jsonl`` holds the smallest IR of the set with one
primitive version raised, and one case that expects the version error.

    python -I scripts/gen_ir_vectors.py          # write the files
    python -I scripts/gen_ir_vectors.py --check  # regenerate in memory and compare
"""
import argparse
import csv
import json
import sys
import warnings
from pathlib import Path
from typing import Dict, List

warnings.simplefilter("ignore")

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from orthography2ipa.ir import layout  # noqa: E402
from orthography2ipa.ir.compiler import build_ir  # noqa: E402
from orthography2ipa.ir.interpreter import Interpreter, IRVersionError  # noqa: E402

OUT = REPO / "tests" / "conformance" / "ir-v1"
GOLDEN = REPO / "tests" / "data" / "ir_golden_ci.json"
#: The codes of ir_golden_ci.json and kab: the set that scripts/ir_parity_ci.py checks.
SPECS = tuple(sorted([*json.loads(GOLDEN.read_text(encoding="utf-8")), "kab"]))
SAMPLE = 200
EXTRA = {"pt-PT": ["os jogos"]}
VERSION_ERROR = "unsupported primitive version"
#: Vector files of an IR with a fragment: name -> (code, fragment, words).
FRAGMENT_VECTORS = {
    "pt-PT-syllable": ("pt-PT", REPO / "tests" / "data" / "ir_fragment_syllable.json", (
        "carro", "nascer", "exceto", "desça", "bairro", "rainha", "juiz", "ainda", "ao", "aos", "aorta",
        "arruinar", "adleriano", "sublinhar", "sublocar", "sublime", "distribuidor", "construir",
        "cuidado", "ingenuidade", "contiguidade", "kubitschek", "gourmet", "facebookiano", "bureau",
        "boxeur", "marathon", "alzheimer", "pacto", "atleta", "abstrair")),
}


def _line(obj: dict) -> str:
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "\n"


def sample(code: str, golden: Dict[str, list]) -> List[str]:
    if code in golden:
        return sorted({w for w, _ in golden[code]})[:SAMPLE]
    tsv = next((REPO / "orthography2ipa" / "data" / "gold").glob(f"*/{code}.tsv"))
    with tsv.open(encoding="utf-8") as f:
        return sorted({row["sentence"] for row in csv.DictReader(f, delimiter="\t")})[:SAMPLE]


def encoded(ir: dict) -> dict:
    """The canonical IR without ``source``, which holds the package version."""
    doc = layout.encode(ir)
    del doc["source"]
    return doc


def vector_file(code: str, texts: List[str], fragments: List[dict] = (), words: List[str] = ()) -> str:
    ir = build_ir(code, None, fragments=fragments)
    doc = encoded(ir)
    it = Interpreter(doc)
    lines = [_line({"kind": "ir", "lang": code, "revision": layout.spec_revision(ir), "ir": doc})]
    for text in texts:
        cps = [ord(c) for c in text]
        lines.append(_line({"kind": "case", "input": cps,
                            "expect": [ord(c) for c in it.transcribe(text, width=1)]}))
    for word in words:
        lines.append(_line({"kind": "syllables", "input": [ord(c) for c in word],
                            "expect": [[ord(c) for c in s] for s in it.syllables(word)]}))
    return "".join(lines)


def version_file(code: str) -> str:
    ir = build_ir(code, None)
    doc = encoded(ir)
    name = sorted(doc["primitives"])[0]
    doc["primitives"][name] += 1
    try:
        Interpreter(doc)
    except IRVersionError as exc:
        assert str(exc).startswith(VERSION_ERROR), exc
    else:
        raise AssertionError("the interpreter accepted a raised primitive version")
    return (_line({"kind": "ir", "lang": code, "revision": layout.spec_revision(ir), "ir": doc})
            + _line({"kind": "case", "input": [], "expect_error": VERSION_ERROR}))


def generate(codes) -> Dict[str, str]:
    golden = json.loads(GOLDEN.read_text(encoding="utf-8"))
    files = {}
    for code in codes:
        texts = sample(code, golden) + EXTRA.get(code, []) + [""]
        files[f"{code}.jsonl"] = vector_file(code, texts)
        print(f"{code}: N in {len(texts)}, N out {files[f'{code}.jsonl'].count(chr(10)) - 1}", flush=True)
    if codes == SPECS:
        files["unknown-version.jsonl"] = version_file("cop")
        for name, (code, path, words) in FRAGMENT_VECTORS.items():
            fragment = json.loads(path.read_text(encoding="utf-8"))
            files[f"{name}.jsonl"] = vector_file(code, list(words), [fragment], list(words))
            print(f"{name}: N in {len(words)}, N out {files[f'{name}.jsonl'].count(chr(10)) - 1}", flush=True)
    return files


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="compare with the files on disk, write nothing")
    ap.add_argument("--lang", action="append", choices=SPECS, help="write only the file of this spec")
    args = ap.parse_args()
    files = generate(tuple(args.lang) if args.lang else SPECS)
    n_cases = sum(text.count("\n") - 1 for text in files.values())
    size = sum(len(text.encode()) for text in files.values())
    print(f"specs {len(SPECS)}, files {len(files)}, cases {n_cases}, bytes {size}")
    if args.check:
        stale = sorted(name for name, text in files.items()
                       if not (OUT / name).exists() or (OUT / name).read_text(encoding="utf-8") != text)
        extra = [] if args.lang else sorted(p.name for p in OUT.glob("*.jsonl") if p.name not in files)
        for name in stale + extra:
            print(f"STALE {name}")
        return 1 if stale or extra else 0
    OUT.mkdir(parents=True, exist_ok=True)
    for name, text in files.items():
        (OUT / name).write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
