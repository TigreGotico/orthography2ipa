# Glottolog alignment

Reference: **Glottolog** (`clld/glottolog-cldf`, `cldf/languages.csv` + the `classification`
parameter in `cldf/values.csv`), which gives a full ancestor path per glottocode.

Glottolog is the reference for **genetic classification only**. This library is deliberately
**finer** than Glottolog (dialects, historical stages, reconstructed proto-nodes) and **richer**
(contact edges — substrate, superstrate, adstrate — which Glottolog does not model at all).
Glottolog is used to catch errors and fill gaps, never to flatten the graph.

## What Glottolog governs, and what it does not

| Concern | Authority |
|---|---|
| `glottolog_code` on a spec | Glottolog. A code must resolve, and must point at *that* language — not at the subgroup above it. |
| Which clade node a language hangs from | Glottolog, where it has an opinion. |
| Whether a dialect exists at all | This library. Glottolog files most sub-national lects under the national language; that is a coarser resolution, not a correction. |
| Contact ancestry (substrate/superstrate/adstrate) | This library. Glottolog does not model it. |
| `family` | Derived from the clade chain — never authored, never generated from a Glottolog string. See [ancestry.md](ancestry.md#clade-nodes-and-the-derived-family). |

`null` is the honest value for `glottolog_code` when Glottolog genuinely has no node for a variety.
A wrong code is worse than no code: a code that silently points at the subgroup above the language,
or at an unrelated language entirely, corrupts every audit built on top of it.

## Coverage

Counted over the shipped specs (`orthography2ipa/data/*.json`):

| | Count |
|---|---:|
| Language specs | 493 |
| Clade nodes | 63 |
| Total spec files | 556 |
| Specs carrying a `glottolog_code` | 420 (362 languages, 58 clades) |
| Distinct derived family paths | 68 |
| Top-level families | 30 |
| Largest family path | `Indo-European > Italic > Romance > Ibero-Romance` (118 languages) |

Regenerate the numbers straight from the data:

```python
import orthography2ipa

codes = orthography2ipa.available_codes()                       # 493 languages
clades = set(orthography2ipa.available_codes(include_clades=True)) - set(codes)   # 63
with_code = [c for c in codes if orthography2ipa.get(c).glottolog_code]           # 362
families = orthography2ipa.available_families()                                   # 68 paths
```

## Why the classification path is not a raw Glottolog slice

Glottolog's path to Portuguese runs through nodes whose names are unusable as branch labels
(`Italic > Latino-Faliscan > Latinic > Imperial Latin > Shifted Western Romance > …`). The clade
nodes in this library instead use the traditional branch names a linguist would recognise —
`Indo-European > Italic > Romance > Ibero-Romance` — with each node cited, and Glottolog's
glottocode attached where a corresponding node exists.

Depth matters. A flat two-level scheme would collapse every Romance variety into one bucket and
destroy the `Ibero-Romance` / `Gallo-Romance` / `West Germanic` / `West Slavic` distinctions that
carry the project's Iberian granularity. The CLI's `--family` filter matches *any* step of the
path, so `--family Romance` and `--family Ibero-Romance` both work, and depth costs the caller
nothing.

## Where Glottolog has no node

131 language specs carry no `glottolog_code`, and that is the correct value for them:

- **102 are dialect or historical varieties** (`-x-` codes: `pt-PT-x-porto`,
  `es-ES-x-andalusia-w`, `la-x-hispania`, …). Glottolog resolves at the language level and files
  these under the national language; a code pointing at the parent would claim the spec *is* the
  parent, which is exactly the error `null` avoids.
- **29 are national varieties** Glottolog does not separate (`en-US`, `de-AT`, `nl-BE`, `pt-AO`,
  `es-CR`, …) — the same argument one level up.
- A handful of **reconstructed proto-nodes** have no node of their own
  (`brx-x-proto-boro-garo`, `xpa`).

Glottolog does have nodes for the awkward-looking cases, and they are used: Esperanto
(`espe1235`, family `Constructed`), Iberian (`iber1250`, `Isolate`), Tartessian (`tart1237`,
`Unclassifiable`). Creoles are the case the explicit `family` override exists for — their ancestry
is a lexifier plus a creole base, not a single line of descent.

## Where the roster is still thin

Well-attested in Glottolog, plausible for the project, absent from the roster: Cantonese (`yue`),
Uyghur (`ug`), Kurdish (`ku` / `ckb`), Hokkien (`nan`), Hakka (`hak`) and Wu (`wuu`). Atlantic-Congo
coverage remains thin relative to Romance. A new language is added by writing its spec and pointing
its `parent` at the right clade node — see [adding_a_language.md](adding_a_language.md).

---

**Navigation:** [Docs home](index.md) · [Ancestry](ancestry.md) · [Registry](registry.md) · [Adding a language](adding_a_language.md)
