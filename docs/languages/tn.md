# Tswana (`tn`)

<!-- atlas:summary begin -->
Tswana is a Bantu language, written in the Latin script. Glottolog places it in 5 countries. The `tn` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `tn` |
| ISO 639-3 | [tsn](https://iso639-3.sil.org/code/tsn), Tswana |
| Glottolog | [tswa1253](https://glottolog.org/resource/languoid/id/tswa1253), Tswana |
| Wikipedia | [Tswana language](https://en.wikipedia.org/wiki/Tswana_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) > [Bantu](by-family.md#atlantic-congo--bantu) |
| Region | [Africa](by-region.md#africa) > [Botswana](by-region.md#botswana), [Namibia](by-region.md#namibia), [South Africa](by-region.md#south-africa), [Zambia](by-region.md#zambia), [Zimbabwe](by-region.md#zimbabwe) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Bantu](https://tigregotico.github.io/orthography2ipa/#x-clade-narr1281) `x-clade-narr1281` |
| Explorer | [`tn` in the data explorer](https://tigregotico.github.io/orthography2ipa/#tn) |
| Spec file | [`tn.json`](../../orthography2ipa/data/tn.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Tswana (Setswana), Sotho-Tswana (Bantu) language, official in Botswana and South Africa, written disjunctively in the Latin script.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1955 to 2016. [Sources](#sources) lists them. The spec file writes all 40 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/tn.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `tn` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-cole1955"></a>Cole, Desmond T. (1955). *An Introduction to Tswana Grammar*. Longmans, Green & Co.
2. <a id="src-bennett2016"></a>Bennett, William G., Diemer, Maxine, Kerford, Justine, Probert, Tracy, Wesi, Tsholofelo (2016). *Setswana (South African)*. Journal of the International Phonetic Association 46(2), 235-246. [doi.org](https://doi.org/10.1017/S0025100316000050)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `tn` | generated | epitran-derived | CC0 1.0 | 2271 | 0.3953 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 41 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | pʰ pʼ |  | d tʰ tʼ |  |  | kʰ kʼ |  |  |
| Affricate |  |  | tsʰ tsʰʷ tsʼ tsʼʷ tɬʼ t͡ɬʰ | dʒ |  |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  | f | s | ʃ |  | x ɣ | χ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e̝ | o̝ |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [fʃ] [pʃʼ] [w] [ǃ] [ǃʰ] [ɓ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [ɓ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e̝] [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨fj⟩ | [fʃ] |  |
| ⟨g⟩ | [ɣ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [kʼ] |  |
| ⟨kg⟩ | [χ] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o̝] [ɔ] |  |
| ⟨p⟩ | [pʼ] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨pj⟩ | [pʃʼ] |  |
| ⟨q⟩ | [ǃ] |  |
| ⟨qh⟩ | [ǃʰ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [tʼ] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨tl⟩ | [tɬʼ] |  |
| ⟨tlh⟩ | [t͡ɬʰ] |  |
| ⟨ts⟩ | [tsʼ] |  |
| ⟨tsh⟩ | [tsʰ] |  |
| ⟨tshw⟩ | [tsʰʷ] |  |
| ⟨tsw⟩ | [tsʼʷ] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ê⟩ | [ɛ] |  |
| ⟨ô⟩ | [ɔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "tn")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Tsonga](ts.md) · [Home](../index.md) · [Tulu →](tcy.md)
