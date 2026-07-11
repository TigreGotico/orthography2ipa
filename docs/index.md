
# orthography2ipa

Text-to-speech and speech-to-text systems need to know how words *sound*,
not just how they're spelled. `orthography2ipa` answers that question for
350+ languages and dialects: give it a word in its native orthography and
it returns an IPA (International Phonetic Alphabet) transcription.

```python
>>> import orthography2ipa
>>> orthography2ipa.transcribe("olá mundo", "pt")
'oˈla ˈmundu'
>>> orthography2ipa.transcribe("hello world", "en")
'hɛllɒ wɔːɹld'
```

## Why this exists, and why it has no model weights

Most G2P (grapheme-to-phoneme) tools are either narrow — one hand-tuned
rule set bolted onto a specific TTS engine — or heavyweight: a trained
sequence model per language, with all the data-collection and retraining
cost that implies. `orthography2ipa` takes a third path: it is **pure
data**. Every language is a JSON file describing, in linguistically
citable terms, which graphemes (letters, digraphs, trigraphs) map to
which IPA phonemes, and how those phonemes surface as allophones in
context. A small, shared, language-agnostic engine — tokenizer, beam
search, stress marking, sandhi — turns that data into transcriptions.
Adding a language means writing data, not training a model or writing
bespoke code.

That design has a direct consequence worth stating up front: the engine
picks the *statistically most common* pronunciation for an ambiguous
spelling, not the contextually correct one. There is no language model
scoring candidates against neighbouring words — see [Honest
limitations](#honest-limitations-read-this-before-you-trust-a-tier)
before relying on this for anything where mistakes are costly.

## The two maps: graphemes vs. allophones

Every language spec keeps two mappings deliberately separate:

- **Graphemes** — which phonemes a *spelling* can represent. English
  ⟨th⟩ → `['θ', 'ð']` (the "thin" vs. "this" sounds).
- **Allophones** — how a *phoneme* surfaces depending on context. English
  /t/ → `['t', 'tʰ', 'ʔ', 'ɾ']` — aspirated word-initially, glottalised
  before a pause, flapped between vowels (American "butter").

Transcription (text → phonemes) uses the grapheme map. Pronunciation
modelling (phoneme → realistic surface form) uses the allophone map.
Conflating the two is a common source of bugs in G2P systems; keeping
them apart is the first design decision this library makes.

## Install and run your first transcription

```bash
pip install orthography2ipa
```

```python
import orthography2ipa

orthography2ipa.transcribe("olá mundo", "pt")   # 'oˈla ˈmundu'
orthography2ipa.transcribe("bona nuèit", "oc")  # 'ˈbunɔ ˈnyɛjt'

en = orthography2ipa.get("en-GB")
en.graphemes["th"]   # ['θ', 'ð']
en.allophones["t"]   # ['t', 'tʰ', 'ʔ', 'ɾ']
en.name, en.family   # ('British English (RP)', 'Germanic')
```

That is the whole mental model: `transcribe()` for the common case,
`get()` when you want the underlying `LanguageSpec` — grapheme maps,
allophones, ancestry, quality tier, sources — to build something more
specific on top.

## Choose your own adventure

Different readers need different depth. Pick the path that matches what
you are trying to do.

**I want to convert text to IPA in a TTS/ASR pipeline.**
Start with [getting_started.md](getting_started.md) for the full Python
API walkthrough (spec lookup, tokenizer, beam search, distance metrics),
then [tokenizer.md](tokenizer.md) for how candidate ranking actually
works and [quality_tiers.md](quality_tiers.md) to know which languages
are trustworthy enough for production use today.

**I'm a linguist and want to add or improve a language.**
Go straight to [adding_a_language.md](adding_a_language.md) for the
step-by-step JSON spec format, then [linguistic_accuracy.md](linguistic_accuracy.md)
for the sourcing and IPA conventions every spec must follow, and
[data_model.md](data_model.md) for the full `LanguageSpec` field
reference.

**I maintain a downstream engine (Arabic, Portuguese, or similar) and
need the plugin ABCs.**
Read [architecture.md](architecture.md) for how the engine pipeline
(normalize → tokenize → beam search → stress → sandhi → dialect
transform) fits together, then look at `G2PPlugin` in
[registry.md](registry.md) — that is the extension point
[arbtok](https://github.com/TigreGotico/arbtok) and
[tugaphone](https://github.com/TigreGotico/tugaphone) build on.

**I want the ranked pronunciation lattice, or to build a specialised
phonemizer.**
The lattice is the library's headline building block.
[lattice.md](lattice.md) covers the structured `ipa_lattice` (ranked IPA
candidates with `-log P` costs per grapheme), the per-word confidence / OOV
signal, and the `LatticeRescorer` seam — how a downstream engine refines the
shared beam by re-costing candidates instead of forking a tokenizer.

**I want to understand the benchmark and quality-tier system.**
[quality_tiers.md](quality_tiers.md) defines what `stub` → `skeleton` →
`research` → `production` actually require, and
[benchmarks.md](benchmarks.md) plus [scoreboard.md](scoreboard.md) show
the measured PER (phoneme error rate) per language against
human-curated gold data — including the honest, currently mediocre
numbers for several languages.

**I'm doing production-readiness due diligence.**
[api_stability.md](api_stability.md) covers what is a public,
version-guarded surface; [scoreboard.md](scoreboard.md) is the
unfiltered accuracy table; [link-audit.md](link-audit.md) covers
citation URL liveness; the license is Apache 2.0. No language currently
carries the `production` quality tier — see [Honest
limitations](#honest-limitations-read-this-before-you-trust-a-tier)
below.

## Honest limitations (read this before you trust a tier)

- **Candidate ordering is naive.** When a spelling is ambiguous
  (English ⟨th⟩ could be /θ/ or /ð/), the engine ranks candidates by how
  common that mapping is across the language generally — it does not
  look at neighbouring words or meaning. Beam search surfaces the
  alternatives; it does not disambiguate them for you.
- **Some languages have an input contract that is not plain native
  text.** `zh` expects Pinyin romanisation, not Hanzi — converting Hanzi
  to Pinyin (e.g. via a CC-CEDICT-backed dictionary) is a separate step
  this library does not perform; tone marks are not encoded either.
  `ko` expects decomposed jamo (ㄱ, ㅏ, ㄴ…), not composed Hangul
  syllable blocks (가, 는…) — the grapheme map is keyed on individual
  jamo, so a Hangul-decomposition step comes first. Check a language's
  `notes` field
  (`orthography2ipa.get(code).notes`) before assuming raw native-script
  input works end to end.
- **PER (phoneme error rate) is genuinely mediocre for several
  languages**, not only the exotic ones: English sits around 0.48
  against WikiPron gold, Tamil around 0.89, Scottish Gaelic around 0.69.
  See the full, unfiltered [scoreboard.md](scoreboard.md) — reported for
  honesty, not flattery. Every score is reproducible with
  `python scripts/benchmark.py`.
- **The gold data itself is a grain of salt.** Reliable G2P gold barely
  exists, so most benchmark datasets are semi-automated,
  dictionary-extracted, community-scraped, or a phonemizer's own output
  reused as a reference — a low PER against a machine-generated gold means
  "agrees with that tool", not "correct", and an espeak comparison on an
  espeak-derived gold is partly circular. Read PER as directional, not
  precise, and cross-reference each row's bootstrap `95% CI` (small-`N`
  rows are anecdotes). Every dataset's reliability tier is on the
  [scoreboard](scoreboard.md) (`provenance` column); the taxonomy and
  per-dataset evidence are in
  [benchmarks.md](benchmarks.md#provenance-and-reliability-read-this-before-trusting-any-number).
- **No language is at `production` tier yet.** Every registered language
  is at `research` tier or below — it has at least one cited source and
  usually a benchmark, but has not cleared the volume and accuracy bar
  `quality_tiers.md` defines for production use. Check
  `orthography2ipa.get(code).quality` before depending on a language for
  anything where accuracy matters.

## Reference index

| Doc | Covers |
| :--- | :--- |
| [getting_started.md](getting_started.md) | Narrative on-ramp: install → first call → what happened → where next |
| [architecture.md](architecture.md) | Module layout, pipeline stages, design decisions |
| [data_model.md](data_model.md) | `LanguageSpec` and every field it carries |
| [registry.md](registry.md) | Full language registry, code resolution, `G2PPlugin` |
| [tokenizer.md](tokenizer.md) | `PhonetokTokenizer`, maximal-munch tokenization, beam search |
| [lattice.md](lattice.md) | The structured pronunciation lattice: ranked per-position candidates and `-log P` costs |
| [candidate_scoring.md](candidate_scoring.md) | Per-candidate weights and how they become beam costs |
| [distance.md](distance.md) | Phonological distance metrics between languages |
| [architecture.md](architecture.md#script_distancepy) | Typological distance between writing systems (`script_distance.py`) |
| [ancestry.md](ancestry.md) | Dialect lineage: roles, weights, phylogenetic distance |
| [positional_graphemes.md](positional_graphemes.md) | Context-sensitive grapheme overrides |
| [adding_a_language.md](adding_a_language.md) | How to add a new language spec |
| [linguistic_accuracy.md](linguistic_accuracy.md) | Data quality standards and sourcing rules |
| [ipa_reference.md](ipa_reference.md) | IPA symbol reference with Unicode code points |
| [bibliography.md](bibliography.md) | Citation management, `LinguisticSource` |
| [quality_tiers.md](quality_tiers.md) | What `stub`/`skeleton`/`research`/`production` require |
| [benchmarks.md](benchmarks.md) | Gold datasets, methodology, how to reproduce a score |
| [scoreboard.md](scoreboard.md) | Every measured PER/exact-match result |
| [espeak_agreement.md](espeak_agreement.md) | Agreement analysis against espeak-ng |
| [comparison.md](comparison.md) | Cross-system PER comparison vs espeak-ng, epitran, gruut |
| [api_stability.md](api_stability.md) | What is public and version-guarded |
| [link-audit.md](link-audit.md) | Citation URL liveness audit |
| [languages/index.md](languages/index.md) | Per-language phonology deep-dives |
| [explorer.md](explorer.md) | Interactive, self-contained language-data explorer (gh-pages) |

---

**Navigation:** [Getting started](getting_started.md) · [Architecture](architecture.md) · [Languages](languages/index.md) · [Scoreboard](scoreboard.md) · [Benchmarks](benchmarks.md)

*Related: [Architecture](architecture.md) · [Lattice](lattice.md) · [Allophony](allophony.md) · [Quality tiers](quality_tiers.md)*
