# Public API stability

This page defines the stable public API surface of `orthography2ipa`: the
symbols that downstream consumers import today, and the deprecation
guarantee that covers them.

## Method

The inventory below was built by grepping every downstream repo checked out
under the `ml` cluster (`arbtok`, `tugaphone`, `g2p_barranquenho`,
`mwl_phonemizer`, `phonematcher`, `sotaque_forcado`) for
`from orthography2ipa` / `import orthography2ipa` statements, across both
library and test code. `phonematcher` and `sotaque_forcado` have no such
imports in their checked-out state.

## Stability commitment

Every symbol listed in the table below is covered by the project's
deprecation convention: a symbol is never renamed or removed outright.
Renaming or removal follows the semver + conventional-commits flow —
announced as a breaking change (`feat!:` / `BREAKING CHANGE:`), superseded
by a documented replacement, and only actually removed once the major
version advances past the one in which the deprecation was announced. The
target removal version is always derived dynamically from
`orthography2ipa/version.py` (`VERSION_MAJOR + 1`) at deprecation time,
never hardcoded into a comment or doc.

## Imported by downstream repos

| Symbol | Source module | Used by |
| --- | --- | --- |
| `G2PPlugin` | `orthography2ipa.g2p_plugin` | arbtok, tugaphone, g2p_barranquenho, mwl_phonemizer |
| `WordContext` | `orthography2ipa.g2p_plugin` | arbtok, tugaphone, g2p_barranquenho, mwl_phonemizer |
| `SyllabifierPlugin` | `orthography2ipa.syllabifier_plugin` | tugaphone |
| `get` | `orthography2ipa` (top-level) | tugaphone, g2p_barranquenho, mwl_phonemizer, arbtok |
| `get_syllabifier` | `orthography2ipa` (top-level) | tugaphone |
| `detect_stress` | `orthography2ipa.stress` | tugaphone |
| `registry` (module) | `orthography2ipa.registry` | tugaphone |

Notes on the table:
- `get` and `get_syllabifier` are consumed both via `import orthography2ipa`
  + attribute access (`orthography2ipa.get(...)`) and via `from
  orthography2ipa import get`. Both call paths route through the same
  `orthography2ipa/__init__.py` re-export and `orthography2ipa/registry.py`
  implementation, so both forms are covered.
- `G2PPlugin` and `WordContext` are the shared contract every downstream
  G2P plugin (arbtok, tugaphone, g2p_barranquenho, mwl_phonemizer)
  subclasses/consumes to implement its own language plugin. A downstream
  plugin's **phonological rule cascade** (sun-letter assimilation,
  silent-`e`, reduction) belongs in a `LatticeRescorer` over the shared
  lattice — see [Rescoring the lattice](lattice.md#rescoring-the-lattice) —
  rather than in a forked tokenizer.
- `SyllabifierPlugin` is the equivalent contract for syllabifier plugins;
  currently only tugaphone implements one.
- `tugaphone`'s test suite imports `orthography2ipa.registry` as a module
  and `orthography2ipa.stress.detect_stress` directly, in addition to the
  top-level re-exports — both paths are stable per `orthography2ipa/__init__.py`.

## Internal — not covered by this guarantee

Everything else exported from `orthography2ipa/__init__.py` is public-facing
(importable, part of `__all__`) but has no observed downstream consumer in
the repos audited above. These names may be reshaped more freely; treat any
reliance on them from outside this repo as unsupported until a downstream
consumer is added to the inventory above:

- `transcribe`, `G2P`, `TranscriptionResult`, `WordTranscription`,
  `ConfidenceBreakdown` (`orthography2ipa.g2p`)
- `UnmappedScriptError` (`orthography2ipa.exceptions`)
- `resolve`, `available_codes`, `available_families` (`orthography2ipa.registry`)
- `load_lexicon` (`orthography2ipa.json_loader`)
- `SandhiEngine` (`orthography2ipa.sandhi`)
- `LanguageSpec`, `Grapheme2IPA`, `AllophoneMap`, `Ancestor`, `AncestorRole`,
  `PositionalGrapheme2IPA`, `QualityTier`, `ScriptType`, `SandhiRule`,
  `StressRules` (`orthography2ipa.types`)
- `apply_stress_mark`, `syllabify` (`orthography2ipa.stress`)
- `ScriptFeatures`, `SCRIPT_REGISTRY`, `script_distance`,
  `script_distance_by_name` (`orthography2ipa.script_distance`)
- `PhonetokTokenizer`, `Token`, `TokenKind`, `IPAPath`, `Candidate`,
  `SegmentSlot`, `GraphemeContext`, `TokenSequence`, `slot_confidence`,
  `lattice_confidence` (`orthography2ipa.phonetok`)
- `segment_distance`, `inventory_distance`, `grapheme_divergence`,
  `allophone_overlap`, `phonological_distance`, `ancestry_similarity`,
  `full_distance`, `pairwise_distances`, `feature_vector`,
  `InventoryDistance`, `GraphemeDivergence`, `PhonologicalDistance`
  (`orthography2ipa.distance`)
- `apply_transform`, `debias_lisbon`, `available_profiles`,
  `DIALECT_PROFILES`, `DialectTransform`, `IPARule`, `IPAChainShift`,
  `IPALexicalRule`, `load_clup_profile` (`orthography2ipa.transforms`)

## Unmapped-character observability (additive)

`G2P` and `WordTranscription` (`orthography2ipa.g2p`) expose optional,
additive surface for detecting words that contain characters absent from a
spec's grapheme table — e.g. feeding a script the spec doesn't cover at all.
Without it, such words would produce an empty `ipa` string
indistinguishable from legitimate silence (a pure-punctuation word); this
surface makes the distinction observable.

- `WordTranscription.unmapped: Tuple[str, ...] = ()` — the specific
  characters in `WordTranscription.word` with no grapheme mapping. Empty
  when every character mapped.
- `WordTranscription.coverage: float = 1.0` — fraction of the word's
  characters that mapped to a grapheme, in `[0.0, 1.0]`.
- `G2P(..., on_unmapped: str = "ignore")` — `"ignore"` (default, zero
  behavior change: `ipa` output is unaffected), `"log"` (same output, plus
  one `logging.warning` per distinct `(lang, word)` pair), or `"raise"`
  (raises `UnmappedScriptError` instead of returning a result for that
  word).

The default (`on_unmapped="ignore"`) reproduces the exact prior behavior —
callers that never pass `on_unmapped` and never read the new
`WordTranscription` fields see no change in `transcribe()` /
`transcribe_detailed()` output.

## Per-word confidence / OOV signal (additive)

`G2P` and `WordTranscription` (`orthography2ipa.g2p`) expose an optional,
additive per-word **confidence** — a pure, deterministic read off the
pronunciation lattice (Workstream B5) so a downstream specialized phonemizer
can spend its lexicon/rules only where the base engine is unsure. It changes
no existing output: `transcribe`, `transcribe_detailed().ipa`, `ipa_best`,
and the scoreboard are byte-identical whether or not it is read.

- `WordTranscription.confidence: float = 1.0` — confidence that `ipa` is the
  right pronunciation, in `[0.0, 1.0]`. The `[0, 1]`-normalised weakest-link
  of the per-slot top-1/top-2 `cost` margin, each slot's winner rarity, and
  the word's `coverage`. `1.0` is the neutral default for a
  `WordTranscription` constructed without the lattice.
- `G2P.word_confidence(word, *, beam_width=8) -> float` — the same number for
  a single word.
- `G2P.confidence_breakdown(word, *, beam_width=8) -> ConfidenceBreakdown` —
  the per-signal detail (`value`, `lattice`, `per_slot`, `coverage`,
  `unmapped`).
- `ConfidenceBreakdown` (`orthography2ipa.g2p`, re-exported from
  `orthography2ipa`) — the frozen breakdown dataclass.

The exact formula is documented in [`lattice.md`](lattice.md). This surface
is versioned as part of the stable import surface below; a plain
`WordTranscription(word=..., ipa=...)` keeps `confidence == 1.0`, so existing
callers are unaffected.

## Sentence-context seam (additive)

`G2P` (`orthography2ipa.g2p`) and the `orthography2ipa.sentence` module expose
an optional, additive **cross-word** surface (Workstream C4) so a downstream
engine can consume a shared sentence orchestrator instead of forking one. It
changes no existing output: `transcribe`, `transcribe_detailed().ipa`, and the
scoreboard are byte-identical whether or not it is used, because the seam only
runs when a caller passes `sentence_rescorer=`.

- `G2P(..., sentence_rescorer=None)` — accepts a `SentenceRescorer`, an
  iterable of them, or `None` (the default, byte-identical path). Rescorers run
  before the spec's declarative `sandhi_rules`, which are unchanged.
- `G2P.sentence_lattice(text, *, search="greedy", beam_width=8) -> SentenceLattice`
  — a pure read exposing every word's lattice, IPA, and phrase / utterance
  position in order; never affects `transcribe`.
- `SentenceLattice`, `WordSlot`, `Position` (an `Enum`),
  `SentenceRescorer` (ABC), `SentenceRescoreContext`
  (`orthography2ipa.sentence`, re-exported from `orthography2ipa`) — the shape a
  cross-word rule reads and rewrites. `WordSlot.slots` is the word's
  `SegmentSlot` lattice; `WordSlot.initial_slot` / `final_slot` are its edge
  candidates; `SentenceRescoreContext.prev_word` / `next_word` and the
  `phrase_position` / `utterance_position` fields give cross-word adjacency and
  position.

These symbols join the stable, version-guarded import surface: they are never
renamed or removed outright, only via the semver + conventional-commits
deprecation flow, with the removal version derived dynamically from
`orthography2ipa/version.py` (`VERSION_MAJOR + 1`). There is no new
`LanguageSpec` field — cross-word rules are caller-supplied plugin objects, so
the spec data surface and its `FIELD_INHERITANCE` manifest are unchanged. The
full seam is documented in [`sentence_context.md`](sentence_context.md). A
caller that never passes `sentence_rescorer=` and never calls `sentence_lattice`
sees no change.

This is a documentation-only audit: it records the current import surface
and stability commitment, and does not rename, deprecate, or otherwise
modify any code in `orthography2ipa`.

---

**Navigation:** [Docs home](index.md) · [Getting started](getting_started.md) · [Architecture](architecture.md) · [Languages](languages/index.md) · [Scoreboard](scoreboard.md)

*Related: [Architecture](architecture.md) · [Lattice](lattice.md) · [Data model](data_model.md)*
