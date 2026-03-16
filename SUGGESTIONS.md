# SUGGESTIONS.md — orthography2ipa

_Last updated: 2026-03-16 | Author: Claude Sonnet 4.6_

Agent proposals for refactors and enhancements. Each item is labelled with effort
and rationale. Humans decide whether to act on these.

---

## S1 — Add `mypy` to CI [Effort: Low]

Add a `.github/workflows/typecheck.yml` workflow running `mypy orthography2ipa/
--ignore-missing-imports`. This catches type errors before they reach reviewers.
Start permissive; tighten incrementally.

**Why**: The codebase has partial type annotations. Without CI enforcement, gaps
accumulate silently. `feats.py:56` is a current example.

---

## S2 — Add Coverage Reporting to CI [Effort: Low]

Add `--cov=orthography2ipa --cov-report=xml` to the existing `unit_tests.yml`
workflow and upload the report as a CI artifact (or integrate with Codecov/Coveralls).

**Why**: 7375 tests exist but no coverage baseline is tracked. A coverage gate
prevents future regressions going unnoticed.

---

## S3 — Deprecate and Remove `lm.py` Legacy Wrappers in v0.3.0 [Effort: Low]

The `DeprecationWarning` wrappers in `feats.py` for `build_ngram_lm`, `perplexity`,
and `phoneme_embeddings` were added in 2026-03-09. Remove them in v0.3.0.

**Why**: The wrappers exist only for backwards compatibility. Keeping them long-term
bloats `feats.py` and confuses new contributors.

**Plan**: Add a `TODO: remove in v0.3.0` comment now; remove in the 0.3.0 PR.

---

## S4 — Implement Tashkeel ONNX Model [Effort: High]

`orthography2ipa/plugins/tashkeel.py` is a stub. Implement it using a permissively-
licensed pre-trained ONNX model (e.g., `shakeel-ali/arabic-diacritizer` on HuggingFace,
Apache 2.0). This would make `ArabicG2PPlugin` production-ready for unvowelled Arabic input.

**Why**: Arabic G2P without diacritics is ambiguous. The infrastructure is in place;
only the model is missing.

**Prerequisite**: Verify model license is Apache 2.0 or compatible before bundling.

---

## S5 — Add Beam-Search Path Caching to `PhonetokTokenizer` [Effort: Medium]

`phonetok.py:ipa_beam()` recomputes paths on every call. Add an LRU cache keyed by
`(grapheme_sequence, beam_width)` — e.g., `functools.lru_cache` on an internal method
or a `dict`-based cache on the tokenizer instance.

**Why**: Repeated transcription of the same words (e.g., in TTS pipelines) is
currently O(n) per call. Caching makes it O(1) for warm inputs.

---

## S6 — Add `strict=False` Parameter to `segment_distance()` [Effort: Low]

`distance.py:segment_distance(a, b)` silently skips unrecognized IPA phones.
Adding `strict: bool = False` that raises `ValueError` on unrecognized input
would make errors explicit for callers who want them.

**Why**: Silent skip can mask data quality issues (e.g., malformed IPA from a
third-party source). The opt-in `strict` mode is safe and non-breaking.

---

## S7 — Extract Transforms Documentation to `docs/transforms.md` [Effort: Low]

15 dialect transform profiles are defined in `transforms.py` with inline docstrings.
Extracting these to `docs/transforms.md` with one section per profile (name, rules,
linguistic source, example) would make the feature discoverable without reading source.

**Why**: The transforms feature is one of the most distinctive capabilities of the
package. It deserves a standalone doc page.

---

## S8 — Expand African and Southeast Asian Language Coverage [Effort: High]

~238 stub specs exist for languages across Africa, Southeast Asia, and Oceania.
Prioritize:
- Swahili (`sw`) and Swahili variants
- Tagalog (`tl`) / Filipino dialects
- Tibetan (`bo`)
- Yoruba (`yo`)
- Thai (`th`)

**Why**: These are high-traffic NLP languages with significant speaker populations.
Stub specs produce empty tokenizer output, limiting usefulness.

**Process**: Each language requires a linguistically reviewed grapheme table,
allophone inventory, and positional graphemes. Community contributions are welcome.

---

## S9 — Add `pip-audit` to CI [Effort: Low]

Add a `.github/workflows/pip-audit.yml` step to scan runtime dependencies
(`numpy`, `langcodes`, `onnxruntime`) for known CVEs.

**Why**: Good security hygiene. Low false-positive rate for these stable packages.

---

## S10 — Multi-Version Python Matrix in CI [Effort: Low]

`pyproject.toml` claims support for Python 3.9–3.13. The CI only tests one version.
Add a matrix strategy to `unit_tests.yml`:

```yaml
strategy:
  matrix:
    python-version: ["3.9", "3.10", "3.11", "3.12", "3.13"]
```

**Why**: `numpy` and `langcodes` occasionally have version-specific behavior.
Testing the full matrix ensures the classifier claims are accurate.
