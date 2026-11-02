# The sentence-context seam

The [pronunciation lattice](lattice.md) is word-local by design. A `LatticeRescorer` sees one grapheme slot and its neighbours inside a word, and it never crosses a word boundary. That scope suits phonology inside the word. A whole class of processes lives between words, and the word lattice cannot express them:

| Process | What happens |
| --- | --- |
| Arabic waṣl | The *hamzat al-waṣl* of a word, such as the vowel of the definite article, elides after a preceding word |
| Arabic pausal forms | A phrase-final word is realised differently, with *tanwīn* suppression and *tāʾ marbūṭa* as [h] |
| French liaison | A latent word-final consonant becomes the onset of the next word before a vowel |
| Portuguese external /s/-sandhi | A word-final /s/ changes across the word boundary |

Each of these needs two things that the word lattice does not carry. It needs to see the edge of the adjacent word, that is its final or initial candidates. It also needs the position of the word in its phrase and in the utterance. The sentence-context seam is the shared cross-word surface that gives both, so a downstream engine does not need its own sentence orchestrator.

## The two objects

### `SentenceLattice`: the utterance, in order

`G2P.sentence_lattice(text, *, search="greedy", beam_width=8)` returns a `SentenceLattice`. It holds the utterance as an ordered tuple of `WordSlot` objects, one per word:

```python
from orthography2ipa import G2P

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

### `SentenceRescorer`: the boundary-aware rewrite seam

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

Return `context.this_word_ipa` for a no-op. A process can change both words at a boundary. Each word's call rewrites its own side while it reads the shared boundary. That is how resyllabification and waṣl elision on the right word work. The older `SandhiEngine` can rewrite only the left word of a pair.

## Phrase and utterance position

A phrase is a run of words between two pauses, or between a pause and an utterance edge. A pause is a mark from `orthography2ipa.phonetok.PAUSE_PUNCTUATION`, which names the pause marks of each script. For Latin text these are `. , ; : ! ? …`. The tokenizer uses the same boundary when it marks a word as pausal.

`Position` is computed for the phrase and for the whole utterance. The first word of a span is `INITIAL`, the last is `FINAL` and the words between are `MEDIAL`. A span of one word is `SOLE`, and `SOLE` counts as both initial and final for `is_initial()` and `is_final()`.

## Worked example 1: Arabic waṣl and pausal forms

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

The first word opens the utterance, so waṣl has no preceding word and does nothing. On the second word, the article's vowel elides across the boundary, and the pausal form then applies because the word ends the phrase. The change happens across a boundary and on the right word. The adjacent word (`prev_word`), the edge slot (`initial_slot`) and the phrase position (`is_phrase_final`) drove both edits.

## Worked example 2: French liaison

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

## How it composes with the word lattice

The sentence seam sits above the word [lattice](lattice.md). Each `WordSlot.slots` is the word's `ipa_lattice`. A `SentenceRescorer` reads the edge slots and rewrites at the level of the word's IPA.

In `transcribe`, the sentence rescorers run first, with a view of the whole utterance. The spec's declarative `sandhi_rules` then run through `SandhiEngine`, and the two coexist. A list of sentence rescorers composes like lattice rescorers: each pass sees the rewrites of the pass before it. Inside one pass, every word reads the same snapshot taken before the pass, so the order of the words does not change the result.

The engine passes `SandhiEngine.apply` the pause flag of each word, so a declarative rule stays inside its prosodic domain. No rule joins two words that a pause separates (Nespor & Vogel 1986, *Prosodic Phonology*). The blocked boundary is the intonational phrase, which is what punctuation writes. Some rules have the smaller phonological phrase as their real domain. Such a rule still applies at a phonological-phrase edge inside a clause, so the pause flags give a lower bound only. A sentence rescorer sees the same positions through `WordSlot.phrase_position`.

## Off by default

Nothing in this seam runs unless a caller passes `sentence_rescorer=` to `G2P`, or calls `sentence_lattice`. Without a sentence rescorer, `transcribe` does not use the seam, and the scoring of single words and the benchmark board do not change. A spec's `sandhi_rules` work the same either way. The seam adds no spec field: cross-word rules are plugin objects that the caller supplies, so the spec data surface stays the same.

## Refine, fork, or use this seam

The [refine-or-fork guidance](lattice.md#refine-the-lattice-or-fork-the-tokenizer) still applies, with a third option between the two. For phonology inside the word, refine the word lattice with a `LatticeRescorer`. For a non-local process, such as cross-word sandhi, pausal forms or liaison, use this seam instead of a private orchestrator. Fork only for a representation that the seam cannot express. Examples are morphological structure, prosody or an intermediate form that is not IPA. A downstream engine such as [arbtok](https://github.com/TigreGotico/arbtok) can move waṣl, pausal forms and assimilation onto `SentenceRescorer` classes over the shared `SentenceLattice`. It then keeps private only the stages that are truly its own.

## Still downstream: semantic and part-of-speech disambiguation

This seam gives position and cross-word adjacency, not meaning. It cannot express a homograph choice that needs part of speech or sense. Examples are English *read* /riːd/ against /rɛd/, and Portuguese *sede* 'thirst' against 'headquarters'. The context carries no part-of-speech or sense field, on purpose, and that choice stays with a downstream engine. The boundary is the same one that [lattice.md](lattice.md#refine-the-lattice-or-fork-the-tokenizer) draws. Send a word that needs context to the layer that has that context, never silently through a layer that does not.

---
[← The pronunciation lattice](lattice.md) · [Home](index.md) · [Lattice PER →](lattice_per.md)
