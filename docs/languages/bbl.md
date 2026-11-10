# Bats (`bbl`)

<!-- atlas:summary begin -->
Bats is a Nakh-Daghestanian language, written in the Georgian script. Glottolog places it in the Eurasia macroarea. The `bbl` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `bbl` |
| ISO 639-3 | [bbl](https://iso639-3.sil.org/code/bbl), Bats |
| Wikipedia | [Bats language](https://en.wikipedia.org/wiki/Bats_language) |
| Family | [Nakh-Daghestanian](by-family.md#nakh-daghestanian) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Georgian](by-script.md#georgian) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Nakh-Daghestanian](https://tigregotico.github.io/orthography2ipa/#x-clade-nakh1245) `x-clade-nakh1245` |
| Explorer | [`bbl` in the data explorer](https://tigregotico.github.io/orthography2ipa/#bbl) |
| Spec file | [`bbl.json`](../../orthography2ipa/data/bbl.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Bats (Tsova-Tush) is a Nakh (Northeast Caucasian) language written in the Georgian Mkhedruli script supplemented by extra letters.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1994 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 42 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/bbl.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `bbl` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-bbl_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Bats (bats1242)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/bats1242)
2. <a id="src-holisky_gagua1994"></a>Holisky, Dee Ann, Gagua, Rusudan (1994). *Tsova-Tush (Batsbi)*. In Rieks Smeets (ed.), The Indigenous Languages of the Caucasus, vol. 4: North East Caucasian Languages, Part 2. Caravan Books, Delmar, NY, pp. 147-212. Cited: 147-212. [people.umass.edu](https://people.umass.edu/maxfield/Resources/Tsova%20Tush.pdf)
3. <a id="src-bbl_orthography"></a>Wikipedia contributors (2024). *Bats language, writing system and phonology*. [en.wikipedia.org](https://en.wikipedia.org/wiki/Bats_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `bbl` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 414 | 0.2790 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 42 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b pʰ pʼ |  | d tʰ tʼ |  | kʰ kʼ ɡ | qʼ |  | ʔ |
| Affricate |  |  | dz tsʰ tsʼ | dʒ tʃʰ tʃʼ |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | x ɣ |  | ʕ | h |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i ĩ |  | u ũ |
| Close-mid | ẽ |  | õ |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Open | a ã |  |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ა⟩ | [a] |  |
| ⟨აჼ⟩ | [ã] |  |
| ⟨ბ⟩ | [b] |  |
| ⟨გ⟩ | [ɡ] |  |
| ⟨დ⟩ | [d] |  |
| ⟨ე⟩ | [ɛ] |  |
| ⟨ეჼ⟩ | [ẽ] |  |
| ⟨ვ⟩ | [v] |  |
| ⟨ზ⟩ | [z] |  |
| ⟨თ⟩ | [tʰ] |  |
| ⟨ი⟩ | [i] |  |
| ⟨იჼ⟩ | [ĩ] |  |
| ⟨კ⟩ | [kʼ] |  |
| ⟨ლ⟩ | [l] |  |
| ⟨მ⟩ | [m] |  |
| ⟨ნ⟩ | [n] |  |
| ⟨ო⟩ | [ɔ] |  |
| ⟨ოჼ⟩ | [õ] |  |
| ⟨პ⟩ | [pʼ] |  |
| ⟨ჟ⟩ | [ʒ] |  |
| ⟨რ⟩ | [r] |  |
| ⟨ს⟩ | [s] |  |
| ⟨ტ⟩ | [tʼ] |  |
| ⟨უ⟩ | [u] |  |
| ⟨უჼ⟩ | [ũ] |  |
| ⟨ფ⟩ | [pʰ] |  |
| ⟨ქ⟩ | [kʰ] |  |
| ⟨ღ⟩ | [ɣ] |  |
| ⟨ყ⟩ | [qʼ] |  |
| ⟨შ⟩ | [ʃ] |  |
| ⟨ჩ⟩ | [tʃʰ] |  |
| ⟨ც⟩ | [tsʰ] |  |
| ⟨ძ⟩ | [dz] |  |
| ⟨წ⟩ | [tsʼ] |  |
| ⟨ჭ⟩ | [tʃʼ] |  |
| ⟨ხ⟩ | [x] |  |
| ⟨ჯ⟩ | [dʒ] |  |
| ⟨ჰ⟩ | [h] |  |
| ⟨ჶ⟩ | [f] |  |
| ⟨ჷ⟩ | [ə] |  |
| ⟨ჸ⟩ | [ʔ] |  |
| ⟨ჺ⟩ | [ʕ] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "bbl")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Bashkir](ba.md) · [Home](../index.md) · [Belarusian →](be.md)
