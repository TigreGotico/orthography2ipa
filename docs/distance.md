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
