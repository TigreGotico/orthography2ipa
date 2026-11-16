# Moksha (`mdf`)

<!-- atlas:summary begin -->
Moksha is an Uralic language, written in the Cyrillic script. Glottolog places it in Russia. The `mdf` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mdf` |
| ISO 639-3 | [mdf](https://iso639-3.sil.org/code/mdf), Moksha |
| Glottolog | [moks1248](https://glottolog.org/resource/languoid/id/moks1248), Moksha |
| Wikidata | [Q13343](https://www.wikidata.org/wiki/Q13343) |
| Wikipedia | [Moksha language](https://en.wikipedia.org/wiki/Moksha_language) |
| Family | [Uralic](by-family.md#uralic) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Proto-Uralic (family node)](https://tigregotico.github.io/orthography2ipa/#urj) `urj` |
| Explorer | [`mdf` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mdf) |
| Spec file | [`mdf.json`](../../orthography2ipa/data/mdf.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Moksha (мокшень кяль), Mordvinic (Uralic), Russia. Written in a Cyrillic alphabet identical in inventory to Russian. Palatalisation is phonemic and is written the Russian way (soft sign <ь>, iotated vowel letters <е ё ю я>), which is why those letters map to a palatalising sequence.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1999 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 35 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mdf.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mdf` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-bartens1999"></a>Bartens, Raija (1999). *Mordvalaiskielten rakenne ja kehitys*. Suomalais-Ugrilainen Seura, Helsinki.
2. <a id="src-moksha_wiki"></a>Wikipedia contributors (2024). *Moksha language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Moksha_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `mdf` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 330 | 0.2212 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 43 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |
| Affricate |  |  | ts |  | tɕ |  |
| Nasal | m |  | n |  |  |  |
| Trill |  |  | r r̥ |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | ɕ | x |
| Approximant |  |  |  |  | j j̥ |  |
| Lateral approximant |  |  | l l̥ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u ʲu |
| Close-mid | e ʲe |  | o ʲo |
| Mid |  | ə |  |
| Open-mid | ɛ |  |  |
| Near-open | æ |  |  |
| Open | a ʲa |  | ɑ |

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
| ⟨е⟩ | [ʲe] [je] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨йх⟩ | [j̥] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨лх⟩ | [l̥] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨рх⟩ | [r̥] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tɕ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ʲu] [ju] |  |
| ⟨я⟩ | [ʲa] [ja] |  |
| ⟨ё⟩ | [ʲo] [jo] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mdf")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Mohawk](moh.md) · [Home](../index.md) · [Mongolian →](mn.md)
