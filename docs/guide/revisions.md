# Revisions and pinning

<!-- agent-hint
covers: which revision names the phonemizer of a trained voice, what moves each revision, and how to compare them
source: orthography2ipa/revision.py:spec_revision, orthography2ipa/revision.py:lexicon_revision, orthography2ipa/revision.py:ENGINE_MODULES, orthography2ipa/ir/layout.py:spec_revision, orthography2ipa/ir/layout.py:SEMANTICS
generated: no
verify: .venv/bin/python -m doctest docs/guide/revisions.md
see: docs/guide/loom_export.md, docs/reference/api_stability.md, docs/guide/lexicon.md, docs/ir/o2i-ir-v1.md
-->

A voice learns the phonemes of one phonemizer. This page says which value names that phonemizer, what changes the value, and how to check it later.

## Three revisions

Each revision is a `"sha256:"` string. Each one covers a different part of the phonemizer:

| Revision | Function | Covers |
| :--- | :--- | :--- |
| Package spec revision | `orthography2ipa.spec_revision(code)` | The spec of `code`, every spec on its inheritance chains, the source of the rules-path modules and the Unicode version of the running Python |
| IR revision | `orthography2ipa.ir.layout.spec_revision(ir)` | The compiled IR document and the version of each primitive it uses. The loom exporter records this value |
| Lexicon revision | `orthography2ipa.lexicon_revision(code, patches=False)` | The files of the packaged lexicon |

## Step 1: read the package revisions

An alias and its canonical code give one revision:

```python
>>> from orthography2ipa import spec_revision
>>> spec_revision("pt-PT").startswith("sha256:")
True
>>> spec_revision("pt") == spec_revision("pt-PT")
True

```

The default `transcribe(text, code)` also reads the packaged lexicon, when a package supplies one. With no such package, `lexicon_revision` raises `LookupError`:

```python
>>> from orthography2ipa import lexicon_revision
>>> try:
...     lexicon_revision("pt-PT")
... except LookupError as err:
...     print(err)  # doctest: +ELLIPSIS
no installed package supplies a lexicon file for 'pt-PT'; installed: ...

```

A voice trained on the default path records both values. A voice trained with `Pipeline(lexicon={})` reads no lexicon, and the spec revision alone covers it.

## Step 2: read the IR revision

The IR revision is the value that a loom export records. Compile the IR and hash it:

```python
>>> from orthography2ipa.ir.compiler import build_ir
>>> from orthography2ipa.ir.layout import spec_revision as ir_revision
>>> ir_revision(build_ir("pt-PT")).startswith("sha256:")
True

```

The hash input is the canonical IR and a manifest. The manifest lists each primitive, predicate node and syllable relation that the IR uses, with its semantics version from `layout.SEMANTICS`. So a fix to one primitive moves the revision of each language whose IR uses it, and leaves the other languages as they were.

## What moves the IR revision

Every input that can change the output is in the hash. A compile option changes the IR, so it changes the revision:

```python
>>> from orthography2ipa.ir.compiler import build_ir
>>> from orthography2ipa.ir.layout import spec_revision as ir_revision
>>> plain = ir_revision(build_ir("pt-PT"))
>>> plain == ir_revision(build_ir("pt-PT", apply_stress=False))
False
>>> plain == ir_revision(build_ir("pt-PT", dialect_profile="beira_alta"))
False

```

Older spec data gives another IR, and so another revision:

```python
>>> from orthography2ipa.ir.compiler import build_ir
>>> from orthography2ipa.ir.layout import spec_revision as ir_revision
>>> old = build_ir("kab", "7.30.0")
>>> old["source"]["data_ref"]
'7.30.0'
>>> ir_revision(old) == ir_revision(build_ir("kab"))
False

```

The table lists what moves each revision:

| Change | Package spec revision | IR revision |
| :--- | :--- | :--- |
| An edit to the spec, or to a spec on its chains, that changes its parsed JSON | moves | moves when the compiled IR changes |
| A whitespace-only edit to a spec | stays | stays |
| A compile option: `apply_stress`, `apply_allophony`, `apply_sandhi`, `expand_allophones`, `dialect_profile` | stays | moves |
| A higher semantics version of a primitive that the IR uses | stays | moves |
| A compiler change that writes an equivalent IR in another form | stays | can move |
| A change to a rules-path module in `ENGINE_MODULES` | moves | stays, unless the IR changes |
| A change to `orthography2ipa/ir/interpreter.py` with no semantics version bump | stays | stays |
| Another Unicode version in Python | moves | moves when the compiled character tables change |
| A lexicon | stays | stays |

The IR revision is conservative. It can move when the output does not change. It does not stay equal when the output can change, provided each primitive fix bumps its semantics version ([behaviour_is_data.md](../contributing/behaviour_is_data.md#change-a-version-change-the-spec)).

`ENGINE_MODULES` lists the modules of the rules path. It does not list the modules of `orthography2ipa/ir/`.

## Step 3: compare later

Keep the revisions with the voice. Before you run the voice on another install, compute the same revisions there and compare:

- On the Python path, compare `spec_revision(code)`, and `lexicon_revision(code)` when the voice read a lexicon.
- On loom, read `o2i.spec_revisions` from the GGUF ([loom_export.md](loom_export.md#step-2-check-what-the-file-holds)). The value travels with the file, so the phonemizer cannot drift from it.

When a value differs, the phonemes can differ. Compile the spec data of the training run with `--rev`, or with `build_ir(code, data_ref)`, to get the old rules back.

---
[← Export a phonemizer to loom](loom_export.md) · [Home](../index.md) · [Distance Metrics →](distance.md)
