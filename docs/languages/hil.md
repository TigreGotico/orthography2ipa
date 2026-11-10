# Hiligaynon (`hil`)

<!-- atlas:summary begin -->
Hiligaynon is a Malayo-Polynesian language, written in the Latin script. Glottolog places it in the Africa, Eurasia, Papunesia and South America macroareas. The `hil` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `hil` |
| ISO 639-3 | [hil](https://iso639-3.sil.org/code/hil), Hiligaynon |
| Wikipedia | [Hiligaynon language](https://en.wikipedia.org/wiki/Hiligaynon_language) |
| Family | [Austronesian](by-family.md#austronesian) > [Malayo-Polynesian](by-family.md#austronesian--malayo-polynesian) |
| Region | [Africa](by-region.md#several-macroareas), [Eurasia](by-region.md#several-macroareas), [Papunesia](by-region.md#several-macroareas), [South America](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Malayo-Polynesian](https://tigregotico.github.io/orthography2ipa/#x-clade-mala1545) `x-clade-mala1545` |
| Explorer | [`hil` in the data explorer](https://tigregotico.github.io/orthography2ipa/#hil) |
| Spec file | [`hil.json`](../../orthography2ipa/data/hil.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. A Central Philippine (Bisayan) Austronesian language of Panay and Negros, written in a Latin alphabet based on the modern Filipino/abakada convention. The grapheme map covers the native consonant and five-vowel inventory plus the digraph ng for the velar nasal.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 20 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/hil.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `hil` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-hil_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Hiligaynon (hili1240)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/hili1240)
2. <a id="src-hil_wikipedia"></a>Wikipedia contributors (2024). *Hiligaynon language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Hiligaynon_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `hil` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 466 | 0.0966 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 20 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d t |  | k ɡ |  |
| Nasal | m | n |  | ŋ |  |
| Tap |  | ɾ |  |  |  |
| Fricative |  | s |  |  | h |
| Approximant |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid |  | o |
| Open-mid | ɛ |  |
| Open | a |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "hil")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Herero](hz.md) · [Home](../index.md) · [Hill Mari →](mrj.md)
