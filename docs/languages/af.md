# Afrikaans (`af`)

<!-- atlas:summary begin -->
Afrikaans is a West Germanic language, written in the Latin script. Glottolog places it in 6 countries. The `af` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `af` |
| ISO 639-3 | [afr](https://iso639-3.sil.org/code/afr), Afrikaans |
| Glottolog | [afri1274](https://glottolog.org/resource/languoid/id/afri1274), Afrikaans |
| Wikidata | [Q14196](https://www.wikidata.org/wiki/Q14196) |
| Wikipedia | [Afrikaans](https://en.wikipedia.org/wiki/Afrikaans) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > West Germanic](by-family.md#indo-european--germanic--northwest-germanic--west-germanic) |
| Region | [Africa](by-region.md#africa) > [Botswana](by-region.md#botswana), [Mozambique](by-region.md#mozambique), [Namibia](by-region.md#namibia), [South Africa](by-region.md#south-africa), [Zambia](by-region.md#zambia), [Zimbabwe](by-region.md#zimbabwe) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1700, living |
| Parent | [Dutch](nl-NL.md) `nl-NL` |
| Explorer | [`af` in the data explorer](https://tigregotico.github.io/orthography2ipa/#af) |
| Spec file | [`af.json`](../../orthography2ipa/data/af.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Afrikaans (Standard Afrikaans). Descended from 17th-century Dutch of VOC settlers (Cape Colony, established 1652), but its sound system diverged far enough that a Dutch grapheme table is not a usable starting point.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1993 to 2020. [Sources](#sources) lists them. The spec file writes all 66 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/af.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `af` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-donaldson1993"></a>Donaldson, B.C. (1993). *A Grammar of Afrikaans*. Mouton de Gruyter.
2. <a id="src-wissing2020"></a>Wissing, Daan P. (2020). *Afrikaans (Illustrations of the IPA)*. Journal of the International Phonetic Association 50(1), 127-140. Cited: 127-140. [doi.org](https://doi.org/10.1017/S0025100318000269)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `af` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2076 | 0.1653 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 64 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |  |
| Affricate |  |  |  | dʒ tʃ |  |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  | ʀ |  |
| Fricative |  | f v | s | ʃ |  | x ɣ | χ | h ɦ |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i y |  | u |
| Close-mid | e eː øː |  | o oː |
| Mid |  | ə əː |  |
| Open-mid | œ œː ɛ ɛː |  | ɔ ɔː |
| Open | a aː |  | ɑː |

Sequences that the spec writes as one unit: [ai] [eɪ] [iə] [iəu] [iːø] [ki] [ks] [sk] [ui] [uə] [uəi] [w] [yœ] [ŋk] [œu] [œy] [œɪ] [ɑːi] [ɔi] [ɔu] [əi].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | ∅ |  |
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [ɑː] |  |
| ⟨aai⟩ | [ɑːi] |  |
| ⟨ai⟩ | [ai] |  |
| ⟨au⟩ | [œu] |  |
| ⟨b⟩ | [b] | default [b] · word final [p] |
| ⟨c⟩ | [k] [s] |  |
| ⟨ch⟩ | [x] |  |
| ⟨d⟩ | [d] | default [d] · word final [t] |
| ⟨e⟩ | [ɛ] [ə] | default [ɛ] [ə] · nucleus unstressed [ə] |
| ⟨eau⟩ | [oː] |  |
| ⟨ee⟩ | [iə] |  |
| ⟨eeu⟩ | [iəu] |  |
| ⟨ei⟩ | [əi] |  |
| ⟨eu⟩ | [yœ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [x] [ɡ] |  |
| ⟨gh⟩ | [ɡ] |  |
| ⟨h⟩ | [ɦ] |  |
| ⟨i⟩ | [ə] [i] |  |
| ⟨ie⟩ | [i] |  |
| ⟨ieu⟩ | [iːø] |  |
| ⟨ij⟩ | [əi] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨oe⟩ | [u] |  |
| ⟨oei⟩ | [ui] |  |
| ⟨oi⟩ | [ɔi] |  |
| ⟨oo⟩ | [uə] |  |
| ⟨ooi⟩ | [uəi] |  |
| ⟨ou⟩ | [œu] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [f] |  |
| ⟨q⟩ | [k] |  |
| ⟨r⟩ | [r] [ʀ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sch⟩ | [sk] |  |
| ⟨sj⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [t] |  |
| ⟨tj⟩ | [ki] |  |
| ⟨tjie⟩ | [ki] |  |
| ⟨u⟩ | [œ] |  |
| ⟨ui⟩ | [œy] |  |
| ⟨uu⟩ | [y] |  |
| ⟨v⟩ | [f] [v] | default [f] [v] · word final [f] |
| ⟨w⟩ | [v] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [əi] |  |
| ⟨z⟩ | [s] | default [s] · word final [s] |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [eː] |  |
| ⟨ê⟩ | [ɛː] |  |
| ⟨ë⟩ | [ə] |  |
| ⟨î⟩ | [əː] |  |
| ⟨ï⟩ | [i] |  |
| ⟨ô⟩ | [ɔː] |  |
| ⟨û⟩ | [œː] |  |
| ⟨ü⟩ | [y] |  |

Stress falls on the first syllable by default.

Whole-word exceptions (1): ⟨'n⟩ [ə].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 7 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `NL_CODA_DEVOICE_G` | /ɣ/ → [x], in the coda, before [t] [k] [s] [f] [p] [x] [χ], spelled ⟨g⟩ | ⟨zeg-t⟩ [zɛxt] | Booij 1995 |
| `NL_CODA_DEVOICE_B` | /b/ → [p], in the coda, before [t] [k] [s] [f] [p] [x] [χ], spelled ⟨b⟩ | - | Booij 1995 |
| `NL_CODA_DEVOICE_D` | /d/ → [t], in the coda, before [t] [k] [s] [f] [p] [x] [χ], spelled ⟨d⟩ | ⟨raad-sel⟩ [raːtsəl] | Booij 1995 |
| `NL_CODA_DEVOICE_VELD` | /d/ → [t], in the coda, before [t] [k] [s] [f] [p] [x] [χ], spelled ⟨veld⟩ | ⟨veldslag⟩ [ˈvɛltslɑχ] | Gussenhoven 1992 |
| `NL_CODA_DEVOICE_V` | /v/ → [f], in the coda, before [t] [k] [s] [f] [p] [x] [χ], spelled ⟨v⟩ | - | Booij 1995 |
| `NL_CODA_DEVOICE_Z` | /z/ → [s], in the coda, before [t] [k] [s] [f] [p] [x] [χ], spelled ⟨z⟩ | ⟨raad-sel⟩ [raːtsəl] | Booij 1995 |
| `NL_QU_FRENCH_K` | /ʋ w/ → ∅, after [k], spelled ⟨qu⟩, in 29 listed words | ⟨pubquiz⟩ [ˈpʏpkʋɪs] | Paardekooper 1987 |

The spec switches off 16 inherited rules: `NL_UNSTRESSED_TENSE_I_FINAL`, `NL_UNSTRESSED_TENSE_I_HIATUS`, `NL_HIGH_TENSE_LENGTHENING_BEFORE_R_I`, `NL_HIGH_TENSE_LENGTHENING_BEFORE_R_Y`, `NL_MID_TENSE_CENTRING_BEFORE_R_E`, `NL_MID_TENSE_CENTRING_BEFORE_R_OE`, `NL_MID_TENSE_CENTRING_BEFORE_R_O`, `NL_MID_TENSE_CLOSING_DIPHTHONG_E`, `NL_MID_TENSE_CLOSING_DIPHTHONG_OE`, `NL_MID_TENSE_CLOSING_DIPHTHONG_O`, `NL_CODA_R_APPROXIMANT`, `NL_OPEN_SYLLABLE_A`, `NL_OPEN_SYLLABLE_E`, `NL_OPEN_SYLLABLE_I`, `NL_OPEN_SYLLABLE_O`, `NL_OPEN_SYLLABLE_U`.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "af")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Afar](aa.md) · [Home](../index.md) · [Ainu →](ain.md)
