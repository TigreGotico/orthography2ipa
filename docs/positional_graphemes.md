# Positional Graphemes

## Overview

The **positional grapheme system** extends the base `graphemes` mapping with optional context-sensitive IPA overrides. 
Many languages have graphemes whose pronunciation depends systematically on position within a word or syllable. Rather than listing all possible realisations in the flat `graphemes` dict (leaving consumers to guess which applies), `positional_graphemes` encodes exactly which IPA mapping applies in each phonological environment.

> NOTE: This is provided as utility for downstream G2P tasks, but it's not within the scope of this repo to perform full phonemization

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
| `NUCLEUS` | Generic syllable nucleus | σ_σ | When stress is not distinguished |
| `NUCLEUS_STRESSED` | Stressed syllable nucleus | σ́_σ | Full vowel quality in stressed position |
| `NUCLEUS_UNSTRESSED` | Unstressed syllable nucleus | σ_σ̆ | Portuguese ⟨e⟩ → [ɨ], English ⟨a⟩ → [ə] |
| `CODA` | Syllable coda | _]σ | English dark [ɫ], Korean neutralisation, Brazilian [w] |
| `PRETONIC` | Before stressed syllable | — | Pretonic vowel reduction |
| `POSTTONIC` | After stressed syllable | — | Posttonic vowel reduction |
| `BEFORE_VOWEL` | Before any vowel | _V | Consonant allophony before vowels |
| `AFTER_VOWEL` | After any vowel | V_ | Post-vocalic consonant changes |
| `BEFORE_CONSONANT` | Before any consonant | _C | Pre-consonantal changes |
| `AFTER_CONSONANT` | After any consonant | C_ | Post-consonantal changes |
| `BEFORE_A` | Before ⟨a⟩ | _a | Velar softening contexts |
| `BEFORE_E` | Before ⟨e⟩ | _e | Velar softening contexts |
| `BEFORE_I` | Before ⟨i⟩ | _i | Velar softening contexts |
| `BEFORE_O` | Before ⟨o⟩ | _o | Velar softening contexts |
| `BEFORE_U` | Before ⟨u⟩ | _u | Velar softening contexts |
| `BEFORE_FRONT_VOWEL` | Before any front vowel letter | _[+front] | Romance c/g softening (soft) |
| `BEFORE_BACK_VOWEL` | Before any back vowel letter | _[+back] | Romance c/g softening (hard) |
| `AFTER_FRONT_VOWEL` | After any front vowel letter | [+front]_ | German ⟨ch⟩ → [ç] (Ich-Laut) |
| `AFTER_BACK_VOWEL` | After any back vowel letter | [+back]_ | German ⟨ch⟩ → [x] (Ach-Laut) |
| `CONSONANTAL` | Consonantal context | — | Grapheme realised as consonant |
| `VOCALIC` | Vocalic context | — | Grapheme realised as vowel |

These positions correspond to standard phonological environments documented in:

- Kenstowicz, M. (1994). *Phonology in Generative Grammar*. Blackwell.
- Hayes, B. (2009). *Introductory Phonology*. Wiley-Blackwell.
- Zsiga, E. (2013). *The Sounds of Language*. Wiley-Blackwell.

---

## Vowel-class positions (front / back)

The per-letter positions `BEFORE_A` … `BEFORE_U` (and their `AFTER_*` mirrors)
force a spec to enumerate one rule per triggering vowel — and, worse, per
*accented* variant of that vowel. The most common context-sensitive rule in
Latin-script orthographies, Romance **c/g softening**, conditions on the whole
*front vs. back vowel class*, not on individual letters: ⟨c⟩ is soft before any
of ⟨e i y é è ê …⟩ and hard before any of ⟨a o u á à â …⟩.

The class positions express this in a single entry each:

- **`BEFORE_FRONT_VOWEL`** / **`AFTER_FRONT_VOWEL`** — the following /
  preceding grapheme starts with a *front* vowel letter.
- **`BEFORE_BACK_VOWEL`** / **`AFTER_BACK_VOWEL`** — the following /
  preceding grapheme starts with a *back* vowel letter.

Membership is decided **solely** by
[`orthography2ipa.vowels`](../orthography2ipa/vowels.py), the single source of
truth for vowel classification:

```python
from orthography2ipa.vowels import is_front_vowel, is_back_vowel

is_front_vowel("é")   # True  — front, incl. accented and y / ü ö ø œ æ
is_back_vowel("â")    # True  — back,  incl. accented a o u
```

Front class: `e i y` + accented forms + the front rounded letters `ü ö ø œ æ`.
Back class: `a o u` + accented forms. `y` is treated as front (it patterns with
⟨i⟩ for softening). See the `vowels` module docstring for every borderline
classification.

### Worked example — Italian ⟨c⟩ softening

Instead of five near-identical per-letter entries, one class entry captures the
rule (⟨c⟩ → /tʃ/ before a front vowel, /k/ otherwise):

```json
{
  "graphemes": { "c": ["k"] },
  "positional_graphemes": {
    "c": { "before_front_vowel": ["tʃ"] }
  }
}
```

```python
eng.transcribe_word("ce")   # "tʃe"   before_front_vowel → /tʃ/
eng.transcribe_word("ci")   # "tʃi"
eng.transcribe_word("cé")   # "tʃe"   accented front vowel matches too
eng.transcribe_word("cy")   # "tʃi"   ⟨y⟩ is front
eng.transcribe_word("ca")   # "ka"    back vowel → default /k/
eng.transcribe_word("co")   # "ko"
eng.transcribe_word("cu")   # "ku"
```

### Resolution order

For any grapheme + neighbouring-context, the engine tries positions
**most-specific first** and takes the first one the spec actually declares:

1. **Exact-letter position** — `BEFORE_E`, `AFTER_A`, … (a specific vowel letter).
2. **Vowel-class position** — `BEFORE_FRONT_VOWEL`, `AFTER_BACK_VOWEL`, ….
3. **Default grapheme mapping** — the base `graphemes[grapheme]` list.

So a spec can declare `BEFORE_FRONT_VOWEL` for the general case and still add a
narrower `BEFORE_E` override for one letter that behaves differently — the exact
`BEFORE_E` entry wins for ⟨e⟩ while every other front vowel falls through to the
class rule. Class positions are inert for any spec that does not declare them, so
adding them changes no existing transcription.

### The engine and the standalone beam agree

Positional resolution is **not** engine-only. The standalone tokenizer beam
(`PhonetokTokenizer.ipa_beam` / `ipa_best`) consults the same
`positional_graphemes` overrides — including the vowel-class positions — through
the shared resolver in `orthography2ipa.positional`. So for a single word the
tokenizer and the full engine select the **same** context-conditioned candidate:

```python
from orthography2ipa import get
from orthography2ipa.g2p import G2P
from orthography2ipa.phonetok import PhonetokTokenizer

spec = get("es-ES")
G2P("es-ES").transcribe_word("cena")        # "ˈθena"  (c → /θ/ before ⟨e⟩)
PhonetokTokenizer(spec).ipa_best("cena")    # "θena"   same choice, no stress
```

The one difference is deliberate: **stress and sandhi stay engine-only**, because
the standalone tokenizer has no sentence context. The engine additionally supplies
syllable/stress information so the stress-conditioned nucleus positions
(`NUCLEUS_STRESSED`, `PRETONIC`, …) can fire and stress marks are added; the beam
omits exactly those. Every other position — `BEFORE_FRONT_VOWEL`, `INTERVOCALIC`,
`WORD_INITIAL`, `WORD_FINAL`, and the rest — resolves identically in both. The
per-word grapheme→IPA selection therefore matches (modulo stress marks/sandhi).

Both paths call one function, `orthography2ipa.positional.resolve_branches`, so
the engine and the beam cannot drift out of agreement.

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
    positional_graphemes: PositionalGrapheme2IPA = None  # normalised to {} in __post_init__
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

### Example: Spanish lenition (JSON)

In `orthography2ipa/data/es-ES.json`:

```json
{
  "positional_graphemes": {
    "b": {
      "default": ["b"],
      "intervocalic": ["β"]
    },
    "d": {
      "default": ["d"],
      "intervocalic": ["ð"],
      "word_final": ["ð", "∅"]
    },
    "g": {
      "default": ["ɡ"],
      "intervocalic": ["ɣ"]
    }
  }
}
```

### Example: Brazilian Portuguese coda vocalization (JSON)

In `orthography2ipa/data/pt-BR.json`:

```json
{
  "positional_graphemes": {
    "l": {
      "onset": ["l"],
      "coda": ["w"]
    },
    "s": {
      "word_initial": ["s"],
      "intervocalic": ["z"],
      "coda": ["s", "z"],
      "word_final": ["s"]
    },
    "r": {
      "word_initial": ["ʁ"],
      "intervocalic": ["ɾ"],
      "coda": ["ɾ", "ʁ", "h"]
    }
  }
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

## Integration with Distance Metrics

The distance calculation functions in `distance.py` continue to use the base `graphemes` mapping for inventory-level comparisons. Positional data provides finer-grained disambiguation for G2P but does not change the phoneme inventory or allophone set, so distance metrics remain consistent.

However, consumers building on this package can use positional data to compute **positional divergence** between related languages — for example, comparing how Portuguese and Spanish handle intervocalic stops differently.
