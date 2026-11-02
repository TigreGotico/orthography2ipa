# orthography2ipa: agent guide

Read this file before you change anything in the repository. It gives the
map, the setup, the hard rules and the checks to run before a push. Each rule
links to a page with the detail. The documentation index is
[docs/index.md](docs/index.md).

`orthography2ipa` is a Python package of cited, per-language JSON specs and a
language-agnostic engine. The engine turns the specs into IPA
transcriptions, ranked pronunciation lattices and distances between
languages. It ships no trained weights and no word lists.

## Repository map

| Path | Holds |
|---|---|
| `orthography2ipa/data/*.json` | One spec per language, dialect or clade node. This is the payload |
| `orthography2ipa/data/SCHEMA.md` | Every JSON key the loader reads |
| `orthography2ipa/data/gold/` | Hand-built gold sets and correction overlays. In the repository only, not in the wheel |
| `orthography2ipa/json_loader.py` | Loads a spec and resolves its inheritance (`graphemes_base` and the other `*_base` keys) |
| `orthography2ipa/types.py` | The frozen dataclasses (`LanguageSpec`, `AllophoneRule`, `StressRules`) and `FIELD_INHERITANCE` |
| `orthography2ipa/schema.py` | Validation of a spec, used by `orthography2ipa validate` |
| `orthography2ipa/registry.py` | `get`, `resolve`, `available_codes`, the alias table and plugin discovery |
| `orthography2ipa/g2p.py` | `G2P` and `transcribe`: the pipeline from text to IPA |
| `orthography2ipa/phonetok.py` | The maximal-munch tokenizer, the lattice and beam search |
| `orthography2ipa/allophony.py`, `stress.py`, `sandhi.py`, `sentence.py` | Allophone rules, stress, cross-word rules and the sentence lattice |
| `orthography2ipa/distance.py`, `feats.py`, `script_distance.py` | The distance metrics |
| `orthography2ipa/plugins.py` and `*_plugin.py` | The pipeline steps a package can replace |
| `orthography2ipa/cli.py` | The `orthography2ipa` command |
| `docs/` | The documentation. `docs/index.md` sets the reading order |
| `scripts/` | Benchmark harness, board guards, generators ([scripts/README.md](scripts/README.md)) |
| `benchmarks/` | The committed board files ([benchmarks/README.md](benchmarks/README.md)) |
| `tests/` | The test suite ([tests/README.md](tests/README.md)) |
| `examples/` | Runnable usage scripts |

The full list of exported names is [docs/reference/api.md](docs/reference/api.md).

## Setup

```bash
unset VIRTUAL_ENV
uv venv --python 3.11 .venv
uv pip install --python .venv --prerelease=allow -e '.[test]'
```

Use uv, never pip. Build the venv inside the checkout. The `test` extra
carries `silabificador`, because the board and the gold sets pin output that
was produced with it. The CoRuSS gold needs `unar` or `unrar` on `PATH`.

## Pick the tests

The full suite takes several minutes. When you edit a spec, run the files
that name it first:

```bash
PYTHONPATH=$PWD .venv/bin/python scripts/which_tests.py --lang fi
PYTHONPATH=$PWD .venv/bin/python -m pytest $(PYTHONPATH=$PWD .venv/bin/python scripts/which_tests.py --lang fi)
```

With no `--lang`, `which_tests.py` reads the specs that changed against
`origin/dev`. Run the full suite before you push:

```bash
PYTHONPATH=$PWD .venv/bin/python -m pytest tests
```

Use `PYTHONPATH=$PWD` for every script, so that it measures the checkout
and not an installed package.

## Hard rules

1. The engine is language-agnostic. No language name, script or code drives
   a branch in `orthography2ipa/*.py`, and a spec carries no logic. A missing
   behaviour is a new generic capability
   ([engine.md](docs/contributing/engine.md)).
2. A `graphemes` key is an orthographic unit, never an n-gram, a cartesian
   product or a suffix chunk
   ([spec_authoring.md](docs/contributing/spec_authoring.md#a-grapheme-key-is-an-orthographic-unit)).
3. Never encode context by enumeration. Context goes in the rule layer
   ([spec_authoring.md](docs/contributing/spec_authoring.md#express-a-context)).
4. Linguistic accuracy outranks the score. A hack that lowers PER is still
   removed ([engine.md](docs/contributing/engine.md#accuracy-outranks-the-score)).
5. Every mapping is a cited claim. Quote the source you opened, with the
   page. Wikipedia and Ciberdúvidas are extra sources only
   ([citations.md](docs/contributing/citations.md)).
6. LLM-written and engine-pinned reference sets are silver labels, never
   gold, and they gate nothing
   ([citations.md](docs/contributing/citations.md#silver-labels-are-never-gold)).
7. The package ships no corpus: no lexicon, no gold set in the wheel, no
   weights. The caller supplies a lexicon
   ([spec_authoring.md](docs/contributing/spec_authoring.md#supply-a-lexicon-never-bundle-one)).
8. The library does not normalise text. Normalisation, diacritic restoration
   and script conversion belong downstream.
9. Leave no holes in the ancestry graph. A referenced ancestor with no file
   gets a cited stub.
10. A new spec field lands in `types.py`, `schema.py`, `json_loader.py` and
    `SCHEMA.md`, or it does not land
    ([engine.md](docs/contributing/engine.md#add-a-capability)).
11. Never carry the board backwards. Regenerate the five board files
    together, resolve a board conflict row by row, and keep `dev`'s value
    for every row you did not rescore
    ([board.md](docs/contributing/board.md)).
12. A burn-down list (`_WIKIPEDIA_ONLY_SOURCES_BURNDOWN`,
    `_DOCS_PROSE_RATCHET`) may only shrink. Never add an entry to make a red
    build green.
13. Never edit a generated file by hand: the board files,
    `docs/reference/*.md`, `llms.txt` and the navigation footers. Fix the
    generator and run it.
14. `tests/test_grammatical_endings.py` caps the list-valued endings per
    spec. Raising the cap is an amendment to this file, argued here first
    ([spec_authoring.md](docs/contributing/spec_authoring.md#ambiguous-grammatical-endings)).
15. Never edit `orthography2ipa/version.py`. The release workflow bumps it
    from the conventional-commit prefix.

## Before you push

1. Run the full test suite.
2. If you changed `docs/`, a generator, an exported name, its docstring or a
   CLI option, run the prose test and the two generators:

```bash
PYTHONPATH=$PWD .venv/bin/python -m pytest tests/test_docs_prose.py
.venv/bin/python scripts/docs_nav.py --check
PYTHONPATH=$PWD .venv/bin/python scripts/gen_reference_docs.py --check
```

3. If you added, removed or moved a page, add it to a table in
   `docs/index.md`, then run `scripts/docs_nav.py --write` and
   `scripts/gen_reference_docs.py --write`.
4. If you changed a spec, run the board guards in
   [board.md](docs/contributing/board.md#the-guards). If the change moves board
   rows it does not own, add a `Board-Rows:` line to the pull request.
5. If you changed engine code, answer the review gate in
   [engine.md](docs/contributing/engine.md#the-review-gate-for-engine-code).
6. Squash to one commit with a conventional-commit message (`fix:`, `feat:`,
   `docs:`). Open the pull request against `dev`, as a draft, and fill in
   `.github/pull_request_template.md`.

## Conventions

- `dev` is the work branch and `master` is the stable branch. There is no
  `main`.
- Commit identity: `JarbasAi <jarbasai@mailfence.com>`.
- Reusable workflows from `OpenVoiceOS/gh-automations` are referenced at
  `@dev`.
- No Neon packages or references.
- Documentation states what is. It carries no dates, no history and no
  "design mistake" framing.
- Documentation prose follows ASD-STE100 in its flavoured mode.
  `scripts/ste_lint.py` checks every page under `docs/`.

## Gotchas

- `pyproject.toml` reads the version from `orthography2ipa/version.py` and
  lists the dependencies itself.
- Check `spec.quality` before you rely on a mapping. Most specs are `stub`.
- `graphemes` maps a spelling to the phonemes it can stand for, and
  `allophones` maps a phoneme to its surface forms. Keep them apart.
- espeak-ng data is GPL. The comparison harness builds it in
  `.espeak_rules_only/` and `.o2i_lex_cache/`, which git ignores. Never commit
  it.
