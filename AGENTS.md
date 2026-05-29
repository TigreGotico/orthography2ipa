# orthography2ipa — Agent Guide

Pure-data Python package: linguistically motivated grapheme→IPA and allophone mappings for 350+ language codes (356 JSON specs), plus a maximal-munch IPA tokenizer, phonological/script distance metrics, dialect transforms, and a pluggable G2P plugin system (e.g. algorithmic Arabic).

## Setup

```bash
pip install -e .
# optional algorithmic Arabic G2P (ONNX diacritization):
pip install -e .[arabic]
```

Runtime deps are minimal: `numpy`, `langcodes` (see `requirements.txt`). `langcodes` is used for ISO 639-3 → BCP-47 normalisation, with a hand-maintained fallback alias table in `registry.py`.

## Test

```bash
pytest tests
# with coverage (as CI runs it):
pytest --cov=orthography2ipa --cov-report xml tests
```

`tests/pytest.ini` and `tests/conftest.py` configure the suite. There is a broad per-family test layout (`test_iberian.py`, `test_celtic.py`, `test_slavic.py`, `test_germanic.py`, `test_indo_iranian.py`, …) plus `test_all_languages.py` and `test_language_integrity.py` that sweep every data file.

## Lint/Typecheck

No linter or type checker is configured. Code uses `from __future__ import annotations` and typed dataclasses but there is no mypy/ruff/flake8 config.

## Layout

- `orthography2ipa/types.py` — frozen dataclasses: `LanguageSpec`, `Grapheme2IPA`, `AllophoneMap`, `Ancestor`, `PositionalGrapheme2IPA`, `SandhiRule`; enums `QualityTier`/`ScriptType`/`AncestorRole`.
- `orthography2ipa/data/*.json` — 356 language/dialect spec files (the actual payload). `data/SCHEMA.md` documents the format; dialects inherit via `graphemes_base`/`allophones_base`. `data/lexicons/*.csv` hold reference word lists.
- `orthography2ipa/json_loader.py` — loads JSON specs and lexicons, resolves multi-ancestor inheritance.
- `orthography2ipa/registry.py` — `get()`, `available_codes()`, `available_families()`; lazy cache + plugin discovery + ISO alias table.
- `orthography2ipa/phonetok.py` — `PhonetokTokenizer`, beam-search IPA expansion (`IPAPath`, `Token`, `TokenKind`).
- `orthography2ipa/distance.py` + `feats.py` + `script_distance.py` — phonological/inventory/grapheme/tone/script distance metrics and feature vectors.
- `orthography2ipa/transforms.py` + `sandhi.py` + `lm.py` — dialect transforms, sandhi rules, language-model scoring helpers.
- `orthography2ipa/g2p_plugin.py` — `G2PPlugin` base; `plugins/arabic_g2p.py`, `plugins/tashkeel.py`, `plugins/arabic_utils.py` implement algorithmic Arabic G2P.
- `orthography2ipa/cli.py` — `orthography2ipa` console entry point (`list`, `info`, `transcribe`, `distance`; all support `--json`).
- `examples/` — runnable usage demos; `docs/` — Markdown reference (architecture, data model, tokenizer, distance, adding a language, bibliography).

### Entry-point groups

- `[project.scripts]` → `orthography2ipa = orthography2ipa.cli:main` (CLI).
- `[project.entry-points."orthography2ipa.g2p"]` → `arabic = orthography2ipa.plugins.arabic_g2p:ArabicG2PPlugin`. This is a **package-private** plugin group (not an OVOS/OPM group); third parties register algorithmic G2P backends here.

## Conventions (Org hard rules)

- Branches: `dev` for work, `master` for stable. NEVER `main`.
- Never edit `orthography2ipa/version.py` — gh-automations bumps semver from conventional-commit prefixes (`feat:`, `fix:`, `feat!:`).
- New repos private by default; do not make source public without asking.
- Commit identity: `JarbasAi <jarbasai@mailfence.com>`.
- Reference `TigreGotico`/`OpenVoiceOS` gh-automations reusable workflows at `@dev` (this repo currently pins `@master` — see TODO).
- No Neon / `neon-*` references.
- No meta-commentary: describe current state only — no history, dates, or "design mistake" framing in docs/commits/PRs/comments.
- CI is provided by gh-automations reusable workflows.

## Gotchas

- This is **pure data + logic, no trained network weights** despite living in the ML cluster — the only model artifact is the optional ONNX Arabic diacritizer, and `plugins/tashkeel.py` still has `# TODO: Load and run ONNX model for diacritization` (the ONNX path is not wired up).
- `dynamic = ["version", "dependencies"]`: version comes from `orthography2ipa/version.py` attr, deps from `requirements.txt`. The release workflows reference a `setup.py` that is not present in the tree — packaging is `pyproject`-only, so the `setup.py`-based release steps will fail.
- `QualityTier` ranges from `stub`/`skeleton` through `research`/`production`; not every one of the 356 specs is `production` quality. Check `spec.quality` before relying on a mapping.
- Graphemes ≠ allophones: `graphemes` maps a spelling to the phonemes it can represent; `allophones` maps a phoneme to its contextual surface forms. Keep them distinct.
- Many scratch report files (AUDIT.md, MAINTENANCE_REPORT.md, SUGGESTIONS.md, PLAN.md, QUICK_FACTS.md, FAQ.md) and 78 `.pyc` files are committed despite `.gitignore` — do not add more.
