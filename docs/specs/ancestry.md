# Ancestry System

The ancestry system records how languages relate in history. It holds parent descent and also the contact edges: substrate, superstrate, adstrate and the creole roles. The distance metrics weight these edges, and the classification path of each language comes from them.

## Why model ancestry

A comparison of inventories and spellings alone misses several facts:

1. Two languages can sound alike because they share an ancestor, or because they converged through contact. The two cases need different edges.
2. A substrate explains features that depart from the genetic parent. The `es-ES` spec cites a Basque substrate for the Latin *f* to *h* change (*filium* to *hijo*).
3. A creole or a contact language does not fit a single parent chain.
4. A distance metric improves when it adds ancestry to the phonological comparison.

## Clade Nodes and the Derived `family`

The ancestry graph has two kinds of node above the languages.

A proto-language, such as `ine` (Proto-Indo-European) or `la-x-hispania` (Hispanic Vulgar Latin), is a reconstructed language. It has phonology and a grapheme table, and it is a data ancestor. A descendant can inherit graphemes, sandhi rules and allophone rules from it. A proto-language whose reconstruction has no data yet, such as `bnt` (Proto-Bantu), has no grapheme table and is only a node of the graph.

A clade node, such as `x-clade-roma1334` (Romance) or `x-clade-west2793` (West Germanic), is classification only. It has `"clade": true`, empty `graphemes` and `allophones`, and the quality tier `stub`. It is never a source of inherited data. It puts the classification hierarchy into the one ancestry graph, so that no spec carries a hand-kept family string.

A clade node cites its Glottolog languoid in `glottolog_code` (`roma1334` Romance, `celt1248` Celtic, `semi1276` Semitic) and its Wikipedia page. Some clades have no Glottolog node with exactly their membership, such as Ibero-Romance, Gallo-Romance, Italo-Romance, Vasconic and Tyrsenian. Such a node cites Wikipedia, and its `notes` name the nearest Glottolog node.

The loader splices the clade nodes into the parent chain and never puts one in place of a language:

```python
from orthography2ipa.registry import ancestry_chain

ancestry_chain("pt-PT")
# ['pt-PT-x-medieval', 'roa-x-galaico-pt', 'x-clade-iberrom', 'la-x-hispania',
#  'x-clade-roma1334', 'la-x-late', 'la', 'la-x-archaic', 'ine-x-italic',
#  'x-clade-ital1284', 'ine', 'x-clade-indo1319']
```

The loader derives `family` from this chain. It walks `parent` upwards and collects the names of the clades it passes, broadest first:

```python
import orthography2ipa

orthography2ipa.get("pt-PT").family_path   # ('Indo-European', 'Italic', 'Romance', 'Ibero-Romance')
orthography2ipa.get("pt-PT").family        # 'Indo-European > Italic > Romance > Ibero-Romance'
```

`available_families()` groups the codes by the full path string. The CLI filter `orthography2ipa list --family` matches any one step of the path, so `--family Romance` and `--family Ibero-Romance` both list `pt-PT`.

A spec can carry an explicit `family` string, which wins over the derived one. It serves the groupings that are not genetic clades: creoles (`English Creole`), constructed languages (`Constructed`), isolates (`Isolate`) and unclassifiable languages (`Unclassifiable`).

### Clades never change inheritance

`parent` is the fallback edge for inherited `sandhi_rules` and `allophone_rules`, when a spec declares no `graphemes_base`. A node with no content on that edge would strip the inherited rules. So the loader walks through clade nodes when it looks for the nearest data-bearing ancestor. The distance metrics do the same when they weight ancestry. A clade node on the chain is therefore transparent, and transcription and ancestry weights are the same as without it.

## The ancestry model

Each `LanguageSpec` has an `ancestors` tuple of `Ancestor` objects:

```python
@dataclass(frozen=True)
class Ancestor:
    code: str            # language code
    role: AncestorRole   # relationship type
    weight: float = 0.5  # phonological contribution, 0.0 to 1.0
    notes: str = ""      # the reasoning and its source
```

A spec that sets only `parent` gets one `PARENT` ancestor with weight 1.0.

### `AncestorRole` values

| Role | Meaning | Example in the data |
|---|---|---|
| `parent` | primary genetic descent, at most one per language | `es-ES` from `es-ES-x-medieval`, 0.85 |
| `parent_dialect` | a dialect ancestor inside the same language | `el-CY` from `el` |
| `proto_language` | the reconstructed ancestor at the top of a lineage | `aln` from `ine` |
| `ancestor` | an earlier stage of the same lineage that is not the parent | `ja` from `ojp`, 0.10 |
| `substrate` | the language of a population before it adopted this one | `es-ES` from `xaq` (Basque), 0.06 |
| `superstrate` | the language of a dominant group that the local language absorbed | `fr-FR` from `gem` (Frankish), 0.18 |
| `adstrate` | a neighbour of about equal prestige, with ongoing contact | `es-ES` from `xaa` (Andalusi Arabic), 0.06 |
| `lexifier` | the source of most of the vocabulary of a creole or pidgin | `bi` (Bislama) from `en-GB`, 0.65 |
| `creole_base` | a language that gave grammatical structure to a creole | |
| `related` | a sister language with shared features and no descent | for typological comparison |

A substrate shows as features that depart from the parent. It can also show as sound changes limited to the area of the substrate, or as prosodic and syllable patterns that mirror it. A superstrate changed the local language heavily before it disappeared. An adstrate leaves its trace through bilingualism and loans. The Andalusi Arabic adstrate left Spanish and Portuguese words with *al-*, such as *alcohol*, *algodón* and *almohada*.

## Accessing ancestry data

```python
from orthography2ipa.types import AncestorRole

spec = orthography2ipa.get("es")
spec.code   # 'es-ES'

for anc in spec.get_ancestors():
    print(f"{anc.role.value:12s} {anc.code:18s} w={anc.weight:.2f}")
# parent       es-ES-x-medieval   w=0.85
# substrate    xaq                w=0.06
# superstrate  got                w=0.04
# adstrate     xaa                w=0.06

spec.get_ancestors(AncestorRole.SUBSTRATE)   # (Ancestor('xaq', substrate, w=0.06),)
spec.primary_parent                          # 'es-ES-x-medieval'
spec.substrate_codes                         # ('xaq',)
spec.superstrate_codes                       # ('got',)
spec.contact_codes                           # ('xaq', 'got', 'xaa')
```

`contact_codes` holds every ancestor that is not a parent.

## The pre-Roman layer of Iberia

The ancestry chains of the Iberian Romance languages use these pre-Roman and contact languages as substrates and superstrates:

| Code | Name in the spec | Note |
|---|---|---|
| `xce` | Celtiberian | Celtic, eastern Iberia, child of `cel` |
| `xib` | Iberian | not Indo-European, eastern coast |
| `xlg` | Lusitanian | child of `ine`, western Iberia |
| `txr` | Tartessian (Southwestern) | south-western Iberia |
| `xaq` | Aquitanian (Proto-Basque) | parent of `eu` |
| `phn` | Phoenician/Punic | Semitic, coastal trading colonies |
| `cel` | Proto-Celtic (reconstructed) | parent of Celtiberian |

## Ancestry similarity

`orthography2ipa.distance.ancestry_similarity(spec_a, spec_b)` returns a value from 0.0 to 1.0. The algorithm has three steps:

1. Trace every ancestor of each language through all the edges. The weight of a path is the product of the edge weights on it. When several paths reach one ancestor, the strongest path counts. Clade nodes are skipped.
2. For each ancestor that both languages reach, multiply the two path weights. The similarity is the largest of these products.
3. When one language is itself an ancestor of the other, the result is the larger of its path weight and the shared-ancestor score.

A language compared with itself returns 1.0. The result is capped at 1.0.

```python
from orthography2ipa.distance import ancestry_similarity

get = orthography2ipa.get
ancestry_similarity(get("pt-PT"), get("pt-PT-x-porto"))   # 0.9
ancestry_similarity(get("es"), get("pt"))                 # 0.5304000000000001
ancestry_similarity(get("es"), get("ja"))                 # 0.0015342500000000005
```

The products shrink fast along a long chain, so distant relatives score low. Spanish and Japanese still share a small score, because `ja` has an English adstrate and English reaches `ine` and `gem`. Two languages whose graphs never meet score 0.0.

With `temporal_decay=True`, each edge weight also decays with the time gap between the ancestor and the descendant, when both specs carry a `timespan`. The factor is `exp(-gap / decay_halflife)`, and `decay_halflife` defaults to 1000 years. [distance.md](../guide/distance.md) covers the other metrics that use ancestry.

## Writing ancestry for a language

Read the historical linguistics literature for four things:

1. The primary parent: the known language this one descends from.
2. The substrate candidates: the languages spoken in the area before.
3. The superstrate candidates: conquest or prestige languages that left phonological traces.
4. The adstrate candidates: the neighbouring languages in continuous contact.

Make the weight reflect the effect on phonology, not the length of the contact. Centuries of contact can leave a phonology almost unchanged, and that edge takes a low weight. A short and intense contact, such as the Norman conquest of England, can take a higher weight because of the sound changes it caused.

Put the reasoning and its source in `notes`:

```python
Ancestor(
    code="xib",
    role=AncestorRole.SUBSTRATE,
    weight=0.06,
    notes="Iberian substrate in Catalan: some place names, possibly /ɾ/ "
          "as default rhotic vs. /r/ trill; cf. Coromines (1954)",
)
```

Point `parent` at the right clade node or data ancestor. [../contributing/spec_authoring.md](../contributing/spec_authoring.md) gives the full procedure.

## Alignment with Glottolog

The reference for genetic classification is Glottolog, read from `clld/glottolog-cldf`: `cldf/languages.csv` and the `classification` parameter in `cldf/values.csv`. These give a full ancestor path for each glottocode.

Glottolog governs genetic classification only. This library is finer than Glottolog, because it has dialects, historical stages and reconstructed proto-nodes. It is also richer, because it has the contact edges, which Glottolog does not model. Glottolog serves to catch errors and fill gaps, and never to flatten the graph.

| Concern | Authority |
|---|---|
| `glottolog_code` on a spec | Glottolog. The code must resolve, and it must point at that language, not at the subgroup above it. |
| The clade node a language hangs from | Glottolog, where it has an opinion. |
| Whether a dialect exists | This library. Glottolog files most sub-national varieties under the national language, which is a coarser resolution and not a correction. |
| Contact ancestry | This library. Glottolog does not model it. |
| `family` | The clade chain. It is never authored and never copied from a Glottolog string. |

`null` is the correct `glottolog_code` when Glottolog has no node for a variety. A wrong code is worse than no code. A code that points at the subgroup above the language, or at an unrelated language, corrupts every audit that reads it.

### Coverage

Compute the coverage from the data. A printed figure goes stale as specs are added:

```python
codes = orthography2ipa.available_codes()                                        # languages
clades = set(orthography2ipa.available_codes(include_clades=True)) - set(codes)  # clade nodes
with_code = [c for c in codes if orthography2ipa.get(c).glottolog_code]          # languages with a glottolog_code
families = orthography2ipa.available_families()                                  # codes grouped by family path

len(codes), len(clades), len(codes) + len(clades), len(with_code)
```

### Why the path is not a raw Glottolog slice

Glottolog's path to Portuguese runs through nodes whose names do not work as branch labels: `Italic > Latino-Faliscan > Latinic > Imperial Latin > Shifted Western Romance > …`. The clade nodes of this library use the traditional branch names that a linguist knows, such as `Indo-European > Italic > Romance > Ibero-Romance`. Each node carries a citation, and it carries the glottocode where Glottolog has a matching node.

Depth matters. A flat scheme with two levels would put every Romance variety into one bucket. It would lose the Ibero-Romance, Gallo-Romance, West Germanic and West Slavic distinctions that the Iberian detail of this library depends on. The `--family` filter matches any step of the path, so the depth costs the caller nothing.

### Where Glottolog has no node

A spec without a `glottolog_code` is usually one of three kinds:

1. A dialect or historical variety with an `-x-` code, such as `pt-PT-x-porto`. Glottolog files it under the national language. A code that pointed at the parent would claim that the spec is the parent, which is the error `null` avoids.
2. A national variety that Glottolog does not separate, such as `en-US`, `de-AT`, `nl-BE`, `pt-AO` and `es-CR`.
3. A reconstructed proto-node with no Glottolog node, such as `brx-x-proto-boro-garo` and `xpa`.

Glottolog does have nodes for the hard-looking cases, and the specs use them. Esperanto is `espe1235` with family `Constructed`, Iberian is `iber1250` with `Isolate`, and Tartessian is `tart1237` with `Unclassifiable`. A creole has a lexifier and a creole base, not one line of descent. The explicit `family` override exists for that case.

---
[← Quality tiers](quality_tiers.md) · [Home](../index.md) · [IPA Reference →](ipa_reference.md)
