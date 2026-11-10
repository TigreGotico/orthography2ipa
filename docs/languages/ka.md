# Georgian (`ka`)

<!-- atlas:summary begin -->
Georgian is a Kartvelian language, written in the Georgian script. Glottolog places it in 6 countries. The `ka` spec is at the research tier. It cites 1 source and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ka` |
| ISO 639-3 | [kat](https://iso639-3.sil.org/code/kat), Georgian |
| Glottolog | [nucl1302](https://glottolog.org/resource/languoid/id/nucl1302), Georgian |
| Wikidata | [Q8108](https://www.wikidata.org/wiki/Q8108) |
| Wikipedia | [Georgian language](https://en.wikipedia.org/wiki/Georgian_language) |
| Family | [Kartvelian](by-family.md#kartvelian) |
| Region | [Eurasia](by-region.md#eurasia) > [Armenia](by-region.md#armenia), [Azerbaijan](by-region.md#azerbaijan), [Georgia](by-region.md#georgia), [Iran](by-region.md#iran), [Russia](by-region.md#russia), [Türkiye](by-region.md#türkiye) |
| Script | [Georgian](by-script.md#georgian) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 430, living |
| Parent | [Proto-Kartvelian (family node)](https://tigregotico.github.io/orthography2ipa/#ccs) `ccs` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`ka` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ka) |
| Spec file | [`ka.json`](../../orthography2ipa/data/ka.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Georgian (Kartuli), official language of Georgia. Written in Mkhedruli script. Three-way consonant distinction: voiced (ბ,გ,დ,ვ,ზ,ჟ,ჯ,ძ), aspirated (თ,ფ,ქ,ჩ,ც,ხ,ჰ), ejective (კ,პ,ტ,ყ,წ,ჭ). Complex consonant clusters. Kartvelian language family unrelated to Indo-European.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 1 work, from 2006. [Sources](#sources) lists them. The spec file writes all 33 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ka.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `ka` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Judeo-Georgian](https://tigregotico.github.io/orthography2ipa/#jge) `jge`: Georgia, Israel, stub tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 1 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-shosted_chikovani2006"></a>Shosted, Ryan K. & Chikovani, Vakhtang (2006). *Standard Georgian*. Journal of the International Phonetic Association 36(2), 255-264. Cited: 255-264. [doi.org](https://doi.org/10.1017/S0025100306002659)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `ka` | generated | epitran-derived | CC0 1.0 | 79887 | 0.2337 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 33 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b pʰ pʼ |  | d tʰ tʼ |  | kʰ kʼ ɡ | qʼ |  |
| Affricate |  |  | dz tsʰ tsʼ | dʒ tʃʰ tʃʼ |  |  |  |
| Nasal | m |  | n |  |  |  |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | v | s z | ʃ ʒ | x ɣ |  | h |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid |  | o |
| Open-mid | ɛ |  |
| Open | a |  |
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ა⟩ | [a] |  |
| ⟨ბ⟩ | [b] |  |
| ⟨გ⟩ | [ɡ] |  |
| ⟨დ⟩ | [d] |  |
| ⟨ე⟩ | [ɛ] |  |
| ⟨ვ⟩ | [v] |  |
| ⟨ზ⟩ | [z] |  |
| ⟨თ⟩ | [tʰ] |  |
| ⟨ი⟩ | [i] |  |
| ⟨კ⟩ | [kʼ] |  |
| ⟨ლ⟩ | [l] |  |
| ⟨მ⟩ | [m] |  |
| ⟨ნ⟩ | [n] |  |
| ⟨ო⟩ | [o] |  |
| ⟨პ⟩ | [pʼ] |  |
| ⟨ჟ⟩ | [ʒ] |  |
| ⟨რ⟩ | [r] |  |
| ⟨ს⟩ | [s] |  |
| ⟨ტ⟩ | [tʼ] |  |
| ⟨უ⟩ | [u] |  |
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

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ka")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Gen](gej-TG.md) · [Home](../index.md) · [German →](de-DE.md)
