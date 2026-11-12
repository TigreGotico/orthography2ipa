# Architecture

`orthography2ipa` has two parts: the per-language JSON specs under `orthography2ipa/data/`, and one engine that reads any spec. This page describes the stages of the engine, the modules that hold them and the design choices behind them. The repository map in [`AGENTS.md`](../../AGENTS.md) gives the short view of the files.

The engine has no language-specific code. A behaviour that one language needs becomes a generic capability that any spec can switch on, and the spec holds only data. [orthography2ipa.cpp](https://github.com/loom-ai-org/orthography2ipa.cpp) is a C++17 port of the same data-driven core, and it reads the same JSON specs.

## The pipeline

`G2P` in `g2p.py` is the full engine, and `transcribe()` wraps it. Each call runs the stages below in order. Each stage reads only the spec and the input. A stage with nothing to do (no rules, no plugin, no rescorer) leaves the output as it is.

| Step | Stage | What happens |
| :--- | :--- | :--- |
| 1 | Markup | `markup.parse_markup` splits out each `<phoneme ph="…">` element. A forced word keeps its IPA through the word stages and gets no stress mark ([lexicon.md](../guide/lexicon.md)). |
| 2 | Prepare the text | `Pipeline.expand` runs on each plain run, and then `Pipeline.mark` runs once on the sentence. With neither field set, the normalize plugin that the spec or the deprecated `plugins=` argument names runs, and then the deprecated `normalizer` callable. With none of them, the text passes through unchanged, because the library does not normalise text. |
| 3 | Word override | Each word looks up the spec's `word_exceptions`, and then the lexicon of the engine. A hit replaces the rules for that word. |
| 4 | Tokenize | `PhonetokTokenizer` cuts the word into grapheme tokens by maximal munch over a trie of the grapheme keys. |
| 5 | Select | Each grapheme slot gets its candidates and their costs from the positional overrides and the weights. A grammatical ending can rewrite the end of the word. |
| 6 | Rescore | The rescorers re-cost each slot in the context of its neighbours. The rescorers of `Pipeline.rescore` run first, then the rescorers of declared plugins, then the allophone rules of the spec. |
| 7 | Beam select | Greedy search keeps one path, and beam search keeps `beam_width` paths. The best path wins. |
| 8 | Finalize the word | Computed tone, geminate collapse, the word-final virama vowel, tone-mark docking, iambic lengthening and the stress mark apply in that order. |
| 9 | Compound stress | A spec with `compound_stress == "last"` marks hyphen-joined compounds. |
| 10 | Sentence rescorers | A `SentenceRescorer` that the caller passes in the deprecated `sentence_rescorer=` argument sees the whole utterance and can rewrite across words. |
| 11 | Sandhi | The declarative `sandhi_rules` of the spec run, and then `Pipeline.sandhi`. With no `Pipeline.sandhi`, a declared sandhi plugin runs in its place. |
| 12 | Dialect transform | An optional `dialect_profile` rewrites the final IPA. |
| 13 | NFC | The engine normalises the output to Unicode [Normalization Form C](https://unicode.org/reports/tr15/). |

### Tokenizer and lattice

`phonetok.py` is the tokenizer, and it works from a `LanguageSpec` alone. `_GraphemeTrie` matches the longest grapheme key at each position. [tokenizer.md](tokenizer.md) describes the token kinds and the context view.

```
text
  │
  ▼
PhonetokTokenizer.tokenize()
  ├── trie lookup (maximal munch) → GRAPHEME tokens
  ├── regex match → WHITESPACE, PUNCTUATION, DIGIT
  └── fallback → UNKNOWN tokens
  │
  ▼
List[Token]   (each with .grapheme and the .ipa candidates)
  │
  ▼
PhonetokTokenizer.ipa_beam()
  ├── resolve the candidates of each slot (positional overrides, weights)
  ├── rescore (optional): re-cost each slot given its neighbours
  └── beam search over the slot candidates
  │
  ▼
List[IPAPath]   (sorted by score, best first)
```

The pronunciation lattice and the rescorer seam both rest on the `GraphemeContext` view of each grapheme. The view holds the neighbours of the grapheme and its class predicates from `vowels.py`. A phonemizer built on the engine reads the same view, so it needs no index arithmetic or vowel sets of its own.

`ipa_lattice(text)` returns the ranked lattice, and `ipa_best(text)` returns its best path. [lattice.md](lattice.md) describes the lattice, and [Rescoring the lattice](lattice.md#rescoring-the-lattice) describes the rescore stage. [Refine or fork?](lattice.md#refine-the-lattice-or-fork-the-tokenizer) says when a downstream rule cascade belongs in it.

### Allophony

The allophony stage is the rescorer built into the engine. A spec's `allophone_rules` are post-lexical rewrites from phoneme to surface form, such as final devoicing, place assimilation, reduction and flapping. `allophony.compile_allophone_rescorer` compiles them into an `AllophoneRescorer`, the last rescorer of the rescore stage. `allophone_passes` sets how many times the pass runs, so one rule can feed another.

The stage turns the phoneme lattice into an allophone lattice. It needs the stress context of the engine, so a stress-conditioned rule does not fire on the standalone tokenizer path. Sandhi and stress marks are absent from that path for the same reason. A spec with no `allophone_rules` compiles to no rescorer. [allophony.md](allophony.md) describes the rules.

### Stress and syllabification

`stress.syllabify` is the bundled syllabifier. It splits a word by vowel groups and maximises the onset. A spec that sets `constrain_onsets` maximises the onset only as far as the language allows. The allowed shapes come from `_OnsetJudge`, which reads the grapheme table of the spec through the sonority scale in `vowels.py`. A `stress.max_onset` cap in the spec limits the onset further.

A declared `stress.onset_clusters` list decides every complex onset in place of the shapes, so `pt-BR` divides *pasta* as `pas.ta` and *advogado* as `ad.vo.ga.do`. The shapes fit Germanic and Romance, so the flag is opt-in. Modern Greek leaves it off, because ⟨σμ κτ πτ γν μν βγ βδ⟩ all begin words and never split. The flag follows the `graphemes_base` edge, so a variety that uses a constrained table syllabifies it as its base does. For Portuguese, a caller can pass the full [silabificador](https://github.com/TigreGotico/silabificador) syllabifier in `Pipeline(syllabifier=...)`.

The stress mark needs a second division, of the transcription and not of the spelling. The mark goes before the stressed syllable, so the start of that syllable decides its position. `stress.syllabify_for_mark` divides the IPA with the same rule of maximal, constrained onsets, through `_IpaOnsetJudge`. That judge uses the same shapes, read off IPA segments, and it also allows every rise onto a glide.

The orthographic shapes refuse an obstruent + /j/ onset, because in continental Germanic that sequence marks a morpheme boundary. A transcription shows no boundaries, so no grapheme table enters this division, and `constrain_onsets` does not gate it. `stress.ipa_diphthongs`, or `stress.diphthongs` where the spec declares none, decide which vowel sequences are one nucleus. A declared `stress.max_onset` caps the onset here too.

The IPA shapes fit Germanic, Slavic and Romance. A language outside that range states its own case in one of two ways. The first way is `stress.onset_clusters`, which names the complex onsets of the language and then decides all of them. Ibero-Romance declares its obstruent + liquid inventory, which has no /s/ + stop, so Spanish *castigo* gives `kasˈtiɣo` and not `kaˈstiɣo`.

The second way is `stress.constrain_mark_onsets` set to `false`, which turns the judgement off for a language whose onsets the shapes get wrong. Greek sets it, for the same reason it leaves `constrain_onsets` off. Khmer sets it too, because its subscript consonants make onsets that no sonority scale predicts. The mark then falls where the vowel groups put it.

A caller that is sensitive to quantity has already divided the transcription, because it read its weights off that division. It passes the syllables to `apply_stress_mark` as `ipa_syllables`, and the function uses them as given.

### Sandhi and the sentence

`sandhi.SandhiEngine` applies the `SandhiRule` objects of a spec across word boundaries. A rule can rewrite the left word, the right word or both, and the first matching rule wins on each side ([data_model.md](../specs/data_model.md#sandhirule)). The punctuation between words marks a pause, and a rule applies only inside its prosodic domain.

`sentence.py` holds the cross-word context: `SentenceLattice`, `SentenceRescorer`, `WordSlot`, `Position` and `WordContext`, the context an engine passes down. [The sentence-context seam](lattice.md#the-sentence-context-seam) describes it.

## Pluggable steps

Five stages accept a plugin. All of them can change the transcription, so the spec or the caller must name the plugin. Discovery alone never selects one, because the install of a package must not change a transcription. A caller passes each step as an object in a `Pipeline` field, and that step needs no entry point.

| Stage | `Pipeline` field | Base class | Entry-point group |
| :--- | :--- | :--- | :--- |
| `normalize` | `expand`, `mark` | `NormalizePlugin` (`plugins.py`), deprecated | `orthography2ipa.normalize`, deprecated |
| `syllabify` | `syllabifier` | `SyllabifierPlugin` (`syllabifier_plugin.py`) | None |
| `stress` | None: the spec's stress rules | `StressPlugin` (`stress_plugin.py`), deprecated | `orthography2ipa.stress`, deprecated |
| `rescore` | `rescore` | `RescorerPlugin` (`rescorer_plugin.py`), deprecated | `orthography2ipa.rescore`, deprecated |
| `sandhi` | `sandhi` | `SandhiPlugin` (`plugins.py`) | `orthography2ipa.sandhi`, deprecated |

The spec names a plugin in its `plugins` field by entry-point name, such as `{"sandhi": "arbtok"}`. The caller overrides it with the `Pipeline` field of the stage, and the engine then does not resolve the name. The caller can also name a plugin with `G2P(lang, plugins={...})`, which is deprecated. A declared plugin that is not installed raises `MissingPlugin`, and the engine never falls back to the built-in answer. The discovery by entry point, the three deprecated base classes and the constants `STAGES`, `OUTPUT_CHANGING_STAGES` and `ENTRY_POINT_GROUPS` go in the next major release. Each one raises a `DeprecationWarning` when a caller uses it.

`plugins.py` states the contract of each stage. `conformance.py` holds the contract checks: `assert_syllabifier_conforms` fails if an installed syllabifier moves the output, and `assert_rescorer_conforms` checks a rescorer. Discovery uses Python [entry points](https://packaging.python.org/en/latest/specifications/entry-points/). [registry.md](../reference/registry.md#plugin-discovery) describes how the registry finds plugins and which one wins.

## Modules

| Module | Responsibility | Main names |
| :--- | :--- | :--- |
| `types.py` | The frozen data model and the inheritance manifest | `LanguageSpec`, `Ancestor`, `AncestorRole`, `QualityTier`, `ScriptType`, `OrthographyKind`, `GraphemePosition`, `SandhiRule`, `AllophoneRule`, `StressRules`, `FIELD_INHERITANCE` |
| `json_loader.py` | Loads a spec file and resolves its inheritance | `load_json_spec`, `load_all_json_specs`, `available_json_codes` |
| `schema.py` | Pydantic validation behind `orthography2ipa validate` | |
| `registry.py` | Code resolution, lazy loading, the deprecated plugin discovery | `get`, `resolve`, `available_codes`, `available_families`, `ancestry_chain`, `get_syllabifier`, `MissingPlugin` |
| `g2p.py` | The pipeline from text to IPA | `G2P`, `transcribe`, `TranscriptionResult`, `WordTranscription`, `ConfidenceBreakdown` |
| `phonetok.py` | Tokenizer, lattice and beam search | `PhonetokTokenizer`, `Token`, `TokenKind`, `IPAPath`, `Candidate`, `SegmentSlot`, `GraphemeContext`, `TokenSequence` |
| `positional.py`, `weights.py` | Positional grapheme contexts, grammatical endings, and candidate weights | |
| `vowels.py` | Phonological classes of graphemes and segments | `grapheme_is_vowel`, `is_ipa_vowel` |
| `rescorer.py`, `allophony.py` | The rescorer seam and the allophone rules compiled onto it | `LatticeRescorer`, `RescoreContext`, `AllophoneRescorer`, `compile_allophone_rescorer` |
| `stress.py`, `tone.py` | Syllabification, stress placement and tone marks | `syllabify`, `syllabify_ipa`, `detect_stress`, `apply_stress_mark` |
| `sandhi.py`, `sentence.py` | Cross-word rules and the sentence lattice | `SandhiEngine`, `SentenceLattice`, `SentenceRescorer`, `WordContext` |
| `pipeline.py` | The configuration that a caller gives to one engine | `Pipeline` |
| `lexicon.py`, `markup.py` | The lexicon overlay and the `<phoneme>` markup | `load_lexicon`, `packaged_lexicon`, `MarkupError` |
| `features.py` | Feature export for ML and CRF G2P ([feature export](lattice.md#feature-export-for-a-learned-model)) | `WordFeatures`, `GraphemeFeatures` |
| `inventory.py`, `underspecification.py` | Emission and phoneme inventories, TTS tokens, and the places where the spelling leaves a reading open | `phoneme_inventory`, `emission_inventory`, `is_underdetermined` |
| `distance.py` | The relational distance metrics ([distance.md](../guide/distance.md)) | See below |
| `feats.py` | The distinctive-feature matrix: the 21 SPE and IPA features of [PyPhone](https://github.com/lingz/pyphone) (MIT), plus a click feature and a nasal-vowel feature | `vectorize_phones`, `is_vowel_phone`, `phonetic_distance` |
| `script_distance.py` | Typological distance between writing systems | `ScriptFeatures`, `SCRIPT_REGISTRY`, `script_distance`, `script_distance_by_name` |
| `lattice_per.py` | Phone error rate against a lattice ([lattice_per.md](lattice_per.md)) | `lattice_per`, `LatticePER` |
| `transforms.py` | IPA dialect transforms for Portuguese and Ibero-Romance | `DialectTransform`, `IPARule`, `IPAChainShift`, `IPALexicalRule`, `apply_transform`, `debias_lisbon`, `available_profiles`, `load_clup_profile`, `DIALECT_PROFILES` |
| `lm.py` | Phoneme n-gram language model utilities | `phoneme_embeddings`, `build_ngram_lm`, `perplexity` |
| `plugins.py`, `*_plugin.py`, `syllabifiers.py`, `conformance.py` | The pluggable steps, the bundled `silabificador` plugin and the contract checks | `SandhiPlugin`, `SyllabifierPlugin` |
| `exceptions.py` | Exception and warning types | `UnmappedScriptError`, `UnmappedGraphemeWarning`, `StubSpecWarning` |
| `cli.py` | The `orthography2ipa` command ([reference/cli.md](../reference/cli.md)) | `main` |
| `version.py` | The version, which the release workflow sets | `VERSION_STR` |

### The distance metrics

`distance.py` answers one question per function. It never folds the axes into one similarity number by default. The phonological metrics build on the feature matrix in `feats.py`, and `len(orthography2ipa.distance.feature_names())` gives its width.

| Axis | Functions |
| :--- | :--- |
| Phonological | `feature_vector`, `feature_names`, `segment_distance`, `inventory_distance`, `allophone_overlap`, `phonological_distance`, `tone_distance`, `phoneme_coverage` |
| Orthographic | `grapheme_divergence` (same text, same sounds?), `spelling_divergence` (same sounds, same spelling?), `positional_divergence`, `orthographic_distance` |
| Genealogical, temporal, geographic | `ancestry_similarity`, `temporal_distance`, `geographic_distance` (which returns `None` when a spec has no `location`) |
| Combined, for a caller that wants one number | `full_distance`, `weighted_full_distance`, `pairwise_distances` |

### Dialect transforms

`transforms.py` rewrites a finished IPA string into a dialect. An `IPARule` is one rewrite, an `IPAChainShift` is an ordered chain of shifts, and an `IPALexicalRule` is a rule that the orthography conditions. A `DialectTransform` bundles the rules of one dialect.

`DIALECT_PROFILES` holds the built-in profiles, such as northern Portuguese, Galician and Leonese, and `available_profiles()` lists their names. `apply_transform(ipa, profile, ortho=None, debias=True, allophone_weights=None)` applies one profile. `debias_lisbon(ipa, ortho=None)` moves eSpeak PT-PT output towards the neutral standard. `load_clup_profile(region, clup_csv)` reads the allophone weights of one region from a CSV analysis of the [Arquivo Dialetal do CLUP](https://cl.up.pt/arquivo/), in the form that `allophone_weights` takes.

## Design decisions

### Frozen data

`LanguageSpec`, `Ancestor`, `Token` and `IPAPath` are frozen dataclasses. The loader also freezes every mapping inside a spec, nested mappings included, as a `FrozenDict` that refuses in-place changes. So threads can share a spec, and `registry.get()` hands every caller the same cached object.

The candidate lists inside those mappings stay ordinary Python lists, because the public contract types them as `List[str]`. Treat them as read-only. A change to one of them changes the shared spec for every caller in the process.

### JSON data files

Each spec is a JSON file, apart from the code. People can review, edit and validate a spec without reading Python. A dialect reuses its base through the `*_base` keys ([data_model.md](../specs/data_model.md#inheritance-between-specs)).

### Maximal munch

[Maximal munch](https://en.wikipedia.org/wiki/Maximal_munch), the longest match first, is the standard way to tokenize an orthography with digraphs and longer graphemes. Portuguese ⟨lh⟩ must match as one unit, not as ⟨l⟩ + ⟨h⟩. A [trie](https://en.wikipedia.org/wiki/Trie) of the grapheme keys finds the match in O(k) time, where k is the length of the longest key.

### Beam search

Ambiguous graphemes multiply the paths of a word: English ⟨c⟩ alone gives /k/ or /s/. A full enumeration does not scale to long words, so the engine uses [beam search](https://en.wikipedia.org/wiki/Beam_search) and keeps the cheapest paths. Without weights, the cheapest path takes the first candidate of each grapheme. With weights, it is the most probable path ([How cost works](lattice.md#how-cost-works)).

### Lazy loading

An import of `orthography2ipa` indexes the file names in the data directory and parses no JSON. `registry.get()` loads a spec on first request and caches it. So a session loads only the languages it uses.

## Downstream engines

`orthography2ipa` hosts no G2P engine plugins. Nothing here discovers or calls a whole engine. Language-specific engines consume this library. They read its spec data, drive its lattice and add their own rescorers, or keep a tokenizer of their own ([lattice.md](lattice.md#refine-the-lattice-or-fork-the-tokenizer) covers the choice). That is the opposite direction from a plugin.

| Engine | Language | C++ port |
| :--- | :--- | :--- |
| [arbtok](https://github.com/TigreGotico/arbtok) | Arabic | [arbtok.cpp](https://github.com/loom-ai-org/arbtok.cpp) |
| [tugaphone](https://github.com/TigreGotico/tugaphone) | Portuguese, across the Lusophone dialects | [tugaphone.cpp](https://github.com/loom-ai-org/tugaphone.cpp) |
| [euskaphone](https://github.com/TigreGotico/euskaphone) | Basque, as a dialect-aware TTS front end over the lattice | |

What a package can replace is one step of the pipeline, through the stages above. [api_stability.md](../reference/api_stability.md) lists the names those engines import.

## Extending the package

[../contributing/spec_authoring.md](../contributing/spec_authoring.md) covers a new language, and [contributing/engine.md](../contributing/engine.md) covers a change to the engine.

---
[← Public API stability](../reference/api_stability.md) · [Home](../index.md) · [Tokenizer →](tokenizer.md)
