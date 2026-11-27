# Export a phonemizer to loom

<!-- agent-hint
covers: how to write the phonemizer of a voice into one loom GGUF, pin it to the spec data of a release, check its revisions and run it
source: orthography2ipa/export_to_loom.py, orthography2ipa/ir/interpreter.lua, orthography2ipa/ir/compiler.py:_data_at, orthography2ipa/ir/layout.py:spec_revision
generated: no
verify: .venv/bin/python -m doctest docs/guide/loom_export.md
see: docs/guide/revisions.md, docs/engine/ir.md, docs/engine/plugins.md
-->

This page writes the phonemizer of a voice into one GGUF file for [loom.cpp](https://github.com/loom-ai-org/loom.cpp). The file holds the Lua interpreter and the compiled IR of each language you name, and nothing else.

## Before you start

The exporter needs the `loom` extra, which installs `gguf`:

```bash
uv pip install --python .venv --prerelease=allow -e '.[loom]'
```

To compile older spec data with `--rev`, run the exporter from a git checkout of the repository. The exporter reads the old spec files with `git show`.

## Step 1: export the languages of the voice

Name every language that the voice speaks with `--langs`. The order sets the language index that loom uses:

```bash
.venv/bin/python -I -m orthography2ipa.export_to_loom --langs pt-PT,kab --out voice.gguf
```

The command prints the path it wrote:

```text
voice.gguf
```

The file is about 370 KB for these two languages. The compiler has already resolved inheritance, so the IR of a language holds everything that the language needs.

## Step 2: check what the file holds

The GGUF records the package version, the languages, the revision of each IR and the phonemizer identity of each language. This script reads them:

```python
import sys
from gguf import GGUFReader

reader = GGUFReader(sys.argv[1])
for key in ("loom.task", "loom.phonemizer.ruleset", "loom.text.languages", "o2i.version", "o2i.spec_revisions"):
    print(key, "=", reader.fields[key].contents())
```

Its output for `voice.gguf`:

```text
loom.task = text2phonemes
loom.phonemizer.ruleset = orthography2ipa 7.124.49a1; pt-PT=sha256:3cc0986e71aa4de4166e748163949a0ff9d415b23b981a2861e5f245b2ca88ce; kab=sha256:b9222eb6085eeb68fffa3a433016a3122253cf3157290e1008939ce76341f110
loom.text.languages = ['pt-PT', 'kab']
o2i.version = 7.124.49a1
o2i.spec_revisions = ['sha256:3cc0986e71aa4de4166e748163949a0ff9d415b23b981a2861e5f245b2ca88ce', 'sha256:b9222eb6085eeb68fffa3a433016a3122253cf3157290e1008939ce76341f110']
```

The key `o2i.phonemizer_identity` holds a JSON object with one identity per language. Each identity has the keys of the `PhonemizerIdentity` of scriptconv, which a phoonnx voice records as `phonemizer_identity`: `backend`, `distribution`, `version`, `lang`, `revision` and `frontend`. Its `revision` is the IR revision.

For each language, the key `o2i.phonemes.<code>` holds the phoneme set of its IR as an array of strings: every segment that the language can emit, equal to `orthography2ipa.phoneme_set(code)`. The segments are NFD and hold no stress marks or syllable dots. A voice reads the key at load time and checks that its symbol table holds each segment. A language with an empty set, such as a stub, has no key. The set is exact for well-formed words with the default options: no dialect profile, no lexicon and no host hooks.

The set holds no stress marks (ˈ ˌ), syllable dots or tie bars. A voice adds ˈ and ˌ to its symbol table itself. A tied segment such as `t͡ʃ` is one entry of the set, so a voice that reads one code point per symbol splits each segment into its code points. Any language code that `orthography2ipa.registry.resolve` accepts works, lect codes included.

Record `o2i.spec_revisions` with the voice. [revisions.md](revisions.md) says what moves a revision, and how to compare two of them.

A plugin that ships a word table gives it to the export with `--fragment PATH`. Repeat the flag for more than one file. A fragment is a JSON file `{"ir_version": 1, "words": {"word": "ipa"}}`. The export merges the word tables into every language, and a later file wins on a duplicate word. The key `o2i.fragments` lists the sha256 of each fragment, and the revision of each language covers the words.

A fragment may also carry `sandhi`, a list of rules between words, and `unsupported`, a list of the names of the plugin's rules that a fragment cannot express. A sandhi rule has the keys `left`, `right`, `left_out` and `right_out` of a spec sandhi rule, and may add `left_spelling` and `right_spelling`, patterns on the written word, or `"pause": true` for a rule on a word at a pause. The export adds the rules after the rules of each spec. The key `o2i.unsupported` lists the names from `unsupported`: the loom file does not run those rules, so the plugin keeps them as a host hook.

## Step 3: pin the spec data of the training run

A voice learns the phonemes of the spec data it was trained with. A later change to a spec changes the phonemes, and the voice then hears input it never saw. `--rev` compiles the spec data of a git tag or commit with the current compiler, so the file keeps the rules of the training run.

The Kabyle voices were trained on release 7.30.0. Export Kabyle at that tag:

```bash
.venv/bin/python -I -m orthography2ipa.export_to_loom --langs kab --rev 7.30.0 --out kab-7.30.0.gguf
```

The ruleset string records the data ref:

```text
loom.phonemizer.ruleset = orthography2ipa 7.124.49a1 data_ref=7.30.0; kab=sha256:72b3dce7aaef00b490b3ddd416f407c67cfa84f91d3d774cb9d705d3a71bba9a
```

Between 7.30.0 and the current data, the Kabyle spec changed the reading of ⟨ɣ⟩ from `ɣ` to `ʁ`. The two files show it on the same sentence:

```text
kab-7.30.0.gguf   Iwacu i ɣ-tugiḍ ad nruḥ?   ->   iwæʃu i ɣ θuʝiðˤ æð nruħ
voice.gguf        Iwacu i ɣ-tugiḍ ad nruḥ?   ->   iwæʃu i ʁ θuʝiðˤ æð nruħ
```

`--rev` replaces the spec data only. The compiler and the interpreter stay current. When only the spec data changed after the ref, the output equals the output of that release. An engine fix after the ref can still change it ([section 8.2 of the IR spec](../ir/o2i-ir-v1.md#82-compiling-older-spec-data)).

## Step 4: run it in loom

loom passes only numbers between the host and the Lua driver. The driver defines two functions:

| Function | Input | Output |
| :--- | :--- | :--- |
| `infer` | `text`: the text as an array of codepoints. `lang`: the 0-based index into `loom.text.languages` | The IPA as an array of codepoints |
| `info` | `lang` | The recorded revision of that language, as an array of byte values |

A host calls `infer` through the session bridge of loom:

```cpp
std::unordered_map<std::string, loom::LoomLuaBridge::Value> inputs;
inputs["text"] = utf8_to_codepoints(line);
inputs["lang"] = 0.0;
const auto result = session.bridge().call("infer", inputs);
```

A small host that reads one line per text and prints the IPA gives this for `voice.gguf`, language 0 (`pt-PT`):

```text
$ printf 'pedra\nos jogos\n' | o2i_loom voice.gguf 0
ˈpɛdɾɐ
u ˈʒɔɡuʃ
```

The same text through the Python package gives the same IPA:

```python
>>> import orthography2ipa
>>> orthography2ipa.transcribe("pedra", "pt-PT"), orthography2ipa.transcribe("os jogos", "pt-PT")
('ˈpɛdɾɐ', 'u ˈʒɔɡuʃ')

```

## Run the Lua interpreter without loom

`interpreter.lua` also runs under plain LuaJIT. It reads an IR JSON file, then one line of decimal codepoints per text on standard input:

```bash
.venv/bin/python -I -c "
import json
from orthography2ipa.ir.compiler import compile_spec
json.dump(compile_spec('pt-PT'), open('pt-PT.ir.json', 'w'), ensure_ascii=False)"
echo '112 101 100 114 97' | luajit orthography2ipa/ir/interpreter.lua pt-PT.ir.json
```

It prints the codepoints of the IPA, and the CPU time on standard error:

```text
lua: 1 texts in 0.003 s cpu
712 112 603 100 638 592
```

The codepoints `712 112 603 100 638 592` spell `ˈpɛdɾɐ`.

## Check an export from Python

`export_to_loom` writes the GGUF and returns the metadata that it wrote. With `expect_revisions`, it refuses to write a file when the revision of a language differs from the one you expect. `expect_revisions` takes the values of `o2i.spec_revisions`, which equal `orthography2ipa.spec_revision(code)` ([revisions.md](revisions.md)):

```python
>>> import tempfile
>>> from pathlib import Path
>>> from gguf import GGUFReader
>>> from orthography2ipa.export_to_loom import export_to_loom
>>> out = Path(tempfile.mkdtemp()) / "voice.gguf"
>>> meta = export_to_loom(["pt-PT", "kab"], out)
>>> sorted(meta)
['fragments', 'o2i_version', 'phonemes', 'phonemizer_identity', 'ruleset', 'spec_revisions', 'unsupported']
>>> GGUFReader(str(out)).fields["o2i.spec_revisions"].contents() == list(meta["spec_revisions"].values())
True
>>> export_to_loom(["kab"], out, expect_revisions={"kab": "sha256:0"})  # doctest: +ELLIPSIS
Traceback (most recent call last):
...
ValueError: kab: expected revision sha256:0, the data gives sha256:...

```

An installed package that is not a git checkout exports its own spec data only. It refuses `data_ref`.

## What the file leaves out

The file holds no lexicon and no Python extension. A voice trained with a lexicon or a rescorer gets other phonemes in loom ([plugins.md](../engine/plugins.md)).

---
[← Lexicons and forced pronunciations](lexicon.md) · [Home](../index.md) · [Revisions and pinning →](revisions.md)
