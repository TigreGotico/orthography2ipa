# AGENTS.md — orthography2ipa

AI agent instructions for this repository.
Read this file before starting any task here.

---

## 1. Commands

```bash
# Install in editable mode (use uv, never pip directly)
uv pip install -e .

# Run all tests
uv run pytest tests/

# Run fast tests only
uv run pytest tests/ -m "not slow"

# Run with coverage (mandatory before marking a task done)
uv run pytest tests/ -v --cov=orthography2ipa --cov-report=term-missing

# Run a single test file
uv run pytest tests/test_language_integrity.py -v

# Run a single test function
uv run pytest tests/test_types.py::test_resolve_grapheme_positional -v
```

---

## 2. Architecture

| Module | Responsibility |
| :--- | :--- |
| `orthography2ipa/types.py` | Frozen dataclasses: `LanguageSpec`, `LinguisticSource`, `Ancestor`, `SandhiRule`, enums |
| `orthography2ipa/registry.py` | Lazy-load registry mapping BCP-47 codes → `LanguageSpec` |
| `orthography2ipa/json_loader.py` | JSON → `LanguageSpec` with inheritance resolution |
| `orthography2ipa/phonetok.py` | Maximal-munch tokenizer + beam-search IPA expansion |
| `orthography2ipa/distance.py` | Phonological distance (inventory, grapheme, ancestry) |
| `orthography2ipa/feats.py` | 23-feature SPE/IPA distinctive-feature system |
| `orthography2ipa/transforms.py` | 15 dialect transform profiles (Iberian Romance) |
| `orthography2ipa/script_distance.py` | Typological distance between writing systems |
| `orthography2ipa/sandhi.py` | Cross-word-boundary phonological rules |
| `orthography2ipa/plugins/` | Arabic G2P, tashkeel stub, abstract plugin interface |
| `orthography2ipa/data/*.json` | 308 language specs (see SCHEMA.md) |
| `orthography2ipa/__init__.py` | Aggregated public surface |

### Central data object: `LanguageSpec` (`types.py`)

- `graphemes: Dict[str, List[str]]` — orthographic unit → IPA candidates (most common first)
- `allophones: Dict[str, List[str]]` — phoneme → surface realisations
- `positional_graphemes: Dict[str, Dict[GraphemePosition, List[str]]]` — context-sensitive overrides
- `ancestors: Tuple[Ancestor, ...]` — ancestry chain with weighted roles
- `sources: Tuple[LinguisticSource, ...]` — bibliographic references for phonological decisions
- `parent: str | None` — shorthand for primary parent code

`LanguageSpec.resolve_grapheme(grapheme, position)` applies a three-level lookup:
positional override → positional DEFAULT fallback → base `graphemes`.

All dataclasses are **frozen** (hashable, safe to cache and use as dict keys).

### Registry

`registry.py` maps `code → lazy-loaded LanguageSpec`. Languages are imported only when `get(code)` is called. ISO 639-3 codes (e.g. `"eng"`) are resolved to BCP-47 (e.g. `"en-GB"`) via `_resolve_code()`.

---

## 3. Language JSON Files (`orthography2ipa/data/*.json`)

See `orthography2ipa/data/SCHEMA.md` for the full schema.

Key conventions:
- `"graphemes"`: canonical phonemes only, most common first.
- `"graphemes_base"`: use this instead of redefining a key that is identical to the parent.
- Set a key explicitly to `null` to suppress an inherited grapheme or allophone.
- `"allophones"`: all canonical phonemes → surface realisations, most common first.
- `"positional_graphemes"`: define only ambiguous graphemes; skip unambiguous ones.
- `"sources"`: **required for any `quality` tier other than `"stub"`** — array of `LinguisticSource` objects.
- Language codes follow BCP-47 with `x-` private extensions for dialects (e.g. `"pt-BR-x-rj"`).

### `LinguisticSource` JSON structure

```json
{
  "id": "wells1982_vol1",
  "author": "Wells, J.C.",
  "year": 1982,
  "title": "Accents of English, Vol. 1: An Introduction",
  "publisher": "Cambridge University Press",
  "url": null,
  "pages": "120–135",
  "notes": "Primary phoneme inventory reference"
}
```

- `id` is a short cite key (e.g. `wells1982`, `roach2009`).
- `url`: use `null` for print-only works. Never fabricate URLs.
- Wikipedia is acceptable for language overview only, not for phonological claims.
- Prefer: DOI links, publisher pages, archive.org. Google Books / WorldCat acceptable for print works.

---

## 4. Ongoing Work: Linguistic Reference Audit

Read `PLAN.md` and `TODO.md` at project root before resuming any sourcing work.

### Progress

| Phase | Scope | Status |
| :--- | :--- | :--- |
| Phase 0 — Infrastructure | `LinguisticSource` type, `json_loader`, `SCHEMA.md` | **COMPLETE** |
| Phase 1 — Germanic | 33 files (en-*, de-*, nl-*, sv-*, da-*, nb, nn, is, fo, af, nds, enm, ang, non, osx, goh, gem-*) | **COMPLETE** |
| Phase 2 — Romance | 60+ files (es-*, pt-*, it-*, fr-*, ca-*, gl-*, ro-*, oc, sc, scn, la-*, …) | **COMPLETE** |
| Phase 3 — Semitic/Arabic | ar-*, arb, sem-*, phn, cop | **COMPLETE** |
| Phase 4 — Indo-Iranian | hi, ur, bn, pa, gu, mr, ne, sa, pi, fa-*, ps, sd, iir, ira, … | **COMPLETE** |
| Phase 5 — Other Modern | ru-*, uk, be, bg, cs, pl, el, tr, fi, hu, eu-*, ko, ja, zh, ms, … | **COMPLETE** |
| Phase 6 — Ancient/Extinct | ine, cel-*, osc, etr, xib, xlg, xpa, cop, peo, pal, cu, … | **COMPLETE** |

After adding sources to a batch:
```bash
uv run pytest tests/test_sources.py -v
uv run pytest tests/test_language_integrity.py -v
```

---

## 5. Testing Rules

- Every code change requires passing unit tests before the task is considered done.
- Tests live in `tests/`.
- Custom markers: `slow` (skip with `-m "not slow"`), `linguistic` (spot-check tests).
- `test_language_integrity.py` validates ALL registered language specs structurally — always run this after touching any JSON or `json_loader.py`.
- `test_sources.py` enforces that non-stub languages have at least one `LinguisticSource`.
- Coverage must not decrease. Check with `--cov-report=term-missing`.

---

## 6. Git Rules

- **Never `git push`** under any circumstances. Prepare commits locally only.
- Humans push commits and open/merge PRs.
- Commit after each logical batch (e.g. per language family).
- Do not commit `.pyc` files or `.venv/` contents.

---

## 7. Documentation Rules

Update the following files after any task that changes public API, JSON schema, or language data:

| File | When to update |
| :--- | :--- |
| `FAQ.md` | First — any user-visible behaviour change |
| `QUICK_FACTS.md` | Version, class list, entry points |
| `MAINTENANCE_REPORT.md` | Every session — date-stamped log of changes |
| `AUDIT.md` | New known issues or resolved debt |
| `SUGGESTIONS.md` | New improvement proposals |
| `docs/bibliography.md` | After adding sources for a language family |
| `PLAN.md` | After completing a phase or major milestone |
| `TODO.md` | Tick off completed items; add new ones |

All docs describing runtime behaviour **must cite source code** as `` `ClassName.method` — `path/to/file.py:LINE` ``.

---

## 8. Code Standards

- Python 3.10+ support required (the `.venv` may use 3.13 but code must be compatible with 3.10+).
- Type hints and docstrings are mandatory for all public functions and classes.
- No relative imports — explicit imports only.
- PEP 8 style. Use `dataclasses` for structured data.
- Use `uv run`, `uv pip install`, `uv add` — never bare `pip`.
