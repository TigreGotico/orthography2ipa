# Gawri (`gwc`)

<!-- atlas:summary begin -->
Gawri is an Indo-Aryan language, written in the Arabic script. Glottolog places it in the Eurasia, Papunesia and South America macroareas. The `gwc` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `gwc` |
| ISO 639-3 | [gwc](https://iso639-3.sil.org/code/gwc), Gawri |
| Wikipedia | [Gawri language](https://en.wikipedia.org/wiki/Gawri_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#several-macroareas), [Papunesia](by-region.md#several-macroareas), [South America](by-region.md#several-macroareas) |
| Script | [Arabic](by-script.md#arabic) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Indo-Aryan](https://tigregotico.github.io/orthography2ipa/#x-clade-indo1321) `x-clade-indo1321` |
| Explorer | [`gwc` in the data explorer](https://tigregotico.github.io/orthography2ipa/#gwc) |
| Spec file | [`gwc.json`](../../orthography2ipa/data/gwc.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Gawri (Kalam Kohistani), a Dardic Indo-Aryan language of the Swat and Dir Kohistan valleys of Pakistan, written in the Perso-Arabic orthography agreed by the Gawri spelling committee in 1995 (Baart & Sagar §2.3 'Script'), which keeps maximum conformity with Urdu and adds four letters for sounds Urdu lacks.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2004 to 2024. [Sources](#sources) lists them. The spec file writes all 68 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/gwc.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `gwc` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-gwc_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Gawri (kala1373)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/kala1373)
2. <a id="src-gwc_baart_sagar"></a>Baart, Joan L. G., Sagar, Muhammad Zaman (2014). *The Gawri Language of Kalam and Dir Kohistan*. SIL International. [fli-online.org](https://fli-online.org/documents/languages/gawri/gawri_introduction.pdf)
3. <a id="src-gwc_baart2004_tone"></a>Baart, Joan L. G. (2004). *Tone and song in Kalam Kohistani (Pakistan)*. In Hugo Quene & Vincent van Heuven (eds.), On Language and Speech: Studies for Sieb G. Nooteboom. Utrecht: Netherlands Graduate Institute of Linguistics. [fli-online.org](https://www.fli-online.org/documents/languages/gawri/tone_sound_Kalam_kohistani.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `gwc` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 165 | 0.4170 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 52 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d̪ t̪ t̪ʰ | ɖ ʈ ʈʰ |  | k kʰ ɡ | q |  |
| Affricate |  |  | t̪s t̪sʰ | ʈʂ ʈʂʰ | dʑ tɕ tɕʰ |  |  |  |
| Nasal | m |  | n | ɳ |  | ŋ |  |  |
| Tap |  |  | ɾ | ɽ |  |  |  |  |
| Fricative |  | f | s z | ʂ | ɕ ʑ | x ɣ |  | h |
| Lateral fricative |  |  | ɬ |  |  |  |  |  |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Near-open | æ |  |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w] [ʰ] [̃].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ء⟩ | ∅ |  |
| ⟨آ⟩ | [aː] |  |
| ⟨ئ⟩ | [j] |  |
| ⟨ئی⟩ | [j] |  |
| ⟨ا⟩ | [aː] | default [aː] · word initial [a] [i] [u] |
| ⟨ب⟩ | [b] |  |
| ⟨بھ⟩ | [b] |  |
| ⟨ت⟩ | [t̪] |  |
| ⟨تھ⟩ | [t̪ʰ] |  |
| ⟨ث⟩ | [s] |  |
| ⟨ج⟩ | [dʑ] |  |
| ⟨جھ⟩ | [dʑ] |  |
| ⟨ح⟩ | [h] |  |
| ⟨خ⟩ | [x] |  |
| ⟨د⟩ | [d̪] |  |
| ⟨دھ⟩ | [d̪] |  |
| ⟨ذ⟩ | [z] |  |
| ⟨ر⟩ | [ɾ] |  |
| ⟨ز⟩ | [z] |  |
| ⟨س⟩ | [s] |  |
| ⟨ش⟩ | [ɕ] |  |
| ⟨ص⟩ | [s] |  |
| ⟨ض⟩ | [z] |  |
| ⟨ط⟩ | [t̪] |  |
| ⟨ظ⟩ | [z] |  |
| ⟨ع⟩ | ∅ |  |
| ⟨غ⟩ | [ɣ] |  |
| ⟨ف⟩ | [f] |  |
| ⟨ق⟩ | [q] |  |
| ⟨ل⟩ | [l] |  |
| ⟨م⟩ | [m] |  |
| ⟨ن⟩ | [n] |  |
| ⟨نڑ⟩ | [ɳ] |  |
| ⟨نگ⟩ | [ŋ] |  |
| ⟨و⟩ | [oː] [uː] [o] [u] [w] | after vowel [w] · default [oː] [uː] [o] [u] · word initial [w] |
| ⟨وْ⟩ | [o] |  |
| ⟨َ⟩ | [a] |  |
| ⟨ُ⟩ | [u] |  |
| ⟨ِ⟩ | [i] |  |
| ⟨ْ⟩ | ∅ |  |
| ⟨ٞ⟩ | [æ] |  |
| ⟨ٹ⟩ | [ʈ] |  |
| ⟨ٹھ⟩ | [ʈʰ] |  |
| ⟨پ⟩ | [p] |  |
| ⟨پھ⟩ | [pʰ] |  |
| ⟨ڄ⟩ | [ʈʂ] |  |
| ⟨ڄھ⟩ | [ʈʂʰ] |  |
| ⟨څ⟩ | [t̪s] |  |
| ⟨څھ⟩ | [t̪sʰ] |  |
| ⟨چ⟩ | [tɕ] |  |
| ⟨چھ⟩ | [tɕʰ] |  |
| ⟨ڈ⟩ | [ɖ] |  |
| ⟨ڈھ⟩ | [ɖ] |  |
| ⟨ڑ⟩ | [ɽ] |  |
| ⟨ڑھ⟩ | [ɽ] |  |
| ⟨ژ⟩ | [ʑ] |  |
| ⟨ک⟩ | [k] |  |
| ⟨کھ⟩ | [kʰ] |  |
| ⟨گ⟩ | [ɡ] |  |
| ⟨گھ⟩ | [ɡ] |  |
| ⟨ں⟩ | [̃] |  |
| ⟨ھ⟩ | [ʰ] |  |
| ⟨ہ⟩ | [h] | default [h] · word final [a] |
| ⟨ی⟩ | [eː] [iː] [e] [i] [j] | after vowel [j] · default [eː] [iː] [e] [i] · word initial [j] |
| ⟨یْ⟩ | [e] |  |
| ⟨ے⟩ | [e] |  |
| ⟨ݪ⟩ | [ɬ] |  |
| ⟨ݭ⟩ | [ʂ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "gwc")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Garo](grt.md) · [Home](../index.md) · [Gawwada →](gwd.md)
