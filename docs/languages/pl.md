# Polish (`pl`)

<!-- atlas:summary begin -->
Polish is a West Slavic language, written in the Latin script. Glottolog places it in 8 countries. The `pl` spec is at the research tier. It cites 3 sources and has 3 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `pl` |
| Aliases | `pol` |
| ISO 639-3 | [pol](https://iso639-3.sil.org/code/pol), Polish |
| Glottolog | [poli1260](https://glottolog.org/resource/languoid/id/poli1260), Polish |
| Wikidata | [Q809](https://www.wikidata.org/wiki/Q809) |
| Wikipedia | [Polish language](https://en.wikipedia.org/wiki/Polish_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Balto-Slavic > Slavic > West Slavic](by-family.md#indo-european--balto-slavic--slavic--west-slavic) |
| Region | [Eurasia](by-region.md#eurasia) > [Belarus](by-region.md#belarus), [Czechia](by-region.md#czechia), [Germany](by-region.md#germany), [Lithuania](by-region.md#lithuania), [Poland](by-region.md#poland), [Russia](by-region.md#russia), [Slovakia](by-region.md#slovakia), [Ukraine](by-region.md#ukraine) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1400, living |
| Parent | [West Slavic](https://tigregotico.github.io/orthography2ipa/#x-clade-west2792) `x-clade-west2792` |
| Explorer | [`pl` in the data explorer](https://tigregotico.github.io/orthography2ipa/#pl) |
| Spec file | [`pl.json`](../../orthography2ipa/data/pl.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Polish. Three sibilant series: alveolar /s z ts dz/, retroflex /ʂ ʐ tʂ dʐ/, alveolo-palatal /ɕ ʑ tɕ dʑ/. Nasal vowels ⟨ą ę⟩ realise as VN sequences before stops. FINAL DEVOICING: Polish obstruents devoice in coda/word-finally.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1993 to 2002. [Sources](#sources) lists them. The spec file writes all 44 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/pl.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `pl` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-comrie_corbett1993"></a>Comrie, B. & Corbett, G. (eds.) (1993). *The Slavonic Languages*. Routledge.
2. <a id="src-swan2002"></a>Swan, O. (2002). *A Grammar of Contemporary Polish*. Slavica Publishers.
3. <a id="src-szpyra_kozlowski2002"></a>Szpyra-Kozłowski, J. (2002). *Wprowadzenie do współczesnej fonologii*. Wydawnictwo UMCS.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `pl` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 148990 | 0.0480 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `pl` | generated | espeak-derived | CC BY 4.0 | 15523 | 0.2465 | no |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `pl` | generated | epitran-derived | CC0 1.0 | 47592 | 0.0186 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 51 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Retroflex | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |
| Affricate |  |  | dz ts |  | dʑ tɕ |  |
| Nasal | m |  | n |  | ɲ | ŋ |
| Trill |  |  | r |  |  |  |
| Tap |  |  | ɾ |  |  |  |
| Fricative |  | f v | s z | ʂ ʐ | ɕ ʑ | x |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Open-mid | ɛ ɛ̃ |  | ɔ ɔ̃ |
| Open | a |  |  |

Sequences that the spec writes as one unit: [dʐ] [dʑi] [tɕi] [tʂ] [w] [ɔm] [ɔn] [ɔw̃] [ɔŋ] [ɕi] [ɛm] [ɛn] [ɛw̃] [ɛŋ] [ɲi] [ʑi].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] | default [b] · word final [p] |
| ⟨c⟩ | [ts] |  |
| ⟨ch⟩ | [x] |  |
| ⟨ci⟩ | [tɕi] | before vowel [tɕ] · default [tɕi] |
| ⟨cz⟩ | [tʂ] |  |
| ⟨d⟩ | [d] | default [d] · word final [t] |
| ⟨dz⟩ | [dz] | default [dz] · word final [ts] |
| ⟨dzi⟩ | [dʑi] | before vowel [dʑ] · default [dʑi] |
| ⟨dź⟩ | [dʑ] | default [dʑ] · word final [tɕ] |
| ⟨dż⟩ | [dʐ] | default [dʐ] · word final [tʂ] |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] | default [ɡ] · word final [k] |
| ⟨h⟩ | [x] |  |
| ⟨i⟩ | [i] | before vowel [j] · default [i] |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ni⟩ | [ɲi] | before vowel [ɲ] · default [ɲi] |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨rz⟩ | [ʐ] | default [ʐ] · word final [ʂ] |
| ⟨s⟩ | [s] |  |
| ⟨si⟩ | [ɕi] | before vowel [ɕ] · default [ɕi] |
| ⟨sz⟩ | [ʂ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [v] | default [v] · word final [f] |
| ⟨y⟩ | [ɨ] |  |
| ⟨z⟩ | [z] | default [z] · word final [s] |
| ⟨zi⟩ | [ʑi] | before vowel [ʑ] · default [ʑi] |
| ⟨ó⟩ | [u] |  |
| ⟨ą⟩ | [ɔ̃] [ɔw̃] [ɔm] [ɔn] [ɔŋ] | before consonant [ɔ̃] · default [ɔ̃] · word final [ɔw̃] |
| ⟨ć⟩ | [tɕ] |  |
| ⟨ę⟩ | [ɛ̃] [ɛw̃] [ɛm] [ɛn] [ɛŋ] | before consonant [ɛ̃] · default [ɛ̃] · word final [ɛ] |
| ⟨ł⟩ | [w] |  |
| ⟨ń⟩ | [ɲ] |  |
| ⟨ś⟩ | [ɕ] |  |
| ⟨ź⟩ | [ʑ] | default [ʑ] · word final [ɕ] |
| ⟨ż⟩ | [ʐ] | default [ʐ] · word final [ʂ] |

Stress falls on the penult by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 29 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `PL_NASAL_DECOMP_O_M` | /ɔ̃/ → [ɔm], before [p] [b] | ⟨ząb⟩ [zɔmp] | Gussmann 2007 |
| `PL_NASAL_DECOMP_O_N` | /ɔ̃/ → [ɔn], before [t] [d] [ts] [dz] [tʂ] [dʐ] [tɕ] [dʑ] | ⟨kąt⟩ [kɔnt] | Gussmann 2007 |
| `PL_NASAL_DECOMP_O_NG` | /ɔ̃/ → [ɔŋ], before [k] [ɡ] | - | Gussmann 2007 |
| `PL_NASAL_DECOMP_E_M` | /ɛ̃/ → [ɛm], before [p] [b] | - | Gussmann 2007 |
| `PL_NASAL_DECOMP_E_N` | /ɛ̃/ → [ɛn], before [t] [d] [ts] [dz] [tʂ] [dʐ] [tɕ] [dʑ] | - | Gussmann 2007 |
| `PL_NASAL_DECOMP_E_NG` | /ɛ̃/ → [ɛŋ], before [k] [ɡ] | ⟨ręka⟩ [rɛŋka] | Gussmann 2007 |
| `PL_REGR_DEVOICE_B` | /b/ → [p], before [p] [t] [k] [f] [s] [ʂ] [ɕ] [x] and 3 more | ⟨Abchaz-⟩ [apx-] | Gussmann 2007 |
| `PL_REGR_DEVOICE_D` | /d/ → [t], before [p] [t] [k] [f] [s] [ʂ] [ɕ] [x] and 3 more | ⟨wódka⟩ [vutka] | Gussmann 2007 |
| `PL_REGR_DEVOICE_Ɡ` | /ɡ/ → [k], before [p] [t] [k] [f] [s] [ʂ] [ɕ] [x] and 3 more | ⟨wódka⟩ [vutka] | Gussmann 2007 |
| `PL_REGR_DEVOICE_V` | /v/ → [f], before [p] [t] [k] [f] [s] [ʂ] [ɕ] [x] and 3 more | - | Gussmann 2007 |
| `PL_REGR_DEVOICE_Z` | /z/ → [s], before [p] [t] [k] [f] [s] [ʂ] [ɕ] [x] and 3 more | - | Gussmann 2007 |
| `PL_REGR_DEVOICE_ʐ` | /ʐ/ → [ʂ], before [p] [t] [k] [f] [s] [ʂ] [ɕ] [x] and 3 more | - | Gussmann 2007 |
| `PL_REGR_DEVOICE_ʑ` | /ʑ/ → [ɕ], before [p] [t] [k] [f] [s] [ʂ] [ɕ] [x] and 3 more | - | Gussmann 2007 |
| `PL_REGR_DEVOICE_DZ` | /dz/ → [ts], before [p] [t] [k] [f] [s] [ʂ] [ɕ] [x] and 3 more | - | Gussmann 2007 |
| `PL_REGR_DEVOICE_Dʐ` | /dʐ/ → [tʂ], before [p] [t] [k] [f] [s] [ʂ] [ɕ] [x] and 3 more | - | Gussmann 2007 |
| `PL_REGR_DEVOICE_Dʑ` | /dʑ/ → [tɕ], before [p] [t] [k] [f] [s] [ʂ] [ɕ] [x] and 3 more | - | Gussmann 2007 |
| `PL_REGR_VOICE_P` | /p/ → [b], before [b] [d] [ɡ] [z] [ʑ] [dz] [dʐ] [dʑ] | ⟨prośba⟩ [prɔʑba] | Gussmann 2007 |
| `PL_REGR_VOICE_T` | /t/ → [d], before [b] [d] [ɡ] [z] [ʑ] [dz] [dʐ] [dʑ] | - | Gussmann 2007 |
| `PL_REGR_VOICE_K` | /k/ → [ɡ], before [b] [d] [ɡ] [z] [ʑ] [dz] [dʐ] [dʑ] | ⟨Afgan-⟩ [avɡ-] | Gussmann 2007 |
| `PL_REGR_VOICE_F` | /f/ → [v], before [b] [d] [ɡ] [z] [ʑ] [dz] [dʐ] [dʑ] | ⟨Afgan-⟩ [avɡ-] | Gussmann 2007 |
| `PL_REGR_VOICE_S` | /s/ → [z], before [b] [d] [ɡ] [z] [ʑ] [dz] [dʐ] [dʑ] | - | Gussmann 2007 |
| `PL_REGR_VOICE_Ʂ` | /ʂ/ → [ʐ], before [b] [d] [ɡ] [z] [ʑ] [dz] [dʐ] [dʑ] | - | Gussmann 2007 |
| `PL_REGR_VOICE_ɕ` | /ɕ/ → [ʑ], before [b] [d] [ɡ] [z] [ʑ] [dz] [dʐ] [dʑ] | ⟨prośba⟩ [prɔʑba] | Gussmann 2007 |
| `PL_REGR_VOICE_TS` | /ts/ → [dz], before [b] [d] [ɡ] [z] [ʑ] [dz] [dʐ] [dʑ] | - | Gussmann 2007 |
| `PL_REGR_VOICE_TꟅ` | /tʂ/ → [dʐ], before [b] [d] [ɡ] [z] [ʑ] [dz] [dʐ] [dʑ] | - | Gussmann 2007 |
| `PL_REGR_VOICE_Tɕ` | /tɕ/ → [dʑ], before [b] [d] [ɡ] [z] [ʑ] [dz] [dʐ] [dʑ] | - | Gussmann 2007 |
| `PL_PROGR_DEVOICE_V` | /v/ → [f], after [p] [t] [k] [f] [s] [ʂ] [ɕ] [x] and 3 more | ⟨kwiat⟩ [kfjat] | Gussmann 2007 |
| `PL_PROGR_DEVOICE_ʐ` | /ʐ/ → [ʂ], after [p] [t] [k] [f] [s] [ʂ] [ɕ] [x] and 3 more | ⟨przy⟩ [pʂɨ] | Gussmann 2007 |
| `PL_N_VELAR` | /n/ → [ŋ], before [k] [ɡ] | ⟨bank⟩ [baŋk] | Gussmann 2007 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "pl")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Polabian](pox.md) · [Home](../index.md) · [Pontic Greek →](pnt.md)
