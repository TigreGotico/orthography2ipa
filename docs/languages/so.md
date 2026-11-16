# Somali (`so`)

<!-- atlas:summary begin -->
Somali is a Cushitic language, written in the Latin script. Glottolog places it in Djibouti, Ethiopia, Kenya and Somalia. The `so` spec is at the research tier. It cites 7 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `so` |
| ISO 639-3 | [som](https://iso639-3.sil.org/code/som), Somali |
| Glottolog | [soma1255](https://glottolog.org/resource/languoid/id/soma1255), Somali |
| Wikidata | [Q13275](https://www.wikidata.org/wiki/Q13275) |
| Wikipedia | [Somali language](https://en.wikipedia.org/wiki/Somali_language) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Cushitic](by-family.md#afro-asiatic--cushitic) |
| Region | [Africa](by-region.md#africa) > [Djibouti](by-region.md#djibouti), [Ethiopia](by-region.md#ethiopia), [Kenya](by-region.md#kenya), [Somalia](by-region.md#somalia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1972, living |
| Parent | [Cushitic](https://tigregotico.github.io/orthography2ipa/#x-clade-cush1243) `x-clade-cush1243` |
| Explorer | [`so` in the data explorer](https://tigregotico.github.io/orthography2ipa/#so) |
| Spec file | [`so.json`](../../orthography2ipa/data/so.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Somali in the official Latin orthography (1972). C = pharyngeal /ʕ/, X = pharyngeal /ħ/, DH = retroflex /ɖ/, "sometimes pronounced as a flap" between vowels, which Mohamed 2013 writes [ɼ] in ⟨bádhi⟩ 'buttocks', because that description is a hedge the stop is kept as the second candidate.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 7 works, from 1905 to 2013. [Sources](#sources) lists them. The spec file writes all 34 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/so.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `so` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 7 works. 5 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-saeed1999"></a>Saeed, J.I. (1999). *Somali*. John Benjamins.
2. <a id="src-kirk1905"></a>Kirk, J.W.C. (1905). *A Grammar of the Somali Language, with Examples in Prose and Verse*. Cambridge University Press. Cited: 7. [archive.org](https://archive.org/details/grammarofsomalil00kirkuoft)
3. <a id="src-saeed1982"></a>Saeed, John I. (1982). *Central Somali: A Grammatical Outline*. Afroasiatic Linguistics 8(2), Undena Publications. Cited: 3-4. [archive.org](https://archive.org/details/SaeedCentralSomaliAGrammaticalOutline1982)
4. <a id="src-mohamed2013"></a>Mohamed, Ahmed (2013). *An Overview of the Interface Between Aspects of Somali Phonology and Morphology: A Resource Guide for ESL Teachers*. St. Cloud State University (MA thesis). Cited: 10. [orthographyclearinghouse.org](http://orthographyclearinghouse.org/theses/mohamedAnOverviewtheInterfacebetweenAspectsofSomaliPhonologyandMorphology.pdf)
5. <a id="src-bruhn_somali"></a>Bruhn, Daniel (2007). *Somali and the Nature of Morphophonological Alternations*. University of California, Berkeley (Linguistics 211B term paper). [linguistics.berkeley.edu](http://linguistics.berkeley.edu/~dwbruhn/211B_Somali-paper_dwbruhn.pdf)
6. <a id="src-armstrong1964"></a>Armstrong, Lilias E. (1964). *The phonetic structure of Somali*. Berlin: Gregg Press.
7. <a id="src-gabbard2010"></a>Gabbard, Kevin M. (2010). *A Phonological Analysis of Somali and the Guttural Consonants*. The Ohio State University (BA Linguistics Honors Thesis, advisor David A. Odden). [kb.osu.edu](https://kb.osu.edu/server/api/core/bitstreams/8c6e0078-b862-57e1-8d30-f076429ec823/content)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `kaikki` ([kaikki.org](https://kaikki.org/dictionary/)) | `so` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 230 | 0.5579 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 48 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b |  |  | d t |  | ɖ |  | k ɡ | q |  | ʔ |
| Affricate |  |  |  |  | dʒ tʃ |  |  |  |  |  |  |
| Nasal | m |  |  | n |  |  |  | ŋ |  |  |  |
| Trill |  |  |  | r |  |  |  |  |  |  |  |
| Tap |  |  |  |  |  | ɽ |  |  |  |  |  |
| Fricative | β | f | ð | s | ʃ |  |  | ɣ | χ | ħ ʕ | h |
| Approximant |  |  |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w] [ʔa] [ʔaː] [ʔe] [ʔeː] [ʔi] [ʔiː] [ʔo] [ʔoː] [ʔu] [ʔuː].

Tones: [◌́] high, [◌̀] low.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | [ʔ] |  |
| ⟨a⟩ | [a] | word initial [ʔa] |
| ⟨aa⟩ | [aː] | word initial [ʔaː] |
| ⟨b⟩ | [b] | intervocalic [b] [β] |
| ⟨c⟩ | [ʕ] |  |
| ⟨d⟩ | [d] | intervocalic [d] [ð] |
| ⟨dh⟩ | [ɖ] | intervocalic [ɽ] [ɖ] |
| ⟨e⟩ | [e] | word initial [ʔe] |
| ⟨ee⟩ | [eː] | word initial [ʔeː] |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] | intervocalic [ɡ] [ɣ] |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] | word initial [ʔi] |
| ⟨ii⟩ | [iː] | word initial [ʔiː] |
| ⟨j⟩ | [dʒ] [tʃ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [χ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o] | word initial [ʔo] |
| ⟨oo⟩ | [oː] | word initial [ʔoː] |
| ⟨q⟩ | [q] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] | word initial [ʔu] |
| ⟨uu⟩ | [uː] | word initial [ʔuː] |
| ⟨w⟩ | [w] | after a [u] [w] · after o [u] [w] · intervocalic [w] |
| ⟨x⟩ | [ħ] |  |
| ⟨y⟩ | [j] | after a [i] [j] · after e [i] [j] · after o [i] [j] · intervocalic [j] |
| ⟨’⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "so")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Slovenian](sl.md) · [Home](../index.md) · [Soninke →](snk.md)
