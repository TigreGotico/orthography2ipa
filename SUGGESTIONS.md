# SUGGESTIONS.md — orthography2ipa

_Last updated: 2026-03-25 | Author: Claude Opus 4.6_

Agent proposals for refactors and enhancements. Each item is labelled with effort
and rationale. Humans decide whether to act on these.

---

## S1 — Add `mypy` to CI [Effort: Low]

Add a `.github/workflows/typecheck.yml` workflow running `mypy orthography2ipa/
--ignore-missing-imports`. Start permissive; tighten incrementally.

**Why**: Partial type annotations exist. Without CI enforcement, gaps accumulate.
`feats.py:650-683` deprecation shims are a current example.

---

## S2 — Add Coverage Reporting to CI [Effort: Low]

Add `--cov=orthography2ipa --cov-report=xml` to the existing `unit_tests.yml`
workflow and upload the report as a CI artifact (or integrate with Codecov/Coveralls).

**Why**: 7375 tests exist but no coverage baseline is tracked. A coverage gate
prevents future regressions going unnoticed.

---

## S3 — Remove `lm.py` Legacy Wrappers in v0.3.0 [Effort: Low]

The `DeprecationWarning` wrappers in `feats.py:650-683` for `build_ngram_lm`, `perplexity`,
and `phoneme_embeddings` were added in 2026-03-09. Remove them in v0.3.0.

**Why**: The wrappers exist only for backwards compatibility. Keeping them long-term
bloats `feats.py` and confuses new contributors.

---

## S4 — Implement Tashkeel ONNX Model [Effort: High]

`orthography2ipa/plugins/tashkeel.py` is a stub. Implement it using a permissively-
licensed pre-trained ONNX model. This would make `ArabicG2PPlugin` production-ready
for unvowelled Arabic input.

**Why**: Arabic G2P without diacritics is ambiguous. The infrastructure is in place;
only the model is missing.

**Prerequisite**: Verify model license is Apache 2.0 or compatible before bundling.

---

## S5 — Add Beam-Search Path Caching to `PhonetokTokenizer` [Effort: Medium]

`phonetok.py:ipa_beam()` recomputes paths on every call. Add an LRU cache keyed by
`(grapheme_sequence, beam_width)`.

**Why**: Repeated transcription of the same words (e.g., in TTS pipelines) is
currently O(n) per call. Caching makes it O(1) for warm inputs.

---

## S6 — Add `strict=False` Parameter to `segment_distance()` [Effort: Low]

`distance.py:segment_distance(a, b)` silently skips unrecognized IPA phones.
Adding `strict: bool = False` that raises `ValueError` on unrecognized input
would make errors explicit for callers who want them.

**Why**: Silent skip can mask data quality issues. Opt-in `strict` mode is non-breaking.

---

## S7 — Extract Transforms Documentation to `docs/transforms.md` [Effort: Low]

15 dialect transform profiles are defined in `transforms.py` with inline docstrings.
Extracting these to a standalone doc page would make the feature discoverable
without reading source.

**Why**: The transforms feature is one of the most distinctive capabilities of the
package. It deserves a standalone doc page.

---

## S8 — Expand African and Southeast Asian Language Coverage [Effort: High]

~238 stub specs exist for languages across Africa, Southeast Asia, and Oceania.
Prioritize: Swahili (`sw`), Tagalog (`tl`), Tibetan (`bo`), Yoruba (`yo`), Thai (`th`).

**Why**: High-traffic NLP languages with significant speaker populations.
Stub specs produce empty tokenizer output, limiting usefulness.

---

## S9 — Add `pip-audit` to CI [Effort: Low]

Add a `.github/workflows/pip-audit.yml` step to scan runtime dependencies for known CVEs.

**Why**: Good security hygiene. Low false-positive rate for stable packages.

---

## S10 — Multi-Version Python Matrix in CI [Effort: Low]

`pyproject.toml` claims support for Python 3.9–3.13. CI only tests 3.10–3.12.
Add 3.13 to the matrix.

**Why**: `numpy` and `langcodes` occasionally have version-specific behavior.

---

## S11 — Context-Aware Tokenizer Trie [Effort: High] (NEW)

The maximal-munch trie in `phonetok.py` causes conflicts for languages where
digraph priorities depend on surrounding context (e.g., Rionorese `en` vs `nh`).
A weighted or context-aware trie would resolve these without requiring per-language
workarounds.

**Why**: Currently affects Rionorese `benhir` tokenization. Could affect other
languages with similar grapheme overlaps.

---

## S12 — Promote Skeleton Specs to Research Quality [Effort: Medium] (NEW)

~222 skeleton-tier specs have minimal grapheme inventories. A systematic promotion
pass (validate against Phoible/WALS, add positional graphemes for high-traffic
languages) would improve data quality for NLP pipelines.

**Priority candidates**: Hindi (`hi`), Russian (`ru`), Polish (`pl`), Czech (`cs`),
Greek (`el`), Turkish (`tr`) — all already have `positional_graphemes` added
(2026-03-19 session).
