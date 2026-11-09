# Norwegian (`no`)

<!-- atlas:summary begin -->
Norwegian is a North Germanic language, written in the Latin script. Glottolog places it in 5 countries. The `no` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `no` |
| Aliases | `nor` |
| ISO 639-3 | [nor](https://iso639-3.sil.org/code/nor), Norwegian |
| Glottolog | [norw1258](https://glottolog.org/resource/languoid/id/norw1258), Norwegian |
| Wikidata | [Q9043](https://www.wikidata.org/wiki/Q9043) |
| Wikipedia | [Norwegian language](https://en.wikipedia.org/wiki/Norwegian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > North Germanic](by-family.md#indo-european--germanic--northwest-germanic--north-germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [Finland](by-region.md#finland), [Norway](by-region.md#norway), [Russia](by-region.md#russia), [Svalbard & Jan Mayen](by-region.md#svalbard--jan-mayen), [Sweden](by-region.md#sweden) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Parent | [North Germanic](https://tigregotico.github.io/orthography2ipa/#x-clade-nort3160) `x-clade-nort3160` |
| Child lects | 2, see [Related lects](#related-lects) |
| Explorer | [`no` in the data explorer](https://tigregotico.github.io/orthography2ipa/#no) |
| Spec file | [`no.json`](../../orthography2ipa/data/no.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Urban East Norwegian (standard Bokmål pronunciation). Retroflex assimilation shared with Swedish. Western/Northern dialects may use uvular [ʁ] for /r/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1976 to 2000. [Sources](#sources) lists them. The spec file writes all 47 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/no.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `no` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Norwegian Bokmål](nb.md) `nb`: Norway, research tier
- [Norwegian Nynorsk](nn.md) `nn`: research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-haugen1976"></a>Haugen, E. (1976). *The Scandinavian Languages: An Introduction to their History*. Faber and Faber.
2. <a id="src-kristoffersen2000"></a>Kristoffersen, G. (2000). *The Phonology of Norwegian*. Oxford University Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 52 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  | ɖ ʈ |  | k kʰ ɡ |  |
| Nasal | m |  | n |  | ɳ |  | ŋ |  |
| Trill |  |  | r |  |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |  |
| Fricative |  | f v | s | ʃ | ʂ | ç |  | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  | ɭ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː yː | ʉ ʉː | uː |
| Near-close | ɪ ʏ |  |  |
| Close-mid | eː ø øː |  | oː |
| Mid |  | ə |  |
| Open-mid | ɛ |  | ɔ |
| Near-open | æ æː |  |  |
| Open |  |  | ɑ ɑː |

Sequences that the spec writes as one unit: [ks] [sk] [æi] [æʉ] [øy] [ŋk] [ɑi].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] [ɑː] |  |
| ⟨ai⟩ | [ɑi] |  |
| ⟨au⟩ | [æʉ] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] [s] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ɛ] [eː] [ə] |  |
| ⟨ei⟩ | [æi] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [j] |  |
| ⟨gj⟩ | [j] |  |
| ⟨h⟩ | [h] |  |
| ⟨hj⟩ | [j] |  |
| ⟨i⟩ | [ɪ] [iː] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] [ç] |  |
| ⟨kj⟩ | [ç] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨o⟩ | [ɔ] [uː] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨rd⟩ | [ɖ] |  |
| ⟨rl⟩ | [ɭ] |  |
| ⟨rn⟩ | [ɳ] |  |
| ⟨rs⟩ | [ʂ] |  |
| ⟨rt⟩ | [ʈ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sj⟩ | [ʃ] |  |
| ⟨sk⟩ | [ʃ] [sk] |  |
| ⟨skj⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨tj⟩ | [ç] |  |
| ⟨u⟩ | [ʉ] [ʉː] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [v] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [ʏ] [yː] |  |
| ⟨z⟩ | [s] |  |
| ⟨å⟩ | [ɔ] [oː] |  |
| ⟨æ⟩ | [æ] [æː] |  |
| ⟨ø⟩ | [ø] [øː] |  |
| ⟨øy⟩ | [øy] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "no")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Northern Yukaghir](ykg.md) · [Home](../index.md) · [Norwegian Bokmål →](nb.md)
