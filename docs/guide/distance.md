# Distance Metrics

Languages relate along several independent axes, and a pair can be close on one axis and far apart on another. The `orthography2ipa.distance` module measures each axis on its own instead of folding them into one number. Unless a section says otherwise, a distance runs from 0.0 (identical) to 1.0 (maximally different).

| Axis | Question | Functions |
|---|---|---|
| Phonological | Do they use the same sounds? | `inventory_distance`, `allophone_overlap`, `phonological_distance`, `phoneme_coverage` |
| Reading | Given the same text, do they sound alike? | `grapheme_divergence` |
| Spelling | Given the same sound, do they write it alike? | `spelling_divergence` |
| Script | Are the writing systems alike in type? | `orthographic_distance`, `script_distance` |
| Tone | Do they share tones? | `tone_distance` |
| Genealogical | Do they share ancestors? | `ancestry_similarity` |
| Temporal | Were they spoken at the same time? | `temporal_distance` |
| Geographic | Are they spoken in the same place? | `geographic_distance` |
| Combined | All of these, weighted | `full_distance`, `weighted_full_distance`, `pairwise_distances` |

Reading and spelling are inverses, and Galician shows why both exist. The RAG norm and the reintegrationist norm are one language with one phonology. One writes /ɲ/ as ⟨ñ⟩ and the other as ⟨nh⟩.

`spelling_divergence` and `geographic_distance` are not in the module's `__all__`, so import them by name.

## The feature system

The segment metrics use the distinctive features in `orthography2ipa.feats`, a hybrid SPE and IPA system adapted from PyPhone. `feature_names()` returns the 23 features in order:

```python
from orthography2ipa.distance import feature_names

feature_names()
# ('syllabic', 'sonorant', 'consonantal', 'continuant', 'delayed_release', 'lateral',
#  'nasal', 'strident', 'voice', 'spread_glottis', 'constricted_glottis', 'anterior',
#  'coronal', 'distributed', 'labial', 'high', 'low', 'back', 'round', 'tense', 'long',
#  'click', 'nasal_vowel')
```

The weights in `feats.feature_weights` give the major-class features (syllabic, sonorant, consonantal) the most weight. Each of them weighs eight times as much as the lightest features, such as `strident`, `voice` and `long`.

## `feature_vector`

`feature_vector(segment)` returns a tuple of 23 floats. A value of 1.0 means the feature is present, 0.0 means it is absent, and 0.5 means it is unspecified. The function handles diacritics and modifiers such as ⟨ˤ ˞ ː⟩. For an unknown segment, it returns the neutral vector of 0.5 values and raises no exception.

```python
from orthography2ipa.distance import feature_vector

p = dict(zip(feature_names(), feature_vector("p")))
{k: p[k] for k in ("consonantal", "voice", "labial", "coronal", "strident")}
# {'consonantal': 1.0, 'voice': 0.0, 'labial': 1.0, 'coronal': 0.0, 'strident': 0.5}
```

## `segment_distance`

`segment_distance(seg_a, seg_b, strict=False)` returns the weighted feature distance between two IPA segments, from 0.0 to 1.0.

```python
from orthography2ipa.distance import segment_distance

segment_distance("p", "p")   # 0.0
round(segment_distance("p", "b"), 4)   # 0.0426
round(segment_distance("p", "f"), 4)   # 0.1702
round(segment_distance("p", "t"), 4)   # 0.2553
round(segment_distance("n", "ŋ"), 4)   # 0.4255
segment_distance("p", "a")   # 1.0
```

A vowel against a consonant always returns 1.0, because the two classes are compared on different feature sets. `feats.phonetic_distance` scores a consonant pair on twice the scale of a vowel pair, and `segment_distance` caps the result at 1.0. An empty segment or `∅` against any other segment returns 1.0.

The `strict` flag controls unknown segments:

```python
segment_distance("ℵ", "p")                # 1.0
segment_distance("ℵ", "p", strict=True)   # ValueError: Unknown IPA segment: 'ℵ'
```

## `inventory_distance`

`inventory_distance(spec_a, spec_b)` compares the phoneme inventories of two languages. It reads each spec's declared `phonemes`, and it derives the inventory from `graphemes` only for a spec that declares none.

```python
import orthography2ipa
from orthography2ipa.distance import inventory_distance

inventory_distance(orthography2ipa.get("es"), orthography2ipa.get("pt-BR"))
# InventoryDistance(jaccard=0.719, feature=0.069, shared=18/59)
```

| Field | Type | Meaning |
|---|---|---|
| `jaccard` | float | Jaccard distance on the raw phoneme sets, 1 - \|A∩B\| / \|A∪B\| |
| `feature_mean` | float | mean of the nearest-phoneme feature distances, averaged over both directions |
| `size_a`, `size_b` | int | the number of phonemes in each language |
| `shared` | int | the number of phonemes in common |

The representation prints `shared` over the larger of the two sizes.

Jaccard measures set overlap. It is 0.0 for identical inventories and 1.0 for no overlap. The feature mean finds, for each phoneme in A, the nearest phoneme in B by feature distance. It averages those distances, does the same from B to A, and takes the mean of the two. So it sees near misses: a language with /θ/ against one with /s/ shows a low feature distance, although the phonemes differ.

## `grapheme_divergence`

`grapheme_divergence(spec_a, spec_b)` measures how differently two languages read the grapheme keys they share. The comparison ignores case.

```python
from orthography2ipa.distance import grapheme_divergence

grapheme_divergence(orthography2ipa.get("es"), orthography2ipa.get("it"))
# GraphemeDivergence(shared=45/87, ipa_dist=0.240, overlap=0.517)

grapheme_divergence(orthography2ipa.get("es"), orthography2ipa.get("ja"))
# GraphemeDivergence(shared=0/366, ipa_dist=1.000, overlap=0.000)
```

| Field | Type | Meaning |
|---|---|---|
| `shared_graphemes` | int | the number of grapheme keys in common |
| `total_graphemes` | int | the number of grapheme keys in the union |
| `mean_ipa_distance` | float | the mean feature distance between the IPA candidates of the shared keys |
| `overlap_ratio` | float | Jaccard similarity of the two key sets |

For each shared key, the function pairs each candidate with its nearest candidate on the other side and averages the distances. Two Latin-script languages can share many keys and still read them very differently, which gives a high `mean_ipa_distance`. A pair with no shared key returns a `mean_ipa_distance` of 1.0.

## `spelling_divergence`

`spelling_divergence(spec_a, spec_b)` measures how differently two orthographies write the same sounds. The reading metric asks whether the same text sounds alike, as ⟨j⟩ is /ʒ/ in Portuguese and /x/ in Spanish. The spelling metric asks whether the same sound is written alike.

The function inverts each grapheme map into `phoneme → {graphemes that write it}`. For each phoneme that both orthographies can spell, it takes the Jaccard distance of the two spelling sets. The result is the mean over the shared phonemes.

```python
from orthography2ipa.distance import spelling_divergence

gl = orthography2ipa.get("gl-ES")                  # RAG norm, /ɲ/ is ⟨ñ⟩
glr = orthography2ipa.get("gl-ES-x-reintegr")   # reintegrationist norm, /ɲ/ is ⟨nh⟩

round(grapheme_divergence(gl, glr).mean_ipa_distance, 4)   # 0.0189
round(spelling_divergence(gl, glr).mean_distance, 4)       # 0.0782

sd = spelling_divergence(gl, glr)
sd.shared_phonemes, sd.identical_spellings, sd.disjoint_spellings   # (49, 44, 3)
```

| Field | Meaning |
|---|---|
| `shared_phonemes` | the phonemes both orthographies can spell |
| `total_phonemes` | the union of the two inverted maps |
| `mean_distance` | the mean spelling distance over the shared phonemes, 0.0 when spelled identically |
| `identical_spellings` | the shared phonemes the two spell exactly alike |
| `disjoint_spellings` | the shared phonemes for which they share no spelling |

A pair with no shared phoneme returns a `mean_distance` of 1.0. A silent grapheme, which maps to the empty string, spells no phoneme and adds nothing.

## `allophone_overlap`

`allophone_overlap(spec_a, spec_b)` returns the Jaccard similarity, not a distance, of the two allophone inventories. A value of 1.0 means identical inventories, and 0.0 means no overlap. Two specs with no allophones at all return 1.0.

```python
from orthography2ipa.distance import allophone_overlap

round(allophone_overlap(orthography2ipa.get("es"), orthography2ipa.get("pt")), 4)   # 0.5385
round(allophone_overlap(orthography2ipa.get("es"), orthography2ipa.get("ja")), 4)   # 0.3462
```

## `phonological_distance`

`phonological_distance(spec_a, spec_b, *, w_inventory=0.60, w_allophone=0.40)` is the combined sound distance:

```
combined = w_inventory × inventory.feature_mean + w_allophone × (1 - allophone_sim)
```

```python
from orthography2ipa.distance import phonological_distance

phonological_distance(orthography2ipa.get("la"), orthography2ipa.get("it-IT"))
# PhonologicalDistance(combined=0.266, inv=0.053, allo=0.414, [graph=0.108 not scored])
```

| Field | Type | Meaning |
|---|---|---|
| `inventory` | `InventoryDistance` | the inventory comparison |
| `allophone_sim` | float | the allophone Jaccard similarity |
| `combined` | float | the weighted combination of the two |
| `grapheme` | `GraphemeDivergence` | the reading divergence, reported but not part of `combined` |

The writing system takes no part in `combined`. Hindi in Devanagari and Urdu in the Arabic script have one phonology and two scripts. Serbian in Cyrillic and Croatian in Latin are the same case. A metric that read the spelling would put each pair far apart. A change to a spec's `graphemes` that leaves its `phonemes` alone does not move this number.

For the orthographic side, use `grapheme_divergence`, `spelling_divergence` or `orthographic_distance`. To weigh sound and spelling together, use `weighted_full_distance`, which has a `w_grapheme` term.

## `phoneme_coverage`

`phoneme_coverage(spec_native, spec_target)` is asymmetric. It returns the fraction of the target's phonemes that the native inventory already holds.

```python
from orthography2ipa.distance import phoneme_coverage

es = orthography2ipa.get("es-ES")
pt = orthography2ipa.get("pt-PT")

round(phoneme_coverage(es, pt), 4)   # 0.3103
round(phoneme_coverage(pt, es), 4)   # 0.7826
phoneme_coverage(es, es)   # 1.0
```

A value of 1.0 means the native language covers every target phoneme, and 0.0 means it covers none. A high value predicts an easier transfer for a second-language learner. A target with no phonemes returns 1.0.

## `orthographic_distance` and `script_distance`

`orthographic_distance(spec_a, spec_b)` adds a script-type term from `orthography2ipa.script_distance` to the grapheme divergence. For a same-script pair, the script term is 0.0 and the result is the plain `mean_ipa_distance`. For a cross-script pair, the result is `0.6 × script_distance + 0.4 × mean_ipa_distance`.

```python
from orthography2ipa.distance import orthographic_distance
from orthography2ipa.script_distance import script_distance_by_name

round(orthographic_distance(gl, glr), 4)               # 0.0189
round(script_distance_by_name("Latin", "Arabic"), 4)   # 0.57
pt_br, ar = orthography2ipa.get("pt-BR"), orthography2ipa.get("ar")
round(orthographic_distance(pt_br, ar), 4)             # 0.742
```

`script_distance_by_name` looks the names up in `SCRIPT_REGISTRY`, and `script_distance` compares two `ScriptFeatures` entries. When a script name is not in the registry, `orthographic_distance` uses 0.0 for a same-name pair and 0.5 for any other pair.

## `tone_distance`

`tone_distance(spec_a, spec_b)` is the Jaccard distance on the tone inventories. Two languages without tones are 0.0 apart. A language without tones is 1.0 from a tonal one.

## `ancestry_similarity`

`ancestry_similarity(spec_a, spec_b, max_depth=10, temporal_decay=False, decay_halflife=1000.0)` returns a similarity from 0.0 to 1.0. It multiplies the edge weights along each path and keeps the best path to each ancestor. The result is the strongest connection through a shared ancestor. [ancestry.md](../specs/ancestry.md#ancestry-similarity) gives the full algorithm.

```python
from orthography2ipa.distance import ancestry_similarity

round(ancestry_similarity(orthography2ipa.get("es"), orthography2ipa.get("pt")), 4)   # 0.5304
round(ancestry_similarity(orthography2ipa.get("es"), orthography2ipa.get("ja")), 4)   # 0.0015
```

## `temporal_distance`

`temporal_distance(spec_a, spec_b, reference_year=2025)` compares the attestation periods in each spec's `timespan`. It returns 1 minus the Jaccard index of the two intervals. A living language, with no `end_year`, runs to `reference_year`. The function returns `None` when either spec has no `timespan`.

```python
from orthography2ipa.distance import temporal_distance

temporal_distance(orthography2ipa.get("la"), orthography2ipa.get("es-ES"))   # 1.0
round(temporal_distance(es, pt), 4)                                          # 0.2759
```

## `geographic_distance`

`geographic_distance(spec_a, spec_b, normalize=True)` returns the great-circle distance between the representative points in the two specs' `location` fields (`latitude`, `longitude`, `source`). It returns kilometres when `normalize` is `False`. Otherwise it divides by half the Earth's circumference, the largest distance two points can have.

```python
from orthography2ipa.distance import geographic_distance

round(geographic_distance(pt, es, normalize=False), 1)   # 377.8
round(geographic_distance(pt, es), 4)                    # 0.0189

orthography2ipa.get("ca").location
# Location(latitude=41.453, longitude=1.569, source='glottolog',
#          notes="Glottolog's representative point for Catalan.")
```

A point is a rough proxy for an area, and the error is not uniform. For a dialect anchored to a region, the point is a fair summary. That is where the metric is useful: on a dialect continuum, the order of the points follows the order of the isoglosses. For a widespread macrolanguage, one point is arbitrary. Spanish spans two hemispheres, and its distance to anything says more about the point Glottolog chose than about the language. A clade node's point is a computed centroid of its descendants, which is weaker still. Give this axis a low weight, or none, when you compare macrolanguages.

The function returns `None`, not 0.0, when either spec has no `location`. Two languages of unknown position are not neighbours. A caller must handle `None` and not fold it into an average.

## `positional_divergence`

`positional_divergence(spec_a, spec_b)` measures how differently two specs use their [positional overrides](../engine/positional_graphemes.md). It returns 0.0 when neither spec has positional data.

```python
from orthography2ipa.distance import positional_divergence

round(positional_divergence(es, pt), 4)   # 0.9331
positional_divergence(es, es)   # 0.0
```

A grapheme with overrides in only one spec adds 1.0. For a grapheme with overrides in both, each position adds the `segment_distance` of the two first candidates, or 1.0 when only one spec declares that position, divided by the number of positions. The function divides the sum by the number of graphemes with any positional data and caps the result at 1.0.

## `full_distance`

`full_distance(spec_a, spec_b, *, w_phonological=0.60, w_ancestry=0.40)` combines the phonological distance with the ancestry similarity:

```
full = w_phonological × phonological_distance.combined + w_ancestry × (1 - ancestry_similarity)
```

```python
from orthography2ipa.distance import full_distance

round(full_distance(orthography2ipa.get("es"), orthography2ipa.get("pt")), 4)   # 0.3178
```

A lower value means a closer pair. The result does not include the orthography.

## `weighted_full_distance`

`weighted_full_distance` is the configurable entry point for every component:

```text
weighted_full_distance(spec_a, spec_b, *, w_inventory=0.25, w_grapheme=0.20,
                       w_allophone=0.15, w_ancestry=0.40, w_temporal=0.0,
                       reference_year=2025)
```

```python
from orthography2ipa.distance import weighted_full_distance

result = weighted_full_distance(es, pt)
round(result.combined, 3)   # 0.316
result.weights              # (0.25, 0.2, 0.15, 0.4, 0.0)

only_inventory = weighted_full_distance(es, pt, w_inventory=1.0, w_grapheme=0.0,
                                        w_allophone=0.0, w_ancestry=0.0)
only_inventory.combined == only_inventory.inventory   # True
```

The result is an `orthography2ipa.types.WeightedDistance`:

| Field | Meaning |
|---|---|
| `inventory` | `feature_mean` from `inventory_distance` |
| `grapheme` | `mean_ipa_distance` from `grapheme_divergence` |
| `allophone` | the allophone similarity, higher for more overlap |
| `ancestry` | the ancestry similarity, higher for closer kin |
| `temporal` | the temporal distance, or `None` when a `timespan` is missing |
| `combined` | the weighted distance, from 0.0 to 1.0 |
| `weights` | the tuple `(w_inventory, w_grapheme, w_allophone, w_ancestry, w_temporal)` |

`allophone` and `ancestry` are similarities, and the formula turns them into distances:

```
combined = (w_inventory × inventory + w_grapheme × grapheme + w_allophone × (1 - allophone)
            + w_ancestry × (1 - ancestry) + w_temporal × temporal) / total_weight
```

The weights need not sum to 1.0, because the function divides by their total. When `temporal` is `None`, the temporal weight drops out of the total. The temporal term is off by default (`w_temporal=0.0`).

| Weight | Default | Reason |
|---|---|---|
| `w_inventory` | 0.25 | the phoneme inventory is a strong signal |
| `w_grapheme` | 0.20 | grapheme overlap matters for languages that share a script |
| `w_allophone` | 0.15 | the surface realisations |
| `w_ancestry` | 0.40 | relatedness is the dominant factor |
| `w_temporal` | 0.0 | off unless the caller sets it |

## `pairwise_distances`

`pairwise_distances(specs, metric="combined")` returns a symmetric N×N matrix with zeros on the diagonal. The `metric` values are `"combined"`, `"inventory"`, `"grapheme"`, `"allophone"` and `"ancestry"`. The first four read `phonological_distance` with its default weights. `"ancestry"` uses 1 minus `ancestry_similarity`. Any other value silently falls back to `"combined"`.

```python
from orthography2ipa.distance import pairwise_distances

langs = [orthography2ipa.get(c) for c in ("es", "pt", "it", "fr", "en")]
matrix = pairwise_distances(langs, metric="combined")
[round(d, 3) for d in matrix[0]]   # [0.0, 0.217, 0.265, 0.256, 0.376]
```

The `combined` metric has a narrow range. It gives 0.051 for `pt-BR` against `pt-PT` and 0.394 for `es` against `zh`, rounded. Use the `"ancestry"` metric or `weighted_full_distance` when relatedness matters.

---
[← Lexicons and forced pronunciations](lexicon.md) · [Home](../index.md) · [Known limitations →](known_limitations.md)
