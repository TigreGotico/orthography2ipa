# American English (General American) (`en-US`)

<!-- atlas:summary begin -->
American English (General American) is a West Germanic language, written in the Latin script. Its code names United States. The `en-US` spec is at the research tier. It cites 7 sources and has 4 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `en-US` |
| ISO 639-3 | [eng](https://iso639-3.sil.org/code/eng), English |
| Wikidata | [Q7976](https://www.wikidata.org/wiki/Q7976) |
| Wikipedia | [American English](https://en.wikipedia.org/wiki/American_English) |
| Family | [Indo-European](by-family.md#indo-european) > [Germanic > Northwest Germanic > West Germanic](by-family.md#indo-european--germanic--northwest-germanic--west-germanic) |
| Region | [North America](by-region.md#north-america) > [United States](by-region.md#united-states) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1500, living |
| Parent | [British English (RP)](en-GB.md) `en-GB` |
| Explorer | [`en-US` in the data explorer](https://tigregotico.github.io/orthography2ipa/#en-US) |
| Spec file | [`en-US.json`](../../orthography2ipa/data/en-US.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> General American (GA), reference accent for US media/education. RHOTIC: /r/ preserved in all positions. No TRAP-BATH split (bath words = /æ/). LOT-PALM merger: /ɑ/ for both (written without the length mark, see BROAD BY DECLARATION and the no-length-marks paragraph below).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 7 works, from 1953 to 2011. [Sources](#sources) lists them. The spec file writes 7 of the 84 spellings of its letter table and takes the other 77 from [British English (RP)](en-GB.md) `en-GB`.

The [spec file](../../orthography2ipa/data/en-US.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `en-US` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 7 works. 0 of them have a DOI or a URL. The spec file holds a note on what 6 of them support.

1. <a id="src-wells1982_vol3"></a>Wells, J.C. (1982). *Accents of English, Vol. 3: Beyond the British Isles*. Cambridge University Press.
2. <a id="src-ladefoged1999_ame"></a>Ladefoged, P. (1999). *American English*. Cambridge University Press.
3. <a id="src-ladefoged2011"></a>Ladefoged, P. & Johnson, K. (2011). *A Course in Phonetics (6th ed.)*. Wadsworth.
4. <a id="src-wells2008"></a>Wells, J.C. (2008). *Longman Pronunciation Dictionary (3rd ed.)*. Pearson Longman.
5. <a id="src-kenyon1953"></a>Kenyon, J.S. & Knott, T.A. (1953). *A Pronouncing Dictionary of American English*. G. & C. Merriam.
6. <a id="src-labov2006_anae"></a>Labov, W., Ash, S. & Boberg, C. (2006). *The Atlas of North American English: Phonetics, Phonology and Sound Change*. Mouton de Gruyter.
7. <a id="src-kretzschmar2004"></a>Kretzschmar, W.A. (2004). *Standard American English pronunciation*. Mouton de Gruyter.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `cmudict` ([cmusphinx/cmudict](https://github.com/cmusphinx/cmudict)) | `en-US` | gold | lexicon-derived | BSD-style (CMU) | 126050 | 0.3376 | yes |
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `en-US` | gold | lexicon-derived | MIT, each file its own | 125925 | 0.2908 | yes |
| `ipa_babylm` ([phonemetransformers/IPA-BabyLM](https://huggingface.co/datasets/phonemetransformers/IPA-BabyLM)) | `en-US` | generated | espeak-derived | Not stated upstream | 20107 | 0.3520 | no |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `en-US` | generated | espeak-derived | CC BY 4.0 | 18054 | 0.2655 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 111 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b b̥ p pʰ p̚ |  |  | d d̥ d̪ t tʰ t̚ |  |  | k kʰ k̚ ɡ ɡ̊ | ʔ |
| Affricate |  |  |  |  | dʒ dʒ̊ tʃ |  |  |  |
| Nasal | m | ɱ |  | n n̪ |  |  | ŋ |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative |  | f v v̥ | ð θ | s z z̥ | ʃ ʒ ʒ̊ |  |  | h ɦ |
| Approximant |  |  |  | ɹ |  | j |  |  |
| Lateral approximant |  |  |  | l ɫ |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i iː | ʉː | u uː |
| Near-close | ɪ |  | ʊ |
| Mid |  | ə |  |
| Open-mid | ɛ | ɜː | ɔ ɔː ʌ |
| Near-open | æ | ɐ |  |
| Open |  |  | ɑ ɑː ɒ |

Sequences that the spec writes as one unit: [aɪ] [aɪə] [aɪəɹ] [aʊ] [aʊə] [aʊəɹ] [eə] [eɪ] [ju] [juː] [jʊə] [jʊəɹ] [ks] [kw] [ndʒ] [oʊ] [oʊɪ] [sk] [w] [w̥] [æɹ] [æʊ] [ŋɡ] [ɑɪ] [ɑɹ] [ɑːɹ] [ɒf] [ɒɹ] [ɔɪ] [ɔɹ] [ɔːɹ] [əw] [əɹ] [əʊ] [ɚ] [ɛə] [ɛəɹ] [ɛɹ] [ɜːɹ] [ɝ], and 10 more.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [æ] [ɑː] [eɪ] [ə] [ɔː] | before mute e [eɪ] · default [æ] [ɑː] [eɪ] [ə] [ɔː] · nucleus unstressed [ə] · word final [ə] |
| ⟨aa⟩ | [ɑ] |  |
| ⟨ai⟩ | [eɪ] |  |
| ⟨air⟩ | [ɛəɹ] |  |
| ⟨ar⟩ | [ɑːɹ] | nucleus unstressed [əɹ] |
| ⟨are⟩ | [ɛəɹ] |  |
| ⟨au⟩ | [ɔː] [ɑː] [ɒ] | before vowel [aʊ] · default [ɔː] [ɑː] [ɒ] |
| ⟨aw⟩ | [ɔː] | before vowel [əw] · default [ɔː] |
| ⟨ay⟩ | [eɪ] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] [s] | before e [s] · before i [s] · before y [s] · default [k] |
| ⟨ch⟩ | [tʃ] [k] [ʃ] |  |
| ⟨ck⟩ | [k] |  |
| ⟨d⟩ | [d] |  |
| ⟨dg⟩ | [dʒ] |  |
| ⟨dge⟩ | [dʒ] |  |
| ⟨e⟩ | [ɛ] [iː] [ə] | before mute e [iː] · default [ɛ] [iː] [ə] · nucleus unstressed closed [ə] · word final ∅ |
| ⟨ea⟩ | [iː] [ɛ] |  |
| ⟨ear⟩ | [ɪəɹ] [ɛəɹ] |  |
| ⟨eau⟩ | [juː] [oʊ] |  |
| ⟨ee⟩ | [iː] |  |
| ⟨eer⟩ | [ɪəɹ] |  |
| ⟨ei⟩ | [iː] [eɪ] |  |
| ⟨er⟩ | [ɜːɹ] [əɹ] |  |
| ⟨eu⟩ | [juː] |  |
| ⟨ew⟩ | [juː] [uː] |  |
| ⟨ey⟩ | [iː] [eɪ] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [dʒ] | before e [dʒ] [ɡ] · before i [ɡ] [dʒ] · before y [dʒ] · default [ɡ] |
| ⟨gg⟩ | [ɡ] |  |
| ⟨gh⟩ | [ɡ] [f] ∅ |  |
| ⟨gn⟩ | [n] |  |
| ⟨h⟩ | [h] | default [h] · word final ∅ |
| ⟨i⟩ | [ɪ] [iː] [aɪ] | before mute e [aɪ] · before vowel [i] · default [ɪ] [iː] [aɪ] · word final [i] |
| ⟨ie⟩ | [aɪ] [iː] |  |
| ⟨igh⟩ | [aɪ] |  |
| ⟨ir⟩ | [ɜːɹ] |  |
| ⟨ire⟩ | [aɪəɹ] |  |
| ⟨j⟩ | [dʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [k] |  |
| ⟨kn⟩ | [n] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] [ŋɡ] | before final vowel [ndʒ] · default [ŋ] |
| ⟨o⟩ | [ɒ] [oʊ] [ɔː] [ʌ] [uː] | before mute e [oʊ] · default [ɒ] [oʊ] [ɔː] [ʌ] [uː] · nucleus unstressed [ə] · word final [oʊ] |
| ⟨oa⟩ | [oʊ] |  |
| ⟨oar⟩ | [ɔːɹ] |  |
| ⟨oe⟩ | [oʊ] [uː] |  |
| ⟨oi⟩ | [ɔɪ] |  |
| ⟨oo⟩ | [uː] [ʊ] |  |
| ⟨or⟩ | [ɔːɹ] | nucleus unstressed [əɹ] |
| ⟨ore⟩ | [ɔːɹ] |  |
| ⟨ou⟩ | [aʊ] [ʌ] [uː] |  |
| ⟨ough⟩ | [ɔː] [oʊ] [ʌf] [ɒf] [aʊ] [uː] |  |
| ⟨our⟩ | [aʊəɹ] [ɔːɹ] |  |
| ⟨ow⟩ | [aʊ] [oʊ] |  |
| ⟨oy⟩ | [ɔɪ] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [f] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [ɹ] |  |
| ⟨s⟩ | [s] [z] | default [s] · intervocalic [z] · word final [s] [z] · word initial [s] |
| ⟨sc⟩ | [s] | before e [s] · before i [s] · before y [s] · default [sk] |
| ⟨sch⟩ | [sk] |  |
| ⟨sh⟩ | [ʃ] |  |
| ⟨ss⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨tch⟩ | [tʃ] |  |
| ⟨th⟩ | [θ] [ð] | default [θ] · intervocalic [ð] · word initial [θ] [ð] |
| ⟨u⟩ | [ʌ] [juː] [uː] [ʊ] | before mute e [juː] [uː] · default [ʌ] [juː] [uː] [ʊ] · nucleus unstressed [ə] · word final [uː] [juː] |
| ⟨ue⟩ | [juː] [uː] |  |
| ⟨ui⟩ | [uː] [ɪ] |  |
| ⟨ur⟩ | [ɜːɹ] |  |
| ⟨ure⟩ | [jʊəɹ] [ʊəɹ] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨wh⟩ | [w] [ʍ] |  |
| ⟨wr⟩ | [ɹ] |  |
| ⟨x⟩ | [ks] [ɡz] | default [ks] · word initial [z] |
| ⟨y⟩ | [j] [iː] [aɪ] [ɪ] | before final vowel [aɪ] · before mute e [aɪ] · before vowel [j] · default [ɪ] [aɪ] [i] · word final [i] [aɪ] · word initial [j] |
| ⟨z⟩ | [z] |  |

Stress falls on the first syllable by default. These endings take the penult: ⟨-ic⟩ ⟨-ics⟩ ⟨-ion⟩ ⟨-ions⟩.

Whole-word exceptions (46): ⟨'re⟩ [ɹ], ⟨'ve⟩ [v], ⟨a⟩ [ə], ⟨above⟩ [əˈbʌv], ⟨an⟩ [ən], ⟨are⟩ [ɑɹ], ⟨as⟩ [æz], ⟨come⟩ [kʌm], ⟨do⟩ [du], ⟨does⟩ [dʌz], ⟨doing⟩ [ˈduɪŋ], ⟨done⟩ [dʌn], ⟨dove⟩ [dʌv], ⟨eye⟩ [aɪ], ⟨give⟩ [ɡɪv], ⟨glove⟩ [ɡlʌv], ⟨gone⟩ [ɡɒn], ⟨has⟩ [hæz], ⟨have⟩ [hæv], ⟨his⟩ [hɪz], ⟨i⟩ [aɪ], ⟨i'd⟩ [aɪd], ⟨i'll⟩ [aɪl], ⟨i'm⟩ [aɪm], ⟨is⟩ [ɪz], ⟨live⟩ [lɪv], ⟨lose⟩ [luːz], ⟨love⟩ [lʌv], ⟨menu⟩ [ˈmɛnju], ⟨move⟩ [muːv], and 16 more in the spec file.

Grammatical endings: ⟨-cial⟩ [ʃəl], ⟨-cian⟩ [ʃən], ⟨-cion⟩ [ʃən], ⟨-cious⟩ [ʃəs], ⟨-ous⟩ [əs], ⟨-ssion⟩ [ʃən], ⟨-ssure⟩ [ʃɚ], ⟨-stial⟩ [stʃəl], ⟨-stion⟩ [stʃən], ⟨-stious⟩ [stʃəs], ⟨-sure⟩ [ʒɚ], ⟨-tial⟩ [ʃəl], ⟨-tion⟩ [ʃən], ⟨-tious⟩ [ʃəs], ⟨-ture⟩ [tʃɚ].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 34 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `EN_GB_PREVOCALIC_R_AR_GEMINATE` | /ɑːɹ/ → [æ], spelled ⟨ar⟩, before ⟨r⟩, with more context in the spec | ⟨marry⟩ [ˈmæɹi] | [Wells 1982](#src-wells1982_vol3), Carney 1994 |
| `EN_GB_PREVOCALIC_R_AR` | /ɑːɹ/ → [æɹ], before a vowel, spelled ⟨ar⟩ | ⟨marry⟩ [ˈmæɹi] | [Wells 1982](#src-wells1982_vol3), Carney 1994 |
| `EN_GB_PREVOCALIC_R_ER_GEMINATE` | /əɹ/ → [ɛ], spelled ⟨er⟩, before ⟨r⟩, with more context in the spec | ⟨merry⟩ [ˈmɛɹi] | [Wells 1982](#src-wells1982_vol3), Carney 1994 |
| `EN_GB_PREVOCALIC_R_ER` | /əɹ/ → [ɛɹ], before a vowel, spelled ⟨er⟩ | ⟨merry⟩ [ˈmɛɹi] | [Wells 1982](#src-wells1982_vol3), Carney 1994 |
| `EN_GB_PREVOCALIC_R_IR_GEMINATE` | /ɜːɹ/ → [ɪ], spelled ⟨ir⟩, before ⟨r⟩, with more context in the spec | ⟨mirror⟩ [ˈmɪɹə] | [Wells 1982](#src-wells1982_vol3), Carney 1994 |
| `EN_GB_PREVOCALIC_R_IR` | /ɜːɹ/ → [ɪɹ], before a vowel, spelled ⟨ir⟩ | ⟨mirror⟩ [ˈmɪɹə] | [Wells 1982](#src-wells1982_vol3), Carney 1994 |
| `EN_GB_PREVOCALIC_R_UR_GEMINATE` | /ɜːɹ/ → [ʌ], spelled ⟨ur⟩, before ⟨r⟩, with more context in the spec | ⟨hurry⟩ [ˈhʌɹi] | [Wells 1982](#src-wells1982_vol3), Carney 1994 |
| `EN_GB_PREVOCALIC_R_UR` | /ɜːɹ/ → [ʌɹ], before a vowel, spelled ⟨ur⟩ | ⟨hurry⟩ [ˈhʌɹi] | [Wells 1982](#src-wells1982_vol3), Carney 1994 |
| `EN_GB_PREVOCALIC_R_OR_GEMINATE` | /ɔːɹ/ → [ɒ], spelled ⟨or⟩, before ⟨r⟩, with more context in the spec | ⟨sorry⟩ [ˈsɒɹi] | [Wells 1982](#src-wells1982_vol3), Carney 1994 |
| `EN_GB_PREVOCALIC_R_OR` | /ɔːɹ/ → [ɒɹ], before a vowel, spelled ⟨or⟩ | ⟨sorry⟩ [ˈsɒɹi] | [Wells 1982](#src-wells1982_vol3), Carney 1994 |
| `EN_GB_ED_EPENTHESIS` | /ɛ ə/ → [ɪ], after [t] [d], spelled ⟨e⟩, before ⟨d⟩, with more context in the spec | - | [Wells 2008](#src-wells2008), Cruttenden 2014 |
| `EN_GB_ED_SYNCOPE_AFTER_V` | /ɛ ə/ → ∅, spelled ⟨e⟩, before ⟨d⟩, with more context in the spec | - | [Wells 2008](#src-wells2008), Cruttenden 2014 |
| `EN_GB_ED_SYNCOPE_AFTER_C` | /ɛ ə/ → ∅, spelled ⟨e⟩, before ⟨d⟩, with more context in the spec | - | [Wells 2008](#src-wells2008), Cruttenden 2014 |
| `EN_GB_ED_DEVOICING` | /d/ → [t], word-finally, spelled ⟨d⟩, after ⟨e⟩, with more context in the spec | - | [Wells 2008](#src-wells2008), Cruttenden 2014 |
| `EN_GB_FINAL_S_VOICING` | /s/ → [z], word-finally, before a word boundary, after [b] [d] [ɡ] [v] [ð] [m] [n] [ŋ] and 2 more, spelled ⟨s⟩ | - | [Wells 2008](#src-wells2008), Cruttenden 2014 |
| `EN_GB_ES_EPENTHESIS` | /ɛ ə iː/ → [ɪ], after [s] [z] [ʃ] [ʒ] [tʃ] [dʒ] [ɡ], spelled ⟨e⟩, before ⟨s⟩, with more context in the spec | - | [Wells 2008](#src-wells2008), Cruttenden 2014 |
| `EN_GB_ES_SYNCOPE` | /ɛ ə iː/ → ∅, after a consonant, spelled ⟨e⟩, before ⟨s⟩, with more context in the spec | - | [Wells 2008](#src-wells2008), Cruttenden 2014 |
| `EN_GB_ES_VOICING_AFTER_MUTE_E` | /s/ → [z], word-finally, spelled ⟨s⟩, after ⟨e⟩, with more context in the spec | - | [Wells 2008](#src-wells2008), Cruttenden 2014 |
| `EN_GB_ES_VOICING_AFTER_EPENTHESIS` | /s/ → [z], word-finally, spelled ⟨s⟩, after ⟨e⟩, with more context in the spec | - | [Wells 2008](#src-wells2008), Cruttenden 2014 |
| `EN_GB_OING_HIATUS` | /ɔɪ/ → [oʊɪ], spelled ⟨oi⟩, before ⟨ng⟩, with more context in the spec | - | - |
| `EN_GB_FINAL_E_SOLE_VOWEL` | ∅ → [i], word-finally, spelled ⟨e⟩, with more context in the spec | ⟨be⟩ [bi] | [Kenyon 1953](#src-kenyon1953) |
| `EN_GB_FINAL_Y_MONOSYLLABLE` | /i/ → [aɪ], word-finally, spelled ⟨y⟩, with more context in the spec | ⟨my⟩ [maɪ] | - |
| `EN_US_FINAL_S_VOICING_AFTER_TENSE_VOWEL` | /s/ → [z], word-finally, before a word boundary, after [i] [u] [eɪ] [oʊ] [aɪ] [aʊ] [ɔɪ] [ɑ] and 16 more, spelled ⟨s⟩ | ⟨days⟩ [deɪz] | [Wells 1982](#src-wells1982_vol3), [Kenyon 1953](#src-kenyon1953) |
| `EN_US_LOT_PALM_MERGER` | /ɒ/ → [ɑ] | - | [Wells 1982](#src-wells1982_vol3) |
| `EN_US_NURSE_RCOLOURED` | /ɜːɹ/ → [ɝ] | - | [Wells 1982](#src-wells1982_vol3), [Ladefoged 2011](#src-ladefoged2011), [Kenyon 1953](#src-kenyon1953) |
| `EN_US_LETTER_RCOLOURED` | /əɹ/ → [ɚ] | - | [Wells 1982](#src-wells1982_vol3), [Ladefoged 2011](#src-ladefoged2011), [Kenyon 1953](#src-kenyon1953) |
| `EN_US_START_NO_LENGTH` | /ɑːɹ/ → [ɑɹ] | - | [Wells 1982](#src-wells1982_vol3), [Kenyon 1953](#src-kenyon1953), [Labov 2006](#src-labov2006_anae) |
| `EN_US_NORTH_NO_LENGTH` | /ɔːɹ/ → [ɔɹ] | - | [Wells 1982](#src-wells1982_vol3), [Kenyon 1953](#src-kenyon1953), [Labov 2006](#src-labov2006_anae) |
| `EN_US_PALM_NO_LENGTH` | /ɑː/ → [ɑ] | - | [Wells 1982](#src-wells1982_vol3), [Kenyon 1953](#src-kenyon1953), [Labov 2006](#src-labov2006_anae) |
| `EN_US_THOUGHT_NO_LENGTH` | /ɔː/ → [ɔ] | - | [Wells 1982](#src-wells1982_vol3), [Kenyon 1953](#src-kenyon1953), [Labov 2006](#src-labov2006_anae) |
| `EN_US_FLEECE_NO_LENGTH` | /iː/ → [i] | - | [Wells 1982](#src-wells1982_vol3), [Kenyon 1953](#src-kenyon1953), [Labov 2006](#src-labov2006_anae) |
| `EN_US_GOOSE_NO_LENGTH` | /uː/ → [u] | - | [Wells 1982](#src-wells1982_vol3), [Kenyon 1953](#src-kenyon1953), [Labov 2006](#src-labov2006_anae) |
| `EN_US_GOOSE_YOD_NO_LENGTH` | /juː/ → [ju] | - | [Wells 1982](#src-wells1982_vol3), [Kenyon 1953](#src-kenyon1953) |
| `EN_US_NURSE_NO_LENGTH` | /ɜː/ → [ɝ] | - | [Wells 1982](#src-wells1982_vol3), [Kenyon 1953](#src-kenyon1953) |

The spec switches off 22 inherited rules: `EN_GB_NONRHOTIC_AR_PRECONS`, `EN_GB_NONRHOTIC_AR_FINAL`, `EN_GB_NONRHOTIC_NURSE_PRECONS`, `EN_GB_NONRHOTIC_NURSE_FINAL`, `EN_GB_NONRHOTIC_OR_PRECONS`, `EN_GB_NONRHOTIC_OR_FINAL`, `EN_GB_NONRHOTIC_LETTER_PRECONS`, `EN_GB_NONRHOTIC_LETTER_FINAL`, `EN_GB_NONRHOTIC_SQUARE_PRECONS`, `EN_GB_NONRHOTIC_SQUARE_FINAL`, `EN_GB_NONRHOTIC_NEAR_PRECONS`, `EN_GB_NONRHOTIC_NEAR_FINAL`, `EN_GB_NONRHOTIC_CURE_PRECONS`, `EN_GB_NONRHOTIC_CURE_FINAL`, `EN_GB_NONRHOTIC_CURE_J_PRECONS`, `EN_GB_NONRHOTIC_CURE_J_FINAL`, `EN_GB_NONRHOTIC_FIRE_PRECONS`, `EN_GB_NONRHOTIC_FIRE_FINAL`, `EN_GB_NONRHOTIC_HOUR_PRECONS`, `EN_GB_NONRHOTIC_HOUR_FINAL`, `EN_GB_NONRHOTIC_R_PRECONS`, `EN_GB_NONRHOTIC_R_FINAL`.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "en-US")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Alguerese](ca-x-alguer.md) · [Home](../index.md) · [Amharic →](am.md)
