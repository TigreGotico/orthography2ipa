# Known limitations

Language specs in this repository carry prose notes that describe things the
spec does not do. The phrasing is uniform — "not modelled", "left unencoded",
"known miss", "DECLARED GAP" — but the phrasing hides four very different
situations, and only one of them is a defect worth fixing.

This page separates them. A note that says "not modelled" because the language
uses a second script nobody feeds to the engine costs nothing. A note that says
"left unencoded" about a contrast the spelling plainly marks is a bug with a
measurable price.

Across the spec set, 214 specs carry 277 such mentions. Of those specs, 80 have
no gold dataset at all, so their claims cannot be checked against data and
cannot be sized; what follows separates measured claims from unmeasurable ones
throughout.

## The four classes

**Deliberate scope limits** are design boundaries. A secondary script, a
neighbouring dialect, a morphological process that belongs downstream. These
need no issue and no fix. Roughly 79 specs are in this class.

**Engine limitations** are things the rule layer genuinely cannot express, where
the spec author correctly identified the obstacle. These need an engine change
or an explicit refusal with a reason, not a spec edit. Around 21 specs name an
engine or rule-layer obstacle directly.

**Unwritten contrasts** are cases where the orthography does not encode the
thing at all. The spec is behaving correctly and the note is describing an error
floor. These should be quantified against gold, not fixed. Around 114 specs are
in this class, tone and stress exemptions dominating.

**Parked defects** are the ones that matter: the trigger is visible in the
spelling, the engine can express the rule, and the gold shows the engine getting
it wrong. Thirteen are confirmed and sized below.

## Parked defects

Each entry gives the language, what the spec says, and how many gold words the
engine currently transcribes wrongly on account of it. Sizes are measured
against the cached gold by running the current engine, not estimated.

**Thai, bare ⟨ว⟩ before a coda — 407 words.** The spec states plainly that
"the bare-⟨ว⟩-before-a-coda spelling is NOT handled: ⟨ขวด⟩ still reads its ⟨ว⟩
as an onset glide." It reproduces: `ขวด` returns `kʰwot̚˨˩` where the gold has
`kʰua̯t̚˨˩`. Of 561 gold words with a consonant–⟨ว⟩–consonant sequence, 407 have
the `ua̯` nucleus in gold and do not get it from the engine. This is the largest
single sized defect in the spec set.

**Kildin Sami, palatalisation signs — 258 words.** The spec calls the
suprasegmental palatalisation signalled by ⟨ь ҍ ъ⟩ "mostly orthographically
silent" and leaves it unencoded as an engine-limit gap. The gold disagrees: of
273 words containing one of those letters, 258 carry a `ʲ` in the gold
transcription that the engine never produces. The sign is contiguous and
visible in the spelling, so the engine-limit framing does not hold.

**Yoruba, syllabic nasal before a consonant — 160 words.** The spec's first
listed known gap. It reads ⟨n⟩ before a consonant as plain `/n/`, arguing that
the gold splits between a nasal vowel and a syllabic `[ŋ]` for medial ⟨Vn⟩+C.
The split is real, but on the narrower question of the syllabic nasal the gold
is one-sided: 160 of 565 candidate words have `ŋ` in gold and none of them get
it from the engine.

**Wiyot, non-initial ⟨h⟩ — 49 words.** The spec already states the number, and
the number is right. Of 151 gold words, 61 contain a non-word-initial ⟨h⟩ and 49
are standalone ⟨h⟩ subject to the `h~[ʔ]` allophony; all 49 come out with `h`
where the gold has `ʔ`. The conditioning is purely positional, which the rule
layer expresses elsewhere, so the exemption looks avoidable.

**Sranan Tongo, Dutch-influenced spellings — 29 words.** "Older Dutch-influenced
spellings are common in the wild and are not handled." Twenty-nine gold words
carry them, and the engine passes the digraphs through untouched: `boegroe`
returns `boeɡɾoe` against a gold `buɡɾu`, and `basja` returns `basa` against
`baʃa`.

**Lao, coda ⟨ລ ຣ⟩ — 18 words.** The spec explains the trade-off honestly: adding
a coda-liquid rule misread the onset `/l/` of ⟨ຫຼວງ⟩ and ⟨ຕຳຫຼວດ⟩. The scope is
small — 18 gold words end in one of those letters — and a rule conditioned on
word-final position rather than the general coda would not touch the onsets that
caused the reversal.

**Lashi, ⟨a⟩ before a labial coda — 7 words.** "Also left unencoded is the
fronting of ⟨a⟩ to [æ] before a labial coda that the Waingmaw transcriptions
show." Thirteen gold words have ⟨a⟩ before a labial; seven have `æ` in gold and
none get it. The trigger is a two-grapheme window.

**Jamaican Creole, ⟨ky⟩ and ⟨gy⟩ onsets — 5 words.** The spec declines to model
the palatalised onsets. The gold writes them as `ʲ` on the preceding consonant
(`gyal` → `ɡʲal`); the engine emits `ɡjal`. Five gold words are affected.

**Thai, ho nam standing mid-word — 5 words.** The claim as written overstates
its own scope, and the corrected size belongs here rather than in the failed
list, because the residue is real. See the note under failed reproductions.

**Lao, ho nam — 4 words.** Same shape as the Thai case: of 302 gold words with
⟨ຫ⟩ before a sonorant, four get a spurious `/h/`.

**Passamaquoddy-Maliseet, intervocalic voicing — 2 words.** "Stops and s are
voiceless underlyingly but voice intervocalically, which is left unencoded."
Sixty-four gold words have the intervocalic environment; only two show the
voicing in gold. The claim is true and its cost is nearly nil.

**Plains Cree, intervocalic voicing — 1 word.** The same claim in the sibling
spec, with the same outcome: 96 candidate environments, one gold word showing
the voicing.

**Bouyei, apical vowel after ⟨s⟩ and ⟨z⟩ — 1 word.** "The apical vowel that
Chinese loans have after s and z is not modelled, so ⟨siy⟩ ⟨zij⟩ come out with
i." Exactly one gold word, `siyzij`, is affected.

## Claims that do not reproduce

These notes describe a gap that the data does not show, or show at a scale far
below what the wording implies. A note that misdescribes the engine is worse
than no note, because it sends a maintainer looking for a defect that is not
there.

**Yoruba, geminate vowel after a nasal onset.** The spec records a second known
gap: "a written geminate vowel after a nasal onset (⟨maapu⟩, ⟨ibomii⟩) does not
reliably nasalise both vowel slots." Thirty-one gold words have a nasal onset
followed by a doubled vowel. Only four carry nasalisation in gold at all, and
the engine misses none of them. There is nothing to fix.

**Thai, ho nam standing mid-word.** The note says such cases are "not reached
either". The general case is reached: of 967 gold words with a word-internal
⟨ห⟩ before a sonorant, only five receive a spurious `/h/`. The specific example
the note gives does reproduce — ⟨พหล⟩ returns `pʰol˧` — so a narrow residue
exists, but the claim as written is roughly two hundred times larger than the
measurement.

**Central Atlas Tamazight, unmarked gemination.** "Consonant gemination is not
marked in the script and is left unencoded." The gold carries no length marking
anywhere across its 690 entries, so the omission has no measurable cost and does
not contribute to the error floor the note implies.

**Zulu, long vowel on the ⟨i-⟩ augment.** The note reports that the gold writes
a long vowel on 46% of three-syllable and 29% of four-syllable ⟨i-⟩ nouns and
that nothing separates the two groups. The engine already emits a length mark in
all 875 gold words beginning with ⟨i⟩, so the residual is one of placement, not
of an absent feature.

**Catalan, the wave-2 known miss.** The note flags one miss among the closed-class
entries it added. None of the words named — the auxiliary ⟨he⟩, the possessives,
the suppletive infinitives — occur anywhere in the Catalan gold, so the claim
cannot be sized and no regression guard covers it.

**Chuvash, the reduced-vowel stress skip.** The stress note explains that the
declared final position is "wrong for one ending in ӑ/ӗ". No gold word ends in
either letter, so the described failure mode never fires against the data the
project scores.

## Unmeasurable claims

Eighty of the 214 claim-bearing specs have no gold dataset. Their notes may be
right or wrong; nothing in the repository can tell. Among them are several whose
wording suggests a sizeable defect — Fon's unmodelled nasal vowels, Ga's
unmodelled vowel doubling, Bislama's unmodelled labialisation, Tyap's fortis
doubling, Kokborok's unencodable `/ə/` — all of which describe triggers plainly
visible in the spelling and would belong with the parked defects if a gold set
existed to price them. Acquiring gold for these languages is the prerequisite
for acting on their notes.

Two further claims are unmeasurable for a different reason: Kabyle's
labiovelarised `kʷ gʷ` and Riffian's ⟨ř⟩ never appear in their respective gold
orthographies, so the graphemes the notes discuss are absent from the data.

## Measured ceilings worth keeping

Some unwritten-contrast notes carry numbers, and the numbers hold. These are not
defects and should not become issues; they are the honest floor of what the
orthography permits.

Classical Syriac's spirantization note claims 8 `/θ/`, 5 `/ð/`, 4 `/f/` and 2
`/v/` tokens in gold against an input that never carries the quššaya and rukkakha
dots. Nineteen gold words are affected, matching the stated token count. Turoyo
records the same alternation from unpointed text at a larger scale: 56 of 232
gold words carry a spirantized reflex that the consonantal spelling cannot
predict. Both are correctly left unencoded.

## Reading a note in a spec

The distinguishing question is whether the trigger is visible in the input
string. If it is — a letter, a digraph, a diacritic, a position in the word —
then "left unencoded" is a defect claim and should carry a measured size. If it
is not, the note is describing either a scope decision or an error floor, and
the honest form of the note is a number rather than a promise.
