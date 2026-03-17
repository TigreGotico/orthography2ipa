# Distance Metrics

The `distance` module provides a suite of phonological distance metrics grounded in distinctive feature theory. All distances are normalized to [0.0, 1.0] where 0.0 = identical and 1.0 = maximally different.

---

## The Feature System

The package delegates to **phonematcher**'s 21-feature SPE/IPA system:

| Index | Feature | Description |
|---|---|---|
| 0 | `syllabic` | Can form a syllable nucleus |
| 1 | `sonorant` | Produced with non-turbulent airflow |
| 2 | `consonantal` | Obstruent-like articulation |
| 3 | `continuant` | Airflow not completely stopped |
| 4 | `delayed_release` | Affricate-type release |
| 5 | `lateral` | Airflow around tongue sides |
| 6 | `nasal` | Nasal airflow |
| 7 | `strident` | High-frequency turbulence |
| 8 | `voice` | Vocal fold vibration |
| 9 | `spread_glottis` | Aspirated |
| 10 | `constricted_glottis` | Glottalised |
| 11 | `anterior` | Articulation forward of palate |
| 12 | `coronal` | Tongue blade/tip involved |
| 13 | `distributed` | Blade vs. tip distinction |
| 14 | `labial` | Lip involvement |
| 15 | `high` | High tongue body |
| 16 | `low` | Low tongue body |
| 17 | `back` | Back tongue body |
| 18 | `round` | Lip rounding |
| 19 | `tense` | Tense/lax distinction |
| 20 | `long` | Long/short duration |

Major-class features (syllabic, sonorant, consonantal) are weighted **7× heavier** than minor features. This means a consonant↔vowel mismatch returns 1.0 regardless of other similarities.

---

## `feature_vector(segment)`

```python
from orthography2ipa.distance import feature_vector, feature_names

vec = feature_vector("p")
names = feature_names()
for name, val in zip(names, vec):
    if val != 0.5:  # 0.5 = unspecified/neutral
        print(f"  {name}: {val}")

# consonantal: 1.0
# voice: 0.0      ← voiceless
# labial: 1.0     ← bilabial
# ...
```

Returns a 21-element tuple of floats:
- `1.0` = feature is **+** (present)
- `0.0` = feature is **-** (absent)
- `0.5` = unspecified or not applicable

For unknown segments, returns the neutral vector (all 0.5). This ensures graceful degradation rather than exceptions.

---

## `segment_distance(a, b)`

```python
from orthography2ipa.distance import segment_distance

segment_distance("p", "p")    # 0.0  — identical
segment_distance("p", "b")    # 0.06 — differ only in voicing
segment_distance("p", "t")    # 0.12 — differ in place (labial vs coronal)
segment_distance("p", "f")    # 0.18 — differ in manner (stop vs fricative)
segment_distance("p", "a")    # 1.0  — consonant vs vowel (always 1.0)
segment_distance("s", "ʃ")    # 0.09 — differ in anterior/distributed
segment_distance("n", "ŋ")    # 0.07 — differ in place (coronal vs dorsal)
```

Uses phonematcher's weighted feature distance, normalized to [0, 1]. Vowel↔consonant comparisons always return 1.0 due to the high weight on major-class features.

---

## `inventory_distance(spec_a, spec_b)`

Compares the full phoneme inventories of two languages.

```python
from orthography2ipa.distance import inventory_distance
import orthography2ipa

result = inventory_distance(orthography2ipa.get("es"), orthography2ipa.get("pt-BR"))
print(result)
# InventoryDistance(jaccard=0.231, feature=0.087, shared=23/43)
```

### `InventoryDistance` fields

| Field | Type | Description |
|---|---|---|
| `jaccard` | float | Jaccard distance on raw phoneme sets: 1 - |A∩B|/|A∪B| |
| `feature_mean` | float | Mean minimum feature distance (both directions averaged) |
| `size_a` | int | Number of phonemes in language A |
| `size_b` | int | Number of phonemes in language B |
| `shared` | int | Number of phonemes in common |

**Jaccard** measures set overlap directly. Two languages with exactly the same phoneme inventory → 0.0; no overlap → 1.0.

**Feature mean** is more nuanced: for each phoneme in A, find the closest phoneme in B by feature distance, average those minimum distances, then do the same in reverse and average. This captures "near misses" — a language with /θ/ when compared to one with /s/ will show low feature distance even though the phonemes differ.

---

## `grapheme_divergence(spec_a, spec_b)`

Measures how differently two languages use the same graphemes.

```python
from orthography2ipa.distance import grapheme_divergence

# Spanish vs. Italian — both use Latin script, many shared graphemes
result = grapheme_divergence(
    orthography2ipa.get("es"),
    orthography2ipa.get("it")
)
print(result)
# GraphemeDivergence(shared=28/51, ipa_dist=0.142, overlap=0.549)

# Spanish vs. Japanese — very different scripts
result2 = grapheme_divergence(
    orthography2ipa.get("es"),
    orthography2ipa.get("ja")
)
print(result2)
# GraphemeDivergence(shared=0/..., ipa_dist=1.000, overlap=0.000)
```

### `GraphemeDivergence` fields

| Field | Type | Description |
|---|---|---|
| `shared_graphemes` | int | Number of grapheme keys in common |
| `total_graphemes` | int | Number of grapheme keys in the union |
| `mean_ipa_distance` | float | Mean feature distance between IPA mappings of shared graphemes |
| `overlap_ratio` | float | Jaccard on grapheme key sets |

**Why this matters**: English and French both have `⟨c⟩`, but English maps it to /k, s/ while French maps it to /s, k/ — different ordering and different context-dependence. Latin script languages sharing many grapheme keys but mapping them to very different IPA will show high `mean_ipa_distance`.

---

## `allophone_overlap(spec_a, spec_b)`

Returns the Jaccard **similarity** (not distance) of the allophone surface-form inventories.

```python
from orthography2ipa.distance import allophone_overlap

sim = allophone_overlap(orthography2ipa.get("es"), orthography2ipa.get("pt"))
# → ~0.45 (many shared allophones between Spanish and Portuguese)

sim2 = allophone_overlap(orthography2ipa.get("es"), orthography2ipa.get("ja"))
# → ~0.05 (very few shared surface forms)
```

Returns a value in [0, 1] where 1.0 = identical allophone inventories, 0.0 = no overlap.

---

## `phonological_distance(spec_a, spec_b)`

The main combined distance metric.

```python
from orthography2ipa.distance import phonological_distance

d = phonological_distance(
    orthography2ipa.get("la"),
    orthography2ipa.get("it"),
    w_inventory=0.40,   # weight for inventory component
    w_grapheme=0.30,    # weight for grapheme divergence component
    w_allophone=0.30,   # weight for allophone component
)
print(d)
# PhonologicalDistance(combined=0.307, inv=0.142, graph=0.203, allo=0.412)
```

### `PhonologicalDistance` fields

| Field | Type | Description |
|---|---|---|
| `inventory` | `InventoryDistance` | Full inventory comparison result |
| `grapheme` | `GraphemeDivergence` | Full grapheme divergence result |
| `allophone_sim` | float | Allophone Jaccard similarity |
| `combined` | float | Weighted combination |

**Formula:**
```
combined = w_inventory × inventory.feature_mean
         + w_grapheme  × grapheme.mean_ipa_distance
         + w_allophone × (1 - allophone_sim)
```

---

## `ancestry_similarity(spec_a, spec_b)`

Measures how much ancestry two languages share, weighted by ancestor contribution weights.

```python
from orthography2ipa.distance import ancestry_similarity

# Spanish and Portuguese share Latin as a heavy ancestor
sim = ancestry_similarity(
    orthography2ipa.get("es"),
    orthography2ipa.get("pt")
)
# → high similarity (~0.7+)

# Spanish and Japanese share no ancestors
sim2 = ancestry_similarity(
    orthography2ipa.get("es"),
    orthography2ipa.get("ja")
)
# → 0.0
```

Traverses the full ancestry graph recursively, accumulating shared ancestor weights.

---

## `full_distance(spec_a, spec_b)`

Combines phonological distance and ancestry similarity into a single scalar:

```python
from orthography2ipa.distance import full_distance

d = full_distance(orthography2ipa.get("es"), orthography2ipa.get("pt"))
# Lower values = more related languages
```

---

## `pairwise_distances(specs, metric)`

Compute a symmetric N×N distance matrix for a list of languages.

```python
from orthography2ipa.distance import pairwise_distances
import orthography2ipa

langs = [
    orthography2ipa.get("es"),
    orthography2ipa.get("pt"),
    orthography2ipa.get("it"),
    orthography2ipa.get("fr"),
    orthography2ipa.get("en"),
]

matrix = pairwise_distances(langs, metric="combined")
# matrix[i][j] = phonological distance between langs[i] and langs[j]
# matrix[i][i] = 0.0

# Available metrics: "combined", "inventory", "grapheme", "allophone", "ancestry"
```

The matrix is symmetric (`matrix[i][j] == matrix[j][i]`) and has zeros on the diagonal.

---

## Expected Distance Ranges

| Language pair | Expected `combined` range | Notes |
|---|---|---|
| es vs pt | 0.15–0.25 | Closely related Ibero-Romance |
| es vs it | 0.25–0.35 | Romance but more distant |
| la vs es | 0.25–0.35 | Direct ancestor |
| la vs en | 0.55–0.70 | Distant, different family |
| es vs zh | 0.75–0.90 | Unrelated |
| pt-BR vs pt-PT | 0.05–0.15 | Dialects of same language |

These are rough empirical ranges; exact values depend on the completeness of each language's grapheme and allophone data.

---

## `segment_distance(a, b, strict=False)`

The `strict` parameter controls behaviour for unknown IPA segments:

```python
segment_distance("ℵ", "p")              # returns float in [0, 1] (graceful)
segment_distance("ℵ", "p", strict=True) # raises ValueError: Unknown IPA segment
```

| `strict` | Unknown segment behaviour |
|---|---|
| `False` (default) | Returns a value based on the neutral vector (all-0.5) |
| `True` | Raises `ValueError` immediately |

---

## `phoneme_coverage(spec_native, spec_target) -> float`

Asymmetric measure: fraction of `spec_target`'s phonemes already present in `spec_native`'s inventory.

```python
from orthography2ipa.distance import phoneme_coverage
import orthography2ipa

es = orthography2ipa.get("es-ES")
pt = orthography2ipa.get("pt-PT")

phoneme_coverage(es, pt)   # Spanish→Portuguese: how much of pt's inventory es covers
phoneme_coverage(pt, es)   # May differ (asymmetric)
phoneme_coverage(es, es)   # 1.0 — identity
```

- `1.0` = native language covers all target phonemes (easy transfer)
- `0.0` = no shared phonemes (maximum difficulty)

Use this to predict L2 phonological acquisition difficulty: a high coverage score indicates the learner's native inventory already contains most target sounds.

---

## `weighted_full_distance(spec_a, spec_b, *, w_inventory, w_grapheme, w_allophone, w_ancestry) -> WeightedDistance`

Single configurable entry point combining all four distance components.

```python
from orthography2ipa.distance import weighted_full_distance

result = weighted_full_distance(spec_a, spec_b)
# WeightedDistance(inventory=0.12, grapheme=0.31, allophone=0.67, ancestry=0.54, combined=0.41, ...)

# Custom weights — focus purely on phoneme inventory
result = weighted_full_distance(spec_a, spec_b, w_inventory=1.0, w_grapheme=0.0, w_allophone=0.0, w_ancestry=0.0)
assert result.combined == result.inventory
```

### `WeightedDistance` fields — `orthography2ipa.types.WeightedDistance`

| Field | Description |
|---|---|
| `inventory` | `feature_mean` from `inventory_distance()` — [0, 1] |
| `grapheme` | `mean_ipa_distance` from `grapheme_divergence()` — [0, 1] |
| `allophone` | Jaccard allophone *similarity* — [0, 1] (higher = more overlap) |
| `ancestry` | Ancestry *similarity* — [0, 1] (higher = more related) |
| `combined` | Weighted combined *distance* — [0, 1] |
| `weights` | `(w_inventory, w_grapheme, w_allophone, w_ancestry)` tuple used |

Note: `allophone` and `ancestry` are stored as *similarities*; the formula converts them to distances internally: `combined = (w_inv * inventory + w_gra * grapheme + w_allo * (1 - allophone) + w_anc * (1 - ancestry)) / total_w`.

### Default weights

| Component | Default weight | Rationale |
|---|---|---|
| `w_inventory` | 0.25 | Phoneme inventory is a strong signal |
| `w_grapheme` | 0.20 | Grapheme overlap matters for script-sharing languages |
| `w_allophone` | 0.15 | Surface realisation similarity |
| `w_ancestry` | 0.40 | Phylogenetic relatedness is the dominant factor |

---

## `positional_divergence(spec_a, spec_b) -> float`

Measures how differently two specs use positional grapheme overrides (initial/medial/final/intervocalic etc.).

```python
from orthography2ipa.distance import positional_divergence

d = positional_divergence(spec_a, spec_b)  # float in [0.0, 1.0]
```

- `0.0` = identical positional override sets (or neither spec has positional data)
- `1.0` = maximally different positional usage

For each grapheme that appears in either spec's `positional_graphemes`:
- If only one spec has overrides for it: contributes 1.0 to divergence
- If both have overrides: per-position IPA distance is measured using `segment_distance()`

Result is normalised by the total number of graphemes with any positional data.
