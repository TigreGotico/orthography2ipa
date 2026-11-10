# Nenets (`yrk`)

<!-- atlas:summary begin -->
Nenets is an Uralic language, written in the Cyrillic script. Glottolog places it in the Eurasia macroarea. The `yrk` spec is at the research tier. It cites 3 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `yrk` |
| ISO 639-3 | [yrk](https://iso639-3.sil.org/code/yrk), Nenets |
| Wikipedia | [Tundra Nenets language](https://en.wikipedia.org/wiki/Tundra_Nenets_language) |
| Family | [Uralic](by-family.md#uralic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Uralic](https://tigregotico.github.io/orthography2ipa/#x-clade-ural1272) `x-clade-ural1272` |
| Explorer | [`yrk` in the data explorer](https://tigregotico.github.io/orthography2ipa/#yrk) |
| Spec file | [`yrk.json`](../../orthography2ipa/data/yrk.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Tundra Nenets is a Samoyedic language of the Uralic family, written in an extended Russian Cyrillic alphabet (Salminen 1993, 1997). Beyond the base letters the map covers Ӈ (velar nasal) and the two apostrophe letters that write the glottal-stop phonemes.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1997 to 2024. [Sources](#sources) lists them. The spec file writes all 44 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/yrk.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `yrk` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-yrk_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Tundra Nenets (nene1249)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/nene1249)
2. <a id="src-salminen1997"></a>Salminen, Tapani (1997). *Tundra Nenets Inflection (Mémoires de la Société Finno-Ougrienne 227)*. Suomalais-Ugrilainen Seura.
3. <a id="src-salminen2023"></a>Salminen, Tapani (2023). *An introduction to the Nenets languages*. Kone Foundation & Department of Modern Languages, University of Helsinki (lecture course materials). Cited: 23, 25-26, 43. [mv.helsinki.fi](https://www.mv.helsinki.fi/home/tasalmin/INL.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `yrk` | gold | lexicon-derived | CC BY 4.0 | 1016 | 0.1907 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `yrk` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 295 | 0.3500 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 49 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bʲ p pʲ |  | d dʲ t tʲ |  |  | k kʲ ɡ | ʔ |
| Affricate |  |  | ts | tʃ |  |  |  |
| Nasal | m mʲ |  | n nʲ |  |  | ŋ |  |
| Trill |  |  | r rʲ |  |  |  |  |
| Fricative |  | f v vʲ | s sʲ z zʲ | ʃ ʒ | ɕ | x |  |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l lʲ |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid | e eː |  | o |
| Mid |  | ə |  |
| Near-open | æ |  |  |
| Open |  |  | ɑ |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨"⟩ | [ʔ] |  |
| ⟨'⟩ | [ʔ] |  |
| ⟨ʼ⟩ | [ʔ] |  |
| ⟨ˮ⟩ | [ʔ] |  |
| ⟨а⟩ | [ɑ] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [je] | after consonant [e] |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [æ] |  |
| ⟨э̇⟩ | [eː] |  |
| ⟨ю⟩ | [ju] | after consonant [u] |
| ⟨я⟩ | [ja] | after consonant [ɑ] |
| ⟨ё⟩ | [jo] | after consonant [o] |
| ⟨ӈ⟩ | [ŋ] |  |
| ⟨ӑ⟩ | [ə] |  |
| ⟨‘⟩ | [ʔ] |  |
| ⟨’⟩ | [ʔ] |  |
| ⟨“⟩ | [ʔ] |  |
| ⟨”⟩ | [ʔ] |  |

Stress falls on the last syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 12 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `YRK_PAL_B` | /b/ → [bʲ], before a palatal | - | - |
| `YRK_PAL_V` | /v/ → [vʲ], before a palatal | - | - |
| `YRK_PAL_D` | /d/ → [dʲ], before a palatal | - | - |
| `YRK_PAL_Z` | /z/ → [zʲ], before a palatal | - | - |
| `YRK_PAL_K` | /k/ → [kʲ], before a palatal | - | - |
| `YRK_PAL_L` | /l/ → [lʲ], before a palatal | - | - |
| `YRK_PAL_M` | /m/ → [mʲ], before a palatal | - | - |
| `YRK_PAL_N` | /n/ → [nʲ], before a palatal | - | - |
| `YRK_PAL_P` | /p/ → [pʲ], before a palatal | - | - |
| `YRK_PAL_R` | /r/ → [rʲ], before a palatal | - | - |
| `YRK_PAL_S` | /s/ → [sʲ], before a palatal | - | - |
| `YRK_PAL_T` | /t/ → [tʲ], before a palatal | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "yrk")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Neapolitan](nap.md) · [Home](../index.md) · [Nepali →](ne.md)
