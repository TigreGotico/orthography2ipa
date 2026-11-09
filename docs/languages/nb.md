# Norwegian Bokmål (`nb`)

<!-- atlas:summary begin -->
Norwegian Bokmål is a North Germanic language, written in the Latin script. Glottolog places it in Norway. The `nb` spec is at the research tier. It cites 4 sources and has 3 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `nb` |
| ISO 639-3 | [nob](https://iso639-3.sil.org/code/nob), Norwegian Bokmål |
| Glottolog | [norw1259](https://glottolog.org/resource/languoid/id/norw1259), Norwegian Bokmål |
| Wikidata | [Q25167](https://www.wikidata.org/wiki/Q25167) |
| Wikipedia | [Bokmål](https://en.wikipedia.org/wiki/Bokmål) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > North Germanic](by-family.md#indo-european--germanic--northwest-germanic--north-germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [Norway](by-region.md#norway) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Parent | [Norwegian](no.md) `no` |
| Explorer | [`nb` in the data explorer](https://tigregotico.github.io/orthography2ipa/#nb) |
| Spec file | [`nb.json`](../../orthography2ipa/data/nb.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Norwegian Bokmål, majority written standard (~85%), Urban East Norwegian phonology (Kristoffersen 2000).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1976 to 2019. [Sources](#sources) lists them. The spec file writes 37 of the 81 spellings of its letter table and takes the other 44 from [Norwegian](no.md) `no`.

The [spec file](../../orthography2ipa/data/nb.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `nb` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-haugen1976"></a>Haugen, E. (1976). *The Scandinavian Languages: An Introduction to their History*. Faber and Faber.
2. <a id="src-kristoffersen2000"></a>Kristoffersen, G. (2000). *The Phonology of Norwegian*. Oxford University Press.
3. <a id="src-phoible"></a>Moran, Steven & McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/)
4. <a id="src-kristoffersen2015"></a>Kristoffersen, G. (2015). *Innføring i norsk fonologi*. University of Bergen (Bergen Open Research Archive), 4th ed. Cited: 3, 6, 24, 29. [bora.uib.no](https://bora.uib.no/handle/1956/15694)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `nb` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2725 | 0.3580 | yes |
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `nb` | generated | machine-generated | MIT, each file its own | 10169 | 0.2942 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `nb` | generated | espeak-derived | CC BY 4.0 | 3176 | 0.3501 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 86 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bː p pʰ pː |  | d dː t tʰ tː |  | ɖ ʈ |  | k kʰ kː ɡ ɡː |  |
| Nasal | m mː |  | n nː |  | ɳ |  | ŋ |  |
| Trill |  |  | r rː |  |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative |  | f fː v | s sː | ʃ | ʂ | ç |  | h |
| Approximant |  | ʋ ʋː |  |  |  | j |  |  |
| Lateral approximant |  |  | l lː |  | ɭ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː yː | ʉ ʉː | uː |
| Near-close | ɪ ʏ |  |  |
| Close-mid | eː ø øː |  | oː |
| Mid |  | ə |  |
| Open-mid | œ ɛ |  | ɔ |
| Near-open | æ æː |  |  |
| Open |  |  | ɑ ɑː |

Sequences that the spec writes as one unit: [br] [dr] [fr] [kr] [ks] [lr] [mr] [nr] [pr] [rb] [rf] [rk] [rm] [rp] [rɡ] [rʋ] [sk] [sr] [tr] [æi] [æʉ] [øy] [ŋk] [ɑi] [ɡr] [ʋr].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] [ɑː] | default [ɑ] · nucleus stressed [ɑː] |
| ⟨ai⟩ | [ɑi] |  |
| ⟨au⟩ | [æʉ] |  |
| ⟨b⟩ | [b] |  |
| ⟨bb⟩ | [bː] |  |
| ⟨br⟩ | [br] |  |
| ⟨c⟩ | [k] [s] |  |
| ⟨ck⟩ | [kː] |  |
| ⟨d⟩ | [d] |  |
| ⟨dd⟩ | [dː] |  |
| ⟨dr⟩ | [dr] |  |
| ⟨e⟩ | [ɛ] [eː] [ə] | default [ɛ] · nucleus stressed [eː] · nucleus unstressed [ə] |
| ⟨ei⟩ | [æi] |  |
| ⟨f⟩ | [f] |  |
| ⟨ff⟩ | [fː] |  |
| ⟨fr⟩ | [fr] |  |
| ⟨g⟩ | [ɡ] [j] | before front vowel [j] · default [ɡ] |
| ⟨gg⟩ | [ɡː] |  |
| ⟨gj⟩ | [j] |  |
| ⟨gr⟩ | [ɡr] |  |
| ⟨h⟩ | [h] |  |
| ⟨hj⟩ | [j] |  |
| ⟨hv⟩ | [ʋ] |  |
| ⟨i⟩ | [ɪ] [iː] | default [ɪ] · nucleus stressed [iː] |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] [ç] | before front vowel [ç] · default [k] |
| ⟨kj⟩ | [ç] |  |
| ⟨kk⟩ | [kː] |  |
| ⟨kr⟩ | [kr] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [lː] |  |
| ⟨lr⟩ | [lr] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [mː] |  |
| ⟨mr⟩ | [mr] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨nn⟩ | [nː] |  |
| ⟨nr⟩ | [nr] |  |
| ⟨o⟩ | [ɔ] [uː] | default [ɔ] · nucleus stressed [uː] |
| ⟨p⟩ | [p] |  |
| ⟨pp⟩ | [pː] |  |
| ⟨pr⟩ | [pr] |  |
| ⟨q⟩ | [k] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨rb⟩ | [rb] |  |
| ⟨rd⟩ | [ɖ] |  |
| ⟨rf⟩ | [rf] |  |
| ⟨rg⟩ | [rɡ] |  |
| ⟨rk⟩ | [rk] |  |
| ⟨rl⟩ | [ɭ] |  |
| ⟨rm⟩ | [rm] |  |
| ⟨rn⟩ | [ɳ] |  |
| ⟨rp⟩ | [rp] |  |
| ⟨rr⟩ | [rː] |  |
| ⟨rs⟩ | [ʂ] |  |
| ⟨rt⟩ | [ʈ] |  |
| ⟨rv⟩ | [rʋ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sj⟩ | [ʃ] |  |
| ⟨sk⟩ | [ʃ] [sk] | before front vowel [ʃ] · default [sk] |
| ⟨skj⟩ | [ʃ] |  |
| ⟨sr⟩ | [sr] |  |
| ⟨ss⟩ | [sː] |  |
| ⟨t⟩ | [t] |  |
| ⟨tj⟩ | [ç] |  |
| ⟨tr⟩ | [tr] |  |
| ⟨tt⟩ | [tː] |  |
| ⟨u⟩ | [ʉ] [ʉː] | default [ʉ] · nucleus stressed [ʉː] |
| ⟨v⟩ | [ʋ] |  |
| ⟨vr⟩ | [ʋr] |  |
| ⟨vv⟩ | [ʋː] |  |
| ⟨w⟩ | [ʋ] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [ʏ] [yː] | default [ʏ] · nucleus stressed [yː] |
| ⟨z⟩ | [s] |  |
| ⟨å⟩ | [ɔ] [oː] | default [ɔ] · nucleus stressed [oː] |
| ⟨æ⟩ | [æ] [æː] | default [æ] · nucleus stressed [æː] |
| ⟨ø⟩ | [ø] [øː] | default [œ] · nucleus stressed [øː] |
| ⟨øy⟩ | [øy] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 13 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `NB_VELAR_K_SOFTENING_INITIAL_ONLY` | /ç/ → [k], not word-initially, spelled ⟨k⟩ | ⟨kake⟩ [kɑːkə] | [Kristoffersen 2000](#src-kristoffersen2000) |
| `NB_VELAR_G_SOFTENING_INITIAL_ONLY` | /j/ → [ɡ], not word-initially, spelled ⟨g⟩ | ⟨dagen⟩ [dɑːɡən] | [Kristoffersen 2000](#src-kristoffersen2000) |
| `NB_SHORTEN_A` | /ɑː/ → [ɑ], before a consonant cluster | - | - |
| `NB_SHORTEN_E` | /eː/ → [ɛ], before a consonant cluster | - | - |
| `NB_SHORTEN_I` | /iː/ → [ɪ], before a consonant cluster | - | - |
| `NB_SHORTEN_O` | /uː/ → [ɔ], before a consonant cluster | - | - |
| `NB_SHORTEN_U` | /ʉː/ → [ʉ], before a consonant cluster | - | - |
| `NB_SHORTEN_Y` | /yː/ → [ʏ], before a consonant cluster | - | - |
| `NB_SHORTEN_Æ` | /æː/ → [æ], before a consonant cluster | - | - |
| `NB_SHORTEN_Ø` | /øː/ → [œ], before a consonant cluster | - | - |
| `NB_SHORTEN_Å` | /oː/ → [ɔ], before a consonant cluster | - | - |
| `NB_SILENT_D` | /d/ → ∅, word-finally, after [n] [l] | - | - |
| `NB_SILENT_D_BEFORE_T` | /d/ → ∅, after [n] [l], before [t] | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "nb")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Norwegian](no.md) · [Home](../index.md) · [Norwegian Nynorsk →](nn.md)
