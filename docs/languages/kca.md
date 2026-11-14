# Khanty (`kca`)

<!-- atlas:summary begin -->
Khanty is an Uralic language, written in the Cyrillic script. Glottolog places it in Russia. The `kca` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kca` |
| ISO 639-3 | [kca](https://iso639-3.sil.org/code/kca), Khanty |
| Glottolog | [khan1273](https://glottolog.org/resource/languoid/id/khan1273), Kazym-Berezover-Suryskarer Khanty |
| Wikipedia | [Khanty language](https://en.wikipedia.org/wiki/Khanty_language) |
| Family | [Uralic](by-family.md#uralic) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Uralic](https://tigregotico.github.io/orthography2ipa/#x-clade-ural1272) `x-clade-ural1272` |
| Explorer | [`kca` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kca) |
| Spec file | [`kca.json`](../../orthography2ipa/data/kca.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Northern Khanty, Kazym dialect (standard literary Khanty), Ob-Ugric branch, Khanty-Mansi Autonomous Okrug, Russia. INPUT CONTRACT: modern Kazym Khanty Cyrillic orthography, NFC (⟨Ӓӓ Ӧӧ Ӱӱ Ӈӈ⟩ are precomposed characters, ⟨ӆ⟩ is the lateral fricative letter, distinct from plain ⟨л⟩).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1999 to 2024. [Sources](#sources) lists them. The spec file writes all 50 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kca.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kca` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-nikolaeva1999"></a>Nikolaeva, Irina (1999). *Ostyak*. Languages of the World/Materials 305, LINCOM Europa. [lincom-shop.eu](https://www.lincom-shop.eu/)
2. <a id="src-glottolog2024"></a>Hammarström, Harald, Forkel, Robert, Haspelmath, Martin, Bank, Sebastian (2024). *Glottolog 5.0*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/)
3. <a id="src-phoible2019"></a>Moran, Steven, McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0 (doi:10.5281/zenodo.2562766)*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/inventories/view/184)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `kca` | gold | lexicon-derived | CC BY 4.0 | 863 | 0.0232 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 74 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t tʰ |  | ʈ | c | k kʰ k̟ʰ |  |
| Affricate |  |  | ts | t̠ʃ | ʈʂ |  |  |  |
| Nasal | m m̥ |  | n n̥ |  | ɳ ɳ̥ | ɲ ɲ̥ | ŋ ŋ̟ ŋ̥ |  |
| Trill |  |  | r r̥ |  |  |  |  |  |
| Fricative |  | f | s z | ʃ ʒ |  | ɕ | x ɣ ɣ̟ | χ |
| Lateral fricative |  |  | ɬ |  |  |  |  |  |
| Approximant |  |  |  |  |  | j j̥ |  |  |
| Lateral approximant |  |  | l l̥ l̥ʲ |  | ɭ ɭ̥ | ʎ |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ʉ | u |
| Near-close | ɪ |  |  |
| Close-mid | e̞ | ɵ̞ | o̞ |
| Mid |  | ə ə̆ |  |
| Near-open | æ |  |  |
| Open | a |  | ɒ̆ |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [w] [ɲa] [ɲe] [ɲi] [ɲo] [ɲu] [ʍ] [ʎa] [ʎe] [ʎi] [ʎo] [ʎu] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [w] |  |
| ⟨г⟩ | [ɣ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [je] [e̞] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨ле⟩ | [ʎe] |  |
| ⟨ли⟩ | [ʎi] |  |
| ⟨ль⟩ | [ʎ] |  |
| ⟨лю⟩ | [ʎu] |  |
| ⟨ля⟩ | [ʎa] |  |
| ⟨лё⟩ | [ʎo] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨не⟩ | [ɲe] |  |
| ⟨ни⟩ | [ɲi] |  |
| ⟨нь⟩ | [ɲ] |  |
| ⟨ню⟩ | [ɲu] |  |
| ⟨ня⟩ | [ɲa] |  |
| ⟨нё⟩ | [ɲo] |  |
| ⟨о⟩ | [o̞] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [χ] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [c] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɪ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [ə] |  |
| ⟨ю⟩ | [ju] [u] |  |
| ⟨я⟩ | [ja] [a] |  |
| ⟨ё⟩ | [jo] [o̞] |  |
| ⟨ӆ⟩ | [ɬ] |  |
| ⟨ӈ⟩ | [ŋ] |  |
| ⟨ӓ⟩ | [æ] |  |
| ⟨ӧ⟩ | [ɵ̞] |  |
| ⟨ӱ⟩ | [ʉ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kca")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Khalaj](klj.md) · [Home](../index.md) · [Khasi →](kha.md)
