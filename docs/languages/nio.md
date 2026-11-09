# Nganasan (`nio`)

<!-- atlas:summary begin -->
Nganasan is an Uralic language, written in the Cyrillic script. Glottolog places it in Russia. The `nio` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `nio` |
| ISO 639-3 | [nio](https://iso639-3.sil.org/code/nio), Nganasan |
| Glottolog | [ngan1291](https://glottolog.org/resource/languoid/id/ngan1291), Nganasan |
| Wikipedia | [Nganasan language](https://en.wikipedia.org/wiki/Nganasan_language) |
| Family | [Uralic](by-family.md#uralic) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Uralic](https://tigregotico.github.io/orthography2ipa/#x-clade-ural1272) `x-clade-ural1272` |
| Explorer | [`nio` in the data explorer](https://tigregotico.github.io/orthography2ipa/#nio) |
| Spec file | [`nio.json`](../../orthography2ipa/data/nio.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Nganasan (ня’ануасана баа), Samoyedic branch, Taymyr Peninsula, Russia. INPUT CONTRACT: Nganasan Cyrillic orthography (1990s standardisation, Wagner-Nagy 2018), NFC.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2018 to 2024. [Sources](#sources) lists them. The spec file writes all 55 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/nio.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `nio` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-wagnernagy2018"></a>Wagner-Nagy, Beáta (2018). *A Grammar of Nganasan*. Studies in Diversity Linguistics 111, Language Science Press. [langsci-press.org](https://langsci-press.org/catalog/book/119)
2. <a id="src-glottolog2024"></a>Hammarström, Harald, Forkel, Robert, Haspelmath, Martin, Bank, Sebastian (2024). *Glottolog 5.0*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/)
3. <a id="src-phoible2019"></a>Moran, Steven, McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0 (doi:10.5281/zenodo.2562766)*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/inventories/view/494)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `nio` | gold | lexicon-derived | CC BY 4.0 | 1024 | 0.0972 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 54 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  | c ɟ | k ɡ | ʔ |
| Affricate |  |  |  | ts |  |  | kx |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |
| Trill |  |  |  | r |  |  |  |  |
| Fricative |  | f v | ð | s sʲ z | ʃ ʒ | ɕ | x |  |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  | ʎ |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i y | ɨ | u |
| Close-mid | e̞ |  | o̞ |
| Mid |  | ə |  |
| Near-open |  | ɐ |  |

Sequences that the spec writes as one unit: [dʲe] [dʲi] [dʲu] [dʲɐ] [ja] [je] [jo] [ju] [sʲa] [sʲe] [sʲi] [sʲu] [ɲe] [ɲi] [ɲu] [ɲɐ] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ˮ⟩ | [ʔ] |  |
| ⟨а⟩ | [ɐ] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨де⟩ | [dʲe] |  |
| ⟨ди⟩ | [dʲi] |  |
| ⟨дь⟩ | [ɟ] |  |
| ⟨дю⟩ | [dʲu] |  |
| ⟨дя⟩ | [dʲɐ] |  |
| ⟨е⟩ | [je] [e̞] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨з̌⟩ | [ð] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨кх⟩ | [kx] |  |
| ⟨л⟩ | [l] |  |
| ⟨ль⟩ | [ʎ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨не⟩ | [ɲe] |  |
| ⟨ни⟩ | [ɲi] |  |
| ⟨нь⟩ | [ɲ] |  |
| ⟨ню⟩ | [ɲu] |  |
| ⟨ня⟩ | [ɲɐ] |  |
| ⟨о⟩ | [o̞] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨се⟩ | [sʲe] |  |
| ⟨си⟩ | [sʲi] |  |
| ⟨сь⟩ | [sʲ] |  |
| ⟨сю⟩ | [sʲu] |  |
| ⟨ся⟩ | [sʲa] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [c] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [e̞] |  |
| ⟨ю⟩ | [ju] [u] |  |
| ⟨я⟩ | [ja] [ɐ] |  |
| ⟨ё⟩ | [jo] [o̞] |  |
| ⟨ү⟩ | [y] |  |
| ⟨ӈ⟩ | [ŋ] |  |
| ⟨ә⟩ | [ə] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "nio")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Newar](new.md) · [Home](../index.md) · [Nheengatu →](yrl.md)
