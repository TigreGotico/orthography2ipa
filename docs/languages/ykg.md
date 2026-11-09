# Northern Yukaghir (`ykg`)

<!-- atlas:summary begin -->
Northern Yukaghir is a Yukaghir language, written in the Cyrillic script. Glottolog places it in Russia. The `ykg` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ykg` |
| ISO 639-3 | [ykg](https://iso639-3.sil.org/code/ykg), Northern Yukaghir |
| Glottolog | [nort2745](https://glottolog.org/resource/languoid/id/nort2745), Northern Yukaghir |
| Wikipedia | [Yukaghir languages](https://en.wikipedia.org/wiki/Yukaghir_languages) |
| Family | [Yukaghir](by-family.md#yukaghir) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Yukaghir](https://tigregotico.github.io/orthography2ipa/#x-clade-yuka1259) `x-clade-yuka1259` |
| Explorer | [`ykg` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ykg) |
| Spec file | [`ykg.json`](../../orthography2ipa/data/ykg.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Northern (Tundra) Yukaghir, Yukaghir family (an isolate-level branch outside Uralic), Sakha Republic/Chukotka, Russia. INPUT CONTRACT: Tundra Yukaghir Cyrillic orthography, NFC.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 2003 to 2024. [Sources](#sources) lists them. The spec file writes all 45 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ykg.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ykg` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 4 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-maslova2003tundra"></a>Maslova, Elena (2003). *Tundra Yukaghir*. Languages of the World/Materials 372, LINCOM Europa. [lincom-shop.eu](https://lincom-shop.eu/LWM-372-Tundra-Yukaghir/en)
2. <a id="src-schmalz2013"></a>Schmalz, Mark (2013). *Aspects of the Grammar of Tundra Yukaghir*. PhD dissertation, University of Amsterdam. [pure.uva.nl](https://pure.uva.nl/ws/files/1518096/130869_thesis.pdf)
3. <a id="src-glottolog2024"></a>Hammarström, Harald, Forkel, Robert, Haspelmath, Martin, Bank, Sebastian (2024). *Glottolog 5.0*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/)
4. <a id="src-phoible2019"></a>Moran, Steven, McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0 (doi:10.5281/zenodo.2562766)*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/inventories/view/193)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `ykg` | gold | lexicon-derived | CC BY 4.0 | 813 | 0.3052 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 47 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d dʲ t |  |  | k ɡ | q ɢ |
| Affricate |  |  | ts | tʃ |  |  |  |
| Nasal | m |  | n nʲ |  |  | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f | s z | ʃ ʒ | ɕ | x | ʁ |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l lʲ |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u uː |
| Near-close | ɪ ɪː |  |  |
| Close-mid | e | ɵ̞ | o̞ o̞ː |
| Open-mid | ɛ |  |  |
| Open | a aː a̟ a̟ː |  |  |

Sequences that the spec writes as one unit: [ja] [jo̞] [ju] [jɛ] [w] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a̟] |  |
| ⟨аа⟩ | [a̟ː] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [w] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨дь⟩ | [dʲ] |  |
| ⟨е⟩ | [jɛ] [ɛ] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [ɪ] |  |
| ⟨ии⟩ | [ɪː] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨ль⟩ | [lʲ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨нь⟩ | [nʲ] |  |
| ⟨о⟩ | [o̞] |  |
| ⟨оо⟩ | [o̞ː] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨уу⟩ | [uː] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɪ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [ɛ] |  |
| ⟨ю⟩ | [ju] [u] |  |
| ⟨я⟩ | [ja] [a̟] |  |
| ⟨ё⟩ | [jo̞] [o̞] |  |
| ⟨ӄ⟩ | [q] |  |
| ⟨ӈ⟩ | [ŋ] |  |
| ⟨ө⟩ | [ɵ̞] |  |
| ⟨ӷ⟩ | [ʁ] |  |
| ⟨ӻ⟩ | [ʁ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ykg")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Northern Tiwa](twf.md) · [Home](../index.md) · [Norwegian →](no.md)
