# Afar (`aa`)

<!-- atlas:summary begin -->
Afar is a Cushitic language, written in the Latin script. Glottolog places it in Djibouti, Eritrea and Ethiopia. The `aa` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `aa` |
| ISO 639-3 | [aar](https://iso639-3.sil.org/code/aar), Afar |
| Glottolog | [afar1241](https://glottolog.org/resource/languoid/id/afar1241), Afar |
| Wikidata | [Q27811](https://www.wikidata.org/wiki/Q27811) |
| Wikipedia | [Afar language](https://en.wikipedia.org/wiki/Afar_language) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Cushitic](by-family.md#afro-asiatic--cushitic) |
| Region | [Africa](by-region.md#africa) > [Djibouti](by-region.md#djibouti), [Eritrea](by-region.md#eritrea), [Ethiopia](by-region.md#ethiopia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1976, living |
| Parent | [Proto-Cushitic (family node)](https://tigregotico.github.io/orthography2ipa/#cus) `cus` |
| Explorer | [`aa` in the data explorer](https://tigregotico.github.io/orthography2ipa/#aa) |
| Spec file | [`aa.json`](../../orthography2ipa/data/aa.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Afar (Qafár af), Lowland East Cushitic, Djibouti/Eritrea/Ethiopia. Official Latin orthography (the 'Qafar Feera', adopted 1976) is phonemic: long vowels are written double (aa, ee, ii, oo, uu), <c> = /ħ/, <q> = /ʕ/, <x> = /ɖ/ (retroflex stop), <r> = /ɾ/. <ch>, <kh>, <sh>, <dh> occur mainly in loanwords.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1981 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 31 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/aa.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `aa` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-bliese1981"></a>Bliese, Loren F. (1981). *A Generative Grammar of Afar*. Summer Institute of Linguistics / University of Texas at Arlington.
2. <a id="src-afar_wiki"></a>Wikipedia contributors (2024). *Afar language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Afar_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `aa` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1713 | 0.2151 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 30 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b |  | d t |  | ɖ |  | k ɡ |  |  |
| Affricate |  |  |  | tʃ |  |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |  |
| Fricative |  | f | s | ʃ |  |  | x | ħ ʕ | h |
| Approximant |  |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open-mid |  | ʌ |
| Open | aː |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ʌ] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ħ] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dh⟩ | [ɖ] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [x] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨q⟩ | [ʕ] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ɖ] |  |
| ⟨y⟩ | [j] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "aa")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Adyghe](ady.md) · [Home](../index.md) · [Afrikaans →](af.md)
