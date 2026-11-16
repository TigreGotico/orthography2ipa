# Acehnese (`ace`)

<!-- atlas:summary begin -->
Acehnese is an Austronesian language, written in the Latin script. Glottolog places it in Indonesia. The `ace` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ace` |
| ISO 639-3 | [ace](https://iso639-3.sil.org/code/ace), Achinese |
| Glottolog | [achi1257](https://glottolog.org/resource/languoid/id/achi1257), Acehnese |
| Wikidata | [Q27683](https://www.wikidata.org/wiki/Q27683) |
| Wikipedia | [Acehnese language](https://en.wikipedia.org/wiki/Acehnese_language) |
| Family | [Austronesian](by-family.md#austronesian) |
| Region | [Eurasia](by-region.md#several-macroareas), [Papunesia](by-region.md#several-macroareas) > [Indonesia](by-region.md#indonesia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Austronesian](https://tigregotico.github.io/orthography2ipa/#x-clade-aust1307) `x-clade-aust1307` |
| Explorer | [`ace` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ace) |
| Spec file | [`ace.json`](../../orthography2ipa/data/ace.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Acehnese (Basa Acèh / Acèh), Malayo-Polynesian language of Aceh, Sumatra. Latin orthography (1980 standard, replacing the earlier Husaini/Dutch-based spelling), the Jawoë (Arabic-derived) script is also traditionally used and is NOT modelled here, input is assumed to be in the Latin orthography.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1984 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 29 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ace.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ace` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-acehnese_language_wiki"></a>Wikipedia contributors (2026). *Acehnese language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Acehnese_language)
2. <a id="src-durie1984"></a>Durie, Mark (1984). *A grammar of Acehnese*. Australian National University (PhD thesis, published 1985 as VKI 112, Foris). Cited: 34-35. DOI [10.25911/5d6fa25bcc31c](https://doi.org/10.25911/5d6fa25bcc31c) · [openresearch-repository.anu.edu.au](https://openresearch-repository.anu.edu.au/handle/1885/138059)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ace` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 267 | 0.1102 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 30 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d t |  | c ɟ | k ɡ | ʔ |
| Nasal | m | n |  | ɲ | ŋ |  |
| Trill |  | r |  |  |  |  |
| Fricative |  | s | ʃ |  |  | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u ɯ |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ ʌ |
| Open | a |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [c] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ə] |  |
| ⟨eu⟩ | [ɯ] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ɟ] |  |
| ⟨k⟩ | [k] [ʔ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sy⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [e] |  |
| ⟨ô⟩ | [o] |  |
| ⟨ö⟩ | [ʌ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ace")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Abruzzese](it-IT-x-abruzzo.md) · [Home](../index.md) · [Adyghe →](ady.md)
