# Ewe (`ee`)

<!-- atlas:summary begin -->
Ewe is an Atlantic-Congo language, written in the Latin script. Glottolog places it in Ghana and Togo. The `ee` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ee` |
| ISO 639-3 | [ewe](https://iso639-3.sil.org/code/ewe), Ewe |
| Glottolog | [ewee1241](https://glottolog.org/resource/languoid/id/ewee1241), Ewe |
| Wikidata | [Q30005](https://www.wikidata.org/wiki/Q30005) |
| Wikipedia | [Ewe language](https://en.wikipedia.org/wiki/Ewe_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#africa) > [Ghana](by-region.md#ghana), [Togo](by-region.md#togo) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1857, living |
| Parent | [Atlantic-Congo](https://tigregotico.github.io/orthography2ipa/#x-clade-atla1278) `x-clade-atla1278` |
| Explorer | [`ee` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ee) |
| Spec file | [`ee.json`](../../orthography2ipa/data/ee.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Ewe (Eʋegbe), Gbe (Atlantic-Congo), Ghana and Togo. Latin alphabet with the Africa Alphabet letters ɖ ƒ ɣ ŋ ɔ ɛ ʋ and the digraphs dz gb kp ny ts.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1961 to 1991. [Sources](#sources) lists them. The spec file writes all 126 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ee.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ee` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-ansre1961"></a>Ansre, Gilbert (1961). *The Tonal Structure of Ewe*. Hartford Seminary Foundation.
2. <a id="src-capo1991"></a>Capo, Hounkpati B. C. (1991). *A Comparative Phonology of Gbe*. Foris / de Gruyter.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ee` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 247 | 0.4445 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 103 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t | ɖ |  | k ɡ |  |
| Affricate |  |  | d͡z t͡s |  |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Tap |  |  | ɾ ɾ̃ | ɽ |  |  |  |
| Fricative | ɸ β | f v | s z |  |  | x ɣ | h |
| Approximant |  |  |  |  | j | ɰ |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i ì í î ĩ ĩ̀ ĩ́ ĩ̂ ĩ̌ ǐ |  | u ù ú û ũ ũ̀ ũ̂ ũ̌ ǔ ṹ |
| Close-mid | e è é ê ě ẽ ẽ̀ ẽ́ ẽ̂ ẽ̌ |  | o ò ó ô õ õ̀ õ̂ õ̌ ǒ ṍ |
| Mid |  | ə |  |
| Open-mid | ɛ ɛ̀ ɛ́ ɛ̂ ɛ̃ ɛ̃̀ ɛ̃́ ɛ̃̂ ɛ̃̌ ɛ̌ |  | ɔ ɔ̀ ɔ́ ɔ̂ ɔ̃ ɔ̃̀ ɔ̃́ ɔ̃̂ ɔ̃̌ ɔ̌ |
| Open | a à á â ã ã̀ ã́ ã̂ ã̌ ǎ |  |  |

Sequences that the spec writes as one unit: [k͡p] [w] [ɡ͡b].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨dz⟩ | [d͡z] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gb⟩ | [ɡ͡b] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨kp⟩ | [k͡p] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] | after consonant [l] · default [r] |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [t͡s] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [ɰ] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨à⟩ | [à] |  |
| ⟨à̃⟩ | [ã̀] |  |
| ⟨á⟩ | [á] |  |
| ⟨á̃⟩ | [ã́] |  |
| ⟨â⟩ | [â] |  |
| ⟨ã⟩ | [ã] |  |
| ⟨ã̀⟩ | [ã̀] |  |
| ⟨ã́⟩ | [ã́] |  |
| ⟨ã̂⟩ | [ã̂] |  |
| ⟨ã̌⟩ | [ã̌] |  |
| ⟨è⟩ | [è] |  |
| ⟨è̃⟩ | [ẽ̀] |  |
| ⟨é⟩ | [é] |  |
| ⟨é̃⟩ | [ẽ́] |  |
| ⟨ê⟩ | [ê] |  |
| ⟨ì⟩ | [ì] |  |
| ⟨ì̃⟩ | [ĩ̀] |  |
| ⟨í⟩ | [í] |  |
| ⟨í̃⟩ | [ĩ́] |  |
| ⟨î⟩ | [î] |  |
| ⟨î̃⟩ | [ĩ̂] |  |
| ⟨ò⟩ | [ò] |  |
| ⟨ò̃⟩ | [õ̀] |  |
| ⟨ó⟩ | [ó] |  |
| ⟨ó̃⟩ | [ṍ] |  |
| ⟨ô⟩ | [ô] |  |
| ⟨õ⟩ | [õ] |  |
| ⟨õ̀⟩ | [õ̀] |  |
| ⟨õ̂⟩ | [õ̂] |  |
| ⟨õ̌⟩ | [õ̌] |  |
| ⟨ù⟩ | [ù] |  |
| ⟨ù̃⟩ | [ũ̀] |  |
| ⟨ú⟩ | [ú] |  |
| ⟨ú̃⟩ | [ṹ] |  |
| ⟨û⟩ | [û] |  |
| ⟨û̃⟩ | [ũ̂] |  |
| ⟨ě⟩ | [ě] |  |
| ⟨ě̃⟩ | [ẽ̌] |  |
| ⟨ĩ⟩ | [ĩ] |  |
| ⟨ĩ̀⟩ | [ĩ̀] |  |
| ⟨ĩ́⟩ | [ĩ́] |  |
| ⟨ĩ̂⟩ | [ĩ̂] |  |
| ⟨ĩ̌⟩ | [ĩ̌] |  |
| ⟨ŋ⟩ | [ŋ] |  |
| ⟨ũ⟩ | [ũ] |  |
| ⟨ũ̀⟩ | [ũ̀] |  |
| ⟨ũ̂⟩ | [ũ̂] |  |
| ⟨ũ̌⟩ | [ũ̌] |  |
| ⟨ƒ⟩ | [ɸ] |  |
| ⟨ǎ⟩ | [ǎ] |  |
| ⟨ǎ̃⟩ | [ã̌] |  |
| ⟨ǐ⟩ | [ǐ] |  |
| ⟨ǐ̃⟩ | [ĩ̌] |  |
| ⟨ǒ⟩ | [ǒ] |  |
| ⟨ǒ̃⟩ | [õ̌] |  |
| ⟨ǔ⟩ | [ǔ] |  |
| ⟨ǔ̃⟩ | [ũ̌] |  |
| ⟨ɔ⟩ | [ɔ] |  |
| ⟨ɔ̀⟩ | [ɔ̀] |  |
| ⟨ɔ̀̃⟩ | [ɔ̃̀] |  |
| ⟨ɔ́⟩ | [ɔ́] |  |
| ⟨ɔ́̃⟩ | [ɔ̃́] |  |
| ⟨ɔ̂⟩ | [ɔ̂] |  |
| ⟨ɔ̂̃⟩ | [ɔ̃̂] |  |
| ⟨ɔ̃⟩ | [ɔ̃] |  |
| ⟨ɔ̃̀⟩ | [ɔ̃̀] |  |
| ⟨ɔ̃́⟩ | [ɔ̃́] |  |
| ⟨ɔ̃̂⟩ | [ɔ̃̂] |  |
| ⟨ɔ̃̌⟩ | [ɔ̃̌] |  |
| ⟨ɔ̌⟩ | [ɔ̌] |  |
| ⟨ɔ̌̃⟩ | [ɔ̃̌] |  |
| ⟨ɖ⟩ | [ɖ] |  |
| ⟨ɛ⟩ | [ɛ] |  |
| ⟨ɛ̀⟩ | [ɛ̀] |  |
| ⟨ɛ̀̃⟩ | [ɛ̃̀] |  |
| ⟨ɛ́⟩ | [ɛ́] |  |
| ⟨ɛ́̃⟩ | [ɛ̃́] |  |
| ⟨ɛ̂⟩ | [ɛ̂] |  |
| ⟨ɛ̂̃⟩ | [ɛ̃̂] |  |
| ⟨ɛ̃⟩ | [ɛ̃] |  |
| ⟨ɛ̃̀⟩ | [ɛ̃̀] |  |
| ⟨ɛ̃́⟩ | [ɛ̃́] |  |
| ⟨ɛ̃̂⟩ | [ɛ̃̂] |  |
| ⟨ɛ̃̌⟩ | [ɛ̃̌] |  |
| ⟨ɛ̌⟩ | [ɛ̌] |  |
| ⟨ɛ̌̃⟩ | [ɛ̃̌] |  |
| ⟨ɣ⟩ | [ɣ] |  |
| ⟨ʋ⟩ | [β] |  |
| ⟨ṍ⟩ | [ṍ] |  |
| ⟨ṹ⟩ | [ṹ] |  |
| ⟨ẫ⟩ | [ã̂] |  |
| ⟨ẽ⟩ | [ẽ] |  |
| ⟨ẽ̀⟩ | [ẽ̀] |  |
| ⟨ẽ́⟩ | [ẽ́] |  |
| ⟨ẽ̂⟩ | [ẽ̂] |  |
| ⟨ẽ̌⟩ | [ẽ̌] |  |
| ⟨ễ⟩ | [ẽ̂] |  |
| ⟨ỗ⟩ | [õ̂] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ee")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Evenki](evn.md) · [Home](../index.md) · [Ewondo →](ewo.md)
