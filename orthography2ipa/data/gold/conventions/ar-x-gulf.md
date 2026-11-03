# Transcription conventions: Proto-Gulf Arabic (ar-x-gulf)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark primary stress with ˈ before the stressed syllable on every word of two or more syllables, counted on the word as finally transcribed in this sentence. Monosyllables get no mark: fiː, beːt, ʃʃams. The rule works from the end of the word. (1) A final superheavy syllable (CVVC, CVCC, CVVCC) takes the stress: ʃadˈdeːt, kiˈtabt, maˈsaːkiːn → masaːˈkiːn. (2) Otherwise a heavy penult (CVV or CVC) takes it: kiˈtaːbah, ʕinˈdakum, lmaˈdiːna, ilˈbeːt. (3) Otherwise the antepenult takes it: ˈmadrasa, ˈʃaʁala; stress never goes further back than the antepenult. A long vowel makes its syllable heavy. A geminate closes the syllable before it, so that syllable is heavy (ˈʕalla, mʕalˈlim), and the ˈ goes between the two halves of the geminate: ʃadˈdeːt. Pronominal suffixes and the article count as part of the word: ilˈbeːt, kiˈtaːbha. There are no case endings in this lect, so none ever affect stress. Lexicalised -an adverbs follow the same rule: ˈʃukran, ˈdaːyman.

Source: The Classical-type quantity-sensitive rule (final superheavy, else heavy penult, else antepenult) as given for Gulf Arabic by Holes 1990 and Qafisheh 1977 (editions not consulted, no locators). Watson 2002, The Phonology and Morphology of Arabic, ch. 4, gives the same rule for the Bedouin/Gulf type. The spec's own example fiː lmaˈdiːna agrees.

## Stressed and unstressed words

The following are never marked for stress, even when they have two syllables: the article il- (written inside its host); the proclitics b-, l-, w-, fa-; the free prepositions fi/fiː, min, ʕala, ʕan, ʕind, maʕa, ila; the conjunctions w/u, inn, liʔann, law, laːkin; the relative illi; the vocative yaː; the negators maː, laː, muː; the future/habitual proclitic b- and the future particle raːħ when it is used as a particle. For example: ʕala ttaːwla, ʕan ilwalad, illi ʃifta. The following are stressed by the stress rule like content words (monosyllables still unmarked): independent pronouns (ˈʔana, ˈinta, ˈiħna, huː, hiː); demonstratives (ˈhaːða, ˈhaːði, ˈhaːðeːl); interrogatives (ˈʃinu, weːn, ˈleːʃ); the auxiliary kaːn and its inflections (ˈkaːnaw, kaːn); and prepositions carrying a pronominal suffix (ʕaˈleːh, ˈʕindi, ˈwiyyaːh).

Source: Holes 1990 and Qafisheh 1977 (editions not consulted), for the Gulf inventory of clitics and particles. The unstressed treatment of the article and of proclitics follows the spec's sandhi rule AR_GULF_WASL_IL_ARTICLE (fiː lmaˈdiːna).

## Pausal forms

Not applicable as a classical pausal system. Gulf Arabic has no case endings and no productive tanwīn, so each word has the same form at sentence end, at a comma and sentence-internally. If the diacritised input writes a case vowel or tanwīn on a noun, it is not transcribed: كِتابٌ → kiˈtaːb. The exception is the frozen adverbs in -an, which keep -an: ˈʃukran, ˈʔabadan, ˈtaɡriːban. Final ة is -a in every position, never -ah: ˈmadrasa. It is -at only when the word is the first member of a construct and the possessor follows: ˈsaːʕat ilwalad. Before a pronominal suffix it is always -t within the word: ˈmadrasatna.

Source: Holes 1990 and Qafisheh 1977 (editions not consulted), on the absence of case and nunation in Gulf Arabic and on the construct -at. The spec's ية/وة keys carry the same [ja, jat]/[wa, wat] order.

## Connected speech

Only two cross-boundary processes are written, and both change only the second word.
(1) Waṣl elision. The unwritten initial i of the article il- is dropped when the preceding word in the same sentence ends in a vowel. So is the prosthetic i of any word written with initial bare ‹ا›. Examples: fiː lmaˈdiːna (vs. min ilmaˈdiːna); ˈʔana ʃtaˈʁalt. After a consonant-final word, at sentence start, and after a comma, the i stays: ilˈbeːt, min ilbeːt. Stress is then counted on the shortened word: ilˈbeːt but fiː lbeːt.
(2) The sun-letter assimilation of the article is always written inside its word as a geminate: iʃˈʃams, iddaːr, irˈradʒʒaːl; after a vowel these become ʃʃams, ddaːr.
Nothing else is written across word boundaries: no n→m or place assimilation, no voicing assimilation, no linking or liaison symbols, and no resyllabification. Each word keeps its own segments in its own slot.

Source: Spec sandhi rule AR_GULF_WASL_IL_ARTICLE (fiː lmaˈdiːna), and Holes 1990 / Qafisheh 1977 (editions not consulted) for the il- article with sun-letter assimilation. The spec keeps the sun-letter keys with an unraised a seat (assalaːm-type), but this transcription follows the grammars and writes i in those forms too: iʃˈʃams, not aʃˈʃams.

## Glides and diphthongs

Glides are always the consonant symbols j and w, never i̯ u̯ or y. Geminate glides are written double: ˈʔawwal, ˈɡawijja. The old diphthongs *ay and *aw are written as the monophthongs eː and oː: beːt, weːn, joːm, loːn, ˈbeːtitʃ. A sequence aj or aw is written only where the glide carries its own vowel (ħajaˈwaːn, jaˈwadd) or is geminate. ‹و›/‹ي› after a consonant letter are read as uː/iː, or as oː/eː where the word has the old diphthong. In the adjacent pairs يو/وي, the first letter is the glide (bjuːt), and before final ة the letter is the glide (ˈɡahwa → ˈɡɑhwɑ, ˈʕaːfja).

Source: Holes 1990 (ē/ō monophthongs; edition not consulted), as reported in Alshammari 2026 p. 1335. Wikipedia 'Gulf Arabic' (2026), Vowels/Allophony: sˤeːf, moːj, ɡɑhwɑ, ʕaːfja. The spec's َي→eː, َو→oː, وَيْ→weː, يَوْ→joː keys.

## Other choices

### *q reflex

‹ق› is ɡ in all native words: ɡaːl, ˈɡahwa → ˈɡɑhwɑ. q is used only in evidently learned MSA words: ˈqurʔaːn, ˈqaːnuːn. ‹گ› is ɡ.

Source: Holes 1990; Qafisheh 1977; Khalifa et al. 2016 §3 ('/q/ may be realized ... as /g/ as in /ga:l/').

### Velar affrication

k → tʃ and ɡ (< *q) → dʒ only when adjacent to i or iː and not next to an emphatic consonant: tʃibiːr, dʒidir, ˈtʃiːs. Elsewhere they stay velar: ˈkalb, ɡaːl. The 2sg feminine suffix -ik is always -itʃ: ˈbeːtitʃ, ʔuˈbuːtʃ. The masculine stays -ak: ˈbeːtak. Write the affricates without a tie bar: tʃ, dʒ.

Source: Mustafawi 2006/2007 (Qatari) and Matar 1969 (Kuwaiti) as surveyed in Alshammari 2026 p. 1335; Szreder & Derrick 2023 (k~tʃ lexicalised); Wikipedia 'Gulf Arabic', ʔʊˈbʊːt͡ʃ.

### Jiim

‹ج› is dʒ throughout: ˈdʒamal, ˈradʒʒaːl. The eastern-Gulf j variant is not written, so every sentence uses one reflex.

Source: Khalifa et al. 2016 Table 3 (‹ج› → /dʒ/ or /j/, dʒ listed first); Szreder & Derrick 2023 (dʒ~j is synchronic variation).

### Dad/zah and fricatives

‹ض› and ‹ظ› are both ðˤ: ðˤɑʁtˤ, ˈðˤɑhar. ‹ث› is θ and ‹ذ› is ð (interdentals retained). ‹خ› is χ and ‹غ› is ʁ: χubz, ˈʃuʁul.

Source: Holes 1990; Qafisheh 1977; Al Taisan 2019 (ʁ, χ, ðˤɑʁtˤ); Al-Balushi 2016 pp. 85-90 (interdental retention).

### Vowel symbols and emphatic backing

The short vowels are i a u, never ɪ ʊ ə. The long vowels are iː eː aː oː uː. a/aː are written ɑ/ɑː only when the immediately preceding or following consonant is tˤ, sˤ or ðˤ: sˤɑˈbaːħ, tˤɑːħ, ðˤɑʁtˤ.

Source: Holes 1990 phonemic five-long/three-short system (edition not consulted); spec emphatic spreading inherited from ar-x-peninsular (AR_PEN_EMPH_*); Wikipedia 'Gulf Arabic' ðˤ/ɡɑhwɑ examples. The spec writes the article vowel as ɪ in its gold; this transcription writes i.

### Word-final long vowels

A vowel written with a final mater is written long in monosyllables: fiː, maː, laː, huː, hiː. In words of two or more syllables it is written short: ˈʔana, ʕala, ˈbeːtha, ˈbeːtna, ˈʕindi.

Source: Holes 1990 / Qafisheh 1977 (editions not consulted) on final-vowel shortening in Gulf Arabic. This departs from the spec, which reads every ‹ا› as aː.

### Hamza

Write ʔ for written hamzat al-qaṭʿ and for written hamza seats: ʔakal, ˈsuʔaːl. Bare initial ‹ا› has no glottal onset: ism, ilˈbeːt.

Source: Spec feature (5) (Wright I §19-20; Ryding 2005 §2.10 as cited there). Gulf grammars (Holes 1990) note that medial and final hamza is often lost (raːs); this transcription follows the written hamza for consistency.

### Geminates

Write every geminate as a doubled symbol, never with ː: ˈʕalla, mʕalˈlim, ʃʃams.

Source: Spec doubled keys (قَوِيَّة → awijja); the usual practice in Holes 1990 and Qafisheh 1977.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
