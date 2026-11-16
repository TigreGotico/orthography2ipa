# Zulu (`zu`)

<!-- atlas:summary begin -->
Zulu is a Bantu language, written in the Latin script. Glottolog places it in 5 countries. The `zu` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `zu` |
| ISO 639-3 | [zul](https://iso639-3.sil.org/code/zul), Zulu |
| Glottolog | [zulu1248](https://glottolog.org/resource/languoid/id/zulu1248), Zulu |
| Wikidata | [Q10179](https://www.wikidata.org/wiki/Q10179) |
| Wikipedia | [Zulu language](https://en.wikipedia.org/wiki/Zulu_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) > [Bantu](by-family.md#atlantic-congo--bantu) |
| Region | [Africa](by-region.md#africa) > [Botswana](by-region.md#botswana), [Eswatini](by-region.md#eswatini), [Lesotho](by-region.md#lesotho), [Mozambique](by-region.md#mozambique), [South Africa](by-region.md#south-africa) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1800, living |
| Parent | [Proto-Bantu (family node)](https://tigregotico.github.io/orthography2ipa/#bnt) `bnt` |
| Explorer | [`zu` in the data explorer](https://tigregotico.github.io/orthography2ipa/#zu) |
| Spec file | [`zu.json`](../../orthography2ipa/data/zu.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Zulu (isiZulu), the largest Nguni language of South Africa. Sister of Xhosa, unlike Xhosa it has no native /r/ (⟨r⟩ occurs in loans only) and no palatal ⟨ty dy⟩ series.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1926 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 66 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/zu.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `zu` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-zulu_wiki"></a>Wikipedia contributors (2026). *Zulu language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Zulu_language)
2. <a id="src-zulu_phonology_wiki"></a>Wikipedia contributors (2026). *Zulu phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Zulu_phonology)
3. <a id="src-doke1926"></a>Doke, C. M. (1926). *The Phonetics of the Zulu Language*. University of the Witwatersrand Press (Bantu Studies vol. 2 special number).
4. <a id="src-poulos_msimang1998"></a>Poulos, G. & Msimang, C.T. (1998). *A Linguistic Analysis of Zulu*. Via Afrika.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `zu` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1754 | 0.2311 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 79 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  |  | k kʰ ɡ |  |
| Affricate |  |  | ts | dʒ tʃ |  | kx |  |
| Nasal | m m̩ |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ |  |  | h ɦ |
| Lateral fricative |  |  | ɬ ɮ |  |  |  |  |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Close-mid | e eː | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [mb] [mf] [mp] [mpʰ] [mv] [m̩b] [m̩f] [m̩p] [m̩pʰ] [m̩v] [m̩ɓ] [nd] [nt] [nts] [nz] [nɬ] [nɮ] [w] [ŋk] [ŋǀ] [ŋǀʱ] [ŋǁ] [ŋǁʱ] [ŋǃ] [ŋǃʱ] [ŋɡ] [ǀ] [ǀʰ] [ǁ] [ǁʰ] [ǃ] [ǃʰ] [ɓ] [ɠ] [ɡǀʱ] [ɡǁʱ] [ɡǃʱ] [ɲdʒ] [ɲtʃ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] | nucleus stressed [aː] |
| ⟨b⟩ | [ɓ] |  |
| ⟨bh⟩ | [b] |  |
| ⟨c⟩ | [ǀ] |  |
| ⟨ch⟩ | [ǀʰ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dl⟩ | [ɮ] |  |
| ⟨e⟩ | [e] | nucleus stressed [eː] |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gc⟩ | [ɡǀʱ] |  |
| ⟨gq⟩ | [ɡǃʱ] |  |
| ⟨gx⟩ | [ɡǁʱ] |  |
| ⟨h⟩ | [h] |  |
| ⟨hh⟩ | [ɦ] |  |
| ⟨hl⟩ | [ɬ] |  |
| ⟨i⟩ | [i] | nucleus stressed [iː] |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [ɠ] [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨kl⟩ | [kx] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [mb] |  |
| ⟨mbh⟩ | [mb] |  |
| ⟨mf⟩ | [mf] |  |
| ⟨mp⟩ | [mp] |  |
| ⟨mph⟩ | [mpʰ] |  |
| ⟨mv⟩ | [mv] |  |
| ⟨n⟩ | [n] |  |
| ⟨nc⟩ | [ŋǀ] |  |
| ⟨nd⟩ | [nd] |  |
| ⟨ndl⟩ | [nɮ] |  |
| ⟨ng⟩ | [ŋɡ] |  |
| ⟨ngc⟩ | [ŋǀʱ] |  |
| ⟨ngq⟩ | [ŋǃʱ] |  |
| ⟨ngx⟩ | [ŋǁʱ] |  |
| ⟨nhl⟩ | [nɬ] |  |
| ⟨nj⟩ | [ɲdʒ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨nq⟩ | [ŋǃ] |  |
| ⟨nt⟩ | [nt] |  |
| ⟨nts⟩ | [nts] |  |
| ⟨ntsh⟩ | [ɲtʃ] |  |
| ⟨nx⟩ | [ŋǁ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨nz⟩ | [nz] |  |
| ⟨o⟩ | [o] | nucleus stressed [oː] |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨q⟩ | [ǃ] |  |
| ⟨qh⟩ | [ǃʰ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨tsh⟩ | [tʃ] |  |
| ⟨u⟩ | [u] | nucleus stressed [uː] |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ǁ] |  |
| ⟨xh⟩ | [ǁʰ] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |

Stress falls on the penult by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 12 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `ZU_SYLLABIC_M` | /m/ → [m̩], before a consonant | ⟨ummese⟩ [um̩meːse] | - |
| `ZU_UM_PREFIX_SYLLABIC_MB` | /mb/ → [m̩ɓ], after [u], spelled ⟨mb⟩, with more context in the spec | ⟨umbala⟩ [um̩ɓâːla] | - |
| `ZU_UM_PREFIX_SYLLABIC_MP` | /mp/ → [m̩p], after [u], with more context in the spec | - | - |
| `ZU_UM_PREFIX_SYLLABIC_MF` | /mf/ → [m̩f], after [u], with more context in the spec | ⟨umfana⟩ [um̩fáːna] | - |
| `ZU_UM_PREFIX_SYLLABIC_MV` | /mv/ → [m̩v], after [u], with more context in the spec | - | - |
| `ZU_UM_PREFIX_SYLLABIC_MBH` | /mb/ → [m̩b], after [u], spelled ⟨mbh⟩, with more context in the spec | ⟨umbhede⟩ [um̩beːde] | - |
| `ZU_UM_PREFIX_SYLLABIC_MPH` | /mpʰ/ → [m̩pʰ], after [u], with more context in the spec | - | - |
| `ZU_NO_FINAL_LENGTH_A` | /aː/ → [a], word-finally | - | - |
| `ZU_NO_FINAL_LENGTH_E` | /eː/ → [e], word-finally | - | - |
| `ZU_NO_FINAL_LENGTH_I` | /iː/ → [i], word-finally | - | - |
| `ZU_NO_FINAL_LENGTH_O` | /oː/ → [o], word-finally | - | - |
| `ZU_NO_FINAL_LENGTH_U` | /uː/ → [u], word-finally | ⟨indlu⟩ [íːnɮu] | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "zu")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Zou](zom.md) · [Home](../index.md) · [Comparative phonology →](comparative.md)
