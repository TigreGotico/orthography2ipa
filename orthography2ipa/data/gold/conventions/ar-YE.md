# Transcription conventions: Yemeni Arabic (Ṣanʿānī) (ar-YE)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark primary stress with ˈ before the stressed syllable on every lexical word, including monosyllables (ˈbajt, ˈʃams). Function words get no mark (see function_words). Syllabify first: a long vowel (CVː) or a closed syllable (CVC) is heavy, and a geminate closes the syllable before it. Apply the Ṣanʿānī rule in this order. (1) A final superheavy syllable (CVːC, CVCC) takes stress: kaˈtabt, kiˈtaːb. (2) Otherwise stress the rightmost non-final heavy syllable, even if it lies further left than the antepenult: ˈmadrasah (not Cairene madˈrasa), ˈdarras, kiˈtaːbak. (3) If there is no heavy syllable, stress the first syllable: ˈkatab. Stress is computed on the dialect form. There are no case endings, so they never shift stress. Clitics and prefixes inside the written word count as part of it: walˈbajt.

Source: Watson 2002, chapter on word stress, which contrasts Ṣanʿānī with Cairene. This follows the Ṣanʿānī pattern there, not the Cairene window-based rule used in many general descriptions (e.g. Holes 2004).

## Stressed and unstressed words

Unstressed, never marked with ˈ: the article al/l; the prepositions fi, bi, li, min, ʕala, maʕ, ila; the conjunctions wa, fa, ʔaw, ʔinn; the negators ma, la; the relative alladi/ʔilli; all pronominal suffixes and verbal prefix particles inside their host word. Stressed and marked: independent pronouns (ˈʔana, ˈhuː, ˈhiː), demonstratives (ˈhaːða, ˈhaːðiː), interrogatives (ˈman, ˈmaː, ˈkajf), and the existential/negator words used predicatively. Example: ma ˈʃaːf al ˈwalad.

Source: Watson 2002, stress chapter (clitics and affixes do not form stress domains of their own); Holes 2004 on clitic status of particles.

## Pausal forms

Pausal forms apply nowhere as a separate written rule. The lect has no case endings or tanwīn, so they are never written, and MSA-looking words are read with dialect phonology: ˈkitaːb, not kitaːbun. Final short vowels are written as the dialect form has them in every position. Feminine tāʔ marbūṭa is -ah in all positions (ˈmadrasah) and -at only in construct before a following noun or suffix (madraˈsatak). Fossilized adverbial -an is kept as a lexical part of the word: ˈʔabadan. Phonetic pre-pausal devoicing and glottalization of final segments are not written in broad transcription.

Source: Watson 2002 (dialect lacks inflectional case; Ṣanʿānī feminine ending); pre-pausal phonetics per Watson's work on south-western Arabian pausal forms, deliberately left unmarked here.

## Connected speech

Each word is transcribed in its own place, and only these processes are written. (a) The article's initial vowel elides after a vowel-final word and is written on the article's own word: fi lˈbajt. After a pause or a consonant it is written al, with no ʔ: al ˈbajt. Hamzat al-waṣl is likewise vowel-initial without ʔ. (b) Assimilation of the article to a following coronal ('sun letter'), written inside the word that carries the article: aʃˈʃams, adˈdʒabal is not assimilated (dʒ is not a sun letter in this lect). When the article is a separate word, write it assimilated: aʃ ˈʃams. Do not write any other cross-word assimilation, epenthetic vowels, linking or resyllabification.

Source: Watson 2002, chapters on phonological processes (article assimilation, elision); general Arabic description in Versteegh 2001.

## Glides and diphthongs

Glides are consonants j and w, never i̯ u̯ or y. Diphthongs are written as vowel + glide: ˈbajt, ˈjawm, ˈlawn. Ṣanʿānī keeps them as diphthongs, so do not monophthongize them to eː oː. Geminate glides are doubled: ˈsajjaːrah, ˈʔawwal.

Source: Watson 2002, inventory Table 2.2 p.19 and §2.2 (Ṣanʿānī retention of /aj aw/); IPA j for Arabic yāʔ.

## Other choices

### qāf and jīm

ق is always ɡ (IPA ɡ), in religious and Standard words as well: al ɡurˈʔaːn, ˈɡaːl. ج is always dʒ: ˈdʒabal, ˈradʒʒaːl. ك is always k, never tʃ.

Source: Watson 2002 p.11 and §2.2 p.20; Taʿizzī ɡ for jīm (§2.1.6 p.16) is not used.

### interdentals and ḍād

ث θ, ذ ð, ظ ðˤ are retained. ض is ðˤ as well, merged with ظ: ˈðˤahr, ˈʔarðˤ. Never write dˤ or zˤ.

Source: Watson 2002 §2.1.4 pp.14–15, Table 2.2 p.19, §2.2 p.20.

### symbols for emphatics, gutturals and length

Emphatics are tˤ sˤ ðˤ. The gutturals are ħ, ʕ, h and ʔ. Kh and gh are x and ɣ. Hamzat al-qaṭʕ is kept as ʔ: ˈʔakal, suˈʔaːl. Long vowels are aː iː uː. Short vowels are a i u. Geminates are written as doubled consonants, not ː: ˈdarras, ˈʃadd.

Source: Watson 2002, consonant inventory Table 2.2 p.19; long-vowel and geminate notation per IPA broad practice.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
