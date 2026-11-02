# The pronunciation lattice

Most words have one sensible pronunciation, and the hard cases are the words that have several. `orthography2ipa` does not hide that ambiguity behind a single answer. It exposes a lattice: for each grapheme of a word, the ranked IPA options that the grapheme can realise, each with a cost. The rest of the library, and the phonemizers built on it, consume this object.

This page covers the lattice, its costs, rescoring and the confidence signal. The [tokenizer](tokenizer.md) page covers how text becomes graphemes and how the beam search (`ipa_beam`) turns the same search space into whole-word readings.

## What the lattice is

A lattice is a list of slots, one per grapheme, in surface order. Each slot is a `SegmentSlot`:

| Member | Meaning |
| --- | --- |
| `grapheme` | The source grapheme, lower-cased as the tokenizer produced it |
| `span` | The `(start, end)` character offsets, with the same contract as `GraphemeContext.span`: `unicodedata.normalize("NFC", text)[start:end].lower() == grapheme` |
| `candidates` | A tuple of `Candidate(ipa, cost)`, best (lowest cost) first |
| `top` | The first candidate, which is the canonical choice |

Two methods return a lattice. `PhonetokTokenizer.ipa_lattice(text, *, beam_width=8, expand_allophones=False, rescorer=None)` works from the spec alone. `G2P.ipa_lattice(word, *, beam_width=8)` adds the engine's context, as [Positional overrides apply here too](#positional-overrides-apply-here-too) explains. In both, `beam_width` is the number of candidates kept per slot, and `-1` keeps all of them. The truncation never removes the top candidate. A grapheme that resolves to no candidates, such as a silent marker letter, gets no slot.

The costs of the slots are independent and additive. The lattice and the beam are therefore two views of the same search:

```python
from orthography2ipa import get
from orthography2ipa.phonetok import PhonetokTokenizer

tok = PhonetokTokenizer(get("en-GB"))
slots = tok.ipa_lattice("through")

assert "".join(s.top.ipa for s in slots) == tok.ipa_best("through")
```

The top candidates of the slots, joined, give `ipa_best` with its default arguments. The lattice has no slots for whitespace or punctuation. It therefore does not reflect a non-default `word_separator`, or `include_special=True`, passed to the beam. The beam flattens the options into whole-word `IPAPath` strings, while the lattice keeps every ranked option per position. Use the lattice to see why a word got its pronunciation, or to change the choice at one position.

## A worked example

English ⟨cough⟩ shows a small ambiguity. The ⟨c⟩ has a clear first choice, and the ⟨ough⟩ cluster has six readings.

```python
tok = PhonetokTokenizer(get("en-GB"))
for slot in tok.ipa_lattice("cough"):
    print(slot.grapheme, slot.span, [(c.ipa, round(c.cost, 2)) for c in slot.candidates])
```

```text
c (0, 1) [('k', 0.0), ('s', 1.0)]
ough (1, 5) [('ɔː', 0.0), ('əʊ', 1.0), ('ʌf', 2.0), ('ɒf', 3.0), ('aʊ', 4.0), ('uː', 5.0)]
```

The top candidates give `kɔː`. The ⟨ough⟩ slot keeps five other readings in rank order. A downstream rule or lexicon can promote the correct one for this word, `ɒf`, without tokenizing the word again.

## How cost works

`Candidate.cost` is an additive cost, and lower is better. Each grapheme uses one of two regimes.

A grapheme with a plain list of candidates, such as `"e": ["e", "ɛ"]`, has no frequency data. Its cost is the rank: 0.0 for the first candidate, 1.0 for the next, and so on. Most graphemes in most specs use this regime.

A grapheme can instead declare candidate frequencies. The en-GB spec declares `"er": {"ipa": ["ɜːɹ", "əɹ"], "weights": [0.2, 0.8]}`. The weights become a probability distribution, and the cost of each candidate is `-log p`. The common `əɹ` (p = 0.8) costs 0.22, and `ɜːɹ` (p = 0.2) costs 1.61. The beam therefore prefers `əɹ`, although the spec lists it second. The weight format, the rules for malformed weights and the sourcing rules are in [candidate_scoring.md](candidate_scoring.md).

Because `-log p` is additive, the score of a whole path is the negative log of the product of its candidate probabilities. That is an unnormalised sequence log-probability. The beam score of the best path is the sum of the top costs:

```python
slots = tok.ipa_lattice("gher")
best = tok.ipa_beam("gher", beam_width=1)[0]
for s in slots:
    print(s.grapheme, [(c.ipa, round(c.cost, 3)) for c in s.candidates])
print(best.ipa, best.score == sum(s.top.cost for s in slots))
```

```text
gh [('', 0.163), ('f', 2.12), ('ɡ', 3.507)]
er [('əɹ', 0.223), ('ɜːɹ', 1.609)]
əɹ True
```

## Positional overrides apply here too

The lattice uses the same shared resolver as the full engine. Context-sensitive [positional overrides](positional_graphemes.md), the vowel-class positions included, therefore fire in the lattice. Spanish ⟨c⟩ is /θ/ before a front vowel and /k/ elsewhere:

```python
tok = PhonetokTokenizer(get("es-ES"))
c_slot = next(s for s in tok.ipa_lattice("cena") if s.grapheme == "c")
assert c_slot.top.ipa == "θ"
c_slot = next(s for s in tok.ipa_lattice("casa") if s.grapheme == "c")
assert c_slot.top.ipa == "k"
```

`G2P.ipa_lattice(word)` returns the same structure with more context. The engine supplies syllables and stress, so the stress-conditioned positions also fire. It also runs its rescorers over the slots, and these include the spec's `allophone_rules`. The en-GB non-rhotic rule, for example, removes the /ɹ/ of ⟨er⟩ at the end of a word:

```python
from orthography2ipa import G2P

print([c.ipa for c in PhonetokTokenizer(get("en-GB")).ipa_lattice("her")[1].candidates])
print([c.ipa for c in G2P("en-GB").ipa_lattice("her")[1].candidates])
```

```text
['əɹ', 'ɜːɹ']
['ə', 'ɜː']
```

The engine lattice is the pre-lexical lattice. The engine builds it before it inserts stress marks, before cross-word sandhi, and before any word-level override from `word_exceptions` or `grammatical_endings`. A downstream engine reasons over this object.

## What builds on the lattice

Several parts of the library read the `SegmentSlot` and `Candidate` shape without changing it:

| Consumer | What it does | Page |
| --- | --- | --- |
| Rescorer | Re-costs the candidates of each slot, given its neighbours, before a path is chosen | [Rescoring the lattice](#rescoring-the-lattice) |
| Confidence | Reads how sure the engine is about a word from the cost margins and the unmapped characters | [Per-word confidence](#per-word-confidence--oov-signal) |
| Sentence lattice | Puts the lattices of all words of an utterance in order, with phrase position | [sentence_context.md](sentence_context.md) |
| Feature view | Exports the lattice and the grapheme context as flat records for a learned model | [features.md](features.md) |
| Lattice PER | Scores a phone sequence against every reading the lattice admits | [lattice_per.md](lattice_per.md) |

## Rescoring the lattice

A rescorer lets a downstream rule cascade run over the shared lattice, instead of a parallel tokenizer. It is a pure pass that re-costs the candidates of one slot, given the slot and its context. It can also reorder, add or remove candidates, or delete the slot.

### Where it runs in the pipeline

A rescorer runs after the resolver has made each slot's candidates, with their positional order and weight costs. It runs before the beam selects a path:

```
normalize → tokenize → resolve branches (positional + weights)
                          │
                          ▼
                       rescore   ← re-cost each slot given its neighbours
                          │
                          ▼
             beam path selection → stress → sandhi → dialect
```

A rescorer sees the fully resolved lattice, with the candidates of every neighbouring slot, not a half-selected beam path. A list of rescorers therefore composes in a fixed way: they apply in order, and each one sees the output of the one before. The post-lexical allophone pass attaches at the same point. A rewrite from phoneme to surface form is a rescorer that replaces the IPA of a slot with its context-conditioned realisation.

### The API

Subclass `LatticeRescorer` and implement `rescore(slot, context)`. Pass the rescorer with the `rescorer=` argument of `ipa_beam`, `ipa_best` or `ipa_lattice` on the tokenizer, or of the `G2P(...)` constructor. The argument takes one rescorer or a list. With the default `None`, the lattice and the beam do not change.

`rescore` returns the slot's candidate list. The engine sorts the returned candidates by `(cost, ipa)` before the beam reads them, so a rescorer promotes a candidate by lowering its cost. Returning `slot.candidates` unchanged is a no-op. An empty list deletes the slot: the slot gives no segment to any path, and `ipa_lattice` leaves it out. A silent-letter rule uses this.

The `RescoreContext` gives the rescorer these members:

| Member | Meaning |
| --- | --- |
| `slot`, `index`, `slots` | The current slot, its position in the word and all slots of the word, so `slots[index] is slot` |
| `grapheme` | The [`GraphemeContext`](tokenizer.md#context-model) of the slot, with word-local `prev` and `next` and the class predicates |
| `prev_slot`, `next_slot` | The neighbouring slots in the same word, or `None` at a word edge or when an earlier rescorer deleted the neighbour |
| `is_word_initial` | True for the first grapheme of the word |
| `is_word_final` | True when every later grapheme of the word is silent, so it marks the last pronounced grapheme |
| `syll_idx`, `stressed_syll_idx`, `is_stressed` | Syllable and stress information, or `None` where it is not available |

The context never crosses a word boundary, on either entry path. Stress information depends on the entry path. The engine methods `G2P.transcribe` and `G2P.ipa_lattice` compute syllables and stress, so they fill the stress members. The tokenizer methods `PhonetokTokenizer.ipa_beam` and `ipa_lattice` have no stress detection, so these members are `None` there. A rescorer that needs stress must check for `None`, and it can do nothing when stress is absent.

In the engine, the caller's rescorers run first. The rescorers of declared plugins run next, and the spec's allophone rules run last, so the spec has the last word. The plugin stage is in [architecture.md](architecture.md).

### Worked example: final devoicing

Final-obstruent devoicing makes a voiced obstruent voiceless at the end of a word, as in German, Dutch, Russian and Catalan. The whole rule fits in a short rescorer. English has no such rule, so the example applies it to en-GB to show the effect:

```python
from orthography2ipa import G2P, LatticeRescorer, Candidate

class FinalDevoicing(LatticeRescorer):
    VOICED = {"b": "p", "d": "t", "ɡ": "k", "z": "s", "v": "f", "ʒ": "ʃ"}

    def rescore(self, slot, context):
        if not context.is_word_final:
            return slot.candidates
        return [Candidate(self.VOICED.get(c.ipa, c.ipa), c.cost)
                for c in slot.candidates]

print(G2P("en-GB").transcribe("dog"))
print(G2P("en-GB", rescorer=FinalDevoicing()).transcribe("dog"))
```

```text
ˈdɒɡ
ˈdɒk
```

The same shape expresses ⟨c⟩ softening before a front vowel: read `context.grapheme.next.is_front` and lower the cost of the soft candidate. A sun-letter assimilation reads the IPA of `context.prev_slot`. The rule reads the shared lattice and never tokenizes again.

### Who builds on this

The engine's own post-lexical allophone rules use this seam. A spec's declarative `allophone_rules` compile into an `AllophoneRescorer`, which the engine runs after phoneme selection. These rules are the second of the library's two maps, and [allophony.md](allophony.md) describes them. A downstream engine attaches its own cascade the same way, such as Arabic sun-letter assimilation or a Portuguese sibilant rule. The next section helps decide whether that is the right choice for an engine.

## Refine the lattice, or fork the tokenizer?

A downstream phonemizer can build on this library in two ways. The shape of its rules decides which one fits. Both are supported, and each has a cost.

### Refine: rules as rescorers over the shared lattice

Keep the shared tokenizer and lattice, and add `LatticeRescorer` classes that re-cost candidates.

This fits when your rules choose, in context, among the candidates that the shared trie already lists. A coronal-triggered assimilation, a positional sibilant and a silent letter all have that shape. It also needs your IPA to come from candidate selection per grapheme, so `ipa_lattice` or `ipa_best` is, or can become, your generation path. In return you get maximal munch, positional conditioning, candidate weights and the confidence signal for every language. Your rules also compose with the built-in allophone rules and with each other.

Refinement has three limits:

1. A rescorer sees one slot and its neighbours in the same word. A rule that needs context outside the word does not fit a rescorer: cross-word sandhi, pausal and phrase-final forms, morphological decomposition, part of speech. Such a rule belongs in a thin layer above the lattice. The [sentence-context seam](sentence_context.md) (`SentenceLattice` and `SentenceRescorer`) is that shared layer. It gives cross-word adjacency and phrase and utterance position, so an engine does not need to fork its own.
2. A rescorer can only choose among the candidates that the spec offers. If the spec leaves out or mis-states a candidate that a rule needs, re-costing cannot recover it. Examples are a semivowel that must geminate, or a word-final long vowel that competes with a consonant reading. The fix belongs in the spec data, not in a workaround.
3. If your engine makes IPA some other way, such as a character-level cascade, a rescorer does nothing until your generation goes through `ipa_lattice`.

### Fork: a bespoke tokenizer and rule engine

Own the tokenization and the rule pass from end to end.

This fits when you need a representation that the per-slot lattice cannot express. Examples are rules over the whole utterance, morphological structure, prosody, or an intermediate form that is not IPA. It also fits when your data differs so much from the base spec that inheriting it causes more work than it saves. A fork also gives independence from this library's release cycle, and a hand-tuned path where the general lattice costs more than it returns.

The cost is that you implement and maintain tokenization yourself: the maximal-munch scan and the digraph and trigraph handling, with their bugs. You also lose the shared grapheme data, positional conditioning, candidate weights, the confidence signal and every later engine fix. Your rules cannot compose with the rescorers of another engine or with the built-in allophone layer.

### In practice: hybrid, and push gaps upstream

Most engines become a hybrid. Phonology inside the word runs as rescorers over the shared lattice. The non-local part, such as cross-word sandhi, pausal forms and lexical exceptions, runs on a small layer that calls the lattice. Enforce the boundary between the two in code. A word that needs cross-word context must go to the layer that has that context, never silently through the word lattice.

Treat each missing capability as a task for this library, not as a reason to fork for good. Sometimes a rule cannot be expressed, because the shared spec has the wrong candidate or the engine lacks a hook. Then fix the spec or add the hook. More of each engine then moves onto the shared lattice, and the next engine gets the fix too.

## Per-word confidence / OOV signal

The lattice also tells how sure the base engine is about a word. A downstream phonemizer uses this signal to decide where to spend effort. A word with high confidence can keep the base engine's reading. A word with low confidence is where an expensive lexicon lookup or a hand-written rule cascade pays off.

The signal is a deterministic read of the lattice, with no global state, so it is thread-safe. It comes in three forms:

| Where | What |
| --- | --- |
| `WordTranscription.confidence` | A float on every word of a `transcribe_detailed(...)` result |
| `G2P.word_confidence(word, *, beam_width=8)` | The float for one word |
| `G2P.confidence_breakdown(word, *, beam_width=8)` | A `ConfidenceBreakdown` with the detail per slot, to find the position the engine was unsure about |

`ConfidenceBreakdown` has the fields `value`, `lattice`, `per_slot`, `coverage` and `unmapped`. The functions `slot_confidence(slot)` and `lattice_confidence(slots)` in `orthography2ipa.phonetok` compute the two lattice terms.

### The formula

Confidence uses only the costs that the lattice already carries (see [How cost works](#how-cost-works)). It combines three signals.

Ambiguity is the margin between the two best candidates of a slot. Let cost₁ and cost₂ be the two lowest costs, and let m = cost₂ - cost₁. A slot with one candidate has no rival, so m is infinite. The margin maps into [0, 1]:

```
ambiguity = 1 - exp(-m)      # m = 0 gives 0 (a tie), m = inf gives 1 (decisive)
```

Rarity is the cost of the winner. A slot whose winner has a high cost, such as a rare mapping with a large `-log p`, is less trustworthy than a slot whose winner costs 0:

```
rarity = exp(-cost₁)         # cost₁ = 0 gives 1, a larger cost gives less
```

Coverage is the fraction of the word's characters that map to a grapheme. An unmapped character means the engine has no opinion at that point. `WordTranscription.coverage` holds this value, and it multiplies straight in.

Each slot multiplies its two lattice factors. Across the word the minimum slot wins, and coverage then multiplies in:

```
slot_confidence = ambiguity × rarity
word_confidence = min(slot_confidence over all slots) × coverage
```

The minimum is deliberate. A downstream engine needs to know whether any position is uncertain, not the average. `confidence_breakdown` gives the full `per_slot` tuple, so a caller can compute a mean or find the single hard grapheme instead. A `word_exceptions` override is a certain answer, so its lattice confidence is 1.0, and only coverage can lower it. An empty lattice also has lattice confidence 1.0.

### Worked example: where a downstream engine spends effort

```python
from orthography2ipa import G2P

es = G2P("es-ES")
print(es.word_confidence("luz"), es.word_confidence("gato"))
```

```text
1.0 0.6321205588285577
```

Every grapheme of Spanish ⟨luz⟩ has one candidate in the engine lattice. Every margin is infinite, so the confidence is 1.0. In ⟨gato⟩, ⟨g⟩ has the rival /x/ and ⟨o⟩ has the rival /ɔ/, each at rank cost 1.0 over a winner that costs 0. Each of those slots scores 1 - exp(-1) ≈ 0.6321, and the weakest slot sets the word. A Spanish phonemizer can skip ⟨luz⟩ and spend its lexicon on words like ⟨gato⟩.

A spec with weights gives a graded answer instead of the flat 0.6321 of rank costs:

```python
en = G2P("en-GB")
print(en.word_confidence("bar"), round(en.word_confidence("her"), 4))
print([(c.ipa, round(c.cost, 3)) for c in en.ipa_lattice("her")[1].candidates])
```

```text
1.0 0.6
[('ə', 0.223), ('ɜː', 1.609)]
```

In ⟨bar⟩, ⟨b⟩ and ⟨ar⟩ each have one candidate. In ⟨her⟩, the weighted ⟨er⟩ slot has a margin of 1.609 - 0.223 = 1.386, so its ambiguity is 1 - exp(-1.386) = 0.75. The winner does not cost 0, so its rarity is exp(-0.223) = 0.80. The slot, and the word, score 0.75 × 0.80 = 0.60. The probabilistic ambiguity of ⟨er⟩ gives a number between the certain 1.0 and a tie.

An unmapped character lowers confidence through coverage:

```python
b = en.confidence_breakdown("bar你")
print(b.value, b.lattice, b.per_slot, b.coverage, b.unmapped)
```

```text
0.75 1.0 (1.0, 1.0) 0.75 ('你',)
```

Three of the four characters map, so coverage is 0.75. The lattice of ⟨bar⟩ is certain, so the word confidence is 1.0 × 0.75. A word with an unmapped character is the clearest case for a downstream engine, or a person, to handle.

---
[← Candidate scoring](candidate_scoring.md) · [Home](index.md) · [The sentence-context seam →](sentence_context.md)
