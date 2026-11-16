# Guaraní (`gn`)

<!-- atlas:summary begin -->
Guaraní is a Tupian language, written in the Latin script. Glottolog places it in Argentina and Paraguay. The `gn` spec is at the research tier. It cites 4 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `gn` |
| ISO 639-3 | [grn](https://iso639-3.sil.org/code/grn), Guarani |
| Glottolog | [para1311](https://glottolog.org/resource/languoid/id/para1311), Paraguayan Guaraní |
| Wikidata | [Q17478066](https://www.wikidata.org/wiki/Q17478066) |
| Wikipedia | [Guarani language](https://en.wikipedia.org/wiki/Guarani_language) |
| Family | [Tupian](by-family.md#tupian) |
| Region | [South America](by-region.md#south-america) > [Argentina](by-region.md#argentina), [Paraguay](by-region.md#paraguay) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Tupian](https://tigregotico.github.io/orthography2ipa/#x-clade-tupi1275) `x-clade-tupi1275` |
| Explorer | [`gn` in the data explorer](https://tigregotico.github.io/orthography2ipa/#gn) |
| Spec file | [`gn.json`](../../orthography2ipa/data/gn.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Paraguayan Guaraní (avañe'ẽ), co-official language of Paraguay, written in the achegety. Six oral vowels /a e i o u ɨ/ and a nasal counterpart for each, written with a tilde ⟨ã ẽ ĩ õ ũ ỹ⟩, ⟨y⟩ is the close central unrounded vowel /ɨ/, not a glide, and the palatal obstruent /dʒ~ʝ/ is written ⟨j⟩.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1997 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 39 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/gn.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `gn` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-cabrera2023"></a>Cabrera Sanchez, Marisabel (2023). *Nasal harmony in Paraguayan Guarani: Positional effects and the representation of nasality*. University of California, Los Angeles (MA thesis). Cited: 11-14. [escholarship.org](https://escholarship.org/content/qt75s541nd/qt75s541nd_noSplash_ad1f65f59d8f1c6f9fb3fb23e2c53275.pdf)
2. <a id="src-wikipedia_gn_alphabet"></a>Wikipedia contributors (2026). *Guarani alphabet*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Guarani_alphabet)
3. <a id="src-wikipedia_gn_phonology"></a>Wikipedia contributors (2026). *Guarani language, Phonology*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Guarani_language)
4. <a id="src-campbell1997"></a>Campbell, Lyle (1997). *American Indian Languages: The Historical Linguistics of Native America*. Oxford University Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `gn` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 347 | 0.1458 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `gn` | generated | epitran-derived | CC0 1.0 | 4264 | 0.1675 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 37 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p |  | t ⁿd ⁿt |  |  |  | k | ʔ |
| Affricate |  |  |  | dʒ |  |  |  |  |
| Nasal | m |  | n |  |  | ɲ | ŋ |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative |  |  | s | ʃ | ʐ | ɕ ʝ | x | h |
| Approximant |  | ʋ |  |  |  |  | ɰ ɰ̃ |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i ĩ | ɨ ɨ̃ | u ũ |
| Close-mid | e ẽ |  | o õ |
| Open | a ã |  |  |

Sequences that the spec writes as one unit: [ᵐb] [ᵑɡ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨ch⟩ | [ʃ] [ɕ] |  |
| ⟨e⟩ | [e] |  |
| ⟨g⟩ | [ɰ] |  |
| ⟨g̃⟩ | [ɰ̃] [ŋ] |  |
| ⟨h⟩ | [h] [x] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] [ʝ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [ᵐb] [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [ⁿd] [n] |  |
| ⟨ng⟩ | [ᵑɡ] [ŋ] |  |
| ⟨nt⟩ | [ⁿt] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨rr⟩ | [ʐ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [ʋ] |  |
| ⟨y⟩ | [ɨ] |  |
| ⟨á⟩ | [a] |  |
| ⟨ã⟩ | [ã] |  |
| ⟨é⟩ | [e] |  |
| ⟨í⟩ | [i] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ó⟩ | [o] |  |
| ⟨õ⟩ | [õ] |  |
| ⟨ú⟩ | [u] |  |
| ⟨ý⟩ | [ɨ] |  |
| ⟨ĩ⟩ | [ĩ] |  |
| ⟨ũ⟩ | [ũ] |  |
| ⟨ẽ⟩ | [ẽ] |  |
| ⟨ỹ⟩ | [ɨ̃] |  |

Stress falls on the last syllable by default. A written ⟨á⟩ ⟨é⟩ ⟨í⟩ ⟨ó⟩ ⟨ú⟩ ⟨ý⟩ marks the stressed vowel.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "gn")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Guadramilese](ast-PT-x-guadrami.md) · [Home](../index.md) · [Gujarati →](gu.md)
