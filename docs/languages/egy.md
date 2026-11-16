# Ancient Egyptian (`egy`)

<!-- atlas:summary begin -->
Ancient Egyptian is an Egyptian language, written in the Latin script. Glottolog places it in Egypt. The `egy` spec is at the research tier. It cites 5 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `egy` |
| ISO 639-3 | [egy](https://iso639-3.sil.org/code/egy), Egyptian (Ancient) |
| Glottolog | [egyp1246](https://glottolog.org/resource/languoid/id/egyp1246), Egyptian (Ancient) |
| Wikidata | [Q50868](https://www.wikidata.org/wiki/Q50868) |
| Wikipedia | [Egyptian language](https://en.wikipedia.org/wiki/Egyptian_language) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Egyptian](by-family.md#afro-asiatic--egyptian) |
| Region | [Africa](by-region.md#africa) > [Egypt](by-region.md#egypt) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Parent | [Egyptian](https://tigregotico.github.io/orthography2ipa/#x-clade-egyp1245) `x-clade-egyp1245` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`egy` in the data explorer](https://tigregotico.github.io/orthography2ipa/#egy) |
| Spec file | [`egy.json`](../../orthography2ipa/data/egy.json) |
<!-- atlas:header end -->

## Overview

The `egy` spec reads Egyptological transliteration and writes the Egyptological pronunciation: the conventional way Egyptologists read the words aloud. It does not claim to show how Egyptian was spoken.

**Sources read**: the Wiktionary page *Appendix:Egyptian pronunciation*, which publishes the convention. It gives the letter values, the epenthesis constraint, the one-consonant words, the ⟨w⟩ split and the ⟨ꜥnḫ⟩ exception. *Wiktionary:About Egyptian* names Schenkel's *Tübinger Einführung in die klassisch-ägyptische Sprache und Schrift* (1991) as the source of the convention, with reference to Peust (1999). Neither book was consulted. Loprieno (1995) and Allen (2013) are cited for the reconstruction that this spec does not encode.

Its descendant is Coptic (`cop`), through Demotic.

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

The convention lines come from the same published guidelines that the spec encodes. The row is therefore a reproduction test, not an accuracy measurement, and it is not eligible for comparison. See [the module-generated WikiPron rows](../evaluation/datasets.md#module-generated-wikipron-rows). For the score, see the [scoreboard](../evaluation/generated/scoreboard.md).

The misses fall into three groups. Most are placements inside a cluster, where the spec satisfies the constraint differently from the gold or cannot reach the position. The others are causative s- words and one-letter words.

The causative words are a gap that the convention could close. The Appendix states that the causative prefix s- and the -w suffixes do not count when the vowel is placed. That is why ⟨swḏ⟩ reads *sewedj*, with its ⟨w⟩ still a consonant. The statement is about letters, so it is encodable in principle. The hard part is to decide whether a word-initial ⟨s⟩ is the prefix or a radical, and the letter string does not say. The spec gives ⟨swḏ⟩ as [suːd͡ʒ].

## Coptic

`cop` descends from `egy` and inherits from it. Coptic has its own alphabet, which spells vowels. The `cop` spec therefore redeclares each Egyptian reading rule with no target phonemes, which is how a spec states that a parent's process is absent. Its transcriptions are not affected by those rules.

<!-- atlas:lects begin -->
## Related lects

These specs name `egy` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Coptic (Sahidic)](https://tigregotico.github.io/orthography2ipa/#cop) `cop`: Egypt, research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-loprieno1995"></a>Loprieno, A. (1995). *Ancient Egyptian: A Linguistic Introduction*. Cambridge University Press.
2. <a id="src-schenkel1991"></a>Schenkel, W. (1991). *Tübinger Einführung in die klassisch-ägyptische Sprache und Schrift*. Tübingen.
3. <a id="src-peust1999"></a>Peust, C. (1999). *Egyptian Phonology: An Introduction to the Phonology of a Dead Language*. Peust & Gutschmidt.
4. <a id="src-allen2013"></a>Allen, J. P. (2013). *The Ancient Egyptian Language: An Historical Study*. Cambridge University Press.
5. <a id="src-wiktionary_egy_appendix"></a>Wiktionary contributors (2026). *Appendix:Egyptian pronunciation*. Wiktionary. [en.wiktionary.org](https://en.wiktionary.org/wiki/Appendix:Egyptian_pronunciation)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `egy` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2185 | 0.0183 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 26 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ | ʔ |
| Affricate |  |  |  | d͡ʒ t͡ʃ |  |  |  |
| Nasal | m |  | n |  |  |  |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f | s z | ʃ | ç | x | h |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː | uː |
| Open-mid | ɛ |  |
| Open |  | ɑ ɑː |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨j⟩ | [i] |  |
| ⟨k⟩ | [k] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨w⟩ | [uː] | default [uː] · word initial [w] |
| ⟨y⟩ | [iː] |  |
| ⟨z⟩ | [z] |  |
| ⟨š⟩ | [ʃ] |  |
| ⟨ḏ⟩ | [d͡ʒ] |  |
| ⟨ḥ⟩ | [h] |  |
| ⟨ḫ⟩ | [x] |  |
| ⟨ṯ⟩ | [t͡ʃ] |  |
| ⟨ẖ⟩ | [ç] |  |
| ⟨ꜣ⟩ | [ɑ] |  |
| ⟨ꜥ⟩ | [ɑː] |  |

The spec declares no stress rule.

Whole-word exceptions (1): ⟨ꜥnḫ⟩ [ɑːnx].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 7 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `EGY_EPEN_INITIAL` | insert [ɛ] after /b d d͡ʒ f h k m n p r s t t͡ʃ x z ç ɡ ʃ w/, word-initially, before a consonant | ⟨nfr⟩ [nɛfɛr] | - |
| `EGY_EPEN_RUN_THIRD` | insert [ɛ] after /b d d͡ʒ f h k m n p r s t t͡ʃ x z ç ɡ ʃ w/, after a consonant, before a consonant, with more context in the spec | ⟨mnmnt⟩ [mɛnmɛnɛt] | - |
| `EGY_EPEN_BEFORE_FINAL` | insert [ɛ] after /b d d͡ʒ f h k m n p r s t t͡ʃ x z ç ɡ ʃ w/, not word-finally, before a consonant, with more context in the spec | ⟨bbr⟩ [bɛbɛr] | - |
| `EGY_LONE_CONSONANT` | insert [ɛ] after /b d d͡ʒ f h k p s t t͡ʃ x z ç ɡ ʃ w/, word-initially, word-finally | - | - |
| `EGY_HIATUS_A` | insert [ʔ] after /ɑ ɑː/, before [ɑ] [ɑː] | - | - |
| `EGY_HIATUS_I` | insert [ʔ] after /i iː/, before [i] [iː] | - | - |
| `EGY_HIATUS_U` | insert [ʔ] after /uː/, before [uː] | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="nfr|bḥdt|mnmnt|nḫbḫb|bbr|wbnt|nfrtj|ꜣꜣ|jj|ꜥnḫ|swḏ" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "egy")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| nfr | [nɛfɛr] |
| bḥdt | [bɛhdɛt] |
| mnmnt | [mɛnmɛnɛt] |
| nḫbḫb | [nɛxbɛxɛb] |
| bbr | [bɛbɛr] |
| wbnt | [wɛbnɛt] |
| nfrtj | [nɛfrɛti] |
| ꜣꜣ | [ɑʔɑ] |
| jj | [iʔi] |
| ꜥnḫ | [ɑːnx] |
| swḏ | [suːd͡ʒ] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Amis](ami.md) · [Home](../index.md) · [Apulian →](it-IT-x-puglia.md)
