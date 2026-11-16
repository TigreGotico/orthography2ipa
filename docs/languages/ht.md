# Haitian Creole (`ht`)

<!-- atlas:summary begin -->
Haitian Creole is a French Creole language, written in the Latin script. Glottolog places it in Dominican Republic and Haiti. The `ht` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ht` |
| ISO 639-3 | [hat](https://iso639-3.sil.org/code/hat), Haitian |
| Glottolog | [hait1244](https://glottolog.org/resource/languoid/id/hait1244), Haitian |
| Wikipedia | [Haitian Creole](https://en.wikipedia.org/wiki/Haitian_Creole) |
| Family | [French Creole](by-family.md#french-creole) |
| Region | [North America](by-region.md#north-america) > [Dominican Republic](by-region.md#dominican-republic), [Haiti](by-region.md#haiti) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1700, living |
| Explorer | [`ht` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ht) |
| Spec file | [`ht.json`](../../orthography2ipa/data/ht.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Haitian Creole (Kreyòl ayisyen), French-lexifier creole of Haiti, co-official since 1987. The IPN orthography (Institut Pédagogique National, 1979) is strictly phonemic: 32 symbols, no silent letters.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1989 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 31 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ht.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ht` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-haitian_creole_wiki"></a>Wikipedia contributors (2026). *Haitian Creole*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Haitian_Creole)
2. <a id="src-holm1989"></a>Holm, John (1989). *Pidgins and Creoles, Volume II: Reference Survey*. Cambridge University Press.
3. <a id="src-apics2013"></a>Michaelis, S.M., Maurer, P., Haspelmath, M. & Huber, M. (eds.) (2013). *The Atlas of Pidgin and Creole Language Structures (APiCS)*. Oxford University Press. [apics-online.info](https://apics-online.info/)
4. <a id="src-lefebvre1998"></a>Lefebvre, Claire (1998). *Creole Genesis and the Acquisition of Grammar: The Case of Haitian Creole*. Cambridge University Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ht` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1691 | 0.0302 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 33 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  | dʒ |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Fricative |  | f v | s z | ʃ ʒ |  | ɣ | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u ũ |
| Close-mid | e | o |
| Open-mid | ɛ ɛ̃ | ɔ ɔ̃ |
| Open | a ã |  |

Sequences that the spec writes as one unit: [w] [ɥi].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨an⟩ | [ã] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [ʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dj⟩ | [dʒ] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] |  |
| ⟨ou⟩ | [u] |  |
| ⟨oun⟩ | [ũ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [ɣ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨ui⟩ | [ɥi] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨ò⟩ | [ɔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 3 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `HT_NASAL_e` | /e/ → [ɛ̃], before a coda nasal | - | - |
| `HT_NASAL_o` | /o/ → [ɔ̃], before a coda nasal | - | - |
| `HT_NASAL_ABSORB` | /n m/ → ∅, in the coda, after a vowel | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ht")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Hadza](hts.md) · [Home](../index.md) · [Hakha Chin →](cnh.md)
