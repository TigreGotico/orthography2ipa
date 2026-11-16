# Cusco Quechua (`quz`)

<!-- atlas:summary begin -->
Cusco Quechua is a Quechuan language, written in the Latin script. Glottolog places it in Peru. The `quz` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `quz` |
| ISO 639-3 | [quz](https://iso639-3.sil.org/code/quz), Cusco Quechua |
| Glottolog | [cusc1236](https://glottolog.org/resource/languoid/id/cusc1236), Cusco Quechua |
| Wikidata | [Q35147](https://www.wikidata.org/wiki/Q35147) |
| Wikipedia | [Cusco Quechua](https://en.wikipedia.org/wiki/Cusco_Quechua) |
| Family | [Quechuan](by-family.md#quechuan) |
| Region | [South America](by-region.md#south-america) > [Peru](by-region.md#peru) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Quechua](https://tigregotico.github.io/orthography2ipa/#qu) `qu` |
| Explorer | [`quz` in the data explorer](https://tigregotico.github.io/orthography2ipa/#quz) |
| Spec file | [`quz.json`](../../orthography2ipa/data/quz.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Cusco Quechua (Qusqu-Qullaw), the Southern Quechua variety of the Cusco region, Peru.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1976 to 2025. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 33 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/quz.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `quz` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-cusco_quechua_wiki"></a>Wikipedia contributors (2025). *Cusco Quechua*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Cusco_Quechua)
2. <a id="src-southern_quechua_wiki"></a>Wikipedia contributors (2025). *Southern Quechua*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Southern_Quechua)
3. <a id="src-cusihuaman_1976"></a>Cusihuamán, Antonio (1976). *Gramática Quechua Cuzco-Collao*. Ministerio de Educación / Instituto de Estudios Peruanos.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `quz` | generated | espeak-derived | CC BY 4.0 | 1853 | 0.3549 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 36 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ pʼ |  | d t tʰ tʼ |  |  | k kʰ kʼ ɡ | q qʰ qʼ |  |
| Affricate |  |  |  | tʃ tʃʰ tʃʼ |  |  |  |  |
| Nasal | m |  | n |  | ɲ |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative |  | f | s | ʃ |  |  |  | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  | ʎ |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Open-mid | ɛ | ɔ |
| Open | a | ɑ |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨ch'⟩ | [tʃʼ] |  |
| ⟨chh⟩ | [tʃʰ] |  |
| ⟨d⟩ | [d] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨k'⟩ | [kʼ] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨p⟩ | [p] |  |
| ⟨p'⟩ | [pʼ] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨q⟩ | [q] |  |
| ⟨q'⟩ | [qʼ] |  |
| ⟨qh⟩ | [qʰ] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨t'⟩ | [tʼ] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ñ⟩ | [ɲ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 6 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `QUZ_UVULAR_LOWER_A` | /a/ → [ɑ], before [q] [qʰ] [qʼ] | - | - |
| `QUZ_UVULAR_LOWER_A_AFTER` | /a/ → [ɑ], after [q] [qʰ] [qʼ] | - | - |
| `QUZ_UVULAR_LOWER_I` | /i/ → [ɛ], before [q] [qʰ] [qʼ] | - | - |
| `QUZ_UVULAR_LOWER_I_AFTER` | /i/ → [ɛ], after [q] [qʰ] [qʼ] | - | - |
| `QUZ_UVULAR_LOWER_U` | /u/ → [ɔ], before [q] [qʰ] [qʼ] | - | - |
| `QUZ_UVULAR_LOWER_U_AFTER` | /u/ → [ɔ], after [q] [qʰ] [qʼ] | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "quz")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Cuban Spanish](es-CU.md) · [Home](../index.md) · [Cypriot Greek →](el-CY.md)
