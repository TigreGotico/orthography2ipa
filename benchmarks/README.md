# Benchmarks

This directory holds the committed board files. Scripts write every file
here, so never edit one by hand. The procedure is in
[docs/contributing/board.md](../docs/contributing/board.md).

| File | Holds | Written by |
|---|---|---|
| `results.json` | Every board row on the full gold set: PER, `n`, confidence interval, `provenance`, `gating` | `scripts/benchmark.py --scoreboard` |
| `results_ci_sample.json` | The same rows at a uniform sample of 1000 words, the baseline of the CI regression gate | `scripts/benchmark.py --ci-sample` |
| `comparison.json` | The same gold rows scored by espeak-ng, epitran, gruut and other systems | `scripts/compare_systems.py --scoreboard` |
| `lexicon_results.json` | Rules-only PER against PER with a lexicon | `scripts/benchmark.py --lexicon-report` |
| `espeak_agreement.json` | Symbol-level agreement with espeak-ng | `scripts/espeak_agreement.py` |
| `latency.py` | A script that times `G2P.transcribe` per utterance | Run it: `python benchmarks/latency.py` |

`docs/scoreboard.md`, `docs/comparison.md`, `docs/lexicon_scoreboard.md` and
`docs/espeak_agreement.md` are the rendered pages of these files. A
whole-board `--scoreboard` run also writes `results_environment.json`, the
versions of the plugin and scorer packages it used.

How a score is computed and how far it can be trusted is in
[docs/benchmark_methodology.md](../docs/benchmark_methodology.md) and
[docs/benchmarks.md](../docs/benchmarks.md).
