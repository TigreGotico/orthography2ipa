# Central Siberian Yupik (`ess`)

<!-- atlas:summary begin -->
Central Siberian Yupik is an Eskimo-Aleut language, written in the Cyrl script. Glottolog places it in Russia and United States. The `ess` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ess` |
| ISO 639-3 | [ess](https://iso639-3.sil.org/code/ess), Central Siberian Yupik |
| Glottolog | [cent2128](https://glottolog.org/resource/languoid/id/cent2128), Central Siberian Yupik |
| Wikipedia | [Central Siberian Yupik language](https://en.wikipedia.org/wiki/Central_Siberian_Yupik_language) |
| Family | [Eskimo-Aleut](by-family.md#eskimo-aleut) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia), [United States](by-region.md#united-states) |
| Script | [Cyrl](by-script.md#cyrl) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Eskimo-Aleut](https://tigregotico.github.io/orthography2ipa/#x-clade-eski1264) `x-clade-eski1264` |
| Explorer | [`ess` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ess) |
| Spec file | [`ess.json`](../../orthography2ipa/data/ess.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Cyrillic literary orthography for Central Siberian (Chaplino/Naukan-area) Yupik, following de Reuse (1994), Siberian Yupik Eskimo: The Language and Its Contacts with Chukchi, and the Soviet-era practical alphabet used in Chaplino/Sireniki-area primers (extends Russian with eng /ŋ/ and gamma /ɣ/).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1994 to 2024. [Sources](#sources) lists them. The spec file writes all 29 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ess.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ess` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-glottolog2024"></a>Hammarström, Harald, Forkel, Robert, Haspelmath, Martin, Bank, Sebastian (2024). *Glottolog 5.0*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/)
2. <a id="src-phoible2019"></a>Moran, Steven, McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0 (doi:10.5281/zenodo.2562766)*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/inventories/view/319)
3. <a id="src-dereuse1994"></a>de Reuse, Willem J. (1994). *Siberian Yupik Eskimo: The Language and Its Contacts with Chukchi*. University of Utah Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `ess` | gold | lexicon-derived | CC BY 4.0 | 814 | 0.1074 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 28 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p |  | t |  | k kʷ | q | ʔ |
| Affricate |  |  | tɬ |  |  |  |  |
| Nasal | m |  | n |  | ŋ ŋʷ |  |  |
| Fricative |  | f v | s z |  | x xʷ ɣ ɣʷ |  |  |
| Approximant |  |  | ɹ | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Open | a |  |  |

Sequences that the spec writes as one unit: [ja] [ju].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɣ] |  |
| ⟨гу⟩ | [ɣʷ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨ку⟩ | [kʷ] |  |
| ⟨л⟩ | [l] |  |
| ⟨лъ⟩ | [tɬ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [ɹ] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ху⟩ | [xʷ] |  |
| ⟨ъ⟩ | [ʔ] |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ӄ⟩ | [q] |  |
| ⟨ӈ⟩ | [ŋ] |  |
| ⟨ӈу⟩ | [ŋʷ] |  |
| ⟨ӷ⟩ | [ɣ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ess")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Central Nahuatl](nhn.md) · [Home](../index.md) · [Chadian Arabic →](shu-TD.md)
