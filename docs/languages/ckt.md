# Chukot (`ckt`)

<!-- atlas:summary begin -->
Chukot is a Chukotko-Kamchatkan language, written in the Cyrl script. Glottolog places it in Russia. The `ckt` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ckt` |
| ISO 639-3 | [ckt](https://iso639-3.sil.org/code/ckt), Chukot |
| Glottolog | [chuk1273](https://glottolog.org/resource/languoid/id/chuk1273), Chukchi |
| Wikipedia | [Chukchi language](https://en.wikipedia.org/wiki/Chukchi_language) |
| Family | [Chukotko-Kamchatkan](by-family.md#chukotko-kamchatkan) |
| Region | [Eurasia](by-region.md#eurasia) > [Russia](by-region.md#russia) |
| Script | [Cyrl](by-script.md#cyrl) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Chukotko-Kamchatkan](https://tigregotico.github.io/orthography2ipa/#x-clade-chuk1271) `x-clade-chuk1271` |
| Explorer | [`ckt` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ckt) |
| Spec file | [`ckt.json`](../../orthography2ipa/data/ckt.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Cyrillic literary orthography for Chukchi, codified by Skorik (1961/1968, Grammatika chukotskogo yazyka) and described in Dunn (1999), A Grammar of Chukchi.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1961 to 2024. [Sources](#sources) lists them. The spec file writes all 26 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ckt.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ckt` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 3 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-glottolog2024"></a>Hammarström, Harald, Forkel, Robert, Haspelmath, Martin, Bank, Sebastian (2024). *Glottolog 5.0*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/)
2. <a id="src-phoible2019"></a>Moran, Steven, McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0 (doi:10.5281/zenodo.2562766)*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/inventories/view/195)
3. <a id="src-dunn1999"></a>Dunn, Michael John (1999). *A Grammar of Chukchi*. PhD dissertation, Australian National University. [openresearch-repository.anu.edu.au](https://openresearch-repository.anu.edu.au/handle/1885/9331)
4. <a id="src-skorik1961"></a>Skorik, Pyotr Ya. (1961). *Grammatika chukotskogo yazyka (Grammar of the Chukchi Language), vol. 1*. Academy of Sciences, USSR.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `ckt` | gold | lexicon-derived | CC BY 4.0 | 993 | 0.0972 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 47 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p | t |  |  |  | k kʰ | q | ʔ |
| Affricate |  | ts tɬ | t̠ʃ |  | tɕ | kx |  |  |
| Nasal | m | n nʲ |  |  |  | ŋ |  |  |
| Trill |  | r̠ |  |  |  |  |  |  |
| Fricative | ɸ β | sʲ | ʃ | ʐ͇ | ʝ | x ɣ ɣʷ |  |  |
| Lateral fricative |  | ɬ |  |  |  |  |  |  |
| Approximant |  | ɹ |  |  | j j̥ |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Near-close | ɪ |  |  |
| Close-mid | e | ɵ ɵ̞̆ | o |
| Mid |  | ə ə̆ |  |
| Near-open |  | ɐ |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [a̯e] [a̯ə] [e̯ɪ] [o̯u] [qχ] [tɮ] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨а⟩ | [a] |  |
| ⟨в⟩ | [β] |  |
| ⟨г⟩ | [ɣ] |  |
| ⟨е⟩ | [e] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨к’⟩ | [q] |  |
| ⟨л⟩ | [ɬ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨р⟩ | [ɹ] |  |
| ⟨с⟩ | [sʲ] |  |
| ⟨т⟩ | [t] |  |
| ⟨у⟩ | [u] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨ч⟩ | [tɕ] |  |
| ⟨ъ⟩ | [ʔ] |  |
| ⟨ы⟩ | [ə] |  |
| ⟨ь⟩ | [ʔ] |  |
| ⟨э⟩ | [e] |  |
| ⟨ӄ⟩ | [q] |  |
| ⟨ӈ⟩ | [ŋ] |  |
| ⟨’⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ckt")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Choctaw](cho.md) · [Home](../index.md) · [Chuvash →](cv.md)
