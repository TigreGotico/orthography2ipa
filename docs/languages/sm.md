# Samoan (`sm`)

<!-- atlas:summary begin -->
Samoan is a Malayo-Polynesian language, written in the Latin script. Glottolog places it in American Samoa and Samoa. The `sm` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `sm` |
| ISO 639-3 | [smo](https://iso639-3.sil.org/code/smo), Samoan |
| Glottolog | [samo1305](https://glottolog.org/resource/languoid/id/samo1305), Samoan |
| Wikipedia | [Samoan language](https://en.wikipedia.org/wiki/Samoan_language) |
| Family | [Austronesian](by-family.md#austronesian) > [Malayo-Polynesian](by-family.md#austronesian--malayo-polynesian) |
| Region | [Papunesia](by-region.md#papunesia) > [American Samoa](by-region.md#american-samoa), [Samoa](by-region.md#samoa) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1834, living |
| Parent | [Malayo-Polynesian](https://tigregotico.github.io/orthography2ipa/#x-clade-mala1545) `x-clade-mala1545` |
| Explorer | [`sm` in the data explorer](https://tigregotico.github.io/orthography2ipa/#sm) |
| Spec file | [`sm.json`](../../orthography2ipa/data/sm.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Samoan (Gagana Sāmoa), Polynesian. Fourteen native letters: vowels a e i o u (long: ā ē ī ō ū, the macron faʻamamafa), consonants f g l m n p s t v plus the koma liliu ⟨ʻ⟩ = glottal stop /ʔ/. ⟨g⟩ is the velar nasal /ŋ/, never a stop. ⟨h k r⟩ occur only in loanwords.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1992 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 23 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/sm.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `sm` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-mosel_hovdhaugen1992"></a>Mosel, Ulrike & Hovdhaugen, Even (1992). *Samoan Reference Grammar*. Scandinavian University Press.
2. <a id="src-samoan_language_wiki"></a>Wikipedia contributors (2026). *Samoan language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Samoan_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 24 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | p |  | t | k | ʔ |
| Nasal | m |  | n | ŋ |  |
| Tap |  |  | ɾ |  |  |
| Fricative |  | f v | s |  | h |
| Lateral approximant |  |  | l |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | iː | u uː |
| Near-close | ɪ |  |
| Close-mid | eː | o |
| Open-mid | ɛ | ɔː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ŋ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ɪ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨ā⟩ | [aː] |  |
| ⟨ē⟩ | [eː] |  |
| ⟨ī⟩ | [iː] |  |
| ⟨ō⟩ | [ɔː] |  |
| ⟨ū⟩ | [uː] |  |
| ⟨ʻ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "sm")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Salar](slr.md) · [Home](../index.md) · [Samogitian →](sgs.md)
