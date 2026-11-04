# Arabic dialects

**Family**: Afro-Asiatic > Semitic > Central Semitic | **Script**: Arabic (abjad)

This page covers the spoken Arabic specs: Egyptian, the Peninsular lects, Levantine, Iraqi, the Maghreb and Sudanese. Modern Standard Arabic, the grapheme base of all of them, has its own page: [ar.md](ar.md). For the live list of specs and their tiers, run `orthography2ipa list` or read the [scoreboard](../evaluation/generated/scoreboard.md).

## What the dialect specs share

Every dialect spec descends from Classical Arabic (`arb`) through one of three regional nodes. Each node sets `graphemes_base` to `ar` and `allophones_base` to `arb`. A dialect therefore starts from the MSA grapheme table and the Classical allophone inventory, and declares only its own deltas.

```
arb → ar (grapheme base)
  ├─ ar-x-mashriqi   → arz-EG, acm-IQ → ar-IQ-x-qeltu, apd-SD, shu-TD, apc → apc-SY, apc-LB, apc-JO, apc-PS
  ├─ ar-x-peninsular → ars-SA, acw-SA, acx-OM, ayn-YE, afb → afb-AE, afb-BH, afb-KW, afb-QA
  └─ ar-x-maghrebi   → ary-MA, arq-DZ, aeb-TN, ar-LY, mey-MR
```

A dialect with an ISO 639-3 code of its own is keyed by that code and its country, such as `arz-EG` for Egyptian and `ars-SA` for Najdi. The Gulf and Levantine nodes take the bare codes `afb` and `apc`. The region and private-use tags `ar-EG`, `ar-SA-x-najd`, `ar-x-gulf` and the others for the same varieties are aliases, and they resolve to the same specs.

The resolved rule set of every dialect holds these inherited pieces:

| Inherited from | What | Effect |
|:--|:--|:--|
| `arb` | `AR_EMPHASIS_SPREAD_*` allophone rules | vowels next to an emphatic back to [ɑ ɑː ɪ ɪː ʊ ʊː] |
| `arb` | `AR_WASL_EPENTHESIS` | a bare wasl alif before a sukūn consonant takes /i/ |
| `arb` | `AR_HAMZAT_WASL_ARTICLE` sandhi rule | the article's /a/ elides after a vowel-final word |
| `arb` | article digraphs | sun-letter assimilation when the shadda is written |
| `ar` | `AR_EMPH_BACK_*`, `AR_GLIDE_*` | MSA emphatic backing of /a aː/, and consonantal glides before a vowel |
| `ar` | `stress` block | quantity-sensitive stress |

All dialect specs share the input contract of [`ar`](ar.md): they expect fully diacritized text. Dialectal Arabic is normally written without short vowels, so short vowels, gemination and sukūn surface only where the input writes them. Rules that condition on a short vowel, such as the Gulf and Najdi velar affrication, do not fire on undiacritized text.

### Gold rows and the short-vowel ceiling

Each dialect spec has `arabic_tts` and `gold20_arabic` rows, and many have a `primary_sources` row. The WikiPron rows are `arz-EG` (`arz`), `ary-MA` (`ary`), `apc-SY` (`apc`), `apc-JO` (`ajp`), `afb` (`afb`) and `acw-SA` (`acw`). The harness registers the Mesopotamian and Libyan WikiPron golds under their ISO 639-3 codes `acm` and `ayl`, so those rows carry the ISO code, not `acm-IQ` or `ar-LY`.

The dialect WikiPron golds are undiacritized skeletons, like the `ar` gold described in [ar.md](ar.md#gold-benchmark). Their IPA writes short vowels that the input does not. Two scripts measure how much of a row's error that unwritten material holds. Both use the segment set `a i u ə ɪ ʊ ɛ ɔ e o`, because these dialects also realise the unwritten short-vowel phonemes as reduced or allophonic qualities.

| Script | What it removes | What it measures |
|:--|:--|:--|
| `scripts/folded_per.py` | the short vowels, from the output and the gold | how well the spec does on the material the spelling supplies |
| `scripts/omission_score.py` | the short vowels, from the output only | what a spec that declines to guess short vowels would score |

The omission score is the one number on the same scale as the row's PER. It is a strategy's score, not a floor. Deleting a vowel and guessing it wrong cost the same single edit, so a spec that guesses well scores below it. Folding can raise a row's score above its baseline, because the gold gets shorter and each consonant error weighs more.

The vowel fold explains a large share of the error on these rows, but not all of it. The golds also hold homographs: one skeleton that the file transcribes two or more ways, as `arz` أجر → `ʔaɡr`, `ʔadʒdʒar`, `ʔadʒr`, `ʔaɡɡar`. The harness scores a skeleton against the closest of its transcriptions, so a homograph costs nothing extra. These figures come from the shipped gold, not from a grammar. No spec carries a fold or a vocalisation rule that its input does not supply.

## Defining features by lect

The table gives the spec's first reading of each letter, with the alternates the spec also lists in brackets. "Merged" means the interdentals ث ذ ظ read as stops. "Kept" means they read [θ ð ðˤ].

| Code | Variety | ق | ج | ث ذ ظ | Other modelled features |
|:--|:--|:--|:--|:--|:--|
| `arz-EG` | Cairo | [ʔ] (ɡ, q) | [ɡ] | merged (s z zˤ) | چ [ʒ], wide emphasis spreading, /aj aw/ → [eː oː] |
| `ars-SA` | Central Arabia, Riyadh | [ɡ] (q) | [dʒ] (ɡ) | kept (t d dˤ) | ض [ðˤ], /k ɡ/ → [ts dz] by a front vowel, gahawa epenthesis |
| `acw-SA` | Mecca, Medina, Jeddah | [ɡ] (q) | [dʒ] | merged (θ ð zˤ) | /aj aw/ → [eː oː] |
| `afb` | Gulf node for AE, BH, KW, QA | [ɡ] (q) | [dʒ] (j) | kept | ض [ðˤ], /k/ → [tʃ] and /ɡ/ → [dʒ] by /i iː/, article /il-/ |
| `acx-OM` | Muscat, Ṣalālah | [q] (ɡ) | [dʒ] | kept (t d) | /k/ → [tʃ] by /i iː/ |
| `ayn-YE` | Ṣanʿāʾ | [ɡ] (q) | [dʒ] (ɡ) | kept | ض [ðˤ] |
| `apc` | Levantine node | [ʔ] (ɡ, k, q) | [ʒ] (dʒ) | merged (s z zˤ, θ ð ðˤ) | /aj aw/ → [eː oː], emphasis spreading |
| `apc-SY` | Damascus | [ʔ] (q) | [ʒ] (dʒ) | merged | inherits the node |
| `apc-LB` | Beirut | [ʔ] (q) | [ʒ] (dʒ) | merged | imāla /aː/ → [eː], final /-a/ → [e] |
| `apc-JO` | Amman | [ɡ] (ʔ, q) | [dʒ] (ʒ) | merged | inherits the node |
| `apc-PS` | Palestine | [ʔ] (k, ɡ, q) | [ʒ] (dʒ) | merged | four-way split of ق |
| `acm-IQ` | Baghdad, gilit | [ɡ] | [dʒ] | kept | /k/ → [tʃ] and /ɡ/ → [dʒ] by a front vowel |
| `ar-IQ-x-qeltu` | Mosul, qəltu | [q] | [dʒ] | kept | no velar affrication |
| `ar-x-maghrebi` | Maghreb node | [q] | [ʒ] (dʒ) | merged | پ [p], ڤ [v] |
| `ary-MA` | Morocco | [q] | [ʒ] (dʒ) | merged | /i/ → [ə] before a cluster |
| `arq-DZ` | Algeria | [q] (ɡ) | [ʒ] (dʒ) | merged (z zˤ) | /i/ → [ə] before a cluster |
| `aeb-TN` | Tunis | [q] (ɡ) | [ʒ] (dʒ) | kept (t d dˤ) | imāla /aː/ → [ɛː], /aj aw/ → [iː uː] |
| `ar-LY` | Tripoli | [ɡ] (q) | [ʒ] (dʒ) | merged (θ ð ðˤ) | /aj aw/ → [eː oː] |
| `mey-MR` | Mauritania, Hassaniya | [ɡ] (q) | [ʒ] (dʒ) | kept (t d dˤ) | ض [ðˤ], ڤ [v] |
| `apd-SD` | Khartoum | [ɡ] (q) | [ɟ] (dʒ) | merged (s z zˤ) | /aj aw/ → [eː oː] |

Further specs hang off the same tree. Each one documents its own phonology in its spec `notes`.

| Code | Variety | Parent |
|:--|:--|:--|
| `aec-EG`, `avl-EG`, `arz-EG-x-fayyum` | Upper Egyptian, Eastern Egyptian Bedawi, Eastern Fayyum | `arz-EG` |
| `ars-SA-x-qassim`, `ars-SA-x-shamali` | Qassimi, Northern Najdi | `ars-SA` |
| `afb-SA-x-sharqiya`, `afb-SA-x-dawasir` | Eastern Saudi, Dawāsir | `afb`, `afb-SA-x-sharqiya` |
| `ar-SA-x-janubi`, `ar-SA-x-rijal-alma`, `ar-SA-x-tihama-qahtan` | Janūbi, Rijāl Almaʿ, Tihāmi Qaḥtāni | `ar-x-peninsular` |
| `abv-BH` | Bahārna Arabic of Bahrain | `afb-BH` |
| `adf-OM` | Coastal Dhofari | `acx-OM` |
| `ayn-YE-x-highland`, `ayn-YE-x-manakha` | Central Highland Yemeni, Manākhi | `ayn-YE` |
| `shu-TD`, `shu-NG` | Chadian, Nigerian Shuwa | `ar-x-mashriqi`, `shu-TD` |
| `apc-TR-x-cukurova`, `ar-TR-x-kinderib` | Çukurova, Kinderib | `apc-SY`, `ar-IQ-x-qeltu` |

## Egyptian, Cairene (`arz-EG`)

Cairene inherits the Eastern node `ar-x-mashriqi`. Its signature reflexes are in the grapheme table. The letter ج is [ɡ], so جَمَل is `ˈɡamal`. The letter ق is [ʔ] in inherited words, as in قَلْب `ˈʔalb`, with [q] in learned borrowings and [ɡ] in Bedouin and loan strata. The interdentals merge to stops, with sibilant alternates for learned words, and the emphatics are /tˤ dˤ sˤ zˤ/. The loan letter چ reads [ʒ], because native ج is already [ɡ].

Cairene has wide emphasis spreading, and the `AR_EG_EMPH_BACK_*` rules back /a aː/ next to an emphatic: صَبَاح is `sˤɑˈbaːħ`. The rules `EG_MONO_AY` and `EG_MONO_AW` give /aj aw/ → [eː oː], so بَيْت is `ˈbeːt` and صَوْت is `ˈsˤoːt` (Watson 2002, ch. 2). Sources: Watson (2002), Mitchell (1956), Badawi & Hinds (1986).

## Najdi (`ars-SA`)

Najdi covers central Arabia, Riyadh included, and inherits `ar-x-peninsular` with its emphatic-spreading rules `AR_PEN_EMPH_BACK_*`. The primary reference is Ingham (1994).

ق is [ɡ] in Bedouin and traditional speech, with [q] in MSA loans and proper names such as القرآن. The interdentals are kept. Najdi neutralises the old ض and ظ contrast to one emphatic interdental, so ض reads [ðˤ]: ضَرَب is `ˈðˤɑrab`.

Velar affrication turns /k/ into [ts] and /ɡ/ into [dz] next to a front vowel. The `NAJD_AFFRIC_*` rules give كِلاب `tsiˈlaːb` and قِرْد `ˈdzird`, while كَلْب stays `ˈkalb`. Affrication that is lexicalised before a historical front vowel is not predictable from the spelling and is not captured. Alshammari (2026) gives an Optimality-Theoretic account of the Northern Najdi process.

The gahawa syndrome inserts /a/ after a guttural /h x ɣ ħ ʕ/ in a low vowel, guttural, consonant sequence. The `NAJD_GAHAWA_*` rules rewrite the coda guttural as the guttural plus [a]: لَحْم is `ˈlaħam`.

## Hejazi (`acw-SA`)

Hejazi is the urban speech of Mecca, Medina and Jeddah (Omar 1975, and Abdoh 2010), and inherits `ar-x-peninsular`. ق is [ɡ] in inherited words, so قَلْب is `ˈɡalb`. The [ʔ] reflex sometimes given for Hejazi belongs to Levantine and Egyptian. [q] occurs only in learned borrowings. ج stays the affricate [dʒ].

The urban koine merges the interdentals to stops: ث [t], ذ [d], ظ [dˤ]. The emphatics are /sˤ dˤ tˤ zˤ/, and Hejazi has no velar affrication. The rules `HEJ_MONO_AY` and `HEJ_MONO_AW` give the Classical diphthongs as [eː oː]: بَيْت is `ˈbeːt` and يَوْم is `ˈjoːm`. The result is the eight-vowel system /a i u aː iː uː eː oː/.

## Gulf, Khaleeji (`afb`, `afb-AE`, `afb-BH`, `afb-KW`, `afb-QA`)

`afb` is an abstract node that inherits `ar-x-peninsular`. Emirati, Bahraini, Kuwaiti and Qatari inherit it, so the shared Gulf features live on the node once. The four country specs declare no grapheme overrides of their own. Omani is a Gulf-region dialect, but it is Peninsular and inherits `ar-x-peninsular` directly.

The node gives ق as [ɡ], with [q] as the formal alternate: قَلَم is `ˈɡalam`. The interdentals are kept, Bedouin-type, unlike sedentary Levantine and Egyptian: ثَلاثَة is `θaˈlaːθa` and ذَهَب is `ˈðahab`. ج varies between [dʒ] and [j]. The loan phonemes /p/ and /v/ are integrated, spelt پ and ڤ.

Velar affrication is the defining Gulf feature, and the spec models it with two post-lexical [allophone](../engine/allophony.md) rules. The rule `GULF_K_AFFRICATION` gives /k/ → [tʃ] next to /i iː/: كِتَاب is `tʃiˈtaːb`, and كَلْب stays `ˈkalb`. The rule `GULF_G_AFFRICATION` gives /ɡ/ → [dʒ] in the same context: قِرْد is `ˈdʒird`. The high-front conditioning follows Mustafawi's (2006, 2007) analysis of Qatari, as Alshammari (2026) reports it.

The rule notes record the limits. Johnstone (1967) and Szreder & Derrick (2023) treat [k~tʃ] as a completed phonemic change, with /tʃ/ an independent phoneme. Adjacent emphatics and the OCP also block affrication. The coda case (samak → simatʃ) and Matar's non-adjacent Kuwaiti trigger across /r l/ are not modelled.

The Gulf article is /il-/. The sandhi rule `AR_GULF_WASL_IL_ARTICLE` elides its /i/ after a vowel-final word, as the inherited rule does for the MSA /a/: فِي الْمَدِينَة is `fiː lmaˈdiːna`.

| Code | What the spec notes |
|:--|:--|
| `afb-AE` | /p v tʃ ŋ/ are fully integrated. For Szreder & Derrick (2023), [k~tʃ] is a completed change, so the inherited rule approximates the historical distribution. The [dʒ~j] alternation is a live process: a nearby similar coronal obstruent inhibits the voiced [j] variant, while [tʃ] shows no such inhibition. |
| `afb-BH` | The spec follows the Bedouin-descended Sunni ʕArab variety, which patterns like mainstream Gulf. The sedentary Shia Baḥārna variety has its own spec, `abv-BH`. |
| `afb-KW` | Matar's (1969) /ɡ/ → [dʒ] pattern is noted. The 2fsg suffix -tʃ (kashkasha) is morphology and out of scope. |
| `afb-QA` | The inherited high-front conditioning is Mustafawi's Qatari analysis. Her further blocking contexts (emphatics, the OCP, levelling in broken plurals and verbs) are engine limits. |

## Omani (`acx-OM`)

Omani inherits `ar-x-peninsular` directly. The prestige sedentary speech of Muscat and Ṣalālah keeps qāf as [q], so ق lists [q] first: قَلْب is `ˈqalb`. Bedouin varieties have [ɡ], the northern mountain sedentary speech [k], and Sur and Ṣoḥār [dʒ] (Al-Balushi 2016, p. 88). ج is [dʒ], a free variant of /ɡ/ in most words (Glover 1988, p. 38, in Al-Balushi 2016, p. 89).

The spec applies `OM_K_AFFRICATION`, so كِتَاب is `tʃiˈtaːb`. The rule notes record that this affrication is a Bedouin and interior feature, and that the sedentary Muscat norm does not affricate productively. The coastal Dhofari variety has its own spec, `adf-OM`.

## Ṣanʿānī Yemeni (`ayn-YE`)

The reference variety is highland Ṣanʿānī, per Watson (2002). It inherits `ar-x-peninsular`. Two of its reflexes are the opposite of a "conservative Peninsular" guess, and Watson is explicit about both.

| Feature | Ṣanʿānī reflex | Example | Source |
|:--|:--|:--|:--|
| qāf ق | [ɡ] | قَلْب → `ˈɡalb` | Watson 2002, p. 11, §2.2 p. 20 |
| jīm ج | [dʒ] | جَمَل → `ˈdʒamal` | Watson 2002, p. 11, §2.2 p. 20 |
| interdentals ث ذ ظ | kept | ثَلاثَة → `θaˈlaːθa` | Watson 2002, §2.1.4 pp. 14-15, Table 2.2 p. 19 |
| ḍād ض and ẓāʾ ظ | both [ðˤ] | | Watson 2002, §2.2 p. 20 |

Watson (p. 20) states that "the original voiceless uvular stop, *q, is not realized in any lexemes in the dialect". Even religious words take /g/, as in al-gurʔān. The [ɡ] jīm that some accounts give for "Yemeni" belongs to Cairene and to the lower-Yemeni Taʿizz and Hugariyyah dialects (§2.1.6, p. 16). `ayn-YE` therefore lists [dʒ] first and [ɡ] as the Taʿizzī alternate. The ḍād and ẓāʾ merger to one emphatic interdental loses one Classical phoneme. The Ṣanʿānī imāla is documented as an alternate, not as the primary reflex.

## Levantine (`apc`, `apc-SY`, `apc-LB`, `apc-JO`, `apc-PS`)

The urban Levantine processes live on the node `apc`, and the four city specs inherit them. Each city declares a small delta.

| Feature | Realisation on the node | Source |
|:--|:--|:--|
| qāf ق | urban koine [ʔ], Bedouin and rural [ɡ], central rural Palestinian [k], qəltu enclaves [q] | Fadda 2016, p. 28, after Al-Wer & Herin 2011, p. 60 |
| jīm ج | urban [ʒ], Bedouin and rural [dʒ] | Al-Wer 2020, p. 560 |
| interdentals | urban koine [t d dˤ], rural, Bedouin and Druze speech keeps them | Cotter 2016, pp. 150-154. Fadda 2016, pp. 27-28 |
| diphthongs /aj aw/ | [eː oː] (`AR_LEV_MONO_AY`, `AR_LEV_MONO_AW`) | Almbark & Hellmuth 2015, §1.1. Fadda 2016, p. 30 |
| emphasis spreading | /a aː/ → [ɑ ɑː] next to /tˤ dˤ sˤ ðˤ zˤ/ (`AR_LEV_EMPH_BACK_*`) | Watson 2002. Almbark & Hellmuth 2015, §1 |

The urban vowel system has five long vowels /iː eː aː oː uː/ over three contrastive short vowels /i a u/. The short mid vowels [e o] and schwa are allophones of /i u/. This is the acoustic finding of Almbark & Hellmuth (2015, §3-4) for fifteen Damascene speakers, which refines Cowell's (1964) auditory ten-vowel account. The long mid vowels come from the Classical diphthongs ("coalescence of vowel-glide sequences", §1.1), which is what the monophthongization rules model.

```python
>>> from orthography2ipa import G2P
>>> lev = G2P("apc")
>>> lev.transcribe("بَيْت"), lev.transcribe("صَوْت"), lev.transcribe("صَار")
('ˈbeːt', 'ˈsˤoːt', 'ˈsˤɑːr')
```

### Damascene (`apc-SY`)

Damascene is the most influential prestige koine. ق is [ʔ], ج is [ʒ], and the interdentals are stops: قَلْب is `ˈʔalb` and ثَلْج is `ˈtalʒ`. Almbark & Hellmuth (2015, p. 2) report that Damascene /aː/ is less fronted than Coastal Syrian /aː/. The spec therefore declares no strong imāla rule, and Damascene inherits only the shared rules.

### Beiruti (`apc-LB`)

The salient Lebanese marker is imāla. Classical /aː/ fronts and raises to [eː] outside emphatic, guttural and /r/ contexts, and final /-a/, the tāʔ marbūṭa included, raises to [e]. Rule order does the blocking in one pass. The inherited `AR_LEV_EMPH_BACK_AA_*` rules fire first, and the identity rules `LB_IMALA_BLOCK_GUTT_*` and `LB_IMALA_BLOCK_R_*` keep /aː/ next to a guttural or /r/. Only the plain /aː/ that remains reaches `LB_IMALA_RAISE_AA`.

```python
>>> lb = G2P("apc-LB")
>>> [lb.transcribe(w) for w in ["بَاب", "رَاح", "صَار", "مَدْرَسَة"]]
['ˈbeːb', 'ˈraːħ', 'ˈsˤɑːr', 'ˈmadrase']
```

The Beiruti magnitude of the raise rests partly on secondary description, because Naïm's Beirut grammar was not obtained. The spec `notes` say so.

### Ammani (`apc-JO`)

Ammani is a new dialect that formed from Jordanian and urban Palestinian contact (Al-Wer 2020). Its ق is a socially reallocated variable [ɡ] ~ [ʔ]: third-generation women use [ʔ] consistently, and men use both (Al-Wer 2020, p. 560). The spec lists [ɡ] first as the distinctively Jordanian value. The koine favours the merged stops [t d dˤ], which makes its consonant system "identical to other Levantine cities" (Fadda 2016, pp. 27-28). قَلْب is `ˈɡalb`, جَمَل is `ˈdʒamal` and بَيْت is `ˈbeːt`.

### Palestinian (`apc-PS`)

Palestinian varies along an urban, rural and Bedouin axis. ق shows the classic four-way split (Fadda 2016, p. 28, after Al-Wer & Herin 2011, p. 60). Urban Jerusalem and Jaffa have [ʔ]. The central and northern rural West Bank has [k], with the kaf shift /k/ → [tʃ]. The south, the Bedouin and indigenous Gaza City have [ɡ] (Cotter 2016, p. 152), and qəltu enclaves have [q]. ج is [ʒ] in urban and [dʒ] in rural speech. قَلْب is `ˈʔalb` and جَمَل is `ˈʒamal`.

## Iraqi (`acm-IQ`, `ar-IQ-x-qeltu`)

The gilit/qəltu split is the defining Mesopotamian isogloss. It takes its name from "I said": Muslim Baghdad says gilit, while Mosul and the Jewish and Christian communities of Baghdad say qəltu. Blanc (1964), from fieldwork in 1957 to 1962, showed that in Baghdad the boundary is communal as well as geographical (§2, §7). The Muslim majority speak a Bedouin-type gilit dialect. The Jewish and Christian minorities speak sedentary qəltu dialects that pattern with Mosul.

`acm-IQ` models gilit and inherits `ar-x-mashriqi`. `ar-IQ-x-qeltu` inherits `acm-IQ`, sets ق to [q], and overrides the four affrication rules by id with identity rules. It keeps the shared interdentals and emphatic backing.

| Feature | gilit `acm-IQ` | qəltu `ar-IQ-x-qeltu` | Source |
|:--|:--|:--|:--|
| qāf ق | [ɡ]: قَالَ → `ˈɡaːla` | [q]: قَالَ → `ˈqaːla` | Blanc 1964, §3.26, pp. 26-27. Jasim 2020, §2.4 |
| kāf ك | [tʃ] next to a front vowel (`IQ_GILIT_AFFRIC_K_*`): دِيك → `ˈdiːtʃ` | [k], /k/ and /tʃ/ are separate phonemes: دِيك → `ˈdiːk` | Blanc 1964, §3.25, p. 25. Jasim 2020, §2.9.2 |
| /ɡ/ from qāf | [dʒ] before a front vowel (`IQ_GILIT_AFFRIC_G_*`): قِرْد → `ˈdʒird` | not applicable: قِرْد → `ˈqird` | Blanc 1964, §3.26, p. 28 |
| interdentals | kept: ثَلْج → `ˈθaldʒ` | kept (Mosul, Jewish) | Blanc 1964, §3.2. Jasim 2020, §2.4 |
| jīm ج | [dʒ] | [dʒ] | Blanc 1964 |
| emphatic backing (tafxīm) | /a aː/ → [ɑ ɑː] (`IQ_EMPH_*`): طَالِب → `ˈtˤɑːlib` | inherited | Jasim 2020. Blanc 1964, §3.3 |

Blanc (§3.26): "In J and C, the reflex of OA/q/ is, in practically every instance, /q/. in M, it is usually /g/ … JC/qal/, M/gal/ 'to say'." Jasim (§2.4) states that the /q/ of Muslawi qəltu "is realised as the voiced velar stop [ɡ] in Baghdadi Gilit". MSA-learned words keep /q/ even in gilit, as in القرآن, but the spelling does not separate them.

The spec models the phonetically conditioned part of gilit kāf affrication. The lexicalised part, as in M/čan/ < kān and M/čalb/ < kalb, has lost its trigger vowel and is not predictable from the spelling. Two sub-variety facts are documented and not modelled. Christian Baghdadi merges the interdentals to stops while it keeps /q/ (Blanc 1964, §3.2, and Jasim 2020, §2.3). Old Arabic /r/ becomes [ʁ] or [ɣ] in many Muslawi and Jewish or Christian Baghdadi words, as in M/ras/ ~ JC/ɣas/ 'head' (Blanc 1964, §3.24). The change is lexical.

## The Maghreb (`ar-x-maghrebi`, `ary-MA`, `arq-DZ`, `aeb-TN`, `ar-LY`, `mey-MR`)

The node `ar-x-maghrebi` holds the shared sedentary Maghrebi reflexes: ج [ʒ], merged interdentals, ق [q], and پ ڤ for /p v/. Every country spec inherits them and declares only its deltas.

Across sedentary Morocco, Algeria, Tunisia and urban Libya, ج is the fricative [ʒ], never the Mashriqi affricate [dʒ]. Watson (p. 16) writes that in most Maghribi dialects "the phoneme does not have an initial occlusive element and is realized as /ž/", after Heath (1987, pp. 20-21) for Moroccan.

The most salient Maghrebi trait is short-vowel reduction to schwa and deletion, which builds heavy clusters. The Amazigh substrate drives it, and `ary-MA` links that substrate in its ancestry. Noamane (p. 49) gives the Moroccan vowel inventory as "three underlying short vowels /i, u, a/ and an epenthetic schwa /ə/" with no long vowels. Heath (p. 216) says the koiné "reduce[s] all three short vowels to just one short vowel ə", and original short vowels syncopate in weak metrical positions.

The spec models part of the reduction. `MA_SHORT_REDUCE` and `DZ_SHORT_REDUCE` turn /i/ into [ə] before a consonant cluster. Written short vowels otherwise surface as written, because predicting syncope from spelling is an engine limit.

```python
>>> ma = G2P("ary-MA")
>>> [ma.transcribe(w) for w in ["جَمَل", "قَلْب", "ثَلاثَة", "مِسْكِين"]]
['ˈʒamal', 'ˈqalb', 'taˈlaːta', 'məsˈkiːn']
```

| Code | qāf ق | Interdentals | What else the spec records |
|:--|:--|:--|:--|
| `ary-MA` | [q], the urban reference | merged | French adstrate for /p v e o/ |
| `arq-DZ` | [q] (ɡ), west and Oran [ɡ] | merged | French and Berber (Kabyle) adstrate |
| `aeb-TN` | [q] (ɡ), Bedouin and rural [ɡ] | kept (Gibson 2009) | imāla /aː/ → [ɛː], /aj/ → [iː] (Singer 1984, and Gibson 2009) |
| `ar-LY` | [ɡ] (q), [q] only in recent literary loans (Pereira 2011) | merged in Tripoli, kept in the east and among Bedouin (Benkato 2020, and Owens 1984) | /aj/ → [eː] (Pereira 2010, pp. 66-67) |
| `mey-MR` | [ɡ] (q) (Taine-Cheikh 2007) | kept, ض [ðˤ] | westernmost Bedouin variety |

## Sudanese (`apd-SD`)

The Khartoum and central-Sudan koine belongs to the Egypto-Sudanic group and inherits `ar-x-mashriqi`. Its marquee feature is an archaic palatal jīm, which sets it apart from Egyptian [ɡ] and Levantine [ʒ].

| Feature | Sudanese reflex | Example | Source |
|:--|:--|:--|:--|
| jīm ج | [ɟ] | جَمَل → `ˈɟamal` | Leddy-Cecere 2021, §3.1.1 |
| qāf ق | [ɡ] | قَلْب → `ˈɡalb` | Leddy-Cecere 2021, §3.1. Youssef 2021, §3.1 |
| interdentals | merged, with /s z zˤ/ in loans | ثَلْج → `ˈtalɟ` | Leddy-Cecere 2021, §3.1 |

Leddy-Cecere (§3.1.1) writes that "the palatal articulation /ɟ/ dominates in the core Sudanic region represented by the dialects of Khartoum and the Šukriyya". The Sudanic area also has a distinctive extra emphatic /ḍ/ reflex of *ð (§3.1). Gasim (1965) documents Nubian, Beja and Nilotic influence on the lexicon only. The spec therefore models no substrate sound change. The rules `SD_MONO_AY` and `SD_MONO_AW` give /aj aw/ → [eː oː]. Their notes cite Dickins (2007), which the spec sources list as not obtained in full.

## Sources

The spec `sources` give the page and section for each claim. The table shows which works were read and in what form. A work marked not obtained supports no claim here, except as reported by a work that was read. The `aeb-TN`, `ar-LY`, `mey-MR` and `apd-SD` rule citations come from the `sources` field of those specs.

| Lects | Read | Not obtained |
|:--|:--|:--|
| Egyptian | Watson (2002), Mitchell (1956), Badawi & Hinds (1986) | |
| Najdi, Hejazi | Ingham (1994), Omar (1975), Abdoh (2010), Alshammari (2026) | |
| Gulf, Omani | Alshammari (2026), read in full, whose review (p. 1335) surveys Mustafawi, Matar and Johnstone. Al-Balushi (2016), pp. 85-90. Szreder & Derrick (2023), abstract and published summary | Holes (1990, 2001) and Qafisheh (1977), cited only as reported in the works read |
| Yemeni, Maghrebi | Watson (2002), open-access PDF, pp. 11, 13, 14-16, 19-20. Noamane (2020), pp. 45, 49. Heath (2020), p. 216. Ennaji et al. (2004), pp. 2-7 | Harrell (1962), Heath (2002), Caubet (1993) |
| Levantine | Almbark & Hellmuth (2015), Cotter (2016), Al-Wer (2020), all in full. Fadda (2016), pp. 27-30, 52 | Cowell (1964), cited as reported by Almbark & Hellmuth. Watson (2002) not read in full for emphasis spreading |
| Iraqi | Blanc (1964), OCR full text, §3.2-3.3, §3.24-3.26. Jasim (2020), §2.3, §2.4, §2.9.2 | Erwin (1963) |
| Sudanese | Leddy-Cecere (2021), Youssef (2021) | Dickins (2007) |

- Abdoh, E. (2010). *A Study of the Phonology and Morphology of Urban Meccan Arabic*. PhD diss., University of Kansas.
- Al-Balushi, R. (2016). Omani Arabic: More than a Dialect. *Macrolinguistics* 4(1): 80-125.
- Almbark, R. & Hellmuth, S. (2015). Acoustic analysis of the Syrian Arabic vowel system. ICPhS 2015, paper 0612.
- Alshammari, K.K. (2026). An Optimality-Theoretic Account of Velar Affrication in Northern Najdi Arabic. *Journal of Language Teaching and Research* 17(4): 1333-1341. [doi:10.17507/jltr.1704.19](https://doi.org/10.17507/jltr.1704.19)
- Al-Wer, E. (2020). New-dialect formation: The Amman dialect. In Lucas & Manfredi (eds.), *Arabic and contact-induced change*, 551-566. Language Science Press.
- Badawi, E.S. & Hinds, M. (1986). *A Dictionary of Egyptian Arabic*. Librairie du Liban.
- Blanc, H. (1964). *Communal Dialects in Baghdad*. Harvard Middle Eastern Monographs X, Harvard University Press.
- Cotter, W.M. (2016). One Piece of the Puzzle: Notes on the Historic Interdental Fricatives /θ, ð, ðˤ/ in the Arabic Dialect of Gaza City. *JAIS* 16: 149-162.
- Ennaji, M. et al. (2004). *A Grammar of Moroccan Arabic*. Fès.
- Fadda, H. (2016). *Language Variation in Western Amman*. MA thesis, CanIL.
- Heath, J. (2020). Moroccan Arabic. Ch. 10 in Lucas & Manfredi (eds.), *Arabic and Contact-Induced Change*. Language Science Press.
- Ingham, B. (1994). *Najdi Arabic: Central Arabian*. John Benjamins.
- Jasim, M. (2020). *Tafxiːm in the vowels of Muslawi Qəltu and Baghdadi Gilit dialects of Arabic*. PhD thesis, Newcastle University.
- Leddy-Cecere, T.A. (2021). Interrogating the Egypto-Sudanic Arabic Connection. *Languages* 6(3): 123.
- Mitchell, T.F. (1956). *An Introduction to Egyptian Colloquial Arabic*. Oxford University Press.
- Noamane, A. (2020). Consonant Gemination in Moroccan Arabic. *Journal of Applied Language and Culture Studies* 3: 37-68.
- Omar, M.K. (1975). *Saudi Arabic, Urban Hijazi Dialect: A Basic Course*. Foreign Service Institute.
- Szreder, M. & Derrick, D. (2023). Phonological conditioning of affricate variability in Emirati Arabic. *Journal of the International Phonetic Association* 54(1): 146-164. [doi:10.1017/S0025100323000166](https://doi.org/10.1017/S0025100323000166)
- Watson, J.C.E. (2002). *The Phonology and Morphology of Arabic*. Oxford University Press.
- Youssef, I. (2021). Contrastive Feature Typologies of Arabic Consonant Reflexes. *Languages* 6(3): 141.

---
[← Modern Standard Arabic](ar.md) · [Home](../index.md) · [Kabyle / Taqbaylit →](kab.md)
