# Dutch (`nl-NL`)

<!-- atlas:summary begin -->
Dutch is a West Germanic language, written in the Latin script. Its code names Netherlands. The `nl-NL` spec is at the research tier. It cites 9 sources and has 4 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `nl-NL` |
| Aliases | `nl`, `nld` |
| ISO 639-3 | [nld](https://iso639-3.sil.org/code/nld), Dutch |
| Glottolog | [dutc1256](https://glottolog.org/resource/languoid/id/dutc1256), Dutch |
| Wikidata | [Q7411](https://www.wikidata.org/wiki/Q7411) |
| Wikipedia | [Dutch language](https://en.wikipedia.org/wiki/Dutch_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > West Germanic](by-family.md#indo-european--germanic--northwest-germanic--west-germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [Netherlands](by-region.md#netherlands) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Parent | [West Germanic](https://tigregotico.github.io/orthography2ipa/#x-clade-west2793) `x-clade-west2793` |
| Child lects | 6, see [Related lects](#related-lects) |
| Explorer | [`nl-NL` in the data explorer](https://tigregotico.github.io/orthography2ipa/#nl-NL) |
| Spec file | [`nl-NL.json`](../../orthography2ipa/data/nl-NL.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Dutch (ABN / Algemeen Nederlands). ⟨g⟩ and ⟨ch⟩ are the voiceless uvular [χ].

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 9 works, from 1980 to 2007. [Sources](#sources) lists them. The spec file writes all 66 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/nl-NL.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `nl-NL` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Belgian Dutch (Flemish)](https://tigregotico.github.io/orthography2ipa/#nl-BE) `nl-BE`: Belgium, skeleton tier
- [West Flemish](https://tigregotico.github.io/orthography2ipa/#vls) `vls`: Belgium, France, Netherlands, stub tier
- [Afrikaans](af.md) `af`: Botswana, Mozambique, Namibia, South Africa, Zambia, Zimbabwe, research tier
- [Groningen Standard Dutch (Netherlands)](https://tigregotico.github.io/orthography2ipa/#nl-NL-x-groninge) `nl-NL-x-groninge`: Netherlands, skeleton tier
- [Limburg Standard Dutch (Netherlands)](https://tigregotico.github.io/orthography2ipa/#nl-NL-x-limburg) `nl-NL-x-limburg`: Netherlands, skeleton tier
- [Polder Dutch (Netherlands)](https://tigregotico.github.io/orthography2ipa/#nl-NL-x-polder) `nl-NL-x-polder`: Netherlands, skeleton tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 9 works. 6 of them have a DOI or a URL. The spec file holds a note on what 8 of them support.

1. <a id="src-gussenhoven1999"></a>Gussenhoven, C. (1999). *Dutch*. Cambridge University Press.
2. <a id="src-vdHulst_ritter1999"></a>van der Hulst, H. & Ritter, N.A. (eds.) (1999). *The Syllable: Views and Facts*. Mouton de Gruyter.
3. <a id="src-paardekooper1987"></a>Paardekooper, P.C. (1987). *ABN-uitspraakgids*. Heideland-Orbis. Cited: VIII, X, XV, XVIII, 11, 12, 35-41, 45, 49, 57-60, 66, 72, 87, 154, 155, 158, 164, 169, 181, 192, 207. [dbnl.org](https://www.dbnl.org/tekst/paar001abnu01_01/)
4. <a id="src-zonneveld_trommelen1980"></a>Zonneveld, W. & Trommelen, M. (1980). *Egg, onion, ouch! On the representation of Dutch diphthongs*. Martinus Nijhoff. Cited: 265-292. [dbnl.org](https://www.dbnl.org/tekst/zonn004eggo01_01/zonn004eggo01_01_0001.php)
5. <a id="src-gussenhoven1992"></a>Gussenhoven, C. (1992). *Dutch*. Journal of the International Phonetic Association. Cited: 45-47. [doi.org](https://doi.org/10.1017/S002510030000459X)
6. <a id="src-verhoeven2005"></a>Verhoeven, J. (2005). *Belgian Standard Dutch*. Journal of the International Phonetic Association. Cited: 243-247. [doi.org](https://doi.org/10.1017/S0025100305002173)
7. <a id="src-verhoeven_hageman2007"></a>Verhoeven, J. & Hageman, G. (2007). *De verstemlozing van fricatieven in Vlaanderen*. Nederlandse Taalkunde. Cited: 138-151.
8. <a id="src-trommelen_zonneveld1989"></a>Trommelen, M. & Zonneveld, W. (1989). *Klemtoon en metrische fonologie*. Dick Coutinho, Muiderberg. Cited: 131-138. [dbnl.org](https://www.dbnl.org/tekst/trom001klem01_01/)
9. <a id="src-dewulf2003"></a>De Wulf, C. (2003). *Procope van de h-*. Taal en Tongval. Cited: 216-231. [journal-archive.aup.nl](https://www.journal-archive.aup.nl/taal-en-tongval/jrg_2003_vol_55_-_procope_van_de_h-.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `nl-NL` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 45872 | 0.1824 | yes |
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `nl-NL` | generated | machine-generated | MIT, each file its own | 117869 | 0.2649 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `nl-NL` | generated | espeak-derived | CC BY 4.0 | 8108 | 0.2673 | no |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `nl-NL` | generated | epitran-derived | CC0 1.0 | 25904 | 0.3804 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 77 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k |  |  |
| Nasal | m |  | n |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  | ʀ |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative | β̞ | f v | s z | ʃ |  | x ɣ | ʁ χ | h ɦ |
| Approximant |  | ʋ | ɹ |  | j |  |  |  |
| Lateral approximant |  |  | l ɫ |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː y yː |  | u uː |
| Near-close | ɪ ʏ |  |  |
| Close-mid | eː øː |  | oː |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Open | aː |  | ɑ |

Sequences that the spec writes as one unit: [aːi] [brɛχt] [bɛɹχ] [ei] [ei̞] [eːu] [eːʋ] [eᵊ] [is] [iu] [iʋ] [jøː] [ks] [kɛɹk] [kʋ] [ou] [oᵊ] [sχ] [vɛld] [vɛlt] [w] [yu] [yʋ] [øy] [øᵊ] [ŋk] [œy] [œʏ] [ɑu] [ɔi] [ɛi] [ɛɪ] [ʌu].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] | default [ɑ] · open syllable [aː] |
| ⟨aa⟩ | [aː] |  |
| ⟨aauw⟩ | [ɑu] |  |
| ⟨ai⟩ | [aːi] |  |
| ⟨au⟩ | [ɑu] |  |
| ⟨auw⟩ | [ɑu] |  |
| ⟨b⟩ | [b] | default [b] · word final [p] |
| ⟨berg⟩ | [bɛɹχ] |  |
| ⟨brecht⟩ | [brɛχt] |  |
| ⟨c⟩ | [k] [s] | before e [s] · before i [s] · default [k] |
| ⟨ch⟩ | [χ] |  |
| ⟨d⟩ | [d] | default [d] · word final [t] |
| ⟨e⟩ | [ɛ] [ə] | default [ɛ] [ə] · nucleus stressed closed [ɛ] · nucleus stressed open [eː] · nucleus unstressed [ə] |
| ⟨eau⟩ | [oː] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨eeuw⟩ | [eːu] | before vowel [eːʋ] · default [eːu] |
| ⟨ei⟩ | [ɛi] |  |
| ⟨eu⟩ | [øː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɣ] [x] | default [χ] · word final [χ] |
| ⟨h⟩ | [ɦ] | default [ɦ] · word initial [ɦ] |
| ⟨i⟩ | [ɪ] | default [ɪ] · open syllable [i] |
| ⟨ie⟩ | [i] |  |
| ⟨ieu⟩ | [jøː] |  |
| ⟨ieuw⟩ | [iu] | before vowel [iʋ] · default [iu] |
| ⟨ij⟩ | [ɛi] |  |
| ⟨isch⟩ | [is] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨kerk⟩ | [kɛɹk] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨o⟩ | [ɔ] | default [ɔ] · open syllable [oː] |
| ⟨oe⟩ | [u] |  |
| ⟨oi⟩ | [ɔi] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨ou⟩ | [ɑu] |  |
| ⟨ouw⟩ | [ɑu] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [f] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [kʋ] |  |
| ⟨r⟩ | [r] [ʁ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sj⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [t] |  |
| ⟨u⟩ | [ʏ] | default [ʏ] · open syllable [y] |
| ⟨ui⟩ | [œy] |  |
| ⟨uu⟩ | [y] |  |
| ⟨uw⟩ | [yu] | before vowel [yʋ] · default [yu] |
| ⟨v⟩ | [v] [f] | default [v] · word final [f] |
| ⟨veld⟩ | [vɛld] [vɛlt] | default [vɛld] · word final [vɛlt] |
| ⟨w⟩ | [ʋ] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [i] [j] [ei̞] |  |
| ⟨z⟩ | [z] [s] | default [z] · word final [s] |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [eː] |  |
| ⟨ê⟩ | [ɛ] |  |
| ⟨ë⟩ | [ə] |  |
| ⟨ï⟩ | [i] |  |
| ⟨ü⟩ | [y] |  |

Stress falls on the first syllable by default.

Whole-word exceptions (18): ⟨bevel⟩ [bəˈvɛl], ⟨gestel⟩ [χəˈstɛl], ⟨gezel⟩ [χəˈzɛl], ⟨gezwel⟩ [χəˈzʋɛl], ⟨matjok⟩ [ˈmaːtʃɔk], ⟨nestje⟩ [ˈnɛstʃə], ⟨tietjerk⟩ [ˈtitʃɛɹk], ⟨tjaffelen⟩ [ˈtʃɑfələn], ⟨tjalhuizum⟩ [ˈtʃɑlɦœyzʏm], ⟨tjanten⟩ [ˈtʃɑntən], ⟨tjap⟩ [ˈtʃɑp], ⟨tjappen⟩ [ˈtʃɑpən], ⟨tjaptjoi⟩ [ˈtʃɑptʃɔi], ⟨tjauwmin⟩ [ˈtʃɑumɪn], ⟨tjerkgaast⟩ [ˈtʃɛɹkχaːst], ⟨tjerkwerd⟩ [ˈtʃɛɹkʋəɹt], ⟨tjetten⟩ [ˈtʃɛtən], ⟨tjokvol⟩ [ˈtʃɔkfɔl].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 18 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `NL_CODA_DEVOICE_G` | /ɣ/ → [x], in the coda, before [t] [k] [s] [f] [p] [x] [χ], spelled ⟨g⟩ | ⟨zeg-t⟩ [zɛxt] | Booij 1995 |
| `NL_UNSTRESSED_TENSE_I_FINAL` | /ɪ/ → [i], word-finally, unstressed, spelled ⟨i⟩ | ⟨Ali⟩ [aːli] | Booij 1995 |
| `NL_UNSTRESSED_TENSE_I_HIATUS` | /ɪ/ → [i], unstressed, before a vowel, spelled ⟨i⟩ | - | Booij 1995 |
| `NL_HIGH_TENSE_LENGTHENING_BEFORE_R_I` | /i/ → [iː], before [r] | ⟨banier⟩ [baːniːr] | [Gussenhoven 1999](#src-gussenhoven1999), Booij 1995 |
| `NL_HIGH_TENSE_LENGTHENING_BEFORE_R_Y` | /y/ → [yː], before [r] | ⟨aanvuren⟩ [aːnvyːrə] | [Gussenhoven 1999](#src-gussenhoven1999), Booij 1995 |
| `NL_MID_TENSE_CENTRING_BEFORE_R_E` | /eː/ → [eᵊ], before [r] | ⟨they are pronounced⟩ [eᵊ, øᵊ, oᵊ] | [Gussenhoven 1992](#src-gussenhoven1992) |
| `NL_MID_TENSE_CENTRING_BEFORE_R_OE` | /øː/ → [øᵊ], before [r] | ⟨they are pronounced⟩ [eᵊ, øᵊ, oᵊ] | [Gussenhoven 1992](#src-gussenhoven1992) |
| `NL_MID_TENSE_CENTRING_BEFORE_R_O` | /oː/ → [oᵊ], before [r] | ⟨they are pronounced⟩ [eᵊ, øᵊ, oᵊ] | [Gussenhoven 1992](#src-gussenhoven1992) |
| `NL_MID_TENSE_CLOSING_DIPHTHONG_E` | /eː/ → [ei] | ⟨beet⟩ [beit] | [Paardekooper 1987](#src-paardekooper1987), [Gussenhoven 1992](#src-gussenhoven1992) |
| `NL_MID_TENSE_CLOSING_DIPHTHONG_OE` | /øː/ → [øy] | ⟨neus⟩ [nøys] | [Paardekooper 1987](#src-paardekooper1987), [Gussenhoven 1992](#src-gussenhoven1992) |
| `NL_MID_TENSE_CLOSING_DIPHTHONG_O` | /oː/ → [ou], with more context in the spec | ⟨boot⟩ [bout] | [Paardekooper 1987](#src-paardekooper1987), [Gussenhoven 1992](#src-gussenhoven1992) |
| `NL_CODA_DEVOICE_B` | /b/ → [p], in the coda, before [t] [k] [s] [f] [p] [x] [χ], spelled ⟨b⟩ | - | Booij 1995 |
| `NL_CODA_DEVOICE_D` | /d/ → [t], in the coda, before [t] [k] [s] [f] [p] [x] [χ], spelled ⟨d⟩ | ⟨raad-sel⟩ [raːtsəl] | Booij 1995 |
| `NL_CODA_DEVOICE_VELD` | /d/ → [t], in the coda, before [t] [k] [s] [f] [p] [x] [χ], spelled ⟨veld⟩ | ⟨veldslag⟩ [ˈvɛltslɑχ] | [Gussenhoven 1992](#src-gussenhoven1992) |
| `NL_CODA_DEVOICE_V` | /v/ → [f], in the coda, before [t] [k] [s] [f] [p] [x] [χ], spelled ⟨v⟩ | - | Booij 1995 |
| `NL_CODA_DEVOICE_Z` | /z/ → [s], in the coda, before [t] [k] [s] [f] [p] [x] [χ], spelled ⟨z⟩ | ⟨raad-sel⟩ [raːtsəl] | Booij 1995 |
| `NL_CODA_R_APPROXIMANT` | /r/ → [ɹ], not word-initially, in the coda, with more context in the spec | ⟨door⟩ [doᵊɹ] | [Gussenhoven 1992](#src-gussenhoven1992) |
| `NL_QU_FRENCH_K` | /ʋ w/ → ∅, after [k], spelled ⟨qu⟩, in 29 listed words | ⟨pubquiz⟩ [ˈpʏpkʋɪs] | [Paardekooper 1987](#src-paardekooper1987) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "nl-NL")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Dungan](dng.md) · [Home](../index.md) · [Dzongkha →](dz.md)
