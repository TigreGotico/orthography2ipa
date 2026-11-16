# Morisyen (`mfe`)

<!-- atlas:summary begin -->
Morisyen is a Romance language, written in the Latin script. Glottolog places it in the Africa, Eurasia, North America, Papunesia and South America macroareas. The `mfe` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mfe` |
| ISO 639-3 | [mfe](https://iso639-3.sil.org/code/mfe), Morisyen |
| Wikipedia | [Mauritian Creole](https://en.wikipedia.org/wiki/Mauritian_Creole) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance](by-family.md#indo-european--italic--romance) |
| Region | [Africa](by-region.md#several-macroareas), [Eurasia](by-region.md#several-macroareas), [North America](by-region.md#several-macroareas), [Papunesia](by-region.md#several-macroareas), [South America](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Romance](https://tigregotico.github.io/orthography2ipa/#x-clade-roma1334) `x-clade-roma1334` |
| Explorer | [`mfe` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mfe) |
| Spec file | [`mfe.json`](../../orthography2ipa/data/mfe.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> French-lexifier creole of Mauritius written in a Latin, largely phonemic orthography. Grapheme map follows the modern conventions: ou [u], ch [ʃ], j [ʒ], z [z], gn [ɲ], ng [ŋ].

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2013 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 30 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mfe.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mfe` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-mfe_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Morisyen (mori1278)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/mori1278)
2. <a id="src-mfe_wikipedia"></a>Wikipedia contributors (2024). *Mauritian Creole (Wikipedia)*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Mauritian_Creole)
3. <a id="src-baker_kriegel_apics_morisyen"></a>Baker, Philip and Kriegel, Sibylle (2013). *Morisyen structure dataset*. Atlas of Pidgin and Creole Language Structures (APiCS) Online. [apics-online.info](https://apics-online.info/contributions/60)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `mfe` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 206 | 0.1238 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 38 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | ʁ | h |
| Approximant |  |  |  |  | j | ɰ |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː y yː | u |
| Close-mid | e eː | o oː |
| Open-mid | ɛ ɛː ɛ̃ | ɔ̃ |
| Open | a aː | ɑ̃ |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [ʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gn⟩ | [ɲ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nn⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨ou⟩ | [u] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ʁ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [y] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [e] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 13 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `MFE_R_ONSET` | /ʁ/ → [ɰ], in the onset | ⟨frer⟩ [fɰɛː] | - |
| `MFE_R_CODA_DELETE` | /ʁ/ → ∅, in the coda | ⟨ser⟩ [sɛː] | - |
| `MFE_LENGTHEN_A` | /a/ → [aː], before a coda, before [ʁ] | - | - |
| `MFE_LENGTHEN_E` | /e/ → [eː], before a coda, before [ʁ] | - | - |
| `MFE_LENGTHEN_I` | /i/ → [iː], before a coda, before [ʁ] | - | - |
| `MFE_LENGTHEN_O` | /o/ → [oː], before a coda, before [ʁ] | - | - |
| `MFE_LENGTHEN_Y` | /y/ → [yː], before a coda, before [ʁ] | - | - |
| `MFE_LENGTHEN_Ɛ` | /ɛ/ → [ɛː], before a coda, before [ʁ] | ⟨ser⟩ [sɛː] | - |
| `MFE_NASAL_A` | /a/ → [ɑ̃], before a coda nasal | ⟨gran⟩ [ɡɰɑ̃] | Baker & Hookoomsing 1987 |
| `MFE_NASAL_O` | /o/ → [ɔ̃], before a coda nasal | ⟨non⟩ [nɔ̃] | Baker & Hookoomsing 1987 |
| `MFE_NASAL_E` | /e/ → [ɛ̃], before a coda nasal | ⟨morisien⟩ [moʁisjɛ̃] | Baker & Hookoomsing 1987 |
| `MFE_NASAL_I` | /i/ → [ɛ̃], before a coda nasal | ⟨morisien⟩ [moʁisjɛ̃] | Baker & Hookoomsing 1987 |
| `MFE_NASAL_ABSORB` | /n/ → ∅, in the coda, after a vowel | ⟨kontan⟩ [kɔ̃tɑ̃] | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mfe")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Mooré](mos.md) · [Home](../index.md) · [Moroccan Arabic →](ary-MA.md)
