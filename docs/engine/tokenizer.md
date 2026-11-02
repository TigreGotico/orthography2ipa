# Tokenizer

`PhonetokTokenizer`, in `orthography2ipa.phonetok`, splits text into the graphemes of one language spec and expands each grapheme into its IPA candidates. The same class works for every spec in the registry, because all language knowledge comes from the spec. This page covers tokenization, maximal munch, the beam search (`ipa_beam`), allophone expansion and special characters. The [pronunciation lattice](lattice.md) page covers the per-grapheme lattice, its costs, rescoring and the confidence signal.

## Core concepts

### Maximal munch

At each position the tokenizer takes the longest grapheme key in the spec's table. A digraph or trigraph therefore wins over the single letters it contains. Portuguese ⟨ch⟩ is one grapheme read /ʃ/, not ⟨c⟩ followed by ⟨h⟩:

```python
import orthography2ipa
from orthography2ipa.phonetok import PhonetokTokenizer

tok = PhonetokTokenizer(orthography2ipa.get("pt-PT"))
for word in ("chuva", "lhano"):
    print(word, [t.grapheme for t in tok.grapheme_tokens(word)], tok.ipa_best(word))
```

```text
chuva ['ch', 'u', 'v', 'a'] ʃuvɐ
lhano ['lh', 'a', 'n', 'o'] ʎanu
```

### IPA Ambiguity and Beam Search

Many graphemes map to several IPA values. The number of whole-word readings is the product of the candidate counts of its graphemes, so it grows fast with word length. English ⟨ice⟩ has three candidates for ⟨i⟩, two for ⟨c⟩ and four for ⟨e⟩, which gives 24 readings:

```python
tok = PhonetokTokenizer(orthography2ipa.get("en-GB"))
print(len(tok.ipa_beam("ice", beam_width=-1)))
for path in tok.ipa_beam("ice", beam_width=4):
    print(path)
```

```text
24
IPAPath('aɪs', score=0.0)
IPAPath('aɪk', score=1.0)
IPAPath('aɪsɛ', score=1.0)
IPAPath('ɪs', score=1.0)
```

The beam search keeps only the `beam_width` cheapest partial readings at each grapheme. Every candidate has a cost, and a reading's score is the sum of the costs of its candidates. Without candidate weights the cost is the rank: the first candidate costs 0, the second 1, and so on. A spec can attach weights to a grapheme, and then the cost is `-log p`. The [lattice page](lattice.md#how-cost-works) explains the two cost regimes, and [lattice.md](lattice.md#how-cost-works) gives the weight format.

The rank comes from the context, not only from the flat grapheme table. The beam resolves each grapheme through the spec's [positional overrides](positional_graphemes.md). In ⟨ice⟩ the flat table lists /k/ first for ⟨c⟩, but the override for a ⟨c⟩ before a front vowel ranks /s/ first. The word-final ⟨e⟩ ranks its silent reading first for the same reason.

## Classes

### `TokenKind`

Every token has one of these kinds.

| Member | Meaning |
| --- | --- |
| `GRAPHEME` | A grapheme from the language's table |
| `WHITESPACE` | A run of whitespace characters |
| `PUNCTUATION` | A punctuation mark |
| `DIGIT` | A run of consecutive digits |
| `UNKNOWN` | A character that no grapheme, punctuation or digit rule matches |
| `BOS` | Beginning-of-sequence sentinel |
| `EOS` | End-of-sequence sentinel |

### `Token`

A `Token` is a frozen dataclass with these fields.

| Field | Type | Meaning |
| --- | --- | --- |
| `kind` | `TokenKind` | The kind of token |
| `grapheme` | `str` | The table key it matched, lower-cased for `GRAPHEME` tokens and in its original case for the others |
| `ipa` | `tuple[str, ...]` | The flat-table IPA candidates, empty for every kind except `GRAPHEME` |
| `position` | `int` | Character offset into the normalised input |
| `length` | `int` | Number of characters the token consumed |

The `grapheme` key is not always the full input span. An abugida consonant followed by a virama matches the bare consonant key and consumes the virama too. Use `length`, or `token.text_span(text)` on the normalised text, to recover the characters that the token consumed.

```python
tok = PhonetokTokenizer(orthography2ipa.get("es"))
for t in tok.tokenize("niño"):
    print(repr(t))
```

```text
Token(GRAPHEME, 'n', [n], pos=0)
Token(GRAPHEME, 'i', [i], pos=1)
Token(GRAPHEME, 'ñ', [ɲ], pos=2)
Token(GRAPHEME, 'o', [o|ɔ], pos=3)
```

### `IPAPath`

`ipa_beam` returns a list of `IPAPath` objects. Each one is a whole reading of the input.

| Field | Type | Meaning |
| --- | --- | --- |
| `segments` | `tuple[str, ...]` | The IPA chosen for each `GRAPHEME` token |
| `score` | `float` | The summed cost of the chosen candidates, lower is better |
| `graphemes` | `tuple[str, ...]` | The grapheme key behind each segment, or empty when the producer did not record it |
| `ipa` | property, `str` | The segments joined into one string |

For a spec without weights, `score` counts how far down its candidate list each choice went. A score of 0 means every grapheme took its first candidate.

## `PhonetokTokenizer`

### Constructor

```python
PhonetokTokenizer(spec, *, add_bos=False, add_eos=False, collapse_whitespace=True)
```

| Parameter | Default | Effect |
| --- | --- | --- |
| `spec` | required | The `LanguageSpec` that supplies the grapheme table |
| `add_bos` | `False` | Put a `BOS` token before every `tokenize()` result |
| `add_eos` | `False` | Put an `EOS` token after every `tokenize()` result |
| `collapse_whitespace` | `True` | Store each whitespace run as a single space in `grapheme`, while `length` keeps the real width |

The constructor builds a prefix trie from `spec.graphemes`. It also adds every key that exists only in `spec.positional_graphemes`, so that the trie can match it. Such a key gets its `DEFAULT` positional candidates as its flat IPA, or its first declared position when it has no `DEFAULT`.

### `tokenize(text)`

`tokenize` returns every token, including whitespace and punctuation, so the structure of the text survives. Before the scan, it normalises the text to NFC and removes the diacritics the spec lists in `fold_diacritics`. For an Arabic-script spec, it also decomposes presentation forms and, if the spec models shadda, expands gemination.

The scan then goes left to right. At each position it tries whitespace, punctuation, digits, the longest grapheme, and finally a single unknown character, in that order. A grapheme wins over punctuation when the spec claims the punctuation characters, as Tetum does with the apostrophe.

```python
tok_en = PhonetokTokenizer(orthography2ipa.get("en"))
for t in tok_en.tokenize("the cat sat."):
    print(f"{t.kind.name:12s}  {t.grapheme!r:8s}  {t.ipa}")
```

```text
GRAPHEME      'th'      ('θ', 'ð')
GRAPHEME      'e'       ('ɛ', 'iː', 'ə')
WHITESPACE    ' '       ()
GRAPHEME      'c'       ('k', 's')
GRAPHEME      'a'       ('æ', 'ɑː', 'eɪ', 'ə', 'ɔː')
GRAPHEME      't'       ('t',)
WHITESPACE    ' '       ()
GRAPHEME      's'       ('s', 'z')
GRAPHEME      'a'       ('æ', 'ɑː', 'eɪ', 'ə', 'ɔː')
GRAPHEME      't'       ('t',)
PUNCTUATION   '.'       ()
```

The `ipa` on a token is the flat-table list. It does not apply positional overrides. Two helpers wrap `tokenize`: `graphemes(text)` returns the `grapheme` string of every token, and `grapheme_tokens(text)` returns the `GRAPHEME` tokens only.

### `ipa_beam(text, ...)`

```python
def ipa_beam(
    self,
    text: str,
    *,
    beam_width: int = 8,
    expand_allophones: bool = False,
    word_separator: str = " ",
    include_special: bool = False,
    length_norm: bool = False,
    diversity: float = 0.0,
    rescorer=None,
) -> List[IPAPath]: ...
```

| Parameter | Default | Effect |
| --- | --- | --- |
| `beam_width` | `8` | Maximum number of partial readings kept at each grapheme. `-1` keeps all of them |
| `expand_allophones` | `False` | Branch each phoneme into its variants from `spec.allophones` (see [Allophone expansion](#allophone-expansion)) |
| `word_separator` | `" "` | The string written for a whitespace token when `include_special` is true |
| `include_special` | `False` | Write whitespace, punctuation, digits and unknown characters into the reading as literal strings |
| `length_norm` | `False` | Report each score as the mean cost per segment |
| `diversity` | `0.0` | Demote readings that are near copies of a better one |
| `rescorer` | `None` | One `LatticeRescorer` or a list of them, applied before the beam picks a path (see [Rescoring the lattice](lattice.md#rescoring-the-lattice)) |

`ipa_beam` returns the readings sorted by score, best first:

```python
tok_es = PhonetokTokenizer(orthography2ipa.get("es"))
for p in tok_es.ipa_beam("ciudad", beam_width=6):
    print(f"score={p.score:.1f}  /{p.ipa}/")
```

```text
score=0.0  /θjuðað/
score=1.0  /kjuðað/
score=1.0  /θjudað/
score=1.0  /θjuðad/
score=2.0  /kjuðad/
score=2.0  /θjudad/
```

`length_norm=True` divides each score by the number of segments. The beam still prunes on the raw cost. All readings of one word share a segment count, so the order stays the same and only the scale changes. The normalised score lets you compare inputs of different lengths.

`diversity=λ`, with λ above zero, re-ranks the returned readings by Maximal Marginal Relevance. The best reading stays first. Each next pick minimises its score plus λ times its largest segment overlap with a reading already picked. On a long word, the raw beam fills with readings that differ from the best one in a single grapheme. This pass pushes them down. The score values themselves do not change.

```python
tok = PhonetokTokenizer(orthography2ipa.get("en-GB"))
for kwargs in ({}, {"diversity": 5.0}):
    paths = tok.ipa_beam("weather", beam_width=8, **kwargs)
    print([(p.ipa, round(p.score, 2)) for p in paths[:4]])
```

```text
[('wiːðəɹ', 0.22), ('wiːθəɹ', 1.22), ('wɛðəɹ', 1.22), ('wiːðɜːɹ', 1.61)]
[('wiːðəɹ', 0.22), ('wɛθəɹ', 2.22), ('wiːθəɹ', 1.22), ('wɛðəɹ', 1.22)]
```

### `ipa_best(text, ...)`

`ipa_best` returns the IPA string of the best reading. It is equal to `ipa_beam(text, beam_width=1)[0].ipa`, and it takes the same `expand_allophones`, `word_separator`, `include_special` and `rescorer` arguments.

### `ipa_lattice(text, ...)`

`ipa_lattice` returns the same search space as ranked candidates per grapheme, instead of whole-word strings. The [pronunciation lattice](lattice.md) page describes it.

## Allophone expansion

With `expand_allophones=True`, the beam branches each phoneme into the variants that `spec.allophones` lists for it. The first variant keeps the phoneme's cost. Each later variant adds 0.5 per place down the list.

```python
tok = PhonetokTokenizer(orthography2ipa.get("es"))
for p in tok.ipa_beam("habla", beam_width=10, expand_allophones=True):
    print(p.score, p.ipa)
```

```text
0.0 abla
0.5 aβla
```

This expansion ignores context. It lists the surface variants, for example to generate pronunciation variants or to count allophones, and it does not choose between them. The context-conditioned choice of an allophone is the job of the spec's `allophone_rules`, which the full engine runs. See [allophony.md](allophony.md).

## Special characters

### Digits

A run of digits is one `DIGIT` token:

```python
tok = PhonetokTokenizer(orthography2ipa.get("es"))
print([(t.kind.name, t.grapheme) for t in tok.tokenize("hay 3 gatos")])
```

```text
[('GRAPHEME', 'h'), ('GRAPHEME', 'a'), ('GRAPHEME', 'y'), ('WHITESPACE', ' '), ('DIGIT', '3'), ('WHITESPACE', ' '), ('GRAPHEME', 'g'), ('GRAPHEME', 'a'), ('GRAPHEME', 't'), ('GRAPHEME', 'o'), ('GRAPHEME', 's')]
```

### Unknown characters

A character that matches no grapheme, whitespace, digit or punctuation rule becomes an `UNKNOWN` token:

```python
print([(t.kind.name, t.grapheme) for t in tok.tokenize("café你")])
```

```text
[('GRAPHEME', 'c'), ('GRAPHEME', 'a'), ('GRAPHEME', 'f'), ('GRAPHEME', 'é'), ('UNKNOWN', '你')]
```

The full engine counts these characters against the word's coverage, which lowers its [confidence](lattice.md#per-word-confidence--oov-signal).

### Case

The tokenizer lower-cases text before the trie lookup, so ⟨CH⟩ and ⟨ch⟩ both match the `ch` key. The `grapheme` field of a `GRAPHEME` token holds the lower-case form. For Turkish (`tr` and its subtags) the lower-casing maps the dotted and dotless I explicitly.

## Context model

`tokenize()` returns a flat list. When a consumer must reason about the surroundings of a grapheme, `tokenize_with_context()` returns a `TokenSequence`. It wraps every `GRAPHEME` token in a `GraphemeContext`, and iteration, indexing and `len()` work on these contexts. The full token list stays available as `seq.tokens`.

```python
tok = PhonetokTokenizer(orthography2ipa.get("es-ES"))
for c in tok.tokenize_with_context("cera"):
    print(c.grapheme, c.span, c.is_vowel, c.is_front)
```

```text
c (0, 1) False False
e (1, 2) True True
r (2, 3) False False
a (3, 4) True False
```

### Neighbours

Neighbours are word-local. They never cross a whitespace, punctuation, digit or unknown token.

| Member | Returns |
| --- | --- |
| `prev`, `next` | The adjacent grapheme, or `None` at a word edge |
| `at(offset)` | The grapheme `offset` places away, such as `at(2)` or `at(-1)`, or `None` past a word edge |
| `neighbors(n=1)` | Up to `2*n` graphemes within `±n`, left to right, without `self`, clamped at the word edges |
| `index` | The position of this grapheme among all graphemes of the sequence |

### Span

`span` gives the `(start, end)` character offsets of the grapheme. The offsets index the NFC-normalised input that `tokenize()` reads, and `grapheme` is lower-cased. The exact contract is:

```python
unicodedata.normalize("NFC", text)[start:end].lower() == grapheme
```

A raw `text[start:end]` against the caller's string matches only when that string is already lower-case NFC. It fails for upper-case input and for NFD input.

### Class predicates

The predicates delegate to `orthography2ipa.vowels`, which is the one place where the library classifies vowels.

| Predicate | True when |
| --- | --- |
| `is_vowel` | The grapheme is a written vowel |
| `is_consonant` | The grapheme is not a vowel |
| `is_front`, `is_back` | The grapheme is a front or a back vowel |
| `is_palatal` | The first IPA candidate is a palatal or palato-alveolar consonant |
| `is_emphatic` | The first IPA candidate is pharyngealized (it carries ˤ) |

The vowel predicates read the grapheme's leading character for Latin and Greek. For other scripts they read the spec's flat IPA for the grapheme, then the Unicode name of the character. A spec's `vowel_graphemes` list overrides all of this for the whole graphemes it names. A consonant digraph such as ⟨ch⟩ is therefore a consonant, and a vowel digraph such as ⟨ai⟩ reports by its leading vowel.

### Why it exists

Without the context model, a phonemizer built on this library does its own index arithmetic and keeps its own vowel list. A rule such as "⟨c⟩ is soft before a front vowel" then needs every accented front vowel spelled out by hand. With the context model, one shared predicate covers them:

```python
def c_readings(word):
    return ["θ" if c.next is not None and c.next.is_front else "k"
            for c in tok.tokenize_with_context(word) if c.grapheme == "c"]

print(c_readings("cecina"), c_readings("cocí"), c_readings("acción"))
```

```text
['θ', 'θ'] ['k', 'θ'] ['k', 'θ']
```

`is_front` already covers ⟨e i y⟩ and their accented forms, so the rule cannot drift from the rest of the library's vowel classification.

### The beam uses the context model

`ipa_beam`, `ipa_best` and `ipa_lattice` build a `TokenSequence` internally. They resolve each grapheme against the spec's [positional overrides](positional_graphemes.md) through the shared resolver in `orthography2ipa.positional`, the same resolver the full `G2P` engine uses. The standalone beam is therefore context-aware, and it is not a flat product of the grapheme table.

Some stages exist only in the engine. The engine adds syllable and stress context, so the stress-conditioned positions fire there and not in the standalone beam. It also runs the spec's `allophone_rules`, its `word_exceptions` and `grammatical_endings`, cross-word sandhi and stress marking.

## Performance

The trie is built once, at construction, and every later call reuses it. The cost of `tokenize()` is O(n·k), where n is the text length and k is the longest grapheme key. The cost of `ipa_beam()` is O(n · beam_width · candidates per grapheme), which suits words and short phrases. The context view of `tokenize_with_context()` adds one O(n) pass. Its neighbour lookups `prev`, `next` and `at` are O(1). For a long document, tokenize one sentence at a time.

---
[← Architecture](architecture.md) · [Home](../index.md) · [The pronunciation lattice →](lattice.md)
