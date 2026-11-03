# Transcription conventions: Rijāl Almaʿ Arabic (ar-SA-x-rijal-alma)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark one primary stress per stressed word with ˈ placed before the onset of the stressed syllable. Do not write syllable dots or secondary stress. Monosyllabic content words also get ˈ. Find the stress by counting from the end of the word as written, including suffixes and any vowel written in the harakat. (1) If the final syllable is superheavy (CVVC, CVCC or CVVCC), stress it: [ɡaːˈbalt] 'I met', [kaˈtabt], [maˈdaːris] is not this case (see 2). (2) Otherwise, if the penult is heavy (CVV or CVC), stress the penult: [maˈdaːris], [ˈbajtak], [ˈmaktab]. (3) Otherwise stress the antepenult: [ˈsaraɡu] 'they stole', [ˈbaɡara]. Never go further back than the antepenult. Disyllables with two light syllables take initial stress: [ˈbaɡar], [ˈwalad]. Long vowels make a syllable heavy, but a word-final open long vowel counts as light: [ˈmaʃa] or [ˈmaʃaː] is stressed on the first syllable either way. A geminate closes the preceding syllable, which makes it heavy. Split the geminate around ˈ: [muˈdarris], [ˈdarrasat], [ʃaˈbbaːk] → write [ʃabˈbaːk]. Case vowels and tanwīn written in the harakat count as ordinary syllables when stress is computed in non-pausal position. After pausal deletion (see pausal_forms), recompute the stress on the remaining form.

Source: The Eastern-Arabic / Levantine-type weight rule (final superheavy > heavy penult > antepenult) as set out in Watson (2002), The Phonology and Morphology of Arabic, ch. 5 (syllable structure and stress). Asiri (2009), which describes Rijāl Almaʿ prosody directly, is not held locally. This rule is a general peninsular-sedentary default, not a verified Rijāl Almaʿ-specific statement.

## Stressed and unstressed words

Function words that receive no ˈ: the definite article [im]/[m]; single-consonant proclitics b-, l-, w-, f-, k- written on their host ([wimˈbaɡar]); pronominal enclitics, which take no stress of their own, although the host's stress may shift onto them by the weight rule ([kaˈtabtah], [ˈbajtak]); and monosyllabic or disyllabic prepositions written as separate words, such as fi, min, ʕala, ʔila, maʕ, ʕan ([fi mˈbajt], [min], [ʕala]). Also unstressed: the coordinating conjunctions ʔaw and θumma, the relative pronoun, and the copula-like particle ʔinna. Function words that do receive ˈ: independent pronouns ([ˈʔana], [ˈhuː]), demonstratives, interrogatives, negators ([ˈmaː], [ˈlaː]), auxiliary and modal verbs, and all content words.

Source: General peninsular practice in Watson (2002), ch. 5. The article form follows Asiri (2008:72-73) as quoted in Alfaifi (2024:177-178): m=walad, im=bagar, m=bayt. Asiri (2009) was not checked locally for stress on function words.

## Pausal forms

Apply pausal forms only to the last word of a sentence, before . ! or ?, and to the last word before a comma, semicolon or colon. Elsewhere use context forms. The dialect has no case inflection, so pause mainly affects vocalised classicisms. In pause: delete a final short vowel written in the harakat (a classical -u/-i/-a case vowel becomes zero: [kiˈtaːb]); delete tanwīn -un and -in ([kiˈtaːb]); reduce tanwīn -an to [a] ([ˈʃukra]). Tāʾ marbūṭa is [a] in pause and in non-construct context ([ˈbaɡara]). It is [at] in construct and before suffixes ([baɡarat ˈʕali], [baˈɡaratah]). Hamza and long vowels are not otherwise altered. Recompute stress after deletion: [kiˈtaːbun] in context becomes [kiˈtaːb] in pause.

Source: Classical waqf rules as summarised in Watson (2002). The tāʾ marbūṭa realisation [a]~[at] is the general peninsular pattern. Asiri (2009) was not checked locally for Rijāl Almaʿ pausal phenomena.

## Connected speech

Keep every word in its own place, and write each word in its citation form, with two exceptions. (1) Article and hamzat al-waṣl allomorphy. The definite article, and any other word-initial hamzat al-waṣl (for example form VII/VIII verbs, ism, ibn), is written as [im]/[i] without a glottal stop at sentence start or after a consonant-final word: [imˈbaɡar], [inˈkasar]. After a vowel-final word, the prop vowel is dropped and the article is written [m]: [ˈʃaːfu mˈbaɡar], [fi mˈbajt]. The article never assimilates to a following coronal; write [imˈʃams], not *[iʃˈʃams]. The name Allah keeps [aɫˈɫaːh]. (2) Pausal forms, as under pausal_forms. Do not write cross-word place or voicing assimilation, resyllabification, linking consonants or vowel coalescence. A real hamza ء is always written [ʔ], even after a vowel.

Source: Article forms m= / im= follow Asiri (2008:72-73) as quoted in Alfaifi (2024:177-178). The vowel-conditioned choice between [m] and [im] is an inferred generalisation from those examples, not an explicit published rule. The broad, no-cross-word-assimilation policy is a transcription decision.

## Glides and diphthongs

Write glides as consonantal [j] and [w], never [i̯ u̯]. Write the retained diphthongs as [aj] and [aw]: [ˈbajt] 'house', [ˈjawm], [mˈbajt]. Do not monophthongise them to [eː] or [oː]. Write long vowels as [aː], [iː], [uː], not as [ij] or [uw]: [kaˈbiːr], [ˈjuːmiːn] → write [juːˈmiːn]. Write intervocalic or geminate glides as consonants: [ʔaˈjjaːm], [ˈɡawwa] → write [ɡawˈwa] only if the weight rule requires it.

Source: Diphthong retention per Asiri (2008:72-73) via Alfaifi (2024:177-178): m=bayt, not *beet. The symbol choice is the spec's broad-IPA practice.

## Other choices

### lateral emphatics

Write ض as [ɮˤ] and ظ as [ɬˤ] in every word, by grapheme, and keep the two distinct: [jiˈɮˤaːrib] 'he fights', [ˈɮˤarf] 'circumstance' (spelled with ظ, so written [ˈɬˤarf]), [ɬˤaːˈmiː] 'thirsty'. Do not apply the lexical exceptions noted by Watson & Al-Azraqi (2011:428).

Source: Watson & Al-Azraqi (2011:427-428), citing Asiri (2009); Al-Azraqi (2010). The spec's grapheme mapping is followed.

### qāf and ǧīm

Write ق as [ɡ] everywhere: [ɡaːˈbalt], [ˈbaɡar], [ˈɡatˤaʕaw]. Use [q] only in unmistakable classical citations, such as Qurʾānic quotations. Write ج as [dʒ]: [ˈradʒil]. Write ك as [k], with no affrication, since [tʃ] is Qarni and not Rijāl Almaʿ.

Source: Asiri (2008:72-73) via Alfaifi (2024:177-178) for [ɡ], which contradicts the earlier [q] claim attributed to Asiri (2009). ǧīm [dʒ] follows Watson & Al-Azraqi (2011) as cited in the spec; Alqarni (2025:46-48) is cited for the [tʃ] contrast.

### emphatic vowel backing

Write /a/ and /aː/ as [ɑ] and [ɑː] when immediately adjacent, within the same word, to sˤ, tˤ, ɮˤ or ɬˤ: [ˈtˤɑːlib], [ˈɮˤɑrab]. Write [a] elsewhere, including next to ɡ, q, x, ɣ and r. High vowels are not changed.

Source: Watson (2002), emphasis and vowel backing, inherited from the peninsular parent (spec rule AR_PEN_EMPH_*).

### unvocalised input

Write short vowels only where the harakat show them, as the input contract requires. Write long vowels from matres lectionis (ا و ي) as [aː uː iː] unless sukūn or the context shows a diphthong or glide. Write shadda as a doubled consonant.

Source: Spec input contract (notes).

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
