# Odia (`or`)

<!-- atlas:summary begin -->
Odia is an Indo-Aryan language, written in the Odia script. Glottolog places it in India. The `or` spec is at the research tier. It cites 3 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `or` |
| ISO 639-3 | [ori](https://iso639-3.sil.org/code/ori), Oriya (macrolanguage) |
| Glottolog | [oriy1255](https://glottolog.org/resource/languoid/id/oriy1255), Odia |
| Wikidata | [Q33810](https://www.wikidata.org/wiki/Q33810) |
| Wikipedia | [Odia language](https://en.wikipedia.org/wiki/Odia_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [India](by-region.md#india) |
| Script | [Odia](by-script.md#odia) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1400, living |
| Parent | [Sanskrit](sa.md) `sa` |
| Explorer | [`or` in the data explorer](https://tigregotico.github.io/orthography2ipa/#or) |
| Spec file | [`or.json`](../../orthography2ipa/data/or.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Odia (Odisha). Distinct Odia script. Inherent vowel is /ɔ/ (like Bengali). Retroflex lateral ⟨ଳ⟩ = [ɭ] phonemic. Four-way laryngeal contrast.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1991 to 2003. [Sources](#sources) lists them. The spec file writes all 62 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/or.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `or` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-masica1991"></a>Masica, C. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
2. <a id="src-cardona_jain2003"></a>Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
3. <a id="src-mohanty1992"></a>Mohanty, P.K. (1992). *Odia: A Descriptive Grammar*. Munshiram Manoharlal.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `or` | generated | machine-generated | MIT, each file its own | 6216 | 0.1115 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `or` | generated | epitran-derived | CC0 1.0 | 7918 | 0.2689 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 50 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d̪ t̪ t̪ʰ |  | ɖ ʈ ʈʰ |  | k kʰ ɡ |  |
| Affricate |  |  |  |  |  | dʑ tɕ tɕʰ |  |  |
| Nasal | m |  | n |  | ɳ | ɲ | ŋ |  |
| Trill |  |  | r r̩ |  |  |  |  |  |
| Tap |  |  |  |  | ɽ |  |  |  |
| Fricative |  |  | s | ʃ | ʂ |  |  | h ɦ |
| Approximant |  | ʋ |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  | ɭ |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e | o |
| Open-mid |  | ɔ |
| Open | aː |  |

Sequences that the spec writes as one unit: [bʱ] [dʑʱ] [d̪ʱ] [oi] [ou] [w] [ɖʱ] [ɡʱ] [ɽʱ] [̃].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ଁ⟩ | [̃] |  |
| ⟨ଂ⟩ | [̃] |  |
| ⟨ଃ⟩ | [h] |  |
| ⟨ଅ⟩ | [ɔ] |  |
| ⟨ଆ⟩ | [aː] |  |
| ⟨ଇ⟩ | [i] |  |
| ⟨ଈ⟩ | [iː] |  |
| ⟨ଉ⟩ | [u] |  |
| ⟨ଊ⟩ | [uː] |  |
| ⟨ଋ⟩ | [r̩] |  |
| ⟨ଏ⟩ | [e] |  |
| ⟨ଐ⟩ | [oi] |  |
| ⟨ଓ⟩ | [o] |  |
| ⟨ଔ⟩ | [ou] |  |
| ⟨କ⟩ | [k] |  |
| ⟨ଖ⟩ | [kʰ] |  |
| ⟨ଗ⟩ | [ɡ] |  |
| ⟨ଘ⟩ | [ɡʱ] |  |
| ⟨ଙ⟩ | [ŋ] |  |
| ⟨ଚ⟩ | [tɕ] |  |
| ⟨ଛ⟩ | [tɕʰ] |  |
| ⟨ଜ⟩ | [dʑ] |  |
| ⟨ଝ⟩ | [dʑʱ] |  |
| ⟨ଞ⟩ | [ɲ] |  |
| ⟨ଟ⟩ | [ʈ] |  |
| ⟨ଠ⟩ | [ʈʰ] |  |
| ⟨ଡ⟩ | [ɖ] |  |
| ⟨ଡ଼⟩ | [ɽ] |  |
| ⟨ଢ⟩ | [ɖʱ] |  |
| ⟨ଢ଼⟩ | [ɽʱ] |  |
| ⟨ଣ⟩ | [ɳ] |  |
| ⟨ତ⟩ | [t̪] |  |
| ⟨ଥ⟩ | [t̪ʰ] |  |
| ⟨ଦ⟩ | [d̪] |  |
| ⟨ଧ⟩ | [d̪ʱ] |  |
| ⟨ନ⟩ | [n] |  |
| ⟨ପ⟩ | [p] |  |
| ⟨ଫ⟩ | [pʰ] |  |
| ⟨ବ⟩ | [b] [ʋ] |  |
| ⟨ଭ⟩ | [bʱ] |  |
| ⟨ମ⟩ | [m] |  |
| ⟨ଯ⟩ | [dʑ] [j] |  |
| ⟨ର⟩ | [r] |  |
| ⟨ଲ⟩ | [l] |  |
| ⟨ଳ⟩ | [ɭ] |  |
| ⟨ଶ⟩ | [ʃ] |  |
| ⟨ଷ⟩ | [ʂ] |  |
| ⟨ସ⟩ | [s] |  |
| ⟨ହ⟩ | [ɦ] |  |
| ⟨ା⟩ | [aː] |  |
| ⟨ି⟩ | [i] |  |
| ⟨ୀ⟩ | [iː] |  |
| ⟨ୁ⟩ | [u] |  |
| ⟨ୂ⟩ | [uː] |  |
| ⟨ୃ⟩ | [r̩] |  |
| ⟨େ⟩ | [e] |  |
| ⟨ୈ⟩ | [oi] |  |
| ⟨ୋ⟩ | [o] |  |
| ⟨ୌ⟩ | [ou] |  |
| ⟨୍⟩ | ∅ |  |
| ⟨ୟ⟩ | [j] |  |
| ⟨ୱ⟩ | [w] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "or")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Occitan](oc.md) · [Home](../index.md) · [Ojibwe →](oji.md)
