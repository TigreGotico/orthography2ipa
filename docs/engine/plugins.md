# Host-side plugins

<!-- agent-hint
covers: which extensions run in the Python host around the IR interpreter, the hook each one uses, how a cost crosses the hook, and why none of them goes into a loom export
source: orthography2ipa/ir/interpreter.py:Hooks, orthography2ipa/g2p.py:G2P._interpreter, orthography2ipa/g2p.py:G2P._transcribe_ir, orthography2ipa/ir/compiler.py:build_ir, orthography2ipa/pipeline.py, orthography2ipa/plugins.py
generated: no
verify: .venv/bin/python -m doctest docs/engine/plugins.md
see: docs/engine/ir.md, docs/engine/architecture.md, docs/guide/lexicon.md, docs/guide/loom_export.md
-->

This page lists the extensions that run in the Python host and not in the IR. Each one runs around the interpreter at a fixed hook, so the engine stays on the IR. None of them goes into a loom export.

## A lexicon runs around the interpreter

A lexicon replaces the rules for the words it holds. The host passes it to the interpreter, which checks each word against it before the rules run:

```python
>>> from orthography2ipa import G2P, Pipeline
>>> plain = G2P("pt-PT")
>>> plain.transcribe("pedra dura")
'ˈpɛdɾɐ ˈduɾɐ'
>>> with_lexicon = G2P("pt-PT", pipeline=Pipeline(lexicon={"pedra": "ˈpedɾɐ"}))
>>> with_lexicon.transcribe("pedra dura")
'ˈpedɾɐ ˈduɾɐ'

```

The private attribute `_interpreter` holds the interpreter of the engine. A lexicon does not change it:

```python
>>> from orthography2ipa import G2P, Pipeline
>>> G2P("pt-PT")._interpreter is not None
True
>>> G2P("pt-PT", pipeline=Pipeline(lexicon={"pedra": "ˈpedɾɐ"}))._interpreter is not None
True

```

`Pipeline.expand` and `Pipeline.mark` also run in the host. They prepare the text, and the interpreter receives the result.

## The hooks of the interpreter

The interpreter has four fixed hooks, the fields of `orthography2ipa.ir.interpreter.Hooks`. The engine fills them from its pipeline, its plugins and its arguments. A hook is a host callback: the IR document is the same with hooks or without them.

| Hook | When it runs | What fills it |
| :--- | :--- | :--- |
| `text(run) -> run` | on each plain run of the input, before the interpreter prepares it | the normalize plugins, then the deprecated `normalizer` |
| `rescore(word, tokens, slots, syllables, stressed) -> slots` | on the beam slots of each word, before the allophony pass of the IR | `Pipeline(rescore=...)` and the rescore plugins |
| `syllables(word) -> syllables or None` | in place of the written syllable division of the IR | `Pipeline(syllabifier=...)` |
| `sandhi(words, surfaces, pausal) -> words` | after the sandhi of the IR, before the dialect program and NFC | the sentence rescorers, then `Pipeline(sandhi=...)` or the sandhi plugins |

The sentence stage runs in this order: the words, the IR sandhi, the `sandhi` hook, the dialect program, NFC.

A rescorer works on floats and the IR works on integer micro-units. A cost crosses the hook as `cost / 1_000_000` into the rescorer and `round(cost * 1_000_000)` back, which is the rule the compiler uses for the IR costs. Two costs that differ by less than half a micro-unit are equal after the crossing.

A syllabifier that fails on a word, or that returns syllables that do not spell the word, gives the word back to the IR division.

This rescorer reads every ⟨t⟩ as [θ], and the engine stays on the IR:

```python
>>> from orthography2ipa import G2P, Pipeline
>>> from orthography2ipa.phonetok import Candidate
>>> from orthography2ipa.rescorer import LatticeRescorer
>>> class Theta(LatticeRescorer):
...     def rescore(self, slot, context):
...         if slot.grapheme == "t":
...             return [Candidate("θ", 0.0)]
...         return slot.candidates
>>> engine = G2P("pt-PT", pipeline=Pipeline(rescore=[Theta()]))
>>> engine._interpreter is not None
True
>>> engine.transcribe("pedra dura gata")
'ˈpɛdɾɐ ˈduɾɐ ˈɡaθɐ'

```

### What a hook may change

Each hook gets values and returns values. It never gets the interpreter, the IR document or a cache, so it cannot change them.

| Hook | It may change | It must keep | What the interpreter does with a bad result |
| :--- | :--- | :--- | :--- |
| `text` | the characters of the run | one string for one run | no check |
| `rescore` | the candidates and costs of each slot, or empty a slot to delete its grapheme | one slot per token, in token order | no check |
| `syllables` | where the word splits | syllables that spell the word | an empty result falls back to the IR division |
| `sandhi` | the IPA of each word | one string per word, in word order | a wrong word count raises `ValueError` |

The interpreter may call a hook more than once for the same text, and it caches some results. The `rescore` hook also runs on the parts of a word with a clitic. The `syllables` hook runs once per distinct word, and the interpreter keeps the list it returns. A hook must therefore return the same result for the same input, keep no state between calls, and never change a list after it returns it.

## Forced words, caller specs and the board option

A `<phoneme ph="...">` word goes to the interpreter as a word with its reading already set, as a lexicon hit does. The interpreter does not stress it. The text hook and `Pipeline.expand` never see it.

The `spec` argument of `G2P` is compiled with `build_ir(code, spec=...)` for that engine alone. Its IR does not go into the disk cache, so the first transcription pays the compile time each time.

`expose_ambiguous_endings=False` is a compile option. The compiler drops the lower-ranked readings of each list-valued `grammatical_endings` entry, so they never reach the beam.

## Every host-side extension

| Extension | How a caller supplies it | Hook |
| :--- | :--- | :--- |
| Lexicon | `Pipeline(lexicon=...)`, or the packaged lexicon of the `orthography2ipa.lexicons` entry points and the patches of `orthography2ipa.lexicon_patches` | interpreter argument |
| Text preparation | `Pipeline(expand=..., mark=...)` | before the interpreter |
| Normalize plugin | a plugin of the `orthography2ipa.normalize` entry points, named by the spec or the caller, and the `normalizer` argument | `text` |
| Rescorer | `Pipeline(rescore=...)`, a plugin of the `orthography2ipa.rescore` entry points | `rescore` |
| Syllabifier | `Pipeline(syllabifier=...)` | `syllables` |
| Sandhi | `Pipeline(sandhi=...)`, a plugin of the `orthography2ipa.sandhi` entry points | `sandhi` |
| Sentence rescorer | the `sentence_rescorer` argument | `sandhi` |
| Forced pronunciation | `<phoneme ph="...">` markup in the text | interpreter argument |
| Caller spec | the `spec` argument of `G2P` | compile option |
| Board option | `expose_ambiguous_endings=False` | compile option |
| Stress | a plugin of the `orthography2ipa.stress` entry points, through `stress.source = "plugin"` | none: the compiler refuses the spec, and `G2P` raises `IRUnsupportedFeature` |

The entry-point groups other than the two lexicon groups are deprecated. [architecture.md](architecture.md#pluggable-steps) gives the contract of each step.

## What an export leaves out

`export_to_loom` writes the IR of each language and the Lua interpreter. It writes no Python, so no extension of the table above goes into the GGUF. The Lua interpreter has no host hooks, and loom carries no lexicon.

A voice that was trained with a host-side extension therefore gets other phonemes in loom. Train a voice for loom with `G2P(lang, pipeline=Pipeline(lexicon={}))`, so that it reads no lexicon and runs on the IR alone. [loom_export.md](../guide/loom_export.md) gives the export steps, and [revisions.md](../guide/revisions.md) says which revision to record.

---
[← Compiler, IR and interpreters](ir.md) · [Home](../index.md) · [Tokenizer →](tokenizer.md)
