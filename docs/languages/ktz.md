# Juǀʼhoan (`ktz`)

<!-- atlas:summary begin -->
Juǀʼhoan is a Kxa language, written in the Latin script. Glottolog places it in the Africa macroarea. The `ktz` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ktz` |
| ISO 639-3 | [ktz](https://iso639-3.sil.org/code/ktz), Juǀʼhoan |
| Wikipedia | [JuǀʼHoan dialect](https://en.wikipedia.org/wiki/Ju%C7%80%CA%BCHoan_dialect) |
| Family | [Kxa](by-family.md#kxa) |
| Region | [Africa](by-region.md#africa) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Kxa](https://tigregotico.github.io/orthography2ipa/#x-clade-kxaa1236) `x-clade-kxaa1236` |
| Explorer | [`ktz` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ktz) |
| Spec file | [`ktz.json`](../../orthography2ipa/data/ktz.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Kxa (formerly Northern Khoisan) click language of Namibia and Botswana, in the standardized Dickens (1994) orthography, the best-documented San orthography.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 81 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ktz.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ktz` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-ktz_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: South-Eastern Ju (juho1239)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/juho1239)
2. <a id="src-ktz_wikipedia"></a>Wikipedia contributors (2024). *Juǀʼhoan dialect*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Ju%C7%80%CA%BCHoan_dialect)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ktz` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 134 | 0.3464 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 79 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ | d t tʰ |  | k kʰ ɡ |  |  |
| Affricate |  | ts tsʰ tsʼ | tʃ tʃʰ tʃʼ | kxʼ |  |  |
| Nasal | m | n |  | ŋ |  |  |
| Tap |  | ɾ |  |  |  |  |
| Fricative |  | s z | ʃ ʒ |  | χ | ɦ |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i ĩ | u ũ |
| Close-mid | e ẽ | o oˤ õ |
| Open | a aˤ ã |  |

Sequences that the spec writes as one unit: [b͡pʰ] [d͡tsʰ] [d͡tʃʰ] [d͡tʰ] [ǀ] [ǀʰ] [ǀˀ] [ǀ͡χ] [ǁ] [ǁʰ] [ǁˀ] [ǁ͡χ] [ǂ] [ǂʰ] [ǂˀ] [ǂ͡χ] [ǃ] [ǃʰ] [ǃˀ] [ǃ͡χ] [ɡ͡kʰ] [ᵏǀʼ] [ᵏǁʼ] [ᵏǂʼ] [ᵏǃʼ] [ᵑǀ] [ᵑǀʰ] [ᵑǀˀ] [ᵑǁ] [ᵑǁʰ] [ᵑǁˀ] [ᵑǂ] [ᵑǂʰ] [ᵑǂˀ] [ᵑǃ] [ᵑǃʰ] [ᵑǃˀ] [ᶢǀ] [ᶢǁ] [ᶢǂ], and 1 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨an⟩ | [ã] |  |
| ⟨ang⟩ | [ŋ] |  |
| ⟨aq⟩ | [aˤ] |  |
| ⟨b⟩ | [b] |  |
| ⟨bh⟩ | [b͡pʰ] |  |
| ⟨c⟩ | [ʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dc⟩ | [tʃʼ] |  |
| ⟨dch⟩ | [d͡tʃʰ] |  |
| ⟨dh⟩ | [d͡tʰ] |  |
| ⟨ds⟩ | [tsʼ] |  |
| ⟨dsh⟩ | [d͡tsʰ] |  |
| ⟨e⟩ | [e] |  |
| ⟨en⟩ | [ẽ] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gh⟩ | [ɡ͡kʰ] |  |
| ⟨gǀ⟩ | [ᶢǀ] |  |
| ⟨gǁ⟩ | [ᶢǁ] |  |
| ⟨gǂ⟩ | [ᶢǂ] |  |
| ⟨gǃ⟩ | [ᶢǃ] |  |
| ⟨h⟩ | [ɦ] |  |
| ⟨i⟩ | [i] |  |
| ⟨in⟩ | [ĩ] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨kx⟩ | [kxʼ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨nǀ⟩ | [ᵑǀ] |  |
| ⟨nǀh⟩ | [ᵑǀʰ] |  |
| ⟨nǁ⟩ | [ᵑǁ] |  |
| ⟨nǁh⟩ | [ᵑǁʰ] |  |
| ⟨nǂ⟩ | [ᵑǂ] |  |
| ⟨nǂh⟩ | [ᵑǂʰ] |  |
| ⟨nǃ⟩ | [ᵑǃ] |  |
| ⟨nǃh⟩ | [ᵑǃʰ] |  |
| ⟨o⟩ | [o] |  |
| ⟨on⟩ | [õ] |  |
| ⟨oq⟩ | [oˤ] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tc⟩ | [tʃ] |  |
| ⟨tch⟩ | [tʃʰ] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨tj⟩ | [tʃʼ] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨tsh⟩ | [tsʰ] |  |
| ⟨tz⟩ | [tsʼ] |  |
| ⟨u⟩ | [u] |  |
| ⟨un⟩ | [ũ] |  |
| ⟨x⟩ | [χ] |  |
| ⟨z⟩ | [z] |  |
| ⟨ǀ⟩ | [ǀ] |  |
| ⟨ǀh⟩ | [ǀʰ] |  |
| ⟨ǀk⟩ | [ᵏǀʼ] |  |
| ⟨ǀx⟩ | [ǀ͡χ] |  |
| ⟨ǀʼ⟩ | [ǀˀ] |  |
| ⟨ǀʼh⟩ | [ᵑǀˀ] |  |
| ⟨ǁ⟩ | [ǁ] |  |
| ⟨ǁh⟩ | [ǁʰ] |  |
| ⟨ǁk⟩ | [ᵏǁʼ] |  |
| ⟨ǁx⟩ | [ǁ͡χ] |  |
| ⟨ǁʼ⟩ | [ǁˀ] |  |
| ⟨ǁʼh⟩ | [ᵑǁˀ] |  |
| ⟨ǂ⟩ | [ǂ] |  |
| ⟨ǂh⟩ | [ǂʰ] |  |
| ⟨ǂk⟩ | [ᵏǂʼ] |  |
| ⟨ǂx⟩ | [ǂ͡χ] |  |
| ⟨ǂʼ⟩ | [ǂˀ] |  |
| ⟨ǂʼh⟩ | [ᵑǂˀ] |  |
| ⟨ǃ⟩ | [ǃ] |  |
| ⟨ǃh⟩ | [ǃʰ] |  |
| ⟨ǃk⟩ | [ᵏǃʼ] |  |
| ⟨ǃx⟩ | [ǃ͡χ] |  |
| ⟨ǃʼ⟩ | [ǃˀ] |  |
| ⟨ǃʼh⟩ | [ᵑǃˀ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ktz")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Juba Arabic](pga.md) · [Home](../index.md) · [Kabardian →](kbd.md)
