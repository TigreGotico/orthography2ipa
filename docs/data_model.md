# Data Model

## Overview

The entire package is built around a small, stable set of types defined in `types.py`. All types are immutable (frozen dataclasses or enums), enabling safe caching and sharing.

---

## `Grapheme2IPA`

```python
Grapheme2IPA = Dict[str, List[str]]
```

A mapping from orthographic strings to lists of IPA phoneme strings.

**Keys** are graphemes as they appear in the language's orthography. They may be:
- Single characters: `"a"`, `"b"`, `"ñ"`, `"ü"`
- Digraphs: `"ch"`, `"ll"`, `"sh"`, `"lh"`, `"nh"`, `"rr"`
- Trigraphs (rare): `"sch"` in German, `"tch"` in French
- Diphthong spellings: `"ai"`, `"ie"`, `"ua"` — for languages where diphthong graphemes need explicit handling

**Values** are lists of IPA strings representing the possible phonemic realisations of the grapheme, ordered from most to least common:

```python
# English
"c":  ["k", "s"]      # /k/ is primary (cat, cup), /s/ secondary (cent, city)
"th": ["θ", "ð"]      # /θ/ primary (think), /ð/ secondary (the, this)

# Castilian Spanish
"c":  ["k", "θ"]      # /k/ before a,o,u; /θ/ before e,i
"ll": ["ʎ", "ʝ"]     # /ʎ/ traditional lleísmo; /ʝ/ yeísmo variant

# Portuguese
"lh": ["ʎ"]           # always /ʎ/ — no ambiguity
"x":  ["ʃ", "ks", "s", "z"]  # highly ambiguous in Portuguese
```

The ordering matters: the `PhonetokTokenizer`'s beam search treats the first value as the canonical (lowest-scoring) option.

---

## `AllophoneMap`

```python
AllophoneMap = Dict[str, List[str]]
```

A mapping from underlying phonemes to their contextual surface realisations (allophones).

**Keys** are IPA phoneme strings (the underlying phonological forms).

**Values** are lists of IPA strings representing the attested surface forms:

```python
# English /t/ — multiple allophones depending on phonological context
"t": ["t",   # canonical: word-initial (top, ten)
      "tʰ",  # aspirated: syllable-initial before stressed vowel
      "ɾ",   # flap: intervocalic in North American English (butter, water)
      "ʔ",   # glottal stop: before syllabic /n/ (button, cotton)
      "t̚"]  # unreleased: word-final (cat, but)

# Spanish /b/ — lenition
"b": ["b",   # after pause or nasal (burro, un barco)
      "β"]   # spirantised: all other positions (lobo, el barco)

# Spanish /n/ — place assimilation
"n": ["n",   # default alveolar
      "m",   # before bilabials (un padre → [um padre])
      "ɱ",   # labiodental before /f/ (enfermo)
      "n̪",  # dental before /t,d/
      "ŋ",   # velar before /k,g/ (banco)
      "ɲ"]   # palatal before /ʎ,ʝ/ (ancho)
```

The `AllophoneMap` does **not** encode the phonological rules that determine which allophone occurs — it only records *which allophones exist* for distance calculations and phonological inventory analysis. Allophone selection rules would need to be implemented separately by the consumer.

---

## `AncestorRole`

```python
class AncestorRole(Enum):
    PARENT       = "parent"
    SUBSTRATE    = "substrate"
    SUPERSTRATE  = "superstrate"
    ADSTRATE     = "adstrate"
    LEXIFIER     = "lexifier"
    CREOLE_BASE  = "creole_base"
```

Encodes the **type of historical relationship** between a language and its ancestor.

| Role | Definition | Example |
|---|---|---|
| `PARENT` | Primary genetic descent | Latin → Spanish |
| `SUBSTRATE` | Language of the pre-existing population | Basque substrate in Castilian |
| `SUPERSTRATE` | Language of a dominant group, later absorbed | Frankish superstrate in French |
| `ADSTRATE` | Peer contact influence from a neighbouring language | Arabic adstrate on Ibero-Romance |
| `LEXIFIER` | Vocabulary source in creole/pidgin formation | Portuguese lexifier of Papiamento |
| `CREOLE_BASE` | Grammar/structural source in creole formation | West African languages as creole base |

### Linguistic notes

**PARENT**: Every language (except reconstructed proto-languages) should have exactly one PARENT. This is the primary line of descent. The weight is typically 0.7–1.0.

**SUBSTRATE**: A substrate is the language of the original population that adopted the incoming language. Substrate effects show up as phonological features that deviate from the parent. The Basque substrate in Castilian is the classic explanation for the *f-* → *h-* sound change (Latin *filium* → Spanish *hijo*). Weight: 0.05–0.30.

**SUPERSTRATE**: A superstrate is a prestige language whose speakers eventually shift to the local language but leave phonological and lexical traces. Frankish (Proto-Germanic) contributed vocabulary and possibly phonological features to Old French. Weight: 0.10–0.40.

**ADSTRATE**: An adstrate is a neighbouring language at roughly equal social status that exerts ongoing influence. Arabic was an adstrate on medieval Ibero-Romance, contributing over 4,000 loanwords to Spanish and Portuguese. Weight: 0.05–0.20.

---

## `Ancestor`

```python
@dataclass(frozen=True)
class Ancestor:
    code: str            # Language code of the ancestor
    role: AncestorRole   # Type of relationship
    weight: float = 0.5  # Contribution weight [0.0, 1.0]
    notes: str = ""      # Optional explanatory notes
```

### Weight guidelines

| Role | Typical weight range |
|---|---|
| PARENT | 0.70–1.00 |
| SUBSTRATE | 0.05–0.30 |
| SUPERSTRATE | 0.10–0.40 |
| ADSTRATE | 0.05–0.20 |
| LEXIFIER | 0.50–0.80 |
| CREOLE_BASE | 0.20–0.50 |

Weights do not need to sum to 1.0. They represent approximate phonological contribution, not relative proportion of heritage.

### Example

```python
from orthography2ipa.types import Ancestor, AncestorRole

Ancestor(
    code="la-x-hispania",
    role=AncestorRole.PARENT,
    weight=0.80,
    notes="Primary descent from Hispanic Vulgar Latin"
)
```

---

## `LanguageSpec`

`orthography2ipa/types.py:379`

```python
@dataclass(frozen=True)
class LanguageSpec:
    code: str                                          # BCP-47 or ISO 639 code
    name: str                                          # Human-readable name
    family: str                                        # DERIVED classification path
    family_path: Tuple[str, ...]                       # DERIVED clade chain, broadest first
    clade: bool                                        # classification-only node
    script: str                                        # Primary script
    graphemes: Grapheme2IPA                            # Grapheme → IPA
    allophones: AllophoneMap                           # Phoneme → allophones
    parent: Optional[str] = None                       # Primary parent code (shorthand)
    ancestors: Tuple[Ancestor, ...] = ()               # Full ancestry specification
    positional_graphemes: PositionalGrapheme2IPA = None # Context-sensitive IPA (normalised to {} in __post_init__)
    glottolog_code: str | None = None                  # Glottolog languoid code
    notes: str = ""                                    # Free-form notes
    quality: QualityTier = QualityTier.RESEARCH        # Data maturity tier
    script_type: ScriptType = ScriptType.ALPHABET      # Writing system typology
    inherent_vowel: Optional[str] = None               # For abugidas (e.g. "ə" for Hindi)
    iso639_3: Optional[str] = None                     # ISO 639-3 code
    sandhi_rules: Tuple[SandhiRule, ...] = ()           # Cross-word phonological rules
    tone_inventory: Optional[Dict[str, str]] = None    # IPA tone mark → label
    sources: Tuple[LinguisticSource, ...] = ()         # Bibliographic references
    wikipedia: Tuple[str, ...] = ()                    # Wikipedia article URLs
```

### Accessor methods and properties

```python
spec = orthography2ipa.get("es-ES")

# Primary parent code
spec.primary_parent          # "la-x-hispania"

# All ancestors, optionally filtered by role
spec.get_ancestors()                           # all ancestors
spec.get_ancestors(AncestorRole.SUBSTRATE)     # substrate ancestors only

# Convenience tuples of codes
spec.substrate_codes          # ('xaq',)
spec.superstrate_codes        # ('got',)
spec.contact_codes            # all non-parent ancestors: ('xaq', 'xaa', 'got')

# Positional grapheme resolution
spec.resolve_grapheme("b", GraphemePosition.INTERVOCALIC)  # ["β"]
spec.has_positional_data()           # bool
spec.positional_grapheme_keys()      # frozenset of graphemes with overrides
spec.positions_for_grapheme("b")     # tuple of GraphemePosition values
```

### The `parent` vs `ancestors` fields

For backward compatibility, `LanguageSpec` supports both `parent` (a simple string shorthand) and `ancestors` (the full typed tuple). If `ancestors` is empty but `parent` is set, `__post_init__` synthesises a `PARENT` ancestor with weight 1.0 automatically. Conversely, if `parent` is empty but `ancestors` contains a PARENT-role entry, `parent` is set from it.

For new languages and dialects, always populate the `ancestors` tuple for richest data. Simple dialects that differ minimally from a parent may use just `parent`.

### `QualityTier` enum

`orthography2ipa/types.py:174`

| Value | Description |
|---|---|
| `STUB` | Code + name + family + script only |
| `SKELETON` | Graphemes + allophones from auto-generation (unvalidated) |
| `RESEARCH` | Validated against published phonology; positional rules present |
| `PRODUCTION` | Full coverage, regression-tested, cited sources |

### `ScriptType` enum

`orthography2ipa/types.py:194`

| Value | Description |
|---|---|
| `ALPHABET` | Latin, Cyrillic, Greek, Armenian, Georgian |
| `ABJAD` | Arabic, Hebrew — consonants primary, vowels optional |
| `ABUGIDA` | Devanagari, Bengali, Tamil, Thai — inherent vowel |
| `SYLLABARY` | Kana, Cherokee |
| `LOGOGRAPHIC` | Hanzi / CJK ideographs |
| `FEATURAL` | Hangul |
| `MIXED` | Japanese (logographic + syllabary) |
| `RECONSTRUCTION` | IPA-based phonological reconstruction for extinct languages |

### `LinguisticSource` dataclass

`orthography2ipa/types.py:258`

Fields: `id`, `author`, `year`, `title`, `publisher`, `url`, `wikipedia_url`, `pages`, `notes`.

### `SandhiRule` dataclass

`orthography2ipa/types.py:300`

Fields: `id`, `name`, `left_context`, `right_context`, `transform`, `obligatory`, `notes`.

---

## Lexicon overlay (sidecar `word_exceptions` at scale)

`orthography2ipa/lexicon.py`

Deep-orthography languages (English, Danish, Irish) cannot reach production
accuracy from grapheme rules alone — too many words are irregular. The
`word_exceptions` field on `LanguageSpec` handles a *closed, tiny* set of
irregulars inline in the JSON, but it does not scale to thousands of entries.

A **lexicon** is an optional, convention-based sidecar file
`orthography2ipa/data/lexicons/{code}.tsv` — one `word<TAB>ipa` pair per line,
UTF-8, NFC-normalised, lowercase words, sorted, first-entry-wins. It needs **no
new spec field and no JSON change**: the file is discovered by its name (the
resolved language code, e.g. `en-GB.tsv`), so `FIELD_INHERITANCE` is untouched.

Contract:

- **Lazy.** Importing the package, and even loading a `LanguageSpec`, reads
  **no** lexicon. A language's TSV is read once, on the first transcription for
  that language (`get_lexicon(code)`), then cached for the process lifetime.
- **Same pathway as `word_exceptions`.** `G2P._override_for` folds a lexicon
  hit into the *exact* override path `word_exceptions` uses, so a lexicon entry
  still gets stress-mark insertion and cross-word sandhi applied and is
  reported with `confidence == 1.0` (a certain answer).
- **Precedence:** inline `word_exceptions` **>** lexicon **>** rules. An inline
  exception always wins; the sidecar always wins over the grapheme/positional
  beam.
- **Absent lexicon → byte-identical.** A language with no `{code}.tsv` gets an
  empty overlay and behaves exactly as before this feature existed.

Every shipped TSV is validated (parseable `word<TAB>ipa`, NFC, lowercase word,
IPA-characters-only) by `lexicon.validate_lexicon_text`; the shipped-data test
runs that guard over every file. The one bundled pilot is `en-GB.tsv`
(CMUdict-derived — see [`bibliography.md`](bibliography.md) and
`scripts/build_en_lexicon.py`); the rules-only vs with-lexicon PER impact is
reported in [`lexicon_scoreboard.md`](lexicon_scoreboard.md). Full production
lexica belong downstream — see [`adding_a_language.md`](adding_a_language.md).

---

## Relationship between `graphemes` and `allophones`

These are **different layers** of phonological description:

```
orthography → graphemes → underlying phonemes → allophones → surface forms
    "butter"    b,u,tt,e,r     /b ʌ t ə r/     [b ʌ ɾ ə r]    "buh-der"
```

- `graphemes` maps **orthography → phonology** (abstract level)
- `allophones` maps **phonology → phonetics** (surface level)

A word like English *butter* goes through two mappings:
1. Grapheme step: `tt` → `/t/` (the underlying phoneme)
2. Allophone step: `/t/` → `[ɾ]` (the flap allophone in this context)

The package stores both levels; rule-based selection between allophones requires implementation by the consumer.

---

**Navigation:** [Docs home](index.md) · [Getting started](getting_started.md) · [Architecture](architecture.md) · [Languages](languages/index.md) · [Scoreboard](scoreboard.md)

*Related: [Architecture](architecture.md) · [Positional graphemes](positional_graphemes.md) · [Allophony](allophony.md) · [Registry](registry.md)*
