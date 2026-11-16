# Mandinka (`mnk`)

<!-- atlas:summary begin -->
Mandinka is a Mande language, written in the Latin script. Glottolog places it in Gambia, Guinea, Guinea-Bissau and Senegal. The `mnk` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mnk` |
| ISO 639-3 | [mnk](https://iso639-3.sil.org/code/mnk), Mandinka |
| Glottolog | [mand1436](https://glottolog.org/resource/languoid/id/mand1436), Mandinka |
| Wikidata | [Q34845](https://www.wikidata.org/wiki/Q34845) |
| Wikipedia | [Mandinka language](https://en.wikipedia.org/wiki/Mandinka_language) |
| Family | [Mande](by-family.md#mande) |
| Region | [Africa](by-region.md#africa) > [Gambia](by-region.md#gambia), [Guinea](by-region.md#guinea), [Guinea-Bissau](by-region.md#guinea-bissau), [Senegal](by-region.md#senegal) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Mande](https://tigregotico.github.io/orthography2ipa/#x-clade-mand1469) `x-clade-mand1469` |
| Explorer | [`mnk` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mnk) |
| Spec file | [`mnk.json`](../../orthography2ipa/data/mnk.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Mandinka (Mandingo), the Manding branch of Mande, spoken in Casamance (Senegal), the Gambia (where it is co-official) and Guinea-Bissau.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 2013 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 29 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mnk.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mnk` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-mnk_wiki"></a>Wikipedia contributors (2026). *Mandinka language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Mandinka_language)
2. <a id="src-creissels_sambou_2013"></a>Creissels, Denis and Sambou, Pierre (2013). *Le mandinka (Sénégal, Gambie, Guinée-Bissau): phonologie, grammaire, textes*. Karthala.
3. <a id="src-wals_tone"></a>Maddieson, Ian (2013). *Tone (WALS chapter 13)*. World Atlas of Language Structures Online. [wals.info](https://wals.info/chapter/13)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 29 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f | s |  |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ŋ⟩ | [ŋ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mnk")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Mandarin Chinese](zh.md) · [Home](../index.md) · [Mansi →](mns.md)
