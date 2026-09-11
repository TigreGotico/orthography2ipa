# Ranking error: where the beam has the answer and ranks it wrong

The [scoreboard](scoreboard.md) reports both a 1-best PER and an
**oracle PER@k** — the per-word minimum over the engine's top *k*
readings. The gap between the two is *ranking* error: the beam already
holds a better reading and puts it in the wrong place. What is left at
oracle@k is *model* error: no reading in the beam is any better.

For French that gap was most of the story. Before this pass,
wikipron/fr scored PER `0.0951` against an oracle@5 of `0.0682`. This
page records how that was attributed, what came of it, and — as
importantly — which of the candidate fixes were measured and thrown
away.

## Method

`scripts/rank_diag.py` takes a random sample of a dataset row, keeps
every word where some top-*k* reading beats the 1-best, and aligns the
two beam paths **slot by slot**. Each disagreement is bucketed by
`(grapheme, chosen IPA → better IPA, flat-table or positional
override)`, which names the single decision that went wrong rather than
the whole word. Sampling is random over the full corpus with a fixed
seed: the corpora are alphabetically ordered, so a `--limit` prefix is a
sample of the letter A, not of the language.

`scripts/rank_sweep.py` dumps per-word PER for one engine state, so two
states can be diffed word by word and bucket by bucket. **Every
"rejected" verdict below is a sweep, not an opinion.**

`<unaligned>` counts words where the two paths have different segment
counts (a grammatical-ending rewrite or an allophone expansion changed
the slot count), so no per-slot blame can be assigned.

## French, before

2000-word random sample of wikipron/fr, top-1 PER `0.1276`, oracle@5
`0.0975`, 348 words where the beam ranks a better reading below the
winner.

| Mechanism | Words | Examples | Verdict |
|---|---:|---|---|
| ⟨e⟩ `ɑ̃`→`e` in verbal ⟨-ent⟩ | 77 | munissent, convoquèrent, rétablissent | **rejected** — see "verbal ⟨-ent⟩" below |
| ⟨ai⟩ `ɛ`→`e` | 43 | dépérirai, emménagerai, railway | not expressible; word-final ⟨ai⟩ (95% `e`) and ⟨ais⟩/⟨ait⟩/⟨aient⟩ (99% `ɛ`) both look word-final to `effective_word_end` |
| ⟨r⟩ `∅`→`ʁ` word-final | 37 | indicateur, nageur, rebonjour | **fixed (data)** |
| ⟨e⟩ `ə`→`e` | 37 | guetteur, ferraillant, resserreras | loi de position on ⟨e⟩ — not reachable, see "rejected" |
| ⟨eu⟩ `ø`→`œ` | 30 | escrimeur, chasseur, bronzeurs | **fixed (mechanism + data)** |
| `<unaligned>` | 29 | fouetter, hamburger | slot counts differ; no per-slot blame |
| ⟨s⟩ `∅`→`s` word-final | 17 | albatros, madras, gens, consensus | lexical (loans); a lexicon, not a rule |
| ⟨o⟩ `ɔ`→`o` | 16 | forêt, monochrome, protoplasme | **measured and rejected** (below) |
| ⟨y⟩ `i`→`j` | 13 | abstrayais, incroyables, cyan | candidate order; plausible next data fix |
| ⟨s⟩ `s`↔`z` | 23 | pléonasme, œcuménisme / présupposeras | intervocalic ⟨s⟩ in learned compounds; the compound boundary is invisible |
| ⟨t⟩/⟨p⟩ `∅`→ pronounced | 15 | inuit, Christ, cégep, Alep | lexical |
| ⟨x⟩ `ks`→`ɡz` | 8 | exaltation, réexaminâmes | ⟨ex⟩ + vowel voices to `ɡz`; needs a `before_vowel` entry on ⟨x⟩ |

## French, after

Same sample: top-1 PER `0.1224`, oracle@5 `0.0961`, 310 ranking failures
(was 348). Full corpus: PER `0.0951` → `0.0891`, oracle@5 `0.0682` →
`0.0668`, exact match `0.5974` → `0.6179`. The ranking gap fell from
`0.0269` to `0.0223`.

Every oracle number on this page — like every oracle cell on the
scoreboard — is measured **without injected alternatives**, i.e. with
list-valued `grammatical_endings` entries contributing nothing to the
beam. The single exception is the explicitly labelled
injected-alternative block under "Verbal ⟨-ent⟩" below, which exists to
report that movement and is labelled precisely so it cannot be read as
one of these numbers. That is what makes `PER − Oracle@k` readable as ranking error at
all: an injected alternative lowers an oracle by construction, so
folding it in would mark our own diagnostic to our own edit. See
[`benchmark_methodology.md`](benchmark_methodology.md#injected-alternatives-do-not-count-as-ranking-error);
the movement ⟨-ent⟩ does cause is reported there, separately, as
reachability.

For scale: espeak-ng scores `0.0740` on the same row. French does **not**
beat espeak here and this pass does not claim to — it closes about 28%
of a `+0.0211` deficit, leaving `+0.0151`.

## Dutch

500-word random sample of wikipron/nl, top-1 PER `0.1807`, oracle@5
`0.1470`, 117 ranking failures. Far more concentrated than French:
**94 of 117 failures are a single grapheme, ⟨e⟩.**

| Mechanism | Words | Examples | Reading |
|---|---:|---|---|
| ⟨e⟩ `ə`→`ɛ` | 35 | elektronisch, afkerven, aanhelpen | stress placed on the wrong syllable, so the reduction rule fires where it should not |
| ⟨e⟩ `ə`→`eː` | 29 | conformeren, adverteren, betweterig | open-syllable lengthening not reaching this word |
| ⟨e⟩ `eː`→`ə` | 18 | gezichtspunt, beschadiging, eraan | the mirror case: a prefix syllable that should reduce |
| ⟨e⟩ `ɛ`→`ə` | 12 | verbrandingsoven, besneeuwen | same |
| ⟨v⟩ `v`→`f`, ⟨g⟩ `ɣ`→`x`, ⟨z⟩ `z`→`s` | 23 | opvanghuis, bloedgroep, datzelfde | devoicing at a COMPOUND-internal boundary, which the word-level `word_final` rule cannot see |

**No Dutch change ships**, and the reason is not the one you would guess
from the table. Dutch **already implements open-syllable lengthening**,
in `allophone_rules` (`followed_by_2=vowel`, Booij 1995 ch. 2 — see
`nl.json`'s notes). Declaring the aperture positions on top of it made
things worse, not better (below). Dutch's residual ⟨e⟩ error is stress
placement and compound segmentation, not a missing aperture vocabulary.

## What was fixed, and at which level

**Mechanism.** Six new `GraphemePosition` values —
`OPEN_SYLLABLE`, `CLOSED_SYLLABLE` and the four stress-crossed
`NUCLEUS_{STRESSED,UNSTRESSED}_{OPEN,CLOSED}` — let a spec condition a
nucleus on whether its syllable has a coda: the environment the Romance
*loi de position* is stated in (Fougeron & Smith 1993; Tranel 1987
ch. 4, both in `fr-FR`'s `sources`). Aperture is read off the spec's own
syllabification of the ORTHOGRAPHIC word, minus, in the last syllable,
the trailing graphemes the spec itself emits nothing for — so French
*heureux* is open (mute ⟨x⟩), *beuh* is open (mute ⟨h⟩), and
*chanteurs* is closed (mute ⟨s⟩ over a pronounced ⟨r⟩).

Syllabification was also decoupled from `spec.stress`, which had hidden
aperture from every stress-less spec, French among them. Both the
syllabification and the per-nucleus aperture computation are gated on
the spec actually declaring one of the six keys, so a spec that does not
use the feature pays nothing for it — measured at parity with `dev` on
`hi` and `de`.

**Ending matcher.** `match_grammatical_ending` matched only endings that
began exactly at a grapheme-token boundary, so an ending starting
*inside* a digraph was silently invisible. It now matches on the word's
trailing **letters** and rounds the covered span outward to whole
tokens. This is a latent-bug fix with no French consumer: it repairs
English ⟨-cious⟩/⟨-cial⟩/⟨-cian⟩ over the ⟨sc⟩ digraph — *conscious*,
*luscious*, *Gramscian*, *fascial* — 10 words on wikipron/en-GB, 10
wins, 0 losses.

**Data (fr-FR only).** Two changes, each cited in the spec's `notes`:

1. `r.word_final` `[""]` → `["ʁ", ""]`. Word-final ⟨r⟩ IS pronounced;
   the mute case is the ⟨-er⟩ sequence, which `grammatical_endings`
   already owns. Measured on the gold set: after ⟨e⟩ it is silent in
   96.5% of 7108 words, after any other letter it is pronounced in
   ~99% of 2313.
2. `eu` gains `open_syllable: ["ø", "œ"]` / `closed_syllable:
   ["œ", "ø"]`.

## Measured and rejected

### Verbal ⟨-ent⟩ — rewrite rejected, ambiguity now exposed

A `grammatical_endings` `"ent": ""` entry (3PL inflection is mute:
*ils parlent* [paʁl]) wins **3844 wikipron/fr types against 254
losses** — a 94% win rate and, on its own, `0.0891` → `0.0754` PER.
It is **not shipped.**

The 254 losses are the nominal/adjectival ⟨-ent⟩ class: *vent, dent,
cent, argent, accent, talent, absent, serpent, Occident, Vincent*. Type
PER counts each of those once, exactly like the inflected verb forms it
wins; running text does not. This library feeds TTS, where saying "v"
for *vent* is not paid for by 3844 rare verb forms.

It also fails `grammatical_endings`' own stated precondition (see
`types.py`): the counter-set must be **closed** and live in
`word_exceptions` — the way French ⟨-er⟩ keeps *mer*, *hiver*. French
⟨-ent⟩ nouns and adjectives are not closed, and the proper nouns
(*Laurent*, *Florent*, *Clément*) are open-ended. Verb-vs-noun is not
decidable from spelling; it needs part of speech, which this layer does
not have. Deferred to a morphology-aware pass.

A `"ment": "mɑ̃"` companion entry existed only to defend against
`"ent"`. Without `"ent"` it is unnecessary — the nasal ⟨en⟩ plus a
silent ⟨t⟩ already give *rapidement* [ʁapidəmɑ̃] — so it is gone too.
It was also actively harmful while the token-alignment defect stood:
⟨mm⟩ is one token, so ⟨-ment⟩ could not match in the ⟨-amment⟩/
⟨-emment⟩ adverb class and *comment* → [kɔm], *apparemment* → [apaʁəm],
**131 losses against 7 wins** in that bucket.

**What ships instead.** Rejecting the rewrite is not the same as
accepting the output. Part of speech belongs to a downstream rescorer
(owner ruling: o2i takes no POS input), and a rescorer can only fix what
the beam contains. It did not contain [paʁl] at any width — a coverage
hole, not a ranking error. French now declares

```json
"ent": [null, ""]
```

a **deferring candidate list**: `null` at element 0 keeps rank 1
exactly where it was, and the mute reading is added below it. Measured
on a 300-word sample of the gold-mute ⟨-ent⟩ class, gold-in-top-10 goes
**0 → 192**, and exact@1 stays **0** — as it must, because o2i is not
the layer that decides.

> **Injected-alternative movement — NOT ranking error, and not on the
> scoreboard.** The oracle figures in this indented block are the one
> place on this page measured WITH the injected alternative exposed
> (`expose_ambiguous_endings=True`). They are reported as *reachability*
> and must never be folded into a `PER − Oracle@k` headroom figure, a
> ranking-failure count, or a cross-system claim — adding candidates to
> a beam lowers an oracle by construction. On the full 85495-word
> wikipron/fr row, measured with `expose_ambiguous_endings` off then on:
> oracle@5 `0.0665` → `0.0627` and OracleX@5 `0.6712` → `0.6888`, while
> PER `0.0888` and exact match `0.6185` are identical in both modes —
> which is the proof that an injected reading never reaches rank 1.
> Oracle@3 does not move at all (`0.0723`), because the mute reading
> lands at rank 4-5. The scoreboard publishes only the without-injection
> numbers. See
> [`benchmark_methodology.md`](benchmark_methodology.md#injected-alternatives-do-not-count-as-ranking-error).

See [SCHEMA.md](../orthography2ipa/data/SCHEMA.md#ambiguous-endings).

⟨-ment⟩ is deliberately *not* declared alongside it. It is the same
ambiguity (*dorment*, *ferment* are mute; *moment*, *comment* are not),
so shielding it with a longer entry would re-open the coverage hole for
exactly the verbs this fixes.

### ⟨o⟩ under the loi de position

Declared and measured: **+4.4 PER points** on wikipron/fr. French ⟨o⟩ is
`[ɔ]` in most open syllables too (*moto*, *protoplasme*), so the law is
far weaker for it than for ⟨eu⟩. Shipped as nothing rather than as half
a rule.

### Dutch aperture

Declared for ⟨e⟩ and for ⟨a o u⟩, measured, reverted: PER `0.1604` →
`0.1816` (⟨e⟩ only), `0.2282` (⟨a o u⟩), `0.2496` (both). Two reasons,
both disqualifying at the time: Dutch already lengthens in
`allophone_rules`, so the positions duplicate a better-targeted rule;
and the syllabification underneath was not good enough —
`_syllables_for` maximised the onset without consulting phonotactics, so
*elektronisch* came out `e·le·ktro·nisch` with an illegal `ktr` onset
and a spurious open `le`. It also ignored `stress.max_onset` entirely.

The second reason no longer holds: the syllabifier now constrains
onset maximisation by the licit onsets of the language (see
`_OnsetJudge` in `orthography2ipa/stress.py`), and *elektronisch* is
`e·lek·tro·nisch`. The Dutch aperture data wave is therefore worth
re-measuring against the corrected boundaries; the first reason
(duplication with `allophone_rules`) still stands and has to be
answered before any of it ships.

## Known gaps this pass does NOT close

- **The loanword ⟨-er⟩ class.** 138 of 6211 word-final ⟨-er⟩ types keep
  a pronounced /ʁ/ — *Jupiter, laser, cancer, Esther, Asperger*, and a
  long tail of English and German loans and toponyms. The final-⟨r⟩
  inversion does not reach them, because the ⟨-er⟩ *grammatical ending*
  rewrite runs after the beam and silences the whole ending regardless.
  Only `word_exceptions` (or a loanword-aware layer) can reach them;
  the spec already lists a handful (*revolvers*, *leaders*, *pokers*).
- **Verbal ⟨-ent⟩**, above: needs part of speech, so o2i
  exposes both readings and ranks neither well.
- **Compound-internal boundaries**, in both languages: French
  intervocalic ⟨s⟩ in learned compounds, Dutch devoicing.

## Follow-ups (designs, not built)

1. ~~**A sonority-aware orthographic syllabifier** that honours
   `stress.max_onset`.~~ **Built,** for the specs that opt in with
   `constrain_onsets` (`de-DE`, `nl`, `fr-FR` — the aperture readers).
   Onset maximisation is constrained by the licit onsets of the language,
   derived from the spec's own grapheme→IPA table through the sonority
   scale in `orthography2ipa/vowels.py`, under a spec-declared
   `stress.max_onset` cap where one exists. *elektronisch* is
   `e·lek·tro·nisch`, *Monsieur* is `Mon·sieur`, *Abmeldung* is
   `Ab·mel·dung`. The shapes are calibrated on Germanic and Romance;
   extending the flag to a language whose onset inventory exceeds them
   (Greek, the Slavic and Uralic families) needs that inventory declared
   first. What it unblocks — the French ⟨e⟩/⟨o⟩ and Dutch aperture data
   waves — is still to do: one PR, one concern.
2. **A learned rescorer.** Out of scope here, and the diagnosis does not
   call for one yet: every French cluster above is a stateable rule, a
   lexical entry, a morphological fact, or the syllabifier bug. If it is
   ever wanted, the hook exists (`RescorerPlugin`): a per-lect phone
   n-gram LM re-costing each `SegmentSlot` by interpolating the spec
   cost with the LM's continuation cost, trained on the lect's own gold,
   shipped as data, gated on the same fail-before/pass-after evidence as
   any rule. It would paper over follow-up 1 rather than fix it, which
   is why it is last.

## Reproducing

```bash
PYTHONPATH=. python scripts/rank_diag.py fr 2000    # cluster table
PYTHONPATH=. python scripts/rank_eval.py fr 5000    # PER + oracle on a sample
PYTHONPATH=. python scripts/rank_sweep.py fr a.tsv  # per-word dump, for diffs
python scripts/benchmark.py --dataset wikipron --lang fr   # full corpus
```

---
[← Known limitations](known_limitations.md) · [Home](index.md) · [Spec diagnostics →](spec_diagnostics.md)
