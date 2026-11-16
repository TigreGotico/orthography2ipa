# Shan (`shn`)

<!-- atlas:summary begin -->
Shan is a Tai-Kadai language, written in the Shan (Burmese-derived) script. Glottolog places it in China, Myanmar (Burma) and Thailand. The `shn` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `shn` |
| ISO 639-3 | [shn](https://iso639-3.sil.org/code/shn), Shan |
| Glottolog | [shan1277](https://glottolog.org/resource/languoid/id/shan1277), Shan |
| Wikidata | [Q56482](https://www.wikidata.org/wiki/Q56482) |
| Wikipedia | [Shan language](https://en.wikipedia.org/wiki/Shan_language) |
| Family | [Tai-Kadai](by-family.md#tai-kadai) |
| Region | [Eurasia](by-region.md#eurasia) > [China](by-region.md#china), [Myanmar (Burma)](by-region.md#myanmar-burma), [Thailand](by-region.md#thailand) |
| Script | [Shan (Burmese-derived)](by-script.md#shan-burmese-derived) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Parent | [Tai-Kadai](https://tigregotico.github.io/orthography2ipa/#x-clade-taik1256) `x-clade-taik1256` |
| Explorer | [`shn` in the data explorer](https://tigregotico.github.io/orthography2ipa/#shn) |
| Spec file | [`shn.json`](../../orthography2ipa/data/shn.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Shan (တႆး, Tai Long), a Southwestern Tai (Tai-Kadai) language of Shan State, Myanmar, ~3-4 million speakers, the majority/regional language of Shan State.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 2019 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 36 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/shn.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `shn` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 4 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-shan_alphabet_wiki"></a>Wikipedia contributors (2026). *Shan alphabet*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Shan_alphabet)
2. <a id="src-shan_language_wiki"></a>Wikipedia contributors (2024). *Shan language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Shan_language)
3. <a id="src-phoible"></a>Moran, Steven & McCloy, Daniel (eds.) (2019). *PHOIBLE 2.0*. Max Planck Institute for the Science of Human History. [phoible.org](https://phoible.org/)
4. <a id="src-r12a_shn_script_notes"></a>Ishida, Richard (2024). *Shan Script Notes*. r12a (W3C Internationalization). [r12a.github.io](https://r12a.github.io/scripts/mymr/shn.html)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `shn` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2604 | 0.2985 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 36 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ |  |  | t tʰ |  |  | k kʰ | ʔ |
| Affricate |  |  |  |  | tʃ |  |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |
| Fricative |  | f | θ | s |  |  |  | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u ɯ ɯː |
| Close-mid | e | oː ɤ ɤː |
| Open-mid | ɛː |  |
| Open | a aː |  |

Sequences that the spec writes as one unit: [w] [˥] [˦˨ˀ] [˧˦˧] [˧˨] [˩].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨င⟩ | [ŋ] |  |
| ⟨တ⟩ | [t] |  |
| ⟨ထ⟩ | [tʰ] |  |
| ⟨ပ⟩ | [p] |  |
| ⟨မ⟩ | [m] |  |
| ⟨ယ⟩ | [j] |  |
| ⟨ရ⟩ | [j] [l] |  |
| ⟨လ⟩ | [l] |  |
| ⟨ဝ⟩ | [w] |  |
| ⟨သ⟩ | [s] |  |
| ⟨ဢ⟩ | [ʔ] |  |
| ⟨ိ⟩ | [i] |  |
| ⟨ို⟩ | [ɯ] |  |
| ⟨ိုဝ်⟩ | [ɯː] |  |
| ⟨ိူ⟩ | [ɤ] |  |
| ⟨ိူဝ်⟩ | [ɤː] |  |
| ⟨ီ⟩ | [iː] |  |
| ⟨ု⟩ | [u] |  |
| ⟨ူ⟩ | [oː] |  |
| ⟨ေ⟩ | [e] |  |
| ⟨း⟩ | [˥] |  |
| ⟨ၢ⟩ | [aː] |  |
| ⟨ၵ⟩ | [k] |  |
| ⟨ၶ⟩ | [kʰ] |  |
| ⟨ၸ⟩ | [tʃ] |  |
| ⟨ၺ⟩ | [ɲ] |  |
| ⟨ၼ⟩ | [n] |  |
| ⟨ၽ⟩ | [pʰ] |  |
| ⟨ၾ⟩ | [f] |  |
| ⟨ႀ⟩ | [θ] |  |
| ⟨ႁ⟩ | [h] |  |
| ⟨ႄ⟩ | [ɛː] |  |
| ⟨ႇ⟩ | [˩] |  |
| ⟨ႈ⟩ | [˧˨] |  |
| ⟨ႉ⟩ | [˦˨ˀ] |  |
| ⟨ႊ⟩ | [˧˦˧] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "shn")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Seychellois Creole](crs.md) · [Home](../index.md) · [Shawiya →](shy.md)
