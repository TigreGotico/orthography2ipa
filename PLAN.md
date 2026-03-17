# PLAN.md — orthography2ipa

_Last updated: 2026-03-17_

## Project Status: Alpha (v0.2.0a1)

orthography2ipa is a linguistically motivated grapheme-to-IPA conversion library
covering 308+ language codes with allophone inventories, dialect transforms, phonological
distance metrics, language ancestry modelling, and a G2P plugin architecture.

---

## Architecture Overview

| Layer | Module | Responsibility |
| :--- | :--- | :--- |
| Data model | `types.py` | Frozen dataclasses: `LanguageSpec`, `Ancestor`, `SandhiRule`, enums |
| Registry | `registry.py` | Lazy-load registry + entry-point plugin discovery |
| JSON loading | `json_loader.py` | JSON→LanguageSpec conversion, inheritance resolution |
| Tokenizer | `phonetok.py` | Maximal-munch tokenizer + beam-search IPA expansion |
| Distance | `distance.py` | Phonological distance (inventory, grapheme, ancestry) |
| Features | `feats.py` | 23-feature SPE/IPA distinctive-feature system |
| Transforms | `transforms.py` | 15 dialect transform profiles (Iberian Romance) |
| Script distance | `script_distance.py` | Typological distance between writing systems |
| Sandhi | `sandhi.py` | Cross-word-boundary phonological rules |
| Plugins | `plugins/` | Arabic G2P, tashkeel stub, abstract plugin interface |
| Public API | `__init__.py` | Aggregated public surface |

**Data**: 308 JSON language specs in `data/`, 1 CSV lexicon.
**CI**: 4 GitHub Actions workflows (unit tests, release, PyPI publish, commit labeling).
**Tests**: 22 test files, 7375 passing tests.

---

## Current Phase: Documentation & Quality Hardening

### Phase Goals
1. Close mandatory documentation gaps (QUICK_FACTS.md, AUDIT.md, SUGGESTIONS.md)
2. Complete type hint coverage in `feats.py` and `plugins/arabic_g2p.py`
3. Add CI coverage reporting
4. Fix minor issues identified in review

### Out of Scope (next major version)
- Tashkeel ONNX implementation (requires external model; optional feature)
- Expanding stub language data (ongoing linguistics work)
- New dialect transform profiles

---

## Planned Changes

### P1 — Required Documentation (blocking for 0.2.0 stable)

| File | Content Summary |
| :--- | :--- |
| `QUICK_FACTS.md` | Package name, version, Python support, key classes, install command, quick example |
| `AUDIT.md` | Known issues with file:line citations, tech debt, data quality notes |
| `SUGGESTIONS.md` | Proposed refactors and enhancement ideas |

### P2 — Code Quality (0.2.0 stable)

| File | Issue | Fix |
| :--- | :--- | :--- |
| `orthography2ipa/feats.py:56` | `phone_features` dict has no type annotation | Add `Dict[str, List[Optional[bool]]]` |
| `orthography2ipa/plugins/arabic_g2p.py` | Some helper methods missing `-> str` return type | Add return type annotations |
| `orthography2ipa/json_loader.py:115` | Unclear TODO comment (`# TODO - error log, illegal`) | Clarify: cycle detection comment |
| `pyproject.toml` | Description says "20+ languages", actual: 308+ | Update description string |

### P3 — CI Improvements (0.2.x)

| Workflow to Add | Purpose |
| :--- | :--- |
| Coverage reporting (`--cov`) | Track coverage %; prevent regressions |
| Multi-version Python matrix | Verify 3.9–3.13 compatibility |
| Lint (flake8 or ruff) | Enforce PEP 8 |

---

## Data Roadmap

| Tier | Count | Status |
| :--- | :--- | :--- |
| Production-quality | ~50 | ✓ Validated, allophone inventories complete |
| Research-quality | ~20 | ✓ Reviewed against academic sources |
| Stub/skeleton | ~238 | Auto-generated from ancestry; minimal data |

Stub specs need community/contributor data; not a solo-agent task.

---

## Dependency Strategy

- `numpy` — feature vector operations in `feats.py`; keep
- `langcodes` — BCP-47 normalization; keep
- `onnxruntime` — optional for Arabic tashkeel; keep optional
- No new runtime dependencies planned

---

## Testing Strategy

- All new code changes require unit tests in `test/`
- Run: `uv run pytest test/ -v --cov=orthography2ipa --cov-report=term-missing`
- Target: maintain or increase coverage percentage
- Integration tests in `test/test_integration.py` for end-to-end pipelines

---

## Linguistic Reference Audit

### Goal
Every language spec with `quality != "stub"` must have a populated `sources` array
traceable to published phonological literature. Enables reproducibility and
future `quality: "production"` promotion.

### Infrastructure (Phase 0) — COMPLETE
- `LinguisticSource` frozen dataclass added to `types.py`
- `sources: Tuple[LinguisticSource, ...]` field added to `LanguageSpec`
- `json_loader.py` parses `sources` array
- `SCHEMA.md` documents `sources` field and its schema
- `tests/test_sources.py` enforces non-stub languages have sources

### Source Audit Progress

| Phase | Languages | Status |
| :--- | :--- | :--- |
| Phase 1 — Germanic | en-GB, en-US, en-AU, en-CA, en-IE, en-ZA, en-GB-x-scotland, de-DE, de-AT, de-CH, nl, nl-NL, nl-BE, sv, sv-x-rikssvenska, nb, nn, no, da, da-x-copenhagen, is, fo, af, nds, enm, ang, non, osx, goh, gem, gem-x-ingvaeonic, gem-x-north, gem-x-northwest | COMPLETE (33 files) |
| Phase 2 — Romance | es-ES, es-*, pt-PT, pt-BR, pt-*, fr-FR, it-IT, it-*, ca, ca-*, ro-RO, gl, oc, sc, scn, lij, lmo, vec, fur, frp, nap, egl, pms, la, etc. | TODO |
| Phase 3 — Semitic/Arabic | ar, ar-*, arb, sem, sem-*, etc. | TODO |
| Phase 4 — Indo-Iranian | hi, ur, bn, pa, gu, mr, ne, sa, pi, fa, fa-*, ps, sd, etc. | TODO |
| Phase 5 — Other Modern | ru, ru-*, uk, be, bg, mk, sr, hr, cs, sk, pl, sl, sla, el, cy, ga, gd, kw, br, gv, eu, tr, fi, hu, ko, ja, zh, ms, etc. | TODO |
| Phase 6 — Ancient/Extinct | ine, iir, ira, cop, cu, phn, peo, pal, osc, xum, xlp, etc. | TODO |

### Session Resume Instructions
1. Read this `PLAN.md` for current progress
2. Read `TODO.md` for per-language checklist
3. Check `MAINTENANCE_REPORT.md` for last session's changes
4. Continue from next unchecked phase
5. After adding sources: `uv run pytest tests/test_sources.py -v`
