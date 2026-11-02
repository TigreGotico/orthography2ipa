# Citation honesty

Every mapping in a spec is a claim about a language, and every claim needs a
source that a reader can open and check. This page says what counts as a
source, how to record one, and which reference data counts as evidence.
[sourcing.md](../sourcing.md) lists where to find sources, and the `sources`
fields are in [`SCHEMA.md`](../../orthography2ipa/data/SCHEMA.md#sources-schema).

## Quote the source you opened

1. Open the source before you cite it. A citation copied from another work's
   bibliography is a claim that you did not check.
2. Record the page in `pages` only when you read that page. If you did not
   check a page, leave `pages` out. Do not take a number from a table of
   contents.
3. Quote the passage that supports the rule in the spec's `notes`, with the
   author, the year and the page, such as "Kirby (2011: 386)".
4. Mark a data table `# ATTESTED` only when you checked each marked form
   against the source. A form you inferred is not attested.
5. Prefer a DOI, then a stable publisher page, as the `doi` or `url`.

A source is a reference grammar, a peer-reviewed paper, a dissertation or a
dataset published by a university or a standards body. Another G2P system's
output is not a source. The `sources` array of every spec above `stub` must
name at least one real work. `tests/test_sources.py` enforces this.

## Wikipedia and Ciberdúvidas are extra sources only

Wikipedia is a reading path into the literature. Put its articles in the
`wikipedia` field, and cite the reference grammar or paper that the article
cites. Keep the Wikipedia link next to it, and do not remove it. A spec whose
only source is Wikipedia fails `tests/test_sources.py`. The specs on its
`_WIKIPEDIA_ONLY_SOURCES_BURNDOWN` list predate that test. The list may only
shrink.

Ciberdúvidas da Língua Portuguesa answers questions about Portuguese usage.
It is an extra source in the same way. Cite the grammar that a Ciberdúvidas
answer quotes, with its page, and give the Ciberdúvidas URL as the reading
path. An answer that quotes no grammar can support a note, but it cannot be
the only source for a rule.

## A cited disagreement with the board is a win

A benchmark number is evidence, never a justification. If a cited rule
lowers a score against a gold set, keep the rule. Gold sets contain errors,
and [gold_defects.md](../gold_defects.md) records the ones that were measured.
If a change has no source that survives a check, refuse it, even when it
scores better. [sourcing.md](../sourcing.md#refusing-a-change-is-a-valid-outcome)
gives a worked example.

## Silver labels are never gold

Some reference sets have no error model. Call these sets silver labels, in
spec notes, in documentation and in pull request text, and never gold:

- Sets that a large language model wrote, such as `mirandese_dict`,
  `barranquenho_dict`, `arabic_tts` and `portuguese_tts`. An audit against the
  literature makes them more reliable, but it does not give them an error
  model.
- Sets that are pinned to this engine's own output. A score near zero on an
  engine-pinned set shows that the output did not change. It does not show
  that the output is correct.
- Sets that another phonemizer produced, such as the `espeak-derived` and
  `epitran-derived` rows. These measure agreement with that tool.

The board records these sets in the `provenance` column as `llm-generated`,
`espeak-derived` or `epitran-derived`. A silver row can never qualify a spec
for the `production` tier, and it can never block one. The tiers are defined
in [benchmarks.md](../benchmarks.md#reliability-tiers).

## Corrections to a gold set

A correction overlay repairs a defect in an upstream gold set and leaves the
upstream file unchanged. A correction may come only from the spelling of the
word or from a citation that you opened. It may never come from the output of
orthography2ipa, because that makes the gold circular. The overlay files and
their rules are in
[`orthography2ipa/data/gold/corrections/README.md`](../../orthography2ipa/data/gold/corrections/README.md),
and [benchmarks.md](../benchmarks.md#corrections-overlays) explains how the
board scores them.

## AI-written specs

Large language models wrote most specs, under the direction of a human
maintainer. A model reads the sources and encodes them as JSON under these
rules. A cited spec that a model wrote is still not a native-speaker
judgment, and the `quality` tier records that. If you speak a language and a
spec is wrong, open an issue with a citation or a native-speaker judgment.
Corrections from speakers have priority over all other work in this
repository.

---
[← Spec authoring rules](spec_authoring.md) · [Home](../index.md) · [Board regeneration →](board.md)
