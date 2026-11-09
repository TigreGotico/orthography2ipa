# Polabian (`pox`)

<!-- atlas:summary begin -->
Polabian is a West Slavic language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `pox` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `pox` |
| ISO 639-3 | [pox](https://iso639-3.sil.org/code/pox), Polabian |
| Wikipedia | [Polabian language](https://en.wikipedia.org/wiki/Polabian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic > West Slavic](by-family.md#indo-european--balto-slavic--slavic--west-slavic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [West Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-west2792) `x-clade-west2792` |
| Explorer | [`pox` in the data explorer](https://tigregotico.github.io/orthography2ipa/#pox) |
| Spec file | [`pox.json`](../../orthography2ipa/data/pox.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. West Slavic (Lechitic) language of the Elbe, extinct since the 18th century and known only from German-authored word lists and glossaries.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 2004 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 46 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/pox.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `pox` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 4 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-pox_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Polabian (pola1255)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/pola1255)
2. <a id="src-pox_wikipedia"></a>Wikipedia contributors (2024). *Polabian language (Wikipedia)*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Polabian_language)
3. <a id="src-pox_kortlandt_accentuation"></a>Kortlandt, Frederik (2011). *Polabian Accentuation*. Leiden University (kortlandt.nl). Cited: 1-2. [kortlandt.nl](https://www.kortlandt.nl/publications/art107e.pdf)
4. <a id="src-pox_zygis_2004"></a>Żygis, Marzena (2004). *(Un)markedness of trills: The case of Slavic r-palatalisation*. ZAS Papers in Linguistics 37, 137-166. Cited: 142. [zaspil.leibniz-zas.de](https://zaspil.leibniz-zas.de/article/download/592/572/1121)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `pox` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 314 | 0.2538 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 41 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʲ |  | d dʲ t tʲ |  |  | k ɡ |
| Affricate |  |  | ts | tʃ | tɕ |  |
| Nasal | m mʲ |  | n |  | ɲ |  |
| Trill |  |  | r rʲ |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | ɕ ʑ | x |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l lʲ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i y | ɨ | u |
| Close-mid | e ø |  | o |
| Mid |  | ə |  |
| Open-mid |  |  | ɔ ɔ̃ |
| Open | a |  |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨ch⟩ | [x] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [x] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [ɨ] |  |
| ⟨z⟩ | [z] |  |
| ⟨å⟩ | [ɔ] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨ü⟩ | [y] |  |
| ⟨ą⟩ | [ɔ̃] |  |
| ⟨ć⟩ | [tɕ] |  |
| ⟨č⟩ | [tʃ] |  |
| ⟨ď⟩ | [dʲ] |  |
| ⟨ĕ⟩ | [ə] |  |
| ⟨ė⟩ | [e] |  |
| ⟨ľ⟩ | [lʲ] |  |
| ⟨ń⟩ | [ɲ] |  |
| ⟨ŕ⟩ | [rʲ] |  |
| ⟨ś⟩ | [ɕ] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ť⟩ | [tʲ] |  |
| ⟨ź⟩ | [ʑ] |  |
| ⟨ž⟩ | [ʒ] |  |
| ⟨ǫ⟩ | [ɔ̃] |  |
| ⟨ə⟩ | [ə] |  |
| ⟨ḿ⟩ | [mʲ] |  |
| ⟨ṕ⟩ | [pʲ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "pox")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Pnar](pbv.md) · [Home](../index.md) · [Polish →](pl.md)
