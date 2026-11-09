# Abruzzese (`it-IT-x-abruzzo`)

<!-- atlas:summary begin -->
Abruzzese is an Italo-Romance variety, written in the Latin script. Its code names Italy. The `it-IT-x-abruzzo` spec is at the research tier. It cites 4 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `it-IT-x-abruzzo` |
| ISO 639-3 | [ita](https://iso639-3.sil.org/code/ita), Italian |
| Wikipedia | [Dialetti dell'Abruzzo](https://it.wikipedia.org/wiki/Dialetti_dell%27Abruzzo) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Italo-Romance](by-family.md#indo-european--italic--romance--italo-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Italy](by-region.md#italy) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1400, living |
| Parent | [Italo-Romance](https://tigregotico.github.io/orthography2ipa/#x-clade-italorom) `x-clade-italorom` |
| Explorer | [`it-IT-x-abruzzo` in the data explorer](https://tigregotico.github.io/orthography2ipa/#it-IT-x-abruzzo) |
| Spec file | [`it-IT-x-abruzzo.json`](../../orthography2ipa/data/it-IT-x-abruzzo.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Abruzzese. Southern Italo-Romance of Abruzzo and Molise. Part of the upper Southern Italian (Neapolitan) dialect continuum. ~1.5 million speakers. Key features: (1) Very strong vowel reduction (unstressed finals → [ə]). (2) Productive metaphony (vowel harmony). (3) Gemination preserved.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 4 works, from 1893 to 2009. [Sources](#sources) lists them. The spec file writes all 48 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/it-IT-x-abruzzo.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `it-IT-x-abruzzo` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-maiden_parry1997"></a>Maiden, M. & Parry, M. (eds.) (1997). *The Dialects of Italy*. Routledge.
2. <a id="src-loporcaro2009"></a>Loporcaro, M. (2009). *Profilo linguistico dei dialetti italiani*. Laterza.
3. <a id="src-lepschy_lepschy1988"></a>Lepschy, A.L. & Lepschy, G. (1988). *The Italian Language Today*. Hutchinson.
4. <a id="src-finamore1893"></a>Finamore, G. (1893). *Vocabolario dell'uso abruzzese*. S. Lapi, Città di Castello. Cited: 12-13. [archive.org](https://archive.org/details/vocabolariodell01finagoog)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 55 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bː p pː |  |  | d dː t tː |  |  | k kː ɡ ɡː |
| Affricate |  |  |  | dz dːz ts tːs | dʒ dːʒ tʃ tːʃ |  |  |
| Nasal | m mː | ɱ |  | n nː |  | ɲ | ŋ |
| Trill |  |  |  | r rː |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |
| Fricative | β | f fː v | ð | s sː z | ʃ ʒ |  | ɣ |
| Approximant |  |  |  |  |  | j |  |
| Lateral approximant |  |  |  | l lː |  | ʎ |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Open | a |  |  |

Sequences that the spec writes as one unit: [kw] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨bb⟩ | [bː] |  |
| ⟨c⟩ | [k] [tʃ] | before e [tʃ] · before i [tʃ] · default [k] |
| ⟨cc⟩ | [kː] [tːʃ] |  |
| ⟨ch⟩ | [k] |  |
| ⟨d⟩ | [d] |  |
| ⟨dd⟩ | [dː] |  |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨ff⟩ | [fː] |  |
| ⟨g⟩ | [ɡ] [dʒ] | before e [dʒ] · before i [dʒ] · default [ɡ] |
| ⟨gg⟩ | [ɡː] [dːʒ] | before e [dːʒ] · before i [dːʒ] · default [ɡː] |
| ⟨gh⟩ | [ɡ] |  |
| ⟨gl⟩ | [ʎ] |  |
| ⟨gn⟩ | [ɲ] |  |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [lː] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [mː] |  |
| ⟨n⟩ | [n] |  |
| ⟨nn⟩ | [nː] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨pp⟩ | [pː] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [r] |  |
| ⟨rr⟩ | [rː] |  |
| ⟨s⟩ | [s] [z] |  |
| ⟨sc⟩ | [ʃ] |  |
| ⟨ss⟩ | [sː] |  |
| ⟨t⟩ | [t] |  |
| ⟨tt⟩ | [tː] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨z⟩ | [ts] [dz] |  |
| ⟨zz⟩ | [tːs] [dːz] |  |
| ⟨à⟩ | [a] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [e] |  |
| ⟨ë⟩ | [ə] |  |
| ⟨ì⟩ | [i] |  |
| ⟨ò⟩ | [ɔ] |  |
| ⟨ó⟩ | [o] |  |
| ⟨ù⟩ | [u] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "it-IT-x-abruzzo")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Abkhaz](ab.md) · [Home](../index.md) · [Acehnese →](ace.md)
