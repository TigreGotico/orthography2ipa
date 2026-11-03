# Transcription conventions: Iraqi Arabic (Northern / qəltu) (ar-IQ-x-qeltu)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Write ˈ before the stressed syllable of every word of two or more syllables. Do not mark monosyllables. Syllabify first: a geminate or a medial CC cluster splits across the syllable boundary (mud.da, mad.ra.sa). Then apply these steps in order. (1) A final superheavy syllable (CVVC, CVCC, CVVCC) takes the stress: kiˈtaːb, bilqiˈtˤɑːr, ʃifˈnaːh. (2) Otherwise a heavy penult (CVV, or CVC including the first half of a geminate) takes it: niˈsaːfir, ˈmaktab, ˈmudda, ˈbaːrid, ˈbaːkiʁ. (3) Otherwise the antepenult takes it: ˈmadrasa, ˈkatabat. A word of two light syllables is stressed on the first: ˈʔana. A final open long vowel counts as light for stress and never draws stress: ˈduɣʁiː. Long vowels and geminates count only as syllable weight, as above. Case endings do not exist in the dialect, so they never affect stress. Pronoun suffixes are part of the word and move the stress by the same rule: ˈbeːtak, beːˈtakum. In the rare words that take the epenthetic vowel the orthography writes, the epenthetic vowel is unstressed: ˈsˤɑbir.

Source: Mesopotamian Arabic stress as described for the qəltu dialects in Jastrow 1978 (Die mesopotamisch-arabischen qəltu-Dialekte I, phonology chapter). Not obtained for this pass; the steps are checked against the stress marks in the arbitrated gold quoted in the spec notes (niˈsaːfir, bilqiˈtˤɑːr) and against Watson 2002 ch.4 on weight-sensitive Arabic stress. Blanc 1964 does not treat stress separately for the communal dialects.

## Stressed and unstressed words

Monosyllabic function words are unstressed and carry no ˈ. This covers the conjunctions w/u, aw, bass, fa; the prepositions fi, ʕa, mən, ʕan, la; the particles maː, laː, qad, ja; and monosyllabic auxiliaries or pseudo-verbs when they are their own word, such as kaːn, ʕand as a separate word, and fiː. Proclitics written attached to their host are part of the host word and are never stressed: the article l-, b(i)-, l(i)-, w(u)-, k(a)-. Examples: bilbeːt, wilwalad, lilmadrasa. Polysyllabic function words keep their lexical stress mark by the stress rule: ˈʔana, ˈʔənta, ˈhaːða, ˈhaːðiː, ˈʔiða, ˈwaktiː. Independent pronouns are always marked when they have two or more syllables. Pronoun suffixes are never separate words and never take stress on their own, apart from the general rule (beːˈtakum).

Source: General Mesopotamian Arabic practice in Blanc 1964 ch.4 (communal morphology, qəltu particles mən, qad, fiː) and Jastrow 1978; Watson 2002 ch.4 for the clitic/stress interaction.

## Pausal forms

Does not apply. The dialect has no case endings, no tanwīn and no pause-conditioned alternations, so every word is written the same at the end of the sentence, at a comma and phrase-internally. Do not write any MSA case vowel or tanwīn that appears in the vocalised input. The only exception is lexicalised adverbial -an in fixed words, which is written as part of the word in all positions: ˈʃukran, ˈʔabadan, ˈtaqriːban. Tāʾ marbūṭa is -a everywhere (ˈmadrasa). It is -at- only before a suffix or in a construct written with the t (madrasˈtak, madrasat il...).

Source: Blanc 1964 ch.4 (dialect morphology without iʿrāb); Watson 2002 §1 on the loss of case and nunation in the modern dialects.

## Connected speech

No cross-word processes are written. Each word keeps its citation form whatever its neighbours. Do not assimilate, elide, link or resyllabify across a word boundary, and do not delete an initial vowel after a vowel-final word. Within a word, the article assimilates fully to a following coronal ('sun letter') and stays l before others: issˤɑbir, iʃʃams, iddaːr, but ilqiˈtˤɑːr, ilbeːt. A word-initial article is written il-, with no glottal stop, in every position (hamzat al-waṣl is never ʔ). After an attached proclitic the article vowel drops: bilqiˈtˤɑːr, wiʃʃams, lilbeːt. A hamzat qaṭʿ is written ʔ word-initially in all positions: ʔaʕʁif, ʔana.

Source: Within-word article assimilation as in Blanc 1964 ch.4 and Jasim 2020 §2 transcriptions (ɑsˤsˤɑbir in the gold). The no-cross-word-sandhi rule is a convention of this transcription set chosen for row-to-row consistency, not a claim about fast speech.

## Glides and diphthongs

Write consonantal glides as j and w, never as i̯ u̯ or y: jeːt, walad, ʔajjaːm, ˈqawwa. Geminate glides are doubled. Final -iy and -uw are the long vowels iː and uː: ˈduɣʁiː, ˈkursiː. The old diphthongs *ay and *aw are written as the monophthongs eː and oː in native words: beːt 'house', joːm 'day', ʃoːf. This applies even when the input writes fatḥa plus sukūn on yāʾ/wāw; it departs from a literal reading of the vocalised orthography. Write aj or aw only where the glide is geminated or followed by a vowel (ʔajjaːm, ˈhawa), or in evident MSA loans read as such.

Source: Blanc 1964 ch.3 (vowels: ē, ō from the old diphthongs in the communal dialects); Jastrow 1978 for Mosul ē, ō. Symbol choice follows the spec's broad IPA.

## Other choices

### qāf

Write qāf ق always as q, never ɡ: qal, ˈqəltu written ˈqiltu per the orthography's vowels, bilqiˈtˤɑːr.

Source: Blanc 1964 §3.26 pp.26–27; Jasim 2020 §2.4.

### kāf and jīm

kāf is always k and never tʃ, so there is no affrication: kalb, ˈbaːkiʁ. Write tʃ only for written چ in loans. jīm is dʒ: dʒaːr.

Source: Jasim 2020 §2.9.2.

### interdentals

Keep θ, ð, ðˤ as written: θaˈlaːθa, haːða, ðˤɑhar. Do not apply the Christian Baghdadi merger to t, d, dˤ.

Source: Blanc 1964 §3.2; Jasim 2020 §2.3–2.4 (majority Mosul/Jewish reflex).

### rāʾ

Write r by default. Write ʁ only in the lexemes the spec lists as Muslawi-r words (baːkiʁ, ʔaʕʁif, duɣʁiː). Use ʁ, not ɣ, for this reflex. Keep r next to emphatics: bilqiˈtˤɑːr, ˈsˤɑbir. Do not extend ʁ to other words by analogy.

Source: Blanc 1964 §3.24 p.25 ('in many instances'); Jasim 2020 §2.4 ([ʁ] variants). The lexical list follows the spec's word exceptions.

### emphatic backing (tafxīm)

Write a and aː as ɑ and ɑː in a word containing tˤ, sˤ, dˤ or ðˤ (and q-adjacent ɑ where the spec backs it): tˤɑːr, sˤɑbir. Elsewhere write a and aː. Emphatic consonants carry ˤ.

Source: Jasim 2020 (whole thesis, Muslawi Qəltu tafxīm).

### short vowels and imāla

Write the short vowels a, i, u exactly as vocalised. Use i, not ə, for the short high central-front vowel, so qəltu is written qiltu. Do not write Mosul imāla (ā > ē/ī); keep aː as written. Published descriptions (Jastrow 1978) report imāla in Mosul, but it is lexically and phonologically irregular, so it is not transcribed.

Source: Spec input contract (vocalised input); Jastrow 1978 on Mosul imāla (not obtained), departed from for consistency.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
