# Positional Graphemes

## Overview

The **positional grapheme system** extends the base `graphemes` mapping with optional context-sensitive IPA overrides. Many languages have graphemes whose pronunciation depends systematically on position within a word or syllable. Rather than listing all possible realisations in the flat `graphemes` dict (leaving consumers to guess which applies), `positional_graphemes` encodes exactly which IPA mapping applies in each phonological environment.

This feature is **fully backward-compatible** — existing `LanguageSpec` objects without positional data continue to work identically.

---

## Why Positional Graphemes?

Consider Portuguese ⟨s⟩. The flat `graphemes` mapping lists all possibilities:

```python
"s": ["s", "z", "ʃ", "ʒ"]
```

But the distribution is entirely predictable by position:

| Position | Realisation | Example |
|---|---|---|
| Word-initial | [s] | **s**ol → [sɔl] |
| Intervocalic | [z] | ca**s**a → [kazɐ] |
| Coda (before voiceless) | [ʃ] | e**s**tar → [ɨʃtar] |
| Coda (before voiced) | [ʒ] | me**s**mo → [meʒmu] |
| Word-final | [ʃ] | gato**s** → [gatuʃ] |
| Cross-word before vowel | [z] | os amigos → [uz‿ɐmiɡuʃ] |

The `positional_graphemes` field captures this directly:

```python
positional_graphemes={
    "s": {
        GraphemePosition.WORD_INITIAL: ["s"],
        GraphemePosition.INTERVOCALIC: ["z"],
        GraphemePosition.CODA: ["ʃ", "ʒ"],         # [ʃ] default, [ʒ] before voiced
        GraphemePosition.WORD_FINAL: ["ʃ"],
        GraphemePosition.INTERVOCALIC_CROSS_WORD: ["z"],
    },
}
```

This makes the phonemizer significantly more accurate out of the box, even though the primary goal of this package is phoneme inventories rather than full G2P.

---

## `GraphemePosition` Enum

```python
from orthography2ipa.types import GraphemePosition
```

| Value | Environment | Notation | Example phenomena |
|---|---|---|---|
| `DEFAULT` | Context-free fallback | — | Equivalent to base `graphemes` |
| `WORD_INITIAL` | Absolute word-initial | #_ | English aspiration, German [z] for ⟨s⟩ |
| `WORD_FINAL` | Absolute word-final | _# | German Auslautverhärtung, Portuguese [ʃ] |
| `INTERVOCALIC` | Between vowels (same word) | V_V | Spanish lenition, Portuguese voicing |
| `INTERVOCALIC_CROSS_WORD` | Between vowels across words | V#_V | French liaison, Portuguese sandhi |
| `ONSET` | Syllable onset | σ[_ | English clear [l], Korean aspirated stops |
| `NUCLEUS` | Syllable nucleus | σ_σ | Portuguese unstressed vowel reduction |
| `CODA` | Syllable coda | _]σ | English dark [ɫ], Korean neutralisation, Brazilian [w] |

These positions correspond to standard phonological environments documented in:

- Kenstowicz, M. (1994). *Phonology in Generative Grammar*. Blackwell.
- Hayes, B. (2009). *Introductory Phonology*. Wiley-Blackwell.
- Zsiga, E. (2013). *The Sounds of Language*. Wiley-Blackwell.

---

## `PositionalGrapheme2IPA` Type

```python
PositionalGrapheme2IPA = Dict[str, Dict[GraphemePosition, List[str]]]
```

Maps grapheme keys to dicts of `{GraphemePosition: [IPA candidates]}`. Only graphemes whose IPA changes by position need entries. All other graphemes use the base `graphemes` mapping.

---

## `LanguageSpec` Integration

```python
@dataclass(frozen=True)
class LanguageSpec:
    # ... existing fields ...
    positional_graphemes: PositionalGrapheme2IPA = {}
```

### Resolution method

```python
spec.resolve_grapheme(grapheme, position=GraphemePosition.DEFAULT) -> List[str]
```

**Lookup order:**
1. `positional_graphemes[grapheme][position]` — exact match
2. `positional_graphemes[grapheme][DEFAULT]` — positional default override
3. `graphemes[grapheme]` — base mapping fallback
4. `KeyError` if not found anywhere

### Introspection methods

```python
spec.has_positional_data()           # bool — any positional overrides?
spec.positional_grapheme_keys()      # frozenset — which graphemes have overrides
spec.positions_for_grapheme("s")     # tuple of GraphemePosition values
```

---

## Usage Examples

### Basic resolution

```python
import orthography2ipa
from orthography2ipa.types import GraphemePosition

pt = orthography2ipa.get("pt-PT")

# Context-free (uses base graphemes or positional DEFAULT)
pt.resolve_grapheme("s")                                    # ["s", "z", "ʃ", "ʒ"]

# Positional (if positional_graphemes is populated)
pt.resolve_grapheme("s", GraphemePosition.WORD_INITIAL)     # ["s"]
pt.resolve_grapheme("s", GraphemePosition.INTERVOCALIC)     # ["z"]
pt.resolve_grapheme("s", GraphemePosition.WORD_FINAL)       # ["ʃ"]

# Grapheme without positional override falls back to base
pt.resolve_grapheme("a", GraphemePosition.ONSET)            # ["a"] (from base)
```

### Checking for positional data

```python
if pt.has_positional_data():
    keys = pt.positional_grapheme_keys()
    print(f"Positional overrides for: {keys}")
    for g in keys:
        positions = pt.positions_for_grapheme(g)
        for pos in positions:
            ipa = pt.resolve_grapheme(g, pos)
            print(f"  ⟨{g}⟩ in {pos.value}: {ipa}")
```

---

## Adding Positional Data to a Language

When creating or extending a `LanguageSpec`, add `positional_graphemes` for graphemes with position-dependent pronunciation. Only include graphemes that genuinely vary — if a grapheme has the same IPA in all positions, leave it in the base `graphemes` only.

### Example: Spanish lenition

```python
POSITIONAL_GRAPHEMES_ES = {
    # Voiced stops → fricatives intervocalically
    "b": {
        GraphemePosition.DEFAULT: ["b"],
        GraphemePosition.INTERVOCALIC: ["β"],
    },
    "d": {
        GraphemePosition.DEFAULT: ["d"],
        GraphemePosition.INTERVOCALIC: ["ð"],
        GraphemePosition.WORD_FINAL: ["ð", "∅"],  # weakened or deleted
    },
    "g": {
        GraphemePosition.DEFAULT: ["ɡ"],
        GraphemePosition.INTERVOCALIC: ["ɣ"],
    },
}

SPECS = {
    "es-ES": LanguageSpec(
        code="es-ES",
        name="Castilian Spanish",
        family="Romance",
        script="Latin",
        graphemes=GRAPHEMES_ES,
        allophones=ALLOPHONES_ES,
        positional_graphemes=POSITIONAL_GRAPHEMES_ES,
        # ... other fields ...
    ),
}
```

### Example: English onset/coda split

```python
POSITIONAL_GRAPHEMES_EN = {
    "l": {
        GraphemePosition.ONSET: ["l"],     # clear l
        GraphemePosition.CODA: ["ɫ"],      # dark l (velarised)
    },
    "t": {
        GraphemePosition.WORD_INITIAL: ["t"],     # aspirated [tʰ] is allophonic
        GraphemePosition.INTERVOCALIC: ["ɾ"],     # flapping (GA)
        GraphemePosition.WORD_FINAL: ["t"],
    },
}
```

### Example: Brazilian Portuguese coda vocalization

```python
POSITIONAL_GRAPHEMES_PT_BR = {
    "l": {
        GraphemePosition.ONSET: ["l"],
        GraphemePosition.CODA: ["w"],     # l-vocalization
    },
    "s": {
        GraphemePosition.WORD_INITIAL: ["s"],
        GraphemePosition.INTERVOCALIC: ["z"],
        GraphemePosition.CODA: ["s", "z"],  # [s] before voiceless, [z] before voiced
        GraphemePosition.WORD_FINAL: ["s"],
    },
    "r": {
        GraphemePosition.WORD_INITIAL: ["ʁ"],
        GraphemePosition.INTERVOCALIC: ["ɾ"],
        GraphemePosition.CODA: ["ɾ", "ʁ", "h"],  # varies by dialect
    },
}
```

---

## Relationship to Allophones

The `positional_graphemes` system operates at the **grapheme → phoneme** level, not the **phoneme → allophone** level. The two layers are complementary:

```
orthography → positional_graphemes → phoneme → allophones → surface
   "casa"       ⟨s⟩ intervocalic      /z/        [z]        [z]
   "sol"        ⟨s⟩ word-initial      /s/        [s]        [s]
   "gatos"      ⟨s⟩ word-final        /ʃ/        [ʃ]        [ʃ]
```

- **`positional_graphemes`**: Disambiguates *which phoneme* a grapheme represents based on position
- **`allophones`**: Documents *which surface variants* a phoneme has (regardless of how we got to that phoneme)

Some phenomena (like English /t/ flapping) could be modelled at either level. As a guideline:

- If the orthography→phoneme step is ambiguous → use `positional_graphemes`
- If the phoneme→surface step varies → use `allophones`
- If both apply, use both

---

## Backward Compatibility

The positional system is designed to be fully backward-compatible:

- `positional_graphemes` defaults to `{}` (empty dict) when not provided
- `LanguageSpec` with `positional_graphemes=None` automatically normalises to `{}`
- `resolve_grapheme("x")` without a position argument returns the same result as `graphemes["x"]` when no positional data exists
- All existing `LanguageSpec` objects continue to work without modification
- The `PhonetokTokenizer` falls back gracefully when positional data is absent

---

## Integration with Distance Metrics

The distance calculation functions in `distance.py` continue to use the base `graphemes` mapping for inventory-level comparisons. Positional data provides finer-grained disambiguation for G2P but does not change the phoneme inventory or allophone set, so distance metrics remain consistent.

However, consumers building on this package can use positional data to compute **positional divergence** between related languages — for example, comparing how Portuguese and Spanish handle intervocalic stops differently.
