# Ancient Egyptian (egy): the Egyptological reading convention

**Code**: `egy` | **Family**: Afro-Asiatic > Egyptian | **Script**: Egyptological transliteration (Latin with diacritics)
**Quality tier**: research | **Descendant**: Coptic (`cop`), through Demotic

The `egy` spec reads Egyptological transliteration and writes the Egyptological pronunciation: the conventional way Egyptologists read the words aloud. It does not claim to show how Egyptian was spoken.

**Sources read**: the Wiktionary page *Appendix:Egyptian pronunciation*, which publishes the convention. It gives the letter values, the epenthesis constraint, the one-consonant words, the ⟨w⟩ split and the ⟨ꜥnḫ⟩ exception. *Wiktionary:About Egyptian* names Schenkel's *Tübinger Einführung in die klassisch-ägyptische Sprache und Schrift* (1991) as the source of the convention, with reference to Peust (1999). Neither book was consulted. Loprieno (1995) and Allen (2013) are cited for the reconstruction that this spec does not encode.

## Input contract

The input is the Latin transliteration of the hieroglyphs, such as ⟨nfr⟩, ⟨bḥdt⟩ or ⟨ꜥnḫ⟩. Dictionaries, corpora and gold sets use this form as the citation form of an Egyptian word. The spec does not read hieroglyphs, so transliterate them first. The letters are ꜣ ꜥ b p f m n r h ḥ ḫ ẖ z s š q k g t ṯ d ḏ j y w. They form a consonantal skeleton, because the script writes no vowels.

## What the IPA means

The convention reads the weak consonants ꜣ ꜥ j y w as vowels. Where the script leaves a run of consonants without a vowel, it supplies a fixed ⟨e⟩ [ɛ]. That is why ⟨nfr⟩ reads *nefer* and ⟨bḥdt⟩ reads *behdet*.

The reconstructed phonology is a different object, and an orthography-to-IPA map cannot reach it. Reconstructions read ꜣ as a rhotic or a glottal, ꜥ as a pharyngeal, and ṯ and ḏ as palatals. They also supply vowels that the writing system never recorded, and those vowels differ between Old, Middle and Late Egyptian. The spec asserts none of that.

## Letter values

| Letter | IPA | Note |
|:--|:--|:--|
| ꜣ | ɑ | weak consonant, read as a vowel |
| ꜥ | ɑː | weak consonant, read as a long vowel |
| j | i | weak consonant, read as a vowel |
| y | iː | |
| w | w word-initially, uː elsewhere | the Appendix gives [uː] in general and [w] root-initially. The letter string does not show root boundaries, so the spec uses word-initial position. |
| ḥ, h | h | the convention merges them |
| ḫ | x | |
| ẖ | ç | |
| š | ʃ | |
| ṯ | t͡ʃ | |
| ḏ | d͡ʒ | |
| q | k | |
| z | z | |

## The conventional vowel

The Appendix states the vowel as a constraint, not as a placement recipe. It inserts /ɛ/ to break up consonant clusters, so that one consonant at most starts or ends each word, and two at most stand together inside it. Three allophone rules implement the three clauses. Each one appends a vowel to a consonant and rewrites nothing.

| Rule | Clause | Examples |
|:--|:--|:--|
| `EGY_EPEN_INITIAL` | a word-initial consonant before another consonant takes the vowel, so one consonant starts the word | ⟨nfr⟩ [nɛfɛr], ⟨bḥdt⟩ [bɛhdɛt] |
| `EGY_EPEN_RUN_THIRD` | the third consonant of a word-initial run takes one, so two consonants at most stand together | ⟨mnmnt⟩ [mɛnmɛnɛt], ⟨nḫbḫb⟩ [nɛxbɛxɛb] |
| `EGY_EPEN_BEFORE_FINAL` | the consonant before a word-final consonant takes one, so one consonant ends the word | ⟨bbr⟩ [bɛbɛr], ⟨wbnt⟩ [wɛbnɛt] |

A constraint leaves the answer open wherever more than one placement satisfies it. The gold does not always choose the same placement: ⟨nfrtj⟩ is [nɛfɛrti] in the gold and [nɛfrɛti] here, and both obey the constraint. The Appendix also says that the two halves of a reduplication sound the same, with no /ɛ/ between them. The rule layer cannot see reduplication. The third-consonant rule is the reachable approximation: about half the words it fires on are reduplicated, and it satisfies the cluster constraint on the rest.

Two adjacent weak consonants keep both radicals audible across a glottal stop: ⟨ꜣꜣ⟩ is [ɑʔɑ] and ⟨jj⟩ is [iʔi]. The `EGY_HIATUS_*` rules do this. A word written with a single consonant takes the vowel after it, so ⟨s⟩ is [sɛ] (`EGY_LONE_CONSONANT`).

Some placements are out of reach. Runs longer than four consonants, and runs that begin after a vowel, are past the rule layer's lookback of three slots. A word with such a run comes out with a vowel missing. This is a limit of the spec, not of the convention. The sonorants m, n and r take the vowel before them when they stand alone as a word ("em", "en", "er"). The rule layer can append but not prepend, so those three words come out bare.

⟨ꜥnḫ⟩ is [ɑːnx], not the [ɑːnɛx] that the constraint would give. The Appendix names it as the significant exception, so the spec encodes it as a word exception.

## Doubling is not gemination

A doubled letter in a consonantal skeleton is two radicals of a root, not one long consonant. ⟨bbr⟩ is b-b-r, and the convention puts a vowel between the two ⟨b⟩. The spec says so with `doubled_letters_geminate: false`. That setting releases the geminate protection of the allophony pass, which exists for orthographies where a doubled letter spells one long segment.

## What the benchmark shows

The `egy` WikiPron gold mixes two kinds of transcription under the same headword. Some lines are generated Egyptological readings. Others are hand-entered reconstructions of various stages, with ejectives, schwas, an explicit `V` for an unknown vowel, and forms that follow Coptic. Scoring takes the closest of a word's variants, so the row measures conformance to the reading convention, which every headword in this gold carries. The orthography cannot reach the reconstructions, but none of them is a headword's only reading, so none puts a floor under the row.

The convention lines come from the same published guidelines that the spec encodes. The row is therefore a reproduction test, not an accuracy measurement, and it is not eligible for comparison. See [the module-generated WikiPron rows](../benchmark_datasets.md#module-generated-wikipron-rows). For the score, see the [scoreboard](../scoreboard.md).

The misses fall into three groups. Most are placements inside a cluster, where the spec satisfies the constraint differently from the gold or cannot reach the position. The others are causative s- words and one-letter words.

The causative words are a gap that the convention could close. The Appendix states that the causative prefix s- and the -w suffixes do not count when the vowel is placed. That is why ⟨swḏ⟩ reads *sewedj*, with its ⟨w⟩ still a consonant. The statement is about letters, so it is encodable in principle. The hard part is to decide whether a word-initial ⟨s⟩ is the prefix or a radical, and the letter string does not say. The spec gives ⟨swḏ⟩ as [suːd͡ʒ].

## Coptic

`cop` descends from `egy` and inherits from it. Coptic has its own alphabet, which spells vowels. The `cop` spec therefore redeclares each Egyptian reading rule with no target phonemes, which is how a spec states that a parent's process is absent. Its transcriptions are not affected by those rules.

---
[← Kabyle / Taqbaylit](kab.md) · [Home](../index.md) · [Hausa →](ha.md)
