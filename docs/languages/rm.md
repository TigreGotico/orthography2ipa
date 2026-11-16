# Romansh (`rm`)

<!-- atlas:summary begin -->
Romansh is a Gallo-Romance language, written in the Latin script. Glottolog places it in Austria, Italy and Switzerland. The `rm` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `rm` |
| ISO 639-3 | [roh](https://iso639-3.sil.org/code/roh), Romansh |
| Glottolog | [roma1326](https://glottolog.org/resource/languoid/id/roma1326), Romansh |
| Wikidata | [Q13199](https://www.wikidata.org/wiki/Q13199) |
| Wikipedia | [Romansh language](https://en.wikipedia.org/wiki/Romansh_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Gallo-Romance](by-family.md#indo-european--italic--romance--gallo-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Austria](by-region.md#austria), [Italy](by-region.md#italy), [Switzerland](by-region.md#switzerland) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1400, living |
| Parent | [Gallo-Romance](https://tigregotico.github.io/orthography2ipa/#x-clade-gallorom) `x-clade-gallorom` |
| Explorer | [`rm` in the data explorer](https://tigregotico.github.io/orthography2ipa/#rm) |
| Spec file | [`rm.json`](../../orthography2ipa/data/rm.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Romansh (Rumantsch). Rhaeto-Romance language of Graubünden, Switzerland. ~60,000 speakers. National language since 1938. Written standard: Rumantsch Grischun (1982). Five spoken idioms: Sursilvan, Sutsilvan, Surmiran, Puter, Vallader. Key features: (1) CA- palatalisation. (2) Front rounded vowels /y/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1996 to 1999. [Sources](#sources) lists them. The spec file writes all 31 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/rm.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `rm` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-liver1999"></a>Liver, R. (1999). *Rätoromanisch: Eine Einführung in das Bündnerromanische*. Narr.
2. <a id="src-maiden_parry1997"></a>Maiden, M. & Parry, M. (eds.) (1997). *The Dialects of Italy*. Routledge.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 35 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  | ts | dʒ tʃ | tɕ |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f v | s z | ʃ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  | ʎ |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u |
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
| ⟨c⟩ | [k] [ts] |  |
| ⟨ch⟩ | [k] [tɕ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [dʒ] |  |
| ⟨gh⟩ | [ɡ] |  |
| ⟨gl⟩ | [ʎ] |  |
| ⟨gn⟩ | [ɲ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] [z] |  |
| ⟨sch⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨tg⟩ | [tɕ] |  |
| ⟨tsch⟩ | [tʃ] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨z⟩ | [ts] |  |
| ⟨ü⟩ | [y] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "rm")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Romanian](ro-RO.md) · [Home](../index.md) · [Russian →](ru.md)
