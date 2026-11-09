# Korean (`ko`)

<!-- atlas:summary begin -->
Korean is a Koreanic language, written in the Hangul script. Glottolog places it in China, North Korea, Russia and South Korea. The `ko` spec is at the research tier. It cites 3 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ko` |
| Aliases | `kor` |
| ISO 639-3 | [kor](https://iso639-3.sil.org/code/kor), Korean |
| Glottolog | [kore1280](https://glottolog.org/resource/languoid/id/kore1280), Korean |
| Wikidata | [Q9176](https://www.wikidata.org/wiki/Q9176) |
| Wikipedia | [Korean language](https://en.wikipedia.org/wiki/Korean_language) |
| Family | [Koreanic](by-family.md#koreanic) |
| Region | [Eurasia](by-region.md#eurasia) > [China](by-region.md#china), [North Korea](by-region.md#north-korea), [Russia](by-region.md#russia), [South Korea](by-region.md#south-korea) |
| Script | [Hangul](by-script.md#hangul) (featural) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1200, living |
| Parent | [Proto-Koreanic (family node)](https://tigregotico.github.io/orthography2ipa/#pko) `pko` |
| Explorer | [`ko` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ko) |
| Spec file | [`ko.json`](../../orthography2ipa/data/ko.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Seoul standard. Three-way laryngeal contrast (lax/tense/aspirated). Extensive sandhi rules (nasalisation, lateralisation, tensification) apply at morpheme/word boundaries.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1978 to 1999. [Sources](#sources) lists them. The spec file writes all 118 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ko.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ko` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-sohn1999"></a>Sohn, H.-M. (1999). *The Korean Language*. Cambridge University Press.
2. <a id="src-ramsey1978"></a>Ramsey, S.R. (1978). *Accent and Morphology in Korean Dialects*. Tower Press.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `ko` | gold | crowd-scraped | MIT, each file its own | 62447 | 0.2319 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `ko` | generated | epitran-derived | CC0 1.0 | 6123 | 0.0728 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 56 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ p̚ p͈ | d t tʰ t̚ t͈ |  |  | k kʰ k̚ k͈ ɡ |  |
| Affricate |  |  |  | dʑ tɕ tɕʰ tɕ͈ t͈ɕ |  |  |
| Nasal | m | n |  |  | ŋ |  |
| Tap |  | ɾ |  |  |  |  |
| Fricative | ɸ | s s͈ |  | ç ɕ ɕ͈ |  | h ɦ |
| Lateral approximant |  | l | ɭ |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u ɯ |
| Close-mid | e ø | o |
| Open-mid | ɛ | ʌ |
| Open | a |  |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [jɛ] [jʌ] [wa] [we] [wi] [wɛ] [wʌ] [ɰi].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ᄀ⟩ | [k] |  |
| ⟨ᄁ⟩ | [k͈] |  |
| ⟨ᄂ⟩ | [n] |  |
| ⟨ᄃ⟩ | [t] |  |
| ⟨ᄄ⟩ | [t͈] |  |
| ⟨ᄅ⟩ | [ɾ] [l] |  |
| ⟨ᄆ⟩ | [m] |  |
| ⟨ᄇ⟩ | [p] |  |
| ⟨ᄈ⟩ | [p͈] |  |
| ⟨ᄉ⟩ | [s] |  |
| ⟨ᄊ⟩ | [s͈] |  |
| ⟨ᄋ⟩ | ∅ |  |
| ⟨ᄌ⟩ | [tɕ] |  |
| ⟨ᄍ⟩ | [t͈ɕ] |  |
| ⟨ᄎ⟩ | [tɕʰ] |  |
| ⟨ᄏ⟩ | [kʰ] |  |
| ⟨ᄐ⟩ | [tʰ] |  |
| ⟨ᄑ⟩ | [pʰ] |  |
| ⟨ᄒ⟩ | [h] |  |
| ⟨ᅡ⟩ | [a] |  |
| ⟨ᅢ⟩ | [ɛ] |  |
| ⟨ᅣ⟩ | [ja] |  |
| ⟨ᅤ⟩ | [jɛ] |  |
| ⟨ᅥ⟩ | [ʌ] |  |
| ⟨ᅦ⟩ | [e] |  |
| ⟨ᅧ⟩ | [jʌ] |  |
| ⟨ᅨ⟩ | [je] |  |
| ⟨ᅩ⟩ | [o] |  |
| ⟨ᅪ⟩ | [wa] |  |
| ⟨ᅫ⟩ | [wɛ] |  |
| ⟨ᅬ⟩ | [we] [ø] |  |
| ⟨ᅭ⟩ | [jo] |  |
| ⟨ᅮ⟩ | [u] |  |
| ⟨ᅯ⟩ | [wʌ] |  |
| ⟨ᅰ⟩ | [we] |  |
| ⟨ᅱ⟩ | [wi] [y] |  |
| ⟨ᅲ⟩ | [ju] |  |
| ⟨ᅳ⟩ | [ɯ] |  |
| ⟨ᅴ⟩ | [ɰi] |  |
| ⟨ᅵ⟩ | [i] |  |
| ⟨ᆨ⟩ | [k̚] |  |
| ⟨ᆩ⟩ | [k̚] |  |
| ⟨ᆪ⟩ | [k̚] |  |
| ⟨ᆫ⟩ | [n] |  |
| ⟨ᆬ⟩ | [n] |  |
| ⟨ᆭ⟩ | [n] |  |
| ⟨ᆮ⟩ | [t̚] |  |
| ⟨ᆯ⟩ | [ɭ] |  |
| ⟨ᆰ⟩ | [k̚] |  |
| ⟨ᆱ⟩ | [m] |  |
| ⟨ᆲ⟩ | [ɭ] |  |
| ⟨ᆳ⟩ | [ɭ] |  |
| ⟨ᆴ⟩ | [ɭ] |  |
| ⟨ᆵ⟩ | [p̚] |  |
| ⟨ᆶ⟩ | [ɭ] |  |
| ⟨ᆷ⟩ | [m] |  |
| ⟨ᆸ⟩ | [p̚] |  |
| ⟨ᆹ⟩ | [p̚] |  |
| ⟨ᆺ⟩ | [t̚] |  |
| ⟨ᆻ⟩ | [t̚] |  |
| ⟨ᆼ⟩ | [ŋ] |  |
| ⟨ᆽ⟩ | [t̚] |  |
| ⟨ᆾ⟩ | [t̚] |  |
| ⟨ᆿ⟩ | [k̚] |  |
| ⟨ᇀ⟩ | [t̚] |  |
| ⟨ᇁ⟩ | [p̚] |  |
| ⟨ᇂ⟩ | [t̚] |  |
| ⟨ㄱ⟩ | [k] |  |
| ⟨ㄲ⟩ | [k͈] |  |
| ⟨ㄳ⟩ | [k] |  |
| ⟨ㄴ⟩ | [n] |  |
| ⟨ㄵ⟩ | [n] |  |
| ⟨ㄶ⟩ | [n] |  |
| ⟨ㄷ⟩ | [t] |  |
| ⟨ㄸ⟩ | [t͈] |  |
| ⟨ㄹ⟩ | [ɾ] [l] |  |
| ⟨ㄺ⟩ | [k] |  |
| ⟨ㄻ⟩ | [m] |  |
| ⟨ㄼ⟩ | [l] |  |
| ⟨ㄽ⟩ | [l] |  |
| ⟨ㄾ⟩ | [l] |  |
| ⟨ㄿ⟩ | [p] |  |
| ⟨ㅀ⟩ | [l] |  |
| ⟨ㅁ⟩ | [m] |  |
| ⟨ㅂ⟩ | [p] |  |
| ⟨ㅃ⟩ | [p͈] |  |
| ⟨ㅄ⟩ | [p] |  |
| ⟨ㅅ⟩ | [s] |  |
| ⟨ㅆ⟩ | [s͈] |  |
| ⟨ㅇ⟩ | ∅ [ŋ] |  |
| ⟨ㅈ⟩ | [tɕ] |  |
| ⟨ㅉ⟩ | [tɕ͈] |  |
| ⟨ㅊ⟩ | [tɕʰ] |  |
| ⟨ㅋ⟩ | [kʰ] |  |
| ⟨ㅌ⟩ | [tʰ] |  |
| ⟨ㅍ⟩ | [pʰ] |  |
| ⟨ㅎ⟩ | [h] |  |
| ⟨ㅏ⟩ | [a] |  |
| ⟨ㅐ⟩ | [ɛ] |  |
| ⟨ㅑ⟩ | [ja] |  |
| ⟨ㅒ⟩ | [jɛ] |  |
| ⟨ㅓ⟩ | [ʌ] |  |
| ⟨ㅔ⟩ | [e] |  |
| ⟨ㅕ⟩ | [jʌ] |  |
| ⟨ㅖ⟩ | [je] |  |
| ⟨ㅗ⟩ | [o] |  |
| ⟨ㅘ⟩ | [wa] |  |
| ⟨ㅙ⟩ | [wɛ] |  |
| ⟨ㅚ⟩ | [we] |  |
| ⟨ㅛ⟩ | [jo] |  |
| ⟨ㅜ⟩ | [u] |  |
| ⟨ㅝ⟩ | [wʌ] |  |
| ⟨ㅞ⟩ | [we] |  |
| ⟨ㅟ⟩ | [wi] |  |
| ⟨ㅠ⟩ | [ju] |  |
| ⟨ㅡ⟩ | [ɯ] |  |
| ⟨ㅢ⟩ | [ɰi] |  |
| ⟨ㅣ⟩ | [i] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 4 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `KO_LAX_VOICING_K` | /k/ → [ɡ], after [a] [ɛ] [e] [i] [o] [u] [ʌ] [ɯ] and 11 more, before [a] [ɛ] [e] [i] [o] [u] [ʌ] [ɯ] and 5 more | ⟨한국⟩ [hanɡuk̚] | [Sohn 1999](#src-sohn1999), Kiaer & Cha 2012 |
| `KO_LAX_VOICING_T` | /t/ → [d], after [a] [ɛ] [e] [i] [o] [u] [ʌ] [ɯ] and 11 more, before [a] [ɛ] [e] [i] [o] [u] [ʌ] [ɯ] and 5 more | ⟨바다⟩ [pada] | [Sohn 1999](#src-sohn1999), Kiaer & Cha 2012 |
| `KO_LAX_VOICING_P` | /p/ → [b], after [a] [ɛ] [e] [i] [o] [u] [ʌ] [ɯ] and 11 more, before [a] [ɛ] [e] [i] [o] [u] [ʌ] [ɯ] and 5 more | - | [Sohn 1999](#src-sohn1999), Kiaer & Cha 2012 |
| `KO_LAX_VOICING_Tɕ` | /tɕ/ → [dʑ], after [a] [ɛ] [e] [i] [o] [u] [ʌ] [ɯ] and 11 more, before [a] [ɛ] [e] [i] [o] [u] [ʌ] [ɯ] and 5 more | - | [Sohn 1999](#src-sohn1999), Kiaer & Cha 2012 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ko")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Konkani](kok.md) · [Home](../index.md) · [Kotava →](avk.md)
