# Aragonese (`an`)

<!-- atlas:summary begin -->
Aragonese is an Ibero-Romance language, written in the Latin script. Glottolog places it in France and Spain. The `an` spec is at the research tier. It cites 5 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `an` |
| Aliases | `arg` |
| ISO 639-3 | [arg](https://iso639-3.sil.org/code/arg), Aragonese |
| Glottolog | [arag1245](https://glottolog.org/resource/languoid/id/arag1245), Aragonese |
| Wikidata | [Q8765](https://www.wikidata.org/wiki/Q8765) |
| Wikipedia | [Aragonese language](https://en.wikipedia.org/wiki/Aragonese_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Ibero-Romance](by-family.md#indo-european--italic--romance--ibero-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [France](by-region.md#france), [Spain](by-region.md#spain) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1050, living |
| Parent | [Ibero-Romance](https://tigregotico.github.io/orthography2ipa/#x-clade-iberrom) `x-clade-iberrom` |
| Child lects | 8, see [Related lects](#related-lects) |
| Explorer | [`an` in the data explorer](https://tigregotico.github.io/orthography2ipa/#an) |
| Spec file | [`an.json`](../../orthography2ipa/data/an.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Aragonese (aragonés, also called fabla aragonesa), an Ibero-Romance language of the autonomous community of Aragon, Spain.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 2001 to 2023. [Sources](#sources) lists them. The spec file writes all 58 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/an.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `an` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Ansotano Aragonese (Ansó valley)](https://tigregotico.github.io/orthography2ipa/#an-x-ansotano) `an-x-ansotano`: skeleton tier
- [Belsetán Aragonese (Bielsa valley)](an-x-belsetan.md) `an-x-belsetan`: research tier
- [Benasquese (patués, Benasque valley)](an-x-benasque.md) `an-x-benasque`: research tier
- [Cheso Aragonese (Hecho/Echo valley)](an-x-cheso.md) `an-x-cheso`: research tier
- [Chistabín Aragonese (Gistaín/Chistau valley)](an-x-chistau.md) `an-x-chistau`: research tier
- [Western Aragonese](an-x-occident.md) `an-x-occident`: research tier
- [Eastern Aragonese (Ribagorçan)](https://tigregotico.github.io/orthography2ipa/#an-x-oriental) `an-x-oriental`: skeleton tier
- [Tensino Aragonese (Valle de Tena / Panticosa)](https://tigregotico.github.io/orthography2ipa/#an-x-tensino) `an-x-tensino`: skeleton tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 1 of them have a DOI or a URL.

1. <a id="src-hualde2005"></a>Hualde, J.I. (2005). *The Sounds of Spanish*. Cambridge University Press.
2. <a id="src-nagore_lain2001"></a>Nagore Laín, F. (2001). *Gramática de la Lengua Aragonesa*. Librería General.
3. <a id="src-penny2002"></a>Penny, R. (2002). *A History of the Spanish Language*. Cambridge University Press.
4. <a id="src-GBA2021"></a>Estudio de Filología Aragonesa (2021). *Gramatica basica de l'aragonés*. Prensas de la Universidad de Zaragoza.
5. <a id="src-OA2023"></a>Academia Aragonesa de la Lengua (2023). *Ortografía de l'aragonés*. Academia Aragonesa de la Lengua. [academiaaragonesadelalengua.org](https://academiaaragonesadelalengua.org/sites/default/files/ficheros-pdf/ortografia-aragones.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `an` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 902 | 0.0580 | yes |
| `spain_romance_tts` | `an` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.0420 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 52 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |
| Affricate |  |  |  | ts | tʃ |  |  |
| Nasal | m |  |  | n |  | ɲ |  |
| Trill |  |  |  | r |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |
| Fricative | β | f | ð θ | s | ʃ | ʝ | x ɣ |
| Approximant |  |  |  |  |  | j |  |
| Lateral approximant |  |  |  | l |  | ʎ |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [aj] [aw] [ej] [ew] [iʃ] [ja] [je] [jo] [ju] [jʃ] [ks] [oj] [w] [wa] [we] [wi] [wo] [ɡw] [ɡwe] [ɡwi].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [aj] |  |
| ⟨au⟩ | [aw] |  |
| ⟨b⟩ | [b] | intervocalic [β] |
| ⟨c⟩ | [k] [θ] [s] | before e [θ] [s] · before i [θ] [s] |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] | intervocalic [ð] · word final [ð] ∅ |
| ⟨e⟩ | [e] |  |
| ⟨ei⟩ | [ej] |  |
| ⟨eu⟩ | [ew] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [tʃ] [x] | before e [x] [tʃ] · before i [x] [tʃ] · intervocalic [ɣ] |
| ⟨gu⟩ | [ɡ] | before a [ɡw] · before e [ɡ] · before i [ɡ] · before o [ɡw] · default [ɡ] |
| ⟨güe⟩ | [ɡwe] |  |
| ⟨güi⟩ | [ɡwi] |  |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨ia⟩ | [ja] |  |
| ⟨ie⟩ | [je] |  |
| ⟨io⟩ | [jo] |  |
| ⟨iu⟩ | [ju] |  |
| ⟨ix⟩ | [ʃ] [iʃ] [jʃ] |  |
| ⟨j⟩ | [x] [tʃ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] [ʎ] | onset [l] [ʎ] |
| ⟨ll⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨oi⟩ | [oj] |  |
| ⟨p⟩ | [p] |  |
| ⟨qu⟩ | [k] |  |
| ⟨r⟩ | [ɾ] [r] | before consonant [ɾ] · intervocalic [ɾ] · word final [ɾ] · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨tz⟩ | [θ] [ts] |  |
| ⟨u⟩ | [u] |  |
| ⟨ua⟩ | [wa] |  |
| ⟨ue⟩ | [we] |  |
| ⟨ui⟩ | [wi] |  |
| ⟨uo⟩ | [wo] |  |
| ⟨v⟩ | [b] | intervocalic [β] |
| ⟨w⟩ | [w] [b] |  |
| ⟨x⟩ | [ʃ] [ks] |  |
| ⟨y⟩ | [ʝ] [j] [i] |  |
| ⟨z⟩ | [θ] [s] |  |
| ⟨á⟩ | [a] |  |
| ⟨è⟩ | [ɛ] |  |
| ⟨é⟩ | [e] |  |
| ⟨í⟩ | [i] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ò⟩ | [ɔ] |  |
| ⟨ó⟩ | [o] |  |
| ⟨ú⟩ | [u] |  |
| ⟨ü⟩ | [u] |  |

Stress falls on the penult by default. A written ⟨á⟩ ⟨é⟩ ⟨è⟩ ⟨í⟩ ⟨ó⟩ ⟨ò⟩ ⟨ú⟩ marks the stressed vowel. These endings take final stress: ⟨-r⟩ ⟨-l⟩ ⟨-d⟩ ⟨-z⟩ ⟨-x⟩ ⟨-t⟩ ⟨-c⟩ ⟨-k⟩ ⟨-f⟩ ⟨-n⟩ ⟨-m⟩. These endings take the penult: ⟨-s⟩ ⟨-ns⟩.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "an")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Arabic](ar-Latn-x-buckwalt.md) · [Home](../index.md) · [Aranese →](oc-x-aranes.md)
