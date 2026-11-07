# Standard Thai (`th`)

**Code**: `th` | **Family**: Tai-Kadai > Southwestern Tai | **Script**: Thai (abugida) | **Quality tier**: research

The `th` spec describes Standard (Central) Thai in the Thai script. Two facts shape it. Thai does not write tone, so the spec computes it from the shape of the syllable. Thai also writes vowels around the consonant, not only after it.

Thai is a deep orthography, so the 0.25 PER production threshold applies (see [quality tiers](../specs/quality_tiers.md#the-per-threshold)). No part of a Thai syllable is a one-to-one correspondence. Four interacting properties give the tone, and none of them is a tone letter. A vowel can be written before, above, below or after its consonant. The coda inventory neutralises most of the alphabet.

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

## Sources

- Slayden, G. (2009). *Survey of Central Thai Phonology*. thai-language.com. <http://www.thai-language.com/resources/slayden-thai-phonology.pdf> (§4.3 compound vowels, §5 phonotactics, §6 tones, Appendix C).
- Iwasaki, S. & Ingkaphirom, P. (2005). *A Reference Grammar of Thai*. Cambridge University Press.
- Haas, M.R. (1964). *Thai-English Student's Dictionary*. Stanford University Press.

---
[← Vietnamese](vi.md) · [Home](../index.md) · [Yoruba →](yo.md)
