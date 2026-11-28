"""Compile the IR of the slow specs, for the wheel.

The release job runs this before it builds the wheel, so that a first
``G2P(code).transcribe`` of a slow spec reads a document instead of
compiling. The tool times the ``build_ir`` call of every spec that has a grapheme table, in a
warm process with an empty compile cache, and writes the document of each
one that took at least ``--min-seconds``. A
faster spec compiles on first use into the user cache. A stub spec has no
grapheme table and compiles in a fraction of a second, so it is not timed.

    python -I scripts/build_ir_cache.py [--out DIR] [--lang CODE ...] [--jobs N] [--min-seconds S]

The tool prints N in, N written, N fast, N stub, N refused and N failed, and
the size of the documents written.
"""
import argparse
import sys
import time
import warnings
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path


def _warm() -> None:
    """Load the package and run one compile, so a timed compile costs only
    its own spec."""
    warnings.simplefilter("ignore")
    from orthography2ipa.ir import compiler
    compiler.build_ir("es-ES")


def build(code: str, out: str, min_seconds: float):
    from orthography2ipa.ir import cache, compiler, layout
    from orthography2ipa.ir.compiler import IRUnsupportedFeature
    compiler._base_ir.cache_clear()
    t0 = time.perf_counter()
    try:
        ir = compiler.build_ir(code, **cache.DEFAULT_OPTIONS)
    except IRUnsupportedFeature as exc:
        return code, "refused", exc.feature
    except Exception as exc:  # reported, never fatal to the whole build
        return code, "failed", f"{type(exc).__name__}: {exc}"
    seconds = time.perf_counter() - t0
    if seconds < min_seconds:
        return code, "fast", f"{seconds:.2f} s"
    cache.write(Path(out), f"{code}-{cache.cache_key(code, cache.DEFAULT_OPTIONS)}.json.xz",
                layout.encode(ir))
    return code, "written", f"{seconds:.1f} s"


def main() -> None:
    from orthography2ipa import registry
    from orthography2ipa.ir.cache import PRECOMPILED
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(PRECOMPILED))
    ap.add_argument("--lang", action="append", default=[])
    ap.add_argument("--jobs", type=int, default=1)
    ap.add_argument("--min-seconds", type=float, default=1.0,
                    help="write the document of a spec that compiles at least this slowly; 0 writes all")
    args = ap.parse_args()
    codes = [registry.resolve(c) for c in args.lang] or registry.available_codes()
    counts = {"written": 0, "fast": 0, "stub": 0, "refused": 0, "failed": 0}
    timed = []
    for code in codes:
        spec = registry.get(code)
        if spec.graphemes or spec.positional_graphemes:
            timed.append(code)
        else:
            counts["stub"] += 1
    n = len(codes)
    # Each worker is warm, and each timed call starts with an empty compile
    # cache, so a time is the build_ir call of one spec alone.
    with ProcessPoolExecutor(args.jobs, initializer=_warm) as pool:
        for code, status, detail in pool.map(build, timed, [args.out] * len(timed),
                                             [args.min_seconds] * len(timed)):
            counts[status] += 1
            print(f"{code}: {status} ({detail})", flush=True)
    size = sum(p.stat().st_size for p in Path(args.out).glob("*.json.xz")) if Path(args.out).is_dir() else 0
    print(f"N in {n}, N written {counts['written']}, N fast {counts['fast']}, N stub {counts['stub']}, "
          f"N refused {counts['refused']}, N failed {counts['failed']}, {size / 1e6:.1f} MB in {args.out}")
    sys.exit(1 if counts["failed"] else 0)


if __name__ == "__main__":
    main()
