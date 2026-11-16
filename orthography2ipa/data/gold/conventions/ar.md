# Transcription conventions: Arabic (ar)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark one primary stress ˈ on every stressed word (see function_words); unstressed function words carry no mark. Never mark secondary stress. Syllabify the word exactly as it is written in that sentence, with case endings, tanwīn, attached clitics and suffixes when pronounced, and in pausal shape when paused. A geminate closes the preceding syllable (muʕ.al.lim → mu.ʕal.lim). Light = CV; heavy = CVː or CVC; superheavy = CVːC or CVCC (word-final only). Rule: (1) a final superheavy syllable takes the stress: kiˈtaːb, ʔalˈbaːb, ʔant. (2) Otherwise a heavy penult takes the stress: kiˈtaːbun, muˈʕallim, darˈsun → ˈdarsun. (3) Otherwise stress the antepenult, never further left: ˈkataba, ˈmadrasa, ʔalˈmadrasa, kiˈtaːbuhu, waˈkataba. (4) A disyllable with no superheavy final is stressed on its first syllable (ˈkatab, ˈbajtun); a monosyllable is stressed (ˈbajt). Long vowels and geminates count only through syllable weight. Case endings count as syllables when pronounced and may move the stress: ˈmadrasatun vs pausal ˈmadrasa. The article and other attached proclitics count as part of the word. Place ˈ before the onset of the stressed syllable. When that onset is the second half of a geminate, place ˈ between the two halves: ʔaʃˈʃamsu. This follows the Eastern/Levantine-style MSA stress tradition, not the Egyptian one, which would give madˈrasa. The notes declare no stress block; this convention adds stress marking that the spec itself omits.

Source: Ryding 2005, ch. 2 (syllable structure and word stress); Watson 2002, ch. 4 (stress), which gives the Eastern vs Egyptian MSA stress patterns; Holes 2004, ch. 3.

## Stressed and unstressed words

Unstressed, no ˈ: separate prepositions (fiː, min, ʕan, ʕalaː, ʔilaː, maʕa, ħattaː, munðu, ladaː), conjunctions and particles (ʔaw, θumma, ʔam, bal, lakin, lakinna, ʔan, ʔanna, ʔinna, ʔiðaː, law, qad, sawfa, lam, lan, laː, maː when negative, jaː, hal, ʔa- interrogative), and the relative ʔallaðiː/ʔallatiː/ʔallaðiːna. Proclitics wa-, fa-, bi-, li-, ka-, sa- and the article ʔal- belong to their host word. They take no stress of their own, but they count in syllabifying the host: waˈkataba, bilˈqalami. Pronoun suffixes (-hu, -haː, -ka, -naː, -hum, ...) also belong to the host and count for its stress: kiˈtaːbuhu. Stressed, with ˈ: independent pronouns (ˈʔanaː, ˈhuwa, ˈhija, ˈnaħnu), demonstratives (ˈhaːðaː, ˈhaːðihi, ˈðaːlika), interrogatives (ˈmaːðaː, ˈman, ˈkajfa, ˈʔajna, ˈmataː, ˈlimaːðaː), and the auxiliaries and copulas ˈkaːna, ˈlajsa, ˈsˤɑːra, ˈʔasˤbɑħa. Also stressed: laː and maː when they stand alone as an answer, and any function word that is contrastively focused.

Source: Ryding 2005, ch. 2 and the chapters on particles and pronouns; Watson 2002, ch. 4 (clitics as part of the stress domain).

## Pausal forms

Apply the pausal form (waqf) to the last word before any phrase-ending punctuation mark: . ? ! : ; , and also at the end of the text. Apply it nowhere else. Every non-pausal word keeps full iʿrāb as diacritized: case and mood vowels, tanwīn -un/-in/-an, and ة as t before its vowel (madiːnatun, madiːnatu lˈwalad). At a pause: (a) drop a word-final short vowel, whether case, mood, verbal or pronominal: ˈkataba → ˈkatab, kiˈtaːbu → kiˈtaːb, ˈʔanta → ʔant, kiˈtaːbuhu → kiˈtaːbuh. (b) Drop tanwīn -un/-in entirely: ˈbajtun → ˈbajt. (c) Accusative tanwīn -an becomes -aː: ˈkitaːban → kiˈtaːbaː. (d) ة with its ending becomes -a: ˈmadrasatun → ˈmadrasa, not -ah and not -at. (e) Word-final long vowels stay: fiː, ˈʕalaː, jaˈktubuː. Re-apply the stress rule to the pausal shape. A word right after a pause behaves as utterance-initial for hamzat al-waṣl (see connected_speech). This agrees with the spec note that ة at a pause is /a/.

Source: Ryding 2005 §2.3.2 (tāʾ marbūṭa silent only at pause) and ch. 2 on pausal form; Holes 2004, ch. 3 (pausal vs contextual forms in MSA reading); Versteegh 2001, ch. 6.

## Connected speech

Each word stays in its own slot, and only the words at a boundary change. (1) Hamzat al-waṣl: the article ʔal- and waṣl-initial words (ibn, ism, imraʔa, ithnaːni, imperatives, and Form VII–X perfects and maṣdars) lose their ʔ and initial vowel after any word inside the same phrase: ˈbaːbu lˈbajti, qaːla bˈnuhu. They keep ʔ plus vowel only at utterance start or after a pause: ʔalˈwaladu. (2) A word-final long vowel shortens before the resulting consonant cluster, and the short vowel is written on the first word: fiː + ʔalbajti → fi lˈbajti; ʔilaː + ʔalmadrasati → ʔila lˈmadrasati. (3) A consonant-final word before a waṣl cluster takes a helping vowel, written at the end of the first word. Use -a after min (mina lˈbajti), -u after the plural pronoun suffixes -tum/-hum/-kum (ʕalajhimu lˈqitaːlu), and -i everywhere else, including tanwīn (ˈbajtuni lˈwaladi, lami lˈwaladu, qadi ...). (4) Sun-letter assimilation of the article's l to a following coronal (t θ d ð r z s ʃ sˤ dˤ tˤ ðˤ l n) applies always, written as a geminate inside the host word: ʔaʃˈʃamsu, wa ʃˈʃamsu after waṣl, fi ttˤˈtˤɑːwilati. Lexical d͡ʒ, k, q etc. do not assimilate. (5) Write no other cross-word assimilation: no Quranic idghām, iqlāb or ikhfāʾ (min ˈbajtin, not mim ˈbajtin). Write no linking or syllable marks. Resyllabification is not shown, and no ‿ or . is used.

Source: Ryding 2005, ch. 2 (hamzat al-waṣl, helping vowels, sun and moon letters); Watson 2002 (sun-letter assimilation as coronal-place rule); Holes 2004, ch. 3.

## Glides and diphthongs

Consonantal glides are j and w, in onsets and codas alike: ˈwalad, jaˈktubu. Diphthongs are written as short vowel plus glide, aj and aw: ˈbajt, ˈjawm. Never use i̯, u̯, ai or au. Geminate glides are doubled: qawˈwaːs, ʕujˈjina, ˈmisˤrijj in pause, misˤˈrijjun, ħurˈrijja. Long vowels are iː, uː and aː, never ij, uw or ii: fiː, jaˈqu:lu → jaˈquːlu. A glide before a vowel is consonantal: ˈsajjida, ʔaˈjjaːm → ʔajˈjaːm.

Source: Ryding 2005, pp. 15–16 (waaw/yaa as consonants, gemination) and pp. 29–30 (diphthongs /aw/, /ay/); spec notes (AR_GLIDE rules).

## Other choices

### emphasis (pharyngealization) and vowel backing

Write the emphatics as tˤ dˤ sˤ ðˤ. Write ض as dˤ, not ɮˤ, per the spec note. Write a and aː as ɑ and ɑː only when directly adjacent, before or after, to an emphatic in the same word: ˈtˤɑːlib, ˈsˤɑbr, ʔalˈʔɑrdˤ in pause. Do not spread further, and do not back after q, x, ɣ or r: ˈqalb, ˈxabar. i and u are never changed. This follows the spec's AR_EMPH_BACK rule. Watson describes wider, word-level spreading, which this broad convention deliberately does not write.

Source: Ryding 2005, pp. 33–35; Watson 2002, ch. on emphasis; spec notes.

### realization of ج and other variable consonants

ج is d͡ʒ throughout: ˈd͡ʒamiːl, masˈd͡ʒid. Do not use the regional ʒ, g or ɟ. ق is q, ث is θ, ذ is ð, ظ is ðˤ. Do not use dialectal ʔ, t, s, d, z or dˤ for these.

Source: Thelwall & Sa'Adeddin 1990 (JIPA illustration); Watson 2002 (consonant inventory); Holes 2004, ch. 3 on MSA standard vs regional realizations.

### glottal stop and gemination

Write hamza as ʔ wherever pronounced, including word-initially at utterance start and in hamzat al-qaṭʿ words after other words (wa ʔakala → waˈʔakala, min ʔaˈħadin). It is never dropped except under waṣl. Write shadda as a doubled consonant, never with ː: ˈʕamma, muˈʕallim.

Source: Ryding 2005, p. 16 ('strong hamza is a regular consonant'), pp. 15–16 (gemination).

### tāʾ marbūṭa in construct (iḍāfa) and vowel inventory

Inside a phrase, ة is always t followed by its case vowel, in iḍāfa as elsewhere: madiːnatu lˈqudsi, ˈmadrasatun. It is -a only at a pause. Alif maqṣūra is aː: ˈʕalaː, ˈmustaʃfaː. It shortens before a waṣl cluster. The vowel symbols are only a i u aː iː uː, plus ɑ ɑː by the emphasis rule. Never use e, o, ə or ɪ.

Source: Ryding 2005 §2.3.2 and ch. 2 vowel system; spec notes.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
