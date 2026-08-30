# Benchmark methodology

How a score is computed, how to reproduce one, and how to work out why a
language scores the way it does. The datasets these numbers are measured
against are catalogued in
[benchmark_datasets.md](benchmark_datasets.md), and what their provenance
tiers mean is in [benchmarks.md](benchmarks.md).

## Diagnosing a language

The scoreboard tells you *that* a language scores badly. It does not tell
you *why*. `scripts/error_analysis.py` is the microscope: it runs a gold
dataset through the engine and reports where the errors concentrate, so
spec work starts from evidence instead of guesswork. It is strictly
read-only: it never touches a spec or any other file.

```bash
PYTHONPATH=$PWD python scripts/error_analysis.py pt-PT --dataset portuguese_unified --limit 300
```

`<lang>` is required. `--dataset` is optional (when omitted, the first
registered dataset that covers the language is used), `--limit` caps the
gold slice (default 300, same as the benchmark harness), and `--json`
emits all three sections as one JSON object instead of the text report.
Alignment reuses the same routine (`scripts.benchmark.align`) and the
same default normalization (stress marks and narrow diacritics stripped)
that the scoreboard uses, so what you see here matches how PER is scored.

The report has three sections. Read them in this order:

1. **Top-20 phoneme confusion pairs** (`gold -> hyp`). Each row is an
   aligned mismatch, ranked by how often it occurs. `∅` on the gold side
   is an *insertion* (the engine emitted a phoneme the gold does not
   have). `∅` on the hyp side is a *deletion* (the engine dropped a gold
   phoneme). A single high-count pair: e.g. `'r' -> 'ɾ'`: is usually
   one wrong or missing grapheme/allophone rule and the fastest fix.

2. **Top-20 worst words**: the words with the highest per-word PER, gold
   and hyp side by side. Use these to see the confusion pairs *in
   context*: whether a substitution is systematic (every word) or
   conditioned (only before front vowels, only word-finally, etc.), which
   tells you whether the fix is a flat grapheme change or a positional
   rule.

3. **Per-grapheme blame**: for each orthographic character/digraph in
   the spec's grapheme map, the mean PER of gold words containing it
   (minimum 3 occurrences), worst-first. This points at which *spelling*
   is costing you accuracy. It is a triage signal (substring containment,
   not tokenization), so treat a high-blame grapheme as "look here first",
   then confirm against the confusion pairs and worst words.

Feed the top confusion pairs into the per-language procedure: classify
each systematic error (missing/wrong grapheme mapping, missing positional
rule, missing sandhi, stress placement, or genuinely lexical), cite a
published source for every spec change, and re-run the tool to confirm
the pair's count dropped.

## Methodology

- **PER**: character-level Levenshtein distance over IPA, divided by
  reference length. Mean over evaluated words. **WER**: fraction of
  words with any error.
- **Multi-reference**: rows are grouped by word and a hypothesis is
  scored against every gold variant, keeping the minimum PER.
- **Segmentation-free**: whitespace is removed before comparison (some
  gold sets space-separate phonemes).
- **Default normalization**: stress marks and narrow-transcription
  apparatus (raising/dentality diacritics, syllable separators, tie
  bars) are stripped from both sides: gold sets differ in
  transcription depth, and the engine should not be scored on notation
  conventions. `--keep-stress` / `--narrow` disable this.
- The committed `--scoreboard` scores the **full** gold set of every
  language (no cap), so each row's `N` is the number of gold words covered,
  not a sample (see
  "Full-dataset scoreboard" below). Ad-hoc `--limit N` runs (and the CI
  regression sample) apply a uniform cap for speed. Those are reference
  points, not the published number.

### Full-dataset scoreboard

The committed scoreboard (`docs/scoreboard.md` / `benchmarks/results.json`)
is **full-dataset**: `scripts/benchmark.py --scoreboard` scores the entire
gold set of every registered dataset/language with **no cap**, applied
uniformly (there is no per-language limit). The `N` column is therefore the
real number of covered gold words, not a sample size. Regenerating it is
slow (the 598k-row `portuguese_unified` gold
dominates the runtime), which is why the CI regression gate does *not* re-run
it in full: see below.

`--limit N` still exists for ad-hoc fast runs and applies the **same** cap
`N` to every language (never a per-language mix). The one dataset that stays
bounded even under the full run is `hitz_basque_ipa`: its loader pages the
Hugging Face rows API and stops at `_HITZ_BASQUE_MAX_PARAGRAPHS` (500)
paragraphs rather than pulling the full 1.67M-row corpus: a fixed,
language-agnostic paging bound, not a sampling `--limit`, disclosed in its
dataset section above.

**CI regression strategy (full-vs-sample would be dishonest, so it isn't
done).** Re-running the full scoreboard inside a PR CI job is too slow to be
practical, but comparing a *sampled* current run against the *full* baseline
would compare two different slices and manufacture spurious "regressions".
So the gate never mixes slices: `scripts/check_benchmark_regression.py`
re-scores at a fixed **uniform** sample (`benchmark.CI_SAMPLE_LIMIT`, the
same cap for every language) and compares against a **separate** baseline
committed at that identical cap, `benchmarks/results_ci_sample.json`
(generated by `scripts/benchmark.py --ci-sample`, clearly labeled the "CI
regression sample"). Both sides are sliced identically, so a flagged
regression is a real PER change, not slice noise. The published docs
scoreboard stays full regardless. A minimum-scored-row floor still fails the
gate closed if a wholesale dataset-loading outage would otherwise produce a
false green. Refresh `results_ci_sample.json` whenever the full scoreboard is
regenerated.

**Board staleness is a separate failure the regression gate cannot see.**
That gate is one-sided: it fires when a row gets WORSE, so a row left
behind by a change to its own gold loader publishes a stale number
indefinitely and CI stays green. `scripts/check_board_row_counts.py` is
the tripwire for that. It reloads each committed row's gold and fails when
the row's `n` exceeds the pair count the loader now yields, which is an
impossibility — scoring consumes the loader's output, so `n` sits at or
below it. The check is deliberately one-directional, because an `n` BELOW
the pair count is normal: `ja` scores 42.5k of 48.6k pairs, since the kana
spec produces no hypothesis for a kanji-only word. A row whose loader
refuses the language outright is reported too, which catches a board row
fossilised by a de-registration. Run it after every board regeneration:

Read the Japanese rows with that partial coverage in mind, because dropping
the kanji-only words removes far less of the problem than it looks. A word
is scored the moment it contains one kana, and most Japanese words are a
kanji stem with a kana ending, so the majority of scored words hand the
engine an okurigana and ask it for the whole reading. Those words carry
roughly six times the error rate of the words written in kana throughout,
and they outnumber them, so the published Japanese PER is mostly a
measurement of the missing kanji front-end. The kana→IPA quality the spec
actually controls is visible only in the all-kana subset, which has to be
split out by hand — no board column reports it.

```bash
PYTHONPATH=$PWD python scripts/check_board_row_counts.py
```

### Confidence intervals

Every scoreboard row (`docs/scoreboard.md` / `benchmarks/results.json`)
carries a 95% bootstrap confidence interval on the mean PER, alongside
the point estimate, so a single-slice PER number can be read with its
uncertainty rather than as a false-precision leaderboard entry:

- The per-word PER list underlying a row's mean PER is resampled with
  replacement 1000 times. The mean of each resample is computed, and
  the interval is the 2.5th/97.5th percentile of that distribution.
- Resampling uses `random.Random(BOOTSTRAP_SEED)` (`scripts/benchmark.py`),
  never the global RNG, with a fixed seed constant: the same input PER
  list always yields the same `[low, high]` bounds, on any machine, on
  any run. This is what makes the CI reproducible rather than a
  moving target that would itself trigger false benchmark-regression
  noise.
- The regression gate (`scripts/check_benchmark_regression.py`) keeps
  comparing the point-estimate PER against the committed baseline with
  its existing epsilon: the CI is a reporting/diagnostic addition, not
  part of the pass/fail regression check.
- A wide interval is itself informative: it flags a row whose PER is
  noisy given its sample size (small `N`, or high per-word variance),
  and is a signal to grow the gold set before trusting a narrow slice
  of PER movement as a real regression or improvement.
- A narrow interval is only informative when `N` backs it up. Bootstrap
  resampling draws its samples from the row's own per-word PER list, so
  on a handful of words it can only ever reshuffle the same handful of
  values back at itself: a row scored on one word gets a `[x, x]`
  interval that looks perfectly precise, and a row scored on two or
  three words gets one nearly as tight, purely because there was
  nothing to resample. That is an artifact of the sample size, not
  evidence the PER is well measured. `docs/scoreboard.md` marks any row
  under 20 scored words with a `†` after its `N` for exactly this
  reason: read a marked row's PER as a single anecdote, never rank it
  against, or average it with, an unmarked row scored on hundreds or
  thousands of words. A row's weight on the board is its `N`, not its
  position in a PER sort.

### Top-k oracle PER (lattice quality vs ranking error)

A single PER number answers "was the first guess right". It cannot say
*why* a wrong guess was wrong. Two very different failures hide behind
one score:

- **Ranking error** — a BETTER reading than the one the engine ranked
  first is somewhere in the top-k. Nothing is missing from the language
  data; the weights ordered the beam badly. This is recoverable
  downstream: consumers of the lattice rescore it.
- **Model error** — no better reading exists in the lattice at any
  depth. No reranking can find one. Only new rules or new data fix this.

**Oracle PER@k** separates the two. It is the per-word *minimum* PER
over the engine's top-k readings, averaged exactly like the 1-best PER
(same normalization, same edit distance, same multi-gold rule). So:

    PER − Oracle@k   = ranking error  (the rescoring headroom)
    Oracle@k         = model error    (what rules/data must fix)

The columns `Oracle@3` and `Oracle@5` are in `docs/scoreboard.md` and
`benchmarks/results.json` (`oracle_per_top3`, `oracle_per_top5`).

**The headroom is an upper bound, not a forecast.** An oracle picks the
best candidate per word *after seeing the gold*. No real rescorer has
that information, so `PER − Oracle@k` is the ceiling on what any
reranking could ever buy, and a deployed rescorer will realize some
fraction of it. Quote it as a ceiling.

**A better reading is not the right reading.** `Oracle@k` dropping means
a CLOSER candidate is in the beam — closer in edit distance, and usually
still wrong. The strict version is the **`OracleX@k`** columns
(`oracle_exact_top3`, `oracle_exact_top5`): the fraction of words where
some top-k candidate *equals* a gold exactly. That is the `Exact match`
column generalized from k=1 to k. Measured on the current board, only a
minority of the PER-oracle gain is exact hits — fr 41.4%, de 25.8% —
so the PER oracle overstates "the engine already knows the answer" by
roughly 2x. Use `OracleX@k` for any claim of that shape. Both shares are
computed on the board's numbers and therefore **without injected
alternatives** (see the next section): the ratio is taken over the
committed row's `PER → Oracle@5` and `Exact match → OracleX@5`, never
over the injected-alternative figures, which would inflate it.

### Injected alternatives do not count as ranking error

Some oracle movement is not a discovery about the engine. It is a reading the
data **deliberately injected** into the beam — a list-valued
`grammatical_endings` entry, which adds a licit reading the spec cannot choose
between so that a downstream rescorer can (see
[SCHEMA.md](../orthography2ipa/data/SCHEMA.md#ambiguous-endings)). French
⟨-ent⟩ is the first of these.

**HARD rule: oracle@k movement caused by an injected alternative is reported
separately, under its own heading, and never counts toward ranking-error
analysis or any beat-espeak claim.**

**This is enforced by construction, not by discipline.** The scoreboard run
builds its engine with `G2P(lang, expose_ambiguous_endings=False)`, so a
list-valued ending contributes nothing to the beam it scores: every oracle cell
in `docs/scoreboard.md` and `benchmarks/results.json`, for every language and
every dataset, is measured on the beam the engine RANKS. A row whose language
declares injected alternatives records which ones it excluded in
`oracle_injected_alternatives` (`["fr-FR ent"]` on the fr/wikipron row), so the
exclusion travels with the numbers. That field is derived from the flag the row
was **scored with**, not from the spec: a row measured with exposure on claims
no exclusion and leaves the field off, because a provenance field that asserts
an exclusion the run did not perform is worse than no field at all. 1-best is
identical either way — an
alternative can never reach rank 1 — so the `PER` and `Exact match` columns do
not depend on this choice at all.

To measure the injected movement itself, pass the flag explicitly:

```python
evaluate_words_oracle(pairs, "fr", strip_stress=True, broad=True,
                      expose_ambiguous_endings=True)
```

Reproduced on the full fr/wikipron row (n=85495): `PER 0.0888` and
`Exact match 0.6185` in BOTH modes; `Oracle@5 0.0665 → 0.0627` and
`OracleX@5 0.6712 → 0.6888` when the ⟨-ent⟩ alternative is exposed, with
`Oracle@3` unmoved at `0.0723` because the mute reading lands at rank 4-5. The
first pair is the accuracy claim, and its invariance is the proof that an
injected reading never reaches rank 1; the second pair is reachability and
belongs only under this heading.

The reason is that the two would otherwise be the same number measured
differently. `PER − Oracle@k` is meant to read as "the engine already produced a
better answer and mis-ranked it" — a property of the weights that a rescorer
could realise. An injected alternative moves that gap by *construction*: adding
candidates to the beam can only lower an oracle, so any spec could raise its own
oracle arbitrarily by declaring more alternatives, while the 1-best does not
move and nothing about the ranking got better. Folding it into the headroom
would be marking our own diagnostic to our own edit.

So, when reporting:

- Give the 1-best columns first, and say they are unchanged. That is the claim
  an injected alternative is allowed to make.
- Give the oracle delta under an explicit **injected-alternative oracle
  movement** heading, naming the ending and the spec that declares it.
- Do not add it to a `PER − Oracle@k` headroom figure, a ranking-error budget,
  or a per-phenomenon ranking-failure count.
- Never carry it into `comparison.md` or any "beats espeak / epitran / X"
  sentence. Those compare one pronunciation to one pronunciation, and this is
  the k-inflating case the oracle ban below already exists for.

The value of an injected alternative is *reachability* — the reading exists for
a rescorer that has the fact we do not. Report it as reachability (for example,
"gold in top-10 went 0 → 192 of 300 gold-mute types"), not as accuracy.

### The Oracle@1 self-check

The readings come from `G2P.word_candidates`, which runs every beam path
through the same word-final pipeline as `transcribe_word` — geminate
collapse, grammatical-ending rewrite, stress marking, lexicon override.
Element 0 is therefore normally `transcribe_word`'s own answer, which is
what makes Oracle@1 equal the PER column.

That identity is **not guaranteed by construction**: `transcribe_word`
defaults to greedy width-1 search, while `word_candidates` runs a
width-`max(k, 8)` beam, and a wider beam may reach a cheaper path that
greedy pruning discarded. The two agree on every gold set measured, but
the harness verifies rather than assumes: it computes Oracle@1 on every
run, and if it differs from PER — or if any word's candidate 0 differs
from its 1-best — the run prints `ENGINE BUG` and **exits non-zero
without writing the scoreboard**. A corrupt committed artifact reported
as success is worse than a failed run.

**Oracle@k is a diagnostic for this engine only. It must never appear
in a cross-system comparison or a "beats X" claim.** espeak-ng, epitran
and every other system in [`comparison.md`](comparison.md) emit ONE
pronunciation. Setting their single answer against the best of k of ours
compares k guesses to one, and any conclusion drawn from it is an
artifact of the k. `scripts/compare_systems.py` does not read these
fields, and the CI regression gate
(`benchmarks/results_ci_sample.json`) stays 1-best.

Two more limits worth stating plainly:

- **Word-level only.** The beam is per word. Sentence-level gold sets
  (`4catac` and the TTS gold sets — note `vox_communis` is *word*-level
  and does get an oracle) get none: the columns read `-` and
  `oracle_scored_words` is `0`. Composing a sentence-level beam out of
  word beams would invent a ranking the engine never produces, so the
  harness refuses to.
- **`·` is not `-`.** A cell reads `·` when the row has not been
  rescored since the oracle columns were added, and `-` when the row is
  sentence-level and can never have one. A full scoreboard is ~10M
  scored words, so most rows are still `·` and get refreshed in batches.
  The two states are never merged into one blank: an unrescored row must
  not read as "no ranking error".
- **Phenomena-neutral.** The gap says a better reading was mis-ranked.
  It does not say *which* phonological phenomenon is involved. Use
  [`error_analysis.py`](../scripts/error_analysis.py) for that.

Cost, measured on `fr` WikiPron (85k words, beam width 8): **1.63x** the
1-best run in a cold process (2.04s vs 1.25s over a 3000-word probe,
reproduced across runs). That is cheap enough that `--scoreboard` opts
in; `--no-topk` turns it off for a fast ad-hoc rerun.

`build_scoreboard(..., oracle=...)` defaults to **off**, and each caller
opts in explicitly. The CI regression gate
(`check_benchmark_regression.py`) and the `--ci-sample` baseline compare
1-best PER only, and would otherwise pay 1.6x across every row for
columns they never read.

Because a full scoreboard is ~10M scored words, rows can be refreshed a
few at a time and merged into the committed board:

```bash
PYTHONPATH=$PWD python scripts/benchmark.py --scoreboard \
    --dataset wikipron --lang fr
```

A subset run scores each row exactly as the full run does; the rows it
did not touch are carried through unchanged.

### Rules-only vs with-lexicon PER (lexicon overlay)

Languages that ship an optional lexicon overlay
(a caller-registered TSV, never bundled: see
[`data_model.md`](data_model.md#lexicon-overlay-sidecar-word_exceptions-at-scale))
are scored **twice** on the same gold: once with the lexicon disabled
(`get_lexicon` stubbed to `{}`, the "rules-only PER") and once with it active
(the "with-lexicon PER"). This keeps rule quality honest: the overlay has to
*improve* PER without letting the underlying grapheme rules rot behind lexicon
coverage. The results live in a dedicated report, separate from the main
scoreboard (which is untouched: languages with no lexicon are byte-identical
with or without this feature):

```bash
python scripts/benchmark.py --lexicon-report
```

writes [`lexicon_scoreboard.md`](lexicon_scoreboard.md) and
`benchmarks/lexicon_results.json`. Each row reports both the **full-slice**
delta and the **covered-subset** delta (scoring restricted to gold words the
lexicon actually contains: where the overlay can act). The covered-subset
delta is the honest measure of the lexicon's own accuracy vs the rules on the
*same* words. The full-slice number is diluted by every gold word outside the
deliberately capped, top-frequency pilot lexicon. The shipped `en-GB` pilot
(CMUdict-derived, General American) cuts PER on covered words roughly in half
against the independent WikiPron gold: the pilot proves the mechanism. Full
production lexica belong downstream.

## Reference numbers

`python scripts/benchmark.py --dataset <d> --lang <l> --limit 300`:

| Dataset | Lang | N | PER | WER |
|---|---|---:|---:|---:|
| wikipron | eo | 300 | 0.030 | 0.13 |
| wikipron | fi | 294 | 0.039 | 0.25 |
| wikipron | ro | 281 | 0.060 | 0.36 |
| wikipron | gl | 264 | 0.073 | 0.37 |
| wikipron | eu | 240 | 0.077 | 0.41 |
| wikipron | ast | 300 | 0.088 | 0.41 |
| wikipron | sq | 249 | 0.092 | 0.31 |
| wikipron | es | 298 | 0.100 | 0.52 |
| wikipron | it | 276 | 0.101 | 0.51 |
| wikipron | pl | 287 | 0.120 | 0.64 |
| wikipron | sk | 300 | 0.121 | 0.53 |
| wikipron | tr | 296 | 0.138 | 0.60 |
| wikipron | el | 298 | 0.152 | 0.69 |
| wikipron | oc | 266 | 0.160 | 0.63 |
| wikipron | pt | 243 | 0.190 | 0.71 |
| wikipron | cy | 271 | 0.217 | 0.70 |
| ipadict | is | 300 | 0.230 | 0.91 |
| mirandese | mwl | 205 | 0.230 | 0.76 |
| wikipron | is | 258 | 0.223 | 0.86 |
| wikipron | hr | 292 | 0.276 | 0.98 |
| wikipron | tl | 269 | 0.231 | 0.96 |
| ep_dialects | pt-PT | 30 | 0.260 | 1.00 |
| ep_dialects | pt-PT-x-porto | 40 | 0.342 | 1.00 |
| ep_dialects | pt-PT-x-madeira | 30 | 0.362 | 1.00 |
| ep_dialects | pt-PT-x-algarve | 30 | 0.394 | 1.00 |
| ep_dialects | pt-PT-x-lisbon | 45 | 0.398 | 1.00 |
| ep_dialects | pt-PT-x-alentejo | 30 | 0.423 | 1.00 |
| ep_dialects | pt-PT-x-acores | 29 | 0.474 | 1.00 |
| wikipron | nl | 260 | 0.314 | 0.83 |
| wikipron | fr | 279 | 0.318 | 0.81 |
| wikipron | sv | 279 | 0.351 | 0.94 |
| wikipron | de | 269 | 0.366 | 0.97 |
| wikipron | hy | 297 | 0.070 | 0.38 |
| wikipron | ga | 134 | 0.433 | 0.96 |
| wikipron | da | 273 | 0.442 | 0.95 |
| wikipron | hi | 262 | 0.457 | 0.99 |
| mirandese | mwl-x-sendim | 11 | 0.553 | 0.82 |
| wikipron | nb | 226 | 0.513 | 0.98 |
| cmudict | en-US | 300 | 0.612 | 0.98 |
| wikipron | gd | 210 | 0.687 | 0.97 |
| wikipron | ml | 281 | 0.672 | 1.00 |
| wikipron | ta | 293 | 0.895 | 1.00 |
| wikipron | pt-BR | 125 | 0.328 | 0.99 |

Reading the table: languages whose specs carry positional grapheme
rules and stress blocks (gl, es, pt-PT, mwl) score far better than
those without: the engine consults
`positional_graphemes`/`stress` whenever a spec provides them, so the
per-language path to a better number is richer spec data, not engine
changes. The pt-BR/pt-AO/pt-TL rows lack positional vowel-reduction
blocks. The en-US row reflects English orthography itself.

Among the newer rows: rule-complete languages with positional
grapheme blocks score best (eo, fi, ro, gl, eu, ast, sq, it). The
nb/da/sv/de rows reflect irregular stress and vowel-reduction patterns
not yet encoded in those specs, and the hi/ta/ml rows expose the
Indic-script calibration gap: engine-spec gaps, not dataset problems.


## Agreement with espeak-ng

[`scripts/espeak_agreement.py`](../scripts/espeak_agreement.py) compares
this engine's output against espeak-ng on the same word lists. This is
**not an accuracy benchmark**: espeak is not a gold standard. It
answers a deployment question: a TTS model trained on espeak
phonemization maps phoneme symbols to embedding IDs, so replacing its
front-end requires symbol-level compatibility, not correctness.

Signals: **exact** (identical transcription), **exact-nostress**
(identical after stress-mark removal: espeak places stress inside the
syllable, this engine before it), **segmental** (mean character
similarity, stress-stripped), and **oov-rate**: the fraction of words
whose transcription contains a symbol espeak never emits for that
voice. Out-of-inventory symbols become unknown embedding IDs, so
oov-rate is the hard-failure signal. The offending symbols are listed
per run.

Coverage is the overlap between this repo's registered gold-dataset
languages and espeak-ng's own voice list: every language with both a
wordlist loader and an espeak-ng voice gets a row. Languages with no
espeak-ng voice (e.g. Galician, Mirandese) are skipped rather than
scored as zero.

Full committed scoreboard: [`docs/espeak_agreement.md`]
(espeak_agreement.md) (machine-readable:
[`benchmarks/espeak_agreement.json`](../benchmarks/espeak_agreement.json)).
Regenerate with:

```bash
PYTHONPATH=$PWD python scripts/espeak_agreement.py --scoreboard
```

This is a snapshot, not a CI-gated check: there is no ground truth to
regress against, so `scripts/check_benchmark_regression.py` never reads
these numbers. One language (`en-US`) needs the optional `scriptconv`
loader, and a handful of sentence-level sources (`ca` and its regional
variants) trip espeak-ng's own sentence-splitting on punctuation, which
misaligns the word-for-word comparison. Both cases are skipped with a
visible warning rather than reported as fabricated numbers: rerun with
those dependencies installed and the missing rows fill in.

Reading the table: stress-mark placement alone rules out byte-exact
replacement almost everywhere. Segmental similarity shows how close the
phone sequences are. The oov-rate column decides deployability. A
near-zero oov-rate (Spanish, French, Italian) means a symbol-mapping
shim suffices. A high one (English: espeak-ng writes the TRAP vowel as
⟨a⟩ where this engine emits ⟨æ⟩) means a per-symbol translation table
must be built and validated before any swap. A low oov-rate is a
signal of espeak-compatible **output shape**, not of linguistic
correctness: espeak-ng is an imperfect system being agreed with, not a
gold standard, so this table never substitutes for the gold-benchmark
scoreboard above.

---
[← Benchmark gold datasets](benchmark_datasets.md) · [Home](index.md) · [Arabic TTS gold set →](arabic-tts-gold.md)
