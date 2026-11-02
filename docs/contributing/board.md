# Board regeneration

The benchmark board is five files that must move together:

| File | Written by |
|---|---|
| `benchmarks/results.json` | `scripts/benchmark.py --scoreboard` |
| `docs/scoreboard.md` | `scripts/benchmark.py --scoreboard` |
| `benchmarks/results_ci_sample.json` | `scripts/benchmark.py --ci-sample` |
| `benchmarks/comparison.json` | `scripts/compare_systems.py --scoreboard` |
| `docs/comparison.md` | `scripts/compare_systems.py --scoreboard` |

Never edit these files by hand. A change that touches one board file
regenerates the others in the same run, or the consistency tests fail. This
page gives the procedure and every guard that checks the result. The
scoring method is in [benchmarks.md](../benchmarks.md).

## Before you regenerate

1. Set `ESPEAK_RULES_DATA_PATH` to a rules-only espeak-ng data directory.
   Without it, the comparison writer sets every `espeak_rules` cell it cannot
   reproduce to null. It also drops those rows from the fair-comparison table
   and shrinks the published tally. The directory must contain its
   `rules_only_manifest.tsv`, or the writer marks the cells n/a.
   `scripts/build_espeak_rules_only.sh` builds the directory from espeak-ng
   1.52.0 source.
2. Install the `compare` extra (`uv pip install --python .venv -e '.[compare]'`)
   before a comparison run. Without epitran and gruut, the writer reports
   their cells as n/a and drops their columns from the tables.
3. Write down the rows that your change defends. Every other row that moves
   is drift. Exclude it, or declare it in the pull request.
4. Freeze the word lists before a differential on `vox_communis`. Its loads
   change between sessions, so run both trees in one session against one
   cache. Report a spec change at constant `n`, and report an `n` change from
   a refetch on its own.

```bash
scripts/build_espeak_rules_only.sh en fr de nl ca sv eu
export ESPEAK_RULES_DATA_PATH=$PWD/.espeak_rules_only
```

The script clones espeak-ng into a scratch directory and writes only to
`.espeak_rules_only/`, which git ignores. No GPL data enters the tree.

## Regenerate

Use `--lang` or `--dataset` to rescore only the rows you own. A scoped run
merges its rows into the committed files and keeps every other row.

```bash
PYTHONPATH=$PWD python scripts/benchmark.py --scoreboard --lang fi
PYTHONPATH=$PWD python scripts/benchmark.py --ci-sample --lang fi
PYTHONPATH=$PWD python scripts/compare_systems.py --scoreboard --lang fi
```

`compare_systems.py --lang` accepts only the languages that
`compare_systems.py --list` prints. Without `--lang`, each command rescores
its whole board, which takes hours. A whole-board `--scoreboard` run also
writes `benchmarks/results_environment.json`, the version of every plugin
and scorer package it used. When a row moves with no spec change, read that
file first.

After the run, diff the CI sample against the merge base and count the rows
that changed. Only your rows may move. `check_benchmark_regression.py` fails
only when a row gets worse, so a sweep of unrelated improvements passes CI
without a word. Restrict the refresh to your rows, or disclose the sweep in
the pull request.

## Check the result

1. Diff `docs/comparison.md`. Both espeak-ng columns (stock and rules-only)
   must stay in every table that had them. The "N of M" tally changes only
   where your change defends it.
2. Run the board tests and your language's tests:

```bash
PYTHONPATH=$PWD python -m pytest tests/test_compare_systems.py \
    tests/test_check_benchmark_regression.py tests/test_thin_row_marker.py \
    $(PYTHONPATH=$PWD python scripts/which_tests.py --lang fi)
```

3. Run the four CI guards locally (see the table below).
4. Fetch `origin/dev` and rebase before you push. Other pull requests merge
   board rows while you work. Check that their rows survive your files byte
   for byte, then run the tests again on the rebased tree.

On a long run, `origin/dev` moves under you. Compute your rows first. Then
fetch, rebase, and merge your rows into the board files of the final base as
the last step before the commit. A board copied from `origin/dev` at the
start of a long run is stale at the end, and it reverts the rows that merged
in between.

## The guards

| Guard | What it fails on | Local command |
|---|---|---|
| Benchmark regression | A CI-sample row whose PER or stress accuracy gets worse by more than 0.005 | `PYTHONPATH=$PWD python scripts/check_benchmark_regression.py --epsilon 0.005` |
| Row counts | A row whose `n` is larger than the pairs its gold loader yields, or a row for a language the dataset does not register | `PYTHONPATH=$PWD python scripts/check_board_row_counts.py` |
| Board freshness | A row that a touched spec owns, whose fresh score differs from the committed value in either board file | `PYTHONPATH=$PWD python scripts/check_board_freshness.py --base origin/dev` |
| Board not reverting | A merge result that puts back a row value `dev` already moved past, or that grows a burn-down list | `PYTHONPATH=$PWD python scripts/check_board_not_reverting.py --base origin/dev --body-file pr-body.md` |
| Scoreboard in sync | A `docs/scoreboard.md` that differs from what `results.json` renders | `PYTHONPATH=$PWD python -m pytest tests/test_thin_row_marker.py` |
| Docs prose | A generated page that fails the prose lint (fix the generator, then regenerate) | `PYTHONPATH=$PWD python -m pytest tests/test_docs_prose.py` |

The CI workflow `.github/workflows/benchmark-regression.yml` runs the first
four guards. `board-not-reverting` runs the copy of the script on the base
branch, so a branch cannot weaken the guard that judges it.

## Never carry the board backwards

A branch rescores only its own rows. Every other row is a copy of `dev` from
when the branch was cut. A three-way merge keeps `dev`'s newer values for rows
the branch did not edit, so that copy alone is harmless. The harm comes when
you merge `dev` into the branch and resolve a conflicted board file by keeping
your side. Then `dev`'s newer numbers are lost, and both sides stay green.

Resolve each board file row by row. Keep `dev`'s value for every row you did
not rescore, then regenerate `docs/scoreboard.md`.
`check_board_not_reverting.py` merges the two sides with `git merge-tree` and
fails on an old value, unless the branch edits that language's spec. An edit
to a parent or clade spec owns the rows of every language that inherits from
it, through `parent` or a `*_base` table.

A harness or engine change can move rows it does not own. The guard reads
those rows off the merge result. A `Board-Rows:` line in the pull request
body or a commit message is optional, and the guard checks it against the
rows the merge actually moves:

```text
Board-Rows: mr/wikipron, xh/kaikki
Board-Rows: all - stress placement reworked, every row rescored
```

The same guard reads two burn-down lists off the merge result. Each list may
only shrink:

- `_WIKIPEDIA_ONLY_SOURCES_BURNDOWN` in `tests/test_sources.py` holds specs
  whose only sources are bare Wikipedia links.
- `_DOCS_PROSE_RATCHET` in `tests/test_docs_prose.py` holds pages that
  predate the prose lint.

Both lists are allowlists, so a longer list makes the suite greener. When you
resolve a conflict in one of these files, keep `dev`'s shorter set.

## Fairness rules for the comparison board

- Every language carries both espeak-ng columns, stock and rules-only.
- Every engine that carries a lexicon gets a rules-only column.
- The winner and the ranking use only lexicon-free values.
- The lexicon-backed tier is a separate table with its own label.

---
[← Citation honesty](citations.md) · [Home](../index.md) · [Engine changes →](engine.md)
