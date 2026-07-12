# Adding a new Language

## Overview

All phonological data — graphemes, allophones, positional graphemes, ancestry,
sources — lives in standalone JSON files under `orthography2ipa/data/`, one per
language code. The engine is language-agnostic: adding a language means writing
cited data, never code. The field-by-field authoring reference is
[`SCHEMA.md`](../orthography2ipa/data/SCHEMA.md); this page is the walkthrough.

Two things a spec does **not** declare:

- **No `family` string.** Classification comes from the clade nodes above the
  spec in the ancestry graph — set `parent` and `family` derives itself. See
  [Classification](#classification-wire-it-into-the-clade-chain) below.
- **No engine hooks.** If a language needs behaviour the shared engine cannot
  express, that is a gap in the engine or in the spec vocabulary, not a reason
  for language-specific code.

---

## Architecture

```
orthography2ipa/
├── types.py          # Data types
├── json_loader.py    # JSON loading with inheritance resolution
├── registry.py       
├── data/
│   ├── SCHEMA.md     # JSON schema reference
│   ├── ine.json          # Proto-Indo-European
│   ├── la.json           # Classical Latin
│   ├── la-x-hispania.json
│   ├── la-x-gallia.json
│   ├── es-ES.json        # Castilian Spanish
│   ├── es-ES-x-andalusia-w.json  # inherits from es-ES
│   ├── fr-FR.json
│   ├── pt-PT.json
│   ├── pt-BR.json        # inherits from pt-PT
│   ├── it-IT.json
│   ├── gem.json          # Proto-Germanic
│   ├── goh.json          # Old High German
│   ├── enm.json          # Middle English
│   ├── en-GB.json
│   ├── de-DE.json
│   └── nl-NL.json
│   └── ...
```

---

## JSON Loader API

```python
from orthography2ipa.json_loader import (
    load_json_spec,
    load_all_json_specs,
    available_json_codes
)

# Load a single spec
spec = load_json_spec("es-ES")

# Load all specs
specs = load_all_json_specs()

# List available codes
codes = available_json_codes()  # ['de-DE', 'en-GB', 'es-ES', ...]

```

---

## Inheritance System

Many dialects share most of their phonological data with a parent variety. Instead of duplicating entire grapheme maps,
JSON files can inherit from a base spec using `*_base` fields:

```json
{
  "code": "es-ES-x-andalusia-w",
  "graphemes_base": "es-ES",
  "graphemes": {
    "c": [
      "k",
      "s",
      "θ"
    ],
    "ll": [
      "ʝ"
    ]
  },
  "allophones_base": "es-ES",
  "allophones": {
    "s": [
      "s",
      "h",
      "∅"
    ],
    "x": [
      "h"
    ]
  }
}
```

The loader resolves `es-ES` first, copies its graphemes, then overlays the four overridden entries. This replaces the
Python `{**GRAPHEMES_ES, ...}` pattern.

### Inheritance rules

1. Only explicitly listed entries override the base — everything else is inherited.
2. Inheritance chains are resolved recursively (A inherits B which inherits C).
3. Circular inheritance is detected and raises `ValueError`.
4. Each of `graphemes`, `allophones`, and `positional_graphemes` can independently inherit from different bases.

---

## Adding a New Language (JSON)

### Step 1: Create the JSON file

Create `orthography2ipa/data/{code}.json`:

```json
{
  "code": "xx-YY",
  "name": "Language Name",
  "script": "Latin",
  "graphemes": {
    "a": [
      "a"
    ],
    "ch": [
      "tʃ"
    ]
  },
  "allophones": {
    "a": [
      "a"
    ],
    "tʃ": [
      "tʃ"
    ]
  },
  "positional_graphemes": {
    "b": {
      "default": [
        "b"
      ],
      "intervocalic": [
        "β"
      ]
    }
  },
  "parent": "parent-code",
  "ancestors": [
    {
      "code": "parent-code",
      "role": "parent",
      "weight": 0.85,
      "notes": "Primary descent"
    }
  ],
  "notes": "Source: Author (year). Title."
}
```

### Step 2: Ensure parent exists

The parent language must have its own JSON file. If adding a dialect, ensure the standard variety is already in the
dataset. For historical languages, ensure the ancestral chain connects back to a proto-language.

### Classification: wire it into the clade chain

A family is a **clade node**: a spec whose JSON carries `"clade": true`, a
`name` (`"Ibero-Romance"`), and a `parent` pointing at the next clade up. It is
classification and nothing else — no graphemes, no allophones, never inherited
from, and excluded from `available_codes()` unless `include_clades=True`.

So a new language is classified by pointing its `parent` at the right node, and
`family` / `family_path` derive themselves:

```python
import orthography2ipa

orthography2ipa.get("pt-BR").family_path   # ('Indo-European', 'Italic', 'Romance', 'Ibero-Romance')
orthography2ipa.get("pt-BR").family        # 'Indo-European > Italic > Romance > Ibero-Romance'
```

If the clade the language belongs to has no node yet, add the node — do not
author a `family` string to route around the missing one. The one case where an
explicit `family` string is right is a grouping that is *not* a genetic clade:
creoles, constructed languages, isolates, unclassified languages.

### Metadata worth filling in

Beyond the phonology, a spec is the place to record what the language *is*:

| Field | Why it matters |
|---|---|
| `sources` | The citation bar for `research` tier — every mapping traceable to a published description |
| `orthography_standard` | The official spelling norm, where one exists: the primary authority for what a grapheme *is* |
| `location` | Representative point (lat/lon); feeds `geographic_distance` — most meaningful for region-anchored dialects |
| `timespan` | Attestation period; decays ancestry weights across time |
| `glottolog_code`, `wikidata_qid`, `phoible_id`, `wals_code`, `iso639_3` | Cross-references. `wikidata_qid` is the hub — one QID resolves the rest |
| `wikipedia`, `urls` | Human-readable references |

### Step 3: For dialects, use inheritance

If the language shares most phonological data with a parent:

```json
{
  "code": "xx-YY-x-dialect",
  "graphemes_base": "xx-YY",
  "graphemes": {
    "only": [
      "overrides"
    ]
  },
  "allophones_base": "xx-YY",
  "allophones": {
    "only": [
      "overrides"
    ]
  }
}
```

### Step 4: Run tests

```bash
uv run pytest tests/ -v
```

The test suite validates:

- All JSON files parse correctly
- Every spec has required fields (graphemes, allophones, name, script)
- Every `parent` field points to an existing spec
- Every PARENT-role ancestor exists in the dataset
- Linguistic accuracy for key languages (Spanish θ, English th, German Auslautverhärtung, etc.)

---

## Adding a lexicon overlay (optional)

When grapheme rules cannot reach production accuracy for a deep-orthography
language, ship a **lexicon**: a sidecar file
`orthography2ipa/data/lexicons/{code}.tsv` (`word<TAB>ipa`, UTF-8, NFC,
lowercase words, sorted, first-entry-wins), named by the language's resolved
code (e.g. `en-GB.tsv`). No JSON change and no new spec field are needed — the
file is discovered by convention and read lazily on first use. See
[`data_model.md`](data_model.md#lexicon-overlay-sidecar-word_exceptions-at-scale)
for the full contract (precedence: inline `word_exceptions` > lexicon > rules).

Rules to follow when adding one:

1. **Keep the pilot small and license-clean.** The bundled `en-GB.tsv` is a
   ~5k top-frequency slice of CMUdict (BSD-style, public domain), converted to
   broad IPA by `scripts/build_en_lexicon.py`. Cite the source in
   [`bibliography.md`](bibliography.md). Full production lexica (hundreds of
   thousands of entries) belong in a downstream package, not in this library.
2. **Validate.** Every entry must pass `lexicon.validate_lexicon_text` (correct
   `word<TAB>ipa` shape, NFC, lowercase word, IPA-characters-only, no
   duplicates); the shipped-data test enforces this over every `*.tsv`.
3. **Speak the spec's IPA convention.** Convert source pronunciations to the
   same broad IPA the language's `graphemes` use, so lexicon and rule output
   are comparable.
4. **Report the impact.** Regenerate the rules-only vs with-lexicon comparison
   with `python scripts/benchmark.py --lexicon-report` so
   [`lexicon_scoreboard.md`](lexicon_scoreboard.md) shows the overlay improves
   PER without masking rule regressions.

---

## Positional Grapheme Keys

| JSON key                  | Description                 | Example                                   |
|---------------------------|-----------------------------|-------------------------------------------|
| `default`                 | Default (any position)      | Spanish `"b": {"default": ["b"]}`         |
| `word_initial`            | Word-initial                | Portuguese `"s": {"word_initial": ["s"]}` |
| `word_final`              | Word-final                  | German `"d": {"word_final": ["t"]}`       |
| `intervocalic`            | Between vowels              | Spanish `"b": {"intervocalic": ["β"]}`    |
| `intervocalic_cross_word` | Between vowels across words | Portuguese liaison                        |
| `onset`                   | Syllable onset              | Portuguese `"l": {"onset": ["l"]}`        |
| `nucleus`                 | Generic syllable nucleus    | When stress not distinguished             |
| `nucleus_stressed`        | Stressed syllable nucleus   | Full vowel quality                        |
| `nucleus_unstressed`      | Unstressed syllable nucleus | Portuguese ⟨e⟩ → [ɨ]                     |
| `coda`                    | Syllable coda               | Brazilian `"l": {"coda": ["w"]}`          |
| `pretonic`                | Before stressed syllable    | Pretonic vowel reduction                  |
| `posttonic`               | After stressed syllable     | Posttonic vowel reduction                 |
| `before_vowel`            | Before any vowel            | Consonant allophony                       |
| `after_vowel`             | After any vowel             | Post-vocalic changes                      |
| `before_consonant`        | Before any consonant        | Pre-consonantal changes                   |
| `after_consonant`         | After any consonant         | Post-consonantal changes                  |
| `before_a` .. `before_u`  | Before specific vowel       | Velar softening contexts                  |
| `consonantal`             | Consonantal context         | Grapheme as consonant                     |
| `vocalic`                 | Vocalic context             | Grapheme as vowel                         |

---

## Ancestor Roles

| JSON value    | Description                                                |
|---------------|------------------------------------------------------------|
| `parent`      | Primary genetic descent (weight 0.7–1.0)                   |
| `substrate`   | Pre-existing population language (weight 0.05–0.30)        |
| `superstrate` | Dominant group language, later absorbed (weight 0.10–0.40) |
| `adstrate`    | Peer contact influence (weight 0.05–0.20)                  |
| `lexifier`    | Vocabulary source in creole (weight 0.50–0.80)             |
| `creole_base` | Grammar source in creole (weight 0.20–0.50)                |


---

**Navigation:** [Docs home](index.md) · [Getting started](getting_started.md) · [Architecture](architecture.md) · [Languages](languages/index.md) · [Scoreboard](scoreboard.md)

*Related: [Data model](data_model.md) · [Registry](registry.md) · [Quality tiers](quality_tiers.md) · [Ancestry](ancestry.md)*
