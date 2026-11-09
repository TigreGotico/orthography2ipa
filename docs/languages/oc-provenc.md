# Provençal (Occitan) (`oc-provenc`)

<!-- atlas:summary begin -->
Provençal (Occitan) is a Gallo-Romance language, written in the Latin script. Glottolog places it in France. The `oc-provenc` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `oc-provenc` |
| Aliases | `oc-x-provencau` |
| ISO 639-3 | [oci](https://iso639-3.sil.org/code/oci), Occitan (post 1500) |
| Glottolog | [prov1235](https://glottolog.org/resource/languoid/id/prov1235), Provençal |
| Wikidata | [Q241243](https://www.wikidata.org/wiki/Q241243) |
| Wikipedia | [Provençal](https://fr.wikipedia.org/wiki/Proven%C3%A7al) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Gallo-Romance](by-family.md#indo-european--italic--romance--gallo-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [France](by-region.md#france) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1200, living |
| Parent | [Occitan](oc.md) `oc` |
| Explorer | [`oc-provenc` in the data explorer](https://tigregotico.github.io/orthography2ipa/#oc-provenc) |
| Spec file | [`oc-provenc.json`](../../orthography2ipa/data/oc-provenc.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Provençal (provençau) in the classical (Alibertine) norm, as a child of the Lengadocian spec. Only the letters whose value the source states SEPARATELY for Provençal are written here.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1973 to 2026. [Sources](#sources) lists them. The spec file writes 3 of the 68 spellings of its letter table and takes the other 65 from [Occitan](oc.md) `oc`.

The [spec file](../../orthography2ipa/data/oc-provenc.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `oc-provenc` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-locongres_graphie_phonie"></a>Lo Congrès permanent de la lenga occitana, scientific direction Maurici Romieu, with Joan Claudi Rixte and Bernat Molin (2026). *Relacions grafia-fonia / Relations graphie-phonie*. Lo Congrès permanent de la lenga occitana. [locongres.org](https://locongres.org/fr/competences/normes/graphie-phonie/prononciation)
2. <a id="src-alibert1976"></a>Alibert, L. (1976). *Gramatica occitana*. Institut d'Estudis Occitans.
3. <a id="src-bec1973"></a>Bec, P. (1973). *Manuel pratique d'occitan moderne*. Picard.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 50 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Uvular |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  | ts | dʒ tʃ |  |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |
| Trill |  |  |  | r |  |  |  | ʀ |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative | β | f v | ð | s z | ʃ |  | ɣ |  |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  | ʎ |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u |
| Close-mid | e |  |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [aj] [aw] [ej] [ew] [iw] [sk] [uj] [w] [we] [wej] [ɔj] [ɔw] [ɛj] [ɛw] [ɡw] [ɥɛ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | ∅ |  |
| ⟨a⟩ | [a] [ɔ] | default [a] · posttonic [ɔ] · word final [ɔ] |
| ⟨ai⟩ | [aj] | default [aj] · posttonic [ej] · pretonic [ej] |
| ⟨au⟩ | [aw] | default [aw] · posttonic [ɔw] · pretonic [ɔw] |
| ⟨b⟩ | [b] [β] | default [b] · intervocalic [β] · word final [p] |
| ⟨c⟩ | [k] [s] | before e [s] · before i [s] · default [k] · word final ∅ |
| ⟨cc⟩ | [ts] [k] | before e [ts] · before i [ts] · default [k] |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] [ð] | default [d] · intervocalic [ð] · word final ∅ |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨ei⟩ | [ej] |  |
| ⟨eu⟩ | [ew] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [dʒ] [ɣ] | before e [dʒ] · before i [dʒ] · default [ɡ] · intervocalic [ɣ] · word final ∅ |
| ⟨gu⟩ | [ɡ] | before a [ɡw] · before e [ɡ] · before i [ɡ] · before o [ɡw] · default [ɡ] |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] [j] | before vowel [j] · default [i] · nucleus stressed [i] |
| ⟨iu⟩ | [iw] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨lh⟩ | [ʎ] | default [ʎ] · word final [j] |
| ⟨m⟩ | [m] | default [m] · word final [n] |
| ⟨n⟩ | [n] ∅ | default [n] · word final [n] |
| ⟨nh⟩ | [ɲ] | default [ɲ] · word final [n] |
| ⟨o⟩ | [u] |  |
| ⟨oi⟩ | [wej] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [k] |  |
| ⟨qu'⟩ | [k] |  |
| ⟨qu’⟩ | [k] |  |
| ⟨r⟩ | [ɾ] [r] ∅ | default [ɾ] · word final [ʀ] · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] [z] | default [s] · intervocalic [z] |
| ⟨sc⟩ | [sk] [s] | before e [s] · before i [s] · default [sk] |
| ⟨sh⟩ | [ʃ] |  |
| ⟨ss⟩ | [s] |  |
| ⟨t⟩ | [t] | default [t] · word final ∅ |
| ⟨tg⟩ | [dʒ] |  |
| ⟨th⟩ | [t] |  |
| ⟨tj⟩ | [dʒ] |  |
| ⟨tz⟩ | [ts] [z] | default [ts] · word final [s] |
| ⟨u⟩ | [y] [w] |  |
| ⟨ue⟩ | [ɥɛ] [we] |  |
| ⟨uè⟩ | [ɥɛ] |  |
| ⟨v⟩ | [v] | default [v] · intervocalic [v] |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ts] [s] | before consonant [s] · default [ts] |
| ⟨y⟩ | [i] |  |
| ⟨z⟩ | [z] |  |
| ⟨à⟩ | [a] |  |
| ⟨á⟩ | [e] |  |
| ⟨ç⟩ | [s] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨èi⟩ | [ɛj] |  |
| ⟨èu⟩ | [ɛw] |  |
| ⟨é⟩ | [e] |  |
| ⟨í⟩ | [i] |  |
| ⟨ï⟩ | [i] |  |
| ⟨ò⟩ | [ɔ] |  |
| ⟨òi⟩ | [ɔj] |  |
| ⟨òu⟩ | [ɔw] |  |
| ⟨ó⟩ | [u] |  |
| ⟨ói⟩ | [uj] |  |
| ⟨ú⟩ | [y] |  |
| ⟨ü⟩ | [y] |  |
| ⟨’⟩ | ∅ |  |

Stress falls on the last syllable by default. A written ⟨à⟩ ⟨á⟩ ⟨è⟩ ⟨é⟩ ⟨í⟩ ⟨ò⟩ ⟨ó⟩ ⟨ú⟩ marks the stressed vowel. These endings take final stress: ⟨-ai⟩ ⟨-au⟩ ⟨-ei⟩ ⟨-èi⟩ ⟨-eu⟩ ⟨-èu⟩ ⟨-iu⟩ ⟨-oi⟩ ⟨-òi⟩ ⟨-ói⟩ ⟨-ou⟩ ⟨-òu⟩ ⟨-ui⟩ ⟨-uè⟩. These endings take the penult: ⟨-a⟩ ⟨-e⟩ ⟨-i⟩ ⟨-o⟩ ⟨-u⟩ ⟨-as⟩ ⟨-es⟩ ⟨-is⟩ ⟨-os⟩ ⟨-us⟩.
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "oc-provenc")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Proto-Peninsular Arabic](ar-x-peninsul.md) · [Home](../index.md) · [Puerto Rican Spanish →](es-PR.md)
