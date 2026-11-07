# Hausa (ha): a shallow orthography that hides tone, length and one consonant contrast

**Code**: `ha` | **Family**: Afro-Asiatic > Chadic > West Chadic | **Script**: Latin (Boko)
**Quality tier**: research
**Source read**: Newman, P. (1996), "Hausa Phonology", chapter 27 of A. S. Kaye & P. T. Daniels (eds.), *Phonologies of Asia and Africa*, Eisenbrauns, pp. 537-552 ([full text](https://scholarworks.iu.edu/dspace/bitstreams/f1d4231b-d713-4134-970c-071c5f8485ed/download)). The consonant inventory is Table 27-1 on p. 538, and the segmental discussion is on pp. 539-540. A second description is read alongside it: Schuh, R. G. & Yalwa, L. D. (1999), "Hausa", Illustrations of the IPA, in *Handbook of the International Phonetic Association*, Cambridge University Press, pp. 90-95 ([scan](https://archive.org/details/rosettaproject_hau_phon-4)). It describes the Kano standard and disagrees with Newman on two letters.

Boko spells most Hausa consonants one to one, and the spec reads them directly. Three contrasts are absent from the spelling: tone, vowel length, and the two rhotics. No grapheme-driven transcriber can recover tone or length. The spec carries the rhotics as a candidate pair.

## Input contract

The spec reads Boko, the modified Roman alphabet introduced under British administration. It is the predominant writing system for Hausa in Nigeria and Niger. Ajami (Arabic script) is a different orthography, and the spec does not model it.

Boko uses the ordinary Latin letters plus four hooked letters ⟨ɓ ɗ ƙ ƴ⟩ and the digraphs ⟨sh ts kw gw ƙw ky gy ƙy fy⟩. Niger spells ⟨ƴ⟩ as ⟨ʼy⟩. The spec accepts both spellings and transcribes them alike, because they are one phoneme.

The apostrophe is a letter of the alphabet, not punctuation. It spells the glottal stop, which reaches Hausa mostly through Arabic loans, as in *’addu’aa* 'prayer' and *saba’in* 'seventy' (p. 540). The spec maps three characters to it: the typewriter apostrophe U+0027, the modifier letter U+02BC, and the curly apostrophe U+2019. Newman's own citation forms use the curly one. The two-letter ⟨'y⟩ or ⟨’y⟩ still wins in the tokenizer, so the glottalized approximant never splits into a glottal stop and /j/.

The U+2019 mapping has a cost. The alphabet gives no way to tell it from a closing quotation mark, so a quoted word picks up a glottal stop at each end:

```python
>>> import orthography2ipa
>>> orthography2ipa.transcribe("'sannu'", "ha")
'ʔsannuʔ'
```

A word-initial ⟨ʔs⟩ is not a possible Hausa onset, which shows that the source was punctuation, but the spec cannot act on that. The mapping stays, because without it the spec would drop the letter silently on every genuine occurrence, and that case is more common.

Newman's citation forms mark the rhotic contrast. They write ⟨r̃⟩ for the tap or roll and leave plain ⟨r⟩ for the flap (p. 539). The spec reads the mark: where the input writes ⟨r̃⟩, the flap candidate is excluded. The WikiPron gold has only a handful of ⟨r̃⟩ headwords, so the data shows little about how widely writers outside Newman follow the convention.

## What Boko does not write

Tone. Hausa has high, low and falling tones, all lexically and grammatically contrastive, and the alphabet marks none of them. Newman states this for tone and length alike (p. 537).

Vowel length. All five vowels have long and short counterparts, contrastive in open syllables: *fiitoo* 'whistling' against *fitoo* 'ferrying'. In closed syllables all vowels are short, which is predictable, but the contrast in open syllables is lexical. Dictionaries and teaching materials sometimes write long vowels doubled, and standard Boko does not. Niger tried to make the doubled spelling official, and the attempt "proved to be a failure and was eventually dropped" (Newman 1996, p. 537 n. 2).

The rhotic contrast. This gap is of a different kind, and the spec treats it differently. Hausa contrasts an apical tap or roll /r/ with a retroflex flap /ɽ/, and Boko spells both ⟨r⟩. The flap is the native rhotic. The roll came in through Arabic, Kanuri and English loanwords, through ideophones and intensives, and through rhotacization of syllable-final alveolars (pp. 539-540). Which rhotic a word takes is a lexical fact with no cue in the spelling.

Schuh & Yalwa give the standard minimal pair: [bàràː] 'begging' against [ɓaraː] 'servant', "both orthographic *bara*". They add that their Kano speaker "is among the minority of Hausa speakers who have only the single r sound, [r]" (p. 93), so the contrast does not hold for every speaker. The spec therefore encodes ⟨r⟩ as an ordered candidate pair [r, ɽ]. Both readings are in the lattice, and the order is a decoding default, not a claim about frequency.

```python
>>> from orthography2ipa import G2P
>>> G2P("ha").word_candidates("bara")
['bara', 'baɽa']
```

Word-finally only the roll occurs (p. 539), and the spec declares that as a `word_final` positional entry. The entry does not enforce the constraint: it adds to the default candidate list and does not replace it. The flap reading therefore stays in the beam at word end, as `word_candidates("kar")` gives `['kar', 'kaɽ']`. The roll wins there only because it already sorts first. An exclusive positional constraint is engine work.

## Letter values

| Letter | IPA | Note |
|:--|:--|:--|
| ɓ, ɗ | ɓ, ɗ | laryngealized implosive stops |
| ƙ | kʼ | ejective, with plain counterpart /k/ |
| ts | sʼ, tsʼ | ejective, with plain counterpart /s/. The fricative is first (Newman, p. 539), the affricate second (Schuh & Yalwa, p. 92). |
| ƴ, ʼy | j̰, ʔʲ | one phoneme, two spellings: Newman's glottalized palatal approximant (p. 539) or Schuh & Yalwa's palatalized glottal stop (p. 92) |
| c, j | tʃ, dʒ | affricates in Standard (Kano) Hausa |
| sh | ʃ | |
| kw, gw, ƙw | kʷ, ɡʷ, kʷʼ | unit labialized velars |
| ky, gy, ƙy | kʲ, ɡʲ, kʲʼ | unit palatalized velars |
| fy | fʲ | palatalized labial, lexically infrequent |
| r | r, ɽ | see above. The word-final roll is declared but not enforced. |
| r̃ | r | tap or roll only, the mark excludes the flap |
| ' ʼ ’ | ʔ | glottal stop, a letter and not punctuation |
| p | p | loan spellings only, not a native phoneme |
| n | n, and n or ŋ word-finally | see "Word-final /n/" below |

Kw, gw, ky and gy are phonemes, not a consonant and a glide. They contrast with the plain velars before /a(a)/: *gadaa* 'duiker', *gwadaa* 'test!', *gyaɗaa* 'peanuts' (p. 539). Velars are also redundantly labialized before back vowels and palatalized before front vowels, so *doogoo* 'tall' is [doogwoo]. That allophony is predictable and the orthography never shows it, so the spec does not encode it.

Hausa has no vowel-initial syllables, and a word-initial vowel takes an epenthetic glottal-stop onset. The spec writes it through `word_initial` positional entries on the vowels.

## Where the two descriptions disagree

Newman and Schuh & Yalwa describe the same language and differ on two letters. The spelling cannot resolve either difference. The spec ships both readings of each letter as an ordered candidate pair and states which description put each reading first.

⟨ts⟩ is an ejective. Newman pairs it with ⟨ƙ⟩ and gives the plain counterparts as /s/ and /k/, which makes ⟨ts⟩ the ejective fricative /sʼ/ (p. 539). Schuh & Yalwa describe the sound as ranging "from an ejective alveolar affricate with clear plosive component to an ejective fricative". In the Kano dialect "it tends to be realized as the affricate" (p. 92). The fricative stays first, because Newman states it without qualification. The WikiPron gold, the only `ha` gold whose IPA column is human notation, writes `sʼ` throughout and never `t͡s`. The affricate is second, so the Kano reading of Schuh & Yalwa, which epitran also writes, is in the lattice.

⟨ƴ⟩, Niger ⟨ʼy⟩, is one phoneme with four accepted spellings. Newman calls it the glottalized laryngealized palatal approximant /j̰/ (p. 539). Schuh & Yalwa give it for Kano and "a broad range of dialects" as a palatalized glottal stop /ʔʲ/. Historically it is a contraction of ɗ and j, which Sokoto keeps: Sokoto *ɗiyaa*, Kano *ʼyaa* (p. 92). Both are candidates, with the approximant first. The VoxCommunis gold writes `ʔʲ` where the spec writes `j̰`, so this is a notation difference between two published descriptions, not an error in either.

Both second candidates leave the 1-best output unchanged. What they change is lattice reachability: a published reading of each letter is in the candidate set, so an oracle over the beam can reach it.

## Deliberate divergences from the WikiPron gold

The spec follows the citation, not the gold's convention, in three places, and pays for each against that gold.

The gold writes ⟨j⟩ as /ʒ/, which Newman gives as the Niger pronunciation. Standard Kano Hausa has the affricate /dʒ/ (p. 538), and the spec writes that. The gold also writes ⟨ky gy⟩ as the palatal stops [c ɟ], and the spec follows Newman's palatalized velars /kʲ ɡʲ/.

Putting the flap first for ⟨r⟩ was measured and refused. On VoxCommunis it would improve the score, but that gold writes `ɽ` everywhere and never a bare `r`. It cannot represent the contrast, so the gain would be agreement with epitran, not accuracy. On WikiPron, which writes `r` more often than `ɽ`, the same order costs PER. Newman's remark that the flap is the native rhotic is about origin, not about text frequency.

### Word-final /n/

Newman gives word-final /n/ as pronounced [ŋ] (p. 539). The statement is strictly positional and says nothing about /n/ elsewhere. The spec encodes it that way, as a word-final candidate pair ⟨n⟩ → /n ŋ/, not as an unconditioned allophone of /n/.

The difference matters for the lattice. An unconditioned entry would generate a word-initial [ŋ] in *nasara*, an intervocalic [ŋ] in *kwana*, and a half-geminate [anŋ] for the final ⟨nn⟩ of *ann*. None of these is Hausa, and all of them would reach the lattice that downstream rescorers read. With the word-final entry, /n/ stays the broad transcription that both golds agree with, and [ŋ] stays reachable at word end. The spec also encodes ⟨nn⟩ as a digraph, so its second letter never resolves as an independent word-final /n/. Neither gold contains `ŋ`, so this buys no measured score. It stops the lattice from emitting a symbol that no gold can hold.

### Doubled digraphs

Gemination of a doubled digraph, ⟨kkw⟩ as /kʷkʷ/ and ⟨ssh⟩ as /ʃʃ/, follows Newman. "All Hausa consonants can be geminated", and where a digraph geminates only its first letter is written doubled (p. 540). *Gásasshee* 'roasted' is /ɡasaʃʃee/, with a geminate /ʃʃ/, not a plain consonant before the digraph. The spec encodes that closed set of doubled-digraph spellings in the grapheme table.

## Reading the WikiPron row

The `ha` WikiPron gold is entirely `Module:ha-IPA` output. Every headword in a random sample carried a bare `{{ha-IPA|<respelling>}}` template and no hand-typed IPA. The row therefore certifies reproduction of the module's tone- and length-marked respelling, not independent pronunciation accuracy. See [Module-generated WikiPron rows](../evaluation/datasets.md#module-generated-wikipron-rows).

The gold's IPA column marks tone and length in full, while its orthographic column carries neither. Almost all of the row's error is that mismatch, not rule error. The script `scripts/fold_ha_notation.py` measures it by folding the marks out of both sides. The `valid_ceiling` block in `ha.json` records the result. For the scores, see the [scoreboard](../evaluation/generated/scoreboard.md).

| Fold | What it shows |
|:--|:--|
| tone alone | removes most of the error, because tone is the more frequent mark |
| length alone | removes little, because a word that loses its length marks still carries a tone mark |
| tone and length | leaves a small residual, with most words then exact |

Counted as aligned edits, unwritten tone and length together make up nearly all of the total. The residual after both folds is the genuinely segmental error, and the ⟨r⟩ ambiguity is most of it: a gold /ɽ/ against a transcribed /r/. That gap is unrecoverable as well, but lexically, not notationally. The rest is the deliberate ⟨ky gy⟩ divergence, word-final ⟨f⟩ realised [p], dropped ⟨h⟩ in Arabic names, and single cases.

The orthographic column was checked directly. The only diacritic in it is the ⟨r̃⟩ rhotic mark, which the spec reads. No headword carries a macron, an accent, a doubled vowel, or any other tone or length cue, so no marked-orthography convention is left unread. Every letter in the headwords is in the grapheme table, so no character drops out silently. Two headwords, ⟨Ƴ⟩ and ⟨ƴ⟩, are the letter itself and not a word, which is negligible.

## Reading the VoxCommunis row

The gap between the two `ha` rows is notation, not rule quality.

The VoxCommunis gold carries no tone mark and no length mark. WikiPron carries tone on nearly every word and length on most. The VoxCommunis row is `epitran-derived`, and its phone tier writes epitran's notation only: `t͡s` and never `sʼ`, `ɽ` and never a bare `r`, `ɸ` and never a bare `f`, and no labialization mark `ʷ`. Each contested decision of the spec is therefore unscoreable on that row by construction. The decisions are ⟨ts⟩ as /sʼ/, ⟨f⟩ as /f/, and ⟨kw gw ƙw⟩ as unit /kʷ ɡʷ kʷʼ/. Agreement with that column measures agreement with epitran, and a loss there is the expected price of following the description.

Fold each gold's own notation out of both sides, and the two rows land close together. Tone and length come out of the WikiPron row. Epitran's exclusive `ɽ`, `ɸ` and `t͡s` and its unlabialized velars come out of the VoxCommunis row. One spec reads Hausa against two golds in incompatible notations. One gold marks two phonemic contrasts that the alphabet does not write. The other marks neither, and writes three segments in a convention the spec does not follow.

"Narrow transcription" is the wrong name for the WikiPron marking. Tone and vowel length are phonemic in Hausa. Schuh & Yalwa state that "Hausa has two distinctive tones" plus a falling tone on heavy syllables (p. 94), and that the vowel system is "five vowels, each with a long and a short counterpart" (p. 90). Newman states that the alphabet marks neither (p. 537). A transcription that writes them is a complete broad transcription. The deficient party is Boko, which underdifferentiates its own phonemes.

One real disagreement between the golds survives all the folding. Schuh & Yalwa say that [ʔ] "occurs predictably before words written in the standard orthography with initial vowels" (p. 91), and the spec writes it. WikiPron writes it too. VoxCommunis writes no initial glottal stop on any vowel-initial headword, which is the largest single part of that row's residual after folding. The spec follows the description and the human-notation gold, and pays those edits against epitran.

---
[← Ancient Egyptian](egy.md) · [Home](../index.md) · [Hindi →](hi.md)
