# Nanai (`gld`)

<!-- atlas:summary begin -->
Nanai is a Tungusic language, written in the Cyrl script. Glottolog places it in China and Russia. The `gld` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `gld` |
| ISO 639-3 | [gld](https://iso639-3.sil.org/code/gld), Nanai |
| Glottolog | [nana1257](https://glottolog.org/resource/languoid/id/nana1257), Nanai |
| Wikipedia | [Nanai language](https://en.wikipedia.org/wiki/Nanai_language) |
| Family | [Tungusic](by-family.md#tungusic) |
| Region | [Eurasia](by-region.md#eurasia) > [China](by-region.md#china), [Russia](by-region.md#russia) |
| Script | [Cyrl](by-script.md#cyrl) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Tungusic](https://tigregotico.github.io/orthography2ipa/#x-clade-tung1282) `x-clade-tung1282` |
| Explorer | [`gld` in the data explorer](https://tigregotico.github.io/orthography2ipa/#gld) |
| Spec file | [`gld.json`](../../orthography2ipa/data/gld.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Cyrillic literary orthography for Nanai, following Avrorin (1959/1961, Grammatika nanaiskogo yazyka) and the standard Nanai alphabet in use since the 1980s (Stolyarov, ABC-based primers), which extends Russian with Ng (velar nasal) and macron-marked long vowels a-macron/o-macron/e-macron.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1959 to 2024. [Sources](#sources) lists them. The spec file writes all 36 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/gld.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `gld` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-glottolog2024"></a>Hammarström, Harald, Forkel, Robert, Haspelmath, Martin, Bank, Sebastian (2024). *Glottolog 5.0*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/)
2. <a id="src-phoible2019"></a>Moran, Steven, McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0 (doi:10.5281/zenodo.2562766)*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/inventories/view/341)
3. <a id="src-avrorin1959"></a>Avrorin, Valentin A. (1959). *Grammatika nanaiskogo yazyka, vol. 1*. Academy of Sciences, USSR.
4. <a id="src-an1961"></a>An, S. A. (1961). *Nanai orthography and primer materials*. Uchpedgiz.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `gld` | gold | lexicon-derived | CC BY 4.0 | 887 | 0.1532 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 31 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d t |  |  | k ɡ |
| Affricate |  |  | d̠ʒ t̠ʃ |  |  |
| Nasal | m | n |  |  | ŋ |
| Trill |  | r |  |  |  |
| Fricative |  | s |  |  | x |
| Approximant |  |  |  | j |  |
| Lateral approximant |  | l |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u |
| Near-close | ɪ |  |  |
| Close-mid |  |  | oː |
| Mid |  | ə əː |  |
| Open-mid |  |  | ɔ |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ā⟩ | [aː] |  |
| ⟨ē⟩ | [əː] |  |
| ⟨ō⟩ | [oː] |  |
| ⟨а⟩ | [a] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [w] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [je] |  |
| ⟨ж⟩ | [d̠ʒ] |  |
| ⟨з⟩ | [s] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [ɔ] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [x] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [t̠ʃ] |  |
| ⟨ч⟩ | [t̠ʃ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɪ] |  |
| ⟨ь⟩ | ∅ |  |
| ⟨э⟩ | [ə] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨ӈ⟩ | [ŋ] |  |
| ⟨ӣ⟩ | [iː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "gld")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Namuyi](nmy.md) · [Home](../index.md) · [Navajo →](nv.md)
