# Erzya (`myv`)

<!-- atlas:summary begin -->
Erzya is an Uralic language, written in the Cyrillic script. Glottolog places it in 8 countries. The `myv` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `myv` |
| ISO 639-3 | [myv](https://iso639-3.sil.org/code/myv), Erzya |
| Glottolog | [erzy1239](https://glottolog.org/resource/languoid/id/erzy1239), Erzya |
| Wikidata | [Q29952](https://www.wikidata.org/wiki/Q29952) |
| Wikipedia | [Erzya language](https://en.wikipedia.org/wiki/Erzya_language) |
| Family | [Uralic](by-family.md#uralic) |
| Region | [Eurasia](by-region.md#eurasia) > [Azerbaijan](by-region.md#azerbaijan), [Belarus](by-region.md#belarus), [Estonia](by-region.md#estonia), [Kazakhstan](by-region.md#kazakhstan), [Latvia](by-region.md#latvia), [Lithuania](by-region.md#lithuania), [Russia](by-region.md#russia), [Ukraine](by-region.md#ukraine) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Uralic](https://tigregotico.github.io/orthography2ipa/#x-clade-ural1272) `x-clade-ural1272` |
| Explorer | [`myv` in the data explorer](https://tigregotico.github.io/orthography2ipa/#myv) |
| Spec file | [`myv.json`](../../orthography2ipa/data/myv.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Erzya (эрзянь кель), Mordvinic (Uralic) language of Mordovia. Written in the Russian Cyrillic alphabet.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2022 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 32 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/myv.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `myv` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-erzya_language_wiki"></a>Wikipedia contributors (2026). *Erzya language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Erzya_language)
2. <a id="src-hamari_ajanki2022"></a>Hamari, Arja, Ajanki, Rigina (2022). *Mordvin (Erzya and Moksha). In Bakró-Nagy, Laakso & Skribnik (eds.), The Oxford Guide to the Uralic Languages, 392-431*. Oxford University Press, accepted manuscript in the University of Turku repository (UTUPub). Cited: 393-394. [utupub.fi](https://www.utupub.fi/handle/10024/191945)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `myv` | generated | epitran-derived | CC0 1.0 | 6442 | 0.0944 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 32 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |
| Affricate |  |  | t͡s | t͡ʃ |  |  |
| Nasal | m |  | n |  |  |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z | ʃ ʃː ʒ |  | x |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid | e |  | o |
| Open | a |  |  |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [ʲ].
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
| ⟨е⟩ | [je] |  |
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
| ⟨ц⟩ | [t͡s] |  |
| ⟨ч⟩ | [t͡ʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ʃː] |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ё⟩ | [jo] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "myv")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Eonavian](gl-ES-x-eonavia.md) · [Home](../index.md) · [Esperanto →](eo.md)
