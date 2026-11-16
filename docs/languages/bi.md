# Bislama (`bi`)

<!-- atlas:summary begin -->
Bislama is an English Creole language, written in the Latin script. Glottolog places it in New Caledonia and Vanuatu. The `bi` spec is at the research tier. It cites 4 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `bi` |
| ISO 639-3 | [bis](https://iso639-3.sil.org/code/bis), Bislama |
| Glottolog | [bisl1239](https://glottolog.org/resource/languoid/id/bisl1239), Bislama |
| Wikipedia | [Bislama](https://en.wikipedia.org/wiki/Bislama) |
| Family | [English Creole](by-family.md#english-creole) |
| Region | [Papunesia](by-region.md#papunesia) > [New Caledonia](by-region.md#new-caledonia), [Vanuatu](by-region.md#vanuatu) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1860, living |
| Explorer | [`bi` in the data explorer](https://tigregotico.github.io/orthography2ipa/#bi) |
| Spec file | [`bi.json`](../../orthography2ipa/data/bi.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Bislama, English-lexifier creole (national language of Vanuatu), with an Oceanic (Austronesian) phonology and grammar. Post-1995 standard orthography: 5 vowels, the digraphs ⟨ae⟩ and ⟨ao⟩ for diphthongs, ⟨ng⟩ /ŋ/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 4 works, from 1989 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 25 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/bi.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `bi` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-crowley2004"></a>Crowley, Terry (2004). *Bislama Reference Grammar*. University of Hawaiʻi Press.
2. <a id="src-bislama_wiki"></a>Wikipedia contributors (2024). *Bislama*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Bislama)
3. <a id="src-holm1989"></a>Holm, John (1989). *Pidgins and Creoles, Volume II: Reference Survey*. Cambridge University Press.
4. <a id="src-apics2013"></a>Michaelis, S.M., Maurer, P., Haspelmath, M. & Huber, M. (eds.) (2013). *The Atlas of Pidgin and Creole Language Structures (APiCS)*. Oxford University Press. [apics-online.info](https://apics-online.info/)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 27 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f v | s |  |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [ae] [ao] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ae⟩ | [ae] |  |
| ⟨ao⟩ | [ao] |  |
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
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "bi")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Biscayan Basque](eu-biscayan.md) · [Home](../index.md) · [Bodo →](brx.md)
