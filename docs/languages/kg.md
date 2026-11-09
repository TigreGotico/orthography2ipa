# Kongo (`kg`)

<!-- atlas:summary begin -->
Kongo is a Bantu language, written in the Latin script. Glottolog places it in Angola, Congo - Brazzaville and Congo - Kinshasa. The `kg` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kg` |
| ISO 639-3 | [kon](https://iso639-3.sil.org/code/kon), Kongo |
| Glottolog | [koon1244](https://glottolog.org/resource/languoid/id/koon1244), South-Central Koongo |
| Wikidata | [Q33702](https://www.wikidata.org/wiki/Q33702) |
| Wikipedia | [Kongo language](https://en.wikipedia.org/wiki/Kongo_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) > [Bantu](by-family.md#atlantic-congo--bantu) |
| Region | [Africa](by-region.md#africa) > [Angola](by-region.md#angola), [Congo - Brazzaville](by-region.md#congo---brazzaville), [Congo - Kinshasa](by-region.md#congo---kinshasa) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Proto-Bantu (family node)](https://tigregotico.github.io/orthography2ipa/#bnt) `bnt` |
| Explorer | [`kg` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kg) |
| Spec file | [`kg.json`](../../orthography2ipa/data/kg.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Kongo / Kikongo (Kikôngo), Bantu zone H (DRC, Congo, Angola). Latin orthography, five vowels with contrastive length written double. Prenasalised consonants are written as digraphs (mb, mp, mf, mv, nd, nt, ns, nz, nk, ng), <ng> is ambiguous between prenasalised /ŋɡ/ and plain /ŋ/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1887 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 35 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kg.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kg` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-bentley1887"></a>Bentley, W. Holman (1887). *Dictionary and Grammar of the Kongo Language*. Baptist Missionary Society / Trübner.
2. <a id="src-kongo_wiki"></a>Wikipedia contributors (2024). *Kongo language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Kongo_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 36 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | k ɡ |
| Nasal | m |  | n |  | ŋ |
| Fricative |  | f v | s z |  |  |
| Approximant |  |  |  | j |  |
| Lateral approximant |  |  | l |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [mb] [mf] [mp] [mv] [nd] [nk] [ns] [nt] [nz] [w] [ŋɡ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [mb] |  |
| ⟨mf⟩ | [mf] |  |
| ⟨mp⟩ | [mp] |  |
| ⟨mv⟩ | [mv] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [nd] |  |
| ⟨ng⟩ | [ŋɡ] [ŋ] |  |
| ⟨nk⟩ | [nk] |  |
| ⟨ns⟩ | [ns] |  |
| ⟨nt⟩ | [nt] |  |
| ⟨nz⟩ | [nz] |  |
| ⟨o⟩ | [o] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kg")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Komi-Permyak](koi.md) · [Home](../index.md) · [Konkani →](kok.md)
