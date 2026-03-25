# Architecture

## Package Layout

```
orthography2ipa/
├── __init__.py          # Public API — re-exports everything
├── version.py           # VERSION_STR source of truth
├── types.py             # Core data types: LanguageSpec, Ancestor, AncestorRole, etc.
├── registry.py          # Language registry with lazy loading
├── json_loader.py       # JSON spec loading with inheritance resolution
├── phonetok.py          # Grapheme tokenizer + IPA beam search
├── distance.py          # Phonological distance metrics
├── feats.py             # 21-feature SPE/IPA distinctive-feature matrix
├── transforms.py        # IPA dialect transform system (Ibero-Romance)
├── script_distance.py   # Typological distance between writing systems
├── sandhi.py            # Cross-word-boundary phonological rule engine
├── lm.py                # Phoneme n-gram language model utilities
├── g2p_plugin.py        # Abstract G2P plugin interface
├── plugins/             # Concrete G2P plugin implementations (e.g. Arabic)
│
└── data/                # 308 JSON language spec files
    ├── SCHEMA.md        # JSON schema reference
    ├── en-GB.json
    ├── es-ES.json
    ├── pt-PT.json
    ├── pt-BR.json       # inherits from pt-PT via graphemes_base
    ├── de-DE.json
    ├── fr-FR.json
    ├── ...              # (all other languages/dialects)
    └── lexicons/        # Optional word lists per language
```

---

## Module Responsibilities

### `types.py`

Defines the immutable data model — `types.py:1-634`:

- `Grapheme2IPA = Dict[str, List[str]]` — orthographic key → list of IPA candidates — `types.py:20`
- `AllophoneMap = Dict[str, List[str]]` — phoneme → list of surface realisations — `types.py:23`
- `PositionalGrapheme2IPA` — grapheme → `{GraphemePosition: [IPA]}` — `types.py:26`
- `GraphemePosition` — enum of 21 positional contexts — `types.py:34`
- `AncestorRole` — enum of relationship types (PARENT, SUBSTRATE, etc.) — `types.py:142`
- `QualityTier` — data maturity enum (STUB, SKELETON, RESEARCH, PRODUCTION) — `types.py:174`
- `ScriptType` — writing system typology enum — `types.py:194`
- `LinguisticSource` — bibliographic reference dataclass — `types.py:258`
- `SandhiRule` — cross-word phonological rule dataclass — `types.py:300`
- `Ancestor` — frozen dataclass linking a code, role, and weight — `types.py:334`
- `LanguageSpec` — frozen dataclass holding all phonological data for one variety — `types.py:379`

All types are **frozen** (immutable) to allow safe caching.

### `registry.py`

Manages language code resolution and lazy loading — `registry.py:1-130`:

- `_ALIASES` — ISO 639-3 → BCP-47 alias table — `registry.py:18-40`
- `_resolve_code(code)` — normalises aliases using the table and optional `langcodes` library — `registry.py:49`
- `get(code)` — resolves aliases, loads JSON spec on demand, caches the `LanguageSpec` — `registry.py:68`
- `available_codes()` — all registered codes (from JSON files) — `registry.py:85`
- `available_families()` — codes grouped by language family — `registry.py:120`
- `get_plugin(code)` — return a G2P plugin for the code, if registered — `registry.py:111`

Lazy loading means importing `orthography2ipa` is essentially free; only requested languages are loaded.

### `json_loader.py`

Loads `LanguageSpec` objects from JSON files under `data/` — `json_loader.py:1-295`:

- `load_json_spec(code)` — load and resolve a single spec with inheritance — `json_loader.py:87`
- `load_all_json_specs()` — load all specs from the data directory — `json_loader.py:250`
- `available_json_codes()` — sorted list of all codes with JSON data files — `json_loader.py:270`
- `load_lexicon(code)` — load an optional word list for a language — `json_loader.py:275`

Inheritance is resolved via `graphemes_base`, `allophones_base`, and `positional_graphemes_base` fields in JSON.

### `phonetok.py`

A language-agnostic tokenizer that works entirely from a `LanguageSpec` — `phonetok.py:1-400+`:

- `TokenKind` — enum: GRAPHEME, WHITESPACE, PUNCTUATION, DIGIT, UNKNOWN, BOS, EOS — `phonetok.py:66`
- `Token` — immutable dataclass representing one tokenizer output unit — `phonetok.py:92`
- `IPAPath` — a scored candidate IPA transcription — `phonetok.py:124`
- `_GraphemeTrie` — prefix trie built from `spec.graphemes` for O(k) maximal-munch matching — `phonetok.py:188`
- `PhonetokTokenizer` — the main class; wraps the trie — `phonetok.py:225`
  - `tokenize(text)` — produces `List[Token]`
  - `ipa_beam(text, beam_width)` — beam search over all IPA paths
  - `ipa_expand(tokens, include_allophones)` — expand tokens into IPA paths with optional allophone substitution

### `distance.py`

Phonological distance metrics built on the 21-feature SPE/IPA system — `distance.py:1-850+`:

- `feature_vector(segment)` → 21-element float tuple — `distance.py:140`
- `feature_names()` → tuple of feature name strings — `distance.py:165`
- `segment_distance(a, b)` → normalized [0,1] phonetic distance — `distance.py:174`
- `inventory_distance(spec_a, spec_b)` → `InventoryDistance` — `distance.py:266`
- `grapheme_divergence(spec_a, spec_b)` → `GraphemeDivergence` — `distance.py:321`
- `allophone_overlap(spec_a, spec_b)` → Jaccard similarity float — `distance.py:371`
- `phonological_distance(spec_a, spec_b)` → `PhonologicalDistance` (combined) — `distance.py:404`
- `ancestry_similarity(spec_a, spec_b)` → float based on shared ancestors — `distance.py:558`
- `full_distance(spec_a, spec_b)` → combined phonological + ancestry distance — `distance.py:658`
- `pairwise_distances(specs, metric)` → N×N distance matrix — `distance.py:444`
- `tone_distance(spec_a, spec_b)` → tone inventory distance — `distance.py:690`
- `orthographic_distance(spec_a, spec_b)` → grapheme-level distance — `distance.py:715`
- `weighted_full_distance(spec_a, spec_b)` → `WeightedDistance` with component breakdown — `distance.py:767`
- `positional_divergence(spec_a, spec_b)` → positional grapheme divergence — `distance.py:816`

### `feats.py`

Distinctive-feature matrix for IPA phones — `feats.py:1-683`:

Adapted from [PyPhone](https://github.com/lingz/pyphone) (MIT). Encodes a 21-feature SPE/IPA system. Used internally by `distance.py`.

- `vectorize_phones(phones)` — convert IPA string to feature vector — `feats.py:470`
- `is_vowel_phone(phone)` — check if a phone is a vowel — `feats.py:568`
- `phonetic_distance(phone_a, phone_b)` — segment-level distance — `feats.py:582`

### `transforms.py`

IPA dialect transform system for Portuguese and Ibero-Romance — `transforms.py:1-1000+`:

- `IPARule` — single IPA rewrite rule — `transforms.py:56`
- `IPAChainShift` — ordered chain of vowel/consonant shifts — `transforms.py:79`
- `IPALexicalRule` — orthography-conditioned IPA rule — `transforms.py:119`
- `DialectTransform` — named bundle of rules for a dialect — `transforms.py:145`
- `debias_lisbon(ipa, ortho)` — de-bias eSpeak PT-PT output to neutral standard — `transforms.py:168`
- `apply_transform(ipa, profile, ortho)` — apply a dialect profile — `transforms.py:855`
- `available_profiles()` — list registered dialect profile names — `transforms.py:938`
- `load_clup_profile(path)` — load a CLUP dialect profile — `transforms.py:972`
- `DIALECT_PROFILES` — dict of built-in profiles (Northern PT, Galician, Leonese, etc.)

### `script_distance.py`

Typological distance between writing systems — `script_distance.py:1-250`:

- `ScriptFeatures` — typological feature bundle for a writing system — `script_distance.py:30`
- `SCRIPT_REGISTRY` — built-in registry of script feature bundles
- `script_distance(a, b)` → float distance between two `ScriptFeatures` — `script_distance.py:191`
- `script_distance_by_name(a, b)` → float distance by script name strings — `script_distance.py:245`

### `sandhi.py`

Cross-word-boundary phonological rule engine — `sandhi.py:1-77`:

- `SandhiEngine` — applies `SandhiRule` objects across word boundaries — `sandhi.py:32`

### `lm.py`

Phoneme n-gram language model utilities — `lm.py:1-116`:

- `phoneme_embeddings(spec)` — 21-feature vectors for all phonemes — `lm.py:22`
- `build_ngram_lm(words, spec, n)` — build n-gram LM over IPA sequences — `lm.py:49`
- `perplexity(lm, test_words, spec, n)` — evaluate perplexity — `lm.py:79`

### `g2p_plugin.py`

Abstract G2P plugin interface — `g2p_plugin.py:1-55`:

- `WordContext` — sentence context for sandhi/liaison — `g2p_plugin.py:29`
- `G2PPlugin` — abstract base class with `transcribe()` and `transcribe_word()` — `g2p_plugin.py:38`

Plugins are discovered via `importlib.metadata` entry points in the `orthography2ipa.g2p` group.

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
  └── Beam search over cartesian product of .ipa values
      │
      ▼
List[IPAPath]  (sorted by score, best first)
```

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

With 308 JSON data files, eager loading would make `import orthography2ipa` slow and memory-heavy. Lazy loading means only the languages actually used in a session are loaded. The registry is a pure dictionary lookup; no disk I/O until `get()` is called. — `registry.get` — `registry.py:68`

---

## Extending the Package

See [Adding a Language](adding_a_language.md) for the full guide. The short version:

1. Create `orthography2ipa/data/{code}.json` with the required fields (see `data/SCHEMA.md`).
2. For dialects, use `graphemes_base`/`allophones_base` to inherit from the parent.
3. Run the test suite to verify the spec validates correctly.
