# Tetum (Tetun Dili / Tetun Prasa) (`tet`)

<!-- atlas:summary begin -->
Tetum (Tetun Dili / Tetun Prasa) is a Malayo-Polynesian language, written in the Latin script. Glottolog places it in Indonesia and Timor-Leste. The `tet` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `tet` |
| ISO 639-3 | [tet](https://iso639-3.sil.org/code/tet), Tetum |
| Glottolog | [tetu1245](https://glottolog.org/resource/languoid/id/tetu1245), Tetum |
| Wikidata | [Q34125](https://www.wikidata.org/wiki/Q34125) |
| Wikipedia | [Tetum language](https://en.wikipedia.org/wiki/Tetum_language) |
| Family | [Austronesian](by-family.md#austronesian) > [Malayo-Polynesian](by-family.md#austronesian--malayo-polynesian) |
| Region | [Papunesia](by-region.md#papunesia) > [Indonesia](by-region.md#indonesia), [Timor-Leste](by-region.md#timor-leste) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1800, living |
| Parent | [Malayo-Polynesian](https://tigregotico.github.io/orthography2ipa/#x-clade-mala1545) `x-clade-mala1545` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`tet` in the data explorer](https://tigregotico.github.io/orthography2ipa/#tet) |
| Spec file | [`tet.json`](../../orthography2ipa/data/tet.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Tetun Dili (Tetun Prasa), the Austronesian national and co-official language of Timor-Leste, written in the official orthography declared by Government Decree 1/2004 and curated by the Instituto Nacional de Linguística.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1999 to 2021. [Sources](#sources) lists them. The spec file writes all 36 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/tet.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `tet` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Tetun Terik (conservative rural Tetun)](https://tigregotico.github.io/orthography2ipa/#tet-x-terik) `tet-x-terik`: Indonesia, Timor-Leste, skeleton tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-williams_van_klinken2002"></a>Williams-van Klinken, C., Hajek, J. & Nordlinger, R. (2002). *Tetun Dili: A grammar of an East Timorese language*. Pacific Linguistics 528, The Australian National University. Cited: 6-13. [doi.org](https://doi.org/10.15144/PL-528)
2. <a id="src-avram2021"></a>Avram, A. A. (2021). *Contact-induced variation in Tetun Dili phonology*. Acta Linguistica Asiatica 11(1):75-98. Cited: 75-98. [doi.org](https://doi.org/10.4312/ala.11.1.75-98)
3. <a id="src-van_klinken1999"></a>van Klinken, C. (1999). *A grammar of the Fehan dialect of Tetun: An Austronesian language of West Timor*. Pacific Linguistics, The Australian National University.
4. <a id="src-hull2001"></a>Hull, G. (2001). *Timor-Leste: Identity, Language and Education*. University of Western Australia.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `primary_sources` | `tet` | gold | expert-human | Apache-2.0 (this repository). Each row quotes and cites a published example. | 55 | 0.0683 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 45 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  | c | k ɡ | ʔ |
| Affricate |  |  |  | dʒ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative | β | f v | s z | ʃ ʒ |  |  | h ɦ |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l ɫ |  | ʎ |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Near-close |  |  | ʊ |
| Close-mid | e eː |  | o oː |
| Open-mid | ɛ ɛː |  | ɔ ɔː |
| Near-open |  | ɐ |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | ∅ [ʔ] |  |
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [c] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] | before vowel [i] [j] |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨lh⟩ | [ʎ] |  |
| ⟨ll⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] | word final [n] [ŋ] |
| ⟨nh⟩ | [ɲ] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] | word final [ɾ] [r] · word initial [r] |
| ⟨s⟩ | [s] | word final [s] [ʃ] |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ʃ] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨á⟩ | [a] |  |
| ⟨é⟩ | [e] [ɛ] |  |
| ⟨í⟩ | [i] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ó⟩ | [o] [ɔ] |  |
| ⟨ú⟩ | [u] |  |
| ⟨’⟩ | ∅ [ʔ] |  |

Stress falls on the penult by default. A written ⟨á⟩ ⟨é⟩ ⟨í⟩ ⟨ó⟩ ⟨ú⟩ marks the stressed vowel.

Whole-word exceptions (3): ⟨bainhira⟩ [bainˈhira], ⟨bainhitu⟩ [bainˈhitu], ⟨bainhát⟩ [bainˈhaːt].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 7 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `TET_LENGTHEN_STRESSED_FINAL_A` | /a/ → [aː], stressed, with more context in the spec | ⟨hát⟩ [ˈhaːt] | [Williams-van 2002](#src-williams_van_klinken2002), Hajek & Nordlinger 2002 |
| `TET_LENGTHEN_STRESSED_FINAL_E` | /e/ → [eː], stressed, with more context in the spec | - | - |
| `TET_LENGTHEN_STRESSED_FINAL_OPEN_E` | /ɛ/ → [ɛː], stressed, with more context in the spec | - | - |
| `TET_LENGTHEN_STRESSED_FINAL_I` | /i/ → [iː], stressed, after a consonant, with more context in the spec | - | - |
| `TET_LENGTHEN_STRESSED_FINAL_O` | /o/ → [oː], stressed, with more context in the spec | - | - |
| `TET_LENGTHEN_STRESSED_FINAL_OPEN_O` | /ɔ/ → [ɔː], stressed, with more context in the spec | - | - |
| `TET_LENGTHEN_STRESSED_FINAL_U` | /u/ → [uː], stressed, after a consonant, with more context in the spec | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "tet")`. They are engine output, not reference transcriptions.

The next table sets the engine output against worked examples printed in a cited source, from the [primary-source gold](../evaluation/datasets.md#primary-source-gold-primary_sources). The rows are spread evenly over that set. The last column says whether the two transcriptions are the same string.

| Spelling | Printed in the source | Engine output | Source, page | Same |
|:--|:--|:--|:--|:--|
| baba | [ˈbaba] | [ˈbaba] | Williams-van Klinken 2002, p. 9 | yes |
| festa | [ˈfesta] | [ˈfesta] | Williams-van Klinken 2002, p. 9 | yes |
| kaixa | /kaiʃa/ | [ˈkaiʃa] | Williams-van Klinken 2002, p. 10 | no |
| ahi | [ˈahi] | [ˈahi] | Williams-van Klinken 2002, p. 10 | yes |
| fevreiru | /fevˈreiɾu/ | [feˈvreiru] | Williams-van Klinken 2002, p. 10 | no |
| yayasan | /jajasan/ | [jaˈjasan] | Williams-van Klinken 2002, p. 11 | no |
| hemu | [ˈhemu] | [ˈhemu] | Williams-van Klinken 2002, p. 11 | yes |
| sae | [ˈsa.e] | [ˈsae] | Williams-van Klinken 2002, p. 12 | no |
| mama | [ˈmãmã] | [ˈmama] | Williams-van Klinken 2002, p. 12 | no |
| kabén | /kaˈben/ | [kaˈbeːn] | Williams-van Klinken 2002, p. 12 | no |
| sinál | /siˈnal/ | [siˈnaːl] | Williams-van Klinken 2002, p. 12 | no |
| nanál | /naˈnal/ | [naˈnaːl] | Williams-van Klinken 2002, p. 12 | no |

Source: Williams-van Klinken, C., Hajek, J. & Nordlinger, R. (2002). *Tetun Dili: A grammar of an East Timorese language*. Pacific Linguistics 528, The Australian National University. [doi.org](https://doi.org/10.15144/PL-528)
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Tetelcingo Nahuatl](nhg.md) · [Home](../index.md) · [Tewa →](tew.md)
