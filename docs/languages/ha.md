# Hausa (ha): a shallow orthography that hides tone, length and one consonant contrast

**Code**: `ha` | **Family**: Afro-Asiatic > Chadic > West Chadic | **Script**: Latin (Boko)
**Quality tier**: research
**Source read**: Newman, P. (1996), "Hausa Phonology", chapter 27 of A. S. Kaye & P. T. Daniels
(eds.), *Phonologies of Asia and Africa*, Eisenbrauns, pp. 537-552
([full text](https://scholarworks.iu.edu/dspace/bitstreams/f1d4231b-d713-4134-970c-071c5f8485ed/download)).
The consonant inventory is Table 27-1 on p. 538; the segmental discussion is pp. 539-540.

## Input contract

The spec reads **Boko**, the modified Roman alphabet introduced under British
administration and still the predominant writing system for Hausa in both
Nigeria and Niger. Ajami (Arabic script) is a different orthography and is not
modelled here.

Boko uses the ordinary Latin letters plus four hooked letters, ⟨ɓ ɗ ƙ ƴ⟩, and the
digraphs ⟨sh ts kw gw ƙw ky gy ƙy fy⟩. Niger spells ⟨ƴ⟩ as ⟨ʼy⟩; both spellings are
accepted and both transcribe alike, because they are one phoneme.

The apostrophe is a letter of the alphabet, not punctuation: it spells the
glottal stop, which reaches Hausa mostly through Arabic loans and is written
medially in words like *’addu’aa* 'prayer' and *saba’in* 'seventy' (p. 540).
The typewriter apostrophe U+0027, the modifier letter U+02BC and the curly
quotation-mark apostrophe U+2019 — the mark Newman's own citation forms use —
are all accepted and map alike. The two-letter ⟨'y⟩/⟨’y⟩ still wins the
tokenizer, so the glottalized approximant is never split into a glottal stop
plus /j/.

Mapping the quotation-mark apostrophe has a cost: nothing in the alphabet
reading distinguishes it from an actual quotation mark, so a quoted word now
picks up a spurious glottal stop at both ends — `'sannu'` comes out
`ʔsannuʔ`, and `don't` comes out `donʔt`. Word-initial ⟨ʔs⟩ is not a possible
Hausa onset, which is the tell that the source was punctuation rather than
the letter, but the spec has no way to act on that tell. The trade is kept
because leaving U+2019 unmapped drops the letter silently on every genuine
occurrence, which is the more common case and the one the spec exists to get
right.

Writing that marks the rhotic contrast — Newman's own citation forms — uses
⟨r̃⟩ for the tap or roll and leaves plain ⟨r⟩ for the flap (p. 539); the
gold's eight ⟨r̃⟩ headwords are the only evidence here for how widely that
convention is followed beyond Newman himself. The spec reads it: where the
diacritic is written, the flap candidate is excluded.

## What Boko does not write

Three things are contrastive in Hausa and absent from the spelling. Two of them
no grapheme-driven transcriber can recover at all.

**Tone.** Hausa has high, low and falling tone, all lexically and grammatically
contrastive, and the alphabet marks none of it. Newman states the point directly
for both tone and length (p. 537).

**Vowel length.** All five vowels have long and short counterparts, contrastive
in open syllables — *fiitoo* 'whistling' against *fitoo* 'ferrying'. In closed
syllables all vowels are short, which is predictable, but the open-syllable
contrast is lexical. Long vowels are sometimes written doubled in dictionaries
and teaching materials; standard Boko does not do it. Niger tried to make the
doubled spelling official and the attempt "proved to be a failure and was
eventually dropped" (Newman 1996, p. 537 n. 2).

**The rhotic contrast.** This one is different in kind, and the spec treats it
differently. Hausa contrasts an apical tap or roll /r/ with a retroflex flap
/ɽ/, and Boko spells both ⟨r⟩. The flap is the native Hausa rhotic; the roll
arrived through Arabic, Kanuri and English loanwords, through ideophones and
intensives, and through rhotacization of syllable-final alveolars (pp. 539-540).
Which rhotic a given word takes is a lexical fact with no cue in the spelling,
so ⟨r⟩ is encoded as an ordered **candidate pair** rather than a single guess:
both readings are in the lattice, and the ordering is a decoding default, not an
assertion about frequency. One position is deterministic — word-finally only
the roll occurs (p. 539) — and the spec declares that as a positional
constraint. It is not yet an enforced rule: the word-final entry unions with
the default candidate list rather than replacing it, so the flap reading
stays in the beam at word end and the roll wins there only when it already
sorted first by default. Making the constraint exclusive is separate engine
work.

## Hallmark correspondences

| Letter | IPA | Note |
|:--|:--|:--|
| ɓ, ɗ | ɓ, ɗ | laryngealized implosive stops |
| ƙ | kʼ | ejective; plain counterpart /k/ |
| ts | sʼ | ejective **fricative**, not an affricate; plain counterpart /s/ (p. 539) |
| ƴ, ʼy | j̰ | glottalized laryngealized palatal approximant; one phoneme, two spellings |
| c, j | tʃ, dʒ | affricates in Standard (Kano) Hausa |
| sh | ʃ | |
| kw, gw, ƙw | kʷ, ɡʷ, kʷʼ | unit labialized velars |
| ky, gy, ƙy | kʲ, ɡʲ, kʲʼ | unit palatalized velars |
| fy | fʲ | palatalized labial; lexically infrequent |
| r | r / ɽ | see above; word-finally the roll is declared but not enforced |
| r̃ | r | tap or roll only; the diacritic excludes the flap |
| ' , ʼ , ’ | ʔ | glottal stop; a letter, not punctuation |
| p | p | loan spellings only; not a native phoneme |

Kw, gw, ky and gy are phonemes rather than consonant-plus-glide sequences
because they contrast with the plain velars before /a(a)/: *gadaa* 'duiker',
*gwadaa* 'test!', *gyaɗaa* 'peanuts' (p. 539). Velars are also redundantly
labialized before back vowels and palatalized before front vowels — *doogoo*
'tall' is [doogwoo] — but that is predictable allophony the orthography never
shows, so the spec does not encode it.

Word-initial vowels take an epenthetic glottal-stop onset, since Hausa has no
vowel-initial syllables.

## Reading the wikipron row

The `ha` gold is entirely `Module:ha-IPA` output — every headword in a random
sample carried a bare `{{ha-IPA|<respelling>}}` template and no hand-typed IPA
— so the row certifies reproduction of that module's editor-typed
tone-and-length-marked respelling, not independent pronunciation accuracy;
see [Module-generated WikiPron rows](benchmarks.md#module-generated-wikipron-rows).

The `ha` wikipron row scores against a gold whose IPA column is fully marked for
tone and length while its orthographic column is stripped of both. Almost all of
the reported error is that mismatch rather than rule error, and the split is
worth stating precisely, with all four combinations measured rather than just
the two that move the most. Measured over the 1857 scored items: baseline PER
is 0.5340 (exact match 0.0022); folding tone marks out of both sides alone
leaves about a third of the error (PER 0.1690, exact match jumps to 0.2186,
since tone is the more frequent mark — 5477 combining tone diacritics against
2395 length marks in the gold IPA); folding length alone, leaving tone in,
barely moves it (PER 0.4565, exact match still 0.0022, because almost every
word that survives length-folding still carries at least one tone mark);
folding both together leaves about a twenty-fourth of the original error (PER
0.0223, with 89.1% of words then matching exactly). Tone is doing most of the
work in the combined number and length is doing almost none of it alone,
which is expected: length folds a single character class out of syllables
that mostly also carry a tone diacritic, so on its own it rarely turns a wrong
word into a right one. Counted as aligned edits — total Levenshtein edits
between the transcription and the closer gold, summed across the gold, before
and after folding each mark out of both sides — unwritten tone is 67.7% of the
total edit count and unwritten length a further 29.0%, so the two together are
96.7% of it. What remains after both is the genuinely segmental error, and the
largest single share of *that* is the ⟨r⟩ ambiguity described above — also
unrecoverable, but lexically rather than notationally so: 102 of the remaining
aligned edits are a gold /ɽ/ against a transcribed /r/.

The orthographic column itself was checked directly rather than assumed blank:
of the 1857 headwords, exactly 8 carry any diacritic at all, and all 8 are the
⟨r̃⟩ rhotic marking already described above (*bishar̃a*, *fetur̃*, *iƙir̃ar̃i*,
*mashar̃ci*, *mashawar̃ta*, *matukar̃*, *sanar̃wa*, *shawar̃a*) — the spec already
reads that mark. Zero headwords carry a macron, an accent, a doubled vowel, or
any other length or tone cue, so there is no marked-orthography convention
being left unread here: the ceiling is real, not a missed rule. The full
character inventory of the 1857 headwords was also checked against the
grapheme table and every letter is mapped; there is no silently-dropped
character behind the PER either. Gold composition was checked for the
padding pattern (alphabet-chart entries, bound morphemes) that turned up
elsewhere in this wave: two of the 1857 headwords, ⟨Ƴ⟩ and ⟨ƴ⟩, are the
letter itself rather than a word, at 0.1% of the set — negligible on its own
but recorded here rather than silently absorbed into the ceiling.

Reordering the ⟨r⟩ candidates to put the flap first was measured, on the
shipped spec, and refused. It would take the epitran-derived vox_communis row
from PER 0.1130 to 0.0692 and its exact match from 0.4937 to 0.6763, but that
gold writes `ɽ` 1380 times and a bare `r` not once — it cannot represent the
contrast, so the gain is agreement with epitran rather than accuracy. On
wikipron, the only `ha` gold whose IPA column is human notation, the same
reordering *costs* PER, 0.5340 to 0.5378; that gold writes `r` 366 times
against `ɽ` 236. The shipped ordering stays, and Newman's remark that the flap
is the native rhotic is a statement about origin, not about text frequency.

Two further divergences from that gold are deliberate. It writes ⟨j⟩ as /ʒ/,
which Newman gives as the Niger pronunciation, where Standard Kano Hausa has the
affricate /dʒ/ (p. 538); it also writes ⟨ky gy⟩ as the palatal stops [c ɟ],
where the spec follows Newman's palatalized velars /kʲ ɡʲ/ instead. Both cost
the spec against this gold and are paid for deliberately, on the citation
rather than on the gold's convention.

Word-final /n/ is a different case. Newman gives it as pronounced [ŋ] (p.
539), and that statement is strictly positional: it says nothing about /n/
anywhere else. The spec encodes it that way, as a word-final candidate pair
⟨n⟩ → /n ŋ/ and not as an unconditioned allophone of /n/. The difference is
not cosmetic. An unconditioned entry generates word-initial [ŋ] in *nasara*,
intervocalic [ŋ] in *kwana* and half-geminate [anŋ] for word-final ⟨nn⟩ as in
*ann* — none of which are Hausa — and those forms then enter the candidate
lattice that downstream rescorers consume. Confined to word-final position,
/n/ stays the broad transcription that every word-final-⟨n⟩ headword in both
golds agrees with, [ŋ] stays reachable at a word end, and the ⟨nn⟩ digraph is
encoded directly so its second letter is never resolved as an independent
word-final /n/ in the first place.

Gemination of a doubled digraph — ⟨kkw⟩ as /kʷkʷ/, ⟨sasshee⟩ as /saʃʃee/ — is
not a divergence from Newman; it is what Newman describes. "All Hausa
consonants can be geminated," and where a digraph is involved only its first
letter is written doubled, so *gásasshee* 'roasted' is /ɡasaʃʃee/, a geminate
/ʃʃ/, not a plain consonant before the digraph (p. 540). The spec encodes that
closed set of doubled-digraph spellings directly in the grapheme table.

## Reading the vox_communis row

The two `ha` rows move in opposite directions, and the reason is the notation
each gold is written in rather than the quality of the rules. Scored in one
session against one gold cache at a constant 3721 vox_communis and 1857
wikipron items, the Newman-based spec puts wikipron at PER
0.5397 where the previous spec had 0.5469, and vox_communis at PER 0.1129
where the previous spec had 0.1015, with exact match on that row falling from
0.5151 to 0.4937. The vox_communis row is a real loss and it is accepted
deliberately.

vox_communis is `epitran-derived`, and its `ha` phone tier writes epitran's
notation exclusively. Over the loaded gold: `t͡s` occurs 130 times and `sʼ`
never; `ɽ` occurs 1380 times and a bare `r` never; `ɸ` occurs 380 times and a
bare `f` never; the labialization mark `ʷ` never occurs at all. Every one of
this spec's contested decisions — ⟨ts⟩ as the ejective fricative /sʼ/, ⟨f⟩ as
/f/, ⟨kw gw ƙw⟩ as unit /kʷ ɡʷ kʷʼ/ — is therefore unscoreable on that row by
construction: the gold has no symbol that could reward them. Agreeing with
that column measures agreement with epitran, not accuracy, so a loss there is
the expected price of following the description instead. wikipron is the only
`ha` row whose IPA column is human notation, and it improves.

Neither gold contains a single `ŋ` — 0 occurrences across the 3721
vox_communis pairs and 0 across the 2176 wikipron pairs. Confining [ŋ] to
word-final position therefore buys no measured PER on either row; it stops the
lattice emitting a symbol no gold can contain. That is a notation and
lattice-purity result, not phonological progress, and it is worth exactly
that much.
