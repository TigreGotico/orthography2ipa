# Gawwada (`gwd`)

<!-- atlas:summary begin -->
Gawwada is an Afro-Asiatic language, written in the Latin script. Glottolog places it in Ethiopia. The `gwd` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `gwd` |
| ISO 639-3 | [gwd](https://iso639-3.sil.org/code/gwd), Gawwada |
| Glottolog | [gaww1239](https://glottolog.org/resource/languoid/id/gaww1239), Ale-Gawwada |
| Wikipedia | [Gawwada language](https://en.wikipedia.org/wiki/Gawwada_language) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) |
| Region | [Africa](by-region.md#africa) > [Ethiopia](by-region.md#ethiopia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Afro-Asiatic](https://tigregotico.github.io/orthography2ipa/#x-clade-afro1255) `x-clade-afro1255` |
| Explorer | [`gwd` in the data explorer](https://tigregotico.github.io/orthography2ipa/#gwd) |
| Spec file | [`gwd.json`](../../orthography2ipa/data/gwd.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Placed so the ancestry graph covers every living ISO 639-3 language. Classification and coordinates follow Glottolog.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2021 to 2026. [Sources](#sources) lists them. The spec file writes all 33 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/gwd.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `gwd` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-glottolog2024"></a>Hammarström, Harald, Forkel, Robert, Haspelmath, Martin, Bank, Sebastian (2024). *Glottolog 5.0*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/)
2. <a id="src-omniglot-gawwada"></a>Ager, Simon (2026). *Omniglot chart (gawwada.xls)*. Omniglot. [omniglot.com](https://www.omniglot.com/)
3. <a id="src-gwd_tosco"></a>Tosco, Mauro (2021). *A Grammar of Gawwada*. Rüdiger Köppe Verlag (Cushitic and Omotic Studies 8). [koeppe.de](https://www.koeppe.de/titel_print_a-grammar-of-gawwada)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wold` ([lexibank/wold](https://github.com/lexibank/wold)) | `gwd` | gold | lexicon-derived | CC BY 4.0 | 976 | 0.0385 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 33 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p |  | t tʼ |  |  | k kʼ | q |  | ʔ |
| Nasal | m |  | n |  | ɲ |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Fricative |  | f | s | ʃ |  |  |  | ʕ | h ɦ |
| Approximant |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w] [ɓ] [ɗ] [ɠ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨f⟩ | [f] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨k⟩ | [k] |  |
| ⟨k’⟩ | [kʼ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [q] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨t’⟩ | [tʼ] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ɓ⟩ | [ɓ] |  |
| ⟨ɗ⟩ | [ɗ] |  |
| ⟨ɠ⟩ | [ɠ] |  |
| ⟨ɦ⟩ | [ɦ] |  |
| ⟨ʔ⟩ | [ʔ] |  |
| ⟨ʕ⟩ | [ʕ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "gwd")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Gawri](gwc.md) · [Home](../index.md) · [Gen →](gej-TG.md)
