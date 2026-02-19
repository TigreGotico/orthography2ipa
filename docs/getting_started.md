# Getting Started

## Installation

```bash
pip install orthography2ipa
```

The package depends on **phonematcher** for its 21-feature distinctive-feature system. This is installed automatically as a dependency.

---

## Quick Start

### 1. Fetch a language spec

```python
import orthography2ipa

# By BCP-47 code
en = orthography2ipa.get("en")
es = orthography2ipa.get("es")
pt = orthography2ipa.get("pt")
pt_br = orthography2ipa.get("pt-BR")

# By ISO 639-3 code (aliases are supported)
eng = orthography2ipa.get("eng")   # same as "en"
por = orthography2ipa.get("por")   # same as "pt"
```

### 2. Explore grapheme → IPA mappings

```python
# Each grapheme key maps to a list of possible IPA phonemes
en.graphemes["th"]     # ['θ', 'ð']   — voiceless and voiced dental fricative
en.graphemes["c"]      # ['k', 's']   — /k/ or /s/
es.graphemes["c"]      # ['k', 'θ']   — Castilian: /k/ or /θ/
es.graphemes["ll"]     # ['ʎ', 'ʝ']  — traditional lleísmo vs yeísmo
pt_br.graphemes["lh"]  # ['ʎ']        — palatal lateral (unique to Portuguese)

# Digraphs are first-class keys
es.graphemes["ch"]     # ['tʃ']
en.graphemes["sh"]     # ['ʃ']
```

### 3. Explore allophone inventories

```python
# Allophones are the contextual surface realisations of phonemes
en.allophones["t"]     # ['t', 'tʰ', 'ɾ', 'ʔ', 't̚']
# tʰ = aspirated (word-initial), ɾ = flap (intervocalic), ʔ = glottalised, t̚ = unreleased

es.allophones["b"]     # ['b', 'β']
# b = after pause/nasal, β = intervocalic (lenition)

es.allophones["n"]     # ['n', 'm', 'ɱ', 'n̪', 'ŋ', 'ɲ']
# nasal place assimilation
```

### 4. Tokenise text and get IPA paths

```python
from orthography2ipa.phonetok import PhonetokTokenizer

tok = PhonetokTokenizer(orthography2ipa.get("pt-BR"))

# Tokenise — returns a list of Token objects
tokens = tok.tokenize("chuva")
print([t.grapheme for t in tokens])  # ['ch', 'u', 'v', 'a']

# Get all possible IPA transcriptions (beam search)
paths = tok.ipa_beam("chuva", beam_width=4)
print(paths[0].ipa)   # 'ʃuva'
print(paths[0].score) # 0.0 (most canonical path)
```

### 5. Measure phonological distance

```python
from orthography2ipa.distance import phonological_distance, segment_distance

# Distance between two IPA segments
d_pb = segment_distance("p", "b")   # 0.0625 — differ only in voicing
d_pa = segment_distance("p", "a")   # 0.75   — consonant vs vowel

# Distance between languages
la = orthography2ipa.get("la")
it = orthography2ipa.get("it")
dist = phonological_distance(la, it)
print(dist.combined)           # ~0.31
print(dist.inventory.jaccard)  # ~0.40
```

---

## Language Codes

The package uses **BCP-47** codes as the primary identifier:

| Code | Language |
|---|---|
| `en` | English |
| `es` | Spanish (Castilian) |
| `es-AR` | Rioplatense Spanish |
| `pt` | Portuguese (European) |
| `pt-BR` | Brazilian Portuguese |
| `pt-BR-x-rj` | Rio de Janeiro Portuguese |
| `fr` | French |
| `it` | Italian |
| `la` | Classical Latin |
| `de` | German |
| `eu` | Basque |
| `ar` | Arabic |
| `zh` | Mandarin Chinese |
| `ja` | Japanese |

For the full list, see [Language Registry](registry.md) or call:

```python
orthography2ipa.available_codes()
```

ISO 639-3 three-letter codes are also accepted as aliases:

```python
orthography2ipa.get("por")  # → pt
orthography2ipa.get("spa")  # → es
orthography2ipa.get("lat")  # → la
```

---

## Inspecting Language Metadata

Every `LanguageSpec` carries rich metadata:

```python
spec = orthography2ipa.get("es")
print(spec.name)     # "Spanish (Castilian)"
print(spec.family)   # "Romance"
print(spec.script)   # "Latin"
print(spec.notes)    # free-form linguistic notes

# Ancestry
print(spec.primary_parent)      # "la-x-hispania"
print(spec.substrate_codes)     # ('xaq',)  ← Basque substrate
print(spec.contact_codes)       # ('xaq', 'xaa', 'got')

for anc in spec.get_ancestors():
    print(anc)
# Ancestor('la-x-hispania', parent, w=0.80)
# Ancestor('xaq', substrate, w=0.08)
# Ancestor('xaa', adstrate, w=0.07)
# Ancestor('got', superstrate, w=0.05)
```

---

## Error Handling

```python
try:
    spec = orthography2ipa.get("xx")
except KeyError as e:
    print(e)  # "Language 'xx' is not registered. Available: ..."
```
