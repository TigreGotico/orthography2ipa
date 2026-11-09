# Franco-Provençal (Arpitan) (`frp`)

<!-- atlas:summary begin -->
Franco-Provençal (Arpitan) is a Gallo-Romance language, written in the Latin script. Glottolog places it in France, Italy and Switzerland. The `frp` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `frp` |
| ISO 639-3 | [frp](https://iso639-3.sil.org/code/frp), Arpitan |
| Glottolog | [fran1260](https://glottolog.org/resource/languoid/id/fran1260), Arpitan |
| Wikidata | [Q15087](https://www.wikidata.org/wiki/Q15087) |
| Wikipedia | [Arpitan language](https://en.wikipedia.org/wiki/Arpitan_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Gallo-Romance](by-family.md#indo-european--italic--romance--gallo-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [France](by-region.md#france), [Italy](by-region.md#italy), [Switzerland](by-region.md#switzerland) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1200, living |
| Parent | [Gallo-Romance](https://tigregotico.github.io/orthography2ipa/#x-clade-gallorom) `x-clade-gallorom` |
| Explorer | [`frp` in the data explorer](https://tigregotico.github.io/orthography2ipa/#frp) |
| Spec file | [`frp.json`](../../orthography2ipa/data/frp.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Franco-Provençal / Arpitan. A distinct Gallo-Romance language intermediate between French (Oïl) and Occitan (Oc). Spoken historically in Savoie, Lyonnais, Suisse Romande, and Aosta Valley. Key features: (1) CA- → [tʃ] (like French, vs Occitan [ka]). (2) Final -a preserved (unlike French).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1959 to 1996. [Sources](#sources) lists them. The spec file writes all 39 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/frp.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `frp` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-fouche1959"></a>Fouché, P. (1959). *Traité de prononciation française*. Klincksieck.
2. <a id="src-martin1990"></a>Martin, J.-B. (1990). *Le francoprovençal: langue oubliée*. in G. Vermes (ed.), Vingt-cinq communautés linguistiques de la France.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 48 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Uvular |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  | dz ts | dʒ tʃ |  |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |
| Trill |  |  |  | r |  |  |  | ʀ |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative | β | f v | ð | s z | ʃ ʒ |  | ɣ | ʁ |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  | ʎ |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u |
| Close-mid | e ẽ | o õ |
| Open-mid | ɛ | ɔ |
| Open | a ã | ɑ |

Sequences that the spec writes as one unit: [aj] [aw] [ej] [w] [we] [wɛ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [aj] [ɛ] |  |
| ⟨an⟩ | [ã] |  |
| ⟨au⟩ | [aw] [o] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] [s] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨dz⟩ | [dz] |  |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨ei⟩ | [ej] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [dʒ] |  |
| ⟨gn⟩ | [ɲ] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [dʒ] [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [ʎ] [j] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨oi⟩ | [we] [wɛ] |  |
| ⟨ou⟩ | [u] |  |
| ⟨p⟩ | [p] |  |
| ⟨qu⟩ | [k] |  |
| ⟨r⟩ | [ʁ] [r] |  |
| ⟨s⟩ | [s] [z] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨u⟩ | [y] |  |
| ⟨v⟩ | [v] |  |
| ⟨z⟩ | [z] [dz] |  |
| ⟨â⟩ | [ɑ] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [e] |  |
| ⟨ê⟩ | [ɛ] |  |
| ⟨ô⟩ | [o] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 3 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `FRP_NASAL_e` | /e/ → [ẽ], before a coda nasal | - | - |
| `FRP_NASAL_o` | /o/ → [õ], before a coda nasal | - | - |
| `FRP_NASAL_ABSORB` | /n m/ → ∅, in the coda, after a vowel | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "frp")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Forest Enets](enf.md) · [Home](../index.md) · [French →](fr-FR.md)
