# Chechen (`ce`)

<!-- atlas:summary begin -->
Chechen is a Nakh-Daghestanian language, written in the Cyrillic script. Glottolog places it in Georgia, Kazakhstan and Russia. The `ce` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ce` |
| ISO 639-3 | [che](https://iso639-3.sil.org/code/che), Chechen |
| Glottolog | [chec1245](https://glottolog.org/resource/languoid/id/chec1245), Chechen |
| Wikidata | [Q33350](https://www.wikidata.org/wiki/Q33350) |
| Wikipedia | [Chechen language](https://en.wikipedia.org/wiki/Chechen_language) |
| Family | [Nakh-Daghestanian](by-family.md#nakh-daghestanian) |
| Region | [Eurasia](by-region.md#eurasia) > [Georgia](by-region.md#georgia), [Kazakhstan](by-region.md#kazakhstan), [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1938, living |
| Parent | [Nakh-Daghestanian](https://tigregotico.github.io/orthography2ipa/#x-clade-nakh1245) `x-clade-nakh1245` |
| Explorer | [`ce` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ce) |
| Spec file | [`ce.json`](../../orthography2ipa/data/ce.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Chechen in Cyrillic script. Rich ejective series: КӀ, ПӀ, ТӀ, ЦӀ, ЧӀ. ГӀ = pharyngeal /ʕ/, ХЬ = pharyngeal /ħ/, ХӀ = /h/. Front rounded vowels: УЬ = /y/, ОЬ = /wø/, ЭЬ = /ø/. Pharyngeals and ejectives are typologically notable. Complex consonant clusters.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2017 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 43 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ce.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ce` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-chechen_wiki"></a>Wikipedia contributors (2024). *Chechen language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Chechen_language)
2. <a id="src-dotton_wagner_chechen"></a>Dotton, Zura & Wagner, John Doyle (2017). *A Grammar of Chechen*. Duke University, Slavic and Eurasian Language Resource Center. Cited: 5-7. [slaviccenters.duke.edu](https://slaviccenters.duke.edu/sites/slaviccenters.duke.edu/files/file-attachments/chechen-grammar.original.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ce` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 461 | 0.2541 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 42 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʼ |  | d t tʼ |  |  | k kʼ ɡ |  | ʔ |
| Affricate |  |  | ts tsʼ | tʃ tʃʼ |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x | ħ ʕ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u |
| Close-mid | e ø | o |
| Near-open | æ |  |
| Open | a |  |

Sequences that the spec writes as one unit: [ja] [je] [ju] [wo] [wø].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨I⟩ | [ʔ] |  |
| ⟨а⟩ | [a] |  |
| ⟨аь⟩ | [æ] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨гӀ⟩ | [ʕ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [je] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨кӀ⟩ | [kʼ] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [wo] [o] |  |
| ⟨оь⟩ | [wø] |  |
| ⟨п⟩ | [p] |  |
| ⟨пӀ⟩ | [pʼ] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨тӀ⟩ | [tʼ] |  |
| ⟨у⟩ | [u] |  |
| ⟨уь⟩ | [y] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨хь⟩ | [ħ] |  |
| ⟨хӀ⟩ | [h] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨цӀ⟩ | [tsʼ] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨чӀ⟩ | [tʃʼ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ʃ] |  |
| ⟨ъ⟩ | [ʔ] |  |
| ⟨э⟩ | [e] |  |
| ⟨эь⟩ | [ø] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ce")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Chavacano](cbk-PH.md) · [Home](../index.md) · [Cherokee →](chr.md)
