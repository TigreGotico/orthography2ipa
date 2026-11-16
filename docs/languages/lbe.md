# Lak (`lbe`)

<!-- atlas:summary begin -->
Lak is a Nakh-Daghestanian language, written in the Cyrillic script. Glottolog places it in 5 countries. The `lbe` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `lbe` |
| ISO 639-3 | [lbe](https://iso639-3.sil.org/code/lbe), Lak |
| Glottolog | [lakk1252](https://glottolog.org/resource/languoid/id/lakk1252), Lak |
| Wikidata | [Q36206](https://www.wikidata.org/wiki/Q36206) |
| Wikipedia | [Lak language](https://en.wikipedia.org/wiki/Lak_language) |
| Family | [Nakh-Daghestanian](by-family.md#nakh-daghestanian) |
| Region | [Eurasia](by-region.md#eurasia) > [Azerbaijan](by-region.md#azerbaijan), [Georgia](by-region.md#georgia), [Kazakhstan](by-region.md#kazakhstan), [Russia](by-region.md#russia), [Ukraine](by-region.md#ukraine) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1938, living |
| Parent | [Nakh-Daghestanian](https://tigregotico.github.io/orthography2ipa/#x-clade-nakh1245) `x-clade-nakh1245` |
| Explorer | [`lbe` in the data explorer](https://tigregotico.github.io/orthography2ipa/#lbe) |
| Spec file | [`lbe.json`](../../orthography2ipa/data/lbe.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Lak (лакку маз), a Northeast Caucasian language of Dagestan, written in a Cyrillic alphabet (48 letters, later 54 with the doubled letters).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1955 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 53 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/lbe.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `lbe` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-lak_wiki"></a>Wikipedia contributors (2024). *Lak language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Lak_language)
2. <a id="src-zhirkov1955"></a>Zhirkov, L. I. (1955). *Лакский язык: фонетика и морфология (The Lak Language: Phonetics and Morphology)*. USSR Academy of Sciences.
3. <a id="src-lak_alphabet_wiki_table"></a>Wikipedia contributors (2026). *Lak language, Writing system: comparative Cyrillic / Latin / Perso-Arabic / IPA table*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Lak_language)
4. <a id="src-schulze_lak"></a>Schulze, Wolfgang (2007). *Lak (Northeast Caucasian): a grammatical sketch*. Ludwig-Maximilians-Universität München.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `lbe` | gold | lexicon-derived | CC BY 4.0 | 1048 | 0.0387 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 58 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʼ pː |  | d t tʼ tː |  |  | k kʼ kː ɡ | q qʼ qː |  | ʔ |
| Affricate |  |  | t͡s t͡sʼ t͡sː | t͡ʃ t͡ʃʼ t͡ʃː |  |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Fricative | β | f | s sː z | ʃ ʃʷ ʒ |  | x xː | ʁ χ χː | ħ | h |
| Approximant |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i y |  | u |
| Close-mid | e ø |  | o oˤ |
| Mid |  | ə |  |
| Open-mid | ɛ |  |  |
| Near-open | æ |  |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] [ə] [ɛ] |  |
| ⟨аь⟩ | [æ] [ɛ] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [w] [β] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨гъ⟩ | [ʁ] |  |
| ⟨гь⟩ | [h] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [e] [je] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] [y] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨кк⟩ | [kː] |  |
| ⟨къ⟩ | [qː] |  |
| ⟨кь⟩ | [qʼ] |  |
| ⟨кӏ⟩ | [kʼ] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨оь⟩ | [oˤ] [ø] |  |
| ⟨п⟩ | [p] |  |
| ⟨пп⟩ | [pː] |  |
| ⟨пӏ⟩ | [pʼ] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨сс⟩ | [sː] |  |
| ⟨т⟩ | [t] |  |
| ⟨тт⟩ | [tː] |  |
| ⟨тӏ⟩ | [tʼ] |  |
| ⟨у⟩ | [u] [y] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [χ] |  |
| ⟨хх⟩ | [χː] |  |
| ⟨хъ⟩ | [q] |  |
| ⟨хь⟩ | [x] |  |
| ⟨хьхь⟩ | [xː] |  |
| ⟨хӏ⟩ | [ħ] |  |
| ⟨ц⟩ | [t͡s] |  |
| ⟨цц⟩ | [t͡sː] |  |
| ⟨цӏ⟩ | [t͡sʼ] |  |
| ⟨ч⟩ | [t͡ʃ] |  |
| ⟨чч⟩ | [t͡ʃː] |  |
| ⟨чӏ⟩ | [t͡ʃʼ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ʃʷ] |  |
| ⟨ъ⟩ | [ʔ] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] [y] |  |
| ⟨я⟩ | [ja] [æ] |  |
| ⟨ё⟩ | [jo] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "lbe")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Ladino](lad.md) · [Home](../index.md) · [Lakota →](lkt.md)
