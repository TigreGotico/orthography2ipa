# Lower Sorbian (`dsb`)

<!-- atlas:summary begin -->
Lower Sorbian is a West Slavic language, written in the Latin script. Glottolog places it in Germany. The `dsb` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `dsb` |
| ISO 639-3 | [dsb](https://iso639-3.sil.org/code/dsb), Lower Sorbian |
| Glottolog | [lowe1385](https://glottolog.org/resource/languoid/id/lowe1385), Lower Sorbian |
| Wikidata | [Q13286](https://www.wikidata.org/wiki/Q13286) |
| Wikipedia | [Lower Sorbian language](https://en.wikipedia.org/wiki/Lower_Sorbian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic > West Slavic](by-family.md#indo-european--balto-slavic--slavic--west-slavic) |
| Region | [Eurasia](by-region.md#eurasia) > [Germany](by-region.md#germany) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1574, living |
| Parent | [West Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-west2792) `x-clade-west2792` |
| Explorer | [`dsb` in the data explorer](https://tigregotico.github.io/orthography2ipa/#dsb) |
| Spec file | [`dsb.json`](../../orthography2ipa/data/dsb.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Lower Sorbian (Dolnoserbski), West Slavic minority language spoken in Lower Lusatia, Germany. Closely related to Upper Sorbian. Distinct palatal fricatives ś /ɕ/ and ź /ʑ/. More conservative vowel system than Upper Sorbian.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2003 to 2024. [Sources](#sources) lists them. The spec file writes all 37 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/dsb.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `dsb` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-wiki-dsb"></a>Wikipedia contributors (2024). *Lower Sorbian language*.
2. <a id="src-zygis2003"></a>Żygis, Marzena (2003). *Phonetic and phonological aspects of Slavic sibilant fricatives*. ZAS Papers in Linguistics 3, 175-213. Cited: 180-181. [zaspil.leibniz-zas.de](https://zaspil.leibniz-zas.de/article/download/191/191)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `dsb` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2010 | 0.1487 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 36 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  | ts | dʒ tʃ | tɕ |  |  |
| Nasal | m |  | n |  | ɲ |  |  |
| Trill |  |  | r rʲ |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | ɕ ʑ | x | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
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
| ⟨ó⟩ | [o] |  |
| ⟨ć⟩ | [tɕ] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨ě⟩ | [e] |  |
| ⟨ł⟩ | [w] |  |
| ⟨ń⟩ | [ɲ] |  |
| ⟨ŕ⟩ | [rʲ] |  |
| ⟨ś⟩ | [ɕ] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ź⟩ | [ʑ] |  |
| ⟨ž⟩ | [ʒ] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "dsb")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Lower Navarrese Basque](eu-x-nafarra-beherea.md) · [Home](../index.md) · [Luba-Kasai →](lua.md)
