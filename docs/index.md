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
| Turn text into IPA in a TTS or ASR pipeline | [getting_started.md](getting_started.md) | `tokenizer.md`, `lattice.md`, `quality_tiers.md` |
| Add or correct a language | [adding_a_language.md](adding_a_language.md) | `contributing/spec_authoring.md`, `contributing/citations.md`, `SCHEMA.md` |
| Build a phonemizer on the engine | [lattice.md](lattice.md) | `sentence_context.md`, `features.md`, `reference/api.md` |
| Compare two languages | [distance.md](distance.md) | `ancestry.md` |
| Know how far a score can be trusted | [benchmarks.md](benchmarks.md) | `benchmark_datasets.md`, `scoreboard.md`, `gold_defects.md` |
| Check production readiness | [api_stability.md](api_stability.md) | `quality_tiers.md`, `scoreboard.md` |
| Change the repository | [`AGENTS.md`](../AGENTS.md) | the four pages under `contributing/` |

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
spec passed the volume and accuracy bar of [quality_tiers.md](quality_tiers.md),
and a test checks that bar against the board. Check
`orthography2ipa.get(code).quality` before you depend on a language. This
expression lists the `production` specs:

```python
import orthography2ipa as o2i
from orthography2ipa import QualityTier

[c for c in o2i.available_codes() if o2i.get(c).quality is QualityTier.PRODUCTION]
```

PER is poor for several major languages, English among them. The
[scoreboard](scoreboard.md) shows every row without a filter, and
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
[benchmarks.md](benchmarks.md#provenance-and-reliability-read-this-before-trusting-any-number)
defines the tiers.

## Reading order

The tables below set the order of the documentation. Each page ends with a
footer that links its neighbours in this order.

### Using the library

| Page | Covers |
| :--- | :--- |
| [getting_started.md](getting_started.md) | Install, the first transcription, the two maps, the explorer |
| [architecture.md](architecture.md) | Module layout, the pipeline stages and the design decisions |
| [data_model.md](data_model.md) | `LanguageSpec`, every field it carries, and the kinds of orthography |
| [registry.md](registry.md) | Code resolution, aliases and plugin discovery |
| [lexicon.md](lexicon.md) | Lexicon sidecars and caller overrides for words the rules cannot predict |
| [api_stability.md](api_stability.md) | The public, version-guarded surface |

### Reference

| Page | Covers |
| :--- | :--- |
| [reference/api.md](reference/api.md) | Every name `orthography2ipa` exports, with its docstring summary (generated) |
| [reference/cli.md](reference/cli.md) | The `--help` output of every `orthography2ipa` subcommand (generated) |

### The engine

| Page | Covers |
| :--- | :--- |
| [tokenizer.md](tokenizer.md) | `PhonetokTokenizer`, maximal-munch tokenization and beam search |
| [candidate_scoring.md](candidate_scoring.md) | Per-candidate weights and how they become beam costs |
| [lattice.md](lattice.md) | The pronunciation lattice, `LatticeRescorer` and the per-word confidence |
| [sentence_context.md](sentence_context.md) | The cross-word seam: `SentenceLattice` and `SentenceRescorer` |
| [lattice_per.md](lattice_per.md) | Phone error rate for ASR against every reading the lattice admits |
| [features.md](features.md) | Feature export for ML and CRF G2P |

### Comparing languages

| Page | Covers |
| :--- | :--- |
| [distance.md](distance.md) | Every relational axis and its API |
| [ancestry.md](ancestry.md) | Ancestor roles, clade nodes, ancestry distance and the Glottolog alignment |

### Writing a language spec

| Page | Covers |
| :--- | :--- |
| [adding_a_language.md](adding_a_language.md) | The steps to add a spec or a dialect |
| [allophony.md](allophony.md) | Post-lexical `allophone_rules` |
| [positional_graphemes.md](positional_graphemes.md) | Context-sensitive grapheme overrides |
| [quality_tiers.md](quality_tiers.md) | What `stub`, `skeleton`, `research` and `production` require |
| [ipa_reference.md](ipa_reference.md) | IPA symbols, code points and common errors |
| [bibliography.md](bibliography.md) | Reference works by family, and `LinguisticSource` |

### Contributing

| Page | Covers |
| :--- | :--- |
| [contributing/spec_authoring.md](contributing/spec_authoring.md) | The rules a spec keeps, how to express a context, and how to audit the data |
| [contributing/citations.md](contributing/citations.md) | Where to find a source, how to quote it, and which gold sets are silver |
| [contributing/board.md](contributing/board.md) | How to regenerate the benchmark board, and the guards that check it |
| [contributing/engine.md](contributing/engine.md) | How to add an engine capability, and the review gate for engine code |

### Measuring accuracy

| Page | Covers |
| :--- | :--- |
| [benchmarks.md](benchmarks.md) | What a score means, how it is computed and reproduced, and how to diagnose one |
| [benchmark_datasets.md](benchmark_datasets.md) | Every gold dataset, where it comes from, and the caveats on its rows |
| [wikipron_mirror.md](wikipron_mirror.md) | The pinned WikiPron snapshot and how to refresh it |
| [tts_gold.md](tts_gold.md) | The hand-built sentence gold sets for TTS voices |
| [scoreboard.md](scoreboard.md) | Every measured PER and exact-match result (generated) |
| [comparison.md](comparison.md) | PER against espeak-ng, epitran, gruut and other systems (generated) |
| [espeak_agreement.md](espeak_agreement.md) | Symbol-level agreement with espeak-ng (generated) |
| [lexicon_scoreboard.md](lexicon_scoreboard.md) | Rules-only against with-lexicon PER (generated) |
| [gold_defects.md](gold_defects.md) | Defects in gold rows, and how much of a row is alphabet-chart entries |
| [known_limitations.md](known_limitations.md) | What the specs and the ranker do not do, classified |
| [spec_diagnostics.md](spec_diagnostics.md) | A mechanical hunt for specs that are wrong rather than imprecise (generated) |

### Per language

| Page | Covers |
| :--- | :--- |
| [languages/index.md](languages/index.md) | The per-language pages, by family |
