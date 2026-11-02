# Benchmarks

A benchmark number from this project is the phoneme error rate (PER) of the engine against one gold dataset for one language. This page says how far such a number can be trusted, how the harness computes it, and how to reproduce and diagnose it. A provenance tier says where a gold transcription came from. It does not say whether the transcription is right about the language, and this page is where that difference is defined.

[benchmark_datasets.md](benchmark_datasets.md) catalogues every gold dataset with its source and its caveats. It also lists the candidates this project examined and refused. The measured numbers are on the [scoreboard](scoreboard.md) and in [`benchmarks/results.json`](../benchmarks/results.json). The cross-system view is [comparison.md](comparison.md). [gold_defects.md](gold_defects.md) records individual gold rows with a measured defect. Such a row merges a contrast, marks something the language forbids, or describes the wrong variety. It can also mix transcription traditions or derive from the system it scores.

To score one row yourself, run [`scripts/benchmark.py`](../scripts/benchmark.py) from a checkout:

```bash
python scripts/benchmark.py --list
python scripts/benchmark.py --dataset wikipron --lang fi
python scripts/benchmark.py --dataset portuguese_unified --lang pt-PT
```

`--list` prints every registered dataset with the languages it covers. The other two commands download the gold file on the first run and read it from the cache after that.

## Provenance and reliability (read this before trusting any number)

Reliable gold for grapheme-to-phoneme conversion barely exists. Most languages here have no large, human-verified word list in IPA. From most to least trusted, the datasets here are curated by phoneticians, collected from native speakers, or extracted from dictionaries. Below those come Wiktionary scrapes and the output of a phonemizer reused as a reference. That is the state of the field, and it changes how every number on the [scoreboard](scoreboard.md) must be read.

The value of a gold set is its error model. A human or lexicon gold is trustworthy.

A gold made by a rule system such as espeak-ng or epitran measures agreement with a competitor. That agreement is informative, because a disagreement with a deterministic rule system can be traced to a rule and judged against a source. It can never certify this engine. A gold written by a large language model has no error model at all. It has no lexicon and no rules, so a disagreement with it cannot be attributed to anything.

A low PER against a gold that a tool generated means "agrees with that tool". It does not mean "correct". The rows of `vox_communis`, `ipa_childes`, `ipa_babylm` and `hitz_basque_ipa` all come from an automatic phonemizer. A good score there says that this engine reproduces the decisions of that tool, right or wrong.

Scoring a system against a gold that its own generator produced is close to a tautology. The gold of `hitz_basque_ipa` is the output of the ahoNT/AhoTTS phonemizer of HiTZ. A low PER for AhoTTS on that row only shows that the tool reproduces itself. Use an independent gold, such as the `wikipron` `eu` row, for a fair comparison.

The same trap makes a comparison with espeak-ng partly circular on gold of espeak lineage. `vox_communis`, `ipa_babylm` and the `ipa_childes` languages that `phonemizer` processed all come from that lineage. An espeak-against-o2i table on that gold measures how similarly two systems move away from the truth, not which one is closer to it. Epitran has the same problem. The [comparison](comparison.md) page scores this engine against epitran (`epitran_per`), and six `ipa_childes` languages are the output of epitran. If those rows counted as truth, epitran would be both rival and referee.

Read an absolute PER as a direction, not a precise measurement. The published scoreboard scores the whole gold set of every language. The `N` column is the number of gold words covered, and PER is the figure for the whole set. PER is still bound by the notation and provenance of the gold. Compare numbers as a ranking, and do not read them to three decimals.

A row with a small `N` is an anecdote. Many `clup_dialect` rows and several `ep_dialects` and `mirandese_g2p` rows score only a few words. Always read the bootstrap `95% CI` of a row on the scoreboard. A wide interval means the row is noisy. `n too small` means the row has fewer than 20 scored words, has no interval and cannot gate. In both cases the row gives a hint, never a conclusion. The scoreboard marks such a row with `†` after `N`, as described under [Confidence intervals](#confidence-intervals).

Even the `expert-human` tier is not the truth. It is bound by the transcription conventions of the team that annotated it: broad or narrow choices, stress and tie-bar notation, and the target dialect. In this repository it is also often small and not yet peer-validated outside the team. The tiers rank how the IPA was produced. They do not guarantee that it is correct.

### Reliability tiers

Each row carries one tier, shown in the `provenance` column of [`docs/scoreboard.md`](scoreboard.md) and the `provenance` field of [`benchmarks/results.json`](../benchmarks/results.json). The function `provenance_for(dataset, lang)` in `scripts/benchmark.py` resolves it. A test forces every registered dataset to carry a tier, so a dataset cannot be added without a classification.

Most datasets come from one source, so one entry in `PROVENANCE` describes the whole dataset. Some datasets are collections of files from independent sources, and one tier for the whole collection would be false. For example, ipa-dict ships a human Icelandic dictionary next to a German list built from Wiktionary. It also ships British English that espeak generated.

Such a dataset has a tier per language in `PROVENANCE_BY_LANG`, and `provenance_for` prefers it over the dataset-wide value. The row then carries the tier of the file it was scored against. The dataset-wide value is only a fallback, set to the most pessimistic tier of that dataset. An unclassified file therefore falls to "distrust it" and never inherits a tier it did not earn. A test forces every wired ipa-dict language to carry its own tier.

| Tier | Meaning | Caveat |
|---|---|---|
| `expert-human` | IPA curated by phoneticians, trained annotators or native speakers. | Bound by the notation of the team. Often small and not peer-validated here. |
| `lexicon-derived` | Human lexicographers, through the notation of a published dictionary. | Dictionary conventions are not surface phonetics. A mechanical transform, such as ARPABET to IPA, can add its own errors. |
| `crowd-scraped` | Community edits on Wiktionary, through WikiPron or Wiktextract. | Quality is uneven per language. Some entries are the output of an editor's rule or a Wiktionary module. |
| `machine-generated` | The output of a tool that this project does not compete with. | A low PER means agreement with that tool, not correctness. |
| `espeak-derived` | The output of espeak-ng, directly or through a wrapper such as `phonemizer` or G2P+. | Never gates. This project scores itself against espeak-ng, so a divergence can mean that this engine is right. |
| `epitran-derived` | The output of [epitran](https://github.com/dmort27/epitran). | Never gates, for the same reason as `espeak-derived`. Still diagnostic, because epitran is a rule system. |
| `llm-generated` | IPA written by a large language model. | Never gates. There is no error model, so the row certifies nothing and diagnoses nothing. |

The order of the tiers in `RELIABILITY_TIERS` is the order of the table. Gating is set membership, not position. `NON_QUALIFYING_TIERS` holds `espeak-derived`, `epitran-derived` and `llm-generated`, and `can_gate_promotion()` refuses those three. `machine-generated` sits below the human tiers but still gates (`GATING_CUTOFF_TIER`). A tool that this project does not compete with has an error model that a disagreement can be traced to. Judge a divergence from a competitor tier against a cited source, never against the row.

[quality_tiers.md](quality_tiers.md) says how a gating row can qualify or block a language. The tier of each dataset is in the summary table of [benchmark_datasets.md](benchmark_datasets.md#summary).

### Provenance discipline

Because reliable gold is scarce, the harness prefers human and community provenance. It admits a gold that a tool generated only explicitly, per dataset, with the reason recorded next to the registration. Each such row carries the tier that its own generator earns, so the caveat travels with every number it produces. Adding another tool-generated source needs the same explicit decision. It is never the default. A gold whose provenance cannot be established gets the most pessimistic tier its evidence permits, or it is rejected.

The two dictionaries that a language model wrote, `barranquenho_dict` and `mirandese_dict`, carry the `llm-generated` tier. The model was conditioned on published orthographic norms and descriptive research, so the IPA is not verified by a phonetician and can be wrong. No phonemizer, no part of this engine and no consumer of it produced that IPA, so scoring against it is not circular. Never use the scoreboard to move a spec toward these golds, because that would copy model output into the spec. They show disagreements to investigate against real sources.

## Corrections overlays

Some upstream gold sets carry a defect that is visible from outside and that can be repaired without a guess. An overlay ships that repair. It is a small committed file with one row per corrected gold entry. Each row records the spelling, the reading that upstream shipped and the reading that replaces it. It also records the reason and the authority for the correction. The upstream file is never edited. `scripts/build_gold_corrections.py` writes the overlays, `scripts/benchmark.py` applies them, and the overlays live in `orthography2ipa/data/gold/corrections/`.

A correction may come only from the orthography of the word or from a fetched citation. It may never come from what orthography2ipa outputs. A gold repaired with the answers of this project is circular. Its board row looks excellent and measures nothing, because the engine is scored against a copy of itself.

The derivation script names no orthography2ipa module. A test checks this by parsing the source for all four ways of naming one: `import`, `from ... import`, `sys.modules[...]`, and `importlib.import_module` or `__import__`. That test checks what the source says. It is not a sandbox. The build imports `scripts/benchmark.py` for the base gold loader, which puts the engine in `sys.modules` anyway. What keeps the derivation honest is its shape: each correction is computed from `(spelling, reading)` pairs and the spelling alone, with nothing else in scope.

An overlay is a separate dataset, never a rewrite. A corrected gold has its own registry key, such as `vox_communis_corrected` beside `vox_communis` and `ipadict_corrected` beside `ipadict`, so both rows stay on the board. The difference between the two rows is the measurement of the upstream defect, and nobody can read it if only one number is published. A correction is keyed on the spelling and the original reading together. When upstream revises a row, the correction lapses and does not overwrite a row that nobody inspected.

An overlay can never gate a promotion. A corrected gold keeps the tier of its base, because the repair of one defect leaves the untouched majority of the rows as they were. An automated process applied the repair, not a phonetician who read each row, so the row never gates, whatever its tier is. Every overlaid dataset is in `CORRECTED_DATASETS` in `scripts/benchmark.py`, and `row_gates()`, the regression gate and the promotion check all refuse a row on one of them. A test asserts this. An overlay makes a gold easier to read, not more authoritative.

Anything that the rule above cannot reach stays in the gold and is counted in the build report. That covers a spelling whose reading does not show the defect the overlay repairs, and a spelling whose correct value cannot be determined at all. A skipped row is a negative result to report, not a gap to fill with a plausible guess.

`portuguese_unified_corrected` sits beside `portuguese_unified` on the board. Its overlay, `portuguese_unified_pt.jsonl`, is keyed on the source row of the dataset: source, region, word, part of speech, field and the reading the row ships. The overlay moves or adds a primary stress mark where the spelling settles the stressed syllable. A written accent settles it, and so do the accent rules of the Acordo Ortográfico 1990. It drops rows that transcribe another headword or that end in mis-encoded text.

The corrected row scores the same sampled words as the base row, so the two numbers compare. The other two overlays are described with their datasets in [benchmark_datasets.md](benchmark_datasets.md).

## How a score is computed

PER is the character-level Levenshtein distance between the hypothesis and the reference IPA, divided by the length of the reference. A row reports the mean PER over the words it evaluates. WER is the share of words with any error.

Gold rows are grouped by word. A hypothesis is scored against every gold variant of its word, and the lowest PER counts. The harness removes whitespace before the comparison, because some gold sets separate phonemes with spaces.

By default the harness strips stress marks and narrow-transcription marks from both sides before it compares them. The narrow marks (`_NARROW_MARKS`) are the diacritics for raised, lowered, dental, apical, laminal, advanced and retracted articulation. They also include the non-syllabic mark, the syllable separators and the parentheses of optional segments. Gold sets differ in transcription depth, and the engine is not scored on notation conventions. `--keep-stress` keeps the stress marks and `--narrow` keeps the narrow marks. Tie bars are removed from both sides in every mode, because `t͡s` and `ts` are the same phoneme string.

A gold file is downloaded once and read from a cache after that, so a row is scored against the snapshot that the machine holds. Upstream corpora grow, and a stale snapshot looks exactly like a current one. The `N` column is the only visible symptom, and it is easy to read as ordinary drift. The flag `--refresh-cache` downloads every gold file the run reads and names the files that upstream changed. Scoring never refreshes the cache on its own, so a board row stays reproducible from the cache that produced it.

### Full-dataset scoreboard

The committed scoreboard ([`docs/scoreboard.md`](scoreboard.md) and `benchmarks/results.json`) scores the whole gold set of every registered dataset and language, with no cap. `python scripts/benchmark.py --scoreboard` writes both files. The `N` column is therefore the real number of covered gold words, not a sample size. A full run is slow, and `portuguese_unified` takes most of the time.

`--limit N` exists for fast ad-hoc runs. It applies the same cap to every language, never a different cap per language. One loader stays bounded in a full run: `load_hitz_basque` pages the Hugging Face rows API and stops after `_HITZ_BASQUE_MAX_PARAGRAPHS` (500) paragraphs. That is a fixed paging bound that applies to every language alike, not a sampling limit.

A full scoreboard takes long, so rows can be rescored a few at a time and merged into the committed board:

```bash
PYTHONPATH=$PWD python scripts/benchmark.py --scoreboard \
    --dataset wikipron --lang fr
```

A scoped run scores each row exactly as the full run does, and it carries the rows it did not touch through unchanged. [contributing/board.md](contributing/board.md) gives the procedure for a change that regenerates board files.

### The CI regression sample

A pull-request job cannot rerun the full scoreboard. A sampled run compared against the full baseline would compare two different slices and report false regressions. The gate therefore never mixes slices. The script `scripts/check_benchmark_regression.py` rescores every row at one uniform sample, `benchmark.CI_SAMPLE_LIMIT` (1000 rows). It compares the result with a separate baseline committed at the same cap, `benchmarks/results_ci_sample.json`, which `python scripts/benchmark.py --ci-sample` writes. Both sides are sliced the same way, so a flagged regression is a real change in PER.

A row fails the gate when its PER worsens by more than the epsilon, which defaults to 0.005. It also fails when its `stress_acc` drops by more than that epsilon. A row that cannot gate reports its worsening as `drifted`, not `regressed`, and does not block. The gate also fails closed when fewer than 20 rows score at all (`MIN_SCORED_ROWS`), so a failure to load the datasets cannot pass as green.

Refresh `results_ci_sample.json` each time the full scoreboard is regenerated. A refresh scoped with `--lang` or `--dataset` rescores only those rows and merges them into the committed sample. A fix to one language then carries no unrelated drift and downloads no other dataset.

### Stale board rows

The regression gate is one-sided and fires only when a row gets worse. A row left behind by a change to its own gold loader can therefore publish a stale number while CI stays green. The script `scripts/check_board_row_counts.py` catches that. It reloads the gold of each committed row and fails when the `n` of the row exceeds the number of pairs that the loader yields. That cannot happen in a fresh row, because scoring consumes the output of the loader.

The check is one-directional on purpose, because an `n` below the pair count is normal. A row whose loader refuses the language is reported too, which catches a row left behind by a deregistration. Run it after every board regeneration:

```bash
PYTHONPATH=$PWD python scripts/check_board_row_counts.py
```

The Japanese `ipadict` row is the usual example of an `n` below the pair count. A word written only in kanji gets no hypothesis from the kana spec and drops out. A word that contains at least one kana is scored, and most Japanese words are a kanji stem with a kana ending.

The engine then reads the ending and must still produce the reading of the whole word. Those words carry several times the error rate of the words written only in kana, and they outnumber them. The Japanese PER therefore mostly measures the missing kanji front-end. The quality of the kana-to-IPA rules shows only in the all-kana subset, and no board column reports that subset.

### Confidence intervals

Every scoreboard row carries a 95% bootstrap confidence interval on the mean PER, next to the point estimate. Read a single PER together with its uncertainty, not as an entry on a precise leaderboard.

The harness resamples the per-word PER list of a row with replacement `BOOTSTRAP_REPS` (1000) times and computes the mean of each resample. The interval is the 2.5th and 97.5th percentile of those means. Resampling uses `random.Random(BOOTSTRAP_SEED)` with a fixed seed, never the global random generator. The same PER list therefore gives the same bounds on any machine and any run, so the interval cannot itself cause false regression reports. The regression gate still compares the point estimate. The interval is a diagnostic and takes no part in the pass or fail decision.

A wide interval tells you that the PER of the row is noisy for its sample size. Grow the gold set before you trust a small PER movement on that row. A narrow interval is informative only when `N` supports it. The bootstrap draws from the row's own list, so on a few words it only reshuffles the same values. A row of one word would get a `[x, x]` interval that looks precise and means nothing.

A row with fewer than `THIN_ROW_N` (20) scored words therefore has `null` for `per_ci_low` and `per_ci_high`, and the scoreboard shows `n too small` in its `95% CI` cell. The floor comes from a simulation of the percentile interval on per-word PERs with many zeros. Against a nominal 0.95, the interval covered the true mean in 0.48 of trials at n=2 and 0.79 at n=5. Coverage was 0.88 at n=10, and 0.90 to 0.92 from n=15 up.

The same floor decides whether a row gates. A row under `THIN_ROW_N` words has `gating: false` in `results.json`, so it can neither qualify a language nor block one. The function `row_gates()` also sets `gating: false` for a tier that cannot gate and for a corrections overlay. The scoreboard writes `†` after the `N` of a thin row and `‡` after the `PER` of every row that does not gate.

Read the PER of a thin row as one anecdote. Never rank it against, or average it with, a row scored on thousands of words. The weight of a row is its `N`, not its position in a PER sort.

### Stress accuracy

PER strips stress marks from both sides. A transcription with every segment right and the stress on the wrong syllable therefore scores a perfect PER. The `Stress` column of the [scoreboard](scoreboard.md) measures that one thing. The field `stress_acc` is the share of eligible gold words whose primary stress the engine puts on the syllable of the gold. The field `n_stress` is the number of eligible words. Both come from the same 1-best transcriptions as PER, and PER does not change.

A gold entry is eligible when its spelling is one word with no space and it carries exactly one primary mark `ˈ`. It must also have at least two syllables. The harness reads an ASCII apostrophe as `ˈ`. A word with several golds counts once, and it is a hit when the hypothesis matches the stress of any eligible gold. That is the rule PER uses, which scores a word against its best gold.

A multi-word entry is never eligible, even when its gold has no space. A hyphenated compound is one word. Its gold has one primary mark, so a hypothesis with a primary mark on every element is a miss. A row with fewer than 20 eligible words reports `stress_acc` as null, which is the floor for thin rows. A gold with no stress marks reports null and `n_stress` 0. That is not a score of zero.

The hypothesis misses when it has no primary mark, more than one, or a mark on another syllable. To find the syllable, the harness splits both transcriptions into segments and removes the stress marks and syllable boundaries. A segment is a character with its diacritics, and a tie bar (U+0361, U+035C) joins the two characters it links into one segment. Each segment gets the folds that PER applies.

The harness then aligns the two segment strings by unit-cost edit distance. It asks whether the stressed nucleus of the gold aligns with the stressed nucleus of the hypothesis. When two alignments have the same cost, it takes the one that pairs vowels with vowels. A nucleus is an IPA vowel letter with its diacritics that is not marked non-syllabic (U+032F), or any letter marked syllabic (U+0329). The glides `j w ɥ ɰ` are never a nucleus. The stressed nucleus is the first nucleus after the mark, and where a transcription writes syllable boundaries (`.`), they bound the syllables too.

The first two cases below show why the harness aligns instead of counting nuclei from the end of the word. The last two fix the details of the alignment.

| Word | Gold | Hypothesis | Result |
|---|---|---|---|
| `saída` | `sɐˈidɐ` | `ˈsajdɐ` | Miss. The hypothesis reads the hiatus as a diphthong. The stressed `i` of the gold aligns with `j`. |
| `texto` | `ˈtɐjʃtu` | `ˈtɐʃtu` | Hit. The lost glide is a segment error. The stressed `ɐ` aligns with the stressed `ɐ`. |
| `melhor` | `meˈʎɒɹ` | `meˈʎɔ` | Hit. Deleting `ɹ` and deleting `ɒ` cost the same. Only the first pairs `ɒ` with the vowel `ɔ`. |
| `exigência` | `ˌeziʒˈe͡ɪŋsjæ` | `eziˈʒẽsjɐ` | Hit. The tied `e͡ɪ` is one segment, so it pairs with `ẽ`. |

## Top-k oracle PER (lattice quality vs ranking error)

A single PER says whether the first guess was right. It cannot say why a wrong guess was wrong, and two different failures hide behind one score. A ranking error means that a better reading than the one ranked first is in the top k. Nothing is missing from the language data. The weights ordered the beam badly, and a consumer that rescores the lattice can recover the reading.

A model error means that no better reading exists in the lattice at any depth. No reranking can find one, and only new rules or new data fix it.

Oracle PER@k separates the two. It is the per-word minimum PER over the top k readings of the engine. It is averaged exactly like the 1-best PER, with the same normalization, edit distance and multi-gold rule. So:

```text
PER − Oracle@k   = ranking error  (the rescoring headroom)
Oracle@k         = model error    (what rules or data must fix)
```

The scoreboard has the columns `Oracle@3` and `Oracle@5`, and `results.json` has the fields `oracle_per_top3` and `oracle_per_top5`.

The headroom is an upper bound, not a forecast. An oracle picks the best candidate per word after it sees the gold. No real rescorer has that information, so `PER − Oracle@k` is the most that any reranking could gain. Quote it as a ceiling.

A lower `Oracle@k` means that a closer candidate is in the beam, closer in edit distance and usually still wrong. The strict version is the `OracleX@k` columns (`oracle_exact_top3`, `oracle_exact_top5`). Each is the share of words where some top-k candidate equals a gold exactly, which is the `Exact match` column taken from k=1 to k. On the French and German rows, exact hits are a minority of the PER-oracle gain. The PER oracle therefore overstates how often the engine already knows the answer.

Use `OracleX@k` for any claim of that kind. Take the ratio from the committed row's `PER` to `Oracle@5` and `Exact match` to `OracleX@5`, never from figures measured with injected alternatives, which would inflate it.

### Finding where the beam ranks a better reading wrong

[`scripts/rank_diag.py`](../scripts/rank_diag.py) shows which decision went wrong when the beam holds a better reading than the 1-best. It reads the `wikipron` gold of one language and takes a random sample with a fixed seed. It keeps every word where some top-5 reading beats the 1-best, and it aligns the two beam paths of that word slot by slot. Each disagreement goes into a bucket keyed by the grapheme, the chosen IPA and the better IPA. The key also says whether the choice came from the flat grapheme table or from a positional override. A bucket names the one decision that went wrong, not the whole word.

The sample is random over the whole corpus on purpose. The corpora are in alphabetical order, so a `--limit` prefix samples the letter A, not the language. The bucket `<unaligned>` counts words where the two paths have different numbers of segments, for example after a grammatical-ending rewrite or an allophone expansion. No per-slot blame is possible for those words.

[`scripts/rank_sweep.py`](../scripts/rank_sweep.py) writes the per-word PER of one engine state as `word`, `per`, `hyp` and `gold` columns. Run it before and after a spec change and diff the two files word by word and bucket by bucket. A candidate fix is accepted or rejected on such a sweep, never on an opinion. The script [`scripts/rank_eval.py`](../scripts/rank_eval.py) prints the top-1 PER, WER and oracle figures for a random sample of a row. All three scripts read their arguments by position and read gold from the cache:

```bash
PYTHONPATH=. python scripts/rank_diag.py fr 2000              # bucket table, as JSON
PYTHONPATH=. python scripts/rank_eval.py fr 5000 wikipron     # PER and oracle on a sample
PYTHONPATH=. python scripts/rank_sweep.py fr a.tsv wikipron   # per-word dump, for diffs
python scripts/benchmark.py --dataset wikipron --lang fr      # the full row
```

[known_limitations.md](known_limitations.md) records the rewrites that such sweeps rejected and the gaps they left open.

### Injected alternatives do not count as ranking error

Some oracle movement is not a discovery about the engine. It is a reading that the data deliberately puts into the beam. A list-valued `grammatical_endings` entry adds a licit reading that the spec cannot choose between. A downstream rescorer can then choose (see [SCHEMA.md](../orthography2ipa/data/SCHEMA.md#ambiguous-endings)). French ⟨-ent⟩ is an example.

Hard rule: report oracle@k movement caused by an injected alternative separately, under its own heading. It never counts toward ranking-error analysis or any claim to beat espeak.

The code enforces the rule. The scoreboard run builds its engine with `G2P(lang, expose_ambiguous_endings=False)`, so a list-valued ending adds nothing to the beam it scores. Every oracle cell on the scoreboard and in `results.json`, for every language and dataset, is measured on the beam that the engine ranks. A row whose language declares injected alternatives records the excluded ones in `oracle_injected_alternatives` (`["fr-FR ent"]` on the `fr` `wikipron` row), so the exclusion travels with the numbers. That field comes from the flag the row was scored with, not from the spec. A row measured with exposure on claims no exclusion and leaves the field out, because a false exclusion is worse than no field.

An injected alternative can never reach rank 1, so the `PER` and `Exact match` columns are the same in both modes. To see the injected movement, pass the flag explicitly. Run this from the root of a checkout:

```python
import sys
sys.path.insert(0, "scripts")
from benchmark import evaluate_words_oracle

pairs = [("parlent", "paʁl"), ("vent", "vɑ̃"), ("chantent", "ʃɑ̃t")]
for expose in (False, True):
    n, covered, pers, per, wer, oracle = evaluate_words_oracle(
        pairs, "fr", strip_stress=True, broad=True,
        expose_ambiguous_endings=expose)
    print(expose, f"PER={per:.4f}", f"oracle@5={oracle.oracle_per[5]:.4f}")
```

```text
False PER=0.3333 oracle@5=0.1667
True PER=0.3333 oracle@5=0.0000
```

PER does not move, and the oracle drops only because the mute reading of ⟨-ent⟩ joined the beam. The full French `wikipron` row behaves the same way. `PER` and `Exact match` are identical in both modes, and `Oracle@5` and `OracleX@5` improve with exposure. `Oracle@3` does not move, because the mute reading lands at rank 4 or 5. The first pair is the accuracy claim, and its invariance proves that an injected reading never reaches rank 1. The second pair is reachability and belongs only under this heading.

Without the rule, both quantities would be one number measured two ways. The headroom `PER − Oracle@k` says that the engine already produced a better answer and ranked it wrong. That is a property of the weights that a rescorer could use.

An injected alternative moves that gap by construction. Adding candidates to the beam can only lower an oracle, so a spec could lower its own oracle without limit by declaring more alternatives. The 1-best would not move, and the ranking would not improve. Folding that into the headroom would grade our own diagnostic with our own edit.

When you report such a change:

1. Give the 1-best columns first, and say that they did not change. That is the only accuracy claim an injected alternative may make.

2. Give the oracle delta under an explicit heading for injected-alternative oracle movement. Name the ending and the spec that declares it.
3. Do not add the delta to a `PER − Oracle@k` headroom figure, a ranking-error budget or a count of ranking failures per phenomenon.
4. Never carry it into [comparison.md](comparison.md) or into a sentence that says this engine beats espeak, epitran or another system. Those compare one pronunciation with one pronunciation.

The value of an injected alternative is reachability: the reading exists for a rescorer that knows a fact this engine does not. Report it as reachability, for example "gold in the top 10 for N of M gold-mute types", not as accuracy.

### The Oracle@1 self-check

The readings come from `G2P.word_candidates`, which runs every beam path through the same word-final pipeline as `transcribe_word`: geminate collapse, grammatical-ending rewrite, stress marking and lexicon override. Element 0 is therefore normally the answer of `transcribe_word`, and that is why Oracle@1 equals the PER column.

Nothing guarantees that identity by construction. The method `transcribe_word` defaults to greedy search with width 1. The method `word_candidates` runs a beam of width `max(k, 8)`, which can reach a cheaper path that greedy pruning discarded.

The two agree on every gold set measured, but the harness verifies the identity on every run. Oracle@1 can differ from PER, or the candidate 0 of a word can differ from its 1-best. In either case the run prints `ENGINE BUG` and exits non-zero without writing the scoreboard. A corrupt artifact reported as a success is worse than a failed run.

### Limits of the oracle

Oracle@k is a diagnostic for this engine only. It must never appear in a cross-system comparison or in a claim to beat another system. Every system in [comparison.md](comparison.md), espeak-ng and epitran included, gives one pronunciation. Setting their one answer against the best of k of ours compares k guesses with one. Any conclusion from that is an artifact of k. The script `scripts/compare_systems.py` does not read the oracle fields, and the CI regression sample stays 1-best.

The oracle is word-level only, because the beam is per word. Sentence-level gold sets, such as `4catac` and the TTS gold sets, get no oracle. Their columns read `-` and their `oracle_scored_words` is 0. The `vox_communis` gold is word-level and does get an oracle. Building a sentence-level beam out of word beams would invent a ranking that the engine never produces, so the harness does not do it.

A cell reads `·` when the row was not rescored with the oracle columns, and `-` when the row is sentence-level and can never have them. The two states are never merged into one blank, because an unrescored row must not read as "no ranking error".

The gap does not name a phonological phenomenon. It says that a better reading was ranked wrong, not which phenomenon is involved. Use [`error_analysis.py`](../scripts/error_analysis.py) for that, as described under [Diagnosing a language](#diagnosing-a-language).

The oracle costs about 1.6 times the 1-best run, measured on French `wikipron` with beam width 8. The flag `--scoreboard` turns it on, and `--no-topk` turns it off for a fast ad-hoc rerun. The function `build_scoreboard(..., oracle=...)` defaults to off, and each caller turns it on explicitly. The regression gate and the `--ci-sample` baseline compare 1-best PER only, and they would otherwise pay that cost on every row for columns they never read.

## Rules-only vs with-lexicon PER (lexicon overlay)

A language with a registered lexicon overlay is scored twice on the same gold. The overlay is a TSV that the caller registers and that the library never bundles (see [lexicon.md](lexicon.md)). The first score is the rules-only PER, with `get_lexicon` replaced by a stub that returns `{}`. The second is the with-lexicon PER, with the overlay active. Inline `word_exceptions` stay active in both runs.

The comparison keeps rule quality honest: the overlay must improve PER, and the grapheme rules must not decay behind lexicon coverage. The results go to a separate report and leave the main scoreboard unchanged.

```bash
python scripts/benchmark.py --lexicon-report
```

This writes [`lexicon_scoreboard.md`](lexicon_scoreboard.md) and `benchmarks/lexicon_results.json`. Each row reports the delta on the full slice and on the covered subset, which is the gold words that the lexicon contains. The covered-subset delta is the honest measure of the lexicon's own accuracy against the rules on the same words. The full-slice delta is diluted by every gold word outside the lexicon. The `en-GB` pilot lexicon, built from CMUdict by `scripts/build_en_lexicon.py`, holds a capped set of the most frequent words. It proves the mechanism, and a full production lexicon belongs downstream.

## Board environment

A whole-board `--scoreboard` run writes `benchmarks/results_environment.json`. It lists the resolved version of every registered plugin entry point and of every optional scorer package, or `null` for one that is not installed. When a row moves with no spec change, diff this file first. A package with a floor pin, such as `silabificador`, resolves to the newest release on each machine.

A whole-board run exits non-zero and writes nothing when it cannot score a row that the committed board carries. The message names each row as `dataset/lang`. A run scoped with `--lang` or `--dataset` prints the same names as a warning and keeps the committed values. A row whose scorer package no CI job installs carries `"ci_reproducible": false`, and the scoreboard shows `(not CI-reproducible)` in its `Provenance` cell.

## Diagnosing a language

The scoreboard says that a language scores badly. It does not say why. The script [`scripts/error_analysis.py`](../scripts/error_analysis.py) runs a gold dataset through the engine and reports where the errors concentrate. Spec work can then start from evidence. It only reads. It never writes to a spec or any other file.

```bash
PYTHONPATH=$PWD python scripts/error_analysis.py pt-PT --dataset portuguese_unified --limit 300
```

The language is required. `--dataset` is optional, and without it the script uses the first registered dataset that covers the language. `--limit` caps the gold slice and defaults to 300. `--json` writes all three sections as one JSON object instead of the text report. The script aligns with the same routine as the scoreboard (`scripts.benchmark.align`) and the same default normalization, so what it shows matches how PER is scored.

Read the three sections of the report in this order:

1. The top 20 phoneme confusion pairs (`gold -> hyp`). Each row is an aligned mismatch, ranked by frequency. An empty gold side (`∅`) is an insertion, a phoneme that the gold does not have. An empty hypothesis side is a deletion, a gold phoneme that the engine dropped. One pair with a high count, such as `'r' -> 'ɾ'`, usually points at one wrong or missing rule. It is the fastest fix.

2. The top 20 worst words, with the highest per-word PER, gold and hypothesis side by side. Use them to see the confusion pairs in context. They show whether a substitution happens in every word or only in one context, such as at the end of a word. That tells you whether the fix is a flat grapheme change or a positional rule.

3. The blame per grapheme. The report takes each orthographic character or digraph in the grapheme map of the spec. It gives the mean PER of the gold words that contain it, worst first, with at least 3 occurrences. It uses substring containment, not tokenization. Treat a grapheme with high blame as the place to look first, and confirm it against the confusion pairs and the worst words.

Then classify each systematic error: a missing or wrong grapheme mapping, a missing positional rule, missing sandhi, wrong stress placement, or a lexical fact. Cite a published source for every spec change, and run the tool again to confirm that the count of the pair dropped.

## Agreement with espeak-ng

[`scripts/espeak_agreement.py`](../scripts/espeak_agreement.py) compares the output of this engine with espeak-ng on the same word lists. It is not an accuracy benchmark, because espeak-ng is not a gold standard. It answers a deployment question. A TTS model trained on espeak phonemization maps phoneme symbols to embedding IDs, so a replacement front-end needs symbol-level compatibility, not correctness.

The script reports four signals:

| Signal | Meaning |
|---|---|
| exact | The two transcriptions are identical. |
| exact-nostress | The two are identical after stress marks are removed. espeak-ng puts stress inside the syllable, and this engine puts it before. |
| segmental | Mean character similarity with stress stripped. |
| oov-rate | The share of words whose transcription contains a symbol that espeak-ng never writes for that voice. |

A symbol outside the espeak inventory becomes an unknown embedding ID, so oov-rate is the signal for a hard failure. Each run lists the symbols that cause it.

Coverage is the overlap between the languages that have a gold loader here and the voice list of espeak-ng. A language with a loader and no espeak-ng voice, such as Galician or Mirandese, is skipped, not scored as zero. The committed results are in [`docs/espeak_agreement.md`](espeak_agreement.md) and [`benchmarks/espeak_agreement.json`](../benchmarks/espeak_agreement.json). Regenerate them with:

```bash
PYTHONPATH=$PWD python scripts/espeak_agreement.py --scoreboard
```

The table is a snapshot, not a CI-gated check. It has no ground truth to regress against, so `check_benchmark_regression.py` never reads it. `en-US` needs the optional `scriptconv` package for its CMUdict loader. A few sentence-level sources (`ca` and its regional variants) trip the sentence splitting of espeak-ng on punctuation, which misaligns the word-for-word comparison. Both cases are skipped with a visible warning. Install the missing dependency and run again to fill the rows.

Stress placement alone rules out a byte-exact replacement almost everywhere. Segmental similarity shows how close the phone sequences are, and the oov-rate decides whether a swap can work. A near-zero oov-rate means that a symbol-mapping shim is enough. A high one means that a per-symbol translation table must be built and validated before a swap. English is the clear case: espeak-ng writes the TRAP vowel as ⟨a⟩ where this engine writes ⟨æ⟩. A low oov-rate shows output of a shape compatible with espeak, not linguistic correctness, so this table never replaces the gold scoreboard.

---
[← Engine changes](contributing/engine.md) · [Home](index.md) · [Benchmark gold datasets →](benchmark_datasets.md)
