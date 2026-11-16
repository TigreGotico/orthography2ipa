# Corsican (`co`)

<!-- atlas:summary begin -->
Corsican is an Italo-Romance language, written in the Latin script. Glottolog places it in France and Italy. The `co` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `co` |
| ISO 639-3 | [cos](https://iso639-3.sil.org/code/cos), Corsican |
| Glottolog | [cors1241](https://glottolog.org/resource/languoid/id/cors1241), Corsican |
| Wikidata | [Q33111](https://www.wikidata.org/wiki/Q33111) |
| Wikipedia | [Corsican language](https://en.wikipedia.org/wiki/Corsican_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Italo-Romance](by-family.md#indo-european--italic--romance--italo-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [France](by-region.md#france), [Italy](by-region.md#italy) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Parent | [Italo-Romance](https://tigregotico.github.io/orthography2ipa/#x-clade-italorom) `x-clade-italorom` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`co` in the data explorer](https://tigregotico.github.io/orthography2ipa/#co) |
| Spec file | [`co.json`](../../orthography2ipa/data/co.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Corsican. Italo-Romance of Corsica, closely related to Tuscan Italian but with its own innovations and archaic retentions. ~100,000 speakers (declining rapidly under French pressure). Key features: (1) Close to medieval Tuscan. (2) Gorgia (aspiration of voiceless stops) in some areas (Tuscan heritage).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1991 to 1997. [Sources](#sources) lists them. The spec file writes all 48 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/co.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `co` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Gallurese](https://tigregotico.github.io/orthography2ipa/#sdn) `sdn`: Italy, skeleton tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-maiden_parry1997"></a>Maiden, M. & Parry, M. (eds.) (1997). *The Dialects of Italy*. Routledge.
2. <a id="src-dalbera_stefanaggi1991"></a>Dalbera-Stefanaggi, M.-J. (1991). *Langues corses*. Édisud.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `co` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 459 | 0.1955 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 55 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bː p pː |  |  | d dː t tː |  | c ɟ | k kː ɡ ɡː |  |
| Affricate |  |  |  | dz ts tːs | dʒ dːʒ tʃ tːʃ |  |  |  |
| Nasal | m mː |  |  | n nː |  | ɲ | ŋ |  |
| Trill |  |  |  | r rː |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative | β | f fː v | ð | s sː z | ʃ ʒ |  | ɣ | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l lː |  | ʎ |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [kw] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨bb⟩ | [bː] |  |
| ⟨c⟩ | [k] [tʃ] |  |
| ⟨cc⟩ | [kː] [tːʃ] |  |
| ⟨ch⟩ | [k] |  |
| ⟨chj⟩ | [c] |  |
| ⟨d⟩ | [d] |  |
| ⟨dd⟩ | [dː] |  |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨f⟩ | [f] |  |
| ⟨ff⟩ | [fː] |  |
| ⟨g⟩ | [ɡ] [dʒ] |  |
| ⟨gg⟩ | [ɡː] [dːʒ] |  |
| ⟨gh⟩ | [ɡ] |  |
| ⟨ghj⟩ | [ɟ] |  |
| ⟨gl⟩ | [ʎ] |  |
| ⟨gn⟩ | [ɲ] |  |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [lː] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [mː] |  |
| ⟨n⟩ | [n] |  |
| ⟨nn⟩ | [nː] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨p⟩ | [p] |  |
| ⟨pp⟩ | [pː] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [r] |  |
| ⟨rr⟩ | [rː] |  |
| ⟨s⟩ | [s] [z] |  |
| ⟨sc⟩ | [ʃ] |  |
| ⟨sg⟩ | [ʒ] |  |
| ⟨ss⟩ | [sː] |  |
| ⟨t⟩ | [t] |  |
| ⟨tt⟩ | [tː] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨z⟩ | [ts] [dz] |  |
| ⟨zz⟩ | [tːs] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "co")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Cornish](kw.md) · [Home](../index.md) · [Cree →](cr.md)
