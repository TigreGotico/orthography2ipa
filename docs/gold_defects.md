# Gold defects

Every gold dataset in the harness has a provenance tier
([benchmarks.md](benchmarks.md), [quality_tiers.md](quality_tiers.md)), but a
tier only says where a transcription came from. It does not say whether the
transcription is *wrong about the language*. This page is the registry of the
specific, measured defects found in individual gold rows: cases where the gold
collapses a contrast the language makes, marks something the language forbids,
describes a different lect than its tag claims, or was produced by the system it
is being used to score.

Every figure below was measured directly against the cached gold in
`.benchmark_cache/`, using the same loaders the scoreboard uses, so any of them
can be reproduced. Where a figure differs from one recorded elsewhere in the
repository, both are given and the difference explained.

The registry exists because these findings determine what a reader may conclude
from a score. A PER of 0.56 on a row whose gold merges two tones is not a
statement about the spec. Fixing the spec toward such a gold is gold-fitting, and
the harness rules forbid it.

## What a defect class means

The class of a defect decides what can be done about it, so the registry is
organised by class rather than by language.

**Merged contrast.** The gold writes one symbol for two things the language keeps
apart. The information is destroyed, but the source data (the orthography) still
carries it, so the merge is in principle undoable by whoever owns the gold.

**Missing data.** The gold never encoded the contrast at all — no symbol for it
appears anywhere in the file. Nothing can recover it. The only honest options are
to exclude the row or to read it as a partial score over the subset it does
cover.

**Structurally impossible marking.** The gold places a mark where the language it
claims to describe cannot have one. This is a generator bug, not a transcription
choice, and it is correctable only upstream in the tool that produced it.

**Wrong variety.** The gold is internally consistent and possibly excellent, but
it describes a different lect than the tag it is filed under. Correcting it means
relabelling it, or replacing it with a gold for the variety actually named.

**Mixed conventions.** The gold merges two or more incompatible transcription
traditions into one file. Whether this is repairable depends on whether the
traditions separate cleanly, which has to be tested rather than assumed.

**Circular.** The gold derives from the system being scored, or from the same
authorship lineage that wrote the specs. The score measures self-agreement.

**False provenance label.** The recorded tier names a tool that was not, and
could not have been, used to produce the file. The number may still be usable,
but the reason a reader was given for trusting or distrusting it is wrong.

## A note on gating

`can_gate_promotion()` in `scripts/benchmark.py` decides whether a row may
qualify or block a language for the `production` quality tier. It refuses
`espeak-derived`, `epitran-derived` and `llm-generated`, because those are a
competitor's output or an LLM's, and accepts everything else.

The consequence is that the lattice does not run in the order a reader expects.
`machine-generated` — a rule script or an automatic annotator — **gates**, while
`epitran-derived` does not, because the objection to the competitor tiers is
circularity rather than quality. So the most consequential entries in this
registry are not the worst-transcribed ones. They are the ones on `crowd-scraped`
and `machine-generated` rows, which are free to block a promotion while carrying
a defect that has nothing to do with the spec.

## Merged contrast

### Vietnamese, `vox_communis`

The row loads 2,475 word types, of which 2,468 carry at least one tone letter.
The gold writes ⟨˨˨⟩ for two contrastive tones at once. Reading each headword's
tone off its orthographic diacritic — Vietnamese writes tone unambiguously, so
this is decidable per type — ngang (no diacritic) takes ⟨˨˨⟩ in 584 of its 590
types, and huyền (grave accent) in all 406 of its 406. No other tone class uses
the symbol, apart from one stray hỏi type. 991 types therefore contain ⟨˨˨⟩ and
967 have it as their only tone run, which is 39.1% of the row.

Ngang is a level tone and huyền is a low falling, often breathy, tone. They are a
minimal contrast in Vietnamese, and the gold gives them the same Chao letter, so
roughly two fifths of the row cannot distinguish a correct tone from an incorrect
one.

The row has a second, separate problem of placement. In 1,957 of the 2,468 toned
types (79.3%) the tone letter sits inside the rime with segments after it —
`t oː˨˨ j` for *tôi*, where the tone belongs to the syllable as a whole and is
conventionally written after it. Any spec that writes tone syllable-finally
mismatches those 1,957 types on position alone, independently of whether it got
the tone right.

Earlier records of this row report 566/590 for ngang and 401/406 for huyền, and
77.2% for the placement figure. Those did not reproduce; the values above are the
measured ones. The 39.1% coverage figure did reproduce exactly.

Provenance is `epitran-derived`, so the row cannot gate. Correcting it is not a
local matter: the tone merge lives in the VoxCommunis lexicons and would have to
be fixed by their maintainers. Rewriting the shipped gold here is forbidden.

## Missing data

### Abkhaz, `vox_communis`

Abkhaz has a large labialized consonant series, and the gold has no way to write
it. Of 76,459 raw word types in the file, 44,279 (57.9%) have `spn` — the forced
aligner's "spoken noise" marker, which the pipeline also emits for any word its
lexicon could not cover — in place of their phones. The remaining 32,180
scoreable types use exactly 35 distinct phone symbols, and not one of them
carries the labialization diacritic ⟨ʷ⟩. The inventory is `a b d f j kʲʼ kʼ l m n
pʼ qʲʼ qʼ r s t ts tsʼ tʃ tʃʲ tʃʲʼ tʼ v w z ħ ə ɡ ɡʲ ʃ ʃʲ ʒ ʒʲ χ χʲ` —
palatalization is present throughout, labialization is absent throughout.

The unmapped half of the file is not random. Eight Abkhaz letters are `spn` in
every single type that contains them: ⟨ә⟩ (30,743 types), ⟨ԥ⟩ (7,984), ⟨қ⟩
(7,058), ⟨ӡ⟩ (5,024), ⟨ҩ⟩ (4,035), ⟨ҿ⟩ (2,678), ⟨ӷ⟩ (1,741) and ⟨џ⟩ (811). The
gold's lexicon simply does not cover them, so the scoreable subset is
systematically the part of the vocabulary that avoids those letters. An earlier
record gives the denominator as 76,464; the numerator and the percentage
reproduce, the denominator is 76,459.

Nothing can be recovered here. A missing symbol cannot be inferred from a file
that never contains it, so the row is not correctable — only excludable, or
readable as a score over a biased subset. Provenance is `epitran-derived`, so it
cannot gate in any case.

## Structurally impossible marking

### Danish, `ipa_childes`

Danish stød is a laryngealization associated with a stressed syllable. Two rules
of the language bear on the gold: a stress group carries at most one stød, and
stød requires a stødbasis — a long vowel or a sonorant coda. A short vowel
followed by a voiceless stop cannot carry it.

The scored column (`ipa_g2p_plus`) writes stød as ⟨ˤ⟩, not ⟨ʔ⟩. Of 2,233 word
types, 1,302 carry the mark, 328 carry it twice or more, and 224 place it on a
short vowel immediately before a voiceless stop: *op* → `ɔˤp`, *ikke* → `eˤkə`,
*nok* → `nɔˤk`, *lidt* → `leˤt`. Multiple-stød types are ordinary bimorphemic
words, not compounds with two stress groups: *hedder* → `heˤðɔˤ`, *holder* →
`hɔˤlɔˤ`, *flere* → `fleˤɔˤ`.

The mechanism is visible by comparing the two IPA columns of the same file. The
raw `ipa_espeak` column marks 1,297 types with ⟨ʔ⟩, of which 110 are
**word-initial** — that is not stød at all, it is the epenthetic glottal onset
espeak-ng inserts before a vowel-initial word. 106 of those 110 reappear in the
scored column carrying ⟨ˤ⟩ on the vowel: *op* `ʔʌp` → `ɔˤp`, *også* `ʔʌsə` →
`ɔˤsə`, *ikke* `ʔekə` → `eˤkə`, *en* `ʔen` → `eˤn`. espeak-ng uses one symbol for
two unrelated things, and the G2P+ conversion reads every one of them as stød.
That single confusion generates the impossible stødbasis cases and inflates the
double-stød count.

The counts 328 and 224 reproduce exactly. The attribution does not: the earlier
record describes the defect in terms of ⟨ʔ⟩ in the scored data, and the scored
data contains no ⟨ʔ⟩ at all. The symbol is ⟨ˤ⟩, and ⟨ʔ⟩ is what the upstream
espeak column shows.

Correction belongs to espeak-ng and to G2P+, not here. Provenance is
`espeak-derived`, so the row cannot gate; it also cannot be read as evidence
about stød placement in either direction.

## Wrong variety

### East Timorese Portuguese, `portuguese_unified`

The `pt-TL` row draws on the `pt-TL-x-dili` region of the unified lexicon, and
that region is not independent Timorese lexicography. Diffed word for word
against `pt-PT-x-lisboa`, the two regions share 53,147 words. Restricting to the
35,800 shared entries whose transcriptions are the same length — where a
positional diff is meaningful — 90.6% of all 63,189 character differences fall in
six substitutions: ɐ→ə (30,042), u→ʊ (12,075), u→o (7,345), ʀ→r (4,186), ɐ→a
(1,858) and ɫ→w (1,724). Further down: d→ð (223) and ɡ→ɣ (150). A further 3,076
shared words are byte-identical between the two regions.

Re-spelling European Portuguese's centralized unstressed vowel with a different
symbol does not remove it. 60% of `pt-TL-x-dili` entries still contain a reduced
[ə] and 31% still end in a reduced [ʊ], and coda /s/ still surfaces as the Lisbon
*chiado*: gold *instrumentista* is `ĩʃtɾumẽntˈiʃtə` against Lisbon's
`ĩʃtɾumẽtˈiʃtɐ`. Albuquerque (2010:275 fn.7, 277), the source the `pt-TL` spec
is built on, documents the opposite for this variety — no unstressed-vowel
reduction and an alveolar, non-hush coda /s/. The row therefore measures
conformity to a re-symbolized European Portuguese, not to the acrolectal East
Timorese Portuguese the spec models.

The earlier record for this row gives ɐ→ə 28,713, u→ʊ 11,653, ʀ→r 3,994, ɫ→w
1,681, d→ð 212 and ɡ→ɣ 146. Those did not reproduce exactly — the direction and
magnitude hold, the counts are the ones above, measured over first-variant pairs
of equal length. The 53,147 shared-word count, the 60% and 31% residual figures,
and the *instrumentista* example all reproduced exactly.

This is the sharpest entry in the registry, because `pt-TL` is classified
`machine-generated` and **can gate**. The classification is already a deliberate
downgrade from the dataset-wide `lexicon-derived` tier, recorded in
`_PT_UNIFIED_PROVENANCE`, so a low PER here cannot be read as "the spec is
right". But the tier lattice still lets the row block a promotion, and it should
not be read as doing so on phonological grounds. The defect is not correctable
by transcription work; it needs a gold collected from Timorese speakers.

### Persian, `wikipron`

The WikiPron `fa` set is predominantly Classical or Early New Persian, not the
modern Iranian Persian the `fa` tag names. Measured over the file's 62,914 gold
segments, the classical reading wins on every diagnostic: ⟨aː⟩ 5,654 against
⟨ɒː⟩ 142, ⟨r⟩ 4,078 against ⟨ɾ⟩ 154, ⟨w⟩ 1,130 against ⟨v⟩ 24, ⟨q⟩ 880 against
⟨ɣ⟩ 332. The *majhūl* vowels that Iranian Persian merged into /iː uː/ centuries
ago are still present and frequent, ⟨eː⟩ 513 and ⟨oː⟩ 523, as is labialized
⟨xʷ⟩ 124 for ⟨خو⟩. Modern short /e o/ appear 139 and 106 times against classical
/i u/ at 2,796 and 2,075. Every one of these counts reproduced.

Describing Persian more accurately cannot improve this row. The only way down is
to transcribe Classical Persian under the tag `fa`, which would be false. The
correction is a relabelling — the gold is fine, its tag is wrong — or a
replacement gold scraped from a modern Iranian source. Provenance is
`crowd-scraped`, so the row **can gate**, which makes the mislabelling
consequential. Tracked as issue #107, and described at length in
[benchmarks.md](benchmarks.md) under "Variety mismatch (`fa`)".

### Algerian Arabic, `primary_sources`

The `ar-DZ` row on `primary_sources` holds exactly one gold pair: id
`guerrero2019-010`, زَوْجَتُه "his wife", filed against Guerrero (2019), which
in turn quotes W. Marçais's 1908 description of Tlemcen Arabic (W. Marçais,
*Le dialecte arabe parlé à Tlemcen*, 1902, is the same author's earlier
monograph on the same city). `per_ci_low` and `per_ci_high` both read 0.7143
in `benchmarks/results.json` because there is nothing to bound — a
confidence interval needs more than one row. Reading this PER as "the worst
row on the board" treats a single word as a certification of the whole
variety, which the harness's own `PROVENANCE` comment already warns against:
`primary_sources` rows "diagnose rules rather than certify a language on
their own."

The `ar-DZ` spec's baseline is old-urban Algiers, per Boucherit (2002); its
own sources cite Marçais's Tlemcen material only for the interdental-stop
isogloss, not as the target variety. Guerrero's example is genuinely
Algerian, but it is western-Algerian Tlemcen speech, not the Algiers
phonology the spec otherwise models, and it happens to carry a construct-
state contraction the spec was never built to reproduce: زَوْجَتُه surfaces
in Marçais's data as *zūžtăh* ['zuːʃtah] — the medial short /a/ of the
possessive suffix syncopates, the /aw/ of the first syllable contracts to
/uː/, and the resulting /ʒ/ devoices to [ʃ] before the voiceless /t/. The
spec renders the fully-vocalized input literally as ˈzawʒatuh: no syncope,
no contraction, no devoicing.

None of the three moves is an oversight. `DZ_SHORT_REDUCE`, the spec's one
syncope rule, already documents that short /a/ syncope (as opposed to /i/) is
deliberately scoped out pending an engine class that can except gutturals
and pharyngeals, precisely because a blanket /a/→ə rule over-generates. The
/aw/-contraction and cross-morpheme devoicing this single Tlemcen form shows
are additional phenomena with no other attestation in the spec's sources;
writing a rule to match one word would be gold-fitting on n=1, not a sourced
correction. Nothing here is fixed: the row is read correctly as too small to
diagnose anything beyond the one already-documented gap, not as evidence the
spec mishandles Algerian Arabic. Provenance is `expert-human`, so the row
technically **can gate**, but a promotion decision that turns on this single
word should not be read as phonological.

### Middle English, `wikipron`

The `enm` gold (`enm_latn_broad.tsv`, 18,272 readings over 6,466 distinct
headwords) is Wiktionary's crowd-scraped reconstruction of Chaucerian Late
Middle English pronunciation, and its vowel-length notation does not hold
still within a single headword. Counted on the harness's own SCORED
representation (each reading run through `benchmark.normalize(broad=True,
strip_stress=True)`, then deduplicated per headword) rather than the raw TSV
strings, 1,403 of the 6,466 headwords (21.7%) retain two or more distinct
normalized readings that differ from each other ONLY by the presence of the
length mark ⟨ː⟩ on a vowel — the same editor community disagreeing with
itself about whether a given vowel in a given word is long. (Counting the
same predicate over raw, un-normalized TSV strings instead gives 1,291
(20.0%); the two numbers diverge because narrow-mark and NFC folding merge a
few otherwise-distinct raw readings before the ⟨ː⟩ comparison runs. 1,403 is
the count that matches what actually enters the PER computation below, since
scoring always normalizes first.) Spot-checking the mismatches this produces
against the spec (`Irish` → gold /iːriʃ/, `Simon` → gold /simɔːn/, `amen` →
gold /aːmɛn/) shows length assigned to plain, unmarked vowel letters in
closed syllables with no orthographic signal the spec's macron-letter
graphemes (⟨ā ē ī ō ū⟩) could have used to predict it — length here tracks
Wiktionary's own open-syllable-lengthening reconstruction, not the spelling.

As-scored PER (n=6,466, `broad`, `strip_stress`) was measured at 0.2981
against a spec that had no grapheme entry for ⟨y⟩ anywhere — not in
`graphemes`, not in `positional_graphemes` — so the engine silently dropped
every ⟨y⟩ instead of erroring (`ymage` → `maɡɛ`, `yong` → `ɔnɡ`). ⟨y⟩ occurs
in 4,593 of the 18,272 gold readings (25.1%); of the first 400 such words,
356 have `j`, `i` or `ɪ` in the gold, so the character was being deleted, not
merely notated differently. With ⟨y⟩ encoded positionally (a glide /j/ before
a vowel — `yong`, `yarn`, `York` — and a vowel /i/ elsewhere, where it is a
graphic variant of ⟨i⟩ next to minim strokes, e.g. `ydel` matching `idle`;
Mossé 1952 and Jordan 1974 both describe this ⟨y⟩/⟨i⟩ alternation), plus
⟨x⟩ → /ks/ (191 occurrences, all realised /ks/ in the gold, e.g. `Oxenford`)
and ⟨ð⟩ as a thorn variant (11 occurrences, all realised [ð] in the sampled
gold), as-scored PER moves to 0.2620. In isolation: the ⟨y⟩ fix alone moves
0.2981 → 0.2652; adding ⟨x⟩ moves it to 0.2621; adding ⟨ð⟩ moves it to 0.2620,
a noise-level contribution given its 11 occurrences.

Folding the length mark ⟨ː⟩ out of both hypothesis and gold — the instrument,
not a rule change — now measures 0.2163 against the fixed spec, clearing the
0.25 production threshold: the row is input-limited by the gold's internal
vowel-length disagreement rather than by a spec defect. The previously
recorded 0.2538 folded figure was measured against the ⟨y⟩-dropping spec and
undercounted correct segments the fixed spec now produces; it does not add to
the new figure, it is superseded by it. Folding combining acute/grave/caron
accents alongside the length mark made no difference in either measurement
(the gold does not carry them for this row), a negative result recorded in
the spec's `valid_ceiling.wikipron.citation` rather than reported as part of
the fold.

Word-final ⟨-e⟩ shows the same instability: of the 2,350 headwords with an
orthographic final ⟨e⟩, only 12 have every reading realise it as [ə] and 416
have every reading drop it; the remaining 1,922 (81.8%) mix pronounced and
silent readings for the *same* headword. A naive fold (strip a trailing [ə]
from both sides whenever the headword ends in ⟨e⟩) was tried against the
fixed spec and still makes PER worse — 0.2772, up from the 0.2620 as-scored
figure — because plenty of the spec's correct [ə] outputs get stripped into
mismatches against gold readings that keep theirs. This is reported as a
negative result:
final-⟨e⟩ inconsistency is real and documented, but no defensible fold for it
was found, so no ceiling is recorded for it.

Headword spelling itself is not standardised: an adjacent-sort near-duplicate
scan (Ratcliff/Obershelp similarity > 0.86, length difference ≤ 2) over the
6,466 headwords finds 669 adjacent pairs plausibly belonging to the same
lexeme (dialectal/scribal spelling variants such as Northern vs. Midland
forms sitting side by side), which the harness's per-word multi-reference
scoring cannot merge because they are distinct headwords, not distinct
readings of one headword. This is a property of an unstandardised medieval
written language, not a defect: it is recorded here so a future reader does
not mistake it for spec breakage.

`enm` is the genealogical parent of `en-GB`, which carries zero `*_base` keys
of its own (its `graphemes`/`allophones`/etc. are fully self-contained) — so
nothing crosses from `enm` into `en-GB` or any further descendant. `en-US`,
by contrast, inherits from `en-GB` (not `enm`) through four `*_base` keys
(`graphemes_base`, `allophones_base`, `grammatical_endings_base`,
`word_exceptions_base`). A future audit of `enm` is safe to edit freely; an
audit of `en-GB` is not, since it is the actual base four other lects merge
data through.

Provenance is `crowd-scraped`, so the row **can gate**. `valid_ceiling.wikipron`
records the length-mark fold (0.2163, now below the 0.25 threshold — an
input-limited row) measured against the fixed spec; the final-⟨e⟩ negative
result and the diacritic no-op are recorded in the same citation rather than
as separate ceiling fields.

## Mixed conventions

### Coptic, `wikipron`

The Coptic gold merges reconstruction traditions rather than recording one. The
file holds 881 rows over 591 distinct spellings, and 155 spellings carry two or
more distinct readings. Symbols that belong to competing reconstructions appear
side by side across the file: ⟨ʔ⟩ in 181 readings, ⟨β⟩ in 68, ⟨x⟩ in 30, ⟨v⟩ in
19, ⟨θ⟩ in 8.

An earlier record gives 290 spellings with multiple readings. It does not
reproduce; the count is 155.

The obvious repair — split the file into two coherent systems, one plain and
short-voweled, one ejective and long-voweled — **was tested and does not work**.
Of the 881 readings, 536 are plain with no length mark and 38 are ejective with
length, but 307 are mixed: they combine a marker from one tradition with a marker
from the other. The Coptic gold cannot be cleanly separated by tradition, so the
only correction available is per-row tagging by someone competent in Coptic
philology. This negative result matters more than the counts: it closes off the
cheap fix.

Provenance is `crowd-scraped`, so the row **can gate**.

### Limburgish, `wikipron`

The `li` spec implements *Spelling 2003 voor de Limburgse dialecten* (the
Veldeke spelling), and states that Dutch-based and German-based ad-hoc spellings
are out of scope. The gold does not respect that boundary: it draws headwords
from Wiktionary's German-based, Rheinische-Dokumenta and Eupen-dialect
alternative forms alongside the Veldeke ones. The file holds 1,128 gold lines
over 989 distinct headwords, of which 123 are homographs with two or more
distinct readings — the orthography underdetermines the pronunciation, partly
through dialect variation and partly because Spelling 2003 does not write the
sleeptoon/stoottoon contrast at all. 90 gold lines, covering 55 distinct words,
carry an IPA tone letter that the orthography cannot supply. All of these
reproduced.

A useful negative result sits alongside them, recorded in the `li` spec notes:
folding the tone letters out of both hypothesis and gold moves PER only from the
board's 0.3819 to 0.3771, so unlike the
Hausa and Kikuyu tone folds, tone is not the dominant error source here. The
dominant driver is the spelling-convention mix, and mistranscribing an
out-of-contract spelling is the documented behaviour of the spec, not a defect
in it.

The convention mix is measurable from the gold's own spelling. Of the 140
headwords whose gold IPA contains a postalveolar fricative, 130 write it
`sch` and 7 write it `sj`, the Spelling 2003 form; `ae` appears in 10
headwords and `ao` in 14, against 114 carrying `ä` and 34 carrying `ü`. The
Veldeke convention the row is scored against is therefore a small minority of
the file. Two of the other conventions separate cleanly and do not overlap at
all: 89 headwords carry a sign that belongs to Rheinische Dokumenta and to
nothing else (`e̩`, `ǫ`, `ṣ`, `c͜h`), 222 carry the acute and diaeresis signs of
the Eupen-dialect spelling, and no headword carries both.

Rheinische Dokumenta is a published standard — the Landschaftsverband
Rheinland's transcription system for the dialects of the Rhineland (Honnen
1987) — so it gets its own entry, `li-x-rheindok`, per this repo's convention
that a distinct written convention for the same language is modeled separately.
It scores its 89 headwords at PER 0.0609 where `li` scores them at 0.3245, and
58 of the 89 come out exactly right. `li` is unchanged and keeps targeting
Spelling 2003. The Eupen block is left unmodeled: no published orthography for
it was found, and inferring a sign table from the gold it would then be scored
against is fitting, not describing.

The board still scores the whole file against `li`, so the row's PER is
unmoved at 0.3819. Splitting the gold by convention is upstream work at
Wiktionary or a local exclusion, not a spec change. Provenance is
`crowd-scraped`, so the row **can gate**. Tracked as issue #120. The `li` spec
carries the verdict as a machine-readable `mislabeled_gold` audit record.

### Scottish Gaelic, `wikipron`

The `gd` gold (3720 distinct headwords over 6000 lines) mixes two things that
the spec cannot follow at once. First, a notational split for the plain stop
series ⟨b d g⟩: the modern instrumental analysis (Nance & Stuart-Smith 2013,
summarised in Nance & Ó Maolalaigh 2020) finds "very little or no closure
voicing even in word-medial stops which are orthographically b d g" and
transcribes the series as an aspiration contrast, /pʰ/ vs /p/ — the analysis
this spec follows. 185 of the 3720 headwords instead carry the older
Borgstrøm (1940) / Oftedal (1956) devoicing convention, /b̥ d̥ ɡ̊/, for the
same sounds. Second, dialect mixing: 986 of the 3720 headwords carry two or
more mutually incompatible pronunciations (different stressed-vowel quality,
different presence/absence of preaspiration), consistent with WikiPron's
crowd-scraped, multi-contributor origin rather than a single consistent
variety.

A useful negative result sits alongside these counts. Two phenomena the
orthography genuinely underdetermines — preaspiration (`GD_PREASP_*`, already
encoded) and svarabhakti (an unwritten epenthetic vowel, not encoded — see the
`gd` spec notes) — were folded out of both hypothesis and gold and rescored.
Neither fold lowers PER: preaspiration folding moves the board's 0.3202 to
0.3205, and a svarabhakti fold moves it to 0.3264, both flat-to-worse. So
unlike the Hausa/Kikuyu tone folds and the Limburgish tone fold, neither
phenomenon is this row's dominant error source; the mixed devoicing
convention and the mixed dialects are the larger, harder-to-fold drivers.

Correcting the row means either normalising the two devoicing conventions in
the benchmark's IPA normalizer (a confusable fold, not a spec change) or
filtering to a single-dialect subset upstream at Wiktionary/WikiPron — neither
is a spec change. Provenance is `crowd-scraped`, so the row **can gate**.

### Middle High German, `wikipron`

The `gmh` spec's grapheme table targets Karl Lachmann's normalised MHG
orthography — circumflex for long vowels (â ê î ô û) and ⟨æ œ⟩ for the umlaut
reflexes (Paul, *Mittelhochdeutsche Grammatik*, rev. Klein/Solms/Wegera, 2007).
The gold (1724 source words, 1516 scored after tokenizer filtering) does not
use that convention: 0 of the 1724 words carry a circumflex vowel and 0 carry
⟨ë⟩, while 115 carry ⟨æ⟩ or ⟨œ⟩ and 130 carry ⟨ä ö ü⟩.

That is not a defect in the gold; it is a second, legitimate spelling
convention for the same language, and it is fully accounted for by English
Wiktionary's own style page (*Wiktionary:About Middle High German*), which
WikiPron scrapes: "certain letters with diacritics (ë ā ē ī ō ū ȥ) are not
used in article titles, but are used when displaying the word", while "this
does not apply to the umlauted vowels ä, ö, ü, æ, œ, which are treated as
separate letters and thus appear in titles like any other letter." That
policy predicts exactly the counts above — zero circumflex, zero ë, umlaut
vowels intact — because WikiPron scrapes the MediaWiki page title, not the
displayed headword line. Per this repo's convention that a distinct written
convention for the same language gets its own spec entry (`cdo-Latn-buc`
alongside `cdo`, `zh` alongside `zh-Hani`), this convention is modeled as
`gmh-x-wikt`, inheriting `gmh`'s phonology whole via `graphemes_base` and
nulling only the circumflex length graphemes, which this convention never
writes. `gmh` itself is unchanged and keeps targeting Lachmann's convention,
which is correct for edited MHG text using scholarly normalisation; the two
specs describe the same language in two different, both-real, spellings. The
`wikipron` gold should be scored against `gmh-x-wikt`, not `gmh` — see the
scoreboard note below.

The bare, non-doubled ⟨z⟩ grapheme is a separate, narrower unrecoverable case
that affects both specs equally: MHG ⟨z⟩ continues two different High German
Consonant Shift outcomes, an affricate [t͡s] (e.g. "herze", "heizen",
"gezogen") and a dorsal fricative [s] (e.g. "az", "biz", "daz"), and only the
doubled spellings disambiguate it unambiguously (⟨tz⟩ = geminate affricate,
⟨zz⟩ = geminate fricative — both fixed in the spec). Some editions mark the
fricative reflex with a diacritic z (ȝ/ȥ); this gold's source spelling does
not carry it, so the bare-z split is input-limited here and is left at the
affricate default rather than fitted to this one gold's distribution.

Provenance is `crowd-scraped`, so the row **can gate**; fixing the schwa
reduction, apical ⟨s⟩, and ⟨tz⟩/⟨zz⟩ gemination rules (all recoverable from
the gold's own spelling) moved PER from 0.2938 to 0.1022 at constant n=1516,
measured before `gmh-x-wikt` existed (i.e. still against `gmh`); re-scoring
against `gmh-x-wikt` is a follow-up, not part of this change.

### Kapampangan, `wikipron`

The `pam` spec's mid front vowel /ɛ/ is analysed as open-mid, following the
language's Wikipedia phonology summary (which in turn cites Forman 1971,
*Kapampangan Grammar Notes*, pp.28-29, for the language's stress system). The
gold never writes that symbol: 0 of 926 headwords carry ⟨ɛ⟩, while 119 carry
the plain ⟨e⟩ this spec's own transcribed vowel is not. The vowel letter is
written in both cases — only the IPA symbol choice differs — so this is a
notation-convention mismatch, not an unwritten contrast, and it is left
unfixed rather than mimicked: fixing the spec's phoneme to plain /e/ to match
one gold's transcription convention would be gold-fitting against a
Forman-sourced analysis. Folding ⟨ɛ⟩ to ⟨e⟩ on both sides moves this row's PER
from 0.2861 to 0.2586 in isolation; it is not counted toward the spec's
`valid_ceiling` for this row (see `pam.json`), which is reserved for
phenomena the orthography genuinely cannot write (the glottal stop and the
lexical, unmarked stress that drives the /a/~[ə], /i/~[ɪ], /u/~[ʊ]
alternation).

The same file also carries plain crowd-scraped noise: 48 of its headwords
recur with two or more mutually incompatible readings for the identical
spelling (e.g. "Guagua" → ɡwaɡwə vs wawəʔ, "anak" → ənak vs anək), consistent
with unpredictable per-annotator stress placement rather than a systematic
convention split. Provenance is `crowd-scraped`, so the row **can gate**.

## Circular

### Portuguese and Arabic TTS gold (`portuguese_tts`, `arabic_tts`)

Both datasets sit at PER exactly 0.0000 on every row. `portuguese_tts` has 47
rows and `arabic_tts` has 34, all 81 at zero, all `llm-generated`, and every
single row at n = 20. Nothing in either dataset is anything other than a perfect
score on twenty items.

The reason is circularity. The transcriptions were drafted by a large language
model and then audited against the literature; the harness's own provenance
comment on the sibling `gold20_arabic` dataset calls it "near-circular, same
Claude lineage that authored the o2i Arabic dialect specs". The same lineage
authored these. A perfect score against a gold written by the same authorship
that wrote the spec measures agreement between two expressions of one belief.

Both are `llm-generated`, so neither can gate, and the tier is correct. The
defect is not that the number is used wrongly by the harness — it is that the
number looks like a result and is not one. No amount of auditing converts it;
only an independently collected gold would.

For completeness: 82 rows on the scoreboard sit at PER exactly 0.0000, not 81.
The 82nd is `tew` / `wikipron`, n = 106, `crowd-scraped` — a different situation
from these two datasets and not part of this registry.

## False provenance label

### Abkhaz, `vox_communis`

The `ab` row is recorded as `epitran-derived`, and epitran cannot have produced
it. epitran 1.35.2 ships 161 grapheme-to-phoneme maps in `epitran/data/map/`, and
none of them is Abkhaz — there is no `abk` map and no `ab` map of any script.
Whatever built the Abkhaz phone tier, it was one of the other tools in the
VoxCommunis pipeline (XPF, Charsiu, or a custom dictionary), not epitran.

The dataset-wide `epitran-derived` tier is a reasonable default for VoxCommunis
as a whole, since its lexicons are built from a mix of tools and the tier is
deliberately pessimistic. But for this particular row the label names a specific
competitor, and the identity of the competitor is precisely what the tier
name exists to communicate — a reader is being told to interpret the row as
divergence from epitran, and there is no epitran output to diverge from.

The practical effect is nil, because `epitran-derived` and the alternatives all
refuse to gate. The correction is a naming one: the row should carry a tier that
does not assert a tool that was not used.

---
[← Gold composition](gold_composition.md) · [Home](index.md) · [Known limitations →](known_limitations.md)
