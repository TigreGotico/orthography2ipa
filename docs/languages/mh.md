# Marshallese (`mh`)

<!-- atlas:summary begin -->
Marshallese is an Austronesian language, written in the Latin script. Glottolog places it in Marshall Islands. The `mh` spec is at the research tier. It cites 7 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mh` |
| ISO 639-3 | [mah](https://iso639-3.sil.org/code/mah), Marshallese |
| Glottolog | [mars1254](https://glottolog.org/resource/languoid/id/mars1254), Marshallese |
| Wikidata | [Q36280](https://www.wikidata.org/wiki/Q36280) |
| Wikipedia | [Marshallese language](https://en.wikipedia.org/wiki/Marshallese_language) |
| Family | [Austronesian](by-family.md#austronesian) |
| Region | [Papunesia](by-region.md#papunesia) > [Marshall Islands](by-region.md#marshall-islands) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Austronesian](https://tigregotico.github.io/orthography2ipa/#x-clade-aust1307) `x-clade-aust1307` |
| Explorer | [`mh` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mh) |
| Spec file | [`mh.json`](../../orthography2ipa/data/mh.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Marshallese (Kajin Ṃajeḷ), a Micronesian language of the Marshall Islands.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 7 works, from 1968 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 41 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/mh.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mh` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 7 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-marshallese_language_wiki"></a>Wikipedia contributors (2026). *Marshallese language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Marshallese_language)
2. <a id="src-med1976"></a>Abo, Takaji, Bender, Byron W., Capelle, Alfred, DeBrum, Tony (1976). *Marshallese-English Dictionary*. University of Hawaii Press. [trussel2.com](http://www.trussel2.com/MOD/)
3. <a id="src-bender1969"></a>Bender, Byron W. (1969). *Spoken Marshallese: An Intensive Language Course with Grammatical Notes and Glossary*. University of Hawaii Press.
4. <a id="src-willson2003"></a>Willson, Heather (2003). *Marshallese Phonology and Morphology*. UCLA.
5. <a id="src-bender1968"></a>Bender, Byron W. (1968). *Marshallese Phonology*. Oceanic Linguistics 7(1).
6. <a id="src-choi1992"></a>Choi, John D. (1992). *Phonetic Underspecification and Target Interpolation: An Acoustic Study of Marshallese Vowel Allophony*. UCLA Working Papers in Phonetics 82.
7. <a id="src-wiktionary_mh_guidelines"></a>Wiktionary contributors (2026). *Wiktionary:Marshallese entry guidelines*. Wiktionary. [en.wiktionary.org](https://en.wiktionary.org/wiki/Wiktionary:About_Marshallese)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `mh` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 947 | 0.1182 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 65 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|
| Plosive | bʲ bˠ pʲ pˠ | dˠ tʲ tˠ |  | k kʷ ɡ ɡʷ |
| Nasal | mʲ mˠ | nʲ nʷ nˠ |  | ŋ ŋʷ |
| Trill |  | rʲ rʷ rˠ |  |  |
| Fricative |  | zʲ |  |  |
| Approximant |  |  | j |  |
| Lateral approximant |  | lʲ lʷ lˠ ɫ ɫʷ |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u ɯ |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ ʌ |
| Near-open | æ |  |  |
| Open |  |  | ɑ ɒ |

Sequences that the spec writes as one unit: [ej] [ew] [eɰ] [ij] [iw] [iɰ] [je] [ji] [jæ] [jɛ] [w] [we] [wi] [wæ] [wɛ] [æj] [æw] [æɰ] [ɛj] [ɛw] [ɛɰ] [ɰe] [ɰi] [ɰæ] [ɰɛ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [æ] | after back vowel [ɰæ] · after front vowel [jæ] · after vowel [ɰæ] · word final [æɰ] · word initial [ɰæ] |
| ⟨b⟩ | [pˠ] |  |
| ⟨bw⟩ | [pˠ] |  |
| ⟨d⟩ | [rʲ] |  |
| ⟨e⟩ | [ɛ] [e] | after vowel [jɛ] [je] · word final [ɛj] [ej] · word initial [jɛ] [je] |
| ⟨i⟩ | [i] | after vowel [ji] · word final [ij] · word initial [ji] |
| ⟨j⟩ | [tʲ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kw⟩ | [kʷ] |  |
| ⟨l⟩ | [lʲ] |  |
| ⟨m⟩ | [mʲ] |  |
| ⟨m̧⟩ | [mˠ] |  |
| ⟨m̧w⟩ | [mˠ] |  |
| ⟨n⟩ | [nʲ] |  |
| ⟨n̄⟩ | [ŋ] |  |
| ⟨n̄w⟩ | [ŋʷ] |  |
| ⟨o⟩ | [ɛ] [e] | after vowel [wɛ] [we] · word final [ɛw] [ew] · word initial [wɛ] [we] |
| ⟨o̧⟩ | [æ] | after vowel [wæ] · word final [æw] · word initial [wæ] |
| ⟨p⟩ | [pʲ] |  |
| ⟨r⟩ | [rˠ] |  |
| ⟨rw⟩ | [rʷ] |  |
| ⟨t⟩ | [tˠ] |  |
| ⟨u⟩ | [i] | after vowel [wi] · word final [iw] · word initial [wi] |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨ñ⟩ | [ŋ] |  |
| ⟨ñw⟩ | [ŋʷ] |  |
| ⟨ā⟩ | [æ] | after vowel [jæ] · word final [æj] · word initial [jæ] |
| ⟨ļ⟩ | [lˠ] |  |
| ⟨ļw⟩ | [lʷ] |  |
| ⟨ņ⟩ | [nˠ] |  |
| ⟨ņw⟩ | [nʷ] |  |
| ⟨ō⟩ | [ɛ] [e] | after vowel [ɰɛ] [ɰe] · word final [ɛɰ] [eɰ] · word initial [ɰɛ] [ɰe] |
| ⟨ū⟩ | [i] | after vowel [ɰi] · word final [iɰ] · word initial [ɰi] |
| ⟨ḷ⟩ | [lˠ] |  |
| ⟨ḷw⟩ | [lʷ] |  |
| ⟨ṃ⟩ | [mˠ] |  |
| ⟨ṃw⟩ | [mˠ] |  |
| ⟨ṇ⟩ | [nˠ] |  |
| ⟨ṇw⟩ | [nʷ] |  |
| ⟨ọ⟩ | [æ] | after vowel [wæ] · word final [æw] · word initial [wæ] |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mh")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Marchigiano](it-IT-x-marche.md) · [Home](../index.md) · [Meitei →](mni.md)
