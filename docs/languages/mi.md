# Māori (`mi`)

<!-- atlas:summary begin -->
Māori is a Malayo-Polynesian language, written in the Latin script. Glottolog places it in New Zealand. The `mi` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mi` |
| ISO 639-3 | [mri](https://iso639-3.sil.org/code/mri), Maori |
| Glottolog | [maor1246](https://glottolog.org/resource/languoid/id/maor1246), Maori |
| Wikipedia | [Māori language](https://en.wikipedia.org/wiki/M%C4%81ori_language) |
| Family | [Austronesian](by-family.md#austronesian) > [Malayo-Polynesian](by-family.md#austronesian--malayo-polynesian) |
| Region | [Papunesia](by-region.md#papunesia) > [New Zealand](by-region.md#new-zealand) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1200, living |
| Parent | [Malayo-Polynesian](https://tigregotico.github.io/orthography2ipa/#x-clade-mala1545) `x-clade-mala1545` |
| Explorer | [`mi` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mi) |
| Spec file | [`mi.json`](../../orthography2ipa/data/mi.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Māori (te reo Māori), Eastern Polynesian, New Zealand. Highly regular phonemic orthography: 5 vowel qualities with a phonemic length contrast written with a macron (tohutō: ā ē ī ō ū), 10 consonants, plus the digraphs ⟨ng⟩ /ŋ/ and ⟨wh⟩ (most commonly [ɸ], [f] for many speakers, [ʔw]/[w] in some dialects).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1993 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 20 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mi.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mi` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-bauer1993"></a>Bauer, Winifred (1993). *Maori (Descriptive Grammars series)*. Routledge.
2. <a id="src-harlow2007"></a>Harlow, Ray (2007). *Māori: A Linguistic Introduction*. Cambridge University Press.
3. <a id="src-maori_phonology_wiki"></a>Wikipedia contributors (2024). *Māori phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/M%C4%81ori_phonology)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `mi` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1003 | 0.0719 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 24 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p |  | t |  | k |  |
| Affricate |  |  |  | tʃ |  |  |
| Nasal | m |  | n |  | ŋ |  |
| Trill |  |  | r |  |  |  |
| Tap |  |  | ɾ |  |  |  |
| Fricative | ɸ | f |  |  |  | h |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨e⟩ | [e] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨w⟩ | [w] |  |
| ⟨wh⟩ | [ɸ] [f] |  |
| ⟨ā⟩ | [aː] |  |
| ⟨ē⟩ | [eː] |  |
| ⟨ī⟩ | [iː] |  |
| ⟨ō⟩ | [oː] |  |
| ⟨ū⟩ | [uː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mi")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Muscogee](mus.md) · [Home](../index.md) · [N'Ko →](nqo.md)
