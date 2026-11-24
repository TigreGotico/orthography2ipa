# Lolopo (`ycl`)

<!-- agent-hint
covers: what the `ycl` spec holds: its place in the family tree, its sources and scores, its sounds, its spelling rules and transcribed examples
source: `orthography2ipa/data/ycl.json`, `benchmarks/results.json`, `scripts/atlas_snapshot.json`
generated: partly. `scripts/gen_language_atlas.py` writes this hint and the blocks between the `atlas:` markers. Edit the generator for those, and the page for the prose between them
verify: `PYTHONPATH=$PWD python scripts/gen_language_atlas.py --check`
see: `docs/languages/a-z.md`, `docs/specs/quality_tiers.md`, `orthography2ipa/data/SCHEMA.md`
-->

<!-- atlas:summary begin -->
Lolopo is a Sino-Tibetan language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `ycl` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ycl` |
| ISO 639-3 | [ycl](https://iso639-3.sil.org/code/ycl), Lolopo |
| Wikipedia | [Lolopo language](https://en.wikipedia.org/wiki/Lolopo_language) |
| Family | [Sino-Tibetan](by-family.md#sino-tibetan) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Sino-Tibetan](https://tigregotico.github.io/orthography2ipa/#x-clade-sino1245) `x-clade-sino1245` |
| Explorer | [`ycl` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ycl) |
| Spec file | [`ycl.json`](../../orthography2ipa/data/ycl.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Lolopo / Yao'an Central Yi (Loloish, Sino-Tibetan) of Yunnan, China, in the Roman practical orthography developed by W. Scott Merrifield, in which speakers call their own speech ⟨Loxrlavu⟩. The Yi syllabary is a SEPARATE writing system for the Yi languages and is not mapped here (see the `ii` spec).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 5 works, from 2001 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 44 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ycl.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ycl` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 3 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-ycl_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Lolopo (lolo1259)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/lolo1259)
2. <a id="src-ycl_wikipedia"></a>Wikipedia contributors (2024). *Lolopo language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Lolopo_language)
3. <a id="src-ycl_merrifield_j2010"></a>Merrifield, Judith Thomas (2010). *Yao'an Lolo Grammar Sketch*. MA thesis, Graduate Institute of Applied Linguistics.
4. <a id="src-ycl_merrifield2012"></a>Merrifield, W. Scott (2012). *Yáo'ān Central Yi Phonology*. SIL International (SIL Electronic Working Papers 2012-002). [sil.org](https://www.sil.org/resources/publications/entry/48227)
5. <a id="src-ycl_bradley2001"></a>Bradley, David (2001). *Language policy for the Yi*. In: Harrell, S. (ed.), Perspectives on the Yi of Southwest China, University of California Press, pp. 195-213.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ycl` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 111 | 0.0108 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 127 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bʲ bʷ p pʰ pʰʲ pʰʷ pʲ pʷ |  | d dʲ dʷ t tʰ tʰʲ tʰʷ tʲ tʷ |  |  | k kʰ kʰʲ kʰʷ kʲ kʷ ɡ ɡʲ ɡʷ | ʔ ʔʲ ʔʲʷ ʔʷ ʔʷʲ |
| Affricate |  |  | dz ts tsʰ | dʒ tʃ tʃʰ |  |  |  |
| Nasal | m mʲ mʷ |  | n nʲ nʷ |  |  | ŋ ŋʲ ŋʷ |  |
| Fricative |  | f fʲ fʷ v vʲ vʷ | s sʰʲ sʰʷ sʲ sʷ z zʲ zʷ z̩ z̩ʷ | ʃ ʃʰʲ ʃʰʷ ʃʲ ʃʷ ʒʲ ʒʷ | ʝ ʝʲ ʝʷ | x xʲ xʷ ɣ ɣʲ ɣʷ | h hʲ hʷ |
| Lateral fricative |  |  | ɮ ɮʲ ɮʷ |  |  |  |  |
| Lateral approximant |  |  | l lʲ lʷ |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i i̠ |  | ɯ ɯ̠ |
| Close-mid | e e̠ |  | o o̠ ɤ ɤ̠ |
| Mid |  | ə ə̠ |  |
| Open-mid | ɛ ɛ̠ |  |  |
| Near-open | æ æ̠ |  |  |
| Open | a a̠ |  |  |

Sequences that the spec writes as one unit: [a˧˧] [e˧˧] [i˧˧] [o˧˧] [w] [w̠] [z̩ʷ˧˧] [z̩˧˧] [æ˧˧] [ə˧˧] [ɛ˧˧] [ɤ˧˧] [ɯ˧˧] [ʔ˨˩] [ʔ˨˩ʲ] [ʔ˨˩ʷ] [˥˥] [˦˦] [˦˦ɮ] [˦˦˨˩] [˨˩].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a˧˧] | word initial [ʔa˧˧] |
| ⟨ae⟩ | [æ˧˧] | word initial [ʔæ˧˧] |
| ⟨b⟩ | [p] |  |
| ⟨bb⟩ | [b] |  |
| ⟨c⟩ | [tsʰ] |  |
| ⟨d⟩ | [t] |  |
| ⟨dd⟩ | [d] |  |
| ⟨e⟩ | [ɯ˧˧] | word initial [ʔɯ˧˧] |
| ⟨ei⟩ | [e˧˧] | word initial [ʔe˧˧] |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [k] |  |
| ⟨gg⟩ | [ɡ] |  |
| ⟨h⟩ | [x] [h] |  |
| ⟨hh⟩ | [ɣ] |  |
| ⟨i⟩ | [i˧˧] | word initial [ʔi˧˧] |
| ⟨ia⟩ | [ʲa˧˧] | word initial [ʔʲa˧˧] |
| ⟨iae⟩ | [ʲæ˧˧] | word initial [ʔʲæ˧˧] |
| ⟨ie⟩ | [ʲɛ˧˧] | word initial [ʔʲɛ˧˧] |
| ⟨io⟩ | [ʲo˧˧] | word initial [ʔʲo˧˧] |
| ⟨iu⟩ | [ʲo˧˧] | word initial [ʔʲo˧˧] |
| ⟨j⟩ | [tʃ] |  |
| ⟨jj⟩ | [dʒ] |  |
| ⟨k⟩ | [kʰ] |  |
| ⟨l⟩ | [ɮ] [l] | before vowel [ɮ] [l] · default [˥˥] |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨o⟩ | [o˧˧] | word initial [ʔo˧˧] |
| ⟨p⟩ | [pʰ] |  |
| ⟨q⟩ | [tʃʰ] |  |
| ⟨r⟩ | [˨˩] |  |
| ⟨s⟩ | [s] |  |
| ⟨ss⟩ | [z] |  |
| ⟨t⟩ | [tʰ] |  |
| ⟨u⟩ | [ɤ˧˧] | word initial [ʔɤ˧˧] |
| ⟨ua⟩ | [ʷa˧˧] | word initial [ʔʷa˧˧] |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ʃ] | before vowel [ʃ] · default [̠˦˦] |
| ⟨xl⟩ | [̠˥˥] | before vowel [̠˦˦ɮ] · default [̠˥˥] |
| ⟨xr⟩ | [̠ʔ˨˩] | before vowel [̠˦˦˨˩] · default [̠ʔ˨˩] |
| ⟨y⟩ | [ʝ] |  |
| ⟨z⟩ | [ts] |  |
| ⟨zz⟩ | [dz] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 36 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `YCL_MID_UNSPELLED_C_a` | /a˧˧/ → [a], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_MID_UNSPELLED_C_e` | /e˧˧/ → [e], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_APICAL_TONED_C_i` | /i˧˧/ → [z̩], after [s] [z] [ts] [dz] [tsʰ], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_APICAL_C_i` | /i˧˧/ → [z̩˧˧], after [s] [z] [ts] [dz] [tsʰ] | - | - |
| `YCL_MID_UNSPELLED_C_i` | /i˧˧/ → [i], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_MID_UNSPELLED_C_o` | /o˧˧/ → [o], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_MID_UNSPELLED_C_æ` | /æ˧˧/ → [æ], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_APICAL_TONED_C_ɤ` | /ɤ˧˧/ → [z̩ʷ], after [s] [z] [ts] [dz] [tsʰ], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_APICAL_C_ɤ` | /ɤ˧˧/ → [z̩ʷ˧˧], after [s] [z] [ts] [dz] [tsʰ] | - | - |
| `YCL_MID_UNSPELLED_C_ɤ` | /ɤ˧˧/ → [ɤ], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_APICAL_TONED_C_ɯ` | /ɯ˧˧/ → [ə], after [s] [z] [ts] [dz] [tsʰ] [tʃ] [dʒ] [tʃʰ] and 3 more, before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_APICAL_C_ɯ` | /ɯ˧˧/ → [ə˧˧], after [s] [z] [ts] [dz] [tsʰ] [tʃ] [dʒ] [tʃʰ] and 3 more | - | - |
| `YCL_MID_UNSPELLED_C_ɯ` | /ɯ˧˧/ → [ɯ], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_MID_UNSPELLED_C_ʲa` | /ʲa˧˧/ → [ʲa], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_MID_UNSPELLED_C_ʲo` | /ʲo˧˧/ → [ʲo], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_MID_UNSPELLED_C_ʲæ` | /ʲæ˧˧/ → [ʲæ], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_MID_UNSPELLED_C_ʲɛ` | /ʲɛ˧˧/ → [ʲɛ], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_MID_UNSPELLED_C_ʷa` | /ʷa˧˧/ → [ʷa], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_MID_UNSPELLED_ʔ_a` | /ʔa˧˧/ → [ʔa], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_MID_UNSPELLED_ʔ_e` | /ʔe˧˧/ → [ʔe], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_APICAL_TONED_ʔ_i` | /ʔi˧˧/ → [ʔz̩], after [s] [z] [ts] [dz] [tsʰ], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_APICAL_ʔ_i` | /ʔi˧˧/ → [ʔz̩˧˧], after [s] [z] [ts] [dz] [tsʰ] | - | - |
| `YCL_MID_UNSPELLED_ʔ_i` | /ʔi˧˧/ → [ʔi], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_MID_UNSPELLED_ʔ_o` | /ʔo˧˧/ → [ʔo], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_MID_UNSPELLED_ʔ_æ` | /ʔæ˧˧/ → [ʔæ], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_APICAL_TONED_ʔ_ɤ` | /ʔɤ˧˧/ → [ʔz̩ʷ], after [s] [z] [ts] [dz] [tsʰ], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_APICAL_ʔ_ɤ` | /ʔɤ˧˧/ → [ʔz̩ʷ˧˧], after [s] [z] [ts] [dz] [tsʰ] | - | - |
| `YCL_MID_UNSPELLED_ʔ_ɤ` | /ʔɤ˧˧/ → [ʔɤ], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_APICAL_TONED_ʔ_ɯ` | /ʔɯ˧˧/ → [ʔə], after [s] [z] [ts] [dz] [tsʰ] [tʃ] [dʒ] [tʃʰ] and 3 more, before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_APICAL_ʔ_ɯ` | /ʔɯ˧˧/ → [ʔə˧˧], after [s] [z] [ts] [dz] [tsʰ] [tʃ] [dʒ] [tʃʰ] and 3 more | - | - |
| `YCL_MID_UNSPELLED_ʔ_ɯ` | /ʔɯ˧˧/ → [ʔɯ], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_MID_UNSPELLED_ʔ_ʲa` | /ʔʲa˧˧/ → [ʔʲa], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_MID_UNSPELLED_ʔ_ʲo` | /ʔʲo˧˧/ → [ʔʲo], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_MID_UNSPELLED_ʔ_ʲæ` | /ʔʲæ˧˧/ → [ʔʲæ], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_MID_UNSPELLED_ʔ_ʲɛ` | /ʔʲɛ˧˧/ → [ʔʲɛ], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
| `YCL_MID_UNSPELLED_ʔ_ʷa` | /ʔʷa˧˧/ → [ʔʷa], before [˨˩] [̠ʔ˨˩] [̠˦˦] [̠˦˦ɮ] [̠˥˥] [˥˥] | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ycl")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Lojban](jbo.md) · [Home](../index.md) · [Lombard →](lmo.md)
