# Isthmus-Mecayapan Nahuatl (`nhx`)

<!-- atlas:summary begin -->
Isthmus-Mecayapan Nahuatl is an Uto-Aztecan language, written in the Latin script. Glottolog places it in the North America macroarea. The `nhx` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `nhx` |
| ISO 639-3 | [nhx](https://iso639-3.sil.org/code/nhx), Isthmus-Mecayapan Nahuatl |
| Wikipedia | [Isthmus Nahuatl](https://en.wikipedia.org/wiki/Isthmus_Nahuatl) |
| Family | [Uto-Aztecan](by-family.md#uto-aztecan) |
| Region | [North America](by-region.md#north-america) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Nahuatl](https://tigregotico.github.io/orthography2ipa/#nah) `nah` |
| Explorer | [`nhx` in the data explorer](https://tigregotico.github.io/orthography2ipa/#nhx) |
| Spec file | [`nhx.json`](../../orthography2ipa/data/nhx.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. Uto-Aztecan (Nahuan) variety of the Isthmus of Veracruz written in an SIL-based practical orthography. Digraphs ch=[tʃ], ts=[ts], cu/qu for [kʷ]/[k], hu=[w] and x=[ʃ], j=[h] are mapped, this variety merged the historic tl to [t]. Voiced stops b d g occur as allophones of the voiceless series in some contexts.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2002 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 26 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/nhx.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `nhx` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-nhx_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Isthmus-Mecayapan Nahuatl (isth1242)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/isth1242)
2. <a id="src-nhx_orthography"></a>Wikipedia contributors (2024). *Mecayapan Nahuatl (Isthmus-Mecayapan), Wikipedia*. Wikimedia Foundation. [en.wikipedia.org](https://en.wikipedia.org/wiki/Isthmus_Nahuatl)
3. <a id="src-nhx_wolgemuth2002"></a>Wolgemuth, Carl (2002). *Gramática náhuatl (melaꞌtájto̱l) de los municipios de Mecayapan y Tatahuicapan de Juárez, Veracruz*. Instituto Lingüístico de Verano (SIL Mexico). [mexico.sil.org](https://mexico.sil.org/resources/archives/1919)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `nhx` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 145 | 0.1852 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 22 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d t |  |  | k kʷ ɡ | ʔ |
| Affricate |  | ts | tʃ |  |  |  |
| Nasal | m | n |  |  |  |  |
| Fricative |  | s | ʃ |  |  | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i |  |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨cu⟩ | [kʷ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨hu⟩ | [w] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [h] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨qu⟩ | [k] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ʃ] |  |
| ⟨y⟩ | [j] |  |
| ⟨ʼ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "nhx")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Irish](ga.md) · [Home](../index.md) · [Italian →](it-IT.md)
