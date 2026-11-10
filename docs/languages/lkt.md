# Lakota (`lkt`)

<!-- atlas:summary begin -->
Lakota is a Siouan language, written in the Latin script. Glottolog places it in Canada and United States. The `lkt` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lkt` |
| ISO 639-3 | [lkt](https://iso639-3.sil.org/code/lkt), Lakota |
| Glottolog | [lako1247](https://glottolog.org/resource/languoid/id/lako1247), Lakota |
| Wikidata | [Q33537](https://www.wikidata.org/wiki/Q33537) |
| Wikipedia | [Lakota language](https://en.wikipedia.org/wiki/Lakota_language) |
| Family | [Siouan](by-family.md#siouan) |
| Region | [North America](by-region.md#north-america) > [Canada](by-region.md#canada), [United States](by-region.md#united-states) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Siouan](https://tigregotico.github.io/orthography2ipa/#x-clade-siou1252) `x-clade-siou1252` |
| Explorer | [`lkt` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lkt) |
| Spec file | [`lkt.json`](../../orthography2ipa/data/lkt.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Lakota (Lakȟótiyapi), Siouan (Dakotan branch, sister to Dakota). Orthography follows the New Lakota Dictionary / Lakota Language Consortium (LLC) standard.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1996 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 39 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/lkt.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `lkt` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-lakota_wiki"></a>Wikipedia contributors (2026). *Lakota language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Lakota_language)
2. <a id="src-ullrich2008"></a>Ullrich, Jan (ed.) (2008). *New Lakota Dictionary*. Lakota Language Consortium.
3. <a id="src-rood_taylor1996"></a>Rood, David S. & Taylor, Allan R. (1996). *Sketch of Lakhota, a Siouan Language*. Handbook of North American Indians, Vol. 17 (Smithsonian Institution).
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 41 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ pʼ | t tʰ tʼ |  |  | k kʰ kʼ |  | ʔ |
| Affricate |  |  | tʃ tʃʰ tʃʼ |  |  |  |  |
| Nasal | m | n |  |  |  |  |  |
| Trill |  |  |  |  |  | ʀ |  |
| Fricative |  | s sʼ z | ʃ ʃʼ ʒ |  | ɣ | ʁ χ χʼ | h |
| Approximant |  |  |  | j |  |  |  |
| Lateral approximant |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i ĩ | u ũ |
| Close-mid | e | o |
| Open | a ã |  |

Sequences that the spec writes as one unit: [kˣ] [pˣ] [tˣ] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨aŋ⟩ | [ã] |  |
| ⟨e⟩ | [e] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨iŋ⟩ | [ĩ] |  |
| ⟨k⟩ | [k] |  |
| ⟨k'⟩ | [kʼ] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨kȟ⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨p'⟩ | [pʼ] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨pȟ⟩ | [pʰ] |  |
| ⟨s⟩ | [s] |  |
| ⟨s'⟩ | [sʼ] |  |
| ⟨t⟩ | [t] |  |
| ⟨t'⟩ | [tʼ] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨tȟ⟩ | [tʰ] |  |
| ⟨u⟩ | [u] |  |
| ⟨uŋ⟩ | [ũ] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨č'⟩ | [tʃʼ] |  |
| ⟨čh⟩ | [tʃʰ] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨š'⟩ | [ʃʼ] |  |
| ⟨ž⟩ | [ʒ] |  |
| ⟨ǧ⟩ | [ʁ] |  |
| ⟨ȟ⟩ | [χ] |  |
| ⟨ȟ'⟩ | [χʼ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lkt")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Lak](lbe.md) · [Home](../index.md) · [Lamboya →](lmy.md)
