# Kaingang (`kgp`)

<!-- atlas:summary begin -->
Kaingang is a Nuclear-Macro-Je language, written in the Latin script. Glottolog places it in the South America macroarea. The `kgp` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kgp` |
| ISO 639-3 | [kgp](https://iso639-3.sil.org/code/kgp), Kaingang |
| Wikipedia | [Kaingang language](https://en.wikipedia.org/wiki/Kaingang_language) |
| Family | [Nuclear-Macro-Je](by-family.md#nuclear-macro-je) |
| Region | [South America](by-region.md#south-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Nuclear-Macro-Je](https://tigregotico.github.io/orthography2ipa/#x-clade-nucl1710) `x-clade-nucl1710` |
| Explorer | [`kgp` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kgp) |
| Spec file | [`kgp.json`](../../orthography2ipa/data/kgp.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Macro-Je language of southern Brazil, Latin orthography. The letters m/n/nh/g denote the nasal-consonant series whose oral and prestopped allophones ([m~b], [n~d], [ɲ~ɟ], [ŋ~ɡ]) are conditioned by adjacent vowel nasality and are not written, the nasal phonemic value is mapped.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 28 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kgp.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kgp` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-kgp_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Kaingang (kain1272)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/kain1272)
2. <a id="src-kgp_wikipedia"></a>Wikipedia contributors (2024). *Kaingang language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Kaingang_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `kgp` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 106 | 0.2351 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 28 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | p | t |  | k | ʔ |
| Nasal | m | n | ɲ | ŋ |  |
| Fricative | ɸ |  | ç |  | h |
| Approximant |  | ɹ | j |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i ĩ | u ũ |
| Close-mid | e ẽ | o ɤ ɤ̃ |
| Open-mid | ɛ | ɔ ʌ |
| Open | a ã |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [ɸ] |  |
| ⟨g⟩ | [ŋ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨nh⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɹ] |  |
| ⟨s⟩ | [ç] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [w] |  |
| ⟨y⟩ | [ɤ] |  |
| ⟨á⟩ | [ʌ] |  |
| ⟨ã⟩ | [ã] |  |
| ⟨é⟩ | [ɛ] |  |
| ⟨ó⟩ | [ɔ] |  |
| ⟨ĩ⟩ | [ĩ] |  |
| ⟨ũ⟩ | [ũ] |  |
| ⟨ẽ⟩ | [ẽ] |  |
| ⟨ỹ⟩ | [ɤ̃] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kgp")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kabyle](kab.md) · [Home](../index.md) · [Kalmyk →](xal.md)
