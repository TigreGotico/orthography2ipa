# Welsh (`cy`)

<!-- atlas:summary begin -->
Welsh is a Brythonic language, written in the Latin script. Glottolog places it in Argentina and United Kingdom. The `cy` spec is at the research tier. It cites 3 sources and has 3 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `cy` |
| ISO 639-3 | [cym](https://iso639-3.sil.org/code/cym), Welsh |
| Glottolog | [wels1247](https://glottolog.org/resource/languoid/id/wels1247), Welsh |
| Wikidata | [Q9309](https://www.wikidata.org/wiki/Q9309) |
| Wikipedia | [Welsh language](https://en.wikipedia.org/wiki/Welsh_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Celtic > Brythonic](by-family.md#indo-european--celtic--brythonic) |
| Region | [Eurasia](by-region.md#eurasia) > [Argentina](by-region.md#argentina), [United Kingdom](by-region.md#united-kingdom) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Ancestor | [Common Brythonic](https://tigregotico.github.io/orthography2ipa/#xbr) `xbr` |
| Explorer | [`cy` in the data explorer](https://tigregotico.github.io/orthography2ipa/#cy) |
| Spec file | [`cy.json`](../../orthography2ipa/data/cy.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Welsh (Cymraeg). ~880,000 speakers (2021 census). Voiceless lateral /ɬ/ (⟨ll⟩), voiceless nasal /m̥ n̥/ (⟨mh nh⟩), voiceless rhotic /r̥/ (⟨rh⟩), velar fricative /x/ (⟨ch⟩). Initial consonant mutation: soft, nasal, aspirate. Stress on penultimate syllable. Refs: Thomas (1996), Ball & Müller (2009).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1977 to 2003. [Sources](#sources) lists them. The spec file writes all 40 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/cy.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `cy` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-king2003"></a>King, G. (2003). *Modern Welsh: A Comprehensive Grammar*. Routledge.
2. <a id="src-macaulay1992"></a>MacAulay, D. (ed.) (1992). *The Celtic Languages*. Cambridge University Press.
3. <a id="src-jones_thomas1977"></a>Jones, G.E. & Thomas, A.R. (1977). *Welsh Phonology*. University of Wales Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `cy` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 14760 | 0.1823 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `cy` | generated | espeak-derived | CC BY 4.0 | 4662 | 0.2985 | no |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `cy` | generated | epitran-derived | CC0 1.0 | 18701 | 0.1172 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 44 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  |  | d t tʰ |  |  | k kʰ ɡ |  |
| Affricate |  |  |  |  | dʒ |  |  |  |
| Nasal | m m̥ |  |  | n n̥ |  |  | ŋ ŋ̊ |  |
| Trill |  |  |  | r r̥ |  |  |  |  |
| Fricative |  | f v | ð θ | s | ʃ |  | x | h |
| Lateral fricative |  |  |  | ɬ |  |  |  |  |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː | ɨ ɨː | uː |
| Near-close | ɪ |  | ʊ |
| Close-mid | eː |  | oː |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] |  |
| ⟨ch⟩ | [x] |  |
| ⟨d⟩ | [d] |  |
| ⟨dd⟩ | [ð] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [v] |  |
| ⟨ff⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ɪ] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [ɬ] |  |
| ⟨m⟩ | [m] |  |
| ⟨mh⟩ | [m̥] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ngh⟩ | [ŋ̊] |  |
| ⟨nh⟩ | [n̥] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [f] |  |
| ⟨r⟩ | [r] |  |
| ⟨rh⟩ | [r̥] |  |
| ⟨s⟩ | [s] |  |
| ⟨si⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [θ] |  |
| ⟨u⟩ | [ɨ] [i] |  |
| ⟨w⟩ | [ʊ] [w] |  |
| ⟨y⟩ | [ə] [ɨ] |  |
| ⟨â⟩ | [aː] |  |
| ⟨ê⟩ | [eː] |  |
| ⟨î⟩ | [iː] |  |
| ⟨ô⟩ | [oː] |  |
| ⟨û⟩ | [ɨː] |  |
| ⟨ŵ⟩ | [uː] |  |
| ⟨ŷ⟩ | [ɨː] [iː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "cy")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Wayuu](guc.md) · [Home](../index.md) · [West Coast Bajau →](bdr.md)
