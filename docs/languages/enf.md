# Forest Enets (`enf`)

<!-- atlas:summary begin -->
Forest Enets is an Uralic language, written in the Cyrillic script. Glottolog places it in Russia. The `enf` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `enf` |
| ISO 639-3 | [enf](https://iso639-3.sil.org/code/enf), Forest Enets |
| Glottolog | [fore1265](https://glottolog.org/resource/languoid/id/fore1265), Forest Enets |
| Wikipedia | [Enets language](https://en.wikipedia.org/wiki/Enets_language) |
| Family | [Uralic](by-family.md#uralic) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Uralic](https://tigregotico.github.io/orthography2ipa/#x-clade-ural1272) `x-clade-ural1272` |
| Explorer | [`enf` in the data explorer](https://tigregotico.github.io/orthography2ipa/#enf) |
| Spec file | [`enf.json`](../../orthography2ipa/data/enf.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Forest Enets (пэ бай эннэчэ), Samoyedic branch, Krasnoyarsk Krai (Taymyr), Russia, a severely endangered, weakly standardised language: the orthography follows the practical Cyrillic conventions used in Sorokina & Bolina's dictionaries and Siegl (2013)'s text collection, not a fixed school-taught norm.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2013 to 2024. [Sources](#sources) lists them. The spec file writes all 57 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/enf.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `enf` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-siegl2013"></a>Siegl, Florian (2013). *Materials on Forest Enets, an Indigenous Language of Northern Siberia*. Uralica Helsingiensia 5, University of Helsinki. [mv.helsinki.fi](https://www.mv.helsinki.fi/home/jjanhune/uralica.htm)
2. <a id="src-glottolog2024"></a>Hammarström, Harald, Forkel, Robert, Haspelmath, Martin, Bank, Sebastian (2024). *Glottolog 5.0*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/)
3. <a id="src-phoible2019"></a>Moran, Steven, McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0 (doi:10.5281/zenodo.2562766)*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/inventories/view/2469)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `enf` | gold | lexicon-derived | CC BY 4.0 | 838 | 0.0892 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 55 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d dʲ t tʲ |  |  | k ɡ |  |
| Affricate |  |  | ts |  | tɕ |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f | s sʲ z | ʃ ʒ | ɕ |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  | ʎ |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Open-mid | ɛ |  | ɔ |
| Near-open | æ |  |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [dʲe] [dʲi] [ja] [ju] [jɔ] [jɛ] [sʲa] [sʲe] [sʲi] [sʲu] [tʲe] [tʲi] [w] [ɲa] [ɲi] [ɲu] [ɲɛ] [ʎa] [ʎe] [ʎi] [ʎu] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [w] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨де⟩ | [dʲe] |  |
| ⟨ди⟩ | [dʲi] |  |
| ⟨дь⟩ | [dʲ] |  |
| ⟨е⟩ | [jɛ] [ɛ] |  |
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
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨не⟩ | [ɲɛ] |  |
| ⟨ни⟩ | [ɲi] |  |
| ⟨нь⟩ | [ɲ] |  |
| ⟨ню⟩ | [ɲu] |  |
| ⟨ня⟩ | [ɲa] |  |
| ⟨о⟩ | [ɔ] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨се⟩ | [sʲe] |  |
| ⟨си⟩ | [sʲi] |  |
| ⟨сь⟩ | [sʲ] |  |
| ⟨сю⟩ | [sʲu] |  |
| ⟨ся⟩ | [sʲa] |  |
| ⟨т⟩ | [t] |  |
| ⟨те⟩ | [tʲe] |  |
| ⟨ти⟩ | [tʲi] |  |
| ⟨ть⟩ | [tʲ] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [h] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tɕ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [ɛ] |  |
| ⟨ю⟩ | [ju] [u] |  |
| ⟨я⟩ | [ja] [a] |  |
| ⟨ё⟩ | [jɔ] [ɔ] |  |
| ⟨ҫ⟩ | [ɕ] |  |
| ⟨ӈ⟩ | [ŋ] |  |
| ⟨ԑ⟩ | [æ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "enf")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Fon](fon.md) · [Home](../index.md) · [Franco-Provençal →](frp.md)
