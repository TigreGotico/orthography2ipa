# Candidate scoring (per-spec candidate weights)

When a grapheme maps to several IPA candidates, the beam has to decide
which one wins. By default that decision is *positional* order: the first
IPA listed for a grapheme is the canonical form and gets beam cost `0`,
the second gets `+1`, and so on (see
[tokenizer.md](tokenizer.md#ipa-ambiguity-and-beam-search)). This is a
reasonable default — list the most common pronunciation first — but it is
a coarse, integer, rank-only signal.

**Candidate weights** let a spec attach real candidate *frequencies* to a
grapheme so the beam favours the corpus-dominant pronunciation and,
crucially, so a path's score becomes a proper (unnormalised)
log-probability rather than a rank sum. This is the mechanism that turns
the beam into a probabilistic lattice.

## The two JSON shapes

A grapheme's value in a language spec may be written in **either** form:

```jsonc
// plain list — today's shape, unchanged
"c": ["k", "s"]

// weighted object — new, optional
"th": { "ipa": ["θ", "ð"], "weights": [0.7, 0.3] }
```

Both are normalised, in one place
([`orthography2ipa/weights.py`](../orthography2ipa/weights.py), called
from the JSON loader), to the same internal representation: a plain IPA
list in `spec.graphemes` plus a *sparse* `spec.grapheme_weights` table
that carries an entry **only** for graphemes written in the weighted-object
form. Every existing consumer keeps seeing `spec.graphemes` as a plain
`list[str]` map.

`weights` is aligned index-for-index with `ipa`.

## How cost maps to weight

| grapheme value | candidate *i* beam cost |
| --- | --- |
| plain list | `float(i)` — rank `0, 1, 2, …` |
| weighted object | `-log(pᵢ)`, where `pᵢ = weightᵢ / Σ weight` |

Because beam cost is **additive** over a word's graphemes, using `-log(p)`
makes a whole path's cost the negative log of the product of its
candidate probabilities — a sequence log-probability. Lower weight →
higher cost → the candidate falls later in the beam.

**Absent weights == today.** A grapheme with no weights uses the rank
cost `0, 1, 2, …`, which is *byte-identical* to the behaviour that
predates this feature. Every spec that uses only plain lists produces
exactly the same transcriptions and the same scoreboard numbers as before.

The same normalisation and cost function feed **both** beam paths — the
standalone `PhonetokTokenizer.ipa_beam` and the engine's positional beam
in `g2p.py` — so they never disagree about a grapheme's costs. (Weights
apply to the flat grapheme table; a grapheme resolved by a
`positional_graphemes` override keeps rank ordering — per-position weights
are a separate, later layer.)

## Defensive handling of malformed weights

Weights are validated before use. Any of the following makes the whole
entry fall back to plain rank ordering (with a warning), so a bad weight
can never crash transcription or silently drop a candidate:

- `weights` length ≠ `ipa` length,
- any weight negative or non-numeric,
- the weight sum is `0`.

A single **zero** weight (with a positive sum elsewhere) is *kept*: its
probability is floored to `1e-6` so its cost is large but finite — the
candidate is strongly disfavoured yet still reachable.

## Inheritance

`grapheme_weights` is **not inherited** through ancestry
(`InheritanceMode.NOT_INHERITED`; see the `FIELD_INHERITANCE` manifest in
[`types.py`](../orthography2ipa/types.py)). A variety that pulls its
`graphemes` from a parent via `graphemes_base` gets the parent's IPA lists
but **not** its weights, so its transcription stays byte-identical to
rank ordering until it declares its own weights. Two reasons:

1. Candidate frequency is *variety-specific* corpus data — the relative
   frequency of ⟨ou⟩ → /aʊ/ vs /uː/ in en-GB is not the same statistic as
   in en-US — so a child must cite its own, not silently inherit.
2. It preserves the byte-identical guarantee for every inheriting child.

Within one spec a grapheme's IPA list and its weights live together in
the weighted-object value, so they are always authored (and overridden)
as a unit.

## Provenance

Weights must be justifiable candidate frequencies from cited corpora
(recorded in the spec's `sources` / `notes`), never PER-tuned parameters.
The first weighted spec is **en-GB** (see its `notes`), grounded in
Gontijo, Gontijo & Shillcock (2003), *Grapheme–phoneme probabilities in
British English*, and Berndt, Reggia & Mitchum (1987), *Empirically
derived probabilities for grapheme-to-phoneme correspondences in English*.
