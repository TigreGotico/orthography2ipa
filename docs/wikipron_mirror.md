# The pinned WikiPron mirror

`TigreGotico/wikipron-restored-orthography` is a snapshot of every
pronunciation scrape in [CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron),
taken at one commit, with a second orthography column holding the
headword English Wiktionary displays.

It exists for two reasons.

The first is reproducibility. WikiPron publishes its scrapes on a branch
it keeps editing. A benchmark that reads that branch scores against
different data from one week to the next with no code change, which
makes an upstream edit indistinguishable from an engine regression. The
mirror pins one commit and records each file's upstream SHA-256, so a
refresh produces a diff instead of a mystery.

The second is the lossy orthography. WikiPron pairs a pronunciation with
the MediaWiki **page title**. Several language style policies keep
diacritics out of titles and put them back only on the headword line, so
for those languages the scraped word no longer writes contrasts the
pronunciation still transcribes. Scoring a grapheme-to-phoneme system on
those rows measures the input, not the system.

## Schema

`orthography`, `restored_orthography`, `ipa`, tab separated, one header
row, one file per upstream file under `data/`. Columns one and three are
WikiPron's own two columns, byte for byte. Column two is empty wherever
restoration was refused or has not been attempted, so a refusal is
visible in the data rather than a missing row.

`scripts/benchmark.py` reads column two and skips empty cells, which is
why the `wikipron_restored` row is a subset of the matching `wikipron`
row and comparable only to that row restricted to the same words.

## The screen

Restoration costs one page render per word, so no language is restored
before it is screened. The screen is cheap and has two halves, and a
language passes only if both agree.

The policy half fetches `Wiktionary:About <Language>` once per language
and looks for a statement about diacritics in titles as against display.
The data half counts the marks that statement names in the scraped
orthography. A policy saying macrons never reach titles predicts zero
macrons; where they are present in quantity the policy does not reach
this dataset.

Latin is why the second half is not optional. Its policy says the page
name "should not contain diacritical marks", almost word for word like
Old English's, and yet its scraped words carry more than a hundred
thousand macrons across eighty-eight thousand rows. Old English, with
the same policy, carries four. One is a real defect and the other is
not, and only the data says which. Latin was caught by reading the
policy and the count together, and is curated `not_affected` on that
basis. The automatic downgrade exists so the next such language does not
depend on a reader noticing: a `confirmed` verdict whose data carries
the policy's marks above a stray rate becomes `not_affected`, with the
rate that overturned it recorded beside it.

A verdict is a snapshot against a live wiki, and the wiki moves.
Mandarin is recorded `no_policy_page`, yet `Wiktionary:About Mandarin`
redirects to `Wiktionary:Chinese entry guidelines`, which exists. That
page describes no title/headword split, so the verdict stands, and the
mismatch is what drift looks like. Expect some `no_policy_page` to have
grown a page, and re-screen before trusting an old negative. Only the
pinned scrape is stable.

Verdicts recorded in `manifest.json`:

| Verdict | Meaning |
|---|---|
| `confirmed` | a policy states the split, and the gold agrees |
| `confirmed_empirical` | no policy statement, but the marks are absent from every scraped word |
| `not_affected` | a policy mentions diacritics and titles but creates no split here |
| `no_policy_page` | `Wiktionary:About <Language>` does not exist |
| `inconclusive` | the page exists and says nothing decisive |

A verdict says whether a language is affected, never whether anything
was done about it. `restoration_attempted` is the separate fact: false
means nobody has run the language yet, and the empty
`restored_orthography` column carries no other meaning. A language that
was run and recovered nothing has a broken lookup rather than an empty
Wiktionary — Tundra Nenets did exactly that, upstream's metadata calling
it `yrk` where Wiktionary tags its headwords `yrk-tun` — so the build
refuses to publish that state and the restore script exits non-zero.

Negative results are recorded on purpose. A language written down as
`not_affected` does not have to be investigated again.

## What restoration will not do

`scripts/restore_wikipron_orthography.py` never invents a form.

* A Wiktionary page holds one section per language. The wikitext is cut
  to the target `==Language==` section before any headword template is
  read, and the rendered headword is matched on its `lang` attribute.
  `Adam` renders an English `Adam` and an Ewe `Ádàm`; `helfen` renders a
  Middle High German `hëlfen` and an Old High German `hëlfēn`.
* Whole pages are rendered, never sections. A section render's natural
  cache key is the page title while its result depends on the language
  whose templates were expanded, and `ade` is both Ewe and Yoruba.
* Headwords are read from positional template arguments as well as
  `head=`: `{{ee-proper noun|Àfɔ̀fìɛ́}}` carries its headword positionally.
* Two headwords that disagree are refused, not resolved. One unpointed
  title often spells several distinct words.
* A restored form whose base-letter spine differs from the title is
  discarded.

## Refreshing

One documented sequence, run from a checkout:

```bash
# 1. Re-pin upstream and record what moved.
python scripts/wikipron_mirror.py pin --clone-dir ~/tmp/wikipron
python scripts/wikipron_mirror.py diff \
    --old mirror/manifest.json --new mirror.new/manifest.json

# 2. Screen any language whose file is new or changed.
python scripts/wikipron_mirror.py screen --clone-dir ~/tmp/wikipron

# 3. Re-restore only the changed languages. The MediaWiki cache under
#    $O2I_WIKT_CACHE makes an unchanged language nearly free.
python scripts/restore_wikipron_orthography.py <lang> --out-dir restored/

# 4. Rebuild the mirror and its card, then publish.
python scripts/wikipron_mirror.py build --clone-dir ~/tmp/wikipron \
    --restored-dir restored/ --out-dir mirror/
huggingface-cli upload TigreGotico/wikipron-restored-orthography \
    mirror/ . --repo-type dataset
```

There is no scheduled workflow, deliberately. A refresh needs a write
token for a public dataset, hours of MediaWiki renders for any language
whose scrape changed, and a judgement call on each new language's screen
verdict that a regular expression cannot make. A job that republished a
public dataset unattended would move benchmark numbers with nobody
reading the diff, which is the failure the pin exists to prevent. The
pin is what makes the manual cadence safe: until someone runs the
refresh, the data does not move.

A restoration run is resumable. Every page fetched is written to the
cache before it is used, so a run that is interrupted — or one whose
connection stalls, which happens over thousands of requests — can be
killed and started again at no cost beyond the pages in flight.

## Caches and disk

The MediaWiki cache defaults to `~/tmp/o2i-wiktionary-cache` and holds
one file per page title, wikitext and rendered HTML separately. Renders
dominate it and it grows to gigabytes across a large restoration run.
Set `O2I_WIKT_CACHE` to place it somewhere with room, and delete the
`html/` subdirectory once a run is published: the wikitext half is small
and is what makes a re-screen cheap.
