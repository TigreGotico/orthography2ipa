# Aranese (Gascon Occitan) (`oc-x-aranes`)

<!-- atlas:summary begin -->
Aranese (Gascon Occitan) is a Gallo-Romance variety, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `oc-x-aranes` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `oc-x-aranes` |
| ISO 639-3 | [oci](https://iso639-3.sil.org/code/oci), Occitan (post 1500) |
| Glottolog | [aran1260](https://glottolog.org/resource/languoid/id/aran1260), Aranese |
| Wikidata | [Q10196](https://www.wikidata.org/wiki/Q10196) |
| Wikipedia | [Aranese dialect](https://en.wikipedia.org/wiki/Aranese_dialect) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Gallo-Romance](by-family.md#indo-european--italic--romance--gallo-romance) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1200, living |
| Parent | [Occitan](oc.md) `oc` |
| Explorer | [`oc-x-aranes` in the data explorer](https://tigregotico.github.io/orthography2ipa/#oc-x-aranes) |
| Spec file | [`oc-x-aranes.json`](../../orthography2ipa/data/oc-x-aranes.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Aranese (Aranès), the Gascon variety of Occitan spoken in the Val d'Aran and co-official in Catalonia, regulated by the Conselh Generau d'Aran. Written in the classical Occitan orthography with Gascon conventions.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1973 to 1996. [Sources](#sources) lists them. The spec file writes all 68 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/oc-x-aranes.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `oc-x-aranes` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-alibert1976"></a>Alibert, L. (1976). *Gramatica occitana*. Institut d'Estudis Occitans.
2. <a id="src-bec1973"></a>Bec, P. (1973). *Manuel pratique d'occitan moderne*. Picard.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `spain_romance_tts` | `oc-x-aranes` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.0787 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 55 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  | dz ts | dʒ tʃ |  |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |
| Trill |  |  |  | r |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative | β | f | ð | s z | ʃ ʒ |  | ɣ | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  | ʎ |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u |
| Close-mid | e |  |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [aj] [aw] [ej] [ew] [iw] [ks] [kw] [nh] [ow] [sh] [uj] [w] [we] [wɛ] [yj] [ɔj] [ɔw] [ɛj] [ɛw] [ɡw].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | ∅ |  |
| ⟨a⟩ | [a] [ɔ] |  |
| ⟨ai⟩ | [aj] |  |
| ⟨au⟩ | [aw] |  |
| ⟨b⟩ | [b] | default [b] · intervocalic [β] |
| ⟨c⟩ | [k] [s] |  |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] | default [d] · intervocalic [ð] |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨ei⟩ | [ej] |  |
| ⟨eu⟩ | [ew] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [dʒ] | before e [dʒ] [ʒ] · before i [dʒ] [ʒ] · default [ɡ] · intervocalic [ɣ] |
| ⟨gu⟩ | [ɡ] [ɡw] | before a [ɡw] · before e [ɡ] · before i [ɡ] · before o [ɡw] · default [ɡ] |
| ⟨h⟩ | [h] ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨ish⟩ | [ʃ] |  |
| ⟨iu⟩ | [iw] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨lh⟩ | [ʎ] |  |
| ⟨ll⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨nh⟩ | [ɲ] |  |
| ⟨n·h⟩ | [nh] |  |
| ⟨o⟩ | [u] |  |
| ⟨oi⟩ | [uj] |  |
| ⟨ou⟩ | [ow] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [k] [kw] |  |
| ⟨r⟩ | [r] [ɾ] | intervocalic [ɾ] · onset [ɾ] · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] [z] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨ss⟩ | [s] |  |
| ⟨s·h⟩ | [sh] |  |
| ⟨t⟩ | [t] |  |
| ⟨tg⟩ | [dʒ] |  |
| ⟨th⟩ | [t] [tʃ] |  |
| ⟨tj⟩ | [dʒ] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨tz⟩ | [dz] [ts] | default [ts] · intervocalic [dz] · word final [ts] |
| ⟨u⟩ | [y] |  |
| ⟨ue⟩ | [we] |  |
| ⟨ui⟩ | [yj] |  |
| ⟨uè⟩ | [wɛ] |  |
| ⟨v⟩ | [b] [β] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [i] |  |
| ⟨z⟩ | [z] |  |
| ⟨à⟩ | [a] |  |
| ⟨ç⟩ | [s] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨èi⟩ | [ɛj] |  |
| ⟨èu⟩ | [ɛw] |  |
| ⟨é⟩ | [e] |  |
| ⟨í⟩ | [i] |  |
| ⟨ò⟩ | [ɔ] |  |
| ⟨òi⟩ | [ɔj] |  |
| ⟨òu⟩ | [ɔw] |  |
| ⟨ó⟩ | [u] |  |
| ⟨ói⟩ | [uj] |  |
| ⟨ú⟩ | [y] |  |
| ⟨’⟩ | ∅ |  |

Stress falls on the last syllable by default. A written ⟨à⟩ ⟨è⟩ ⟨é⟩ ⟨í⟩ ⟨ò⟩ ⟨ó⟩ ⟨ú⟩ marks the stressed vowel. These endings take final stress: ⟨-ai⟩ ⟨-au⟩ ⟨-ei⟩ ⟨-èi⟩ ⟨-eu⟩ ⟨-èu⟩ ⟨-iu⟩ ⟨-oi⟩ ⟨-òi⟩ ⟨-ou⟩ ⟨-òu⟩ ⟨-ui⟩. These endings take the penult: ⟨-a⟩ ⟨-e⟩ ⟨-i⟩ ⟨-o⟩ ⟨-u⟩ ⟨-as⟩ ⟨-es⟩ ⟨-is⟩ ⟨-os⟩ ⟨-us⟩.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 1 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `n-velar-assimilation` | /n/ → [ŋ], before [k] [ɡ] | ⟨ancora⟩ [aŋˈkuɾɔ] | [Alibert 1976](#src-alibert1976) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "oc-x-aranes")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Aragonese](an.md) · [Home](../index.md) · [Armenian →](hy.md)
