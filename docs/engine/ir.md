# Compiler, IR and interpreters

<!-- agent-hint
covers: how the compiler, the versioned IR and the interpreters work, and what each stage does to one word
source: orthography2ipa/ir/compiler.py, orthography2ipa/ir/interpreter.py, orthography2ipa/ir/interpreter.lua, orthography2ipa/ir/layout.py
generated: no
verify: .venv/bin/python -m doctest docs/engine/ir.md
see: docs/ir/o2i-ir-v1.md, docs/guide/loom_export.md, docs/guide/revisions.md, docs/contributing/behaviour_is_data.md
-->

This page explains how the IR runs a spec. It follows the Portuguese word ⟨pedra⟩ through each stage and shows the real data at each step. The format of the IR is in [o2i-ir-v1.md](../ir/o2i-ir-v1.md).

## One word, stage by stage

Start with the result. `transcribe` gives the IPA of ⟨pedra⟩ in European Portuguese, and the IR gives the same string:

```python
>>> import orthography2ipa
>>> orthography2ipa.transcribe("pedra", "pt-PT")
'ˈpɛdɾɐ'

```

Two programs make that string. The compiler reads the `pt-PT` spec and writes the IR, a JSON document. The interpreter reads the IR and the text, and writes the IPA. The steps below run both by hand.

### Step 1: compile the spec

`compile_spec` resolves the spec, follows its inheritance chain and writes the canonical IR document:

```python
>>> from orthography2ipa.ir.compiler import compile_spec
>>> doc = compile_spec("pt-PT")
>>> doc["ir_version"], doc["lang"]
(1, 'pt-PT')
>>> sorted(doc)
['allophony', 'atoms', 'beam', 'bits', 'char_maps', 'chars', 'debug', 'entries', 'fallback', 'ir_version', 'lang', 'primitives', 'rewrites', 'sandhi', 'source', 'stress', 'strings', 'syllable', 'word']

```

The document holds only integers, arrays and objects. Every string is an index into the `strings` table. `layout.decode` turns the indexes back into text, so a person can read the tables:

```python
>>> from orthography2ipa.ir import layout
>>> ir = layout.decode(doc)
>>> for e in ir["entries"]:
...     if e["key"] in ("p", "e", "d", "r", "a"):
...         print(e["key"], e["cands"], e["costs"])
a ['a', 'ɐ'] [0, 1000000]
d ['d'] [0]
e ['e', 'ɨ', 'ɛ'] [0, 1000000, 2000000]
p ['p'] [0]
r ['ɾ', 'ʁ'] [0, 1000000]

```

Each entry is one grapheme with its candidate readings. The costs are integers: one candidate step costs 1,000,000. Integer costs give the same sums in Python and in Lua.

### Step 2: tokenize

The interpreter cuts the word into graphemes by the longest match in a trie of the entry keys. Each grapheme carries its readings:

```python
>>> from orthography2ipa.ir.compiler import compile_spec
>>> from orthography2ipa.ir.interpreter import Interpreter
>>> it = Interpreter(compile_spec("pt-PT"))
>>> [(t.grapheme, t.readings) for t in it.grapheme_tokens("pedra")]
[('p', ('p',)), ('e', ('e', 'ɨ', 'ɛ')), ('d', ('d',)), ('r', ('ɾ', 'ʁ')), ('a', ('a', 'ɐ'))]

```

### Step 3: syllables and stress

The splitter divides the written word with the onset tables of the IR. The stress decision list then picks a syllable. Index 0 is the first syllable:

```python
>>> syllables = it.syllables("pedra")
>>> syllables, it.detect_stress("pedra", syllables)
(['pe', 'dra'], 0)

```

⟨pedra⟩ ends in a vowel, so the decision list stresses the penultimate syllable.

### Step 4: positional rules

An entry holds positional rules. Each rule is a predicate and a replacement candidate list. The third rule of ⟨e⟩ reads: when this vowel is in the stressed syllable, read `ɛ`, then `e`.

```python
>>> import json
>>> from orthography2ipa.ir.compiler import build_ir
>>> e = next(e for e in build_ir("pt-PT")["entries"] if e["key"] == "e")
>>> print(json.dumps(e["positional"][2], ensure_ascii=False))
[["and", ["or", ["ebit", 0, 0], ["ebit", 0, 21]], ["and", ["syll", "has_stress"]], ["syll", "idx_eq_stressed"]], ["ɛ", "e"]]

```

The predicate names no language. `ebit 0 0` tests bit 0 of the entry at offset 0, and the `bits` table of the IR names that bit `vowel`. The compiler wrote the rule from the spec, and the interpreter only evaluates it.

### Step 5: allophony and the beam

The allophone rules re-cost the candidates of each slot. They change nothing in ⟨pedra⟩. The beam then sums the costs and keeps the cheapest paths:

```python
>>> result = it.transcribe_word("pedra", 3)
>>> for segments, cost in result.paths:
...     print("".join(segments), cost)
pɛdɾɐ 0
pɛdɾa 1000000
pɛdʁɐ 1000000

```

### Step 6: finish the word

The best path gets the stress mark before the stressed syllable:

```python
>>> result.ipa
'ˈpɛdɾɐ'

```

A sentence adds three more steps: compound stress, the sandhi rules between words, and NFC by table. [Section 3.1 of the IR spec](../ir/o2i-ir-v1.md#31-stage-order-and-host-hooks) lists every stage in order.

## Why a compiler and an IR

The spec format is rich. It has inheritance, named contexts, classes of sounds and fields that refer to other fields. An engine that reads the spec at runtime must know all of that, and so must every port of it. The compiler does that work once, in Python. It writes a document in which nothing is implied: character tables with flag bits, a trie with integer costs, predicates over explicit sets, onset tables, an ordered stress decision list, a small regular-expression subset for rewrites, and exception lists.

The interpreter is then small and fixed. It knows a closed set of primitives and no language, script or sound class. A second interpreter is a port of those primitives only, not of the spec format. Two interpreters exist:

| Interpreter | Runs in | Role |
| :--- | :--- | :--- |
| `orthography2ipa/ir/interpreter.py` | Python | The reference. Every other interpreter matches it byte for byte |
| `orthography2ipa/ir/interpreter.lua` | LuaJIT inside [loom.cpp](https://github.com/loom-ai-org/loom.cpp) | The export target ([loom_export.md](../guide/loom_export.md)) |

Each version of the IR and each primitive has a version number. An interpreter refuses an IR that needs a version it does not have. The revision of an IR is a hash over the document and the primitive versions it uses, so it moves when the output can move ([revisions.md](../guide/revisions.md)).

## What lives where

| Place | Holds |
| :--- | :--- |
| `orthography2ipa/data/*.json` | The specs: all language behaviour |
| `orthography2ipa/ir/compiler.py` | Spec to IR. The only IR code that may hold a table of language facts |
| `orthography2ipa/ir/layout.py` | The IR schema, the primitive versions (`SEMANTICS`), the encoding and `spec_revision` of an IR |
| `orthography2ipa/ir/interpreter.py`, `pattern.py`, `dialect.py` | The reference interpreter and its regex subset and dialect primitives |
| `orthography2ipa/ir/interpreter.lua` | The Lua interpreter |
| `orthography2ipa/export_to_loom.py` | Writes the Lua interpreter and the IRs into one GGUF |
| `orthography2ipa/g2p.py` | `G2P`: the host steps around the interpreter |

## The IR and `transcribe`

Every method of `G2P`, and so `transcribe`, runs the IR on the Python interpreter. A loom export runs the same IR on the Lua interpreter. The text preparation steps and a lexicon are host steps around the interpreter ([plugins.md](plugins.md)).

---
[← Architecture](architecture.md) · [Home](../index.md) · [Host-side plugins →](plugins.md)
