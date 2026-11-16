# Ket (`ket`)

<!-- atlas:summary begin -->
Ket is a Yeniseian language, written in the Cyrl script. Glottolog places it in Russia. The `ket` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ket` |
| ISO 639-3 | [ket](https://iso639-3.sil.org/code/ket), Ket |
| Glottolog | [kett1243](https://glottolog.org/resource/languoid/id/kett1243), Ket |
| Wikipedia | [Ket language](https://en.wikipedia.org/wiki/Ket_language) |
| Family | [Yeniseian](by-family.md#yeniseian) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia) |
| Script | [Cyrl](by-script.md#cyrl) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Yeniseian](https://tigregotico.github.io/orthography2ipa/#x-clade-yeni1252) `x-clade-yeni1252` |
| Explorer | [`ket` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ket) |
| Spec file | [`ket.json`](../../orthography2ipa/data/ket.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Cyrillic-based practical orthography for Ket following Vajda (2004), Ket, and Vajda & Zinn's teaching materials. The northeuralex gold's apostrophe marking laryngealized tone (Vajda, E. J.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 2004 to 2024. [Sources](#sources) lists them. The spec file writes all 45 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ket.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ket` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 3 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-glottolog2024"></a>Hammarström, Harald, Forkel, Robert, Haspelmath, Martin, Bank, Sebastian (2024). *Glottolog 5.0*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/)
2. <a id="src-phoible2019"></a>Moran, Steven, McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0 (doi:10.5281/zenodo.2562766)*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/inventories/view/2)
3. <a id="src-vajda2004"></a>Vajda, Edward J. (2004). *Ket*. Lincom Europa (Languages of the World/Materials 204).
4. <a id="src-vajda2010"></a>Vajda, Edward J. (2010). *Metathesis and Reanalysis in Ket*. Proceedings of the 36th Annual Meeting of the Berkeley Linguistics Society (BLS 36), pp. 457-471. [doi.org](https://doi.org/10.3765/bls.v36i1.3930)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `ket` | gold | lexicon-derived | CC BY 4.0 | 793 | 0.2688 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 75 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʲ |  | d t tʲ |  | c ɟ | k k̟ ɡ ɡ̟ | q ɢ | ʔ |
| Affricate |  |  |  | tʃ t̠ʃʲ |  |  |  |  |
| Nasal | m m̥ |  | n nʲ n̥ n̥ʲ |  | ɲ | ŋ ŋ̥ |  |  |
| Trill |  |  | r |  |  |  | ʀ |  |
| Fricative | β | v | s sʲ | ʃʲ | ɕ ʝ | x ɣ | ʁ χ | h |
| Lateral approximant |  |  | l lʲ lˠ l̥ʲ l̥ˠ |  | ʎ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː | ɨ ɨː | uː |
| Near-close | ɪ |  | ʊ |
| Close-mid | e ø | ɵ̞ ɵ̞ː | o |
| Mid |  | ə |  |
| Open-mid | ɛ ɛː |  | ɔ ɔː |
| Near-open | æ æː |  |  |
| Open | a aː a̟ a̟ː |  |  |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [qχ] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ʼ⟩ | [ʔ] |  |
| ⟨а⟩ | [a] |  |
| ⟨аа⟩ | [aː] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨дь⟩ | [ɟ] |  |
| ⟨е⟩ | [je] |  |
| ⟨и⟩ | [i] |  |
| ⟨ии⟩ | [iː] |  |
| ⟨й⟩ | [ʝ] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨ль⟩ | [ʎ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨нь⟩ | [ɲ] |  |
| ⟨о⟩ | [ɔ] |  |
| ⟨оо⟩ | [ɔː] |  |
| ⟨с⟩ | [s] |  |
| ⟨сь⟩ | [ɕ] |  |
| ⟨т⟩ | [t] |  |
| ⟨ть⟩ | [c] |  |
| ⟨у⟩ | [ʊ] |  |
| ⟨уу⟩ | [uː] |  |
| ⟨х⟩ | [x] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ыы⟩ | [ɨː] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [ɛ] |  |
| ⟨ээ⟩ | [ɛː] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨һ⟩ | [h] |  |
| ⟨ӄ⟩ | [q] |  |
| ⟨ӈ⟩ | [ŋ] |  |
| ⟨ә⟩ | [ə] |  |
| ⟨ө⟩ | [ɵ̞] |  |
| ⟨өө⟩ | [ɵ̞ː] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ket")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kazakh](kk.md) · [Home](../index.md) · [Khakas →](kjh.md)
