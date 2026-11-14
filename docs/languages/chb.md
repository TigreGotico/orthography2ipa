# Chibcha (`chb`)

<!-- atlas:summary begin -->
Chibcha is a Chibchan language, written in the Latin script. Glottolog places it in the North America and South America macroareas. The `chb` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `chb` |
| ISO 639-3 | [chb](https://iso639-3.sil.org/code/chb), Chibcha |
| Wikipedia | [Chibcha language](https://en.wikipedia.org/wiki/Chibcha_language) |
| Family | [Chibchan](by-family.md#chibchan) |
| Region | [North America](by-region.md#several-macroareas), [South America](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Chibchan](https://tigregotico.github.io/orthography2ipa/#x-clade-chib1249) `x-clade-chib1249` |
| Explorer | [`chb` in the data explorer](https://tigregotico.github.io/orthography2ipa/#chb) |
| Spec file | [`chb.json`](../../orthography2ipa/data/chb.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Chibchan language (Muisca) of the Colombian highlands, extinct since the late 18th century. There is no living pronunciation, phonemic values are RECONSTRUCTED from the colonial Spanish-based orthography of de Lugo (1619) and later grammars, following Constenla (1984) and Gonzalez de Perez (2006).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1984 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 22 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/chb.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `chb` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-chb_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Chibcha (chib1270)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/chib1270)
2. <a id="src-chb_wikipedia"></a>Wikipedia contributors (2024). *Chibcha language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Chibcha_language)
3. <a id="src-constenla1984"></a>Constenla Umaña, Adolfo (1984). *Los fonemas del muisca*. Estudios de Lingüística Chibcha 2, 65-111. Cited: 65-111.
4. <a id="src-gonzalezdeperez2006"></a>González de Pérez, María Stella (2006). *Aproximación al sistema fonético-fonológico de la lengua muisca*. Instituto Caro y Cuervo, Bogotá.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `chb` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 99 | 0.1313 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 19 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p | t |  |  | k |  |
| Nasal | m | n |  |  |  |  |
| Fricative | ɸ β | s | ʂ |  | ɣ | h |
| Approximant |  |  |  | j |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid | e |  | o |
| Open | a |  |  |

Sequences that the spec writes as one unit: [tʂ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [β] |  |
| ⟨c⟩ | [k] |  |
| ⟨ch⟩ | [tʂ] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [ɸ] |  |
| ⟨g⟩ | [ɣ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [k] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨x⟩ | [ʂ] |  |
| ⟨y⟩ | [ɨ] |  |
| ⟨z⟩ | [tʂ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "chb")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Cheyenne](chy.md) · [Home](../index.md) · [Chichewa →](ny.md)
