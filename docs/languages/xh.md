# Xhosa (`xh`)

<!-- atlas:summary begin -->
Xhosa is a Bantu language, written in the Latin script. Glottolog places it in Botswana, Lesotho and South Africa. The `xh` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `xh` |
| ISO 639-3 | [xho](https://iso639-3.sil.org/code/xho), Xhosa |
| Glottolog | [xhos1239](https://glottolog.org/resource/languoid/id/xhos1239), Xhosa |
| Wikidata | [Q13218](https://www.wikidata.org/wiki/Q13218) |
| Wikipedia | [Xhosa language](https://en.wikipedia.org/wiki/Xhosa_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) > [Bantu](by-family.md#atlantic-congo--bantu) |
| Region | [Africa](by-region.md#africa) > [Botswana](by-region.md#botswana), [Lesotho](by-region.md#lesotho), [South Africa](by-region.md#south-africa) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1800, living |
| Parent | [Bantu](https://tigregotico.github.io/orthography2ipa/#x-clade-narr1281) `x-clade-narr1281` |
| Explorer | [`xh` in the data explorer](https://tigregotico.github.io/orthography2ipa/#xh) |
| Spec file | [`xh.json`](../../orthography2ipa/data/xh.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Xhosa (isiXhosa), a Nguni language of South Africa. Related to Zulu, has /r/ unlike Zulu.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 2002 to 2020. [Sources](#sources) lists them. The spec file writes all 82 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/xh.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `xh` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 5 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-hyman2013_penult"></a>Larry M. Hyman (2013). *Penultimate lengthening in Bantu: Analysis and spread*. John Benjamins (Language Typology and Historical Contingency, eds. Bickel, Grenoble, Peterson & Timberlake). [linguistics.berkeley.edu](https://linguistics.berkeley.edu/~hyman/papers/2013-hyman-penult.pdf)
2. <a id="src-jessen_roux2002"></a>Michael Jessen and Justus C. Roux (2002). *Voice quality differences associated with stops and clicks in Xhosa*. Journal of Phonetics 30(1). Cited: 1-52. [doi.org](https://doi.org/10.1006/jpho.2001.0150)
3. <a id="src-choti2015"></a>Jonathan Choti (2015). *Phonological Asymmetries of Bantu Nasal Prefixes*. Cascadilla Proceedings Project (Selected Proceedings of the 44th Annual Conference on African Linguistics, ed. Ruth Kramer et al.). Cited: 37-51. [lingref.com](http://www.lingref.com/cpp/acal/44/paper3125.pdf)
4. <a id="src-jessen2002_acoustic"></a>Michael Jessen (2002). *An Acoustic Study of Contrasting Plosives and Click Accompaniments in Xhosa*. Phonetica 59(2-3). Cited: 150-179. [doi.org](https://doi.org/10.1159/000066068)
5. <a id="src-saul_botha2020"></a>Zandisile W. Saul and Rudolph Botha (2020). *Phonemes, Graphemes and Democracy: The Significance of Accuracy in the Orthographical Development of isiXhosa*. University of KwaZulu-Natal Press. [amazon.com](https://www.amazon.com/dp/1869144384)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `kaikki` ([kaikki.org](https://kaikki.org/dictionary/)) | `xh` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 888 | 0.3776 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 88 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  | c cʰ ɟ | k kʰ ɡ |  |
| Affricate |  |  | ts tɬ | dʒ tʃ |  | kx |  |
| Nasal | m m̩ |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ |  | x | h ɦ |
| Lateral fricative |  |  | ɬ ɮ |  |  |  |  |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [kǀ] [kǀʰ] [kǁ] [kǁʰ] [kǃ] [kǃʰ] [mb] [mp] [mpʰ] [mɬ] [m̩b] [m̩f] [m̩p] [m̩pʰ] [m̩v] [m̩ɓ] [m̩ɬ] [nd] [ndz] [ndɮ] [nt] [ntɬ] [ntʃ] [w] [ŋk] [ŋkǀ] [ŋkǁ] [ŋkǃ] [ŋǀ] [ŋǁ] [ŋǃ] [ŋɡ] [ɓ] [ɡǀ] [ɡǁ] [ɡǃ] [ɱbv] [ɱpf] [ɲc] [ɲdʒ], and 3 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] | nucleus stressed [aː] |
| ⟨b⟩ | [ɓ] |  |
| ⟨bh⟩ | [b] |  |
| ⟨c⟩ | [kǀ] |  |
| ⟨ch⟩ | [kǀʰ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dl⟩ | [ɮ] |  |
| ⟨dy⟩ | [ɟ] |  |
| ⟨e⟩ | [e] | nucleus stressed [eː] |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gc⟩ | [ɡǀ] |  |
| ⟨gq⟩ | [ɡǃ] |  |
| ⟨gx⟩ | [ɡǁ] |  |
| ⟨h⟩ | [h] |  |
| ⟨hh⟩ | [ɦ] |  |
| ⟨hl⟩ | [ɬ] |  |
| ⟨i⟩ | [i] | nucleus stressed [iː] |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨kr⟩ | [kx] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [mb] |  |
| ⟨mbh⟩ | [mb] |  |
| ⟨mf⟩ | [ɱpf] |  |
| ⟨mh⟩ | [m] |  |
| ⟨mhl⟩ | [mɬ] |  |
| ⟨mp⟩ | [mp] |  |
| ⟨mph⟩ | [mpʰ] |  |
| ⟨mv⟩ | [ɱbv] |  |
| ⟨n⟩ | [n] |  |
| ⟨nc⟩ | [ŋǀ] |  |
| ⟨nd⟩ | [nd] |  |
| ⟨ndl⟩ | [ndɮ] |  |
| ⟨ndy⟩ | [ɲɟ] |  |
| ⟨ng⟩ | [ŋɡ] |  |
| ⟨ng'⟩ | [ŋ] |  |
| ⟨ngc⟩ | [ŋǀ] |  |
| ⟨ngh⟩ | [ŋ] |  |
| ⟨ngq⟩ | [ŋǃ] |  |
| ⟨ngx⟩ | [ŋǁ] |  |
| ⟨ngʼ⟩ | [ŋ] |  |
| ⟨nh⟩ | [n] |  |
| ⟨nj⟩ | [ɲdʒ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨nkc⟩ | [ŋkǀ] |  |
| ⟨nkq⟩ | [ŋkǃ] |  |
| ⟨nkx⟩ | [ŋkǁ] |  |
| ⟨nq⟩ | [ŋǃ] |  |
| ⟨nt⟩ | [nt] |  |
| ⟨ntl⟩ | [ntɬ] |  |
| ⟨ntsh⟩ | [ɲtʃ] |  |
| ⟨nty⟩ | [ɲc] |  |
| ⟨nx⟩ | [ŋǁ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨nyh⟩ | [ɲ] |  |
| ⟨nz⟩ | [ndz] |  |
| ⟨o⟩ | [o] | nucleus stressed [oː] |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨q⟩ | [kǃ] |  |
| ⟨qh⟩ | [kǃʰ] |  |
| ⟨r⟩ | [r] |  |
| ⟨rh⟩ | [x] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨tl⟩ | [tɬ] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨tsh⟩ | [tʃ] |  |
| ⟨ty⟩ | [c] |  |
| ⟨tyh⟩ | [cʰ] |  |
| ⟨u⟩ | [u] | nucleus stressed [uː] |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [kǁ] |  |
| ⟨xh⟩ | [kǁʰ] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |

Stress falls on the penult by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 14 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `XH_LABIALIZED` | /w/ → [ʷ], after a consonant | ⟨incwadi⟩ [iŋǀʷaːdi] | - |
| `XH_SYLLABIC_M` | /m/ → [m̩], before a consonant | - | - |
| `XH_SYLLABIC_MHL` | /mɬ/ → [m̩ɬ] | - | - |
| `XH_UM_PREFIX_SYLLABIC_MB` | /mb/ → [m̩ɓ], spelled ⟨mb⟩, after ⟨u⟩, with more context in the spec | - | - |
| `XH_UM_PREFIX_SYLLABIC_MBH` | /mb/ → [m̩b], spelled ⟨mbh⟩, after ⟨u⟩, with more context in the spec | ⟨umbhobho⟩ [um̩boːbo] | - |
| `XH_UM_PREFIX_SYLLABIC_MP` | /mp/ → [m̩p], after ⟨u⟩, with more context in the spec | - | - |
| `XH_UM_PREFIX_SYLLABIC_MPH` | /mpʰ/ → [m̩pʰ], after ⟨u⟩, with more context in the spec | - | - |
| `XH_UM_PREFIX_SYLLABIC_MF` | /ɱpf/ → [m̩f], after ⟨u⟩, with more context in the spec | - | - |
| `XH_UM_PREFIX_SYLLABIC_MV` | /ɱbv/ → [m̩v], after ⟨u⟩, with more context in the spec | - | - |
| `XH_NO_FINAL_LENGTH_A` | /aː/ → [a], word-finally | - | Hyman 2013 |
| `XH_NO_FINAL_LENGTH_E` | /eː/ → [e], word-finally | - | Hyman 2013 |
| `XH_NO_FINAL_LENGTH_I` | /iː/ → [i], word-finally | - | Hyman 2013 |
| `XH_NO_FINAL_LENGTH_O` | /oː/ → [o], word-finally | ⟨molo⟩ [moːlo] | Hyman 2013 |
| `XH_NO_FINAL_LENGTH_U` | /uː/ → [u], word-finally | - | Hyman 2013 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "xh")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Wu Chinese](wuu-Latn-wugniu.md) · [Home](../index.md) · [Yakut →](sah.md)
