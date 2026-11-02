# Lattice PER: pronunciation-fair phone error rate

`orthography2ipa.lattice_per` scores a phone sequence against every pronunciation that a lect admits for a reference text. The phone sequence is usually ASR phone output, or the phonemized form of an ASR word hypothesis. A plain phone error rate compares against one reference transcription, and that one choice of reading is arbitrary.

## Why single-reference PER is unfair

A phone error rate against a single reference transcription charges the model for pronunciation choices that are not errors:

| Source of variation | Example |
| --- | --- |
| Optional sandhi | A Basque speaker says *ez dut* with the contracted [es̻ tut]. A reference that keeps the uncontracted form marks each contraction as two errors, and the reverse holds too |
| Dialectal allophones | Seseo against distinción, a tap against a trill, open against closed mid vowels |
| Cliticization and reduction | Variants that the spelling does not distinguish |

The effect is systematic. Speakers of non-standard lects score worse because they speak their lect, not because the model misheard them. Dialect-ASR references are usually normalised toward a standard. The reported error rate then partly measures how far the speaker is from the standard.

## What the lattice gives

The candidate lattice of a reference text, under a lect spec, is the set of pronunciations that a speaker of that lect could validly produce. The function therefore computes the oracle edit distance: the minimum, over all admissible readings, of the segment-level edit distance to the hypothesis. A hypothesis pays only for segments that are wrong on every valid reading.

Two kinds of reading are admissible:

1. Every path through the sentence lattice of the reference (`G2P.sentence_lattice(ref_text)`), which takes one candidate per grapheme slot, in order, before sandhi.
2. The engine's final reading, `G2P(lang).transcribe(ref_text)`. It includes the cross-word sandhi and the sentence rescorers that the lattice does not apply.

The oracle does not enumerate paths. It pushes a Levenshtein frontier through the lattice, slot by slot, and takes the element-wise minimum over the candidates of each slot. This is the edit-distance transducer composed with the acyclic lattice. The cost is linear in the lattice size times the hypothesis length.

## Usage

```python
from orthography2ipa.lattice_per import lattice_per

for hyp in ("es̻ pada", "es baða"):
    r = lattice_per(hyp, "ez bada", "eu")
    print(r.distance, round(r.per, 4), round(r.top_per, 4), round(r.variant_credit, 4))
```

```text
1.0 0.1667 0.1667 0.0
1.0 0.1667 0.3333 0.1667
```

The engine's final reading of *ez bada* is `es̻ paða`, with sandhi, and the lattice path is `es̻ baða`. The first hypothesis is one segment away from the final reading, so the naive score and the fair score agree. The second hypothesis is two segments away from the final reading but one away from the lattice path. The lattice admits the unsandhied reading, so half of the naive error is a valid variant. The values depend on the `eu` spec and change when the spec changes, so run the lines to read the values that apply to your version.

`lattice_per(hyp_ipa, ref_text, lang, *, weighted=False, beam_width=8)` takes these arguments:

| Argument | Meaning |
| --- | --- |
| `hyp_ipa` | The hypothesis phone string. The function removes whitespace and the stress and boundary marks `ˈ ˌ . ‿ \| ‖`. A segment keeps its combining diacritics, so `s̻` is one segment |
| `ref_text` | The reference text as orthography. The function builds its lattice under `lang` |
| `lang` | The lect code |
| `weighted` | With `True`, a substitution costs the articulatory feature distance in [0, 1], and insertions and deletions still cost 1 |
| `beam_width` | The number of candidates per slot for the sentence lattice |

With `weighted=True`, the metric becomes a graded phonological error rate. A laminal against apical sibilant confusion costs a fraction of a stop against vowel confusion. A segment outside the feature table compares by its base character, plus a penalty of one feature flip (1/16) for the diacritic. A substitution never costs more than 1.

```python
print(lattice_per("es pada", "ez bada", "eu").distance)
print(round(lattice_per("es pada", "ez bada", "eu", weighted=True).distance, 4))
```

```text
2.0
0.2753
```

The result is a frozen `LatticePER`:

| Field | Meaning |
| --- | --- |
| `distance` | The oracle edit distance over all admissible readings |
| `per` | `distance / ref_segments`, the headline figure |
| `top_distance` | The edit distance against the engine's final reading only, which is what single-reference PER gives |
| `top_per` | `top_distance / ref_segments` |
| `ref_segments` | The segment count of the engine's final reading, which is the denominator |
| `hyp_segments` | The segment count of the hypothesis after mark removal |
| `lang` | The resolved lect code |
| `variant_credit` | A property, `top_per - per` |

The denominator is the segment count of the engine's final reading. Oracle paths differ in length, so one fixed denominator keeps scores comparable across runs.

## Reading the two numbers

Report `per` and `top_per` together. `per` is the fair figure: the errors that no valid pronunciation explains. `variant_credit` is how much the naive metric over-charged.

Over a test set, a large credit shows that the references are normalised away from how the speakers talk. That is a diagnostic of the dataset in itself. A row whose hypothesis is far from every lattice path is a candidate for mislabeled audio, not for a model error.

## Caveats

The metric inherits the spec. A permissive spec, with many candidates per slot, makes hypotheses look better, and a thin spec under-reports valid variation. Report the lect code and the engine version next to any number. The gap between `per` and `top_per` on known-good hypotheses is a probe for permissiveness.

The lattice that `lattice_per` builds keeps only the top candidate of each slot. It calls `sentence_lattice` with the default greedy search, so the `beam_width` argument has no effect. The admissible readings are therefore the top lattice path and the final reading, and the lower-ranked candidates of the spec do not reach the oracle.

The lattice path before sandhi and the final reading do not cover every combination of sandhi. An optional sandhi that the final reading applied is admissible through reading 2, and its absence is admissible through reading 1. A mixture, with one contraction applied and another not in the same utterance, is covered only when the lattice itself carries it.

Scoring is per IPA segment: a base character with its combining marks, with affricate ties kept. A hypothesis in another notation must first be folded to the spec's conventions, as the cross-engine benchmarks do.

---
[← The pronunciation lattice](lattice.md) · [Home](../index.md) · [Allophony →](allophony.md)
