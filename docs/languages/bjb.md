# Banggarla (`bjb`)

<!-- atlas:summary begin -->
Banggarla is a Pama-Nyungan language, written in the Latin script. Glottolog places it in the Australia and Papunesia macroareas. The `bjb` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `bjb` |
| ISO 639-3 | [bjb](https://iso639-3.sil.org/code/bjb), Banggarla |
| Wikipedia | [Barngarla language](https://en.wikipedia.org/wiki/Barngarla_language) |
| Family | [Pama-Nyungan](by-family.md#pama-nyungan) |
| Region | [Australia](by-region.md#several-macroareas), [Papunesia](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Pama-Nyungan](https://tigregotico.github.io/orthography2ipa/#x-clade-pama1250) `x-clade-pama1250` |
| Explorer | [`bjb` in the data explorer](https://tigregotico.github.io/orthography2ipa/#bjb) |
| Spec file | [`bjb.json`](../../orthography2ipa/data/bjb.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Pama-Nyungan (Thura-Yura) language of the Eyre Peninsula, South Australia, in the modern revival orthography. Retroflex consonants are written as r-plus-consonant digraphs (rd, rn, rl), the retroflex approximant as rh, dental consonants with h (dh, nh, lh) and the palatal stop as dy.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 2015 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 26 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/bjb.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `bjb` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-bjb_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Banggarla (bang1339)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/bang1339)
2. <a id="src-bjb_wikipedia"></a>Wikipedia contributors (2024). *Barngarla language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Barngarla_language)
3. <a id="src-bjb_clendon2015"></a>Clendon, Mark (2015). *Clamor Schürmann's Barngarla Grammar: A commentary on the first section of A Vocabulary of the Parnkalla Language*. University of Adelaide Press. [adelaide.edu.au](https://www.adelaide.edu.au/press/titles/barngarla)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `bjb` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 136 | 0.1021 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 26 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Retroflex | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | b | d d̪ | ɖ | ɟ | ɡ |
| Nasal | m | n n̪ | ɳ | ɲ | ŋ |
| Trill |  | r |  |  |  |
| Tap |  | ɾ |  |  |  |
| Approximant |  |  | ɻ | j |  |
| Lateral approximant |  | l l̪ | ɭ | ʎ |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨dh⟩ | [d̪] |  |
| ⟨dy⟩ | [ɟ] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨l⟩ | [l] |  |
| ⟨lh⟩ | [l̪] |  |
| ⟨ly⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nh⟩ | [n̪] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨oo⟩ | [u] |  |
| ⟨r⟩ | [r] |  |
| ⟨rd⟩ | [ɖ] |  |
| ⟨rh⟩ | [ɻ] |  |
| ⟨rl⟩ | [ɭ] |  |
| ⟨rn⟩ | [ɳ] |  |
| ⟨rr⟩ | [ɾ] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "bjb")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Bambara](bm.md) · [Home](../index.md) · [Banjar →](bjn.md)
