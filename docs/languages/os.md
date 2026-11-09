# Ossetian (`os`)

<!-- atlas:summary begin -->
Ossetian is an Iranian language, written in the Cyrillic script. Glottolog places it in Russia. The `os` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `os` |
| Glottolog | [iron1242](https://glottolog.org/resource/languoid/id/iron1242), Iron Ossetian |
| Wikidata | [Q33968](https://www.wikidata.org/wiki/Q33968) |
| Wikipedia | [Ossetian language](https://en.wikipedia.org/wiki/Ossetian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Iranian](by-family.md#indo-european--indo-iranian--iranian) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1798, living |
| Parent | [Iranian](https://tigregotico.github.io/orthography2ipa/#x-clade-iran1269) `x-clade-iran1269` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`os` in the data explorer](https://tigregotico.github.io/orthography2ipa/#os) |
| Spec file | [`os.json`](../../orthography2ipa/data/os.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Ossetian (ирон æвзаг), Iron literary standard, Eastern Iranian language of the Caucasus, written in Cyrillic since 1938. The alphabet extends Russian Cyrillic with ⟨ӕ⟩ /ɐ/, the ejective digraphs ⟨къ пъ тъ цъ чъ⟩, the uvulars ⟨хъ⟩ /q/ and ⟨гъ⟩ /ʁ/, and the labialised series written with a following ⟨у⟩ (гу, ку, хъу, …).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1964 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 41 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/os.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `os` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Digor Ossetic](https://tigregotico.github.io/orthography2ipa/#osd) `osd`: stub tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-abaev1964"></a>Abaev, V. I. (1964). *A Grammatical Sketch of Ossetic*. Indiana University.
2. <a id="src-ossetian_wiki"></a>Wikipedia contributors (2025). *Ossetian language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Ossetian_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 43 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʼ |  | d t tʼ |  |  | k kʷ kʷʼ kʼ ɡ ɡʷ | q qʷ |
| Affricate |  |  | dz ts tsʼ | dʒ tʃ tʃʼ |  |  |  |
| Nasal | m |  | n |  |  |  |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | ʁ ʁʷ χ χʷ |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | ɫ |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e | ɘ | o |
| Near-open |  | ɐ |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨гу⟩ | [ɡʷ] |  |
| ⟨гъ⟩ | [ʁ] |  |
| ⟨гъу⟩ | [ʁʷ] |  |
| ⟨д⟩ | [d] |  |
| ⟨дж⟩ | [dʒ] |  |
| ⟨дз⟩ | [z] [dz] |  |
| ⟨е⟩ | [e] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [ʒ] [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨ку⟩ | [kʷ] |  |
| ⟨къ⟩ | [kʼ] |  |
| ⟨къу⟩ | [kʷʼ] |  |
| ⟨л⟩ | [ɫ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨пъ⟩ | [pʼ] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [ʃ] [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨тъ⟩ | [tʼ] |  |
| ⟨у⟩ | [u] [w] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [χ] |  |
| ⟨ху⟩ | [χʷ] |  |
| ⟨хъ⟩ | [q] |  |
| ⟨хъу⟩ | [qʷ] |  |
| ⟨ц⟩ | [s] [ts] |  |
| ⟨цъ⟩ | [tsʼ] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨чъ⟩ | [tʃʼ] |  |
| ⟨ы⟩ | [ɘ] |  |
| ⟨ӕ⟩ | [ɐ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "os")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Oromo](om.md) · [Home](../index.md) · [Ottoman Turkish →](ota.md)
