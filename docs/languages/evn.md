# Evenki (`evn`)

<!-- atlas:summary begin -->
Evenki is a Tungusic language, written in the Cyrillic script. Glottolog places it in the Eurasia macroarea. The `evn` spec is at the research tier. It cites 3 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `evn` |
| ISO 639-3 | [evn](https://iso639-3.sil.org/code/evn), Evenki |
| Wikipedia | [Evenki language](https://en.wikipedia.org/wiki/Evenki_language) |
| Family | [Tungusic](by-family.md#tungusic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Tungusic](https://tigregotico.github.io/orthography2ipa/#x-clade-tung1282) `x-clade-tung1282` |
| Explorer | [`evn` in the data explorer](https://tigregotico.github.io/orthography2ipa/#evn) |
| Spec file | [`evn.json`](../../orthography2ipa/data/evn.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Evenki is a Northern Tungusic language written in a Cyrillic alphabet (Nedjalkov 1997) that extends Russian with a single extra letter, Ӈ (velar nasal).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1997 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 39 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/evn.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `evn` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-evn_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Evenki (even1259)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/even1259)
2. <a id="src-nedjalkov1997"></a>Nedjalkov, Igor (1997). *Evenki (Descriptive Grammars)*. Routledge.
3. <a id="src-evn_orthography"></a>Wikipedia contributors (2024). *Evenki language, writing system and phonology*. [en.wikipedia.org](https://en.wikipedia.org/wiki/Evenki_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `evn` | gold | lexicon-derived | CC BY 4.0 | 1132 | 0.0970 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `evn` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 145 | 0.2447 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 37 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |
| Affricate |  |  | ts | tʃ |  |  |
| Nasal | m |  | n |  |  | ŋ |
| Trill |  |  | r |  |  |  |
| Fricative |  | f | s z | ʃ ʒ | ɕ | x |
| Approximant |  |  |  |  | j |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː | ɨ | u uː |
| Close-mid |  |  | o oː |
| Mid |  | ə əː |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨а̄⟩ | [aː] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [w] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [je] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨о̄⟩ | [oː] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ь⟩ | ∅ |  |
| ⟨э⟩ | [ə] |  |
| ⟨э̄⟩ | [əː] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨ӈ⟩ | [ŋ] |  |
| ⟨ӣ⟩ | [iː] |  |
| ⟨ӯ⟩ | [uː] |  |

Stress falls on the penult by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "evn")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Etruscan](ett.md) · [Home](../index.md) · [Ewe →](ee.md)
