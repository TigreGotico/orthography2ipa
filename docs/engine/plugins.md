# Host-side plugins

<!-- agent-hint
covers: which extensions run in the Python host outside the IR, and why none of them goes into a loom export
source: orthography2ipa/pipeline.py, orthography2ipa/plugins.py, orthography2ipa/lexicon.py, orthography2ipa/export_to_loom.py
generated: no
see: docs/engine/ir.md, docs/engine/architecture.md, docs/guide/lexicon.md, docs/guide/loom_export.md
-->

This page lists the extensions that run in the Python host and not in the IR. The IR holds only data, so it cannot hold Python code. None of these extensions goes into a loom export.

## Every host-side extension

| Extension | How a caller supplies it |
| :--- | :--- |
| Lexicon | `Pipeline(lexicon=...)`, or the packaged lexicon of the `orthography2ipa.lexicons` entry points and the patches of `orthography2ipa.lexicon_patches` |
| Text preparation | `Pipeline(expand=..., mark=...)`, the `normalizer` argument |
| Normalize plugin | a normalize plugin of the `orthography2ipa.normalize` entry points, named by the spec or the caller |
| Rescorer | `Pipeline(rescore=...)`, a rescore plugin of the `orthography2ipa.rescore` entry points |
| Syllabifier | `Pipeline(syllabifier=...)` |
| Sandhi | `Pipeline(sandhi=...)`, a sandhi plugin of the `orthography2ipa.sandhi` entry points |
| Stress | a stress plugin of the `orthography2ipa.stress` entry points, through `stress.source = "plugin"`. The compiler refuses such a spec |
| Sentence rescorer | the `sentence_rescorer` argument |
| Forced pronunciation | `<phoneme ph="...">` markup in the text |

The entry-point groups other than the two lexicon groups are deprecated. [architecture.md](architecture.md#pluggable-steps) gives the contract of each step.

## What an export leaves out

`export_to_loom` writes the IR of each language and the Lua interpreter. It writes no Python, so no extension of the table above goes into the GGUF. The Lua interpreter has no host hooks, and loom carries no lexicon.

A voice that was trained with a host-side extension therefore gets other phonemes in loom. Train a voice for loom with `G2P(lang, pipeline=Pipeline(lexicon={}))`, so that it reads no lexicon. [loom_export.md](../guide/loom_export.md) gives the export steps, and [revisions.md](../guide/revisions.md) says which revision to record.

---
[← Compiler, IR and interpreters](ir.md) · [Home](../index.md) · [Tokenizer →](tokenizer.md)
