# Western Armenian (`hyw`)

<!-- atlas:summary begin -->
Western Armenian is an Armenic language, written in the Armenian script. Glottolog places it in Türkiye. The `hyw` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `hyw` |
| ISO 639-3 | [hyw](https://iso639-3.sil.org/code/hyw), Western Armenian |
| Glottolog | [homs1234](https://glottolog.org/resource/languoid/id/homs1234), Western Armenian |
| Wikidata | [Q180945](https://www.wikidata.org/wiki/Q180945) |
| Wikipedia | [Western Armenian](https://en.wikipedia.org/wiki/Western_Armenian) |
| Family | [Indo-European](by-family.md#indo-european) > [Armenic](by-family.md#indo-european--armenic) |
| Region | [Eurasia](by-region.md#eurasia) > [Türkiye](by-region.md#türkiye) |
| Script | [Armenian](by-script.md#armenian) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Armenian](hy.md) `hy` |
| Explorer | [`hyw` in the data explorer](https://tigregotico.github.io/orthography2ipa/#hyw) |
| Spec file | [`hyw.json`](../../orthography2ipa/data/hyw.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Western Armenian (Արեւմտահայերէն), the standard form of Modern Armenian of the Ottoman/diaspora tradition, written in the Armenian alphabet using classical (Mesropian) spelling.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1998 to 2024. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 40 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/hyw.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `hyw` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-vaux1998"></a>Vaux, Bert (1998). *The Phonology of Armenian*. Oxford University Press.
2. <a id="src-hyw_wiki"></a>Wikipedia contributors (2024). *Western Armenian*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Western_Armenian)
3. <a id="src-hy_alphabet_wiki"></a>Wikipedia contributors (2024). *Armenian alphabet*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Armenian_alphabet)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `hyw` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 17009 | 0.2709 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 34 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b pʰ |  | d tʰ |  |  | kʰ ɡ |  |  |
| Affricate |  |  | dz tsʰ | dʒ tʃʰ |  |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | ʁ χ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid |  |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Open |  |  | ɑ |

Sequences that the spec writes as one unit: [ɛv].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ա⟩ | [ɑ] |  |
| ⟨բ⟩ | [pʰ] |  |
| ⟨գ⟩ | [kʰ] |  |
| ⟨դ⟩ | [tʰ] |  |
| ⟨ե⟩ | [ɛ] |  |
| ⟨զ⟩ | [z] |  |
| ⟨է⟩ | [ɛ] |  |
| ⟨ը⟩ | [ə] |  |
| ⟨թ⟩ | [tʰ] |  |
| ⟨ժ⟩ | [ʒ] |  |
| ⟨ի⟩ | [i] |  |
| ⟨լ⟩ | [l] |  |
| ⟨խ⟩ | [χ] |  |
| ⟨ծ⟩ | [dz] |  |
| ⟨կ⟩ | [ɡ] |  |
| ⟨հ⟩ | [h] |  |
| ⟨ձ⟩ | [tsʰ] |  |
| ⟨ղ⟩ | [ʁ] |  |
| ⟨ճ⟩ | [dʒ] |  |
| ⟨մ⟩ | [m] |  |
| ⟨յ⟩ | [j] [h] |  |
| ⟨ն⟩ | [n] |  |
| ⟨շ⟩ | [ʃ] |  |
| ⟨ո⟩ | [ɔ] |  |
| ⟨ու⟩ | [u] |  |
| ⟨չ⟩ | [tʃʰ] |  |
| ⟨պ⟩ | [b] |  |
| ⟨ջ⟩ | [tʃʰ] |  |
| ⟨ռ⟩ | [r] |  |
| ⟨ս⟩ | [s] |  |
| ⟨վ⟩ | [v] |  |
| ⟨տ⟩ | [d] |  |
| ⟨ր⟩ | [ɾ] |  |
| ⟨ց⟩ | [tsʰ] |  |
| ⟨ւ⟩ | [v] |  |
| ⟨փ⟩ | [pʰ] |  |
| ⟨ք⟩ | [kʰ] |  |
| ⟨օ⟩ | [o] |  |
| ⟨ֆ⟩ | [f] |  |
| ⟨և⟩ | [ɛv] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "hyw")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Western Aragonese](an-x-occident.md) · [Home](../index.md) · [Western Asturian-Leonese →](ast-x-occident.md)
