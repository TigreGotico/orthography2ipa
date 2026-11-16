# Dargwa (`dar`)

<!-- atlas:summary begin -->
Dargwa is a Nakh-Daghestanian language, written in the Cyrillic script. Glottolog places it in Azerbaijan, Kazakhstan, Russia and Ukraine. The `dar` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `dar` |
| ISO 639-3 | [dar](https://iso639-3.sil.org/code/dar), Dargwa |
| Glottolog | [darg1241](https://glottolog.org/resource/languoid/id/darg1241), North-Central Dargwa |
| Wikipedia | [Dargwa language](https://en.wikipedia.org/wiki/Dargwa_language) |
| Family | [Nakh-Daghestanian](by-family.md#nakh-daghestanian) |
| Region | [Eurasia](by-region.md#eurasia) > [Azerbaijan](by-region.md#azerbaijan), [Kazakhstan](by-region.md#kazakhstan), [Russia](by-region.md#russia), [Ukraine](by-region.md#ukraine) |
| Script | [Cyrillic](by-script.md#cyrillic) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Nakh-Daghestanian](https://tigregotico.github.io/orthography2ipa/#x-clade-nakh1245) `x-clade-nakh1245` |
| Explorer | [`dar` in the data explorer](https://tigregotico.github.io/orthography2ipa/#dar) |
| Spec file | [`dar.json`](../../orthography2ipa/data/dar.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Dargwa (дарган мез), Northeast Caucasian (Dargic) macro-language of central Dagestan, the literary standard is based on the Akusha dialect and has used a Cyrillic alphabet with the Dagestani ⟨ъ⟩/⟨ь⟩/palochka-style ejective marking since 1938. SKELETON: grapheme inventory now specified.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 2001 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 53 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/dar.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `dar` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what 3 of them support.

1. <a id="src-glottolog2024"></a>Hammarström, Harald, Forkel, Robert, Haspelmath, Martin, Bank, Sebastian (2024). *Glottolog 5.0*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/)
2. <a id="src-dargwa_language_wiki"></a>Wikipedia contributors (2024). *Dargwa language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Dargwa_language)
3. <a id="src-vandenberg2001"></a>van den Berg, Helma (2001). *Dargi Folktales: Oral Stories from the Caucasus with an Introduction to Dargi Grammar*. CNWS, Leiden University.
4. <a id="src-sumbatova_mutalov2003"></a>Sumbatova, Nina R. & Mutalov, Rasul O. (2003). *A Grammar of Icari Dargwa*. Lincom Europa.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `dar` | gold | lexicon-derived | CC BY 4.0 | 1056 | 0.0691 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 53 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ tʼ |  |  | k kʼ kː ɡ | q qʼ qː |  | ʔ |
| Affricate |  |  | t͡s t͡sʰ t͡sʼ t͡ɬʼ | t͡ʃ t͡ʃʰ t͡ʃʼ |  |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Fricative |  | f | s z | ʃ ʃː ʒ |  | x | ʁ χ χː | ħ ʕ | h |
| Lateral fricative |  |  | ɬ |  |  |  |  |  |  |
| Approximant |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid | e |  | o |
| Open | a |  |  |

Sequences that the spec writes as one unit: [ja] [je] [ju] [q͡χ] [w] [ʲ].
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
| ⟨къ⟩ | [q] |  |
| ⟨къкъ⟩ | [qː] |  |
| ⟨кь⟩ | [qʼ] |  |
| ⟨кӏ⟩ | [kʼ] |  |
| ⟨л⟩ | [l] |  |
| ⟨лъ⟩ | [ɬ] |  |
| ⟨лӏ⟩ | [t͡ɬʼ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [pʰ] |  |
| ⟨пп⟩ | [p] |  |
| ⟨р⟩ | [r] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [tʰ] |  |
| ⟨тт⟩ | [t] |  |
| ⟨тӏ⟩ | [tʼ] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [χ] |  |
| ⟨хх⟩ | [χː] |  |
| ⟨хъ⟩ | [q͡χ] |  |
| ⟨хь⟩ | [x] |  |
| ⟨хӏ⟩ | [ħ] |  |
| ⟨ц⟩ | [t͡sʰ] |  |
| ⟨цц⟩ | [t͡s] |  |
| ⟨цӏ⟩ | [t͡sʼ] |  |
| ⟨ч⟩ | [t͡ʃʰ] |  |
| ⟨чч⟩ | [t͡ʃ] |  |
| ⟨чӏ⟩ | [t͡ʃʼ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨щ⟩ | [ʃː] |  |
| ⟨ъ⟩ | [ʔ] |  |
| ⟨ы⟩ | [ɨ] |  |
| ⟨ь⟩ | [ʲ] |  |
| ⟨э⟩ | [e] |  |
| ⟨ю⟩ | [ju] |  |
| ⟨я⟩ | [ja] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "dar")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Danish](da.md) · [Home](../index.md) · [Dido →](ddo.md)
