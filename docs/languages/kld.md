# Gamilaraay (`kld`)

<!-- atlas:summary begin -->
Gamilaraay is a Pama-Nyungan language, written in the Latin script. Glottolog places it in the Australia and Papunesia macroareas. The `kld` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kld` |
| ISO 639-3 | [kld](https://iso639-3.sil.org/code/kld), Gamilaraay |
| Wikipedia | [Gamilaraay language](https://en.wikipedia.org/wiki/Gamilaraay_language) |
| Family | [Pama-Nyungan](by-family.md#pama-nyungan) |
| Region | [Australia](by-region.md#several-macroareas), [Papunesia](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Pama-Nyungan](https://tigregotico.github.io/orthography2ipa/#x-clade-pama1250) `x-clade-pama1250` |
| Explorer | [`kld` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kld) |
| Spec file | [`kld.json`](../../orthography2ipa/data/kld.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Research. Pama-Nyungan (Yuwaalaraay-Gamilaraay) language of New South Wales, Australia. The single stop series is spelled with voiced letters (b d g, dental dh, palatal dj), rr is the alveolar trill and single r the retroflex approximant. Long vowels are written by doubling (aa ii uu).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1993 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 21 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kld.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kld` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-kld_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Yuwaalaraay-Gamilaraay (gami1243)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/gami1243)
2. <a id="src-austin1993"></a>Austin, Peter (1993). *A Reference Grammar of Gamilaraay, Northern New South Wales*. La Trobe University. [peterkaustin.com](http://www.peterkaustin.com/docs/Austin_1993_Gamilaraay.pdf)
3. <a id="src-kld_wikipedia"></a>Wikipedia contributors (2024). *Gamilaraay language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Gamilaraay_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `kld` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 515 | 0.0550 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 21 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Retroflex | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|
| Plosive | b | d d̪ |  | ɟ | ɡ |
| Nasal | m | n n̪ |  | ɲ | ŋ |
| Trill |  | r |  |  |  |
| Approximant |  |  | ɻ | j |  |
| Lateral approximant |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
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
| ⟨dj⟩ | [ɟ] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nh⟩ | [n̪] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨r⟩ | [ɻ] |  |
| ⟨rr⟩ | [r] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kld")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Galician](gl-ES-x-reintegr.md) · [Home](../index.md) · [Garo →](grt.md)
