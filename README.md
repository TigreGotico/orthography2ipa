# ipa-mappings

Linguistically motivated **grapheme→IPA** and **allophone** mappings for 25+ languages.

## What this is

A pure-data Python package providing two things per language:

1. **Graphemes** — orthographic units (individual characters + official digraphs/trigraphs/diphthongs) mapped to their canonical IPA phoneme(s)
2. **Allophones** — each phoneme mapped to its positional / contextual surface realisations

Only linguistically motivated mappings based on official orthography and grammar are included. No arbitrary n-grams. No digit-to-word mappings. No search or clustering logic.

## Installation

```bash
pip install ipa-mappings
```

## Quick start

```python
import orthography2ipa

# Get a language spec
en = orthography2ipa.get("en")

# Grapheme → IPA
en.graphemes["th"]    # ['θ', 'ð']
en.graphemes["ough"]  # ['ɔː', 'oʊ', 'ʌf', 'ɒf', 'aʊ', 'uː']

# Allophone map
en.allophones["t"]    # ['t', 'tʰ', 'ɾ', 'ʔ', 't̚']
en.allophones["l"]    # ['l', 'ɫ']

# Metadata
en.name    # 'English'
en.family  # 'Germanic'
en.script  # 'Latin'
en.notes   # '...'

# Regional variants
pt_br = orthography2ipa.get("pt-BR")
pt_br.graphemes["t"]  # ['t', 'tʃ']   — palatalisation before /i/
pt_br.parent          # 'pt'

# List everything
orthography2ipa.available_codes()
# ['ar', 'ca', 'cs', 'da', 'de', 'el', 'en', 'es', 'es-419', 'es-AR', ...]
```

## Languages

| Family     | Codes                                      |
|------------|--------------------------------------------|
| Romance    | `pt`, `pt-BR`, `pt-AO`, `gl`, `es`, `es-419`, `es-AR`, `ca`, `oc`, `fr`, `it`, `ro` |
| Germanic   | `en`, `de`, `nl`, `sv`, `da`, `no`         |
| Slavic     | `ru`, `uk`, `pl`, `cs`                     |
| Semitic    | `ar`                                       |
| Iranian    | `fa`                                       |
| Indo-Aryan | `hi`                                       |
| Sinitic    | `zh` (Pinyin)                              |
| Japonic    | `ja` (Hiragana/Katakana)                   |
| Koreanic   | `ko` (Jamo)                                |
| Turkic     | `tr`                                       |
| Uralic     | `fi`                                       |
| Hellenic   | `el`                                       |
| Isolate    | `eu` (Basque)                              |

ISO 639-3 codes also work: `orthography2ipa.get("eng")`, `orthography2ipa.get("por")`, etc.

## Design principles

- **Linguistically motivated only** — digraphs like English ⟨th⟩, Portuguese ⟨lh⟩, or German ⟨sch⟩ are included because they're standard orthographic units. Arbitrary substrings like "ti" → [ʃ] are excluded.
- **Graphemes ≠ allophones** — the grapheme map tells you what phonemes a spelling can represent. The allophone map tells you how a phoneme surfaces in context. These are distinct linguistic concepts.
- **Regional variants** — where pronunciation diverges systematically (e.g. Brazilian vs European Portuguese), separate `LanguageSpec` objects are provided with `parent` links.
- **Pure data, no logic** — this package provides mappings only. Context-dependent grapheme-to-phoneme conversion (G2P) requires rule engines or neural models on top.

## Data structure

```python
@dataclass(frozen=True)
class LanguageSpec:
    code: str              # 'en', 'pt-BR', etc.
    name: str              # 'English'
    family: str            # 'Germanic'
    script: str            # 'Latin'
    graphemes: dict[str, list[str]]   # 'th' → ['θ', 'ð']
    allophones: dict[str, list[str]]  # 'θ' → ['θ']
    parent: str | None     # 'pt' for 'pt-BR'
    notes: str             # caveats, sources
```

## Contributing

To add a new language, create `orthography2ipa/languages/{code}.py` following the pattern of existing files. Each module must export a `SPECS` dict mapping language codes to `LanguageSpec` objects, then register the codes in `registry.py`.

## License

Apache 2.0
