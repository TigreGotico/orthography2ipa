# Meitei (`mni`)

<!-- atlas:summary begin -->
Meitei is a Sino-Tibetan language, written in the Latin script. Glottolog places it in Bangladesh, India and Myanmar (Burma). The `mni` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mni` |
| ISO 639-3 | [mni](https://iso639-3.sil.org/code/mni), Manipuri |
| Glottolog | [mani1292](https://glottolog.org/resource/languoid/id/mani1292), Manipuri |
| Wikidata | [Q33868](https://www.wikidata.org/wiki/Q33868) |
| Wikipedia | [Meitei language](https://en.wikipedia.org/wiki/Meitei_language) |
| Family | [Sino-Tibetan](by-family.md#sino-tibetan) |
| Region | [Eurasia](by-region.md#eurasia) > [Bangladesh](by-region.md#bangladesh), [India](by-region.md#india), [Myanmar (Burma)](by-region.md#myanmar-burma) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Ancestor | [Proto-Kuki-Chin (reconstructed)](https://tigregotico.github.io/orthography2ipa/#mni-x-proto-kuki-chin) `mni-x-proto-kuki-chin` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`mni` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mni) |
| Spec file | [`mni.json`](../../orthography2ipa/data/mni.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Meitei/Manipuri (Manipur, India). Tibeto-Burman, Kuki-Chin, Naga area, Meiteic is a sister branch of Kuki-Chin proper, not a daughter (VanBik 2009, Glottolog). Phonemic tone (falling vs. non-falling in stressed syllable). Meitei Mayek script (traditional, restored 2013 as official).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1996 to 2005. [Sources](#sources) lists them. The spec file writes all 34 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mni.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `mni` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Meitei/Manipuri (Meetei Mayek script)](https://tigregotico.github.io/orthography2ipa/#mni-Mtei) `mni-Mtei`: Bangladesh, India, Myanmar (Burma), skeleton tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-chelliah1997"></a>Chelliah, S.L. (1997). *A Grammar of Meithei*. Mouton de Gruyter.
2. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
3. <a id="src-gordon2005"></a>Gordon, R.G. (ed.) (2005). *Ethnologue: Languages of the World (15th ed.)*. SIL International.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 34 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ | d t tʰ |  |  | k kʰ ɡ | ʔ |
| Affricate |  |  | dʒ tʃ tʃʰ |  |  |  |
| Nasal | m | n |  |  | ŋ |  |
| Trill |  | r |  |  |  |  |
| Fricative |  | s z |  |  |  | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Close-mid | e eː |  | o oː |
| Mid |  | ə |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [w].

Tones: [falling] falling tone, [level] level tone.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aː⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [tʃ] |  |
| ⟨ch⟩ | [tʃʰ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨eː⟩ | [eː] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨iː⟩ | [iː] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨oː⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨u⟩ | [u] |  |
| ⟨uː⟩ | [uː] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ŋ⟩ | [ŋ] |  |
| ⟨ə⟩ | [ə] |  |
| ⟨ʔ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mni")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Marshallese](mh.md) · [Home](../index.md) · [Mende →](men.md)
