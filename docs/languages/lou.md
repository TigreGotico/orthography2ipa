# Louisiana Creole (`lou`)

<!-- atlas:summary begin -->
Louisiana Creole is a Romance language, written in the Latin script. Glottolog places it in the Africa, Eurasia, North America, Papunesia and South America macroareas. The `lou` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lou` |
| ISO 639-3 | [lou](https://iso639-3.sil.org/code/lou), Louisiana Creole |
| Wikipedia | [Louisiana Creole](https://en.wikipedia.org/wiki/Louisiana_Creole) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance](by-family.md#indo-european--italic--romance) |
| Region | [Africa](by-region.md#several-macroareas), [Eurasia](by-region.md#several-macroareas), [North America](by-region.md#several-macroareas), [Papunesia](by-region.md#several-macroareas), [South America](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Romance](https://tigregotico.github.io/orthography2ipa/#x-clade-roma1334) `x-clade-roma1334` |
| Explorer | [`lou` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lou) |
| Spec file | [`lou.json`](../../orthography2ipa/data/lou.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Skeleton. French-lexifier creole of Louisiana written in a Latin, French-based spelling. Grapheme map follows French conventions adapted to the creole: ou [u], ch [ʃ], j [ʒ], gn [ɲ], the nasal-vowel digraphs an/en [ã], on [ɔ̃], in [ɛ̃], and accented è/é.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2003 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 36 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/lou.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `lou` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-lou_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Louisiana Creole French (loui1240)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/loui1240)
2. <a id="src-lou_wikipedia"></a>Wikipedia contributors (2024). *Louisiana Creole (Wikipedia)*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Louisiana_Creole)
3. <a id="src-lou_klingler2003"></a>Klingler, Thomas A. (2003). *If I Could Turn My Tongue like That: The Creole Language of Pointe Coupee Parish, Louisiana*. Louisiana State University Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `lou` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 262 | 0.1953 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 31 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |  |
| Nasal | m |  | n |  | ɲ |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | ʁ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u |
| Close-mid | e | o |
| Open-mid | ɛ ɛ̃ | ɔ ɔ̃ |
| Open | a ã |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨an⟩ | [ã] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] |  |
| ⟨ch⟩ | [ʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨en⟩ | [ã] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gn⟩ | [ɲ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨in⟩ | [ɛ̃] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨on⟩ | [ɔ̃] |  |
| ⟨ou⟩ | [u] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨r⟩ | [ʁ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [y] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨â⟩ | [a] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [e] |  |
| ⟨ò⟩ | [ɔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lou")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Lombard](lmo-x-milanese.md) · [Home](../index.md) · [Low German →](nds.md)
