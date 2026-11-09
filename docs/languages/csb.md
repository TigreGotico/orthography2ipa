# Kashubian (`csb`)

<!-- atlas:summary begin -->
Kashubian is a West Slavic language, written in the Latin script. Glottolog places it in Poland. The `csb` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `csb` |
| ISO 639-3 | [csb](https://iso639-3.sil.org/code/csb), Kashubian |
| Glottolog | [kash1274](https://glottolog.org/resource/languoid/id/kash1274), Kashubian |
| Wikidata | [Q33690](https://www.wikidata.org/wiki/Q33690) |
| Wikipedia | [Kashubian language](https://en.wikipedia.org/wiki/Kashubian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic > West Slavic](by-family.md#indo-european--balto-slavic--slavic--west-slavic) |
| Region | [Eurasia](by-region.md#eurasia) > [Poland](by-region.md#poland) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1589, living |
| Parent | [West Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-west2792) `x-clade-west2792` |
| Explorer | [`csb` in the data explorer](https://tigregotico.github.io/orthography2ipa/#csb) |
| Spec file | [`csb.json`](../../orthography2ipa/data/csb.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Kashubian (Kaszëbsczi jãzëk), West Slavic language/dialect spoken in Pomerania, Poland. Official regional language since 2005. Nasal vowel ą /ɔ̃/, schwa ë /ə/. Digraphs sz, cz, rz, dż precede single letters. Significant German loanword influence.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2001 to 2024. [Sources](#sources) lists them. The spec file writes all 39 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/csb.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `csb` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-wiki-csb"></a>Wikipedia contributors (2024). *Kashubian language*.
2. <a id="src-hopkins2001"></a>Hopkins, Paul Stanley (2001). *The phonological structure of the Kashubian word*. University of Victoria (PhD thesis). Cited: xi. [dspace.library.uvic.ca](https://dspace.library.uvic.ca/items/3953007f-eb2c-4560-8c93-a003ed8b45be)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `csb` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2825 | 0.1663 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 35 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |
| Affricate |  |  | dz ts | dʒ tʃ |  |  |
| Nasal | m |  | n |  | ɲ |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid |  |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ ɔ̃ |
| Open | a ã |  |  |

Sequences that the spec writes as one unit: [w] [wɛ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨cz⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dz⟩ | [dz] |  |
| ⟨dż⟩ | [dʒ] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [x] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨rz⟩ | [ʒ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sz⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [v] |  |
| ⟨y⟩ | [ɨ] |  |
| ⟨z⟩ | [z] |  |
| ⟨ã⟩ | [ã] |  |
| ⟨é⟩ | [ɛ] |  |
| ⟨ë⟩ | [ə] |  |
| ⟨ò⟩ | [wɛ] |  |
| ⟨ó⟩ | [o] |  |
| ⟨ô⟩ | [ɔ] |  |
| ⟨ù⟩ | [u] |  |
| ⟨ą⟩ | [ɔ̃] |  |
| ⟨ł⟩ | [w] |  |
| ⟨ń⟩ | [ɲ] |  |
| ⟨ż⟩ | [ʒ] |  |

Stress falls on the penult by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "csb")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kashmiri](ks.md) · [Home](../index.md) · [Kazakh →](kk.md)
