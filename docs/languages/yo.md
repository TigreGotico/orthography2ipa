# Yoruba (`yo`)

<!-- atlas:summary begin -->
Yoruba is an Atlantic-Congo language, written in the Latin script. Glottolog places it in Benin and Nigeria. The `yo` spec is at the research tier. It cites 5 sources and has 2 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `yo` |
| ISO 639-3 | [yor](https://iso639-3.sil.org/code/yor), Yoruba |
| Glottolog | [yoru1245](https://glottolog.org/resource/languoid/id/yoru1245), Yoruba |
| Wikidata | [Q34311](https://www.wikidata.org/wiki/Q34311) |
| Wikipedia | [Yoruba language](https://en.wikipedia.org/wiki/Yoruba_language) |
| Family | [Atlantic-Congo](by-family.md#atlantic-congo) |
| Region | [Africa](by-region.md#africa) > [Benin](by-region.md#benin), [Nigeria](by-region.md#nigeria) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1800, living |
| Parent | [Niger-Congo (family node)](https://tigregotico.github.io/orthography2ipa/#nic) `nic` |
| Explorer | [`yo` in the data explorer](https://tigregotico.github.io/orthography2ipa/#yo) |
| Spec file | [`yo.json`](../../orthography2ipa/data/yo.json) |
<!-- atlas:header end -->

## Overview

Yoruba is a tonal language whose orthography gives a phonemizer almost everything it needs. The spelling writes tone on the vowel and vowel nasalisation with a following ⟨n⟩. A subdot marks the two vowel qualities that a bare Latin alphabet cannot tell apart. The `yo` spec reads all of this from the page and does not treat it as unrecoverable.

The page places Yoruba in the Volta-Niger (Defoid) group of Niger-Congo.

## Segments

The seven oral vowels /i e ɛ a ɔ o u/ are written ⟨i e ẹ a ọ o u⟩. The two subdot letters ⟨ẹ ọ⟩ are the open-mid pair, and ⟨ṣ⟩ is /ʃ/.

Yoruba has two labial-velar stops and no plain /p/, so the letter ⟨p⟩ carries a doubly-articulated stop. The spec writes ⟨gb⟩ as `ɡ͡b` and ⟨p⟩ as `kp`, without a tie bar. Part of the literature analyses ⟨j⟩ as a palatal stop /ɟ/. The spec writes /dʒ/, which is a notation choice, not a claim about the language. The letter ⟨r⟩ is an alveolar tap [ɾ], not a trill (Akinlabi 2004, Bamgboṣe 1966).

## Tone

Yoruba has three level tones: high, mid and low. The orthography writes high with an acute, low with a grave, and mid with nothing. The spec emits all three with the IPA level-tone diacritics ◌́ ◌̄ ◌̀, mid included.

Mid is a specified tone in Yoruba, not the absence of a tone. A bare vowel in the output would claim that a word such as ⟨ọkọ⟩ 'hoe' has no tone. It would also collapse the classic minimal triple into one string. The spec keeps the three apart:

```python
>>> import orthography2ipa
>>> [orthography2ipa.transcribe(w, "yo") for w in ["ọkọ", "ọkọ̀", "ọ̀kọ̀"]]
['ɔ̄kɔ̄', 'ɔ̄kɔ̀', 'ɔ̀kɔ̀']
```

The words are 'hoe', 'vehicle' and 'spear'.

## Nasal vowels

Yoruba has five nasal vowels /ĩ ɛ̃ ã ɔ̃ ũ/, written ⟨in ẹn an ọn un⟩. There are no nasal counterparts of /e/ and /o/, and the orthography shows that gap. The spellings ⟨en⟩ and ⟨on⟩ are not nasal-vowel spellings, so the spec keeps their ⟨n⟩ as a consonant.

An ⟨n⟩ after one of the five nasalisable vowels, and not followed by a vowel, spells nasalisation of that vowel. It is not a segment of its own, so ⟨Abiọdun⟩ is `ābīɔ̄dũ̄`, with no final /n/. Before a vowel the same letter is an ordinary onset, and the vowel before it stays oral. A `before_vowel` positional override on each nasal digraph states this. The spec does not rely on longest-match tokenisation to get it right.

A vowel after an onset ⟨m⟩ or ⟨n⟩ is itself nasal for /i a ɔ u/. The orthography writes no ⟨n⟩ for it, because the nasality is predictable: ⟨mi⟩ ⟨mu⟩ ⟨mọ⟩ are `mĩ̄`, `mũ̄`, `mɔ̃̄`. The onset ⟨n⟩ is the nasal allophone of /l/, which occurs only before a nasal vowel, so ⟨inú⟩ /īlṹ/ surfaces as `īnṹ`. Likewise ⟨ana⟩ is `ānã̄` and ⟨ẹni⟩ is `ɛ̄nĩ̄`. The `YO_NASAL_AFTER_NASAL_ONSET_*` allophone rules carry this.

/ɛ/ stays out of the rule. The source that states the nasalisation confines phonemic /ɛ̃/ to the one word ìyẹn ~ yẹn 'that'. The gold agrees, because /ɛ/ after a nasal onset is rarely nasal there. The inventory, not the consonant, bounds the rule. /e/ and /o/ have no nasal counterpart either, so ⟨me⟩ ⟨mo⟩ ⟨ne⟩ ⟨no⟩ stay oral.

The remaining oral-vowel words are not a loanword stratum. The oral-/ɛ/ words are the core numerals and their derivatives. Examples are mẹfa, mẹta, mẹrin, mẹjọ, mẹwaa, mẹrẹẹrin, mẹtẹẹta, idamẹfa, ẹẹmẹta, mẹkunnu. Oral /a/ after a nasal onset occurs in native words such as Olodumare, Eledumare, Oṣumare, amala, awọsanma, majele, magun, mariwo, imale and nama. That is lexical knowledge, which a grapheme spec does not have, and it belongs in a caller-supplied lexicon.

The order of the marks matters. The spec writes the nasalisation tilde before the tone mark, so that u, tilde and acute compose to the standard ṹ. The other order gives a string that only looks the same.

## The syllabic nasal

Yoruba permits only open syllables, so an ⟨n⟩ before a consonant is never a coda. It is either the nasalisation mark of the vowel before it, or a syllable nucleus with its own tone.

The vowel decides which. The nasal-vowel reading needs a vowel with a nasal counterpart, one of /ĩ ɛ̃ ã ɔ̃ ũ/. Where no such vowel is available, only the syllabic reading is left, and the spec applies it there. That covers ⟨n⟩ before a consonant at the start of a word or after another consonant, as in ⟨nkọ⟩ `ŋ̩̄kɔ̄`, ⟨njẹ⟩ and ⟨nnkan⟩. It also covers ⟨n⟩ after ⟨e⟩ or ⟨o⟩, neither of which has a nasal counterpart, as in ⟨Aderonkẹ⟩ `ādēɾōŋ̩̄kɛ̄` and ⟨otente⟩.

Longest-match tokenisation makes the selection unaided. The graphemes ⟨an in ọn un ẹn⟩ are longer and take precedence, so one `before_consonant` override on ⟨n⟩ reaches exactly the residue. The gold agrees with the syllabic reading in that residue without exception. The nucleus adds a tone slot, so more outputs have the same number of tone-bearing units as the gold.

The spec emits one velar nasal and does not guess a place of articulation from the spelling. The reference grammars describe the syllabic nasal as homorganic with what follows. Standard Yoruba already spells the labial variant ⟨m⟩, as in ⟨òrombó⟩ 'orange'. An ⟨n⟩ before a labial is therefore no evidence of a labial nasal. The gold takes the same view and writes a velar in every nasal-before-consonant context it holds. That includes ⟨n⟩ before ⟨b p f⟩, as in ⟨Ganbia⟩ ɡáŋ́bíà, and ⟨m⟩ before a consonant, as in ⟨Abimbọla⟩ ābíŋ̄bɔ́lá. A labial [m̩] would be a phonetic refinement that the gold cannot confirm and would contradict.

The spec writes syllabicity with ◌̩, to match its entries for ⟨ń⟩ and ⟨ǹ⟩. The gold writes a bare ŋ with a tone mark. The difference is a convention, not an error.

## What the spec does not model

After ⟨a i ọ u ẹ⟩, an ⟨n⟩ before a consonant stays a nasal vowel. Both readings are possible there, the gold splits, and no orthographic condition separates the two. Most of the gold's remaining ŋ is in that residue.

The spec does not model downstep. The WikiPron gold marks it, but the orthography does not, so the spelling cannot recover it. A minority of gold entries use the ⟨ị⟩ and ⟨ụ⟩ of the extended orthography. The spec does not map them, so it drops them.

## The gold rows read two conventions

Yoruba has gold rows that disagree about what a Yoruba transcription contains. For the scores, see the [scoreboard](../evaluation/generated/scoreboard.md).

The `wikipron` row (`yor_latn_broad`) comes from Wiktionary and marks tone and nasalisation in full, so it rewards a spec that emits both. Its orthographic column, however, almost never carries tone. Tone is recoverable in Yoruba, but not from this gold's input. The spec reads an unmarked vowel as mid, which is correct for the spelling it gets, and the gold says high or low. That gap is most of the row's remaining error, and the spec `audit` entry records the row as `input_limited`.

The `wikipron_restored` dataset uses the same gold with the input repaired. Wiktionary writes the tone on the headword line and leaves it out of the page title, and WikiPron scrapes the title. The script `scripts/restore_wikipron_orthography.py` recovers the headword from the MediaWiki API. Most rows come back, and what remains on them is downstep and the unmapped ⟨ị ụ⟩. The rows that do not come back are mostly titles shared by several words, as untoned ⟨aba⟩ is abà, abá, àba and àbá. No row is emitted for them. Rank Yoruba on the restored set where it covers a word, and on `wikipron` elsewhere. The two are not the same sample.

The `vox_communis` row is epitran-derived. Its orthography is real, fully accented Yoruba, but its phone column has no tone at all and handles nasal vowels inconsistently, because epitran produces that. It measures agreement with epitran, not accuracy, so a spec that emits tone scores badly on it. `scripts/fold_yo_vox_notation.py` folds tone and nasalisation out of both sides. What remains after the fold is mostly epitran's own conventions. These are its ɡ͡b and ṣ notations, its doubling, and its choice of nasal tokens.

The `audit` entry for `vox_communis` records the fold as `at_ceiling_documented`. It is not a `valid_ceiling`, because Yoruba spelling writes tone: the gap is the gold's notation, not a contrast the orthography cannot signal. An epitran-derived tier never gates a promotion.

<!-- atlas:lects begin -->
## Related lects

No spec names `yo` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 5 works. 1 of them have a DOI or a URL. The spec file holds a note on what 4 of them support.

1. <a id="src-adesola_gs"></a>Adesola, Oluseye (2005). *Yoruba: A Grammar Sketch, Version 1.0*. Afranaph Project. Cited: §2.1.1 charts 2-3, §2.1.2, p. 2 n. 4. [afranaphproject.afranaphdatabase.com](https://afranaphproject.afranaphdatabase.com/images/stories/downloads/casefiles/YorubaGS.pdf)
2. <a id="src-akinlabi2004"></a>Akinlabi, A. (2004). *Yoruba*. Cambridge University Press.
3. <a id="src-bamgbose1969"></a>Bamgboṣe, Ayọ (1969). *Yoruba. In Elizabeth Dunstan (ed.), Twelve Nigerian Languages*. Africana Publishing Corp. Cited: p. 166.
4. <a id="src-abraham1958"></a>Abraham, Roy Clive (1958). *Dictionary of Modern Yoruba*. University of London Press.
5. <a id="src-sachnine1997"></a>Sachnine, Michka (1997). *Dictionnaire yorùbá-français, suivi d'un index français-yorùbá*. Karthala/IFRA.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `yo` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 4065 | 0.3828 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `yo` | generated | epitran-derived | CC0 1.0 | 5263 | 0.6392 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 75 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b |  | d t |  |  | k ɡ |  |
| Affricate |  |  |  | dʒ |  |  |  |
| Nasal | m |  | n ń̩ ǹ̩ |  |  | ŋ̩̀ ŋ̩́ ŋ̩̄ |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f | s | ʃ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | ì í ĩ̀ ĩ́ ĩ̄ ī | ù ú ũ̀ ũ̄ ū ṹ |
| Close-mid | è é ē | ò ó ō |
| Open-mid | ɛ̀ ɛ́ ɛ̃̀ ɛ̃́ ɛ̃̄ ɛ̄ | ɔ̀ ɔ́ ɔ̃̀ ɔ̃́ ɔ̃̄ ɔ̄ |
| Open | à á ã̀ ã́ ã̄ ā |  |

Sequences that the spec writes as one unit: [kp] [k͡p] [w] [àn] [án] [ìn] [ín] [ùn] [ún] [ān] [īn] [ūn] [ɔ̀n] [ɔ́n] [ɔ̄n] [ɛ̀n] [ɛ́n] [ɛ̄n] [ɡ͡b].

Tones: [◌́] high, [◌̀] low, [◌̄] mid, [unmarked] mid.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [ā] |  |
| ⟨an⟩ | [ã̄] | before vowel [ān] |
| ⟨b⟩ | [b] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [ē] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gb⟩ | [ɡ͡b] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [ī] |  |
| ⟨in⟩ | [ĩ̄] | before vowel [īn] |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] | before consonant [ŋ̩̄] |
| ⟨o⟩ | [ō] |  |
| ⟨p⟩ | [kp] |  |
| ⟨r⟩ | [ɾ] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [ū] |  |
| ⟨un⟩ | [ũ̄] | before vowel [ūn] |
| ⟨w⟩ | [w] |  |
| ⟨y⟩ | [j] |  |
| ⟨à⟩ | [à] |  |
| ⟨àn⟩ | [ã̀] | before vowel [àn] |
| ⟨á⟩ | [á] |  |
| ⟨án⟩ | [ã́] | before vowel [án] |
| ⟨è⟩ | [è] |  |
| ⟨é⟩ | [é] |  |
| ⟨ì⟩ | [ì] |  |
| ⟨ìn⟩ | [ĩ̀] | before vowel [ìn] |
| ⟨í⟩ | [í] |  |
| ⟨ín⟩ | [ĩ́] | before vowel [ín] |
| ⟨ò⟩ | [ò] |  |
| ⟨ó⟩ | [ó] |  |
| ⟨ù⟩ | [ù] |  |
| ⟨ùn⟩ | [ũ̀] | before vowel [ùn] |
| ⟨ú⟩ | [ú] |  |
| ⟨ún⟩ | [ṹ] | before vowel [ún] |
| ⟨ń⟩ | [ń̩] | before consonant [ŋ̩́] |
| ⟨ǹ⟩ | [ǹ̩] | before consonant [ŋ̩̀] |
| ⟨ṣ⟩ | [ʃ] |  |
| ⟨ẹ⟩ | [ɛ̄] |  |
| ⟨ẹn⟩ | [ɛ̃̄] | before vowel [ɛ̄n] |
| ⟨ẹ̀⟩ | [ɛ̀] |  |
| ⟨ẹ̀n⟩ | [ɛ̃̀] | before vowel [ɛ̀n] |
| ⟨ẹ́⟩ | [ɛ́] |  |
| ⟨ẹ́n⟩ | [ɛ̃́] | before vowel [ɛ́n] |
| ⟨ọ⟩ | [ɔ̄] |  |
| ⟨ọn⟩ | [ɔ̃̄] | before vowel [ɔ̄n] |
| ⟨ọ̀⟩ | [ɔ̀] |  |
| ⟨ọ̀n⟩ | [ɔ̃̀] | before vowel [ɔ̀n] |
| ⟨ọ́⟩ | [ɔ́] |  |
| ⟨ọ́n⟩ | [ɔ̃́] | before vowel [ɔ́n] |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 12 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `YO_NASAL_AFTER_NASAL_ONSET_I_MID` | /ī/ → [ĩ̄], after [m] [n] | - | [Bamgboṣe 1969](#src-bamgbose1969), [Abraham 1958](#src-abraham1958), [Sachnine 1997](#src-sachnine1997) |
| `YO_NASAL_AFTER_NASAL_ONSET_I_HIGH` | /í/ → [ĩ́], after [m] [n] | - | - |
| `YO_NASAL_AFTER_NASAL_ONSET_I_LOW` | /ì/ → [ĩ̀], after [m] [n] | - | - |
| `YO_NASAL_AFTER_NASAL_ONSET_A_MID` | /ā/ → [ã̄], after [m] [n] | - | - |
| `YO_NASAL_AFTER_NASAL_ONSET_A_HIGH` | /á/ → [ã́], after [m] [n] | - | - |
| `YO_NASAL_AFTER_NASAL_ONSET_A_LOW` | /à/ → [ã̀], after [m] [n] | - | - |
| `YO_NASAL_AFTER_NASAL_ONSET_OPEN_O_MID` | /ɔ̄/ → [ɔ̃̄], after [m] [n] | - | - |
| `YO_NASAL_AFTER_NASAL_ONSET_OPEN_O_HIGH` | /ɔ́/ → [ɔ̃́], after [m] [n] | - | - |
| `YO_NASAL_AFTER_NASAL_ONSET_OPEN_O_LOW` | /ɔ̀/ → [ɔ̃̀], after [m] [n] | - | - |
| `YO_NASAL_AFTER_NASAL_ONSET_U_MID` | /ū/ → [ũ̄], after [m] [n] | - | - |
| `YO_NASAL_AFTER_NASAL_ONSET_U_HIGH` | /ú/ → [ṹ], after [m] [n] | - | - |
| `YO_NASAL_AFTER_NASAL_ONSET_U_LOW` | /ù/ → [ũ̀], after [m] [n] | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="Abiọdun|Aderonkẹ|ana|ẹni|inú|mi|mọ|mu|nkọ|ọkọ|òrombó" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "yo")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| Abiọdun | [ābīɔ̄dũ̄] |
| Aderonkẹ | [ādēɾōŋ̩̄kɛ̄] |
| ana | [ānã̄] |
| ẹni | [ɛ̄nĩ̄] |
| inú | [īnṹ] |
| mi | [mĩ̄] |
| mọ | [mɔ̃̄] |
| mu | [mũ̄] |
| nkọ | [ŋ̩̄kɔ̄] |
| ọkọ | [ɔ̄kɔ̄] |
| òrombó | [òɾōmbó] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Yiddish](yi.md) · [Home](../index.md) · [Yucatec Mexican Spanish →](es-MX-x-yucatan.md)
