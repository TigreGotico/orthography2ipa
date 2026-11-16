# Transcription conventions: Kabuverdianu (Cape Verdean Creole) (kea)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Variety: Badiu (Santiago). Write primary stress with ˈ before the stressed syllable of every polysyllabic word, content or function word; never mark a monosyllable. Placement follows the ALUPEC default rule. (1) A word ending in a vowel, or in a vowel plus plural -s, is stressed on the penult: kaza /ˈkaza/, mininu /miˈninu/, mininus /miˈninus/. (2) A word ending in any other consonant is stressed on the final syllable. This includes coda n marking nasality, l, r and z: kurason /kuɾaˈsõ/, mudjer /muˈdʒɛɾ/. (3) A final diphthong also takes final stress: papai /paˈpaj/. (4) A written acute or circumflex overrides the rule and marks both stress and vowel quality: kumê /kuˈme/, sábadu /ˈsabadu/. TMA suffix -ba and plural -s never move stress: kumeba /kuˈmeba/. There are no phonemic long vowels, no geminates and no case endings, so nothing is written for them.

Source: ALUPEC stress rules (Decreto-Lei 67/98; Decreto-Lei 8/2009) as applied to Santiago speech in Baptista (2002) ch. 2 and Lang (2002, Dicionário do crioulo da ilha de Santiago).

## Stressed and unstressed words

Monosyllabic function words are unstressed and written without a stress mark. They keep their full vowel quality, because unstressed vowels are not reduced in Badiu. This covers subject clitics N, bu, e, nu, nhos, es; object clitics m, bu, l, nu, nhos, s; TMA markers ta /ta/, sa /sa/, dja /dʒa/; negator ka /ka/; prepositions di /di/, na /na/, pa /pa/, ku /ku/, a /a/, te /te/; conjunctions i /i/, ma /ma/, ki /ki/, o /o/; indefinite un /ũ/; copula e /ɛ/. Polysyllabic function words keep their lexical stress mark by the stress rule: sima /ˈsima/, riba /ˈɾiba/, purki /puɾˈki/. Emphatic and strong pronouns are full words and are marked if polysyllabic: ami /ˈami/.

Source: Baptista (2002) ch. 2–3 on the clitic and strong pronoun series and TMA markers; Lang (2013) on TMA ta/sa/dja/-ba.

## Pausal forms

Does not apply: Kabuverdianu has no pausal forms, case endings or nunation, and words are written in the same form at a comma, at sentence end and sentence-internally.

Source: Baptista (2002) ch. 2; Quint (2000), Grammaire de la langue cap-verdienne.

## Connected speech

Write each word in its citation form, with no linking, liaison or resyllabification marks and no elision of vowels across words. There is one exception. The 1sg subject clitic N is a syllabic nasal homorganic with the next word's initial consonant: [m̩] before p b m f v, [ŋ̍] before k g, and [n̩] elsewhere. Before a vowel it is written [n]. Examples: N bai /m̩ ˈbaj/ (bai is monosyllabic, so unmarked), N kumê /ŋ̍ kuˈme/, N ta /n̩ ta/, N átxa /n ˈatʃa/. Text already contracted with an apostrophe is split by the engine. Transcribe each piece as it stands: k' → /k/. Do not restore the missing vowel.

Source: Baptista (2002) ch. 2 on the homorganic 1sg nasal; Quint (2000).

## Glides and diphthongs

Write non-syllabic i and u as consonant symbols /j w/, never i̯ u̯. Examples: pai /paj/, sabedoria-type rising sequences as written, mau /maw/, kuatu /ˈkwatu/. In the nasal diphthongs ãi and ãu, write the tilde on the first element only: mãi /mãj/, nãu /nãw/. Vowel sequences in hiatus stay two syllabic vowels: dia /ˈdia/.

Source: Baptista (2002) ch. 2 (diphthong inventory); ALUPEC (1998/2009) for ãi/ãu.

## Other choices

### variety

Transcribe Santiago Badiu (Sotavento) norms throughout. Write full unstressed vowels, with none of the Barlavento/Sampadjudo deletion of unstressed vowels: mininu /miˈninu/, not [ˈmnin].

Source: Baptista (2002), The Syntax of Cape Verdean Creole: The Sotavento Varieties, ch. 2; Veiga (2002) contrasts Barlavento.

### oral vowel inventory

Write seven oral vowels /i e ɛ a ɔ o u/. This departs from the note's 'five-vowel system': published descriptions contrast e/ɛ and o/ɔ in stressed syllables. Written é ó → /ɛ ɔ/; ê ô → /e o/. Otherwise use the Santiago dictionary quality for stressed e/o, and write /e o/ in unstressed syllables. Never write /ɨ/ or reduced vowels; unstressed a stays /a/.

Source: Baptista (2002) ch. 2; Lang (2002) dictionary; Quint (2000).

### nasal vowels

Write vowel + coda n as a nasal vowel /ĩ ẽ ã õ ũ/, with no nasal consonant, both word-finally and before a consonant: bon /bõ/, kantu /ˈkãtu/. Do not write the phonetic homorganic nasal before stops. nh = /ɲ/, as in nha /ɲa/.

Source: Baptista (2002) ch. 2; ALUPEC conventions as in the spec notes.

### rhotics

Single intervocalic and coda r → /ɾ/; rr and word-initial r → alveolar trill /r/: rapaz /raˈpas/, karru /ˈkaru/. This departs from the note's /ʀ/: Santiago speech has an alveolar trill, and uvular realizations belong to other islands and urban speech.

Source: Baptista (2002) ch. 2; Quint (2000).

### sibilants, affricates and h

s → /s/ in all positions, including coda, with no Portuguese-style coda [ʃ]: mas /mas/. z → /z/; x → /ʃ/; j → /ʒ/; tx → /tʃ/ and dj → /dʒ/, written without a tie bar. h is silent.

Source: Baptista (2002) ch. 2; ALUPEC (1998/2009).

### final obstruent weakening

Write every written final consonant. Do not transcribe optional Badiu deletion of final obstruents or liquids, since a broad citation-form transcription keeps them: mudjer /muˈdʒɛɾ/.

Source: Baptista (2002) ch. 2 (deletion described as variable).

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
