# Kashmiri (`kas`)

<!-- atlas:summary begin -->
Kashmiri is an Indo-Aryan language, written in the Arabic script. Glottolog places it in India and Pakistan. The `kas` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kas` |
| ISO 639-3 | [kas](https://iso639-3.sil.org/code/kas), Kashmiri |
| Glottolog | [kash1277](https://glottolog.org/resource/languoid/id/kash1277), Kashmiri |
| Wikidata | [Q33552](https://www.wikidata.org/wiki/Q33552) |
| Wikipedia | [Kashmiri language](https://en.wikipedia.org/wiki/Kashmiri_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Indo-Iranian > Indo-Aryan](by-family.md#indo-european--indo-iranian--indo-aryan) |
| Region | [Eurasia](by-region.md#eurasia) > [India](by-region.md#india), [Pakistan](by-region.md#pakistan) |
| Script | [Arabic](by-script.md#arabic) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Indo-Aryan](https://tigregotico.github.io/orthography2ipa/#x-clade-indo1321) `x-clade-indo1321` |
| Explorer | [`kas` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kas) |
| Spec file | [`kas.json`](../../orthography2ipa/data/kas.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Kashmiri (کٲشُر, कॉशुर), a Dardic (Northwestern Indo-Aryan) language, ~7 million speakers, official/scheduled language of Jammu & Kashmir (India) and taught/published in Pakistan-administered Azad Kashmir, the Eighth Schedule (Indian Constitution) scheduled language.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1997 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 58 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/kas.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `kas` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-wali_koul1997"></a>Wali, Kashi & Koul, Omkar N. (1997). *Kashmiri: A Cognitive-Descriptive Grammar*. Routledge.
2. <a id="src-kashmiri_alphabet_wiki"></a>Wikipedia contributors (2026). *Kashmiri alphabet*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Kashmiri_alphabet)
3. <a id="src-phoible"></a>Moran, Steven & McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `kas` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 683 | 0.2848 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 47 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  | ɖ ʈ ʈʰ |  | k kʰ ɡ | q | ʔ |
| Affricate |  |  |  | dʒ tʃ tʃʰ |  |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |  |  |
| Trill |  |  | r |  |  |  |  |  |  |
| Tap |  |  |  |  | ɽ |  |  |  |  |
| Fricative |  | f | s z | ʃ ʒ |  |  | x ɣ |  | h |
| Approximant |  |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː | ɨ ɨː | u uː |
| Close-mid | eː |  | oː |
| Mid |  | ə əː |  |
| Open-mid |  |  | ɔ |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [w] [ʲ] [̃].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ؠ⟩ | [ʲ] |  |
| ⟨آ⟩ | [aː] |  |
| ⟨أ⟩ | [ə] |  |
| ⟨ا⟩ | [aː] |  |
| ⟨او⟩ | [aː] [w] | default [aː] [w] · word initial [oː] |
| ⟨ب⟩ | [b] |  |
| ⟨ت⟩ | [t] |  |
| ⟨تھ⟩ | [tʰ] |  |
| ⟨ث⟩ | [s] |  |
| ⟨ج⟩ | [dʒ] |  |
| ⟨ح⟩ | [h] |  |
| ⟨خ⟩ | [x] |  |
| ⟨د⟩ | [d] |  |
| ⟨ذ⟩ | [z] |  |
| ⟨ر⟩ | [r] |  |
| ⟨ز⟩ | [z] |  |
| ⟨س⟩ | [s] |  |
| ⟨ش⟩ | [ʃ] |  |
| ⟨ص⟩ | [s] |  |
| ⟨ض⟩ | [z] |  |
| ⟨ط⟩ | [t] |  |
| ⟨ظ⟩ | [z] |  |
| ⟨ع⟩ | [ʔ] ∅ |  |
| ⟨غ⟩ | [ɣ] |  |
| ⟨ف⟩ | [f] |  |
| ⟨ق⟩ | [q] [k] |  |
| ⟨ل⟩ | [l] |  |
| ⟨م⟩ | [m] |  |
| ⟨ن⟩ | [n] |  |
| ⟨و⟩ | [w] [uː] |  |
| ⟨َ⟩ | [a] |  |
| ⟨ُ⟩ | [u] |  |
| ⟨ِ⟩ | [i] |  |
| ⟨ٔ⟩ | [ə] |  |
| ⟨ٕ⟩ | [ɨ] |  |
| ⟨ٗ⟩ | [uː] |  |
| ⟨ٚ⟩ | [ɨː] |  |
| ⟨ٛ⟩ | [ɨ] |  |
| ⟨ٟ⟩ | [ɨː] |  |
| ⟨ٲ⟩ | [əː] |  |
| ⟨ٹ⟩ | [ʈ] |  |
| ⟨ٹھ⟩ | [ʈʰ] |  |
| ⟨پ⟩ | [p] |  |
| ⟨پھ⟩ | [pʰ] |  |
| ⟨چ⟩ | [tʃ] |  |
| ⟨چھ⟩ | [tʃʰ] |  |
| ⟨ڈ⟩ | [ɖ] |  |
| ⟨ڑ⟩ | [ɽ] |  |
| ⟨ژ⟩ | [ʒ] |  |
| ⟨ک⟩ | [k] |  |
| ⟨کھ⟩ | [kʰ] |  |
| ⟨گ⟩ | [ɡ] |  |
| ⟨ں⟩ | [̃] |  |
| ⟨ہ⟩ | [h] [aː] |  |
| ⟨ۄ⟩ | [ɔ] |  |
| ⟨ۆ⟩ | [oː] |  |
| ⟨ی⟩ | [j] [iː] |  |
| ⟨ے⟩ | [eː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kas")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Karelian](krl.md) · [Home](../index.md) · [Kashmiri →](ks.md)
