# Middle Low German (`gml`)

<!-- atlas:summary begin -->
Middle Low German is a West Germanic language, written in the Latin script. Glottolog places it in Germany. The `gml` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `gml` |
| ISO 639-3 | [gml](https://iso639-3.sil.org/code/gml), Middle Low German |
| Glottolog | [midd1318](https://glottolog.org/resource/languoid/id/midd1318), Middle Low German |
| Wikipedia | [Middle Low German](https://en.wikipedia.org/wiki/Middle_Low_German) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > West Germanic](by-family.md#indo-european--germanic--northwest-germanic--west-germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [Germany](by-region.md#germany) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Ancestor | [Proto-Ingvaeonic (North Sea Germanic)](https://tigregotico.github.io/orthography2ipa/#gem-x-ingvaeon) `gem-x-ingvaeon` |
| Explorer | [`gml` in the data explorer](https://tigregotico.github.io/orthography2ipa/#gml) |
| Spec file | [`gml.json`](../../orthography2ipa/data/gml.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. West Germanic (Ingvaeonic/Low Saxon) medieval stage written in the Latin alphabet. Grapheme map covers the basic vowels, doubled long vowels, the digraphs sch [ʃ], ch [x], ng and ck, and the plain consonants with v and w both mapped to [v].

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1914 to 2024. [Sources](#sources) lists them. The spec file writes all 32 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/gml.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `gml` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-gml_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Middle Low German (midd1318)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/midd1318)
2. <a id="src-lasch1914"></a>Lasch, Agathe (1914). *Mittelniederdeutsche Grammatik*. Niemeyer, Halle. Cited: 116-117 (§§211-212), 151 (§290), 155-156 (§299), 173-175 (§334), 179 (§340), 180 (§342). [archive.org](https://archive.org/details/mittelniederdeut00lasc)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `gml` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 143 | 0.2771 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 30 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | k ɡ |  |
| Nasal | m |  | n |  | ŋ |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s |  | x ɣ | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e eː |  | o oː |
| Mid |  | ə |  |
| Open-mid | ɛː |  |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [sk] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨ae⟩ | [ɛː] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] |  |
| ⟨ch⟩ | [x] |  |
| ⟨ck⟩ | [k] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] | default [e] · nucleus stressed [e] · nucleus unstressed [ə] |
| ⟨ee⟩ | [eː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɣ] [ɡ] | before consonant [x] · default [ɣ] · word final [x] |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sc⟩ | [sk] |  |
| ⟨sch⟩ | [sk] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] [f] | default [v] · word initial [f] |
| ⟨w⟩ | [w] |  |
| ⟨z⟩ | [s] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "gml")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Middle Irish](mga.md) · [Home](../index.md) · [Middle Welsh →](wlm.md)
