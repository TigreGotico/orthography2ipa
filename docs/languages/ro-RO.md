# Romanian (`ro-RO`)

<!-- atlas:summary begin -->
Romanian is an Eastern Romance language, written in the Latin script. Its code names Romania. The `ro-RO` spec is at the production tier. It cites 9 sources and has 4 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ro-RO` |
| Aliases | `ron` |
| ISO 639-3 | [ron](https://iso639-3.sil.org/code/ron), Romanian |
| Glottolog | [roma1327](https://glottolog.org/resource/languoid/id/roma1327), Romanian |
| Wikidata | [Q7913](https://www.wikidata.org/wiki/Q7913) |
| Wikipedia | [Romanian language](https://en.wikipedia.org/wiki/Romanian_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Eastern Romance](by-family.md#indo-european--italic--romance--eastern-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Romania](by-region.md#romania) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [production](../specs/quality_tiers.md#production) |
| Attested | from 1600, living |
| Parent | [Eastern Romance](https://tigregotico.github.io/orthography2ipa/#x-clade-east2714) `x-clade-east2714` |
| Explorer | [`ro-RO` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ro-RO) |
| Spec file | [`ro-RO.json`](../../orthography2ipa/data/ro-RO.json) |
<!-- atlas:header end -->

## Overview

The `ro-RO` spec transcribes Standard Romanian (limba română standard). The registry resolves the bare tag `ro` to this spec. The spelling and pronunciation norm is the academic dictionary DOOM3, which is open to read at [doom.lingv.ro](https://doom.lingv.ro/). The explanatory dictionary portal [dexonline](https://dexonline.ro/) is also open.

Romanian counts as a shallow orthography, so the production bar is a PER of 0.15 ([quality tiers](../specs/quality_tiers.md#the-per-threshold)). The letters map to sounds almost one to one. The difficult part is the stress, which the spelling does not write. The main open source for stress is Franzén & Horne (1997), in the [Lund Working Papers](https://lucris.lub.lu.se/ws/files/5380394/624462.pdf).

## Letters and vowels

The spec has seven vowels, /a e i o u ə ɨ/. Each central vowel has a letter of its own: ⟨ă⟩ is /ə/, and both ⟨â⟩ and ⟨î⟩ are /ɨ/. The choice between ⟨â⟩ and ⟨î⟩ follows the position in the word. The 1993 norm of the Romanian Academy writes ⟨î⟩ at the start and at the end of a word and ⟨â⟩ inside it, as the [Wikipedia article on the Romanian alphabet](https://en.wikipedia.org/wiki/Romanian_alphabet) explains. The spelling before 1993 used ⟨î⟩ inside words too. The spec does not cover that older spelling, because orthography2ipa does not normalise its input.

The spec declares ⟨ă⟩ in `vowel_graphemes`, because the engine's closed set of Latin vowel letters does not include it. Without that declaration, a rule that tests for a vowel next to ⟨ă⟩ would fail, as in ⟨băieți⟩.

The Romanian Academy requires the comma-below letters ⟨ș⟩ and ⟨ț⟩ for /ʃ/ and /ts/. Much text still uses the cedilla letters ⟨ş⟩ (U+015F) and ⟨ţ⟩ (U+0163), because fonts did not support the comma-below letters for a long time ([Romanian alphabet](https://en.wikipedia.org/wiki/Romanian_alphabet)). The spec maps only the comma-below letters.

## Consonants

The rules `RO_SOFT_C` and `RO_SOFT_G` read ⟨c⟩ as /tʃ/ and ⟨g⟩ as /dʒ/ before ⟨e⟩ and ⟨i⟩. The digraphs ⟨ch⟩ and ⟨gh⟩ are graphemes of their own and keep /k/ and /ɡ/. So ⟨cer⟩ gives `ˈtʃer` and ⟨cheie⟩ gives `ˈkeje`. DOOM3 treats the ⟨i⟩ and ⟨e⟩ of ⟨ci ce gi ge⟩ as the mark of the palatal reading, as the spec notes state.

The spec maps ⟨p t c⟩ to plain stops in every position, because Romanian has no lenition between vowels. So ⟨lup⟩ gives `ˈlup`. Franzén & Horne (1997, p. 75) transcribe ⟨copil⟩ 'child' as [kopˈil], with the plain [p] between vowels.

## Glides and final i

The diphthongs ⟨ea⟩ /e̯a/ and ⟨oa⟩ /o̯a/ are graphemes, so ⟨soare⟩ gives `ˈso̯are`. Two rules read ⟨i⟩ as the glide [j]. The rule `RO_I_GLIDE_INITIAL` applies before a vowel at the start of a word, and `RO_I_GLIDE_POSTVOCALIC` applies after a vowel. So the plural ⟨copii⟩ 'children' gives `koˈpij`, the form that Franzén & Horne (1997, p. 82) print as [kopˈij].

The final ⟨i⟩ of a plural or of a second-person singular verb has no syllable of its own. The rule `RO_FINAL_I_ASYLLABIC` deletes the vowel and palatalises the consonant before it, so ⟨lupi⟩ gives `ˈlupʲ`. The rule `RO_FINAL_I_ASYLLABIC_LIQUID` does the same after ⟨l⟩ or ⟨r⟩. It does not apply when the liquid is the second consonant of an obstruent and liquid onset, so ⟨codri⟩ gives `ˈkodri`. Both rules apply only when the word keeps another vowel (Chițoran 2002, ch. 5).

Word-initial ⟨e⟩ is [je] only in a closed set of words. The set holds the personal pronouns ⟨eu el ea ei ele⟩ and the present and imperfect forms of ⟨a fi⟩ 'to be', such as ⟨este⟩ and ⟨era⟩ (DOOM3 and Chițoran 2002, ch. 2). The spec lists these words in `word_exceptions`. So ⟨este⟩ gives `ˈjeste`, and ⟨elev⟩ 'pupil' gives `eˈlev`.

## Stress

Romanian stress is lexical, and the standard spelling does not mark it. Franzén & Horne (1997, p. 75) state the basic rule for nouns and adjectives. Stress falls on the penultimate syllable if the final syllable is open, and on the final syllable if it is closed. Their examples are [kopˈil] 'child' and [bəjetsˈandru] 'little boy'. Chițoran (2002, pp. 75-77) gives the same default. The spec reads her rule through the tables of Alexei & Ulfsbjorninn (2022, pp. 2-5).

The `stress` block states this default. A word that ends in a consonant takes final stress, as in *bărbát* and *animál*. A word that ends in a falling diphthong also takes final stress, as in *gunói* and *biróu*. So does a word that ends in ⟨ea⟩ [e̯a], as in *cafeá* and *aveá*, because that diphthong occurs only in stressed position (Alexei & Ulfsbjorninn 2022, p. 18). Franzén & Horne (1997, p. 81) print ⟨acea⟩ 'that' as acˈea. Any other word takes penultimate stress, as in *máre* and *feméie*.

Franzén & Horne (1997, pp. 77-78) find words that follow the default in the Dacian, Latin and Slavic layers of the vocabulary, such as balˈaur 'dragon', bolovˈan 'rock' and cojˈoc 'fur'. Stressed derivational suffixes keep the default too, as in singurătˈate, verdeˈață and copilărˈie (p. 80), and in îngerˈaș and clopoțˈel (p. 83). Inflection does not change the stress of the stem (p. 79). The benchmark strips stress marks, so the stress block does not change the PER.

## Weak points

The stress default misses the lexically marked words, and the spec lists none of them. The table gives words from Franzén & Horne (1997) with the source form and the output of `orthography2ipa.transcribe`.

| Word | Source form | Engine output |
|---|---|---|
| repede 'rapid' | ˈrepede (p. 76) | `reˈpede` |
| înger 'angel' | ˈînger (p. 77) | `ɨnˈdʒer` |
| suflet 'heart' | ˈsuflet (p. 77) | `suˈflet` |
| lingură 'spoon' | ˈlingură (p. 77) | `linˈɡurə` |
| biserică 'church' | bisˈerică (p. 77) | `biseˈrikə` |
| oaspete 'guest' | oˈaspete (p. 77) | `o̯aˈspete` |
| zgomot 'noise' | ˈzgomot (p. 78) | `zɡoˈmot` |
| copilului 'little child (sg. G/D)' | copˈilului (p. 78) | `kopiˈluluj` |
| acele 'needles' | ˈacele (p. 81) | `aˈtʃele` |
| copii 'copies' | ˈcopii (p. 81) | `koˈpij` |

The same classes appear in the spec notes. Some consonant-final words take penultimate stress (*záhăr*, *călúgăr*), and the engine gives `zaˈhər`. Some vowel-final words take antepenultimate stress (*pépene*, *cámeră*), and the engine gives `peˈpene` and `kaˈmerə`. Some words take final stress on a plain vowel (*macará*, *pané*), and the engine gives `maˈkara` and `ˈpane`.

Inflectional endings keep the stress of the stem (Franzén & Horne 1997, p. 79). The engine reads the whole word, so *lupul*, *trenuri* and *caselor* take the mark one syllable late: `luˈpul`, `treˈnurʲ` and `kaseˈlor`. The definite article on a noun in *-e* also writes ⟨ea⟩, so *cartea* gives `karˈte̯a` with the mark on the article. The spec does not resolve homographs that differ only in stress. Franzén & Horne (1997, p. 81) give ˈacele 'needles' against acˈele 'these', and ˈcopii 'copies' against copˈii 'children'. The engine gives one form for each pair.

After ⟨c⟩ or ⟨g⟩, an ⟨i⟩ before a vowel is silent in the inherited words and syllabic in the learned words. The spec notes give ⟨cioban⟩ [tʃoˈban] and ⟨Dacia⟩ [ˈdatʃi.a]. The split is lexical, not orthographic. The spec gives the syllabic reading for both, so ⟨cioban⟩ gives `tʃioˈban`. ⟨Dacia⟩ gives `daˈtʃia`, with the stress on the wrong syllable. A lexicon from the caller can correct these words.

The spec has no mapping for the cedilla letters ⟨ş⟩ and ⟨ţ⟩, so the engine drops them with an `UnmappedGraphemeWarning`. So ⟨şase⟩ gives `ˈase` where ⟨șase⟩ gives `ˈʃase`, and ⟨ţară⟩ gives `ˈarə` where ⟨țară⟩ gives `ˈtsarə`. A caller must change the cedilla letters to comma-below letters before transcription.

Two rows can gate a promotion. The [ipa-dict](https://github.com/open-dict-data/ipa-dict) Romanian list ([ro.txt](https://github.com/open-dict-data/ipa-dict/blob/master/data/ro.txt)) is lexicon-derived and sits under `ro-RO`. The [WikiPron Romanian list](https://github.com/CUNY-CL/wikipron/blob/master/data/scrape/tsv/ron_latn_broad.tsv) is crowd-scraped and sits under the bare tag `ro`. The `vox_communis` row is epitran output and the `ipa_childes` row is espeak output. Those two rows measure agreement with another system, so they cannot gate.

<!-- atlas:lects begin -->
## Related lects

No spec names `ro-RO` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 9 works. 2 of them have a DOI or a URL. The spec file holds a note on what 6 of them support.

1. <a id="src-mallinson1986"></a>Mallinson, G. (1986). *Romanian*. Croom Helm.
2. <a id="src-deletant_alexandrescu1983"></a>Deletant, D. & Alexandrescu, I. (1983). *Teach Yourself Romanian*. Hodder & Stoughton.
3. <a id="src-ladefoged_maddieson1996"></a>Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
4. <a id="src-chitoran2002"></a>Chițoran, I. (2002). *The Phonology of Romanian: A Constraint-based Approach*. Mouton de Gruyter.
5. <a id="src-renwick2014"></a>Renwick, M. E. L. (2014). *The Phonetics and Phonology of Contrast: The Case of the Romanian Vowel System*. De Gruyter Mouton.
6. <a id="src-vasiliu1965"></a>Vasiliu, E. (1965). *Fonologia limbii române*. Editura Științifică.
7. <a id="src-doom3"></a>Academia Română, Institutul de Lingvistică „Iorgu Iordan, Al. Rosetti” (2021). *Dicționarul ortografic, ortoepic și morfologic al limbii române (DOOM3)*. Univers Enciclopedic.
8. <a id="src-alexei_ulfsbjorninn2022"></a>Alexei, S. & Ulfsbjorninn, S. (2022). *Metrical exceptionality and stress shift in Romanian nouns and adjectives*. Isogloss. Open Journal of Romance Linguistics 8(1)/4. Cited: 1-29. [doi.org](https://doi.org/10.5565/rev/isogloss.240)
9. <a id="src-franzen_horne1997"></a>Franzén, V. & Horne, M. (1997). *Word stress in Romanian*. Lund University, Dept. of Linguistics, Working Papers 46. Cited: 75-91. [lucris.lub.lu.se](https://lucris.lub.lu.se/ws/files/5380394/624462.pdf)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `ro-RO` | gold | lexicon-derived | MIT, each file its own | 72375 | 0.0359 | yes |
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `ro` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 8977 | 0.0198 | yes |
| `ipa_childes` ([fdemelo/ipa-childes-split](https://huggingface.co/datasets/fdemelo/ipa-childes-split)) | `ro-RO` | generated | espeak-derived | CC BY 4.0 | 2311 | 0.2644 | no |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `ro` | generated | epitran-derived | CC0 1.0 | 10679 | 0.0693 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 43 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  | ts | dʒ tʃ |  |  |  |
| Nasal | m |  | n |  |  | ŋ |  |
| Trill |  |  | r |  |  |  |  |
| Tap |  |  | ɾ |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  | x | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i | ɨ | u |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Open-mid | ɛ |  |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [aw] [ew] [e̯a] [e̯aw] [ks] [ow] [o̯a] [w] [wa] [we] [ɡz].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨au⟩ | [aw] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] [tʃ] |  |
| ⟨ch⟩ | [k] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨ea⟩ | [e̯a] |  |
| ⟨eau⟩ | [e̯aw] |  |
| ⟨eu⟩ | [ew] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] [dʒ] |  |
| ⟨gh⟩ | [ɡ] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨oa⟩ | [o̯a] |  |
| ⟨ou⟩ | [ow] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨r⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨ua⟩ | [wa] |  |
| ⟨ue⟩ | [we] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [v] [w] |  |
| ⟨x⟩ | [ks] [ɡz] |  |
| ⟨y⟩ | [i] [j] |  |
| ⟨z⟩ | [z] |  |
| ⟨â⟩ | [ɨ] |  |
| ⟨î⟩ | [ɨ] |  |
| ⟨ă⟩ | [ə] |  |
| ⟨ș⟩ | [ʃ] |  |
| ⟨ț⟩ | [ts] |  |

Stress falls on the penult by default. These endings take final stress: ⟨-b⟩ ⟨-c⟩ ⟨-d⟩ ⟨-f⟩ ⟨-g⟩ ⟨-h⟩ ⟨-j⟩ ⟨-k⟩ ⟨-l⟩ ⟨-m⟩ ⟨-n⟩ ⟨-p⟩ ⟨-q⟩ ⟨-r⟩ ⟨-s⟩ ⟨-ș⟩ ⟨-t⟩ ⟨-ț⟩ ⟨-v⟩ ⟨-x⟩ ⟨-z⟩ ⟨-ai⟩ ⟨-oi⟩ ⟨-âi⟩ ⟨-au⟩ ⟨-ău⟩ ⟨-âu⟩ ⟨-eu⟩ ⟨-ou⟩ ⟨-ea⟩.

Whole-word exceptions (13): ⟨e⟩ [je], ⟨ea⟩ [ja], ⟨ei⟩ [jej], ⟨el⟩ [jel], ⟨ele⟩ [jele], ⟨era⟩ [jera], ⟨erai⟩ [jeraj], ⟨eram⟩ [jeram], ⟨erau⟩ [jeraw], ⟨erați⟩ [jeratsʲ], ⟨este⟩ [jeste], ⟨eu⟩ [jew], ⟨ești⟩ [jeʃtʲ].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 6 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `RO_SOFT_C` | /k/ → [tʃ], before a front vowel, spelled ⟨c⟩ | - | Chitoran 2002 |
| `RO_SOFT_G` | /ɡ/ → [dʒ], before a front vowel, spelled ⟨g⟩ | - | Chitoran 2002 |
| `RO_I_GLIDE_INITIAL` | /i/ → [j], word-initially, before a vowel, with more context in the spec | ⟨iarnă⟩ [ˈjarnə] | [Vasiliu 1965](#src-vasiliu1965), Chitoran 2002, Hayes 2009 |
| `RO_I_GLIDE_POSTVOCALIC` | /i/ → [j], after a vowel, with more context in the spec | ⟨mai⟩ [maj] | Chitoran 2002, Hayes 2009 |
| `RO_FINAL_I_ASYLLABIC` | /i/ → ∅, word-finally, after [b] [d] [dʒ] [f] [ɡ] [h] [k] [m] and 10 more, with more context in the spec | ⟨lupi⟩ [lupʲ] | [Renwick 2014](#src-renwick2014), Chitoran 2002 |
| `RO_FINAL_I_ASYLLABIC_LIQUID` | /i/ → ∅, word-finally, after [l] [r], with more context in the spec | ⟨adevăruri⟩ [adeˈvərurʲ] | Chitoran 2002 |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="cer|cheie|lup|lupi|soare|copii|codri|este|elev|cioban|copil|teorie|cafea|repede|înger|lingură|biserică|zgomot|copilului|acele|șase|şase" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ro-RO")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| cer | [ˈtʃer] |
| cheie | [ˈkeje] |
| lup | [ˈlup] |
| lupi | [ˈlupʲ] |
| soare | [ˈso̯are] |
| copii | [koˈpij] |
| codri | [ˈkodri] |
| este | [ˈjeste] |
| elev | [eˈlev] |
| cioban | [tʃioˈban] |
| copil | [koˈpil] |
| teorie | [teoˈrie] |
| cafea | [kaˈfe̯a] |
| repede | [reˈpede] |
| înger | [ɨnˈdʒer] |
| lingură | [linˈɡurə] |
| biserică | [biseˈrikə] |
| zgomot | [zɡoˈmot] |
| copilului | [kopiˈluluj] |
| acele | [aˈtʃele] |
| șase | [ˈʃase] |
| şase | [ˈase] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Romani](rom.md) · [Home](../index.md) · [Romansh →](rm.md)
