# Ancestry System

The ancestry system models the historical relationships between languages — parent descent, substrate influences, superstrate overlays, and ongoing contact — in a structured, typed way. This data powers phylogenetically-informed distance calculations and enables the package to be used as a digital reference for historical linguistics.

---

## Why Model Ancestry?

Purely synchronic phonological comparison (inventory distance, grapheme divergence) misses important information:

1. **Two languages can be phonologically similar for different reasons** — they might share a common ancestor, or they might have converged through contact.
2. **Substrate effects** explain phonological features that deviate from the genetic ancestor. The Basque substrate is the leading explanation for Castilian's *f → h* change; knowing this lets us weight the Basque connection appropriately.
3. **Creoles and contact languages** cannot be adequately described with a single parent chain.
4. **Distance metrics improve** when ancestry similarity is factored in alongside synchronic phonological metrics.

---

## The Ancestry Model

Each `LanguageSpec` has an `ancestors` tuple of `Ancestor` objects:

```python
@dataclass(frozen=True)
class Ancestor:
    code: str            # Language code
    role: AncestorRole   # Relationship type
    weight: float        # Phonological contribution [0.0, 1.0]
    notes: str           # Optional documentation
```

### AncestorRole values

#### `PARENT`

Primary genetic descent. The normal line of language transmission across generations.

- Every living/attested language should have exactly one PARENT (except reconstructed proto-languages).
- Weight: 0.70–1.00

```python
# Latin → Spanish
Ancestor("la-x-hispania", AncestorRole.PARENT, 0.80,
         "Primary descent from Hispanic Vulgar Latin")
```

#### `SUBSTRATE`

The language of the indigenous population who adopted the incoming language. Substrate effects typically manifest as:
- Phonological features that deviate from the parent language
- Sound changes that occur only in geographic areas where the substrate was spoken
- Structural patterns (prosody, syllable typology) that mirror the substrate

```python
# Basque substrate in Castilian Spanish
Ancestor("xaq", AncestorRole.SUBSTRATE, 0.08,
         "Basque substrate: f→h change, reinforcement of 5-vowel system")
```

Classic substrate effects in the package:
- **Basque substrate → Castilian**: The *f → h* sound change (*filium* → *hijo*) is attested only in the Basque-speaking area of medieval Iberia.
- **Gaulish substrate → French**: Lenition of intervocalic stops, vowel nasalization.
- **Pre-Roman substrate → French /y/**: The front rounded vowel /y/ is unusual in Romance and may reflect a Gaulish or pre-IE substrate.

#### `SUPERSTRATE`

The language of a socially dominant group that was eventually absorbed by the local population. The dominant group's language influenced the local language heavily before disappearing.

```python
# Visigothic (Gothic) superstrate in Spanish
Ancestor("got", AncestorRole.SUPERSTRATE, 0.05,
         "Visigothic: guerra, guardar, ropa; some palatalization influence")

# Frankish superstrate in French
Ancestor("gem", AncestorRole.SUPERSTRATE, 0.10,
         "Frankish influence: vocabulary, some phonological features")
```

#### `ADSTRATE`

A neighbouring language at roughly equal social prestige that exerts ongoing influence through bilingualism and lexical borrowing.

```python
# Arabic adstrate on medieval Ibero-Romance
Ancestor("xaa", AncestorRole.ADSTRATE, 0.07,
         "Andalusi Arabic adstrate: ~4000 loanwords in Spanish/Portuguese")
```

The 700-year Arabic presence on the Iberian Peninsula left a massive lexical footprint (words beginning with *al-* in Spanish and Portuguese: *alcohol*, *algodón*, *almohada*) and some phonological influence in southern dialects.

#### `LEXIFIER`

The language providing the majority of vocabulary in a creole or pidgin. In creole linguistics, the lexifier is sometimes called the "superstrate," though the sociolinguistic situation differs from the above.

```python
# Portuguese as lexifier of Papiamentu (not currently in registry — example only)
Ancestor("pt", AncestorRole.LEXIFIER, 0.65,
         "Portuguese lexifier: core vocabulary")
```

#### `CREOLE_BASE`

The substrate language(s) contributing grammatical structure to a creole. In many Atlantic creoles, West African languages contributed the tonal/serial verb structure while the lexifier supplied most vocabulary.

---

## Accessing Ancestry Data

```python
import orthography2ipa
from orthography2ipa.types import AncestorRole

spec = orthography2ipa.get("es")

# All ancestors
for anc in spec.get_ancestors():
    print(f"  {anc.role.value:12s}  {anc.code:20s}  w={anc.weight:.2f}  {anc.notes}")

# Substrate ancestors only
subs = spec.get_ancestors(AncestorRole.SUBSTRATE)

# Convenience properties
print(spec.primary_parent)      # 'la-x-hispania'
print(spec.substrate_codes)     # ('xaq',)
print(spec.superstrate_codes)   # ('got',)
print(spec.contact_codes)       # all non-parent: ('xaq', 'xaa', 'got')
```

---

## The Iberian Pre-Roman Layer

The package has unusually deep coverage of the pre-Roman Iberian Peninsula, reflecting the complex linguistic landscape before Latin arrived:

| Code | Language | Notes |
|---|---|---|
| `xce` | Celtiberian | Celtic branch of IE, spoken in eastern Iberia |
| `xib` | Iberian | Non-IE language of the eastern coast, script partially deciphered |
| `xlg` | Lusitanian | Possibly IE, spoken in what is now Portugal/Extremadura |
| `txr` | Tartessian | Possibly Celtic, script only partially read, SW Iberia |
| `xaq` | Proto-Basque (Aquitanian) | Non-IE isolate, only ancestor of modern Basque |
| `phn` | Phoenician | Semitic, trading colonies along Mediterranean coast |
| `cel` | Common Celtic | Ancestor of Celtiberian and other Iberian Celtic |

These are used as substrates and superstrates in the ancestry chains of modern Iberian Romance languages, enabling more nuanced distance calculations.

---

## Ancestry Distance Calculation

The `ancestry_similarity` function traverses the full ancestry graph recursively:

```python
from orthography2ipa.distance import ancestry_similarity

# Languages with shared ancestors → higher similarity
sim_es_pt = ancestry_similarity(
    orthography2ipa.get("es"),
    orthography2ipa.get("pt")
)
# Both descend from la-x-hispania (via Vulgar Latin)
# Both have the Basque substrate (xaq)
# Both have the Arabic adstrate (xaa)
# → high similarity

sim_es_ja = ancestry_similarity(
    orthography2ipa.get("es"),
    orthography2ipa.get("ja")
)
# No shared ancestors anywhere in the tree
# → 0.0
```

The algorithm:
1. Build the full ancestor graph for each language (recursively following all ancestry links)
2. For each shared ancestor, add `min(weight_a, weight_b)` to the similarity score
3. Normalize by the total weight

---

## Writing Ancestry for New Languages

When adding a new language, consult the historical linguistics literature for:

1. **The primary parent** — usually straightforward (which known language gave rise to this one?)
2. **Substrate candidates** — what languages were spoken in this area before?
3. **Superstrate candidates** — were there any conquest/prestige languages that left phonological traces?
4. **Adstrate candidates** — what neighboring languages have been in continuous contact?

### Weights should reflect phonological impact, not just historical presence

A language can have had centuries of contact with Arabic without Arabic affecting its phonology much. In that case, use a low weight even if the historical relationship is well-documented. Conversely, a brief but intense contact event (like the Norman conquest of England) can merit a higher weight due to phonological changes it triggered.

### Document your reasoning in `notes`

```python
Ancestor(
    code="xib",
    role=AncestorRole.SUBSTRATE,
    weight=0.06,
    notes=(
        "Iberian substrate in Catalan: some place names, possibly /ɾ/ "
        "as default rhotic vs. /r/ trill; cf. Coromines (1954)"
    )
)
```

---

## Transitive Ancestry

When computing ancestry similarity, the system follows the full tree recursively. This means:

- Spanish and Portuguese are close not only because both have `la-x-hispania` as parent, but because `la-x-hispania` → `la` (Classical Latin) → `ine` (Proto-Indo-European), and both languages inherit these deep connections.
- Two dialects of the same language will show near-1.0 ancestry similarity because they share essentially all ancestors.
- Unrelated language families will converge to 0.0 because their ancestry trees never intersect.
