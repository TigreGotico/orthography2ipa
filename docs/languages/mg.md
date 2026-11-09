# Malagasy (`mg`)

<!-- atlas:summary begin -->
Malagasy is a Malayo-Polynesian language, written in the Latin script. Glottolog places it in the Africa macroarea. The `mg` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mg` |
| ISO 639-3 | [mlg](https://iso639-3.sil.org/code/mlg), Malagasy |
| Glottolog | [mala1537](https://glottolog.org/resource/languoid/id/mala1537), Malagasic |
| Wikipedia | [Malagasy language](https://en.wikipedia.org/wiki/Malagasy_language) |
| Family | [Austronesian](by-family.md#austronesian) > [Malayo-Polynesian](by-family.md#austronesian--malayo-polynesian) |
| Region | [Africa](by-region.md#africa) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1823, living |
| Parent | [Malayo-Polynesian](https://tigregotico.github.io/orthography2ipa/#x-clade-mala1545) `x-clade-mala1545` |
| Explorer | [`mg` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mg) |
| Spec file | [`mg.json`](../../orthography2ipa/data/mg.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Malagasy, Austronesian (Barito) language of Madagascar, the standard is based on the Merina dialect and is written in the Latin script (21 letters, c, q, u, w, x are unused). Orthography is largely phonemic: ⟨o⟩ = /u/, ⟨ô⟩ = /o/ (mostly in loans, northern dialects have /o/ for ⟨o⟩), ⟨y⟩ = /i/ word-finally, ⟨j⟩ = /dz/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1951 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 35 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mg.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mg` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-dahl1951"></a>Dahl, Otto Christian (1951). *Malgache et Maanjan: une comparaison linguistique*. Egede-Instituttet, Oslo.
2. <a id="src-malagasy_wiki"></a>Wikipedia contributors (2025). *Malagasy language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Malagasy_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 34 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Retroflex | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | k ɡ |  |
| Affricate |  |  | dz ts | ɖʐ ʈʂ |  |  |
| Nasal | m |  | n |  |  |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f v | s z |  |  | h |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [mb] [mp] [nd] [ndz] [nt] [nts] [ŋk] [ŋɡ] [ɳɖʐ] [ɳʈʂ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨dr⟩ | [ɖʐ] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dz] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [mb] |  |
| ⟨mp⟩ | [mp] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [nd] |  |
| ⟨ndr⟩ | [ɳɖʐ] |  |
| ⟨ng⟩ | [ŋɡ] |  |
| ⟨nj⟩ | [ndz] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨nt⟩ | [nt] |  |
| ⟨ntr⟩ | [ɳʈʂ] |  |
| ⟨nts⟩ | [nts] |  |
| ⟨o⟩ | [u] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tr⟩ | [ʈʂ] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨v⟩ | [v] |  |
| ⟨y⟩ | [i] |  |
| ⟨z⟩ | [z] |  |
| ⟨ô⟩ | [o] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mg")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Makasar](mak.md) · [Home](../index.md) · [Malay →](ms.md)
