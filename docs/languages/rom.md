# Romani (`rom`)

<!-- atlas:summary begin -->
Romani is an Indo-Aryan language, written in the Latin script. Glottolog places it in 32 countries. The `rom` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `rom` |
| ISO 639-3 | [rom](https://iso639-3.sil.org/code/rom), Romany |
| Glottolog | [vlax1238](https://glottolog.org/resource/languoid/id/vlax1238), Vlax Romani |
| Wikidata | [Q13201](https://www.wikidata.org/wiki/Q13201) |
| Wikipedia | [Romani language](https://en.wikipedia.org/wiki/Romani_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [Albania](by-region.md#albania), [Austria](by-region.md#austria), [Belarus](by-region.md#belarus), [Bosnia & Herzegovina](by-region.md#bosnia--herzegovina), [Bulgaria](by-region.md#bulgaria), [Croatia](by-region.md#croatia), [Czechia](by-region.md#czechia), [Finland](by-region.md#finland) and 24 more |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1400, living |
| Parent | [Indo-Aryan](https://tigregotico.github.io/orthography2ipa/#x-clade-indo1321) `x-clade-indo1321` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`rom` in the data explorer](https://tigregotico.github.io/orthography2ipa/#rom) |
| Spec file | [`rom.json`](../../orthography2ipa/data/rom.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Romani (Vlax dialect group, standard reference). Indo-Aryan language of the Roma people. Highly diverse with many dialects. Aspirated stops čh, kh, ph, th are distinctive (Sanskrit inheritance). Phonology influenced by contact with European languages.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 2011 to 2024. [Sources](#sources) lists them. The spec file writes all 40 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/rom.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `rom` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Romano-Serbian](https://tigregotico.github.io/orthography2ipa/#rsb) `rsb`: Serbia, stub tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-wiki-rom"></a>Wikipedia contributors (2024). *Romani language*.
2. <a id="src-matras2011"></a>Matras, Yaron (2011). *Romani. In Kortmann & van der Auwera (eds.), The Languages and Linguistics of Europe: A Comprehensive Guide, 257-268*. De Gruyter Mouton, author's manuscript on yaronmatras.org. Cited: 257-268 (chapter), §2.1 is the third page of the manuscript, which carries no printed numbers. [yaronmatras.org](https://yaronmatras.org/wp-content/uploads/2021/10/matras-y.-2011.-romani.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 32 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  |  | k kʰ ɡ |  |
| Affricate |  |  |  | dʒ tʃ tʃʰ |  |  |  |
| Nasal | m |  | n |  |  |  |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | ɕ ʑ | x | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [x] |  |
| ⟨d⟩ | [d] |  |
| ⟨dž⟩ | [dʒ] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [v] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨zh⟩ | [ʒ] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨čh⟩ | [tʃʰ] |  |
| ⟨ř⟩ | [r] |  |
| ⟨ś⟩ | [ɕ] |  |
| ⟨ź⟩ | [ʑ] |  |
| ⟨ǎ⟩ | [a] |  |
| ⟨ǐ⟩ | [i] |  |
| ⟨ǒ⟩ | [o] |  |
| ⟨ǔ⟩ | [u] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "rom")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Romanesco](it-IT-x-roma.md) · [Home](../index.md) · [Romansh →](rm.md)
