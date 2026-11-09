# Tatar (`tt`)

<!-- atlas:summary begin -->
Tatar is a Turkic language, written in the Cyrillic script. Glottolog places it in 11 countries. The `tt` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `tt` |
| ISO 639-3 | [tat](https://iso639-3.sil.org/code/tat), Tatar |
| Glottolog | [tata1255](https://glottolog.org/resource/languoid/id/tata1255), Tatar |
| Wikidata | [Q25285](https://www.wikidata.org/wiki/Q25285) |
| Wikipedia | [Tatar language](https://en.wikipedia.org/wiki/Tatar_language) |
| Family | [Turkic](by-family.md#turkic) |
| Region | [Eurasia](by-region.md#eurasia) > [Azerbaijan](by-region.md#azerbaijan), [Belarus](by-region.md#belarus), [China](by-region.md#china), [Estonia](by-region.md#estonia), [Finland](by-region.md#finland), [Georgia](by-region.md#georgia), [Kazakhstan](by-region.md#kazakhstan), [Latvia](by-region.md#latvia) and 3 more |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1939, living |
| Parent | [Proto-Turkic (family node)](https://tigregotico.github.io/orthography2ipa/#trk) `trk` |
| Explorer | [`tt` in the data explorer](https://tigregotico.github.io/orthography2ipa/#tt) |
| Spec file | [`tt.json`](../../orthography2ipa/data/tt.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Tatar in Cyrillic script (Tatarstan). Nine vowels with front/back harmony: а /ɑ/, ә /æ/, о /o/, ө /ø/, у /u/, ү /y/, ы /ɯ/, и /i/, е /e/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1998 to 2018. [Sources](#sources) lists them. The spec file writes all 39 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/tt.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `tt` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-henry_2018_ot_tatar"></a>Henry, Cassidy (2018). *An Optimality Theoretic analysis of vowel harmony in Kazan Tatar*. Proceedings of the Linguistic Society of America 3(1): 4:1-11. Cited: 3. [doi.org](https://doi.org/10.3765/plsa.v3i1.4278)
2. <a id="src-berta_1998_tatar_bashkir"></a>Berta, Árpád (1998). *Tatar and Bashkir*. Routledge, in The Turkic Languages (Johanson, Lars & Csató, Éva Ágnes, eds.).
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `tt` | generated | epitran-derived | CC0 1.0 | 22220 | 0.2455 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 38 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | ʔ |
| Affricate |  |  | ts | tʃ |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | ʑ | x | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u ɯ |
| Close-mid | e ø | o |
| Near-open | æ |  |
| Open |  | ɑ |

Sequences that the spec writes as one unit: [je] [jo] [ju] [jɑ] [ʃtʃ].
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
| ⟨е⟩ | [je] [e] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
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
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ʃtʃ] |  |
| ⟨ъ⟩ | [ʔ] ∅ |  |
| ⟨ы⟩ | [ɯ] |  |
| ⟨ь⟩ | [ʔ] ∅ |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [jɑ] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨җ⟩ | [ʑ] |  |
| ⟨ң⟩ | [ŋ] |  |
| ⟨ү⟩ | [y] |  |
| ⟨һ⟩ | [h] |  |
| ⟨ә⟩ | [æ] |  |
| ⟨ө⟩ | [ø] |  |

Stress falls on the last syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "tt")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Tarifit](rif.md) · [Home](../index.md) · [Telugu →](te.md)
