# Bashkir (`ba`)

<!-- atlas:summary begin -->
Bashkir is a Turkic language, written in the Cyrillic script. Glottolog places it in Kazakhstan, Russia and Ukraine. The `ba` spec is at the research tier. It cites 2 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ba` |
| ISO 639-3 | [bak](https://iso639-3.sil.org/code/bak), Bashkir |
| Glottolog | [bash1264](https://glottolog.org/resource/languoid/id/bash1264), Bashkir |
| Wikidata | [Q13389](https://www.wikidata.org/wiki/Q13389) |
| Wikipedia | [Bashkir language](https://en.wikipedia.org/wiki/Bashkir_language) |
| Family | [Turkic](by-family.md#turkic) |
| Region | [Eurasia](by-region.md#eurasia) > [Kazakhstan](by-region.md#kazakhstan), [Russia](by-region.md#russia), [Ukraine](by-region.md#ukraine) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1939, living |
| Parent | [Proto-Turkic (family node)](https://tigregotico.github.io/orthography2ipa/#trk) `trk` |
| Explorer | [`ba` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ba) |
| Spec file | [`ba.json`](../../orthography2ipa/data/ba.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Bashkir in Cyrillic script (Russia). Distinctive interdentals: Ҙ = /ð/, Ҫ = /θ/, unusual among Turkic and a defining contrast against Tatar. Ҡ = /q/ (uvular stop), Ғ = /ʁ/, Ң = /ŋ/, Һ = /h/. Nine vowels with front/back harmony: а /a/, ә /æ/, о /o/, ө /ø/, у /u/, ү /y/, ы /ɯ/, и /i/, е /e/.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 2 works, from 1964 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 60 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ba.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ba` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-bashkir_wiki"></a>Wikipedia contributors (2024). *Bashkir language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Bashkir_language)
2. <a id="src-poppe_1964"></a>Poppe, Nicholas (1964). *Bashkir Manual*. Indiana University, Uralic and Altaic Series.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ba` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 171 | 0.2685 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `ba` | generated | epitran-derived | CC0 1.0 | 70528 | 0.4047 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 57 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ | q |  |
| Affricate |  |  |  | ts | tʃ |  |  |  |  |
| Nasal | m |  |  | n |  |  | ŋ |  |  |
| Trill |  |  |  | r |  |  |  |  |  |
| Fricative |  | f v | ð θ | s z | ʃ ʒ |  | x | ʁ | h |
| Approximant |  |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u ɯ |
| Close-mid | e ø | o |
| Near-open | æ |  |
| Open | a |  |

Sequences that the spec writes as one unit: [aje] [aw] [eje] [ew] [ije] [iw] [ja] [je] [jew] [jo] [ju] [oje] [ow] [uw] [yw] [æje] [æw] [øje] [øw] [ɯje] [ɯw] [ʃtʃ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨ае⟩ | [aje] |  |
| ⟨ау⟩ | [aw] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [v] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨д⟩ | [d] |  |
| ⟨е⟩ | [je] | default [e] · word initial [je] |
| ⟨ее⟩ | [eje] |  |
| ⟨еү⟩ | [ew] | default [ew] · word initial [jew] |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨ие⟩ | [ije] |  |
| ⟨иү⟩ | [iw] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨л⟩ | [l] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨ое⟩ | [oje] |  |
| ⟨оу⟩ | [ow] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨уу⟩ | [uw] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [x] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tʃ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ʃtʃ] |  |
| ⟨ъ⟩ | ∅ |  |
| ⟨ъе⟩ | [je] |  |
| ⟨ы⟩ | [ɯ] |  |
| ⟨ые⟩ | [ɯje] |  |
| ⟨ыу⟩ | [ɯw] |  |
| ⟨ь⟩ | ∅ |  |
| ⟨ье⟩ | [je] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |
| ⟨ё⟩ | [jo] |  |
| ⟨ғ⟩ | [ʁ] |  |
| ⟨ҙ⟩ | [ð] |  |
| ⟨ҡ⟩ | [q] |  |
| ⟨ң⟩ | [ŋ] |  |
| ⟨ҫ⟩ | [θ] |  |
| ⟨ү⟩ | [y] |  |
| ⟨үү⟩ | [yw] |  |
| ⟨һ⟩ | [h] |  |
| ⟨ә⟩ | [æ] |  |
| ⟨әе⟩ | [æje] |  |
| ⟨әү⟩ | [æw] |  |
| ⟨ө⟩ | [ø] |  |
| ⟨өе⟩ | [øje] |  |
| ⟨өү⟩ | [øw] |  |

Stress falls on the last syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ba")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Basaa](bas.md) · [Home](../index.md) · [Bats →](bbl.md)
