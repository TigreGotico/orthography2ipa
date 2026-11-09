# Pijin (`pis`)

<!-- atlas:summary begin -->
Pijin is an English Creole language, written in the Latin script. Glottolog places it in Solomon Islands. The `pis` spec is at the research tier. It cites 4 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `pis` |
| ISO 639-3 | [pis](https://iso639-3.sil.org/code/pis), Pijin |
| Glottolog | [piji1239](https://glottolog.org/resource/languoid/id/piji1239), Pijin |
| Wikidata | [Q36699](https://www.wikidata.org/wiki/Q36699) |
| Wikipedia | [Pijin](https://en.wikipedia.org/wiki/Pijin) |
| Family | [English Creole](by-family.md#english-creole) |
| Region | [Papunesia](by-region.md#papunesia) > [Solomon Islands](by-region.md#solomon-islands) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1870, living |
| Explorer | [`pis` in the data explorer](https://tigregotico.github.io/orthography2ipa/#pis) |
| Spec file | [`pis.json`](../../orthography2ipa/data/pis.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Pijin (Solomon Islands Pijin), the lingua franca of the Solomon Islands, an English-lexifier Pacific creole closely related to Tok Pisin (Papua New Guinea) and Bislama (Vanuatu).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 4 works, from 1989 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 25 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/pis.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `pis` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-pis_wiki"></a>Wikipedia contributors (2024). *Pijin*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Pijin)
2. <a id="src-jourdan2007"></a>Jourdan, Christine (2007). *Solomon Islands Pijin: phonetics and phonology*. De Gruyter Mouton, in Varieties of English. DOI [10.1515/9783110208412.1.164](https://doi.org/10.1515/9783110208412.1.164)
3. <a id="src-simons_young2007"></a>Simons, Linda & Young, Hugh (2007). *Pijin: A Grammar of Solomon Islands Pidgin*. SIL-PNG / Pacific Linguistics.
4. <a id="src-holm1989"></a>Holm, John (1989). *Pidgins and Creoles, Volume II: Reference Survey*. Cambridge University Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 26 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | k ɡ |  |
| Affricate |  |  |  | dʒ |  |  |
| Nasal | m |  | n |  | ŋ |  |
| Trill |  |  | r |  |  |  |
| Tap |  |  | ɾ |  |  |  |
| Fricative |  | f v | s |  |  | h |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [ai] [au] [oi] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [ai] |  |
| ⟨au⟩ | [au] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] |  |
| ⟨oi⟩ | [oi] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "pis")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Piedmontese](pms.md) · [Home](../index.md) · [Pitjantjatjara →](pjt.md)
