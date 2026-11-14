# Ojibwe (`oji`)

<!-- atlas:summary begin -->
Ojibwe is an Algic language, written in the Latin script. Glottolog places it in the North America macroarea. The `oji` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `oji` |
| ISO 639-3 | [oji](https://iso639-3.sil.org/code/oji), Ojibwa |
| Glottolog | [ojib1241](https://glottolog.org/resource/languoid/id/ojib1241), Ojibwa |
| Wikidata | [Q33875](https://www.wikidata.org/wiki/Q33875) |
| Wikipedia | [Ojibwe language](https://en.wikipedia.org/wiki/Ojibwe_language) |
| Family | [Algic](by-family.md#algic) |
| Region | [North America](by-region.md#north-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Algic](https://tigregotico.github.io/orthography2ipa/#x-clade-algi1248) `x-clade-algi1248` |
| Explorer | [`oji` in the data explorer](https://tigregotico.github.io/orthography2ipa/#oji) |
| Spec file | [`oji.json`](../../orthography2ipa/data/oji.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Ojibwe (Anishinaabemowin), Algonquian. PRIMARY INPUT CONTRACT: the double-vowel (Fiero) Latin orthography, the standard teaching/reference system (Nichols & Nyholm 1995, Valentine 2001), NFC.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1995 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 27 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/oji.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `oji` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-ojibwe_wiki"></a>Wikipedia contributors (2026). *Ojibwe language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Ojibwe_language)
2. <a id="src-nichols_nyholm1995"></a>Nichols, John D. & Nyholm, Earl (1995). *A Concise Dictionary of Minnesota Ojibwe*. University of Minnesota Press.
3. <a id="src-valentine2001"></a>Valentine, J. Randolph (2001). *Nishnaabemwin Reference Grammar*. University of Toronto Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `oji` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 136 | 0.2973 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 36 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ | d t tʰ |  |  | k kʰ ɡ | ʔ |
| Affricate |  |  | dʒ tʃ tʃʰ |  |  |  |
| Nasal | m | n |  |  |  |  |
| Fricative |  | s sʰ z | ʃ ʃʰ ʒ |  |  | h |
| Approximant |  |  |  | j |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  |  |
| Near-close | ɪ |  | ʊ |
| Close-mid | eː |  | o oː |
| Mid |  | ə |  |
| Open-mid |  |  | ʌ |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [w] [ŋɡ].
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
| ⟨ch⟩ | [tʃʰ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [eː] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [kʰ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋɡ] |  |
| ⟨o⟩ | [o] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [pʰ] |  |
| ⟨s⟩ | [sʰ] |  |
| ⟨sh⟩ | [ʃʰ] |  |
| ⟨t⟩ | [tʰ] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨zh⟩ | [ʒ] |  |
| ⟨ʼ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "oji")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Odia](or.md) · [Home](../index.md) · [Old Tupi →](tpn.md)
