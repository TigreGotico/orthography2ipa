# Fernando Po Creole English (`fpe`)

<!-- atlas:summary begin -->
Fernando Po Creole English is a West Germanic language, written in the Latin script. Glottolog places it in the Africa, Australia, Eurasia, North America, Papunesia and South America macroareas. The `fpe` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `fpe` |
| ISO 639-3 | [fpe](https://iso639-3.sil.org/code/fpe), Fernando Po Creole English |
| Wikipedia | [Pichi language](https://en.wikipedia.org/wiki/Pichi_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > West Germanic](by-family.md#indo-european--germanic--northwest-germanic--west-germanic) |
| Region | [Africa](by-region.md#several-macroareas), [Australia](by-region.md#several-macroareas), [Eurasia](by-region.md#several-macroareas), [North America](by-region.md#several-macroareas), [Papunesia](by-region.md#several-macroareas), [South America](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Ancestor | [Proto-Ingvaeonic (North Sea Germanic)](https://tigregotico.github.io/orthography2ipa/#gem-x-ingvaeon) `gem-x-ingvaeon` |
| Explorer | [`fpe` in the data explorer](https://tigregotico.github.io/orthography2ipa/#fpe) |
| Spec file | [`fpe.json`](../../orthography2ipa/data/fpe.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research tier, consulting Yakpo's grammar of Pichi. English-lexifier Atlantic creole of Bioko (Equatorial Guinea), an offshoot of Krio, written in a Latin phonemic orthography. Grapheme map covers the seven-vowel system (a e ɛ i o ɔ u), the labial-velar stops kp/gb, and the digraphs ch, sh, ny and ng.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2013 to 2024. [Sources](#sources) lists them. The spec file writes all 38 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/fpe.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `fpe` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-fpe_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Pichi (fern1234)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/fern1234)
2. <a id="src-fpe_yakpo2019"></a>Yakpo, Kofi (2019). *A Grammar of Pichi*. Language Science Press (Studies in Diversity Linguistics 23). Cited: 11-12, 40. [langsci-press.org](https://langsci-press.org/catalog/book/85)
3. <a id="src-fpe_apics2013"></a>Yakpo, Kofi (2013). *Pichi (Survey chapter and structure dataset)*. In: Michaelis, S.M., Maurer, P., Haspelmath, M. & Huber, M. (eds.), Atlas of Pidgin and Creole Language Structures Online, chapter 19, Max Planck Institute for Evolutionary Anthropology. [apics-online.info](https://apics-online.info/surveys/19)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `fpe` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 261 | 0.0301 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 38 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | ì í | ù ú |
| Close-mid | è é | ò ó |
| Open-mid | ɛ̀ ɛ́ | ɔ̀ ɔ́ |
| Open | à á |  |

Sequences that the spec writes as one unit: [k͡p] [w] [ɡ͡b].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [à] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [è] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gb⟩ | [ɡ͡b] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ì] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kp⟩ | [k͡p] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [ò] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [ù] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨á⟩ | [á] |  |
| ⟨é⟩ | [é] |  |
| ⟨í⟩ | [í] |  |
| ⟨ó⟩ | [ó] |  |
| ⟨ú⟩ | [ú] |  |
| ⟨ɔ⟩ | [ɔ̀] |  |
| ⟨ɔ́⟩ | [ɔ́] |  |
| ⟨ɛ⟩ | [ɛ̀] |  |
| ⟨ɛ́⟩ | [ɛ́] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "fpe")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Farefare](gur.md) · [Home](../index.md) · [Fijian →](fj.md)
