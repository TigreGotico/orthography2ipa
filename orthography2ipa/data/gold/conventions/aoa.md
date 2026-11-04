# Transcription conventions: Angolar (aoa)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Tone is lexical (H/L) but is not written. Do not put tone marks or tone letters in any row, because the orthography gives no tone and transcribers cannot recover it reliably. Mark primary stress with ˈ before the syllable onset, once in every content word of two or more syllables. Default: stress the penultimate syllable, e.g. ⟨ngandu⟩ [ˈŋɡandu], ⟨mina⟩ [ˈmina]. Stress the final syllable only where the orthography marks it with an acute accent, or where the word is a known oxytone from a Portuguese oxytone. Never mark monosyllables, e.g. ⟨kwa⟩ [kwa], ⟨tha⟩ [θa]. Long vowels written double (⟨aa⟩) are one long nucleus [aː] and count as one syllable when you count back from the end. Angolar has no geminates and no case endings, so those clauses do not apply. Vowels never reduce in unstressed syllables.

Source: Maurer 1995 (phonology chapter, tone and prominence: lexical H/L tone, with the prominent syllable of Portuguese-derived words usually matching the Portuguese stress); Maurer 2013 APiCS ch. 36. Stress is marked only as a consistency convention, because tone is unrecoverable from the spelling.

## Stressed and unstressed words

Function words never get a stress mark, whatever their length. This covers subject and object pronouns, preverbal tense/mood/aspect markers (e.g. ⟨ka⟩ [ka]), prepositions, conjunctions, the copula ⟨tha⟩ [θa], negators and determiners. They keep their full vowel quality: write [a], [ɛ], [ɔ], never schwa. Mark stress only on emphatic or independent pronouns of two or more syllables used on their own or in focus, and only by the penultimate rule.

Source: Maurer 1995 (pronoun and TMA chapters: short pronouns and preverbal markers are clitic-like and atonal or tonally dependent); Maurer 2013 APiCS ch. 36.

## Pausal forms

Does not apply: Angolar has no pausal forms, no case endings and no nunation. Write the same citation form at the end of the sentence, at a comma and medially.

Source: Maurer 1995; Maurer 2013 APiCS ch. 36 (no pause-conditioned morphology described).

## Connected speech

Write every word in its citation form in its own slot. Do not write cross-word assimilation, vowel elision or coalescence, liaison or resyllabification. Do not write optional nasalization spreading from a neighbouring nasal. If the orthography itself writes a reduced or contracted form, transcribe exactly what is written, as its own word.

Source: Maurer 1995 (sandhi and nasal spreading described as optional or phonetic); this follows the broad-transcription notes of the specification.

## Glides and diphthongs

Write glides as the consonants j and w, which are phonemes /j w/ in the inventory. Never write i̯ or u̯. Write ⟨i u⟩ before another vowel in the same word as [j w], e.g. ⟨kua⟩ [kwa]. Write falling diphthongs with j or w: ⟨ai⟩ [aj], ⟨au⟩ [aw]. Write ⟨y⟩ as [j] and ⟨w⟩ as [w].

Source: Maurer 2013 APiCS ch. 36 (inventory /p b t d k g f v θ ð l m n ɲ j w/).

## Other choices

### interdental fricatives

Write ⟨th⟩ as [θ] and ⟨dh⟩ as [ð] everywhere, e.g. ⟨tha⟩ [θa]. Never use the plain stops [t d] of the contact variant. Write ⟨s z⟩ as [s z], as spelled; these mainly occur before /i/.

Source: Maurer 1995 and Maurer 2013 APiCS ch. 36 (conservative norm), rather than Lorenzino 1998 (younger-speaker [t d] variant).

### prenasalized stops

Write ⟨mb nd ng⟩ as the clusters [mb nd ŋɡ] without a tie bar, in every position including word-initially: ⟨ngandu⟩ [ˈŋɡandu]. Write word-final ⟨ng⟩ as [ŋ], and ⟨nh⟩ as [ɲ].

Source: Maurer 2013 APiCS ch. 36 (prenasalized stops in all positions).

### vowel quality and nasality

There are seven oral vowels. Write ⟨ê⟩ as [e], ⟨ô⟩ as [o], plain ⟨e⟩ as [ɛ], plain ⟨o⟩ as [ɔ], and ⟨â î û⟩ as [a i u]. A circumflex never means nasality. Write a nasal vowel such as [ã] only where the orthography explicitly writes nasality, for example with a tilde.

Source: Maurer 1995 (seven-vowel system, small marginal nasal-vowel set); the specification notes.

### rhotic

The native inventory has no /r/; Portuguese r corresponds to [l]. Write ⟨l⟩ as [l]. Write an ⟨r⟩ that appears in an unassimilated recent Portuguese loan as [ɾ].

Source: Maurer 2013 APiCS ch. 36 (no rhotic in the inventory); Maurer 1995.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
