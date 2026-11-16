# Avar (`av`)

<!-- atlas:summary begin -->
Avar is a Nakh-Daghestanian language, written in the Cyrillic script. Glottolog places it in Azerbaijan, Georgia, Russia and Türkiye. The `av` spec is at the research tier. It cites 2 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `av` |
| ISO 639-3 | [ava](https://iso639-3.sil.org/code/ava), Avaric |
| Glottolog | [avar1256](https://glottolog.org/resource/languoid/id/avar1256), Avar |
| Wikidata | [Q29561](https://www.wikidata.org/wiki/Q29561) |
| Wikipedia | [Avar language](https://en.wikipedia.org/wiki/Avar_language) |
| Family | [Nakh-Daghestanian](by-family.md#nakh-daghestanian) |
| Region | [Eurasia](by-region.md#eurasia) > [Azerbaijan](by-region.md#azerbaijan), [Georgia](by-region.md#georgia), [Russia](by-region.md#russia), [Türkiye](by-region.md#türkiye) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Nakh-Daghestanian](https://tigregotico.github.io/orthography2ipa/#x-clade-nakh1245) `x-clade-nakh1245` |
| Explorer | [`av` in the data explorer](https://tigregotico.github.io/orthography2ipa/#av) |
| Spec file | [`av.json`](../../orthography2ipa/data/av.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Avar (авар мацӏ, Magharul mats'), the largest Northeast Caucasian (Avar, Andic) language, literary language of Dagestan. Cyrillic alphabet since 1938, digraphs with ⟨ъ⟩, ⟨ь⟩ and the palochka ⟨ӏ⟩ mark uvulars, laterals and ejectives, and doubled letters mark the fortis (geminate) series.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1981 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 56 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/av.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `av` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-avar_language_wiki"></a>Wikipedia contributors (2026). *Avar language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Avar_language)
2. <a id="src-charachidze1981"></a>Charachidzé, Georges (1981). *Grammaire de la langue avar*. Éditions Jean-Favard. [archive.org](https://archive.org/details/rosettaproject_ava_phon-1)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `av` | gold | lexicon-derived | CC BY 4.0 | 954 | 0.0990 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 56 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t tʼ |  |  | k kʼ kː ɡ |  |  | ʔ |
| Affricate |  |  | t͡s t͡sʼ t͡sʼː t͡sː t͡ɬʼː t͡ɬː | t͡ʃ t͡ʃʼ t͡ʃʼː t͡ʃː |  |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Fricative |  | f | s sː z | ʃ ʃː ʒ |  | x xː | ʁ χ χː | ħ ʕ | h |
| Lateral fricative |  |  | ɬ ɬː |  |  |  |  |  |  |
| Approximant |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid | e |  | o |
| Open | a |  |  |

Sequences that the spec writes as one unit: [ja] [je] [jo] [ju] [q͡χʼː] [q͡χː] [w] [ʲ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [w] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨гъ⟩ | [ʁ] |  |
| ⟨гь⟩ | [h] |  |
| ⟨гӏ⟩ | [ʕ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [e] [je] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨кк⟩ | [kː] |  |
| ⟨къ⟩ | [q͡χʼː] |  |
| ⟨кь⟩ | [t͡ɬʼː] |  |
| ⟨кӏ⟩ | [kʼ] |  |
| ⟨л⟩ | [l] |  |
| ⟨лъ⟩ | [ɬ] |  |
| ⟨лълъ⟩ | [ɬː] |  |
| ⟨лӏ⟩ | [t͡ɬː] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨сс⟩ | [sː] |  |
| ⟨т⟩ | [t] |  |
| ⟨тӏ⟩ | [tʼ] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [χ] |  |
| ⟨хх⟩ | [χː] |  |
| ⟨хъ⟩ | [q͡χː] |  |
| ⟨хь⟩ | [x] |  |
| ⟨хьхь⟩ | [xː] |  |
| ⟨хӏ⟩ | [ħ] |  |
| ⟨ц⟩ | [t͡s] |  |
| ⟨цц⟩ | [t͡sː] |  |
| ⟨цӏ⟩ | [t͡sʼ] |  |
| ⟨цӏцӏ⟩ | [t͡sʼː] |  |
| ⟨ч⟩ | [t͡ʃ] |  |
| ⟨чч⟩ | [t͡ʃː] |  |
| ⟨чӏ⟩ | [t͡ʃʼ] |  |
| ⟨чӏчӏ⟩ | [t͡ʃʼː] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ʃː] |  |
| ⟨ъ⟩ | [ʔ] |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ё⟩ | [jo] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "av")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Atong](aot.md) · [Home](../index.md) · [Ayacucho Quechua →](quy.md)
