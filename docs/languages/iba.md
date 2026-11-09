# Iban (`iba`)

<!-- atlas:summary begin -->
Iban is a Malayo-Polynesian language, written in the Latin script. Glottolog places it in Brunei, Indonesia and Malaysia. The `iba` spec is at the research tier. It cites 1 source and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `iba` |
| ISO 639-3 | [iba](https://iso639-3.sil.org/code/iba), Iban |
| Glottolog | [iban1264](https://glottolog.org/resource/languoid/id/iban1264), Iban |
| Wikipedia | [Iban language](https://en.wikipedia.org/wiki/Iban_language) |
| Family | [Austronesian](by-family.md#austronesian) > [Malayo-Polynesian](by-family.md#austronesian--malayo-polynesian) |
| Region | [Papunesia](by-region.md#papunesia) > [Brunei](by-region.md#brunei), [Indonesia](by-region.md#indonesia), [Malaysia](by-region.md#malaysia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Malayo-Polynesian](https://tigregotico.github.io/orthography2ipa/#x-clade-mala1545) `x-clade-mala1545` |
| Explorer | [`iba` in the data explorer](https://tigregotico.github.io/orthography2ipa/#iba) |
| Spec file | [`iba.json`](../../orthography2ipa/data/iba.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Iban (Jaku Iban) of Sarawak, written in the Latin script with Malay-style spelling conventions: ⟨ny⟩=/ɲ/, ⟨ng⟩=/ŋ/, ⟨c⟩=/tʃ/, ⟨j⟩=/dʒ/, ⟨y⟩=/j/. Six vowels /i e ə a o u/, with ⟨e⟩ writing both /e/ and /ə/. Vowels are nasalised after a nasal consonant, word-final ⟨k⟩ is commonly a glottal stop.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 1 work, from 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 23 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/iba.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `iba` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 1 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-iba_wiki"></a>Wikipedia contributors (2024). *Iban language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Iban_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `iba` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 571 | 0.1655 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 28 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p | d t |  |  | k ɡ | ʔ |
| Affricate |  |  | dʒ tʃ |  |  |  |
| Nasal | m | n |  | ɲ | ŋ |  |
| Trill |  | r |  |  |  |  |
| Fricative |  | s |  |  |  | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i ĩ |  | u ũ |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open | a ã |  |  |

Sequences that the spec writes as one unit: [w].
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
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "iba")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Hunsrik](hrx.md) · [Home](../index.md) · [Icelandic →](is.md)
