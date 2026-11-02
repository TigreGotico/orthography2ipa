# The pinned WikiPron mirror

[TigreGotico/wikipron-restored-orthography](https://huggingface.co/datasets/TigreGotico/wikipron-restored-orthography) is a snapshot of every pronunciation scrape in [CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron) at one commit. A second orthography column holds the headword that English Wiktionary displays. The `wikipron_restored` benchmark row reads it (see [benchmark_datasets.md](benchmark_datasets.md#wikipron-with-the-display-headword-restored-wikipron_restored)). This page is the maintainer procedure that refreshes it.

The mirror exists for two reasons.

The first is reproducibility. WikiPron publishes its scrapes on a branch that it keeps editing. A benchmark that reads that branch scores against other data from one week to the next, with no code change. An upstream edit then looks the same as an engine regression. The mirror pins one commit and records the upstream SHA-256 of each file, so a refresh gives a diff and not a mystery. The plain `wikipron` row still reads the upstream branch, so only the restored row has this protection.

The second reason is the lossy orthography. WikiPron pairs a pronunciation with the MediaWiki page title. Several language style policies keep diacritics out of titles and put them back only on the headword line. For those languages the scraped word does not write contrasts that the pronunciation still transcribes. Scoring a grapheme-to-phoneme system on those rows measures the input, not the system.

## Schema

Each file under `data/` is tab-separated, with one header row and the columns `orthography`, `restored_orthography` and `ipa`. There is one file per upstream file. The first and third columns are the two WikiPron columns, byte for byte. The second column is empty where restoration was refused or not attempted, so a refusal shows in the data and is not a missing row.

`scripts/benchmark.py` reads the second column and skips empty cells. The `wikipron_restored` row is therefore a subset of the matching `wikipron` row. Compare it only with that row restricted to the same words.

The build also writes `manifest.json` and the dataset card `README.md`. The manifest holds the upstream commit and its date, the SHA-256 and row count of each file, and a screen record per language.

## The screen

Restoration costs one page render per word, so no language is restored before it is screened. The screen has two halves, and a language passes only if both agree.

The policy half fetches `Wiktionary:About <Language>` once per language and looks for a statement about diacritics in titles against display. The data half counts the marks that the statement names in the scraped orthography. A policy that says macrons never reach titles predicts zero macrons. Where macrons occur in quantity, the policy does not reach this dataset.

Latin is why the data half is required. Its policy says that the page name "should not contain diacritical marks", in almost the same words as the policy of Old English. Its scraped words still carry more than one macron per row on average, and the Old English words carry almost none. One of the two is a real defect and the other is not, and only the data says which. Latin is curated `not_affected` for that reason.

The automatic downgrade covers the next such language. A `confirmed` verdict whose data carries the marks of the policy above `STRAY_RATE` (0.01 marks per row) becomes `not_affected`, and the rate that overturned it is recorded with it.

A verdict is a snapshot of a live wiki, and the wiki changes. The published manifest records Mandarin as `no_policy_page`, but `Wiktionary:About Mandarin` redirects to `Wiktionary:Chinese entry guidelines`, which exists. That page describes no split between title and headword, so the verdict stands, and the mismatch shows what drift looks like. Expect some `no_policy_page` languages to gain a page, and screen again before you trust an old negative. Only the pinned scrape is stable.

`manifest.json` records one of these verdicts per language:

| Verdict | Meaning |
|---|---|
| `confirmed` | A policy states the split, and the gold agrees. |
| `confirmed_empirical` | No policy statement, but the marks are absent from every scraped word. |
| `not_affected` | A policy mentions diacritics and titles, but it creates no split here. |
| `no_policy_page` | `Wiktionary:About <Language>` does not exist. |
| `inconclusive` | The page exists and says nothing decisive. |

A verdict says whether a language is affected, never whether anything was done about it. The separate field `restoration_attempted` records that. A false value means that nobody has run the language, and an empty `restored_orthography` column has no other meaning. A language that ran and recovered nothing has a broken lookup, not an empty Wiktionary. Tundra Nenets did that, because the upstream metadata calls it `yrk` and Wiktionary tags its headwords `yrk-tun`. The build refuses to publish that state, and the restore script exits with status 1.

The screen records negative results on purpose. A language recorded as `not_affected` does not need another investigation.

## What restoration will not do

`scripts/restore_wikipron_orthography.py` never invents a form. These rules apply to every language:

| Rule | Reason |
|---|---|
| The wikitext is cut to the target `==Language==` section before any headword template is read, and the rendered headword is matched on its `lang` attribute. | A page holds one section per language. `Adam` renders an English `Adam` and an Ewe `Ádàm`. `helfen` renders a Middle High German `hëlfen` and an Old High German `hëlfēn`. |
| Whole pages are rendered, never sections. | The cache key of a section render is the page title, but its result depends on the language whose templates were expanded. `ade` is both Ewe and Yoruba. |
| Headwords are read from positional template arguments as well as from `head=`. | `{{ee-proper noun|Àfɔ̀fìɛ́}}` carries its headword positionally. |
| Two headwords that disagree are refused, not resolved. | One unpointed or untoned title often spells several different words. |
| A restored form whose base-letter skeleton differs from the title is discarded. | The skeleton is NFD with the combining marks removed. A different skeleton means more than a restoration of diacritics. |

## Refreshing the mirror

Run the refresh from a checkout of the repository, with the repository venv. It needs network access, a Hugging Face write token for the dataset, and hours of MediaWiki renders for each language whose scrape changed. Before the first step, read `df -h` for the disk that holds the clone and the cache. A large restoration run fills gigabytes.

1. Clone the upstream scrape into a new directory. Use a fresh directory for each refresh. `pin` on an existing clone fetches `master` but does not move `HEAD`, so it reports the old commit.

   ```bash
   python scripts/wikipron_mirror.py pin --clone-dir ~/tmp/wikipron-<date>
   ```

   The command makes a blobless sparse clone of `data/scrape/tsv/` and `data/scrape/lib/languages.json`, and prints the pinned commit as JSON.

2. Fetch the policy pages. The command writes the map of languages to their `Wiktionary:About` pages to the `--policy-pages` file (default `policy_pages.json`).

   ```bash
   python scripts/wikipron_mirror.py screen --clone-dir ~/tmp/wikipron-<date> \
       --policy-pages policy_pages.json
   ```

3. Read the policy page of each language that is new or whose verdict could change. Write a hand-read verdict into `SCREEN` in `scripts/wikipron_mirror.py`, with the verbatim quote and the marks that the policy names. For a confirmed language, add its Wiktionary section name and language code to `LANGS` in `scripts/restore_wikipron_orthography.py`. This step is a judgement, and no script makes it.

4. Restore the languages that are new or whose scrape changed. Point `O2I_WIKIPRON_TSV` at the pinned scrape. The script stops with an error when the variable is not set. Each language writes `<code>.json` to `--out-dir`. An unchanged language is almost free, because the MediaWiki cache holds its pages.

   ```bash
   O2I_WIKIPRON_TSV=~/tmp/wikipron-<date>/data/scrape/tsv \
       python scripts/restore_wikipron_orthography.py ewe gmh yor heb --out-dir restored/
   ```

5. Build the new mirror into a new directory. The build reads the pinned scrape, the restoration maps in `--restored-dir` and the policy pages, then writes `data/`, `manifest.json` and `README.md`.

   ```bash
   python scripts/wikipron_mirror.py build --clone-dir ~/tmp/wikipron-<date> \
       --restored-dir restored/ --out-dir mirror.new/ --policy-pages policy_pages.json
   ```

6. Download the manifest of the published mirror and compare the two snapshots. The diff prints the two commits and each file that was added, removed or changed, with its row counts.

   ```bash
   hf download TigreGotico/wikipron-restored-orthography manifest.json \
       --repo-type dataset --local-dir mirror.old/
   python scripts/wikipron_mirror.py diff \
       --old mirror.old/manifest.json --new mirror.new/manifest.json
   ```

7. Read the diff. Then publish the new mirror.

   ```bash
   hf upload TigreGotico/wikipron-restored-orthography mirror.new/ . --repo-type dataset
   ```

8. Score the `wikipron_restored` row again with `--refresh-cache`, so the harness fetches the new files and not its cached copies. The board procedure is in [contributing/board.md](contributing/board.md).

   ```bash
   python scripts/benchmark.py --dataset wikipron_restored --refresh-cache
   ```

9. Delete the `html/` subdirectory of the MediaWiki cache. Remove the clone directory and the build directories when the refresh is published.

## Why the refresh is manual

The repository has no scheduled workflow for the refresh, on purpose. A refresh needs a write token for a public dataset and hours of MediaWiki renders. It also needs a judgement on the screen verdict of each new language, which a regular expression cannot make. An unattended job that republished a public dataset would move benchmark numbers with nobody reading the diff. That is the failure that the pin prevents.

The pin makes the manual cadence safe. Until someone runs the refresh, the data does not move.

A restoration run can resume. Every fetched page goes to the cache before it is used. A run that stops, or one whose connection stalls over thousands of requests, can be killed and started again. The only cost is the pages that were in flight.

## Caches and disk

The restore script reads these environment variables:

| Variable | Default | Purpose |
|---|---|---|
| `O2I_WIKIPRON_TSV` | none, required | The `data/scrape/tsv` directory of the pinned clone. |
| `O2I_WIKT_CACHE` | `~/tmp/o2i-wiktionary-cache` | The MediaWiki cache, with `wikitext/` and `html/` subdirectories. |
| `O2I_WIKT_RATE` | `3` | Requests per second against the MediaWiki API. |
| `O2I_WIKT_WORKERS` | `4` | Concurrent requests under the same rate cap. |

The cache holds one file per page title, with wikitext and rendered HTML in separate subdirectories. The renders take most of the space, and the cache grows to gigabytes over a large restoration run. Set `O2I_WIKT_CACHE` to a disk with room. Delete the `html/` subdirectory once a run is published. The wikitext half is small, and it is what makes a later screen cheap.

---
[← Benchmark gold datasets](benchmark_datasets.md) · [Home](index.md) · [TTS sentence gold sets →](tts_gold.md)
