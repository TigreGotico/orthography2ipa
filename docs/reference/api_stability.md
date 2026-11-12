# Public API stability

This page lists the names that downstream code imports from `orthography2ipa`, and the deprecation rule that protects them. It also describes the surfaces that a caller can add to the engine without a change to the default output.

## The stability commitment

No covered name is renamed or removed in one step. A rename or a removal follows the [semver](https://semver.org/) and [conventional-commit](https://www.conventionalcommits.org/) flow. The commit announces the change as breaking (`feat!:` or `BREAKING CHANGE:`), and a documented replacement supersedes the name. The name goes only after the major version passes the one that announced the deprecation. The removal version comes from `orthography2ipa/version.py` (`VERSION_MAJOR + 1`) at deprecation time, and no comment or page writes it by hand.

The commitment covers each name in the two tables of the next section. It also covers the names of the sentence-context seam and of the feature export, which the sections below describe.

The same rule covers the spec fields that `G2P` reads. The `plugins` field and the value `"plugin"` of `stress.source` are deprecated, and they go in the next major release. `G2P` raises a `DeprecationWarning` when it builds an engine on a spec that sets either one, once per engine. No shipped spec sets them, so `G2P(code)` stays silent for every code. A caller passes each step to one engine in a `Pipeline`.

## Names that downstream code imports

The inventory comes from the Python imports on the `dev` branch of each downstream repository: [arbtok](https://github.com/TigreGotico/arbtok), [euskaphone](https://github.com/TigreGotico/euskaphone) and [tugaphone](https://github.com/TigreGotico/tugaphone). The scan parses every Python file of each repository, so it covers the library code, the tests, the scripts and the examples. It counts both `from orthography2ipa import X` and attribute access such as `orthography2ipa.get`. [phonematcher](https://github.com/TigreGotico/phonematcher) and [sotaque_forcado](https://github.com/TigreGotico/sotaque_forcado) import nothing from `orthography2ipa`.

A name imported from a submodule and also re-exported at the top level is one name, and both import paths are covered.

### Names in `__all__`

| Name | Module | Used by |
| :--- | :--- | :--- |
| `G2P` | `g2p` | arbtok, euskaphone, tugaphone |
| `WordContext` | `sentence` | arbtok, euskaphone, tugaphone |
| `Pipeline` | `pipeline` | arbtok, euskaphone, tugaphone |
| `get` | `registry` | arbtok, tugaphone |
| `resolve` | `registry` | arbtok, euskaphone, tugaphone |
| `resolves_exactly` | `registry` | arbtok, tugaphone |
| `available_codes` | `registry` | arbtok, euskaphone, tugaphone |
| `who_answers` | `registry` | tugaphone |
| `register_lexicon`, `clear_lexicons` | `lexicon` | arbtok, euskaphone, tugaphone |
| `validate_lexicon_text` | `lexicon` | arbtok, euskaphone |
| `get_lexicon`, `available_lexicon_codes` | `lexicon` | euskaphone |
| `packaged_lexicon` | `lexicon` | tugaphone |
| `PhonetokTokenizer`, `TokenKind` | `phonetok` | arbtok, tugaphone |
| `Candidate`, `SegmentSlot` | `phonetok` | arbtok |
| `LatticeRescorer`, `RescoreContext` | `rescorer` | arbtok |
| `RescorerPlugin` | `rescorer_plugin` | arbtok |
| `NormalizePlugin`, `SandhiPlugin` | `plugins` | arbtok |
| `compile_allophone_rescorer` | `allophony` | arbtok |
| `segment_distance` | `distance` | arbtok |
| `phoneme_inventory`, `tokenize` | `inventory` | arbtok |
| `is_underdetermined`, `underdetermined_positions`, `mark_density` | `underspecification` | arbtok |
| `detect_stress` | `stress` | arbtok, tugaphone |
| `apply_stress_mark` | `stress` | arbtok |
| `syllabify_ipa` | `stress` | arbtok |
| `syllabify` | `stress` | euskaphone |
| `SyllabifierPlugin` | `syllabifier_plugin` | tugaphone |
| `LanguageSpec` | `types` | tugaphone |

`WordContext` is the shared cross-word vocabulary of the downstream engines. A downstream phonological rule cascade (sun-letter assimilation, silent ⟨e⟩, reduction) belongs in a `LatticeRescorer` over the shared lattice, not in a forked tokenizer ([lattice.md](../engine/lattice.md#rescoring-the-lattice)). `SyllabifierPlugin` is the matching contract for a syllabifier, and tugaphone implements one. `Pipeline` is how each of these engines passes its own steps to `G2P`.

### Names outside `__all__`

Downstream code also imports these public names straight from their submodules. They are covered too.

| Name | Module | Used by |
| :--- | :--- | :--- |
| `detect_stress_by_weight`, `is_cliticless` | `stress` | arbtok |
| `is_ipa_vowel` | `vowels` | arbtok |
| `is_front_vowel`, `is_orthographic_vowel` | `vowels` | tugaphone |
| `lexicon_path` | `lexicon` | arbtok |
| `parse_lexicon_text` | `lexicon` | euskaphone, tugaphone |

One downstream import reaches a private name: `phonetok._expand_arabic_gemination` in arbtok. A private name has no guarantee, and it can change in any release.

## Other names in `__all__`

These names are public and importable, but no downstream repository uses them. They can change more freely. Treat a dependency on them from outside this repository as unsupported until a consumer joins the inventory above.

| Module | Names |
| :--- | :--- |
| `g2p` | `transcribe`, `TranscriptionResult`, `WordTranscription`, `ConfidenceBreakdown` |
| `registry` | `ancestry_chain`, `available_families`, `get_rescorers`, `get_stress_plugin`, `get_syllabifier`, `MissingPlugin`, `UnknownVariantWarning` |
| `lexicon` | `load_lexicon`, `set_lexicon_dir`, `resolve_lexicon_source`, `use_packaged_lexicons`, `packaged_lexicon_sources`, `is_ipa_string` |
| `types` | `Grapheme2IPA`, `AllophoneMap`, `PositionalGrapheme2IPA`, `Ancestor`, `AncestorRole`, `QualityTier`, `ScriptType`, `OrthographyKind`, `OrthographyStandard`, `Location`, `SandhiRule`, `AllophoneRule`, `StressRules` |
| `phonetok` | `Token`, `IPAPath`, `GraphemeContext`, `TokenSequence` |
| `allophony`, `sandhi` | `AllophoneRescorer`, `SandhiEngine` |
| `stress_plugin`, `plugins` | `StressPlugin`, `STAGES` |
| `inventory` | `emission_inventory`, `dead_allophone_rules`, `STRESS_MARKS` |
| `distance` | `inventory_distance`, `grapheme_divergence`, `spelling_divergence`, `allophone_overlap`, `phonological_distance`, `ancestry_similarity`, `geographic_distance`, `full_distance`, `pairwise_distances`, `feature_vector`, `InventoryDistance`, `GraphemeDivergence`, `SpellingDivergence`, `PhonologicalDistance` |
| `script_distance` | `ScriptFeatures`, `SCRIPT_REGISTRY`, `script_distance`, `script_distance_by_name` |
| `transforms` | `apply_transform`, `debias_lisbon`, `available_profiles`, `DIALECT_PROFILES`, `DialectTransform`, `IPARule`, `IPAChainShift`, `IPALexicalRule`, `load_clup_profile` |
| `revision` | `spec_revision`, `lexicon_revision`: the format is covered by the commitment, see below |
| `sentence`, `features` | `SentenceLattice`, `SentenceRescorer`, `SentenceRescoreContext`, `WordSlot`, `Position`, `WordFeatures`, `GraphemeFeatures`: covered by the commitment, see below |

The exception types `UnmappedScriptError`, `UnmappedGraphemeWarning`, `StubSpecWarning` and `EngineSourceUnavailable` live in `orthography2ipa.exceptions` and are not re-exported at the top level. `slot_confidence` and `lattice_confidence` live in `orthography2ipa.phonetok` only.

## Spec revisions

`spec_revision(code)` names the rules that an engine for `code` reads. A consumer records the value when it trains, and compares it with the value of the engine that it runs later.

The value is `"sha256:"` followed by a hex digest. It is a function of three inputs, in this order:

1. The spec-format version, `orthography2ipa.revision.SPEC_FORMAT_VERSION`. The version is `1`.
2. The spec files that the loader merges into the spec. These are the file of the resolved code, then every file on its `parent` chain and on each `<field>_base` chain, sorted by code. A clade with no `parent` key continues the chain through its first `parent`-role ancestor, because `LanguageSpec` takes its `parent` from there. Each file counts as its parsed JSON with sorted keys and no whitespace, tagged with its code. The other `ancestors` codes do not count, because the loader merges none of their data.
3. The engine fingerprint. This is a sha256 over the tokens of the modules in `orthography2ipa.revision.ENGINE_MODULES`, the modules on the transcription path. Comments, blank lines and the width of an indent do not count. Statement ends, block edges and docstrings count, so a line that moves into or out of a block changes the value. The package version does not count, because a daily alpha changes it with no change to the engine.

The code resolves as `G2P` resolves it, so an alias and its canonical code give one revision. The value is computed at the first call for a code in a process, and the process keeps it. The engine files are read at that first call. If the package files change on disk before it, the value describes the files on disk and not the code that the process runs. A whitespace-only edit of a spec leaves the revision equal. An edit to a spec that is not on the chains of `code` leaves it equal too.

The engine fingerprint needs the `.py` source of each engine module. An install that ships only byte code still transcribes, but `spec_revision` raises `orthography2ipa.exceptions.EngineSourceUnavailable`, a `RuntimeError`.

The spec-format version goes up when a spec field starts to mean something else. An example is an engine that reads an existing key in a new way. Every spec revision then changes, although no spec file changed. A new optional field does not need a new version, because only the specs that use it change.

`lexicon_revision(code, patches=False)` names the packaged lexicon that `packaged_lexicon(code, patches)` reads. It is a sha256 over the `patches` flag, the bytes of the exceptions file and, with `patches=True`, the bytes of the patch file. The two values of the flag never give one revision. The function raises `LookupError` in the cases where `packaged_lexicon` raises it. A lexicon sits outside the spec, so a consumer that passes one to the engine records both revisions.

## Surfaces that leave the default output unchanged

The surfaces below add information or a hook. None of them changes `transcribe`, `transcribe_detailed().ipa`, `ipa_best` or the scoreboard, whether a caller reads them or not.

### Unmapped characters

A word can hold characters that the grapheme table of the spec does not cover, such as Hanzi sent to the Pinyin spec. Without a signal, such a word gives an empty `ipa`, which looks like real silence. These fields make the difference visible:

| Name | Meaning |
| :--- | :--- |
| `WordTranscription.unmapped: Tuple[str, ...] = ()` | The characters of the word with no grapheme mapping, empty when all mapped |
| `WordTranscription.coverage: float = 1.0` | The share of the characters of the word that mapped, in `[0.0, 1.0]` |
| `G2P(..., on_unmapped="warn")` | How the engine reacts, in one of four modes |

| `on_unmapped` | Behaviour |
| :--- | :--- |
| `"warn"` (default) | Each unmapped letter or combining mark emits one `UnmappedGraphemeWarning` per engine and character |
| `"ignore"` | No signal. Read `unmapped` and `coverage` from `transcribe_detailed` |
| `"log"` | One `logging.warning` per distinct `(lang, word)` pair |
| `"raise"` | `UnmappedScriptError` for that word, in place of a result |

`UnmappedGraphemeWarning` is a `UserWarning` subclass, and its message names the spec code and the code point. Only Unicode letters (`L*`) and marks (`M*`) warn, and punctuation, digits, symbols and spaces do not. A stub spec warns `StubSpecWarning` once instead. To turn the signal off, pass `on_unmapped="ignore"` or filter `UnmappedGraphemeWarning`.

### Per-word confidence

The per-word confidence is a deterministic read off the pronunciation lattice. A downstream phonemizer uses it to spend its lexicon or its rules only where the base engine is unsure.

| Name | Meaning |
| :--- | :--- |
| `WordTranscription.confidence: float = 1.0` | Confidence that `ipa` is the right pronunciation, in `[0.0, 1.0]` |
| `G2P.word_confidence(word, *, beam_width=8) -> float` | The same number for one word |
| `G2P.confidence_breakdown(word, *, beam_width=8) -> ConfidenceBreakdown` | The detail of each signal: `value`, `lattice`, `per_slot`, `coverage`, `unmapped` |
| `ConfidenceBreakdown` | The frozen breakdown dataclass, re-exported from `orthography2ipa` |

The value is the weakest link of three signals, each normalised to `[0, 1]`. The signals are the top-1 to top-2 cost margin of each slot, the rarity of each slot winner, and the word `coverage`. [lattice.md](../engine/lattice.md) gives the formula. A `WordTranscription(word=..., ipa=...)` built without a lattice keeps `confidence == 1.0`, so existing callers see no change.

### Finalized top-k readings

`G2P.word_candidates(word, *, k=5, beam_width=None) -> List[str]` returns the top *k* full transcriptions of one word, best first. A caller that reranks the lattice then needs no copy of the word-final pipeline. Each string has passed the same word-final stages as `transcribe_word`. These are geminate collapse, the rewrite of grammatical endings, the stress mark, and the lexicon or `word_exceptions` override.

The method merges duplicates, so the result can be shorter than *k*. A word with an override has one reading and consults no beam. A word with no output that can be spoken returns an empty list. `beam_width` defaults to `max(k, 8)`.

`G2P.candidates` is a different method. It returns the raw `IPAPath` beam paths, with none of those stages applied:

```python
from orthography2ipa import G2P
g = G2P("fr-FR")
g.candidates("bonjour")[0].ipa    # 'bɔnʒuʁ': no nasalisation, no stress stage
g.word_candidates("bonjour")[0]   # 'bɔ̃ʒuʁ'
```

Use `candidates` for the lattice costs, and `word_candidates` for readings that you compare against a transcription.

Element 0 of `word_candidates` is not by contract `transcribe_word(word)`. It usually is, and every measured gold set agrees. But `transcribe_word` defaults to greedy search of width 1, and this method runs a beam of width `max(k, 8)`. The wider beam can find a cheaper path that greedy pruning lost. Pass `beam_width=1` to make the identity hold by construction. A consumer that depends on the identity must check it, as the benchmark harness does in `assert_oracle_self_check`.

#### Ambiguous grammatical endings

A spec can declare an ending as an ordered candidate list, such as `"ent": [null, ""]`, when the orthography does not decide between its readings ([SCHEMA.md](../../orthography2ipa/data/SCHEMA.md#ambiguous-endings)). French verbal ⟨-ent⟩ is the case this exists for. Each declared alternative appears as an extra reading, ranked below element 0 and never above it. So `transcribe`, `transcribe_detailed().ipa`, `transcribe_word` and the 1-best columns of the scoreboard do not change. `word_candidates` and the oracle columns gain the reading that a downstream rescorer with part-of-speech tags needs.

A caller that assumes `word_candidates` returns only readings that the grapheme tables reach must drop that assumption. A caller that reads element 0 is not affected. `G2P(lang, expose_ambiguous_endings=False)` turns the extra readings off. The benchmark harness uses it, so the oracle columns of the scoreboard stay a pure diagnostic of ranking. The default is `True`, because a declared ambiguous ending exists to expose the reading that the engine cannot choose.

### Sentence-context seam

`G2P` and the `orthography2ipa.sentence` module give a cross-word surface. A downstream engine uses it in place of a sentence orchestrator of its own. The seam runs only when a caller calls `sentence_lattice`, or passes the deprecated `sentence_rescorer=`.

| Name | Meaning |
| :--- | :--- |
| `G2P(..., sentence_rescorer=None)` | Deprecated: use `Pipeline(sandhi=...)`. A `SentenceRescorer`, an iterable of them, or `None` (the default). Rescorers run before the declarative `sandhi_rules` of the spec |
| `G2P.sentence_lattice(text, *, search="greedy", beam_width=8) -> SentenceLattice` | A pure read of the lattice, IPA, and phrase and utterance position of each word, in order |
| `SentenceLattice`, `WordSlot`, `Position`, `SentenceRescorer`, `SentenceRescoreContext` | The shape a cross-word rule reads and rewrites, re-exported from `orthography2ipa` |

`WordSlot.slots` is the `SegmentSlot` lattice of the word, and `WordSlot.initial_slot` and `final_slot` are its edge candidates. `Position` is an enum with the values `INITIAL`, `MEDIAL`, `FINAL` and `SOLE`. `SentenceRescoreContext.prev_word` and `next_word` give the adjacent words, and `phrase_position` and `utterance_position` give the position. The stability commitment covers these names. The seam adds no `LanguageSpec` field, because a cross-word rule is a plugin object that the caller supplies. [../engine/lattice.md](../engine/lattice.md#the-sentence-context-seam) documents the seam.

### Feature export

`G2P` and the `orthography2ipa.features` module export the structure of each grapheme as features. A downstream ML or CRF G2P reads them and rescores the shared lattice. The export is a pure read.

| Name | Meaning |
| :--- | :--- |
| `G2P.features(text) -> list[WordFeatures]` | One `WordFeatures` per word, with the same word split as `transcribe`. It reuses `ipa_lattice`, `confidence_breakdown` and `flat_contexts`, and adds no scoring |
| `WordFeatures` | Frozen dataclass: `word`, `code`, `script`, `confidence`, `graphemes`, and `as_dicts()` for the CRF feature sequence |
| `GraphemeFeatures` | Frozen record per grapheme: `grapheme`, `span`, `index`, `position`, `prev`, `next`, `prev2`, `next2`, `is_vowel`, `is_consonant`, `is_front`, `is_back`, `candidates`, `top1_ipa`, `top1_cost`, `margin`, `n_candidates`, `confidence`, `script`, `code`, and `as_dict()` |

`margin` is `None` for a slot with one candidate. `as_dict()` returns a flat dict of scalars that `json.dumps` accepts, ready for [python-crfsuite](https://github.com/scrapinghub/python-crfsuite) or [sklearn-crfsuite](https://github.com/TeamHG-Memex/sklearn-crfsuite). The stability commitment covers these names, and the export adds no `LanguageSpec` field. [../engine/lattice.md](../engine/lattice.md#feature-export-for-a-learned-model) documents the export.

---
[← Language Registry](registry.md) · [Home](../index.md) · [Architecture →](../engine/architecture.md)
