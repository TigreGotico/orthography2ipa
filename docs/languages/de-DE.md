# German (`de-DE`)

<!-- atlas:summary begin -->
German is a West Germanic language, written in the Latin script. Its code names Germany. The `de-DE` spec is at the research tier. It cites 6 sources and has 3 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `de-DE` |
| Aliases | `deu` |
| ISO 639-3 | [deu](https://iso639-3.sil.org/code/deu), German |
| Glottolog | [stan1295](https://glottolog.org/resource/languoid/id/stan1295), German |
| Wikidata | [Q188](https://www.wikidata.org/wiki/Q188) |
| Wikipedia | [German language](https://en.wikipedia.org/wiki/German_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > West Germanic](by-family.md#indo-european--germanic--northwest-germanic--west-germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [Germany](by-region.md#germany) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1700, living |
| Parent | [West Germanic](https://tigregotico.github.io/orthography2ipa/#x-clade-west2793) `x-clade-west2793` |
| Child lects | 2, see [Related lects](#related-lects) |
| Explorer | [`de-DE` in the data explorer](https://tigregotico.github.io/orthography2ipa/#de-DE) |
| Spec file | [`de-DE.json`](../../orthography2ipa/data/de-DE.json) |
<!-- atlas:header end -->

## Overview

The `de-DE` spec describes Standard German after Wiese (1996), Hall (2003), the Duden pronouncing dictionary (Mangold 2005) and the IPA Illustration by Kohler (1990). German has a deep orthography, so the deep threshold of 0.25 PER applies to a promotion (see [quality tiers](../specs/quality_tiers.md#the-per-threshold)). The spec is at `research` tier. For its scores on the WikiPron gold, see the [scoreboard](../evaluation/generated/scoreboard.md).

## Consonants

The spec maps the consonant letters to this inventory:

| Manner | Bilabial | Labiodental | Alveolar | Palato-alveolar | Palatal | Velar | Uvular or glottal |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Plosive | p b | | t d | | | k ɡ | |
| Affricate | pf | | ts | tʃ | | | |
| Fricative | | f v | s z | ʃ | ç | x | ʁ h |
| Nasal | m | | n | | | ŋ | |
| Lateral | | | l | | | | |
| Approximant | | | | | j | | |

### Final devoicing

German obstruents are voiceless at the end of a word (Auslautverhärtung). The examples are from Wiese (1996):

| Voiced (onset) | Voiceless (word-final) | Example |
|:---:|:---:|:---|
| b | p | `Grab` [ɡʁaːp] against `graben` [ɡʁaːbən] |
| d | t | `Hund` [hʊnt] against `Hunde` [hʊndə] |
| ɡ | k | `Tag` [taːk] against `Tage` [taːɡə] |
| v | f | `brav` [bʁaːf] against `brave` [bʁaːvə] |

The spec states the rule as a `word_final` entry on ⟨b d g v⟩ in `positional_graphemes`:

```json
"b": {"word_final": ["p"], "default": ["b"]}
```

The rule covers only the absolute end of the word. The engine has a `coda` position, but the spec does not use it for these letters. So a coda inside a word keeps its voiced value. The spec gives `ˈabʃiːt` for `Abschied` and `ˈjaɡt` for `Jagd`, where the grammars have [p] and [k].

The spec gives ⟨s⟩ the value [z] at the start of a word and between vowels, as in `sagen` [zaːɡən] and `lesen`. The `word_initial` entry does not check the next letter, so it also voices ⟨s⟩ before a consonant. The spec gives `ˈzkat` for `Skat`.

### Ach-Laut and ich-Laut

The digraph ⟨ch⟩ has two main values. The preceding vowel selects the value (Kohler 1990, Wiese 1996):

| Environment | Value | Examples |
|:---|:---:|:---|
| After a, o, u (back vowels) | [x] (ach-Laut, velar fricative) | `Bach` [bax], `noch` [nɔx], `Buch` [buːx] |
| After e, i (front vowels), after consonants, word-initially | [ç] (ich-Laut, palatal fricative) | `ich` [ɪç], `echt` [ɛçt], `Milch` [mɪlç] |
| Classical loanwords (word-initial) | [k] | `Charakter` [kaˈʁaktɐ], `Chor` [koːɐ̯] |

The spec states this in `positional_graphemes`:

```json
"ch": {
  "after_a": ["x", "ç"],
  "after_o": ["x", "ç"],
  "after_u": ["x", "ç"],
  "after_e": ["ç", "x"],
  "after_i": ["ç", "x"],
  "after_vowel": ["ç", "x"],
  "word_initial": ["k", "ç"],
  "default": ["ç"]
}
```

The `after_a` to `after_u` positions exist only for the five plain vowel letters. After ⟨ä ö ü⟩, ⟨ch⟩ takes the generic `after_vowel` entry, which ranks [ç] first. That is correct, because the umlaut vowels are front vowels (`Bücher`, `Löcher`). A diphthong grapheme counts by its first letter. So ⟨au⟩ selects `after_a` and gives [x] in `Bauch`, and ⟨eu⟩ selects `after_e` and gives [ç] in `euch`.

### Initial sp and st

At the start of a word, ⟨sp⟩ is [ʃp] and ⟨st⟩ is [ʃt]. In other positions they are [sp] and [st]. The spec has a `word_initial` entry for each digraph.

| Position | ⟨sp⟩ | ⟨st⟩ | Examples |
|:---|:---:|:---:|:---|
| Word-initial | [ʃp] | [ʃt] | `spielen` [ʃpiːlən], `stark` [ʃtaʁk] |
| Not initial | [sp] | [st] | `Wespe` [vɛspə], `Fenster` [fɛnstɐ] |

### Final -ig

Word-final ⟨-ig⟩ is [ɪç], as in `König` and `ewig`. The spec does not treat ⟨ig⟩ as a grapheme. The allophone rule `DE_FINAL_IG_SPIRANT` changes the [k] of a word-final ⟨g⟩ after [ɪ] to [ç]. The spec gives `ˈkøːnɪç` for `König`.

## Vowels

Each German vowel letter has a short and a long value, and ⟨e⟩ also has schwa. The examples are from the cited grammars:

| Grapheme | IPA | Length | Example |
|:---:|:---:|:---:|:---|
| a | [a] / [aː] | short/long | `Mann` [man] / `Bahn` [baːn] |
| e | [ɛ] / [eː] / [ə] | short/long/schwa | `Bett` [bɛt] / `See` [zeː] / `bitte` [bɪtə] |
| i | [ɪ] / [iː] | short/long | `mit` [mɪt] / `Lied` [liːt] |
| o | [ɔ] / [oː] | short/long | `voll` [fɔl] / `Boot` [boːt] |
| u | [ʊ] / [uː] | short/long | `Hund` [hʊnt] / `gut` [ɡuːt] |
| ä | [ɛ] / [ɛː] | short/long | `Männer` [mɛnɐ] / `Mädchen` [mɛːtçən] |
| ö | [œ] / [øː] | short/long | `können` [kœnən] / `hören` [høːʁən] |
| ü | [ʏ] / [yː] | short/long | `dünn` [dʏn] / `kühn` [kyːn] |

The spec lists the short value first. The `DE_OPEN_SYLLABLE_*` allophone rules give the long value to a vowel in an open syllable, before one consonant and a vowel. The `DE_UNSTRESSED_TENSE_*` rules give the tense short value [i o u y] to an unstressed vowel before the stress and at the end of a word (Wiese 1996, ch. 2).

Unstressed ⟨e⟩ is [ə] through the `nucleus_unstressed` position, and word-final ⟨er⟩ is [ɐ], as in `Mutter`. A vowel letter followed by the lengthening ⟨h⟩ is one long-vowel grapheme, such as ⟨ah⟩ [aː] in `Bahn`. Before a vowel, the spec keeps the [h] of these graphemes and gives `ˈɡeːhən` for `gehen`.

### Diphthongs

| Grapheme | IPA | Example |
|:---:|:---:|:---|
| ei, ai | [aɪ̯] | `Eis` [aɪ̯s], `Mai` [maɪ̯] |
| au | [aʊ̯] | `Haus` [haʊ̯s] |
| eu, äu | [ɔʏ̯] | `neu` [nɔʏ̯], `Häuser` [hɔʏ̯zɐ] |

The spec writes the diphthongs as `aɪ`, `aʊ` and `ɔʏ`, without the non-syllabic mark.

## Stress

The `stress` block puts stress on the first syllable, which is the Germanic default (Wiese 1996, ch. 8). A closed set of suffixes attracts final stress: -ion, -tät, -ei, -eur, -ent, -ant, -enz, -anz, -ös, -iv, -ur and -al. The suffixes -ieren and -ismus take stress on the penult. The spec gives `naˈtsi̯oːn` for `Nation` and `ʃtuˈdiːʁən` for `studieren`.

The unstressed prefixes be-, ge-, ver-, ent-, er-, zer- and emp- move stress in ways that no suffix rule captures. The spec notes record this gap. Loanword stress is also outside the block, so the spec gives `ˈkaːʁaktɐ` for `Charakter`.

## Word exceptions

The `word_exceptions` table holds two closed sets. The first is the -sal nouns, such as `Schicksal`, `Trübsal` and `Labsal`, where ⟨s⟩ begins a suffix after a consonant and is voiced. The second is the grammatical terms in -tiv, such as `Genitiv` and `Dativ`.

## Positional rules

| Grapheme | Environment | Value | Mechanism |
|:---:|:---|:---:|:---|
| b, d, g, v | word-final | p, t, k, f | `positional_graphemes`, `word_final` |
| s | word-initial, intervocalic | z | `positional_graphemes` |
| ch | after a, o, u | x | `positional_graphemes`, `after_a` to `after_u` |
| ch | after e, i and other vowels | ç | `positional_graphemes`, `after_e`, `after_i`, `after_vowel` |
| sp, st | word-initial | ʃp, ʃt | `positional_graphemes`, `word_initial` |
| e | unstressed nucleus | ə | `positional_graphemes`, `nucleus_unstressed` |
| er | word-final | ɐ | `positional_graphemes`, `word_final` |
| g | word-final after [ɪ] | ç | allophone rule `DE_FINAL_IG_SPIRANT` |

## Glottal stop

Careful Standard German often puts a glottal stop [ʔ] before a vowel at the start of a word or a stressed syllable, as in `Oase` [ʔoˈʔaːzə] (Kohler 1990). It is not phonemic. It is much more frequent in northern varieties than in the south, and colloquial speech often leaves it out ([German phonology](https://en.wikipedia.org/wiki/German_phonology)). The WikiPron gold does not write it. The spec does not insert it, because the gold would count each inserted [ʔ] as an error.

<!-- atlas:lects begin -->
## Related lects

These specs name `de-DE` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Austrian German](https://tigregotico.github.io/orthography2ipa/#de-AT) `de-AT`: Austria, skeleton tier
- [Swiss Standard German (Hochdeutsch)](de-CH.md) `de-CH`: Switzerland, research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 6 works. 2 of them have a DOI or a URL. The spec file holds a note on what 3 of them support.

1. <a id="src-wiese1996"></a>Wiese, R. (1996). *The Phonology of German*. Oxford University Press.
2. <a id="src-hall2003"></a>Hall, T.A. (2003). *Phonologie des Deutschen: eine Einführung*. de Gruyter.
3. <a id="src-mangold2005"></a>Mangold, M. (2005). *Duden Aussprachewörterbuch (6th ed.)*. Dudenverlag.
4. <a id="src-kohler1990"></a>Kohler, K. J. (1990). *Illustrations of the IPA: German*. Journal of the International Phonetic Association 20(1).
5. <a id="src-wikipedia_german_phonology"></a>Wikipedia contributors (2026). *German phonology*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/German_phonology)
6. <a id="src-wikipedia_german_orthography"></a>Wikipedia contributors (2026). *German orthography*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/German_orthography)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `de-DE` | gold | crowd-scraped | MIT, each file its own | 777785 | 0.2303 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `de` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 53010 | 0.2103 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `de-DE` | generated | epitran-derived | CC BY 4.0 | 24857 | 0.3948 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 70 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  |  | k kʰ ɡ |  |  |
| Affricate |  | pf | ts | tʃ |  |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  | ʀ |  |
| Fricative |  | f v | s z | ʃ | ç | x | ʁ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː y yː |  | u uː |
| Near-close | ɪ ʏ |  | ʊ |
| Close-mid | eː øː |  | o oː |
| Mid |  | ə |  |
| Open-mid | œ ɛ ɛː |  | ɔ |
| Near-open |  | ɐ ɐ̯ |  |
| Open | a aː |  |  |

Sequences that the spec writes as one unit: [aɪ] [aʊ] [aːh] [eːh] [iːh] [ks] [kv] [oːh] [sp] [st] [tsi̯oːn] [uːh] [yːh] [øːh] [ŋk] [ɔʏ] [ɛʁ] [ɛːh] [ʃp] [ʃt].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] [aː] |  |
| ⟨aa⟩ | [aː] |  |
| ⟨ah⟩ | [aː] | before vowel [aːh] · default [aː] |
| ⟨ai⟩ | [aɪ] |  |
| ⟨au⟩ | [aʊ] |  |
| ⟨b⟩ | [b] | default [b] · word final [p] |
| ⟨c⟩ | [k] [ts] |  |
| ⟨ch⟩ | [ç] [x] | after a [x] [ç] · after e [ç] [x] · after i [ç] [x] · after o [x] [ç] · after u [x] [ç] · after vowel [ç] [x] · default [ç] · word initial [k] [ç] |
| ⟨ck⟩ | [k] |  |
| ⟨d⟩ | [d] | default [d] · word final [t] |
| ⟨e⟩ | [ɛ] [eː] [ə] | default [ɛ] [eː] [ə] · nucleus stressed [ɛ] · nucleus unstressed [ə] |
| ⟨ee⟩ | [eː] |  |
| ⟨eh⟩ | [eː] | before vowel [eːh] · default [eː] |
| ⟨ei⟩ | [aɪ] |  |
| ⟨er⟩ | [ɛʁ] [ɐ] | default [ɛʁ] · word final [ɐ] |
| ⟨eu⟩ | [ɔʏ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] | default [ɡ] · word final [k] |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ɪ] [iː] |  |
| ⟨ie⟩ | [iː] |  |
| ⟨ih⟩ | [iː] | before vowel [iːh] · default [iː] |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nk⟩ | [ŋk] |  |
| ⟨o⟩ | [ɔ] [oː] |  |
| ⟨oh⟩ | [oː] | before vowel [oːh] · default [oː] |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨pf⟩ | [pf] |  |
| ⟨ph⟩ | [f] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [kv] |  |
| ⟨r⟩ | [ʁ] |  |
| ⟨s⟩ | [z] [s] | default [s] · intervocalic [z] · word final [s] · word initial [z] |
| ⟨sch⟩ | [ʃ] |  |
| ⟨ss⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [t] |  |
| ⟨tion⟩ | [tsi̯oːn] |  |
| ⟨tsch⟩ | [tʃ] |  |
| ⟨tz⟩ | [ts] |  |
| ⟨u⟩ | [ʊ] [uː] |  |
| ⟨uh⟩ | [uː] | before vowel [uːh] · default [uː] |
| ⟨v⟩ | [f] [v] | default [v] · word final [f] |
| ⟨w⟩ | [v] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [ʏ] [yː] |  |
| ⟨z⟩ | [ts] |  |
| ⟨ß⟩ | [s] |  |
| ⟨ä⟩ | [ɛ] [ɛː] |  |
| ⟨äh⟩ | [ɛː] | before vowel [ɛːh] · default [ɛː] |
| ⟨äu⟩ | [ɔʏ] |  |
| ⟨ö⟩ | [œ] [øː] |  |
| ⟨öh⟩ | [øː] | before vowel [øːh] · default [øː] |
| ⟨ü⟩ | [ʏ] [yː] |  |
| ⟨üh⟩ | [yː] | before vowel [yːh] · default [yː] |

Stress falls on the first syllable by default. These endings take final stress: ⟨-ion⟩ ⟨-tät⟩ ⟨-ei⟩ ⟨-eur⟩ ⟨-ent⟩ ⟨-ant⟩ ⟨-enz⟩ ⟨-anz⟩ ⟨-ös⟩ ⟨-iv⟩ ⟨-ur⟩ ⟨-al⟩. These endings take the penult: ⟨-ieren⟩ ⟨-ismus⟩.

Whole-word exceptions (14): ⟨akkusativ⟩ [ˈakuzatiːf], ⟨dativ⟩ [ˈdaːtiːf], ⟨drangsal⟩ [ˈdʁaŋzaːl], ⟨genitiv⟩ [ˈɡeːnitiːf], ⟨imperativ⟩ [ˈɪmperatiːf], ⟨infinitiv⟩ [ˈɪnfinitiːf], ⟨komparativ⟩ [ˈkɔmparatiːf], ⟨labsal⟩ [ˈlaːpzaːl], ⟨mühsal⟩ [ˈmyːzaːl], ⟨nominativ⟩ [ˈnoːminatiːf], ⟨scheusal⟩ [ˈʃɔʏzaːl], ⟨schicksal⟩ [ˈʃɪkzaːl], ⟨superlativ⟩ [ˈzuːpɐlatiːf], ⟨trübsal⟩ [ˈtʁyːpzaːl].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 16 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `DE_FINAL_IG_SPIRANT` | /k/ → [ç], word-finally, after [ɪ], spelled ⟨g⟩ | - | - |
| `DE_OPEN_SYLLABLE_A` | /a/ → [aː], stressed, in the nucleus, before a consonant, spelled ⟨a⟩, with more context in the spec | - | [Wiese 1996](#src-wiese1996) |
| `DE_OPEN_SYLLABLE_E` | /ɛ/ → [eː], stressed, in the nucleus, before a consonant, spelled ⟨e⟩, with more context in the spec | - | [Wiese 1996](#src-wiese1996) |
| `DE_OPEN_SYLLABLE_I` | /ɪ/ → [iː], stressed, in the nucleus, before a consonant, spelled ⟨i⟩, with more context in the spec | - | [Wiese 1996](#src-wiese1996) |
| `DE_OPEN_SYLLABLE_O` | /ɔ/ → [oː], stressed, in the nucleus, before a consonant, spelled ⟨o⟩, with more context in the spec | - | [Wiese 1996](#src-wiese1996) |
| `DE_OPEN_SYLLABLE_U` | /ʊ/ → [uː], stressed, in the nucleus, before a consonant, spelled ⟨u⟩, with more context in the spec | - | [Wiese 1996](#src-wiese1996) |
| `DE_OPEN_SYLLABLE_OE` | /œ/ → [øː], stressed, in the nucleus, before a consonant, spelled ⟨ö⟩, with more context in the spec | - | [Wiese 1996](#src-wiese1996) |
| `DE_OPEN_SYLLABLE_UE` | /ʏ/ → [yː], stressed, in the nucleus, before a consonant, spelled ⟨ü⟩, with more context in the spec | - | [Wiese 1996](#src-wiese1996) |
| `DE_UNSTRESSED_TENSE_I_FINAL` | /ɪ/ → [i], word-finally, unstressed, spelled ⟨i⟩ | ⟨Politik⟩ [poli-] | [Wiese 1996](#src-wiese1996) |
| `DE_UNSTRESSED_TENSE_O_FINAL` | /ɔ/ → [o], word-finally, unstressed, spelled ⟨o⟩ | ⟨Politik⟩ [poli-] | [Wiese 1996](#src-wiese1996) |
| `DE_UNSTRESSED_TENSE_U_FINAL` | /ʊ/ → [u], word-finally, unstressed, spelled ⟨u⟩ | - | [Wiese 1996](#src-wiese1996) |
| `DE_UNSTRESSED_TENSE_Y_FINAL` | /ʏ/ → [y], word-finally, unstressed, spelled ⟨y⟩ | - | [Wiese 1996](#src-wiese1996) |
| `DE_UNSTRESSED_TENSE_I_PRETONIC` | /ɪ/ → [i], pretonic, before a consonant, spelled ⟨i⟩, with more context in the spec | ⟨Politik⟩ [poli-] | [Wiese 1996](#src-wiese1996) |
| `DE_UNSTRESSED_TENSE_O_PRETONIC` | /ɔ/ → [o], pretonic, before a consonant, spelled ⟨o⟩, with more context in the spec | ⟨Politik⟩ [poli-] | [Wiese 1996](#src-wiese1996) |
| `DE_UNSTRESSED_TENSE_U_PRETONIC` | /ʊ/ → [u], pretonic, before a consonant, spelled ⟨u⟩, with more context in the spec | - | [Wiese 1996](#src-wiese1996) |
| `DE_UNSTRESSED_TENSE_Y_PRETONIC` | /ʏ/ → [y], pretonic, before a consonant, spelled ⟨y⟩, with more context in the spec | - | [Wiese 1996](#src-wiese1996) |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="Grab|graben|Hund|Hunde|Tag|brav|Bach|noch|ich|Milch|Charakter|spielen|Wespe|Fenster" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "de-DE")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| Grab | [ˈɡʁap] |
| graben | [ˈɡʁaːbən] |
| Hund | [ˈhʊnt] |
| Hunde | [ˈhʊndə] |
| Tag | [ˈtak] |
| brav | [ˈbʁaf] |
| Bach | [ˈbax] |
| noch | [ˈnɔx] |
| ich | [ˈɪç] |
| Milch | [ˈmɪlç] |
| Charakter | [ˈkaːʁaktɐ] |
| spielen | [ˈʃpiːlən] |
| Wespe | [ˈveːspə] |
| Fenster | [ˈfɛnstɐ] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Georgian](ka.md) · [Home](../index.md) · [Gilyak →](niv.md)
