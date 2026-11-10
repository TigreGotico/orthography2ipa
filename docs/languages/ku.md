# Kurdish (Kurmanji) (`ku`)

<!-- atlas:summary begin -->
Kurdish (Kurmanji) is an Iranian language, written in the Latin script. Glottolog places it in 9 countries. The `ku` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ku` |
| ISO 639-3 | [kmr](https://iso639-3.sil.org/code/kmr), Northern Kurdish |
| Glottolog | [nort2641](https://glottolog.org/resource/languoid/id/nort2641), Northern Kurdish |
| Wikidata | [Q36163](https://www.wikidata.org/wiki/Q36163) |
| Wikipedia | [Kurmanji](https://en.wikipedia.org/wiki/Kurmanji) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Iranian](by-family.md#indo-european--indo-iranian--iranian) |
| Region | [Eurasia](by-region.md#eurasia) > [Armenia](by-region.md#armenia), [Azerbaijan](by-region.md#azerbaijan), [Iran](by-region.md#iran), [Iraq](by-region.md#iraq), [Jordan](by-region.md#jordan), [Kuwait](by-region.md#kuwait), [Syria](by-region.md#syria), [Turkmenistan](by-region.md#turkmenistan) and 1 more |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Iranian](https://tigregotico.github.io/orthography2ipa/#x-clade-iran1269) `x-clade-iran1269` |
| Explorer | [`ku` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ku) |
| Spec file | [`ku.json`](../../orthography2ipa/data/ku.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Northern Kurdish / Kurmanji (kurdî, Kurmancî), the largest Kurdish variety. The mapping above is the 31-letter Hawar Latin alphabet (Celadet Alî Bedirxan, 1932), the script of the ku Wikipedia and of Kurmanji in Turkey, Syria and the diaspora.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2006 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 31 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ku.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ku` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-kurdish_alphabets_wiki"></a>Wikipedia contributors (2026). *Kurdish alphabets*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Kurdish_alphabets)
2. <a id="src-kurmanji_wiki"></a>Wikipedia contributors (2026). *Kurmanji*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Kurmanji)
3. <a id="src-thackston2006"></a>Thackston, W. M. (2006). *Kurmanji Kurdish: A Reference Grammar with Selected Readings*. Harvard University, Iranian Studies (distributed free by the author, archived copy). Cited: 1-3. [web.archive.org](https://web.archive.org/web/20150616142342/http://www.fas.harvard.edu/~iranian/Kurmanji/kurmanji_1_grammar.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ku` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2147 | 0.1440 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 31 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | q |  |
| Affricate |  |  |  | dʒ tʃ |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x |  | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː | ʉ | u |
| Near-close | ɪ |  |  |
| Close-mid | eː |  | o |
| Open-mid | ɛ |  |  |
| Open | aː |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [dʒ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ɪ] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [q] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [ʉ] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨ç⟩ | [tʃ] |  |
| ⟨ê⟩ | [eː] |  |
| ⟨î⟩ | [iː] |  |
| ⟨û⟩ | [u] |  |
| ⟨ş⟩ | [ʃ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ku")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kumyk](kum.md) · [Home](../index.md) · [Kurukh →](kru.md)
