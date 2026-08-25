# Ancient Egyptian (egy): the Egyptological reading convention

**Code**: `egy` | **Family**: Afro-Asiatic > Egyptian | **Script**: Egyptological transliteration (Latin with diacritics)
**Quality tier**: research | **Descendant**: Coptic (`cop`), via Demotic
**Sources read**: Wiktionary, *Appendix:Egyptian pronunciation* — the published statement of the convention: the letter values, the epenthesis constraint, the one-consonant words, the ⟨w⟩ split and the ⟨ꜥnḫ⟩ exception. Also *Wiktionary:About Egyptian*, which names Schenkel's *Tübinger Einführung in die klassisch-ägyptische Sprache und Schrift* (1991) as the source of the convention, with reference to Peust (1999); neither book was consulted here. Loprieno (1995) and Allen (2013) are cited for the reconstruction this spec does not encode.

## Input contract

The spec reads Egyptological **transliteration** — the Latin-with-diacritics
rendering of the hieroglyphs (⟨nfr⟩, ⟨bḥdt⟩, ⟨ꜥnḫ⟩) that dictionaries,
corpora and gold sets use as the citation form of an Egyptian word.
Hieroglyphs themselves are not modelled; transliterate first. The letters are
ꜣ ꜥ b p f m n r h ḥ ḫ ẖ z s š q k g t ṯ d ḏ j y w — a consonantal skeleton,
because the script writes no vowels at all.

## What the IPA means here

The output is the **Egyptological pronunciation**: the conventional way
Egyptologists read the words aloud, not a claim about how Egyptian was spoken.
The convention reads the weak consonants ꜣ ꜥ j y w as vowels and supplies a
fixed ⟨e⟩ [ɛ] where the script leaves a consonant string unvocalised, which is
why ⟨nfr⟩ is read *nefer* and ⟨bḥdt⟩ *behdet*.

The reconstructed phonology is a different object and is out of reach for an
orthography→IPA map. Reconstructions read ꜣ as a rhotic or a glottal, ꜥ as a
pharyngeal, ṯ and ḏ as palatals, and they supply vowels that the writing system
never recorded — vowels that also differ between Old, Middle and Late Egyptian.
Nothing in the spec asserts any of that.

## Hallmark correspondences

| Letter | IPA | Note |
|:--|:--|:--|
| ꜣ | ɑ | weak consonant, read as a vowel |
| ꜥ | ɑː | weak consonant, read as a long vowel |
| j | i | weak consonant, read as a vowel |
| y | iː | |
| w | w / uː | the Appendix gives [uː] generally and [w] ROOT-initially; root boundaries are not in the letter string, so the spec approximates with word-initial |
| ḥ, h | h | the convention merges them |
| ḫ | x | |
| ẖ | ç | |
| š | ʃ | |
| ṯ | t͡ʃ | |
| ḏ | d͡ʒ | |
| q | k | |
| z | z | |

## The conventional vowel

The Appendix states the vowel as a **constraint** rather than a placement
recipe: /ɛ/ is inserted as needed to break up consonant clusters, so that no
more than one consonant in a row starts or ends each word, and no more than two
consonants appear sequentially within it. Three rules implement the three
clauses, all stated in the rule layer as insertions rather than rewrites:

- a word-initial consonant followed by another consonant takes the vowel, so
  one consonant starts the word — ⟨nfr⟩ [nɛfɛr], ⟨bḥdt⟩ [bɛhdɛt];
- the third consonant of a word-initial run takes one, so no more than two
  consonants run together — ⟨mnmnt⟩ [mɛnmɛnɛt], ⟨nḫbḫb⟩ [nɛxbɛxɛb];
- the consonant before a word-final consonant takes one, so one consonant ends
  the word — ⟨bbr⟩ [bɛbɛr], ⟨wbnt⟩ [wɛbnɛt].

A constraint underdetermines the answer whenever more than one placement
satisfies it, and the gold does not always choose the same one: ⟨nfrtj⟩ is
[nɛfɛrti] there and [nɛfrɛti] here, and both obey the constraint. Twenty-one
words differ this way. The Appendix also says the two halves of a reduplication
are pronounced identically with no /ɛ/ between them; the rule layer cannot see
reduplication, and the third-consonant rule is the reachable approximation —
about half the words it fires on are reduplicated, and it satisfies the cluster
constraint on the rest.

Two adjacent weak consonants keep both radicals audible across a glottal stop
(⟨ꜣꜣ⟩ [ɑʔɑ], ⟨jj⟩ [iʔi]), and a word written with a single consonant takes the
vowel after it (⟨s⟩ [sɛ]).

Runs longer than four consonants, and runs that begin after a vowel, are past
the rule layer's three-slot lookback and are not stated: a word built on one
comes out with a vowel missing. That is headroom this spec has not reached, not
a property of the convention. The sonorants m, n and r take the vowel *before*
them when they are a word on their own ("em", "en", "er"); the rule layer can
append but not prepend, so those three words come out bare.

⟨ꜥnḫ⟩ is [ɑːnx], not the [ɑːnɛx] the constraint would give. The Appendix names
it as the significant exception to these conventions, so it is encoded as a word
override.

## Doubling is not gemination

A doubled letter in a consonantal skeleton is two radicals of a root, not one
long consonant: ⟨bbr⟩ is b-b-r and the convention puts a vowel between the two
⟨b⟩. The spec says so with `doubled_letters_geminate: false`, which releases
the allophony pass's geminate protection — that protection exists for
orthographies where doubling spells a single long segment, which this one is
not.

## What the benchmark can and cannot show

The `egy` WikiPron gold mixes two kinds of transcription under the same
headword: automatically generated Egyptological readings, and hand-entered
reconstructions of various stages (with ejectives, schwas, an explicit `V` for
an unknown vowel, and Coptic-influenced forms). Scoring takes the best of a
word's variants, so the row measures conformance to the reading convention,
which every headword in this gold turns out to carry. The reconstructions
cannot be reached from the orthography at all — the vowels they assert were
never written — but none of them is a headword's only reading, so none sets a
floor under the row.

Because the convention lines are generated by the same published guidelines the
spec encodes, the row is a reproduction test rather than an accuracy
measurement, and it is not comparison-eligible: see [the module-generated
WikiPron rows](../benchmarks.md#module-generated-wikipron-rows).

The convention itself reaches further than this spec does in one respect worth
naming. The Appendix states that the causative prefix s- and the -w suffixes are
ignored when deciding where the vowel goes, which is why ⟨swḏ⟩ is read *sewedj*
with its ⟨w⟩ still a consonant. That is a statement about letters, not about a
respelling, so it is encodable in principle; what is hard is deciding whether a
given word-initial ⟨s⟩ is the causative prefix or a radical, which the letter
string alone does not say. Those words are misses here.

Of the words the spec gets wrong, the large majority are placements inside a
cluster where it satisfies the constraint differently from the gold or cannot
reach the position at all, nine are causative s- words, and four are one-letter
words.

## Coptic

`cop` descends from `egy` and inherits from it, but it is written in its own
alphabet, which spells vowels. It therefore declares the Egyptian reading rules
with no target phonemes — the spec's way of saying that a parent's process is
absent — and its transcriptions are unaffected by them.
