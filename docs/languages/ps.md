# Pashto (Standard Afghan) (`ps`)

<!-- atlas:summary begin -->
Pashto (Standard Afghan) is an Iranian language, written in the Arabic script. Glottolog places it in Pakistan. The `ps` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ps` |
| ISO 639-3 | [pus](https://iso639-3.sil.org/code/pus), Pushto |
| Glottolog | [nucl1276](https://glottolog.org/resource/languoid/id/nucl1276), Nuclear Pashto |
| Wikidata | [Q58680](https://www.wikidata.org/wiki/Q58680) |
| Wikipedia | [Pashto](https://en.wikipedia.org/wiki/Pashto) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Iranian](by-family.md#indo-european--indo-iranian--iranian) |
| Region | [Eurasia](by-region.md#eurasia) > [Pakistan](by-region.md#pakistan) |
| Script | [Arabic](by-script.md#arabic) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1000, living |
| Parent | [Iranian](https://tigregotico.github.io/orthography2ipa/#x-clade-iran1269) `x-clade-iran1269` |
| Explorer | [`ps` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ps) |
| Spec file | [`ps.json`](../../orthography2ipa/data/ps.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Pashto (پښتو), Standard Afghan Pashto on a Kandahari (Southwestern) base. Eastern Iranian, ~50, 60 million speakers, one of the two official languages of Afghanistan. DEFINING FEATURES vs.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1979 to 1997. [Sources](#sources) lists them. The spec file writes all 49 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ps.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ps` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-windfuhr1979"></a>Windfuhr, G. (1979). *Persian Grammar: History and State of Its Study*. Mouton.
2. <a id="src-tegey_robson1996"></a>Tegey, H. & Robson, B. (1996). *A Reference Grammar of Pashto*. Center for Applied Linguistics.
3. <a id="src-mahootian1997"></a>Mahootian, S. (1997). *Persian*. Routledge.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ps` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1075 | 0.2453 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 52 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  | ɖ ʈ ʈʰ |  | k kʰ ɡ | q | ʔ |
| Affricate |  |  | dz ts | dʒ tʃ |  |  |  |  |  |
| Nasal | m |  | n |  | ɳ |  | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Tap |  |  | ɾ |  | ɽ |  |  |  |  |
| Fricative |  | f | s z | ʃ ʒ | ʂ ʐ |  | x ɣ |  | h |
| Approximant |  |  |  |  | ɻ | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Near-open |  | ɐ |  |
| Open | a |  | ɑ ɑː |

Sequences that the spec writes as one unit: [ai] [aw] [w] [ɑw] [əi].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨آ⟩ | [ɑ] |  |
| ⟨ئ⟩ | [ai] [əi] |  |
| ⟨ا⟩ | [ɑ] [a] | default [ɑ] [a] · word initial [a] [i] [u] [ɑ] |
| ⟨ب⟩ | [b] |  |
| ⟨ت⟩ | [t] |  |
| ⟨ث⟩ | [s] |  |
| ⟨ج⟩ | [dʒ] |  |
| ⟨ح⟩ | [h] |  |
| ⟨خ⟩ | [x] |  |
| ⟨د⟩ | [d] |  |
| ⟨ذ⟩ | [z] |  |
| ⟨ر⟩ | [r] |  |
| ⟨ز⟩ | [z] |  |
| ⟨س⟩ | [s] |  |
| ⟨ش⟩ | [ʃ] |  |
| ⟨ص⟩ | [s] |  |
| ⟨ض⟩ | [z] |  |
| ⟨ط⟩ | [t] |  |
| ⟨ظ⟩ | [z] |  |
| ⟨ع⟩ | [ʔ] |  |
| ⟨غ⟩ | [ɣ] |  |
| ⟨ف⟩ | [f] |  |
| ⟨ق⟩ | [q] |  |
| ⟨ل⟩ | [l] |  |
| ⟨م⟩ | [m] |  |
| ⟨ن⟩ | [n] |  |
| ⟨ه⟩ | [h] [a] [ə] | default [h] · word final [a] [ə] |
| ⟨و⟩ | [w] [u] [o] | after vowel [w] · default [o] [u] [w] · word initial [w] |
| ⟨ي⟩ | [i] [j] | default [i] [j] · word final [i] · word initial [j] |
| ⟨َ⟩ | [a] |  |
| ⟨ُ⟩ | [u] |  |
| ⟨ِ⟩ | [i] |  |
| ⟨ټ⟩ | [ʈ] |  |
| ⟨پ⟩ | [p] |  |
| ⟨ځ⟩ | [dz] |  |
| ⟨څ⟩ | [ts] |  |
| ⟨چ⟩ | [tʃ] |  |
| ⟨ډ⟩ | [ɖ] |  |
| ⟨ړ⟩ | [ɻ] |  |
| ⟨ږ⟩ | [ʐ] |  |
| ⟨ژ⟩ | [ʒ] |  |
| ⟨ښ⟩ | [ʂ] |  |
| ⟨ک⟩ | [k] |  |
| ⟨ګ⟩ | [ɡ] |  |
| ⟨ڼ⟩ | [ɳ] |  |
| ⟨ۀ⟩ | [ə] |  |
| ⟨ی⟩ | [j] [i] [ai] | after vowel [j] · default [i] [ai] · word initial [j] |
| ⟨ۍ⟩ | [əi] |  |
| ⟨ې⟩ | [e] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 1 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `PS_NASAL_VELAR` | /n/ → [ŋ], before [k] [ɡ] [q] | - | [Tegey 1996](#src-tegey_robson1996), David 2014 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ps")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Pannonian Rusyn](rsk.md) · [Home](../index.md) · [Pennsylvania German →](pdc.md)
