# Proto-Mashriqi Arabic (`ar-x-mashriqi`)

<!-- atlas:summary begin -->
Proto-Mashriqi Arabic is a Central Semitic variety, written in the Arabic script. Glottolog places it in the Eurasia macroarea. The `ar-x-mashriqi` spec is at the research tier. It cites 4 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ar-x-mashriqi` |
| ISO 639-3 | [ara](https://iso639-3.sil.org/code/ara), Arabic |
| Wikipedia | [Mesopotamian Arabic](https://en.wikipedia.org/wiki/Mesopotamian_Arabic) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Semitic > Central Semitic](by-family.md#afro-asiatic--semitic--central-semitic) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Arabic](by-script.md#arabic) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1000, living |
| Ancestor | [Classical Arabic](https://tigregotico.github.io/orthography2ipa/#arb) `arb` |
| Child lects | 5, see [Related lects](#related-lects) |
| Explorer | [`ar-x-mashriqi` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ar-x-mashriqi) |
| Spec file | [`ar-x-mashriqi.json`](../../orthography2ipa/data/ar-x-mashriqi.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Proto-Mashriqi (Eastern) Arabic, GROUPING NODE (glue node) for Egyptian (arz-EG), Sudanese (apd-SD), Chadian/Nigerian West-Sudanic (shu-TD → shu-NG) and the Levantine subtree (apc → apc-SY/apc-LB/apc-JO/apc-PS), plus Mesopotamian acm-IQ/ar-IQ-x-qeltu.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 2000 to 2014. [Sources](#sources) lists them. The spec file writes 43 of the 250 spellings of its letter table and takes the other 207 from [Arabic](ar.md) `ar`.

The [spec file](../../orthography2ipa/data/ar-x-mashriqi.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `ar-x-mashriqi` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Chadian Arabic](shu-TD.md) `shu-TD`: Chad, research tier
- [Egyptian Arabic (Cairene)](arz-EG.md) `arz-EG`: Egypt, research tier
- [Iraqi Arabic (Baghdad / gilit)](acm-IQ.md) `acm-IQ`: Iraq, research tier
- [Proto-Levantine Arabic](apc.md) `apc`: Israel, Lebanon, Syria, Türkiye, research tier
- [Sudanese Arabic](apd-SD.md) `apd-SD`: Sudan, research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-watson2002"></a>Watson, J.C.E. (2002). *The Phonology and Morphology of Arabic*. Oxford University Press. Cited: 9, 12, 16-17.
2. <a id="src-versteegh2014"></a>Versteegh, K. (2014). *The Arabic Language (2nd edition)*. Edinburgh University Press.
3. <a id="src-holes2004"></a>Holes, C. (2004). *Modern Arabic: Structures, Functions, and Varieties*. Georgetown University Press.
4. <a id="src-brustad2000"></a>Brustad, K. (2000). *The Syntax of Spoken Arabic: A Comparative Study of Moroccan, Egyptian, Syrian, and Kuwaiti Dialects*. Georgetown University Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `arabic_tts` | `ar-x-mashriqi` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.0568 | no |
| `gold20_arabic` ([TigreGotico/arabic-dialects-gold20](https://huggingface.co/datasets/TigreGotico/arabic-dialects-gold20)) | `ar-x-mashriqi` | silver | llm-corrected | CC BY 4.0 | 20 | 0.0550 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 219 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d dˤ t tˤ |  |  | k ɡ | q |  | ʔ |
| Affricate |  |  |  |  | dʒ tʃ |  |  |  |  |  |
| Nasal | m |  |  | n |  |  | ŋ |  |  |  |
| Trill |  |  |  | r |  |  |  |  |  |  |
| Fricative |  | f v | ð θ | s sˤ z zˤ | ʃ |  | x ɣ |  | ħ ʕ | h |
| Approximant |  |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  |  | l ɫ |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Near-close | ɪ ɪː | ʊ ʊː |
| Near-open | æ |  |
| Open | a aː | ɑ ɑː |

Sequences that the spec writes as one unit: [add] [adˤdˤ] [aj] [aja] [ajaː] [aji] [ajj] [aju] [al] [all] [allaːh] [an] [ann] [arr] [ass] [asˤsˤ] [at] [att] [atˤtˤ] [aw] [awa] [awaː] [awi] [awu] [aww] [azz] [azˤzˤ] [aðð] [aʃʃ] [aːj] [aθθ] [bi] [bidd] [bidˤdˤ] [bil] [bill] [binn] [birr] [biss] [bisˤsˤ], and 133 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ء⟩ | [ʔ] |  |
| ⟨آ⟩ | [ʔaː] |  |
| ⟨أ⟩ | [ʔa] | before vowel [ʔ] · default [ʔa] |
| ⟨أَ⟩ | [ʔa] |  |
| ⟨أُ⟩ | [ʔu] |  |
| ⟨أُو⟩ | [ʔuː] |  |
| ⟨ؤ⟩ | [ʔ] |  |
| ⟨إ⟩ | [ʔi] | before vowel [ʔ] · default [ʔi] |
| ⟨إِ⟩ | [ʔi] |  |
| ⟨إِي⟩ | [ʔiː] |  |
| ⟨ئ⟩ | [ʔ] |  |
| ⟨ا⟩ | [ʔ] [aː] | default [aː] [ʔ] · word initial [ʔ] [aː] |
| ⟨ال⟩ | [al] [a] |  |
| ⟨التت⟩ | [att] |  |
| ⟨الثث⟩ | [att] [aθθ] |  |
| ⟨الدد⟩ | [add] |  |
| ⟨الذذ⟩ | [add] [aðð] |  |
| ⟨الرر⟩ | [arr] |  |
| ⟨الزز⟩ | [azz] |  |
| ⟨السس⟩ | [ass] |  |
| ⟨الشش⟩ | [aʃʃ] |  |
| ⟨الصص⟩ | [asˤsˤ] |  |
| ⟨الضض⟩ | [adˤdˤ] |  |
| ⟨الطط⟩ | [atˤtˤ] |  |
| ⟨الظظ⟩ | [adˤdˤ] [azˤzˤ] |  |
| ⟨اللل⟩ | [all] |  |
| ⟨اللله⟩ | [allaːh] |  |
| ⟨الله⟩ | [allaːh] |  |
| ⟨النن⟩ | [ann] |  |
| ⟨اً⟩ | [an] |  |
| ⟨اَ⟩ | [a] |  |
| ⟨اَل⟩ | [al] |  |
| ⟨اَلتت⟩ | [att] |  |
| ⟨اَلثث⟩ | [att] [aθθ] |  |
| ⟨اَلدد⟩ | [add] |  |
| ⟨اَلذذ⟩ | [add] [aðð] |  |
| ⟨اَلرر⟩ | [arr] |  |
| ⟨اَلزز⟩ | [azz] |  |
| ⟨اَلسس⟩ | [ass] |  |
| ⟨اَلشش⟩ | [aʃʃ] |  |
| ⟨اَلصص⟩ | [asˤsˤ] |  |
| ⟨اَلضض⟩ | [adˤdˤ] |  |
| ⟨اَلطط⟩ | [atˤtˤ] |  |
| ⟨اَلظظ⟩ | [adˤdˤ] [azˤzˤ] |  |
| ⟨اَللل⟩ | [all] |  |
| ⟨اَلنن⟩ | [ann] |  |
| ⟨اِل⟩ | [il] |  |
| ⟨اِلتت⟩ | [itt] |  |
| ⟨اِلثث⟩ | [itt] [iθθ] |  |
| ⟨اِلدد⟩ | [idd] |  |
| ⟨اِلذذ⟩ | [idd] [iðð] |  |
| ⟨اِلرر⟩ | [irr] |  |
| ⟨اِلزز⟩ | [izz] |  |
| ⟨اِلسس⟩ | [iss] |  |
| ⟨اِلشش⟩ | [iʃʃ] |  |
| ⟨اِلصص⟩ | [isˤsˤ] |  |
| ⟨اِلضض⟩ | [idˤdˤ] |  |
| ⟨اِلطط⟩ | [itˤtˤ] |  |
| ⟨اِلظظ⟩ | [idˤdˤ] [izˤzˤ] |  |
| ⟨اِللل⟩ | [ill] |  |
| ⟨اِلنن⟩ | [inn] |  |
| ⟨ب⟩ | [b] |  |
| ⟨بِال⟩ | [bil] |  |
| ⟨بِالتت⟩ | [bitt] |  |
| ⟨بِالثث⟩ | [bitt] [biθθ] |  |
| ⟨بِالدد⟩ | [bidd] |  |
| ⟨بِالذذ⟩ | [bidd] [biðð] |  |
| ⟨بِالرر⟩ | [birr] |  |
| ⟨بِالزز⟩ | [bizz] |  |
| ⟨بِالسس⟩ | [biss] |  |
| ⟨بِالشش⟩ | [biʃʃ] |  |
| ⟨بِالصص⟩ | [bisˤsˤ] |  |
| ⟨بِالضض⟩ | [bidˤdˤ] |  |
| ⟨بِالطط⟩ | [bitˤtˤ] |  |
| ⟨بِالظظ⟩ | [bidˤdˤ] [bizˤzˤ] |  |
| ⟨بِاللل⟩ | [bill] |  |
| ⟨بِالنن⟩ | [binn] |  |
| ⟨بِٱ⟩ | [bi] |  |
| ⟨ة⟩ | [a] [at] | after vowel ∅ · default [a] [at] |
| ⟨ةً⟩ | [tan] |  |
| ⟨ةٌ⟩ | [tun] |  |
| ⟨ةٍ⟩ | [tin] |  |
| ⟨ةَ⟩ | [ta] |  |
| ⟨ةُ⟩ | [tu] |  |
| ⟨ةِ⟩ | [ti] |  |
| ⟨ت⟩ | [t] |  |
| ⟨ث⟩ | [t] [θ] |  |
| ⟨ج⟩ | [dʒ] |  |
| ⟨ح⟩ | [ħ] |  |
| ⟨خ⟩ | [x] |  |
| ⟨د⟩ | [d] |  |
| ⟨ذ⟩ | [d] [ð] |  |
| ⟨ر⟩ | [r] |  |
| ⟨ز⟩ | [z] |  |
| ⟨س⟩ | [s] |  |
| ⟨ش⟩ | [ʃ] |  |
| ⟨ص⟩ | [sˤ] |  |
| ⟨ض⟩ | [dˤ] |  |
| ⟨ط⟩ | [tˤ] |  |
| ⟨ظ⟩ | [dˤ] [zˤ] |  |
| ⟨ع⟩ | [ʕ] |  |
| ⟨غ⟩ | [ɣ] |  |
| ⟨ـ⟩ | ∅ |  |
| ⟨ف⟩ | [f] |  |
| ⟨فَال⟩ | [fal] |  |
| ⟨فَالتت⟩ | [fatt] |  |
| ⟨فَالثث⟩ | [fatt] [faθθ] |  |
| ⟨فَالدد⟩ | [fadd] |  |
| ⟨فَالذذ⟩ | [fadd] [faðð] |  |
| ⟨فَالرر⟩ | [farr] |  |
| ⟨فَالزز⟩ | [fazz] |  |
| ⟨فَالسس⟩ | [fass] |  |
| ⟨فَالشش⟩ | [faʃʃ] |  |
| ⟨فَالصص⟩ | [fasˤsˤ] |  |
| ⟨فَالضض⟩ | [fadˤdˤ] |  |
| ⟨فَالطط⟩ | [fatˤtˤ] |  |
| ⟨فَالظظ⟩ | [fadˤdˤ] [fazˤzˤ] |  |
| ⟨فَاللل⟩ | [fall] |  |
| ⟨فَالنن⟩ | [fann] |  |
| ⟨فَٱ⟩ | [fa] |  |
| ⟨ق⟩ | [q] |  |
| ⟨ك⟩ | [k] |  |
| ⟨كَال⟩ | [kal] |  |
| ⟨كَالتت⟩ | [katt] |  |
| ⟨كَالثث⟩ | [katt] [kaθθ] |  |
| ⟨كَالدد⟩ | [kadd] |  |
| ⟨كَالذذ⟩ | [kadd] [kaðð] |  |
| ⟨كَالرر⟩ | [karr] |  |
| ⟨كَالزز⟩ | [kazz] |  |
| ⟨كَالسس⟩ | [kass] |  |
| ⟨كَالشش⟩ | [kaʃʃ] |  |
| ⟨كَالصص⟩ | [kasˤsˤ] |  |
| ⟨كَالضض⟩ | [kadˤdˤ] |  |
| ⟨كَالطط⟩ | [katˤtˤ] |  |
| ⟨كَالظظ⟩ | [kadˤdˤ] [kazˤzˤ] |  |
| ⟨كَاللل⟩ | [kall] |  |
| ⟨كَالنن⟩ | [kann] |  |
| ⟨كَٱ⟩ | [ka] |  |
| ⟨ل⟩ | [l] |  |
| ⟨لِل⟩ | [lil] |  |
| ⟨لِلتت⟩ | [litt] |  |
| ⟨لِلثث⟩ | [litt] [liθθ] |  |
| ⟨لِلدد⟩ | [lidd] |  |
| ⟨لِلذذ⟩ | [lidd] [liðð] |  |
| ⟨لِلرر⟩ | [lirr] |  |
| ⟨لِلزز⟩ | [lizz] |  |
| ⟨لِلسس⟩ | [liss] |  |
| ⟨لِلشش⟩ | [liʃʃ] |  |
| ⟨لِلصص⟩ | [lisˤsˤ] |  |
| ⟨لِلضض⟩ | [lidˤdˤ] |  |
| ⟨لِلطط⟩ | [litˤtˤ] |  |
| ⟨لِلظظ⟩ | [lidˤdˤ] [lizˤzˤ] |  |
| ⟨لِللل⟩ | [lill] |  |
| ⟨لِلنن⟩ | [linn] |  |
| ⟨م⟩ | [m] |  |
| ⟨ن⟩ | [n] |  |
| ⟨ه⟩ | [h] |  |
| ⟨و⟩ | [w] [uː] | default [w] [uː] · word final [uː] [w] |
| ⟨وو⟩ | [ww] |  |
| ⟨وَ⟩ | [wa] |  |
| ⟨وَا⟩ | [waː] |  |
| ⟨وَال⟩ | [wal] |  |
| ⟨وَالتت⟩ | [watt] |  |
| ⟨وَالثث⟩ | [watt] [waθθ] |  |
| ⟨وَالدد⟩ | [wadd] |  |
| ⟨وَالذذ⟩ | [wadd] [waðð] |  |
| ⟨وَالرر⟩ | [warr] |  |
| ⟨وَالزز⟩ | [wazz] |  |
| ⟨وَالسس⟩ | [wass] |  |
| ⟨وَالشش⟩ | [waʃʃ] |  |
| ⟨وَالصص⟩ | [wasˤsˤ] |  |
| ⟨وَالضض⟩ | [wadˤdˤ] |  |
| ⟨وَالطط⟩ | [watˤtˤ] |  |
| ⟨وَالظظ⟩ | [wadˤdˤ] [wazˤzˤ] |  |
| ⟨وَاللل⟩ | [wall] |  |
| ⟨وَالنن⟩ | [wann] |  |
| ⟨وَٱ⟩ | [wa] |  |
| ⟨وُ⟩ | [wu] |  |
| ⟨وِال⟩ | [wil] |  |
| ⟨وِالتت⟩ | [witt] |  |
| ⟨وِالثث⟩ | [witt] [wiθθ] |  |
| ⟨وِالدد⟩ | [widd] |  |
| ⟨وِالذذ⟩ | [widd] [wiðð] |  |
| ⟨وِالرر⟩ | [wirr] |  |
| ⟨وِالزز⟩ | [wizz] |  |
| ⟨وِالسس⟩ | [wiss] |  |
| ⟨وِالشش⟩ | [wiʃʃ] |  |
| ⟨وِالصص⟩ | [wisˤsˤ] |  |
| ⟨وِالضض⟩ | [widˤdˤ] |  |
| ⟨وِالطط⟩ | [witˤtˤ] |  |
| ⟨وِالظظ⟩ | [widˤdˤ] [wizˤzˤ] |  |
| ⟨وِاللل⟩ | [will] |  |
| ⟨وِالنن⟩ | [winn] |  |
| ⟨وِٱ⟩ | [wi] |  |
| ⟨ى⟩ | [aː] |  |
| ⟨ي⟩ | [j] [iː] | default [j] [iː] · word final [iː] [j] |
| ⟨يي⟩ | [jj] |  |
| ⟨يَ⟩ | [ja] |  |
| ⟨يَا⟩ | [jaː] |  |
| ⟨يِ⟩ | [ji] |  |
| ⟨ً⟩ | [an] |  |
| ⟨ًا⟩ | [an] |  |
| ⟨ًى⟩ | [an] |  |
| ⟨ٌ⟩ | [un] |  |
| ⟨ٍ⟩ | [in] |  |
| ⟨َ⟩ | [a] |  |
| ⟨َا⟩ | [aː] |  |
| ⟨َاي⟩ | [aːj] |  |
| ⟨َة⟩ | [a] | before vowel [at] · default [a] |
| ⟨َو⟩ | [aw] |  |
| ⟨َوو⟩ | [aww] |  |
| ⟨َوَ⟩ | [awa] |  |
| ⟨َوَا⟩ | [awaː] |  |
| ⟨َوُ⟩ | [awu] |  |
| ⟨َوِ⟩ | [awi] |  |
| ⟨َى⟩ | [aː] |  |
| ⟨َي⟩ | [aj] |  |
| ⟨َيي⟩ | [ajj] |  |
| ⟨َيَ⟩ | [aja] |  |
| ⟨َيَا⟩ | [ajaː] |  |
| ⟨َيُ⟩ | [aju] |  |
| ⟨َيِ⟩ | [aji] |  |
| ⟨َٰ⟩ | [aː] |  |
| ⟨ُ⟩ | [u] |  |
| ⟨ُو⟩ | [uː] |  |
| ⟨ُوا⟩ | [uː] |  |
| ⟨ُوو⟩ | [uww] |  |
| ⟨ُوي⟩ | [uːj] |  |
| ⟨ُوَ⟩ | [uwa] |  |
| ⟨ُوَا⟩ | [uwaː] |  |
| ⟨ِ⟩ | [i] |  |
| ⟨ِي⟩ | [iː] |  |
| ⟨ِيي⟩ | [ijj] |  |
| ⟨ِيَ⟩ | [ija] |  |
| ⟨ِيَا⟩ | [ijaː] |  |
| ⟨ّ⟩ | [ː] |  |
| ⟨ْ⟩ | ∅ |  |
| ⟨ْو⟩ | [w] |  |
| ⟨ْي⟩ | [j] |  |
| ⟨ٰ⟩ | [aː] |  |
| ⟨ٱ⟩ | ∅ |  |
| ⟨ٱل⟩ | [al] |  |
| ⟨ٲ⟩ | [ʔa] |  |
| ⟨پ⟩ | [p] |  |
| ⟨چ⟩ | [tʃ] |  |
| ⟨ڤ⟩ | [v] |  |
| ⟨ک⟩ | [k] |  |
| ⟨ڪ⟩ | [k] |  |
| ⟨ھ⟩ | [h] |  |
| ⟨ی⟩ | [j] [iː] |  |

Stress falls on the antepenult by default. Stress is sensitive to syllable weight.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 21 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `AR_WASL_EPENTHESIS` | /ʔ/ → [ʔi], word-initially, before a consonant | ⟨اسْأَل⟩ [ʔisʔal] | Ryding 2005 |
| `AR_EMPHASIS_SPREAD_A_AFTER` | /a/ → [ɑ], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_A_BEFORE` | /a/ → [ɑ], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_AA_AFTER` | /aː/ → [ɑː], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_AA_BEFORE` | /aː/ → [ɑː], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_I_AFTER` | /i/ → [ɪ], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_I_BEFORE` | /i/ → [ɪ], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_II_AFTER` | /iː/ → [ɪː], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_II_BEFORE` | /iː/ → [ɪː], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_U_AFTER` | /u/ → [ʊ], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_U_BEFORE` | /u/ → [ʊ], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_UU_AFTER` | /uː/ → [ʊː], after an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPHASIS_SPREAD_UU_BEFORE` | /uː/ → [ʊː], before an emphatic consonant | - | [Watson 2002](#src-watson2002), Davis 1995, Card 1983 |
| `AR_EMPH_BACK_A_AFTER` | /a/ → [ɑ], after [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | [Watson 2002](#src-watson2002) |
| `AR_EMPH_BACK_A_BEFORE` | /a/ → [ɑ], before [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | [Watson 2002](#src-watson2002) |
| `AR_EMPH_BACK_AA_AFTER` | /aː/ → [ɑː], after [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | [Watson 2002](#src-watson2002) |
| `AR_EMPH_BACK_AA_BEFORE` | /aː/ → [ɑː], before [tˤ] [dˤ] [sˤ] [ðˤ] [zˤ] | - | [Watson 2002](#src-watson2002) |
| `AR_GLIDE_YA_BEFORE_GEMINATE` | /iː/ → [ij], before [iː] | ⟨مِصْرِيّ⟩ [misˤrijj] | Ryding 2005 |
| `AR_GLIDE_YA_GEMINATE_COPY` | /iː/ → [j], after [iː] | ⟨ends⟩ [ijj] | Ryding 2005 |
| `AR_GLIDE_YA_CONSONANTAL` | /iː/ → [ij], before [j] [ja] [ji] [ju] [jaː] [jiː] [juː] | ⟨ـِيّ⟩ [-ijj] | [Watson 2002](#src-watson2002), Ryding 2005 |
| `AR_GLIDE_WAW_CONSONANTAL` | /uː/ → [uw], before [w] [wa] [wi] [wu] [waː] [wiː] [wuː] | ⟨أُبُوَّة⟩ [ʔubuwwa] | - |

The spec applies 1 rules across a word boundary. The contexts are regular expressions on the IPA of the two words.

| Rule | End of word | Start of next word | Change | Example | Cited |
|:--|:--|:--|:--|:--|:--|
| `AR_HAMZAT_WASL_ARTICLE` | `[aiueoɑæə]ː?$` | `^[aɑ](?=[^aeiouɑɐæɪʊəɛɔː])` | right ∅ | - | Ryding 2005 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ar-x-mashriqi")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

| Repository | What it does with this spec |
|:--|:--|
| [arbtok](https://github.com/TigreGotico/arbtok) | Arabic text to IPA, with tashkeel restoration that knows the dialect. |
<!-- atlas:related end -->

---
[← Proto-Maghrebi Arabic](ar-x-maghrebi.md) · [Home](../index.md) · [Proto-Peninsular Arabic →](ar-x-peninsul.md)
