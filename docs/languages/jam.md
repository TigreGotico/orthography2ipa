# Jamaican Patois (`jam`)

<!-- atlas:summary begin -->
Jamaican Patois is an English Creole language, written in the Latin script. Glottolog places it in Jamaica and Panama. The `jam` spec is at the research tier. It cites 4 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `jam` |
| ISO 639-3 | [jam](https://iso639-3.sil.org/code/jam), Jamaican Creole English |
| Glottolog | [jama1262](https://glottolog.org/resource/languoid/id/jama1262), Jamaican Creole English |
| Wikidata | [Q35939](https://www.wikidata.org/wiki/Q35939) |
| Wikipedia | [Jamaican Patois](https://en.wikipedia.org/wiki/Jamaican_Patois) |
| Family | [English Creole](by-family.md#english-creole) |
| Region | [North America](by-region.md#north-america) > [Jamaica](by-region.md#jamaica), [Panama](by-region.md#panama) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Explorer | [`jam` in the data explorer](https://tigregotico.github.io/orthography2ipa/#jam) |
| Spec file | [`jam.json`](../../orthography2ipa/data/jam.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Jamaican Patois (Jumiekan Kryuol) written in the Cassidy/JLU orthography (Cassidy 1961, standardised by the Jamaican Language Unit, UWI Mona, 2002). Phonemic by design: short vowels i e a o u, long vowels doubled (ii, aa, uu), diphthongs <ie> <uo> <ai> <ou>, <ch>=/tʃ/, <j>=/dʒ/, <sh>=/ʃ/, <zh>=/ʒ/, <ng>=/ŋ/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1980 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 36 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/jam.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `jam` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-cassidy_lepage1980"></a>Cassidy, Frederic G. & Le Page, Robert B. (1980). *Dictionary of Jamaican English (2nd ed.)*. Cambridge University Press.
2. <a id="src-jlu2002"></a>Jamaican Language Unit, University of the West Indies (2002). *Writing Jamaican the Jamaican Way / Ou fi Rait Jamiekan*. University of the West Indies, Mona.
3. <a id="src-harry2006"></a>Harry, Otelemate G. (2006). *Jamaican Creole (Illustrations of the IPA)*. Journal of the International Phonetic Association 36(1), 125-131. Cited: 126-127. [doi.org](https://doi.org/10.1017/S002510030600243X)
4. <a id="src-jampatois_wiki"></a>Wikipedia contributors (2024). *Jamaican Patois*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Jamaican_Patois)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `jam` | gold | lexicon-derived | MIT, each file its own | 1869 | 0.1684 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `jam` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 382 | 0.2762 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 36 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k kʲ ɡ ɡʲ |  |
| Affricate |  |  |  | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e | o |
| Open | a aː |  |

Sequences that the spec writes as one unit: [ai] [ie] [ou] [uo] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨ai⟩ | [ai] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gy⟩ | [ɡʲ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ie⟩ | [ie] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨ky⟩ | [kʲ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] |  |
| ⟨ou⟩ | [ou] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨uo⟩ | [uo] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨zh⟩ | [ʒ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "jam")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Iñupiaq](ik.md) · [Home](../index.md) · [Japanese →](ja.md)
