# Transcription conventions: Principense (Lung'ie) (pre)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Write one primary stress mark ˈ before the syllable carrying the lexical high tone (the accented syllable). Do not write tone diacritics. In vowel-final words of Portuguese origin the accent is usually on the penult: kaza [ˈkaza], fala [ˈfala]. Words whose Portuguese etymon was oxytone, or that are spelled with an acute or circumflex accent, are stressed on the final syllable: kumê [kuˈme]. If a word has high tone on several syllables (common in substrate words), mark only the leftmost high syllable. Do not mark monosyllables: bo [bo]. Long vowels (from vowel coalescence or a lost consonant) are written Vː and carry the stress when they are the accented syllable. The lect has no geminates and no case endings.

Source: Maurer 2009, ch. 1 (phonology: tone and accent); Hagemeijer 2009 for comparative Gulf of Guinea tone/accent. Reducing the tone system to a stress mark is this specification's convention, not Maurer's tonal analysis.

## Stressed and unstressed words

Monosyllabic grammatical words carry no stress mark in connected speech: subject and object pronouns (n, bo, e, no), tense-mood-aspect markers (ka, sa, tava treated as an unstressed auxiliary, first syllable not marked), prepositions (ni, pa, ku), the complementizer/conjunction ki, the negator and the indefinite article. Examples: bo [bo], ni [ni], ka [ka]. Disyllabic full or emphatic pronouns are lexical words and are stressed by the stress rule. Mark tava as [tava] when it is an auxiliary. Never reduce vowels in function words: they keep their full vowel quality.

Source: Maurer 2009, ch. 1 (tone of grammatical morphemes) and the pronoun and TMA chapters of the grammar.

## Pausal forms

Does not apply. Principense has no pausal forms, no case endings and no nunation. Write the same citation form of every word at a comma, at the end of a sentence and inside the sentence.

Source: Maurer 2009, ch. 1 (no pausal alternations described).

## Connected speech

Write each word in its citation form, with one exception. The syllabic nasal of the 1sg pronoun n takes the place of articulation of the following consonant within the pronoun's own word: [m̩] before labials, [n̩] before alveolars and postalveolars, [ŋ̩] before velars and labial-velars. It is written [n̩] before a vowel or a pause. No elision, vowel coalescence, liaison or resyllabification is written across word boundaries, even where fast speech has it.

Source: Maurer 2009, ch. 1 (homorganic nasals, syllabic nasal pronoun); same process described for the cluster in Hagemeijer 2009.

## Glides and diphthongs

Write non-syllabic high vocoids as consonants j and w, never as i̯ or u̯. Before a vowel: mwala [ˈmwala]. In diphthongs: written orthographic ai, ei, oi, au become [aj], [ej], [oj], [aw], e.g. pai [ˈpaj]. Orthographic nh is written [ɲ], not [nj]. A nasal diphthong nasalizes both parts: [ãj].

Source: Maurer 2009, ch. 1 (vowels, glides and diphthongs).

## Other choices

### prenasalized stops

Write word-initial mb, nd, ng as single prenasalized segments [ᵐb], [ⁿd], [ᵑɡ]. Word-medially, Vn plus a consonant is a nasal vowel followed by that consonant, with no nasal consonant written.

Source: Maurer 2009, ch. 1 (prenasalized consonants and nasal vowels).

### labial-velar stops

Write gb as [ɡ͡b] and kp as [k͡p], always with the tie bar.

Source: Maurer 2009, ch. 1; Hagemeijer 2009.

### nasal vowels

Write orthographic Vn before a consonant or at the end of a word as a nasal vowel [ã ẽ ĩ õ ũ], with no nasal consonant: inen [iˈnẽ] (stress by the stress rule). Before a vowel, n is a consonant [n].

Source: Maurer 2009, ch. 1.

### mid vowels

Keep the seven-vowel contrast. é, ó = [ɛ ɔ]; ê, ô = [e o]. For unaccented e and o, use the quality given in Maurer's vocabulary for that word. The vowel is not reduced in unstressed syllables.

Source: Maurer 2009, ch. 1 and Vocabulary.

### palato-alveolar fricatives and affricates

x = [ʃ] and tx = [tʃ], as the notes say. dj = [dʒ]. Departing from the note j=[dʒ], write orthographic j as [ʒ], following the published phoneme inventory and the unified orthography.

Source: Maurer 2009, ch. 1 (consonant inventory). This disagrees with the specification note.

### rhotic

Write the single rhotic as the tap [ɾ].

Source: Maurer 2009, ch. 1.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
