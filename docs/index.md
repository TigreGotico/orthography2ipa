
# orthography2ipa — Documentation Hub

**orthography2ipa** is a Python package providing linguistically motivated grapheme-to-IPA (International Phonetic Alphabet) mappings, allophone inventories, positional grapheme overrides, language ancestry modelling, and phonological distance metrics for 100+ languages and dialects.

It is designed for NLP engineers, TTS/ASR pipeline authors, and computational linguists who need accurate, citation-backed orthographic-to-phonemic conversion.

**Version**: `0.2.0a1` — `orthography2ipa/version.py:1-10`

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

The registry currently covers 308 language/dialect codes spanning 12+ language families. Language data is stored as JSON files under `orthography2ipa/data/` and loaded on demand by `registry.get()` — `orthography2ipa/registry.py:68-82`.

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

ISO 639-3 aliases are supported — `registry._resolve_code` — `orthography2ipa/registry.py:49-65`:

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
| `LanguageSpec` | `orthography2ipa/types.py:379` | Frozen dataclass — complete phonological specification for one language/variety. Central data object of the entire package. |
| `Grapheme2IPA` | `orthography2ipa/types.py:20` | Type alias `Dict[str, List[str]]` — orthographic grapheme → IPA candidates (most common first). |
| `AllophoneMap` | `orthography2ipa/types.py:23` | Type alias `Dict[str, List[str]]` — phoneme → surface realisations. |
| `PositionalGrapheme2IPA` | `orthography2ipa/types.py:26` | Type alias — grapheme → `{GraphemePosition: [IPA]}` for context-sensitive mappings. |
| `GraphemePosition` | `orthography2ipa/types.py:34` | Enum of 21 positional contexts: `WORD_INITIAL`, `WORD_FINAL`, `INTERVOCALIC`, `CODA`, `ONSET`, `BEFORE_VOWEL`, etc. |
| `AncestorRole` | `orthography2ipa/types.py:142` | Enum — `PARENT`, `SUBSTRATE`, `SUPERSTRATE`, `ADSTRATE`, `LEXIFIER`, `CREOLE_BASE`. |
| `QualityTier` | `orthography2ipa/types.py:174` | Enum — `STUB`, `SKELETON`, `RESEARCH`, `PRODUCTION`. |
| `ScriptType` | `orthography2ipa/types.py:194` | Enum — `ALPHABET`, `ABJAD`, `ABUGIDA`, `SYLLABARY`, `LOGOGRAPHIC`, `FEATURAL`, `MIXED`, `RECONSTRUCTION`. |
| `LinguisticSource` | `orthography2ipa/types.py:258` | Frozen dataclass — bibliographic reference: `id`, `author`, `year`, `title`, `url`, etc. |
| `SandhiRule` | `orthography2ipa/types.py:300` | Frozen dataclass — cross-word phonological rule: `id`, `name`, `left_context`, `right_context`, `transform`. |
| `Ancestor` | `orthography2ipa/types.py:334` | Frozen dataclass — one ancestry link: `code`, `role`, `weight`, `notes`. |
| `WeightedDistance` | `orthography2ipa/types.py:230` | Frozen dataclass — result of `weighted_full_distance()` with all component scores. |
| `PhonetokTokenizer` | `orthography2ipa/phonetok.py:225` | Language-agnostic grapheme tokenizer with IPA beam search. Wraps a `LanguageSpec`. |
| `Token` | `orthography2ipa/phonetok.py:92` | Frozen dataclass — one tokenizer output unit: `kind`, `grapheme`, `ipa`, `position`, `length`. |
| `TokenKind` | `orthography2ipa/phonetok.py:66` | Enum — `GRAPHEME`, `WHITESPACE`, `PUNCTUATION`, `DIGIT`, `UNKNOWN`, `BOS`, `EOS`. |
| `IPAPath` | `orthography2ipa/phonetok.py:124` | Frozen dataclass — one scored IPA transcription candidate: `segments`, `score`, `.ipa` property. |
| `InventoryDistance` | `orthography2ipa/distance.py:244` | Frozen dataclass — result of `inventory_distance()`: `jaccard`, `feature_mean`, `size_a`, `size_b`, `shared`. |
| `GraphemeDivergence` | `orthography2ipa/distance.py:302` | Frozen dataclass — result of `grapheme_divergence()`: `shared_graphemes`, `total_graphemes`, `mean_ipa_distance`, `overlap_ratio`. |
| `PhonologicalDistance` | `orthography2ipa/distance.py:387` | Frozen dataclass — combined distance result: `inventory`, `grapheme`, `allophone_sim`, `combined`. |
| `ScriptFeatures` | `orthography2ipa/script_distance.py:30` | Frozen dataclass — typological feature bundle for a writing system. |
| `IPARule` | `orthography2ipa/transforms.py:56` | Dataclass — single IPA rewrite rule with optional context. |
| `DialectTransform` | `orthography2ipa/transforms.py:145` | Dataclass — named bundle of IPA rules for a dialect profile. |
| `SandhiEngine` | `orthography2ipa/sandhi.py:32` | Applies `SandhiRule` objects across word boundaries in an IPA stream. |
| `G2PPlugin` | `orthography2ipa/g2p_plugin.py:38` | Abstract base class for language-specific G2P plugins. |

---

## Key Functions Table

| Function | Module | Signature | Description |
| :--- | :--- | :--- | :--- |
| `get` | `orthography2ipa/registry.py:68` | `get(code: str) -> LanguageSpec` | Fetch (lazy-load and cache) a `LanguageSpec` by BCP-47 or ISO 639-3 code. |
| `available_codes` | `orthography2ipa/registry.py:85` | `() -> List[str]` | Sorted list of all registered language codes. |
| `available_families` | `orthography2ipa/registry.py:120` | `() -> Dict[str, List[str]]` | Codes grouped by language family. |
| `get_plugin` | `orthography2ipa/registry.py:111` | `(code: str) -> Optional[G2PPlugin]` | Return G2P plugin for code, if registered. |
| `feature_vector` | `orthography2ipa/distance.py:140` | `(segment: str) -> FeatureVector` | 21-element distinctive-feature vector for an IPA segment. |
| `feature_names` | `orthography2ipa/distance.py:165` | `() -> Tuple[str, ...]` | Names of the 21 distinctive features. |
| `segment_distance` | `orthography2ipa/distance.py:174` | `(a: str, b: str) -> float` | Normalised [0,1] phonetic distance between two IPA segments. |
| `inventory_distance` | `orthography2ipa/distance.py:266` | `(spec_a, spec_b) -> InventoryDistance` | Compare phoneme inventories. |
| `grapheme_divergence` | `orthography2ipa/distance.py:321` | `(spec_a, spec_b) -> GraphemeDivergence` | How differently two languages map shared graphemes to IPA. |
| `allophone_overlap` | `orthography2ipa/distance.py:371` | `(spec_a, spec_b) -> float` | Jaccard similarity of allophone surface-form inventories. |
| `phonological_distance` | `orthography2ipa/distance.py:404` | `(spec_a, spec_b, …) -> PhonologicalDistance` | Combined weighted phonological distance. |
| `ancestry_similarity` | `orthography2ipa/distance.py:558` | `(spec_a, spec_b) -> float` | Ancestry-weighted phylogenetic similarity [0,1]. |
| `full_distance` | `orthography2ipa/distance.py:658` | `(spec_a, spec_b, …) -> float` | Phonological + ancestry combined distance. |
| `pairwise_distances` | `orthography2ipa/distance.py:444` | `(specs, metric) -> List[List[float]]` | N×N symmetric distance matrix. |
| `tone_distance` | `orthography2ipa/distance.py:690` | `(spec_a, spec_b) -> float` | Tone inventory distance. |
| `orthographic_distance` | `orthography2ipa/distance.py:715` | `(spec_a, spec_b) -> float` | Grapheme-level orthographic distance. |
| `weighted_full_distance` | `orthography2ipa/distance.py:767` | `(spec_a, spec_b, …) -> WeightedDistance` | Full distance with component breakdown. |
| `positional_divergence` | `orthography2ipa/distance.py:816` | `(spec_a, spec_b) -> float` | Positional grapheme divergence. |
| `load_json_spec` | `orthography2ipa/json_loader.py:87` | `(code: str) -> LanguageSpec` | Load and resolve a single spec from its JSON file. |
| `load_all_json_specs` | `orthography2ipa/json_loader.py:250` | `() -> Dict[str, LanguageSpec]` | Load all specs from the data directory. |
| `available_json_codes` | `orthography2ipa/json_loader.py:270` | `() -> List[str]` | Sorted list of all codes with JSON data files. |
| `load_lexicon` | `orthography2ipa/json_loader.py:275` | `(code: str) -> Optional[Dict[str, str]]` | Load optional word list for a language. |
| `apply_transform` | `orthography2ipa/transforms.py:855` | `(ipa, profile, ortho) -> str` | Apply a dialect transform profile to IPA. |
| `debias_lisbon` | `orthography2ipa/transforms.py:168` | `(ipa, ortho) -> str` | De-bias eSpeak PT-PT output to neutral standard. |
| `script_distance_by_name` | `orthography2ipa/script_distance.py:245` | `(a: str, b: str) -> float` | Typological distance between writing systems by name. |

---

## LanguageSpec — Core Fields

Every `LanguageSpec` (`orthography2ipa/types.py:379`) carries:

| Field | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `code` | `str` | *required* | BCP-47 or ISO 639 code (primary key) |
| `name` | `str` | *required* | Human-readable name |
| `family` | `str` | *required* | Language family |
| `script` | `str` | *required* | Primary writing script |
| `graphemes` | `Grapheme2IPA` | *required* | Orthographic grapheme → IPA candidates (context-free default) |
| `allophones` | `AllophoneMap` | *required* | Phoneme → surface realisations |
| `parent` | `str \| None` | `None` | Shorthand for primary parent code |
| `ancestors` | `Tuple[Ancestor, ...]` | `()` | Full ancestry specification |
| `positional_graphemes` | `PositionalGrapheme2IPA` | `None` → `{}` | Context-sensitive IPA overrides by `GraphemePosition` |
| `glottolog_code` | `str \| None` | `None` | Glottolog languoid identifier |
| `notes` | `str` | `""` | Free-form linguistic notes |
| `quality` | `QualityTier` | `RESEARCH` | Data maturity tier |
| `script_type` | `ScriptType` | `ALPHABET` | Typological classification of writing system |
| `inherent_vowel` | `str \| None` | `None` | For abugidas — default vowel (e.g. `"ə"` for Hindi) |
| `iso639_3` | `str \| None` | `None` | ISO 639-3 code for PHOIBLE/Glottolog cross-ref |
| `sandhi_rules` | `Tuple[SandhiRule, ...]` | `()` | Cross-word-boundary phonological rules |
| `tone_inventory` | `Dict[str, str] \| None` | `None` | IPA tone mark → label mapping |
| `sources` | `Tuple[LinguisticSource, ...]` | `()` | Bibliographic references |
| `wikipedia` | `Tuple[str, ...]` | `()` | Wikipedia article URLs |

Key methods: `resolve_grapheme(grapheme, position)` — `types.py:536`; `get_ancestors(role)` — `types.py:601`; `has_positional_data()` — `types.py:580`.

---

## Documentation Files

| File | Description |
| :--- | :--- |
| [index.md](index.md) | This file — overview, install, supported languages, key classes |
| [getting_started.md](getting_started.md) | Step-by-step quickstart with code examples |
| [architecture.md](architecture.md) | Package structure, all module responsibilities, design decisions |
| [data_model.md](data_model.md) | `LanguageSpec`, `Grapheme2IPA`, `AllophoneMap`, `Ancestor`, `AncestorRole`, `QualityTier`, `ScriptType` |
| [registry.md](registry.md) | Full language registry: all supported codes by family |
| [tokenizer.md](tokenizer.md) | `PhonetokTokenizer`, `Token`, `IPAPath`, beam search |
| [distance.md](distance.md) | All distance metrics with expected ranges |
| [ancestry.md](ancestry.md) | Ancestry system: roles, weights, phylogenetic distance |
| [positional_graphemes.md](positional_graphemes.md) | `GraphemePosition` enum (21 values), positional overrides, `resolve_grapheme` |
| [adding_a_language.md](adding_a_language.md) | Step-by-step guide to adding a new JSON language file |
| [linguistic_accuracy.md](linguistic_accuracy.md) | Data quality standards, IPA conventions, language-specific notes |
| [ipa_reference.md](ipa_reference.md) | IPA symbol reference with Unicode code points |
| [bibliography.md](bibliography.md) | `LinguisticSource` dataclass, citation management |
| [README.md](README.md) | Overview (mirrors docs hub structure) |
| [languages/](languages/index.md) | Per-language phonology documentation |

---

## Design Principles

1. **Linguistic accuracy over simplicity** — every mapping cites published phonological descriptions.
2. **Dialect depth** — standard varieties plus dozens of regional dialects with documented deviations.
3. **Structured ancestry** — `Ancestor` objects encode PARENT / SUBSTRATE / SUPERSTRATE / ADSTRATE / LEXIFIER / CREOLE_BASE relationships with weights, enabling phylogenetically-informed distances.
4. **Separation of concerns** — grapheme maps, allophone inventories, tokenization, and distance metrics are cleanly separated across `types.py`, `phonetok.py`, and `distance.py`.
5. **Lazy loading** — language JSON files are read on first `get()` call only; importing the package is essentially free. — `registry.get` — `orthography2ipa/registry.py:68-82`
6. **Immutability** — all data types are frozen dataclasses, enabling safe caching and thread sharing.
