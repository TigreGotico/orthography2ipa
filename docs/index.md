# orthography2ipa

`orthography2ipa` converts the spelling of a language into IPA, and it
measures how languages relate to each other. Each language is a cited JSON
spec. A shared engine with no language-specific code turns the specs into
transcriptions, ranked pronunciation lattices and distances. The package
ships no trained weights and no word lists.

```python
>>> import orthography2ipa
>>> orthography2ipa.transcribe("olá mundo", "pt")
'oˈla ˈmũdu'
>>> orthography2ipa.transcribe("hello world", "en")
'ˈhɛləʊ ˈwɔːld'
```

`available_codes()` returns the registered languages, and
`available_codes(include_clades=True)` adds the classification-only clade
nodes. Run them for the live counts, or run `orthography2ipa list`.

## Pick a starting page

| You want to | Start with | Then read |
| :--- | :--- | :--- |
| Turn text into IPA in a TTS or ASR pipeline | [guide/getting_started.md](guide/getting_started.md) | `engine/tokenizer.md`, `engine/lattice.md`, `specs/quality_tiers.md` |
| Add or correct a language | [contributing/spec_authoring.md](contributing/spec_authoring.md) | `contributing/citations.md`, `specs/data_model.md`, `SCHEMA.md` |
| Build a phonemizer on the engine | [engine/lattice.md](engine/lattice.md) | `engine/architecture.md`, `reference/api.md` |
| Compare two languages | [guide/distance.md](guide/distance.md) | `specs/ancestry.md` |
| Know how far a score can be trusted | [evaluation/benchmarks.md](evaluation/benchmarks.md) | `evaluation/datasets.md`, `evaluation/generated/scoreboard.md`, `evaluation/gold_defects.md` |
| Check production readiness | [reference/api_stability.md](reference/api_stability.md) | `specs/quality_tiers.md`, `evaluation/generated/scoreboard.md` |
| Change the repository | [`AGENTS.md`](../AGENTS.md) | the pages under `contributing/` |

[arbtok](https://github.com/TigreGotico/arbtok) and
[tugaphone](https://github.com/TigreGotico/tugaphone) are downstream engines.
They refine the shared lattice with a `LatticeRescorer` or replace one
pipeline step with a plugin, and keep no tokenizer of their own.

## Honest limitations (read this before you trust a tier)

The engine ranks the readings of an ambiguous spelling by how common each
reading is in the language. It does not look at the neighbouring words or the
meaning. The beam shows the alternatives, but it does not choose between them
for you. A downstream engine adds that context through a rescorer.

Some specs read an input that is not plain native text. `zh` reads Pinyin,
and its `orthography_kind` is `ROMANIZATION`. The native `zh-Hani` spec has no
grapheme map, because a Han character encodes no sound: its reading is a
dictionary lookup, which this library does not do. `ko` reads decomposed jamo
(ㄱ, ㅏ, ㄴ), so a Hangul decomposition step must come first. Read
`orthography2ipa.get(code).notes` before you send raw native script to a spec.

Most specs are `stub` or `skeleton`, and few are `production`. A `production`
spec passed the volume and accuracy bar of [quality_tiers.md](specs/quality_tiers.md),
and a test checks that bar against the board. Check
`orthography2ipa.get(code).quality` before you depend on a language. This
expression lists the `production` specs:

```python
import orthography2ipa as o2i
from orthography2ipa import QualityTier

[c for c in o2i.available_codes() if o2i.get(c).quality is QualityTier.PRODUCTION]
```

PER is poor for several major languages, English among them. The
[scoreboard](evaluation/generated/scoreboard.md) shows every row without a filter, and
`scripts/benchmark.py --scoreboard` reproduces it on the full gold set of each
dataset. A row's `N` is the number of gold words it scored, not a sample size.

Reliable G2P gold is rare. Most gold sets are extracted from dictionaries,
scraped from a wiki, or produced by another phonemizer, so read a PER as a
direction and check its bootstrap confidence interval. A row whose gold is
espeak-ng or epitran output measures agreement with that tool, and a
divergence can mean that the spec is right. A row whose gold a language model
wrote has no error model, so it certifies nothing. Each row in
[`benchmarks/results.json`](../benchmarks/results.json) carries a `gating`
flag: a row gates a quality decision only when its provenance tier can gate,
it scored at least 20 words, and it is not a corrections overlay. The
scoreboard marks a non-gating PER with `‡`.
[benchmarks.md](evaluation/benchmarks.md#provenance-and-reliability-read-this-before-trusting-any-number)
defines the tiers.

## Reading order

The tables below set the order of the documentation. Each page ends with a
footer that links its neighbours in this order. The folders group the pages
by reader: `guide/` for users of the library, `reference/` for exact names,
`engine/` for how the engine works, `specs/` for what a spec holds,
`contributing/` for the rules of change, and `evaluation/` for the scores.
The pages under `evaluation/generated/` are written by scripts.

### Guide

| Page | Covers |
| :--- | :--- |
| [getting_started.md](guide/getting_started.md) | The first transcription, the two maps, language lookup, plugins and the explorer |
| [lexicon.md](guide/lexicon.md) | Lexicon sidecars and caller overrides for words the rules cannot predict |
| [distance.md](guide/distance.md) | Every relational axis between languages and its API |
| [known_limitations.md](guide/known_limitations.md) | What the specs and the ranker do not do, classified |

### Reference

| Page | Covers |
| :--- | :--- |
| [api.md](reference/api.md) | Every name `orthography2ipa` exports, with its docstring summary (generated) |
| [cli.md](reference/cli.md) | The `--help` output of every `orthography2ipa` subcommand (generated) |
| [registry.md](reference/registry.md) | Code resolution, the alias table and plugin discovery |
| [api_stability.md](reference/api_stability.md) | The public, version-guarded surface |

### Engine

| Page | Covers |
| :--- | :--- |
| [architecture.md](engine/architecture.md) | Module layout, the pipeline stages and the design decisions |
| [tokenizer.md](engine/tokenizer.md) | `PhonetokTokenizer`, maximal-munch tokenization and beam search |
| [lattice.md](engine/lattice.md) | Candidate costs, the lattice, rescorers, per-word confidence, the sentence seam and feature export |
| [lattice_per.md](engine/lattice_per.md) | Phone error rate for ASR against every reading the lattice admits |
| [allophony.md](engine/allophony.md) | Post-lexical `allophone_rules` |
| [positional_graphemes.md](engine/positional_graphemes.md) | Context-sensitive grapheme overrides |

### Specs

| Page | Covers |
| :--- | :--- |
| [data_model.md](specs/data_model.md) | `LanguageSpec` and its accessors, the types and the kinds of orthography |
| [quality_tiers.md](specs/quality_tiers.md) | What `stub`, `skeleton`, `research` and `production` require |
| [ancestry.md](specs/ancestry.md) | Ancestor roles, clade nodes, ancestry distance and the Glottolog alignment |
| [ipa_reference.md](specs/ipa_reference.md) | IPA symbols, code points and common errors |
| [bibliography.md](specs/bibliography.md) | Reference works by family, and `LinguisticSource` |

### Contributing

| Page | Covers |
| :--- | :--- |
| [spec_authoring.md](contributing/spec_authoring.md) | The steps to add a spec or a dialect, and the rules a spec keeps |
| [citations.md](contributing/citations.md) | Where to find a source, how to quote it, and which gold sets are silver |
| [board.md](contributing/board.md) | How to regenerate the benchmark board, and the guards that check it |
| [engine.md](contributing/engine.md) | How to add an engine capability, and the review gate for engine code |
| [silver_correction.md](contributing/silver_correction.md) | How to correct the IPA of the silver sentence sets with Claude |

### Evaluation

| Page | Covers |
| :--- | :--- |
| [benchmarks.md](evaluation/benchmarks.md) | What a score means, how it is computed and reproduced, and how to diagnose one |
| [datasets.md](evaluation/datasets.md) | Every gold dataset, where it comes from, and the caveats on its rows |
| [wikipron_mirror.md](evaluation/wikipron_mirror.md) | The pinned WikiPron snapshot and how to refresh it |
| [silver_sets.md](evaluation/silver_sets.md) | The sentence sets for TTS voices, which a language model wrote |
| [gold_defects.md](evaluation/gold_defects.md) | Defects in gold rows, and how much of a row is alphabet-chart entries |
| [scoreboard.md](evaluation/generated/scoreboard.md) | Every measured PER and exact-match result (generated) |
| [comparison.md](evaluation/generated/comparison.md) | PER against espeak-ng, epitran, gruut and other systems (generated) |
| [espeak_agreement.md](evaluation/generated/espeak_agreement.md) | Symbol-level agreement with espeak-ng (generated) |
| [lexicon_scoreboard.md](evaluation/generated/lexicon_scoreboard.md) | Rules-only against with-lexicon PER (generated) |
| [spec_diagnostics.md](evaluation/generated/spec_diagnostics.md) | A mechanical hunt for specs that are wrong rather than imprecise (generated) |

### Per language

| Page | Covers |
| :--- | :--- |
| [languages/index.md](languages/index.md) | The per-language pages, by family |
