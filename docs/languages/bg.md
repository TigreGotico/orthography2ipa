# Bulgarian (`bg`)

<!-- atlas:summary begin -->
Bulgarian is a South Slavic language, written in the Cyrillic script. Glottolog places it in 8 countries. The `bg` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `bg` |
| ISO 639-3 | [bul](https://iso639-3.sil.org/code/bul), Bulgarian |
| Glottolog | [bulg1262](https://glottolog.org/resource/languoid/id/bulg1262), Bulgarian |
| Wikidata | [Q7918](https://www.wikidata.org/wiki/Q7918) |
| Wikipedia | [Bulgarian language](https://en.wikipedia.org/wiki/Bulgarian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic > South Slavic](by-family.md#indo-european--balto-slavic--slavic--south-slavic) |
| Region | [Eurasia](by-region.md#eurasia) > [Bulgaria](by-region.md#bulgaria), [Greece](by-region.md#greece), [Moldova](by-region.md#moldova), [North Macedonia](by-region.md#north-macedonia), [Romania](by-region.md#romania), [Serbia](by-region.md#serbia), [Türkiye](by-region.md#türkiye), [Ukraine](by-region.md#ukraine) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1200, living |
| Parent | [South Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-sout3147) `x-clade-sout3147` |
| Explorer | [`bg` in the data explorer](https://tigregotico.github.io/orthography2ipa/#bg) |
| Spec file | [`bg.json`](../../orthography2ipa/data/bg.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Bulgarian. Analytic Slavic language (lost case system). ⟨ъ⟩ represents the unique phoneme /ɤ/ (back unrounded mid vowel). ⟨щ⟩ = [ʃt] (South Slavic, contrasting with East Slavic [ɕː]). Soft consonants occur mainly before /ɛ/ and /i/. Definite article is a suffix, not a separate word.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1993 to 2011. [Sources](#sources) lists them. The spec file writes all 37 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/bg.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `bg` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-comrie_corbett1993"></a>Comrie, B. & Corbett, G. (eds.) (1993). *The Slavonic Languages*. Routledge.
2. <a id="src-leafgren2011"></a>Leafgren, J. (2011). *A Concise Bulgarian Grammar*. University of Wisconsin.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `bg` | generated | epitran-derived | CC0 1.0 | 18447 | 0.1980 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 40 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d dʲ t tʲ |  |  | k ɡ |
| Affricate |  |  | dz ts | dʒ tʃ |  |  |
| Nasal | m |  | n nʲ |  |  | ŋ |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s sʲ z zʲ | ʃ ʒ |  | x |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l lʲ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Near-close | ɪ |  |  |
| Close-mid |  |  | ɤ |
| Open-mid | ɛ |  | ɔ |
| Near-open |  | ɐ |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [ja] [ju] [ʃt].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨дж⟩ | [dʒ] |  |
| ⟨дз⟩ | [dz] |  |
| ⟨дь⟩ | [dʲ] |  |
| ⟨е⟩ | [ɛ] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨зь⟩ | [zʲ] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨ль⟩ | [lʲ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨нь⟩ | [nʲ] |  |
| ⟨о⟩ | [ɔ] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨сь⟩ | [sʲ] |  |
| ⟨т⟩ | [t] |  |
| ⟨ть⟩ | [tʲ] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ʃt] |  |
| ⟨ъ⟩ | [ɤ] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "bg")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Brunei](kxd.md) · [Home](../index.md) · [Buriat →](bua.md)
