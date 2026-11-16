# Balinese (`ban`)

<!-- atlas:summary begin -->
Balinese is an Austronesian language, written in the Latin script. Glottolog places it in Indonesia. The `ban` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ban` |
| ISO 639-3 | [ban](https://iso639-3.sil.org/code/ban), Balinese |
| Glottolog | [bali1278](https://glottolog.org/resource/languoid/id/bali1278), Balinese |
| Wikidata | [Q33070](https://www.wikidata.org/wiki/Q33070) |
| Wikipedia | [Balinese language](https://en.wikipedia.org/wiki/Balinese_language) |
| Family | [Austronesian](by-family.md#austronesian) |
| Region | [Papunesia](by-region.md#papunesia) > [Indonesia](by-region.md#indonesia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Austronesian](https://tigregotico.github.io/orthography2ipa/#x-clade-aust1307) `x-clade-aust1307` |
| Explorer | [`ban` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ban) |
| Spec file | [`ban.json`](../../orthography2ipa/data/ban.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Balinese (Basa Bali) in the Latin orthography (the Balinese script, Aksara Bali, is also in use and is not covered here). Indonesian-style spelling conventions: ⟨c⟩=/tʃ/, ⟨j⟩=/dʒ/, ⟨ny⟩=/ɲ/, ⟨ng⟩=/ŋ/. Six vowels /i e ə a o u/, ⟨e⟩ writes both /e/ and /ə/ and word-final orthographic ⟨-a⟩ is typically realised as [ə].

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1995 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 28 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ban.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ban` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-ban_wiki"></a>Wikipedia contributors (2024). *Balinese language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Balinese_language)
2. <a id="src-clynes1995"></a>Clynes, Adrian (1995). *Topics in the phonology and morphosyntax of Balinese, based on the dialect of Singaraja, North Bali*. Australian National University (PhD thesis). Cited: xiv, 23, 30. [openresearch-repository.anu.edu.au](https://openresearch-repository.anu.edu.au/handle/1885/10744)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ban` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 299 | 0.1630 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 27 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f | s z |  |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [ks] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] [ə] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [f] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ks] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ban")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Balearic Catalan](ca-x-balear.md) · [Home](../index.md) · [Bambara →](bm.md)
