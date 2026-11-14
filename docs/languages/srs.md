# Sarsi (`srs`)

<!-- atlas:summary begin -->
Sarsi is an Athabaskan-Eyak-Tlingit language, written in the Latin script. Glottolog places it in the North America macroarea. The `srs` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `srs` |
| ISO 639-3 | [srs](https://iso639-3.sil.org/code/srs), Tsuut'ina |
| Wikipedia | [Tsuutʼina language](https://en.wikipedia.org/wiki/Tsuut%CA%BCina_language) |
| Family | [Athabaskan-Eyak-Tlingit](by-family.md#athabaskan-eyak-tlingit) |
| Region | [North America](by-region.md#north-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Athabaskan-Eyak-Tlingit](https://tigregotico.github.io/orthography2ipa/#x-clade-atha1245) `x-clade-atha1245` |
| Explorer | [`srs` in the data explorer](https://tigregotico.github.io/orthography2ipa/#srs) |
| Spec file | [`srs.json`](../../orthography2ipa/data/srs.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Northern Athabaskan (Dene) language of Alberta, self-named Tsuutʼina, in its practical orthography. Lateral obstruents (tł, tł', ł=[ɬ]), affricate series and ejectives written with a following apostrophe, and gh=[ɣ] are mapped. Grapheme table checked against Cook (1984): no discrepancy found.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1984 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 42 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/srs.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `srs` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-srs_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Sarsi (sars1236)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/sars1236)
2. <a id="src-cook1984"></a>Cook, Eung-Do (1984). *A Sarcee Grammar*. UBC Press, Vancouver.
3. <a id="src-srs_orthography"></a>Wikipedia contributors (2024). *Tsuutʼina language (Sarsi), Wikipedia*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Tsuut%CA%BCina_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `srs` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 137 | 0.1765 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 36 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d t tʼ |  |  | k kʷ kʼ ɡ | ʔ |
| Affricate |  | dz ts tsʼ tɬ tɬʼ | dʒ tʃ tʃʼ |  |  |  |
| Nasal | m | n |  |  |  |  |
| Fricative |  | s z | ʃ ʒ |  | x ɣ | h |
| Lateral fricative |  | ɬ |  |  |  |  |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid |  | o |
| Open | a |  |

Sequences that the spec writes as one unit: [dl] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨ch'⟩ | [tʃʼ] |  |
| ⟨chʼ⟩ | [tʃʼ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dl⟩ | [dl] |  |
| ⟨dz⟩ | [dz] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gh⟩ | [ɣ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨k'⟩ | [kʼ] |  |
| ⟨kw⟩ | [kʷ] |  |
| ⟨kʼ⟩ | [kʼ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨t'⟩ | [tʼ] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨ts'⟩ | [tsʼ] |  |
| ⟨tsʼ⟩ | [tsʼ] |  |
| ⟨tł⟩ | [tɬ] |  |
| ⟨tł'⟩ | [tɬʼ] |  |
| ⟨tłʼ⟩ | [tɬʼ] |  |
| ⟨tʼ⟩ | [tʼ] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨zh⟩ | [ʒ] |  |
| ⟨ł⟩ | [ɬ] |  |
| ⟨ʼ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "srs")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Sardinian](sc.md) · [Home](../index.md) · [Sasak →](sas.md)
