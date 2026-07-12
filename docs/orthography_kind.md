# Native scripts, romanizations and transliterations

A spec's `graphemes` map says "this writing produces these sounds". But *which*
writing? Han characters, Pinyin and Buckwalter ASCII are three different claims
about three different things, and a consumer must be able to tell them apart. The
`orthography_kind` field says which one a spec is making.

| `orthography_kind` | What the graphemes are | Standards body | Example |
|---|---|---|---|
| `native` | The language's own writing system | Usually | `zh-Hani` (Han), `ar` (Arabic), `en-GB` (Latin) |
| `romanization` | An alternative orthography **people actually read and write** | Yes | `zh` (Pinyin, ISO 7098) |
| `transliteration` | A lossless machine re-encoding of **another script** | No — that absence is the tell | `ar-Latn-buckwalter` |

```python
import orthography2ipa
from orthography2ipa import OrthographyKind

orthography2ipa.get("zh").orthography_kind                   # OrthographyKind.ROMANIZATION
orthography2ipa.get("zh-Hani").orthography_kind              # OrthographyKind.NATIVE
orthography2ipa.get("ar-Latn-buckwalter").orthography_kind   # OrthographyKind.TRANSLITERATION
```

`native` is the default, so any spec that says nothing is claiming to read the
language's own script.

## A romanization is an orthography; a transliteration is an encoding

The distinction is not cosmetic:

- A **romanization** is a real orthography *of the language*. Pinyin is taught,
  legislated and standardised (ISO 7098); it is what a Chinese primary-school
  child writes. It is also a plain alphabet, which is exactly why it can be
  transcribed by rules when the native script cannot.
- A **transliteration** is a re-encoding of *another script*, for machines.
  Nobody reads Buckwalter as a language. It inherits every property of the script
  it re-encodes — including the limits.

```python
from orthography2ipa import G2P

G2P("zh").transcribe("beijing")   # 'peitɕiŋ' — Pinyin in, IPA out
```

`zh` therefore reads **Pinyin, not Hanzi**, and says so. Converting Han text to
Pinyin is a dictionary lookup (CC-CEDICT and friends), which this library does not
perform.

## Buckwalter cannot escape the abjad

A transliteration that changed the pronunciation would not be a transliteration.
`ar` and `ar-Latn-buckwalter` are the same word in two encodings and give one IPA:

```python
from orthography2ipa import G2P

G2P("ar").transcribe("كَتَبَ")                    # vocalised Arabic
G2P("ar-Latn-buckwalter").transcribe("kataba")   # ...the same string of IPA
```

And re-encoding cannot recover information the script never wrote. Unvocalised
Buckwalter is exactly as unreadable as unvocalised Arabic — the short vowels are
absent from both, and nothing invents them back:

```python
from orthography2ipa import G2P

g = G2P("ar-Latn-buckwalter")
g.transcribe("kataba") != g.transcribe("ktb")   # True — and the bare form has no vowels
```

## The native Han spec is honest about being unreadable

A Han character does not encode sound; its reading depends on the word it sits in.
So `zh-Hani` has **no grapheme map at all**, and that empty map is the answer, not
a gap someone forgot to fill:

```python
import orthography2ipa

han = orthography2ipa.get("zh-Hani")
han.graphemes    # {} — there is no grapheme→IPA rule to write
han.phonemes     # ...yet the phonology is fully declared
```

The input contract for Han text is a **dictionary** — a lexical lookup — not a
phonological rule, and that is a statement about the writing system rather than a
shortcoming of the engine. The romanization walks around it: Pinyin is rule-readable
because it is an alphabet.

This is also why the [phoneme inventory](data_model.md#phonemes--the-inventory-stated-directly)
is declared separately from the graphemes. A language's sounds are not a property
of its writing system, and `zh-Hani` is the proof: no orthography the rules can
read, and a complete phonology regardless.

---

**Navigation:** [Docs home](index.md) · [Data model](data_model.md) · [Registry](registry.md) · [Adding a language](adding_a_language.md)
