# Makasar (`mak`)

<!-- atlas:summary begin -->
Makasar is an Austronesian language, written in the Latin script. Glottolog places it in the Africa, Eurasia, Papunesia and South America macroareas. The `mak` spec is at the research tier. It cites 1 source and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mak` |
| ISO 639-3 | [mak](https://iso639-3.sil.org/code/mak), Makasar |
| Wikipedia | [Makassarese language](https://en.wikipedia.org/wiki/Makassarese_language) |
| Family | [Austronesian](by-family.md#austronesian) |
| Region | [Africa](by-region.md#several-macroareas), [Eurasia](by-region.md#several-macroareas), [Papunesia](by-region.md#several-macroareas), [South America](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Proto-Malayo-Polynesian (family node)](https://tigregotico.github.io/orthography2ipa/#poz) `poz` |
| Explorer | [`mak` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mak) |
| Spec file | [`mak.json`](../../orthography2ipa/data/mak.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. Makasar/Makassarese (South Sulawesi, Austronesian), Latin orthography. Palatal stops ⟨c j⟩=/c ɟ/, ⟨ng⟩=/ŋ/, ⟨ny⟩=/ɲ/ and a phonemic glottal stop written ⟨ʼ⟩. Geminate consonants (doubled letters) are phonemic. Indonesian adstrate.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 1 work, from 2019. [Sources](#sources) lists them. The spec file writes all 26 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mak.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mak` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 1 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-jukes2019"></a>Jukes, Anthony (2019). *A Grammar of Makasar: A Language of South Sulawesi, Indonesia*. Brill.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `mak` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 832 | 0.0194 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 24 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d t | c ɟ | k ɡ | ʔ |
| Nasal | m | n | ɲ | ŋ |  |
| Trill |  | r |  |  |  |
| Fricative |  | s |  |  | h |
| Approximant |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [c] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ɟ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ʼ⟩ | [ʔ] |  |
| ⟨’⟩ | [ʔ] |  |

Stress falls on the penult by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mak")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Maithili](mai.md) · [Home](../index.md) · [Malagasy →](mg.md)
