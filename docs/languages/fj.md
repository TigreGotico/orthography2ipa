# Fijian (`fj`)

<!-- atlas:summary begin -->
Fijian is a Malayo-Polynesian language, written in the Latin script. Glottolog places it in Fiji. The `fj` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `fj` |
| ISO 639-3 | [fij](https://iso639-3.sil.org/code/fij), Fijian |
| Glottolog | [fiji1243](https://glottolog.org/resource/languoid/id/fiji1243), Fijian |
| Wikipedia | [Fijian language](https://en.wikipedia.org/wiki/Fijian_language) |
| Family | [Austronesian](by-family.md#austronesian) > [Malayo-Polynesian](by-family.md#austronesian--malayo-polynesian) |
| Region | [Papunesia](by-region.md#papunesia) > [Fiji](by-region.md#fiji) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Malayo-Polynesian](https://tigregotico.github.io/orthography2ipa/#x-clade-mala1545) `x-clade-mala1545` |
| Explorer | [`fj` in the data explorer](https://tigregotico.github.io/orthography2ipa/#fj) |
| Spec file | [`fj.json`](../../orthography2ipa/data/fj.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Fijian (Na Vosa Vakaviti), Oceanic (Central Pacific) language of Fiji. The Latin orthography devised by David Cargill (1830s) is phonemic but assigns unusual values to several letters: ⟨b d q⟩ are the prenasalised stops /ᵐb ⁿd ᵑɡ/, ⟨g⟩ is /ŋ/, ⟨c⟩ is /ð/ and ⟨v⟩ is /β/. /p/ and /f/ occur only in loanwords.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1985 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 22 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/fj.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `fj` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-fijian_language_wiki"></a>Wikipedia contributors (2026). *Fijian language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Fijian_language)
2. <a id="src-schutz1985"></a>Schütz, Albert J. (1985). *The Fijian Language*. University of Hawai'i Press (open access edition). Cited: 31-32, 647. [hdl.handle.net](http://hdl.handle.net/10125/62912)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 22 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p |  |  | t ⁿd |  | k |
| Nasal | m |  |  | n |  | ŋ |
| Trill |  |  |  | r |  |  |
| Fricative | β | f | ð | s |  |  |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  |  | l |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [w] [ᵐb] [ᵑɡ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [ᵐb] |  |
| ⟨c⟩ | [ð] |  |
| ⟨d⟩ | [ⁿd] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ŋ] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [ᵑɡ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [β] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "fj")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Fernando Po Creole English](fpe.md) · [Home](../index.md) · [Finnish →](fi.md)
