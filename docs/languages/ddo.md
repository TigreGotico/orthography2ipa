# Dido (`ddo`)

<!-- atlas:summary begin -->
Dido is a Nakh-Daghestanian language, written in the Cyrl script. Glottolog places it in Georgia and Russia. The `ddo` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ddo` |
| ISO 639-3 | [ddo](https://iso639-3.sil.org/code/ddo), Dido |
| Glottolog | [dido1241](https://glottolog.org/resource/languoid/id/dido1241), Tsez |
| Wikipedia | [Tsez language](https://en.wikipedia.org/wiki/Tsez_language) |
| Family | [Nakh-Daghestanian](by-family.md#nakh-daghestanian) |
| Region | [Eurasia](by-region.md#eurasia) > [Georgia](by-region.md#georgia), [Russia](by-region.md#russia) |
| Script | [Cyrl](by-script.md#cyrl) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Nakh-Daghestanian](https://tigregotico.github.io/orthography2ipa/#x-clade-nakh1245) `x-clade-nakh1245` |
| Explorer | [`ddo` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ddo) |
| Spec file | [`ddo.json`](../../orthography2ipa/data/ddo.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Cyrillic-based practical orthography for Tsez following the Avar-based Cyrillic convention used for unwritten Daghestanian languages of this area (Alekseev & Radzhabov's descriptions, Comrie & Polinsky's Tsez fieldwork materials).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1999 to 2024. [Sources](#sources) lists them. The spec file writes all 41 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ddo.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ddo` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what 1 of them support.

1. <a id="src-glottolog2024"></a>Hammarström, Harald, Forkel, Robert, Haspelmath, Martin, Bank, Sebastian (2024). *Glottolog 5.0*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/)
2. <a id="src-phoible2019"></a>Moran, Steven, McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0 (doi:10.5281/zenodo.2562766)*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/inventories/view/2329)
3. <a id="src-comrie_polinsky"></a>Comrie, Bernard, Polinsky, Maria (1999). *Reciprocals without reflexives (and other Tsez/Daghestanian materials)*. in Frajzyngier & Curl (eds.), Reciprocals: Forms and Functions.
4. <a id="src-alekseev_dagh"></a>Alekseev, Mikhail E. (2003). *Tsezskie jazyki (Tsezic languages), in Yazyki mira: Kavkazskie jazyki*. Academia.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `northeuralex` ([lexibank/northeuralex](https://github.com/lexibank/northeuralex)) | `ddo` | gold | lexicon-derived | CC BY 4.0 | 871 | 0.1090 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 40 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʼ |  | d̪ t̪ t̪ʼ |  |  | k kʼ ɡ | q qʼ |  | ʔ |
| Affricate |  |  | ts tsʼ t̪ɬʼ | t̠ʃ t̠ʃʼ |  |  |  |  |  |
| Nasal | m |  | n̪ |  |  |  |  |  |  |
| Trill |  |  | r̪ |  |  |  |  |  |  |
| Fricative |  | f | s z | ʃ ʒ |  |  | ʁ χ | ħ | h |
| Lateral fricative |  |  | ɬ |  |  |  |  |  |  |
| Approximant |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w] [ʜ].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ā⟩ | [aː] |  |
| ⟨а⟩ | [a] |  |
| ⟨аа⟩ | [aː] |  |
| ⟨б⟩ | [b] |  |
| ⟨в⟩ | [w] |  |
| ⟨г⟩ | [ɡ] |  |
| ⟨гъ⟩ | [ʁ] |  |
| ⟨гь⟩ | [h] |  |
| ⟨д⟩ | [d̪] |  |
| ⟨е⟩ | [e] |  |
| ⟨ж⟩ | [ʒ] |  |
| ⟨з⟩ | [z] |  |
| ⟨и⟩ | [i] |  |
| ⟨й⟩ | [j] |  |
| ⟨к⟩ | [k] |  |
| ⟨къ⟩ | [qʼ] |  |
| ⟨кь⟩ | [t̪ɬʼ] |  |
| ⟨кӏ⟩ | [kʼ] |  |
| ⟨л⟩ | [l] |  |
| ⟨лӏ⟩ | [ɬ] |  |
| ⟨м⟩ | [m] |  |
| ⟨н⟩ | [n̪] |  |
| ⟨о⟩ | [o] |  |
| ⟨п⟩ | [p] |  |
| ⟨пӏ⟩ | [pʼ] |  |
| ⟨р⟩ | [r̪] |  |
| ⟨с⟩ | [s] |  |
| ⟨т⟩ | [t̪] |  |
| ⟨тӏ⟩ | [t̪ʼ] |  |
| ⟨у⟩ | [u] |  |
| ⟨ф⟩ | [f] |  |
| ⟨х⟩ | [χ] |  |
| ⟨хъ⟩ | [q] |  |
| ⟨хь⟩ | [ʜ] |  |
| ⟨хӏ⟩ | [ħ] |  |
| ⟨ц⟩ | [ts] |  |
| ⟨цӏ⟩ | [tsʼ] |  |
| ⟨ч⟩ | [t̠ʃ] |  |
| ⟨чӏ⟩ | [t̠ʃʼ] |  |
| ⟨ш⟩ | [ʃ] |  |
| ⟨ъ⟩ | [ʔ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ddo")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Dargwa](dar.md) · [Home](../index.md) · [Dinka →](din.md)
