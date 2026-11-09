# Fula (Fulah / Fulfulde / Pular) (`ff`)

<!-- atlas:summary begin -->
Fula (Fulah / Fulfulde / Pular) is an Atlantic-Congo language, written in the Latin script. Glottolog places it in Senegal. The `ff` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ff` |
| ISO 639-3 | [ful](https://iso639-3.sil.org/code/ful), Fulah |
| Glottolog | [fula1264](https://glottolog.org/resource/languoid/id/fula1264), Fula |
| Wikidata | [Q33454](https://www.wikidata.org/wiki/Q33454) |
| Wikipedia | [Fula language](https://en.wikipedia.org/wiki/Fula_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#africa) > [Senegal](by-region.md#senegal) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1800, living |
| Parent | [Atlantic-Congo](https://tigregotico.github.io/orthography2ipa/#x-clade-atla1278) `x-clade-atla1278` |
| Child lects | 2, see [Related lects](#related-lects) |
| Explorer | [`ff` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ff) |
| Spec file | [`ff.json`](../../orthography2ipa/data/ff.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Fula / Fulah / Fulfulde / Pular / Peul. Atlantic-Congo (Senegambian branch) language spoken across the Sahel from Senegal to Sudan by ~65 million people. Major language of Guinea-Bissau (Fula/Pular), Senegal, Guinea, Mali, Nigeria (Fulfulde).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1952 to 1982. [Sources](#sources) lists them. The spec file writes all 42 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ff.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `ff` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Nigerian Fulfulde](fuv.md) `fuv`: Cameroon, Chad, Nigeria, research tier
- [Pular (Fula, Guinea)](fuf.md) `fuf`: Guinea, Guinea-Bissau, Mali, Senegal, Sierra Leone, research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-arnott1970"></a>Arnott, D.W. (1970). *The Nominal and Verbal System of Fula*. Oxford University Press.
2. <a id="src-westermann_bryan1952"></a>Westermann, D. & Bryan, M.A. (1952). *Languages of West Africa*. Oxford University Press / International African Institute.
3. <a id="src-sylla1982"></a>Sylla, Y. (1982). *Grammaire moderne du Pulaar*. Nouvelles Editions Africaines, Dakar.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 39 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  |  | k kː ɡ | ʔ |
| Affricate |  |  |  | dʒ tʃ |  |  |  |  |
| Nasal | m |  | n |  |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |  |
| Tap |  |  |  |  | ɽ |  |  |  |
| Fricative |  | f | s |  |  |  |  | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [mb] [nd] [ndʒ] [w] [ŋɡ] [ɓ] [ɗ] [ʄ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨bh⟩ | [ɓ] |  |
| ⟨c⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dh⟩ | [ɗ] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kk⟩ | [kː] |  |
| ⟨l⟩ | [l] | word final [l] [ɽ] |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [mb] | word initial [mb] |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [nd] | word initial [nd] |
| ⟨ng⟩ | [ŋɡ] | word initial [ŋɡ] |
| ⟨nj⟩ | [ndʒ] | word initial [ndʒ] |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] | word final [o] |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] | word final [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] | word final [u] |
| ⟨uu⟩ | [uː] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ŋ⟩ | [ŋ] |  |
| ⟨ƴ⟩ | [ʄ] |  |
| ⟨ɓ⟩ | [ɓ] |  |
| ⟨ɗ⟩ | [ɗ] |  |
| ⟨ɲ⟩ | [ɲ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ff")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Friulian](fur.md) · [Home](../index.md) · [Ga →](gaa.md)
