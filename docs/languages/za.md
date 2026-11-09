# Zhuang (`za`)

<!-- atlas:summary begin -->
Zhuang is a Tai-Kadai language, written in the Latin script. Glottolog places it in China. The `za` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `za` |
| ISO 639-3 | [zha](https://iso639-3.sil.org/code/zha), Zhuang |
| Glottolog | [yong1276](https://glottolog.org/resource/languoid/id/yong1276), Yongbei Zhuang |
| Wikidata | [Q13216](https://www.wikidata.org/wiki/Q13216) |
| Wikipedia | [Zhuang languages](https://en.wikipedia.org/wiki/Zhuang_languages) |
| Family | [Tai-Kadai](by-family.md#tai-kadai) |
| Region | [Eurasia](by-region.md#eurasia) > [China](by-region.md#china) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1957, living |
| Parent | [Tai-Kadai](https://tigregotico.github.io/orthography2ipa/#x-clade-taik1256) `x-clade-taik1256` |
| Explorer | [`za` in the data explorer](https://tigregotico.github.io/orthography2ipa/#za) |
| Spec file | [`za.json`](../../orthography2ipa/data/za.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Zhuang (Vahcuengh), Tai language of Guangxi, China. The map commits to STANDARD ZHUANG in the OFFICIAL 1982 LATIN ORTHOGRAPHY (the 1957 alphabet's Cyrillic/IPA-derived letters were replaced by plain Latin letters in the 1982 reform), the pronunciation modelled is that of the standard (Wuming/Shuangqiao) dialect.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 2025. 3 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 37 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/za.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `za` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 4 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-zhuang_wiki"></a>Wikipedia contributors (2025). *Zhuang languages*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Zhuang_languages)
2. <a id="src-standard_zhuang_wiki"></a>Wikipedia contributors (2025). *Standard Zhuang*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Standard_Zhuang)
3. <a id="src-sawndip_wiki"></a>Wikipedia contributors (2025). *Sawndip*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Sawndip)
4. <a id="src-vandeweijer2025_hongshui_he_zhuang"></a>van de Weijer, Jeroen, Lin, Yuhan, Wei, Weiyun (2025). *Hongshui He Zhuang (Baima dialect). Illustrations of the IPA*. Journal of the International Phonetic Association 55(3), 537-555 (CC-BY). Cited: 538, 552-553. [doi.org](https://doi.org/10.1017/S0025100325100704)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `za` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1682 | 0.2124 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 35 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʲ |  |  | t |  | k kʲ kʷ |  |
| Nasal | m mʲ |  |  | n | ɲ | ŋ ŋʷ |  |
| Fricative |  | f | θ |  | ɕ | ɣ | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u ɯ |
| Close-mid | e | o oː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w] [ɓ] [ɗ] [˥] [˦˨] [˧] [˧˥] [˧˩].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [aː] |  |
| ⟨ae⟩ | [a] |  |
| ⟨b⟩ | [p] |  |
| ⟨by⟩ | [pʲ] |  |
| ⟨c⟩ | [ɕ] |  |
| ⟨d⟩ | [t] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [k] |  |
| ⟨gv⟩ | [kʷ] |  |
| ⟨gy⟩ | [kʲ] |  |
| ⟨h⟩ | [h] | default [h] · word final [˧] |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [˥] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mb⟩ | [ɓ] |  |
| ⟨my⟩ | [mʲ] |  |
| ⟨n⟩ | [n] |  |
| ⟨nd⟩ | [ɗ] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ngv⟩ | [ŋʷ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [oː] |  |
| ⟨oe⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [˧˥] |  |
| ⟨r⟩ | [ɣ] |  |
| ⟨s⟩ | [θ] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [w] |  |
| ⟨w⟩ | [ɯ] |  |
| ⟨x⟩ | [˦˨] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [˧˩] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "za")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Zazaki](diq.md) · [Home](../index.md) · [Zou →](zom.md)
