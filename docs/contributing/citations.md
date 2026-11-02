# Citation honesty

Every mapping in a spec is a claim about a language, and every claim needs a source that a reader can open and check. This page says what counts as a source, where to find one, how to record it, and which reference data counts as evidence. The `sources` fields are in [`SCHEMA.md`](../../orthography2ipa/data/SCHEMA.md#sources-schema), and the reference works by language family are in [bibliography](../bibliography.md).

## Principles

Primary sources come before secondary sources. Every phonological claim traces back to a peer-reviewed article, a reference grammar or a phonology monograph. Wikipedia, language-learning applications and the output of an AI model are not sources.

A spec describes the standard or prestige variety first. A dialect spec then states how it differs from that standard, and says so in its `notes`.

A small correct list is better than a large wrong one. If you are not sure that an allophone belongs in the list, leave it out.

Every spec carries its bibliography in `sources`. Every mapping that is not obvious carries a line in `notes` that says why. The symbols follow the [IPA reference](../ipa_reference.md).

## Quote the source you opened

1. Open the source before you cite it. A citation copied from the bibliography of another work is a claim that you did not check.

2. Record the page in `pages` only when you read that page. If you did not check a page, leave `pages` out. Do not take a number from a table of contents.

3. Quote the passage that supports the rule in the spec's `notes`, with the author, the year and the page, such as "Kirby (2011: 386)".

4. Mark a data table `# ATTESTED` only when you checked each marked form against the source. A form that you inferred is not attested.

5. Prefer a DOI, then a stable publisher page, as the `doi` or `url`.

A source is a reference grammar, a peer-reviewed paper, a dissertation or a dataset that a university or a standards body publishes. The output of another G2P system is not a source. The `sources` array of every spec above `stub` must name at least one real work, and `tests/test_sources.py` enforces this.

## Where to find a source

These sources are open to every reader, so a claim that cites them can be checked.

| Source | What it is good for | Its limit |
|---|---|---|
| [Language Science Press](https://langsci-press.org) | Open-access reference grammars and phonology monographs, with the full text | Search its catalogue for the language family first |
| JIPA *Illustrations of the IPA* | Short, authoritative phoneme-inventory articles, one per language | Some sit behind the Cambridge paywall. Say in the source entry whether you read it in full |
| University repositories and theses (DSpace and similar) | Dissertations that no commercial publisher took | Quality varies with the thesis |
| [archive.org](https://archive.org) | Full scans of grammars old enough to be out of copyright | The description is as old as the scan |
| PHOIBLE | Phoneme inventories, coded the same way across languages | It says nothing about allophony or orthography |
| Glottolog | A path to the references published on a language | It is not a phonological source of its own |

Two specs show the open sources at work. The Mi'kmaq spec (`mic.json`) cites Fidelholtz's 1968 dissertation on Micmac phonology at MIT's DSpace, handle `1721.1/13001`. The full text is open, and it is the source of the open-mid vowel values that the spec ships. The Mirandese vowel question was settled from archive.org. Leite de Vasconcelos's *Estudos de Philologia Mirandesa*, volume I, identifier `estudosdephilolo01vascuoft`, gives the forms directly and in full text.

A `phoible_id` answers "which phonemes does this language have", and nothing more. A phone inventory never settles which letter spells which phone ([adding a language](../adding_a_language.md#looking-for-a-source-what-a-phone-inventory-cannot-tell-you)). Glottolog has no entry for some of the varieties that this project models. For those, `glottolog_code: null` is the honest state. Do not fill the field with the code of a nearby languoid.

## Wikipedia and Ciberdúvidas are extra sources only

Wikipedia and Wiktionary are pointers, never sources. Put a Wikipedia article in the `wikipedia` field, and cite the reference grammar or paper that the article cites. Open that reference, and make sure it says what the article claims. Do not cite the paraphrase of Wikipedia. Do not cite an author whose name you took from a `<ref>` tag and whose work you did not read. Keep the Wikipedia link next to the citation, and do not remove it.

A Wiktionary rewrite module such as `Module:crk-IPA` is a parser that someone wrote, and it encodes the decisions of its author. Its output is not evidence of what a reference grammar says.

A spec whose only source is Wikipedia fails `tests/test_sources.py`. The specs on its `_WIKIPEDIA_ONLY_SOURCES_BURNDOWN` list fail the rule from before the test existed. The list may only get shorter.

Ciberdúvidas da Língua Portuguesa answers questions about Portuguese usage. It is an extra source in the same way. Cite the grammar that a Ciberdúvidas answer quotes, with its page, and give the Ciberdúvidas URL as the reading path. An answer that quotes no grammar can support a note, but it cannot be the only source for a rule.

## Which source wins

The order of precedence depends on which side of the engine a claim is on. For what the engine emits, a peer-reviewed paper or a reference grammar ranks above the transcription of a native speaker. The engine states one canonical pronunciation, and the literature must support it. For what a parser accepts as input, every attested variant counts, native-speaker forms included. Acceptance covers real usage and does not pick one true form.

Mirandese hundreds are the worked example. Vasconcelos records both the periphrastic `dous cientos` and `duzientos`, and a native speaker calls the second form a lusismo. The emitted form follows the description. The accept-set keeps both, because a parser that rejects a form real speakers use is broken, whatever the grammar prefers.

## A cited disagreement with the board is a win

A benchmark number is evidence, never a justification. If a cited rule makes a score worse against a gold set, keep the rule. Gold sets contain errors, and [gold defects](../gold_defects.md) records the ones that were measured.

## Refusing a change is a valid outcome

A change with no source that survives a check does not go in, even when the alternative scores better on a benchmark. The Mi'kmaq mid vowels are the worked example. A fit of the vowels to the gold data gave a much lower phoneme error rate for that language. The change was refused.

Fidelholtz's dissertation gives the open-mid values that the spec already ships, and no other source contradicts it. A lower error rate bought with the loss of a checked source is not an improvement. It is a regression that happens to score well.

## Silver labels are never gold

Some reference sets have no error model. Call these sets silver labels, never gold, in spec notes, in documentation and in pull request text:

- Sets that a large language model wrote, such as `mirandese_dict`, `barranquenho_dict`, `arabic_tts` and `portuguese_tts`. An audit against the literature makes them more reliable, but it does not give them an error model.

- Sets that are pinned to the output of this engine. A score near zero on an engine-pinned set shows that the output did not change. It does not show that the output is correct.

- Sets that another phonemizer produced, such as the `espeak-derived` and `epitran-derived` rows. These measure agreement with that tool.

The board records these sets in the `provenance` column as `llm-generated`, `espeak-derived` or `epitran-derived`. A silver row can never qualify a spec for the `production` tier, and it can never block one. The tiers are defined in [quality tiers](../quality_tiers.md) and [benchmarks](../benchmarks.md#reliability-tiers).

## Corrections to a gold set

A correction overlay repairs a defect in an upstream gold set and leaves the upstream file unchanged. A correction may come only from the spelling of the word or from a citation that you opened. It may never come from the output of orthography2ipa, because that makes the gold circular. The overlay files and their rules are in [`orthography2ipa/data/gold/corrections/README.md`](../../orthography2ipa/data/gold/corrections/README.md), and [benchmarks](../benchmarks.md#corrections-overlays) explains how the board scores them.

## AI-written specs

Large language models wrote most specs, under the direction of a human maintainer. A model reads the sources and encodes them as JSON under these rules. A cited spec that a model wrote is still not the judgment of a native speaker, and the `quality` tier records that. If you speak a language and a spec is wrong, open an issue with a citation or a native-speaker judgment. Corrections from speakers have priority over all other work in this repository.

---
[← Spec authoring rules](spec_authoring.md) · [Home](../index.md) · [Board regeneration →](board.md)
