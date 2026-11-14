# Norwegian Nynorsk (`nn`)

<!-- atlas:summary begin -->
Norwegian Nynorsk is a North Germanic language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `nn` spec is at the research tier. It cites 6 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `nn` |
| ISO 639-3 | [nno](https://iso639-3.sil.org/code/nno), Norwegian Nynorsk |
| Glottolog | [norw1262](https://glottolog.org/resource/languoid/id/norw1262), Norwegian Nynorsk |
| Wikidata | [Q25164](https://www.wikidata.org/wiki/Q25164) |
| Wikipedia | [Nynorsk](https://en.wikipedia.org/wiki/Nynorsk) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > North Germanic](by-family.md#indo-european--germanic--northwest-germanic--north-germanic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1850, living |
| Parent | [Norwegian](no.md) `no` |
| Explorer | [`nn` in the data explorer](https://tigregotico.github.io/orthography2ipa/#nn) |
| Spec file | [`nn.json`](../../orthography2ipa/data/nn.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Norwegian Nynorsk, the minority written standard, codified on the western and inland dialects rather than on the Dano-Norwegian speech of the capital.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 6 works, from 1976 to 2000. [Sources](#sources) lists them. The spec file writes all 42 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/nn.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `nn` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-haugen1976"></a>Haugen, E. (1976). *The Scandinavian Languages: An Introduction to their History*. Faber and Faber.
2. <a id="src-kristoffersen2000"></a>Kristoffersen, G. (2000). *The Phonology of Norwegian*. Oxford University Press.
3. <a id="src-skjekkeland1997"></a>Skjekkeland, M. (1997). *Dei norske dialektane: Tradisjonelle særdrag i jamføring med skriftmåla*. Høyskoleforlaget.
4. <a id="src-sandoy1985"></a>Sandøy, H. (1985). *Norsk dialektkunnskap*. Novus.
5. <a id="src-beito1986"></a>Beito, O.T. (1986). *Nynorsk grammatikk: Lyd- og ordlære*. Det Norske Samlaget.
6. <a id="src-vanvik1979"></a>Vanvik, A. (1979). *Norsk fonetikk*. Universitetet i Oslo.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `nn` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 3829 | 0.2596 | yes |
| `wikipron_nor` | `nn` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1093 | 0.1705 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 70 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bː p pʰ pː |  | d dː t tʰ tː |  |  |  | k kʰ kː ɡ ɡː |  |  |
| Nasal | m mː |  | n nː |  |  |  | ŋ |  |  |
| Trill |  |  | r rː |  |  |  |  |  |  |
| Tap |  |  | ɾ |  | ɽ |  |  |  |  |
| Fricative |  | f fː v | s sː | ʃ |  | ç |  | ʁ | h |
| Approximant |  | ʋ ʋː |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l lː |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː yː | ʉ ʉː | uː |
| Near-close | ɪ ʏ |  | ʊ |
| Close-mid | eː øː |  | oː |
| Mid |  | ə |  |
| Open-mid | œ ɛ |  | ɔ |
| Near-open | æ æː |  |  |
| Open | a aː |  | ɑ ɑː |

Sequences that the spec writes as one unit: [ks] [lj] [sk] [ŋk] [œʊ] [œʊː] [œʏ] [œʏː] [ɑɪ] [ɛɪ] [ɛɪː].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ai⟩ | [ɑɪ] |  |
| ⟨b⟩ | [b] |  |
| ⟨bb⟩ | [bː] |  |
| ⟨c⟩ | [k] [s] |  |
| ⟨ck⟩ | [kː] |  |
| ⟨d⟩ | [d] |  |
| ⟨dd⟩ | [dː] |  |
| ⟨f⟩ | [f] |  |
| ⟨ff⟩ | [fː] |  |
| ⟨gg⟩ | [ɡː] |  |
| ⟨gj⟩ | [j] |  |
| ⟨h⟩ | [h] |  |
| ⟨hj⟩ | [j] |  |
| ⟨hv⟩ | [ʋ] |  |
| ⟨j⟩ | [j] |  |
| ⟨kj⟩ | [ç] |  |
| ⟨kk⟩ | [kː] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [lː] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [mː] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨nn⟩ | [nː] |  |
| ⟨p⟩ | [p] |  |
| ⟨pp⟩ | [pː] |  |
| ⟨q⟩ | [k] |  |
| ⟨r⟩ | [r] |  |
| ⟨rr⟩ | [rː] |  |
| ⟨s⟩ | [s] |  |
| ⟨sj⟩ | [ʃ] |  |
| ⟨skj⟩ | [ʃ] |  |
| ⟨ss⟩ | [sː] |  |
| ⟨t⟩ | [t] |  |
| ⟨tj⟩ | [ç] |  |
| ⟨tt⟩ | [tː] |  |
| ⟨v⟩ | [ʋ] |  |
| ⟨vv⟩ | [ʋː] |  |
| ⟨w⟩ | [ʋ] |  |
| ⟨x⟩ | [ks] |  |
| ⟨z⟩ | [s] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 14 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `NN_SHORTEN_A` | /ɑː/ → [ɑ], before a consonant cluster | - | [Kristoffersen 2000](#src-kristoffersen2000) |
| `NN_SHORTEN_E` | /eː/ → [ɛ], before a consonant cluster | - | - |
| `NN_SHORTEN_I` | /iː/ → [ɪ], before a consonant cluster | - | - |
| `NN_SHORTEN_O` | /uː/ → [ɔ], before a consonant cluster | - | - |
| `NN_SHORTEN_U` | /ʉː/ → [ʉ], before a consonant cluster | - | - |
| `NN_SHORTEN_Y` | /yː/ → [ʏ], before a consonant cluster | - | - |
| `NN_SHORTEN_Æ` | /æː/ → [æ], before a consonant cluster | - | - |
| `NN_SHORTEN_Ø` | /øː/ → [œ], before a consonant cluster | - | - |
| `NN_SHORTEN_Å` | /oː/ → [ɔ], before a consonant cluster | - | - |
| `NN_SHORTEN_EI` | /ɛɪː/ → [ɛɪ], before a consonant cluster | - | - |
| `NN_SHORTEN_AU` | /œʊː/ → [œʊ], before a consonant cluster | - | - |
| `NN_SHORTEN_ØY` | /œʏː/ → [œʏ], before a consonant cluster | - | - |
| `NN_SILENT_D` | /d/ → ∅, word-finally, after [n] [l] | - | - |
| `NN_SILENT_D_AFTER_R` | /d/ → ∅, word-finally, after [r] | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "nn")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Norwegian Bokmål](nb.md) · [Home](../index.md) · [Novial →](nov.md)
