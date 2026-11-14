# Namuyi (`nmy`)

<!-- atlas:summary begin -->
Namuyi is a Sino-Tibetan language, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `nmy` spec is at the research tier. It cites 8 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `nmy` |
| ISO 639-3 | [nmy](https://iso639-3.sil.org/code/nmy), Namuyi |
| Wikipedia | [Namuyi language](https://en.wikipedia.org/wiki/Namuyi_language) |
| Family | [Sino-Tibetan](by-family.md#sino-tibetan) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Sino-Tibetan](https://tigregotico.github.io/orthography2ipa/#x-clade-sino1245) `x-clade-sino1245` |
| Explorer | [`nmy` in the data explorer](https://tigregotico.github.io/orthography2ipa/#nmy) |
| Spec file | [`nmy.json`](../../orthography2ipa/data/nmy.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Namuyi Khatho (Qiangic, Sino-Tibetan) of southwestern Sichuan, China, in the Roman orthography of Pavlík (2017) as amended by Li (2017), the spelling the Wiktionary Namuyi corpus is written in. INPUT CONTRACT: Pavlík/Li-orthography Namuyi.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 8 works, from 2009 to 2025. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 132 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/nmy.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `nmy` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 8 works. 7 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-nmy_glottolog"></a>Hammarström, H. et al. (Glottolog 5.0) (2024). *Glottolog: Namuyi (namu1246)*. Max Planck Institute for Evolutionary Anthropology. [glottolog.org](https://glottolog.org/resource/languoid/id/namu1246)
2. <a id="src-nmy_wikipedia"></a>Wikipedia contributors (2024). *Namuyi language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Namuyi_language)
3. <a id="src-nmy_pavlik2017"></a>Pavlík, Štěpán (2017). *The Description of Namuzi Language*. PhD thesis, Charles University, Prague. [dspace.cuni.cz](https://dspace.cuni.cz/bitstream/handle/20.500.11956/95965/140058069.pdf?sequence=1)
4. <a id="src-nmy_li2017"></a>Li Jianfu (2017). *A Descriptive Grammar of Namuyi Khatho spoken by Namuyi Tibetans*. PhD thesis, La Trobe University, Victoria.
5. <a id="src-nmy_lakhi2009"></a>Libu Lakhi (Li Jianfu), Tsering Bum & Charles Kevin Stuart (2009). *China's Namuyi Tibetans: Life, Language and Folklore (Asian Highlands Perspectives 2A/2B)*. Asian Highlands Perspectives. [archive.org](https://archive.org/details/ChinasNamziTibetansLifeLanguageAndFolklore.VolumeOne.asian)
6. <a id="src-nmy_wiktionary_guidelines"></a>Wiktionary contributors (2025). *Wiktionary:Namuyi entry guidelines*. Wikimedia Foundation. [en.wiktionary.org](https://en.wiktionary.org/wiki/Wiktionary:Namuyi_entry_guidelines)
7. <a id="src-nmy_wiktionary_module"></a>Wiktionary contributors (2025). *Module:nmy-IPA (English Wiktionary)*. Wikimedia Foundation. [en.wiktionary.org](https://en.wiktionary.org/wiki/Module:nmy-IPA)
8. <a id="src-nmy_asianethnology"></a>Asian Ethnology contributors (2015). *The Namuyi: Linguistic and Cultural Features*. Asian Ethnology. [asianethnology.org](https://asianethnology.org/article/150248-the-namuyi-linguistic-and-cultural-features/attachment/314162.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `nmy` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 354 | 0.1091 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 198 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Retroflex | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  |  | k kʰ ɡ | q qʰ ɢ |  |
| Affricate |  |  | dz ts tsʰ |  | dʑ tɕ tɕʰ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ | ɴ |  |
| Fricative |  | f v | s z | ʂ ʐ |  | x x̃ | ʁ χ | ɦ ɦ̃ |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l l̥ |  |  |  |  |  |

Sequences that the spec writes as one unit: [a˥] [a˥˧] [a˧] [a˧˥] [a˧˩] [a˨] [bʙ] [dʐ] [dʙ] [e˥] [e˥˧] [e˧] [e˧˥] [e˧˩] [e˨] [i˥] [i˥˧] [i˧] [i˧˥] [i˧˩] [i˨] [o˥] [o˥˧] [o˧] [o˧˥] [o˧˩] [o˨] [pʙ̥] [tʂ] [tʂʰ] [tʙ̥] [u˥] [u˥˧] [u˧] [u˧˥] [u˧˩] [u˨] [v̩˥] [v̩˥˧] [v̩˧], and 120 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a˧] | word initial [ʔa˧] |
| ⟨b⟩ | [b] |  |
| ⟨bb⟩ | [bʙ] |  |
| ⟨c⟩ | [tʂ] |  |
| ⟨ch⟩ | [tʂʰ] |  |
| ⟨d⟩ | [d] |  |
| ⟨db⟩ | [dʙ] |  |
| ⟨dz⟩ | [dz] |  |
| ⟨dzh⟩ | [dʐ] |  |
| ⟨e⟩ | [e˧] | word initial [ʔe˧] |
| ⟨eh⟩ | [ɤ˧] | word initial [ʔɤ˧] |
| ⟨er⟩ | [ɚ˧] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gh⟩ | [ɢ] |  |
| ⟨gy⟩ | [dʑ] |  |
| ⟨h⟩ | [ɦ] |  |
| ⟨hn⟩ | [ɦ̃] |  |
| ⟨hr⟩ | [ʁ] |  |
| ⟨i⟩ | [i˧] | word initial [ʔi˧] |
| ⟨ih⟩ | [ɨ˧] | word initial [ʔɨ˧] |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [kʰ] |  |
| ⟨khy⟩ | [tɕʰ] |  |
| ⟨ky⟩ | [tɕ] |  |
| ⟨l⟩ | [l] |  |
| ⟨lh⟩ | [l̥] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ngh⟩ | [ɴɢ] |  |
| ⟨ny⟩ | [ɲ] |  |
| ⟨o⟩ | [o˧] | word initial [ʔo˧] |
| ⟨p⟩ | [p] |  |
| ⟨pb⟩ | [pʙ̥] |  |
| ⟨ph⟩ | [pʰ] |  |
| ⟨q⟩ | [q] |  |
| ⟨qh⟩ | [qʰ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sh⟩ | [ʂ] |  |
| ⟨t⟩ | [t] |  |
| ⟨tb⟩ | [tʙ̥] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨thy⟩ | [tɕʰ] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨tsh⟩ | [tsʰ] |  |
| ⟨ty⟩ | [tɕ] |  |
| ⟨u⟩ | [u˧] | before vowel [w] · word initial [ʔu˧] |
| ⟨uh⟩ | [ʉ˧] | word initial [ʔʉ˧] |
| ⟨v⟩ | [v] |  |
| ⟨vih⟩ | [v̩˧] |  |
| ⟨vìh⟩ | [v̩˥˧] |  |
| ⟨víh⟩ | [v̩˧˥] |  |
| ⟨vîh⟩ | [v̩˥] |  |
| ⟨vīh⟩ | [v̩˧˩] |  |
| ⟨vĭh⟩ | [v̩˨] |  |
| ⟨vȋh⟩ | [v̩˥] |  |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [x] |  |
| ⟨xn⟩ | [x̃] |  |
| ⟨xr⟩ | [χ] |  |
| ⟨y⟩ | [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨zh⟩ | [ʐ] |  |
| ⟨à⟩ | [a˥˧] | word initial [ʔa˥˧] |
| ⟨á⟩ | [a˧˥] | word initial [ʔa˧˥] |
| ⟨â⟩ | [a˥] | word initial [ʔa˥] |
| ⟨ä⟩ | [æ˧] | word initial [ʔæ˧] |
| ⟨ä̀⟩ | [æ˥˧] | word initial [ʔæ˥˧] |
| ⟨ä́⟩ | [æ˧˥] | word initial [ʔæ˧˥] |
| ⟨ä̂⟩ | [æ˥] | word initial [ʔæ˥] |
| ⟨ä̆⟩ | [æ˨] | word initial [ʔæ˨] |
| ⟨ä̑⟩ | [æ˥] | word initial [ʔæ˥] |
| ⟨è⟩ | [e˥˧] | word initial [ʔe˥˧] |
| ⟨èh⟩ | [ɤ˥˧] | word initial [ʔɤ˥˧] |
| ⟨èr⟩ | [ɚ˥˧] |  |
| ⟨é⟩ | [e˧˥] | word initial [ʔe˧˥] |
| ⟨éh⟩ | [ɤ˧˥] | word initial [ʔɤ˧˥] |
| ⟨ér⟩ | [ɚ˧˥] |  |
| ⟨ê⟩ | [e˥] | word initial [ʔe˥] |
| ⟨êh⟩ | [ɤ˥] | word initial [ʔɤ˥] |
| ⟨êr⟩ | [ɚ˥] |  |
| ⟨ì⟩ | [i˥˧] | word initial [ʔi˥˧] |
| ⟨ìh⟩ | [ɨ˥˧] | word initial [ʔɨ˥˧] |
| ⟨í⟩ | [i˧˥] | word initial [ʔi˧˥] |
| ⟨íh⟩ | [ɨ˧˥] | word initial [ʔɨ˧˥] |
| ⟨î⟩ | [i˥] | word initial [ʔi˥] |
| ⟨îh⟩ | [ɨ˥] | word initial [ʔɨ˥] |
| ⟨ò⟩ | [o˥˧] | word initial [ʔo˥˧] |
| ⟨ó⟩ | [o˧˥] | word initial [ʔo˧˥] |
| ⟨ô⟩ | [o˥] | word initial [ʔo˥] |
| ⟨ù⟩ | [u˥˧] | before vowel [w] · word initial [ʔu˥˧] |
| ⟨ùh⟩ | [ʉ˥˧] | word initial [ʔʉ˥˧] |
| ⟨ú⟩ | [u˧˥] | before vowel [w] · word initial [ʔu˧˥] |
| ⟨úh⟩ | [ʉ˧˥] | word initial [ʔʉ˧˥] |
| ⟨û⟩ | [u˥] | before vowel [w] · word initial [ʔu˥] |
| ⟨ûh⟩ | [ʉ˥] | word initial [ʔʉ˥] |
| ⟨ü⟩ | [y˧] | word initial [ʔy˧] |
| ⟨ü̂⟩ | [y˥] | word initial [ʔy˥] |
| ⟨ü̆⟩ | [y˨] | word initial [ʔy˨] |
| ⟨ü̑⟩ | [y˥] | word initial [ʔy˥] |
| ⟨ā⟩ | [a˧˩] | word initial [ʔa˧˩] |
| ⟨ă⟩ | [a˨] | word initial [ʔa˨] |
| ⟨ē⟩ | [e˧˩] | word initial [ʔe˧˩] |
| ⟨ēh⟩ | [ɤ˧˩] | word initial [ʔɤ˧˩] |
| ⟨ēr⟩ | [ɚ˧˩] |  |
| ⟨ĕ⟩ | [e˨] | word initial [ʔe˨] |
| ⟨ĕh⟩ | [ɤ˨] | word initial [ʔɤ˨] |
| ⟨ĕr⟩ | [ɚ˨] |  |
| ⟨ī⟩ | [i˧˩] | word initial [ʔi˧˩] |
| ⟨īh⟩ | [ɨ˧˩] | word initial [ʔɨ˧˩] |
| ⟨ĭ⟩ | [i˨] | word initial [ʔi˨] |
| ⟨ĭh⟩ | [ɨ˨] | word initial [ʔɨ˨] |
| ⟨ō⟩ | [o˧˩] | word initial [ʔo˧˩] |
| ⟨ŏ⟩ | [o˨] | word initial [ʔo˨] |
| ⟨ū⟩ | [u˧˩] | before vowel [w] · word initial [ʔu˧˩] |
| ⟨ūh⟩ | [ʉ˧˩] | word initial [ʔʉ˧˩] |
| ⟨ŭ⟩ | [u˨] | before vowel [w] · word initial [ʔu˨] |
| ⟨ŭh⟩ | [ʉ˨] | word initial [ʔʉ˨] |
| ⟨ǖ⟩ | [y˧˩] | word initial [ʔy˧˩] |
| ⟨ǘ⟩ | [y˧˥] | word initial [ʔy˧˥] |
| ⟨ǜ⟩ | [y˥˧] | word initial [ʔy˥˧] |
| ⟨ǟ⟩ | [æ˧˩] | word initial [ʔæ˧˩] |
| ⟨ȃ⟩ | [a˥] | word initial [ʔa˥] |
| ⟨ȇ⟩ | [e˥] | word initial [ʔe˥] |
| ⟨ȇh⟩ | [ɤ˥] | word initial [ʔɤ˥] |
| ⟨ȇr⟩ | [ɚ˥] |  |
| ⟨ȋ⟩ | [i˥] | word initial [ʔi˥] |
| ⟨ȋh⟩ | [ɨ˥] | word initial [ʔɨ˥] |
| ⟨ȏ⟩ | [o˥] | word initial [ʔo˥] |
| ⟨ȗ⟩ | [u˥] | before vowel [w] · word initial [ʔu˥] |
| ⟨ȗh⟩ | [ʉ˥] | word initial [ʔʉ˥] |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 27 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `NMY_APICAL_BACK_M` | /ɨ˧/ → [ɯ˧], after [tʂ] [tʂʰ] [dʐ] [ʂ] [ʐ] | - | - |
| `NMY_A_BACKED_M` | /a˧/ → [ɑ˧], after [k] [kʰ] [ɡ] [x] [ŋ] [q] [qʰ] [ɢ] and 3 more | - | - |
| `NMY_O_LOWERED_M` | /o˧/ → [ɔ˧], after [q] [qʰ] [ɢ] [χ] [ʁ] [ɴɢ] | - | - |
| `NMY_APICAL_BACK_ML` | /ɨ˧˩/ → [ɯ˧˩], after [tʂ] [tʂʰ] [dʐ] [ʂ] [ʐ] | - | - |
| `NMY_A_BACKED_ML` | /a˧˩/ → [ɑ˧˩], after [k] [kʰ] [ɡ] [x] [ŋ] [q] [qʰ] [ɢ] and 3 more | - | - |
| `NMY_O_LOWERED_ML` | /o˧˩/ → [ɔ˧˩], after [q] [qʰ] [ɢ] [χ] [ʁ] [ɴɢ] | - | - |
| `NMY_APICAL_BACK_HM` | /ɨ˥˧/ → [ɯ˥˧], after [tʂ] [tʂʰ] [dʐ] [ʂ] [ʐ] | - | - |
| `NMY_A_BACKED_HM` | /a˥˧/ → [ɑ˥˧], after [k] [kʰ] [ɡ] [x] [ŋ] [q] [qʰ] [ɢ] and 3 more | - | - |
| `NMY_O_LOWERED_HM` | /o˥˧/ → [ɔ˥˧], after [q] [qʰ] [ɢ] [χ] [ʁ] [ɴɢ] | - | - |
| `NMY_APICAL_BACK_H` | /ɨ˥/ → [ɯ˥], after [tʂ] [tʂʰ] [dʐ] [ʂ] [ʐ] | - | - |
| `NMY_A_BACKED_H` | /a˥/ → [ɑ˥], after [k] [kʰ] [ɡ] [x] [ŋ] [q] [qʰ] [ɢ] and 3 more | - | - |
| `NMY_O_LOWERED_H` | /o˥/ → [ɔ˥], after [q] [qʰ] [ɢ] [χ] [ʁ] [ɴɢ] | - | - |
| `NMY_APICAL_BACK_H` | /ɨ˥/ → [ɯ˥], after [tʂ] [tʂʰ] [dʐ] [ʂ] [ʐ] | - | - |
| `NMY_A_BACKED_H` | /a˥/ → [ɑ˥], after [k] [kʰ] [ɡ] [x] [ŋ] [q] [qʰ] [ɢ] and 3 more | - | - |
| `NMY_O_LOWERED_H` | /o˥/ → [ɔ˥], after [q] [qʰ] [ɢ] [χ] [ʁ] [ɴɢ] | - | - |
| `NMY_APICAL_BACK_˨` | /ɨ˨/ → [ɯ˨], after [tʂ] [tʂʰ] [dʐ] [ʂ] [ʐ] | - | - |
| `NMY_A_BACKED_˨` | /a˨/ → [ɑ˨], after [k] [kʰ] [ɡ] [x] [ŋ] [q] [qʰ] [ɢ] and 3 more | - | - |
| `NMY_O_LOWERED_˨` | /o˨/ → [ɔ˨], after [q] [qʰ] [ɢ] [χ] [ʁ] [ɴɢ] | - | - |
| `NMY_APICAL_BACK_MH` | /ɨ˧˥/ → [ɯ˧˥], after [tʂ] [tʂʰ] [dʐ] [ʂ] [ʐ] | - | - |
| `NMY_A_BACKED_MH` | /a˧˥/ → [ɑ˧˥], after [k] [kʰ] [ɡ] [x] [ŋ] [q] [qʰ] [ɢ] and 3 more | - | - |
| `NMY_O_LOWERED_MH` | /o˧˥/ → [ɔ˧˥], after [q] [qʰ] [ɢ] [χ] [ʁ] [ɴɢ] | - | - |
| `NMY_PALATALISE_tɕ` | /t/ → [tɕ], before ⟨i⟩ ⟨ih⟩ ⟨y⟩ ⟨ì⟩ ⟨ìh⟩ ⟨í⟩ ⟨íh⟩ ⟨î⟩ and 7 more | ⟨tī⟩ [tɕi˧˩] | - |
| `NMY_PALATALISE_tɕʰ` | /tʰ/ → [tɕʰ], before ⟨i⟩ ⟨ih⟩ ⟨y⟩ ⟨ì⟩ ⟨ìh⟩ ⟨í⟩ ⟨íh⟩ ⟨î⟩ and 7 more | ⟨thi⟩ [tɕʰi˧] | - |
| `NMY_H_NASAL` | /ɦ/ → [ɦ̃], before ⟨e⟩ ⟨eh⟩ ⟨i⟩ ⟨ih⟩ ⟨o⟩ ⟨u⟩ ⟨uh⟩ ⟨ä⟩ and 55 more | ⟨hi⟩ [ɦ̃ĩ˧] | - |
| `NMY_N_UVULAR` | /n/ → [ɴ], before ⟨q⟩ ⟨qh⟩ ⟨gh⟩ ⟨xr⟩ | - | - |
| `NMY_N_VELAR` | /n/ → [ŋ], before ⟨k⟩ ⟨kh⟩ | - | - |
| `NMY_Y_LABIALISED` | /j/ → [ɥ], before ⟨ü⟩ ⟨ü̂⟩ ⟨ü̆⟩ ⟨ü̑⟩ ⟨ǖ⟩ ⟨ǘ⟩ ⟨ǜ⟩ | ⟨yǘqhô⟩ [ɥy˧˥qʰo˥] | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "nmy")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Najdi Arabic](ars-SA.md) · [Home](../index.md) · [Nanai →](gld.md)
