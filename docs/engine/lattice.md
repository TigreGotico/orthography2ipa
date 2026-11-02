# The pronunciation lattice

Most words have one sensible pronunciation, and the hard cases are the words that have several. `orthography2ipa` does not hide that ambiguity behind a single answer. It exposes a lattice: for each grapheme of a word, the ranked IPA options that the grapheme can realise, each with a cost. The rest of the library, and the phonemizers built on it, consume this object.

This page follows the order in which a phonemizer author meets the lattice. It covers how candidates get their costs, the lattice and its rescorers, the per-word confidence, the cross-word sentence seam and the feature export. The [tokenizer](tokenizer.md) page covers how text becomes graphemes and how the beam search (`ipa_beam`) turns the same search space into whole-word readings.

## How cost works

`Candidate.cost` is an additive cost, and lower is better. The form of a grapheme's value in the spec selects one of two cost regimes:

| Grapheme value in the spec | Cost of candidate *i* |
| --- | --- |
| Plain list, such as `"c": ["k", "s"]` | `float(i)`, the rank `0, 1, 2, …` |
| Weighted object, such as `"er": {"ipa": ["ɜːɹ", "əɹ"], "weights": [0.2, 0.8]}` | `-log(pᵢ)`, where `pᵢ = weightᵢ / Σ weight` |

A plain list has no frequency data. The first IPA listed is the canonical form, so the spec author lists the most common pronunciation first. The rank says which candidate comes first, but it never gives a size of preference. Most graphemes in most specs use this regime. A spec with only plain lists gives the same transcriptions as it would with no weight support at all.

A weighted object attaches candidate frequencies from a corpus, and `weights` aligns index by index with `ipa`. In the en-GB ⟨er⟩ above, the common `əɹ` (p = 0.8) costs 0.22, and `ɜːɹ` (p = 0.2) costs 1.61. The beam therefore prefers `əɹ`, although the spec lists it second. A lower weight gives a higher cost, so the candidate falls further down the beam.

Because `-log p` is additive, the score of a whole path is the negative log of the product of its candidate probabilities. That is an unnormalised sequence log-probability, so the beam becomes a probabilistic search. The beam score of the best path is the sum of the top costs:

```python
from orthography2ipa import get
from orthography2ipa.phonetok import PhonetokTokenizer

tok = PhonetokTokenizer(get("en-GB"))
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

### Weights in the loaded spec

The JSON loader passes the grapheme table through [`orthography2ipa/weights.py`](../../orthography2ipa/weights.py), which turns both forms into one internal shape. `spec.graphemes` holds a plain IPA list for every grapheme, so every consumer reads it as a `list[str]` map. `spec.grapheme_weights` is sparse: it has an entry only for the graphemes written in the weighted form.

Both beams take their costs from `weights.candidate_base_costs`, through the shared resolver in `orthography2ipa.positional`. The standalone `PhonetokTokenizer.ipa_beam` and the engine's beam in `g2p.py` therefore always agree on the costs of a grapheme. Weights apply to the flat grapheme table only. When a `positional_graphemes` override fires, its candidates come first in their declared order, the flat alternatives follow, and all of them take rank costs.

### Malformed weights

Two layers check weights. The pydantic model `WeightedGraphemeModel` in [`orthography2ipa/schema.py`](../../orthography2ipa/schema.py) rejects a weighted value in three cases:

- the `weights` list and the `ipa` list differ in length,
- a weight is negative or not a number,
- the weights sum to 0 or less.

`orthography2ipa validate` and the test suite run this model on every shipped spec, so a malformed weight fails validation before it ships.

At run time, `candidate_base_costs` checks the same conditions again. If an entry fails, it emits a warning and the whole entry falls back to rank ordering. A bad weight can therefore never stop a transcription or silently drop a candidate.

One zero weight, with a positive sum elsewhere, is valid. Its probability gets the floor `WEIGHT_FLOOR = 1e-6`, so its cost is large but finite. The beam strongly disfavours that candidate, but it can still reach it.

### Weights do not inherit

`grapheme_weights` has the mode `InheritanceMode.NOT_INHERITED` in the `FIELD_INHERITANCE` manifest in [`types.py`](../../orthography2ipa/types.py). A variety that takes its `graphemes` from a parent through `graphemes_base` gets the parent's IPA lists but not its weights. It keeps rank ordering until it declares weights of its own. en-AU, for example, takes its graphemes from en-GB and has an empty `grapheme_weights`.

There are two reasons for this rule. First, candidate frequency is corpus data for one variety. The frequency of ⟨ou⟩ as /aʊ/ against /uː/ in en-GB is not the same statistic as in en-US, so a child must cite its own data. Second, an inheriting child keeps the plain rank ordering that its own data supports. Within one spec, the IPA list and the weights of a grapheme live in the same value, so an author writes and overrides them together.

### Where weights come from

Weights must be candidate frequencies from cited corpora, recorded in the spec's `sources` or `notes`. They are never parameters tuned to lower the PER. The en-GB spec weights ⟨er⟩, ⟨gh⟩ and ⟨ie⟩. Its sources are Gontijo, Gontijo & Shillcock (2003), *Grapheme-phoneme probabilities in British English*, and Berndt, Reggia & Mitchum (1987), *Empirically derived probabilities for grapheme-to-phoneme correspondences in English*. The spec's `notes` give the values and the reasons.

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
slots = tok.ipa_lattice("through")

assert "".join(s.top.ipa for s in slots) == tok.ipa_best("through")
```

The top candidates of the slots, joined, give `ipa_best` with its default arguments. The lattice has no slots for whitespace or punctuation. It therefore does not reflect a non-default `word_separator`, or `include_special=True`, passed to the beam. The beam flattens the options into whole-word `IPAPath` strings, while the lattice keeps every ranked option per position. Use the lattice to see why a word got its pronunciation, or to change the choice at one position.

## A worked example

English ⟨cough⟩ shows a small ambiguity. The ⟨c⟩ has a clear first choice, and the ⟨ough⟩ cluster has six readings.

```python
for slot in tok.ipa_lattice("cough"):
    print(slot.grapheme, slot.span, [(c.ipa, round(c.cost, 2)) for c in slot.candidates])
```

```text
c (0, 1) [('k', 0.0), ('s', 1.0)]
ough (1, 5) [('ɔː', 0.0), ('əʊ', 1.0), ('ʌf', 2.0), ('ɒf', 3.0), ('aʊ', 4.0), ('uː', 5.0)]
```

The top candidates give `kɔː`. The ⟨ough⟩ slot keeps five other readings in rank order. A downstream rule or lexicon can promote the correct one for this word, `ɒf`, without tokenizing the word again.

## Positional overrides apply here too

The lattice uses the same shared resolver as the full engine. Context-sensitive [positional overrides](positional_graphemes.md), the vowel-class positions included, therefore fire in the lattice. Spanish ⟨c⟩ is /θ/ before a front vowel and /k/ elsewhere:

```python
es_tok = PhonetokTokenizer(get("es-ES"))
c_slot = next(s for s in es_tok.ipa_lattice("cena") if s.grapheme == "c")
assert c_slot.top.ipa == "θ"
c_slot = next(s for s in es_tok.ipa_lattice("casa") if s.grapheme == "c")
assert c_slot.top.ipa == "k"
```

`G2P.ipa_lattice(word)` returns the same structure with more context. The engine supplies syllables and stress, so the stress-conditioned positions also fire. It also runs its rescorers over the slots, and these include the spec's `allophone_rules`. The en-GB non-rhotic rule, for example, removes the /ɹ/ of ⟨er⟩ at the end of a word:

```python
from orthography2ipa import G2P

print([c.ipa for c in tok.ipa_lattice("her")[1].candidates])
print([c.ipa for c in G2P("en-GB").ipa_lattice("her")[1].candidates])
```

```text
['əɹ', 'ɜːɹ']
['ə', 'ɜː']
```

The engine lattice is the pre-lexical lattice. The engine builds it before it inserts stress marks, before cross-word sandhi, and before any word-level override from `word_exceptions` or `grammatical_endings`. A downstream engine reasons over this object.

## What builds on the lattice

Several parts of the library read the `SegmentSlot` and `Candidate` shape without changing it:

| Consumer | What it does | Section |
| --- | --- | --- |
| Rescorer | Re-costs the candidates of each slot, given its neighbours, before a path is chosen | [Rescoring the lattice](#rescoring-the-lattice) |
| Confidence | Reads how sure the engine is about a word from the cost margins and the unmapped characters | [Per-word confidence](#per-word-confidence--oov-signal) |
| Sentence lattice | Puts the lattices of all words of an utterance in order, with phrase position | [The sentence-context seam](#the-sentence-context-seam) |
| Feature view | Exports the lattice and the grapheme context as flat records for a learned model | [Feature export for a learned model](#feature-export-for-a-learned-model) |
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

A rescorer sees the fully resolved lattice, with the candidates of every neighbouring slot, not a half-selected beam path. A list of rescorers therefore composes in a fixed way: they apply in order, and each one sees the output of the one before. In the engine, the caller's rescorers run first. The rescorers of declared plugins run next, and the spec's allophone rules run last, so the spec has the last word. The plugin stage is in [architecture.md](architecture.md#pluggable-steps).

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

The engine's own post-lexical allophone rules use this seam. A spec's declarative `allophone_rules` compile into an `AllophoneRescorer`, which replaces the IPA of a slot with its context-conditioned realisation. These rules are the second of the library's two maps, and [allophony.md](allophony.md) describes them. A downstream engine attaches its own cascade the same way, such as Arabic sun-letter assimilation or a Portuguese sibilant rule. The next section helps decide whether that is the right choice for an engine.

## Refine the lattice, or fork the tokenizer?

A downstream phonemizer can build on this library in three ways. It can refine the word lattice, use the sentence seam for cross-word rules, or fork. The shape of its rules decides which one fits, and each has a cost.

### Refine: rules as rescorers over the shared lattice

Keep the shared tokenizer and lattice, and add `LatticeRescorer` classes that re-cost candidates.

This fits when your rules choose, in context, among the candidates that the shared trie already lists. A coronal-triggered assimilation, a positional sibilant and a silent letter all have that shape. It also needs your IPA to come from candidate selection per grapheme, so `ipa_lattice` or `ipa_best` is, or can become, your generation path. In return you get maximal munch, positional conditioning, candidate weights and the confidence signal for every language. Your rules also compose with the built-in allophone rules and with each other.

Refinement has three limits:

1. A rescorer sees one slot and its neighbours in the same word. A rule that needs context outside the word does not fit a rescorer: cross-word sandhi, pausal and phrase-final forms, liaison, morphological decomposition, part of speech. The [sentence-context seam](#the-sentence-context-seam) is the shared layer for the cross-word part, so an engine does not need its own sentence orchestrator.
2. A rescorer can only choose among the candidates that the spec offers. If the spec leaves out or mis-states a candidate that a rule needs, re-costing cannot recover it. Examples are a semivowel that must geminate, or a word-final long vowel that competes with a consonant reading. The fix belongs in the spec data, not in a workaround.
3. If your engine makes IPA some other way, such as a character-level cascade, a rescorer does nothing until your generation goes through `ipa_lattice`.

### Fork: a bespoke tokenizer and rule engine

Own the tokenization and the rule pass from end to end.

This fits when you need a representation that neither the per-slot lattice nor the sentence seam can express. Examples are morphological structure, prosody, or an intermediate form that is not IPA. It also fits when your data differs so much from the base spec that inheriting it causes more work than it saves. A fork also gives independence from this library's release cycle, and a hand-tuned path where the general lattice costs more than it returns.

The cost is that you implement and maintain tokenization yourself: the maximal-munch scan and the digraph and trigraph handling, with their bugs. You also lose the shared grapheme data, positional conditioning, candidate weights, the confidence signal and every later engine fix. Your rules cannot compose with the rescorers of another engine or with the built-in allophone layer.

### In practice: hybrid, and push gaps upstream

Most engines become a hybrid. Phonology inside the word runs as rescorers over the shared lattice. Cross-word sandhi and pausal forms run as sentence rescorers over the shared sentence lattice. Lexical exceptions, and any representation that neither layer expresses, run on a small private layer that calls the lattice. A downstream engine such as [arbtok](https://github.com/TigreGotico/arbtok) can move waṣl, pausal forms and assimilation onto these seams. It then keeps private only the stages that are truly its own.

Enforce the boundary between the layers in code. A word that needs context must go to the layer that has that context, never silently through a layer that does not.

Treat each missing capability as a task for this library, not as a reason to fork for good. Sometimes a rule cannot be expressed, because the shared spec has the wrong candidate or the engine lacks a hook. Then fix the spec or add the hook. More of each engine then moves onto the shared lattice, and the next engine gets the fix too.

## Per-word confidence / OOV signal

The lattice also tells how sure the base engine is about a word. A downstream phonemizer uses this signal to decide where to spend effort. A word with high confidence can keep the base engine's reading. A word with low confidence is where an expensive lexicon lookup, a hand-written rule cascade or a learned model pays off.

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

## The sentence-context seam

The word lattice and its rescorers stop at the word boundary. A whole class of processes lives between words, and the word lattice cannot express them:

| Process | What happens |
| --- | --- |
| Arabic waṣl | The *hamzat al-waṣl* of a word, such as the vowel of the definite article, elides after a preceding word |
| Arabic pausal forms | A phrase-final word is realised differently, with *tanwīn* suppression and *tāʾ marbūṭa* as [h] |
| French liaison | A latent word-final consonant becomes the onset of the next word before a vowel |
| Portuguese external /s/-sandhi | A word-final /s/ changes across the word boundary |

Each of these needs two things that the word lattice does not carry. It needs to see the edge of the adjacent word, that is its final or initial candidates. It also needs the position of the word in its phrase and in the utterance. The sentence-context seam is the shared cross-word surface that gives both.

### `SentenceLattice`: the utterance, in order

`G2P.sentence_lattice(text, *, search="greedy", beam_width=8)` returns a `SentenceLattice`. It holds the utterance as an ordered tuple of `WordSlot` objects, one per word:

```python
g = G2P("pt")
sl = g.sentence_lattice("olá mundo, bonito!")
for w in sl:
    print(w.surface, w.ipa, w.phrase_position.value, w.utterance_position.value)
```

```text
olá oˈla initial initial
mundo ˈmũdu final medial
bonito buˈnitu sole final
```

| `WordSlot` member | Meaning |
| --- | --- |
| `surface` | The normalised spelling of the word |
| `ipa` | The word's IPA in isolation, after stress and before any sentence rescorer or sandhi, not yet NFC-composed |
| `slots` | The word's lattice, equal to `G2P.ipa_lattice(w.surface)`, and empty for a `word_exceptions` override or a word with no mapped grapheme |
| `index` | The position of the word in the utterance |
| `phrase_position`, `utterance_position` | The `Position` of the word in its phrase and in the utterance |
| `pausal` | True when the word stands before a pause, equal to `phrase_position.is_final()` |
| `initial_slot`, `final_slot` | The first and last lattice slots, the onset and coda edges that a cross-word rule inspects, or `None` with no lattice |

A consumer sees the ranked candidates of every word in order, not a flattened string. The lattice iterates and indexes over its words. Its `ipa` property joins the per-word IPA with spaces. `sentence_lattice` only reads: it applies no sentence rescorer and no sandhi, and it never changes `transcribe`.

The `search` argument works as in `transcribe`. With the default `"greedy"`, each slot keeps only its top candidate. Pass `search="beam"` to keep up to `beam_width` candidates per slot.

### `SentenceRescorer`: the boundary-aware rewrite

`SentenceRescorer` is the counterpart of `LatticeRescorer` at sentence scope. The engine calls it once per word with a `SentenceRescoreContext`, and it returns that word's IPA, rewritten or not:

```python
from abc import ABC
from orthography2ipa.sentence import WordSlot, SentenceRescoreContext

class SentenceRescorer(ABC):
    def rescore(self, word: WordSlot, context: SentenceRescoreContext) -> str: ...
```

The context gives a cross-word rule what the word lattice cannot:

| Member | Meaning |
| --- | --- |
| `prev_word`, `next_word` | The adjacent `WordSlot`, with its `final_slot` or `initial_slot`, or `None` at an utterance edge |
| `this_word_ipa`, `prev_word_ipa`, `next_word_ipa` | The current IPA of each word in the chain, which includes the rewrites of earlier rescorers |
| `phrase_position`, `utterance_position` | The `Position` of the word |
| `is_phrase_initial`, `is_phrase_final`, `is_utterance_initial`, `is_utterance_final` | Shortcuts over the two positions |
| `word`, `index`, `words`, `lang` | The word, its index, all words and the resolved language code |

Return `context.this_word_ipa` for a no-op. A process can change both words at a boundary. Each word's call rewrites its own side while it reads the shared boundary. That is how resyllabification and waṣl elision on the right word work.

### Phrase and utterance position

A phrase is a run of words between two pauses, or between a pause and an utterance edge. A pause is a mark in `orthography2ipa.phonetok.PAUSE_PUNCTUATION`, which covers the pause marks of each script. For Latin text these are `. , ; : ! ? …`. The tokenizer uses the same boundary when it marks a word as pausal.

`Position` is computed for the phrase and for the whole utterance. The first word of a span is `INITIAL`, the last is `FINAL` and the words between are `MEDIAL`. A span of one word is `SOLE`, and `SOLE` counts as both initial and final for `is_initial()` and `is_final()`.

### Example: Arabic waṣl and pausal forms

These two rescorers are toys that show the seam. The library does not ship them as language data. They show that the seam gives the cross-word view and the phrase position that an Arabic engine needs.

```python
from orthography2ipa.sentence import SentenceRescorer

class WaslElision(SentenceRescorer):        # rewrites the right word of a boundary
    def rescore(self, word, context):
        ipa = context.this_word_ipa
        onset = word.initial_slot
        if context.prev_word is not None and onset is not None and onset.grapheme == "ال":
            return ipa.replace("a", "", 1)  # elide the vowel of the article
        return ipa

class PausalForm(SentenceRescorer):         # driven by phrase position
    def rescore(self, word, context):
        ipa = context.this_word_ipa
        if context.is_phrase_final and ipa and not ipa.endswith("ʔ"):
            return ipa + "ʔ"                # toy pausal citation form
        return ipa

text = "الكتاب الجديد"
print(G2P("ar").transcribe(text))
print(G2P("ar", sentence_rescorer=[WaslElision(), PausalForm()]).transcribe(text))
```

```text
alkˈtaːb ˈaldʒdjd
alkˈtaːb ˈldʒdjdʔ
```

The first word opens the utterance, so waṣl has no preceding word and does nothing. On the second word, the article's vowel elides across the boundary, and the pausal form then applies because the word ends the phrase. The adjacent word (`prev_word`), the edge slot (`initial_slot`) and the phrase position (`is_phrase_final`) drove both edits.

### Example: French liaison

```python
VOWELS = set("aeiouyɛɔøœɑ")

class FrenchLiaison(SentenceRescorer):
    LATENT = {"s", "x", "z"}

    def rescore(self, word, context):
        ipa = context.this_word_ipa
        prev = context.prev_word
        if prev and prev.surface[-1:] in self.LATENT and ipa[:1] in VOWELS:
            return "z" + ipa                # the right word gains the /z/ onset
        if (context.next_word and word.surface[-1:] in self.LATENT
                and (context.next_word_ipa or "")[:1] in VOWELS):
            return ipa + "‿"                # the left word marks the liaison tie
        return ipa

print(G2P("fr").transcribe("nous avons"))
print(G2P("fr", sentence_rescorer=FrenchLiaison()).transcribe("nous avons"))
```

```text
nu avɔ̃
nu‿ zavɔ̃
```

The latent final consonant of *nous* becomes the onset of *avons*. The right word gains /z/, and the left word marks the tie. A rewrite of the left word only cannot move a segment onto the next word, and this seam can.

### How it composes with sandhi

The sentence seam sits above the word lattice. Each `WordSlot.slots` is the word's `ipa_lattice`. A `SentenceRescorer` reads the edge slots and rewrites at the level of the word's IPA.

In `transcribe`, the sentence rescorers run first, with a view of the whole utterance. The spec's declarative `sandhi_rules` then run through `SandhiEngine`, and the two coexist. A list of sentence rescorers composes like lattice rescorers: each pass sees the rewrites of the pass before it. Inside one pass, every word reads the same snapshot taken before the pass, so the order of the words does not change the result.

The engine passes `SandhiEngine.apply` the pause flag of each word, so a declarative rule stays inside its prosodic domain. No rule joins two words that a pause separates (Nespor & Vogel 1986, *Prosodic Phonology*). The blocked boundary is the intonational phrase, which is what punctuation writes. Some rules have the smaller phonological phrase as their real domain. Such a rule still applies at a phonological-phrase edge inside a clause, so the pause flags give a lower bound only. A sentence rescorer sees the same positions through `WordSlot.phrase_position`.

### Off by default

Nothing in this seam runs unless a caller passes `sentence_rescorer=` to `G2P`, or calls `sentence_lattice`. Without a sentence rescorer, `transcribe` does not use the seam, and the scoring of single words and the benchmark board do not change. A spec's `sandhi_rules` work the same either way. The seam adds no spec field: cross-word rules are plugin objects that the caller supplies, so the spec data surface stays the same.

### Still downstream: semantic and part-of-speech disambiguation

This seam gives position and cross-word adjacency, not meaning. It cannot express a homograph choice that needs part of speech or sense. Examples are English *read* /riːd/ against /rɛd/, and Portuguese *sede* 'thirst' against 'headquarters'. The context carries no part-of-speech or sense field, on purpose, and that choice stays with a downstream engine.

## Feature export for a learned model

`orthography2ipa` ships no trained weights. Every candidate cost is a `-log p` from cited frequencies or a rank cost from the spec. That makes the library a good feature provider for a statistical model downstream.

For each grapheme the library already computes what a sequence model needs: the class predicates, the word-local neighbours, the ranked candidate lattice with its costs, and the per-word confidence. `G2P.features(text)` packages that structure as a flat feature view that serialises to JSON. A CRF, or a small neural G2P, can then train on linguistic features instead of raw character n-grams. `features()` only reads, and it never changes `transcribe`. It reuses `G2P.ipa_lattice`, `confidence_breakdown` and the [`GraphemeContext`](tokenizer.md#context-model) predicates, and it computes no vowel logic of its own.

### The CRF-as-rescorer pattern

The lattice and the learned model work together in three steps:

1. The library gives the candidate lattice and the features. For each grapheme you get the ranked `(ipa, cost)` options and a feature record that describes the position.
2. A trained model re-costs the candidates. A CRF labels each grapheme with the IPA it should realise. A `LatticeRescorer` then makes the predicted candidate the cheapest option of its slot. The model refines the beam and does not replace it, and the beam stays the fallback wherever the model is unsure.
3. The confidence signal shows where learned capacity pays off. Every feature record carries the confidence of its word. The base engine already decides the words with confidence near 1.0. The model is useful on the ambiguous words, such as English ⟨ough⟩ and ⟨th⟩. You can weight training, or gate inference, on that signal.

### A feature record

```python
for wf in en.features("cough"):
    print(wf.word, "confidence", round(wf.confidence, 4))
    for gr in wf.graphemes:
        print(gr.as_dict())
```

```text
cough confidence 0.6321
{'grapheme': 'c', 'index': 0, 'position': 'initial', 'span_start': 0, 'span_end': 1, 'prev': None, 'next': 'ough', 'prev2': None, 'next2': None, 'is_vowel': False, 'is_consonant': True, 'is_front': False, 'is_back': False, 'top1_ipa': 'k', 'top1_cost': 0.0, 'margin': 1.0, 'n_candidates': 2, 'confidence': 0.6321205588285577, 'script': 'Latin', 'code': 'en-GB'}
{'grapheme': 'ough', 'index': 1, 'position': 'final', 'span_start': 1, 'span_end': 5, 'prev': 'c', 'next': None, 'prev2': None, 'next2': None, 'is_vowel': True, 'is_consonant': False, 'is_front': False, 'is_back': True, 'top1_ipa': 'ɔː', 'top1_cost': 0.0, 'margin': 1.0, 'n_candidates': 6, 'confidence': 0.6321205588285577, 'script': 'Latin', 'code': 'en-GB'}
```

⟨cough⟩ is one word with two grapheme slots. Its confidence of 0.6321 marks it as ambiguous, so it is a place where a learned model should focus. The ⟨ough⟩ slot is a vowel grapheme with six ranked candidates.

The `candidates` field of the dataclass holds the full ranked lattice of the slot, the same six options as in [A worked example](#a-worked-example). The dict from `as_dict` leaves it out, so that every value stays a scalar for CRF libraries. A rescorer re-costs exactly these six options. For *cough* /kɒf/ the model must lift `ɒf` to the front, and for *tough* /tʌf/ it must lift `ʌf`.

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

`GraphemeFeatures.as_dict()` renders one grapheme as a flat feature dict. Every value is a `str`, `int`, `float`, `bool` or `None`, so `json.dumps` accepts it. The span appears as `span_start` and `span_end`. `WordFeatures.as_dicts()` returns the feature sequence of the word, one dict per grapheme.

### Feeding a CRF

The output of `WordFeatures.as_dicts()` is already the per-token feature sequence that CRF libraries read. sklearn-crfsuite takes one such sequence per word as `X` in `CRF().fit(X, y)`, with `y` the aligned gold IPA per grapheme. python-crfsuite takes it as the `xseq` of `Trainer.append(xseq, yseq)`. The library does not depend on either package.

At inference, map the model's prediction back onto the lattice as a rescorer. The rescorer needs only `orthography2ipa`. In the example below, a toy function takes the place of the trained tagger:

```python
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

print(tok.ipa_best("tough"), tok.ipa_best("tough", rescorer=PredictedRescorer(toy_predict)))
```

```text
tɔː tʌf
```

The base beam still transcribes every word of every registered language. The model only re-costs candidates that the lattice already offers, and the confidence signal shows where that re-costing is worth doing.

---
[← Tokenizer](tokenizer.md) · [Home](../index.md) · [Lattice PER →](lattice_per.md)
