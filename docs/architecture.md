# Architecture

## Package Layout

```
orthography2ipa/
├── __init__.py              # Public API: the names in __all__
├── version.py               # VERSION_STR, bumped by the release workflow
├── types.py                 # LanguageSpec, AllophoneRule, StressRules, FIELD_INHERITANCE
├── json_loader.py           # Loads a spec JSON file and resolves its inheritance
├── schema.py                # Pydantic validation behind `orthography2ipa validate`
├── registry.py              # get(), resolve(), available_codes(), plugin discovery
├── g2p.py                   # G2P and transcribe(): text to IPA
├── phonetok.py              # Maximal-munch tokenizer, lattice and beam search
├── positional.py            # Positional grapheme contexts and grammatical endings
├── weights.py               # Weighted grapheme candidates
├── vowels.py                # Phonological classes of graphemes and segments
├── allophony.py             # allophone_rules compiled into a lattice rescorer
├── rescorer.py              # LatticeRescorer and RescoreContext
├── stress.py                # Syllabification and stress placement
├── tone.py                  # Tone-mark placement
├── sandhi.py                # Cross-word rules
├── sentence.py              # SentenceLattice, SentenceRescorer, WordContext
├── features.py              # Feature export for ML and CRF G2P
├── inventory.py             # Emission and phoneme inventories, TTS tokens
├── underspecification.py    # Where the spelling leaves a reading undetermined
├── lexicon.py               # Caller-supplied lexicon overlay
├── markup.py                # <phoneme> markup that forces a pronunciation
├── distance.py              # The relational distance metrics
├── feats.py                 # 21-feature SPE/IPA distinctive-feature matrix
├── script_distance.py       # Typological distance between writing systems
├── lattice_per.py           # Lattice-aware phone error rate
├── transforms.py            # IPA dialect transforms (Ibero-Romance)
├── lm.py                    # Phoneme n-gram language model utilities
├── plugins.py               # Pipeline stages, NormalizePlugin, SandhiPlugin
├── rescorer_plugin.py       # RescorerPlugin
├── stress_plugin.py         # StressPlugin
├── syllabifier_plugin.py    # SyllabifierPlugin
├── syllabifiers.py          # The bundled silabificador entry point
├── conformance.py           # Contract checks for plugins
├── exceptions.py            # Exception types
├── cli.py                   # The orthography2ipa command
└── data/
    ├── SCHEMA.md            # Every JSON key the loader reads
    ├── <code>.json          # One spec per language, dialect or clade node
    └── gold/                # Hand-built gold sets and correction overlays (not in the wheel)
```

---

## Module Responsibilities

### `types.py`

Defines the immutable data model:

- `Grapheme2IPA = Dict[str, List[str]]`: orthographic key → list of IPA candidates
- `AllophoneMap = Dict[str, List[str]]`: phoneme → list of surface realisations
- `PositionalGrapheme2IPA`: grapheme → `{GraphemePosition: [IPA]}`
- `GraphemePosition`: enum of 21 positional contexts
- `AncestorRole`: enum of relationship types (PARENT, SUBSTRATE, etc.)
- `QualityTier`: data maturity enum (STUB, SKELETON, RESEARCH, PRODUCTION)
- `ScriptType`: writing system typology enum
- `LinguisticSource`: bibliographic reference dataclass
- `SandhiRule`: cross-word phonological rule dataclass
- `Ancestor`: frozen dataclass linking a code, role, and weight
- `LanguageSpec`: frozen dataclass holding all phonological data for one variety

All types are **frozen** (immutable) to allow safe caching.

### `registry.py`

Manages language code resolution and lazy loading:

- `_ALIASES`: ISO 639-3 → BCP-47 alias table
- `_resolve_code(code)`: normalises aliases using the table and optional `langcodes` library
- `get(code)`: resolves aliases, loads JSON spec on demand, caches the `LanguageSpec`
- `available_codes()`: all registered codes (from JSON files)
- `available_families()`: codes grouped by language family

Lazy loading means importing `orthography2ipa` is essentially free; only requested languages are loaded.

### `json_loader.py`

Loads `LanguageSpec` objects from JSON files under `data/`:

- `load_json_spec(code)`: load and resolve a single spec with inheritance
- `load_all_json_specs()`: load all specs from the data directory
- `available_json_codes()`: sorted list of all codes with JSON data files

Inheritance is resolved via `graphemes_base`, `allophones_base`, and `positional_graphemes_base` fields in JSON.

### `phonetok.py`

A language-agnostic tokenizer that works entirely from a `LanguageSpec`:

- `TokenKind`: enum: GRAPHEME, WHITESPACE, PUNCTUATION, DIGIT, UNKNOWN, BOS, EOS
- `Token`: immutable dataclass representing one tokenizer output unit
- `IPAPath`: a scored candidate IPA transcription
- `_GraphemeTrie`: prefix trie built from `spec.graphemes` for O(k) maximal-munch matching
- `GraphemeContext`: a context-aware view over one GRAPHEME token: word-local neighbours (`prev`/`next`/`at`/`neighbors`), character `span`, and class predicates (`is_vowel`/`is_consonant`/`is_front`/`is_back`) delegating to `vowels.py`
- `TokenSequence`: an indexed view returned by `tokenize_with_context()` wrapping every GRAPHEME token in a `GraphemeContext`
- `PhonetokTokenizer`: the main class; wraps the trie
  - `tokenize(text)`: produces `List[Token]`
  - `tokenize_with_context(text)`: produces a `TokenSequence` of context-aware grapheme views
  - `ipa_beam(text, beam_width)`: beam search over all IPA paths
  - `ipa_lattice(text)` and `ipa_best(text)`: the ranked lattice and its best path

The context model (`GraphemeContext` / `TokenSequence`) is the shared substrate
of the pronunciation lattice and the downstream rescorer seam. It gives specialized phonemizers a single, accent-aware token
context: neighbour access, spans and phonological-class predicates: to build
on instead of re-rolling per-consumer index arithmetic and private vowel sets.

### `distance.py`

The relational axes: one function per question, never collapsed into a single
similarity number. Built on the 21-feature SPE/IPA system. See
[distance.md](distance.md) for the full catalogue and each axis's caveats.

Phonological:

- `feature_vector(segment)` → 21-element float tuple
- `feature_names()` → tuple of feature name strings
- `segment_distance(a, b)` → normalized [0,1] phonetic distance
- `inventory_distance(spec_a, spec_b)` → `InventoryDistance`
- `allophone_overlap(spec_a, spec_b)` → Jaccard similarity float
- `phonological_distance(spec_a, spec_b)` → `PhonologicalDistance` (combined)
- `tone_distance(spec_a, spec_b)` → tone-inventory distance
- `phoneme_coverage(spec_native, spec_target)` → asymmetric transfer coverage

Orthographic: reading vs spelling, which are inverses of each other:

- `grapheme_divergence(spec_a, spec_b)` → `GraphemeDivergence` (same text → same sounds?)
- `spelling_divergence(spec_a, spec_b)` → `SpellingDivergence` (same sounds → same spelling?)
- `positional_divergence(spec_a, spec_b)` → positional-grapheme divergence
- `orthographic_distance(spec_a, spec_b)` → grapheme divergence folded with script distance

Genealogical, temporal, geographic:

- `ancestry_similarity(spec_a, spec_b)` → float based on shared, time-decayed ancestors
- `temporal_distance(spec_a, spec_b)` → attestation-period distance
- `geographic_distance(spec_a, spec_b, normalize=True)` → great-circle distance, or `None` when either spec has no `location`

Combined (when a caller really does want one number):

- `full_distance(spec_a, spec_b)` → phonological + ancestry
- `weighted_full_distance(spec_a, spec_b)` → `WeightedDistance` with per-component breakdown
- `pairwise_distances(specs, metric)` → N×N distance matrix

### `feats.py`

Distinctive-feature matrix for IPA phones:

Adapted from [PyPhone](https://github.com/lingz/pyphone) (MIT). Encodes a 21-feature SPE/IPA system. Used internally by `distance.py`.

- `vectorize_phones(phones)`: convert IPA string to feature vector
- `is_vowel_phone(phone)`: check if a phone is a vowel
- `phonetic_distance(phone_a, phone_b)`: segment-level distance

### `transforms.py`

IPA dialect transform system for Portuguese and Ibero-Romance:

- `IPARule`: single IPA rewrite rule
- `IPAChainShift`: ordered chain of vowel/consonant shifts
- `IPALexicalRule`: orthography-conditioned IPA rule
- `DialectTransform`: named bundle of rules for a dialect
- `debias_lisbon(ipa, ortho)`: de-bias eSpeak PT-PT output to neutral standard
- `apply_transform(ipa, profile, ortho)`: apply a dialect profile
- `available_profiles()`: list registered dialect profile names
- `load_clup_profile(path)`: load a CLUP dialect profile
- `DIALECT_PROFILES`: dict of built-in profiles (Northern PT, Galician, Leonese, etc.)

### `script_distance.py`

Typological distance between writing systems:

- `ScriptFeatures`: typological feature bundle for a writing system
- `SCRIPT_REGISTRY`: built-in registry of script feature bundles
- `script_distance(a, b)` → float distance between two `ScriptFeatures`
- `script_distance_by_name(a, b)` → float distance by script name strings

### `sandhi.py`

Cross-word-boundary phonological rule engine:

- `SandhiEngine`: applies `SandhiRule` objects across word boundaries

### `lm.py`

Phoneme n-gram language model utilities:

- `phoneme_embeddings(spec)`: 21-feature vectors for all phonemes
- `build_ngram_lm(words, spec, n)`: build n-gram LM over IPA sequences
- `perplexity(lm, test_words, spec, n)`: evaluate perplexity

### Downstream engines

orthography2ipa is not an engine plugin host. Nothing here discovers or calls a
"G2P plugin", and the abstract base class that once implied otherwise is gone.

Rich, language-specific engines: **arbtok** (Arabic), **tugaphone** (Portuguese): are **consumers** of this library. They read its spec data, drive its lattice and
layer their own rescorers on top. That is the opposite direction from a plugin,
and conflating the two is what made "the plugin system" impossible to reason
about.

What *is* pluggable is a **step**: see `syllabifier_plugin.py` and
`rescorer_plugin.py`, and the contracts in `conformance.py`.

`WordContext`: the cross-word context an engine passes down: lives in
`sentence.py`, with the rest of the cross-word machinery.


### `syllabifier_plugin.py`

Abstract interface for per-language syllabifiers:

- `SyllabifierPlugin`: abstract base class with `syllabify(word, lang)`, `language_codes`, and `priority`

The bundled `stress.syllabify` is a vowel-group splitter. It maximises the onset; a spec that sets `constrain_onsets` maximises it only as far as the language licenses — the shapes in `_OnsetJudge`, read off the spec's own grapheme→IPA table through the sonority scale in `vowels.py`, under a spec-declared `stress.max_onset` cap where one exists. The shapes are calibrated on Germanic and Romance, so the flag is opt-in: a language whose onset inventory exceeds them (Modern Greek ⟨σμ κτ πτ γν μν βγ βδ⟩ all begin words and never split) leaves it off and gets the unconstrained split. The flag is inherited along the `graphemes_base` edge, so a variety that pulls in a constrained table syllabifies it the same way its base does. Languages with a real syllabifier ship it as a plugin (e.g. `silabificador` for Portuguese) and stress detection picks it up automatically.

Writing the mark needs a second division, of the TRANSCRIPTION rather than the spelling: the mark goes before the stressed syllable, so where that syllable begins is what decides its position. `stress.syllabify_for_mark` divides the IPA with the same maximal-onset-constrained reasoning, through `_IpaOnsetJudge` — the same licit shapes, read off IPA segments instead of graphemes, plus every rise onto a glide (the shapes above refuse an obstruent + /j/ onset on continental Germanic evidence that is a morpheme boundary, and a transcription shows no boundaries). Nothing there is read off a grapheme table, so `constrain_onsets` does not gate it. The spec's `stress.ipa_diphthongs`, or `stress.diphthongs` where it declares none, decide which vowel sequences are one nucleus, and a declared `stress.max_onset` caps the onset.

The shapes are calibrated on Germanic, Slavic and Romance, so a language outside that calibration says so itself, in the same two ways the orthographic side already needed. `stress.onset_clusters` names the language's own complex onsets and then decides all of them: Ibero-Romance declares its obstruent + liquid inventory, which has no /s/ + stop in it, so *castigo* is cas-ti-go where the sibilant appendix would otherwise have made it ca-sti-go. `stress.constrain_mark_onsets` turns the judgement off for a language whose onsets the shapes get wrong and whose inventory is not written down yet — Greek, whose ⟨σμ κτ πτ⟩ begin words for the same reason it leaves `constrain_onsets` off, and Khmer, whose subscript consonants make onsets no sonority scale predicts. The mark then falls where the vowel groups put it.

A quantity-sensitive caller has already divided the transcription — that division is what its weights were read off — and passes it to `apply_stress_mark` as `ipa_syllables`, which is then used verbatim.

Plugins are discovered lazily via `importlib.metadata` entry points in the `orthography2ipa.syllabify` group: `registry._discover_syllabifiers`. Discovery runs once, on first call to `registry.get_syllabifier(code)`, and the result is cached at module scope. The package declares one entry point of its own, `silabificador`, in `pyproject.toml`. It loads only when the `silabificador` package is installed (the `portuguese` extra). With no syllabifier installed, `get_syllabifier()` returns `None` for every code.

When several plugins claim the same language code, the one with the highest `priority` wins (default `50`).

A downstream package registers a syllabifier by declaring the entry point in its own `pyproject.toml`:

```toml
[project.entry-points."orthography2ipa.syllabify"]
silabificador = "silabificador.plugin:PortugueseSyllabifier"
```

where `PortugueseSyllabifier` implements `SyllabifierPlugin` and declares `language_codes = ["pt-PT", "pt-BR"]`.

### `cli.py`

Command-line interface:

- `main(argv)`: entry point registered as `[project.scripts] orthography2ipa`
- Subcommands: `list`, `info`, `transcribe`, `distance`, `validate` ([reference/cli.md](reference/cli.md))
- All subcommands support `--json` for machine-readable output
- Imports are deferred to subcommand handlers for fast `--help` / `--version`

---

## Data Flow

```
User text input
      │
      ▼
PhonetokTokenizer.tokenize()
  ├── Trie lookup (maximal munch) → GRAPHEME tokens
  ├── Regex matching → WHITESPACE, PUNCTUATION, DIGIT
  └── Fallback → UNKNOWN tokens
      │
      ▼
List[Token]  (each with .grapheme and .ipa tuple)
      │
      ▼
PhonetokTokenizer.ipa_beam()
  ├── Resolve branches (positional + weight −log P)
  ├── Rescore (optional)  → re-cost each slot given its neighbours
  └── Beam search over cartesian product of the (rescored) slot candidates
      │
      ▼
List[IPAPath]  (sorted by score, best first)
```

The **rescorer** stage is the downstream-enablement seam: it runs after
positional/weight resolution and before beam path selection, re-costing
each grapheme slot as a pure function of the slot and its context. A
downstream rule cascade: a sun-letter assimilation, a silent-`e` rule: can be expressed as a rescorer over the shared lattice instead of a forked
tokenizer, when the rule is a context-conditioned choice among the
candidates the lattice already carries. See
[Rescoring the lattice](lattice.md#rescoring-the-lattice) and
[Refine or fork?](lattice.md#refine-the-lattice-or-fork-the-tokenizer) for
when each approach fits. Absent a rescorer, the pipeline is byte-identical.

The **allophony** stage is the built-in rescorer: a spec's declarative
`allophone_rules` (post-lexical `phoneme → surface` rewrites: final
devoicing, place assimilation, reduction, flapping) compile into an
`AllophoneRescorer` (`allophony.py`) the **engine** appends after any user
rescorer. In the full engine (`G2P`), the ordered stages are:

```
normalize → tokenize → select (positional + weights)
          → rescore (user rescorer(s) → allophony) → beam select
          → stress marks → sandhi → dialect transform
```

Allophony sits after phoneme selection and before stress/sandhi (it is the
phoneme-lattice → allophone-lattice stage), and needs the engine's stress
context, so: like sandhi and stress: it does not run on the standalone
tokenizer path. It is a no-op for any spec that declares no `allophone_rules`
(all shipped specs bar the Catalan pilots), keeping the default path
byte-identical. See [Allophony](allophony.md).

---

## Design Decisions

### Why frozen dataclasses?

`LanguageSpec`, `Ancestor`, `Token`, and `IPAPath` are all frozen. This ensures they can be safely shared across threads, cached with `lru_cache`, and used as dictionary keys or set members without unexpected mutation.

### Why JSON data files?

Language data was migrated from Python modules to JSON to separate linguistic data from code. JSON files can be reviewed, edited, and validated independently. Inheritance (`graphemes_base`, etc.) replaces Python `{**BASE, ...}` merge patterns.

### Why maximal munch for tokenization?

Maximal munch (longest match) is the standard strategy for tokenization in languages with digraphs and multigraphs. Portuguese `lh` should be matched as a single unit, not as `l` + `h`. The trie ensures this happens in O(k) time where k is the length of the longest grapheme key.

### Why beam search for IPA expansion?

The combinatorial explosion from ambiguous graphemes (e.g., English `c` → /k/ or /s/) makes exhaustive enumeration impractical for longer words. Beam search gives the N most-canonical paths efficiently, where "canonical" means using the first (most common) IPA value for each grapheme.

### Why lazy loading?

With hundreds of JSON data files, eager loading would make `import orthography2ipa` slow and memory-heavy. Lazy loading means only the languages actually used in a session are loaded. The registry is a pure dictionary lookup; no disk I/O until `get()` is called.: `registry.get`

---

## Extending the Package

See [Adding a Language](adding_a_language.md) for the full guide. The short version:

1. Create `orthography2ipa/data/{code}.json` with the required fields (see `data/SCHEMA.md`).
2. For dialects, use `graphemes_base`/`allophones_base` to inherit from the parent.
3. Run the test suite to verify the spec validates correctly.

---
[← Getting Started](getting_started.md) · [Home](index.md) · [Data Model →](data_model.md)
