# Board regeneration

The benchmark board is five files that must move together:

| File | Written by |
|---|---|
| `benchmarks/results.json` | `scripts/benchmark.py --scoreboard` |
| `docs/evaluation/generated/scoreboard.md` | `scripts/benchmark.py --scoreboard` |
| `benchmarks/results_ci_sample.json` | `scripts/benchmark.py --ci-sample` |
| `benchmarks/comparison.json` | `scripts/compare_systems.py --scoreboard` |
| `docs/evaluation/generated/comparison.md` | `scripts/compare_systems.py --scoreboard` |

Never edit these files by hand. A change that touches one board file
regenerates the others in the same run, or the consistency tests fail. This
page gives the procedure and every guard that checks the result. The
scoring method is in [benchmarks.md](../evaluation/benchmarks.md).

## Before you regenerate

1. Set `ESPEAK_RULES_DATA_PATH` to a rules-only espeak-ng data directory.
   Without it, the comparison writer sets every `espeak_rules` cell it cannot
   reproduce to null. It also drops those rows from the fair-comparison table
   and shrinks the published tally. The directory must contain its
   `rules_only_manifest.tsv`, or the writer marks the cells n/a.
   `scripts/build_espeak_rules_only.sh` builds the directory from the
   [espeak-ng 1.52.0](https://github.com/espeak-ng/espeak-ng/releases/tag/1.52.0)
   source. The `ESPEAK_RULES_TAG` variable selects another tag.
2. Install the `compare` extra (`uv pip install --python .venv -e '.[compare]'`)
   before a comparison run. The extra installs
   [epitran](https://github.com/dmort27/epitran),
   [gruut](https://github.com/rhasspy/gruut),
   [pycotovia](https://github.com/TigreGotico/pycotovia) and
   [ahotts-g2p](https://github.com/TigreGotico/ahotts-g2p). Without a system,
   the writer reports its cells as n/a and drops its column from the tables.
   [africa-g2p](https://github.com/AfriSpeech/africa-g2p) and
   [ghana-g2p](https://github.com/GhanaNLP/ghana-g2p) are not in the extra.
   Install them into the venv by name when you rescore an African row.
3. Write down the rows that your change defends. Every other row that moves
   is drift. Exclude it, or declare it in the pull request.
4. Run both trees of any differential in one session against one cache. A
   committed board row can predate a refresh of the gold cache and move on an
   unmodified tree, and a differential across sessions reads that drift as a
   result. Freeze the word lists before a differential on `vox_communis`,
   whose loads change between sessions. Report a spec change at constant `n`,
   and report an `n` change from a refetch on its own.

```bash
scripts/build_espeak_rules_only.sh en fr de nl ca sv eu
export ESPEAK_RULES_DATA_PATH=$PWD/.espeak_rules_only
```

The script clones espeak-ng into a scratch directory and writes only to
`.espeak_rules_only/`, which git ignores. No GPL data enters the tree.

## Regenerate

Use `--lang` or `--dataset` to rescore only the rows you own. A scoped run
scores each row exactly as the full run does. It merges its rows into the
committed files and keeps every other row, so a fix to one language carries
no unrelated drift and downloads no other dataset. Refresh
`results_ci_sample.json` each time you regenerate the scoreboard.

```bash
PYTHONPATH=$PWD python scripts/benchmark.py --scoreboard --lang fi
PYTHONPATH=$PWD python scripts/benchmark.py --ci-sample --lang fi
PYTHONPATH=$PWD python scripts/compare_systems.py --scoreboard --lang fi
```

`compare_systems.py --lang` accepts only the languages that
`compare_systems.py --list` prints. Without `--lang`, each command rescores
its whole board, which takes hours. A whole-board `--scoreboard` run also
writes the [board environment](../evaluation/benchmarks.md#board-environment)
file, which you read first when a row moves with no spec change.

The [language atlas](../languages/index.md) prints the board scores of each
spec in the "Datasets" block of its page, so a board change makes those pages
stale. After the board files, rewrite the atlas, then the navigation footers
and `llms.txt` and `llms-full.txt`, which read the atlas:

```bash
PYTHONPATH=$PWD python scripts/gen_language_atlas.py --write
python scripts/docs_nav.py --write
PYTHONPATH=$PWD python scripts/gen_reference_docs.py --write
```

After the run, diff the CI sample against the merge base and count the rows
that changed. Only your rows may move. The
[regression gate](../evaluation/benchmarks.md#stale-board-rows) is one-sided,
so a sweep of unrelated improvements passes CI without a word. Restrict the refresh to your rows, or disclose the sweep in
the pull request.

## Check the result

1. Diff `docs/evaluation/generated/comparison.md`. Both espeak-ng columns (stock and rules-only)
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
| Benchmark regression | A CI-sample row that gets worse ([the CI regression sample](../evaluation/benchmarks.md#the-ci-regression-sample)) | `PYTHONPATH=$PWD python scripts/check_benchmark_regression.py --epsilon 0.005` |
| Row counts | A stale row ([stale board rows](../evaluation/benchmarks.md#stale-board-rows)). Run it after every regeneration. | `PYTHONPATH=$PWD python scripts/check_board_row_counts.py` |
| Board freshness | A row that a touched spec owns, whose fresh score differs from the committed value in either board file | `PYTHONPATH=$PWD python scripts/check_board_freshness.py --base origin/dev` |
| Board not reverting | A merge result that puts back a row value `dev` already moved past, or that grows a burn-down list | `PYTHONPATH=$PWD python scripts/check_board_not_reverting.py --base origin/dev --body-file pr-body.md` |
| Scoreboard in sync | A `docs/evaluation/generated/scoreboard.md` that differs from what `results.json` renders | `PYTHONPATH=$PWD python -m pytest tests/test_thin_row_marker.py` |
| Docs prose | A generated page that fails the prose lint (fix the generator, then regenerate) | `PYTHONPATH=$PWD python -m pytest tests/test_docs_prose.py` |
| Language atlas | An atlas block or index that differs from what the specs and `results.json` render | `PYTHONPATH=$PWD python scripts/gen_language_atlas.py --check` |

The CI workflow `.github/workflows/benchmark-regression.yml` runs the first
four guards. `board-not-reverting` runs the copy of the script on the base
branch, so a branch cannot weaken the guard that judges it.

CI splits the board-freshness guard into shards. A plan job lists the rows
that the touched specs own, parallel jobs measure one shard each, and the
`board-freshness` job fails on a stale row or on a planned row that no shard
measured. The local command above measures every owned row in one process.

## Never carry the board backwards

A branch rescores only its own rows. Every other row is a copy of `dev` from
when the branch was cut. A three-way merge keeps `dev`'s newer values for rows
the branch did not edit, so that copy alone is harmless. The harm comes when
you merge `dev` into the branch and resolve a conflicted board file by keeping
your side. Then `dev`'s newer numbers are lost, and both sides stay green.

Resolve each board file row by row. Keep `dev`'s value for every row you did
not rescore, then regenerate `docs/evaluation/generated/scoreboard.md`.
`check_board_not_reverting.py` merges the two sides with
[`git merge-tree`](https://git-scm.com/docs/git-merge-tree) and
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

The same guard reads two burn-down lists off the merge result, and each list
may only shrink. `_WIKIPEDIA_ONLY_SOURCES_BURNDOWN` in `tests/test_sources.py`
holds the specs whose only sources are bare Wikipedia links.
`_DOCS_PROSE_RATCHET` in `tests/test_docs_prose.py` holds the pages that
predate the prose lint. Both lists are allowlists, so a longer list makes the
suite greener. When you
resolve a conflict in one of these files, keep `dev`'s shorter set.

## Fairness rules for the comparison board

The comparison board ranks rules against rules. o2i ships no lexicon, so a
system wins a row only on its lexicon-free value. Every language carries
both espeak-ng columns, the stock one and the rules-only one, and every
other engine that carries a lexicon also gets a rules-only column. The
lexicon-backed values stay on the board for information, in a separate table
with its own label, and they never count toward the winner or the ranking.

---
[← Citation honesty](citations.md) · [Home](../index.md) · [Engine changes →](engine.md)
