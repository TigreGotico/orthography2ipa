# Northern Sotho (Sepedi) (`nso`)

<!-- atlas:summary begin -->
Northern Sotho (Sepedi) is a Bantu language, written in the Latin script. Glottolog places it in Botswana and South Africa. The `nso` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `nso` |
| ISO 639-3 | [nso](https://iso639-3.sil.org/code/nso), Pedi |
| Glottolog | [pedi1238](https://glottolog.org/resource/languoid/id/pedi1238), Pedi |
| Wikidata | [Q33890](https://www.wikidata.org/wiki/Q33890) |
| Wikipedia | [Northern Sotho](https://en.wikipedia.org/wiki/Northern_Sotho) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) > [Bantu](by-family.md#atlantic-congo--bantu) |
| Region | [Africa](by-region.md#africa) > [Botswana](by-region.md#botswana), [South Africa](by-region.md#south-africa) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1900, living |
| Parent | [Proto-Bantu (family node)](https://tigregotico.github.io/orthography2ipa/#bnt) `bnt` |
| Explorer | [`nso` in the data explorer](https://tigregotico.github.io/orthography2ipa/#nso) |
| Spec file | [`nso.json`](../../orthography2ipa/data/nso.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Northern Sotho / Sepedi (Bantu S32), Latin orthography. Seven written vowels: a e ê i o ô u (/a e ɛ i o ɔ u/, the circumflexes are frequently omitted in everyday text, which makes ⟨e⟩ and ⟨o⟩ ambiguous between the close-mid and open-mid values).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1969 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 38 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/nso.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `nso` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-nso_wiki"></a>Wikipedia contributors (2024). *Northern Sotho*. Wikipedia. Cited: Seven-vowel system /i e ɛ a ɔ o u/, consonant inventory (ejective vs aspirated series, ɬ, kx), and the Latin orthography (š = [ʃ], tš, kg, hl). [en.wikipedia.org](https://en.wikipedia.org/wiki/Northern_Sotho)
2. <a id="src-ziervogel1969"></a>Ziervogel, D. & Mokgokong, P. C. (1969). *Groot Noord-Sotho-woordeboek / Comprehensive Northern Sotho Dictionary*. Van Schaik.
3. <a id="src-panSALB_nso"></a>Pan South African Language Board (2008). *Sesotho sa Leboa Orthography and Spelling Rules*. PanSALB.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 41 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  |  | k kʰ |  |
| Affricate |  |  | ts tsʰ tɬʰ | dʒ tʃ tʃʰ |  | kx |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative | β | f | s | ʃ |  | x | h ɦ |
| Lateral fricative |  |  | ɬ |  |  |  |  |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [pʃ] [tl] [w] [ɺ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [x] |  |
| ⟨h⟩ | [h] |  |
| ⟨hl⟩ | [ɬ] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kg⟩ | [kx] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨psh⟩ | [pʃ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨tl⟩ | [tl] |  |
| ⟨tlh⟩ | [tɬʰ] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨tsh⟩ | [tsʰ] |  |
| ⟨tš⟩ | [tʃ] |  |
| ⟨tšh⟩ | [tʃʰ] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ê⟩ | [ɛ] |  |
| ⟨ô⟩ | [ɔ] |  |
| ⟨š⟩ | [ʃ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "nso")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Northern Sami](se.md) · [Home](../index.md) · [Northern Tiwa →](twf.md)
