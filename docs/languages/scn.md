# Sicilian (`scn`)

<!-- atlas:summary begin -->
Sicilian is an Italo-Romance language, written in the Latin script. Glottolog places it in Italy. The `scn` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `scn` |
| ISO 639-3 | [scn](https://iso639-3.sil.org/code/scn), Sicilian |
| Glottolog | [sici1248](https://glottolog.org/resource/languoid/id/sici1248), Sicilian |
| Wikidata | [Q33973](https://www.wikidata.org/wiki/Q33973) |
| Wikipedia | [Sicilian language](https://en.wikipedia.org/wiki/Sicilian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Italo-Romance](by-family.md#indo-european--italic--romance--italo-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Italy](by-region.md#italy) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Parent | [Italo-Romance](https://tigregotico.github.io/orthography2ipa/#x-clade-italorom) `x-clade-italorom` |
| Explorer | [`scn` in the data explorer](https://tigregotico.github.io/orthography2ipa/#scn) |
| Spec file | [`scn.json`](../../orthography2ipa/data/scn.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Sicilian. Southern Italo-Romance of Sicily and S. Calabria. ~4.7 million speakers. Key features: (1) 5-VOWEL system /a ɛ i ɔ u/ (like Sardinian, more archaic than Italian's 7). (2) Retroflex consonants: -LL- → [ɖː] (beddu 'beautiful'), TR → [ʈɽ]. (3) Final vowel reduction. Literary tradition from 13th c.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1988 to 2009. [Sources](#sources) lists them. The spec file writes all 48 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/scn.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `scn` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-maiden_parry1997"></a>Maiden, M. & Parry, M. (eds.) (1997). *The Dialects of Italy*. Routledge.
2. <a id="src-loporcaro2009"></a>Loporcaro, M. (2009). *Profilo linguistico dei dialetti italiani*. Laterza.
3. <a id="src-lepschy_lepschy1988"></a>Lepschy, A.L. & Lepschy, G. (1988). *The Italian Language Today*. Hutchinson.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `scn` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1396 | 0.1944 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 55 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bː p pː |  | d dː t tː |  | ɖ ɖː ʈ |  | k kː ɡ ɡː |
| Affricate |  |  | dz dːz ts tːs | dʒ dːʒ tʃ tːʃ |  |  |  |
| Nasal | m mː |  | n nː |  |  | ɲ | ŋ |
| Trill |  |  | r rː |  |  |  |  |
| Tap |  |  | ɾ |  | ɽ |  |  |
| Fricative | β | f fː v | s sː z | ʃ | ʂ |  |  |
| Approximant |  |  |  |  |  | j |  |
| Lateral approximant |  |  | l lː |  |  | ʎ |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [kw] [w] [ʂʈɽ] [ʈɽ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] [v] |  |
| ⟨bb⟩ | [bː] |  |
| ⟨c⟩ | [k] [tʃ] |  |
| ⟨cc⟩ | [kː] [tːʃ] |  |
| ⟨ch⟩ | [k] |  |
| ⟨d⟩ | [d] |  |
| ⟨dd⟩ | [ɖː] |  |
| ⟨e⟩ | [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨ff⟩ | [fː] |  |
| ⟨g⟩ | [ɡ] [dʒ] |  |
| ⟨gg⟩ | [ɡː] [dːʒ] |  |
| ⟨gh⟩ | [ɡ] |  |
| ⟨gl⟩ | [ʎ] |  |
| ⟨gn⟩ | [ɲ] |  |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [ɖː] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [mː] |  |
| ⟨n⟩ | [n] |  |
| ⟨nn⟩ | [nː] |  |
| ⟨o⟩ | [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨pp⟩ | [pː] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [r] [ɽ] |  |
| ⟨rr⟩ | [rː] |  |
| ⟨s⟩ | [s] [z] |  |
| ⟨sc⟩ | [ʃ] |  |
| ⟨ss⟩ | [sː] |  |
| ⟨str⟩ | [ʂʈɽ] |  |
| ⟨t⟩ | [t] |  |
| ⟨tr⟩ | [ʈɽ] |  |
| ⟨tt⟩ | [tː] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨z⟩ | [ts] [dz] |  |
| ⟨zz⟩ | [tːs] [dːz] |  |
| ⟨à⟩ | [a] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨ì⟩ | [i] |  |
| ⟨ò⟩ | [ɔ] |  |
| ⟨ù⟩ | [u] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "scn")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Shor](cjs.md) · [Home](../index.md) · [Sidamo →](sid.md)
