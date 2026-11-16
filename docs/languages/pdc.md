# Pennsylvania German (Pennsylvania Dutch) (`pdc`)

<!-- atlas:summary begin -->
Pennsylvania German (Pennsylvania Dutch) is a Germanic language, written in the Latin script. Glottolog places it in Canada and United States. The `pdc` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `pdc` |
| ISO 639-3 | [pdc](https://iso639-3.sil.org/code/pdc), Pennsylvania German |
| Glottolog | [penn1240](https://glottolog.org/resource/languoid/id/penn1240), Pennsylvania German |
| Wikidata | [Q22711](https://www.wikidata.org/wiki/Q22711) |
| Wikipedia | [Pennsylvania Dutch language](https://en.wikipedia.org/wiki/Pennsylvania_Dutch_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic](by-family.md#indo-european--germanic) |
| Region | [North America](by-region.md#north-america) > [Canada](by-region.md#canada), [United States](by-region.md#united-states) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1700, living |
| Parent | [Germanic](https://tigregotico.github.io/orthography2ipa/#x-clade-germ1287) `x-clade-germ1287` |
| Explorer | [`pdc` in the data explorer](https://tigregotico.github.io/orthography2ipa/#pdc) |
| Spec file | [`pdc.json`](../../orthography2ipa/data/pdc.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Pennsylvania German / Pennsylvania Dutch (Pennsilfaanisch Deitsch), a Palatine (Rhine Franconian) West Germanic variety of North America.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1954 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 37 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/pdc.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `pdc` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-pdc_wiki"></a>Wikipedia contributors (2024). *Pennsylvania Dutch language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Pennsylvania_Dutch_language)
2. <a id="src-buffington_barba1954"></a>Buffington, Albert F. & Barba, Preston A. (1954). *A Pennsylvania German Grammar*. Schlechter's.
3. <a id="src-padutchdictionary_bbb"></a>Pennsylvania Dutch Dictionary (padutchdictionary.com) (2024). *About: the Buffington-Barba-Beam orthography and pronunciation key*. padutchdictionary.com. [padutchdictionary.com](https://www.padutchdictionary.com/about.html)
4. <a id="src-padutch_net_pronunciation"></a>padutch.net (2024). *Pennsylvania Dutch pronunciation*. padutch.net. [padutch.net](https://padutch.net/pronunciation/)
5. <a id="src-wiese1996"></a>Wiese, Richard (1996). *The Phonology of German*. Oxford University Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `pdc` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 405 | 0.2729 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 40 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  | ts |  |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s | ʃ | ç | x | h |
| Approximant |  | ʋ |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː |  | uː |
| Near-close | ɪ |  | ʊ |
| Close-mid | eː |  | oː |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ ɔː |
| Near-open | æː | ɐ |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [aɪ] [aʊ] [ks] [ŋk] [ɔɪ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] [aː] |  |
| ⟨aa⟩ | [ɔː] |  |
| ⟨ae⟩ | [eː] |  |
| ⟨ai⟩ | [aɪ] |  |
| ⟨au⟩ | [aʊ] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [ç] [x] |  |
| ⟨chs⟩ | [ks] |  |
| ⟨d⟩ | [d] | default [d] · word final [t] |
| ⟨e⟩ | [ɛ] [eː] [ə] | default [ɛ] [eː] [ə] · word final [ə] |
| ⟨ee⟩ | [eː] |  |
| ⟨ei⟩ | [aɪ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [j] [k] | default [ɡ] [j] · word final [k] |
| ⟨h⟩ | [h] ∅ |  |
| ⟨i⟩ | [ɪ] [iː] |  |
| ⟨ie⟩ | [iː] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨o⟩ | [ɔ] [oː] |  |
| ⟨oi⟩ | [ɔɪ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] [ɐ] | default [r] [ɐ] · word final [ɐ] |
| ⟨s⟩ | [s] |  |
| ⟨sch⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨tz⟩ | [ts] |  |
| ⟨u⟩ | [ʊ] [uː] |  |
| ⟨v⟩ | [f] |  |
| ⟨w⟩ | [ʋ] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [j] [ɪ] |  |
| ⟨z⟩ | [ts] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "pdc")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Pashto](ps.md) · [Home](../index.md) · [Persian →](fa.md)
