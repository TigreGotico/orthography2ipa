# Sardinian (`sc`)

<!-- atlas:summary begin -->
Sardinian is a Southern Romance language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `sc` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sc` |
| ISO 639-3 | [srd](https://iso639-3.sil.org/code/srd), Sardinian |
| Glottolog | [sard1257](https://glottolog.org/resource/languoid/id/sard1257), Southern Romance |
| Wikidata | [Q33976](https://www.wikidata.org/wiki/Q33976) |
| Wikipedia | [Sardinian language](https://en.wikipedia.org/wiki/Sardinian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Southern Romance](by-family.md#indo-european--italic--romance--southern-romance) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1000, living |
| Parent | [Southern Romance](https://tigregotico.github.io/orthography2ipa/#x-clade-sard1257) `x-clade-sard1257` |
| Child lects | 4, see [Related lects](#related-lects) |
| Explorer | [`sc` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sc) |
| Spec file | [`sc.json`](../../orthography2ipa/data/sc.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Sardinian. THE most conservative Romance language. Primary archaic features: (1) Velars /k, ɡ/ preserved before front vowels (kentu 'hundred', not *centu). (2) 5-vowel system (no ɛ/e or ɔ/o split). (3) No diphthongisation of Latin ĕ, ŏ. (4) Retroflex consonants [ɖː] from Latin -LL-.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1986 to 1997. [Sources](#sources) lists them. The spec file writes all 43 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sc.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `sc` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Campidanese Sardinian](https://tigregotico.github.io/orthography2ipa/#sc-x-campidan) `sc-x-campidan`: Italy, skeleton tier
- [Logudorese Sardinian](https://tigregotico.github.io/orthography2ipa/#sc-x-logudoro) `sc-x-logudoro`: Italy, skeleton tier
- [Logudorese Sardinian](src.md) `src`: Italy, research tier
- [Campidanese Sardinian](sro.md) `sro`: Italy, research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-blasco_ferrer1986"></a>Blasco Ferrer, E. (1986). *La lingua sarda contemporanea*. Della Torre.
2. <a id="src-maiden_parry1997"></a>Maiden, M. & Parry, M. (eds.) (1997). *The Dialects of Italy*. Routledge.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `sc` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 703 | 0.0630 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 46 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Retroflex | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  | ɖː |  | k ɡ |
| Affricate |  |  |  | dz ts | dʒ |  |  |  |
| Nasal | m | ɱ |  | n |  |  | ɲ | ŋ |
| Trill |  |  |  | r rː |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative | β | f v | ð | s z | ʃ ʒ |  |  | ɣ |
| Approximant |  |  |  |  |  |  | j |  |
| Lateral approximant |  |  |  | l lː |  |  | ʎ |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [aj] [aw] [ej] [kw] [oj] [sk] [w] [ŋɡ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [aj] |  |
| ⟨au⟩ | [aw] |  |
| ⟨b⟩ | [b] [β] |  |
| ⟨c⟩ | [k] |  |
| ⟨ch⟩ | [k] |  |
| ⟨d⟩ | [d] |  |
| ⟨dd⟩ | [ɖː] |  |
| ⟨e⟩ | [e] |  |
| ⟨ei⟩ | [ej] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gh⟩ | [ɡ] |  |
| ⟨gl⟩ | [ʎ] |  |
| ⟨gn⟩ | [ɲ] |  |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [lː] [ɖː] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋɡ] |  |
| ⟨o⟩ | [o] |  |
| ⟨oi⟩ | [oj] |  |
| ⟨p⟩ | [p] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [r] |  |
| ⟨rr⟩ | [rː] |  |
| ⟨s⟩ | [s] [z] |  |
| ⟨sc⟩ | [sk] [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨tz⟩ | [ts] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] [β] |  |
| ⟨x⟩ | [ʒ] |  |
| ⟨z⟩ | [ts] [dz] |  |
| ⟨à⟩ | [a] |  |
| ⟨è⟩ | [e] [ɛ] |  |
| ⟨ì⟩ | [i] |  |
| ⟨ò⟩ | [o] [ɔ] |  |
| ⟨ù⟩ | [u] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sc")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Saraiki](skr.md) · [Home](../index.md) · [Sarsi →](srs.md)
