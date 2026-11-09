# Telugu (`te`)

<!-- atlas:summary begin -->
Telugu is a Dravidian language, written in the Telugu script. Glottolog places it in India. The `te` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `te` |
| ISO 639-3 | [tel](https://iso639-3.sil.org/code/tel), Telugu |
| Glottolog | [telu1262](https://glottolog.org/resource/languoid/id/telu1262), Telugu |
| Wikidata | [Q8097](https://www.wikidata.org/wiki/Q8097) |
| Wikipedia | [Telugu language](https://en.wikipedia.org/wiki/Telugu_language) |
| Family | [Dravidian](by-family.md#dravidian) |
| Region | [Eurasia](by-region.md#eurasia) > [India](by-region.md#india) |
| Script | [Telugu](by-script.md#telugu) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1000, living |
| Ancestor | [Proto-Dravidian](https://tigregotico.github.io/orthography2ipa/#ta-x-proto-dravidia) `ta-x-proto-dravidia` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`te` in the data explorer](https://tigregotico.github.io/orthography2ipa/#te) |
| Spec file | [`te.json`](../../orthography2ipa/data/te.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Telugu (Andhra Pradesh and Telangana). Most widely spoken Dravidian language. Unlike Tamil, Telugu has aspirated stops from Sanskrit contact fully integrated into the phonological system. ⟨ళ⟩ = [ɭ] retroflex lateral phonemic. All vowels have short/long distinction.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1985 to 2003. [Sources](#sources) lists them. The spec file writes all 63 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/te.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `te` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Manna-Dora](https://tigregotico.github.io/orthography2ipa/#mju) `mju`: India, stub tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-krishnamurti2003"></a>Krishnamurti, B. (2003). *The Dravidian Languages*. Cambridge University Press.
2. <a id="src-krishnamurti_gwynn1985"></a>Krishnamurti, B. & Gwynn, J.P.L. (1985). *A Grammar of Modern Telugu*. Oxford University Press.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `te` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 5101 | 0.0990 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 49 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d̪ t̪ t̪ʰ | ɖ ʈ ʈʰ |  | k kʰ ɡ |  |
| Affricate |  |  |  |  | dʑ tɕ tɕʰ |  |  |
| Nasal | m ̃m |  | n | ɳ | ɲ | ŋ |  |
| Trill |  |  | r r̩ |  |  |  |  |
| Fricative |  |  | s | ʂ | ɕ |  | h |
| Approximant |  | ʋ |  |  | j |  |  |
| Lateral approximant |  |  | l | ɭ |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [ai] [au] [bʱ] [dʑʱ] [d̪ʱ] [w] [ɖʱ] [ɡʱ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ం⟩ | [̃m] [ŋ] |  |
| ⟨ః⟩ | [h] |  |
| ⟨అ⟩ | [a] |  |
| ⟨ఆ⟩ | [aː] |  |
| ⟨ఇ⟩ | [i] |  |
| ⟨ఈ⟩ | [iː] |  |
| ⟨ఉ⟩ | [u] |  |
| ⟨ఊ⟩ | [uː] |  |
| ⟨ఋ⟩ | [r̩] |  |
| ⟨ఎ⟩ | [e] |  |
| ⟨ఏ⟩ | [eː] |  |
| ⟨ఐ⟩ | [ai] |  |
| ⟨ఒ⟩ | [o] |  |
| ⟨ఓ⟩ | [oː] |  |
| ⟨ఔ⟩ | [au] |  |
| ⟨క⟩ | [k] |  |
| ⟨ఖ⟩ | [kʰ] |  |
| ⟨గ⟩ | [ɡ] |  |
| ⟨ఘ⟩ | [ɡʱ] |  |
| ⟨ఙ⟩ | [ŋ] |  |
| ⟨చ⟩ | [tɕ] |  |
| ⟨ఛ⟩ | [tɕʰ] |  |
| ⟨జ⟩ | [dʑ] |  |
| ⟨ఝ⟩ | [dʑʱ] |  |
| ⟨ఞ⟩ | [ɲ] |  |
| ⟨ట⟩ | [ʈ] |  |
| ⟨ఠ⟩ | [ʈʰ] |  |
| ⟨డ⟩ | [ɖ] |  |
| ⟨ఢ⟩ | [ɖʱ] |  |
| ⟨ణ⟩ | [ɳ] |  |
| ⟨త⟩ | [t̪] |  |
| ⟨థ⟩ | [t̪ʰ] |  |
| ⟨ద⟩ | [d̪] |  |
| ⟨ధ⟩ | [d̪ʱ] |  |
| ⟨న⟩ | [n] |  |
| ⟨ప⟩ | [p] |  |
| ⟨ఫ⟩ | [pʰ] |  |
| ⟨బ⟩ | [b] |  |
| ⟨భ⟩ | [bʱ] |  |
| ⟨మ⟩ | [m] |  |
| ⟨య⟩ | [j] |  |
| ⟨ర⟩ | [r] |  |
| ⟨ఱ⟩ | [r] |  |
| ⟨ల⟩ | [l] |  |
| ⟨ళ⟩ | [ɭ] |  |
| ⟨వ⟩ | [ʋ] |  |
| ⟨శ⟩ | [ɕ] |  |
| ⟨ష⟩ | [ʂ] |  |
| ⟨స⟩ | [s] |  |
| ⟨హ⟩ | [h] |  |
| ⟨ా⟩ | [aː] |  |
| ⟨ి⟩ | [i] |  |
| ⟨ీ⟩ | [iː] |  |
| ⟨ు⟩ | [u] |  |
| ⟨ూ⟩ | [uː] |  |
| ⟨ృ⟩ | [r̩] |  |
| ⟨ె⟩ | [e] |  |
| ⟨ే⟩ | [eː] |  |
| ⟨ై⟩ | [ai] |  |
| ⟨ొ⟩ | [o] |  |
| ⟨ో⟩ | [oː] |  |
| ⟨ౌ⟩ | [au] |  |
| ⟨్⟩ | ∅ |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "te")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Tatar](tt.md) · [Home](../index.md) · [Temne →](tem.md)
