# Faroese (`fo`)

<!-- atlas:summary begin -->
Faroese is a North Germanic language, written in the Latin script. Glottolog places it in Denmark and Faroe Islands. The `fo` spec is at the production tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `fo` |
| ISO 639-3 | [fao](https://iso639-3.sil.org/code/fao), Faroese |
| Glottolog | [faro1244](https://glottolog.org/resource/languoid/id/faro1244), Faroese |
| Wikidata | [Q25258](https://www.wikidata.org/wiki/Q25258) |
| Wikipedia | [Faroese language](https://en.wikipedia.org/wiki/Faroese_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > North Germanic](by-family.md#indo-european--germanic--northwest-germanic--north-germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [Denmark](by-region.md#denmark), [Faroe Islands](by-region.md#faroe-islands) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [production](../specs/quality_tiers.md#production) |
| Attested | from 1400, living |
| Ancestor | [Old Norse](https://tigregotico.github.io/orthography2ipa/#non) `non` |
| Explorer | [`fo` in the data explorer](https://tigregotico.github.io/orthography2ipa/#fo) |
| Spec file | [`fo.json`](../../orthography2ipa/data/fo.json) |
<!-- atlas:header end -->

## Overview

Faroese (*føroyskt*) is the language of the Faroe Islands. Its parent language is Old Norse ([Lockwood](#notes-on-the-sources), p. 7), and the spec notes place it beside Icelandic as a descendant of Old West Norse. The `fo` spec transcribes the written standard into the speech of the central islands.

The written standard goes back to V. U. Hammershaimb. In 1846 he published texts in an orthography that he built on etymological principles, close to Old Norse. Modern Faroese is phonetically far from Old Norse, so the spelling gives an imperfect picture of the spoken word (p. 7). A letter-by-letter reading of a Faroese word is usually wrong. For this reason the spec relies on positional readings and allophone rules more than on its flat letter table.

Lockwood records no recognised standard pronunciation. The speech of the Tórshavn area carries the most weight, and Lockwood describes an average of the central area: Vágar, Streymoy and Eysturoy (p. 7). The spec follows the same central norm. It does not model the northern [ɔi] for ⟨ei⟩ or the other regional variants that Lockwood lists (p. 25).

Faroese is a deep orthography, so the production threshold is a PER of 0.25, not 0.15 ([quality tiers](../specs/quality_tiers.md#the-per-threshold)). Vowel length and vowel quality both follow syllable structure, and the spelling writes only the structure. The spelling writes voicing on the stops, but the spoken contrast is aspiration. The letters ⟨g⟩ and ⟨ð⟩ each stand for several sounds, and the position in the word selects among them.

## Vowel quantity

A stressed vowel letter has two values that differ in quality, not only in length. The long value occurs at the end of a word, before one consonant, and before the groups ⟨kl kr pl pr tr⟩. The short value occurs before a double consonant or before any other group of consonants (Lockwood, p. 10). A vowel in a fully unstressed syllable is short (p. 10).

The spec stores each long value as a `nucleus_stressed` reading of the vowel letter. A `FO_SHORTEN_*` rule for each vowel gives the short value before a consonant group. The values below come from the spec's letter table. Lockwood describes each pair in §4 (pp. 11-15).

| Letter | Long | Short | Lockwood |
|:---:|:---:|:---:|:--|
| ⟨a⟩ | [ɛaː] | [a] | p. 11 |
| ⟨á⟩ | [ɔaː] | [ɔ] | p. 11 |
| ⟨e⟩ | [eː] | [ɛ] | p. 12 |
| ⟨i y⟩ | [iː] | [ɪ] | pp. 12, 14 |
| ⟨í ý⟩ | [ʊiː] | [ʊj] | pp. 12, 14 |
| ⟨o⟩ | [oː] | [ɔ] | p. 13 |
| ⟨ó⟩ | [ɔuː] | [œ] | p. 13 |
| ⟨u⟩ | [uː] | [ʊ] | p. 13 |
| ⟨ú⟩ | [ʉuː] | [ʏ] | pp. 13-14 |
| ⟨ø⟩ | [øː] | [œ] | p. 14 |

The groups ⟨ógv úgv⟩ change the vowel and insert a stop. Lockwood gives ⟨nógv⟩ with a front vowel before [ɡv] and ⟨kúgv⟩ with [ɪ] before [ɡv] (pp. 13-14). No letter-by-letter reading gives these forms, so the spec stores ⟨ógv⟩ as [ɛkv] and ⟨úgv⟩ as [ɪkv], one unit each.

## Stops and aspiration

Faroese stops contrast in aspiration, not in voicing. Lockwood describes ⟨b d g⟩ as only very slightly voiced (p. 9), and the spec writes them as the plain stops [p t k]. The spec writes ⟨p t k⟩ as aspirated at the start of a word and as plain elsewhere.

The spec writes the double stops ⟨pp tt kk⟩ with preaspiration, as [ʰpp ʰtt ʰkk]. It takes this from Árnason (2011), which the spec cites without a page. Lockwood hears the preaspiration only in slow or emphatic speech, and he does not mark it (pp. 9-10). The two sources differ in how central they consider the feature, not in the sound.

## Palatalisation

Before the single vowels ⟨e i y⟩ and the digraph ⟨ey⟩, the letters ⟨k g sk⟩ become palatal. Lockwood gives this for ⟨g⟩ on pp. 17-18, for ⟨k⟩ on p. 19 and for initial ⟨sk⟩ on p. 23. The spec writes the results as [tʃʰ tʃ ʃ]. The digraphs ⟨kj gj sj skj⟩ give the same palatal sounds (pp. 18-19, 23).

The long vowels ⟨í ý⟩ do not palatalise a velar. Lockwood reads them as the diphthong [ʊi] (pp. 12, 14), and he gives ⟨gýsur⟩ with a velar [ɡ] (p. 17). The diphthong ⟨ei⟩ also keeps the velar, as in ⟨geit⟩ "goat" (p. 17). The digraph ⟨ey⟩ does not keep it, as in ⟨geykur⟩ "cuckoo" and ⟨skeyt⟩ "shot" (pp. 18, 23). The spec has separate entries for ⟨kí gí skí⟩ and their ⟨ý⟩ forms, so that these keep the velar. The spellings ⟨kei koy gei goy skei skoy⟩ have entries of their own for the same reason.

Lockwood lists the exceptions as mostly foreign words, such as ⟨kilo⟩ and ⟨Kina⟩ (p. 19). Danish loans also keep the plain [a] before ⟨ng nk⟩, as in ⟨banki⟩ "bank" and ⟨sangur⟩ "song" (p. 11). The spec has no loan lexicon that could separate the two layers of vocabulary.

## ⟨ð⟩ and ⟨g⟩ between vowels

The letter ⟨ð⟩ is silent at the end of a word and next to a consonant (Lockwood, p. 16). Between vowels it is also silent, or a glide appears in its place. The glide depends on the vowels around it (pp. 16-17):

| Context | Glide | Lockwood's example |
|:--|:--|:--|
| After ⟨i y í ý ei ey oy⟩, or before ⟨i⟩ after any vowel but ⟨ó u ú⟩ | [j] | ⟨siður⟩ "custom" (p. 16) |
| Between ⟨a á e æ ø⟩ and ⟨u⟩ | [v] | ⟨maður⟩ "man" (p. 17) |
| After ⟨ó u ú⟩ | [w] | ⟨suður⟩ "south" (p. 17) |
| Between ⟨a á e o⟩ and ⟨a⟩, and in some words between ⟨æ ø⟩ and ⟨a⟩ | none | ⟨ráða⟩ "to advise" (p. 16) |

The letter ⟨g⟩ between vowels follows the same pattern, with [j] in ⟨eyga⟩ "eye", [v] in ⟨dagur⟩ "day" and [w] in ⟨hugur⟩ "mind" (p. 18). After a vowel at the end of a word, ⟨g⟩ is silent, as in ⟨eg⟩ "I" (p. 18).

Between vowels, the spec gives ⟨ð⟩ the glide [j] as the first reading, with [v] and [w] as lower-ranked candidates. It gives intervocalic ⟨g⟩ [j] first and [v] second. It does not encode the contexts in the table above, so the first reading between vowels is always [j].

## Other consonants

The single ⟨r⟩ is the approximant [ɹ] in the spec. Lockwood compares it to the r of English *ring*, and he describes a trill only for the double ⟨rr⟩ (pp. 9, 22).

The double ⟨ll⟩ is [dl] in most words, between vowels and at the end of a word (Lockwood, p. 20). The spec gives [tl] as the first reading of ⟨ll⟩, with [ll] as a second candidate. The double ⟨nn⟩ is a long [nː] in most positions and [dn] after a diphthong, as in ⟨seinni⟩ "later" (p. 21). The spec gives [nn] first and [tn] second.

The group ⟨rn⟩ is [dn] in most words, as in ⟨horn⟩ and ⟨bjørn⟩ "bear". It stays [rn] in some words and in inflected forms where ⟨r⟩ and ⟨n⟩ meet (Lockwood, p. 22). A preceding ⟨r⟩ turns ⟨s⟩ into the retroflex [ʂ], as in ⟨norskur⟩ "Norwegian" (p. 23). The spec encodes neither change. The WikiPron gold splits between the variants word by word, and a categorical rule would state more than the sources support.

## Stress

Stress falls on the first syllable of nearly every native word. The second element of a compound carries a secondary stress, as in ⟨tilbiðja⟩ "to worship" (Lockwood, p. 10). Words with the prefixes ⟨ó-⟩ and ⟨sam-⟩ can also take stress on the second syllable. Many foreign words, such as ⟨studentur⟩ "student", take stress on a later syllable (p. 10). The acute accent on ⟨á í ó ú ý⟩ marks a vowel quality, not stress. The `stress` block of the spec puts the stress on the first syllable of every word.

## Reading the WikiPron row

The board scores the spec on the broad Faroese file of WikiPron, [`fao_latn_broad.tsv`](https://github.com/CUNY-CL/wikipron/blob/master/data/scrape/tsv/fao_latn_broad.tsv). WikiPron scrapes these transcriptions from Wiktionary. The [Faroese pronunciation appendix](https://en.wiktionary.org/wiki/Appendix:Faroese_pronunciation) of Wiktionary describes the transcription that its editors use. The row is crowd-scraped. Five provenance tiers never gate a promotion: the three that name a competing tool (`espeak-derived`, `epitran-derived` and `lupo-derived`) and the two language-model tiers ([which gold can gate](../specs/quality_tiers.md#which-gold-can-gate)). The `Gates` column of the Datasets block below gives the rows that gate. The gold marks vowel length but no stress, and it varies between the regional forms of ⟨rn⟩ and ⟨rs⟩.

An open Faroese speech corpus exists for work beyond single words: the [Ravnursson corpus](https://huggingface.co/datasets/carlosdanielhernandezmena/ravnursson_asr) of recorded speech with transcripts, under CC BY 4.0. Its transcripts are in the orthography, not in IPA, so it is not a gold for this spec.

## Weak points

The engine output below was measured against Lockwood's worked examples. The page numbers are those of Lockwood's section.

Compound secondary stress is the largest class of error. The `nucleus_stressed` position fires only on the first syllable of the word, so a second stem never gets its long vowel. The engine gives ⟨orðabók⟩ "dictionary" as [ˈɔɹapœk]. Lockwood has a long [oː] in the first stem and the long [ɔu] of ⟨ó⟩ in the second (p. 11). The spec notes count 352 of 354 gold rows with two or more length marks that come out short for this reason.

The glide after ⟨ð⟩ and ⟨g⟩ is always [j]. The engine gives ⟨maður⟩ as [ˈmɛaːjʊɹ], ⟨dagur⟩ as [ˈtɛaːjʊɹ] and ⟨hugur⟩ as [ˈhuːjʊɹ]. Lockwood has [v] in the first two and [w] in the third (pp. 17-18).

Before ⟨a⟩ the engine inserts [j] where Lockwood has no glide: ⟨ráða⟩ is [ˈɹɔaːja], and Lockwood gives a long [ɔː] followed by [a] (p. 11). Between vowels and before ⟨i⟩, the engine reads ⟨g⟩ as the palatal [tʃ]. So ⟨degi⟩ "day" is [ˈteːtʃɪ] and ⟨logi⟩ "flame" is [ˈloːtʃɪ], where Lockwood has the glide [j] (p. 18).

A final ⟨g⟩ after a vowel is silent, but the engine writes it: ⟨eg⟩ is [ˈeːk] and ⟨felag⟩ "company" is [ˈfeːlak] (Lockwood, p. 18).

Three consonant groups lose their special reading. The engine gives ⟨hvat⟩ "what" as [ˈhvɛaːt], where Lockwood has [kv] (p. 19).

The engine gives ⟨tjørn⟩ "tarn" as [ˈtʰjœɹn] and ⟨hetja⟩ "hero" as [ˈhɛtja], where ⟨tj⟩ is the palatal [tʃ] (p. 23). It gives ⟨nevnd⟩ "committee" as [ˈnɛvnt], where ⟨v⟩ before ⟨n⟩ forms the diphthong [ɛu] (p. 23).

The spec reads ⟨hj⟩ as [j], so ⟨hjól⟩ "wheel" is [ˈjɔuːl]. Lockwood gives ⟨hj⟩ as the palatal [tʃ] in general, and as [j] only in a few words such as ⟨hjálpa⟩ and ⟨hjarta⟩ (p. 19). The spec notes cite Þráinsson et al. (2004) for [j], without a page.

Some vowel values are missing. The short ⟨ey⟩ is [ɛ], as in ⟨eystur⟩ "east" (Lockwood, p. 15), and the engine gives [ˈɛistʊɹ].

The ⟨a⟩ before ⟨ng nk⟩ is the front vowel of English *set*, as in ⟨langur⟩ "long" (p. 11), and the engine gives [ˈlaŋkʊɹ]. A vowel before ⟨kr⟩ or ⟨pl⟩ is long (pp. 10, 19), but the engine shortens it: ⟨vakrir⟩ "beautiful" is [ˈvakɹɪɹ]. In the place name ⟨Føroyar⟩, the old word for island is reduced to [j] (p. 15), and the engine gives [ˈføːɹɔiaɹ].

A vowel after a vowel gets the long stressed value. The engine gives ⟨fáa⟩ "to obtain" as [ˈfɔaːɛaː] and ⟨búa⟩ as [ˈpʉuːɛaː]. Lockwood gives ⟨fáa⟩ with one long vowel and a short [a] (p. 11), and he states that a vowel in an unstressed syllable is short (p. 10).

The double ⟨nn⟩ after a diphthong and the group ⟨rn⟩ keep their spelling. The engine gives ⟨seinni⟩ as [ˈsainnɪ] and ⟨horn⟩ as [ˈhɔɹn], where Lockwood has [dn] in both (pp. 21-22). Foreign words keep the initial stress of native words, so ⟨studentur⟩ is [ˈstuːtɛntʊɹ] (p. 10).

<!-- atlas:lects begin -->
## Related lects

No spec names `fo` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-arnason2011"></a>Árnason, K. (2011). *The Phonology of Icelandic and Faroese*. Oxford University Press.
2. <a id="src-thrainsson2004"></a>Þráinsson, H., Petersen, H. P., Jacobsen, J. í L. and Hansen, Z. S. (2004). *Faroese: An Overview and Reference Grammar*. Føroya Fróðskaparfelag.
3. <a id="src-lockwood1955"></a>Lockwood, W. B. (1955). *An Introduction to Modern Faroese*. Munksgaard.
<!-- atlas:sources end -->

### Notes on the sources

The spec cites Lockwood's *An Introduction to Modern Faroese* without a page. Its description of Faroese sounds is reprinted in G. V. C. Young and C. R. Clewer, *Føroysk-ensk orðabók* (Føroya Fróðskaparfelag, 1985), pp. 7-29, a scan of which is [open on the Internet Archive](https://archive.org/details/bub_gb_XfvZ9J4oABwC). This page cites that reprint by page as "Lockwood, p. N". The reprint states that it comes from the 1964 Munksgaard edition. [Faroese phonology](https://en.wikipedia.org/wiki/Faroese_phonology) on Wikipedia gives a second overview.

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `fo` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 2957 | 0.1674 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 71 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p pʰ |  | t tʰ |  |  | k kʰ |  |
| Affricate |  |  |  | tʃ tʃʰ |  |  |  |
| Nasal | m |  | n |  | ɲ | ŋ |  |
| Fricative |  | f v | s | ʃ |  |  | h |
| Approximant |  |  | ɹ |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | iː | uː |
| Near-close | ɪ ʏ | ʊ |
| Close-mid | eː øː | oː |
| Open-mid | œ ɛ | ɔ |
| Open | a aː |  |

Sequences that the spec writes as one unit: [ai] [aiː] [au] [av] [kaiː] [kɔiː] [kʊiː] [kʰaiː] [kʰɔiː] [kʰʊiː] [ll] [nj] [nn] [sk] [skaiː] [skɔiː] [skʊiː] [tl] [tn] [w] [ŋk] [ɔaː] [ɔi] [ɔiː] [ɔuː] [ɛaː] [ɛi] [ɛiː] [ɛkv] [ɛu] [ɛuː] [ɪkv] [ʉuː] [ʊiː] [ʊj] [ʰkk] [ʰpp] [ʰtt].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] | default [a] · nucleus stressed [ɛaː] [aː] |
| ⟨au⟩ | [ɛu] | default [ɛu] · nucleus stressed [ɛuː] |
| ⟨av⟩ | [av] | before consonant [au] · default [av] |
| ⟨b⟩ | [p] |  |
| ⟨d⟩ | [t] |  |
| ⟨e⟩ | [ɛ] | default [ɛ] · nucleus stressed [eː] |
| ⟨ei⟩ | [ai] | default [ai] · nucleus stressed [aiː] |
| ⟨ey⟩ | [ɛi] | default [ɛi] · nucleus stressed [ɛiː] |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [k] | before e [tʃ] · before i [tʃ] · before y [tʃ] · default [k] · intervocalic [j] [v] |
| ⟨gei⟩ | [kaiː] |  |
| ⟨ggj⟩ | [tʃ] |  |
| ⟨gj⟩ | [tʃ] |  |
| ⟨goy⟩ | [kɔiː] |  |
| ⟨gí⟩ | [kʊiː] |  |
| ⟨gý⟩ | [kʊiː] |  |
| ⟨h⟩ | [h] |  |
| ⟨hj⟩ | [j] |  |
| ⟨i⟩ | [ɪ] | default [ɪ] · nucleus stressed [iː] |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] | before e [tʃʰ] · before i [tʃʰ] · before y [tʃʰ] · default [k] · word initial [kʰ] |
| ⟨kei⟩ | [kʰaiː] |  |
| ⟨kj⟩ | [tʃʰ] |  |
| ⟨kk⟩ | [ʰkk] |  |
| ⟨koy⟩ | [kʰɔiː] |  |
| ⟨kí⟩ | [kʰʊiː] |  |
| ⟨ký⟩ | [kʰʊiː] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [tl] [ll] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋk] [ŋ] |  |
| ⟨nj⟩ | [nj] | default [nj] · word initial [ɲ] [nj] |
| ⟨nn⟩ | [nn] [tn] |  |
| ⟨o⟩ | [ɔ] | default [ɔ] · nucleus stressed [oː] |
| ⟨oy⟩ | [ɔi] | default [ɔi] · nucleus stressed [ɔiː] |
| ⟨p⟩ | [p] | default [p] · word initial [pʰ] |
| ⟨pp⟩ | [ʰpp] |  |
| ⟨r⟩ | [ɹ] |  |
| ⟨s⟩ | [s] |  |
| ⟨sj⟩ | [ʃ] |  |
| ⟨sk⟩ | [sk] | before e [ʃ] · before i [ʃ] · before y [ʃ] · default [sk] |
| ⟨skei⟩ | [skaiː] |  |
| ⟨skj⟩ | [ʃ] |  |
| ⟨skoy⟩ | [skɔiː] |  |
| ⟨skí⟩ | [skʊiː] |  |
| ⟨ský⟩ | [skʊiː] |  |
| ⟨t⟩ | [t] | default [t] · word initial [tʰ] |
| ⟨tt⟩ | [ʰtt] |  |
| ⟨u⟩ | [ʊ] | default [ʊ] · nucleus stressed [uː] |
| ⟨v⟩ | [v] |  |
| ⟨y⟩ | [ɪ] | default [ɪ] · nucleus stressed [iː] |
| ⟨á⟩ | [ɔ] | default [ɔ] · nucleus stressed [ɔaː] |
| ⟨æ⟩ | [a] | default [a] · nucleus stressed [ɛaː] |
| ⟨í⟩ | [ʊj] | default [ʊj] · nucleus stressed [ʊiː] |
| ⟨ð⟩ | ∅ [j] [v] [w] | default ∅ [j] · intervocalic [j] [v] [w] |
| ⟨ó⟩ | [œ] | default [œ] · nucleus stressed [ɔuː] |
| ⟨ógv⟩ | [ɛkv] |  |
| ⟨ø⟩ | [œ] | default [œ] · nucleus stressed [øː] |
| ⟨ú⟩ | [ʏ] | default [ʏ] · nucleus stressed [ʉuː] |
| ⟨úgv⟩ | [ɪkv] |  |
| ⟨ý⟩ | [ʊj] | default [ʊj] · nucleus stressed [ʊiː] |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 15 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `FO_SHORTEN_00` | /ɛaː/ → [a], before a consonant cluster | - | Jacobsen & Hansen 2004, Arnason 2011 |
| `FO_SHORTEN_01` | /aː/ → [a], before a consonant cluster | - | Jacobsen & Hansen 2004, Arnason 2011 |
| `FO_SHORTEN_02` | /ɔaː/ → [ɔ], before a consonant cluster | - | Jacobsen & Hansen 2004, Arnason 2011 |
| `FO_SHORTEN_03` | /eː/ → [ɛ], before a consonant cluster | - | Jacobsen & Hansen 2004, Arnason 2011 |
| `FO_SHORTEN_04` | /iː/ → [ɪ], before a consonant cluster | - | Jacobsen & Hansen 2004, Arnason 2011 |
| `FO_SHORTEN_05` | /ʊiː/ → [ʊj], before a consonant cluster | - | Jacobsen & Hansen 2004, Arnason 2011 |
| `FO_SHORTEN_06` | /oː/ → [ɔ], before a consonant cluster | - | Jacobsen & Hansen 2004, Arnason 2011 |
| `FO_SHORTEN_07` | /ɔuː/ → [œ], before a consonant cluster | - | Jacobsen & Hansen 2004, Arnason 2011 |
| `FO_SHORTEN_08` | /uː/ → [ʊ], before a consonant cluster | - | Jacobsen & Hansen 2004, Arnason 2011 |
| `FO_SHORTEN_09` | /ʉuː/ → [ʏ], before a consonant cluster | - | Jacobsen & Hansen 2004, Arnason 2011 |
| `FO_SHORTEN_10` | /øː/ → [œ], before a consonant cluster | - | Jacobsen & Hansen 2004, Arnason 2011 |
| `FO_SHORTEN_11` | /aiː/ → [ai], before a consonant cluster | - | Jacobsen & Hansen 2004, Arnason 2011 |
| `FO_SHORTEN_12` | /ɛiː/ → [ɛi], before a consonant cluster | - | Jacobsen & Hansen 2004, Arnason 2011 |
| `FO_SHORTEN_13` | /ɔiː/ → [ɔi], before a consonant cluster | - | Jacobsen & Hansen 2004, Arnason 2011 |
| `FO_SHORTEN_14` | /ɛuː/ → [ɛu], before a consonant cluster | - | Jacobsen & Hansen 2004, Arnason 2011 |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="Føroyar|orðabók|maður|dagur|hugur|eyga|ráða|degi|eg|felag|hvat|tjørn|nevnd|hjól|hjálpa|eystur|langur|vakrir|fáa|seinni|horn|geykur|keisari|kirkja|nógv|kúgv|studentur" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "fo")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| Føroyar | [ˈføːɹɔiaɹ] |
| orðabók | [ˈɔɹapœk] |
| maður | [ˈmɛaːjʊɹ] |
| dagur | [ˈtɛaːjʊɹ] |
| hugur | [ˈhuːjʊɹ] |
| eyga | [ˈɛiːja] |
| ráða | [ˈɹɔaːja] |
| degi | [ˈteːtʃɪ] |
| eg | [ˈeːk] |
| felag | [ˈfeːlak] |
| hvat | [ˈhvɛaːt] |
| tjørn | [ˈtʰjœɹn] |
| nevnd | [ˈnɛvnt] |
| hjól | [ˈjɔuːl] |
| hjálpa | [ˈjɔlpa] |
| eystur | [ˈɛistʊɹ] |
| langur | [ˈlaŋkʊɹ] |
| vakrir | [ˈvakɹɪɹ] |
| fáa | [ˈfɔaːɛaː] |
| seinni | [ˈsainnɪ] |
| horn | [ˈhɔɹn] |
| geykur | [ˈtʃɛiːkʊɹ] |
| keisari | [ˈkʰaiːsaɹɪ] |
| kirkja | [ˈtʃʰɪɹtʃʰa] |
| nógv | [ˈnɛkv] |
| kúgv | [ˈkʰɪkv] |
| studentur | [ˈstuːtɛntʊɹ] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Farefare](gur.md) · [Home](../index.md) · [Fernando Po Creole English →](fpe.md)
