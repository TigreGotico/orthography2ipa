# Esperanto (`eo`)

<!-- atlas:summary begin -->
Esperanto is a Constructed language, written in the Latin script. Glottolog places it in Poland. The `eo` spec is at the production tier. It cites 2 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `eo` |
| ISO 639-3 | [epo](https://iso639-3.sil.org/code/epo), Esperanto |
| Glottolog | [espe1235](https://glottolog.org/resource/languoid/id/espe1235), Esperanto |
| Wikidata | [Q143](https://www.wikidata.org/wiki/Q143) |
| Wikipedia | [Esperanto](https://en.wikipedia.org/wiki/Esperanto) |
| Family | [Constructed](by-family.md#constructed) |
| Region | [Eurasia](by-region.md#eurasia) > [Poland](by-region.md#poland) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [production](../specs/quality_tiers.md#production) |
| Attested | from 1887, living |
| Explorer | [`eo` in the data explorer](https://tigregotico.github.io/orthography2ipa/#eo) |
| Spec file | [`eo.json`](../../orthography2ipa/data/eo.json) |
<!-- atlas:header end -->

## Overview

Esperanto is the constructed language that L. L. Zamenhof published in 1887 in the *Unua Libro*, which the spec cites. Its spelling was designed to be phonemic. The English edition of that book gives two general rules (Zamenhof 1889, p. 26). The first is "Pronounce each word as it is written". The second is "Accent the syllable before the last". The *Fundamento de Esperanto* gives the same two rules as rules 9 and 10 of its grammar. It adds that "there are no silent letters" (Zamenhof 1905, p. 10).

The `eo` spec follows these two rules. It reads each letter as one sound, with no rule that depends on context, and it puts the stress on the penult. Esperanto is the limiting case of a shallow orthography. So the production bar for this spec is a PER of 0.15 ([quality tiers](../specs/quality_tiers.md#the-per-threshold)).

## The alphabet

The alphabet has 28 letters (Zamenhof 1889, p. 23). Six of them carry a diacritic: ⟨ĉ ĝ ĥ ĵ ŝ⟩ have a circumflex and ⟨ŭ⟩ has a breve. Five letters are vowels, ⟨a e i o u⟩, and the other 23 are consonants and semivowels.

The *Fundamento* gives each letter an English key word (Zamenhof 1905, p. 7). The spec follows that key. The letter ⟨c⟩ is the [ts] of *wits*, ⟨ĉ⟩ is the [tʃ] of *church* and ⟨ĝ⟩ is the [dʒ] of *join*. The letter ⟨ĥ⟩ is "strongly aspirated", like Scottish *loch*, and the spec writes it as [x]. The letter ⟨ĵ⟩ is the [ʒ] of *azure* and ⟨ŝ⟩ is the [ʃ] of *show*. So `ĉambro` 'room' is [ˈtʃambro], `ĥoro` 'choir' is [ˈxoro] and `ĵurnalo` 'newspaper' is [ʒurˈnalo].

The semivowels are ⟨j⟩, the *y* of *yoke*, and ⟨ŭ⟩, the second part of the diphthong in *mount* (Zamenhof 1889, p. 23). The spec has no diphthong graphemes. It writes ⟨j⟩ as [j] and ⟨ŭ⟩ as [w], so `aŭto` 'car' is [ˈawto] and `patroj` 'fathers' is [ˈpatroj].

## Stress

Stress always falls on the penult (Zamenhof 1905, p. 10, rule 10). The `stress` block of the spec states this with `default_position: -2`. So `Esperanto` is [espeˈranto], `ĝardeno` 'garden' is [dʒarˈdeno] and `vaporŝipo` 'steamship' is [vaporˈʃipo]. The engine writes a stress mark on each word, the one-syllable words too.

## Reading the datasets

Five provenance tiers never gate a promotion: the three that name a competing tool (`espeak-derived`, `epitran-derived` and `lupo-derived`) and the two language-model tiers ([which gold can gate](../specs/quality_tiers.md#which-gold-can-gate)). The `Gates` column of the Datasets block below gives the rows that gate.

The `wikipron` row is crowd-scraped. WikiPron ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) scrapes the IPA of English Wiktionary. The Esperanto entries `ĝardeno`, `radio`, `familio` and `hodiaŭ` do not type their IPA. They call the template `{{eo-pr}}`, which runs [Module:eo-pron](https://en.wiktionary.org/wiki/Module:eo-pron). Where an entry does that, the gold is the output of the module. The row then measures agreement with a rule system, like the [module-generated rows](../evaluation/datasets.md#module-generated-wikipron-rows) of the dataset catalogue.

The module and the spec use different symbols for one sound. The module writes the ⟨ŭ⟩ of [`hodiaŭ`](https://en.wiktionary.org/wiki/hodia%C5%AD) as [u̯], in /hoˈdiau̯/, and the spec writes [w]. The scorer counts that difference as an error.

The `ipadict` row is machine-generated. The dataset catalogue records no source for the Esperanto file of ipa-dict, so the row shows agreement with an unknown tool.

## Weak points

The engine counts two vowels next to each other as one syllable when it places the stress. The penult rule counts each vowel as a syllable. So the stress falls one syllable too early in many words with a vowel sequence.

| Spelling | Penult by rule 10 | Engine output |
|:--|:--|:--|
| ideo 'idea' | i-DE-o | [ˈideo] |
| radio | ra-DI-o | [ˈradio] |
| kafeo 'coffee' | ka-FE-o | [ˈkafeo] |
| familio 'family' | fa-mi-LI-o | [faˈmilio] |
| poezio 'poetry' | po-e-ZI-o | [ˈpoezio] |
| hodiaŭ 'today' | ho-DI-aŭ | [ˈhodiaw] |

Wiktionary gives /famiˈlio/ for [`familio`](https://en.wiktionary.org/wiki/familio) and /hoˈdiau̯/ for `hodiaŭ`, in line with rule 10. Some words have their vowel sequence at the end and only two syllables. Examples are `mia` 'my' [ˈmia] and `fluo` 'flow' [ˈfluo]. These come out right, because the penult is the first syllable in both counts.

The engine reads only the circumflex and breve letters. The *Fundamento* gives a substitute for a printer with no such type (Zamenhof 1905, p. 7). The printer writes ⟨h⟩ after the letter in place of the circumflex. The printer leaves out the breve. The engine reads that ⟨h⟩ as a letter of its own, so `chambro` comes out as [ˈtshambro], not as `ĉambro` [ˈtʃambro]. Wiktionary lists a second substitute, the X-system, which writes ⟨x⟩ after the letter, as in [`cxambro`](https://en.wiktionary.org/wiki/cxambro). The spec has no ⟨x⟩, so the engine drops it, and `cxambro` comes out as [ˈtsambro].

In elementary works, the *Fundamento* separates the parts of a compound word with an apostrophe, as in `vapor'ŝip'o` 'steamboat' (Zamenhof 1905, p. 10, rule 11). The engine splits the word at each apostrophe and stresses each part. So `vapor'ŝip'o` comes out as [ˈvapor ˈʃip ˈo], but `vaporŝipo` is [vaporˈʃipo].

The *Fundamento* also lets the ⟨a⟩ of the article and the final ⟨o⟩ of a noun drop (Zamenhof 1905, p. 11, rule 16). An apostrophe takes the place of the vowel, as in `de l' mond'o`. The engine gives the bare ⟨l⟩ a stress mark of its own, [ˈde ˈl ˈmond ˈo]. It also counts the syllables of the short form. So `Ŝiller'`, which stands for `Ŝillero`, comes out as [ˈʃiller]. The full form `Ŝillero` is [ʃilˈlero].

<!-- atlas:lects begin -->
## Related lects

No spec names `eo` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL.

1. <a id="src-zamenhof1887"></a>Zamenhof, L.L. (1887). *Unua Libro (An International Language)*. self-published.
2. <a id="src-esperanto_phonology_wiki"></a>Wikipedia contributors (2024). *Esperanto phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Esperanto_phonology)
<!-- atlas:sources end -->

### Notes on the sources

The page numbers on this page come from two editions that the spec does not list. The first is the English edition of the *Unua Libro*: Zamenhof, L. L. (1889), *An Attempt Towards an International Language*, translated by Henry Phillips, New York, Henry Holt ([scan on archive.org](https://archive.org/details/AnAttemptTowardsAnInternationalLanguage)). The second is Zamenhof, L. L. (1905), *Fundamento de Esperanto*, Paris, Hachette, with its English grammar on pp. 7-11 ([scan on archive.org](https://archive.org/details/fundamentodeesp00zamegoog)). Both scans are in the public domain.

The stress notes of the spec name the *Fundamento* (1905) and Wells (1989). Neither work is in its list of sources.


<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `eo` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 41245 | 0.0328 | yes |
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `eo` | generated | machine-generated | MIT, each file its own | 23245 | 0.0120 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 28 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  | ts | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  |  |  |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open | a |  |

Sequences that the spec writes as one unit: [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [ts] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨z⟩ | [z] |  |
| ⟨ĉ⟩ | [tʃ] |  |
| ⟨ĝ⟩ | [dʒ] |  |
| ⟨ĥ⟩ | [x] |  |
| ⟨ĵ⟩ | [ʒ] |  |
| ⟨ŝ⟩ | [ʃ] |  |
| ⟨ŭ⟩ | [w] |  |

Stress falls on the penult by default.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin words="Esperanto|ĝardeno|vaporŝipo|ĉambro|ĥoro|ĵurnalo|aŭto|patroj|mia|fluo|ideo|radio|kafeo|familio|poezio|hodiaŭ|chambro|cxambro|vapor'ŝip'o|de l' mond'o|Ŝiller'|Ŝillero" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "eo")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| Esperanto | [espeˈranto] |
| ĝardeno | [dʒarˈdeno] |
| vaporŝipo | [vaporˈʃipo] |
| ĉambro | [ˈtʃambro] |
| ĥoro | [ˈxoro] |
| ĵurnalo | [ʒurˈnalo] |
| aŭto | [ˈawto] |
| patroj | [ˈpatroj] |
| mia | [ˈmia] |
| fluo | [ˈfluo] |
| ideo | [ˈideo] |
| radio | [ˈradio] |
| kafeo | [ˈkafeo] |
| familio | [faˈmilio] |
| poezio | [ˈpoezio] |
| hodiaŭ | [ˈhodiaw] |
| chambro | [ˈtshambro] |
| cxambro | [ˈtsambro] |
| vapor'ŝip'o | [ˈvapor ˈʃip ˈo] |
| de l' mond'o | [ˈde ˈl ˈmond ˈo] |
| Ŝiller' | [ˈʃiller] |
| Ŝillero | [ʃilˈlero] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Erzya](myv.md) · [Home](../index.md) · [Estonian →](et.md)
