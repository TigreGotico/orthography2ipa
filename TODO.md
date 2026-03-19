# TODO.md — orthography2ipa

_Last updated: 2026-03-19 | Reviewed by: Claude Sonnet 4.6_

Legend: 🔴 Blocking · 🟡 High · 🟢 Medium · ⚪ Low

---

## 🔴 BLOCKING (required before 0.2.0 stable release)

All blocking items resolved. ✅

---

## 🟡 HIGH (target: 0.2.0 stable)

- [ ] **Add 3.9 and 3.13 to CI Python matrix**
  - `unit_tests.yml` currently tests 3.10, 3.11, 3.12 — add 3.9 and 3.13
  - Verify `pyproject.toml` classifiers match actual tested versions

- [ ] **Add lint workflow**
  - Add `.github/workflows/lint.yml` using `ruff`
  - Fix any existing lint errors before enabling in CI

- [ ] **Add `mypy` type-check workflow**
  - Add `.github/workflows/typecheck.yml` with `--ignore-missing-imports`
  - Fix type errors systematically

---

## 🟢 MEDIUM (target: 0.2.x patch releases)

- [ ] **Clarify TODO comment in `json_loader.py:115`**
  - Replace: `continue  # TODO - error log, illegal`
  - With: `continue  # Skip self-reference cycles (parent == code); invalid per schema`

- [ ] **Add `docs/transforms.md`**
  - Extract 15 dialect profile details from `transforms.py` docstrings to standalone doc

- [ ] **Add `pip-audit` workflow**

---

## ⚪ LOW / FUTURE

- [ ] **Implement Arabic tashkeel via ONNX**
  - `orthography2ipa/plugins/tashkeel.py:50`
  - Blocked on: model licensing decision

- [ ] **Add deprecation to `lm.py` legacy functions**
  - Use `warnings.warn()` — plan removal in v0.3.0

- [ ] **Expand stub language data**
  - ~238 stub specs have minimal grapheme data
  - Priority: Swahili variants, Tagalog dialects, Tibetan

- [ ] **Performance: cache beam-search paths**
  - `phonetok.py` beam search recomputes paths on each call
  - Cache by `(language_code, grapheme_sequence)` key

- [ ] **Input validation in `distance.py`**
  - `segment_distance(a, b)` accepts malformed IPA silently
  - Add optional `strict=False` parameter; raise `ValueError` if `strict=True`

---

## Linguistic Reference Audit Checklist

### Phase 0 — Infrastructure (COMPLETE 2026-03-17) ✅
### Phase 1 — Germanic (COMPLETE 2026-03-17) ✅
### Phase 2 — Romance (COMPLETE) ✅
### Phase 3 — Semitic/Arabic (COMPLETE) ✅
### Phase 4 — Indo-Iranian (COMPLETE) ✅
### Phase 5 — Other Modern (COMPLETE) ✅
### Phase 6 — Ancient/Reconstructed/Extinct (COMPLETE) ✅

All 308 non-stub language codes now have at least one bibliographic source or Wikipedia reference.
`wikipedia` field migrated to `Tuple[str, ...]` format (2026-03-19).
