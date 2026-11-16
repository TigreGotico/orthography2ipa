# Võro (`vro`)

<!-- atlas:summary begin -->
Võro is an Uralic language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `vro` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `vro` |
| ISO 639-3 | [vro](https://iso639-3.sil.org/code/vro), Võro |
| Glottolog | [voro1243](https://glottolog.org/resource/languoid/id/voro1243), Võro |
| Wikidata | [Q32762](https://www.wikidata.org/wiki/Q32762) |
| Wikipedia | [Võro language](https://en.wikipedia.org/wiki/V%C3%B5ro_language) |
| Family | [Uralic](by-family.md#uralic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Uralic](https://tigregotico.github.io/orthography2ipa/#x-clade-ural1272) `x-clade-ural1272` |
| Explorer | [`vro` in the data explorer](https://tigregotico.github.io/orthography2ipa/#vro) |
| Spec file | [`vro.json`](../../orthography2ipa/data/vro.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Võro (võro kiil), a South Estonian (Finnic) language of south-eastern Estonia with its own literary standard, regulated by the Võro Institute.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 2007 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 28 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/vro.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `vro` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-võro_language_wiki"></a>Wikipedia contributors (2026). *Võro language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/V%C3%B5ro_language)
2. <a id="src-iva2007"></a>Iva, Sulev (2007). *Võru kirjakeele sõnamuutmissüsteem [Inflectional morphology of the Võro literary language]*. University of Tartu PhD dissertation, Dissertationes Philologiae Estonicae Universitatis Tartuensis 20. Cited: 233-236. [dspace.ut.ee](https://dspace.ut.ee/handle/10062/4860)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 28 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | ʔ |
| Nasal | m |  | n |  |  |  |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u |
| Close-mid | e ø | o ɤ |
| Near-open | æ |  |
| Open |  | ɑ |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [ʔ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨z⟩ | [z] |  |
| ⟨ä⟩ | [æ] |  |
| ⟨õ⟩ | [ɤ] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨ü⟩ | [y] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ž⟩ | [ʒ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "vro")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Votic](vot.md) · [Home](../index.md) · [Waigali →](wbk.md)
