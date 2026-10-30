# Sourcing a claim

Every phonological claim in a spec's `sources` array names a source someone
opened and read at the cited page. This page says where to find such a source
and what each kind of source is good for.

## The reachable sources

**Language Science Press** publishes open-access reference grammars and
phonology monographs; the full text sits behind no paywall, so a claim cited
there can be checked by anyone. Search the catalog at
[langsci-press.org](https://langsci-press.org) for the language family before
reaching for anything less direct.

**JIPA Illustrations of the IPA**, the short phoneme-inventory articles the
Journal of the International Phonetic Association runs for individual
languages, are authoritative and concise. Some sit behind Cambridge's
paywall and some are free; check before citing one as read in full, and say
so in the source entry either way.

**University repositories and theses**, indexed through DSpace and similar
platforms, carry dissertations a commercial publisher never picked up. The
Mi'kmaq spec (`mic.json`) cites Fidelholtz's 1968 dissertation on Micmac
phonology at MIT's DSpace, handle `1721.1/13001` — full text, openly
readable, and the actual source of the open-mid vowel values the spec ships.

**archive.org** holds grammars old enough to be out of copyright, scanned in
full. The Mirandese vowel question was settled this way: Leite de
Vasconcelos's *Estudos de Philologia Mirandesa*, volume I, identifier
`estudosdephilolo01vascuoft`, gives the forms directly, in full text, free of
charge.

**PHOIBLE** is good for one thing: phoneme inventories, cross-linguistically
coded and searchable. It says nothing about allophony, orthography, or how a
phoneme surfaces in a particular writing system, so a `phoible_id` answers
"what phonemes does this language have," and nothing past that.

**Glottolog** is a discovery path to references, not a phonological source
in its own right: use it to find what has been published on a language, not
to cite a phonological claim directly. It also has no entry at all for some
varieties this project models, and `glottolog_code: null` is the honest state
for those — not a gap to close by guessing a nearby code.

**Wikipedia and Wiktionary** are pointers, never sources. Follow their
citation to the reference they name, open that reference, and confirm it
actually says what the Wikipedia text claims before citing it — do not cite
Wikipedia's paraphrase, and do not cite an author's name lifted from a
`<ref>` tag without having read that author. A rewrite module such as
`Module:crk-IPA` is a parser someone wrote, encoding its own author's
decisions; its output is not evidence of what a reference grammar says, and
citing the module's behavior in place of a grammar is the same mistake as
citing Wikipedia's paraphrase.

## What counts as sourced

A `pages:` field is a claim that the source was opened at that page and says
what the entry attributes to it. If a page was not checked, leave `pages`
out rather than guess a number a table of contents suggests. The same is
true of a `# ATTESTED` marker on a data table: it says the marked forms were
checked against the source rather than aggregated from it, and if a form was
inferred rather than checked, it is not attested.

Source precedence differs by which side of the engine a claim lands on.
For what the engine emits, a peer-reviewed paper or reference grammar
outranks a native speaker's transcription, because the engine states one
canonical pronunciation and that pronunciation should be the one the
literature backs. For what a parser accepts as input, every attested
variation counts, native-speaker forms included, because acceptance is
about covering real usage, not about picking the one true form.
Mirandese hundreds are the worked example. Vasconcelos records both the
periphrastic `dous cientos` and `duzientos`, and a native speaker calls the
second one a lusismo; the emitted form follows the description, while the
accept-set keeps both, because a parser that rejects a form real speakers use
is broken whatever the grammar prefers.

## Refusing a change is a valid outcome

A change with no source that survives scrutiny does not go in, even when
the alternative measures better on a benchmark. The Mi'kmaq mid-vowel
refusal is the worked example: fitting the vowels to the gold data would
have brought the phoneme error rate for that language down from 0.1114 to
0.0458, and the change was refused anyway, because Fidelholtz's dissertation
gives the open-mid values the spec already ships, and no other source
contradicts it. A lower error rate bought by discarding a checked source is
not an improvement; it is a regression that happens to score well.

---
[← Link audit](link-audit.md) · [Home](index.md) · [Benchmarks →](benchmarks.md)
