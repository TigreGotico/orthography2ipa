# Arabic (`ar`)

<!-- atlas:summary begin -->
Arabic is a Central Semitic language, written in the Arabic script. Glottolog places it in 25 countries. The `ar` spec is at the research tier. It cites 5 sources and has 5 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ar` |
| Aliases | `ara` |
| ISO 639-3 | [ara](https://iso639-3.sil.org/code/ara), Arabic |
| Glottolog | [stan1318](https://glottolog.org/resource/languoid/id/stan1318), Standard Arabic |
| Wikipedia | [Arabic](https://en.wikipedia.org/wiki/Arabic) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Semitic > Central Semitic](by-family.md#afro-asiatic--semitic--central-semitic) |
| Region | [Eurasia](by-region.md#eurasia) > [Algeria](by-region.md#algeria), [Bahrain](by-region.md#bahrain), [Chad](by-region.md#chad), [Comoros](by-region.md#comoros), [Djibouti](by-region.md#djibouti), [Egypt](by-region.md#egypt), [Eritrea](by-region.md#eritrea), [Iraq](by-region.md#iraq) and 17 more |
| Script | [Arabic](by-script.md#arabic) (abjad) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1400, living |
| Parent | [Proto-Arabic (Old Arabic)](https://tigregotico.github.io/orthography2ipa/#xpa) `xpa` |
| Child lects | [Arabic (Buckwalter transliteration)](https://tigregotico.github.io/orthography2ipa/#ar-Latn-x-buckwalt) `ar-Latn-x-buckwalt`, [Maltese](https://tigregotico.github.io/orthography2ipa/#mt) `mt` |
| Explorer | [`ar` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ar) |
| Spec file | [`ar.json`](../../orthography2ipa/data/ar.json) |
<!-- atlas:header end -->

## Overview

The `ar` spec transcribes Modern Standard Arabic (MSA). It takes its grapheme and allophone tables from Classical Arabic (`arb`) through `graphemes_base` and `allophones_base`, and it overrides a small set of entries at the leaf. The main override is ض: MSA reads it as the emphatic stop [dˤ], while `arb` keeps the Classical lateral fricative [ɮˤ] (Watson 2002).

`ar` is also the grapheme base of every spoken Arabic spec. The three regional nodes `ar-x-mashriqi`, `ar-x-peninsul` and `ar-x-maghrebi` set `graphemes_base` to `ar`, so a change to a bare-letter reading here moves every dialect. The dialect specs have their own page: [Arabic dialects](ar-dialects.md).

## Input contract: fully diacritized text

The spec expects fully vocalised input, with every short vowel, sukūn, shadda and tanwīn written. Most written MSA leaves these marks out, except in the Quran, in children's books and in teaching material. The spec has no diacritic-restoration step. On a bare consonant skeleton it cannot supply the short vowels, and it cannot supply a geminate that no shadda marks.

On undiacritized input the spec keeps a vowel where it can. The hamza carriers أ and إ fall back to `ʔa` and `ʔi` when no harakat follows them, and ا falls back to the long vowel `aː`. The glides ي and و read as long vowels word-finally and as the consonants `j` and `w` elsewhere. A bare skeleton such as مكتوب therefore comes out without its long vowel:

```python
>>> import orthography2ipa
>>> orthography2ipa.transcribe("مكتوب", "ar")
'ˈmktwb'
```

The medial default is the largest single source of error on undiacritized text. The [error analysis](#error-analysis-what-the-remaining-per-is-made-of) below explains why the default stays as it is.

## Normalisation before tokenisation

Two Arabic-script transforms in `orthography2ipa/phonetok.py` run before the grapheme table sees the text. Both apply to every spec that reads Arabic script.

### Presentation forms and the lam-alif ligatures

The function `_decompose_arabic_presentation_forms` maps two Unicode blocks to their canonical letters: Presentation Forms-A (U+FB50 to U+FDFF) and Presentation Forms-B (U+FE70 to U+FEFF). These blocks hold contextual glyph variants and ligatures. The important ones are the four lam-alif ligatures ﻻ ﻷ ﻵ ﻹ, which decompose to ل followed by ا, أ, آ or إ. The grapheme table holds only canonical letters, so an undecomposed ligature would match nothing.

```python
>>> orthography2ipa.transcribe("ﻻ", "ar")
'ˈlaː'
```

The transform touches only the codepoints of those two blocks. A global NFKC would also fold Latin ligatures and full-width forms, so the engine does not use one.

### Gemination: shadda

A consonant with shadda (U+0651) is a geminate, and this holds for every consonant, the glides ي and و included (Ryding 2005, ch. 2, pp. 15-16, and Watson 2002). The function `_expand_arabic_gemination` doubles the base consonant and drops the shadda, so the grapheme table sees two ordinary consonant slots. It accepts both orders of the mark cluster: consonant, shadda, harakat, and consonant, harakat, shadda. The two orders render alike, and NFC does not reorder them.

```python
>>> orthography2ipa.transcribe("عَمَّ", "ar")
'ˈʕamma'
>>> orthography2ipa.transcribe("عُيِّنَ", "ar")
'ˈʕujjina'
>>> orthography2ipa.transcribe("قَوَّاس", "ar")
'qawˈwaːs'
```

## Glides, hamza carriers and matres lectionis

The `ar` leaf overrides several inherited grapheme entries so that fully vocalised words come out right. Each choice follows Ryding (2005) or Wright (1896).

| Spelling | Reading | Example | Source |
|:--|:--|:--|:--|
| glide + fatḥa, يَ وَ | onset /ja/ /wa/ | يَوم → `ˈjawm` | Ryding 2005, pp. 15-16, 29-30 |
| fatḥa + quiescent glide, ـَي ـَو | diphthong /aj/ /aw/ | بَيْت → `ˈbajt` | Ryding 2005, pp. 29-30 |
| hamza carrier before a written vowel, أ إ | bare /ʔ/, the vowel from the harakat | إِيْمَان → `ʔiːˈmaːn` | Ryding 2005, p. 16 |
| word-final ي و | long vowel first, glide second | يُصَلِّي → `jʊˈsˤɑlliː` | Ryding 2005, pp. 25-27 |
| fatḥa + alif maqṣūra, ـَى | one long [aː] | حَتَّى → `ˈħattaː` | Wright 1896, Vol. I, Part First, and Ryding 2005, pp. 25-27 |
| sukūn consonant + ي و | glide /j/ /w/ | رَمْي → `ˈramj` | Wright 1896, Vol. I, Part First, and Ryding 2005, pp. 25-27, 29-30 |
| ة after a harakat | nothing, the fatḥa gives the /a/ | مَدْرَسَة → `ˈmadrasa` | Ryding 2005, §2.3.2 |
| ة with its own vowel | /t/ | مَدِينَةُ الطِّفْل → `maˈdiːnatu tˤˈtˤɪfl` | Ryding 2005, §2.3.2 |

The sukūn rule matters most for the long-vowel preference at word end. A long /iː/ or /uː/ is spelt with its homorganic short vowel, as in ⟨ـِي⟩ and ⟨ـُو⟩. A consonant with sukūn is vowelless, so a glide after it is a consonant. The digraphs ⟨ـْي⟩ and ⟨ـْو⟩ in `arb` read /j/ and /w/, which keeps ظَبْي as `ˈðˤɑbj` and دُنْيَا as `ˈdunjaː`. They need the written sukūn, so they do not touch an undiacritized word such as في, which stays `ˈfiː`.

Four `AR_GLIDE_*` allophone rules on `ar` correct the greedy ⟨ـِي⟩ and ⟨ـُو⟩ digraphs. A glide before a vowel, or before its own geminate copy, keeps its consonantal value. The nisba suffixes therefore read /-ijj/ and /-ijja/: مِصْرِيّ gives `mɪsˤˈrijj` and حُرِّيَّة gives `ħurˈrijja`.

## The definite article: sun letters and hamzat al-wasl

The lām of the article ال assimilates to a following coronal "sun letter" (ت ث د ذ ر ز س ش ص ض ط ظ ل ن). Before a "moon letter" it stays /l/. The `arb` grapheme table carries this as digraphs: the article followed by a doubled sun letter, such as ⟨الشش⟩ → `aʃʃ`. Fully vocalised text writes a shadda on the sun letter. The gemination transform doubles the letter, and the digraph then matches. The `ar` leaf adds the ض forms of these digraphs, because it reads ض as [dˤ].

```python
>>> orthography2ipa.transcribe("اَلشَّمْس", "ar")
'aʃˈʃams'
>>> orthography2ipa.transcribe("الشمس", "ar")
'ˈalʃms'
```

The second call shows the limit. Without the shadda, nothing marks the assimilation, and the article stays `al`.

The vowel of the article is a hamzat al-wasl, and it elides after a vowel-final word. The `arb` sandhi rule `AR_HAMZAT_WASL_ARTICLE` deletes the article's /a/ in that context, and `ar` inherits it unchanged. Hamzat al-qaṭʿ words start with /ʔ/, and the rule does not touch them (Ryding 2005, §2.10).

```python
>>> orthography2ipa.transcribe("فِي الشَّمْسِ", "ar")
'fiː ʃˈʃamsi'
```

At the start of a word, the `arb` allophone rule `AR_WASL_EPENTHESIS` gives a bare wasl alif before a sukūn consonant the prosthetic vowel /i/. اسْأَل therefore comes out as `ˈʔisʔal` (Wright 1896, and Ryding 2005, §2.10).

## Emphatic spreading

The emphatic (pharyngealized) consonants /tˤ dˤ sˤ ðˤ/ colour the vowels next to them, and the spreading goes in both directions (Watson 2002, ch. on emphasis, pp. 267-286, and Ryding 2005, §2). Two rule sets carry it. `arb` declares the `AR_EMPHASIS_SPREAD_*` rules for all six vowels, which give [ɑ ɑː ɪ ɪː ʊ ʊː]. `ar` adds the `AR_EMPH_BACK_*` rules for /a/ and /aː/.

```python
>>> orthography2ipa.transcribe("صَابَ", "ar")
'ˈsˤɑːba'
>>> orthography2ipa.transcribe("بَطَل", "ar")
'ˈbɑtˤɑl'
>>> orthography2ipa.transcribe("قَلْب", "ar")
'ˈqalb'
```

The rules model local spreading to the immediate neighbour only. Emphasis harmony across a whole phonological word is not modelled. The `ar` WikiPron gold is a broad transcription that writes the backed vowels as plain /a/, so it cannot reward [ɑ]. The rules stay because they are correct, and the cost on that gold is within measurement noise.

## Stress

Arabic stress is quantity-sensitive: it falls on a syllable because the syllable is heavy. The `stress` block in `ar.json` encodes the cascade from Ryding (2005, §2.3) and Watson (2002, ch. 3). A superheavy final syllable takes the stress, as in `kiˈtaːb`. Otherwise a heavy penult takes it, and otherwise the antepenult. Every example on this page shows the resulting stress mark.

## Gold benchmark

The `ar` entry of the `wikipron` dataset in `scripts/benchmark.py` is CUNY-CL/wikipron `ara_arab_broad.tsv`: Wiktionary broad IPA, crowd-curated. Wiktionary files Arabic entries under the unvocalised page title, so the input column carries no harakat while the gold IPA writes every short vowel. A spec that follows the input contract cannot recover those vowels from this input.

The `wikipron_ar_diacritized` dataset keeps the same gold IPA and restores the tashkeel on the input side with `text2tashkeel`. That dependency is optional, so CI does not reproduce this row. The `valid_ceiling` block in `ar.json` records the folded score: the spec's output scored with the short vowels removed from both sides. Reproduce it with `scripts/folded_per.py --lang ar --dataset wikipron --segments 'a i u'`. For the scores themselves, see the [scoreboard](../evaluation/generated/scoreboard.md).

### Error analysis: what the remaining PER is made of

Run `python scripts/error_analysis.py ar --dataset wikipron --limit 300` to list the phoneme confusions on the first rows of the set. Most of them follow from the undiacritized input. The spec does not tune a fallback to them, because that would fit the spec to one lexicon.

| Confusion (gold → output) | Cause | Example (gold, output) |
|:--|:--|:--|
| `a i u` → nothing | short vowels the skeleton does not write | آلموت: `alamuːt`, `ʔaːlmwt` |
| `ː` → `w`, `ː` → `j` | bare medial و ي read as a glide, gold has the long vowel | آريوس: `ʔaːrijuːs`, `ʔaːrjws` |
| `j` → nothing, `j` → `ː` | the nisba ⟨ـيّ⟩ /-ijj/ and the plain ⟨ـي⟩ /-iː/ look alike without shadda | آشوري: `ʔaːʃuːrijj`, `ʔaːʃwriː` |
| `u` → `a` | the hamza-carrier default guesses the wrong short vowel | |
| `a` → `ɑ` | correct emphatic backing that the broad gold writes as /a/ | |

The medial mater is the exception. It is not a gap in the input: a bare medial و or ي between consonants is most often the quiescent letter, which is the long vowel. A glide with its own harakat matches a separate grapheme, so by elimination the bare letter should read long. An experiment that read the bare medial mater as the long vowel improved both the plain and the diacritized WikiPron rows. Word-initial glides stayed consonantal in it, and an allophone rule restored the /aw/ /aj/ diphthongs. The experiment is not in the tree.

What blocks the change is inheritance. `ar` is the grapheme base of the whole dialect tree, so the same flip moves every lect. In the experiment it broke verified rows of the `arabic_tts` dialect gold with real errors: وَين `wajn` became `waiːn`, أَيْنَ `ʔajna` became `ʔaiːna`, and Iraqi وِيَّا `wijja` became `wiːja`. The change needs dialect overrides in the same step. It is not a one-line retune of `ar`. The cases it would move first are pinned in `tests/test_arabic_matres_lectionis.py`.

## Weak points

The engine works one word at a time, and three Arabic processes need more than that.

- A word-final ة that carries no written vowel reads as the pausal /a/. In an iḍāfa it should be /at/, and only the following word shows that.
- Pausal dropping of the case vowels needs to know where the utterance ends.
- Sun-letter assimilation on undiacritized text needs a morphological split of the attached article, which the grapheme table cannot make.

The spec reads only fully vocalised text, and most Arabic text is not vocalised. So the PER on the plain WikiPron set is much higher than on the same set with restored tashkeel (see [Datasets](#datasets) below). The [Gold benchmark](#gold-benchmark) section explains where the remaining error comes from.

The rules and this page cite Wright (1896) for the matres lectionis, the jazma and hamzat al-waṣl. The `sources` list of `ar.json` does not include that grammar, so the generated [Sources](#sources) list below leaves it out.


<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-watson2002"></a>Watson, J.C.E. (2002). *The Phonology and Morphology of Arabic*. Oxford University Press.
2. <a id="src-thelwall1990"></a>Thelwall, R. and Sa'Adeddin, M.A. (1990). *Illustrations of the IPA: Arabic*. Journal of the International Phonetic Association, 20(2), 37-39. Cited: 37-39. [phoible.org](https://phoible.org/sources/arb_thelwall1990)
3. <a id="src-holes2004"></a>Holes, C. (2004). *Modern Arabic: Structures, Functions, and Varieties*. Georgetown University Press.
4. <a id="src-versteegh2001"></a>Versteegh, K. (2001). *The Arabic Language*. Edinburgh University Press.
5. <a id="src-ryding2005"></a>Ryding, K.C. (2005). *A Reference Grammar of Modern Standard Arabic*. Cambridge University Press. Cited: 15-35.
<!-- atlas:sources end -->

### Notes on the sources

The page also cites the works below, and two Wikipedia articles as reading paths.

- Wright, W. (1896). *A Grammar of the Arabic Language*, 3rd ed., Vol. I. Cambridge University Press. Part First, "Orthography and Orthoepy", on the matres lectionis and on alif maqṣūra as a spelling of final /aː/. It also covers the jazma (sukūn) as the mark of a vowelless consonant.
- Watson, J.C.E. (2002). *The Phonology and Morphology of Arabic*. Oxford University Press.
- Ryding, K.C. (2005). *A Reference Grammar of Modern Standard Arabic*. Cambridge University Press.
- Wikipedia: [Sun and moon letters](https://en.wikipedia.org/wiki/Sun_and_moon_letters), a reading path for the article assimilation.
- Wikipedia: [Standard Arabic phonology](https://en.wikipedia.org/wiki/Standard_Arabic_phonology), a reading path for the ض merger.

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ar` | gold | crowd-scraped | CC BY-SA | 14268 | 0.3139 | yes |
| `wikipron_ar_diacritized` | `ar` | gold | crowd-scraped | CC BY-SA | 14240 | 0.1721 | yes |
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `ar` | generated | machine-generated | MIT, each file its own | 857160 | 0.3774 | yes |
| `arabic_tts` | `ar` | silver | llm-corrected | - | 20 | 0.0707 | no |
| `gold20_arabic` ([Salesteq/arabic-dialects-gold20](https://huggingface.co/datasets/Salesteq/arabic-dialects-gold20)) | `ar` | silver | llm-corrected | - | 20 | 0.0707 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 216 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b |  |  | d dˤ t tˤ |  |  | k | q |  | ʔ |
| Affricate |  |  |  |  | dʒ |  |  |  |  |  |
| Nasal | m |  |  | n |  |  | ŋ |  |  |  |
| Trill |  |  |  | r |  |  |  |  |  |  |
| Fricative |  | f | ð ðˤ θ | s sˤ z | ʃ |  | x ɣ |  | ħ ʕ | h |
| Lateral fricative |  |  |  | ɮˤ |  |  |  |  |  |  |
| Approximant |  |  |  |  |  | j |  |  |  |  |
| Lateral approximant |  |  |  | l ɫ |  |  |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː |
| Near-close | ɪ ɪː | ʊ ʊː |
| Near-open | æ |  |
| Open | a aː | ɑ ɑː |

Sequences that the spec writes as one unit: [add] [adˤdˤ] [aj] [aja] [ajaː] [aji] [ajj] [aju] [al] [all] [allaːh] [an] [ann] [arr] [ass] [asˤsˤ] [at] [att] [atˤtˤ] [aw] [awa] [awaː] [awi] [awu] [aww] [azz] [aðð] [aðˤðˤ] [aʃʃ] [aːj] [aθθ] [bi] [bidd] [bidˤdˤ] [bil] [bill] [binn] [birr] [biss] [bisˤsˤ], and 133 more.
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
| ⟨الثث⟩ | [aθθ] |  |
| ⟨الدد⟩ | [add] |  |
| ⟨الذذ⟩ | [aðð] |  |
| ⟨الرر⟩ | [arr] |  |
| ⟨الزز⟩ | [azz] |  |
| ⟨السس⟩ | [ass] |  |
| ⟨الشش⟩ | [aʃʃ] |  |
| ⟨الصص⟩ | [asˤsˤ] |  |
| ⟨الضض⟩ | [adˤdˤ] |  |
| ⟨الطط⟩ | [atˤtˤ] |  |
| ⟨الظظ⟩ | [aðˤðˤ] |  |
| ⟨اللل⟩ | [all] |  |
| ⟨اللله⟩ | [allaːh] |  |
| ⟨الله⟩ | [allaːh] |  |
| ⟨النن⟩ | [ann] |  |
| ⟨اً⟩ | [an] |  |
| ⟨اَ⟩ | [a] |  |
| ⟨اَل⟩ | [al] |  |
| ⟨اَلتت⟩ | [att] |  |
| ⟨اَلثث⟩ | [aθθ] |  |
| ⟨اَلدد⟩ | [add] |  |
| ⟨اَلذذ⟩ | [aðð] |  |
| ⟨اَلرر⟩ | [arr] |  |
| ⟨اَلزز⟩ | [azz] |  |
| ⟨اَلسس⟩ | [ass] |  |
| ⟨اَلشش⟩ | [aʃʃ] |  |
| ⟨اَلصص⟩ | [asˤsˤ] |  |
| ⟨اَلضض⟩ | [adˤdˤ] |  |
| ⟨اَلطط⟩ | [atˤtˤ] |  |
| ⟨اَلظظ⟩ | [aðˤðˤ] |  |
| ⟨اَللل⟩ | [all] |  |
| ⟨اَلنن⟩ | [ann] |  |
| ⟨اِل⟩ | [il] |  |
| ⟨اِلتت⟩ | [itt] |  |
| ⟨اِلثث⟩ | [iθθ] |  |
| ⟨اِلدد⟩ | [idd] |  |
| ⟨اِلذذ⟩ | [iðð] |  |
| ⟨اِلرر⟩ | [irr] |  |
| ⟨اِلزز⟩ | [izz] |  |
| ⟨اِلسس⟩ | [iss] |  |
| ⟨اِلشش⟩ | [iʃʃ] |  |
| ⟨اِلصص⟩ | [isˤsˤ] |  |
| ⟨اِلضض⟩ | [idˤdˤ] |  |
| ⟨اِلطط⟩ | [itˤtˤ] |  |
| ⟨اِلظظ⟩ | [iðˤðˤ] |  |
| ⟨اِللل⟩ | [ill] |  |
| ⟨اِلنن⟩ | [inn] |  |
| ⟨ب⟩ | [b] |  |
| ⟨بِال⟩ | [bil] |  |
| ⟨بِالتت⟩ | [bitt] |  |
| ⟨بِالثث⟩ | [biθθ] |  |
| ⟨بِالدد⟩ | [bidd] |  |
| ⟨بِالذذ⟩ | [biðð] |  |
| ⟨بِالرر⟩ | [birr] |  |
| ⟨بِالزز⟩ | [bizz] |  |
| ⟨بِالسس⟩ | [biss] |  |
| ⟨بِالشش⟩ | [biʃʃ] |  |
| ⟨بِالصص⟩ | [bisˤsˤ] |  |
| ⟨بِالضض⟩ | [bidˤdˤ] |  |
| ⟨بِالطط⟩ | [bitˤtˤ] |  |
| ⟨بِالظظ⟩ | [biðˤðˤ] |  |
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
| ⟨ث⟩ | [θ] |  |
| ⟨ج⟩ | [dʒ] |  |
| ⟨ح⟩ | [ħ] |  |
| ⟨خ⟩ | [x] |  |
| ⟨د⟩ | [d] |  |
| ⟨ذ⟩ | [ð] |  |
| ⟨ر⟩ | [r] |  |
| ⟨ز⟩ | [z] |  |
| ⟨س⟩ | [s] |  |
| ⟨ش⟩ | [ʃ] |  |
| ⟨ص⟩ | [sˤ] |  |
| ⟨ض⟩ | [dˤ] |  |
| ⟨ط⟩ | [tˤ] |  |
| ⟨ظ⟩ | [ðˤ] |  |
| ⟨ع⟩ | [ʕ] |  |
| ⟨غ⟩ | [ɣ] |  |
| ⟨ـ⟩ | ∅ |  |
| ⟨ف⟩ | [f] |  |
| ⟨فَال⟩ | [fal] |  |
| ⟨فَالتت⟩ | [fatt] |  |
| ⟨فَالثث⟩ | [faθθ] |  |
| ⟨فَالدد⟩ | [fadd] |  |
| ⟨فَالذذ⟩ | [faðð] |  |
| ⟨فَالرر⟩ | [farr] |  |
| ⟨فَالزز⟩ | [fazz] |  |
| ⟨فَالسس⟩ | [fass] |  |
| ⟨فَالشش⟩ | [faʃʃ] |  |
| ⟨فَالصص⟩ | [fasˤsˤ] |  |
| ⟨فَالضض⟩ | [fadˤdˤ] |  |
| ⟨فَالطط⟩ | [fatˤtˤ] |  |
| ⟨فَالظظ⟩ | [faðˤðˤ] |  |
| ⟨فَاللل⟩ | [fall] |  |
| ⟨فَالنن⟩ | [fann] |  |
| ⟨فَٱ⟩ | [fa] |  |
| ⟨ق⟩ | [q] |  |
| ⟨ك⟩ | [k] |  |
| ⟨كَال⟩ | [kal] |  |
| ⟨كَالتت⟩ | [katt] |  |
| ⟨كَالثث⟩ | [kaθθ] |  |
| ⟨كَالدد⟩ | [kadd] |  |
| ⟨كَالذذ⟩ | [kaðð] |  |
| ⟨كَالرر⟩ | [karr] |  |
| ⟨كَالزز⟩ | [kazz] |  |
| ⟨كَالسس⟩ | [kass] |  |
| ⟨كَالشش⟩ | [kaʃʃ] |  |
| ⟨كَالصص⟩ | [kasˤsˤ] |  |
| ⟨كَالضض⟩ | [kadˤdˤ] |  |
| ⟨كَالطط⟩ | [katˤtˤ] |  |
| ⟨كَالظظ⟩ | [kaðˤðˤ] |  |
| ⟨كَاللل⟩ | [kall] |  |
| ⟨كَالنن⟩ | [kann] |  |
| ⟨كَٱ⟩ | [ka] |  |
| ⟨ل⟩ | [l] |  |
| ⟨لِل⟩ | [lil] |  |
| ⟨لِلتت⟩ | [litt] |  |
| ⟨لِلثث⟩ | [liθθ] |  |
| ⟨لِلدد⟩ | [lidd] |  |
| ⟨لِلذذ⟩ | [liðð] |  |
| ⟨لِلرر⟩ | [lirr] |  |
| ⟨لِلزز⟩ | [lizz] |  |
| ⟨لِلسس⟩ | [liss] |  |
| ⟨لِلشش⟩ | [liʃʃ] |  |
| ⟨لِلصص⟩ | [lisˤsˤ] |  |
| ⟨لِلضض⟩ | [lidˤdˤ] |  |
| ⟨لِلطط⟩ | [litˤtˤ] |  |
| ⟨لِلظظ⟩ | [liðˤðˤ] |  |
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
| ⟨وَالثث⟩ | [waθθ] |  |
| ⟨وَالدد⟩ | [wadd] |  |
| ⟨وَالذذ⟩ | [waðð] |  |
| ⟨وَالرر⟩ | [warr] |  |
| ⟨وَالزز⟩ | [wazz] |  |
| ⟨وَالسس⟩ | [wass] |  |
| ⟨وَالشش⟩ | [waʃʃ] |  |
| ⟨وَالصص⟩ | [wasˤsˤ] |  |
| ⟨وَالضض⟩ | [wadˤdˤ] |  |
| ⟨وَالطط⟩ | [watˤtˤ] |  |
| ⟨وَالظظ⟩ | [waðˤðˤ] |  |
| ⟨وَاللل⟩ | [wall] |  |
| ⟨وَالنن⟩ | [wann] |  |
| ⟨وَٱ⟩ | [wa] |  |
| ⟨وُ⟩ | [wu] |  |
| ⟨وِال⟩ | [wil] |  |
| ⟨وِالتت⟩ | [witt] |  |
| ⟨وِالثث⟩ | [wiθθ] |  |
| ⟨وِالدد⟩ | [widd] |  |
| ⟨وِالذذ⟩ | [wiðð] |  |
| ⟨وِالرر⟩ | [wirr] |  |
| ⟨وِالزز⟩ | [wizz] |  |
| ⟨وِالسس⟩ | [wiss] |  |
| ⟨وِالشش⟩ | [wiʃʃ] |  |
| ⟨وِالصص⟩ | [wisˤsˤ] |  |
| ⟨وِالضض⟩ | [widˤdˤ] |  |
| ⟨وِالطط⟩ | [witˤtˤ] |  |
| ⟨وِالظظ⟩ | [wiðˤðˤ] |  |
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
| ⟨ک⟩ | [k] |  |
| ⟨ڪ⟩ | [k] |  |
| ⟨ھ⟩ | [h] |  |
| ⟨ی⟩ | [j] [iː] |  |

Stress falls on the antepenult by default. Stress is sensitive to syllable weight.

Whole-word exceptions (25): ⟨الله⟩ [ɑɫɫɑːh], ⟨اللَّه⟩ [ɑɫɫɑːh], ⟨اللَّهَ⟩ [ɑɫɫɑːha], ⟨اللَّهُ⟩ [ɑɫɫɑːhu], ⟨اللَّهِ⟩ [ɑɫɫɑːhi], ⟨اللّٰه⟩ [ɑɫɫɑːh], ⟨ذلك⟩ [ðaːlika], ⟨ذَلِك⟩ [ðaːlik], ⟨ذَلِكَ⟩ [ðaːlika], ⟨لكن⟩ [laːkin], ⟨لكنّ⟩ [laːkinna], ⟨لَكِن⟩ [laːkin], ⟨لَكِنَّ⟩ [laːkinna], ⟨لَكِنْ⟩ [laːkin], ⟨هذا⟩ [haːðaː], ⟨هذه⟩ [haːðihi], ⟨هذي⟩ [haːðiː], ⟨هَذَا⟩ [haːðaː], ⟨هَذِه⟩ [haːðih], ⟨هَذِهِ⟩ [haːðihi], ⟨هَذِي⟩ [haːðiː], ⟨هٰذَا⟩ [haːðaː], ⟨والله⟩ [waɫɫɑːh], ⟨وَالله⟩ [waɫɫɑːh], ⟨وَاللَّه⟩ [waɫɫɑːh].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 21 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `AR_WASL_EPENTHESIS` | /ʔ/ → [ʔi], word-initially, before a consonant | ⟨اسْأَل⟩ [ʔisʔal] | [Ryding 2005](#src-ryding2005) |
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
| `AR_GLIDE_YA_BEFORE_GEMINATE` | /iː/ → [ij], before [iː] | ⟨مِصْرِيّ⟩ [misˤrijj] | [Ryding 2005](#src-ryding2005) |
| `AR_GLIDE_YA_GEMINATE_COPY` | /iː/ → [j], after [iː] | ⟨ends⟩ [ijj] | [Ryding 2005](#src-ryding2005) |
| `AR_GLIDE_YA_CONSONANTAL` | /iː/ → [ij], before [j] [ja] [ji] [ju] [jaː] [jiː] [juː] | ⟨ـِيّ⟩ [-ijj] | [Watson 2002](#src-watson2002), [Ryding 2005](#src-ryding2005) |
| `AR_GLIDE_WAW_CONSONANTAL` | /uː/ → [uw], before [w] [wa] [wi] [wu] [waː] [wiː] [wuː] | ⟨أُبُوَّة⟩ [ʔubuwwa] | - |

The spec applies 1 rules across a word boundary. The contexts are regular expressions on the IPA of the two words.

| Rule | End of word | Start of next word | Change | Example | Cited |
|:--|:--|:--|:--|:--|:--|
| `AR_HAMZAT_WASL_ARTICLE` | `[aiueoɑæə]ː?$` | `^[aɑ](?=[^aeiouɑɐæɪʊəɛɔː])` | right ∅ | - | [Ryding 2005](#src-ryding2005) |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="كِتَاب|مَكْتُوب|مكتوب|اَلشَّمْسُ|اَلْقَمَرُ|فِي الشَّمْسِ|اسْأَل|مِصْرِيّ|صَبَاح|طَبِيب|قَالَ|حَتَّى" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ar")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| كِتَاب | [kiˈtaːb] |
| مَكْتُوب | [makˈtuːb] |
| مكتوب | [ˈmktwb] |
| اَلشَّمْسُ | [aʃˈʃamsu] |
| اَلْقَمَرُ | [alˈqamaru] |
| فِي الشَّمْسِ | [fiː ʃˈʃamsi] |
| اسْأَل | [ˈʔisʔal] |
| مِصْرِيّ | [mɪsˤˈrijj] |
| صَبَاح | [sˤɑˈbaːħ] |
| طَبِيب | [tˤɑˈbiːb] |
| قَالَ | [ˈqaːla] |
| حَتَّى | [ˈħattaː] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

| Repository | What it does with this spec |
|:--|:--|
| [arbtok](https://github.com/TigreGotico/arbtok) | Arabic text to IPA, with tashkeel restoration that knows the dialect. |
<!-- atlas:related end -->

---
[← Castilian Spanish](es-ES.md) · [Home](../index.md) · [Mirandese →](mwl.md)
