# Scripts

Every script runs from the repository root with `PYTHONPATH=$PWD`, so that
it measures the checkout and not an installed package. Each script has a
module docstring with its usage, and most take `--help`.

## Benchmark and board

| Script | Does |
|---|---|
| `benchmark.py` | Scores the engine against the gold sets. `--scoreboard` writes the board, `--ci-sample` the CI baseline, `--list` names the datasets |
| `compare_systems.py` | Scores espeak-ng, epitran, gruut and other systems on the same rows. `--scoreboard` writes the comparison board |
| `build_espeak_rules_only.sh` | Builds the rules-only espeak-ng data that `compare_systems.py` reads through `ESPEAK_RULES_DATA_PATH` |
| `check_benchmark_regression.py` | Fails when a row of the CI sample gets worse by more than the epsilon (0.005) |
| `check_board_freshness.py` | Fails when a touched spec no longer produces its committed rows |
| `check_board_not_reverting.py` | Fails when a merge would put back an old board value or grow a burn-down list |
| `check_board_row_counts.py` | Fails when a row scored more words than its gold now holds |
| `espeak_agreement.py` | Measures symbol-level agreement with espeak-ng |
| `error_analysis.py`, `rank_diag.py`, `rank_eval.py`, `rank_sweep.py` | Diagnose why a language misses its gold |
| `folded_per.py`, `omission_score.py`, `fold_*_notation.py` | Measure how much of a row's PER comes from notation the spelling does not write |
| `gold_composition.py`, `spec_diagnostics.py`, `check_unmapped_graphemes.py` | Diagnostics over the gold sets and the specs |
| `wikipron_mirror.py`, `restore_wikipron_orthography.py` | Build the pinned WikiPron mirror |
| `build_gold_corrections.py` | Regenerates the gold correction overlays |
| `*_tts_gold.py`, `_gold_build.py` | Author and validate the hand-built sentence gold sets |
| `build_en_lexicon.py` | Builds an English lexicon from CMUdict for a caller to register |

The procedure and the guards are in
[docs/contributing/board.md](../docs/contributing/board.md).

## Spec data

| Script | Does |
|---|---|
| `gen_stubs.py`, `gen_africa_orthographies.py`, `gen_phoible.py` | Fill stub specs from ISO 639-3, africa-g2p and PHOIBLE |
| `gen_family.py`, `gen_locations.py`, `dialect_places.py` | Fill classification and location fields from Glottolog and Wikidata |
| `gen_burmese.py`, `gen_khmer.py`, `gen_tibetan.py`, `gen_vietnamese.py`, `gen_arabic_orthography_keys.py` | Regenerate the systematic tables of one spec |
| `check_doi_titles.py`, `check_glottolog_codes.py` | Check that cited DOIs and Glottolog codes resolve to the right work and language |
| `which_tests.py` | Names the test files that assert on a spec |

## Documentation

| Script | Does |
|---|---|
| `docs_nav.py` | Checks (`--check`) or rewrites (`--write`) the navigation footers from the order in `docs/index.md` |
| `gen_reference_docs.py` | Writes `docs/reference/api.md`, `docs/reference/cli.md` and `llms.txt` from the code (`--write`, `--check`) |
| `gen_explorer.py` | Writes the self-contained language explorer page |
| `ste_lint.py` | The prose linter that `tests/test_docs_prose.py` runs |

## Other

| Script | Does |
|---|---|
| `smoke_downstream.py` | Imports a downstream G2P package and transcribes one word with it |
| `recompute_th_tone_accuracy.py` | Recomputes the tone-accuracy note in `th.json` |
