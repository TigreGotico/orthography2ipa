# Ainu (`ain`)

<!-- atlas:summary begin -->
Ainu is an Ainu language, written in the Latin script. Glottolog places it in Japan. The `ain` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ain` |
| ISO 639-3 | [ain](https://iso639-3.sil.org/code/ain), Ainu (Japan) |
| Glottolog | [ainu1240](https://glottolog.org/resource/languoid/id/ainu1240), Hokkaido Ainu |
| Wikidata | [Q27969](https://www.wikidata.org/wiki/Q27969) |
| Wikipedia | [Ainu language](https://en.wikipedia.org/wiki/Ainu_language) |
| Family | [Ainu](by-family.md#ainu) |
| Region | [Eurasia](by-region.md#eurasia) > [Japan](by-region.md#japan) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Ainu](https://tigregotico.github.io/orthography2ipa/#x-clade-ainu1252) `x-clade-ainu1252` |
| Explorer | [`ain` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ain) |
| Spec file | [`ain.json`](../../orthography2ipa/data/ain.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Ainu (Hokkaido Ainu) is a language isolate, romanized in the Latin orthography standard in modern Ainu-language dictionaries and pedagogy (Tamura 1988, 2000, Refsing 1986).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1986 to 2000. [Sources](#sources) lists them. The spec file writes all 28 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ain.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ain` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-shibatani1990"></a>Shibatani, M. (1990). *The Languages of Japan*. Cambridge University Press.
2. <a id="src-tamura2000"></a>Tamura, Suzuko (2000). *The Ainu Language*. Sanseido.
3. <a id="src-refsing1986"></a>Refsing, Kirsten (1986). *The Ainu Language: The Morphology and Syntax of the Shizunai Dialect*. Aarhus University Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `ain` | gold | lexicon-derived | CC BY 4.0 | 858 | 0.0200 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 26 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pː | d t tː |  | k kː ɡ |  |
| Affricate |  | ts |  |  |  |
| Nasal | m mː | n nː |  |  |  |
| Tap |  | ɾ |  |  |  |
| Fricative |  | s sː |  |  | h |
| Approximant |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [ts] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨kk⟩ | [kː] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [mː] |  |
| ⟨n⟩ | [n] |  |
| ⟨nn⟩ | [nː] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨pp⟩ | [pː] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [s] |  |
| ⟨ss⟩ | [sː] |  |
| ⟨t⟩ | [t] |  |
| ⟨tt⟩ | [tː] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |

Stress falls on the second syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ain")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Afrikaans](af.md) · [Home](../index.md) · [Aja →](ajg-BJ.md)
