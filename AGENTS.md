# orthography2ipa: agent guide

`orthography2ipa` is a Python package of cited, per-language JSON specs and one language-agnostic engine. The engine turns the specs into IPA transcriptions, ranked pronunciation lattices and distances between languages, with no trained weights and no word lists.

The documentation starts at [docs/index.md](docs/index.md).

## Repository map

| Path | Holds |
|---|---|
| `orthography2ipa/data/*.json` | One spec per language, dialect or clade node. [SCHEMA.md](orthography2ipa/data/SCHEMA.md) lists every key |
| `orthography2ipa/data/gold/` | Gold sets and correction overlays. The wheel ships them, and the euskaphone and arbtok benchmarks read them from the installed package |
| `orthography2ipa/types.py`, `schema.py`, `json_loader.py` | The frozen dataclasses, spec validation, and the loader with its inheritance |
| `orthography2ipa/registry.py` | `get`, `resolve`, `available_codes` and the alias table |
| `orthography2ipa/g2p.py`, `phonetok.py` | `G2P`, `transcribe`, the tokenizer, the lattice and beam search |
| `orthography2ipa/allophony.py`, `stress.py`, `sandhi.py` | Allophone rules, stress and cross-word rules |
| `orthography2ipa/distance.py`, `feats.py`, `script_distance.py` | The distance metrics |
| `orthography2ipa/ir/` | The compiler, the IR schema and the Python and Lua interpreters ([ir.md](docs/engine/ir.md)) |
| `orthography2ipa/export_to_loom.py` | One loom GGUF of the Lua interpreter and the IRs ([loom_export.md](docs/guide/loom_export.md)) |
| `orthography2ipa/cli.py` | The `orthography2ipa` command |
| `docs/`, `scripts/`, `benchmarks/`, `tests/`, `examples/` | Documentation, generators and harness ([scripts/README.md](scripts/README.md)), board files, tests, usage scripts |

## Setup and tests

```bash
unset VIRTUAL_ENV
uv venv --python 3.11 .venv
uv pip install --python .venv --prerelease=allow -e '.[test]'
PYTHONPATH=$PWD .venv/bin/python -m pytest $(PYTHONPATH=$PWD .venv/bin/python scripts/which_tests.py --lang fi)
PYTHONPATH=$PWD .venv/bin/python -m pytest tests
```

Use uv, never pip. `which_tests.py` lists the test files that name a spec. With no `--lang`, it reads the specs that changed against `origin/dev`. Run every script with `PYTHONPATH=$PWD`, so that it measures the checkout. The CoRuSS gold needs `unar` or `unrar` on `PATH`. The comparison harness builds GPL-3.0 espeak-ng data in `.espeak_rules_only/` and `.o2i_lex_cache/`. Git ignores both folders, and you never commit them.

## Hard rules

1. The engine is language-agnostic. No language drives a branch in the transcription code, and a spec carries no logic. Tag resolution in `registry.py` is the one exception: it holds named fallbacks for `fr`, `bs` and `ar` ([engine.md](docs/contributing/engine.md#the-engine-is-language-agnostic)).
2. A `graphemes` key is an orthographic unit, never an n-gram or a suffix chunk ([spec_authoring.md](docs/contributing/spec_authoring.md#a-grapheme-key-is-an-orthographic-unit)).
3. Context goes in the rule layer, never in an enumeration of keys ([spec_authoring.md](docs/contributing/spec_authoring.md#express-a-context)).
4. Linguistic accuracy outranks the score. A hack that lowers PER is removed ([engine.md](docs/contributing/engine.md#accuracy-outranks-the-score)).
5. Every mapping is a cited claim, with the page of the source you opened. Wikipedia and Ciberdúvidas are extra sources only ([citations.md](docs/contributing/citations.md)).
6. LLM-written and engine-pinned reference sets are silver labels. They gate nothing ([citations.md](docs/contributing/citations.md#silver-labels-are-never-gold)).
7. The wheel ships no lexicon and no weights. A caller supplies a lexicon ([spec_authoring.md](docs/contributing/spec_authoring.md#supply-a-lexicon-never-bundle-one)).
8. The library does not normalise text. Normalisation and script conversion belong downstream ([getting_started.md](docs/guide/getting_started.md#preparing-text-before-the-lattice)).
9. A referenced ancestor with no file gets a cited stub ([ancestry.md](docs/specs/ancestry.md)).
10. A new spec field lands in `types.py`, `schema.py`, `json_loader.py` and `SCHEMA.md` together ([engine.md](docs/contributing/engine.md#add-a-capability)).
11. Never carry the board backwards. Regenerate the five board files together and keep `dev`'s value for every row you did not rescore ([board.md](docs/contributing/board.md#never-carry-the-board-backwards)).
12. A burn-down list (`_WIKIPEDIA_ONLY_SOURCES_BURNDOWN`, `_DOCS_PROSE_RATCHET`) may only shrink ([board.md](docs/contributing/board.md#never-carry-the-board-backwards)).
13. Never edit a generated file by hand: the board files, `docs/reference/api.md`, `docs/reference/cli.md`, the navigation footers, the atlas blocks, the agent hints of generated pages and the atlas indexes. Fix the generator and run it.
14. `tests/test_grammatical_endings.py` caps the list-valued endings per spec ([spec_authoring.md](docs/contributing/spec_authoring.md#ambiguous-grammatical-endings)).
15. Never edit `orthography2ipa/version.py` or `CHANGELOG.md`. The release workflow writes them.
16. The IR interpreters hold no language knowledge: no branch on a language, script or family, no Unicode name lookup, no codepoint range test. Only the compiler may hold language tables. Never grow `IR_OPAQUE_WORDS` to pass the check ([behaviour_is_data.md](docs/contributing/behaviour_is_data.md#run-the-guards)).
17. A change to an IR version or a primitive semantics version in `layout.py` changes `docs/ir/o2i-ir-v1.md` in the same pull request ([behaviour_is_data.md](docs/contributing/behaviour_is_data.md#change-a-version-change-the-spec)).
18. The Python and Lua interpreters give the same output, and the IR matches the rules path apart from the ruled changes of section 9 of the IR spec.

## Before you push

1. Run the full test suite.
2. If you changed `docs/`, a generator, an exported name, a docstring, a CLI option, a spec or a board file, run the prose test and the three generators:

```bash
PYTHONPATH=$PWD .venv/bin/python -m pytest tests/test_docs_prose.py
.venv/bin/python scripts/docs_nav.py --check
PYTHONPATH=$PWD .venv/bin/python scripts/gen_reference_docs.py --check
PYTHONPATH=$PWD .venv/bin/python scripts/gen_language_atlas.py --check
```

3. A page you add goes in a table of `docs/index.md` and gets an `agent-hint` comment after its H1. Then `scripts/docs_nav.py --write` writes its footer.
4. If you changed `orthography2ipa/`, run the IR guards (`luajit` on `PATH`):

```bash
.venv/bin/python -I scripts/check_engine_agnostic.py
python3 -I scripts/check_ir_version_doc.py --base origin/dev
.venv/bin/python -I scripts/ir_parity_ci.py
```

5. If you changed a spec, run the board guards ([board.md](docs/contributing/board.md#the-guards)).
6. If you changed engine code, answer the review gate ([engine.md](docs/contributing/engine.md#the-review-gate-for-engine-code)).
7. Open a draft pull request against `dev` with `.github/pull_request_template.md`.

`dev` is the work branch and `master` is the stable branch.
