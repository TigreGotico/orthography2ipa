# Gold composition: how much of a row is alphabet, not text

The [scoreboard](scoreboard.md) reports one PER per gold row, and that
number is only informative about running-text accuracy if the gold is
made of running text. WikiPron scrapes Wiktionary headwords, and for a
small language a Wiktionary edition often carries a full "letters of the
alphabet" appendix as ordinary headwords — single letters, digraph
names, diacritic-marked letter variants — sitting in the same TSV as real
words. A grapheme table transcribes those trivially by construction: it
IS the grapheme table, read back. A row can therefore look excellent
while the gold behind it says almost nothing about how the spec handles
an actual sentence.

This page records how much of that is happening across the board, using
[`scripts/gold_composition.py`](../scripts/gold_composition.py). It
reads each row's already-scored gold from the on-disk cache (it never
fetches new data — see "reading this page" below), splits it into a
trivial subset and a real-word subset, and scores each with the same
harness path the board uses, so `trivial_per` and `real_per` sit in the
same units as the board's `PER` column.

## What counts as trivial, and what was rejected

A fixed length cutoff — "any entry of length <=2 is trivial" — was the
first thing tried and it does not hold up: plenty of registered
languages have short real words (single-letter function words like
French "y" or English "a", monosyllabic content words in many language
families), and a length threshold would misclassify those identically in
every language regardless of how that language's words are actually
shaped. Chinese monosyllables would take the same hit as Kwak'wala
alphabet-chart rows for reasons that have nothing to do with each other.

The signal used instead is tied to the language's own declared alphabet:
every registered spec carries a `graphemes` table (the orthographic
units it maps to IPA — plain letters, but also multi-character units
like digraphs, e.g. Kwak'wala's `kw`, `ch`, `dz`). An entry is a
candidate "short form" if it collapses, once case- and
diacritic-folded, to one or two characters. If the DISTINCT short forms
in a row's gold cover at least 30% of the spec's own alphabet, that
row's short entries are treated as an alphabet chart and marked
trivial; below that coverage they are left as ordinary short words. A
handful of coincidentally short real words never comes close to 30%
coverage of a real alphabet; an actual "letters of the language" scrape
usually clears 60-90% of it. Sentence-level gold entries (space-
separated multi-word rows, from the sentence-level TTS/dialect gold
sets) are never eligible: an alphabet chart is a word-level phenomenon.

This catches more than plain single letters. Diacritic-marked chart rows
(Kwak'wala's "A̱", a bare `a` with a combining macron below, distinct
from the phonemically different plain `a`) fold to the same base form as
their bare letter and are counted once. Multi-character alphabet units —
a chart row that spells out the digraph `kw` as its own headword rather
than a running-text occurrence of it — are recognized too, because the
comparison is against the spec's alphabet, not against a fixed
character-length rule.

What this definition does NOT try to do: identify individual entries
whose gold transcription is a letter NAME rather than the letter's
phonetic value in running text (e.g. an English "y" glossed as /waɪ/, the
name "why", rather than any phonetic value the grapheme takes inside a
word). That would need a per-language table of letter names, which does
not exist here, and guessing it from gold data alone risks manufacturing
the very kind of unsourced rule this project's phonology discipline
rejects. Where it matters, it is visible indirectly: a chart-flagged row
whose trivial-subset PER is unexpectedly *high* despite scoring "the
grapheme table read back" usually means the gold is glossing several
entries with letter names the engine correctly does not produce.

## Reading this page

Every row here was scored from whatever is already sitting in
`.benchmark_cache/` — the script never performs a network fetch. A gold
set that has never been pulled to this machine is skipped and counted
in "rows skipped (no cached gold)" below rather than silently
downloaded, so this page's numbers depend only on what was measured,
never on ambient network access.

`trivial_share` is the fraction of a row's covered gold that the
alphabet-coverage test flagged. `gap` is `real_per − trivial_per`: a
large **positive** gap is the finding this page exists to surface — the
row's headline PER is dragged down by an easy trivial subset while the
real-word subset (the part that actually says something about running
text) scores considerably worse. A **negative** gap means the opposite
happened: the trivial subset scored worse than the real words, which can
happen on a very small chart-flagged row (few genuine words left to
average over) or when the chart entries carry letter-name glosses the
engine cannot reproduce (see above) — in that case the alphabet chart is
not flattering the row, it is dragging it down, and that is reported
honestly rather than folded into the same "flattered" ranking.

`real_n` is the covered word count behind `real_per`. A `gap` computed
from a handful of real words (a chart-heavy small gold set with only a
few genuine entries left over) is noisy in the same way any small-n PER
is noisy on the main scoreboard, and should be read with that
qualification rather than as a settled number.

## The board today

This run scored the 484 board rows whose gold set has 5000 entries or
fewer against what is already sitting in `.benchmark_cache/` (every one
of those had a cache hit — nothing was skipped for a missing gold). The
remaining 155 rows, all above that size, were not loaded at all: a
spec's declared alphabet runs to at most a few dozen graphemes, so even
in the worst case where every alphabet entry appears verbatim as a
headword, the trivial share of a >5000-word gold set is bounded well
under any threshold this page reports against — for most languages.
That bound does NOT hold for languages whose script uses one
character per morpheme: a spot check of `ja/ipadict` (233166 raw
entries once expanded) came in at 28.2% trivial share despite being far
over the cutoff, so the 155 skipped rows are not a blanket "safe to
ignore" set, and a CJK-flavoured row among them could show a real
finding a future run should check explicitly (`--max-n` with a higher
bound, or none at all, accepting the longer runtime).

Of the 484 rows actually scored, 55 have any trivial entries at all, and
**12 rows carry a trivial share above 20%**:

| Lang | Dataset | N | Trivial share |
|---|---|---:|---:|
| kwk | wikipron | 116 | 93.1% |
| sms | wikipron | 119 | 66.4% |
| ktz | wikipron | 135 | 69.6% |
| ab | wikipron | 206 | 63.6% |
| ba | wikipron | 208 | 55.3% |
| dz | wikipron | 243 | 49.0% |
| dv | wikipron | 1551 | 34.4% |
| si | wikipron | 393 | 29.3% |
| new | wikipron | 416 | 27.9% |
| lut | wikipron | 140 | 27.1% |
| bo | wikipron | 3621 | 26.7% |
| kas | wikipron | 751 | 23.7% |

The ten rows whose headline is most flattered by their trivial subset —
ranked by `gap` (`real_per − trivial_per`), the finding this page exists
to surface, not by raw trivial share:

| Lang | Dataset | N | Trivial share | Trivial PER | Real PER | Gap |
|---|---|---:|---:|---:|---:|---:|
| nup | wikipron | 453 | 17.2% | 0.0572 | 0.4679 | +0.4107 |
| ktz | wikipron | 135 | 69.6% | 0.2652 | 0.5305 | +0.2653 |
| bo | wikipron | 3621 | 26.7% | 0.2103 | 0.4266 | +0.2163 |
| yo | wikipron | 4937 | 7.6% | 0.2011 | 0.3913 | +0.1902 |
| ab | wikipron | 206 | 63.6% | 0.2949 | 0.4663 | +0.1714 |
| nv | wikipron | 995 | 4.2% | 0.0944 | 0.2579 | +0.1634 |
| tk | wikipron | 452 | 11.1% | 0.2195 | 0.3728 | +0.1533 |
| ba | wikipron | 208 | 55.3% | 0.1899 | 0.3361 | +0.1462 |
| ky | wikipron | 888 | 6.5% | 0.0952 | 0.2282 | +0.1329 |
| dz | wikipron | 243 | 49.0% | 0.2775 | 0.3939 | +0.1164 |

`kwk/wikipron` — the row this page's method was built against — is a
counter-example worth reading closely rather than a confirmation: 116
raw gold entries, 108 of them (93.1%) trivial under this definition
(mostly single Latin letters, several diacritic-marked chart rows like
"A̱"), but its trivial PER (0.5039) is actually *worse* than its real-word
PER (0.3533), not better — `gap = −0.1506`. With only 8 real words left
to average over, that real-word number is too small-n to lean on, but
the direction is still informative: on the current spec, the alphabet
chart is not what makes this row's headline look good — if anything it
drags it down. The 0.007 PER a spec fix produced on this row in an
earlier, unmerged pass is not reproduced here because that fix is not on
this branch: this page reads whatever is on `dev`.

`tru/wikipron`'s bound-affix rows (entries beginning with U+0640
TATWEEL, inflection-table cells rather than free words — see
`_TATWEEL`'s docstring in the script) account for 6 of its 232 raw
entries, 2.6%: a real but small effect on this dataset, and again a
negative gap (0.6062 trivial vs 0.4823 real) — the bound forms are
harder for the spec, not easier.

## What this page is not

It is not a spec fix, and applying it never moves `docs/scoreboard.md`
or `benchmarks/results.json` — those are regenerated only by
`scripts/benchmark.py`, from the spec's actual behavior. A large `gap`
on a row here is a flag that the row's headline number needs a bigger,
more representative gold before it can support a claim about running-
text accuracy, not evidence that the spec itself is wrong. And, like
every number on the scoreboard, a `trivial_per` or `real_per` computed
from a `crowd-scraped` or lower provenance tier inherits that tier's
caveats in full — see
[`docs/benchmarks.md`](benchmarks.md#provenance-and-reliability-read-this-before-trusting-any-number).

---
[← Lexicon-overlay scoreboard](lexicon_scoreboard.md) · [Home](index.md) · [Gold defects →](gold_defects.md)
