# Maquiritari (`mch`)

<!-- atlas:summary begin -->
Maquiritari is a Cariban language, written in the Latin script. Glottolog places it in the South America macroarea. The `mch` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mch` |
| ISO 639-3 | [mch](https://iso639-3.sil.org/code/mch), Maquiritari |
| Wikipedia | [Ye'kuana language](https://en.wikipedia.org/wiki/Ye%27kuana_language) |
| Family | [Cariban](by-family.md#cariban) |
| Region | [South America](by-region.md#south-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Cariban](https://tigregotico.github.io/orthography2ipa/#x-clade-cari1283) `x-clade-cari1283` |
| Explorer | [`mch` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mch) |
| Spec file | [`mch.json`](../../orthography2ipa/data/mch.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. Cariban language of the Venezuela-Brazil border region, self-named Ye'kwana (also Maquiritari), in the standard orthography used in Venezuela. ch=[tʃ], j=[h], ñ=[ɲ].

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 29 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mch.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mch` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-mch_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Ye'kwana (maqu1238)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/maqu1238)
2. <a id="src-mch_orthography"></a>Wikipedia contributors (2024). *Ye'kuana (Maquiritari) language, Wikipedia*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Ye%27kuana_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `mch` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1746 | 0.1200 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 30 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p | d t |  |  | k | ʔ |
| Affricate |  |  | tʃ |  |  |  |
| Nasal | m | n |  | ɲ |  |  |
| Tap |  | ɾ̠ |  |  |  |  |
| Fricative |  | s | ʃ | ç |  | h |
| Approximant |  |  |  | j |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː | ɨ ɨː | u uː |
| Close-mid | e eː |  | o oː |
| Mid |  | ə əː |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [ɾ̠] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [h] |  |
| ⟨jh⟩ | [ç] |  |
| ⟨k⟩ | [k] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ö⟩ | [ə] |  |
| ⟨öö⟩ | [əː] |  |
| ⟨ü⟩ | [ɨ] |  |
| ⟨üü⟩ | [ɨː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 4 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `MCH_RHOTIC_INITIAL_D` | /ɾ̠/ → [d], word-initially | - | - |
| `MCH_RHOTIC_POST_GLOTTAL_D` | /ɾ̠/ → [d], after [ʔ] | - | - |
| `MCH_GEMINATE_RHOTIC_D_FIRST` | /ɾ̠/ → [d], before [ɾ̠] | - | - |
| `MCH_GEMINATE_RHOTIC_D_SECOND` | /ɾ̠/ → [d], after [ɾ̠] | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mch")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Mapudungun](arn.md) · [Home](../index.md) · [Marathi →](mr.md)
