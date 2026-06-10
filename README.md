# orthography2ipa

Linguistically motivated **grapheme→IPA** and **allophone** mappings for **350+ language codes** across 20+ language families — pure data, a maximal-munch IPA tokenizer, and a family of phonological/script distance metrics, with no trained weights to ship.

Only mappings grounded in official orthography and documented grammar are included. Arbitrary substring rules are excluded.

## Why two maps

The central distinction the package enforces:

- A **grapheme map** tells you which phonemes a spelling *can* represent. English ⟨th⟩ → `['θ', 'ð']`.
- An **allophone map** tells you how a phoneme *surfaces* in context. English /t/ → `['t', 'tʰ', 'ɾ', 'ʔ', 't̚']`.

Keeping these separate lets you go from text to phoneme candidates (transcription) and from phonemes to surface realisations (pronunciation modelling) without conflating the two.

## What each language carries

Every `LanguageSpec` provides:

1. **Graphemes** — orthographic units (characters, digraphs, trigraphs) mapped to canonical IPA phonemes.
2. **Allophones** — each phoneme mapped to its positional/contextual surface realisations.
3. **Positional graphemes** — context-sensitive overrides (word-initial, intervocalic, before /i/, …).
4. **Ancestry** — weighted multi-ancestor lineage (parent, substrate, superstrate, adstrate, …) for dialect trees.
5. **Sandhi rules** — cross-word phonological processes.
6. **Tone inventory** — tone marks → labels, where applicable.
7. **Provenance** — `QualityTier` (stub → skeleton → research → production), `ScriptType`, and bibliographic sources.

Regional varieties get their own `LanguageSpec` objects linked through ancestry, and JSON data files support `graphemes_base`/`allophones_base` inheritance so a dialect only declares what differs from its parent.

## Installation

```bash
pip install orthography2ipa
```

For the optional Arabic G2P backend:

```bash
pip install orthography2ipa[arabic]
```

## Quick start

### Transcribe text to IPA

```python
import orthography2ipa

orthography2ipa.transcribe("olá mundo", "pt")        # 'oˈla ˈmundo'
orthography2ipa.transcribe("hello world", "en")       # 'hɛllɒ wɔːɹld'
orthography2ipa.transcribe("bona nuèit", "oc")        # 'buna nyɛjt'

# Beam search keeps ranked alternatives per word
from orthography2ipa import G2P

engine = G2P("pt-PT")
result = engine.transcribe_detailed("um café", search="beam", beam_width=4)
result.ipa                          # 'ˈum kaˈfɛ'
result.words[1].candidates          # ranked IPAPath alternatives

# The engine pipeline: normalize → tokenize → greedy/beam per word →
# stress marks (when the spec declares stress rules) → word-context
# pass → sandhi → dialect transform. A registered G2P plugin for the
# language (e.g. arbtok for Arabic) takes over automatically;
# use_plugins=False forces the data-driven path.
```

### Language specs

```python
import orthography2ipa

# Get a language spec
en = orthography2ipa.get("en-GB")

# Grapheme → IPA candidates
en.graphemes["th"]    # ['θ', 'ð']

# Allophone map: how /t/ surfaces
en.allophones["t"]    # ['t', 'tʰ', 'ɾ', 'ʔ', 't̚']

# Metadata
en.name               # 'British English (RP)'
en.family             # 'Germanic'
en.script             # 'Latin'

# Regional variants share ancestry but diverge where pronunciation does
pt_br = orthography2ipa.get("pt-BR")
pt_br.graphemes["t"]  # ['t', 't͡ʃ']   — palatalisation before /i/

# Bare tags, ISO 639-3 aliases and near matches all resolve
orthography2ipa.get("eng").name   # 'British English (RP)'
orthography2ipa.resolve("pt")     # 'pt-PT' — reference variety
orthography2ipa.resolve("en-NZ")  # 'en-GB' — nearest registered

# Discover what's available
orthography2ipa.available_codes()
orthography2ipa.available_families()
```

### IPA tokenizer

`PhonetokTokenizer` performs maximal-munch grapheme tokenization with beam-search IPA expansion, ranking candidate transcriptions when a spelling is ambiguous:

```python
from orthography2ipa import get
from orthography2ipa.phonetok import PhonetokTokenizer

tok = PhonetokTokenizer(get("en-GB"))

tok.ipa_best("through")              # 'θɹɔː'
for path in tok.ipa_beam("through", beam_width=8):
    print(path.ipa, path.score)      # θɹɔː 0.0, ðɹɔː 1.0, θɹoʊ 1.0, …
```

### Distance metrics

Compare two languages across inventory, grapheme, allophone, and ancestry dimensions:

```python
from orthography2ipa import get
from orthography2ipa.distance import phonological_distance

d = phonological_distance(get("pt-BR"), get("pt-PT"))
d.combined                    # 0.04 — near-identical
d.inventory.feature_mean      # phoneme-inventory distance
d.grapheme.mean_ipa_distance  # grapheme-mapping divergence
d.allophone_sim               # allophone-overlap similarity
```

Script-level distance and feature vectors are available via `script_distance.py` and `feats.py`.

## Command-line interface

After installation the `orthography2ipa` command is available. Every subcommand accepts `--json` for machine-readable output.

```bash
# List languages and families
orthography2ipa list
orthography2ipa list --families
orthography2ipa list --family Romance

# Inspect a language
orthography2ipa info pt-BR
orthography2ipa info pt-BR --graphemes
orthography2ipa info pt-BR --json

# Transcribe text to IPA
orthography2ipa transcribe pt "olá mundo"
orthography2ipa transcribe en-GB "through" --search beam --beam-width 8

# Phonological distance between two languages
orthography2ipa distance pt-BR pt-PT
orthography2ipa distance es-ES it-IT --json
```

## Languages

| Family     | Examples |
|------------|----------|
| Romance    | `pt-PT`, `pt-BR`, `es-ES`, `es-AR`, `ca`, `fr-FR`, `it-IT`, `ro-RO`, `gl`, `oc`, `sc`, `an` |
| Germanic   | `en-GB`, `de-DE`, `nl-NL`, `sv-SE`, `da-DK`, `no-NO`, `af` |
| Slavic     | `ru-RU`, `uk-UA`, `pl-PL`, `cs-CZ`, `sr-RS`, `hr-HR`, `bg-BG` |
| Celtic     | `cy`, `ga`, `gd`, `br`, `kw`, `gv` |
| Indo-Aryan | `hi-IN`, `bn-BD`, `ur-PK`, `ne-NP`, `pa`, `gu`, `mr` |
| Semitic    | `arb`, `he-IL`, `mt` |
| Turkic     | `tr-TR`, `az`, `kk`, `uz` |
| Hellenic   | `el-GR` |
| Uralic     | `fi-FI`, `hu-HU`, `et-EE` |
| Japonic    | `ja` |
| Sinitic    | `zh` |
| Koreanic   | `ko` |

350+ codes across 40+ family groupings, including reconstructed proto-languages and fine-grained regional dialects.

## Data structure

```python
@dataclass(frozen=True)
class LanguageSpec:
    code: str                              # 'pt-BR'
    name: str                              # 'Brazilian Portuguese'
    family: str                            # 'Romance'
    script: str                            # 'Latin'
    graphemes: Dict[str, List[str]]        # 'th' → ['θ', 'ð']
    allophones: Dict[str, List[str]]       # 't' → ['t', 'tʰ', 'ɾ', 'ʔ', 't̚']
    positional_graphemes: Dict[...]        # context-sensitive overrides
    parent: Optional[str]                  # primary parent code
    ancestors: Tuple[Ancestor, ...]        # weighted multi-ancestor lineage
    quality: QualityTier                   # stub | skeleton | research | production
    script_type: ScriptType                # alphabet | abjad | abugida | ...
    sandhi_rules: Tuple[SandhiRule, ...]   # cross-word rules
    tone_inventory: Optional[Dict]         # tone marks → labels
    sources: Tuple[LinguisticSource, ...]  # bibliographic references
```

When a spec declares graphemes but no explicit allophone map, a baseline identity allophone map is derived: every phoneme a grapheme can produce is, at minimum, its own surface realisation.

## Design principles

- **Linguistically motivated only** — digraphs like English ⟨th⟩, Portuguese ⟨lh⟩, or German ⟨sch⟩ are included because they are standard orthographic units; arbitrary substrings are not.
- **Graphemes ≠ allophones** — spelling-to-phoneme and phoneme-to-surface are modelled separately.
- **Regional variants** — where pronunciation diverges systematically, a separate `LanguageSpec` is provided with ancestry links.
- **Multi-ancestor inheritance** — `graphemes_base`/`allophones_base` let dialect trees declare only their differences.
- **Pure data, pluggable logic** — mappings are declarative JSON; algorithmic G2P (e.g. Arabic) uses the plugin system.

## Plugins

Algorithmic G2P backends register under the `orthography2ipa.g2p` entry-point group. The bundled Arabic plugin (`plugins/arabic_g2p.py`) handles consonant mapping, harakat vowels, sun-letter assimilation, hamzat al-wasl elision, and tanwin forms.

A neural Arabic diacritizer (`plugins/tashkeel.py`) is wired as an optional ONNX backend but ships as a documented stub: with no model loaded it returns input unchanged, and the rule-based plugin transcribes whatever diacritics are present. Bundling a tashkeel model is planned future work.

## Contributing

To add a language, create `orthography2ipa/data/{code}.json` following `orthography2ipa/data/SCHEMA.md`. For dialects, use `graphemes_base`/`allophones_base` to inherit from the parent.

## License

Apache 2.0
