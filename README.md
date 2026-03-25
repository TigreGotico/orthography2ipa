# orthography2ipa

Linguistically motivated **grapheme→IPA** and **allophone** mappings for **310+ language codes** across 20+ language families.

## What this is

A pure-data Python package providing per language:

1. **Graphemes** — orthographic units (characters, digraphs, trigraphs) mapped to canonical IPA phoneme(s)
2. **Allophones** — each phoneme mapped to its positional / contextual surface realisations
3. **Positional graphemes** — context-sensitive overrides (word-initial, intervocalic, etc.)
4. **Language ancestry** — multi-ancestor relationships with weighted contributions
5. **Phonological distance** — feature-based metrics for cross-language comparison
6. **IPA tokenizer** — maximal-munch grapheme tokenizer with beam-search IPA expansion

Only linguistically motivated mappings based on official orthography and grammar are included.

## Installation

```bash
pip install orthography2ipa
```

For Arabic G2P support (optional):
```bash
pip install orthography2ipa[arabic]
```

## Quick start

### Python API

```python
import orthography2ipa

# Get a language spec
en = orthography2ipa.get("en-GB")

# Grapheme → IPA
en.graphemes["th"]    # ['θ', 'ð']

# Allophone map
en.allophones["t"]    # ['t', 'tʰ', 'ɾ', 'ʔ', 't̚']

# Metadata
en.name    # 'British English'
en.family  # 'Germanic'
en.script  # 'Latin'

# Regional variants
pt_br = orthography2ipa.get("pt-BR")
pt_br.graphemes["t"]  # ['t', 'tʃ']   — palatalisation before /i/

# List everything
orthography2ipa.available_codes()
orthography2ipa.available_families()
```

### Command-line interface

After installation, the `orthography2ipa` command is available:

```bash
# List available languages
orthography2ipa list
orthography2ipa list --families
orthography2ipa list --family Romance

# Show language info
orthography2ipa info pt-BR
orthography2ipa info pt-BR --graphemes
orthography2ipa info pt-BR --json

# Transcribe text to IPA
orthography2ipa transcribe pt-BR "chuva"
orthography2ipa transcribe en-GB "through" --beam 8

# Phonological distance between languages
orthography2ipa distance pt-BR pt-PT
orthography2ipa distance es-ES it-IT --json
```

All subcommands support `--json` for machine-readable output.

## Languages

| Family     | Examples |
|------------|----------|
| Romance    | `pt-PT`, `pt-BR`, `es-ES`, `es-AR`, `ca`, `fr-FR`, `it-IT`, `ro-RO`, `gl`, `oc`, `sc`, `an` |
| Germanic   | `en-GB`, `de-DE`, `nl-NL`, `sv-SE`, `da-DK`, `no-NO`, `af` |
| Slavic     | `ru-RU`, `uk-UA`, `pl-PL`, `cs-CZ`, `sr-RS`, `hr-HR`, `bg-BG` |
| Celtic     | `cy`, `ga`, `gd`, `br`, `kw`, `gv` |
| Indo-Aryan | `hi-IN`, `bn-BD`, `ur-PK`, `ne-NP`, `pa`, `gu`, `mr` |
| Semitic    | `ar`, `he-IL`, `mt` |
| Turkic     | `tr-TR`, `az`, `kk`, `uz` |
| Hellenic   | `el-GR` |
| Uralic     | `fi-FI`, `hu-HU`, `et-EE` |
| Japonic    | `ja` |
| Sinitic    | `zh` |
| Koreanic   | `ko` |

310+ codes total. ISO 639-3 aliases work: `orthography2ipa.get("eng")`, `orthography2ipa.get("por")`, etc.

## Data structure

```python
@dataclass(frozen=True)
class LanguageSpec:
    code: str                              # 'pt-BR'
    name: str                              # 'Brazilian Portuguese'
    family: str                            # 'Romance'
    script: str                            # 'Latin'
    graphemes: Dict[str, List[str]]        # 'th' → ['θ', 'ð']
    allophones: Dict[str, List[str]]       # 'θ' → ['θ']
    positional_graphemes: Dict[...]        # context-sensitive overrides
    parent: Optional[str]                  # primary parent code
    ancestors: Tuple[Ancestor, ...]        # multi-ancestor lineage
    quality: QualityTier                   # stub, skeleton, research, production
    script_type: ScriptType                # alphabet, abjad, abugida, ...
    sandhi_rules: Tuple[SandhiRule, ...]   # cross-word rules
    tone_inventory: Optional[Dict]         # tone marks → labels
    sources: Tuple[LinguisticSource, ...]  # bibliographic references
```

## Design principles

- **Linguistically motivated only** — digraphs like English ⟨th⟩, Portuguese ⟨lh⟩, or German ⟨sch⟩ are included because they're standard orthographic units. Arbitrary substrings are excluded.
- **Graphemes ≠ allophones** — the grapheme map tells you what phonemes a spelling can represent. The allophone map tells you how a phoneme surfaces in context.
- **Regional variants** — where pronunciation diverges systematically, separate `LanguageSpec` objects are provided with ancestry links.
- **Multi-ancestor inheritance** — JSON data files support `graphemes_base`/`allophones_base` for dialect trees.
- **Pure data, pluggable logic** — mappings are declarative JSON; algorithmic G2P (e.g. Arabic) uses the plugin system.

## Contributing

To add a new language, create `orthography2ipa/data/{code}.json` following `data/SCHEMA.md`. For dialects, use `graphemes_base`/`allophones_base` to inherit from the parent.

## License

Apache 2.0
