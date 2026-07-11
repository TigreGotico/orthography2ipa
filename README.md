# orthography2ipa

Text-to-speech and speech-to-text systems need to know how words *sound*,
not just how they're spelled. `orthography2ipa` answers that question for
**350+ language codes** across 20+ language families: give it a word in
its native orthography and get back an IPA transcription.

```python
>>> import orthography2ipa
>>> orthography2ipa.transcribe("olá mundo", "pt")
'oˈla ˈmundu'
```

It's **pure data** — a linguistically-sourced grapheme→IPA map per
language, a maximal-munch IPA tokenizer, and a family of
phonological/script distance metrics, with no trained weights to ship.
Only mappings grounded in official orthography and documented grammar
are included; arbitrary substring rules are excluded.

At its core is a **probabilistic pronunciation lattice**: for any word it
returns the ranked IPA options per grapheme with `-log P` costs, a per-word
confidence signal, and a rescorer seam that specialised phonemizers build on
— see [The pronunciation lattice](#the-pronunciation-lattice) below.

New to the library? Start with **[docs/index.md](docs/index.md)** — it
routes you to the right doc depending on whether you're integrating
this into a pipeline, adding a language, building a downstream engine,
or evaluating it for production use, and it states the known accuracy
limitations up front.

## Why two maps

The central distinction the package enforces:

- A **grapheme map** tells you which phonemes a spelling *can* represent. English ⟨th⟩ → `['θ', 'ð']`.
- An **allophone map** tells you how a phoneme *surfaces* in context. English /t/ → `['t', 'tʰ', 'ʔ', 'ɾ']`.

Keeping these separate lets you go from text to phoneme candidates (transcription) and from phonemes to surface realisations (pronunciation modelling) without conflating the two.

**Both maps are now applied.** The pre-lexical map (orthography→phoneme) is
conditioned by `positional_graphemes`, vowel-class positions and candidate
weights; the post-lexical map (phoneme→surface allophone) is applied by
declarative **`allophone_rules`** — context-conditioned `phoneme → surface`
rewrites keyed on syllable position, stress, word position and neighbouring
segments. They compile into a lattice rescorer run after phoneme selection
and before stress/sandhi. Catalan is the first spec to use them: word-final
obstruent devoicing (`fred` → `[ˈfɾet]`) and nasal place assimilation
(`banc` → `[ˈbaŋk]`). See [`docs/allophony.md`](docs/allophony.md).

## The pronunciation lattice

When a spelling is ambiguous, `orthography2ipa` does not just pick a guess —
it builds a **ranked, cost-annotated pronunciation lattice** for the word,
and that lattice is the feature specialised phonemizers are built to stand
on. For any registered language you get, per grapheme, every IPA option it
can realise and a `-log P` cost ranking them:

```python
from orthography2ipa import get
from orthography2ipa.phonetok import PhonetokTokenizer

tok = PhonetokTokenizer(get("en-GB"))
for slot in tok.ipa_lattice("cough"):
    print(slot.grapheme, [(c.ipa, c.cost) for c in slot.candidates])
    # c    → [('k', 0.0), ('s', 1.0)]
    # ough → [('ɔː', 0.0), ('oʊ', 1.0), ('ʌf', 2.0), ('ɒf', 3.0), …]
```

**It tells you when it is unsure.** A per-word confidence — each slot's
top-1 vs top-2 cost margin folded with grapheme coverage — flags exactly
which words a downstream engine should spend its expensive lexicon or rules
on, and which it can take on trust:

```python
from orthography2ipa import G2P

g = G2P("en-GB")
g.word_confidence("bar")     # 1.0000 — one reading, take it
g.word_confidence("cough")   # 0.6321 — ambiguous, look closer
g.word_confidence("bar你")   # 0.7500 — one OOV grapheme drops coverage to 3/4
```

**A downstream engine can refine the lattice with a rescorer.**
A rule is a `LatticeRescorer`: a pure function over one slot and its context
that re-costs candidates. A candidate wins by being made strictly cheapest.
Here is a complete mini-phonemizer that teaches English ⟨ough⟩ its `/ʌf/`
reading (*rough*, *tough*, *enough*):

```python
from orthography2ipa import get
from orthography2ipa.phonetok import PhonetokTokenizer, Candidate
from orthography2ipa.rescorer import LatticeRescorer

class RoughOugh(LatticeRescorer):
    def rescore(self, slot, context):
        if slot.grapheme != "ough":
            return slot.candidates                    # no-op elsewhere
        others = [c for c in slot.candidates if c.ipa != "ʌf"]
        return [Candidate("ʌf", 0.0)] + [Candidate(c.ipa, c.cost + 1.0)
                                         for c in others]

tok = PhonetokTokenizer(get("en-GB"))
tok.ipa_best("tough")                        # 'tɔː'  — generic beam
tok.ipa_best("tough", rescorer=RoughOugh())  # 'tʌf'  — refined
```

The beam is the **universal fallback**: it produces a defensible
transcription for every word in every registered language. Refining it with a
rescorer is one of two supported ways to build a specialised engine on this
library; keeping a bespoke tokenizer is the other. Which fits depends on the
shape of your rules — a rescorer suits context-conditioned choices among the
candidates the shared trie already offers, while cross-word context, a
non-IPA generation model, or data that diverges sharply from the base spec
favour a fork. [arbtok](https://github.com/TigreGotico/arbtok),
[tugaphone](https://github.com/TigreGotico/tugaphone),
[g2p_barranquenho](https://github.com/TigreGotico/g2p_barranquenho) and
[mwl_phonemizer](https://github.com/TigreGotico/mwl_phonemizer) build on this
library; see
[Refine or fork?](docs/lattice.md#refine-the-lattice-or-fork-the-tokenizer)
for the trade-offs and the hybrid most engines settle on.

**Powers ML G2P too: pure-data linguistic features for your CRF/neural model.**
Because `orthography2ipa` ships no trained weights, it is a clean *feature
provider*. `G2P.features(text)` is a pure read that exposes, per grapheme, the
phonological-class predicates, word-local neighbours, the ranked `(ipa, cost)`
candidate lattice, and the confidence signal as flat, JSON-able feature dicts —
so a CRF trains on linguistically-grounded features and plugs back in as a
`LatticeRescorer` over the shared lattice, spending its learned capacity where
confidence says the base engine is unsure. See
[Features for ML / CRF G2P](docs/features.md).

## What each language carries

Every `LanguageSpec` provides:

1. **Graphemes** — orthographic units (characters, digraphs, trigraphs) mapped to canonical IPA phonemes.
2. **Allophones** — each phoneme mapped to its positional/contextual surface realisations.
3. **Positional graphemes** — context-sensitive overrides (word-initial, intervocalic, before /i/, …).
4. **Ancestry** — weighted multi-ancestor lineage (parent, substrate, superstrate, adstrate, …) for dialect trees.
5. **Sandhi rules** — cross-word phonological processes.
6. **Allophone rules** — post-lexical `phoneme → surface` rewrites (final devoicing, assimilation, reduction, flapping) applied in context.
7. **Tone inventory** — tone marks → labels, where applicable.
7. **Provenance** — `QualityTier` (stub → skeleton → research → production), `ScriptType`, and bibliographic sources.

Regional varieties get their own `LanguageSpec` objects linked through ancestry, and JSON data files support `graphemes_base`/`allophones_base` inheritance so a dialect only declares what differs from its parent.

## Installation

```bash
pip install orthography2ipa
```

For richer language-specific pipelines, install a downstream engine
built on this library: [arbtok](https://github.com/TigreGotico/arbtok)
for Arabic, [tugaphone](https://github.com/TigreGotico/tugaphone) for
Portuguese.

## Quick start

### Transcribe text to IPA

```python
import orthography2ipa

orthography2ipa.transcribe("olá mundo", "pt")        # 'oˈla ˈmundu'
orthography2ipa.transcribe("hello world", "en")       # 'hɛllɒ wɔːɹld'
orthography2ipa.transcribe("bona nuèit", "oc")        # 'ˈbunɔ ˈnyɛjt'

# Beam search keeps ranked alternatives per word
from orthography2ipa import G2P

engine = G2P("pt-PT")
result = engine.transcribe_detailed("um café", search="beam", beam_width=4)
result.ipa                          # 'ˈum kɐˈfɛ'
result.words[1].candidates          # ranked IPAPath alternatives

# The engine pipeline: normalize → tokenize → greedy/beam per word →
# stress marks (when the spec declares stress rules) → sandhi →
# dialect transform. Downstream engines (arbtok for Arabic, tugaphone
# for Portuguese) build on this library for richer language-specific
# pipelines.
```

### Language specs

```python
import orthography2ipa

# Get a language spec
en = orthography2ipa.get("en-GB")

# Grapheme → IPA candidates
en.graphemes["th"]    # ['θ', 'ð']

# Allophone map: how /t/ surfaces
en.allophones["t"]    # ['t', 'tʰ', 'ʔ', 'ɾ']

# Metadata
en.name               # 'British English (RP)'
en.family             # 'Indo-European > Germanic > West Germanic'
en.script             # 'Latin'

# Regional variants share ancestry but diverge where pronunciation does
pt_br = orthography2ipa.get("pt-BR")
pt_br.graphemes["t"]  # ['t', 't͡ʃ']   — palatalisation before /i/

# Bare tags, ISO 639-3 aliases and near matches all resolve
orthography2ipa.get("eng").name   # 'British English (RP)'
orthography2ipa.resolve("pt")     # 'pt-PT' — reference variety
orthography2ipa.resolve("en-NZ")  # 'en-GB' — nearest registered

# Discover what's available
orthography2ipa.available_codes()
orthography2ipa.available_families()
```

### IPA tokenizer

`PhonetokTokenizer` performs maximal-munch grapheme tokenization with beam-search IPA expansion, ranking candidate transcriptions when a spelling is ambiguous:

```python
from orthography2ipa import get
from orthography2ipa.phonetok import PhonetokTokenizer

tok = PhonetokTokenizer(get("en-GB"))

tok.ipa_best("through")              # 'θɹɔː'
for path in tok.ipa_beam("through", beam_width=8):
    print(path.ipa, path.score)      # θɹɔː 0.0, ðɹɔː 1.0, θɹoʊ 1.0, …
```

For a *structured* view — the ranked IPA options for each grapheme, with
`-log P` costs, rather than flattened path strings — use the pronunciation
lattice. Each `SegmentSlot` carries a grapheme, its span, and ranked
`Candidate(ipa, cost)` options; concatenating each slot's top candidate
reproduces `ipa_best` with its default arguments:

```python
for slot in tok.ipa_lattice("cough"):
    print(slot.grapheme, [(c.ipa, c.cost) for c in slot.candidates])
    # ough → [('ɔː', 0.0), ('oʊ', 1.0), ('ʌf', 2.0), ('ɒf', 3.0), …]
```

See [docs/lattice.md](docs/lattice.md) for the full story.

### Distance metrics

Compare two languages across inventory, grapheme, allophone, and ancestry dimensions:

```python
from orthography2ipa import get
from orthography2ipa.distance import phonological_distance

d = phonological_distance(get("pt-BR"), get("pt-PT"))
d.combined                    # 0.04 — near-identical
d.inventory.feature_mean      # phoneme-inventory distance
d.grapheme.mean_ipa_distance  # grapheme-mapping divergence
d.allophone_sim               # allophone-overlap similarity
```

Script-level distance and feature vectors are available via `script_distance.py` and `feats.py`.

## Command-line interface

After installation the `orthography2ipa` command is available. Every subcommand accepts `--json` for machine-readable output.

```bash
# List languages and families
orthography2ipa list
orthography2ipa list --families
orthography2ipa list --family Romance          # any step of the path matches
orthography2ipa list --family Ibero-Romance   # ... including the sub-branch

# Inspect a language
orthography2ipa info pt-BR
orthography2ipa info pt-BR --graphemes
orthography2ipa info pt-BR --json

# Transcribe text to IPA
orthography2ipa transcribe pt "olá mundo"
orthography2ipa transcribe en-GB "through" --search beam --beam-width 8

# Phonological distance between two languages
orthography2ipa distance pt-BR pt-PT
orthography2ipa distance es-ES it-IT --json
```

## Languages

| Family     | Examples |
|------------|----------|
| Romance    | `pt-PT`, `pt-BR`, `es-ES`, `es-AR`, `ca`, `fr-FR`, `it-IT`, `ro-RO`, `gl`, `oc`, `sc`, `an` |
| Germanic   | `en-GB`, `de-DE`, `nl-NL`, `sv-SE`, `da-DK`, `no-NO`, `af` |
| Slavic     | `ru-RU`, `uk-UA`, `pl-PL`, `cs-CZ`, `sr-RS`, `hr-HR`, `bg-BG` |
| Celtic     | `cy`, `ga`, `gd`, `br`, `kw`, `gv` |
| Indo-Aryan | `hi-IN`, `bn-BD`, `ur-PK`, `ne-NP`, `pa`, `gu`, `mr` |
| Semitic    | `arb`, `he-IL`, `mt` |
| Turkic     | `tr-TR`, `az`, `kk`, `uz` |
| Hellenic   | `el-GR` |
| Uralic     | `fi-FI`, `hu-HU`, `et-EE` |
| Japonic    | `ja` |
| Sinitic    | `zh` |
| Koreanic   | `ko` |

350+ codes across 40+ family groupings, including reconstructed proto-languages and fine-grained regional dialects.

## Data structure

The core shape of every `LanguageSpec` — the fields you'll reach for
day to day; the full field list (provenance, tone, timespan, stress
rules, lexical exceptions, and more) is in
[docs/data_model.md](docs/data_model.md):

```python
@dataclass(frozen=True)
class LanguageSpec:
    code: str                              # 'pt-BR'
    name: str                              # 'Brazilian Portuguese'
    family: str                            # 'Indo-European > Romance > Ibero-Romance'
    script: str                            # 'Latin'
    graphemes: Dict[str, List[str]]        # 'th' → ['θ', 'ð']
    allophones: Dict[str, List[str]]       # 't' → ['t', 'tʰ', 'ʔ', 'ɾ']
    positional_graphemes: Dict[...]        # context-sensitive overrides
    parent: Optional[str]                  # primary parent code
    ancestors: Tuple[Ancestor, ...]        # weighted multi-ancestor lineage
    quality: QualityTier                   # stub | skeleton | research | production
    script_type: ScriptType                # alphabet | abjad | abugida | ...
    sandhi_rules: Tuple[SandhiRule, ...]   # cross-word rules
    sources: Tuple[LinguisticSource, ...]  # bibliographic references
    # ...plus tone_inventory, stress, word_exceptions, timespan, and
    # bibliographic/identifier fields — see docs/data_model.md
```

When a spec declares graphemes but no explicit allophone map, a baseline identity allophone map is derived: every phoneme a grapheme can produce is, at minimum, its own surface realisation.

## Design principles

- **Linguistically motivated only** — digraphs like English ⟨th⟩, Portuguese ⟨lh⟩, or German ⟨sch⟩ are included because they are standard orthographic units; arbitrary substrings are not.
- **Graphemes ≠ allophones** — spelling-to-phoneme and phoneme-to-surface are modelled separately.
- **Regional variants** — where pronunciation diverges systematically, a separate `LanguageSpec` is provided with ancestry links.
- **Multi-ancestor inheritance** — `graphemes_base`/`allophones_base` let dialect trees declare only their differences.
- **Pure data, self-contained logic** — mappings are declarative JSON; the engine never loads external G2P implementations.

## Building engines on top

`G2PPlugin` and `WordContext` are exported as the base types for richer language-specific engines built **on** this library — [arbtok](https://github.com/TigreGotico/arbtok) (Arabic: contextual rule cascade + tashkeel diacritization) and [tugaphone](https://github.com/TigreGotico/tugaphone) (Portuguese: lexicon, POS and regional-accent layers). They consume the spec data, tokenizer and stress machinery and own their own pipelines. Whether such an engine expresses its rules as rescorers over the shared lattice or keeps a bespoke tokenizer is a design choice covered in [Refine or fork?](docs/lattice.md#refine-the-lattice-or-fork-the-tokenizer).

Component plugins that slot into the bundled engine's own logic use dedicated entry-point groups: per-language syllabifiers register under `orthography2ipa.syllabify` (e.g. `silabificador` for Portuguese) and are honoured by stress detection automatically.

## Benchmarks

The engine is evaluated against the best gold sets available — the
Portal da Língua Portuguesa lexicon (via
[tugalex](https://github.com/TigreGotico/tugalex)), WikiPron, CMUdict,
the Mirandese gold set and others. **Take every number with a grain of
salt:** reliable G2P gold barely exists, so most datasets here are
semi-automated, dictionary-extracted, community-scraped, or a
phonemizer's own output reused as a reference — read PER as
**directional/relative, not precise**, and note that a low PER against a
machine-generated gold means "agrees with that tool", not "correct".
Every dataset is classified by reliability tier (surfaced as a
`provenance` column on the [scoreboard](docs/scoreboard.md)); the tiers,
per-dataset evidence, sources and methodology live in
[docs/benchmarks.md](docs/benchmarks.md). Reproduce any row with
`python scripts/benchmark.py`.

Candidate ordering defaults to rank order (list the most common
pronunciation first). A spec can now attach per-candidate **weights**
(candidate frequencies from cited corpora) so the beam favours the
corpus-dominant phoneme and a path's score becomes a real
log-probability — see [candidate scoring](docs/candidate_scoring.md);
**en-GB** is the first spec to use them (`er`, `gh`, `ie`), and any spec
without weights behaves exactly as before. Contextual (positional)
scoring is still limited, no language is currently at `production`
quality tier, and PER is genuinely mediocre for several languages — see
[docs/index.md](docs/index.md#honest-limitations-read-this-before-you-trust-a-tier)
for the specifics before depending on this for anything accuracy-sensitive.

### Comparison to other G2P systems

`scripts/compare_systems.py` runs the same gold rows above through
orthography2ipa, espeak-ng, epitran and gruut with identical
normalization and scoring, and commits the result to
[docs/comparison.md](docs/comparison.md)
([benchmarks/comparison.json](benchmarks/comparison.json) for the
machine-readable form). It is an honest table: some languages win
against espeak-ng, some lose, and coverage against epitran/gruut is
partial by nature of those projects' own language lists. No row is
cherry-picked.

## Contributing

To add a language, create `orthography2ipa/data/{code}.json` following `orthography2ipa/data/SCHEMA.md`. For dialects, use `graphemes_base`/`allophones_base` to inherit from the parent.

## License

Apache 2.0
