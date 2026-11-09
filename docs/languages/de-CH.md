# Swiss Standard German (Hochdeutsch) (`de-CH`)

<!-- atlas:summary begin -->
Swiss Standard German (Hochdeutsch) is a West Germanic language, written in the Latin script. Its code names Switzerland. The `de-CH` spec is at the research tier. It cites 2 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `de-CH` |
| ISO 639-3 | [deu](https://iso639-3.sil.org/code/deu), German |
| Wikidata | [Q1366643](https://www.wikidata.org/wiki/Q1366643) |
| Wikipedia | [Swiss Standard German](https://en.wikipedia.org/wiki/Swiss_Standard_German) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > West Germanic](by-family.md#indo-european--germanic--northwest-germanic--west-germanic) |
| Region | [Eurasia](by-region.md#eurasia) > [Switzerland](by-region.md#switzerland) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1800, living |
| Parent | [German](de-DE.md) `de-DE` |
| Child lects | 1, see [Related lects](#related-lects) |
| Explorer | [`de-CH` in the data explorer](https://tigregotico.github.io/orthography2ipa/#de-CH) |
| Spec file | [`de-CH.json`](../../orthography2ipa/data/de-CH.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Swiss Standard German (Schweizer Hochdeutsch). NO glottal stop /ʔ/, absent from Swiss German phonology. /r/ = alveolar trill [r] (vs. Standard German uvular [ʀ]). Geminate consonants preserved as distinct (Alemannic feature).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 2 works, from 1996 to 1998. [Sources](#sources) lists them. The spec file writes no spelling of its own. It takes all 61 from [German](de-DE.md) `de-DE`.

The [spec file](../../orthography2ipa/data/de-CH.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `de-CH` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [Alemannic German](de-x-alemanni.md) `de-x-alemanni`: research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 0 of them have a DOI or a URL.

1. <a id="src-wiese1996"></a>Wiese, R. (1996). *The Phonology of German*. Oxford University Press.
2. <a id="src-christen1998"></a>Christen, H. (1998). *Convergenz und Divergenz in der schweizerdeutschen Gegenwartsdialekte*. Francke.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 69 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p pʰ |  | d t tʰ |  |  | k kʰ ɡ |  |  |
| Affricate |  | pf | ts | tʃ |  |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |  |
| Trill |  |  | r |  |  |  |  |  |
| Fricative |  | f v | s z | ʃ | ç | x | ʁ χ | h |
| Approximant |  |  |  |  | j |  |  |  |
| Lateral approximant |  |  | l |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː y yː |  | u uː |
| Near-close | ɪ ʏ |  | ʊ |
| Close-mid | eː øː |  | o oː |
| Mid |  | ə |  |
| Open-mid | œ ɛ ɛː |  | ɔ |
| Near-open |  | ɐ |  |
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

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "de-CH")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Swedish](sv.md) · [Home](../index.md) · [Syrian Arabic →](apc-SY.md)
