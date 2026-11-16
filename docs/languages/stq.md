# Saterland Frisian (`stq`)

<!-- atlas:summary begin -->
Saterland Frisian is a West Germanic language, written in the Latin script. Glottolog places it in Germany. The `stq` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `stq` |
| ISO 639-3 | [stq](https://iso639-3.sil.org/code/stq), Saterfriesisch |
| Glottolog | [sate1242](https://glottolog.org/resource/languoid/id/sate1242), Ems-Weser Frisian |
| Wikidata | [Q27154](https://www.wikidata.org/wiki/Q27154) |
| Wikipedia | [Saterland Frisian](https://en.wikipedia.org/wiki/Saterland_Frisian) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > West Germanic](by-family.md#indo-european--germanic--northwest-germanic--west-germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [Germany](by-region.md#germany) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1700, living |
| Ancestor | [Old Frisian](https://tigregotico.github.io/orthography2ipa/#ofs) `ofs` |
| Explorer | [`stq` in the data explorer](https://tigregotico.github.io/orthography2ipa/#stq) |
| Spec file | [`stq.json`](../../orthography2ipa/data/stq.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Saterland Frisian (Seeltersk), the last surviving variety of East Frisian, spoken by ~1,000, 2,500 people in the four Saterland municipalities (Ramsloh, Strücklingen, Scharrel, Sedelsberg) in the Cloppenburg district of Lower Saxony, Germany.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1980 to 2020. [Sources](#sources) lists them. The spec file writes all 54 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/stq.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `stq` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-peters2017"></a>Peters, Jörg (2019). *Saterland Frisian*. Journal of the International Phonetic Association 49(2), 223-230. Cited: 223-230. [doi.org](https://doi.org/10.1017/S0025100317000226)
2. <a id="src-fort1980"></a>Fort, M.C. (1980). *Saterfriesisches Wörterbuch*. Helmut Buske Verlag.
3. <a id="src-kramer1982"></a>Kramer, P. (1982). *Ksjansen: The Sounds of Saterland Frisian*. Fryske Akademy.
4. <a id="src-markey1981"></a>Markey, T.L. (1981). *Frisian*. Mouton.
5. <a id="src-bergqvist2020"></a>Bergqvist, Sean (2020). *“Wie schrieuwe Seeltersk”, a study of the orthography of Saterland Frisian literary texts*. Us Wurk LXIX, 73, 91. Cited: 80, 82. [ugp.rug.nl](https://ugp.rug.nl/uswurk/article/download/36959/34463/46308)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `stq` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 818 | 0.1959 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 55 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  | ts |  |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f v | s z | ʃ |  | x ɣ | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː yː |  | uː |
| Near-close | ɪ ʏ |  | ʊ |
| Close-mid | eː øː |  | oː |
| Mid |  | ə |  |
| Open-mid | œ ɛ ɛː |  | ɔ ɔː |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [ai] [au] [iə] [ks] [oə] [sp] [st] [uə] [w] [ŋk] [œi] [ɔi] [ɔu] [ɛi] [ʃp] [ʃt].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] | default [a] · open syllable [aː] |
| ⟨aa⟩ | [aː] |  |
| ⟨ai⟩ | [ai] |  |
| ⟨au⟩ | [au] |  |
| ⟨b⟩ | [b] | default [b] · word final [b] [p] |
| ⟨c⟩ | [k] |  |
| ⟨ch⟩ | [x] |  |
| ⟨d⟩ | [d] | default [d] · word final [d] [t] |
| ⟨e⟩ | [ɛ] [ə] | default [ɛ] [ə] · nucleus stressed [ɛ] · nucleus unstressed [ə] |
| ⟨ee⟩ | [eː] |  |
| ⟨ei⟩ | [ɛi] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [ɣ] | default [ɡ] [ɣ] · word final [ɡ] [ɣ] [k] |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ɪ] | default [ɪ] · open syllable [iː] |
| ⟨ie⟩ | [iː] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨o⟩ | [ɔ] | default [ɔ] · open syllable [oː] |
| ⟨oa⟩ | [ɔː] |  |
| ⟨oi⟩ | [ɔi] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨ou⟩ | [ɔu] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] [z] | default [s] · intervocalic [z] · word initial [z] |
| ⟨sch⟩ | [ʃ] |  |
| ⟨sp⟩ | [sp] [ʃp] |  |
| ⟨st⟩ | [st] [ʃt] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨u⟩ | [ʊ] | default [ʊ] · open syllable [uː] |
| ⟨uu⟩ | [uː] |  |
| ⟨v⟩ | [v] | default [v] · word final [v] [f] |
| ⟨w⟩ | [v] [w] |  |
| ⟨x⟩ | [ks] |  |
| ⟨z⟩ | [ts] |  |
| ⟨ä⟩ | [ɛ] |  |
| ⟨äi⟩ | [ɛi] |  |
| ⟨ää⟩ | [ɛː] |  |
| ⟨ë⟩ | [ə] |  |
| ⟨í⟩ | [iː] |  |
| ⟨ö⟩ | [œ] |  |
| ⟨öi⟩ | [œi] |  |
| ⟨öö⟩ | [øː] |  |
| ⟨ú⟩ | [uː] |  |
| ⟨úu⟩ | [uː] |  |
| ⟨ü⟩ | [ʏ] |  |
| ⟨üü⟩ | [yː] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "stq")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Sassarese Sardinian](sdc.md) · [Home](../index.md) · [Saʿīdi Arabic →](aec-EG.md)
