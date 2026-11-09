# West Frisian (`fy`)

<!-- atlas:summary begin -->
West Frisian is a West Germanic language, written in the Latin script. Glottolog places it in Netherlands. The `fy` spec is at the research tier. It cites 4 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `fy` |
| ISO 639-3 | [fry](https://iso639-3.sil.org/code/fry), Western Frisian |
| Glottolog | [west2354](https://glottolog.org/resource/languoid/id/west2354), Western Frisian |
| Wikidata | [Q27175](https://www.wikidata.org/wiki/Q27175) |
| Wikipedia | [West Frisian language](https://en.wikipedia.org/wiki/West_Frisian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > West Germanic](by-family.md#indo-european--germanic--northwest-germanic--west-germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [Netherlands](by-region.md#netherlands) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Ancestor | [Old Frisian](https://tigregotico.github.io/orthography2ipa/#ofs) `ofs` |
| Explorer | [`fy` in the data explorer](https://tigregotico.github.io/orthography2ipa/#fy) |
| Spec file | [`fy.json`](../../orthography2ipa/data/fy.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> West Frisian (Frysk), the most widely spoken Frisian language, spoken in the province of Fryslân (Friesland), Netherlands, where it is an official language alongside Dutch.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1999 to 2006. [Sources](#sources) lists them. The spec file writes all 57 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/fy.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `fy` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-tiersma1999"></a>Tiersma, P.M. (1999). *Frisian Reference Grammar*. Fryske Akademy.
2. <a id="src-hoekstra2001"></a>Hoekstra, J. (2001). *Standard West Frisian*. In: Munske, H.H. (ed.), Handbuch des Friesischen / Handbook of Frisian Studies, Niemeyer. Cited: pp. 83-98.
3. <a id="src-popkema2006"></a>Popkema, J. (2006). *Grammatica Fries: de regels van het Fries*. Bornmeer.
4. <a id="src-gorter2001"></a>Gorter, D. et al. (2001). *Frisian in the Netherlands*. Mercator Education.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `fy` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1091 | 0.2182 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `fy` | generated | epitran-derived | CC0 1.0 | 10681 | 0.3243 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 56 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | k ɡ |  |  |
| Affricate |  |  | ts | tɕ |  |  |  |
| Nasal | m |  | n |  | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f v | s z | ɕ | ɣ | χ | h |
| Approximant |  | ʋ |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː yː |  | u uː |
| Near-close | ɪ |  |  |
| Close-mid | eː ø |  | oː |
| Mid |  | ə |  |
| Open-mid | ɛ ɛː |  | ɔ ɔː |
| Open | a aː |  | ɑ |

Sequences that the spec writes as one unit: [aj] [aːj] [iə] [iːw] [ks] [oj] [oə] [oːj] [uːj] [w] [øy] [ŋk] [ɔu] [ɛi] [ɪə].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨aai⟩ | [aːj] |  |
| ⟨ai⟩ | [aj] |  |
| ⟨au⟩ | [ɔu] |  |
| ⟨b⟩ | [b] | default [b] · word final [p] |
| ⟨c⟩ | [k] [s] | before e [s] · before i [s] · default [k] |
| ⟨ch⟩ | [χ] |  |
| ⟨d⟩ | [d] | default [d] · word final [t] |
| ⟨e⟩ | [ɛ] [ə] | default [ɛ] [ə] · nucleus stressed [ɛ] · nucleus unstressed [ə] |
| ⟨ea⟩ | [ɪə] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨ei⟩ | [ɛi] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [ɣ] | default [ɡ] · intervocalic [ɣ] · word final [χ] · word initial [ɡ] |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ɪ] |  |
| ⟨ie⟩ | [iə] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨iuw⟩ | [iːw] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨oa⟩ | [oə] |  |
| ⟨oai⟩ | [oːj] |  |
| ⟨oe⟩ | [uː] |  |
| ⟨oei⟩ | [uːj] |  |
| ⟨oi⟩ | [oj] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨ou⟩ | [ɔu] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sj⟩ | [ɕ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [t] |  |
| ⟨tj⟩ | [tɕ] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨tsj⟩ | [tɕ] |  |
| ⟨u⟩ | [ø] |  |
| ⟨ui⟩ | [øy] |  |
| ⟨uu⟩ | [yː] |  |
| ⟨v⟩ | [v] | default [v] · word final [f] |
| ⟨w⟩ | [ʋ] [w] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [i] |  |
| ⟨z⟩ | [z] | default [z] · word final [s] |
| ⟨â⟩ | [ɔː] |  |
| ⟨ê⟩ | [ɛː] |  |
| ⟨ô⟩ | [oː] |  |
| ⟨ú⟩ | [yː] |  |
| ⟨û⟩ | [uː] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "fy")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← West Coast Bajau](bdr.md) · [Home](../index.md) · [West Makian →](mqs.md)
