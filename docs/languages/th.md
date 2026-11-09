# Thai (`th`)

<!-- atlas:summary begin -->
Thai is a Tai-Kadai language, written in the Thai script. Glottolog places it in Cambodia, Myanmar (Burma) and Thailand. The `th` spec is at the research tier. It cites 3 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `th` |
| ISO 639-3 | [tha](https://iso639-3.sil.org/code/tha), Thai |
| Glottolog | [thai1261](https://glottolog.org/resource/languoid/id/thai1261), Thai |
| Wikidata | [Q9217](https://www.wikidata.org/wiki/Q9217) |
| Wikipedia | [Thai language](https://en.wikipedia.org/wiki/Thai_language) |
| Family | [Tai-Kadai](by-family.md#tai-kadai) |
| Region | [Eurasia](by-region.md#eurasia) > [Cambodia](by-region.md#cambodia), [Myanmar (Burma)](by-region.md#myanmar-burma), [Thailand](by-region.md#thailand) |
| Script | [Thai](by-script.md#thai) (abugida) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1283, living |
| Parent | [Proto-Tai-Kadai (family node)](https://tigregotico.github.io/orthography2ipa/#tai) `tai` |
| Explorer | [`th` in the data explorer](https://tigregotico.github.io/orthography2ipa/#th) |
| Spec file | [`th.json`](../../orthography2ipa/data/th.json) |
<!-- atlas:header end -->

## Overview

The `th` spec describes Standard (Central) Thai in the Thai script. Two facts shape it. Thai does not write tone, so the spec computes it from the shape of the syllable. Thai also writes vowels around the consonant, not only after it.

Thai is a deep orthography, so the 0.25 PER production threshold applies (see [quality tiers](../specs/quality_tiers.md#the-per-threshold)). No part of a Thai syllable is a one-to-one correspondence. Four interacting properties give the tone, and none of them is a tone letter. A vowel can be written before, above, below or after its consonant. The coda inventory neutralises most of the alphabet.

The page places Thai in the Southwestern Tai branch.

## Tone is computed, not spelled

Thai has five tones: mid, low, falling, high and rising. No letter writes any of them. Four properties name the tone of a syllable:

| Property | Values |
|---|---|
| Class of the initial consonant | high, mid or low |
| Shape of the rime | live, or dead |
| Length of the vowel in a dead rime | short or long |
| Tone mark on the initial | none, or one of ⟨่ ้ ๊ ๋⟩ |

The spec states the whole system in its `tone_rules` block: the class of every consonant letter, the four marks, the codas that check a syllable (`dead_codas`), and the table that crosses class, shape and mark. The engine reads that block in `assign_computed_tones` (`orthography2ipa/tone.py`). That function names no language and no script, and every fact that it uses comes from the spec.

Live and dead are the terms of Slayden (2009). A live syllable ends in a long open vowel, a nasal or a glide. A dead syllable ends in a short open vowel or in a stop.

A tone mark sits on the initial consonant. In a syllable that does not start the word, the mark therefore stands between that consonant and the vowel sign after it. The spec groups every slot from the onset consonant onward with the syllable that the consonant opens. So ⟨เป็นต้อง⟩ gives `peːn˧tɔːŋ˥˩`, with the falling tone on the second syllable.

## Vowel length and the compound vowels

Thai contrasts short and long vowels, and it writes them with different signs. Length therefore comes from the grapheme table: ⟨ะ⟩ /a/ against ⟨า⟩ /aː/, ⟨ิ⟩ /i/ against ⟨ี⟩ /iː/, and so on. Length then feeds the tone table, because a dead syllable on a low-class initial takes a different tone with a short vowel and with a long one.

Three vowels are opening diphthongs, /iːa uːa ɯːa/, each a long high vowel plus /a/ (Slayden 2009, §4.3). Each is written as a circumfix around the consonant. The spec declares the postposed half of each circumfix as a grapheme of its own: ⟨ีย⟩ /iːa/, ⟨ือ⟩ /ɯːa/ and ⟨ัว⟩ /uːa/. The preposed ⟨เ⟩ then falls silent, and the whole nucleus comes from one grapheme. Without these graphemes, the engine reads the two signs as two nuclei, and a word such as ⟨เมือง⟩ splits into two syllables.

| Word | Engine output |
|---|---|
| ⟨เรือ⟩ | `rɯːa˧` |
| ⟨เรือน⟩ | `rɯːan˧` |
| ⟨เรียน⟩ | `riːan˧` |
| ⟨ตัว⟩ | `tuːa˧` |
| ⟨เมือง⟩ | `mɯːaŋ˧` |

A bare ⟨ว⟩ between two consonants also spells /uːa/ in a closed syllable. The `consonant_nuclei` block states this reading, so ⟨ขวด⟩ gives `kʰuːat̚˨˩`. ⟨ขวา⟩ keeps the onset glide, because a vowel follows the ⟨ว⟩: `kʰwaː˩˩˦`.

⟨าะ⟩ /ɔ/ has the same shape (Slayden 2009, Appendix C). The vowel is short, so the tone table reads the syllable as dead-short: ⟨เกาะ⟩ gives `kɔ˨˩`, ⟨เลาะ⟩ `lɔ˦˥` and ⟨เจาะ⟩ `tɕɔ˨˩`.

## The gold rows

Two gold sets score the spec. For the figures, see the [scoreboard](../evaluation/generated/scoreboard.md).

The `wikipron` row (`tha_thai_broad`) is `crowd-scraped` and can gate. The `vox_communis` row is `epitran-derived`, so it can neither qualify nor block a promotion.

Most of the gap between the two rows is notation, not phonology. Both golds write the tone, in different slots. WikiPron writes the Chao letter after the whole syllable, where IPA writes it. The `vox_communis` gold, which comes from Epitran, writes it on the nucleus, before the coda. The spec follows WikiPron. `scripts/fold_th_notation.py` scores both rows with every tone letter moved to the end of the string on both sides, which keeps tone identity and order. That fold removes most of the `vox_communis` gap and a small part of the `wikipron` one. What remains is under a point of PER on either row. The tone that the spec computes is very nearly the tone that both golds carry.

Placement is a notation choice of each gold, and Thai spells tone. So the spec records these folds as `audit` entries (`at_ceiling_documented`), not as a `valid_ceiling`, which is for a contrast that the orthography does not write. [A tone-marked gold measures the tone computation too](../evaluation/datasets.md#a-tone-marked-gold-measures-the-tone-computation-too-th) explains how to read the `th` rows.

## Known limitations

Some circumfix vowels are not read. ⟨เ◌า⟩ /aw/, ⟨เ◌อ⟩ and ⟨เ◌ิ⟩ /ɤː/, and ⟨เ◌ะ แ◌ะ โ◌ะ⟩ each end in a sign that spells another vowel on its own: ⟨า⟩ /aː/, ⟨อ⟩ /ɔː/, ⟨ิ⟩ /i/, ⟨ะ⟩ /a/. The circumfix mechanism takes the whole nucleus from the postposed grapheme, so it cannot tell the two apart. ⟨เขา⟩ gives `kʰaː˩˩˦` for /kʰaw/, and ⟨เธอ⟩ gives `tʰɔː˧` for /tʰɤː/. A fix needs the preposed sign to condition the reading of the postposed one, and no grapheme key can express that.

Mai taikhu ⟨็⟩ shortens the vowel of its syllable. The vowel is written before the consonant that the mark sits on, so no contiguous grapheme key reaches it. The mark is silent, and the engine reads the syllable as dead-long: ⟨เก็บ⟩ gives `keːp̚˨˩` for /kep̚/.

The spec states coda neutralisation as `word_final` entries. A syllable that closes inside a word therefore keeps the onset reading of its last letter. ⟨ครอบครัว⟩ gives `kʰrɔːb˧kʰruːa˧`, but ⟨ครอบ⟩ alone gives `kʰrɔːp̚˥˩`. The wrong coda is not in `dead_codas`, so the tone of that syllable is wrong too.

A consonant with no written vowel always takes the inherent vowel /o/. Thai reads /o/ only in a closed syllable and /a/ in an open one. The spec can declare one `inherent_vowel`, not a pair that depends on the syllable, so ⟨ขนม⟩ gives `kʰon˩˩˦mo˦˥`.

The spec declares ⟨ทร⟩ as an unconditional /s/ digraph for the lexicalised set, such as ⟨ทราย⟩ `saːj˧`. It over-applies to the Indic loans built on ⟨จันทร⟩ 'moon' and ⟨ทร⟩ 'bear, carry', where ⟨ท⟩ and ⟨ร⟩ are a plain cluster: ⟨จันทรา⟩ gives `tɕan˧saː˧`. A fix needs a lexicon overlay or a scoped exception list. The spec `notes` size this gap.

<!-- atlas:lects begin -->
## Related lects

No spec names `th` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-iwasaki2005"></a>Iwasaki, Shoichi & Ingkaphirom, Preeya (2005). *A Reference Grammar of Thai*. Cambridge University Press.
2. <a id="src-haas1964"></a>Haas, M.R. (1964). *Thai-English Student's Dictionary*. Stanford University Press.
3. <a id="src-slayden2009"></a>Slayden, Glenn (2009). *Survey of Central Thai Phonology*. thai-language.com. Cited: §4.3 (compound vowel phonemes), §5 (phonotactics), §6 (tones), Appendix C sets 11, 12, 18, 19. [thai-language.com](http://www.thai-language.com/resources/slayden-thai-phonology.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `th` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 17221 | 0.1788 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `th` | generated | epitran-derived | CC0 1.0 | 23704 | 0.4281 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 59 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ p̚ |  | d t tʰ t̚ |  | k kʰ k̚ | ʔ |
| Affricate |  |  |  | tɕ tɕʰ |  |  |
| Nasal | m |  | n |  | ŋ |  |
| Trill |  |  | r |  |  |  |
| Fricative |  | f | s |  |  | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | u uː ɯ ɯː |
| Close-mid | eː | oː |
| Open-mid | ɛː | ɔ ɔː |
| Open | a aː |  |

Sequences that the spec writes as one unit: [aj] [am] [iːa] [kl] [kr] [kw] [kʰl] [kʰr] [kʰw] [lɯ] [pl] [pr] [pʰl] [pʰr] [rɯ] [tr] [uːa] [w] [ɯːa] [ʔaj] [ʔeː] [ʔoː] [ʔɛː].

Tones: [˧] mid, [˨˩] low, [˥˩] falling, [˦˥] high, [˩˩˦] rising.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨ก⟩ | [k] | word final [k̚] |
| ⟨กร⟩ | [kr] |  |
| ⟨กร์⟩ | ∅ |  |
| ⟨กล⟩ | [kl] |  |
| ⟨กล์⟩ | ∅ |  |
| ⟨กว⟩ | [kw] |  |
| ⟨กว์⟩ | ∅ |  |
| ⟨ก์⟩ | ∅ |  |
| ⟨ข⟩ | [kʰ] | word final [k̚] |
| ⟨ขร⟩ | [kʰr] |  |
| ⟨ขร์⟩ | ∅ |  |
| ⟨ขล⟩ | [kʰl] |  |
| ⟨ขล์⟩ | ∅ |  |
| ⟨ขว⟩ | [kʰw] |  |
| ⟨ขว์⟩ | ∅ |  |
| ⟨ข์⟩ | ∅ |  |
| ⟨ฃ⟩ | [kʰ] | word final [k̚] |
| ⟨ฃ์⟩ | ∅ |  |
| ⟨ค⟩ | [kʰ] | word final [k̚] |
| ⟨คร⟩ | [kʰr] |  |
| ⟨คร์⟩ | ∅ |  |
| ⟨คล⟩ | [kʰl] |  |
| ⟨คล์⟩ | ∅ |  |
| ⟨คว⟩ | [kʰw] |  |
| ⟨คว์⟩ | ∅ |  |
| ⟨ค์⟩ | ∅ |  |
| ⟨ฅ⟩ | [kʰ] | word final [k̚] |
| ⟨ฅ์⟩ | ∅ |  |
| ⟨ฆ⟩ | [kʰ] | word final [k̚] |
| ⟨ฆ์⟩ | ∅ |  |
| ⟨ง⟩ | [ŋ] |  |
| ⟨ง์⟩ | ∅ |  |
| ⟨จ⟩ | [tɕ] | word final [t̚] |
| ⟨จ์⟩ | ∅ |  |
| ⟨ฉ⟩ | [tɕʰ] | word final [t̚] |
| ⟨ฉ์⟩ | ∅ |  |
| ⟨ช⟩ | [tɕʰ] | word final [t̚] |
| ⟨ช์⟩ | ∅ |  |
| ⟨ซ⟩ | [s] | word final [t̚] |
| ⟨ซ์⟩ | ∅ |  |
| ⟨ฌ⟩ | [tɕʰ] | word final [t̚] |
| ⟨ฌ์⟩ | ∅ |  |
| ⟨ญ⟩ | [j] | word final [n] |
| ⟨ญ์⟩ | ∅ |  |
| ⟨ฎ⟩ | [d] | word final [t̚] |
| ⟨ฎ์⟩ | ∅ |  |
| ⟨ฏ⟩ | [t] | word final [t̚] |
| ⟨ฏ์⟩ | ∅ |  |
| ⟨ฐ⟩ | [tʰ] | word final [t̚] |
| ⟨ฐ์⟩ | ∅ |  |
| ⟨ฑ⟩ | [tʰ] | word final [t̚] |
| ⟨ฑ์⟩ | ∅ |  |
| ⟨ฒ⟩ | [tʰ] | word final [t̚] |
| ⟨ฒ์⟩ | ∅ |  |
| ⟨ณ⟩ | [n] | word final [n] |
| ⟨ณ์⟩ | ∅ |  |
| ⟨ด⟩ | [d] | word final [t̚] |
| ⟨ด์⟩ | ∅ |  |
| ⟨ต⟩ | [t] | word final [t̚] |
| ⟨ตร⟩ | [tr] |  |
| ⟨ตร์⟩ | ∅ |  |
| ⟨ต์⟩ | ∅ |  |
| ⟨ถ⟩ | [tʰ] | word final [t̚] |
| ⟨ถ์⟩ | ∅ |  |
| ⟨ท⟩ | [tʰ] | word final [t̚] |
| ⟨ทร⟩ | [s] |  |
| ⟨ทร์⟩ | ∅ |  |
| ⟨ท์⟩ | ∅ |  |
| ⟨ธ⟩ | [tʰ] | word final [t̚] |
| ⟨ธ์⟩ | ∅ |  |
| ⟨น⟩ | [n] | word final [n] |
| ⟨น์⟩ | ∅ |  |
| ⟨บ⟩ | [b] | word final [p̚] |
| ⟨บ์⟩ | ∅ |  |
| ⟨ป⟩ | [p] | word final [p̚] |
| ⟨ปร⟩ | [pr] |  |
| ⟨ปร์⟩ | ∅ |  |
| ⟨ปล⟩ | [pl] |  |
| ⟨ปล์⟩ | ∅ |  |
| ⟨ป์⟩ | ∅ |  |
| ⟨ผ⟩ | [pʰ] | word final [p̚] |
| ⟨ผล⟩ | [pʰl] |  |
| ⟨ผล์⟩ | ∅ |  |
| ⟨ผ์⟩ | ∅ |  |
| ⟨ฝ⟩ | [f] | word final [p̚] |
| ⟨ฝ์⟩ | ∅ |  |
| ⟨พ⟩ | [pʰ] | word final [p̚] |
| ⟨พร⟩ | [pʰr] |  |
| ⟨พร์⟩ | ∅ |  |
| ⟨พล⟩ | [pʰl] |  |
| ⟨พล์⟩ | ∅ |  |
| ⟨พ์⟩ | ∅ |  |
| ⟨ฟ⟩ | [f] | word final [p̚] |
| ⟨ฟ์⟩ | ∅ |  |
| ⟨ภ⟩ | [pʰ] | word final [p̚] |
| ⟨ภ์⟩ | ∅ |  |
| ⟨ม⟩ | [m] |  |
| ⟨ม์⟩ | ∅ |  |
| ⟨ย⟩ | [j] |  |
| ⟨ย์⟩ | ∅ |  |
| ⟨ร⟩ | [r] | word final [n] |
| ⟨ร์⟩ | ∅ |  |
| ⟨ฤ⟩ | [rɯ] |  |
| ⟨ฤ์⟩ | ∅ |  |
| ⟨ล⟩ | [l] | word final [n] |
| ⟨ล์⟩ | ∅ |  |
| ⟨ฦ⟩ | [lɯ] |  |
| ⟨ฦ์⟩ | ∅ |  |
| ⟨ว⟩ | [w] |  |
| ⟨ว์⟩ | ∅ |  |
| ⟨ศ⟩ | [s] | word final [t̚] |
| ⟨ศ์⟩ | ∅ |  |
| ⟨ษ⟩ | [s] | word final [t̚] |
| ⟨ษ์⟩ | ∅ |  |
| ⟨ส⟩ | [s] | word final [t̚] |
| ⟨ส์⟩ | ∅ |  |
| ⟨ห⟩ | [h] |  |
| ⟨หง⟩ | [ŋ] |  |
| ⟨หญ⟩ | [j] |  |
| ⟨หณ⟩ | [n] |  |
| ⟨หน⟩ | [n] |  |
| ⟨หม⟩ | [m] |  |
| ⟨หย⟩ | [j] |  |
| ⟨หร⟩ | [r] |  |
| ⟨หล⟩ | [l] |  |
| ⟨หว⟩ | [w] |  |
| ⟨หฬ⟩ | [l] |  |
| ⟨ห์⟩ | ∅ |  |
| ⟨ฬ⟩ | [l] | word final [n] |
| ⟨ฬ์⟩ | ∅ |  |
| ⟨อ⟩ | [ɔː] | word initial [ʔ] |
| ⟨อย⟩ | [j] |  |
| ⟨อ์⟩ | ∅ |  |
| ⟨ฮ⟩ | [h] |  |
| ⟨ฮ์⟩ | ∅ |  |
| ⟨ฯ⟩ | ∅ |  |
| ⟨ะ⟩ | [a] |  |
| ⟨ั⟩ | [a] |  |
| ⟨ัว⟩ | [uːa] |  |
| ⟨า⟩ | [aː] |  |
| ⟨าะ⟩ | [ɔ] |  |
| ⟨ำ⟩ | [am] |  |
| ⟨ิ⟩ | [i] |  |
| ⟨ี⟩ | [iː] |  |
| ⟨ีย⟩ | [iːa] |  |
| ⟨ีย์⟩ | [iː] |  |
| ⟨ึ⟩ | [ɯ] |  |
| ⟨ื⟩ | [ɯː] |  |
| ⟨ือ⟩ | [ɯːa] |  |
| ⟨ุ⟩ | [u] |  |
| ⟨ู⟩ | [uː] |  |
| ⟨ฺ⟩ | ∅ |  |
| ⟨เ⟩ | [eː] |  |
| ⟨เอ⟩ | [ʔeː] |  |
| ⟨แ⟩ | [ɛː] |  |
| ⟨แอ⟩ | [ʔɛː] |  |
| ⟨โ⟩ | [oː] |  |
| ⟨โอ⟩ | [ʔoː] |  |
| ⟨ใ⟩ | [aj] |  |
| ⟨ใอ⟩ | [ʔaj] |  |
| ⟨ไ⟩ | [aj] |  |
| ⟨ไอ⟩ | [ʔaj] |  |
| ⟨ๅ⟩ | ∅ |  |
| ⟨ๆ⟩ | ∅ |  |
| ⟨็⟩ | ∅ |  |
| ⟨่⟩ | ∅ |  |
| ⟨้⟩ | ∅ |  |
| ⟨๊⟩ | ∅ |  |
| ⟨๋⟩ | ∅ |  |
| ⟨์⟩ | ∅ |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 3 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `TH_UNRELEASED_K_CODA` | /k/ → [k̚], word-finally | - | [Iwasaki 2005](#src-iwasaki2005) |
| `TH_UNRELEASED_T_CODA` | /t/ → [t̚], word-finally | - | [Iwasaki 2005](#src-iwasaki2005) |
| `TH_UNRELEASED_P_CODA` | /p/ → [p̚], word-finally | - | [Iwasaki 2005](#src-iwasaki2005) |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="เก็บ|เกาะ|ขนม|ขวด|ขวา|เขา|ครอบครัว|จันทรา|ทราย|เมือง|เรียน|เรือ" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "th")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| เก็บ | [keːp̚˨˩] |
| เกาะ | [kɔ˨˩] |
| ขนม | [kʰon˩˩˦mo˦˥] |
| ขวด | [kʰuːat̚˨˩] |
| ขวา | [kʰwaː˩˩˦] |
| เขา | [kʰaː˩˩˦] |
| ครอบครัว | [kʰrɔːb˧kʰruːa˧] |
| จันทรา | [tɕan˧saː˧] |
| ทราย | [saːj˧] |
| เมือง | [mɯːaŋ˧] |
| เรียน | [riːan˧] |
| เรือ | [rɯːa˧] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Tewa](tew.md) · [Home](../index.md) · [Tibetan →](bo.md)
