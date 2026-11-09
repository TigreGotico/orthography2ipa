# Upper Sorbian (`hsb`)

<!-- atlas:summary begin -->
Upper Sorbian is a West Slavic language, written in the Latin script. Glottolog places it in Germany. The `hsb` spec is at the research tier. It cites 1 source and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `hsb` |
| ISO 639-3 | [hsb](https://iso639-3.sil.org/code/hsb), Upper Sorbian |
| Glottolog | [uppe1395](https://glottolog.org/resource/languoid/id/uppe1395), Upper Sorbian |
| Wikidata | [Q13248](https://www.wikidata.org/wiki/Q13248) |
| Wikipedia | [Upper Sorbian language](https://en.wikipedia.org/wiki/Upper_Sorbian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic > West Slavic](by-family.md#indo-european--balto-slavic--slavic--west-slavic) |
| Region | [Eurasia](by-region.md#eurasia) > [Germany](by-region.md#germany) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1574, living |
| Parent | [West Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-west2792) `x-clade-west2792` |
| Explorer | [`hsb` in the data explorer](https://tigregotico.github.io/orthography2ipa/#hsb) |
| Spec file | [`hsb.json`](../../orthography2ipa/data/hsb.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Upper Sorbian (Hornjoserbsce), West Slavic minority language of the Sorbian people in Lusatia, Germany. Palatal affricates ć /tɕ/ and dź /dʑ/ are distinctive. Ě = /jɛ/, ł = /w/. Dual grammatical number preserved.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 1 work, from 2024. [Sources](#sources) lists them. The spec file writes all 36 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/hsb.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `hsb` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 1 works. 0 of them have a DOI or a URL.

1. <a id="src-wiki-hsb"></a>Wikipedia contributors (2024). *Upper Sorbian language*.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `hsb` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1126 | 0.2186 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `hsb` | generated | epitran-derived | CC0 1.0 | 5802 | 0.3177 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 35 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  | ts | dʒ tʃ | dʑ tɕ |  |  |
| Nasal | m |  | n |  | ɲ |  |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Near-close |  |  | ʊ |
| Close-mid | e |  | o |
| Open-mid | ɛ |  | ɔ |
| Open | a |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨ch⟩ | [x] |  |
| ⟨d⟩ | [d] |  |
| ⟨dź⟩ | [dʑ] |  |
| ⟨dž⟩ | [dʒ] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [v] |  |
| ⟨y⟩ | [ɨ] |  |
| ⟨z⟩ | [z] |  |
| ⟨ó⟩ | [o] [ʊ] |  |
| ⟨ć⟩ | [tɕ] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨ě⟩ | [e] |  |
| ⟨ł⟩ | [w] |  |
| ⟨ń⟩ | [ɲ] |  |
| ⟨ř⟩ | [ʃ] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ž⟩ | [ʒ] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "hsb")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Upper Navarrese Basque](eu-x-nafarra-garaia.md) · [Home](../index.md) · [Urdu →](ur.md)
