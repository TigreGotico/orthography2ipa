# Itelmen (`itl`)

<!-- atlas:summary begin -->
Itelmen is a Chukotko-Kamchatkan language, written in the Cyrl script. Glottolog places it in Russia. The `itl` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `itl` |
| ISO 639-3 | [itl](https://iso639-3.sil.org/code/itl), Itelmen |
| Glottolog | [itel1242](https://glottolog.org/resource/languoid/id/itel1242), West Itelmen |
| Wikipedia | [Itelmen language](https://en.wikipedia.org/wiki/Itelmen_language) |
| Family | [Chukotko-Kamchatkan](by-family.md#chukotko-kamchatkan) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia) |
| Script | [Cyrl](by-script.md#cyrl) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Chukotko-Kamchatkan](https://tigregotico.github.io/orthography2ipa/#x-clade-chuk1271) `x-clade-chuk1271` |
| Explorer | [`itl` in the data explorer](https://tigregotico.github.io/orthography2ipa/#itl) |
| Spec file | [`itl.json`](../../orthography2ipa/data/itl.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Cyrillic literary orthography for (West) Itelmen described in Georg & Volodin (1999), Die itelmenische Sprache: Grammatik und Texte.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1999 to 2024. [Sources](#sources) lists them. The spec file writes all 41 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/itl.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `itl` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-glottolog2024"></a>Hammarström, Harald, Forkel, Robert, Haspelmath, Martin, Bank, Sebastian (2024). *Glottolog 5.0*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/)
2. <a id="src-phoible2019"></a>Moran, Steven, McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0 (doi:10.5281/zenodo.2562766)*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/inventories/view/2297)
3. <a id="src-georg_volodin1999"></a>Georg, Stefan, Volodin, Alexander P. (1999). *Die itelmenische Sprache: Grammatik und Texte*. Harrassowitz.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `itl` | gold | lexicon-derived | CC BY 4.0 | 603 | 0.0540 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 39 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p | t |  |  | k | q | ʔ |
| Affricate |  | ts | tʃ |  |  |  |  |
| Nasal | m | n nʲ |  |  | ŋ |  |  |
| Trill |  | r |  |  |  |  |  |
| Fricative | ɸ β | s z | ʃ ʒ | ɕ | x ɣ | χ |  |
| Lateral fricative |  | ɬ |  |  |  |  |  |
| Approximant |  |  |  | j |  |  |  |
| Lateral approximant |  | l lʲ |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [ja] [jo] [ju] [kʔ] [pʔ] [tʃʔ] [tʔ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨в⟩ | [β] |  |
| ⟨е⟩ | [e] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨к’⟩ | [kʔ] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨п’⟩ | [pʔ] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨т’⟩ | [tʔ] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [ɸ] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ч’⟩ | [tʃʔ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ь⟩ | ∅ |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨љ⟩ | [lʲ] |  |
| ⟨њ⟩ | [nʲ] |  |
| ⟨ҳ⟩ | [χ] |  |
| ⟨ӄ⟩ | [q] |  |
| ⟨ӆ⟩ | [ɬ] |  |
| ⟨ӈ⟩ | [ŋ] |  |
| ⟨ә⟩ | [ə] |  |
| ⟨ӷ⟩ | [ɣ] |  |
| ⟨’⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "itl")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Italian](it-IT.md) · [Home](../index.md) · [Iñupiaq →](ik.md)
