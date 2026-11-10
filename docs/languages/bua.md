# Buriat (`bua`)

<!-- atlas:summary begin -->
Buriat is a Mongolic language, written in the Cyrillic script. Glottolog places it in the Eurasia macroarea. The `bua` spec is at the research tier. It cites 3 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `bua` |
| ISO 639-3 | [bua](https://iso639-3.sil.org/code/bua), Buriat |
| Wikipedia | [Buryat language](https://en.wikipedia.org/wiki/Buryat_language) |
| Family | [Mongolic](by-family.md#mongolic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Proto-Mongolic (family node)](https://tigregotico.github.io/orthography2ipa/#xgn) `xgn` |
| Explorer | [`bua` in the data explorer](https://tigregotico.github.io/orthography2ipa/#bua) |
| Spec file | [`bua.json`](../../orthography2ipa/data/bua.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Buriat (Buryat) is a Mongolic language written in a Cyrillic alphabet that extends Russian with three letters: Ү (close front rounded /y/), Ө (rounded mid /o/) and Һ (/h/), "Since 1939, the Buryat literary language has employed a Cyrillic orthography with three extra letters (for h ö ü)" (Skribnik 2003:105).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1960 to 2024. [Sources](#sources) lists them. The spec file writes all 44 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/bua.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `bua` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-bua_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Buriat (buri1258)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/buri1258)
2. <a id="src-poppe1960"></a>Poppe, Nicholas (1960). *Buriat Grammar (Uralic and Altaic Series 2)*. Indiana University Publications.
3. <a id="src-skribnik2003"></a>Skribnik, E. (2003). *Buryat*. in J. Janhunen (ed.), The Mongolic Languages, Routledge Language Family Series, London. Cited: pp. 102-108. DOI [10.4324/9780203987919](https://doi.org/10.4324/9780203987919)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `bua` | gold | lexicon-derived | CC BY 4.0 | 1174 | 0.0398 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `bua` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 140 | 0.3571 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 45 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  | ts | tʃ |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ | ɕ | x | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː y yː | ɨ ɨː | u uː |
| Close-mid |  |  | o oː |
| Open-mid | ɛ ɛː |  | ɔ ɔː |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [ja] [je] [ju] [jɔ] [jɛ] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨аа⟩ | [aː] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [jɛ] [je] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨ии⟩ | [iː] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] | word final [ŋ] |
| ⟨о⟩ | [ɔ] |  |
| ⟨оо⟩ | [ɔː] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨уу⟩ | [uː] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ɕ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ыы⟩ | [ɨː] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [ɛ] |  |
| ⟨ээ⟩ | [ɛː] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ё⟩ | [jɔ] |  |
| ⟨ү⟩ | [y] |  |
| ⟨үү⟩ | [yː] |  |
| ⟨һ⟩ | [h] |  |
| ⟨ө⟩ | [o] |  |
| ⟨өө⟩ | [oː] |  |

Stress falls on the last syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 1 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `BUA_DEVOICE_B` | /b/ → [p], before [s] [ʃ] [t] [k] [x] | ⟨үбсүүн⟩ [ypsyːŋ] | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "bua")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Bulgarian](bg.md) · [Home](../index.md) · [Burmese →](my.md)
