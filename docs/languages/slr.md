# Salar (`slr`)

<!-- atlas:summary begin -->
Salar is a Turkic language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `slr` spec is at the research tier. It cites 1 source and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `slr` |
| ISO 639-3 | [slr](https://iso639-3.sil.org/code/slr), Salar |
| Wikipedia | [Salar language](https://en.wikipedia.org/wiki/Salar_language) |
| Family | [Turkic](by-family.md#turkic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Proto-Turkic (family node)](https://tigregotico.github.io/orthography2ipa/#trk) `trk` |
| Explorer | [`slr` in the data explorer](https://tigregotico.github.io/orthography2ipa/#slr) |
| Spec file | [`slr.json`](../../orthography2ipa/data/slr.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. Salar (Oghuz Turkic, Qinghai/Gansu, China), in the TIP Latin orthography. Retains Oghuz vowel harmony, heavy Chinese and Amdo Tibetan contact (unencoded adstrate). ⟨c⟩=/ʝ/, ⟨q⟩=/q/ per the samples.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 1 work, from 2007. [Sources](#sources) lists them. The spec file writes all 32 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/slr.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `slr` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 1 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-dwyer2007"></a>Dwyer, Arienne M. (2007). *Salar: A Study in Inner Asian Language Contact Processes, Part I: Phonology*. Harrassowitz Verlag.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `slr` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 752 | 0.2850 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 33 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | q |  |
| Affricate |  |  |  | dʒ tʃ |  |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | ʝ | x |  | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u ɯ |
| Close-mid | e ø | o |
| Open |  | ɑ |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ʝ] [dʒ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [q] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ç⟩ | [tʃ] |  |
| ⟨ñ⟩ | [ŋ] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨ü⟩ | [y] |  |
| ⟨ı⟩ | [ɯ] |  |
| ⟨ş⟩ | [ʃ] |  |

Stress falls on the last syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "slr")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Sakizaya](szy.md) · [Home](../index.md) · [Samoan →](sm.md)
