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
| `quality`                   | string | no       | Data maturity: `"stub"`, `"skeleton"`, `"research"`, `"production"` (default: `"research"`) |
| `script_type`               | string | no       | Script typology: `"alphabet"`, `"abjad"`, `"abugida"`, `"syllabary"`, `"logographic"`, `"featural"`, `"mixed"`, `"reconstruction"` (default: `"alphabet"`) |
| `inherent_vowel`            | string | no       | For abugidas: vowel assumed when no vowel mark (e.g. `"ə"`) |
| `iso639_3`                  | string | no       | ISO 639-3 three-letter code for cross-referencing |
| `sandhi_rules`              | array  | no       | Cross-word-boundary phonological rules       |
| `tone_inventory`            | object | no       | IPA tone mark → label (e.g. `{"˥": "high"}`) |
| `sources`                   | array  | no       | Bibliographic references (see Sources Schema below) |
| `glottolog_code`            | string | no       | Glottolog languoid code (e.g. `"cast1244"`)  |
| `wikipedia`                 | array  | no       | Wikipedia article URLs (`https://<lang>.wikipedia.org/wiki/…`) |
| `urls`                      | array  | no       | Other reference URLs (Glottolog, Ethnologue, dialect articles, …) |
| `timespan`                  | object | no       | Attestation period `{"start_year": int, "end_year": int\|null}` |
| `lexicon_csv`               | string | no       | Path (relative to `data/`) of a bundled IPA lexicon CSV |

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

## Sandhi Rule Schema

```json
{
  "sandhi_rules": [
    {
      "id": "FR_LIAISON_Z",
      "name": "z-liaison",
      "left_context": "z$",
      "right_context": "^[aeiouɛɔɑãɛ̃ɔ̃]",
      "transform": "z‿",
      "obligatory": true,
      "notes": "les amis → /lez‿ami/"
    }
  ]
}
```

| Sandhi Field   | Type   | Required | Description                          |
|----------------|--------|----------|--------------------------------------|
| `id`           | string | yes      | Unique rule identifier               |
| `name`         | string | yes      | Human-readable name                  |
| `left_context` | string | yes      | Regex on word-final IPA              |
| `right_context`| string | yes      | Regex on next-word-initial IPA       |
| `transform`    | string | yes      | Replacement pattern                  |
| `obligatory`   | bool   | no       | Whether rule is obligatory (default: true) |
| `notes`        | string | no       | Optional notes                       |

## Sources Schema

The `sources` array contains bibliographic references for the phonological data in the spec.

```json
{
  "sources": [
    {
      "id": "wells1982_vol2",
      "author": "Wells, J.C.",
      "year": 1982,
      "title": "Accents of English, Vol. 2: The British Isles",
      "publisher": "Cambridge University Press",
      "url": null,
      "pages": null,
      "notes": null
    }
  ]
}
```

| Source Field  | Type    | Required | Description                                         |
|---------------|---------|----------|-----------------------------------------------------|
| `id`          | string  | yes      | Short cite key (e.g. `"wells1982"`)                 |
| `author`      | string  | yes      | Author(s), e.g. `"Wells, J.C."`                     |
| `year`        | integer | yes      | Publication year                                    |
| `title`       | string  | yes      | Full title of the work                              |
| `publisher`   | string  | no       | Publisher name                                      |
| `url`         | string  | no       | URL or DOI; use `null` for print-only works         |
| `wikipedia_url` | string | no       | Wikipedia article URL for quick human reference     |
| `pages`       | string  | no       | Specific page range, e.g. `"pp. 45-72"`            |
| `notes`       | string  | no       | Annotation about what this source supports          |

## Positional Grapheme Keys

Position keys in `positional_graphemes` use lowercase string values
matching the `GraphemePosition` enum:

| JSON key                    | Enum value                                 |
|-----------------------------|--------------------------------------------|
| `"default"`                 | `GraphemePosition.DEFAULT`                 |
| `"nucleus"`                 | `GraphemePosition.NUCLEUS`                 |
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
| `"before_vowel"`            | `GraphemePosition.BEFORE_VOWEL`            |
| `"after_vowel"`             | `GraphemePosition.AFTER_VOWEL`             |
| `"before_consonant"`        | `GraphemePosition.BEFORE_CONSONANT`        |
| `"after_consonant"`         | `GraphemePosition.AFTER_CONSONANT`         |
| `"before_a"`                | `GraphemePosition.BEFORE_A`                |
| `"before_e"`                | `GraphemePosition.BEFORE_E`                |
| `"before_i"`                | `GraphemePosition.BEFORE_I`                |
| `"before_o"`                | `GraphemePosition.BEFORE_O`                |
| `"before_u"`                | `GraphemePosition.BEFORE_U`                |
| `"before_front_vowel"`      | `GraphemePosition.BEFORE_FRONT_VOWEL`      |
| `"before_back_vowel"`       | `GraphemePosition.BEFORE_BACK_VOWEL`       |
| `"after_front_vowel"`       | `GraphemePosition.AFTER_FRONT_VOWEL`       |
| `"after_back_vowel"`        | `GraphemePosition.AFTER_BACK_VOWEL`        |
| `"consonantal"`             | `GraphemePosition.CONSONANTAL`             |
| `"vocalic"`                 | `GraphemePosition.VOCALIC`                 |

The `*_front_vowel` / `*_back_vowel` positions condition on the whole vowel
**class** of the neighbouring grapheme rather than a single letter — e.g. one
`"before_front_vowel"` entry replaces `"before_e"` + `"before_i"` plus every
accented ⟨e⟩/⟨i⟩ variant (Romance c/g softening). Membership is owned by
`orthography2ipa.vowels.is_front_vowel` / `is_back_vowel`, which classify a
letter by NFD-decomposing it to its base and reading the base — `e i y` are
front, `a o u` are back — whenever every diacritic preserves the front/back
axis (acute, grave, circumflex, caron, macron, breve, ogonek, dot, tilde), so
`é ě ī į ý` are front and `á â ã ā ą` are back without hand-listing. Diaeresis
changes the axis, so `ä ö ü ë ï ÿ` are front by explicit rule, as are dotless
`ı` and non-decomposing `ø œ æ`; ring `å` straddles the axis and is in neither
class. Resolution order is **exact-letter position > vowel-class
position > default `graphemes` mapping**: an exact `"before_e"` entry declared
for the same grapheme wins over `"before_front_vowel"`, and the class positions
are inert (change nothing) for any spec that does not declare them.

## Ancestor Role Values

| JSON value         | Enum value                    |
|--------------------|-------------------------------|
| `"parent"`         | `AncestorRole.PARENT`         |
| `"parent_dialect"` | `AncestorRole.PARENT_DIALECT` |
| `"proto_language"` | `AncestorRole.PROTO_LANGUAGE` |
| `"ancestor"`       | `AncestorRole.ANCESTOR`       |
| `"substrate"`      | `AncestorRole.SUBSTRATE`      |
| `"superstrate"`    | `AncestorRole.SUPERSTRATE`    |
| `"adstrate"`       | `AncestorRole.ADSTRATE`       |
| `"lexifier"`       | `AncestorRole.LEXIFIER`       |
| `"creole_base"`    | `AncestorRole.CREOLE_BASE`    |
| `"related"`        | `AncestorRole.RELATED`        |

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
