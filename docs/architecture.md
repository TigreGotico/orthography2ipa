# Architecture

`orthography2ipa` has two parts: the per-language JSON specs under `orthography2ipa/data/`, and one engine that reads any spec. This page describes the stages of the engine, the modules that hold them and the design choices behind them. The repository map in [`AGENTS.md`](../AGENTS.md) gives the short view of the files.

## The pipeline

`G2P` in `g2p.py` is the full engine, and `transcribe()` wraps it. For each call, it runs these stages in order:

1. Markup. `markup.parse_markup` splits out each `<phoneme ph="…">` element. A forced word keeps its IPA through the word stages and gets no stress mark ([lexicon.md](lexicon.md)).
2. Normalize. The normalize plugin that the spec or the caller names runs first, and then the `normalizer` callable of the caller. With neither, the text passes through unchanged, because the library does not normalise text.
3. Word override. Each word looks up `word_exceptions` and then a registered lexicon. A hit replaces the rules for that word.
4. Tokenize. `PhonetokTokenizer` cuts the word into grapheme tokens by maximal munch over a trie of the grapheme keys.
5. Select. Each grapheme slot gets its candidates and their costs from the positional overrides and the weights. A grammatical ending can rewrite the end of the word.
6. Rescore. The rescorers re-cost each slot in the context of its neighbours. The order is the rescorers of the caller, then the rescorers of declared plugins, then the allophone rules of the spec.
7. Beam select. Greedy search keeps one path, and beam search keeps `beam_width` paths. The best path wins.
8. Finalize the word. Computed tone, geminate collapse, the word-final virama vowel, iambic lengthening and the stress mark apply in that order.
9. Compound stress. A spec with `compound_stress == "last"` marks hyphen-joined compounds.
10. Sentence rescorers. A `SentenceRescorer` that the caller passes sees the whole utterance and can rewrite across words.
11. Sandhi. The declarative `sandhi_rules` of the spec run, and then any declared sandhi plugin.
12. Dialect transform. An optional `dialect_profile` rewrites the final IPA.
13. NFC. The engine normalises the output to NFC.

Each stage reads only the spec and the input. A stage with nothing to do (no rules, no plugin, no rescorer) leaves the output as it is.

### Tokenizer and lattice

`phonetok.py` is the tokenizer, and it works from a `LanguageSpec` alone. `_GraphemeTrie` matches the longest grapheme key at each position in O(k) time, where k is the length of the longest key. Each token has a `TokenKind`: `GRAPHEME`, `WHITESPACE`, `PUNCTUATION`, `DIGIT`, `UNKNOWN`, `BOS` or `EOS`. A character that no key covers becomes an `UNKNOWN` token.

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

`tokenize_with_context(text)` returns a `TokenSequence` that wraps each grapheme token in a `GraphemeContext`. A `GraphemeContext` gives the neighbours in the word (`prev`, `next`, `at`, `neighbors`) and the character `span`. It also gives the class predicates `is_vowel`, `is_consonant`, `is_front` and `is_back` from `vowels.py`.

The pronunciation lattice and the rescorer seam both rest on this context. A phonemizer built on the engine reads the same view, and needs no index arithmetic or vowel sets of its own. `ipa_lattice(text)` returns the ranked lattice, and `ipa_best(text)` returns its best path. [lattice.md](lattice.md) describes the lattice.

### The rescorer seam

The rescore stage runs after the candidates of each slot are resolved and before the beam selects a path. A rescorer re-costs one slot as a pure function of the slot and its context. A downstream rule cascade, such as sun-letter assimilation or a silent-⟨e⟩ rule, can be a rescorer over the shared lattice. That works when the rule chooses among candidates that the lattice already holds. Then the engine needs no forked tokenizer.

[Rescoring the lattice](lattice.md#rescoring-the-lattice) and [Refine or fork?](lattice.md#refine-the-lattice-or-fork-the-tokenizer) say when each approach fits. With no rescorer, the output does not change.

### Allophony

The allophony stage is the rescorer built into the engine. A spec's `allophone_rules` are post-lexical rewrites from phoneme to surface form: final devoicing, place assimilation, reduction and flapping. `allophony.compile_allophone_rescorer` compiles them into an `AllophoneRescorer`, and the engine puts it after every other rescorer, so the rules of the spec have the last word. `allophone_passes` sets how many times the pass runs, so one rule can feed another.

The stage turns the phoneme lattice into an allophone lattice. It needs the stress context of the engine, so it does not run on the standalone tokenizer path, like sandhi and stress. A spec with no `allophone_rules` compiles to no rescorer. [allophony.md](allophony.md) describes the rules.

### Stress and syllabification

`stress.syllabify` is the bundled syllabifier, a splitter by vowel groups that maximises the onset. A spec that sets `constrain_onsets` maximises the onset only as far as the language allows. The allowed shapes come from `_OnsetJudge`, which reads the grapheme table of the spec through the sonority scale in `vowels.py`. A `stress.max_onset` cap in the spec limits the onset further. The shapes fit Germanic and Romance, so the flag is opt-in.

Modern Greek leaves it off, because ⟨σμ κτ πτ γν μν βγ βδ⟩ all begin words and never split. The flag follows the `graphemes_base` edge, so a variety that uses a constrained table syllabifies it as its base does.

The stress mark needs a second division, of the transcription and not of the spelling. The mark goes before the stressed syllable, so the start of that syllable decides its position. `stress.syllabify_for_mark` divides the IPA with the same rule of maximal, constrained onsets, through `_IpaOnsetJudge`. That judge uses the same shapes, read off IPA segments, and also allows every rise onto a glide.

The orthographic shapes refuse an obstruent + /j/ onset, because in continental Germanic that sequence marks a morpheme boundary, and a transcription shows no boundaries. No grapheme table enters this division, so `constrain_onsets` does not gate it. `stress.ipa_diphthongs`, or `stress.diphthongs` where the spec declares none, decide which vowel sequences are one nucleus. A declared `stress.max_onset` caps the onset here too.

The IPA shapes fit Germanic, Slavic and Romance. A language outside that range states its own case in one of two ways. `stress.onset_clusters` names the complex onsets of the language and then decides all of them. Ibero-Romance declares its obstruent + liquid inventory, which has no /s/ + stop, so Spanish *castigo* gives `kasˈtiɣo` and not `kaˈstiɣo`.

`stress.constrain_mark_onsets` set to `false` turns the judgement off for a language whose onsets the shapes get wrong. Greek sets it, for the same reason it leaves `constrain_onsets` off. Khmer sets it too, because its subscript consonants make onsets that no sonority scale predicts. The mark then falls where the vowel groups put it.

A caller that is sensitive to quantity has already divided the transcription, because it read its weights off that division. It passes the syllables to `apply_stress_mark` as `ipa_syllables`, and the function uses them as given.

### Sandhi and the sentence

`sandhi.SandhiEngine` applies the `SandhiRule` objects of a spec across word boundaries. A rule can rewrite the left word, the right word or both, and the first matching rule wins on each side ([data_model.md](data_model.md#sandhirule)). The punctuation between words marks a pause, and a rule applies only inside its prosodic domain. `sentence.py` holds the cross-word context: `SentenceLattice`, `SentenceRescorer`, `WordSlot`, `Position` and `WordContext`, the context an engine passes down. [sentence_context.md](sentence_context.md) describes that seam.

## Pluggable steps

Five stages accept a plugin. Four of them change the transcription, so the spec or the caller must name the plugin. Discovery alone never selects one of these, because an install of a package must not change a transcription. The syllabify stage is neutral: a better syllabifier draws better boundaries and gives the same answer.

| Stage | Base class | Entry-point group | Contract |
| :--- | :--- | :--- | :--- |
| `normalize` | `NormalizePlugin` (`plugins.py`) | `orthography2ipa.normalize` | Declared |
| `syllabify` | `SyllabifierPlugin` (`syllabifier_plugin.py`) | `orthography2ipa.syllabify` | Neutral |
| `stress` | `StressPlugin` (`stress_plugin.py`) | `orthography2ipa.stress` | Declared |
| `rescore` | `RescorerPlugin` (`rescorer_plugin.py`) | `orthography2ipa.rescore` | Declared |
| `sandhi` | `SandhiPlugin` (`plugins.py`) | `orthography2ipa.sandhi` | Declared |

The spec names a plugin in its `plugins` field by entry-point name, such as `{"sandhi": "arbtok"}`. The caller overrides it with `G2P(lang, plugins={...})`. A declared plugin that is not installed raises `MissingPlugin`, and the engine never falls back to the built-in answer. `conformance.py` holds the contract checks: `assert_syllabifier_conforms` fails if an installed syllabifier moves the output, and `assert_rescorer_conforms` checks a rescorer. [registry.md](registry.md#plugin-discovery) describes how the registry finds plugins and which one wins.

## Modules

| Module | Responsibility | Main names |
| :--- | :--- | :--- |
| `types.py` | The frozen data model and the inheritance manifest | `LanguageSpec`, `Ancestor`, `AncestorRole`, `QualityTier`, `ScriptType`, `OrthographyKind`, `GraphemePosition`, `SandhiRule`, `AllophoneRule`, `StressRules`, `FIELD_INHERITANCE` |
| `json_loader.py` | Loads a spec file and resolves its inheritance | `load_json_spec`, `load_all_json_specs`, `available_json_codes` |
| `schema.py` | Pydantic validation behind `orthography2ipa validate` | |
| `registry.py` | Code resolution, lazy loading, plugin discovery | `get`, `resolve`, `available_codes`, `available_families`, `ancestry_chain`, `get_syllabifier`, `who_answers` |
| `g2p.py` | The pipeline from text to IPA | `G2P`, `transcribe`, `TranscriptionResult`, `WordTranscription`, `ConfidenceBreakdown` |
| `phonetok.py` | Tokenizer, lattice and beam search | `PhonetokTokenizer`, `Token`, `TokenKind`, `IPAPath`, `Candidate`, `SegmentSlot`, `GraphemeContext`, `TokenSequence` |
| `positional.py`, `weights.py` | Positional grapheme contexts, grammatical endings, and candidate weights | |
| `vowels.py` | Phonological classes of graphemes and segments | `grapheme_is_vowel`, `is_ipa_vowel` |
| `rescorer.py`, `allophony.py` | The rescorer seam and the allophone rules compiled onto it | `LatticeRescorer`, `RescoreContext`, `AllophoneRescorer`, `compile_allophone_rescorer` |
| `stress.py`, `tone.py` | Syllabification, stress placement and tone marks | `syllabify`, `syllabify_ipa`, `detect_stress`, `apply_stress_mark` |
| `sandhi.py`, `sentence.py` | Cross-word rules and the sentence lattice | `SandhiEngine`, `SentenceLattice`, `SentenceRescorer`, `WordContext` |
| `lexicon.py`, `markup.py` | The lexicon overlay and the `<phoneme>` markup | `register_lexicon`, `get_lexicon`, `MarkupError` |
| `features.py` | Feature export for ML and CRF G2P ([features.md](features.md)) | `WordFeatures`, `GraphemeFeatures` |
| `inventory.py`, `underspecification.py` | Emission and phoneme inventories, TTS tokens, and the places where the spelling leaves a reading open | `phoneme_inventory`, `emission_inventory`, `is_underdetermined` |
| `distance.py` | The relational distance metrics ([distance.md](distance.md)) | See below |
| `feats.py` | The 21-feature SPE/IPA distinctive-feature matrix, adapted from [PyPhone](https://github.com/lingz/pyphone) (MIT) | `vectorize_phones`, `is_vowel_phone`, `phonetic_distance` |
| `script_distance.py` | Typological distance between writing systems | `ScriptFeatures`, `SCRIPT_REGISTRY`, `script_distance`, `script_distance_by_name` |
| `lattice_per.py` | Phone error rate against a lattice ([lattice_per.md](lattice_per.md)) | |
| `transforms.py` | IPA dialect transforms for Portuguese and Ibero-Romance | `DialectTransform`, `IPARule`, `IPAChainShift`, `IPALexicalRule`, `apply_transform`, `debias_lisbon`, `available_profiles`, `load_clup_profile`, `DIALECT_PROFILES` |
| `lm.py` | Phoneme n-gram language model utilities | `phoneme_embeddings`, `build_ngram_lm`, `perplexity` |
| `plugins.py`, `*_plugin.py`, `syllabifiers.py`, `conformance.py` | The pluggable steps, the bundled `silabificador` entry point and the contract checks | `NormalizePlugin`, `SandhiPlugin`, `STAGES`, `SyllabifierPlugin`, `RescorerPlugin`, `StressPlugin` |
| `exceptions.py` | Exception and warning types | `UnmappedScriptError`, `UnmappedGraphemeWarning`, `StubSpecWarning` |
| `cli.py` | The `orthography2ipa` command ([reference/cli.md](reference/cli.md)) | `main` |
| `version.py` | The version, which the release workflow sets | `VERSION_STR` |

### The distance metrics

`distance.py` answers one question per function and never folds the axes into one similarity number by default. The phonological metrics build on the 21-feature matrix in `feats.py`.

| Axis | Functions |
| :--- | :--- |
| Phonological | `feature_vector`, `feature_names`, `segment_distance`, `inventory_distance`, `allophone_overlap`, `phonological_distance`, `tone_distance`, `phoneme_coverage` |
| Orthographic | `grapheme_divergence` (same text, same sounds?), `spelling_divergence` (same sounds, same spelling?), `positional_divergence`, `orthographic_distance` |
| Genealogical, temporal, geographic | `ancestry_similarity`, `temporal_distance`, `geographic_distance` (which returns `None` when a spec has no `location`) |
| Combined, for a caller that wants one number | `full_distance`, `weighted_full_distance`, `pairwise_distances` |

### Dialect transforms

`transforms.py` rewrites a finished IPA string into a dialect. An `IPARule` is one rewrite, an `IPAChainShift` is an ordered chain of shifts, and an `IPALexicalRule` is a rule that the orthography conditions. A `DialectTransform` bundles the rules of one dialect. `DIALECT_PROFILES` holds the built-in profiles, such as northern Portuguese, Galician and Leonese, and `available_profiles()` lists their names. `debias_lisbon(ipa, ortho)` moves eSpeak PT-PT output towards the neutral standard. `load_clup_profile(path)` loads a CLUP dialect profile.

## Design decisions

### Frozen data

`LanguageSpec`, `Ancestor`, `Token` and `IPAPath` are frozen dataclasses. The loader also deep-freezes the dict and list fields of a spec. So threads can share a spec, and `registry.get()` hands every caller the same cached object.

### JSON data files

Each spec is a JSON file, apart from the code. People can review, edit and validate a spec without reading Python. A dialect reuses its base through the `*_base` keys ([data_model.md](data_model.md#inheritance-between-specs)).

### Maximal munch

Maximal munch, the longest match first, is the standard way to tokenize an orthography with digraphs and longer graphemes. Portuguese ⟨lh⟩ must match as one unit, not as ⟨l⟩ + ⟨h⟩. The trie finds the match in O(k) time.

### Beam search

Ambiguous graphemes multiply the paths of a word: English ⟨c⟩ alone gives /k/ or /s/. A full enumeration does not scale to long words. Beam search keeps the cheapest paths. Without weights, the cheapest path takes the first candidate of each grapheme, and with weights it is the most probable path ([candidate_scoring.md](candidate_scoring.md)).

### Lazy loading

Import of `orthography2ipa` indexes the file names in the data directory and parses no JSON. `registry.get()` loads a spec on first request and caches it. So a session loads only the languages it uses.

## Downstream engines

`orthography2ipa` hosts no G2P engine plugins. Nothing here discovers or calls a whole engine. Language-specific engines such as [arbtok](https://github.com/TigreGotico/arbtok) (Arabic) and [tugaphone](https://github.com/TigreGotico/tugaphone) (Portuguese) consume this library. They read its spec data, drive its lattice and add their own rescorers. That is the opposite direction from a plugin.

What a package can replace is one step of the pipeline, through the stages above. [api_stability.md](api_stability.md) lists the names those engines import.

## Extending the package

[adding_a_language.md](adding_a_language.md) is the full guide to a new language. In short, create `orthography2ipa/data/{code}.json` with the fields that `data/SCHEMA.md` requires. A dialect uses `graphemes_base` and `allophones_base` to inherit from its parent. Then run the test suite, which validates the spec. [contributing/engine.md](contributing/engine.md) covers a change to the engine.

---
[← Getting Started](getting_started.md) · [Home](index.md) · [Data Model →](data_model.md)
