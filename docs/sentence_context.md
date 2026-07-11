# The sentence-context seam

The [pronunciation lattice](lattice.md) is deliberately **word-local**: a
`LatticeRescorer` sees one grapheme slot and its neighbours *within a word*,
and never crosses a word boundary. That is the right scope for word-internal
phonology, but a whole class of processes lives *between* words and cannot be
expressed there:

- **Arabic** `waṣl` — a following word's initial *hamzat al-waṣl* (the
  definite article's vowel) elides across a boundary — and **pausal** forms —
  a phrase-final word is realised differently (`tanwīn` suppression,
  `tāʾ marbūṭa` → [h]);
- **French liaison** — a latent word-final consonant resyllabifies as the
  *next* word's onset before a vowel;
- **Portuguese** external `/s/`-sandhi across a word boundary.

Each needs two things the word lattice does not carry: **visibility into the
adjacent word's edge** (its final / initial candidates) and the word's
**phrase / utterance position**. Historically a downstream engine that needed
those forked a private sentence orchestrator on top of this library. The
**sentence-context seam** is the shared cross-word surface downstream consumes
instead — so it does not have to fork one.

## The two objects

### `SentenceLattice` — the utterance, in order

`G2P.sentence_lattice(text) -> SentenceLattice` exposes the whole utterance as
an **ordered** list of `WordSlot`, each carrying that word's per-grapheme
[lattice](lattice.md) (`SegmentSlot`s), its chosen IPA, and its position:

```python
from orthography2ipa import G2P, Position

g = G2P("pt")
sl = g.sentence_lattice("olá mundo, bonito!")
for w in sl:
    print(w.surface, w.ipa, w.phrase_position.value, w.utterance_position.value)
```

```text
olá     oˈla     initial   initial
mundo   ˈmundu   final     medial
bonito  buˈnitu  sole      final
```

A consumer sees the ranked candidates of **every** word in order (not a
flattened string): `w.slots` is exactly what `G2P.ipa_lattice(w.surface)`
returns, and `w.initial_slot` / `w.final_slot` are the onset / coda edge slots
a cross-word rule reaches across a boundary to inspect. `sentence_lattice` is a
pure **read** — it applies no rescorers and never affects `transcribe`.

### `SentenceRescorer` — the boundary-aware rewrite seam

`SentenceRescorer` is the `LatticeRescorer` analogue at sentence scope. It is
invoked once per word with a `SentenceRescoreContext` and returns that word's
(possibly rewritten) IPA:

```python
class SentenceRescorer(ABC):
    def rescore(self, word: WordSlot, context: SentenceRescoreContext) -> str: ...
```

The context gives a cross-word rule what the word lattice cannot:

- `context.prev_word` / `context.next_word` — the adjacent `WordSlot`s (with
  their `.final_slot` / `.initial_slot` edge candidates), `None` at an
  utterance edge;
- `context.prev_word_ipa` / `context.next_word_ipa` / `context.this_word_ipa`
  — the chain-current IPA of each (reflecting earlier rescorers' rewrites);
- `context.phrase_position` / `context.utterance_position` — the word's
  `Position` (`INITIAL` / `MEDIAL` / `FINAL` / `SOLE`) within its
  punctuation-bounded phrase and within the whole utterance, plus the
  `is_phrase_final`, `is_utterance_initial`, … convenience predicates.

**Bidirectional by construction.** Because `rescore` runs once per word, a
boundary process that must change *both* words is expressed by each word's
invocation rewriting its own side while reading the shared boundary — the
resyllabification and `waṣl`-elision the legacy left-only
[`SandhiEngine`](lattice.md#rescoring-the-lattice) cannot do (it could only
rewrite the *left* word of a pair).

## Phrase and utterance position

A **phrase** is a run of words bounded by pause punctuation (`.,;:!?…`) or the
utterance edges — the same boundary the tokenizer already marks as *pausal*.
`Position` is computed for both the phrase span and the whole-utterance span:
the first word of a span is `INITIAL`, the last is `FINAL`, interior words are
`MEDIAL`, and a one-word span is `SOLE` (both initial and final). `word.pausal`
is exactly `word.phrase_position.is_final()`.

## Worked example 1 — Arabic waṣl + pausal

Two toy rescorers (illustrations of the seam, **not** shipped language data)
prove the seam supplies the cross-word visibility and phrase position that
arbtok's private orchestration needs:

```python
class WaslElision(SentenceRescorer):        # right-word rewrite across a boundary
    def rescore(self, word, context):
        ipa = context.this_word_ipa
        if context.prev_word is not None and ipa.startswith("al"):
            return ipa[1:]                  # elide the article's initial vowel
        return ipa

class PausalForm(SentenceRescorer):         # driven by phrase position
    def rescore(self, word, context):
        ipa = context.this_word_ipa
        if context.is_phrase_final and ipa and not ipa.endswith("ʔ"):
            return ipa + "ʔ"                # pausal citation form
        return ipa

g = G2P("ar", sentence_rescorer=[WaslElision(), PausalForm()])
```

| word | default | with seam | why |
| --- | --- | --- | --- |
| `الكتاب` | `alktaːb` | `alktaːb` | utterance-initial — waṣl needs a preceding word |
| `الجديد` | `aldʒdjd` | `ldʒdjdʔ` | `al` elided across the boundary (**right** word), then pausal (phrase-final) |

The winner changes **across a boundary**, and on the *right* word — visibility
(`prev_word`) and phrase position (`is_phrase_final`) drove both edits.

## Worked example 2 — French liaison (resyllabification)

```python
class FrenchLiaison(SentenceRescorer):
    LATENT = {"s", "x", "z"}
    def rescore(self, word, context):
        ipa = context.this_word_ipa
        prev = context.prev_word
        if prev and prev.surface[-1:].lower() in self.LATENT and ipa[:1] in VOWELS:
            return "z" + ipa                # right word gains the /z/ onset
        nxt = context.next_word
        if word.surface[-1:].lower() in self.LATENT and nxt and \
                (context.next_word_ipa or "")[:1] in VOWELS:
            return ipa + "‿"               # left word marks the liaison tie
        return ipa

g = G2P("fr", sentence_rescorer=FrenchLiaison())
```

| input | default | with seam |
| --- | --- | --- |
| `les amis` | `lə ami` | `lə‿ zami` |

The latent final consonant of *les* resyllabifies as the onset of *amis* — the
**right** word gains `z`, the left word marks the tie. A left-only rewrite
cannot move a segment onto the next word; this seam can.

## How it composes with the word lattice

The sentence seam sits **above** the word [lattice](lattice.md): each
`WordSlot.slots` *is* the word's `ipa_lattice`, and a `SentenceRescorer` reads
those edge slots but rewrites at the word-IPA level. In `transcribe`, sentence
rescorers run **first** (whole-utterance visibility), then the spec's
declarative `sandhi_rules` run through the existing `SandhiEngine` exactly as
before — the two **coexist**. A *list* of sentence rescorers composes like
lattice rescorers: each pass sees the previous pass's rewrites, while within a
pass every word reads a stable pre-pass snapshot, so a pass is
order-independent and deterministic.

## Off by default, byte-identical when unused

Nothing here runs unless a caller passes `sentence_rescorer=` to `G2P` (or
calls `sentence_lattice` explicitly). With no sentence rescorer,
`transcribe` is byte-for-byte what it was — single-word scoring never touches
the seam, the benchmark scoreboard is unchanged, and a spec's `sandhi_rules`
keep working exactly as now. There is no new spec field: cross-word *rules* are
caller-supplied plugin objects, keeping the spec data surface unchanged.

## Refine, fork, or reach for this seam

The [refine-or-fork guidance](lattice.md#refine-the-lattice-or-fork-the-tokenizer)
still holds, with a third option between them. Word-internal phonology →
**refine** the word lattice with a `LatticeRescorer`. A genuinely non-local
process (cross-word sandhi, pausal / phrase-final forms, liaison) →
**this seam**, rather than forking a private orchestrator. Only a representation
the seam still cannot express (morphological structure, prosody, a non-IPA
intermediate) is a reason to **fork**. A downstream engine such as
[arbtok](https://github.com/TigreGotico/arbtok) retires its cross-word fork by
moving waṣl / pausal / assimilation onto `SentenceRescorer`s over the shared
`SentenceLattice`, keeping only its truly bespoke stages private.

## Still downstream: semantic / POS disambiguation (C5)

This seam supplies **position and cross-word adjacency, not meaning**.
Homograph disambiguation that needs part of speech or semantics — English
*read* /riːd/ vs /rɛd/, Portuguese *sede* 'thirst' vs 'headquarters' — is
**not** expressible here: the context carries no POS or sense field,
deliberately. That remains a downstream concern (Workstream C5). The honest
boundary is the same one [lattice.md](lattice.md#refine-the-lattice-or-fork-the-tokenizer)
draws: route a word that needs context it cannot see to the layer that has it,
never silently through a layer that does not.

---

**Navigation:** [Docs home](index.md) · [Getting started](getting_started.md) · [Architecture](architecture.md) · [Languages](languages/index.md) · [Scoreboard](scoreboard.md)

*Related: [Lattice](lattice.md) · [Architecture](architecture.md) · [Registry](registry.md) · [API stability](api_stability.md)*
