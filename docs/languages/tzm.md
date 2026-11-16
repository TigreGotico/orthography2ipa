# Central Atlas Tamazight (`tzm`)

<!-- atlas:summary begin -->
Central Atlas Tamazight is a Berber language, written in the Tifinagh script. Glottolog places it in the Africa macroarea. The `tzm` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `tzm` |
| ISO 639-3 | [tzm](https://iso639-3.sil.org/code/tzm), Central Atlas Tamazight |
| Wikipedia | [Central Atlas Tamazight](https://en.wikipedia.org/wiki/Central_Atlas_Tamazight) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Berber](by-family.md#afro-asiatic--berber) |
| Region | [Africa](by-region.md#africa) |
| Script | [Tifinagh](by-script.md#tifinagh) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Kabyle-Atlas Berber](https://tigregotico.github.io/orthography2ipa/#ber-x-kabyle-atlas) `ber-x-kabyle-atlas` |
| Explorer | [`tzm` in the data explorer](https://tigregotico.github.io/orthography2ipa/#tzm) |
| Spec file | [`tzm.json`](../../orthography2ipa/data/tzm.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. Central Atlas Tamazight, a Berber (Afroasiatic) language of Morocco written in IRCAM Neo-Tifinagh.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2024. [Sources](#sources) lists them. The spec file writes all 34 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/tzm.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `tzm` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-tzm_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Central Moroccan Berber (cent2194)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/cent2194)
2. <a id="src-tzm_wikipedia"></a>Wikipedia contributors (2024). *Central Atlas Tamazight / Tifinagh*. Wikipedia.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `tzm` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 658 | 0.0160 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 34 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b |  | d dˤ t tˤ |  |  | k kʷ ɡ ɡʷ | q |  |  |
| Nasal | m |  | n |  |  |  |  |  |  |
| Trill |  |  | r rˤ |  |  |  |  |  |  |
| Fricative |  | f | s sˤ z zˤ | ʃ ʒ |  | ɣ | χ | ħ ʕ | h |
| Approximant |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Mid |  | ə |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [w] [ʷ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ⴰ⟩ | [a] |  |
| ⟨ⴱ⟩ | [b] |  |
| ⟨ⴳ⟩ | [ɡ] |  |
| ⟨ⴳⵯ⟩ | [ɡʷ] |  |
| ⟨ⴷ⟩ | [d] |  |
| ⟨ⴹ⟩ | [dˤ] |  |
| ⟨ⴻ⟩ | [ə] |  |
| ⟨ⴼ⟩ | [f] |  |
| ⟨ⴽ⟩ | [k] |  |
| ⟨ⴽⵯ⟩ | [kʷ] |  |
| ⟨ⵀ⟩ | [h] |  |
| ⟨ⵃ⟩ | [ħ] |  |
| ⟨ⵄ⟩ | [ʕ] |  |
| ⟨ⵅ⟩ | [χ] |  |
| ⟨ⵇ⟩ | [q] |  |
| ⟨ⵉ⟩ | [i] |  |
| ⟨ⵊ⟩ | [ʒ] |  |
| ⟨ⵍ⟩ | [l] |  |
| ⟨ⵎ⟩ | [m] |  |
| ⟨ⵏ⟩ | [n] |  |
| ⟨ⵓ⟩ | [u] |  |
| ⟨ⵔ⟩ | [r] |  |
| ⟨ⵕ⟩ | [rˤ] |  |
| ⟨ⵖ⟩ | [ɣ] |  |
| ⟨ⵙ⟩ | [s] |  |
| ⟨ⵚ⟩ | [sˤ] |  |
| ⟨ⵛ⟩ | [ʃ] |  |
| ⟨ⵜ⟩ | [t] |  |
| ⟨ⵟ⟩ | [tˤ] |  |
| ⟨ⵡ⟩ | [w] |  |
| ⟨ⵢ⟩ | [j] |  |
| ⟨ⵣ⟩ | [z] |  |
| ⟨ⵥ⟩ | [zˤ] |  |
| ⟨ⵯ⟩ | [ʷ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "tzm")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Cebuano](ceb.md) · [Home](../index.md) · [Central Bikol →](bcl.md)
