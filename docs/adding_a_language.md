# Adding a new Language

## Overview

Language phonological data (graphemes, allophones, positional graphemes, ancestry) has been extracted from Python
modules into standalone JSON files. This separation of data from code improves maintainability: linguistic data can be
reviewed, edited, and validated independently of the Python codebase.

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

Create `orthography2ipa/data/{family}/{code}.json`:

```json
{
  "code": "xx-YY",
  "name": "Language Name",
  "family": "FamilyName",
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
python -m unittest tests.test_json_loader -v
```

The test suite validates:

- All JSON files parse correctly
- Every spec has required fields (graphemes, allophones, name, family, script)
- Every `parent` field points to an existing spec
- Every PARENT-role ancestor exists in the dataset
- Linguistic accuracy for key languages (Spanish θ, English th, German Auslautverhärtung, etc.)

---

## Positional Grapheme Keys

| JSON key                  | Description                 | Example                                   |
|---------------------------|-----------------------------|-------------------------------------------|
| `default`                 | Default (any position)      | Spanish `"b": {"default": ["b"]}`         |
| `onset`                   | Syllable onset              | Portuguese `"l": {"onset": ["l"]}`        |
| `nucleus`                 | Syllable nucleus            | Vowel reduction                           |
| `coda`                    | Syllable coda               | Brazilian `"l": {"coda": ["w"]}`          |
| `word_initial`            | Word-initial                | Portuguese `"s": {"word_initial": ["s"]}` |
| `word_final`              | Word-final                  | German `"d": {"word_final": ["t"]}`       |
| `intervocalic`            | Between vowels              | Spanish `"b": {"intervocalic": ["β"]}`    |
| `intervocalic_cross_word` | Between vowels across words | Portuguese liaison                        |

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

