# Malay (`ms`)

<!-- atlas:summary begin -->
Malay is an Austronesian language, written in the Latin script. Glottolog places it in Brunei, Malaysia and Singapore. The `ms` spec is at the research tier. It cites 3 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ms` |
| ISO 639-3 | [msa](https://iso639-3.sil.org/code/msa), Malay (macrolanguage) |
| Glottolog | [stan1306](https://glottolog.org/resource/languoid/id/stan1306), Standard Malay |
| Wikidata | [Q9237](https://www.wikidata.org/wiki/Q9237) |
| Wikipedia | [Malay language](https://en.wikipedia.org/wiki/Malay_language) |
| Family | [Austronesian](by-family.md#austronesian) |
| Region | [Eurasia](by-region.md#eurasia) > [Brunei](by-region.md#brunei), [Malaysia](by-region.md#malaysia), [Singapore](by-region.md#singapore) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1400, living |
| Parent | [Proto-Malayo-Polynesian (family node)](https://tigregotico.github.io/orthography2ipa/#poz) `poz` |
| Explorer | [`ms` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ms) |
| Spec file | [`ms.json`](../../orthography2ipa/data/ms.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Malay (Bahasa Melayu) in the Rumi (Latin) script.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1996 to 2011. [Sources](#sources) lists them. The spec file writes no spelling of its own. It takes all 32 from [Indonesian (Bahasa Indonesia)](id.md) `id`.

The [spec file](../../orthography2ipa/data/ms.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ms` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-adelaar_himmelmann2005"></a>Adelaar, A. & Himmelmann, N. (eds.) (2005). *The Austronesian Languages of Asia and Madagascar*. Routledge.
2. <a id="src-clynes_deterding2011"></a>Clynes, A. & Deterding, D. (2011). *Standard Malay (Brunei)*. Journal of the International Phonetic Association. Cited: 259-268.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ms` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 4887 | 0.0967 | yes |
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `ms` | generated | machine-generated | MIT, each file its own | 28215 | 0.1305 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 34 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | ʔ |
| Affricate |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ |  | x | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [aj] [aw] [ks] [oj] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [aj] |  |
| ⟨au⟩ | [aw] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] [ə] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] | intervocalic [h] ∅ · word final [h] ∅ · word initial [h] |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] [ʔ] | word final [ʔ] · word initial [k] |
| ⟨kh⟩ | [x] |  |
| ⟨l⟩ | [l] | word final [l] |
| ⟨m⟩ | [m] | word final [m] |
| ⟨n⟩ | [n] | word final [n] |
| ⟨ng⟩ | [ŋ] | word final [ŋ] · word initial [ŋ] |
| ⟨ny⟩ | [ɲ] | word initial [ɲ] |
| ⟨o⟩ | [o] |  |
| ⟨oi⟩ | [oj] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] | intervocalic [r] · word final [r] |
| ⟨s⟩ | [s] | word final [s] |
| ⟨sy⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |

Stress falls on the penult by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ms")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Malagasy](mg.md) · [Home](../index.md) · [Malayalam →](ml.md)
