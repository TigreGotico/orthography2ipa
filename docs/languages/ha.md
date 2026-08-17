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
worth stating precisely. Measured over the 1857 scored items, ignoring tone
marks alone leaves about a third of the error (PER 0.5397 to 0.1747); ignoring
tone and length together leaves roughly a twentieth of it (PER 0.0292, with
84.7% of words then matching exactly). What remains after both is the
genuinely segmental error, and the largest single share of *that* is
the ⟨r⟩ ambiguity described above — also unrecoverable, but lexically rather
than notationally so.

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
