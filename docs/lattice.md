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
