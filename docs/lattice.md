# The pronunciation lattice

Most words have exactly one sensible pronunciation. Some do not — and the
ones that do not are where a grapheme-to-IPA engine earns its keep.
`orthography2ipa` does not hide that ambiguity behind a single answer: it
exposes it as a **structured lattice** — for every grapheme, the ranked
list of IPA options that grapheme could realise, each with a cost. The
lattice is the object the rest of the library (and the downstream
phonemizers) is built to consume.

## What the lattice is

A lattice is a list of **slots**, one per grapheme, in surface order. Each
slot is a [`SegmentSlot`](tokenizer.md) carrying:

- `grapheme` — the source grapheme, exactly as tokenised;
- `span` — the `(start, end)` character offsets that locate it (same
  NFC/case-fold contract as `GraphemeContext.span`: `unicodedata.normalize("NFC", text)[start:end].lower() == grapheme`);
- `candidates` — a tuple of `Candidate(ipa, cost)`, ranked best (lowest
  cost) first.

`slot.top` is a shortcut for `slot.candidates[0]`, the canonical choice.

Because the cost of each slot is independent and additive, the lattice and
the beam are two views of the same search:

```python
from orthography2ipa import get
from orthography2ipa.phonetok import PhonetokTokenizer

tok = PhonetokTokenizer(get("en-GB"))
slots = tok.ipa_lattice("through")

assert "".join(s.top.ipa for s in slots) == tok.ipa_best("through")
```

Concatenating each slot's top candidate reproduces `ipa_best` with its
default arguments. (The lattice has no slots for whitespace or
punctuation, so it does not reflect a non-default `word_separator` or
`include_special=True` passed to the beam.) The lattice keeps *all* the
ranked options per position; the beam (`ipa_beam`) flattens them into
whole-word `IPAPath` strings. Reach for the lattice when you want to
reason about *why* a word was pronounced a certain way, or to intervene
at a single position.

## A worked example

English `cough` is a small ambiguity: the `c` is unambiguous, but the
`ough` cluster is famously not.

```python
tok = PhonetokTokenizer(get("en-GB"))
for slot in tok.ipa_lattice("cough"):
    print(slot.grapheme, slot.span,
          [(c.ipa, round(c.cost, 2)) for c in slot.candidates])
```

```text
c    (0, 1)  [('k', 0.0), ('s', 1.0)]
ough (1, 5)  [('ɔː', 0.0), ('oʊ', 1.0), ('ʌf', 2.0), ('ɒf', 3.0), ('aʊ', 4.0), ('uː', 5.0)]
```

The top-of-slot concatenation is `kɔː` — the canonical reading — but the
`ough` slot preserves five alternatives in rank order, ready for a
downstream rule or lexicon to promote the contextually correct one (`ɒf`
for *cough*, in fact) without re-tokenising the word.

## How cost works: −log P

Each `Candidate.cost` is an **additive beam cost**, and lower is better.
There are two regimes, decided per grapheme:

- **Plain-list spec** (the common case). A grapheme like `"e": ["e", "ɛ"]`
  has no frequency data, so the cost is the *rank* cost: `0.0` for the
  first (canonical) candidate, `1.0` for the next, and so on. This is the
  library's historical ordering, unchanged.
- **Weighted spec.** A grapheme may instead declare candidate
  frequencies, e.g. en-GB's `"er": {"ipa": ["ɜːɹ", "əɹ"], "weights": [0.2, 0.8]}`.
  The weights are normalised to a probability distribution and the cost
  becomes `-log P`. So the far more common `əɹ` (P = 0.8) costs
  `-log 0.8 ≈ 0.22`, while `ɜːɹ` (P = 0.2) costs `-log 0.2 ≈ 1.61` — and
  the beam prefers `əɹ` even though it is listed second. See
  [candidate_scoring.md](candidate_scoring.md) for the weight format and
  sourcing rules.

Because `-log P` is additive, a whole path's score is the negative log of
the product of its candidates' probabilities — a proper (unnormalised)
sequence log-probability. That is exactly what a path's total score is:

```python
slots = tok.ipa_lattice("gher")
best  = tok.ipa_beam("gher", beam_width=1)[0]
assert best.score == sum(s.top.cost for s in slots)
```

This is what turns the beam from a rank-sum toy into a real probabilistic
lattice.

## Positional overrides apply here too

The lattice consults the same shared resolver the full engine uses, so
context-sensitive [positional overrides](positional_graphemes.md) —
including the vowel-class positions — fire in the lattice. Spanish `c`
softens to `θ` before a front vowel:

```python
tok = PhonetokTokenizer(get("es-ES"))
c_slot = next(s for s in tok.ipa_lattice("cena") if s.grapheme == "c")
assert c_slot.top.ipa == "θ"          # before 'e' → θ
c_slot = next(s for s in tok.ipa_lattice("casa") if s.grapheme == "c")
assert c_slot.top.ipa == "k"          # before 'a' → k
```

`G2P.ipa_lattice(word)` returns the same structure but with the engine's
**stress and syllable context** supplied, so stress-conditioned nucleus
positions also fire. That lattice is the *pre-lexical* phoneme lattice —
built before stress-mark insertion and cross-word sandhi — which is the
object a downstream engine reasons over.

## Scoring quality: length normalisation and diversity

`ipa_beam` accepts two opt-in scoring knobs. Both default OFF and, off,
reproduce the current ordering byte-for-byte.

- **`length_norm=True`** reports each path's score as the mean per-segment
  cost rather than the raw cumulative cost, making scores comparable
  across inputs of different length. Within a single word every hypothesis
  shares a segment count, so the *ordering* is unchanged — only the scale.
- **`diversity=λ`** (a positive float) re-ranks the returned paths with a
  Maximal-Marginal-Relevance pass: the top path is kept, and each
  subsequent path is penalised by `λ ×` its similarity to the nearest
  already-selected path. On a long word the raw beam collapses to
  near-duplicates of the top path (differing in a single grapheme);
  `diversity` demotes those in favour of genuinely different
  pronunciations. The top-1 result never changes.

```python
tok.ipa_beam("weather", beam_width=8)                 # canonical order
tok.ipa_beam("weather", beam_width=8, diversity=5.0)  # near-dupes demoted
```

## What builds on the lattice

The lattice is designed as an extension point, not a dead end:

- A **rescorer** re-costs each slot's candidates given the neighbouring
  slots before a path is chosen — the seam by which a downstream rule
  cascade (a sun-letter assimilation, a silent-`e` rule) becomes a
  refinement over the shared lattice instead of a parallel tokenizer.
- A **per-word confidence** signal is read from the top-1 vs top-2 cost
  margin within each slot, plus the presence of unmapped graphemes — so an
  engine can spend its expensive lexicon only on the words the lattice is
  unsure about, and trust the fallback elsewhere.

Both read the `SegmentSlot`/`Candidate` shape described here without
changing it; the lattice is the stable substrate they attach to.

## Rescoring the lattice

A **rescorer** is the seam that lets a downstream rule cascade run over the
*shared* lattice instead of forking a parallel tokenizer. It is a pure,
composable pass that re-costs — and may reorder, add, drop, or delete — a
slot's candidates, given that slot and its context.

### Where it runs in the pipeline

A rescorer runs **after** positional + weight branch generation (the −log P
costing from `resolve_branches`) and **before** the beam selects a path:

```
normalize → tokenize → resolve branches (positional + weights)
                          │
                          ▼
                 ┌─ rescore (B4)   ← re-cost each slot given its neighbours
                 │      │
                 ▼      ▼
             beam path selection → stress → sandhi → dialect
```

Because a rescorer sees the **fully resolved** lattice — the pre-rescore
candidates of every neighbouring slot, not a half-selected beam path — a
*list* of rescorers composes deterministically: they apply in order and
each one sees the previous one's output. This is also exactly where the
post-lexical **allophone** pass (B8) attaches: a phoneme→surface rewrite
is a rescorer that replaces a slot's IPA with its context-conditioned
realisation.

### The API

Implement `LatticeRescorer.rescore(slot, context)` and pass it via the
optional `rescorer=` parameter on `ipa_beam`, `ipa_best`, `ipa_lattice`
(the tokenizer) or the `G2P(..., rescorer=...)` constructor (the engine).
`rescorer=` accepts a single rescorer or a list. Absent it (the default
`None`), the lattice and beam behave byte-for-byte as before.

The `RescoreContext` gives the rescorer:

- `context.slot` / `context.index` / `context.slots` — the current slot and
  the full word's slots (surface order);
- `context.grapheme` — the B1 `GraphemeContext`: word-local `prev`/`next`
  grapheme access and `is_vowel`/`is_consonant`/`is_front`/`is_back`
  predicates (single source of truth = `vowels.py`);
- `context.prev_slot` / `context.next_slot` — the resolved neighbouring
  slots, **word-local** (`None` at a word edge);
- `context.is_word_initial` / `context.is_word_final`;
- `context.syll_idx` / `context.stressed_syll_idx` / `context.is_stressed`
  — syllable/stress info **where available**.

**Stress availability differs by entry path, honestly.** The engine path
(`G2P.transcribe`, `G2P.ipa_lattice`) computes syllabification and stress,
so the stress fields are populated. The standalone tokenizer path
(`PhonetokTokenizer.ipa_beam` / `ipa_lattice`) has no sentence-level stress
detection, so `context.is_stressed` (and the syllable indices) are `None`.
A rescorer that needs stress must guard for `None` — and may simply no-op
when it is absent, exactly as the stress-conditioned positional rules do.

**Empty-candidate return** is a feature, not an error: returning an empty
sequence **deletes** the slot — it contributes no segment to any beam path
and is dropped from `ipa_lattice` output. That is how a silent-grapheme
rule (tugaphone silent-`e`) is expressed. The beam never crashes on it.

### Worked example — a mini assimilation rule in ~20 lines

Final-obstruent devoicing (a voiced obstruent surfaces voiceless
word-finally — German, Dutch, Russian, Catalan) is a whole realisation
rule in about twenty lines:

```python
from orthography2ipa import G2P, LatticeRescorer, Candidate

class FinalDevoicing(LatticeRescorer):
    VOICED = {"b": "p", "d": "t", "ɡ": "k", "z": "s", "v": "f", "ʒ": "ʃ"}

    def rescore(self, slot, context):
        if not context.is_word_final:          # only at the word edge
            return slot.candidates
        out = []
        for c in slot.candidates:
            surface = self.VOICED.get(c.ipa, c.ipa)   # devoice if voiced
            out.append(Candidate(surface, c.cost))
        return out                             # re-sorted by cost for you

ca = G2P("ca", rescorer=FinalDevoicing())
ca.transcribe("club")    # "ˈklub" → "ˈklup": final /b/ realised as [p]
```

The same shape expresses *c-before-front-vowel* softening — inspect
`context.grapheme.next.is_front` and promote the soft candidate — or a
sun-letter assimilation (compare `context.prev_slot`'s IPA). The rule reads
the shared lattice; it never re-tokenizes.

### Who builds on this

The post-lexical **allophone rules** (final devoicing, assimilation, vowel
reduction, flapping, …) are the built-in rescorer over this seam — a spec's
declarative `allophone_rules` compile into an `AllophoneRescorer` the engine
runs automatically after phoneme selection. This is the second of the
library's "two maps"; see [`allophony.md`](allophony.md). A downstream
engine can attach its own cascade the same way — Arabic sun-letter
assimilation, a Portuguese sibilant rule — expressing each rule as a
re-costing over the shared lattice. Whether that is the right choice for a
given engine is the subject of the next section.

## Refine the lattice, or fork the tokenizer?

A downstream phonemizer has two honest ways to build on this library, and
which one fits depends on the *shape* of its rules, not on a blanket
preference. Both are supported; each carries a cost.

### Refine — express rules as rescorers over the shared lattice

Keep the shared tokenizer and lattice, and add `LatticeRescorer`s that
re-cost candidates.

Choose this when:

- Your rules are **context-conditioned choices among the grapheme→phoneme
  candidates the shared trie already enumerates** — a coronal-triggered
  assimilation, a positional sibilant, a silent-grapheme drop. Re-costing is
  exactly that shape.
- **IPA is assembled from per-grapheme candidate selection** — that is,
  `ipa_lattice` / `ipa_best` is, or can become, your generation path.
- You want the maximal-munch trie, positional conditioning, candidate
  weights, and the confidence / OOV signal for every language for free, and
  you want your rules to **compose** with the built-in allophone rules and
  with one another.

Where it does not reach:

- A rescorer sees **one slot and its immediate neighbours**. Rules that need
  **non-local context** — cross-word sandhi, pausal or phrase-final forms,
  morphological decomposition, part of speech — do not fit a per-slot
  rescorer; they belong in a thin orchestration layer *above* the lattice,
  not inside it.
- **Multi-segment interactions need care.** A rescorer promotes a candidate
  by making it strictly cheapest, and it can only reason over the candidates
  the spec actually offers. If the shared spec omits or mis-bakes a candidate
  a rule needs — a semivowel that must geminate, a word-final long vowel
  competing with a consonant reading — re-costing alone cannot recover it;
  the fix belongs in the spec data upstream, not in a workaround.
- If your engine's generation model is **not** the lattice — it assembles IPA
  another way, such as a character-level cascade — a rescorer is dead code
  until generation is routed through `ipa_lattice`.

### Fork — keep a bespoke tokenizer and rule engine

Own the tokenization and rule pass end to end.

Choose this when:

- You need a **representation or context the per-slot lattice cannot
  express**: whole-utterance rules, morphological structure, prosody, or a
  non-IPA intermediate the rest of your engine consumes.
- Your data **diverges enough from the base spec** that inheriting it is a
  liability, or you need units the base cannot model and that cannot be
  pushed upstream cleanly.
- You need **independence from the base engine's release cadence**, or a
  hand-tuned path where the lattice's generality costs more than it returns.

What it costs:

- You **re-implement and maintain tokenization** — the maximal-munch scan,
  the digraph and trigraph handling — and its bugs are yours to find.
- You forgo the **shared multilingual grapheme data, positional
  conditioning, candidate weights, confidence signal, and every later engine
  improvement**, and your rules **cannot compose** with another engine's
  rescorers or the built-in allophone layer.

### In practice: hybrid, and push gaps upstream

Most engines land on a **hybrid**: word-internal phonology as rescorers over
the shared lattice, and the genuinely non-local part — cross-word sandhi,
pausal forms, lexical exceptions — on a small orchestration layer that calls
into it. The boundary between the two must be **enforced, not assumed**: a
word that needs cross-word context should be routed to the layer that has it,
never sent silently through the word lattice.

Treat every capability a migration finds missing as an **upstream task**, not
a reason to fork permanently. When a rule cannot be expressed because the
shared spec bakes the wrong candidate or the engine lacks a hook, fix the
spec or add the hook — so more of the engine moves onto the shared lattice
over time and the next engine inherits the fix.

## Per-word confidence / OOV signal

The lattice does not only say *what* a word is pronounced as — read the right
way it also says *how sure the base engine is*. That is the whole point of a
per-word **confidence** signal: it tells a downstream specialized phonemizer
**where to spend effort**. A word the base engine is confident about can be
trusted as-is; a word it is unsure about is exactly where an expensive
lexicon lookup or hand-written rule cascade earns its keep. Confidence is how
`orthography2ipa` *explicitly enables* a specialized engine instead of
competing with it.

The signal is a pure, deterministic read off the lattice — no global state,
thread-safe — surfaced three ways:

- `WordTranscription.confidence: float` on every word of a
  `transcribe_detailed(...)` result;
- `G2P.word_confidence(word) -> float` for a single word;
- `G2P.confidence_breakdown(word) -> ConfidenceBreakdown` for the per-slot
  detail (which position the engine was unsure about).

### The formula

Confidence is built entirely from costs the lattice already carries
(`Candidate.cost`, see [How cost works](#how-cost-works-log-p) above),
combining three signals.

**1 — Ambiguity (top-1 vs top-2 margin).** Within a slot, let `cost₁` and
`cost₂` be the two lowest candidate costs. The **margin** `m = cost₂ − cost₁`
is how decisively the winner beats its nearest rival. A slot with a single
candidate has no rival, so `m = +∞`. Squashed into `[0, 1]`:

```
ambiguity = 1 − exp(−m)      # m = 0 → 0 (a dead tie); m = +∞ → 1 (decisive)
```

**2 — Rarity (winner cost).** A slot whose *winner* is itself high-cost — a
rare mapping, a large −log P — is less trustworthy than one whose winner is
the free, canonical `cost = 0` option:

```
rarity = exp(−cost₁)         # cost₁ = 0 → 1; larger cost → smaller
```

**3 — Coverage (OOV).** Any grapheme the spec's table does not cover lowers
`WordTranscription.coverage` below `1.0`. Because an out-of-script character
means the engine has *no* opinion at all there, it multiplies straight in.

Per slot the two intra-lattice factors multiply; across the word the
**minimum** ("weakest link") wins, then coverage folds in:

```
slot_confidence  = ambiguity × rarity
word_confidence  = min(slot_confidence over all slots) × coverage
```

The weakest-link choice is deliberate: a downstream engine wants to know
whether **any** position is uncertain, not the average. `confidence_breakdown`
exposes the full `per_slot` tuple so a caller that prefers a mean, or wants to
localise the single hard grapheme, can. A `word_exceptions` lexicon override
is a certain answer, so its lattice confidence is `1.0` (only coverage can
lower it).

### Worked example — where a downstream engine spends effort

```python
from orthography2ipa import G2P

es = G2P("es-ES")
es.word_confidence("luz")    # 1.0000  — every grapheme maps one way
es.word_confidence("gato")   # 0.6321  — ⟨g⟩ and ⟨o⟩ each have a rival
```

Spanish `luz` is unambiguous: `l`, `u`, `z` each have a single realisation,
every slot's margin is `+∞`, so confidence is a flat `1.0`. Spanish `gato`
carries two rank-cost rivals (`g → ɡ/x`, `o → o/…`), each a margin of exactly
`1.0` over a free winner — `1 − exp(−1) ≈ 0.6321` — and the weakest such slot
sets the word. A downstream Spanish phonemizer can skip `luz` entirely and
spend its lexicon only on words like `gato`.

Weighted specs give a *graded* answer rather than the flat rank-cost `0.6321`:

```python
en = G2P("en-GB")
en.word_confidence("bar")    # 1.0000  — b, a(only ɑː here), r all decisive
en.word_confidence("her")    # 0.6000  — ⟨er⟩ is −log P weighted
```

en-GB `⟨er⟩` declares candidate weights (`əɹ` P = 0.8 → cost 0.223, `ɜːɹ`
P = 0.2 → cost 1.609). Its margin is `1.609 − 0.223 = 1.386`, so
`ambiguity = 1 − exp(−1.386) = 0.75`, and because the winner is not free
`rarity = exp(−0.223) = 0.80`; the slot — and the word — score
`0.75 × 0.80 = 0.60`. The probabilistic ambiguity of `⟨er⟩` reads out as a
number strictly between the confident `1.0` and a dead tie.

Finally, an out-of-script character drops confidence sharply through
coverage:

```python
b = en.confidence_breakdown("bar你")
b.coverage    # 0.75   — 3 of 4 characters map
b.lattice     # 0.6321 — 'bar' is not perfectly confident on its own
b.value       # 0.4741 — lattice × coverage
b.unmapped    # ('你',)
```

The OOV character pulls the word well below any fully-mapped word — the
strongest signal of all that a downstream engine (or a human) must handle it.

---

**Navigation:** [Docs home](index.md) · [Getting started](getting_started.md) · [Architecture](architecture.md) · [Languages](languages/index.md) · [Scoreboard](scoreboard.md)

*Related: [Tokenizer](tokenizer.md) · [Candidate scoring](candidate_scoring.md) · [Architecture](architecture.md) · [Allophony](allophony.md)*
