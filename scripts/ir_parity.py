"""Compare compile + interpret with recorded outputs.

A golden file maps a language code to ``[text, ipa]`` rows. ``--write-golden``
records ``G2P(code).transcribe`` of the gold words of every language: the
WikiPron words named by ``scripts/benchmark._WIKIPRON_FILES``, else the
spellings of the spec's ``word_exceptions``, at most ``--limit`` each.
``--golden`` runs each row through ``Interpreter(build_ir(code))`` and prints
N in, N out, N identical and every mismatch. ``--expected`` does the same for
one row list, for the languages named by ``--lang``.

A mismatch is classified: a ruled semantic change of section 9 of
docs/ir/o2i-ir-v1.md, or a defect. It is a ruled change when the
interpreter, with that one change switched back, gives the recorded output.

    python -I scripts/ir_parity.py --write-golden OUT.json --gold-cache DIR
    python -I scripts/ir_parity.py --golden OUT.json --report REPORT.json
    python -I scripts/ir_parity.py --lang kab --data-ref 7.30.0 --expected FILE.json
"""
import argparse
import json
import sys
import time
import warnings
from collections import Counter
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple

warnings.simplefilter("ignore")

from orthography2ipa import G2P, registry  # noqa: E402
from orthography2ipa.ir.compiler import IRUnsupportedFeature, build_ir  # noqa: E402
from orthography2ipa.ir.interpreter import Interpreter  # noqa: E402
from orthography2ipa.stress import _ipa_judge  # noqa: E402
from orthography2ipa.lexicon import _process_lexicon  # noqa: E402

REPO = Path(__file__).resolve().parent.parent


def _legacy_onsets(it: Interpreter, code: str) -> None:
    """Counterfactual for 9.1: the runtime judge instead of the table."""
    st = registry.get(code).stress
    judge = _ipa_judge(st.max_onset if st.max_onset_declared else None, st.onset_clusters)
    it._licit_onset = judge.licit


def _legacy_unknown(it: Interpreter, code: str) -> None:
    """Counterfactual for 9.2: unknown chars stay in the written word."""
    it._known_only = lambda word: word
    it._syll_cache.clear()


COUNTERFACTUALS: Dict[str, Callable[[Interpreter, str], None]] = {
    "9.1 onsets from a compiled table": _legacy_onsets,
    "9.2 unknown characters are boundaries": _legacy_unknown,
}


def classify(code: str, ir: dict, line: str, expected: str, lexicon) -> str:
    for name, switch in COUNTERFACTUALS.items():
        it = Interpreter(ir)
        try:
            switch(it, code)
        except Exception:  # a switch that does not apply to this spec
            continue
        if it.transcribe(line, lexicon=lexicon) == expected:
            return name
    return "defect"


def run(code: str, lines: List[str], expected: List[str], *, data_ref: Optional[str] = None,
        lexicon=None, show: int = 10 ** 9, out=sys.stdout) -> dict:
    t0 = time.perf_counter()
    try:
        ir = build_ir(code, data_ref)
    except IRUnsupportedFeature as exc:
        print(f"{code}: refused: {exc.feature}", file=out)
        return {"code": code, "refused": exc.feature}
    compile_s = time.perf_counter() - t0
    it = Interpreter(ir)
    t1 = time.perf_counter()
    got = []
    errors = Counter()
    for line in lines:
        try:
            got.append(it.transcribe(line, lexicon=lexicon))
        except NotImplementedError as exc:
            got.append(f"<error: {exc}>")
            errors[str(exc)] += 1
    run_s = time.perf_counter() - t1
    kinds = Counter()
    mismatches = []
    for line, a, b in zip(lines, expected, got):
        if a != b:
            kind = classify(code, ir, line, a, lexicon) if not b.startswith("<error") else "defect"
            kinds[kind] += 1
            mismatches.append((kind, line, a, b))
    label = code + (f" data_ref={data_ref}" if data_ref else "")
    same = sum(a == b for a, b in zip(expected, got))
    print(f"{label}: N in {len(lines)}, N out {len(got)}, N identical {same}, "
          f"mismatches {len(lines) - same} {dict(kinds)} (compile {compile_s:.1f} s, interpret {run_s:.1f} s)",
          file=out)
    for kind, line, a, b in mismatches[:show]:
        print(f"  [{kind}] {line!r} | expected {a!r} | ir {b!r}", file=out)
    for err, n in errors.items():
        print(f"  error x{n}: {err}", file=out)
    return {"code": code, "n": len(lines), "same": same, "kinds": dict(kinds),
            "errors": dict(errors), "label": label}


def gold_words(code: str, limit: int, cache: Optional[str]) -> Tuple[str, List[str]]:
    """The words of the language's WikiPron gold set (read from the board's
    cache), else the spellings of its word_exceptions."""
    if cache:
        sys.path.insert(0, str(REPO / "scripts"))
        import benchmark
        benchmark.CACHE_DIR = cache
        if code in benchmark._WIKIPRON_FILES and (Path(cache) / benchmark._WIKIPRON_FILES[code]).exists():
            words = [w for w, _ in benchmark.load_wikipron(code, limit)]
            return "wikipron", list(dict.fromkeys(words))
    return "word_exceptions", sorted(registry.get(code).word_exceptions or {})[:limit]


def write_golden(path: str, limit: int, cache: Optional[str]) -> None:
    golden = {}
    for code in registry.available_codes():
        try:
            _, words = gold_words(code, limit, cache)
        except Exception as exc:  # a spec that does not load
            print(f"{code}: does not load: {exc}")
            continue
        if words:
            g = G2P(code)
            golden[code] = [[w, g.transcribe(w)] for w in words]
    n = sum(len(rows) for rows in golden.values())
    print(f"languages {len(golden)}, N rows {n}")
    Path(path).write_text(json.dumps(golden, ensure_ascii=False), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", action="append", default=[])
    ap.add_argument("--data-ref")
    ap.add_argument("--expected", help="JSON list of [text, ipa] rows")
    ap.add_argument("--golden", help="JSON map of code to [text, ipa] rows")
    ap.add_argument("--write-golden")
    ap.add_argument("--limit", type=int, default=2000)
    ap.add_argument("--show", type=int, default=10 ** 9)
    ap.add_argument("--report")
    ap.add_argument("--gold-cache", help="the board's .benchmark_cache directory")
    args = ap.parse_args()
    if args.write_golden:
        write_golden(args.write_golden, args.limit, args.gold_cache)
        return
    results = []
    if args.expected:
        rows = json.loads(Path(args.expected).read_text(encoding="utf-8"))
        rows = rows["rows"] if isinstance(rows, dict) else rows
        for code in args.lang:
            results.append(run(code, [r[0] for r in rows], [r[1] for r in rows],
                               data_ref=args.data_ref, show=args.show))
    elif args.golden:
        golden = json.loads(Path(args.golden).read_text(encoding="utf-8"))
        for code in args.lang or sorted(golden):
            rows = golden[code]
            results.append(run(code, [r[0] for r in rows], [r[1] for r in rows],
                               lexicon=_process_lexicon(code) or None, show=args.show))
            sys.stdout.flush()
        total = sum(r.get("n", 0) for r in results)
        same = sum(r.get("same", 0) for r in results)
        print(f"languages {len(results)}, N in {total}, N identical {same}")
    if args.report:
        Path(args.report).write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
