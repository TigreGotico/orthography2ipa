# Hawaiian (`haw`)

<!-- atlas:summary begin -->
Hawaiian is a Malayo-Polynesian language, written in the Latin script. Glottolog places it in United States. The `haw` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `haw` |
| ISO 639-3 | [haw](https://iso639-3.sil.org/code/haw), Hawaiian |
| Glottolog | [hawa1245](https://glottolog.org/resource/languoid/id/hawa1245), Hawaiian |
| Wikipedia | [Hawaiian language](https://en.wikipedia.org/wiki/Hawaiian_language) |
| Family | [Austronesian](by-family.md#austronesian) > [Malayo-Polynesian](by-family.md#austronesian--malayo-polynesian) |
| Region | [Papunesia](by-region.md#papunesia) > [United States](by-region.md#united-states) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1826, living |
| Parent | [Malayo-Polynesian](https://tigregotico.github.io/orthography2ipa/#x-clade-mala1545) `x-clade-mala1545` |
| Explorer | [`haw` in the data explorer](https://tigregotico.github.io/orthography2ipa/#haw) |
| Spec file | [`haw.json`](../../orthography2ipa/data/haw.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Hawaiian (ʻŌlelo Hawaiʻi), Polynesian. The alphabet (pīʻāpā) has 13 letters: five vowels a e i o u, eight consonants h k l m n p w and the ʻokina ⟨ʻ⟩ = glottal stop /ʔ/, which is a full consonant. The kahakō (macron: ā ē ī ō ū) marks a long vowel. The orthography is essentially one-to-one phonemic.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1979 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 18 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/haw.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `haw` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-elbert_pukui1979"></a>Elbert, Samuel H. & Pukui, Mary Kawena (1979). *Hawaiian Grammar*. University of Hawaii Press.
2. <a id="src-hawaiian_language_wiki"></a>Wikipedia contributors (2026). *Hawaiian language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Hawaiian_language)
3. <a id="src-hawaiian_phonology_wiki"></a>Wikipedia contributors (2026). *Hawaiian phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Hawaiian_phonology)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `haw` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2145 | 0.0127 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 20 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | p |  | t | k | ʔ |
| Nasal | m |  | n |  |  |
| Fricative |  | v |  |  | h |
| Lateral approximant |  |  | l |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨e⟩ | [e] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨ā⟩ | [aː] |  |
| ⟨ē⟩ | [eː] |  |
| ⟨ī⟩ | [iː] |  |
| ⟨ō⟩ | [oː] |  |
| ⟨ū⟩ | [uː] |  |
| ⟨ʻ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "haw")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Hausa](ha.md) · [Home](../index.md) · [Hebrew →](he.md)
