# Roadmap — orthography2ipa

A pure-data, linguistically-grounded grapheme→IPA and allophone resource for 350+
language codes across 20+ families: a maximal-munch IPA tokenizer, phonological /
script distance metrics, weighted multi-ancestor dialect lineage, and a pluggable
G2P backend. The central distinction it enforces: a **grapheme map** (which phonemes
a spelling *can* be) vs an **allophone map** (how a phoneme *surfaces* in context).
It is the **data/feature core** the rest of the phonetics stack should build on.

## Phase 0 — Hardening ✅ (done)

CI on `OpenVoiceOS/gh-automations@dev`; pyproject-only packaging; **pydantic v2
validation of all 356 specs** (`extra='forbid'`) with a `validate` CLI and a
parametrized test; a conservative link audit (`docs/link-audit.md`) that removed
verified-dead URLs; the full suite green (~13.4k tests). Production-ready (PR #16).

## Phase 1 — Correctness & coverage

- Implement the stubbed **Arabic ONNX diacritizer** in `plugins/tashkeel.py`
  (`# TODO: Load and run ONNX model`) using the shared HF cache; until then keep the
  documented graceful-fallback stub.
- Raise specs up the **`QualityTier` ladder** (stub → skeleton → research →
  production): prioritize the languages with real downstream use (Lusophone +
  partnership targets — Frisian, Asturian, Aragonese).
- Keep the link audit current; resolve the audit's "kept for review" items (sole-
  Wikipedia links on non-stub languages; the `cop.wikipedia` DNS case).

## Phase 2 — Be the shared phonetics core

- Expose an `orthography2ipa` **phonemizer backend for `phoonnx`** so synthesis can
  consume its IPA directly.
- Let rule-based, single-language phonemizers be expressed **as `LanguageSpec`s on
  this engine** rather than bespoke code — **mwl_phonemizer** (Mirandese) and
  **g2p_barranquenho** (a pt/es contact dialect → multi-ancestor lineage) are the
  first candidates; **sotaque_forcado**'s phoneme-level mode should reuse the
  allophone/dialect-transform model.
- Have **phonematcher** share this package's feature model (`distance.py`/`feats.py`)
  so retrieval and G2P measure phones in one feature space.
- Reconcile **tugaphone**'s pt `LanguageSpec` with this package's pt data (tugaphone
  keeps its lexicon/POS/number layers on top; the base rules agree).
- Caveat: only adopt the generic engine where it matches a hand-tuned ruleset's
  quality; otherwise keep the language's rules as its spec data.

## Phase 3 — Datasets & publishing

- Publish G2P datasets / reference lexicons derived from the specs (HF).
- Grow the spec library and add a quality-tier coverage view so gaps are visible.
