# Standard Thai (`th`)

Standard (Central) Thai in the Thai script. Two things dominate the spec:
tone is not written, it is computed from the shape of the syllable, and
the vowels are written around the consonant rather than after it.

## Orthographic depth and production threshold

**Deep orthography, the ≤ 0.25 PER production threshold applies** (see
[quality tiers](../quality_tiers.md)). Nothing in a Thai syllable is a
one-to-one correspondence: the tone comes from four interacting
properties and none of them is a tone letter, a vowel can be written
before, above, below and after the consonant it follows, and the coda
inventory neutralises most of the alphabet.

## Tone is computed, not spelled

Thai has five tones — mid, low, falling, high, rising — and no letter
writes any of them. The tone of a syllable is named by the class of its
initial consonant (high, mid or low), by whether the rime is live or
dead, by the length of the vowel in a dead rime, and by which of the
four tone marks ⟨่ ้ ๊ ๋⟩ rides the initial. The spec states that whole
system in its `tone_rules` block: the class of every consonant letter,
the four marks, the codas that check a syllable, and the class × shape ×
mark table itself. The engine reads it in `assign_computed_tones`, which
names no language and no script — every fact it consults comes out of
the spec.

Live and dead is Slayden's terminology: a live syllable ends in a long
open vowel, a nasal or a glide; a dead syllable ends in a short open
vowel or in a stop.

A tone mark is written **on the initial consonant**, which means that in
any syllable that is not word-initial the mark stands between that
consonant and the vowel sign that follows it. The slot grouping keeps
every slot from the onset consonant onward with the syllable that
consonant opens; grouping the mark with the syllable before it instead
read ⟨เป็นต้อง⟩ as /peːn˥˩tɔːŋ˧/, with the two tones swapped.

## Vowel length and the compound vowels

Thai contrasts short and long vowels phonemically, and the two are
written with different signs, so length falls out of the grapheme table
(⟨ะ⟩ /a/ against ⟨า⟩ /aː/, ⟨ิ⟩ /i/ against ⟨ี⟩ /iː/, and so on). Length
then feeds the tone table, because a dead syllable with a short vowel
and a dead syllable with a long one take different tones on a low-class
initial.

Three vowels are opening diphthongs formed by a long high monophthong
plus /a/ — /iːa uːa ɯːa/ — and each is written as a circumfix around the
consonant. The spec declares the **postposed half** of each circumfix as
a grapheme of its own, ⟨ีย⟩ /iːa/, ⟨ือ⟩ /ɯːa/ and ⟨ัว⟩ /uːa/, which is
what lets the preposed ⟨เ⟩ fall silent and the whole nucleus come from
one grapheme: ⟨เรือ⟩ /rɯːa/, ⟨เรือน⟩ /rɯːan/, ⟨เรียน⟩ /riːan/,
⟨ตัว⟩ /tuːa/. Declaring only the halves read the two signs as two
nuclei, and ⟨เมือง⟩ came out as two syllables. ⟨าะ⟩ /ɔ/ is the same
shape and gives ⟨เกาะ⟩ /kɔ̀/, ⟨เลาะ⟩ /lɔ́/, ⟨เจาะ⟩ /tɕɔ̀/; the vowel is
short, so the tone table reads the syllable as dead-short and produces
those tones from the spelling.

## Benchmark (full gold set, no cap)

| dataset | provenance | n | PER | tone-blind PER |
|---|---|---:|---:|---:|
| `wikipron` | crowd-scraped | 16937 | **0.1881** | 0.1651 |
| `vox_communis` | epitran-derived | 23704 | 0.4318 | 0.2218 |

The qualifying row is `wikipron`. `vox_communis` is epitran-derived and
can neither qualify nor block promotion.

The gap between the two rows is almost entirely a notation difference
and not a phonological one. Both golds write the tone, but not in the
same slot: WikiPron writes the Chao letter after the whole syllable,
where the IPA writes it, and the Epitran-derived `vox_communis` rows
write it on the nucleus, before the coda. The spec follows WikiPron.
Scoring both rows with the tone letters moved to the end of the string
on both sides — which neutralises placement while keeping tone identity
and order — gives 0.1713 for `wikipron` and 0.2295 for `vox_communis`.
Placement therefore costs the `vox_communis` row 20.2 PER points and the
`wikipron` row 1.7, and what is left over once placement is neutralised
is under a point on either row. The tone the spec computes is very
nearly the tone both golds carry; the disagreement is about where to
print it.

## Known limitations

- ⟨เ–า⟩ /aw/, ⟨เ–อ⟩ and ⟨เ–ิ⟩ /ɤː/, and ⟨เ–ะ แ–ะ โ–ะ⟩ are not read.
  Each ends in a sign that already spells a different vowel on its own —
  ⟨า⟩ /aː/, ⟨อ⟩ /ɔː/, ⟨ิ⟩ /i/, ⟨ะ⟩ /a/ — and the circumfix mechanism
  takes the whole nucleus from the postposed grapheme, so it cannot tell
  the two apart: ⟨เขา⟩ reads /kʰaː/ for /kʰaw/ and ⟨เธอ⟩ /tʰɔː/ for
  /tʰɤː/. Separating them needs the preposed sign to condition the
  reading of the postposed one, which no grapheme key can express.
- /uːa/ written with a bare ⟨ว⟩ before a coda, as in ⟨ขวด⟩ /kʰùːat/, is
  not read; the ⟨ว⟩ stays an onset glide.
- Mai taikhu ⟨็⟩ shortens the vowel of its syllable (⟨เก็บ⟩ is /kep̚/),
  but that vowel is written before the consonant the mark sits on, so no
  contiguous grapheme key reaches it. The mark is silent and the
  syllable is read dead-long.
- Coda neutralisation is stated as `word_final`, so a syllable that
  closes inside a word keeps the letter's onset reading: ⟨ครอบครัว⟩
  gives /kʰrɔːbkʰruːa/ where ⟨ครอบ⟩ alone gives /kʰrɔːp̚/. Because the
  wrong coda is not in `dead_codas`, the tone of that syllable is wrong
  with it.
- A consonant with no written vowel takes the inherent vowel
  unconditionally, where Thai reads /o/ only in a closed syllable and
  /a/ in an open one.
- ⟨ทร⟩ is declared as an unconditional /s/ digraph for the lexicalised
  set, and over-applies to the Indic loans built on ⟨จันทร⟩ and ⟨ทร⟩.

## Sources

- Slayden, G. (2009). *Survey of Central Thai Phonology*.
  thai-language.com.
  <http://www.thai-language.com/resources/slayden-thai-phonology.pdf>
  (§4.3 compound vowels, §5 phonotactics, §6 tones, Appendix C).
- Iwasaki, S. & Ingkaphirom, P. (2005). *A Reference Grammar of Thai*.
  Cambridge University Press.
- Haas, M.R. (1964). *Thai-English Student's Dictionary*. Stanford
  University Press.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)
