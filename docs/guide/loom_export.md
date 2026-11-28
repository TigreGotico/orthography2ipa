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

The GGUF is a loom phonemizer of kind `lua`. It records the languages, the revision of each IR, the phonemizer identity of each language, the IR of each language and the script that runs them. This script reads the main keys:

```python
import sys
from gguf import GGUFReader

reader = GGUFReader(sys.argv[1])
for key in ("loom.task", "loom.phonemizer.kind", "loom.phonemizer.ruleset", "loom.text.languages"):
    print(key, "=", reader.fields[key].contents())
```

Its output for `voice.gguf`:

```text
loom.task = text2phonemes
loom.phonemizer.kind = lua
loom.phonemizer.ruleset = orthography2ipa 7.136.3a3; pt-PT=sha256:2e15325db2cc166ad7ce1fea4819858f89ca4af97761a9c4283a6dc645f2e033; kab=sha256:95d07b558acd360ba50ce8670d4affafd5916f54557fe071f9f25fbf41855001
loom.text.languages = ['pt-PT', 'kab']
```

| Key | Value |
| :--- | :--- |
| `loom.phonemizer.ruleset` | The package version, the data ref, and the IR revision of each language |
| `loom.phonemizer.script` | The Lua interpreter and its entry points (Step 4) |
| `loom.phonemizer.data.<code>` | The IR of the language, as JSON |
| `loom.phonemizer.phonemes.<code>` | The phoneme set of the language |
| `loom.phonemizer.identity` | One phonemizer identity for each language, as JSON |
| `loom.phonemizer.unsupported` | The fragment rules that the file does not run |

Each identity has the keys of the `PhonemizerIdentity` of scriptconv, which a phoonnx voice records as `phonemizer_identity`: `backend`, `distribution`, `version`, `lang`, `revision` and `frontend`. Its `revision` is the IR revision.

For each language, the key `loom.phonemizer.phonemes.<code>` holds the phoneme set of its IR as an array of strings: every segment that the language can emit, equal to `orthography2ipa.phoneme_set(code)`. The segments are NFD and hold no stress marks or syllable dots. A voice reads the key at load time and checks that its symbol table holds each segment. A language with an empty set, such as a stub, has no key. The set is exact for well-formed words with the default options: no dialect profile, no lexicon and no host hooks.

The set holds no stress marks (ˈ ˌ), syllable dots or tie bars. A voice adds ˈ and ˌ to its symbol table itself. A tied segment such as `t͡ʃ` is one entry of the set, so a voice that reads one code point per symbol splits each segment into its code points. Any language code that `orthography2ipa.registry.resolve` accepts works, lect codes included.

Record the ruleset with the voice. [revisions.md](revisions.md) says what moves a revision, and how to compare two of them.

A plugin that ships a word table gives it to the export with `--fragment PATH`. Repeat the flag for more than one file. A fragment is a JSON file `{"ir_version": 1, "words": {"word": "ipa"}}`. A fragment may carry `langs`, a list of language codes: `{"ir_version": 1, "langs": ["pt-PT"], "words": {"casa": "ˈkazɐ"}}`. The export merges the word tables into each language in the fragment's scope, and a later file wins on a duplicate word. A fragment without `langs` applies to every language. A code of `langs` matches a language when both resolve to the same registered code, so a fragment for `pt-PT` does not reach `pt-PT-x-lisbon`. A code that names no registered language is an error. The revision of each language in the ruleset covers the words.

A fragment may also carry `sandhi`, a list of rules between words, and `unsupported`, a list of the names of the plugin's rules that a fragment cannot express. A sandhi rule has the keys `left`, `right`, `left_out` and `right_out` of a spec sandhi rule, and may add `left_spelling` and `right_spelling`, patterns on the written word, `left_joined_spelling` and `right_joined_spelling`, patterns on the word joined to the word before it by a hyphen, or `"pause": true` for a rule on a word at a pause. The export adds the rules after the rules of each spec in scope. The key `loom.phonemizer.unsupported` lists the names from `unsupported`: the loom file does not run those rules, so the plugin keeps them as a host hook.

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

loom passes only numbers between the host and the script. `lang` is the 0-based index into `loom.text.languages`. The script runs in its own Lua state, without `io` and `os`, and it defines no global names except its two entry points:

| Function | Defined by | Input | Output |
| :--- | :--- | :--- | :--- |
| `phonemizer_data` | the host | `lang` | The string value of `loom.phonemizer.data.<code>`, or `nil` |
| `phonemize` | the script | `codepoints`, `lang` | The IPA as an array of codepoints, then the codepoints that the transcription drops |
| `set_lexicon` | the script | `lang`, an array of `{word codepoints, ipa codepoints}` pairs | nothing |

The script calls `phonemizer_data` the first time it needs a language, and keeps the decoded IR for later calls. The second result of `phonemize` holds the codepoints of the unknown and digit tokens, in text order: the characters that the Python package reports with `UnmappedGraphemeWarning`. The text "Azul 2024! ε" in Kabyle gives `æzul`, and the second result holds the codepoints of `2024ε`. Digits are unreadable for a phonemizer: number normalisation comes before it.

`set_lexicon` merges the pairs into the run-time lexicon of the language, and a later pair wins. The keys are lowercase NFC. The lexicon comes after the spec exceptions and before the fragment words, as the `lexicon` argument of the Python interpreter does. The ruleset does not cover the run-time lexicon, so the host records it.

The Python package gives the same IPA as the script for the same text:

```python
>>> import orthography2ipa
>>> orthography2ipa.transcribe("pedra", "pt-PT"), orthography2ipa.transcribe("os jogos", "pt-PT")
('ˈpɛdɾɐ', 'u ˈʒɔɡuʃ')

```

## Check loom against Python

`scripts/loom_parity.py` runs two text sets through a loom host and counts the texts where the loom output equals the expected output byte for byte:

- Every case of the conformance vectors in `tests/conformance/ir-v1/`, run on the IR of its file. An output case passes when the output equals its `expect`. An error case passes when loom stops with the message of its `expect_error`.
- Every sentence of the gold sets in `orthography2ipa/data/gold/`, compared with `orthography2ipa.transcribe` for the lect of the sentence.

The script exports one GGUF for each language and writes `benchmarks/loom_parity.json`. The last run gives:

| Set | Languages | Cases | Pass |
| :--- | ---: | ---: | ---: |
| Conformance vectors, output cases | 22 files | 3880 | 3880 |
| Conformance vectors, error cases | 1 file | 1 | 1 |
| Gold sentences | 188 lects | 6369 | 6369 |

The run used loom.cpp commit `f58f905` and orthography2ipa 7.133.1a4. To run it again, build loom.cpp and the host, then run the script:

```bash
git clone https://github.com/loom-ai-org/loom.cpp ../loom.cpp
cmake -S scripts/loom_host -B build/loom_host -DLOOM_DIR=$PWD/../loom.cpp -DCMAKE_BUILD_TYPE=Release
cmake --build build/loom_host -j4 --target o2i_loom
PYTHONPATH=$PWD .venv/bin/python scripts/loom_parity.py build/loom_host/o2i_loom "$(git -C ../loom.cpp rev-parse --short HEAD)"
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

`export_to_loom` writes the GGUF and returns the metadata that it wrote. With `expect_revisions`, it refuses to write a file when the revision of a language differs from the one you expect. `expect_revisions` takes the IR revisions of the ruleset, which equal `orthography2ipa.spec_revision(code)` ([revisions.md](revisions.md)):

```python
>>> import tempfile
>>> from pathlib import Path
>>> from gguf import GGUFReader
>>> from orthography2ipa.export_to_loom import export_to_loom
>>> out = Path(tempfile.mkdtemp()) / "voice.gguf"
>>> meta = export_to_loom(["pt-PT", "kab"], out)
>>> sorted(meta)
['fragments', 'o2i_version', 'phonemes', 'phonemizer_identity', 'ruleset', 'spec_revisions', 'unsupported']
>>> ruleset = GGUFReader(str(out)).fields["loom.phonemizer.ruleset"].contents()
>>> all(f"{code}={rev}" in ruleset for code, rev in meta["spec_revisions"].items())
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
