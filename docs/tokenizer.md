# Tokenizer

The `phonetok` module provides a language-agnostic grapheme tokenizer with IPA beam expansion.

---

## Core Concepts

### Maximal Munch

The tokenizer always tries to match the **longest possible grapheme** at each position. This correctly handles digraphs and multigraphs:

```
Input: "chuva" (Portuguese for "rain")
Naive: c h u v a  → [k/s, h, u, v, a]  ❌
Maximal munch: ch u v a → [ʃ, u, v, a]  ✓

Input: "lhano" (Portuguese)
Naive: l h a n o
Maximal munch: lh a n o → [ʎ, a, n, u]  ✓
```

### IPA Ambiguity and Beam Search

Many graphemes map to multiple IPA values. This creates combinatorial explosion:

```
"ice" (English)
  i → /aɪ/ or /ɪ/
  c → /k/ or /s/
  e → /iː/ or /ɛ/ or silent

Total paths: 2 × 2 × 3 = 12
```

Beam search limits this to the N most-canonical paths (ranked by how "non-default" each choice is).

By default that ranking is *positional*: candidate `0` costs `0`, candidate `1` costs `+1`, and so on. A spec can instead attach per-candidate **weights** (candidate frequencies) so the beam favours the corpus-dominant pronunciation and a path's score becomes a real log-probability. Absent weights, the behaviour is exactly the rank ordering above. See [candidate_scoring.md](candidate_scoring.md).

---

## Classes

### `TokenKind`

```python
class TokenKind(Enum):
    GRAPHEME     # A linguistically meaningful grapheme from the language's table
    WHITESPACE   # One or more whitespace characters
    PUNCTUATION  # Punctuation marks
    DIGIT        # One or more consecutive digits
    UNKNOWN      # Characters not matched by any rule
    BOS          # Beginning-of-sequence sentinel
    EOS          # End-of-sequence sentinel
```

### `Token`

```python
@dataclass(frozen=True)
class Token:
    kind: TokenKind
    grapheme: str       # Surface string (lowercase for GRAPHEME, original for others)
    ipa: Tuple[str, ...]  # Possible IPA values (empty for non-GRAPHEME)
    position: int       # Character offset into original input
    length: int         # Number of characters consumed
```

```python
tok = PhonetokTokenizer(orthography2ipa.get("es"))
tokens = tok.tokenize("niño")

for t in tokens:
    print(repr(t))
# Token(GRAPHEME, 'n', [n], pos=0)
# Token(GRAPHEME, 'i', [i], pos=1)
# Token(GRAPHEME, 'ñ', [ɲ], pos=2)
# Token(GRAPHEME, 'o', [o], pos=4)
```

### `IPAPath`

```python
@dataclass(frozen=True)
class IPAPath:
    segments: Tuple[str, ...]  # IPA segment for each GRAPHEME token
    score: float               # Heuristic score (lower = more canonical)

    @property
    def ipa(self) -> str: ...  # Concatenated IPA string
```

The `score` field counts how many "non-canonical" (non-first) IPA choices were made. Score 0 = all default choices; score 1 = one alternative was chosen; etc.

---

## `PhonetokTokenizer`

### Constructor

```python
from orthography2ipa.phonetok import PhonetokTokenizer
import orthography2ipa

tok = PhonetokTokenizer(spec)
```

Where `spec` is any `LanguageSpec` from the registry. The tokenizer builds a prefix trie from `spec.graphemes` at construction time.

### `tokenize(text)`

```python
tokens: List[Token] = tok.tokenize(text)
```

Returns all tokens including whitespace and punctuation. Useful for preserving text structure.

```python
tok_en = PhonetokTokenizer(orthography2ipa.get("en"))
tokens = tok_en.tokenize("the cat sat.")
for t in tokens:
    print(f"{t.kind.name:12s}  {t.grapheme!r:8s}  {t.ipa}")

# GRAPHEME      'th'      ('θ', 'ð')
# GRAPHEME      'e'       ('iː', 'ɛ', 'ə')
# WHITESPACE    ' '       ()
# GRAPHEME      'c'       ('k', 's')
# GRAPHEME      'a'       ('æ', 'eɪ', 'ɑː', 'ə')
# GRAPHEME      't'       ('t',)
# WHITESPACE    ' '       ()
# GRAPHEME      's'       ('s', 'z')
# GRAPHEME      'a'       ('æ', 'eɪ', 'ɑː', 'ə')
# GRAPHEME      't'       ('t',)
# PUNCTUATION   '.'       ()
```

### `ipa_beam(text, beam_width, include_allophones)`

```python
paths: List[IPAPath] = tok.ipa_beam(
    text,
    beam_width=8,        # max number of paths (default 8)
    include_allophones=False  # expand to allophone level (default False)
)
```

Returns up to `beam_width` paths, sorted by score (most canonical first):

```python
tok_es = PhonetokTokenizer(orthography2ipa.get("es"))
paths = tok_es.ipa_beam("ciudad", beam_width=6)

for p in paths:
    print(f"  score={p.score:.1f}  /{p.ipa}/")

# score=0.0  /θjuðað/    ← canonical Castilian (θ for ⟨c⟩, ð for ⟨d⟩ allophones)
# score=1.0  /sjuðað/    ← seseo variant
# ...
```

### `ipa_expand(tokens, include_allophones)`

```python
paths: List[IPAPath] = tok.ipa_expand(
    tokens,                     # List[Token] from tokenize()
    include_allophones=False
)
```

Lower-level version of `ipa_beam` that works directly on pre-tokenized input. Useful if you want to tokenize once and expand multiple times.

---

## Allophone Expansion

When `include_allophones=True`, IPA paths are further expanded to include allophonic variants from `spec.allophones`:

```python
tok = PhonetokTokenizer(orthography2ipa.get("es"))
paths = tok.ipa_beam("habla", beam_width=10, include_allophones=True)

# Without allophones: /aβla/  (lenited /b/)
# With allophones:
#   /abla/   ← [b] stop variant (post-pause)
#   /aβla/   ← [β] spirant variant (intervocalic)
```

This is useful for:
- Phonetic synthesis preprocessing
- Allophone frequency analysis
- Pronunciation variant generation

---

## Handling Special Characters

### Digits

```python
tokens = tok.tokenize("hay 3 gatos")
for t in tokens:
    print(t.kind.name, t.grapheme)
# GRAPHEME  hay   (etc.)
# DIGIT     3
# GRAPHEME  gatos (etc.)
```

### Unknown characters

Characters not matching any grapheme, whitespace, digit, or punctuation pattern become `UNKNOWN` tokens:

```python
tokens = tok.tokenize("café☕")
# 'c', 'a', 'f', 'é' → GRAPHEME
# '☕' → UNKNOWN (not in any grapheme table)
```

### Case insensitivity

GRAPHEME tokens are **lower-cased** before trie lookup. The `.grapheme` field stores the lowercase form. This means `"CH"` and `"ch"` both match the `"ch"` grapheme key.

---

## Context Model

`tokenize()` returns a flat `List[Token]`. When a consumer needs to reason
about a grapheme's *surroundings* — its neighbours, its character span, or
its phonological class — `tokenize_with_context()` returns a
`TokenSequence`: a view that wraps every GRAPHEME token in a
`GraphemeContext`.

```python
seq = tok.tokenize_with_context("cera")
for c in seq:
    print(c.grapheme, c.span, c.is_vowel)
```

Each `GraphemeContext` exposes:

- **Neighbours** (word-local — they never cross whitespace, punctuation,
  digits or unknown characters):
  - `.prev` / `.next` — the adjacent grapheme, or `None` at a word edge.
  - `.at(offset)` — the grapheme `offset` positions away (`at(2)`, `at(-1)`);
    `None` past a word edge.
  - `.neighbors(n)` — up to `2*n` graphemes within `±n`, left-to-right,
    self excluded, clamped at word edges.
- **Span** — `.span` → `(start, end)` character offsets that index the
  **NFC-normalised** input `tokenize()` works on, with `.grapheme` itself
  **case-folded**. The exact contract is
  `unicodedata.normalize("NFC", text)[start:end].lower() == grapheme`. A
  raw `text[start:end]` round-trip against the caller's original string
  only holds when that string is already lower-case NFC — it breaks for
  upper-case input (offsets index the un-folded text) and for NFD input
  (offsets index the NFC-normalised text).
- **Class predicates**, delegating to `orthography2ipa.vowels` (the single
  source of truth — no vowel set is defined here): `.is_vowel`,
  `.is_consonant`, `.is_front`, `.is_back`. They classify by the grapheme's
  leading character, so a consonant digraph (`ch`) is a consonant and a
  vowel digraph (`ai`) reports by its leading vowel.

### Why it exists: replacing hand-rolled index arithmetic

Downstream phonemizers historically re-implemented all of the above by
hand — raw string indexing plus their own vowel sets. The context model is
the shared substrate that replaces that. For a c-softening rule
(`c` → /s/ before a front vowel):

Before — raw index arithmetic and a private vowel list:

```python
chars = list(word.lower())
for idx, char in enumerate(chars):
    next_char = chars[idx + 1] if idx < len(chars) - 1 else ""
    if char == "c":
        phonemes[idx] = "s" if next_char in ("e", "i", "é", "í", "y") else "k"
```

After — one shared, accent-aware predicate:

```python
for c in tok.tokenize_with_context(word):
    if c.grapheme == "c":
        soft = c.next is not None and c.next.is_front
        emit("s" if soft else "k")
```

`is_front` already covers `e i y` plus every accented/diaeresis variant, so
the after-form needs no per-letter enumeration and cannot drift from the
rest of the library's vowel classification.

---

## Performance Notes

- The trie is built once at `PhonetokTokenizer` construction and reused for all subsequent calls.
- `tokenize()` is O(n·k) where n is text length and k is maximum grapheme length.
- `ipa_beam()` complexity is O(n · beam_width · |IPA alternatives|) — practical for words and short phrases.
- `tokenize_with_context()` adds one O(n) pass building lightweight flyweight views; neighbour lookups (`prev`/`next`/`at`) are O(1).
- For very long documents, consider tokenizing sentence-by-sentence.
