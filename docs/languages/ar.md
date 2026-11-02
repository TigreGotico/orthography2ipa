# Modern Standard Arabic (ar)

**Code**: `ar` | **Family**: Afro-Asiatic > Semitic > Central Semitic | **Script**: Arabic (abjad)
**Quality tier**: research | **Sources**: Wright (1896), Watson (2002), Ryding (2005)

The `ar` spec transcribes Modern Standard Arabic (MSA). It takes its grapheme and allophone tables from Classical Arabic (`arb`) through `graphemes_base` and `allophones_base`, and it overrides a small set of entries at the leaf. The main override is ض: MSA reads it as the emphatic stop [dˤ], while `arb` keeps the Classical lateral fricative [ɮˤ] (Watson 2002).

`ar` is also the grapheme base of every spoken Arabic spec. The three regional nodes `ar-x-mashriqi`, `ar-x-peninsular` and `ar-x-maghrebi` set `graphemes_base` to `ar`, so a change to a bare-letter reading here moves every dialect. The dialect specs have their own page: [Arabic dialects](ar-dialects.md).

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

## Remaining engine limits

The engine works one word at a time, and three Arabic processes need more than that.

- A word-final ة that carries no written vowel reads as the pausal /a/. In an iḍāfa it should be /at/, and only the following word shows that.
- Pausal dropping of the case vowels needs to know where the utterance ends.
- Sun-letter assimilation on undiacritized text needs a morphological split of the attached article, which the grapheme table cannot make.

## Gold benchmark

The `ar` entry of the `wikipron` dataset in `scripts/benchmark.py` is CUNY-CL/wikipron `ara_arab_broad.tsv`: Wiktionary broad IPA, crowd-curated. Wiktionary files Arabic entries under the unvocalised page title, so the input column carries no harakat while the gold IPA writes every short vowel. A spec that follows the input contract cannot recover those vowels from this input.

The `wikipron_ar_diacritized` dataset keeps the same gold IPA and restores the tashkeel on the input side with `text2tashkeel`. That dependency is optional, so CI does not reproduce this row. The `valid_ceiling` block in `ar.json` records the folded score: the spec's output scored with the short vowels removed from both sides. Reproduce it with `scripts/folded_per.py --lang ar --dataset wikipron --segments 'a i u'`. For the scores themselves, see the [scoreboard](../scoreboard.md).

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

## References

- Wright, W. (1896). *A Grammar of the Arabic Language*, 3rd ed., Vol. I. Cambridge University Press. Part First, "Orthography and Orthoepy", on the matres lectionis and on alif maqṣūra as a spelling of final /aː/. It also covers the jazma (sukūn) as the mark of a vowelless consonant.
- Watson, J.C.E. (2002). *The Phonology and Morphology of Arabic*. Oxford University Press.
- Ryding, K.C. (2005). *A Reference Grammar of Modern Standard Arabic*. Cambridge University Press.
- Wikipedia: [Sun and moon letters](https://en.wikipedia.org/wiki/Sun_and_moon_letters), a reading path for the article assimilation.
- Wikipedia: [Standard Arabic phonology](https://en.wikipedia.org/wiki/Standard_Arabic_phonology), a reading path for the ض merger.

---
[← Russian](ru.md) · [Home](../index.md) · [Arabic dialects →](ar-dialects.md)
