# Classical Nahuatl (`nci`)

<!-- atlas:summary begin -->
Classical Nahuatl is an Uto-Aztecan language, written in the Latin script. Glottolog places it in Mexico. The `nci` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `nci` |
| ISO 639-3 | [nci](https://iso639-3.sil.org/code/nci), Classical Nahuatl |
| Glottolog | [clas1250](https://glottolog.org/resource/languoid/id/clas1250), Classical Nahuatl |
| Wikidata | [Q2704940](https://www.wikidata.org/wiki/Q2704940) |
| Wikipedia | [Classical Nahuatl](https://en.wikipedia.org/wiki/Classical_Nahuatl) |
| Family | [Uto-Aztecan](by-family.md#uto-aztecan) |
| Region | [North America](by-region.md#north-america) > [Mexico](by-region.md#mexico) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Uto-Aztecan](https://tigregotico.github.io/orthography2ipa/#x-clade-utoa1244) `x-clade-utoa1244` |
| Explorer | [`nci` in the data explorer](https://tigregotico.github.io/orthography2ipa/#nci) |
| Spec file | [`nci.json`](../../orthography2ipa/data/nci.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Classical Nahuatl (Nāhuatlahtōlli), the Uto-Aztecan (Nahuan) literary language of the Aztec empire and colonial central Mexico, recorded in the traditional Hispanic-based ('Jesuit') orthography.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 2003 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes no spelling of its own. It takes all 30 from [Central Nahuatl](nhn.md) `nhn`.

The [spec file](../../orthography2ipa/data/nci.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `nci` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-andrews2003"></a>Andrews, J. Richard (2003). *Introduction to Classical Nahuatl (Revised Edition)*. University of Oklahoma Press.
2. <a id="src-classical_nahuatl_wikipedia"></a>Wikipedia contributors (2026). *Classical Nahuatl, Phonology and Orthography*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Classical_Nahuatl)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `nci` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 839 | 0.1198 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 29 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k kʷ ɡ | ʔ |
| Affricate |  |  | t͡s t͡ɬ | t͡ʃ |  |  |  |
| Nasal | m |  | n |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative | ɸ | f | s | ʃ |  |  | h |
| Lateral fricative |  |  | ɬ |  |  |  |  |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l lː |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] | before front vowel [s] · default [k] |
| ⟨ch⟩ | [t͡ʃ] |  |
| ⟨cu⟩ | [kʷ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [ʔ] |  |
| ⟨hu⟩ | [w] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [lː] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨qu⟩ | [k] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tl⟩ | [t͡ɬ] |  |
| ⟨tz⟩ | [t͡s] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ʃ] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [s] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "nci")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Chuvash](cv.md) · [Home](../index.md) · [Classical Syriac →](syc.md)
