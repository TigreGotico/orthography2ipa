# Transcription conventions: Sri Lanka Portuguese Creole (idb)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark primary stress with ˈ before the onset of the stressed syllable in every content word of two or more syllables. Leave monosyllables unmarked. Stress is predictable and not contrastive. (1) If the word has a phonemically long vowel, stress that syllable: kuˈmeː 'eat', ˈkaːzɐ 'house', ˈliːŋgu 'tongue'. (2) If it has more than one long vowel, stress the first. (3) If it has no long vowel, stress the initial syllable: ˈiɲtʃɐ 'draw'. Syllabify a single intervocalic consonant, affricate or glide with the following vowel. Split a nasal plus consonant cluster after the nasal, so the mark goes after the nasal: aˈmiːŋgu. Allophonic gemination is not written, so it never moves stress. Case markers (dative/accusative -pa, genitive -su, locative -ntu) never take stress and do not shift the stem's stress. When one is a separate word after a hyphen, write it unmarked: ˈkaːzɐ pa.

Source: Quantity-sensitive stress with initial default as restated by Cardoso 2013 (APiCS Online, survey ch. 41, phonology section), following Smith 1977 (Sri Lanka Creole Portuguese Phonology, Cornell diss.). The tie-break of the first long vowel is a working convention of this set, not taken from a source.

## Stressed and unstressed words

Grammatical words carry no stress mark in connected speech and are written in full citation form, keeping their vowel length and quality. They are never reduced. This covers the preverbal tense-mood-aspect particles ta (non-past), ja (past) and lo (irrealis): [ta], [dʒa], [lo]. It also covers case markers written as separate words ([pa], [su], [ntu]), the negator, conjunctions, unstressed personal pronouns, demonstratives used as determiners, and the numeral or indefinite 'one' used as an article. Polysyllabic function words also get no ˈ, but their long vowels stay long. Content words (nouns, lexical verbs, adjectives, adverbs) always get the stress mark, including emphatic or contrastively focused pronouns. Final-/a/ reduction to ɐ (see 'other') applies only to polysyllables, so monosyllabic particles keep [a].

Source: Smith 1977 and Cardoso 2013 (APiCS ch. 41), which describe the TMA particles and case markers as unstressed grammatical elements. Treating all function words as unmarked is a convention of this set.

## Pausal forms

Does not apply: SLPC has no pausal forms, case-ending loss or nunation. Every word is written in the same form at the sentence end, at a comma and sentence-internally. No final-vowel deletion, devoicing or lengthening is written at a pause.

Source: Cardoso 2013 (APiCS ch. 41) and Smith 1977, which describe no pause-conditioned alternations.

## Connected speech

No cross-word process is written. Each word appears in its isolation form in its own slot. Nasal place assimilation is written only inside a word, where nasal plus consonant clusters are always homorganic: ˈliːŋgu, ˈoːndɐ, ˈiɲtʃɐ. A word-final nasal before a consonant-initial word keeps its citation form. Retroflexion of /n l/ is conditioned only by a preceding vowel in the same word. Vowel hiatus across words is kept, with no elision and no inserted linking glide. There is no resyllabification across words and no liaison.

Source: Word-internal homorganic nasal plus consonant clusters follow Hume & Tserdanelis 2002 (Phonology 19(3); ROA-545 preprint pp. 4-5). Leaving cross-word processes unwritten is a convention of this set for row-by-row consistency.

## Glides and diphthongs

Write glides as consonants j and w. Never use i̯ u̯. Falling diphthongs are vowel plus j or w in the same syllable, e.g. [paj]. A glide before a vowel is an onset: [ˈjaː…]. Keep /ʋ/, the reflex of etymological v and written v in the documentation, distinct from /w/, which is written w. Do not write ʋ as w or v. The affricates are tʃ and dʒ, without a tie bar.

Source: Inventory with /j w/ as consonants and /ʋ/ for etymological v, after Cardoso 2013 (APiCS ch. 41). The orthographic convention follows Cardoso's SLP documentation.

## Other choices

### Vowel inventory and contested vowels

Write only i e ɛ a u o ɔ and their long forms iː eː ɛː aː uː oː ɔː, with length marked by ː (doubled letters in the orthography): maal → [mɑːɭ], nɔɔna → [ˈnɔːɳɐ]. Write ɛ ɔ only where the source orthography writes them, and e o elsewhere. Do not use Smith's phonemic /ə/ or /æ æː/. Write such words with a/aː or e per Cardoso's spelling.

Source: Cardoso 2013 (APiCS ch. 41), as against Smith 2013 (Survey of Pidgin and Creole Languages vol. 2, pp. 111-121), which adds /ə æ æː/. This set follows Cardoso.

### Reduced final /a/

In words of two or more syllables, write a short unstressed word-final /a/ as ɐ: [ˈnɔːɳɐ], [ˈkaːzɐ], [ˈoːndɐ]. Write a everywhere else.

Source: The spec notes give [nɔːɳɐ]. Hume & Tserdanelis 2002 (pp. 4-5) write the same reduced vowel as ə (o:ndə). This set keeps the spec's symbol ɐ and treats it as an allophone of /a/, not as Smith's phoneme /ə/.

### Retroflex allophones

Within a word, write /n l/ as ɳ ɭ when the preceding vowel is a non-high back vowel (a, aː, o, oː, ɔ, ɔː): [mɑːɭ], [ˈnɔːɳɐ]. Write /a aː/ immediately before these retroflexes as ɑ ɑː. Word-initial /n l/ and /n l/ after front or high vowels stay n l. No retroflex stop series is written.

Source: Cardoso 2013 (APiCS ch. 41), retroflex allophony (maal, nɔɔna). The backing of /a/ to ɑ follows the spec's example.

### Consonant gemination

Not written. Cardoso describes gemination of voiceless consonants after short stressed vowels, but this set writes single consonants: [ˈsaːku], not [saːkku]. This departs from the pronunciation published by Cardoso, by convention.

Source: Cardoso 2013 (APiCS ch. 41) documents gemination. The spec notes direct that consonant length is not written.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
