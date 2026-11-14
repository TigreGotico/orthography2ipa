# Tibetan (`bo`)

<!-- atlas:summary begin -->
Tibetan is a Sino-Tibetan language, written in the Tibetan script. Glottolog places it in Bhutan, China, India and Nepal. The `bo` spec is at the research tier. It cites 9 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `bo` |
| ISO 639-3 | [bod](https://iso639-3.sil.org/code/bod), Tibetan |
| Glottolog | [tibe1272](https://glottolog.org/resource/languoid/id/tibe1272), Tibetan |
| Wikidata | [Q5128314](https://www.wikidata.org/wiki/Q5128314) |
| Wikipedia | [Tibetan language](https://en.wikipedia.org/wiki/Tibetan_language) |
| Family | [Sino-Tibetan](by-family.md#sino-tibetan) |
| Region | [Eurasia](by-region.md#eurasia) > [Bhutan](by-region.md#bhutan), [China](by-region.md#china), [India](by-region.md#india), [Nepal](by-region.md#nepal) |
| Script | [Tibetan](by-script.md#tibetan) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 600, living |
| Parent | [Proto-Sino-Tibetan (family node)](https://tigregotico.github.io/orthography2ipa/#sit) `sit` |
| Explorer | [`bo` in the data explorer](https://tigregotico.github.io/orthography2ipa/#bo) |
| Spec file | [`bo.json`](../../orthography2ipa/data/bo.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard (Lhasa) Tibetan. The spec resolves the Tibetan SYLLABLE, not the letter: spelling is historical, and a syllable is prefix + superscript + ROOT + subscript + vowel + suffix + post-suffix, of which only the root, the vowel and the register survive intact in the modern language.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 9 works, from 1976 to 2024. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 146 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/bo.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `bo` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 9 works. 7 of them have a DOI or a URL. The spec file holds a note on what 8 of them support.

1. <a id="src-thl_phonetics"></a>Germano, David & Tournadre, Nicolas (2003). *THL Simplified Phonetic Transcription of Standard Tibetan*. Tibetan and Himalayan Library, University of Virginia. [thlib.org](http://www.thlib.org/reference/transliteration/)
2. <a id="src-tournadre_dorje2003"></a>Tournadre, Nicolas & Sangda Dorje (2003). *Manual of Standard Tibetan: Language and Civilization*. Snow Lion.
3. <a id="src-delancey2003"></a>DeLancey, Scott (2003). *Lhasa Tibetan*. In: Thurgood, G. & LaPolla, R. (eds.), The Sino-Tibetan Languages, Routledge.
4. <a id="src-sasm_gnc"></a>SASM/GNC/SRC (1976). *Transcription of Tibetan (Tibetan pinyin)*. State Administration of Surveying and Mapping, China. [eki.ee](https://www.eki.ee/wgrs/rom1_bo.pdf)
5. <a id="src-brush1997"></a>Brush, Beaumont (1997). *The Status of Coronal in the Historical Development of Lhasa Tibetan Rhymes*. SIL Electronic Working Papers. [sil.org](https://www.sil.org/silewp/1997/001/silewp1997-001.pdf)
6. <a id="src-zhang2024"></a>Zhang, Yubin (2024). *Central Tibetan (Lhasa)*. Journal of the International Phonetic Association 54(2). Cited: 788-810. [doi.org](https://doi.org/10.1017/S0025100324000033)
7. <a id="src-tibetan_wiki"></a>Wikipedia contributors (2024). *Lhasa Tibetan*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Lhasa_Tibetan)
8. <a id="src-wikipron"></a>Lee, Jackson L. et al. (2020). *WikiPron: A Tool for Extracting Pronunciation Data from Wiktionary*. LREC. [github.com](https://github.com/CUNY-CL/wikipron)
9. <a id="src-hill2010"></a>Hill, Nathan W. (2010). *An overview of Old Tibetan synchronic phonology*. Transactions of the Philological Society 108(2). Cited: pp. 110-125. DOI [10.1111/j.1467-968X.2010.01234.x](https://doi.org/10.1111/j.1467-968X.2010.01234.x)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `bo` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 1564 | 0.3871 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 158 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Alveolar | Retroflex | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ | t tʰ |  | c cʰ | k kʰ | ʔ |
| Affricate |  | ts tsʰ | ʈʂ ʈʂʰ | tɕ tɕʰ |  |  |
| Nasal | m | n |  | ɲ | ŋ |  |
| Trill |  | r r̥ |  |  |  |  |
| Fricative |  | s | ʂ ʐ | ç ɕ |  | h |
| Approximant |  | ɹ |  | j |  |  |
| Lateral approximant |  | l l̥ |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː yː ĩ ỹ | u uː |
| Close-mid | e eː øː ø̃ ẽ | o oː |
| Open-mid | ɛː ɛ̃ |  |
| Open | a aː |  |

Sequences that the spec writes as one unit: [am˥˥] [am˥˨] [am˩˧˨] [am˩˨] [ap˥˨] [ap˩˧˨] [aŋ˥˥] [aŋ˥˨] [aŋ˩˧˨] [aŋ˩˨] [aʔ˥˨] [aʔ˩˧˨] [aː˥˥] [aː˩˨] [a˥˥] [a˩˨] [em˥˥] [em˥˨] [em˩˧˨] [em˩˨] [ep˥˨] [ep˩˧˨] [eŋ˥˥] [eŋ˥˨] [eŋ˩˧˨] [eŋ˩˨] [eʔ˥˨] [eʔ˩˧˨] [eː˥˥] [eː˥˨] [eː˩˧˨] [eː˩˨] [e˥˥] [e˩˨] [im˥˥] [im˥˨] [im˩˧˨] [im˩˨] [ip˥˨] [ip˩˧˨], and 68 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨་⟩ | ∅ |  |
| ⟨༌⟩ | ∅ |  |
| ⟨ཀ⟩ | [k] |  |
| ⟨ཀྭ⟩ | [k] |  |
| ⟨ཀྱ⟩ | [c] |  |
| ⟨ཀྲ⟩ | [ʈʂ] |  |
| ⟨ཀླ⟩ | [l] |  |
| ⟨ཁ⟩ | [kʰ] |  |
| ⟨ཁྭ⟩ | [kʰ] |  |
| ⟨ཁྱ⟩ | [cʰ] |  |
| ⟨ཁྲ⟩ | [ʈʂʰ] |  |
| ⟨ག⟩ | [kʰ] | after vowel ∅ · before consonant ∅ |
| ⟨གཡ⟩ | [j] |  |
| ⟨གྭ⟩ | [kʰ] |  |
| ⟨གྱ⟩ | [cʰ] |  |
| ⟨གྲ⟩ | [ʈʂʰ] |  |
| ⟨གྲྭ⟩ | [ʈʂʰ] |  |
| ⟨གླ⟩ | [l] |  |
| ⟨ང⟩ | [ŋ] | after vowel ∅ |
| ⟨ཅ⟩ | [tɕ] |  |
| ⟨ཅྭ⟩ | [tɕ] |  |
| ⟨ཆ⟩ | [tɕʰ] |  |
| ⟨ཇ⟩ | [tɕʰ] |  |
| ⟨ཉ⟩ | [ɲ] |  |
| ⟨ཉྭ⟩ | [ɲ] |  |
| ⟨ཏ⟩ | [t] |  |
| ⟨ཏྭ⟩ | [t] |  |
| ⟨ཏྲ⟩ | [ʈʂ] |  |
| ⟨ཐ⟩ | [tʰ] |  |
| ⟨ཐྲ⟩ | [ʈʂʰ] |  |
| ⟨ད⟩ | [tʰ] | after vowel ∅ · before consonant ∅ |
| ⟨དབ⟩ | [w] |  |
| ⟨དབྱ⟩ | [j] |  |
| ⟨དྭ⟩ | [tʰ] |  |
| ⟨དྲ⟩ | [ʈʂʰ] |  |
| ⟨ན⟩ | [n] | after vowel ∅ |
| ⟨པ⟩ | [p] |  |
| ⟨པྱ⟩ | [tɕ] |  |
| ⟨པྲ⟩ | [ʈʂ] |  |
| ⟨ཕ⟩ | [pʰ] |  |
| ⟨ཕྱ⟩ | [tɕʰ] |  |
| ⟨ཕྲ⟩ | [ʈʂʰ] |  |
| ⟨བ⟩ | [pʰ] | after vowel ∅ · before consonant ∅ |
| ⟨བྱ⟩ | [tɕʰ] |  |
| ⟨བྲ⟩ | [ʈʂʰ] |  |
| ⟨བླ⟩ | [l] |  |
| ⟨བྷ⟩ | [b] |  |
| ⟨མ⟩ | [m] | after vowel ∅ · before consonant ∅ |
| ⟨མྱ⟩ | [ɲ] |  |
| ⟨མྲ⟩ | [m] |  |
| ⟨ཙ⟩ | [ts] |  |
| ⟨ཚ⟩ | [tsʰ] |  |
| ⟨ཚྭ⟩ | [tsʰ] |  |
| ⟨ཛ⟩ | [tsʰ] |  |
| ⟨ཝ⟩ | [w] |  |
| ⟨ཞ⟩ | [ɕ] |  |
| ⟨ཞྭ⟩ | [ɕ] |  |
| ⟨ཟ⟩ | [s] |  |
| ⟨ཟྭ⟩ | [s] |  |
| ⟨ཟླ⟩ | [t] |  |
| ⟨ཡ⟩ | [j] |  |
| ⟨ར⟩ | [ʐ] | after vowel ∅ |
| ⟨རྐ⟩ | [k] |  |
| ⟨རྐྱ⟩ | [c] |  |
| ⟨རྐྲ⟩ | [ʈʂ] |  |
| ⟨རྒ⟩ | [k] |  |
| ⟨རྒྱ⟩ | [c] |  |
| ⟨རྒྲ⟩ | [ʈʂ] |  |
| ⟨རྔ⟩ | [ŋ] |  |
| ⟨རྗ⟩ | [tɕ] |  |
| ⟨རྙ⟩ | [ɲ] |  |
| ⟨རྟ⟩ | [t] |  |
| ⟨རྡ⟩ | [t] |  |
| ⟨རྣ⟩ | [n] |  |
| ⟨རྦ⟩ | [p] |  |
| ⟨རྦྱ⟩ | [tɕ] |  |
| ⟨རྦྲ⟩ | [ʈʂ] |  |
| ⟨རྨ⟩ | [m] |  |
| ⟨རྨྱ⟩ | [ɲ] |  |
| ⟨རྩ⟩ | [ts] |  |
| ⟨རྩྭ⟩ | [ts] |  |
| ⟨རྫ⟩ | [ts] |  |
| ⟨རྭ⟩ | [ʐ] |  |
| ⟨རླ⟩ | [l] |  |
| ⟨རྷ⟩ | [r̥] |  |
| ⟨ལ⟩ | [l] | after vowel ∅ |
| ⟨ལྐ⟩ | [k] |  |
| ⟨ལྐྱ⟩ | [c] |  |
| ⟨ལྐྲ⟩ | [ʈʂ] |  |
| ⟨ལྒ⟩ | [k] |  |
| ⟨ལྒྱ⟩ | [c] |  |
| ⟨ལྒྲ⟩ | [ʈʂ] |  |
| ⟨ལྔ⟩ | [ŋ] |  |
| ⟨ལྕ⟩ | [tɕ] |  |
| ⟨ལྗ⟩ | [tɕ] |  |
| ⟨ལྟ⟩ | [t] |  |
| ⟨ལྠ⟩ | [t] |  |
| ⟨ལྡ⟩ | [t] |  |
| ⟨ལྤ⟩ | [p] |  |
| ⟨ལྤྱ⟩ | [tɕ] |  |
| ⟨ལྤྲ⟩ | [ʈʂ] |  |
| ⟨ལྦ⟩ | [p] |  |
| ⟨ལྦྱ⟩ | [tɕ] |  |
| ⟨ལྦྲ⟩ | [ʈʂ] |  |
| ⟨ལྭ⟩ | [l] |  |
| ⟨ལྷ⟩ | [l̥] |  |
| ⟨ཤ⟩ | [ɕ] |  |
| ⟨ཤྭ⟩ | [ɕ] |  |
| ⟨ས⟩ | [s] | after vowel ∅ |
| ⟨སྐ⟩ | [k] |  |
| ⟨སྐྱ⟩ | [c] |  |
| ⟨སྐྲ⟩ | [ʈʂ] |  |
| ⟨སྒ⟩ | [k] |  |
| ⟨སྒྱ⟩ | [c] |  |
| ⟨སྒྲ⟩ | [ʈʂ] |  |
| ⟨སྔ⟩ | [ŋ] |  |
| ⟨སྙ⟩ | [ɲ] |  |
| ⟨སྟ⟩ | [t] |  |
| ⟨སྡ⟩ | [t] |  |
| ⟨སྣ⟩ | [n] |  |
| ⟨སྤ⟩ | [p] |  |
| ⟨སྤྱ⟩ | [tɕ] |  |
| ⟨སྤྲ⟩ | [ʈʂ] |  |
| ⟨སྦ⟩ | [p] |  |
| ⟨སྦྱ⟩ | [tɕ] |  |
| ⟨སྦྲ⟩ | [ʈʂ] |  |
| ⟨སྨ⟩ | [m] |  |
| ⟨སྨྱ⟩ | [ɲ] |  |
| ⟨སྨྲ⟩ | [m] |  |
| ⟨སྩ⟩ | [ts] |  |
| ⟨སྩྭ⟩ | [ts] |  |
| ⟨སྭ⟩ | [s] |  |
| ⟨སྲ⟩ | [s] |  |
| ⟨སླ⟩ | [l] |  |
| ⟨ཧ⟩ | [h] |  |
| ⟨ཧྭ⟩ | [h] |  |
| ⟨ཧྱ⟩ | [ç] |  |
| ⟨ཧྲ⟩ | [ʂ] |  |
| ⟨ཨ⟩ | [ʔ] |  |
| ⟨ཱ⟩ | [ː] |  |
| ⟨ི⟩ | [i] |  |
| ⟨ུ⟩ | [u] |  |
| ⟨ེ⟩ | [e] |  |
| ⟨ཻ⟩ | [e] |  |
| ⟨ོ⟩ | [o] |  |
| ⟨ཽ⟩ | [o] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 142 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `BO_RHYME_3906_a_HIGH` | /a/ → [aʔ˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ག⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3906_INH_HIGH` | /a/ → [aʔ˥˨], after [c] [cʰ] [h] [j] [k] [kʰ] [l] [l̥] and 20 more, spelled ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ག⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3906_i_HIGH` | /i/ → [iʔ˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ག⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3906_u_HIGH` | /u/ → [uʔ˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ག⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3906_e_HIGH` | /e/ → [eʔ˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ག⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3906_o_HIGH` | /o/ → [oʔ˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ག⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3906_a_LOW` | /a/ → [aʔ˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ག⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3906_INH_LOW` | /a/ → [aʔ˩˧˨], after [b] [c] [cʰ] [j] [k] [kʰ] [l] [m] and 17 more, spelled ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ག⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3906_i_LOW` | /i/ → [iʔ˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ག⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3906_u_LOW` | /u/ → [uʔ˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ག⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3906_e_LOW` | /e/ → [eʔ˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ག⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3906_o_LOW` | /o/ → [oʔ˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ག⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3926_a_HIGH` | /a/ → [ap˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨བ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3926_INH_HIGH` | /a/ → [ap˥˨], after [c] [cʰ] [h] [j] [k] [kʰ] [l] [l̥] and 20 more, spelled ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨བ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3926_i_HIGH` | /i/ → [ip˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨བ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3926_u_HIGH` | /u/ → [up˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨བ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3926_e_HIGH` | /e/ → [ep˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨བ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3926_o_HIGH` | /o/ → [op˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨བ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3926_a_LOW` | /a/ → [ap˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨བ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3926_INH_LOW` | /a/ → [ap˩˧˨], after [b] [c] [cʰ] [j] [k] [kʰ] [l] [m] and 17 more, spelled ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨བ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3926_i_LOW` | /i/ → [ip˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨བ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3926_u_LOW` | /u/ → [up˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨བ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3926_e_LOW` | /e/ → [ep˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨བ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3926_o_LOW` | /o/ → [op˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨བ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3921_3942_a_HIGH` | /a/ → [ɛː˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ད⟩ ⟨ས⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3921_3942_INH_HIGH` | /a/ → [ɛː˥˨], after [c] [cʰ] [h] [j] [k] [kʰ] [l] [l̥] and 20 more, spelled ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ད⟩ ⟨ས⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3921_3942_i_HIGH` | /i/ → [iː˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ད⟩ ⟨ས⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3921_3942_u_HIGH` | /u/ → [yː˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ད⟩ ⟨ས⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3921_3942_e_HIGH` | /e/ → [eː˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ད⟩ ⟨ས⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3921_3942_o_HIGH` | /o/ → [øː˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ད⟩ ⟨ས⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3921_3942_a_LOW` | /a/ → [ɛː˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ད⟩ ⟨ས⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3921_3942_INH_LOW` | /a/ → [ɛː˩˧˨], after [b] [c] [cʰ] [j] [k] [kʰ] [l] [m] and 17 more, spelled ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ད⟩ ⟨ས⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3921_3942_i_LOW` | /i/ → [iː˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ད⟩ ⟨ས⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3921_3942_u_LOW` | /u/ → [yː˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ད⟩ ⟨ས⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3921_3942_e_LOW` | /e/ → [eː˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ད⟩ ⟨ས⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3921_3942_o_LOW` | /o/ → [øː˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ད⟩ ⟨ས⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_S_a_HIGH` | /a/ → [aŋ˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ང⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_S_INH_HIGH` | /a/ → [aŋ˥˨], after [c] [cʰ] [h] [j] [k] [kʰ] [l] [l̥] and 20 more, spelled ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ང⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_S_i_HIGH` | /i/ → [iŋ˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ང⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_S_u_HIGH` | /u/ → [uŋ˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ང⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_S_e_HIGH` | /e/ → [eŋ˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ང⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_S_o_HIGH` | /o/ → [oŋ˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ང⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_S_a_LOW` | /a/ → [aŋ˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ང⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_S_INH_LOW` | /a/ → [aŋ˩˧˨], after [b] [c] [cʰ] [j] [k] [kʰ] [l] [m] and 17 more, spelled ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ང⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_S_i_LOW` | /i/ → [iŋ˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ང⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_S_u_LOW` | /u/ → [uŋ˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ང⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_S_e_LOW` | /e/ → [eŋ˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ང⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_S_o_LOW` | /o/ → [oŋ˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ང⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_S_a_HIGH` | /a/ → [am˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨མ⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_S_INH_HIGH` | /a/ → [am˥˨], after [c] [cʰ] [h] [j] [k] [kʰ] [l] [l̥] and 20 more, spelled ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨མ⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_S_i_HIGH` | /i/ → [im˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨མ⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_S_u_HIGH` | /u/ → [um˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨མ⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_S_e_HIGH` | /e/ → [em˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨མ⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_S_o_HIGH` | /o/ → [om˥˨], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨མ⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_S_a_LOW` | /a/ → [am˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨མ⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_S_INH_LOW` | /a/ → [am˩˧˨], after [b] [c] [cʰ] [j] [k] [kʰ] [l] [m] and 17 more, spelled ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨མ⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_S_i_LOW` | /i/ → [im˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨མ⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_S_u_LOW` | /u/ → [um˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨མ⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_S_e_LOW` | /e/ → [em˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨མ⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_S_o_LOW` | /o/ → [om˩˧˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨མ⟩, with more context in the spec | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_a_HIGH` | /a/ → [aŋ˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ང⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_INH_HIGH` | /a/ → [aŋ˥˥], after [c] [cʰ] [h] [j] [k] [kʰ] [l] [l̥] and 20 more, spelled ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ང⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_i_HIGH` | /i/ → [iŋ˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ང⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_u_HIGH` | /u/ → [uŋ˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ང⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_e_HIGH` | /e/ → [eŋ˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ང⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_o_HIGH` | /o/ → [oŋ˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ང⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_a_LOW` | /a/ → [aŋ˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ང⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_INH_LOW` | /a/ → [aŋ˩˨], after [b] [c] [cʰ] [j] [k] [kʰ] [l] [m] and 17 more, spelled ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ང⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_i_LOW` | /i/ → [iŋ˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ང⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_u_LOW` | /u/ → [uŋ˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ང⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_e_LOW` | /e/ → [eŋ˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ང⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3908_o_LOW` | /o/ → [oŋ˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ང⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_a_HIGH` | /a/ → [am˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨མ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_INH_HIGH` | /a/ → [am˥˥], after [c] [cʰ] [h] [j] [k] [kʰ] [l] [l̥] and 20 more, spelled ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨མ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_i_HIGH` | /i/ → [im˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨མ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_u_HIGH` | /u/ → [um˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨མ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_e_HIGH` | /e/ → [em˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨མ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_o_HIGH` | /o/ → [om˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨མ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_a_LOW` | /a/ → [am˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨མ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_INH_LOW` | /a/ → [am˩˨], after [b] [c] [cʰ] [j] [k] [kʰ] [l] [m] and 17 more, spelled ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨མ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_i_LOW` | /i/ → [im˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨མ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_u_LOW` | /u/ → [um˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨མ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_e_LOW` | /e/ → [em˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨མ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3928_o_LOW` | /o/ → [om˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨མ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3923_a_HIGH` | /a/ → [ɛ̃˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ན⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3923_INH_HIGH` | /a/ → [ɛ̃˥˥], after [c] [cʰ] [h] [j] [k] [kʰ] [l] [l̥] and 20 more, spelled ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ན⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3923_i_HIGH` | /i/ → [ĩ˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ན⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3923_u_HIGH` | /u/ → [ỹ˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ན⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3923_e_HIGH` | /e/ → [ẽ˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ན⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3923_o_HIGH` | /o/ → [ø̃˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ན⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3923_a_LOW` | /a/ → [ɛ̃˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ན⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3923_INH_LOW` | /a/ → [ɛ̃˩˨], after [b] [c] [cʰ] [j] [k] [kʰ] [l] [m] and 17 more, spelled ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ན⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3923_i_LOW` | /i/ → [ĩ˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ན⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3923_u_LOW` | /u/ → [ỹ˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ན⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3923_e_LOW` | /e/ → [ẽ˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ན⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3923_o_LOW` | /o/ → [ø̃˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ན⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3939_3936_a_HIGH` | /a/ → [ɛː˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ལ⟩ ⟨འི⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3939_3936_INH_HIGH` | /a/ → [ɛː˥˥], after [c] [cʰ] [h] [j] [k] [kʰ] [l] [l̥] and 20 more, spelled ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ལ⟩ ⟨འི⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3939_3936_i_HIGH` | /i/ → [iː˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ལ⟩ ⟨འི⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3939_3936_u_HIGH` | /u/ → [yː˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ལ⟩ ⟨འི⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3939_3936_e_HIGH` | /e/ → [eː˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ལ⟩ ⟨འི⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3939_3936_o_HIGH` | /o/ → [øː˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ལ⟩ ⟨འི⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3939_3936_a_LOW` | /a/ → [ɛː˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ལ⟩ ⟨འི⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3939_3936_INH_LOW` | /a/ → [ɛː˩˨], after [b] [c] [cʰ] [j] [k] [kʰ] [l] [m] and 17 more, spelled ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ལ⟩ ⟨འི⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3939_3936_i_LOW` | /i/ → [iː˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ལ⟩ ⟨འི⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3939_3936_u_LOW` | /u/ → [yː˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ལ⟩ ⟨འི⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3939_3936_e_LOW` | /e/ → [eː˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ལ⟩ ⟨འི⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3939_3936_o_LOW` | /o/ → [øː˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ལ⟩ ⟨འི⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3938_3936_a_HIGH` | /a/ → [aː˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ར⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3938_3936_INH_HIGH` | /a/ → [aː˥˥], after [c] [cʰ] [h] [j] [k] [kʰ] [l] [l̥] and 20 more, spelled ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ར⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3938_3936_i_HIGH` | /i/ → [iː˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ར⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3938_3936_u_HIGH` | /u/ → [uː˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ར⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3938_3936_e_HIGH` | /e/ → [eː˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ར⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3938_3936_o_HIGH` | /o/ → [oː˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more, before ⟨ར⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3938_3936_a_LOW` | /a/ → [aː˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ར⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3938_3936_INH_LOW` | /a/ → [aː˩˨], after [b] [c] [cʰ] [j] [k] [kʰ] [l] [m] and 17 more, spelled ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ར⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3938_3936_i_LOW` | /i/ → [iː˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ར⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3938_3936_u_LOW` | /u/ → [uː˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ར⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3938_3936_e_LOW` | /e/ → [eː˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ར⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_RHYME_3938_3936_o_LOW` | /o/ → [oː˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more, before ⟨ར⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_TONE_a_HIGH` | /a/ → [a˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_TONE_INH_HIGH` | /a/ → [a˥˥], after [c] [cʰ] [h] [j] [k] [kʰ] [l] [l̥] and 20 more, spelled ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_TONE_i_HIGH` | /i/ → [i˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_TONE_u_HIGH` | /u/ → [u˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_TONE_e_HIGH` | /e/ → [e˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_TONE_o_HIGH` | /o/ → [o˥˥], after ⟨པ⟩ ⟨སྤ⟩ ⟨ལྤ⟩ ⟨ཕ⟩ ⟨རྨ⟩ ⟨སྨ⟩ ⟨སྨྲ⟩ ⟨ཏ⟩ and 72 more | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_TONE_a_LOW` | /a/ → [a˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_TONE_INH_LOW` | /a/ → [a˩˨], after [b] [c] [cʰ] [j] [k] [kʰ] [l] [m] and 17 more, spelled ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_TONE_i_LOW` | /i/ → [i˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_TONE_u_LOW` | /u/ → [u˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_TONE_e_LOW` | /e/ → [e˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_TONE_o_LOW` | /o/ → [o˩˨], after ⟨རྦ⟩ ⟨སྦ⟩ ⟨ལྦ⟩ ⟨བ⟩ ⟨བྷ⟩ ⟨མ⟩ ⟨མྲ⟩ ⟨དབ⟩ and 50 more | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003), [DeLancey 2003](#src-delancey2003) |
| `BO_POST_SUFFIX_S_VOWEL` | /s/ → ∅, spelled ⟨ས⟩, after ⟨ག⟩ ⟨ང⟩ ⟨བ⟩ ⟨མ⟩, with more context in the spec | - | [DeLancey 2003](#src-delancey2003) |
| `BO_POST_SUFFIX_S_CONSONANT` | /s/ → ∅, spelled ⟨ས⟩, after ⟨ག⟩ ⟨ང⟩ ⟨བ⟩ ⟨མ⟩, with more context in the spec | - | [DeLancey 2003](#src-delancey2003) |
| `BO_MEDIAL_BA_LENITION` | /pʰ/ → [w], before [a] [i] [u] [e] [o], spelled ⟨བ⟩, after ⟨་⟩ | - | - |
| `BO_PREFIX_DEASPIRATION_kʰ` | /kʰ/ → [k], before [a] [i] [u] [e] [o], spelled ⟨ག⟩ ⟨གྭ⟩, after ⟨ག⟩ ⟨ད⟩ ⟨བ⟩ ⟨མ⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003) |
| `BO_PREFIX_DEASPIRATION_tʰ` | /tʰ/ → [t], before [a] [i] [u] [e] [o], spelled ⟨ད⟩ ⟨དྭ⟩, after ⟨ག⟩ ⟨ད⟩ ⟨བ⟩ ⟨མ⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003) |
| `BO_PREFIX_DEASPIRATION_pʰ` | /pʰ/ → [p], before [a] [i] [u] [e] [o], spelled ⟨བ⟩, after ⟨ག⟩ ⟨ད⟩ ⟨བ⟩ ⟨མ⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003) |
| `BO_PREFIX_DEASPIRATION_tsʰ` | /tsʰ/ → [ts], before [a] [i] [u] [e] [o], spelled ⟨ཛ⟩, after ⟨ག⟩ ⟨ད⟩ ⟨བ⟩ ⟨མ⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003) |
| `BO_PREFIX_DEASPIRATION_tɕʰ` | /tɕʰ/ → [tɕ], before [a] [i] [u] [e] [o], spelled ⟨ཇ⟩ ⟨བྱ⟩, after ⟨ག⟩ ⟨ད⟩ ⟨བ⟩ ⟨མ⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003) |
| `BO_PREFIX_DEASPIRATION_cʰ` | /cʰ/ → [c], before [a] [i] [u] [e] [o], spelled ⟨གྱ⟩, after ⟨ག⟩ ⟨ད⟩ ⟨བ⟩ ⟨མ⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003) |
| `BO_PREFIX_DEASPIRATION_ʈʂʰ` | /ʈʂʰ/ → [ʈʂ], before [a] [i] [u] [e] [o], spelled ⟨གྲ⟩ ⟨དྲ⟩ ⟨བྲ⟩ ⟨གྲྭ⟩, after ⟨ག⟩ ⟨ད⟩ ⟨བ⟩ ⟨མ⟩ ⟨འ⟩ | - | [Germano 2003](#src-thl_phonetics), [Tournadre 2003](#src-tournadre_dorje2003) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "bo")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Thai](th.md) · [Home](../index.md) · [Tihāmi Qaḥtāni Arabic →](ar-SA-x-tihama-qahtan.md)
