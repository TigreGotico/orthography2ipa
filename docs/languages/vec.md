# Venetian (`vec`)

<!-- atlas:summary begin -->
Venetian is an Italo-Romance language, written in the Latin script. Glottolog places it in 5 countries. The `vec` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `vec` |
| ISO 639-3 | [vec](https://iso639-3.sil.org/code/vec), Venetian |
| Glottolog | [vene1258](https://glottolog.org/resource/languoid/id/vene1258), Venetian |
| Wikidata | [Q32724](https://www.wikidata.org/wiki/Q32724) |
| Wikipedia | [Venetian language](https://en.wikipedia.org/wiki/Venetian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Italo-Romance](by-family.md#indo-european--italic--romance--italo-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Brazil](by-region.md#brazil), [Croatia](by-region.md#croatia), [Italy](by-region.md#italy), [Mexico](by-region.md#mexico), [Slovenia](by-region.md#slovenia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Parent | [Italo-Romance](https://tigregotico.github.io/orthography2ipa/#x-clade-italorom) `x-clade-italorom` |
| Explorer | [`vec` in the data explorer](https://tigregotico.github.io/orthography2ipa/#vec) |
| Spec file | [`vec.json`](../../orthography2ipa/data/vec.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Venetian. NE Italo-Romance language of Veneto, Trentino, Friuli, and Istria. ~3.8 million speakers. Reference: Veneziano. Straddles Gallo-Italic / Italo-Romance boundary. Key features: (1) 7-vowel system (Italo-Romance). (2) Interdental fricatives /θ, ð/ in some varieties. (3) Intervocalic lenition (Gallo-Italic-like).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1988 to 2009. [Sources](#sources) lists them. The spec file writes all 41 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/vec.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `vec` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-maiden_parry1997"></a>Maiden, M. & Parry, M. (eds.) (1997). *The Dialects of Italy*. Routledge.
2. <a id="src-loporcaro2009"></a>Loporcaro, M. (2009). *Profilo linguistico dei dialetti italiani*. Laterza.
3. <a id="src-lepschy_lepschy1988"></a>Lepschy, A.L. & Lepschy, G. (1988). *The Italian Language Today*. Hutchinson.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 40 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |
| Affricate |  |  |  | dz ts | dʒ tʃ |  |  |
| Nasal | m | ɱ |  | n nː |  | ɲ | ŋ |
| Trill |  |  |  | r rː |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |
| Fricative |  | f v | ð θ | s sː z | ʃ |  |  |
| Approximant |  |  |  |  |  | j | ɰ |
| Lateral approximant |  |  |  | l lː |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [kw] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] [tʃ] |  |
| ⟨ch⟩ | [k] |  |
| ⟨d⟩ | [d] |  |
| ⟨dh⟩ | [ð] |  |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [dʒ] |  |
| ⟨gh⟩ | [ɡ] |  |
| ⟨gn⟩ | [ɲ] |  |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [lː] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨nn⟩ | [nː] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [r] |  |
| ⟨rr⟩ | [rː] |  |
| ⟨s⟩ | [s] [z] |  |
| ⟨sc⟩ | [ʃ] |  |
| ⟨ss⟩ | [sː] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [θ] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨x⟩ | [z] |  |
| ⟨z⟩ | [ts] [dz] |  |
| ⟨à⟩ | [a] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [e] |  |
| ⟨ì⟩ | [i] |  |
| ⟨ò⟩ | [ɔ] |  |
| ⟨ó⟩ | [o] |  |
| ⟨ù⟩ | [u] |  |
| ⟨ł⟩ | [ɰ] [l] ∅ |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "vec")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Venda](ve.md) · [Home](../index.md) · [Venezuelan Spanish →](es-VE.md)
