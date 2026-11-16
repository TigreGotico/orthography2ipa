# Transcription conventions: Najdi Arabic (ars-SA)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark primary stress with ˈ before the stressed syllable on every word of two or more syllables. Monosyllables get no mark: [beːt], [ɡaːl]. Find the stress on the whole space-delimited word, counting the article, proclitics (w-, b-, l-, f-) and pronoun suffixes, with syllables built from the vowels the transcription writes. (1) If the final syllable is superheavy (CVːC or CVCC, including a final geminate), stress it: [kiˈtaːb], [alˈbeːt], [ʕaˈleːk], [ˈħadʒdʒ] (a monosyllable, so in practice unmarked). (2) Otherwise, if the penult is heavy (CVː, or CVC including the first half of a geminate), stress the penult: [ˈmaktab], [kiˈtaːbah], [muˈʕallim]. (3) Otherwise stress the antepenult, never anything further left: [ˈkatabat], [ˈmadrasa]. A disyllable with a light penult and a non-superheavy final syllable takes penult stress: [ˈwalad], [ˈkatab]. (4) The article and the one-consonant proclitics never take stress. If the rule lands on them, move stress to the next syllable: [alˈwalad], [wilˈbint]. (5) In a gahawa form, stress the syllable that begins with the guttural: [ɡaˈhawa], [naˈxala]. (6) Long vowels count as heavy wherever they are written. Najdi has no case endings, so they never count (see pausal_forms).

Source: Ingham 1994, ch.1 phonology (pp.13-20), quantity-sensitive Najdi/Bedouin stress; Watson 2002, word-stress chapter (Eastern-Arabic rightmost-heavy/antepenult pattern). The spec notes that Najdi stress is not orthography-predictable; this rule is applied to the vowels as written, without the Najdi high-vowel elision the spec does not model.

## Stressed and unstressed words

Write no stress mark on these unstressed function words, even if they have two syllables: prepositions [fi], [min], [ʕala], [ʕind], [maʕ]; conjunctions [w]/[u], [walla], [law], [ʔinn]; the relative [ʔilli]; and every bound clitic, i.e. the article al-, proclitics b- l- f- w-, and pronoun suffixes such as [-ah], [-ha], [-ik]/[-its], [-na], [-hum]. Bound clitics change the stress of their host by the stress rule but never carry it themselves. These carry normal lexical stress and are marked when polysyllabic: independent pronouns ([ˈʔana], [ˈʔinta], [ˈhuwa], [ˈhija]); demonstratives ([ˈhaːða], [ˈhaːði]); interrogatives ([ˈwiʃʃ], [ˈleːʃ]); negators [maː] and [muː]; the auxiliary [kaːn] (inflected forms such as [ˈkaːnat]). Keep the vowel length the orthography writes, also on unstressed words: [maː], [fi].

Source: Ingham 1994, ch.1 and the morphology chapters (pronouns, particles); Alruwaili 2020 for mā/lā vs mū; the gold rows of the spec (مو [muː], ما [maː]).

## Pausal forms

Nowhere. Najdi has no case inflection and no tanwīn, so the same form is written at sentence end, at a comma and inside the sentence. If vocalised input writes a Classical case vowel or tanwīn on a word (ـُ ـِ ـَ, ـٌ ـٍ ـً), leave it untranscribed everywhere. This departs from the spec's 'transcribe what the harakat give'. The one exception is lexicalised adverbial -an, which is kept: [ˈʃukran], [ˈʔabadan]. Write tāʔ marbūṭa as [a] in the absolute form ([ˈmadrasa], [ɡaˈhawa]) and as [at] before a pronoun suffix or in a construct with a following noun ([madraˈsatah]). Word-final stem vowels that are not case endings stay as written: [ˈʔana], [ˈhaːða].

Source: Ingham 1994 (no case/tanwīn in Najdi; feminine -a / construct -at); Holes 2004, chapter on dialect morphology (loss of case and nunation in the modern dialects).

## Connected speech

Write every word in its citation form. No assimilation, elision, liaison, linking or resyllabification is written across a word boundary. A vowel-final word followed by the article stays as written: [fi] [alˈbeːt], not [fi lbeːt]. Written word-initial hamza (أ إ آ, and initial vowels of pronouns and verbs) is written [ʔ] even after a vowel: [ˈʔana]. The article written with bare alif (hamzat al-waṣl) is [al] with no [ʔ]. Inside the word, these processes are written: article assimilation to a following coronal (t d θ ð s z ʃ sˤ ðˤ tˤ r l n) as a geminate, [aʃˈʃams], [arˈradʒil], with no assimilation before [dʒ] ([aldʒaˈmal]); emphatic backing of /a aː/ to [ɑ ɑː] next to an emphatic in the same word, [ˈtˤɑːlib], [ðˤɑˈruːf]; velar affrication and gahawa epenthesis (see other). The Najdi elision of an unstressed high vowel in an open syllable (katab→ktab, kitaːb→ktaːb) is not written.

Source: Ingham 1994 pp.13-20 (article assimilation, emphasis, elision), following the spec's input contract that vowels are transcribed as written with no resyllabification; the emphatic backing follows the spec's peninsular parent (AR_PEN_EMPH).

## Glides and diphthongs

Write consonantal glides as [j] and [w], never as [i̯ u̯]: [ˈwalad], [jaˈɡuːl], [ˈsajjaːra], [ˈʔawwal]. ي and و after a consonant with kasra/ḍamma or unvocalised as a long vowel are [iː] [uː]: [kiˈbiːr], [ˈsuːɡ]. Old Arabic *ay and *aw before a consonant or word-finally are written as the monophthongs [eː] [oː]: [beːt], [ʃoːk], [foːɡ], [ʕaˈleːk]. This disagrees with the spec note, which keeps the diphthongs [aj aw] in central Najdi. Before a vowel or as part of a geminate they stay [aj] [aw] + vowel, written as [j] [w].

Source: Ingham 1994 p.15 (/eː oː/ in the Najdi vowel system); Algethami 2023 pp.3384-3385 ([beːt]); Al Mahmoud 2020 ([tsef], [ʃok]); Alshammari 2026 p.1336 ([ʃoːk]). This departs from the spec's diphthong-retention note.

## Other choices

### qāf

Write ق as [ɡ] in native words: [ɡaːl], [ɡalb]. Write [q] in MSA loans, religious terms and proper names, especially before /u/: [alqurˈʔaːn], [ˈqibla]. Write گ as [ɡ].

Source: Ingham 1994 pp.13-16; Mahzari 2023 Tables 5-6 p.804; AlAjroush 2020 p.42.

### jīm

Write ج as [dʒ], the urban Riyadh norm, never [ɡ]: [dʒaˈmal], [ˈradʒil].

Source: AlAjroush 2020 p.42; the spec gives a Bedouin [ɡ] variant, which is not used.

### ḍād/ẓāʾ

Write both ض and ظ as [ðˤ]: [ðˤɑˈruːf], [ˈðˤuhur]. Do not use the urban [dˤ] variant.

Source: Ingham 1994; AlAjroush 2020 p.42 ('almost always realised as [ðˤ]').

### interdentals

Keep ث [θ] and ذ [ð]: [θaˈlaːθ], [ˈhaːða].

Source: Ingham 1994; AlAjroush 2020 p.42.

### velar affrication

Write ك as [ts] (no tie bar) when [i iː eː] is in the same syllable, before or after it: [tsiˈbiːr], [dits], [tseːf], and 2fs suffix [-its] as in [ˈʔabuːts]. Write ق=/ɡ/ as [dz] only when [i iː] is in the same syllable: [ˈdzidir], [ˈriːdz]. Never affricate next to /a aː/ (Riyadh): [kalb], [ɡalb]. The exception is چ, which is always [ts]: [tsaːn]. Never affricate next to back vowels ([kum], [ˈɡumar]), in MSA loans or in [q] words.

Source: Al Mahmoud 2020 §3.1; Mahzari 2023 Tables 2 and 4 pp.800-803; Alshammari 2026 pp.1335-1337 (voicing asymmetry; the Northern Najdi extension to /a/ is not adopted).

### gahawa syndrome

After /a/ + guttural (h x ɣ ħ ʕ) + consonant, insert [a] after the guttural, then place stress as in rule (5): [ɡaˈhawa], [naˈxala], [ʔaˈxadˤar].

Source: Ingham 1994; Watson 2002 (Bedouin gahawa syndrome).

### short vowel quality

Write short vowels as the broad symbols [i u a], not the centralised [ɪ ʊ ə] that the acoustic studies report. Write [ɑ ɑː] only for emphatic backing.

Source: Algethami 2023 p.3385 and Ingham 1994 p.15 (centralised short i u are allophonic).

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
