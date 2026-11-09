# Iraqw (`irk`)

<!-- atlas:summary begin -->
Iraqw is an Afro-Asiatic language, written in the Latin script. Glottolog places it in Tanzania. The `irk` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `irk` |
| ISO 639-3 | [irk](https://iso639-3.sil.org/code/irk), Iraqw |
| Glottolog | [iraq1241](https://glottolog.org/resource/languoid/id/iraq1241), Iraqw |
| Wikipedia | [Iraqw language](https://en.wikipedia.org/wiki/Iraqw_language) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) |
| Region | [Africa](by-region.md#africa) > [Tanzania](by-region.md#tanzania) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Afro-Asiatic](https://tigregotico.github.io/orthography2ipa/#x-clade-afro1255) `x-clade-afro1255` |
| Explorer | [`irk` in the data explorer](https://tigregotico.github.io/orthography2ipa/#irk) |
| Spec file | [`irk.json`](../../orthography2ipa/data/irk.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Placed so the ancestry graph covers every living ISO 639-3 language. No orthography is claimed, the phoneme inventory follows the cited PHOIBLE inventory (which itself cites a published description): script is Zyyy (undetermined) until a cited description is encoded. Classification and coordinates follow Glottolog.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1993 to 2026. [Sources](#sources) lists them. The spec file writes all 46 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/irk.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `irk` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 4 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-glottolog2024"></a>Hammarström, Harald, Forkel, Robert, Haspelmath, Martin, Bank, Sebastian (2024). *Glottolog 5.0*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/)
2. <a id="src-phoible2019"></a>Moran, Steven, McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0 (doi:10.5281/zenodo.2562766)*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/inventories/view/129)
3. <a id="src-omniglot-iraqw"></a>Ager, Simon (2026). *Omniglot chart (iraqw.xls)*. Omniglot. [omniglot.com](https://www.omniglot.com/)
4. <a id="src-irk_mous1993"></a>Mous, Maarten (1993). *A Grammar of Iraqw*. Helmut Buske Verlag. [archive.org](https://archive.org/details/rosettaproject_irk_phon-1)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wold` ([lexibank/wold](https://github.com/lexibank/wold)) | `irk` | gold | lexicon-derived | CC BY 4.0 | 1117 | 0.1898 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 49 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t tʰ t̪ |  | c ɟ | k kʷ ɡ ɡʷ | q qʰ qʷʼ |  | ʔ |
| Affricate |  |  | t͡sʼ |  |  |  |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ ŋʷ |  |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Fricative |  | f | s | ʃ |  | x xʷ |  | ħ ʕ | h |
| Lateral fricative |  |  | ɬ |  |  |  |  |  |  |
| Approximant |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː |  | u uː |
| Close-mid | e eː |  | o oː |
| Mid |  | ə |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [t͡ɫʼ] [w] [ɓ] [ɓ̥].

Tones: [˥] PHOIBLE tone segment, [˥˩] PHOIBLE tone segment, [˩] PHOIBLE tone segment.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨/⟩ | [ʕ] |  |
| ⟨a⟩ | [a] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨b⟩ | [b] |  |
| ⟨ch⟩ | [c] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gw⟩ | [ɡʷ] |  |
| ⟨h⟩ | [h] |  |
| ⟨hh⟩ | [ħ] |  |
| ⟨hl⟩ | [ɬ] |  |
| ⟨i⟩ | [i] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [ɟ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kw⟩ | [kʷ] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ngw⟩ | [ŋʷ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [q] |  |
| ⟨qw⟩ | [qʷʼ] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨sl⟩ | [ɬ] |  |
| ⟨t⟩ | [t] |  |
| ⟨tl⟩ | [t͡ɫʼ] |  |
| ⟨ts⟩ | [t͡sʼ] |  |
| ⟨u⟩ | [u] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨xw⟩ | [xʷ] |  |
| ⟨y⟩ | [j] |  |
| ⟨ë⟩ | [ə] |  |
| ⟨ʾ⟩ | [ʔ] |  |
| ⟨ʿ⟩ | [ʕ] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "irk")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Iraqi Arabic](ar-IQ-x-qeltu.md) · [Home](../index.md) · [Irish →](ga.md)
