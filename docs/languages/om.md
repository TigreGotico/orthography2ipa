# Oromo (`om`)

<!-- atlas:summary begin -->
Oromo is a Cushitic language, written in the Latin script. Glottolog places it in Ethiopia and Sudan. The `om` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `om` |
| ISO 639-3 | [orm](https://iso639-3.sil.org/code/orm), Oromo |
| Glottolog | [west2721](https://glottolog.org/resource/languoid/id/west2721), West Central Oromo |
| Wikidata | [Q33864](https://www.wikidata.org/wiki/Q33864) |
| Wikipedia | [Oromo language](https://en.wikipedia.org/wiki/Oromo_language) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Cushitic](by-family.md#afro-asiatic--cushitic) |
| Region | [Africa](by-region.md#africa) > [Ethiopia](by-region.md#ethiopia), [Sudan](by-region.md#sudan) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1991, living |
| Parent | [Cushitic](https://tigregotico.github.io/orthography2ipa/#x-clade-cush1243) `x-clade-cush1243` |
| Explorer | [`om` in the data explorer](https://tigregotico.github.io/orthography2ipa/#om) |
| Spec file | [`om.json`](../../orthography2ipa/data/om.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Oromo (Afaan Oromoo) in Qubee Latin orthography, official in Ethiopia since 1991. Vowel length is phonemic and written with doubled letters, the short vowels are also laxer and more centralised than their long counterparts, so <a e i o u> are /ɐ ɛ ɪ ɔ ʊ/ against long /ɑː eː iː oː uː/ (Abu et al. 2025, Table I).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1985 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 37 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/om.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `om` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-sagalee2025"></a>Turi Abu and Ying Shi and Thomas Fang Zheng and Dong Wang (2025). *Sagalee: an Open Source Automatic Speech Recognition Dataset for Oromo Language*. ICASSP 2025 (IEEE). [arxiv.org](https://arxiv.org/abs/2502.00421)
2. <a id="src-griefenow_mewis2001"></a>Catherine Griefenow-Mewis (2001). *A Grammatical Sketch of Written Oromo*. Rudiger Koppe.
3. <a id="src-owens1985"></a>Jonathan Owens (1985). *A Grammar of Harar Oromo*. Buske.
4. <a id="src-oromo_wiki"></a>Wikipedia contributors (2024). *Oromo phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Oromo_phonology)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `kaikki` ([kaikki.org](https://kaikki.org/dictionary/)) | `om` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 519 | 0.1026 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 37 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʼ |  | d t tʼ |  |  | k kʼ ɡ | ʔ |
| Affricate |  |  |  | dʒ tʃ tʃʼ |  |  |  |
| Nasal | m |  | n |  | ɲ |  |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː |  | uː |
| Near-close | ɪ |  | ʊ |
| Close-mid | eː |  | oː |
| Open-mid | ɛ |  | ɔ |
| Near-open |  | ɐ |  |
| Open |  |  | ɑː |

Sequences that the spec writes as one unit: [w] [ᶑ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [ɐ] |  |
| ⟨aa⟩ | [ɑː] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [tʃʼ] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dh⟩ | [ᶑ] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ɪ] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʼ] |  |
| ⟨q⟩ | [kʼ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [ʊ] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [tʼ] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "om")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Oneida](one.md) · [Home](../index.md) · [Ossetian →](os.md)
