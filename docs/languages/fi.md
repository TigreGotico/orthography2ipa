# Finnish (`fi`)

<!-- atlas:summary begin -->
Finnish is a Finnic language, written in the Latin script. Glottolog places it in 5 countries. The `fi` spec is at the production tier. It cites 3 sources and has 3 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `fi` |
| Aliases | `fin` |
| ISO 639-3 | [fin](https://iso639-3.sil.org/code/fin), Finnish |
| Glottolog | [finn1318](https://glottolog.org/resource/languoid/id/finn1318), Finnish |
| Wikidata | [Q1412](https://www.wikidata.org/wiki/Q1412) |
| Wikipedia | [Finnish language](https://en.wikipedia.org/wiki/Finnish_language) |
| Family | [Uralic](by-family.md#uralic) > [Finnic](by-family.md#uralic--finnic) |
| Region | [Eurasia](by-region.md#eurasia) > [Estonia](by-region.md#estonia), [Finland](by-region.md#finland), [Norway](by-region.md#norway), [Russia](by-region.md#russia), [Sweden](by-region.md#sweden) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [production](../specs/quality_tiers.md#production) |
| Attested | from 1500, living |
| Parent | [Finnic](https://tigregotico.github.io/orthography2ipa/#x-clade-finn1317) `x-clade-finn1317` |
| Explorer | [`fi` in the data explorer](https://tigregotico.github.io/orthography2ipa/#fi) |
| Spec file | [`fi.json`](../../orthography2ipa/data/fi.json) |
<!-- atlas:header end -->

## Overview

The `fi` spec transcribes Standard Finnish. Finnish spelling is close to phonemic: each letter stands for one sound, and a doubled letter writes a long sound. Eliot (1890, pp. 1-5) describes this spelling letter by letter, and the examples below come from his grammar. The spec reads each letter, each double letter and each diphthong as one unit, and it puts the stress on the first syllable.

Finnish is a shallow orthography, so the production bar for this spec is a PER of 0.15 ([quality tiers](../specs/quality_tiers.md#the-per-threshold)). The few letters that need a rule are ⟨ng⟩, ⟨nk⟩ and the letters of loanwords.

## Length

Finnish has eight simple vowels, and all of them are short. A doubled vowel letter writes the long vowel (Eliot 1890, pp. 2-3). The spec has a grapheme for each double vowel, so `tuli` 'fire' is [ˈtuli] and `tuuli` 'wind' is [ˈtuːli]. Eliot (p. 5) lists these pairs to show that length changes the word: `tule` 'come!' and `tulee` 'he comes' differ only in the last vowel.

A doubled consonant is pronounced "distinctly twice, as in Italian" (Eliot 1890, p. 5). The spec writes it as a long consonant: `kukka` 'flower' is [ˈkukːɑ], `pappi` 'priest' is [ˈpɑpːi], and `kylä` 'village' [ˈkylæ] differs from `kyllä` 'enough' [ˈkylːæ]. Eliot (p. 5) also says that the length of a vowel has nothing to do with the stress. The spec keeps length and stress apart in the same way.

## Diphthongs

Eliot (1890, pp. 3-4) lists 16 diphthongs. In three of them the second vowel is the stronger one: ⟨uo yö ie⟩, as in `tuo` 'this', `yö` 'night' and `tie` 'way'. The others end in ⟨u⟩, ⟨y⟩ or ⟨i⟩, as in `kauppa` 'sale', `koulu` 'school' and `päivä` 'day'. The spec notes count 18 diphthongs, and the spec has a grapheme for each one, so that it counts as one syllable nucleus.

Eliot (p. 4) adds that only the diphthongs in ⟨i⟩ occur after the first syllable. Elsewhere the two vowels are two syllables, as in `tapa-us`. The engine marks no syllable boundary, so `tapaus` comes out as [ˈtɑpɑus] with either analysis.

## Consonant letters

In native words the letter ⟨g⟩ occurs only in ⟨ng⟩, which stands for an older ⟨nk⟩. It has the sound of English ⟨ng⟩ (Eliot 1890, p. 1). The spec reads ⟨ng⟩ as the long velar nasal [ŋː] and ⟨nk⟩ as [ŋk]. So `kenkä` 'shoe' is [ˈkeŋkæ], its plural `kengät` is [ˈkeŋːæt], and `Helsinki` is [ˈhelsiŋki]. Eliot gives no length for ⟨ng⟩, so the length comes from the spec alone.

In native words ⟨d⟩ occurs only inside a word, as the weak grade of ⟨t⟩ (Eliot 1890, p. 1): `sota` 'war' has the genitive `sodan`. The spec reads ⟨d⟩ as [d], the educated pronunciation that Eliot names. The alternation of ⟨t⟩ and ⟨d⟩ is consonant gradation, which the spec notes describe. It changes the spelling of the word, not the reading of a letter, so the spec needs no rule for it. Vowel harmony is the same case: it limits which suffixes occur, and the letters keep their readings.

The letter ⟨h⟩ is a stronger aspirate than in English (Eliot 1890, p. 2). It is clearest at the end of a syllable, as in `tehdä` 'to do'. The spec writes it as [h] in every position.

## Stress

The main stress always falls on the first syllable of the word (Eliot 1890, p. 4). The `stress` block of the spec states this with `default_position: 1`. Eliot (p. 4) also gives a secondary stress, usually on the third and fifth syllables and sometimes on the fourth and sixth. The second and the last syllable never take it.

## Reading the datasets

The `wikipron` row is the gating gold. WikiPron ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) scrapes the IPA of English Wiktionary. The Wiktionary entries `kenkä`, `kauppa` and `Helsinki` do not type their IPA. They call the template `{{fi-pronunciation}}`, which runs [Module:fi-pronunciation](https://en.wiktionary.org/wiki/Module:fi-pronunciation). Where an entry does that, the gold is the output of the module. The row then measures agreement with a rule system, like the [module-generated rows](../evaluation/datasets.md#module-generated-wikipron-rows) of the dataset catalogue.

The `ipadict` row is machine-generated. The dataset catalogue traces it to [prosodic1b](https://github.com/jsfalk/prosodic1b), a rule-based tool, run over the Kotus word list. A machine-generated row can gate, but it also measures agreement with another rule system. The `vox_communis` row is the output of [epitran](https://github.com/dmort27/epitran), so it never gates.

## Weak points

The spec has no reading for ⟨š⟩, ⟨ž⟩, ⟨å⟩ or ⟨q⟩, so the engine drops each one with an `UnmappedGraphemeWarning`. So `šakki` 'chess' comes out as [ˈɑkːi], and the Swedish name `Åbo` comes out as [ˈbo]. Eliot (1890, p. 2) names the Swedish ⟨å⟩ among the letters of foreign words and gives its sound as ⟨o⟩.

The engine writes no secondary stress. Eliot (1890, p. 4) marks it on the third, fifth and seventh syllables of *op-pi-mát-to-múu-des-sán-sa* 'in his ability to learn'. The stress notes of the spec state the same rule for odd syllables. The engine gives `oppimattomuudessansa` as [ˈopːimɑtːomuːdesːɑnsɑ], with the main stress only.

Some words end in a slight aspiration that the spelling does not write, as in `vene` 'boat' and `syödä` 'to eat' (Eliot 1890, p. 2). No rule can recover it from the text, so the engine gives `vene` as [ˈʋene]. Gold sets of single words do not test it.

The letters of loanwords keep their face value. The engine reads ⟨ch⟩ in `Bach` as two letters, [ˈbɑkh].

<!-- atlas:lects begin -->
## Related lects

No spec names `fi` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL.

1. <a id="src-abondolo1998"></a>Abondolo, D. (ed.) (1998). *The Uralic Languages*. Routledge.
2. <a id="src-hakulinen1979"></a>Hakulinen, L. (1979). *The Structure and Development of the Finnish Language*. Indiana University Press.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
<!-- atlas:sources end -->

### Notes on the sources

The examples and page numbers on this page come from Eliot, C. N. E. (1890), *A Finnish Grammar*, Oxford, Clarendon Press. The [scan on archive.org](https://archive.org/details/afinnishgrammar00eliogoog) is in the public domain. The spec does not cite this grammar. None of the three works that the spec cites gives a page in the spec file.

The notes of the spec name Karlsson (1999), Hakulinen & Karlsson (1979) and Suomi et al. (2008). These works are not in its list of sources.

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `fi` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 168808 | 0.0184 | yes |
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `fi` | generated | machine-generated | MIT, each file its own | 92836 | 0.0609 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `fi` | generated | epitran-derived | CC0 1.0 | 13324 | 0.0037 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 66 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pː |  | d t tː |  | k kː ɡ |  |
| Affricate |  |  | ts |  |  |  |
| Nasal | m mː |  | n nː |  | ŋ ŋː |  |
| Trill |  |  | r rː |  |  |  |
| Tap |  |  | ɾ |  |  |  |
| Fricative |  | f | s sː | ç | x | h ɦ |
| Approximant |  | ʋ |  | j |  |  |
| Lateral approximant |  |  | l lː |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i iː y yː | u uː |
| Close-mid | e eː ø øː | o oː |
| Near-open | æ æː |  |
| Open |  | ɑ ɑː |

Sequences that the spec writes as one unit: [ei] [eu] [ey] [ie] [iu] [iy] [oi] [ou] [ui] [uo] [w] [yi] [yø] [æi] [æy] [øi] [øy] [ŋk] [ɑi] [ɑu].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] |  |
| ⟨aa⟩ | [ɑː] |  |
| ⟨ai⟩ | [ɑi] |  |
| ⟨au⟩ | [ɑu] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] [s] |  |
| ⟨d⟩ | [d] | default [d] |
| ⟨e⟩ | [e] |  |
| ⟨ee⟩ | [eː] |  |
| ⟨ei⟩ | [ei] |  |
| ⟨eu⟩ | [eu] |  |
| ⟨ey⟩ | [ey] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ie⟩ | [ie] |  |
| ⟨ii⟩ | [iː] |  |
| ⟨iu⟩ | [iu] |  |
| ⟨iy⟩ | [iy] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] | default [k] |
| ⟨kk⟩ | [kː] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [lː] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [mː] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋː] | default [ŋː] |
| ⟨nk⟩ | [ŋk] |  |
| ⟨nn⟩ | [nː] |  |
| ⟨o⟩ | [o] |  |
| ⟨oi⟩ | [oi] |  |
| ⟨oo⟩ | [oː] |  |
| ⟨ou⟩ | [ou] |  |
| ⟨p⟩ | [p] | default [p] |
| ⟨pp⟩ | [pː] |  |
| ⟨r⟩ | [r] |  |
| ⟨rr⟩ | [rː] |  |
| ⟨s⟩ | [s] |  |
| ⟨ss⟩ | [sː] |  |
| ⟨t⟩ | [t] | default [t] |
| ⟨tt⟩ | [tː] |  |
| ⟨u⟩ | [u] |  |
| ⟨ui⟩ | [ui] |  |
| ⟨uo⟩ | [uo] |  |
| ⟨uu⟩ | [uː] |  |
| ⟨v⟩ | [ʋ] |  |
| ⟨w⟩ | [ʋ] |  |
| ⟨y⟩ | [y] |  |
| ⟨yi⟩ | [yi] |  |
| ⟨yy⟩ | [yː] |  |
| ⟨yö⟩ | [yø] |  |
| ⟨z⟩ | [ts] |  |
| ⟨ä⟩ | [æ] |  |
| ⟨äi⟩ | [æi] |  |
| ⟨äy⟩ | [æy] |  |
| ⟨ää⟩ | [æː] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨öi⟩ | [øi] |  |
| ⟨öy⟩ | [øy] |  |
| ⟨öö⟩ | [øː] |  |

Stress falls on the first syllable by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin words="tuli|tuuli|tule|tulee|kukka|pappi|kylä|kyllä|tuo|yö|tie|kauppa|koulu|päivä|tapaus|kenkä|kengät|Helsinki|sota|sodan|tehdä|oppimattomuudessansa|vene|šakki|Åbo|Bach" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "fi")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| tuli | [ˈtuli] |
| tuuli | [ˈtuːli] |
| tule | [ˈtule] |
| tulee | [ˈtuleː] |
| kukka | [ˈkukːɑ] |
| pappi | [ˈpɑpːi] |
| kylä | [ˈkylæ] |
| kyllä | [ˈkylːæ] |
| tuo | [ˈtuo] |
| yö | [ˈyø] |
| tie | [ˈtie] |
| kauppa | [ˈkɑupːɑ] |
| koulu | [ˈkoulu] |
| päivä | [ˈpæiʋæ] |
| tapaus | [ˈtɑpɑus] |
| kenkä | [ˈkeŋkæ] |
| kengät | [ˈkeŋːæt] |
| Helsinki | [ˈhelsiŋki] |
| sota | [ˈsotɑ] |
| sodan | [ˈsodɑn] |
| tehdä | [ˈtehdæ] |
| oppimattomuudessansa | [ˈopːimɑtːomuːdesːɑnsɑ] |
| vene | [ˈʋene] |
| šakki | [ˈɑkːi] |
| Åbo | [ˈbo] |
| Bach | [ˈbɑkh] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Fijian](fj.md) · [Home](../index.md) · [Fon →](fon.md)
