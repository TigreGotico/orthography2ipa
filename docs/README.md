# orthography2ipa — Documentation

**[index.md](index.md) is the front door.** It routes you by what you are trying
to do — integrate the engine, add a language, build a downstream phonemizer,
evaluate the library for production — and states the accuracy limits up front.

`orthography2ipa` measures how languages relate to each other across independent
axes (phonological, reading, spelling, script, genealogical, temporal,
geographic), and converts orthography to IPA from the same per-language data:
493 languages plus 63 classification-only clade nodes, all as cited JSON specs
with no trained weights.

```python
import orthography2ipa as o2i
from orthography2ipa.distance import grapheme_divergence, spelling_divergence

o2i.transcribe("olá mundo", "pt")   # 'oˈla ˈmũdu'

gl, glr = o2i.get("gl"), o2i.get("gl-x-reintegrado")
grapheme_divergence(gl, glr).mean_ipa_distance   # 0.0233 — they read alike
spelling_divergence(gl, glr).mean_distance       # 0.0659 — they are written differently
```

## Contents

| Document | Description |
|---|---|
| [Index](index.md) | Front door: what the library is, where to go, honest limitations |
| [Getting Started](getting_started.md) | Install, first call, the API walkthrough |
| [Architecture](architecture.md) | Package structure, pipeline stages, design decisions |
| [Data Model](data_model.md) | `LanguageSpec` and every field it carries |
| [Orthography kind](orthography_kind.md) | Native scripts, romanizations and transliterations |
| [Language Registry](registry.md) | Code resolution, `available_codes`, step plugins |
| [Tokenizer](tokenizer.md) | `PhonetokTokenizer`, maximal munch, beam search |
| [Lattice](lattice.md) | The ranked pronunciation lattice and the `LatticeRescorer` seam |
| [Sentence context](sentence_context.md) | The cross-word seam: `SentenceLattice`, `SentenceRescorer` |
| [Features](features.md) | Feature export for ML / CRF G2P |
| [Candidate scoring](candidate_scoring.md) | Per-candidate weights and how they become beam costs |
| [Distance Metrics](distance.md) | Every relational axis, with its caveats |
| [Ancestry](ancestry.md) | Clade nodes, the derived `family`, ancestor roles, phylogenetic distance |
| [Allophony](allophony.md) | Post-lexical `allophone_rules` |
| [Positional graphemes](positional_graphemes.md) | Context-sensitive grapheme overrides |
| [Adding a Language](adding_a_language.md) | Step-by-step guide to contributing a spec |
| [Linguistic Accuracy](linguistic_accuracy.md) | Sourcing standards and IPA conventions |
| [Quality tiers](quality_tiers.md) | What `stub` / `skeleton` / `research` / `production` require |
| [Benchmarks](benchmarks.md) | Gold datasets, provenance tiers, methodology |
| [Scoreboard](scoreboard.md) | Every measured PER / exact-match result |
| [Comparison](comparison.md) | Cross-system PER vs espeak-ng, epitran, gruut |
| [IPA Reference](ipa_reference.md) | IPA symbols and their feature values |
| [Bibliography](bibliography.md) | Citation management, `LinguisticSource` |
| [API stability](api_stability.md) | What is public and version-guarded |

The authoring reference for a spec JSON file is
[`orthography2ipa/data/SCHEMA.md`](../orthography2ipa/data/SCHEMA.md).
