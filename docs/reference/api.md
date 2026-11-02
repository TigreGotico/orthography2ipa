# Python API

These are the names `import orthography2ipa` exports, from `orthography2ipa.__all__`. Each summary is the first paragraph of the docstring. Read the docstring itself for the parameters.

`scripts/gen_reference_docs.py` writes this page. Do not edit it by hand.

## Constants and type aliases

| Name | Kind | Summary |
| --- | --- | --- |
| `AllophoneMap` | type alias | `Dict[str, List[str]]` |
| `DIALECT_PROFILES` | constant | A `dict` |
| `Grapheme2IPA` | type alias | `Dict[str, List[str]]` |
| `PositionalGrapheme2IPA` | type alias | `Dict[str, Dict[GraphemePosition, List[str]]]` |
| `SCRIPT_REGISTRY` | constant | A `dict` |
| `STAGES` | constant | A `tuple` |
| `STRESS_MARKS` | constant | A `tuple` |

## `orthography2ipa.allophony`

| Name | Kind | Summary |
| --- | --- | --- |
| `AllophoneRescorer` | class | A `LatticeRescorer` compiled from a spec's `allophone_rules`. |
| `compile_allophone_rescorer` | function | Compile `allophone_rules` into a rescorer, or `None` if empty. |

## `orthography2ipa.distance`

| Name | Kind | Summary |
| --- | --- | --- |
| `GraphemeDivergence` | class | How differently two languages use the same graphemes. |
| `InventoryDistance` | class | Result of comparing two phoneme inventories. |
| `PhonologicalDistance` | class | Combined phonological distance between two languages. |
| `SpellingDivergence` | class | How differently two orthographies WRITE the same sounds. |
| `allophone_overlap` | function | Jaccard similarity (0-1) of the allophone surface-form inventories. |
| `ancestry_similarity` | function | Compute ancestry-weighted similarity between two languages. |
| `feature_vector` | function | Return the 21-element distinctive feature vector for an IPA *segment*. |
| `full_distance` | function | Combined phonological + ancestry distance. |
| `geographic_distance` | function | Great-circle distance between two languages' representative points. |
| `grapheme_divergence` | function | Measure how differently two languages map shared graphemes to IPA. |
| `inventory_distance` | function | Compare the phoneme inventories of two languages. |
| `pairwise_distances` | function | Compute a symmetric distance matrix for a list of languages. |
| `phonological_distance` | function | Compute a combined phonological distance between two languages. |
| `segment_distance` | function | Phonetic distance between two IPA segments, normalised to [0.0, 1.0]. |
| `spelling_divergence` | function | Measure how differently two orthographies spell the same phonemes. |

## `orthography2ipa.features`

| Name | Kind | Summary |
| --- | --- | --- |
| `GraphemeFeatures` | class | The feature record for a single grapheme: one item of a CRF sequence. |
| `WordFeatures` | class | The feature sequence for one word: the unit a CRF trains/predicts on. |

## `orthography2ipa.g2p`

| Name | Kind | Summary |
| --- | --- | --- |
| `ConfidenceBreakdown` | class | Richer, per-signal view behind `confidence`. |
| `G2P` | class | Grapheme→IPA engine for one language. |
| `TranscriptionResult` | class | Detailed result of `transcribe_detailed`. |
| `WordTranscription` | class | One word of a transcription, with its alternatives. |
| `transcribe` | function | One-call convenience: transcribe *text* in *lang* to IPA. |

## `orthography2ipa.inventory`

| Name | Kind | Summary |
| --- | --- | --- |
| `dead_allophone_rules` | function | Ids of `allophone_rules` whose target phoneme this spec cannot produce. |
| `emission_inventory` | function | Every IPA string *spec* can place on a slot. |
| `phoneme_inventory` | function | The **token set**: `emission_inventory`, cut into segments. |
| `tokenize` | function | Cut a transcription into the tokens a TTS model consumes. |

## `orthography2ipa.lexicon`

| Name | Kind | Summary |
| --- | --- | --- |
| `available_lexicon_codes` | function | Sorted language codes with a registered lexicon or a `{code}.tsv` in the dir. |
| `clear_lexicons` | function | Forget every registered lexicon and the lexicon dir. |
| `get_lexicon` | function | Return the `{word: ipa}` overlay for *code*, or `{}` if none is set. |
| `is_ipa_string` | function | Return `True` when *ipa* is NFC and contains only IPA characters. |
| `register_lexicon` | function | Register the lexicon *source* to use for language *code*. |
| `resolve_lexicon_source` | function | Resolve a lexicon *source* to a local file, fetching it if remote. |
| `set_lexicon_dir` | function | Use *path* as a directory of `{code}.tsv` lexicons (`None` to unset). |
| `validate_lexicon_text` | function | Validate a lexicon TSV body; return a list of `(line_no, reason)`. |

## `orthography2ipa.phonetok`

| Name | Kind | Summary |
| --- | --- | --- |
| `Candidate` | class | One ranked IPA option for a single lattice slot. |
| `GraphemeContext` | class | A context-aware view over one GRAPHEME `Token`. |
| `IPAPath` | class | One possible IPA transcription path through a token sequence. |
| `PhonetokTokenizer` | class | Language-agnostic grapheme tokenizer with IPA beam expansion. |
| `SegmentSlot` | class | One position in the structured pronunciation lattice. |
| `Token` | class | A single token emitted by `PhonetokTokenizer`. |
| `TokenKind` | class | Classification of a single token produced by the tokenizer. |
| `TokenSequence` | class | An indexed, context-aware view over a tokenised string. |

## `orthography2ipa.plugins`

| Name | Kind | Summary |
| --- | --- | --- |
| `NormalizePlugin` | class | Decides what the input *is*, canonically, before anything reads it. |
| `SandhiPlugin` | class | What happens between words. |

## `orthography2ipa.registry`

| Name | Kind | Summary |
| --- | --- | --- |
| `MissingPlugin` | class | A spec named a plugin and it is not installed. |
| `UnknownVariantWarning` | class | A private-use (`-x-`) subtag names no registered spec. |
| `ancestry_chain` | function | Return the `parent` chain above *code*, nearest ancestor first. |
| `available_codes` | function | Return all registered language codes. |
| `available_families` | function | Return `{family: [codes]}` for every loaded language. |
| `get` | function | Return the `LanguageSpec` for *code*, loading lazily. |
| `get_rescorers` | function | The rescorers every registered plugin contributes for *code*, in order. |
| `get_stress_plugin` | function | The stress plugin registered for *code*, if any. |
| `get_syllabifier` | function | Return the syllabifier plugin for *code*, if one is registered. |
| `resolve` | function | Return the registered spec code that *code* resolves to. |
| `resolves_exactly` | function | True when *code* names a spec without nearest-language guessing. |
| `who_answers` | function | Who is answering for *code*, and from where. |

## `orthography2ipa.rescorer`

| Name | Kind | Summary |
| --- | --- | --- |
| `LatticeRescorer` | class | A pure, composable re-costing pass over one lattice slot. |
| `RescoreContext` | class | Everything a `LatticeRescorer` sees about one slot's context. |

## `orthography2ipa.rescorer_plugin`

| Name | Kind | Summary |
| --- | --- | --- |
| `RescorerPlugin` | class | Contributes lattice rescorers (phonology) for one or more languages. |

## `orthography2ipa.sandhi`

| Name | Kind | Summary |
| --- | --- | --- |
| `SandhiEngine` | class | Applies sandhi rules across word boundaries in a token stream. |

## `orthography2ipa.script_distance`

| Name | Kind | Summary |
| --- | --- | --- |
| `ScriptFeatures` | class | Typological feature bundle for a writing system. |
| `script_distance` | function | Combined script distance in [0.0, 1.0]. |
| `script_distance_by_name` | function | Convenience: look up scripts by name and compute distance. |

## `orthography2ipa.sentence`

| Name | Kind | Summary |
| --- | --- | --- |
| `Position` | class | Where a word sits inside a bounded span (a phrase, or the utterance). |
| `SentenceLattice` | class | The whole utterance as an ordered list of `WordSlot`. |
| `SentenceRescoreContext` | class | Everything a `SentenceRescorer` sees about one word's place in the utterance. |
| `SentenceRescorer` | class | A pure, composable rewrite pass over one word, with cross-word context. |
| `WordContext` | class | Context for a word in a sentence, enabling sandhi/liaison. |
| `WordSlot` | class | One word's place in a `SentenceLattice`. |

## `orthography2ipa.stress`

| Name | Kind | Summary |
| --- | --- | --- |
| `apply_stress_mark` | function | Insert `rules.stress_mark` before the stressed syllable of *ipa*. |
| `detect_stress` | function | Return the 0-based index of the stressed syllable of *word*. |
| `syllabify` | function | Split *word* into syllables by vowel groups. |
| `syllabify_ipa` | function | Split an IPA word into syllables, dividing clusters by *max_onset*. |

## `orthography2ipa.stress_plugin`

| Name | Kind | Summary |
| --- | --- | --- |
| `StressPlugin` | class | Decides which syllable carries primary stress, for the languages it claims. |

## `orthography2ipa.syllabifier_plugin`

| Name | Kind | Summary |
| --- | --- | --- |
| `SyllabifierPlugin` | class | Abstract base for language-specific syllabifiers. |

## `orthography2ipa.transforms`

| Name | Kind | Summary |
| --- | --- | --- |
| `DialectTransform` | class | A named dialect profile containing an ordered list of transform rules. |
| `IPAChainShift` | class | A simultaneous multi-vowel mapping (chain shift). |
| `IPALexicalRule` | class | A word-specific lexical substitution (requires orthographic word). |
| `IPARule` | class | A single phoneme-level IPA transformation rule. |
| `apply_transform` | function | Apply a dialect transform to an IPA string. |
| `available_profiles` | function | Return sorted list of available dialect profile codes. |
| `debias_lisbon` | function | Convert Lisbon-biased phonemizer output to neutral standard PT-PT. |
| `load_clup_profile` | function | Load a CLUP allophone profile for a region from the analysis CSV. |

## `orthography2ipa.types`

| Name | Kind | Summary |
| --- | --- | --- |
| `AllophoneRule` | class | One declarative, context-conditioned `phoneme → surface` rewrite. |
| `Ancestor` | class | A single ancestry link from a language to one of its ancestors. |
| `AncestorRole` | class | How an ancestor language relates to its descendant. |
| `LanguageSpec` | class | Complete phonological specification for one language / variety. |
| `Location` | class | A representative point for where a language is spoken. |
| `OrthographyKind` | class | What kind of writing a spec's `graphemes` actually encode. |
| `OrthographyStandard` | class | The official, publicly published orthography of a language. |
| `QualityTier` | class | Classification of data quality and completeness for a language spec. |
| `SandhiRule` | class | A single sandhi / liaison rule applied across word boundaries. |
| `ScriptType` | class | Typological classification of a writing system. |
| `StressRules` | class | Declarative rules for primary word-stress placement. |

## `orthography2ipa.underspecification`

| Name | Kind | Summary |
| --- | --- | --- |
| `is_underdetermined` | function | True when *word*'s reading is, in part, a guess. |
| `mark_density` | function | The fraction of *word*'s letters the writing actually determines, in `[0, 1]`. |
| `underdetermined_positions` | function | Indices of the letters in *word* whose reading the writing does not fix. |

---
[← Known limitations](../guide/known_limitations.md) · [Home](../index.md) · [Command line →](cli.md)
