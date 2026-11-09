# Sinhala (`si`)

<!-- atlas:summary begin -->
Sinhala is an Indo-Aryan language, written in the Sinhala script. Glottolog places it in Sri Lanka. The `si` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `si` |
| ISO 639-3 | [sin](https://iso639-3.sil.org/code/sin), Sinhala |
| Glottolog | [sinh1246](https://glottolog.org/resource/languoid/id/sinh1246), Sinhala |
| Wikidata | [Q13267](https://www.wikidata.org/wiki/Q13267) |
| Wikipedia | [Sinhala language](https://en.wikipedia.org/wiki/Sinhala_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [Sri Lanka](by-region.md#sri-lanka) |
| Script | [Sinhala](by-script.md#sinhala) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1400, living |
| Parent | [Sanskrit](sa.md) `sa` |
| Explorer | [`si` in the data explorer](https://tigregotico.github.io/orthography2ipa/#si) |
| Spec file | [`si.json`](../../orthography2ipa/data/si.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Sinhala (Sri Lanka). Typologically diverges from mainland IA: prenasalised stops /ᵐb ⁿd ⁿɖ ᵑɡ ⁿdʒ/ are phonemic (rare in IA), vowels /æ æː/ absent in most other IA languages, dental stops /t d/ distinct from retroflex /ʈ ɖ/ (no dental diacritic). Diglossia: formal (literary) vs. colloquial speech differ markedly.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1991 to 2003. [Sources](#sources) lists them. The spec file writes all 68 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/si.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `si` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-masica1991"></a>Masica, C. (1991). *The Indo-Aryan Languages*. Cambridge University Press.
2. <a id="src-cardona_jain2003"></a>Cardona, G. & Jain, D. (eds.) (2003). *The Indo-Aryan Languages*. Routledge.
3. <a id="src-gair1998"></a>Gair, J.W. (1998). *Studies in South Asian Linguistics*. Oxford University Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `si` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 386 | 0.1394 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 59 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d d̪ t tʰ t̪ t̪ʰ ⁿd |  | ɖ ʈ ʈʰ ⁿɖ |  | k kʰ ɡ |  |
| Affricate |  |  |  | dʒ tʃ tʃʰ ⁿdʒ |  |  |  |  |
| Nasal | m |  | n |  | ɳ | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  | f | s | ʃ | ʂ |  |  | h |
| Approximant |  | ʋ |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  | ɭ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Close-mid | e eː |  | o oː |
| Mid |  | ə |  |
| Near-open | æ æː |  |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [bʱ] [dʒʱ] [dʱ] [d̪ʱ] [ou] [w] [ɖʱ] [ɡʱ] [ᵐb] [ᵑɡ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ං⟩ | [ŋ] |  |
| ⟨ඃ⟩ | [h] |  |
| ⟨අ⟩ | [a] [ə] |  |
| ⟨ආ⟩ | [aː] |  |
| ⟨ඇ⟩ | [æ] |  |
| ⟨ඈ⟩ | [æː] |  |
| ⟨ඉ⟩ | [i] |  |
| ⟨ඊ⟩ | [iː] |  |
| ⟨උ⟩ | [u] |  |
| ⟨ඌ⟩ | [uː] |  |
| ⟨එ⟩ | [e] |  |
| ⟨ඒ⟩ | [eː] |  |
| ⟨ඔ⟩ | [o] |  |
| ⟨ඕ⟩ | [oː] |  |
| ⟨ඖ⟩ | [ou] |  |
| ⟨ක⟩ | [k] |  |
| ⟨ඛ⟩ | [kʰ] [k] |  |
| ⟨ග⟩ | [ɡ] |  |
| ⟨ඝ⟩ | [ɡʱ] [ɡ] |  |
| ⟨ඞ⟩ | [ŋ] |  |
| ⟨ඟ⟩ | [ᵑɡ] |  |
| ⟨ච⟩ | [tʃ] |  |
| ⟨ඡ⟩ | [tʃ] [tʃʰ] |  |
| ⟨ජ⟩ | [dʒ] |  |
| ⟨ඣ⟩ | [dʒ] [dʒʱ] |  |
| ⟨ඤ⟩ | [ɲ] |  |
| ⟨ඦ⟩ | [ⁿdʒ] |  |
| ⟨ට⟩ | [ʈ] |  |
| ⟨ඨ⟩ | [ʈʰ] [ʈ] |  |
| ⟨ඩ⟩ | [ɖ] |  |
| ⟨ඪ⟩ | [ɖʱ] [ɖ] |  |
| ⟨ණ⟩ | [ɳ] |  |
| ⟨ඬ⟩ | [ⁿɖ] |  |
| ⟨ත⟩ | [t] |  |
| ⟨ථ⟩ | [t̪ʰ] [t̪] |  |
| ⟨ද⟩ | [d] |  |
| ⟨ධ⟩ | [d̪ʱ] [d̪] |  |
| ⟨න⟩ | [n] |  |
| ⟨ඳ⟩ | [ⁿd] |  |
| ⟨ප⟩ | [p] |  |
| ⟨ඵ⟩ | [pʰ] [p] |  |
| ⟨බ⟩ | [b] |  |
| ⟨භ⟩ | [bʱ] [b] |  |
| ⟨ම⟩ | [m] |  |
| ⟨ඹ⟩ | [ᵐb] |  |
| ⟨ය⟩ | [j] |  |
| ⟨ර⟩ | [r] |  |
| ⟨ල⟩ | [l] |  |
| ⟨ව⟩ | [ʋ] |  |
| ⟨ශ⟩ | [ʃ] |  |
| ⟨ෂ⟩ | [ʂ] |  |
| ⟨ස⟩ | [s] |  |
| ⟨හ⟩ | [h] |  |
| ⟨ළ⟩ | [ɭ] |  |
| ⟨ෆ⟩ | [f] |  |
| ⟨්⟩ | ∅ |  |
| ⟨ා⟩ | [aː] |  |
| ⟨ැ⟩ | [æ] |  |
| ⟨ෑ⟩ | [æː] |  |
| ⟨ි⟩ | [i] |  |
| ⟨ී⟩ | [iː] |  |
| ⟨ු⟩ | [u] |  |
| ⟨ූ⟩ | [uː] |  |
| ⟨ෙ⟩ | [e] |  |
| ⟨ේ⟩ | [eː] |  |
| ⟨ො⟩ | [o] |  |
| ⟨ෝ⟩ | [oː] |  |
| ⟨ෞ⟩ | [ou] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "si")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Sindhi](sd.md) · [Home](../index.md) · [Skolt Sami →](sms.md)
