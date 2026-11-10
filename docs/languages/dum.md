# Middle Dutch (ca. 1050-1350) (`dum`)

<!-- atlas:summary begin -->
Middle Dutch (ca. 1050-1350) is a West Germanic language, written in the Latin script. Glottolog places it in the Africa, Australia, Eurasia, North America, Papunesia and South America macroareas. The `dum` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `dum` |
| ISO 639-3 | [dum](https://iso639-3.sil.org/code/dum), Middle Dutch (ca. 1050-1350) |
| Wikipedia | [Middle Dutch](https://en.wikipedia.org/wiki/Middle_Dutch) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > West Germanic](by-family.md#indo-european--germanic--northwest-germanic--west-germanic) |
| Region | [Africa](by-region.md#several-macroareas), [Australia](by-region.md#several-macroareas), [Eurasia](by-region.md#several-macroareas), [North America](by-region.md#several-macroareas), [Papunesia](by-region.md#several-macroareas), [South America](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [West Germanic](https://tigregotico.github.io/orthography2ipa/#x-clade-west2793) `x-clade-west2793` |
| Explorer | [`dum` in the data explorer](https://tigregotico.github.io/orthography2ipa/#dum) |
| Spec file | [`dum.json`](../../orthography2ipa/data/dum.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. West Germanic (Low Franconian) medieval stage written in the Latin alphabet. Grapheme map covers the monophthong letters, the digraph long vowels (ae/ee/oo/oe/ie/uu) and diphthongs (ij/ou/au/ei), the fricative digraphs sch and ch, and the plain consonants including g [ɣ] and w [w].

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1976 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 37 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/dum.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `dum` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-dum_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Middle Dutch (midd1321)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/midd1321)
2. <a id="src-vanloey1976"></a>Van Loey, Adolf (1976). *Middelnederlandse Spraakkunst II: Klankleer*. Wolters-Noordhoff, Groningen. [dbnl.org](https://www.dbnl.org/titels/titel.php?id=loey001midd03)
3. <a id="src-dum_wikipedia"></a>Wikipedia contributors (2024). *Middle Dutch (Wikipedia)*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Middle_Dutch)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `dum` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 197 | 0.2776 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 33 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | k |  |
| Nasal | m |  | n |  | ŋ |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z |  | x ɣ | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː y yː | u |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [sx] [w] [ɔu] [ɛi].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ae⟩ | [aː] |  |
| ⟨au⟩ | [ɔu] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] |  |
| ⟨ch⟩ | [x] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨ei⟩ | [ɛi] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɣ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ie⟩ | [iː] |  |
| ⟨ij⟩ | [ɛi] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] |  |
| ⟨oe⟩ | [u] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨ou⟩ | [ɔu] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sch⟩ | [sx] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [y] |  |
| ⟨uu⟩ | [yː] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [i] |  |
| ⟨z⟩ | [z] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "dum")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Mi'kmaq](mic.md) · [Home](../index.md) · [Middle Irish →](mga.md)
