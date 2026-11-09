# Chichewa (Nyanja) (`ny`)

<!-- atlas:summary begin -->
Chichewa (Nyanja) is a Bantu language, written in the Latin script. Glottolog places it in 6 countries. The `ny` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ny` |
| ISO 639-3 | [nya](https://iso639-3.sil.org/code/nya), Chichewa |
| Glottolog | [nyan1308](https://glottolog.org/resource/languoid/id/nyan1308), Nyanja |
| Wikidata | [Q33273](https://www.wikidata.org/wiki/Q33273) |
| Wikipedia | [Chewa language](https://en.wikipedia.org/wiki/Chewa_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) > [Bantu](by-family.md#atlantic-congo--bantu) |
| Region | [Africa](by-region.md#africa) > [Eswatini](by-region.md#eswatini), [Malawi](by-region.md#malawi), [Mozambique](by-region.md#mozambique), [Tanzania](by-region.md#tanzania), [Zambia](by-region.md#zambia), [Zimbabwe](by-region.md#zimbabwe) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1900, living |
| Parent | [Bantu](https://tigregotico.github.io/orthography2ipa/#x-clade-narr1281) `x-clade-narr1281` |
| Explorer | [`ny` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ny) |
| Spec file | [`ny.json`](../../orthography2ipa/data/ny.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Chichewa/Nyanja (Chicheŵa). Bantu language of Malawi, Zambia, Mozambique and Zimbabwe. The orthography is phonemic and maps closely onto the IPA (Downing & Mtenje 2017 §2.1). KEY FEATURES: (1) FIVE-VOWEL SYSTEM: Downing & Mtenje's chart (4) pairs orthographic e/o with IPA /ɛ ɔ/, which is what this spec emits.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1937 to 2017. [Sources](#sources) lists them. The spec file writes all 64 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ny.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ny` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-downing_mtenje2017"></a>Downing, L.J. & Mtenje, A. (2017). *The Phonology of Chichewa*. Oxford University Press (The Phonology of the World's Languages). [api.pageplace.de](https://api.pageplace.de/preview/DT0400.9780191037733_A30389705/preview-9780191037733_A30389705.pdf)
2. <a id="src-mtenje1987"></a>Mtenje, A. (1987). *Tone Shift as a Morphological Phenomenon in Chichewa*. Lingua 72.
3. <a id="src-watkins1937"></a>Watkins, M.H. (1937). *A Grammar of Chichewa*. Language Dissertations 24, Linguistic Society of America.
4. <a id="src-price1966"></a>Price, T. (1966). *The Elements of Nyanja*. Blantyre Mission Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ny` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1564 | 0.3119 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 66 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bʷ p pʰ pʷ pʷʰ |  | d t tʰ tʷ tʷʰ |  |  | k kʰ kʷ kʷʰ ɡ ɡʷ |  |
| Affricate |  |  | ts | dʒ tʃ tʃʰ |  |  |  |
| Nasal | m mʷ |  | n nʷ |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative | β | f v vʷ | s sʷ z zʷ | ʃ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l lʷ |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [mb] [mbʷ] [mp] [mpʰ] [mpʷ] [nd] [ndʷ] [nt] [ntʃʰ] [ntʰ] [nz] [w] [ŋk] [ŋkʰ] [ŋkʷʰ] [ŋɡ] [ŋɡʷ] [ɓ] [ɗ] [ɗʷ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [ɓ] [b] |  |
| ⟨bw⟩ | [bʷ] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [ɗ] [d] |  |
| ⟨dw⟩ | [ɗʷ] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gw⟩ | [ɡʷ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨khw⟩ | [kʷʰ] |  |
| ⟨kw⟩ | [kʷ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [mb] |  |
| ⟨mbw⟩ | [mbʷ] |  |
| ⟨mp⟩ | [mp] |  |
| ⟨mph⟩ | [mpʰ] |  |
| ⟨mpw⟩ | [mpʷ] |  |
| ⟨mw⟩ | [mʷ] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [nd] |  |
| ⟨ndw⟩ | [ndʷ] |  |
| ⟨ng⟩ | [ŋɡ] |  |
| ⟨ng'⟩ | [ŋ] |  |
| ⟨ngw⟩ | [ŋɡʷ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨nkh⟩ | [ŋkʰ] |  |
| ⟨nkhw⟩ | [ŋkʷʰ] |  |
| ⟨nt⟩ | [nt] |  |
| ⟨ntch⟩ | [ntʃʰ] |  |
| ⟨nth⟩ | [ntʰ] |  |
| ⟨nw⟩ | [nʷ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨nz⟩ | [nz] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨phw⟩ | [pʷʰ] |  |
| ⟨pw⟩ | [pʷ] |  |
| ⟨r⟩ | [l] |  |
| ⟨rw⟩ | [lʷ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨sw⟩ | [sʷ] |  |
| ⟨t⟩ | [t] |  |
| ⟨tch⟩ | [tʃʰ] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨thw⟩ | [tʷʰ] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨tw⟩ | [tʷ] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨vw⟩ | [vʷ] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨zw⟩ | [zʷ] |  |
| ⟨ŵ⟩ | [β] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ny")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Chibcha](chb.md) · [Home](../index.md) · [Chickasaw →](cic.md)
