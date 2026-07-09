# Quality tiers

`orthography2ipa.types.QualityTier` classifies the data maturity of a
language spec. Every spec JSON declares its tier explicitly (guarded by
[`tests/test_data_quality.py`](../tests/test_data_quality.py)). This
page defines the measurable criteria a spec must meet for each tier, so
that a tier claim is verifiable against the repository rather than a
subjective label.

## `stub`

- Placeholder entry: `code`, `name`, `family`, `script` are populated.
- `graphemes` and `allophones` may be empty.
- No gold benchmark required.
- Reserved for languages the library has not yet started encoding, or
  extinct languages with metadata-only entries (see
  `test_non_stub_resolves_to_content`).

## `skeleton`

- Non-empty `graphemes` inventory (and therefore a non-empty derived or
  explicit `allophones` map — see `LanguageSpec.__post_init__`).
- Passes every guard in `tests/test_data_quality.py`, in particular
  `test_non_stub_resolves_to_content` (non-extinct languages above stub
  must resolve to usable grapheme and allophone data).
- No positional grapheme rules or stress rules required.
- No gold benchmark required.

## `research`

All `skeleton` criteria, plus:

- At least one entry in `sources` (cited phonological reference).
- A `stress` block when the language has lexical/predictable word
  stress (languages without lexical stress, or whose stress is
  unencoded because it is not orthography-predictable, are exempt —
  document the exemption in the spec's `notes`).
- A gold benchmark registered for at least one of the spec's language
  tags in `scripts/benchmark.py`'s `DATASETS` registry, with a PER
  recorded for it in [`benchmarks/results.json`](../benchmarks/results.json).

## `production`

All `research` criteria, plus:

- The registered gold has **at least 500 evaluated entries** (`n` in
  `benchmarks/results.json`) for at least one dataset/language row.
- PER at or below a documented per-language threshold:
  - **≤ 0.15** for shallow/phonemic orthographies — orthographies where
    grapheme-to-phoneme correspondence is largely regular (e.g.
    Spanish, Finnish, Esperanto). A rule-driven engine should approach
    near-perfect accuracy on these; a higher PER signals a spec gap,
    not an inherent orthographic limit.
  - **≤ 0.25** for deep orthographies — orthographies with significant
    historical, morphophonemic, or dialectal irregularity (e.g.
    English, French, Portuguese, Danish). The threshold is looser
    because even human-curated gold sets disagree on regional/optional
    variants at this rate; PER above it means the engine is missing
    encodable rules, not just irregularity noise.
  - The applicable threshold and the shallow/deep classification for
    the language must be stated in its `docs/languages/` page (see
    below); silence defaults to the deep-orthography threshold.
- A per-language documentation page exists under
  [`docs/languages/`](languages/) covering the spec's phonology,
  sources, and known limitations.
- Any known engine-limit exceptions (documented cases the current
  transcription engine cannot resolve, e.g. the positional-trie or
  hyphen-boundary-stress gaps noted in `AGENTS.md`) are listed on that
  page rather than silently lowering the measured PER's meaning.

## Guard test

[`tests/test_data_quality.py`](../tests/test_data_quality.py) asserts
that any spec whose `quality` field is `production` has a corresponding
row in `benchmarks/results.json` meeting the tier's threshold (`n` ≥
500 and `per` ≤ the documented threshold for that language). No spec is
currently at `production` tier, so the guard is presently vacuous —
promoting a spec to `production` is a test-gated act: the benchmark row
must exist and pass before the tier claim is legitimate.
