# Architecture

## Package Layout

```
orthography2ipa/
├── __init__.py          # Public API — re-exports everything
├── types.py             # Core data types: LanguageSpec, Ancestor, AncestorRole
├── registry.py          # Language registry with lazy loading
├── phonetok.py          # Grapheme tokenizer + IPA beam search
├── distance.py          # Phonological distance metrics
│
├── # ── Language modules ─────────────────────────────────────────────────
├── en.py                # English
├── es.py                # Spanish (Castilian, Latin American, Rioplatense)
├── es_dialects.py       # Spanish dialects of Spain (Andalusian, etc.)
├── es_latam.py          # 20+ Latin American Spanish varieties
├── pt.py                # Portuguese (European + Brazilian standard)
├── pt_dialects.py       # European Portuguese regional dialects
├── pt_br_dialects.py    # Brazilian Portuguese regional dialects
├── fr.py                # French
├── it.py                # Italian
├── la.py                # Classical Latin
├── ...                  # (all other languages)
│
├── # ── Historical / pre-Roman / contact languages ───────────────────────
├── ine.py               # Proto-Indo-European
├── grc.py               # Ancient Greek
├── la_galloromance.py   # Gallo-Latin (ancestor of French/Occitan)
├── iberian_preroman.py  # Celtiberian, Iberian, Lusitanian, Tartessian, Basque
├── iberian_medieval.py  # Hispanic Vulgar Latin, Mozarabic, Andalusi Arabic
├── celtic.py            # Common Celtic, Celtiberian
├── germanic_historical.py  # Proto-Germanic, Gothic
├── phoenician.py        # Phoenician
│
├── # ── Dialect bundles ─────────────────────────────────────────────────
├── ca_dialects.py       # Catalan dialects + Aranese
├── eu_dialects.py       # Basque dialects
├── gl_dialects.py       # Galician dialects + Fala
├── barranquenho.py      # Barranquenho (Portuguese-Spanish contact)
├── rionorese.py         # Rionorês (Asturian-Leonese in Portugal)
├── guadramilese.py      # Guadramilês
└── mwl.py               # Mirandese
```

---

## Module Responsibilities

### `types.py`

Defines the immutable data model:

- `Grapheme2IPA = Dict[str, List[str]]` — orthographic key → list of IPA candidates
- `AllophoneMap = Dict[str, List[str]]` — phoneme → list of surface realisations
- `AncestorRole` — enum of relationship types (PARENT, SUBSTRATE, SUPERSTRATE, ADSTRATE, LEXIFIER, CREOLE_BASE)
- `Ancestor` — frozen dataclass linking a code, role, and weight
- `LanguageSpec` — frozen dataclass holding all phonological data for one variety

All types are **frozen** (immutable) to allow safe caching.

### `registry.py`

Manages the mapping from language codes to module paths and handles lazy loading:

- `_LANG_MODULES` — the central dispatch table (`code → module.path`)
- `get(code)` — resolves aliases, imports the module on demand, caches the `LanguageSpec`
- `available_codes()` — all registered codes
- `available_families()` — codes grouped by language family
- `_resolve_code()` — normalises ISO 639-3 → BCP-47 aliases

Lazy loading means importing `orthography2ipa` is essentially free; only requested languages are loaded.

### `phonetok.py`

A language-agnostic tokenizer that works entirely from a `LanguageSpec`:

- `_GraphemeTrie` — prefix trie built from `spec.graphemes` for O(k) maximal-munch matching
- `PhonetokTokenizer` — the main class; wraps the trie
- `Token` — immutable dataclass representing one tokenizer output unit
- `TokenKind` — enum: GRAPHEME, WHITESPACE, PUNCTUATION, DIGIT, UNKNOWN, BOS, EOS
- `IPAPath` — a scored candidate IPA transcription
- `tokenize(text)` — produces `List[Token]`
- `ipa_beam(text, beam_width)` — beam search over all IPA paths
- `ipa_expand(tokens, include_allophones)` — expand tokens into IPA paths with optional allophone substitution

### `distance.py`

Phonological distance metrics built on **phonematcher**'s 21-feature SPE/IPA system:

- `feature_vector(segment)` → 21-element float tuple
- `segment_distance(a, b)` → normalized [0,1] phonetic distance
- `inventory_distance(spec_a, spec_b)` → `InventoryDistance`
- `grapheme_divergence(spec_a, spec_b)` → `GraphemeDivergence`
- `allophone_overlap(spec_a, spec_b)` → Jaccard similarity float
- `phonological_distance(spec_a, spec_b)` → `PhonologicalDistance` (combined)
- `ancestry_similarity(spec_a, spec_b)` → float based on shared ancestors
- `full_distance(spec_a, spec_b)` → combined phonological + ancestry distance
- `pairwise_distances(specs, metric)` → N×N distance matrix

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

### Why maximal munch for tokenization?

Maximal munch (longest match) is the standard strategy for tokenization in languages with digraphs and multigraphs. Portuguese `lh` should be matched as a single unit, not as `l` + `h`. The trie ensures this happens in O(k) time where k is the length of the longest grapheme key.

### Why beam search for IPA expansion?

The combinatorial explosion from ambiguous graphemes (e.g., English `c` → /k/ or /s/) makes exhaustive enumeration impractical for longer words. Beam search gives the N most-canonical paths efficiently, where "canonical" means using the first (most common) IPA value for each grapheme.

### Why phonematcher for features?

phonematcher implements a well-tested 21-feature SPE/IPA system with linguistic feature weighting (major-class features weighted 7× heavier than minor features). This is more principled than an ad-hoc feature table. Our wrapper normalizes outputs to [0,1] and adds graceful fallback for unknown segments.

### Why lazy loading?

With 50+ language modules, eager loading would make `import orthography2ipa` slow and memory-heavy. Lazy loading means only the languages actually used in a session are loaded. The registry is a pure dictionary lookup; no disk I/O until `get()` is called.

---

## Extending the Package

See [Adding a Language](adding_a_language.md) for the full guide. The short version:

1. Create `orthography2ipa/languages/xx.py` with `GRAPHEMES_XX`, `ALLOPHONES_XX`, and a `SPECS` dict.
2. Add an entry to `_LANG_MODULES` in `registry.py`.
3. Run the test suite to verify the spec validates correctly.
