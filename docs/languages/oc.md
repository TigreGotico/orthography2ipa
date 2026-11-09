# Occitan (`oc`)

<!-- atlas:summary begin -->
Occitan is a Gallo-Romance language, written in the Latin script. Glottolog places it in 5 countries. The `oc` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `oc` |
| Aliases | `oci` |
| ISO 639-3 | [oci](https://iso639-3.sil.org/code/oci), Occitan (post 1500) |
| Glottolog | [occi1239](https://glottolog.org/resource/languoid/id/occi1239), Occitan |
| Wikidata | [Q14185](https://www.wikidata.org/wiki/Q14185) |
| Wikipedia | [Occitan language](https://en.wikipedia.org/wiki/Occitan_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Gallo-Romance](by-family.md#indo-european--italic--romance--gallo-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Andorra](by-region.md#andorra), [France](by-region.md#france), [Italy](by-region.md#italy), [Monaco](by-region.md#monaco), [Spain](by-region.md#spain) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1000, living |
| Parent | [Gallo-Romance](https://tigregotico.github.io/orthography2ipa/#x-clade-gallorom) `x-clade-gallorom` |
| Child lects | 2, see [Related lects](#related-lects) |
| Explorer | [`oc` in the data explorer](https://tigregotico.github.io/orthography2ipa/#oc) |
| Spec file | [`oc.json`](../../orthography2ipa/data/oc.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Lengadocian (Languedocien) in the classical (Alibertine) norm, the reference variety of the norm and the one variety this spec describes.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1973 to 1996. [Sources](#sources) lists them. The spec file writes all 68 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/oc.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `oc` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Provençal (Occitan)](oc-provenc.md) `oc-provenc`: France, research tier
- [Aranese (Gascon Occitan)](oc-x-aranes.md) `oc-x-aranes`: research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-alibert1976"></a>Alibert, L. (1976). *Gramatica occitana*. Institut d'Estudis Occitans.
2. <a id="src-bec1973"></a>Bec, P. (1973). *Manuel pratique d'occitan moderne*. Picard.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
4. <a id="src-wheeler1988"></a>Wheeler, M. W. (1988). *Occitan*. In Harris & Vincent (eds.), The Romance Languages, Routledge. Cited: 246-278.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `oc` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 675 | 0.1283 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 47 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |
| Affricate |  |  |  | ts | dʒ tʃ |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |
| Trill |  |  |  | r |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |
| Fricative | β | f | ð | s z | ʃ |  | ɣ |
| Approximant |  |  |  |  |  | j |  |
| Lateral approximant |  |  |  | l |  | ʎ |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u |
| Close-mid | e |  |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [aj] [aw] [ej] [ew] [iw] [sk] [uj] [w] [we] [ɔj] [ɔw] [ɛj] [ɛw] [ɡw] [ɥɛ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨'⟩ | ∅ |  |
| ⟨a⟩ | [a] [ɔ] | default [a] · posttonic [ɔ] · word final [ɔ] |
| ⟨ai⟩ | [aj] |  |
| ⟨au⟩ | [aw] |  |
| ⟨b⟩ | [b] [β] | default [b] · intervocalic [β] · word final [p] |
| ⟨c⟩ | [k] [s] | before e [s] · before i [s] · default [k] |
| ⟨cc⟩ | [ts] [k] | before e [ts] · before i [ts] · default [k] |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] [ð] | default [d] · intervocalic [ð] · word final [t] |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨ei⟩ | [ej] |  |
| ⟨eu⟩ | [ew] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [dʒ] [ɣ] | before e [dʒ] · before i [dʒ] · default [ɡ] · intervocalic [ɣ] · word final [tʃ] [k] |
| ⟨gu⟩ | [ɡ] | before a [ɡw] · before e [ɡ] · before i [ɡ] · before o [ɡw] · default [ɡ] |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] [j] | before vowel [j] · default [i] · nucleus stressed [i] |
| ⟨iu⟩ | [iw] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨lh⟩ | [ʎ] |  |
| ⟨m⟩ | [m] | default [m] · word final [n] |
| ⟨n⟩ | [n] ∅ | default [n] · word final ∅ |
| ⟨nh⟩ | [ɲ] | default [ɲ] · word final [n] |
| ⟨o⟩ | [u] |  |
| ⟨oi⟩ | [uj] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [k] |  |
| ⟨qu'⟩ | [k] |  |
| ⟨qu’⟩ | [k] |  |
| ⟨r⟩ | [ɾ] [r] ∅ | default [ɾ] · word final ∅ · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] [z] | default [s] · intervocalic [z] |
| ⟨sc⟩ | [sk] [s] | before e [s] · before i [s] · default [sk] |
| ⟨sh⟩ | [ʃ] |  |
| ⟨ss⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tg⟩ | [dʒ] |  |
| ⟨th⟩ | [t] |  |
| ⟨tj⟩ | [dʒ] |  |
| ⟨tz⟩ | [ts] [z] |  |
| ⟨u⟩ | [y] [w] |  |
| ⟨ue⟩ | [ɥɛ] [we] |  |
| ⟨uè⟩ | [ɥɛ] |  |
| ⟨v⟩ | [b] [β] | default [b] · intervocalic [β] |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ts] [s] | before consonant [s] · default [ts] |
| ⟨y⟩ | [i] |  |
| ⟨z⟩ | [z] |  |
| ⟨à⟩ | [a] |  |
| ⟨á⟩ | [ɔ] |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "oc")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Nupe](nup.md) · [Home](../index.md) · [Odia →](or.md)
