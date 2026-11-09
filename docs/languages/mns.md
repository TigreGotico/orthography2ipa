# Mansi (`mns`)

<!-- atlas:summary begin -->
Mansi is an Uralic language, written in the Cyrillic script. Glottolog places it in Russia. The `mns` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mns` |
| ISO 639-3 | [mns](https://iso639-3.sil.org/code/mns), Mansi |
| Glottolog | [mans1258](https://glottolog.org/resource/languoid/id/mans1258), Northern Mansi |
| Wikipedia | [Mansi language](https://en.wikipedia.org/wiki/Mansi_language) |
| Family | [Uralic](by-family.md#uralic) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Uralic](https://tigregotico.github.io/orthography2ipa/#x-clade-ural1272) `x-clade-ural1272` |
| Explorer | [`mns` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mns) |
| Spec file | [`mns.json`](../../orthography2ipa/data/mns.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Northern (Sosva) Mansi, Ob-Ugric branch, Khanty-Mansi Autonomous Okrug, Russia. INPUT CONTRACT: modern Sosva Mansi Cyrillic orthography, NFC.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2001 to 2024. [Sources](#sources) lists them. The spec file writes all 64 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mns.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mns` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-riese2001"></a>Riese, Timothy (2001). *Vogul*. Languages of the World/Materials 158, LINCOM Europa. [lincom-shop.eu](https://www.lincom-shop.eu/)
2. <a id="src-glottolog2024"></a>Hammarström, Harald, Forkel, Robert, Haspelmath, Martin, Bank, Sebastian (2024). *Glottolog 5.0*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/)
3. <a id="src-phoible2019"></a>Moran, Steven, McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0 (doi:10.5281/zenodo.2562766)*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/inventories/view/2475)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `mns` | gold | lexicon-derived | CC BY 4.0 | 992 | 0.1024 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 63 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t̪ t̪ʲ |  |  | k kʷ |  |
| Affricate |  |  | ts |  | tɕ |  |  |
| Nasal | m |  | n̪ |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f | sʲ s̪ z | ʃ ʒ | ɕ | ɣ | χ χʷ |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l̪ |  | ʎ |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Near-close | ɪ |  |  |
| Close-mid | e |  | o ɤː |
| Mid |  | ə |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [oɔ] [sʲa] [sʲe] [sʲi] [sʲu] [t̪ʲa] [t̪ʲe] [t̪ʲi] [t̪ʲu] [w] [ɲa] [ɲe] [ɲi] [ɲo] [ɲu] [ʎa] [ʎe] [ʎi] [ʎo] [ʎu] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨а̄⟩ | [aː] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [w] |  |
| ⟨г⟩ | [ɣ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [je] [e] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨кв⟩ | [kʷ] |  |
| ⟨л⟩ | [l̪] |  |
| ⟨ле⟩ | [ʎe] |  |
| ⟨ли⟩ | [ʎi] |  |
| ⟨ль⟩ | [ʎ] |  |
| ⟨лю⟩ | [ʎu] |  |
| ⟨ля⟩ | [ʎa] |  |
| ⟨лё⟩ | [ʎo] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n̪] |  |
| ⟨не⟩ | [ɲe] |  |
| ⟨ни⟩ | [ɲi] |  |
| ⟨нь⟩ | [ɲ] |  |
| ⟨ню⟩ | [ɲu] |  |
| ⟨ня⟩ | [ɲa] |  |
| ⟨нё⟩ | [ɲo] |  |
| ⟨о⟩ | [o] |  |
| ⟨о̄⟩ | [oɔ] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s̪] |  |
| ⟨се⟩ | [sʲe] |  |
| ⟨си⟩ | [sʲi] |  |
| ⟨сь⟩ | [sʲ] |  |
| ⟨сю⟩ | [sʲu] |  |
| ⟨ся⟩ | [sʲa] |  |
| ⟨т⟩ | [t̪] |  |
| ⟨те⟩ | [t̪ʲe] |  |
| ⟨ти⟩ | [t̪ʲi] |  |
| ⟨ть⟩ | [t̪ʲ] |  |
| ⟨тю⟩ | [t̪ʲu] |  |
| ⟨тя⟩ | [t̪ʲa] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [χ] |  |
| ⟨хв⟩ | [χʷ] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tɕ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɪ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [e] |  |
| ⟨э̄⟩ | [ɤː] |  |
| ⟨ю⟩ | [ju] [u] |  |
| ⟨я⟩ | [ja] [a] |  |
| ⟨ё⟩ | [jo] [o] |  |
| ⟨ӈ⟩ | [ŋ] |  |
| ⟨ӣ⟩ | [iː] |  |
| ⟨ӧ⟩ | [ə] |  |
| ⟨ӯ⟩ | [uː] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mns")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Mandinka](mnk.md) · [Home](../index.md) · [Manx →](gv.md)
