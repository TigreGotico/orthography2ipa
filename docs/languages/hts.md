# Hadza (`hts`)

<!-- atlas:summary begin -->
Hadza is a Hadza language, written in the Latin script. Glottolog places it in the Africa macroarea. The `hts` spec is at the research tier. It cites 6 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `hts` |
| ISO 639-3 | [hts](https://iso639-3.sil.org/code/hts), Hadza |
| Wikipedia | [Hadza language](https://en.wikipedia.org/wiki/Hadza_language) |
| Family | [Hadza](by-family.md#hadza) |
| Region | [Africa](by-region.md#africa) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Hadza](https://tigregotico.github.io/orthography2ipa/#x-clade-hadz1240) `x-clade-hadz1240` |
| Explorer | [`hts` in the data explorer](https://tigregotico.github.io/orthography2ipa/#hts) |
| Spec file | [`hts.json`](../../orthography2ipa/data/hts.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Language isolate of Tanzania (Glottolog hadz1240) with a three-place click series. This map follows the practical orthography of the Miller/Anyawire Hadza lexicon (Miller 2008, Miller & Anyawire et al. 2013), which is the convention the available Hadza word lists are written in.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 6 works, from 1993 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 64 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/hts.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `hts` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-hts_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Hadza (hadz1240)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/hadz1240)
2. <a id="src-hts_wikipedia"></a>Wikipedia contributors (2024). *Hadza language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Hadza_language)
3. <a id="src-hts_miller2008"></a>Miller, Kirk (2008). *Hadza Grammar Notes*. 3rd International Symposium on Khoisan Languages and Linguistics, Riezlern.
4. <a id="src-hts_sands_maddieson_ladefoged1996"></a>Sands, Bonny, Maddieson, Ian, Ladefoged, Peter (1996). *The phonetic structures of Hadza*. Studies in African Linguistics 25(2), 171-204 (also UCLA Working Papers in Phonetics 84). Cited: 171-204.
5. <a id="src-hts_sands2013"></a>Sands, Bonny (2013). *Hadza*. In Rainer Vossen (ed.), The Khoesan Languages, Routledge (Routledge Language Family Series).
6. <a id="src-hts_hartell1993"></a>Hartell, Rhonda L. (ed.) (1993). *Alphabets of Africa / Alphabets de langues africaines*. UNESCO / Summer Institute of Linguistics, Dakar.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `hts` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 329 | 0.0224 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 75 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ pʼ |  | d t tʰ |  |  | k kʰ kʷ kʷʰ ɡ |  |
| Affricate |  |  | d͡z t͡s t͡sʰ t͡sʼ | d͡ʒ t͡ʃ t͡ʃʰ t͡ʃʼ |  | k͡xʷʼ k͡xʼ |  |
| Nasal | m |  | n n̩ |  |  |  |  |
| Fricative |  | f | s | ʃ |  | x | ɦ |
| Lateral fricative |  |  | ɬ |  |  |  |  |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [c͡ʎ̥˔] [c͡ʎ̥˔ʰ] [c͡ʎ̥˔ʼ] [k͡ǀ] [k͡ǀʰ] [k͡ǁ] [k͡ǁʰ] [k͡ǃ] [k͡ǃʰ] [nk͡ǀ] [nk͡ǀʰ] [nk͡ǃʰ] [w] [ŋ͡ǀ] [ŋ͡ǀˀ] [ŋ͡ǁ] [ŋ͡ǁˀ] [ŋ͡ǃ] [ŋ͡ǃˀ] [ɺ] [ʔa] [ʔaː] [ʔe] [ʔeː] [ʔi] [ʔiː] [ʔo] [ʔoː] [ʔu] [ʔuː] [ᵑʘ] [ᵑʘʷ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] | after vowel [ʔa] · default [a] · word initial [ʔa] |
| ⟨b⟩ | [b] |  |
| ⟨bb⟩ | [pʼ] |  |
| ⟨c⟩ | [k͡ǀ] |  |
| ⟨cc⟩ | [ŋ͡ǀˀ] |  |
| ⟨ch⟩ | [k͡ǀʰ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dl⟩ | [c͡ʎ̥˔ʼ] |  |
| ⟨e⟩ | [e] | after vowel [ʔe] · default [e] · word initial [ʔe] |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gg⟩ | [k͡xʼ] |  |
| ⟨ggw⟩ | [k͡xʷʼ] |  |
| ⟨h⟩ | [ɦ] |  |
| ⟨hh⟩ | [x] |  |
| ⟨i⟩ | [i] | after vowel [ʔi] · default [i] · word initial [ʔi] |
| ⟨j⟩ | [d͡ʒ] |  |
| ⟨jj⟩ | [t͡ʃʼ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨khw⟩ | [kʷʰ] |  |
| ⟨kw⟩ | [kʷ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mc⟩ | [ᵑʘ] |  |
| ⟨mcw⟩ | [ᵑʘʷ] |  |
| ⟨n⟩ | [n] |  |
| ⟨nc⟩ | [ŋ͡ǀ] |  |
| ⟨nch⟩ | [nk͡ǀʰ] |  |
| ⟨ngc⟩ | [nk͡ǀ] |  |
| ⟨nq⟩ | [ŋ͡ǃ] |  |
| ⟨nqh⟩ | [nk͡ǃʰ] |  |
| ⟨nx⟩ | [ŋ͡ǁ] |  |
| ⟨o⟩ | [o] | after vowel [ʔo] · default [o] · word initial [ʔo] |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨q⟩ | [k͡ǃ] |  |
| ⟨qh⟩ | [k͡ǃʰ] |  |
| ⟨qq⟩ | [ŋ͡ǃˀ] |  |
| ⟨r⟩ | [ɺ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨sl⟩ | [ɬ] |  |
| ⟨t⟩ | [t] |  |
| ⟨tc⟩ | [t͡ʃ] |  |
| ⟨tch⟩ | [t͡ʃʰ] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨tl⟩ | [c͡ʎ̥˔] |  |
| ⟨tlh⟩ | [c͡ʎ̥˔ʰ] |  |
| ⟨ts⟩ | [t͡s] |  |
| ⟨tsh⟩ | [t͡sʰ] |  |
| ⟨u⟩ | [u] | after vowel [ʔu] · default [u] · word initial [ʔu] |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [k͡ǁ] |  |
| ⟨xh⟩ | [k͡ǁʰ] |  |
| ⟨xx⟩ | [ŋ͡ǁˀ] |  |
| ⟨y⟩ | [j] | default [j] · word initial [ʔi] |
| ⟨z⟩ | [d͡z] |  |
| ⟨zz⟩ | [t͡sʼ] |  |
| ⟨â⟩ | [aː] | after vowel [ʔaː] · default [aː] · word initial [ʔaː] |
| ⟨ê⟩ | [eː] | after vowel [ʔeː] · default [eː] · word initial [ʔeː] |
| ⟨î⟩ | [iː] | after vowel [ʔiː] · default [iː] · word initial [ʔiː] |
| ⟨ô⟩ | [oː] | after vowel [ʔoː] · default [oː] · word initial [ʔoː] |
| ⟨û⟩ | [uː] | after vowel [ʔuː] · default [uː] · word initial [ʔuː] |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 13 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `HTS_POSTNASAL_B` | /b/ → [p], after [n] [m] [ŋ] [n̩] | - | [Sands 1996](#src-hts_sands_maddieson_ladefoged1996), Maddieson & Ladefoged 1996 |
| `HTS_POSTNASAL_D` | /d/ → [t], after [n] [m] [ŋ] [n̩] | - | [Sands 1996](#src-hts_sands_maddieson_ladefoged1996), Maddieson & Ladefoged 1996 |
| `HTS_POSTNASAL_G` | /ɡ/ → [k], after [n] [m] [ŋ] [n̩] | - | [Sands 1996](#src-hts_sands_maddieson_ladefoged1996), Maddieson & Ladefoged 1996 |
| `HTS_POSTNASAL_J` | /d͡ʒ/ → [t͡ʃ], after [n] [m] [ŋ] [n̩] | ⟨nj⟩ [nt͡ʃ] | [Sands 1996](#src-hts_sands_maddieson_ladefoged1996), Maddieson & Ladefoged 1996 |
| `HTS_POSTNASAL_T` | /t/ → [tʰ], after [n] [m] [ŋ] [n̩] | ⟨nt⟩ [ntʰ] | [Sands 1996](#src-hts_sands_maddieson_ladefoged1996), [Sands 2013](#src-hts_sands2013), Maddieson & Ladefoged 1996 |
| `HTS_POSTNASAL_K` | /k/ → [kʰ], after [n] [m] [ŋ] [n̩] | ⟨nk⟩ [nkʰ] | [Sands 1996](#src-hts_sands_maddieson_ladefoged1996), [Sands 2013](#src-hts_sands2013), Maddieson & Ladefoged 1996 |
| `HTS_POSTNASAL_P` | /p/ → [pʰ], after [n] [m] [ŋ] [n̩] | ⟨mp⟩ [mpʰ] | [Sands 2013](#src-hts_sands2013) |
| `HTS_POSTNASAL_TS` | /t͡s/ → [t͡sʰ], after [n] [m] [ŋ] [n̩] | - | [Sands 1996](#src-hts_sands_maddieson_ladefoged1996), Maddieson & Ladefoged 1996 |
| `HTS_GLIDE_Y_BEFORE_FRONT` | /j/ → ∅, after a vowel, before [i] [e] [iː] [eː] | - | [Sands 2013](#src-hts_sands2013) |
| `HTS_GLIDE_Y_AFTER_FRONT` | /j/ → ∅, before a vowel, after [i] [e] [iː] [eː] | - | [Sands 2013](#src-hts_sands2013) |
| `HTS_GLIDE_W_BEFORE_ROUND` | /w/ → ∅, after a vowel, before [o] [u] [oː] [uː] | - | [Sands 2013](#src-hts_sands2013) |
| `HTS_GLIDE_W_AFTER_ROUND` | /w/ → ∅, before a vowel, after [o] [u] [oː] [uː] | - | [Sands 2013](#src-hts_sands2013) |
| `HTS_SYLLABIC_N` | /n/ → [n̩], word-initially, before a consonant | - | [Sands 2013](#src-hts_sands2013) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "hts")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Gun](guw.md) · [Home](../index.md) · [Haitian Creole →](ht.md)
