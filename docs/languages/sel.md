# Selkup (`sel`)

<!-- atlas:summary begin -->
Selkup is an Uralic language, written in the Cyrillic script. Glottolog places it in Russia. The `sel` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sel` |
| ISO 639-3 | [sel](https://iso639-3.sil.org/code/sel), Selkup |
| Glottolog | [selk1253](https://glottolog.org/resource/languoid/id/selk1253), Selkup |
| Wikipedia | [Selkup language](https://en.wikipedia.org/wiki/Selkup_language) |
| Family | [Uralic](by-family.md#uralic) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Uralic](https://tigregotico.github.io/orthography2ipa/#x-clade-ural1272) `x-clade-ural1272` |
| Explorer | [`sel` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sel) |
| Spec file | [`sel.json`](../../orthography2ipa/data/sel.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Northern (Taz) Selkup, Samoyedic branch, Yamalo-Nenets/Tomsk region, Russia. INPUT CONTRACT: Northern Selkup Cyrillic orthography (Cyrillicised script standardised on the Taz dialect), NFC.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1998 to 2024. [Sources](#sources) lists them. The spec file writes all 55 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sel.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sel` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-helimski1998"></a>Helimski, Eugene (1998). *Selkup*. in Daniel Abondolo (ed.), The Uralic Languages, Routledge. [routledge.com](https://www.routledge.com/The-Uralic-Languages/Abondolo-Valijarvi/p/book/9781138459166)
2. <a id="src-glottolog2024"></a>Hammarström, Harald, Forkel, Robert, Haspelmath, Martin, Bank, Sebastian (2024). *Glottolog 5.0*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/)
3. <a id="src-phoible2019"></a>Moran, Steven, McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0 (doi:10.5281/zenodo.2562766)*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/inventories/view/2485)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `sel` | gold | lexicon-derived | CC BY 4.0 | 886 | 0.0342 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 54 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t tː |  |  | k ɡ | q |
| Affricate |  |  | ts |  | tɕ |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f | s z | ʃ ʒ | ɕ | x |  |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  | ʎ |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i y | ɨ | u |
| Close-mid | e ø |  | o |
| Near-open | æ |  |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [pʲe] [pʲi] [tʲe] [tʲi] [w] [ɕe] [ɕo] [ɲa] [ɲe] [ɲi] [ɲu] [ʎa] [ʎe] [ʎi] [ʎu] [ʲ].
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
| ⟨е⟩ | [je] [e] |  |
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
| ⟨не⟩ | [ɲe] |  |
| ⟨ни⟩ | [ɲi] |  |
| ⟨нь⟩ | [ɲ] |  |
| ⟨ню⟩ | [ɲu] |  |
| ⟨ня⟩ | [ɲa] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨пе⟩ | [pʲe] |  |
| ⟨пи⟩ | [pʲi] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨те⟩ | [tʲe] |  |
| ⟨ти⟩ | [tʲi] |  |
| ⟨тт⟩ | [tː] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tɕ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ще⟩ | [ɕe] |  |
| ⟨щё⟩ | [ɕo] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [æ] |  |
| ⟨ю⟩ | [ju] [u] |  |
| ⟨я⟩ | [ja] [a] |  |
| ⟨ё⟩ | [jo] [o] |  |
| ⟨ӄ⟩ | [q] |  |
| ⟨ӈ⟩ | [ŋ] |  |
| ⟨ӧ⟩ | [ø] |  |
| ⟨ө⟩ | [ø] |  |
| ⟨ӱ⟩ | [y] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sel")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Seediq](trv.md) · [Home](../index.md) · [Sena →](seh.md)
