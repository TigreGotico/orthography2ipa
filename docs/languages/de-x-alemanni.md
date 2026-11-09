# Alemannic German (`de-x-alemanni`)

<!-- atlas:summary begin -->
Alemannic German is a West Germanic variety, written in the Latin script. Glottolog places it in the Eurasia and South America macroareas. The `de-x-alemanni` spec is at the research tier. It cites 4 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `de-x-alemanni` |
| Aliases | `de-x-alemannic` |
| ISO 639-3 | [gsw](https://iso639-3.sil.org/code/gsw), Swiss German |
| Glottolog | [alem1243](https://glottolog.org/resource/languoid/id/alem1243), Alemannic |
| Wikidata | [Q131339](https://www.wikidata.org/wiki/Q131339) |
| Wikipedia | [Alemannic German](https://en.wikipedia.org/wiki/Alemannic_German) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > West Germanic](by-family.md#indo-european--germanic--northwest-germanic--west-germanic) |
| Region | [Eurasia](by-region.md#several-macroareas), [South America](by-region.md#several-macroareas) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1000, living |
| Parent | [Swiss Standard German (Hochdeutsch)](de-CH.md) `de-CH` |
| Explorer | [`de-x-alemanni` in the data explorer](https://tigregotico.github.io/orthography2ipa/#de-x-alemanni) |
| Spec file | [`de-x-alemanni.json`](../../orthography2ipa/data/de-x-alemanni.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Alemannic German (Schwyzerdütsch, Alsatian, Swabian, Vorarlbergisch), ISO 639-3 gsw. This is the DIALECT, not Schweizerhochdeutsch: the parent de-CH models Swiss Standard German, which is Standard German with Swiss features and shares the de-DE grapheme table.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1938 to 2000. [Sources](#sources) lists them. The spec file writes 34 of the 74 spellings of its letter table and takes the other 40 from [Swiss Standard German (Hochdeutsch)](de-CH.md) `de-CH`.

The [spec file](../../orthography2ipa/data/de-x-alemanni.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `de-x-alemanni` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 0 of them have a DOI or a URL. The spec file holds a note on what 2 of them support.

1. <a id="src-wiese1996"></a>Wiese, R. (1996). *The Phonology of German*. Oxford University Press.
2. <a id="src-russ1994"></a>Russ, C. (1994). *The Dialects of Modern German*. Routledge.
3. <a id="src-haas2000"></a>Haas, W. (2000). *Die deutschsprachige Schweiz*. Sauerländer.
4. <a id="src-dieth1938"></a>Dieth, E. (1938). *Schwyzertütschi Dialäktschrift*. Orell Füssli.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `de-x-alemanni` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 448 | 0.1736 | yes |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 83 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  |  | k kʰ kː ɡ |  |  |
| Affricate |  | pf | ts | tʃ |  | kx |  |  |
| Nasal | m |  | n |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  | f v | s sː z | ʃ | ç | x | χ | h |
| Approximant |  | ʋ |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː y yː |  | u uː |
| Near-close | ɪ ʏ |  | ʊ |
| Close-mid | e eː ø øː |  | o oː |
| Mid |  | ə |  |
| Open-mid | œ ɛ ɛː |  | ɔ |
| Near-open | æ æː | ɐ |  |
| Open | a aː |  | ɑ ɑː |

Sequences that the spec writes as one unit: [aɪ] [aʊ] [aːh] [eːh] [iə] [iːh] [ks] [kv] [oːh] [sp] [st] [tsi̯oːn] [uə] [uːh] [yə] [yːh] [øːh] [ŋk] [ŋkx] [ɔʏ] [ər] [ɛʁ] [ɛːh] [ʃp] [ʃt].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ɑ] [a] |  |
| ⟨aa⟩ | [ɑː] |  |
| ⟨ah⟩ | [aː] | before vowel [aːh] · default [aː] |
| ⟨ai⟩ | [aɪ] |  |
| ⟨au⟩ | [aʊ] |  |
| ⟨b⟩ | [b] | default [b] · word final [p] |
| ⟨c⟩ | [k] [ts] |  |
| ⟨ch⟩ | [x] [χ] | after a [x] [χ] · after e [x] [χ] · after i [x] [χ] · after o [x] [χ] · after u [x] [χ] · after vowel [x] [χ] · default [x] [χ] · word initial [x] [χ] |
| ⟨ck⟩ | [kx] [k] |  |
| ⟨d⟩ | [d] | default [d] · word final [t] |
| ⟨e⟩ | [ɛ] [eː] [ə] | default [ə] [e] [ɛ] · nucleus stressed [e] [ɛ] · nucleus unstressed [ə] |
| ⟨ee⟩ | [eː] |  |
| ⟨eh⟩ | [eː] | before vowel [eːh] · default [eː] |
| ⟨ei⟩ | [aɪ] |  |
| ⟨er⟩ | [ɛʁ] [ɐ] | default [ər] · word final [ər] |
| ⟨eu⟩ | [ɔʏ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] | default [ɡ] · word final [k] |
| ⟨gg⟩ | [k] [kː] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ie⟩ | [iə] |  |
| ⟨ih⟩ | [iː] | before vowel [iːh] · default [iː] |
| ⟨ii⟩ | [iː] |  |
| ⟨j⟩ | [j] |  |
| ⟨k⟩ | [kx] [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨nk⟩ | [ŋkx] [ŋk] |  |
| ⟨nn⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨oh⟩ | [oː] | before vowel [oːh] · default [oː] |
| ⟨oo⟩ | [oː] |  |
| ⟨p⟩ | [p] |  |
| ⟨pf⟩ | [pf] |  |
| ⟨ph⟩ | [f] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [kv] |  |
| ⟨r⟩ | [r] |  |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] | default [s] · intervocalic [s] · word final [s] · word initial [s] |
| ⟨sch⟩ | [ʃ] |  |
| ⟨ss⟩ | [sː] [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [t] |  |
| ⟨tion⟩ | [tsi̯oːn] |  |
| ⟨tsch⟩ | [tʃ] |  |
| ⟨tz⟩ | [ts] |  |
| ⟨u⟩ | [u] |  |
| ⟨ue⟩ | [uə] |  |
| ⟨uh⟩ | [uː] | before vowel [uːh] · default [uː] |
| ⟨uu⟩ | [uː] |  |
| ⟨v⟩ | [f] [v] | default [v] · word final [f] |
| ⟨w⟩ | [v] [ʋ] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [iː] |  |
| ⟨yy⟩ | [iː] |  |
| ⟨z⟩ | [ts] |  |
| ⟨ß⟩ | [s] |  |
| ⟨ä⟩ | [æ] [ɛ] |  |
| ⟨äh⟩ | [ɛː] | before vowel [ɛːh] · default [ɛː] |
| ⟨äu⟩ | [ɔʏ] |  |
| ⟨ää⟩ | [æː] |  |
| ⟨ö⟩ | [ø] |  |
| ⟨öh⟩ | [øː] | before vowel [øːh] · default [øː] |
| ⟨öö⟩ | [øː] |  |
| ⟨ü⟩ | [y] |  |
| ⟨üe⟩ | [yə] |  |
| ⟨üh⟩ | [yː] | before vowel [yːh] · default [yː] |
| ⟨üü⟩ | [yː] |  |

Stress falls on the first syllable by default. These endings take final stress: ⟨-ion⟩ ⟨-tät⟩ ⟨-ei⟩ ⟨-eur⟩ ⟨-ent⟩ ⟨-ant⟩ ⟨-enz⟩ ⟨-anz⟩ ⟨-ös⟩ ⟨-iv⟩ ⟨-ur⟩ ⟨-al⟩. These endings take the penult: ⟨-ieren⟩ ⟨-ismus⟩.
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

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "de-x-alemanni")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Albanian](sq.md) · [Home](../index.md) · [Algerian Arabic →](arq-DZ.md)
