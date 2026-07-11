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
library's "two maps"; see [`allophony.md`](allophony.md). The
downstream engines migrate their bespoke rule cascades here too: arbtok's
sun-letter/waṣl assimilation and tugaphone's silent-`e`/reduction become
rescorers over the shared engine rather than parallel tokenizers.
