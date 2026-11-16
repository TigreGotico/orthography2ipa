# Ladin (`lld`)

<!-- atlas:summary begin -->
Ladin is a Gallo-Romance language, written in the Latin script. Glottolog places it in Italy. The `lld` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lld` |
| ISO 639-3 | [lld](https://iso639-3.sil.org/code/lld), Ladin |
| Glottolog | [ladi1250](https://glottolog.org/resource/languoid/id/ladi1250), Ladin |
| Wikidata | [Q36202](https://www.wikidata.org/wiki/Q36202) |
| Wikipedia | [Ladin language](https://en.wikipedia.org/wiki/Ladin_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Gallo-Romance](by-family.md#indo-european--italic--romance--gallo-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Italy](by-region.md#italy) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Parent | [Gallo-Romance](https://tigregotico.github.io/orthography2ipa/#x-clade-gallorom) `x-clade-gallorom` |
| Explorer | [`lld` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lld) |
| Spec file | [`lld.json`](../../orthography2ipa/data/lld.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Ladin. Rhaeto-Romance language of the Dolomites (South Tyrol, Trentino, Belluno). ~30,000 speakers. Key features: (1) CA- → [tʃ] palatalisation. (2) Front rounded vowels /y, ø/. (3) Preservation of Latin PL-, CL-, FL- clusters. (4) Central vowel /ə/ in some varieties.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1977 to 1997. [Sources](#sources) lists them. The spec file writes all 30 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/lld.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `lld` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-maiden_parry1997"></a>Maiden, M. & Parry, M. (eds.) (1997). *The Dialects of Italy*. Routledge.
2. <a id="src-craffonara1977"></a>Craffonara, L. (1977). *Zur Stellung des Ladinischen*. Ladinia.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 37 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |
| Affricate |  |  | dz ts | dʒ tʃ |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |
| Trill |  |  | r |  |  |  |
| Tap |  |  | ɾ |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l |  | ʎ |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i y |  | u |
| Close-mid | e ø |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Open | a |  |  |

Sequences that the spec writes as one unit: [kw] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] [tʃ] |  |
| ⟨ch⟩ | [k] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [dʒ] |  |
| ⟨gh⟩ | [ɡ] |  |
| ⟨gl⟩ | [ʎ] |  |
| ⟨gn⟩ | [ɲ] |  |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] [z] |  |
| ⟨sc⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨z⟩ | [ts] [dz] |  |
| ⟨ë⟩ | [ə] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨ü⟩ | [y] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lld")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kyrgyz](ky.md) · [Home](../index.md) · [Ladino →](lad.md)
