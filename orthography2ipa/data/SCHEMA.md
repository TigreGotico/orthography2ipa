# Language JSON Schema

Each `.json` file in this directory defines one or more `LanguageSpec` entries.
Files are named `{code}.json` where `code` is the primary BCP-47 language code.

## Schema

```json
{
  "code": "es-ES",
  "name": "Spanish (Castilian)",
  "family": "Romance",
  "script": "Latin",
  "graphemes_base": null,
  "graphemes": {
    "a": [
      "a"
    ],
    "ch": [
      "tʃ"
    ]
  },
  "allophones_base": null,
  "allophones": {
    "b": [
      "b",
      "β"
    ]
  },
  "positional_graphemes_base": null,
  "positional_graphemes": {
    "b": {
      "intervocalic": [
        "β"
      ]
    }
  },
  "parent": "la-x-hispania",
  "ancestors": [
    {
      "code": "la-x-hispania",
      "role": "parent",
      "weight": 0.80,
      "notes": "Primary descent from Hispanic Vulgar Latin"
    }
  ],
  "notes": "Peninsular Castilian with distinción."
}
```

## Fields

| Field                       | Type   | Required | Description                                  |
|-----------------------------|--------|----------|----------------------------------------------|
| `code`                      | string | yes      | BCP-47 or ISO 639 language code              |
| `name`                      | string | yes      | Human-readable language name                 |
| `family`                    | string | yes      | Language family                              |
| `script`                    | string | yes      | Primary writing script                       |
| `graphemes`                 | object | yes      | Grapheme → IPA mapping (`{str: [str]}`)      |
| `allophones`                | object | yes      | Phoneme → allophone mapping (`{str: [str]}`) |
| `positional_graphemes`      | object | no       | Position-dependent grapheme mappings         |
| `parent`                    | string | no       | Primary parent language code                 |
| `ancestors`                 | array  | no       | Full ancestry specification                  |
| `notes`                     | string | no       | Free-form notes and sources                  |
| `graphemes_base`            | string | no       | Code to inherit graphemes from               |
| `allophones_base`           | string | no       | Code to inherit allophones from              |
| `positional_graphemes_base` | string | no       | Code to inherit positional graphemes from    |

## Inheritance

The `*_base` fields support data inheritance. When set, the loader:

1. Loads the referenced spec's data for that field
2. Deep-merges the current file's data on top (overrides only)

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
    "z": [
      "s",
      "θ"
    ],
    "s": [
      "s",
      "h"
    ],
    "ll": [
      "ʝ"
    ]
  }
}
```

The loader resolves `es-ES` first, copies its graphemes, then overlays
the four overridden entries.

> To mark a deletion, when a grapheme is no longer valid or an allophone no longer present, it can be set to None
> explicitly to avoid inheritance

## Positional Grapheme Keys

Position keys in `positional_graphemes` use lowercase string values
matching the `GraphemePosition` enum:

| JSON key                    | Enum value                                 |
|-----------------------------|--------------------------------------------|
| `"pretonic"`                | `GraphemePosition.PRETONIC`                |
| `"posttonic"`               | `GraphemePosition.POSTTONIC`               |
| `"onset"`                   | `GraphemePosition.ONSET`                   |
| `"nucleus_stressed"`        | `GraphemePosition.NUCLEUS_STRESSED`        |
| `"nucleus_unstressed"`      | `GraphemePosition.NUCLEUS_UNSTRESSED`      |
| `"coda"`                    | `GraphemePosition.CODA`                    |
| `"word_initial"`            | `GraphemePosition.WORD_INITIAL`            |
| `"word_final"`              | `GraphemePosition.WORD_FINAL`              |
| `"intervocalic"`            | `GraphemePosition.INTERVOCALIC`            |
| `"intervocalic_cross_word"` | `GraphemePosition.INTERVOCALIC_CROSS_WORD` |

## Ancestor Role Values

| JSON value      | Enum value                 |
|-----------------|----------------------------|
| `"parent"`      | `AncestorRole.PARENT`      |
| `"substrate"`   | `AncestorRole.SUBSTRATE`   |
| `"superstrate"` | `AncestorRole.SUPERSTRATE` |
| `"adstrate"`    | `AncestorRole.ADSTRATE`    |
| `"lexifier"`    | `AncestorRole.LEXIFIER`    |
| `"creole_base"` | `AncestorRole.CREOLE_BASE` |

## Guidelines:

- under `"graphemes"` mark ONLY canonical phonemes, ordered from most common to less common phoneme
- if a grapheme value is exactly the same as their parent, don't redefine it, set `"graphemes_base"` instead
- when a parent grapheme is no longer valid or no longer present, set it explicitly to None to avoid inheritance
- under `"allophones"` map ALL canonical phonemes to their possible allophones, ordered from most common to less common
  phoneme realization
- if an allophone value is exactly the same as their parent, don't redefine it, set `"allophones_base"` instead
- when a parent allophone is no longer valid or no longer present, set it explicitly to None to avoid inheritance
- under `"positional_graphemes"` mark ALL context around ambiguous graphemes, ordered from most common to less common
  phoneme
- if a grapheme is unambiguous skip defining it in `"positional_graphemes"`
- if an allophone is predictable, use it in  `"positional_graphemes"`

## File Organisation

```
data/
├── SCHEMA.md  (this file)
├── es-ES.json
├── es-ES-x-andalusia-w.json
├── fr-FR.json
├── pt-PT.json
├── en-GB.json
├── de-DE.json
├── ru.json
├── eu.json
└── ...
```
