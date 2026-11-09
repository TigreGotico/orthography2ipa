# Bengali (`bn`)

<!-- atlas:summary begin -->
Bengali is an Indo-Aryan language, written in the Bengali script. Glottolog places it in Bangladesh, India and Nepal. The `bn` spec is at the research tier. It cites 5 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `bn` |
| ISO 639-3 | [ben](https://iso639-3.sil.org/code/ben), Bengali |
| Glottolog | [beng1280](https://glottolog.org/resource/languoid/id/beng1280), Bengali |
| Wikidata | [Q9610](https://www.wikidata.org/wiki/Q9610) |
| Wikipedia | [Bengali language](https://en.wikipedia.org/wiki/Bengali_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [Bangladesh](by-region.md#bangladesh), [India](by-region.md#india), [Nepal](by-region.md#nepal) |
| Script | [Bengali](by-script.md#bengali) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1800, living |
| Parent | [Sanskrit](sa.md) `sa` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`bn` in the data explorer](https://tigregotico.github.io/orthography2ipa/#bn) |
| Spec file | [`bn.json`](../../orthography2ipa/data/bn.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Colloquial Bengali (West Bengal/Kolkata, Rarhi-based), inherent vowel is /ɔ/ (not /ə/ like Hindi), ‘য’ = [dʑ] word-initially, [j] elsewhere, ‘শ’ and ‘ষ’ both → [ʃ] (two Sanskrit sibilants merged, unlike the Bangladeshi standard's ʃ/s contrast, Khan 2010), dental/retroflex contrast maintained, breathy stops phonemic but weakening in Bangladeshi speech.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 1960 to 2012. [Sources](#sources) lists them. The spec file writes all 61 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/bn.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `bn` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Noakhali](https://tigregotico.github.io/orthography2ipa/#oak) `oak`: stub tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-masica1991"></a>Masica, C. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
2. <a id="src-cardona_jain2003"></a>Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
3. <a id="src-thompson2012"></a>Thompson, H.S. (2012). *Bengali*. Routledge.
4. <a id="src-khan2010"></a>Khan, S.u.D. (2010). *Bengali (Bangladeshi Standard)*. Journal of the International Phonetic Association 40(2), 221-225. Cited: 221-225. [reed.edu](https://www.reed.edu/linguistics/khan/assets/Khan%202010%20Bengali%20Bangladeshi%20standard.pdf)
5. <a id="src-ferguson_chowdhury1960"></a>Ferguson, C.A. & Chowdhury, M. (1960). *The Phonemes of Bengali*. Language 36(1), 22-59.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `bn` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 6527 | 0.2395 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `bn` | generated | epitran-derived | CC0 1.0 | 30261 | 0.1581 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 46 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  | ɖ ʈ ʈʰ |  | k kʰ ɡ |  |
| Affricate |  |  |  |  |  | dʑ tɕ tɕʰ |  |  |
| Nasal | m |  | n |  |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |  |
| Tap |  |  |  |  | ɽ |  |  |  |
| Fricative |  | f v | s | ʃ |  |  |  | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid |  | ɔ |
| Near-open | æ |  |
| Open | a |  |

Sequences that the spec writes as one unit: [bʱ] [dʑʱ] [dʱ] [oi] [ou] [ri] [w] [ɖʱ] [ɡʱ] [ɽʱ] [̃].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ঁ⟩ | [̃] |  |
| ⟨ং⟩ | [ŋ] |  |
| ⟨ঃ⟩ | [h] |  |
| ⟨অ⟩ | [ɔ] |  |
| ⟨আ⟩ | [a] |  |
| ⟨ই⟩ | [i] |  |
| ⟨ঈ⟩ | [i] |  |
| ⟨উ⟩ | [u] |  |
| ⟨ঊ⟩ | [u] |  |
| ⟨ঋ⟩ | [ri] |  |
| ⟨এ⟩ | [e] [æ] |  |
| ⟨ঐ⟩ | [oi] |  |
| ⟨ও⟩ | [o] |  |
| ⟨ঔ⟩ | [ou] |  |
| ⟨ক⟩ | [k] |  |
| ⟨খ⟩ | [kʰ] |  |
| ⟨গ⟩ | [ɡ] |  |
| ⟨ঘ⟩ | [ɡʱ] |  |
| ⟨ঙ⟩ | [ŋ] |  |
| ⟨চ⟩ | [tɕ] |  |
| ⟨ছ⟩ | [tɕʰ] |  |
| ⟨জ⟩ | [dʑ] |  |
| ⟨ঝ⟩ | [dʑʱ] |  |
| ⟨ঞ⟩ | [n] |  |
| ⟨ট⟩ | [ʈ] |  |
| ⟨ঠ⟩ | [ʈʰ] |  |
| ⟨ড⟩ | [ɖ] |  |
| ⟨ড়⟩ | [ɽ] |  |
| ⟨ঢ⟩ | [ɖʱ] |  |
| ⟨ঢ়⟩ | [ɽʱ] |  |
| ⟨ণ⟩ | [n] |  |
| ⟨ত⟩ | [t] |  |
| ⟨থ⟩ | [tʰ] |  |
| ⟨দ⟩ | [d] |  |
| ⟨ধ⟩ | [dʱ] |  |
| ⟨ন⟩ | [n] |  |
| ⟨প⟩ | [p] |  |
| ⟨ফ⟩ | [pʰ] [f] |  |
| ⟨ব⟩ | [b] [w] |  |
| ⟨ভ⟩ | [bʱ] [v] |  |
| ⟨ম⟩ | [m] |  |
| ⟨য⟩ | [dʑ] [j] |  |
| ⟨য়⟩ | [j] |  |
| ⟨র⟩ | [r] |  |
| ⟨ল⟩ | [l] |  |
| ⟨শ⟩ | [ʃ] |  |
| ⟨ষ⟩ | [ʃ] |  |
| ⟨স⟩ | [s] [ʃ] |  |
| ⟨হ⟩ | [h] |  |
| ⟨া⟩ | [a] |  |
| ⟨ি⟩ | [i] |  |
| ⟨ী⟩ | [i] |  |
| ⟨ু⟩ | [u] |  |
| ⟨ূ⟩ | [u] |  |
| ⟨ৃ⟩ | [ri] |  |
| ⟨ে⟩ | [e] [æ] |  |
| ⟨ৈ⟩ | [oi] |  |
| ⟨ো⟩ | [o] |  |
| ⟨ৌ⟩ | [ou] |  |
| ⟨্⟩ | ∅ |  |
| ⟨ৎ⟩ | [t] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "bn")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Benasquese](an-x-benasque.md) · [Home](../index.md) · [Bhojpuri →](bho.md)
