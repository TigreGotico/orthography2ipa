
# orthography2ipa — Documentation Hub

**orthography2ipa** is a Python package providing linguistically motivated grapheme-to-IPA (International Phonetic Alphabet) mappings, allophone inventories, positional grapheme overrides, language ancestry modelling, and phonological distance metrics for 100+ languages and dialects.

It is designed for NLP engineers, TTS/ASR pipeline authors, and computational linguists who need accurate, citation-backed orthographic-to-phonemic conversion.

**Version**: `0.1.0` — `orthography2ipa/__init__.py:64`

---

## Quick Start

```python
import orthography2ipa

# Fetch a language spec (lazy-loaded from JSON)
en  = orthography2ipa.get("en-GB")   # British English
es  = orthography2ipa.get("es-ES")   # Castilian Spanish
pt  = orthography2ipa.get("pt-BR")   # Brazilian Portuguese

# Inspect grapheme → IPA mappings
en.graphemes["th"]     # ['θ', 'ð']
es.graphemes["ll"]     # ['ʎ', 'ʝ']
pt.graphemes["lh"]     # ['ʎ']

# Inspect allophone inventories
en.allophones["t"]     # ['t', 'tʰ', 'ɾ', 'ʔ', 't̚']
es.allophones["b"]     # ['b', 'β']

# List all supported codes
orthography2ipa.available_codes()

# Group by family
orthography2ipa.available_families()
```

---

## Install

```bash
pip install orthography2ipa
# or, in the NLP Workspace:
uv pip install -e orthography2ipa/
```

The only runtime dependency is **phonematcher** (installed automatically), which provides the 21-feature SPE/IPA distinctive-feature system used by the distance metrics.

---

## Supported Languages

The registry currently covers more than 100 codes spanning 12+ language families. Language data is stored as JSON files under `orthography2ipa/data/` and loaded on demand by `registry.get()` — `orthography2ipa/registry.py:41-55`.

### By Family (partial)

| Family | Example codes |
| :--- | :--- |
| **Romance** | `la`, `pt-PT`, `pt-BR`, `es-ES`, `es-AR`, `fr-FR`, `it-IT`, `ca`, `gl`, `oc`, `mwl`, `ast`, `an`, `ext` |
| **Germanic** | `en-GB`, `de-DE`, `nl-NL`, `sv`, `da`, `no` |
| **Slavic** | `ru`, `uk`, `pl`, `cs` |
| **Semitic** | `ar`, `arb`, `phn`, `xaa` |
| **Indo-Iranian** | `fa`, `fa-AF`, `hi` |
| **Sino-Tibetan** | `zh` |
| **Japonic** | `ja` |
| **Koreanic** | `ko` |
| **Basque (Isolate)** | `eu`, `eu-x-bizkaiera`, `eu-x-gipuzkera`, `eu-x-zuberera` |
| **Turkic** | `tr` |
| **Uralic** | `fi` |
| **Hellenic** | `el`, `grc` |
| **Pre-Roman Iberian** | `xce`, `xib`, `xlg`, `txr`, `xaq`, `cel`, `phn` |
| **Historical / Proto** | `ine`, `gem`, `got`, `la-x-hispania`, `la-x-gallia` |
| **Contact/Transition** | `ext-PT-x-barrancos` (Barranquenho), `ast-PT-x-rionor` (Rionorês), `mxi` (Mozarabic) |

For the complete table with all dialect sub-codes, see [registry.md](registry.md).

ISO 639-3 aliases are supported — `registry._resolve_code` — `orthography2ipa/registry.py:12-38`:

```python
orthography2ipa.get("por")  # → pt-PT
orthography2ipa.get("eng")  # → en-GB
orthography2ipa.get("spa")  # → es-ES
orthography2ipa.get("lat")  # → la
```

---

## Key Classes Table

| Class / Type | Module | Description |
| :--- | :--- | :--- |
| `LanguageSpec` | `orthography2ipa/types.py:214` | Frozen dataclass — complete phonological specification for one language/variety. Central data object of the entire package. |
| `Grapheme2IPA` | `orthography2ipa/types.py:20` | Type alias `Dict[str, List[str]]` — orthographic grapheme → IPA candidates (most common first). |
| `AllophoneMap` | `orthography2ipa/types.py:23` | Type alias `Dict[str, List[str]]` — phoneme → surface realisations. |
| `PositionalGrapheme2IPA` | `orthography2ipa/types.py:26` | Type alias — grapheme → `{GraphemePosition: [IPA]}` for context-sensitive mappings. |
| `GraphemePosition` | `orthography2ipa/types.py:34` | Enum of positional contexts: `WORD_INITIAL`, `WORD_FINAL`, `INTERVOCALIC`, `CODA`, `ONSET`, etc. |
| `AncestorRole` | `orthography2ipa/types.py:136` | Enum — `PARENT`, `SUBSTRATE`, `SUPERSTRATE`, `ADSTRATE`, `LEXIFIER`, `CREOLE_BASE`. |
| `Ancestor` | `orthography2ipa/types.py:168` | Frozen dataclass — one ancestry link: `code`, `role`, `weight`, `notes`. |
| `PhonetokTokenizer` | `orthography2ipa/phonetok.py:220` | Language-agnostic grapheme tokenizer with IPA beam search. Wraps a `LanguageSpec`. |
| `Token` | `orthography2ipa/phonetok.py:87` | Frozen dataclass — one tokenizer output unit: `kind`, `grapheme`, `ipa`, `position`, `length`. |
| `TokenKind` | `orthography2ipa/phonetok.py:61` | Enum — `GRAPHEME`, `WHITESPACE`, `PUNCTUATION`, `DIGIT`, `UNKNOWN`, `BOS`, `EOS`. |
| `IPAPath` | `orthography2ipa/phonetok.py:119` | Frozen dataclass — one scored IPA transcription candidate: `segments`, `score`, `.ipa` property. |
| `InventoryDistance` | `orthography2ipa/distance.py:216` | Frozen dataclass — result of `inventory_distance()`: `jaccard`, `feature_mean`, `size_a`, `size_b`, `shared`. |
| `GraphemeDivergence` | `orthography2ipa/distance.py:273` | Frozen dataclass — result of `grapheme_divergence()`: `shared_graphemes`, `total_graphemes`, `mean_ipa_distance`, `overlap_ratio`. |
| `PhonologicalDistance` | `orthography2ipa/distance.py:358` | Frozen dataclass — combined distance result: `inventory`, `grapheme`, `allophone_sim`, `combined`. |

---

## Key Functions Table

| Function | Module | Signature | Description |
| :--- | :--- | :--- | :--- |
| `get` | `orthography2ipa/registry.py:41` | `get(code: str) -> LanguageSpec` | Fetch (lazy-load and cache) a `LanguageSpec` by BCP-47 or ISO 639-3 code. |
| `available_codes` | `orthography2ipa/registry.py:58` | `() -> List[str]` | Sorted list of all registered language codes. |
| `available_families` | `orthography2ipa/registry.py:63` | `() -> Dict[str, List[str]]` | Codes grouped by language family. |
| `feature_vector` | `orthography2ipa/distance.py:131` | `(segment: str) -> FeatureVector` | 21-element distinctive-feature vector for an IPA segment. |
| `segment_distance` | `orthography2ipa/distance.py:165` | `(a: str, b: str) -> float` | Normalised [0,1] phonetic distance between two IPA segments. |
| `inventory_distance` | `orthography2ipa/distance.py:238` | `(spec_a, spec_b) -> InventoryDistance` | Compare phoneme inventories. |
| `grapheme_divergence` | `orthography2ipa/distance.py:293` | `(spec_a, spec_b) -> GraphemeDivergence` | How differently two languages map shared graphemes to IPA. |
| `allophone_overlap` | `orthography2ipa/distance.py:343` | `(spec_a, spec_b) -> float` | Jaccard similarity of allophone surface-form inventories. |
| `phonological_distance` | `orthography2ipa/distance.py:376` | `(spec_a, spec_b, …) -> PhonologicalDistance` | Combined weighted phonological distance. |
| `ancestry_similarity` | `orthography2ipa/distance.py:501` | `(spec_a, spec_b) -> float` | Ancestry-weighted phylogenetic similarity [0,1]. |
| `full_distance` | `orthography2ipa/distance.py:601` | `(spec_a, spec_b, …) -> float` | Phonological + ancestry combined distance. |
| `pairwise_distances` | `orthography2ipa/distance.py:416` | `(specs, metric) -> List[List[float]]` | N×N symmetric distance matrix. |
| `load_json_spec` | `orthography2ipa/json_loader.py:62` | `(code: str) -> LanguageSpec` | Load and resolve a single spec from its JSON file. |
| `load_all_json_specs` | `orthography2ipa/json_loader.py:160` | `() -> Dict[str, LanguageSpec]` | Load all specs from the data directory. |
| `available_json_codes` | `orthography2ipa/json_loader.py:180` | `() -> List[str]` | Sorted list of all codes with JSON data files. |

---

## LanguageSpec — Core Fields

Every `LanguageSpec` (`orthography2ipa/types.py:214`) carries:

| Field | Type | Description |
| :--- | :--- | :--- |
| `code` | `str` | BCP-47 or ISO 639 code (primary key) |
| `name` | `str` | Human-readable name |
| `family` | `str` | Language family |
| `script` | `str` | Primary writing script |
| `graphemes` | `Grapheme2IPA` | Orthographic grapheme → IPA candidates (context-free default) |
| `allophones` | `AllophoneMap` | Phoneme → surface realisations |
| `positional_graphemes` | `PositionalGrapheme2IPA` | Context-sensitive IPA overrides by `GraphemePosition` |
| `ancestors` | `Tuple[Ancestor, ...]` | Full ancestry specification |
| `parent` | `str \| None` | Shorthand for primary parent code |
| `glottolog_code` | `str \| None` | Optional Glottolog languoid identifier |
| `notes` | `str` | Free-form linguistic notes |

Key methods: `resolve_grapheme(grapheme, position)` — `types.py:334`; `get_ancestors(role)` — `types.py:399`; `has_positional_data()` — `types.py:378`.

---

## Documentation Files

| File | Description |
| :--- | :--- |
| [index.md](index.md) | This file — overview, install, supported languages, key classes |
| [getting_started.md](getting_started.md) | Step-by-step quickstart with code examples |
| [architecture.md](architecture.md) | Package structure, module responsibilities, design decisions |
| [data_model.md](data_model.md) | `LanguageSpec`, `Grapheme2IPA`, `AllophoneMap`, `Ancestor`, `AncestorRole` |
| [registry.md](registry.md) | Full language registry: all supported codes by family |
| [tokenizer.md](tokenizer.md) | `PhonetokTokenizer`, `Token`, `IPAPath`, beam search |
| [distance.md](distance.md) | All distance metrics with expected ranges |
| [ancestry.md](ancestry.md) | Ancestry system: roles, weights, phylogenetic distance |
| [positional_graphemes.md](positional_graphemes.md) | `GraphemePosition` enum, positional overrides, `resolve_grapheme` |
| [adding_a_language.md](adding_a_language.md) | Step-by-step guide to adding a new JSON language file |
| [linguistic_accuracy.md](linguistic_accuracy.md) | Data quality standards, IPA conventions, language-specific notes |
| [ipa_reference.md](ipa_reference.md) | IPA symbol reference with Unicode code points |
| [README.md](README.md) | Overview (mirrors docs hub structure) |

---

## Design Principles

1. **Linguistic accuracy over simplicity** — every mapping cites published phonological descriptions.
2. **Dialect depth** — standard varieties plus dozens of regional dialects with documented deviations.
3. **Structured ancestry** — `Ancestor` objects encode PARENT / SUBSTRATE / SUPERSTRATE / ADSTRATE / LEXIFIER / CREOLE_BASE relationships with weights, enabling phylogenetically-informed distances.
4. **Separation of concerns** — grapheme maps, allophone inventories, tokenization, and distance metrics are cleanly separated across `types.py`, `phonetok.py`, and `distance.py`.
5. **Lazy loading** — language JSON files are read on first `get()` call only; importing the package is essentially free. — `registry.get` — `orthography2ipa/registry.py:41-55`
6. **Immutability** — all data types are frozen dataclasses, enabling safe caching and thread sharing.
