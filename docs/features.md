# Features: o2i as a feature provider for ML / CRF G2P

`orthography2ipa` ships no trained weights. Every candidate cost is a hand-written `-log p` or a rank cost from the spec. That makes the library a good feature provider for a statistical model downstream.

For each grapheme it already computes what a sequence model needs. That is the class predicates, the word-local neighbours, the ranked candidate lattice with its costs, and a per-word confidence. The method `G2P.features(text)` packages that structure as a flat feature view that serialises to JSON. A CRF, or a small neural G2P, can then train on linguistic features instead of raw character n-grams.

`features()` only reads, and it never changes `transcribe`. It reuses the same [lattice](lattice.md) (`G2P.ipa_lattice`), the same [confidence signal](lattice.md#per-word-confidence--oov-signal) (`confidence_breakdown`) and the same [`GraphemeContext`](tokenizer.md#context-model) predicates. It computes no vowel logic of its own.

## The CRF-as-rescorer pattern

The lattice and the learned model work together in three steps:

1. The library gives the candidate lattice and the features. For each grapheme you get the ranked `(ipa, cost)` options and a feature record that describes the position.

2. A trained model re-costs the candidates. A CRF labels each grapheme with the IPA it should realise. That prediction becomes a [`LatticeRescorer`](lattice.md#rescoring-the-lattice) that makes the predicted candidate the cheapest option of its slot. The model refines the beam and does not replace it, and the beam stays the fallback wherever the model is unsure.

3. The confidence signal shows where learned capacity pays off. Every feature record carries the confidence of its word. The base engine already decides the words with confidence near 1.0. The model is useful on the ambiguous words with low confidence, such as English ⟨ough⟩ and ⟨th⟩. You can weight training, or gate inference, on that signal.

## Worked example

```python
from orthography2ipa import G2P

en = G2P("en-GB")
for wf in en.features("cough"):
    print(wf.word, "confidence", round(wf.confidence, 4))
    for g in wf.graphemes:
        print(g.as_dict())
```

```text
cough confidence 0.6321
{'grapheme': 'c', 'index': 0, 'position': 'initial', 'span_start': 0, 'span_end': 1, 'prev': None, 'next': 'ough', 'prev2': None, 'next2': None, 'is_vowel': False, 'is_consonant': True, 'is_front': False, 'is_back': False, 'top1_ipa': 'k', 'top1_cost': 0.0, 'margin': 1.0, 'n_candidates': 2, 'confidence': 0.6321205588285577, 'script': 'Latin', 'code': 'en-GB'}
{'grapheme': 'ough', 'index': 1, 'position': 'final', 'span_start': 1, 'span_end': 5, 'prev': 'c', 'next': None, 'prev2': None, 'next2': None, 'is_vowel': True, 'is_consonant': False, 'is_front': False, 'is_back': True, 'top1_ipa': 'ɔː', 'top1_cost': 0.0, 'margin': 1.0, 'n_candidates': 6, 'confidence': 0.6321205588285577, 'script': 'Latin', 'code': 'en-GB'}
```

⟨cough⟩ is one word with two grapheme slots. Its confidence of 0.6321 marks it as ambiguous, so it is a place where a learned model should focus. The ⟨c⟩ slot has one dominant reading, and the ⟨ough⟩ slot is a vowel grapheme with six ranked candidates.

The full ranked lattice of a slot is on the `candidates` field of the dataclass. The dict from `as_dict` leaves it out, so that every value stays a scalar for CRF libraries:

```python
ough = en.features("cough")[0].graphemes[1]
print(ough.candidates)
```

```text
(('ɔː', 0.0), ('əʊ', 1.0), ('ʌf', 2.0), ('ɒf', 3.0), ('aʊ', 4.0), ('uː', 5.0))
```

A rescorer re-costs exactly these six options. For *cough* /kɒf/ the model must lift `ɒf` to the front, and for *tough* /tʌf/ it must lift `ʌf`.

### Record shape

`features()` returns a `list[WordFeatures]`, one per word, with the same normaliser and word split as `transcribe`. A `WordFeatures` has the fields `word`, `code`, `script`, `confidence` and `graphemes`, a tuple of `GraphemeFeatures`. Each `GraphemeFeatures` has these fields:

| Field | Meaning |
| --- | --- |
| `grapheme`, `span` | The grapheme and its `(start, end)` offsets, with the contract of `SegmentSlot.span` |
| `index`, `position` | The index of the grapheme in its word, and `"initial"`, `"medial"` or `"final"` |
| `prev`, `next`, `prev2`, `next2` | The neighbouring graphemes in the word, or `None` past a word edge |
| `is_vowel`, `is_consonant`, `is_front`, `is_back` | The class predicates of `GraphemeContext` |
| `candidates` | The ranked `(ipa, cost)` options of the slot |
| `top1_ipa`, `top1_cost` | The best candidate and its cost |
| `margin` | The cost gap between the two best candidates, or `None` for a slot with one candidate |
| `n_candidates` | The number of candidates |
| `confidence` | The confidence of the word, repeated on each grapheme |
| `script`, `code` | The primary script of the spec and the resolved language code |

`margin` is `None`, not infinity, so that the dict stays valid strict JSON. A word with one grapheme gets `"initial"` as its position.

`GraphemeFeatures.as_dict()` renders one grapheme as a flat feature dict. Every value is a `str`, `int`, `float`, `bool` or `None`, so `json.dumps` accepts it and python-crfsuite takes it as an item. The span appears as `span_start` and `span_end`. `WordFeatures.as_dicts()` returns the feature sequence of the word, one dict per grapheme.

## Feeding a CRF

The two CRF snippets below are illustrative sketches: they need `sklearn-crfsuite` or `python-crfsuite`, which the library does not depend on. The output of `WordFeatures.as_dicts()` is already the per-token feature sequence that these libraries read. With sklearn-crfsuite:

```python
import sklearn_crfsuite
from orthography2ipa import G2P

en = G2P("en-GB")

# X: one feature-dict sequence per word. y: the gold IPA per grapheme.
X = [wf.as_dicts() for wf in en.features(" ".join(train_words))]
y = gold_ipa_labels                       # your aligned per-grapheme IPA

crf = sklearn_crfsuite.CRF()
crf.fit(X, y)                             # learns to re-rank the lattice
```

The python-crfsuite loop appends the same dicts:

```python
import pycrfsuite

trainer = pycrfsuite.Trainer()
for wf, labels in zip(en.features(text), gold_label_seqs):
    trainer.append(wf.as_dicts(), labels)   # xseq, yseq
trainer.train("g2p.crfsuite")
```

At inference, map the model's prediction back onto the lattice as a rescorer that makes the predicted IPA the cheapest candidate of its slot. The learned model then plugs into the shared beam instead of replacing it (see [Rescoring the lattice](lattice.md#rescoring-the-lattice)). The rescorer needs only `orthography2ipa`. In the example below, a toy function takes the place of the trained tagger:

```python
from orthography2ipa import get
from orthography2ipa.phonetok import PhonetokTokenizer, Candidate
from orthography2ipa.rescorer import LatticeRescorer

class PredictedRescorer(LatticeRescorer):
    def __init__(self, predict):        # predict(slot, context) -> IPA or None
        self.predict = predict

    def rescore(self, slot, context):
        chosen = self.predict(slot, context)
        if chosen is None:
            return slot.candidates
        others = [c for c in slot.candidates if c.ipa != chosen]
        return [Candidate(chosen, 0.0)] + [Candidate(c.ipa, c.cost + 1.0) for c in others]

def toy_predict(slot, context):         # stands in for a trained CRF tagger
    return "ʌf" if slot.grapheme == "ough" else None

tok = PhonetokTokenizer(get("en-GB"))
print(tok.ipa_best("tough"), tok.ipa_best("tough", rescorer=PredictedRescorer(toy_predict)))
```

```text
tɔː tʌf
```

The base beam still transcribes every word of every registered language. The model only re-costs candidates that the lattice already offers, and the confidence signal shows where that re-costing is worth doing.

---
[← Lattice PER](lattice_per.md) · [Home](index.md) · [Distance Metrics →](distance.md)
