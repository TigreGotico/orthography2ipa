# Ndonga (`ng`)

<!-- atlas:summary begin -->
Ndonga is an Atlantic-Congo language, written in the Latin script. Glottolog places it in Angola and Namibia. The `ng` spec is at the research tier. It cites 5 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ng` |
| ISO 639-3 | [ndo](https://iso639-3.sil.org/code/ndo), Ndonga |
| Glottolog | [ndon1254](https://glottolog.org/resource/languoid/id/ndon1254), Ndonga |
| Wikidata | [Q33900](https://www.wikidata.org/wiki/Q33900) |
| Wikipedia | [Ndonga](https://en.wikipedia.org/wiki/Ndonga) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#africa) > [Angola](by-region.md#angola), [Namibia](by-region.md#namibia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Atlantic-Congo](https://tigregotico.github.io/orthography2ipa/#x-clade-atla1278) `x-clade-atla1278` |
| Explorer | [`ng` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ng) |
| Spec file | [`ng.json`](../../orthography2ipa/data/ng.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Ndonga (Oshindonga), the main Ovambo (Bantu) language of northern Namibia and southern Angola. INPUT CONTRACT: the current standard Namibian orthography (Oshindonga omunyolelo / 'Oshindonga Orthography 3', 2004, implemented by NIED) is assumed, text is expected to be already normalised.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 5 works, from 2003 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 40 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ng.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ng` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 4 of them have a DOI or a URL. The spec file holds a note on what 4 of them support.

1. <a id="src-ndonga_wiki"></a>Wikipedia contributors (2026). *Ndonga*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Ndonga)
2. <a id="src-omniglot_ndonga"></a>Ager, S. (2024). *Ndonga language, alphabet and pronunciation*. Omniglot. [omniglot.com](https://www.omniglot.com/writing/ndonga.htm)
3. <a id="src-fivaz2003"></a>Fivaz, D. (2003). *A Reference Grammar of Oshindonga*. Out of Africa Publishers, Windhoek.
4. <a id="src-ndonga_phonology_wiki"></a>Wikipedia contributors (2025). *Ndonga, Phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Ndonga)
5. <a id="src-oshindonga_orthography3"></a>Namibia. Ministry of Education, National Institute for Educational Development (NIED) (2004). *Oshindonga: omunyolelo 3 / Oshindonga: Orthography 3*. Gamsberg Macmillan, Windhoek. [search.worldcat.org](https://search.worldcat.org/title/61883307)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 40 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k |  |
| Affricate |  |  |  | ts | dʒ |  |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |
| Trill |  |  |  | r |  |  |  |  |
| Fricative |  | f v | ð θ | s z | ʃ |  | x ɣ | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [kw] [mb] [nd] [ndʒ] [w] [ŋɡ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨d⟩ | [d] |  |
| ⟨dh⟩ | [ð] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɣ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [mb] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [nd] |  |
| ⟨ndj⟩ | [ndʒ] |  |
| ⟨ng⟩ | [ŋ] [ŋɡ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [kw] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [θ] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ng")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Nawat](ppl.md) · [Home](../index.md) · [Neapolitan →](nap.md)
