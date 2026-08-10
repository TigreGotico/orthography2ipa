# Design: morphology-aware G2P contexts, and the ceiling o2i accepts

**Status: proposal, for review. Nothing here is built.**

**Conclusion up front.** The three blockers below need a fact
orthography does not encode. o2i does not acquire that fact — not as
data, not as a caller-supplied input. The ceilings are quantified and
accepted (§4). What o2i owes instead is a lattice that still *contains*
the reading it cannot choose, so a downstream rescorer can pick it
(§5) — and for French verbal ⟨-ent⟩ it currently does not.

Three recorded blockers stop at the same wall. The engine reads
orthography; each of these three needs a fact orthography does not
encode.

| Blocker | The fact the engine does not have | Where it is recorded |
|---|---|---|
| French ⟨-ent⟩ | part of speech — verb 3PL inflection is mute (*ils parlent* [paʁl]), noun/adjective ⟨-ent⟩ is [ɑ̃] (*vent*, *cent*, *moment*) | [ranking_error.md](../ranking_error.md) "Verbal ⟨-ent⟩"; `fr-FR.json` notes |
| Dutch compound boundary | where the compound seam is — a non-head member keeps its full vowel and resists schwa reduction (*koffiemelk*, *brandmerk*, *aanzegger*) | [ranking_error.md](../ranking_error.md) "Dutch"; PR #820 residual table |
| English suffix classes | which ⟨-s⟩ is inflectional, and what the ⟨-sion⟩ stem ends in | PR #823 "Deliberately NOT covered" |

This document surveys what the engine already has, states four options
with their costs, recommends one, and states what follows from it.

## 1. What exists

### `grammatical_endings`

A spec section mapping an orthographic word ending to the IPA it
realises, for the case where the realisation belongs to the ending and
not to the letters that spell it. It carries French mute ⟨-er⟩/⟨-ez⟩
and English ⟨-tion⟩/⟨-tial⟩/⟨-cious⟩ palatalization.

Mechanism, from `positional.match_grammatical_ending` and
`G2P._apply_grammatical_ending`:

* the word is tokenized exactly as before; only the emitted IPA of the
  trailing tokens is replaced, so the word's interior is never re-cut;
* the ending must sit at the word's *effective* end —
  `positional.effective_word_end` allows a transparent suffix the spec
  already silences (French plural ⟨-s⟩/⟨-x⟩);
* longest match wins (⟨-stion⟩ over ⟨-tion⟩);
* precedence is `word_exceptions` > `grammatical_endings` > `graphemes`
  / `positional_graphemes`.

It is **purely orthographic**. It asks "how does this word end?", never
"what is this word?". Its stated precondition (`types.py`) is that the
counter-set — the words the ending gets wrong — must be **closed**, so
that `word_exceptions` can hold it, the way *mer* and *hiver* hold the
line against ⟨-er⟩.

### `word_exceptions`

A closed, cited, per-spec list of whole-word overrides. It outranks
everything. It is the sanctioned home of irregularity, and it is
sanctioned **because it is closed**: a spec that enumerates an open
class in `word_exceptions` has shipped a lexicon under another name.

### The charter boundary

`AGENTS.md` §4 and §6 are explicit:

> Anything that is not a linguistic description of the language — text
> normalisation, orthographic reform, lexicon lookup, diacritic
> restoration, **morphology**, application-specific post-processing —
> belongs in a downstream consumer that interfaces with the lattice.

> The package ships **no word lists, no lexicons, no gold sets, no
> weights**.

Built-in lexicons were removed once; the lexicon is now caller-supplied
(`register_lexicon`, `set_lexicon_dir`, `hf://` ids), resolved lazily,
and nothing is fetched unless the caller asked for it.

`plugins.py` already states the composition rule this design must obey:

> A rich engine composes the steps it wants and says so in code …
> a lexicon, a POS tagger, a diacritizer.

So a POS tagger is not a forbidden idea. A *bundled* POS tagger, or a
word list that stands in for one, is.

**Nothing in this design may add a word list, a stem list, a vocabulary,
or a frequency table to the package.**

## 2. The numbers

Measured on the shipped gold caches (WikiPron: `fra_latn_broad`,
`eng_latn_uk_broad`, `nld_latn_broad`), counting **types**, by string
operations on the gold — no engine run, so these are properties of the
languages, not of the current spec.

### French ⟨-ent⟩

| Class | Types | Gold-mute | Gold [ɑ̃] |
|---|---:|---:|---:|
| all ⟨-ent⟩ | 6672 | 3918 | 2754 |
| ⟨-ment⟩ (adverbs, and *moment*/*ciment*/*document*) | 2512 | 45 | 2467 |
| ⟨-ent⟩ not ⟨-ment⟩ | 4160 | 3873 | 287 |

The rejected `"ent": ""` ending is that last row: **3873 wins against
287 losses**, 93%, worth `0.0891` → `0.0754` PER on wikipron/fr. It is
not shipped because the 287 are *vent, dent, cent, argent, accent,
talent, absent, serpent, Occident, Vincent* — high-frequency words, and
this library feeds TTS, where type PER does not price a wrong *vent*.
The counter-set is also open (*Laurent*, *Florent*, *Clément*), so it
cannot go in `word_exceptions`.

The split is close to a clean POS split. With a correct verb/non-verb
tag the same rule fires on 3873 types and stays silent on 287.

### English

| Class | Types (en-GB WikiPron) | Note |
|---|---:|---|
| ⟨-tion⟩ | 1678 | covered today |
| ⟨-tions⟩ | 86 | **not reachable**: English ⟨-s⟩ is pronounced, so it is not transparent to `effective_word_end` |
| ⟨-sions⟩ | 15 | same |
| ⟨-sion⟩ | 203 | 96 gold [ʒ], 107 gold [ʃ] — deliberately uncovered |

The ⟨-sion⟩ split is worth stating precisely, because it is the one
member of this set that is **not** a morphology problem. Testing the
naive left-context rule (after a vowel → [ʒ], after a consonant → [ʃ])
against gold: 73 after a vowel, 130 after a consonant, **27 violations**
— 87% accurate. That is a left-context predicate the ending matcher does
not currently express, not a missing POS tag. It should be handled by
widening the ending matcher, and it is out of scope here.

The genuinely morphological English residue is small: ~101 types where
an inflectional ⟨-s⟩ hides a derivational suffix.

### Dutch

`rank_diag` on a 500-word sample: 117 ranking failures, **94 of them on
⟨e⟩**, split between wrongly-reduced and wrongly-unreduced. A further 23
are compound-internal devoicing (⟨v⟩ `v`→`f`, ⟨g⟩ `ɣ`→`x`, ⟨z⟩ `z`→`s`
in *opvanghuis*, *bloedgroep*, *datzelfde*) that the word-level
`word_final` rule cannot see. PR #820 records the same class from the
other direction: compound-final ⟨e⟩ wrongly reduced —
*koffiemelk*, *brandmerk*, *aanzegger*, *omwenteling*, *dierentemmer* —
"thousands of confusion-pair instances, open class". A prior wave pinned
a closed set (`berg`, `veld`, `kerk`, `brecht`) and stopped there,
correctly.

The Dutch blocker is one fact: **where the seam is**. Booij (1995) ch. 5
states the rest — the non-head member carries secondary stress and keeps
its full vowel; ch. 2 sec. 2.5 states the devoicing.

## 3. Options

### (a) Do nothing; document the ceiling

Keep the engine orthography-only and record, per language, what that
costs.

*French ⟨-ent⟩ worked example.* *parlent* → [paʁlɑ̃] (wrong, should be
[paʁl]); *vent* → [vɑ̃] (right). 3873 types stay wrong, 287 stay right.
Documented in `ranking_error.md` and the spec notes as a class this
layer does not decide.

**For:** costs nothing, breaks nothing, keeps the charter exactly. The
ceiling is honest — every one of the three blockers is a fact about the
*word*, and a library that describes an *orthography* is allowed to not
have it. Downstream consumers (arbtok, tugaphone, bifonia) already own
this layer.

**Against:** the ceiling is real and quantified: fr/wikipron sits at
`0.0891` against espeak's `0.0740`, and ⟨-ent⟩ alone is `0.0137` of the
`0.0151` remaining gap. Dutch ⟨e⟩ is 80% of its ranking failures. Doing
nothing means those numbers never move at this layer.

**This is the recommended option** (§4). Its quantification work is
required regardless of what else is done, and §5 states what o2i owes
downstream once the ceiling is accepted.

### (b) A minimal morphological signal declared in spec data

Add a spec section — say `verbal_suffixes` — listing inflectional
paradigm endings with their conditioning, so that an ending can fire
only when co-occurring orthography confirms the paradigm.

*French ⟨-ent⟩ worked example.* The 3PL ending would need a condition
distinguishing the verb stem before it from a noun. Test the candidates:

* **Preceding stem shape.** *parlent*, *munissent*, *convoquèrent*,
  *rétablissent* against *talent*, *serpent*, *argent*, *Occident*,
  *ciment*. There is no stem-shape predicate that separates them.
  ⟨-issent⟩ and ⟨-èrent⟩ and ⟨-aient⟩ are reliable, but they are
  *longer endings*, which `grammatical_endings` already expresses with
  no new section; the bare productive ⟨-ent⟩ after a 1st-conjugation
  stem is exactly the undecidable case. *parent* is a noun; *parent*
  is also a possible verb form shape. *content* is an adjective;
  *comptent* is a verb.
* **Length or syllable count.** *serpent* (2 syllables) vs *parlent*
  (2 syllables). No.
* **Co-occurring paradigm members.** Would require knowing that
  *parle*, *parles*, *parlons* exist — a vocabulary. Forbidden.

So the honest answer is **mostly no**. The recoverable part —
⟨-èrent⟩, ⟨-issent⟩, ⟨-aient⟩, ⟨-eront⟩ — is recoverable *today* as
longer `grammatical_endings` keys, and adding a section for it buys
nothing. What remains after that is the undecidable core.

**For:** stays in data; no API change; no caller burden.

**Against:** it does not answer the question. Worse, a `verbal_suffixes`
section is an attractive place to smuggle a stem list, and the review
that catches that is the same review that already rejected morpheme
grapheme keys. Rejected.

Dutch fares no better under (b): a `linking_elements: ["s", "en"]`
declaration states a true fact about Dutch (Booij 1995 ch. 5) but does
not locate a seam — see (d).

### (c) An optional caller-provided morphological hint — REJECTED

The shape considered: let the caller pass a part-of-speech tag (and
morpheme boundaries) alongside the word, and let spec rules and endings
condition on it. The engine would ship no tagger; the knowledge would
arrive through a declared interface, the same way the lexicon and the
named plugins already do.

*French ⟨-ent⟩ worked example.* With a `VERB` tag, the mute ending
fires: *parlent* → [paʁl]. With `NOUN`, or with no tag at all, it does
not: *vent* → [vɑ̃].

**Rejected.** Part of speech belongs to the downstream lattice
rescorer, not to this engine's inputs. Two reasons decide it:

* espeak-ng does no POS tagging, and this library is measured against
  espeak. A mechanism that only pays off when the caller supplies a tag
  cannot be the answer to a gap espeak closes without one — it would
  move the target rather than reach it.
* The charter boundary stays where it is. `plugins.py` names a POS
  tagger as something a *downstream engine composes*; composing it means
  the downstream engine owns the decision, not that o2i grows a slot
  for its output.

The consequence is not "the ambiguity is unresolvable". It is that the
resolution happens downstream — which puts the whole weight of the
problem on whether o2i **hands the downstream the material to resolve
it**. That is §5.

### (d) A compound-segmentation pass for Germanic

The spec declares linking elements (`-s-`, `-en-`, `-e-`); the engine
tries every split of the word and keeps the valid ones, then exposes the
seam to the rule layer as a position (`compound_boundary`) so that
Booij's stress and devoicing facts become ordinary rules.

The load-bearing question is **what validates a split**, and the
candidate answer — "each half is independently transcribable" — is very
weak, because in an alphabetic orthography with full grapheme coverage
*every* substring is transcribable. So validation needs a vocabulary,
and the package may not ship one.

*Measured, on the Dutch gold word list used purely as a stand-in
vocabulary (45,872 types) — this is a measurement of the option, not a
proposed implementation:* of 31,677 types of 8+ characters, 14,127 admit
exactly one split, 2,026 admit more than one, 15,524 admit none.

Failure modes, all observed in that run:

* **Ambiguous seams.** *Aalsmeer* → `aal|smeer` or `aal+s|meer`;
  *Aardenburg* → `aard+en|burg` or `aarden|burg`; *Achtersteven* →
  `achter|steven` or `achterste|ven`. 2,026 types, and the two readings
  give different stress.
* **False seams in monomorphemic words.** In a 20-word random sample of
  the unique-split class, 3 were wrong: *Veenstra* → `veen+s|tra`,
  *Jouswerd* → `jou+s|werd`, *Weimeren* → `wei|meren`. Roughly 15%, and
  a false seam does damage — it blocks reduction where reduction is
  correct, the mirror of the bug being fixed.
* **The linking ⟨-e-⟩ is not safely declarable.** *Algerijn* →
  `alg+e|rijn` is pure noise, and *Schapehals* → `schap+e|hals` is
  correct. Same rule.
* **It cannot run without a vocabulary at all.** Drop the word list and
  the split count goes to "every position".

**For:** the phonology on the far side is genuinely rule-shaped and
cited (Booij 1995 ch. 2 sec. 2.5, ch. 5), it would close both the Dutch
⟨e⟩ class and the compound-internal devoicing class, and the same
machinery serves German, Swedish, Norwegian, Danish and Afrikaans.

**Against:** it requires a vocabulary, which is a corpus, which the
charter forbids. This is why Dutch compounds are a **ceiling and not a
deferred plan**: there is no charter-legal validator, and a
caller-supplied vocabulary only relocates the same decision to the
caller — who, having one, can usually supply the segmentation itself.
The measurements above are kept as the record of that, so the option is
not re-opened without new evidence.

## 4. Recommendation

**Ship (a): the ceilings are documented, quantified per language, and
accepted at the o2i layer.**

French verbal ⟨-ent⟩, Dutch compound seams, and the English
inflectional-⟨-s⟩ residue are facts about the *word*. This library
describes an *orthography*. It is allowed to not have them, and the
alternative mechanisms are worse:

* **(b)** does not answer the question — no orthographic predicate
  separates *parlent* from *talent* — and its main effect would be to
  create a plausible-looking place to put a stem list.
* **(c)** is rejected on the ruling above: POS is the downstream
  rescorer's, and beating espeak must not require an input espeak does
  not have.
* **(d)** cannot validate a seam without a vocabulary, which is a
  corpus, which the package may not ship. Its negative evidence is kept
  in §3(d) as documentation of *why Dutch compounds are a ceiling too*,
  not as a deferred plan.

What is owed, then, is the documentation itself: per-language ceiling
notes carrying the §2 numbers, in each affected spec's `notes` and in
`ranking_error.md`, stating the blocked class, its size, and which layer
owns it.

Accepting a ceiling is not the same as accepting the output. §5 is what
o2i should do instead.

### What stays blocked, per language

| Language | Blocked class | Size | Owner |
|---|---|---:|---|
| fr | verbal ⟨-ent⟩ | 3873 types (`0.0891` → ~`0.0754` if resolved) | downstream POS rescorer |
| nl | compound seams: ⟨e⟩ reduction + internal devoicing | 94 + 23 of 117 sampled ranking failures; open *koffiemelk* class | downstream segmenter/rescorer |
| en | inflectional ⟨-s⟩ over a derivational suffix | ~101 types | partly `effective_word_end`, see below |

Two items in that table are **not** ceilings and should be fixed here:

* **⟨-sion⟩, 203 types.** The after-vowel → [ʒ] / after-consonant → [ʃ]
  split scores 176/203 against gold. That is a left-context predicate
  the ending matcher does not express — no morphology, no POS. It
  belongs to the English wave.
* **⟨-tions⟩/⟨-sions⟩, 101 types.** Reachable by widening
  `effective_word_end`'s transparent-suffix set, which is shared
  positional machinery and wants its own PR.

## 5. What o2i should do instead: expose the ambiguity in the lattice

If the decision is downstream's, then o2i's obligation is to **emit
both readings as costed candidates** so a rescorer with POS can choose
between them. A ceiling that leaves the right answer in the lattice is
a ranking problem, which is downstream-solvable. A ceiling that removes
the right answer from the lattice is a coverage problem, which is not
solvable by anyone.

The two languages are on opposite sides of that line, and this was
measured.

### Dutch: already exposed

`word_candidates` on the shipped `nl` spec:

```
koffiemelk  → ['ˈkɔfiːməlk', 'ˈkɔfiːmɛlk']
opvanghuis  → ['ˈɔpvɑŋɦœys', 'ˈɔpfɑŋɦœys']
```

Both compound readings are present; the correct one is ranked second.
On a 300-word random sample of nl WikiPron types of 8+ characters:
**73 exact at 1-best, 111 with gold anywhere in the top 10** — 38
words, 12.7% of the sample, where the lattice holds the answer and
ranks it wrong. Dutch compounds are a **ranking** ceiling. A downstream
rescorer that knows the seam can already fix them with no change here.

### French: not exposed

`ipa_lattice("parlent")` on the shipped `fr` spec:

```
p → (p)          l → (l)
a → (a)          e → (ɑ̃ 0.0) (e 1.0) (ɛ 2.0)
r → (ʁ)          n → ()
                 t → () (t 1.0)
```

⟨e⟩ has no null candidate, so **[paʁl] is not in the lattice at any
beam width**. `word_candidates("parlent", k=50, beam_width=50)` returns
6 readings and [paʁl] is not among them. Measured on a 300-word random
sample of the gold-mute ⟨-ent⟩ class: **0 exact at 1-best, 0 with gold
anywhere in the top 10.** The matching gold-nasal sample scores 140/200
exact.

That is the real defect. French verbal ⟨-ent⟩ is not merely ranked
wrong — the reading does not exist for anything downstream to select.
No POS rescorer, however good, can recover it.

### The mechanism this calls for, without POS

`grammatical_endings` today maps an ending to **one** IPA string and
*rewrites* the tail. The proposal is to let a value be an **ordered
list**, which enters the lattice as costed candidates instead of
replacing it:

```json
"grammatical_endings": {
  "ent": ["ɑ̃", ""]
}
```

Read: "this ending is ambiguous; the nasal reading is preferred, the
mute reading is licit." First element keeps rank 1, so **1-best output
and every benchmark row are unchanged**; the second becomes a costed
alternative visible to `word_candidates`, to oracle@k, and to any
`RescorerPlugin`, which re-costs `SegmentSlot`s and is precisely where
a POS-aware downstream would act.

Assessment against the existing mechanisms:

* **It is the discipline the rest of the data already follows.** A
  `graphemes` value is an ordered candidate list; `positional_graphemes`
  values are ordered candidate lists. A single-valued
  `grammatical_endings` is the outlier, and the ⟨-ent⟩ case is what
  exposes it.
* **It needs no new knowledge.** "⟨-ent⟩ is ambiguous between [ɑ̃] and
  ∅" is a statement about French orthography, citable (Fouché 1959;
  Tranel 1987 §3), and true without reference to any word.
* **It does not smuggle a decision.** The engine still cannot tell
  *parlent* from *talent*; it stops pretending it can, and says so in
  the lattice.
* **It is null-safe.** A string value keeps today's rewrite semantics;
  a list value is opt-in per ending, and only `fr` would use it at
  first.

The costs are real and should be reviewed:

* Ordering the list *is* a claim, and for ⟨-ent⟩ the frequency-honest
  order (nasal first) is the type-count-dishonest one (3873 mute types
  vs 287 nasal). The doc's position is that TTS frequency wins, as it
  did when the rewrite was dropped — but that is a judgement, not a
  measurement.
* Oracle@k improves while 1-best does not. That is the intended shape,
  and it must not be reported as a win on the scoreboard's headline
  number.
* Every consumer reading only `transcribe()` sees nothing. The value is
  realised only by consumers that read the lattice — which is the
  architecture's stated contract ("this library emits the candidate
  lattice; consumers decide what to do with it", `AGENTS.md` §4), so
  the change makes o2i more honest about what it already claims to be.

For Dutch, nothing is needed: the candidates are already there. The
Dutch ceiling is documented, and the downstream that wants it fixed
needs a segmenter, not a change here.

**Scope note.** This section describes what the follow-up PR would
argue. Nothing in it is built, and the candidate-list extension should
be reviewed on its own before any spec declares one.

## 6. Linguistic background

The inflectional/derivational split is the reason these three blockers
behave differently, and it is why one mechanism can serve all three.

**Level ordering.** Derivational suffixes attach at an earlier level
than inflectional ones and trigger phonological alternation in the stem;
inflectional suffixes attach later and are phonologically transparent
(Siegel 1974; Kiparsky 1982; Chomsky & Halle 1968 for the underlying
boundary distinction). This predicts exactly what
`grammatical_endings` already does: English ⟨-ion⟩ is derivational and
palatalizes the stem-final coronal, so its effect is visible in the
spelling neighbourhood and an orthographic ending can capture it.
French ⟨-ent⟩ is inflectional, changes nothing in the stem, and leaves
no orthographic trace — which is precisely why no orthographic
predicate finds it.

**Morphology in G2P.** The dependence of letter-to-sound accuracy on
morphological decomposition is long-standing (Chomsky & Halle 1968;
Sproat 1996 on multilingual TTS text analysis; Black, Lenzo & Pagel
1998 on general letter-to-sound rules; Damper et al. 1999 for the
comparative evaluation; Marchand & Damper 2000 for the data-driven
side). French ⟨-ent⟩ specifically is a standard worked example of a
G2P rule that requires part of speech (Divay & Vitale 1997).

**Dutch compounds.** Booij (1995), *The Phonology of Dutch* — ch. 2 for
open-syllable lengthening and final/regressive devoicing, ch. 5 for
compound stress, the linking elements ⟨-s-⟩/⟨-en-⟩, and the rule that a
non-head member carries secondary stress and so resists reduction.
`nl.json` already cites it. The difficulty of *finding* the seam
automatically is equally well attested (Koehn & Knight 2003, on
empirical German compound splitting, reports the same ambiguity and
false-seam classes measured in §3(d)).

**POS in TTS frontends.** Frontends run a tagger for homograph
disambiguation independently of G2P (Yarowsky 1997). That tagger sits
downstream of this library, which is where the ⟨-ent⟩ decision belongs
— and why §5's obligation is to leave both readings in the lattice for
it, rather than to ask for its output as an input.

Citations here name the literature the design rests on. Only Booij 1995
is currently in a shipped spec's `sources`; adding any of the others to
`docs/bibliography.md` is part of implementing this, not of proposing
it.

---

**Navigation:** [Docs home](../index.md) · [Ranking error](../ranking_error.md) · [Data model](../data_model.md)

*Related: [Positional graphemes](../positional_graphemes.md) · [Sentence context](../sentence_context.md) · [Architecture](../architecture.md)*
