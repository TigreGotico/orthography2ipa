# Old Tupi (Tupinambá) (`tpn`)

<!-- atlas:summary begin -->
Old Tupi (Tupinambá) is a Tupian language, written in the Latin script. Glottolog places it in Brazil. The `tpn` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `tpn` |
| Aliases | `tpw` |
| ISO 639-3 | [tpn](https://iso639-3.sil.org/code/tpn), Tupinambá |
| Glottolog | [tupi1273](https://glottolog.org/resource/languoid/id/tupi1273), Tupinambá |
| Wikidata | [Q56944](https://www.wikidata.org/wiki/Q56944) |
| Wikipedia | [Old Tupi language](https://en.wikipedia.org/wiki/Old_Tupi_language) |
| Family | [Tupian](by-family.md#tupian) |
| Region | [South America](by-region.md#south-america) > [Brazil](by-region.md#brazil) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Tupian](https://tigregotico.github.io/orthography2ipa/#x-clade-tupi1275) `x-clade-tupi1275` |
| Explorer | [`tpn` in the data explorer](https://tigregotico.github.io/orthography2ipa/#tpn) |
| Spec file | [`tpn.json`](../../orthography2ipa/data/tpn.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Old Tupi (Tupinambá), the língua geral of colonial Brazil, written in the normalised orthography of modern editions. Six oral vowels /a ɛ i ɔ u ɨ/ and their nasal counterparts, stops /p t k ʔ/, fricatives /β s ʃ h/, nasals /m n ŋ ɲ/, tap /ɾ/, the velar fricative /ɣ/ and the semivowels /j w ɨ̯/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1956 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 38 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/tpn.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `tpn` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-navarro2013"></a>Navarro, E. de A. (2013). *Dicionário de tupi antigo: a língua indígena clássica do Brasil*. Global Editora.
2. <a id="src-barbosa1956"></a>Barbosa, A. Lemos (1956). *Curso de tupi antigo*. Livraria São José.
3. <a id="src-rodrigues1985"></a>Rodrigues, A. D. (1985). *Evidence for Tupi-Carib Relationships*. University of Texas Press.
4. <a id="src-wikipedia_tpw_phonology"></a>Wikipedia contributors (2026). *Old Tupi language, Phonology*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Old_Tupi_language)
5. <a id="src-wiktionary_tpw_pron"></a>Wiktionary contributors (2026). *Appendix:Old Tupi pronunciation*. Wikimedia Foundation. [en.wiktionary.org](https://en.wiktionary.org/wiki/Appendix:Old_Tupi_pronunciation)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `tpn` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 372 | 0.0951 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 37 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p | t ⁿd |  |  | k ɡ | ʔ |
| Nasal | m | n |  | ɲ | ŋ |  |
| Tap |  | ɾ |  |  |  |  |
| Fricative | β | s | ʃ |  | ɣ | h |
| Approximant |  |  |  | j |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i ĩ | ɨ ɨ̃ ɨ̯ | u ũ |
| Close-mid | e ẽ |  | o õ |
| Open-mid | ɛ ɛ̃ |  | ɔ ɔ̃ |
| Open | a ã |  |  |

Sequences that the spec writes as one unit: [w] [ɡw] [ᵐb].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [β] |  |
| ⟨e⟩ | [ɛ] [e] |  |
| ⟨g⟩ | [ɣ] [ɡ] |  |
| ⟨gû⟩ | [ɡw] [w] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [ᵐb] [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [ⁿd] [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nh⟩ | [ɲ] [j] |  |
| ⟨o⟩ | [ɔ] [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨x⟩ | [ʃ] |  |
| ⟨y⟩ | [ɨ] |  |
| ⟨á⟩ | [a] |  |
| ⟨ã⟩ | [ã] |  |
| ⟨é⟩ | [ɛ] [e] |  |
| ⟨í⟩ | [i] |  |
| ⟨î⟩ | [j] |  |
| ⟨ó⟩ | [ɔ] [o] |  |
| ⟨õ⟩ | [ɔ̃] [õ] |  |
| ⟨ú⟩ | [u] |  |
| ⟨û⟩ | [w] |  |
| ⟨ý⟩ | [ɨ] |  |
| ⟨ĩ⟩ | [ĩ] |  |
| ⟨ũ⟩ | [ũ] |  |
| ⟨ŷ⟩ | [ɨ̯] |  |
| ⟨ẽ⟩ | [ɛ̃] [ẽ] |  |
| ⟨ỹ⟩ | [ɨ̃] |  |

Stress falls on the last syllable by default. A written ⟨á⟩ ⟨é⟩ ⟨í⟩ ⟨ó⟩ ⟨ú⟩ ⟨ý⟩ marks the stressed vowel.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 6 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `nasal-harmony-a` | /a/ → [ã], before [ᵐb] [ⁿd] [m] [n] [ŋ] [ɲ] | - | - |
| `nasal-harmony-ɛ` | /ɛ/ → [ɛ̃], before [ᵐb] [ⁿd] [m] [n] [ŋ] [ɲ] | - | - |
| `nasal-harmony-i` | /i/ → [ĩ], before [ᵐb] [ⁿd] [m] [n] [ŋ] [ɲ] | - | - |
| `nasal-harmony-ɔ` | /ɔ/ → [ɔ̃], before [ᵐb] [ⁿd] [m] [n] [ŋ] [ɲ] | - | - |
| `nasal-harmony-u` | /u/ → [ũ], before [ᵐb] [ⁿd] [m] [n] [ŋ] [ɲ] | - | - |
| `nasal-harmony-ɨ` | /ɨ/ → [ɨ̃], before [ᵐb] [ⁿd] [m] [n] [ŋ] [ɲ] | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "tpn")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Ojibwe](oji.md) · [Home](../index.md) · [Omani Arabic →](acx-OM.md)
