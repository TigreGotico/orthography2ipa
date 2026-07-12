# Features: o2i as a feature provider for ML / CRF G2P

`orthography2ipa` ships **no trained weights** — every candidate cost is a
hand-written `-log P` or a rank cost from the spec. That is exactly what makes
it a good *feature provider* for a downstream statistical model. It already
computes, per grapheme, everything a sequence model wants: phonological-class
predicates, word-local neighbours, the ranked candidate lattice with its costs,
and a per-word confidence signal. `G2P.features(text)` packages that structure
as a clean, flat, JSON-able **feature view** so a CRF (or a small neural G2P)
trains on linguistically-grounded features instead of raw character n-grams.

This is a **pure read**: `features()` never affects `transcribe`. It reuses the
same [lattice](lattice.md) (`ipa_lattice`), the same
[confidence signal](lattice.md#per-word-confidence) (`confidence_breakdown`),
and the same [`GraphemeContext`](tokenizer.md) predicates — no vowel logic is
recomputed.

## The CRF-as-rescorer pattern

The lattice and the learned model compose instead of competing:

1. **o2i emits the candidate lattice + features.** For each grapheme you get
   the ranked `(ipa, cost)` options *and* a feature record describing that
   position (class, neighbours, margin, …).
2. **A trained model re-costs the candidates.** A CRF labels each grapheme with
   the IPA it should realise; that prediction becomes a
   [`LatticeRescorer`](lattice.md#rescoring-the-lattice) that makes the
   predicted candidate the cheapest option for its slot. The model does not
   replace the beam — it *refines* it, and the universal beam remains the
   fallback for everything the model is unsure about.
3. **The B5 confidence signal says WHERE to spend learned capacity.** Every
   feature record carries the word's `confidence`. High-confidence words
   (`confidence ≈ 1.0`) are already decided by the base engine; the model earns
   its keep on the low-confidence, genuinely ambiguous words (English `⟨ough⟩`,
   `⟨th⟩`). You can weight training, or gate inference, on that signal instead
   of treating every position as equally hard.

## Worked example

```python
from orthography2ipa import G2P

en = G2P("en-GB")
for wf in en.features("cough"):
    print(wf.word, "confidence", round(wf.confidence, 4))
    for g in wf.graphemes:
        print(g.as_dict())
```

`cough` is one word with two grapheme slots. `word_confidence("cough")` is
`0.6321` — ambiguous, so a place a learned model should focus. The feature
dicts (formatted here for reading):

```python
# ⟨c⟩ — leading consonant, one dominant reading
{'grapheme': 'c', 'index': 0, 'position': 'initial',
 'span_start': 0, 'span_end': 1,
 'prev': None, 'next': 'ough', 'prev2': None, 'next2': None,
 'is_vowel': False, 'is_consonant': True, 'is_front': False, 'is_back': False,
 'top1_ipa': 'k', 'top1_cost': 0.0, 'margin': 1.0, 'n_candidates': 2,
 'confidence': 0.6321205588285577, 'script': 'Latin', 'code': 'en-GB'}

# ⟨ough⟩ — the ambiguous vowel digraph, six ranked candidates
{'grapheme': 'ough', 'index': 1, 'position': 'final',
 'span_start': 1, 'span_end': 5,
 'prev': 'c', 'next': None, 'prev2': None, 'next2': None,
 'is_vowel': True, 'is_consonant': False, 'is_front': False, 'is_back': True,
 'top1_ipa': 'ɔː', 'top1_cost': 0.0, 'margin': 1.0, 'n_candidates': 6,
 'confidence': 0.6321205588285577, 'script': 'Latin', 'code': 'en-GB'}
```

The `⟨ough⟩` slot's full ranked lattice is on the dataclass field (not in
`as_dict`, which stays scalar for CRF libraries):

```python
ough = en.features("cough")[0].graphemes[1]
ough.candidates
# (('ɔː', 0.0), ('oʊ', 1.0), ('ʌf', 2.0), ('ɒf', 3.0), ('aʊ', 4.0), ('uː', 5.0))
```

Those six options are exactly what a rescorer re-costs — `cough` → `/kɒf/`
wants the model to lift `ɒf` to the front; `tough` → `/tʌf/` wants `ʌf`.

### Record shape

`features()` returns a `list[WordFeatures]`, one per word. Each `WordFeatures`
carries `word`, `code`, `script`, `confidence`, and a `graphemes` tuple of
`GraphemeFeatures`. Every `GraphemeFeatures` exposes: `grapheme`, `span`,
`index`, word-relative `position` (`initial`/`medial`/`final`), the neighbour
graphemes (`prev`/`next` and `prev2`/`next2`), the class predicates
(`is_vowel`/`is_consonant`/`is_front`/`is_back`, delegated to
`GraphemeContext`), the ranked `candidates` as `(ipa, cost)` with `top1_ipa`,
`top1_cost`, `margin` (the top-1↔top-2 cost gap, `None` when a slot has a single
candidate), `n_candidates`, the per-word `confidence`, `script`, and `code`.

`GraphemeFeatures.as_dict()` renders one grapheme as a flat, scalar,
`json.dumps`-clean feature dict (values are `str`/`int`/`float`/`bool`/`None`
only — the nested candidate list is deliberately omitted so the dict is a
direct python-crfsuite item). `WordFeatures.as_dicts()` is the feature
**sequence** for the word.

## Feeding a CRF (illustrative)

o2i adds no training dependency — the sketches below show the *shape* of
wiring the features into a CRF; install `python-crfsuite` or `sklearn-crfsuite`
yourself if you want to train.

`WordFeatures.as_dicts()` is already the per-token feature sequence these
libraries consume. With **sklearn-crfsuite**:

```python
# pip install sklearn-crfsuite   (not a dependency of orthography2ipa)
import sklearn_crfsuite
from orthography2ipa import G2P

en = G2P("en-GB")

# X: one feature-dict sequence per word; y: the gold IPA per grapheme
X = [wf.as_dicts() for wf in en.features(" ".join(train_words))]
y = gold_ipa_labels                       # your aligned per-grapheme IPA

crf = sklearn_crfsuite.CRF()
crf.fit(X, y)                             # learns to re-rank the lattice
```

The equivalent **python-crfsuite** loop appends the same dicts:

```python
import pycrfsuite
trainer = pycrfsuite.Trainer()
for wf, labels in zip(en.features(text), gold_label_seqs):
    trainer.append(wf.as_dicts(), labels)   # xseq, yseq
trainer.train("g2p.crfsuite")
```

At inference, map the model's predicted label back onto the lattice as a
rescorer — make the predicted IPA the cheapest candidate for its slot — so the
learned model plugs into the shared beam rather than replacing it (see
[Rescoring the lattice](lattice.md#rescoring-the-lattice)):

```python
from orthography2ipa import get
from orthography2ipa.phonetok import PhonetokTokenizer, Candidate
from orthography2ipa.rescorer import LatticeRescorer

class CRFRescorer(LatticeRescorer):
    def __init__(self, tagger):        # a trained pycrfsuite.Tagger
        self.tagger = tagger
    def rescore(self, slot, context):
        # predicted IPA for this slot (from the per-word tag sequence)
        chosen = predict_ipa_for(self.tagger, slot, context)
        others = [c for c in slot.candidates if c.ipa != chosen]
        return [Candidate(chosen, 0.0)] + [
            Candidate(c.ipa, c.cost + 1.0) for c in others]

tok = PhonetokTokenizer(get("en-GB"))
tok.ipa_best("tough", rescorer=CRFRescorer(tagger))   # 'tʌf'
```

The base beam still transcribes every word in every registered language; the
CRF only re-costs candidates the lattice already offers, and the confidence
signal tells you where that re-costing is worth doing.

---

**Navigation:** [Docs home](index.md) · [Getting started](getting_started.md) · [Architecture](architecture.md) · [Languages](languages/index.md) · [Scoreboard](scoreboard.md)

*Related: [Lattice](lattice.md) · [Tokenizer](tokenizer.md) · [Candidate scoring](candidate_scoring.md) · [Sentence context](sentence_context.md) · [API stability](api_stability.md)*
