# Quality tiers

`orthography2ipa.types.QualityTier` classifies how mature the data of a spec is. Every spec JSON states its tier in the `quality` field, and [`tests/test_data_quality.py`](../tests/test_data_quality.py) fails a spec that leaves it out. This page defines what a spec must meet for each tier, so that a reader can check a tier claim against the repository.

| Tier | What it means | What a test enforces |
|---|---|---|
| `stub` | A placeholder with metadata and no phonology of its own | No own letter table, except a delta over an inherited base |
| `skeleton` | A grapheme and allophone inventory | Content after inheritance, and at least one real source |
| `research` | A cited description, with stress and a measured gold | The `skeleton` checks |
| `production` | Measured on a trusted gold of 500 words or more | The `skeleton` checks and the benchmark bar |

## `stub`

A stub holds `code`, `name`, `script` and a `parent`, so that the clade chain resolves and `family` derives from it. A grouping that is not a clade states `family` instead. Its `graphemes` and `allophones` may be empty, and it needs no gold. The tier is for a language that the library does not encode yet. It is also for an extinct language with a metadata-only entry.

A stub carries no letter table of its own. A stub dialect may still state a small delta over a base that it inherits a table from (`graphemes_base` or `positional_graphemes_base`). `test_stub_carries_no_table_of_its_own` enforces this. A table on a stub hides the `StubSpecWarning` and makes the engine print IPA that no source supports. A spec whose table a listed source supports is a candidate for promotion, not a stub.

## `skeleton`

A skeleton spec resolves, after inheritance, to a grapheme table and an allophone map that are not empty. `test_non_stub_resolves_to_content` enforces this. When a spec states graphemes and no allophones, `LanguageSpec.__post_init__` derives an identity allophone map from the grapheme values. An extinct language with no graphemes and no allophones fails the test, because such a spec must be a stub.

Every spec above `stub` names at least one real work in `sources`, and `tests/test_sources.py` enforces this. A skeleton spec needs no positional rules, no stress rules and no gold.

## `research`

A research spec meets every `skeleton` criterion. It also has these:

- A `stress` block, when the language has lexical or predictable word stress. A language without lexical stress is exempt. So is a language whose stress the orthography does not predict. State the exemption in the spec's `notes`.

- A gold set in the `DATASETS` registry of `scripts/benchmark.py` for at least one of the spec's language tags. The set has a PER in [`benchmarks/results.json`](../benchmarks/results.json).

Reviewers check these two criteria. No test checks them for every spec.

## `production`

A production spec meets every `research` criterion. It also has a row in `benchmarks/results.json` that passes all of these checks:

| Check | The rule | Where the code holds it |
|---|---|---|
| Size | At least 500 evaluated words (`n`) | `_PRODUCTION_MIN_N` in `tests/test_data_quality.py` |
| Provenance | The tier of the gold can gate a promotion | `can_gate_promotion()` in `scripts/benchmark.py` |
| Overlay | The dataset is not a corrections overlay | `CORRECTED_DATASETS` in `scripts/benchmark.py` |
| PER | At or below 0.25 | `_PRODUCTION_DEEP_PER_CEILING` in `tests/test_data_quality.py` |
| Language | The row's language tag resolves to this spec | `test_production_tier_has_qualifying_benchmark` |

The language check resolves a row tag the way the engine does. A wikipron row registered as `es` counts for `es-ES`, because the registry resolves `es` to that spec. A row with no `provenance` field cannot qualify a spec.

### Which gold can gate

Three provenance tiers can never gate a promotion: `espeak-derived`, `epitran-derived` and `llm-generated`. `can_gate_promotion()` is the single source of truth for this rule, and `tests/test_competitor_derived_gold.py` tests it. The reasons differ by tier:

- A gold that a competing G2P system generated (`espeak-derived`, `epitran-derived`) measures agreement with that competitor, not correctness. This project benchmarks itself against both systems ([comparison](comparison.md)), so their output cannot also be the truth.

- A gold that a large language model generated (`llm-generated`) has no lexicon and no rules, so it has no error model. A disagreement with it says nothing about the spec, so it can certify nothing.

A language whose only gold of 500 words or more sits in one of these tiers has no usable gold, and it stays at `research`. A poor score on one of these tiers never disqualifies a language that clears the bar on a trusted gold. A cited source can require exactly the divergence from espeak, epitran or a model output that such a row counts as error. The tiers of every dataset are in [benchmarks](benchmarks.md#reliability-tiers).

A row on a corrections overlay never gates either, whatever its tier. An automated process applied the corrections, so the row can diagnose and never certify.

`row_gates()` in `scripts/benchmark.py` applies the same rules when it decides whether a row may qualify a language, block one, or fail the regression gate. It adds one more floor: a row with fewer than `THIN_ROW_N` (20) scored words never gates.

### The PER threshold

The threshold depends on how regular the orthography is:

| Orthography | PER at most | Examples | Why |
|---|---|---|---|
| Shallow (phonemic) | 0.15 | Spanish, Finnish, Esperanto | The spelling-to-sound relation is mostly regular, so a rule-driven engine reaches near-perfect accuracy. A higher PER means a gap in the spec |
| Deep | 0.25 | English, French, Portuguese, Danish | The spelling has historical, morphophonemic or dialectal irregularity. Even curated gold sets disagree on regional and optional variants at this rate |

The spec's page under [`docs/languages/`](languages/) states the threshold and the classification of the language. A page that says nothing gets the deep threshold.

`LanguageSpec` has no field for orthographic depth. So `test_production_tier_has_qualifying_benchmark` cannot look up a threshold for each language, and it applies the 0.25 ceiling to every spec. The 0.15 target for a shallow orthography is a reviewer check. A reviewer compares a promotion of such a language with the 0.15 target before the merge, because the test alone does not prove it.

### The language page

A production spec has a page under [`docs/languages/`](languages/). The page covers the phonology, the sources and the known limitations of the spec. It lists the cases that the engine cannot resolve, so that these cases do not silently change what the measured PER means.

## Promotion is a test-gated act

A change of tier to `production` is a claim that a test checks. The benchmark row must exist and pass the checks above, and `test_production_tier_has_qualifying_benchmark` fails every spec that claims `production` without one. For a shallow orthography, a reviewer also confirms the 0.15 target before the tier claim stands.

---
[← Positional Graphemes](positional_graphemes.md) · [Home](index.md) · [IPA Reference →](ipa_reference.md)
