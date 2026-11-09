# Kannada (`kn`)

<!-- atlas:summary begin -->
Kannada is a Dravidian language, written in the Kannada script. Glottolog places it in India. The `kn` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kn` |
| ISO 639-3 | [kan](https://iso639-3.sil.org/code/kan), Kannada |
| Glottolog | [nucl1305](https://glottolog.org/resource/languoid/id/nucl1305), Kannada |
| Wikidata | [Q33673](https://www.wikidata.org/wiki/Q33673) |
| Wikipedia | [Kannada](https://en.wikipedia.org/wiki/Kannada) |
| Family | [Dravidian](by-family.md#dravidian) |
| Region | [Eurasia](by-region.md#eurasia) > [India](by-region.md#india) |
| Script | [Kannada](by-script.md#kannada) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 900, living |
| Ancestor | [Proto-Dravidian](https://tigregotico.github.io/orthography2ipa/#ta-x-proto-dravidia) `ta-x-proto-dravidia` |
| Explorer | [`kn` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kn) |
| Spec file | [`kn.json`](../../orthography2ipa/data/kn.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Kannada (Karnataka). Phonological system closely parallel to Telugu. ⟨ಳ⟩ = [ɭ] retroflex lateral phonemic. Archaic ⟨ೞ⟩ = [ɻ] (retroflex approximant, cf. Tamil ⟨ழ⟩, Malayalam ⟨ഴ⟩, Krishnamurti 2003) survives in some dialects, ⟨ಱ⟩ is a separate archaic letter, kept here as a plain tap.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1970 to 2003. [Sources](#sources) lists them. The spec file writes all 64 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kn.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kn` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-krishnamurti2003"></a>Krishnamurti, B. (2003). *The Dravidian Languages*. Cambridge University Press.
2. <a id="src-sridhar1990"></a>Sridhar, S.N. (1990). *Kannada*. Routledge.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
4. <a id="src-bright1970"></a>Bright, William (1970). *Phonological Rules in Literary and Colloquial Kannada*. Journal of the American Oriental Society 90(1):140-144. Cited: 140-144. [jstor.org](https://www.jstor.org/stable/598435)
5. <a id="src-schiffman1979"></a>Schiffman, Harold F. (1979). *A Reference Grammar of Spoken Kannada*. University of Washington Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `kn` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1706 | 0.0161 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 53 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d̪ t̪ t̪ʰ |  | ɖ ʈ ʈʰ |  | k kʰ ɡ |  |  |
| Affricate |  |  |  | dʒ tʃ tʃʰ |  |  |  |  |  |
| Nasal | m |  | n n̪ |  | ɳ | ɲ | ŋ | ɴ |  |
| Trill |  |  | r r̩ |  |  |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |  |
| Fricative |  |  | s | ʃ | ʂ | ɕ |  |  | h |
| Approximant |  | ʋ |  |  | ɻ | j |  |  |  |
| Lateral approximant |  |  | l |  | ɭ |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Close-mid | e eː |  | o oː |
| Near-open |  | ɐ |  |
| Open | aː |  |  |

Sequences that the spec writes as one unit: [bʱ] [dʒʱ] [d̪ʱ] [w] [ɐi] [ɐu] [ɖʱ] [ɡʱ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ಂ⟩ | [ɴ] |  |
| ⟨ಃ⟩ | [h] |  |
| ⟨ಅ⟩ | [ɐ] |  |
| ⟨ಆ⟩ | [aː] |  |
| ⟨ಇ⟩ | [i] |  |
| ⟨ಈ⟩ | [iː] |  |
| ⟨ಉ⟩ | [u] |  |
| ⟨ಊ⟩ | [uː] |  |
| ⟨ಋ⟩ | [r̩] |  |
| ⟨ಎ⟩ | [e] |  |
| ⟨ಏ⟩ | [eː] |  |
| ⟨ಐ⟩ | [ɐi] |  |
| ⟨ಒ⟩ | [o] |  |
| ⟨ಓ⟩ | [oː] |  |
| ⟨ಔ⟩ | [ɐu] |  |
| ⟨ಕ⟩ | [k] |  |
| ⟨ಖ⟩ | [kʰ] |  |
| ⟨ಗ⟩ | [ɡ] |  |
| ⟨ಘ⟩ | [ɡʱ] |  |
| ⟨ಙ⟩ | [ŋ] |  |
| ⟨ಚ⟩ | [tʃ] |  |
| ⟨ಛ⟩ | [tʃʰ] |  |
| ⟨ಜ⟩ | [dʒ] |  |
| ⟨ಝ⟩ | [dʒʱ] |  |
| ⟨ಞ⟩ | [ɲ] |  |
| ⟨ಟ⟩ | [ʈ] |  |
| ⟨ಠ⟩ | [ʈʰ] |  |
| ⟨ಡ⟩ | [ɖ] |  |
| ⟨ಢ⟩ | [ɖʱ] |  |
| ⟨ಣ⟩ | [ɳ] |  |
| ⟨ತ⟩ | [t̪] |  |
| ⟨ಥ⟩ | [t̪ʰ] |  |
| ⟨ದ⟩ | [d̪] |  |
| ⟨ಧ⟩ | [d̪ʱ] |  |
| ⟨ನ⟩ | [n] |  |
| ⟨ಪ⟩ | [p] |  |
| ⟨ಫ⟩ | [pʰ] |  |
| ⟨ಬ⟩ | [b] |  |
| ⟨ಭ⟩ | [bʱ] |  |
| ⟨ಮ⟩ | [m] |  |
| ⟨ಯ⟩ | [j] |  |
| ⟨ರ⟩ | [ɾ] |  |
| ⟨ಱ⟩ | [r] |  |
| ⟨ಲ⟩ | [l] |  |
| ⟨ಳ⟩ | [ɭ] |  |
| ⟨ವ⟩ | [ʋ] |  |
| ⟨ಶ⟩ | [ʃ] |  |
| ⟨ಷ⟩ | [ʂ] |  |
| ⟨ಸ⟩ | [s] |  |
| ⟨ಹ⟩ | [h] |  |
| ⟨ಾ⟩ | [aː] |  |
| ⟨ಿ⟩ | [i] |  |
| ⟨ೀ⟩ | [iː] |  |
| ⟨ು⟩ | [u] |  |
| ⟨ೂ⟩ | [uː] |  |
| ⟨ೃ⟩ | [r̩] |  |
| ⟨ೆ⟩ | [e] |  |
| ⟨ೇ⟩ | [eː] |  |
| ⟨ೈ⟩ | [ɐi] |  |
| ⟨ೊ⟩ | [o] |  |
| ⟨ೋ⟩ | [oː] |  |
| ⟨ೌ⟩ | [ɐu] |  |
| ⟨್⟩ | ∅ |  |
| ⟨ೞ⟩ | [ɻ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 5 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `KN_ANUS_VELAR` | /ɴ/ → [ŋ], before ⟨ಕ⟩ ⟨ಖ⟩ ⟨ಗ⟩ ⟨ಘ⟩ ⟨ಙ⟩ | - | [Krishnamurti 2003](#src-krishnamurti2003), [Sridhar 1990](#src-sridhar1990) |
| `KN_ANUS_PALATAL` | /ɴ/ → [ɲ], before ⟨ಚ⟩ ⟨ಛ⟩ ⟨ಜ⟩ ⟨ಝ⟩ ⟨ಞ⟩ | - | [Krishnamurti 2003](#src-krishnamurti2003), [Sridhar 1990](#src-sridhar1990) |
| `KN_ANUS_RETROFLEX` | /ɴ/ → [ɳ], before ⟨ಟ⟩ ⟨ಠ⟩ ⟨ಡ⟩ ⟨ಢ⟩ ⟨ಣ⟩ | - | [Krishnamurti 2003](#src-krishnamurti2003), [Sridhar 1990](#src-sridhar1990) |
| `KN_ANUS_DENTAL` | /ɴ/ → [n̪], before ⟨ತ⟩ ⟨ಥ⟩ ⟨ದ⟩ ⟨ಧ⟩ ⟨ನ⟩ | - | [Krishnamurti 2003](#src-krishnamurti2003), [Sridhar 1990](#src-sridhar1990) |
| `KN_ANUS_DEFAULT` | /ɴ/ → [m] | - | [Krishnamurti 2003](#src-krishnamurti2003), [Sridhar 1990](#src-sridhar1990) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kn")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kalmyk](xal.md) · [Home](../index.md) · [Kanuri →](kr.md)
