# Pitjantjatjara (`pjt`)

<!-- atlas:summary begin -->
Pitjantjatjara is a Pama-Nyungan language, written in the Latin script. Glottolog places it in the Australia and Papunesia macroareas. The `pjt` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `pjt` |
| ISO 639-3 | [pjt](https://iso639-3.sil.org/code/pjt), Pitjantjatjara |
| Wikipedia | [Pitjantjatjara dialect](https://en.wikipedia.org/wiki/Pitjantjatjara_dialect) |
| Family | [Pama-Nyungan](by-family.md#pama-nyungan) |
| Region | [Australia](by-region.md#several-macroareas), [Papunesia](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Pama-Nyungan](https://tigregotico.github.io/orthography2ipa/#x-clade-pama1250) `x-clade-pama1250` |
| Explorer | [`pjt` in the data explorer](https://tigregotico.github.io/orthography2ipa/#pjt) |
| Spec file | [`pjt.json`](../../orthography2ipa/data/pjt.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Pama-Nyungan (Wati) language of Central Australia, with a well-established standard orthography. Retroflex consonants are written with an underline (ṯ ṉ ḻ ṟ), the common ASCII substitutions rt/rn/rl are also mapped to the same retroflex values.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 26 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/pjt.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `pjt` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-pjt_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Pitjantjatjara (pitj1243)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/pitj1243)
2. <a id="src-pjt_wikipedia"></a>Wikipedia contributors (2024). *Pitjantjatjara dialect*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Pitjantjatjara_dialect)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `pjt` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 125 | 0.0027 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 23 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Retroflex | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | p | t | ʈ | c | k |
| Nasal | m | n | ɳ | ɲ | ŋ |
| Trill |  | r |  |  |  |
| Approximant |  |  | ɻ | j |  |
| Lateral approximant |  | l | ɭ | ʎ |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Near-close | ɪ ɪː |  | ʊ ʊː |
| Near-open |  | ɐ ɐː |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɐ] |  |
| ⟨aa⟩ | [ɐː] |  |
| ⟨i⟩ | [ɪ] |  |
| ⟨ii⟩ | [ɪː] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ly⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨rl⟩ | [ɭ] |  |
| ⟨rn⟩ | [ɳ] |  |
| ⟨rt⟩ | [ʈ] |  |
| ⟨t⟩ | [t] |  |
| ⟨tj⟩ | [c] |  |
| ⟨u⟩ | [ʊ] |  |
| ⟨uu⟩ | [ʊː] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ḻ⟩ | [ɭ] |  |
| ⟨ṉ⟩ | [ɳ] |  |
| ⟨ṟ⟩ | [ɻ] |  |
| ⟨ṯ⟩ | [ʈ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "pjt")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Pijin](pis.md) · [Home](../index.md) · [Plains Cree →](crk.md)
