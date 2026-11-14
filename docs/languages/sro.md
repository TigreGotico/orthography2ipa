# Campidanese Sardinian (`sro`)

<!-- atlas:summary begin -->
Campidanese Sardinian is a Southern Romance language, written in the Latin script. Glottolog places it in Italy. The `sro` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sro` |
| ISO 639-3 | [sro](https://iso639-3.sil.org/code/sro), Campidanese Sardinian |
| Glottolog | [camp1261](https://glottolog.org/resource/languoid/id/camp1261), Campidanese Sardinian |
| Wikidata | [Q35348](https://www.wikidata.org/wiki/Q35348) |
| Wikipedia | [Campidanese dialect](https://en.wikipedia.org/wiki/Campidanese_dialect) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Southern Romance](by-family.md#indo-european--italic--romance--southern-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Italy](by-region.md#italy) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1000, living |
| Parent | [Sardinian](sc.md) `sc` |
| Explorer | [`sro` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sro) |
| Spec file | [`sro.json`](../../orthography2ipa/data/sro.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Campidanese Sardinian (ISO 639-3 sro). Southern Sardinian dialect group, more phonologically innovative than Logudorese: heavier intervocalic lenition of voiceless stops (p, t, k -> β, ð, ɣ), more retroflex consonants, and centuries of Aragonese-Catalan/Spanish contact influence on the lexicon.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 2019 to 2024. [Sources](#sources) lists them. The spec file writes no spelling of its own. It takes all 43 from [Sardinian](sc.md) `sc`.

The [spec file](../../orthography2ipa/data/sro.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sro` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-mereu2019_cagliari"></a>Mereu, Daniela (2019). *Illustrations of the IPA: Cagliari Sardinian*. Journal of the International Phonetic Association (Cambridge University Press). [cambridge.org](https://www.cambridge.org/core/journals/journal-of-the-international-phonetic-association/article/cagliari-sardinian/5B30AFE68BBB1CB462067B3C9A9CED45)
2. <a id="src-phoible"></a>Moran, Steven & McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/)
3. <a id="src-sil_sro"></a>SIL International (2024). *ISO 639-3: sro, Campidanese Sardinian*. SIL International. [iso639-3.sil.org](https://iso639-3.sil.org/code/sro)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sro")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Calabrian](it-IT-x-calabria.md) · [Home](../index.md) · [Canarian Spanish →](es-ES-x-canarias.md)
