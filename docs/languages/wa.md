# Walloon (`wa`)

<!-- atlas:summary begin -->
Walloon is a Romance language, written in the Latin script. Glottolog places it in Belgium, France and Luxembourg. The `wa` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `wa` |
| ISO 639-3 | [wln](https://iso639-3.sil.org/code/wln), Walloon |
| Glottolog | [wall1255](https://glottolog.org/resource/languoid/id/wall1255), Walloon |
| Wikidata | [Q34219](https://www.wikidata.org/wiki/Q34219) |
| Wikipedia | [Walloon language](https://en.wikipedia.org/wiki/Walloon_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance](by-family.md#indo-european--italic--romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Belgium](by-region.md#belgium), [France](by-region.md#france), [Luxembourg](by-region.md#luxembourg) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Ancestor | [Gallo-Romance Vulgar Latin](https://tigregotico.github.io/orthography2ipa/#la-x-gallia) `la-x-gallia` |
| Explorer | [`wa` in the data explorer](https://tigregotico.github.io/orthography2ipa/#wa) |
| Spec file | [`wa.json`](../../orthography2ipa/data/wa.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Walloon (Walon), the Gallo-Romance langue d'oïl of Wallonia (southern Belgium) and the Ardennes of France, sister to French and Picard.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2024 to 2025. [Sources](#sources) lists them. The spec file writes all 54 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/wa.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `wa` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-orjuela2025"></a>Espinosa Orjuela, J.F., Boula de Mareüil, P. & Evrard, M. (2025). *Speech synthesis for Walloon, an under-resourced minority language*. Proc. 13th Speech Synthesis Workshop (SSW 2025), ISCA. Cited: 189-193. [isca-archive.org](https://www.isca-archive.org/ssw_2025/orjuela25_ssw.pdf)
2. <a id="src-wiki-wa-orthography"></a>Wikipedia contributors (2024). *Walloon orthography*.
3. <a id="src-wiki-wa"></a>Wikipedia contributors (2024). *Walloon language*.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `wa` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2348 | 0.1443 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 59 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |  |
| Affricate |  |  |  | dʒ tʃ |  |  |  |  |
| Nasal | m |  | n |  | ɲ |  |  |  |
| Trill |  |  | r |  |  |  | ʀ |  |
| Fricative |  | f v | s z | ʃ ʒ | ç | x | ʁ χ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː y yː |  | u uː |
| Close-mid | e eː ø ẽ |  | o oː |
| Mid |  | ə |  |
| Open-mid | œ œ̃ ɛ ɛː ɛ̃ |  | ɔ ɔː ɔ̃ |
| Open | a |  | ɑ ɑː ɑ̃ |

Sequences that the spec writes as one unit: [ja] [ks] [nj] [sk] [w] [wa] [wɛ] [ɛj].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ae⟩ | [a] [ɛ] |  |
| ⟨ai⟩ | [eː] [ɛː] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] | before front vowel [s] · default [k] |
| ⟨ch⟩ | [ʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dj⟩ | [dʒ] |  |
| ⟨e⟩ | [ɛ] [ə] | default [ɛ] [ə] · word final ∅ |
| ⟨ea⟩ | [ja] [eː] [ɛː] |  |
| ⟨eu⟩ | [ø] [œ] [ə] |  |
| ⟨ey⟩ | [ɛj] [iː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gn⟩ | [ɲ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨jh⟩ | [ʒ] [h] [ç] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨oe⟩ | [wɛ] [ø] |  |
| ⟨oi⟩ | [wa] [wɛ] [oː] |  |
| ⟨ou⟩ | [u] |  |
| ⟨oû⟩ | [uː] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [k] |  |
| ⟨r⟩ | [ʀ] [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sch⟩ | [ʃ] [h] [sk] [ç] |  |
| ⟨sh⟩ | [ʃ] [s] |  |
| ⟨ss⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tch⟩ | [tʃ] |  |
| ⟨u⟩ | [y] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ks] |  |
| ⟨xh⟩ | [ʃ] [h] [x] [ç] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨â⟩ | [ɑ] |  |
| ⟨å⟩ | [ɔː] [oː] [ɑː] |  |
| ⟨ç⟩ | [s] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [e] |  |
| ⟨ê⟩ | [ɛː] |  |
| ⟨î⟩ | [iː] |  |
| ⟨ô⟩ | [oː] |  |
| ⟨û⟩ | [yː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 14 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `WA_NASAL_a` | /a/ → [ɑ̃], before a coda nasal | - | - |
| `WA_NASAL_i` | /i/ → [ɛ̃], before a coda nasal | - | - |
| `WA_NASAL_e` | /e/ → [ẽ], before a coda nasal | - | - |
| `WA_NASAL_epsilon` | /ɛ/ → [ẽ], before a coda nasal | - | - |
| `WA_NASAL_o` | /ɔ/ → [ɔ̃], before a coda nasal | - | - |
| `WA_NASAL_u` | /y/ → [œ̃], before a coda nasal | - | - |
| `WA_NASAL_ABSORB` | /n m/ → ∅, in the coda, after a vowel | ⟨walon⟩ [walɔ̃] | - |
| `WA_DEVOICE_b` | /b/ → [p], word-finally | - | - |
| `WA_DEVOICE_d` | /d/ → [t], word-finally | - | - |
| `WA_DEVOICE_g` | /ɡ/ → [k], word-finally | - | - |
| `WA_DEVOICE_v` | /v/ → [f], word-finally | - | - |
| `WA_DEVOICE_z` | /z/ → [s], word-finally | - | - |
| `WA_DEVOICE_zh` | /ʒ/ → [ç], word-finally | - | - |
| `WA_DEVOICE_dzh` | /dʒ/ → [tʃ], word-finally | ⟨rodje⟩ [ʀɔtʃ] | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "wa")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Waigali](wbk.md) · [Home](../index.md) · [Waray →](war.md)
