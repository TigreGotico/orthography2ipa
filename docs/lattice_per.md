# Lattice PER — pronunciation-fair phone error rate

`orthography2ipa.lattice_per` scores a phone sequence — typically ASR
phone output, or the phonemized form of an ASR word hypothesis — against
**every pronunciation the lect admits** for a reference text, instead of
against one arbitrary reference transcription.

## Why single-reference PER is unfair

A phoneme error rate computed against a single reference transcription
charges the model for pronunciation choices that are not errors:

- **optional sandhi** — a Basque speaker saying *ez dut* produces the
  contracted [es̻tut]; a reference that pins the uncontracted form marks
  every contraction as two errors, and vice versa;
- **dialectal allophone choices** — seseo vs distinción, tap vs trill,
  open vs closed mid vowels;
- **cliticization and reduction variants** the orthography does not
  disambiguate.

The effect is systematic: speakers of non-standard lects score worse *for
being lect speakers*, not for being misrecognized. References normalized
toward a standard (as dialect-ASR references usually are) make the
reported error rate partly a measure of the speaker's distance from the
standard.

## What the lattice gives

The candidate lattice for a reference text under a lect spec is exactly
the set of pronunciations a speaker of that lect could validly have
produced. `lattice_per` therefore computes the **oracle edit distance**:
the minimum, over all admissible readings, of the segment-level edit
distance to the hypothesis. A hypothesis is only charged for segments
that are wrong on *every* valid reading.

Admissible readings are:

1. every path through `G2P.sentence_lattice(ref_text)` — each grapheme
   slot's ranked candidates, in order, pre-sandhi;
2. the engine's final reading (`transcribe(ref_text, lang)`), which
   includes cross-word sandhi and sentence rescorers the raw lattice
   deliberately does not apply.

The oracle is computed without enumerating paths: a Levenshtein frontier
is pushed through the lattice slot by slot, taking the elementwise
minimum over each slot's candidates — the edit-distance transducer
composed with the acyclic lattice. Cost is linear in lattice size times
hypothesis length.

## Usage

```python
from orthography2ipa.lattice_per import lattice_per

r = lattice_per("es̻ pada", "ez bada", "eu")
r.per              # 0.0 — the sandhi-contracted reading is admissible
r.top_per          # what naive single-reference PER would have said
r.variant_credit   # top_per - per: error mass a valid variant explains

r = lattice_per("es baða", "ez bada", "eu")
r.per              # > 0 — wrong on every reading: a real error
```

- `hyp_ipa` — hypothesis phone string. Whitespace, stress and boundary
  marks (`ˈ ˌ . ‿ | ‖`) are stripped; segments keep their combining
  diacritics (`s̻` is one segment).
- `ref_text` — reference **orthography**; its lattice is built under
  `lang`.
- `weighted=True` — substitutions cost articulatory feature distance in
  `[0, 1]` (insertions/deletions stay 1), turning PER into a graded
  phonological error rate: a laminal/apical sibilant confusion costs a
  fraction of a stop/vowel confusion. Segments outside the feature table
  compare by base character plus a one-feature diacritic penalty.

`per` is normalized by the segment count of the engine's final reading of
the reference — a single deterministic denominator (oracle paths differ
in length).

## Reading the two numbers

Report `per` and `top_per` together:

- `per` is the fair figure — errors no valid pronunciation explains.
- `top_per − per` (`variant_credit`) is how much the naive metric
  over-charged. Aggregated over a test set, a large credit means the
  references are pronunciation-normalized away from how the speakers
  talk — itself a dataset diagnostic: rows whose hypothesis is far from
  every lattice path are candidates for *mislabeled audio*, not model
  errors.

## Caveats — stated so scores stay honest

- **The metric inherits the spec.** A permissive spec (many candidates
  per slot) makes hypotheses look better; a thin spec under-reports valid
  variation. Report the lect code and engine version next to any number.
  The gap between `per` and `top_per` on known-good hypotheses is a
  permissiveness probe.
- **Pre-sandhi lattice + final reading is not every sandhi combination.**
  Optional sandhi that the final reading applied is admissible via
  reading 2, and unapplied via reading 1, but *mixtures* (one contraction
  fired, another not, in the same utterance) are only covered when the
  lattice itself carries them.
- **Segmentation convention.** Scoring is per IPA segment
  (base + combining marks; affricate ties kept). A hypothesis in a
  different notation should be folded to the spec's conventions first,
  as the cross-engine benchmarks do.

*Related: [Lattice](lattice.md) · [Benchmarks](benchmarks.md) ·
[Distance](distance.md)*
