# Sidamo (`sid`)

<!-- atlas:summary begin -->
Sidamo is a Cushitic language, written in the Latin script. Glottolog places it in the Africa macroarea. The `sid` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sid` |
| ISO 639-3 | [sid](https://iso639-3.sil.org/code/sid), Sidamo |
| Wikipedia | [Sidamo language](https://en.wikipedia.org/wiki/Sidamo_language) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Cushitic](by-family.md#afro-asiatic--cushitic) |
| Region | [Africa](by-region.md#africa) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Cushitic](https://tigregotico.github.io/orthography2ipa/#x-clade-cush1243) `x-clade-cush1243` |
| Explorer | [`sid` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sid) |
| Spec file | [`sid.json`](../../orthography2ipa/data/sid.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. Sidamo (Sidaama), a Highland East Cushitic (Afroasiatic) language of Ethiopia written in a Latin orthography modeled on Oromo Qubee.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2024. [Sources](#sources) lists them. The spec file writes all 38 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sid.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sid` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-sid_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Sidamo (sida1246)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/sida1246)
2. <a id="src-sid_wikipedia"></a>Wikipedia contributors (2024). *Sidamo language*. Wikipedia.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `sid` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 297 | 0.0622 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 37 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʼ |  | d t tʼ |  |  | k kʼ ɡ | ʔ |
| Affricate |  |  |  | dʒ tʃ tʃʼ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f | s z | ʃ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w] [ɗ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [tʃʼ] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dh⟩ | [ɗ] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʼ] |  |
| ⟨q⟩ | [kʼ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [tʼ] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ʼ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sid")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Sicilian](scn.md) · [Home](../index.md) · [Silesian →](szl.md)
