# Kazakh (`kk`)

<!-- atlas:summary begin -->
Kazakh is a Turkic language, written in the Cyrillic script. Glottolog places it in 10 countries. The `kk` spec is at the research tier. It cites 1 source and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kk` |
| ISO 639-3 | [kaz](https://iso639-3.sil.org/code/kaz), Kazakh |
| Glottolog | [kaza1248](https://glottolog.org/resource/languoid/id/kaza1248), Kazakh |
| Wikidata | [Q9252](https://www.wikidata.org/wiki/Q9252) |
| Wikipedia | [Kazakh language](https://en.wikipedia.org/wiki/Kazakh_language) |
| Family | [Turkic](by-family.md#turkic) |
| Region | [Eurasia](by-region.md#eurasia) > [Afghanistan](by-region.md#afghanistan), [China](by-region.md#china), [Iran](by-region.md#iran), [Kazakhstan](by-region.md#kazakhstan), [Kyrgyzstan](by-region.md#kyrgyzstan), [Mongolia](by-region.md#mongolia), [Russia](by-region.md#russia), [Tajikistan](by-region.md#tajikistan) and 2 more |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1940, living |
| Parent | [Proto-Turkic (family node)](https://tigregotico.github.io/orthography2ipa/#trk) `trk` |
| Explorer | [`kk` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kk) |
| Spec file | [`kk.json`](../../orthography2ipa/data/kk.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Kazakh in Cyrillic script (Kazakhstan official orthography). Eleven-vowel system with front/back and labial harmony (McCollum & Chen 2020). А = central-back /ɑ/ (not front [a]), Ы = central schwa-like /ə/ (not [ɯ]), Ө = mid central rounded /ɵ/. Қ = uvular /q/, Ғ = /ʁ/, Ң = /ŋ/, Ұ = back unrounded /ʊ/, Ү = /y/, І = /ɪ/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 1 work, from 2020. [Sources](#sources) lists them. The spec file writes all 40 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kk.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kk` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 1 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-mccollum_chen_2020_kazakh"></a>McCollum, Adam G. and Chen, Si (2020). *Kazakh*. Journal of the International Phonetic Association. Cited: 276-298. [doi.org](https://doi.org/10.1017/S0025100319000185)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `kk` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 714 | 0.1820 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `kk` | generated | epitran-derived | CC0 1.0 | 1403 | 0.1264 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 42 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | q |  |
| Affricate |  |  | ts | tʃ |  |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x | ʁ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i y |  | u |
| Near-close | ɪ |  | ʊ |
| Close-mid | e | ɵ | o |
| Mid |  | ə |  |
| Near-open | æ |  |  |
| Open |  |  | ɑ |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [w] [ɪj] [ʃtʃ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [ɑ] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [e] [je] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] [ɪj] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] [w] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ʃtʃ] |  |
| ⟨ы⟩ | [ə] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨і⟩ | [ɪ] |  |
| ⟨ғ⟩ | [ʁ] |  |
| ⟨қ⟩ | [q] |  |
| ⟨ң⟩ | [ŋ] |  |
| ⟨ү⟩ | [y] |  |
| ⟨ұ⟩ | [ʊ] |  |
| ⟨һ⟩ | [h] |  |
| ⟨ә⟩ | [æ] |  |
| ⟨ө⟩ | [ɵ] |  |

Stress falls on the last syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kk")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kashubian](csb.md) · [Home](../index.md) · [Ket →](ket.md)
