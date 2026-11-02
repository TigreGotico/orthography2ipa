# Candidate scoring (per-spec candidate weights)

When a grapheme maps to several IPA candidates, the beam must decide which one wins. By default the order of the list decides. The first IPA listed for a grapheme is the canonical form and costs 0, the second costs 1, and so on. The [tokenizer page](tokenizer.md#ipa-ambiguity-and-beam-search) shows this rank cost in the beam. This default asks the spec author to list the most common pronunciation first, and it gives only a rank, never a size of preference.

Candidate weights let a spec attach real candidate frequencies to a grapheme. The beam then favours the pronunciation that dominates in a corpus. The score of a path also becomes an unnormalised log-probability instead of a sum of ranks. This makes the beam a probabilistic [lattice](lattice.md#how-cost-works).

## The two JSON shapes

A grapheme's value in a language spec takes one of two forms:

```jsonc
// plain list
"c": ["k", "s"]

// weighted object
"er": { "ipa": ["ɜːɹ", "əɹ"], "weights": [0.2, 0.8] }
```

`weights` aligns index by index with `ipa`. The JSON loader passes the grapheme table through [`orthography2ipa/weights.py`](../orthography2ipa/weights.py), which turns both forms into one internal shape. `spec.graphemes` holds a plain IPA list for every grapheme, so every consumer reads `spec.graphemes` as a `list[str]` map. `spec.grapheme_weights` is sparse: it has an entry only for the graphemes written in the weighted form.

## How cost maps to weight

| Grapheme value | Beam cost of candidate *i* |
| --- | --- |
| plain list | `float(i)`, the rank `0, 1, 2, …` |
| weighted object | `-log(pᵢ)`, where `pᵢ = weightᵢ / Σ weight` |

The beam cost adds up over the graphemes of a word. With `-log(p)`, the cost of a whole path is the negative log of the product of its candidate probabilities, which is a sequence log-probability. A lower weight gives a higher cost, and the candidate falls further down the beam.

A grapheme without weights uses the rank cost. A spec that uses only plain lists therefore gives the same transcriptions as it would with no weight support at all.

Both beams use the same cost function, `weights.candidate_base_costs`, through the shared resolver in `orthography2ipa.positional`. The standalone `PhonetokTokenizer.ipa_beam` and the engine's beam in `g2p.py` therefore always agree on the costs of a grapheme. Weights apply to the flat grapheme table only. When a `positional_graphemes` override fires, its candidates come first in their declared order, the flat alternatives follow, and all of them take rank costs.

## Malformed weights

Two layers check weights. The pydantic model `WeightedGraphemeModel` in [`orthography2ipa/schema.py`](../orthography2ipa/schema.py) rejects a weighted value when:

- the `weights` list and the `ipa` list differ in length,
- a weight is negative or not a number,
- the weights sum to 0 or less.

`orthography2ipa validate` and the test suite run this model on every shipped spec, so a malformed weight fails validation before it ships.

At run time, `candidate_base_costs` checks the same conditions again. If an entry fails, it emits a warning and the whole entry falls back to rank ordering. A bad weight can therefore never stop a transcription or silently drop a candidate.

One zero weight, with a positive sum elsewhere, is valid. Its probability gets the floor `WEIGHT_FLOOR = 1e-6`, so its cost is large but finite. The beam strongly disfavours that candidate, but it can still reach it.

## Inheritance

`grapheme_weights` does not inherit through ancestry. Its mode is `InheritanceMode.NOT_INHERITED` in the `FIELD_INHERITANCE` manifest in [`types.py`](../orthography2ipa/types.py). A variety that takes its `graphemes` from a parent through `graphemes_base` gets the parent's IPA lists but not its weights. It keeps rank ordering until it declares weights of its own. en-AU, for example, takes its graphemes from en-GB and has an empty `grapheme_weights`.

There are two reasons for this rule. First, candidate frequency is corpus data for one variety. The frequency of ⟨ou⟩ as /aʊ/ against /uː/ in en-GB is not the same statistic as in en-US. A child must therefore cite its own data and not inherit it silently. Second, an inheriting child keeps the plain rank ordering that its own data supports.

Within one spec, a grapheme's IPA list and its weights live in the same weighted-object value. An author therefore writes and overrides them together.

## Provenance

Weights must be candidate frequencies from cited corpora, recorded in the spec's `sources` or `notes`. They are never parameters tuned to lower the PER. The en-GB spec weights ⟨er⟩, ⟨gh⟩ and ⟨ie⟩. Its sources are Gontijo, Gontijo & Shillcock (2003), *Grapheme-phoneme probabilities in British English*, and Berndt, Reggia & Mitchum (1987), *Empirically derived probabilities for grapheme-to-phoneme correspondences in English*. The spec's `notes` give the values and the reasons.

---
[← Tokenizer](tokenizer.md) · [Home](index.md) · [The pronunciation lattice →](lattice.md)
