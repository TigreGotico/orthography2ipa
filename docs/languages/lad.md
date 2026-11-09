# Ladino (Judeo-Spanish) (`lad`)

<!-- atlas:summary begin -->
Ladino (Judeo-Spanish) is an Ibero-Romance language, written in the Latin script. Glottolog places it in 14 countries. The `lad` spec is at the research tier. It cites 3 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lad` |
| ISO 639-3 | [lad](https://iso639-3.sil.org/code/lad), Ladino |
| Glottolog | [ladi1251](https://glottolog.org/resource/languoid/id/ladi1251), Ladino |
| Wikidata | [Q36196](https://www.wikidata.org/wiki/Q36196) |
| Wikipedia | [Judaeo-Spanish](https://en.wikipedia.org/wiki/Judaeo-Spanish) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Ibero-Romance](by-family.md#indo-european--italic--romance--ibero-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Albania](by-region.md#albania), [Algeria](by-region.md#algeria), [Bosnia & Herzegovina](by-region.md#bosnia--herzegovina), [Bulgaria](by-region.md#bulgaria), [Croatia](by-region.md#croatia), [Greece](by-region.md#greece), [Israel](by-region.md#israel), [Morocco](by-region.md#morocco) and 6 more |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Ancestor | [Castilian](https://tigregotico.github.io/orthography2ipa/#es-ES-x-medieval) `es-ES-x-medieval` |
| Explorer | [`lad` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lad) |
| Spec file | [`lad.json`](../../orthography2ipa/data/lad.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Ladino (Judezmo / Judeo-Spanish / Spanyolit). Romance language descending from medieval Castilian, preserved since the 1492 expulsion of Jews from Spain.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1994 to 2013. [Sources](#sources) lists them. The spec file writes all 35 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/lad.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `lad` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-harris1994"></a>Harris, T.K. (1994). *Death of a Language: The History of Judeo-Spanish*. University of Delaware Press.
2. <a id="src-penny2002"></a>Penny, R. (2002). *A History of the Spanish Language*. Cambridge University Press. Cited: pp. 16, 18, 276, 280.
3. <a id="src-schmid2013"></a>Schmid, B. (2013). *Judezmo*. In: The Languages and Linguistics of Europe, De Gruyter.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `lad` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 131 | 0.1397 | yes |
| `spain_romance_tts` | `lad` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.0399 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 35 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |
| Affricate |  |  |  | ts | dʒ tʃ |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |
| Trill |  |  |  | r |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |
| Fricative | β | f v | ð | s z | ʃ ʒ |  | ɣ |
| Approximant |  |  |  |  |  | j |  |
| Lateral approximant |  |  |  | l |  | ʎ |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] | default [b] · intervocalic [β] |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] | default [d] · intervocalic [ð] |
| ⟨dj⟩ | [dʒ] |  |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] | default [ɡ] · intervocalic [ɣ] |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [ʎ] [j] | default [ʎ] |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] | before consonant [ɾ] · intervocalic [ɾ] · word final [ɾ] · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] | intervocalic [z] [s] · word final [s] |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ʃ] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨zh⟩ | [ʒ] |  |
| ⟨ç⟩ | [s] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨š⟩ | [ʃ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lad")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Ladin](lld.md) · [Home](../index.md) · [Lak →](lbe.md)
