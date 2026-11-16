# Ingush (`inh`)

<!-- atlas:summary begin -->
Ingush is a Nakh-Daghestanian language, written in the Cyrillic script. Glottolog places it in Georgia and Russia. The `inh` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `inh` |
| ISO 639-3 | [inh](https://iso639-3.sil.org/code/inh), Ingush |
| Glottolog | [ingu1240](https://glottolog.org/resource/languoid/id/ingu1240), Ingush |
| Wikidata | [Q33509](https://www.wikidata.org/wiki/Q33509) |
| Wikipedia | [Ingush language](https://en.wikipedia.org/wiki/Ingush_language) |
| Family | [Nakh-Daghestanian](by-family.md#nakh-daghestanian) |
| Region | [Eurasia](by-region.md#eurasia) > [Georgia](by-region.md#georgia), [Russia](by-region.md#russia) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1938, living |
| Parent | [Nakh-Daghestanian](https://tigregotico.github.io/orthography2ipa/#x-clade-nakh1245) `x-clade-nakh1245` |
| Explorer | [`inh` in the data explorer](https://tigregotico.github.io/orthography2ipa/#inh) |
| Spec file | [`inh.json`](../../orthography2ipa/data/inh.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Ingush (гӏалгӏай мотт), a Nakh (Northeast Caucasian) language of Ingushetia, written in a Cyrillic alphabet since 1938.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 2011 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 53 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/inh.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `inh` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 4 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-ingush_language_wiki"></a>Wikipedia contributors (2024). *Ingush language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Ingush_language)
2. <a id="src-nichols2011_ingush_grammar"></a>Nichols, Johanna (2011). *Ingush Grammar*. University of California Press. Cited: 20.
3. <a id="src-omniglot_ingush"></a>Ager, Simon (2024). *Ingush language, alphabet and pronunciation*. Omniglot. [omniglot.com](https://www.omniglot.com/writing/ingush.htm)
4. <a id="src-schrijver2021_nakh_vowels"></a>Schrijver, Peter (2021). *A history of the vowel systems of the Nakh languages (East Caucasian), with special reference to umlaut in Chechen and Ingush*. Languages of the Caucasus 5. Cited: 88. [escholarship.org](https://escholarship.org/uc/item/7gc4x6tv)
5. <a id="src-nichols_berkeley_ingush_orthography"></a>Nichols, Johanna (2011). *Ingush Phonology and Orthography*. University of California, Berkeley (Ingush language project). [linguistics.berkeley.edu](https://linguistics.berkeley.edu/~ingush/orthography.html)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `inh` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 284 | 0.1632 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 55 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʼ |  | d t tʼ |  |  | k kʼ ɡ | q qʼ |  | ʔ |
| Affricate |  |  | t͡s t͡sʼ | t͡ʃ t͡ʃʼ |  |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |  |
| Trill |  |  | r r̥ |  |  |  |  |  |  |
| Fricative |  | f | s z | ʃ ʒ |  | x | ʁ | ħ ʕ | h |
| Approximant |  | ʋ |  |  | j |  |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e | o |
| Near-open | æ |  |
| Open | a |  |

Sequences that the spec writes as one unit: [ei] [ie] [ij] [ja] [je] [jo] [ju] [jæ] [oi] [ow] [oɑ] [ui] [uo] [uw].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨аь⟩ | [æ] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [ʋ] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨гӏ⟩ | [ʁ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [e] [je] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] [iː] |  |
| ⟨ий⟩ | [ij] |  |
| ⟨иэ⟩ | [ie] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨кх⟩ | [q] |  |
| ⟨къ⟩ | [qʼ] |  |
| ⟨кӏ⟩ | [kʼ] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨оа⟩ | [oɑ] |  |
| ⟨ов⟩ | [ow] |  |
| ⟨ои⟩ | [oi] |  |
| ⟨п⟩ | [p] |  |
| ⟨пӏ⟩ | [pʼ] |  |
| ⟨р⟩ | [r] |  |
| ⟨рхӏ⟩ | [r̥] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨тӏ⟩ | [tʼ] |  |
| ⟨у⟩ | [u] [uː] |  |
| ⟨ув⟩ | [uw] |  |
| ⟨уи⟩ | [ui] |  |
| ⟨уо⟩ | [uo] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨хь⟩ | [ħ] |  |
| ⟨хӏ⟩ | [h] |  |
| ⟨ц⟩ | [t͡s] |  |
| ⟨цӏ⟩ | [t͡sʼ] |  |
| ⟨ч⟩ | [t͡ʃ] |  |
| ⟨чӏ⟩ | [t͡ʃʼ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨ъ⟩ | [ʔ] |  |
| ⟨э⟩ | [e] |  |
| ⟨эи⟩ | [ei] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨яь⟩ | [jæ] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨ӏ⟩ | [ʕ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "inh")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Ingrian](izh.md) · [Home](../index.md) · [Interlingua →](ia.md)
