# Khmer (`km`)

<!-- atlas:summary begin -->
Khmer is an Austroasiatic language, written in the Khmer script. Glottolog places it in Cambodia, Laos, Thailand and Vietnam. The `km` spec is at the research tier. It cites 4 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `km` |
| ISO 639-3 | [khm](https://iso639-3.sil.org/code/khm), Khmer |
| Glottolog | [cent1989](https://glottolog.org/resource/languoid/id/cent1989), Central Khmer |
| Wikidata | [Q9205](https://www.wikidata.org/wiki/Q9205) |
| Wikipedia | [Khmer language](https://en.wikipedia.org/wiki/Khmer_language) |
| Family | [Austroasiatic](by-family.md#austroasiatic) |
| Region | [Eurasia](by-region.md#eurasia) > [Cambodia](by-region.md#cambodia), [Laos](by-region.md#laos), [Thailand](by-region.md#thailand), [Vietnam](by-region.md#vietnam) |
| Script | [Khmer](by-script.md#khmer) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 611, living |
| Ancestor | [Proto-Mon-Khmer (reconstructed)](https://tigregotico.github.io/orthography2ipa/#kha-x-proto-mon-khmer) `kha-x-proto-mon-khmer` |
| Explorer | [`km` in the data explorer](https://tigregotico.github.io/orthography2ipa/#km) |
| Spec file | [`km.json`](../../orthography2ipa/data/km.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Khmer (Cambodian), written in the Khmer abugida. The spec is organised around the two-series register system: every consonant letter carries an inherent vowel, â [ɑː] for the a-series and ô [ɔː] for the o-series, and that same series decides which of its two readings each dependent vowel sign takes.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1968 to 2026. 2 of them are Wikipedia articles. [Sources](#sources) lists them. The spec file writes all 374 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/km.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `km` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-huffman1970"></a>Huffman, Franklin E. (1970). *Cambodian System of Writing and Beginning Reader*. Yale University Press.
2. <a id="src-jacob1968"></a>Jacob, Judith M. (1968). *Introduction to Cambodian*. Oxford University Press.
3. <a id="src-khmer_script_wiki"></a>Wikipedia contributors (2026). *Khmer script*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Khmer_script)
4. <a id="src-khmer_wiki"></a>Wikipedia contributors (2026). *Khmer language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Khmer_language)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `km` | gold | lexicon-derived | MIT, each file its own | 3261 | 0.3335 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `km` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 6628 | 0.1922 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 202 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ |  | t tʰ |  | c cʰ | k kʰ ɡ | ʔ |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f | s | ʒ |  |  | h |
| Approximant |  | ʋ |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | iː | ɨ ɨː | u uː |
| Close-mid | eː |  | o oː |
| Mid |  | ə əː |  |
| Open-mid | ɛː |  | ɔː |
| Open | a aː |  | ɑ ɑː |

Sequences that the spec writes as one unit: [ae] [ah] [aj] [am] [ao] [aə] [aɨ] [aʔ] [cj] [cl] [cm] [cn] [cr] [cŋ] [cɲ] [cʋ] [cʰj] [cʰl] [cʰm] [cʰn] [cʰr] [cʰŋ] [cʰɲ] [cʰʋ] [eh] [ej] [eə] [eʔ] [hj] [hl] [hm] [hn] [hr] [hŋ] [hɲ] [hʋ] [ih] [iə] [iʔ] [kj], and 124 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ក⟩ | [k] |  |
| ⟨ក់⟩ | [k] |  |
| ⟨ក៌⟩ | ∅ |  |
| ⟨ក៍⟩ | ∅ |  |
| ⟨ក្ង⟩ | [kŋ] |  |
| ⟨ក្ញ⟩ | [kɲ] |  |
| ⟨ក្ន⟩ | [kn] |  |
| ⟨ក្ម⟩ | [km] |  |
| ⟨ក្យ⟩ | [kj] |  |
| ⟨ក្រ⟩ | [kr] |  |
| ⟨ក្ល⟩ | [kl] |  |
| ⟨ក្វ⟩ | [kʋ] |  |
| ⟨ខ⟩ | [kʰ] |  |
| ⟨ខ់⟩ | [kʰ] |  |
| ⟨ខ៌⟩ | ∅ |  |
| ⟨ខ៍⟩ | ∅ |  |
| ⟨ខ្ង⟩ | [kʰŋ] |  |
| ⟨ខ្ញ⟩ | [kʰɲ] |  |
| ⟨ខ្ន⟩ | [kʰn] |  |
| ⟨ខ្ម⟩ | [kʰm] |  |
| ⟨ខ្យ⟩ | [kʰj] |  |
| ⟨ខ្រ⟩ | [kʰr] |  |
| ⟨ខ្ល⟩ | [kʰl] |  |
| ⟨ខ្វ⟩ | [kʰʋ] |  |
| ⟨គ⟩ | [k] |  |
| ⟨គ់⟩ | [k] |  |
| ⟨គ៌⟩ | ∅ |  |
| ⟨គ៍⟩ | ∅ |  |
| ⟨គ្ណ⟩ | [kn] |  |
| ⟨គ្ឡ⟩ | [kl] |  |
| ⟨ឃ⟩ | [kʰ] |  |
| ⟨ឃ់⟩ | [kʰ] |  |
| ⟨ឃ៌⟩ | ∅ |  |
| ⟨ឃ៍⟩ | ∅ |  |
| ⟨ឃ្ណ⟩ | [kʰn] |  |
| ⟨ឃ្ឡ⟩ | [kʰl] |  |
| ⟨ង⟩ | [ŋ] |  |
| ⟨ង៉⟩ | [ŋ] |  |
| ⟨ង៉់⟩ | [ŋ] |  |
| ⟨ង់⟩ | [ŋ] |  |
| ⟨ង៌⟩ | ∅ |  |
| ⟨ង៍⟩ | ∅ |  |
| ⟨ច⟩ | [c] |  |
| ⟨ច់⟩ | [c] |  |
| ⟨ច៌⟩ | ∅ |  |
| ⟨ច៍⟩ | ∅ |  |
| ⟨ច្ង⟩ | [cŋ] |  |
| ⟨ច្ញ⟩ | [cɲ] |  |
| ⟨ច្ន⟩ | [cn] |  |
| ⟨ច្ម⟩ | [cm] |  |
| ⟨ច្យ⟩ | [cj] |  |
| ⟨ច្រ⟩ | [cr] |  |
| ⟨ច្ល⟩ | [cl] |  |
| ⟨ច្វ⟩ | [cʋ] |  |
| ⟨ឆ⟩ | [cʰ] |  |
| ⟨ឆ់⟩ | [cʰ] |  |
| ⟨ឆ៌⟩ | ∅ |  |
| ⟨ឆ៍⟩ | ∅ |  |
| ⟨ឆ្ង⟩ | [cʰŋ] |  |
| ⟨ឆ្ញ⟩ | [cʰɲ] |  |
| ⟨ឆ្ន⟩ | [cʰn] |  |
| ⟨ឆ្ម⟩ | [cʰm] |  |
| ⟨ឆ្យ⟩ | [cʰj] |  |
| ⟨ឆ្រ⟩ | [cʰr] |  |
| ⟨ឆ្ល⟩ | [cʰl] |  |
| ⟨ឆ្វ⟩ | [cʰʋ] |  |
| ⟨ជ⟩ | [c] |  |
| ⟨ជ់⟩ | [c] |  |
| ⟨ជ៌⟩ | ∅ |  |
| ⟨ជ៍⟩ | ∅ |  |
| ⟨ជ្ណ⟩ | [cn] |  |
| ⟨ជ្ឡ⟩ | [cl] |  |
| ⟨ឈ⟩ | [cʰ] |  |
| ⟨ឈ់⟩ | [cʰ] |  |
| ⟨ឈ៌⟩ | ∅ |  |
| ⟨ឈ៍⟩ | ∅ |  |
| ⟨ឈ្ណ⟩ | [cʰn] |  |
| ⟨ឈ្ឡ⟩ | [cʰl] |  |
| ⟨ញ⟩ | [ɲ] |  |
| ⟨ញ៉⟩ | [ɲ] |  |
| ⟨ញ៉់⟩ | [ɲ] |  |
| ⟨ញ់⟩ | [ɲ] |  |
| ⟨ញ៌⟩ | ∅ |  |
| ⟨ញ៍⟩ | ∅ |  |
| ⟨ដ⟩ | [ɗ] |  |
| ⟨ដ់⟩ | [ɗ] |  |
| ⟨ដ៌⟩ | ∅ |  |
| ⟨ដ៍⟩ | ∅ |  |
| ⟨ដ្ង⟩ | [ɗŋ] |  |
| ⟨ដ្ញ⟩ | [ɗɲ] |  |
| ⟨ដ្ន⟩ | [ɗn] |  |
| ⟨ដ្ម⟩ | [ɗm] |  |
| ⟨ដ្យ⟩ | [ɗj] |  |
| ⟨ដ្រ⟩ | [ɗr] |  |
| ⟨ដ្ល⟩ | [ɗl] |  |
| ⟨ដ្វ⟩ | [ɗʋ] |  |
| ⟨ឋ⟩ | [tʰ] |  |
| ⟨ឋ់⟩ | [tʰ] |  |
| ⟨ឋ៌⟩ | ∅ |  |
| ⟨ឋ៍⟩ | ∅ |  |
| ⟨ឋ្ង⟩ | [tʰŋ] |  |
| ⟨ឋ្ញ⟩ | [tʰɲ] |  |
| ⟨ឋ្ន⟩ | [tʰn] |  |
| ⟨ឋ្ម⟩ | [tʰm] |  |
| ⟨ឋ្យ⟩ | [tʰj] |  |
| ⟨ឋ្រ⟩ | [tʰr] |  |
| ⟨ឋ្ល⟩ | [tʰl] |  |
| ⟨ឋ្វ⟩ | [tʰʋ] |  |
| ⟨ឌ⟩ | [ɗ] |  |
| ⟨ឌ់⟩ | [ɗ] |  |
| ⟨ឌ៌⟩ | ∅ |  |
| ⟨ឌ៍⟩ | ∅ |  |
| ⟨ឌ្ណ⟩ | [ɗn] |  |
| ⟨ឌ្ឡ⟩ | [ɗl] |  |
| ⟨ឍ⟩ | [tʰ] |  |
| ⟨ឍ់⟩ | [tʰ] |  |
| ⟨ឍ៌⟩ | ∅ |  |
| ⟨ឍ៍⟩ | ∅ |  |
| ⟨ឍ្ណ⟩ | [tʰn] |  |
| ⟨ឍ្ឡ⟩ | [tʰl] |  |
| ⟨ណ⟩ | [n] |  |
| ⟨ណ់⟩ | [n] |  |
| ⟨ណ៌⟩ | ∅ |  |
| ⟨ណ៍⟩ | ∅ |  |
| ⟨ត⟩ | [t] |  |
| ⟨ត់⟩ | [t] |  |
| ⟨ត៌⟩ | ∅ |  |
| ⟨ត៍⟩ | ∅ |  |
| ⟨ត្ង⟩ | [tŋ] |  |
| ⟨ត្ញ⟩ | [tɲ] |  |
| ⟨ត្ន⟩ | [tn] |  |
| ⟨ត្ម⟩ | [tm] |  |
| ⟨ត្យ⟩ | [tj] |  |
| ⟨ត្រ⟩ | [tr] |  |
| ⟨ត្ល⟩ | [tl] |  |
| ⟨ត្វ⟩ | [tʋ] |  |
| ⟨ថ⟩ | [tʰ] |  |
| ⟨ថ់⟩ | [tʰ] |  |
| ⟨ថ៌⟩ | ∅ |  |
| ⟨ថ៍⟩ | ∅ |  |
| ⟨ថ្ង⟩ | [tʰŋ] |  |
| ⟨ថ្ញ⟩ | [tʰɲ] |  |
| ⟨ថ្ន⟩ | [tʰn] |  |
| ⟨ថ្ម⟩ | [tʰm] |  |
| ⟨ថ្យ⟩ | [tʰj] |  |
| ⟨ថ្រ⟩ | [tʰr] |  |
| ⟨ថ្ល⟩ | [tʰl] |  |
| ⟨ថ្វ⟩ | [tʰʋ] |  |
| ⟨ទ⟩ | [t] |  |
| ⟨ទ់⟩ | [t] |  |
| ⟨ទ៌⟩ | ∅ |  |
| ⟨ទ៍⟩ | ∅ |  |
| ⟨ទ្ណ⟩ | [tn] |  |
| ⟨ទ្ឡ⟩ | [tl] |  |
| ⟨ធ⟩ | [tʰ] |  |
| ⟨ធ់⟩ | [tʰ] |  |
| ⟨ធ៌⟩ | ∅ |  |
| ⟨ធ៍⟩ | ∅ |  |
| ⟨ធ្ណ⟩ | [tʰn] |  |
| ⟨ធ្ឡ⟩ | [tʰl] |  |
| ⟨ន⟩ | [n] |  |
| ⟨ន៉⟩ | [n] |  |
| ⟨ន៉់⟩ | [n] |  |
| ⟨ន់⟩ | [n] |  |
| ⟨ន៌⟩ | ∅ |  |
| ⟨ន៍⟩ | ∅ |  |
| ⟨ប⟩ | [ɓ] |  |
| ⟨ប៉⟩ | [p] |  |
| ⟨ប៉់⟩ | [p] |  |
| ⟨ប៊⟩ | [ɓ] |  |
| ⟨ប៊់⟩ | [ɓ] |  |
| ⟨ប់⟩ | [ɓ] |  |
| ⟨ប៌⟩ | ∅ |  |
| ⟨ប៍⟩ | ∅ |  |
| ⟨ប្ក⟩ | [pk] |  |
| ⟨ប្ខ⟩ | [pkʰ] |  |
| ⟨ប្គ⟩ | [pk] |  |
| ⟨ប្ឃ⟩ | [pkʰ] |  |
| ⟨ប្ង⟩ | [pŋ] |  |
| ⟨ប្ច⟩ | [pc] |  |
| ⟨ប្ឆ⟩ | [pcʰ] |  |
| ⟨ប្ជ⟩ | [pc] |  |
| ⟨ប្ឈ⟩ | [pcʰ] |  |
| ⟨ប្ញ⟩ | [pɲ] |  |
| ⟨ប្ដ⟩ | [pɗ] |  |
| ⟨ប្ឋ⟩ | [ptʰ] |  |
| ⟨ប្ឌ⟩ | [pɗ] |  |
| ⟨ប្ឍ⟩ | [ptʰ] |  |
| ⟨ប្ត⟩ | [pt] |  |
| ⟨ប្ថ⟩ | [ptʰ] |  |
| ⟨ប្ទ⟩ | [pt] |  |
| ⟨ប្ធ⟩ | [ptʰ] |  |
| ⟨ប្ន⟩ | [pn] |  |
| ⟨ប្ប⟩ | [pɓ] |  |
| ⟨ប្ផ⟩ | [ppʰ] |  |
| ⟨ប្ព⟩ | [pp] |  |
| ⟨ប្ភ⟩ | [ppʰ] |  |
| ⟨ប្ម⟩ | [pm] |  |
| ⟨ប្យ⟩ | [pj] |  |
| ⟨ប្រ⟩ | [pr] |  |
| ⟨ប្ល⟩ | [pl] |  |
| ⟨ប្វ⟩ | [pʋ] |  |
| ⟨ប្ស⟩ | [ps] |  |
| ⟨ប្ហ⟩ | [ph] |  |
| ⟨ប្អ⟩ | [pʔ] |  |
| ⟨ផ⟩ | [pʰ] |  |
| ⟨ផ់⟩ | [pʰ] |  |
| ⟨ផ៌⟩ | ∅ |  |
| ⟨ផ៍⟩ | ∅ |  |
| ⟨ផ្ង⟩ | [pʰŋ] |  |
| ⟨ផ្ញ⟩ | [pʰɲ] |  |
| ⟨ផ្ន⟩ | [pʰn] |  |
| ⟨ផ្ម⟩ | [pʰm] |  |
| ⟨ផ្យ⟩ | [pʰj] |  |
| ⟨ផ្រ⟩ | [pʰr] |  |
| ⟨ផ្ល⟩ | [pʰl] |  |
| ⟨ផ្វ⟩ | [pʰʋ] |  |
| ⟨ព⟩ | [p] |  |
| ⟨ព់⟩ | [p] |  |
| ⟨ព៌⟩ | ∅ |  |
| ⟨ព៍⟩ | ∅ |  |
| ⟨ព្ណ⟩ | [pn] |  |
| ⟨ព្ឡ⟩ | [pl] |  |
| ⟨ភ⟩ | [pʰ] |  |
| ⟨ភ់⟩ | [pʰ] |  |
| ⟨ភ៌⟩ | ∅ |  |
| ⟨ភ៍⟩ | ∅ |  |
| ⟨ភ្ណ⟩ | [pʰn] |  |
| ⟨ភ្ឡ⟩ | [pʰl] |  |
| ⟨ម⟩ | [m] |  |
| ⟨ម៉⟩ | [m] |  |
| ⟨ម៉់⟩ | [m] |  |
| ⟨ម់⟩ | [m] |  |
| ⟨ម៌⟩ | ∅ |  |
| ⟨ម៍⟩ | ∅ |  |
| ⟨យ⟩ | [j] |  |
| ⟨យ៉⟩ | [j] |  |
| ⟨យ៉់⟩ | [j] |  |
| ⟨យ់⟩ | [j] |  |
| ⟨យ៌⟩ | ∅ |  |
| ⟨យ៍⟩ | ∅ |  |
| ⟨រ⟩ | [r] |  |
| ⟨រ៉⟩ | [r] |  |
| ⟨រ៉់⟩ | [r] |  |
| ⟨រ់⟩ | [r] |  |
| ⟨រ៌⟩ | ∅ |  |
| ⟨រ៍⟩ | ∅ |  |
| ⟨ល⟩ | [l] |  |
| ⟨ល៉⟩ | [l] |  |
| ⟨ល៉់⟩ | [l] |  |
| ⟨ល់⟩ | [l] |  |
| ⟨ល៌⟩ | ∅ |  |
| ⟨ល៍⟩ | ∅ |  |
| ⟨វ⟩ | [ʋ] |  |
| ⟨វ៉⟩ | [ʋ] |  |
| ⟨វ៉់⟩ | [ʋ] |  |
| ⟨វ់⟩ | [ʋ] |  |
| ⟨វ៌⟩ | ∅ |  |
| ⟨វ៍⟩ | ∅ |  |
| ⟨ស⟩ | [s] |  |
| ⟨ស៊⟩ | [s] |  |
| ⟨ស៊់⟩ | [s] |  |
| ⟨ស់⟩ | [s] |  |
| ⟨ស៌⟩ | ∅ |  |
| ⟨ស៍⟩ | ∅ |  |
| ⟨ស្ង⟩ | [sŋ] |  |
| ⟨ស្ញ⟩ | [sɲ] |  |
| ⟨ស្ន⟩ | [sn] |  |
| ⟨ស្ម⟩ | [sm] |  |
| ⟨ស្យ⟩ | [sj] |  |
| ⟨ស្រ⟩ | [sr] |  |
| ⟨ស្ល⟩ | [sl] |  |
| ⟨ស្វ⟩ | [sʋ] |  |
| ⟨ហ⟩ | [h] |  |
| ⟨ហ៊⟩ | [h] |  |
| ⟨ហ៊់⟩ | [h] |  |
| ⟨ហ់⟩ | [h] |  |
| ⟨ហ៌⟩ | ∅ |  |
| ⟨ហ៍⟩ | ∅ |  |
| ⟨ហ្គ⟩ | [ɡ] |  |
| ⟨ហ្គ៊⟩ | [ɡ] |  |
| ⟨ហ្ង⟩ | [hŋ] |  |
| ⟨ហ្ញ⟩ | [hɲ] |  |
| ⟨ហ្ន⟩ | [hn] |  |
| ⟨ហ្ម⟩ | [hm] |  |
| ⟨ហ្យ⟩ | [hj] |  |
| ⟨ហ្រ⟩ | [hr] |  |
| ⟨ហ្ល⟩ | [hl] |  |
| ⟨ហ្វ⟩ | [hʋ] |  |
| ⟨ហ្វ៊⟩ | [f] |  |
| ⟨ហ្ស⟩ | [ʒ] |  |
| ⟨ហ្ស៊⟩ | [ʒ] |  |
| ⟨ឡ⟩ | [l] |  |
| ⟨ឡ់⟩ | [l] |  |
| ⟨ឡ៌⟩ | ∅ |  |
| ⟨ឡ៍⟩ | ∅ |  |
| ⟨អ⟩ | [ʔ] |  |
| ⟨អ៊⟩ | [ʔ] |  |
| ⟨អ៊់⟩ | [ʔ] |  |
| ⟨អ់⟩ | [ʔ] |  |
| ⟨អ៌⟩ | ∅ |  |
| ⟨អ៍⟩ | ∅ |  |
| ⟨អ្ង⟩ | [ʔŋ] |  |
| ⟨អ្ញ⟩ | [ʔɲ] |  |
| ⟨អ្ន⟩ | [ʔn] |  |
| ⟨អ្ម⟩ | [ʔm] |  |
| ⟨អ្យ⟩ | [ʔj] |  |
| ⟨អ្រ⟩ | [ʔr] |  |
| ⟨អ្ល⟩ | [ʔl] |  |
| ⟨អ្វ⟩ | [ʔʋ] |  |
| ⟨ឥ⟩ | [ʔe] [ʔə] [ʔəj] |  |
| ⟨ឦ⟩ | [ʔej] |  |
| ⟨ឧ⟩ | [ʔu] [ʔo] |  |
| ⟨ឩ⟩ | [ʔuː] |  |
| ⟨ឪ⟩ | [ʔɨw] [ʔəw] |  |
| ⟨ឫ⟩ | [rɨ] |  |
| ⟨ឬ⟩ | [rɨː] |  |
| ⟨ឭ⟩ | [lɨ] |  |
| ⟨ឮ⟩ | [lɨː] |  |
| ⟨ឯ⟩ | [ʔae] [ʔɛː] [ʔeː] |  |
| ⟨ឰ⟩ | [ʔaj] |  |
| ⟨ឱ⟩ | [ʔao] |  |
| ⟨ឲ⟩ | [ʔao] |  |
| ⟨ឳ⟩ | [ʔaw] |  |
| ⟨ា⟩ | [aː] |  |
| ⟨ាំ⟩ | [am] |  |
| ⟨ិ⟩ | [ə] |  |
| ⟨ិះ⟩ | [eh] |  |
| ⟨ី⟩ | [əj] [ej] |  |
| ⟨ឹ⟩ | [ə] |  |
| ⟨ឹះ⟩ | [əh] |  |
| ⟨ឺ⟩ | [əː] |  |
| ⟨ុ⟩ | [o] |  |
| ⟨ុំ⟩ | [om] |  |
| ⟨ុះ⟩ | [oh] |  |
| ⟨ូ⟩ | [oː] [ou] |  |
| ⟨ួ⟩ | [uə] |  |
| ⟨ើ⟩ | [aə] |  |
| ⟨ើះ⟩ | [əh] |  |
| ⟨ឿ⟩ | [ɨə] |  |
| ⟨ៀ⟩ | [iə] |  |
| ⟨េ⟩ | [eː] |  |
| ⟨េះ⟩ | [eh] |  |
| ⟨ែ⟩ | [ae] |  |
| ⟨ែះ⟩ | [eh] |  |
| ⟨ៃ⟩ | [aj] [ej] |  |
| ⟨ោ⟩ | [ao] |  |
| ⟨ោះ⟩ | [ɑh] |  |
| ⟨ៅ⟩ | [aɨ] |  |
| ⟨ំ⟩ | [ɑm] |  |
| ⟨ះ⟩ | [ah] |  |
| ⟨ៈ⟩ | [aʔ] |  |
| ⟨៎⟩ | ∅ |  |
| ⟨៏⟩ | [ɑː] |  |
| ⟨័⟩ | [a] |  |
| ⟨៓⟩ | ∅ |  |
| ⟨។⟩ | ∅ |  |
| ⟨៕⟩ | ∅ |  |
| ⟨៖⟩ | ∅ |  |
| ⟨ៗ⟩ | ∅ |  |
| ⟨៘⟩ | ∅ |  |
| ⟨៙⟩ | ∅ |  |
| ⟨៚⟩ | ∅ |  |
| ⟨០⟩ | ∅ |  |
| ⟨១⟩ | ∅ |  |
| ⟨២⟩ | ∅ |  |
| ⟨៣⟩ | ∅ |  |
| ⟨៤⟩ | ∅ |  |
| ⟨៥⟩ | ∅ |  |
| ⟨៦⟩ | ∅ |  |
| ⟨៧⟩ | ∅ |  |
| ⟨៨⟩ | ∅ |  |
| ⟨៩⟩ | ∅ |  |
| ⟨​⟩ | ∅ |  |

Stress falls on the last syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 46 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `KM_INHERENT_O_SERIES` | /ɑː/ → [ɔː], after [c] [cʰ] [f] [h] [j] [k] [kʰ] [l] and 16 more, spelled ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17B6` | /aː/ → [iə], spelled ⟨ា⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | ⟨គា⟩ [kiə] | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17B7` | /ə/ → [ɨ], spelled ⟨ិ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17B8` | /əj/ → [iː], spelled ⟨ី⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17B9` | /ə/ → [ɨ], spelled ⟨ឹ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17BA` | /əː/ → [ɨː], spelled ⟨ឺ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17BB` | /o/ → [u], spelled ⟨ុ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17BC` | /oː/ → [uː], spelled ⟨ូ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17BE` | /aə/ → [əː], spelled ⟨ើ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17C2` | /ae/ → [ɛː], spelled ⟨ែ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17C3` | /aj/ → [əj], spelled ⟨ៃ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17C4` | /ao/ → [oː], spelled ⟨ោ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17C5` | /aɨ/ → [əɨ], spelled ⟨ៅ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17BB_17C6` | /om/ → [um], spelled ⟨ុំ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17C6` | /ɑm/ → [um], spelled ⟨ំ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17B6_17C6` | /am/ → [ŏəm], spelled ⟨ាំ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17C7` | /ah/ → [ĕəh], spelled ⟨ះ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17B7_17C7` | /eh/ → [ih], spelled ⟨ិះ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17BB_17C7` | /oh/ → [uh], spelled ⟨ុះ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17C1_17C7` | /eh/ → [ih], spelled ⟨េះ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17C4_17C7` | /ɑh/ → [ŭəh], spelled ⟨ោះ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17C8` | /aʔ/ → [ĕəʔ], spelled ⟨ៈ⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17D0` | /a/ → [ŏə], spelled ⟨័⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_VOWEL_O_17CF` | /ɑː/ → [ɔː], spelled ⟨៏⟩, after ⟨គ⟩ ⟨ឃ⟩ ⟨ង⟩ ⟨ជ⟩ ⟨ឈ⟩ ⟨ញ⟩ ⟨ឌ⟩ ⟨ឍ⟩ and 47 more | - | [Huffman 1970](#src-huffman1970), [Jacob 1968](#src-jacob1968) |
| `KM_BANTOC_O_LABIAL` | /ɔː/ → [u], after [c] [cʰ] [f] [h] [j] [k] [kʰ] [l] and 16 more, before ⟨ប់⟩ ⟨ព់⟩ ⟨ភ់⟩ ⟨ផ់⟩ ⟨ម់⟩ | - | [Huffman 1970](#src-huffman1970) |
| `KM_BANTOC_A` | /ɑː/ → [ɑ], after [c] [cʰ] [f] [h] [j] [k] [kʰ] [l] and 16 more, before ⟨ក់⟩ ⟨ខ់⟩ ⟨គ់⟩ ⟨ឃ់⟩ ⟨ង់⟩ ⟨ច់⟩ ⟨ឆ់⟩ ⟨ជ់⟩ and 38 more | - | [Huffman 1970](#src-huffman1970) |
| `KM_BANTOC_O` | /ɔː/ → [ŏə], after [c] [cʰ] [f] [h] [j] [k] [kʰ] [l] and 16 more, before ⟨ក់⟩ ⟨ខ់⟩ ⟨គ់⟩ ⟨ឃ់⟩ ⟨ង់⟩ ⟨ច់⟩ ⟨ឆ់⟩ ⟨ជ់⟩ and 38 more | - | [Huffman 1970](#src-huffman1970) |
| `KM_BANTOC_AA` | /aː/ → [a], spelled ⟨ា⟩, before ⟨ក់⟩ ⟨ខ់⟩ ⟨គ់⟩ ⟨ឃ់⟩ ⟨ង់⟩ ⟨ច់⟩ ⟨ឆ់⟩ ⟨ជ់⟩ and 38 more | - | [Huffman 1970](#src-huffman1970) |
| `KM_BANTOC_AA_O_VELAR` | /iə/ → [eə], spelled ⟨ា⟩, before ⟨ក់⟩ ⟨គ់⟩ ⟨ង់⟩ ⟨ហ់⟩ | - | [Huffman 1970](#src-huffman1970) |
| `KM_BANTOC_AA_O` | /iə/ → [ŏə], spelled ⟨ា⟩, before ⟨ក់⟩ ⟨ខ់⟩ ⟨គ់⟩ ⟨ឃ់⟩ ⟨ង់⟩ ⟨ច់⟩ ⟨ឆ់⟩ ⟨ជ់⟩ and 38 more | - | [Huffman 1970](#src-huffman1970) |
| `KM_PRESYLLABLE_A` | /ɑː/ → [ɑ], after [c] [cʰ] [f] [h] [j] [k] [kʰ] [l] and 16 more, with more context in the spec | - | [Huffman 1970](#src-huffman1970) |
| `KM_PRESYLLABLE_O` | /ɔː/ → [ŏə], after [c] [cʰ] [f] [h] [j] [k] [kʰ] [l] and 16 more, with more context in the spec | - | [Huffman 1970](#src-huffman1970) |
| `KM_OPEN_17B7_ə` | /ə/ → [eʔ], word-finally, spelled ⟨ិ⟩ | - | [Huffman 1970](#src-huffman1970) |
| `KM_OPEN_17B7_ɨ` | /ɨ/ → [iʔ], word-finally, spelled ⟨ិ⟩ | - | [Huffman 1970](#src-huffman1970) |
| `KM_OPEN_17BB_o` | /o/ → [oʔ], word-finally, spelled ⟨ុ⟩ | - | [Huffman 1970](#src-huffman1970) |
| `KM_OPEN_17BB_u` | /u/ → [uʔ], word-finally, spelled ⟨ុ⟩ | - | [Huffman 1970](#src-huffman1970) |
| `KM_FINAL_R_SILENT` | /r/ → ∅, word-finally, in the coda | - | [Huffman 1970](#src-huffman1970) |
| `KM_FINAL_S_H` | /s/ → [h], word-finally, in the coda | - | [Huffman 1970](#src-huffman1970) |
| `KM_FINAL_IMPLOSIVE_T` | /ɗ/ → [t], word-finally, in the coda | - | [Huffman 1970](#src-huffman1970) |
| `KM_FINAL_B_P` | /ɓ/ → [p], word-finally, in the coda | - | [Huffman 1970](#src-huffman1970) |
| `KM_FINAL_K_GLOTTAL` | /k/ → [ʔ], word-finally, in the coda, after [ɑː] [aː] [iə] [ɨə] [uə] [ɑ] [a] [ĕə] and 1 more | - | [Huffman 1970](#src-huffman1970) |
| `KM_FINAL_K_GLOTTAL_ASP` | /kʰ/ → [ʔ], word-finally, in the coda, after [ɑː] [aː] [iə] [ɨə] [uə] [ɑ] [a] [ĕə] and 1 more | - | [Huffman 1970](#src-huffman1970) |
| `KM_FINAL_DEASPIRATE_K` | /kʰ/ → [k], word-finally, in the coda | - | [Huffman 1970](#src-huffman1970) |
| `KM_FINAL_DEASPIRATE_C` | /cʰ/ → [c], word-finally, in the coda | - | [Huffman 1970](#src-huffman1970) |
| `KM_FINAL_DEASPIRATE_T` | /tʰ/ → [t], word-finally, in the coda | - | [Huffman 1970](#src-huffman1970) |
| `KM_FINAL_DEASPIRATE_P` | /pʰ/ → [p], word-finally, in the coda | - | [Huffman 1970](#src-huffman1970) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "km")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Khiamniungan Naga](kix.md) · [Home](../index.md) · [Khumi Chin →](cnk.md)
