# orthography2ipa — Documentation

**orthography2ipa** is a Python package providing linguistically motivated grapheme-to-IPA (International Phonetic Alphabet) mappings and allophone inventories for 50+ languages and dialects. It is designed for researchers, NLP engineers, and computational linguists who need accurate orthographic-to-phonemic conversion grounded in the phonological literature.

---

## Documentation Contents

| Document | Description |
|---|---|
| [Getting Started](getting_started.md) | Installation, quickstart, and first examples |
| [Architecture](architecture.md) | Package structure, modules, design decisions |
| [Data Model](data_model.md) | `LanguageSpec`, `Grapheme2IPA`, `AllophoneMap`, ancestry types |
| [Language Registry](registry.md) | All supported languages, codes, families |
| [Tokenizer](tokenizer.md) | `PhonetokTokenizer`, beam search, `Token`, `IPAPath` |
| [Distance Metrics](distance.md) | Segment, inventory, grapheme, allophone, and combined distances |
| [Ancestry System](ancestry.md) | `Ancestor`, `AncestorRole`, phylogenetic distance, substrate/superstrate |
| [Adding a Language](adding_a_language.md) | Step-by-step guide to contributing a new language mapping |
| [Linguistic Accuracy Guide](linguistic_accuracy.md) | Standards, sources, and methodology for phonological data |
| [IPA Reference](ipa_reference.md) | IPA symbols used in the package and their feature values |

---

## Package at a Glance

```python
import orthography2ipa

# Fetch a language spec
en = orthography2ipa.get("en")
es = orthography2ipa.get("es")
pt_br = orthography2ipa.get("pt-BR")

# Inspect grapheme→IPA mappings
en.graphemes["th"]         # ['θ', 'ð']
es.graphemes["ll"]         # ['ʎ', 'ʝ']
pt_br.graphemes["lh"]      # ['ʎ']

# Inspect allophone inventories
en.allophones["t"]         # ['t', 'tʰ', 'ɾ', 'ʔ', 't̚']
es.allophones["b"]         # ['b', 'β']

# Tokenize and get IPA paths
from orthography2ipa.phonetok import PhonetokTokenizer
tok = PhonetokTokenizer(es)
paths = tok.ipa_beam("ciudad", beam_width=4)

# Measure phonological distance
from orthography2ipa.distance import phonological_distance
d = phonological_distance(orthography2ipa.get("la"), orthography2ipa.get("it"))
print(d.combined)   # ~0.31

# List available languages
orthography2ipa.available_codes()
orthography2ipa.available_families()
```

---

## Design Goals

1. **Linguistic accuracy over simplicity** — every mapping is grounded in published phonological descriptions. Sources are cited in each module.
2. **Dialect coverage** — standard varieties are not enough; the package covers dozens of regional dialects with their own phonological quirks.
3. **Layered ancestry** — languages carry structured ancestry metadata (parent, substrate, superstrate, adstrate) that enables phylogenetically-informed distance calculations.
4. **Separation of concerns** — grapheme mappings, allophone inventories, tokenization, and distance metrics are cleanly separated.
5. **Composability** — dialect modules extend parent modules rather than duplicating data.

---

## Version

Current version: **0.1.0**
