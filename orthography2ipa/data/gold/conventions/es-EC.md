# Transcription conventions: Ecuadorian Spanish (es-EC)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark primary stress with ˈ before the stressed syllable of every stressed word of two or more syllables. Stressed monosyllables carry no mark, and neither do unstressed words (see function_words). Place the mark at the word-internal syllable boundary given by Spanish syllabification: a single consonant goes with the following vowel; of two consonants, the second goes with the vowel, except for obstruent plus l or ɾ, which stay together. Ignore cross-word resyllabification. Placement follows the orthography. A written accent marks the stressed vowel: [ˈrapiðo], [kaˈfe], [ˈarβol]. With no written accent, a word ending in a vowel, n or s takes penultimate stress and any other word takes final stress: [ˈkasa], [ˈtjenen], [ˈlunes], [paˈred], [kanˈtaɾ]. Words with enclitics written solid keep the host's stress: [ˈdamelo], [diˈsjendole]. Adverbs in -mente take ˌ on the adjective's stress and ˈ on -men-: [ˌrapiðaˈmente], [ˌfasilˈmente]. Where an accent has been dropped on capitals, restore it from the standard spelling. Spanish has no phonemic long vowels, no geminates and no case endings, so these do not apply. Double vowels across a morpheme boundary are written as two vowels: [leˈeɾ], [ˌkoopeˈɾaɾ].

Source: Hualde (2005), The Sounds of Spanish, ch. 10 on stress, including the two-stress analysis of -mente adverbs. Syllabification follows Hualde (2005), ch. 4.

## Stressed and unstressed words

Unstressed, written without ˈ even when polysyllabic: definite articles (el, la, lo, los, las); object and reflexive clitics (me, te, se, nos, os, le, les, lo, la, los, las); prenominal possessives mi, tu, su and their plurals; all prepositions except según ([paɾa], [poɾ], [dezðe], [sin], [soβɾe], [ent̪ɾe] written [entɾe], [asta]); conjunctions (y, e, ni, o, u, pero, porque, aunque, si, que, mas); relatives que, quien, cual, donde, cuando, como, as in [lo ke ˈkjeɾo] and [kwando ˈʝeɣa]; and the titles don, doña, san, santo, as in [santo doˈmiŋɡo]. Stressed, with ˈ when polysyllabic: indefinite articles [ˈuna], [ˈunos]; subject pronouns [noˈsotɾos], [uzˈteð]; prepositional pronouns; demonstratives [ˈesta], [aˈkel]; stressed possessives [ˈmio], [ˈnwestɾo]; interrogatives and exclamatives [ˈkomo], [ˈdonde], [ˈkwando]; según [seˈɣun]; numerals; adverbs. All verb forms are stressed, including the auxiliaries haber, ser and estar: [ˈemos ˈiðo], [esˈtaβa kanˈsaðo]. Tú, él, mí and qué are stressed monosyllables, so they carry no mark either.

Source: Hualde (2005), ch. 10, on stressed versus unstressed words. This is the standard pan-Hispanic classification; nothing in the Ecuadorian descriptions (Lipski 1994) departs from it.

## Pausal forms

Spanish has no pausal morphology. There are no case endings and no nunation (tanwīn), and final vowels are never dropped or shortened at a pause. Every word is written in the same form at a sentence end, at a comma and sentence-internally. A pause, meaning any punctuation (sentence end, comma, colon, semicolon, dash, parenthesis or quotation boundary), only blocks the cross-word processes in connected_speech. After a pause, /b d ɡ/ are stops: [ˈbamos], [doˈminɡo]. Before a pause, word-final /s/ stays voiceless [s] and word-final /n/ stays alveolar [n], not the coastal velar [ŋ]: [ˈtjenen]. Final /ɾ/ before a pause is written [ɾ] even though highland speakers often assibilate it.

Source: Hualde (2005), ch. 6 (stops and approximants) and ch. 9 (nasals). Lipski (1994), Ecuador chapter, on alveolar final /n/ and conservative /s/ in the highlands.

## Connected speech

Each word is written in its own place, and processes across a boundary only change the segment at the edge of a word. These apply only between words not separated by punctuation. (1) Nasal place assimilation: final /n/ takes the place of the next consonant. It is [m] before p b m ([um ˈbeso], [em ˈparis]), [ɱ] before f ([eɱ ˈfin]), and [ŋ] before k ɡ x ([eŋ ˈkasa], [uŋ ˈxaɾo]). It is written [n] before vowels, dentals, alveolars and [ʝ]. (2) Spirantization: /b d ɡ/ at a word start are written [β ð ɣ] after a vowel or a non-nasal consonant ([la ˈβoka], [de ˈðonde], [los ɣaˈtos] written [loz ˈɣatos]). They are stops [b d ɡ] after a nasal, and also /d/ after l ([el ˈdia]). (3) Highland /s/ voicing: word-final /s/ becomes [z] before a vowel or a voiced consonant in the next word ([loz ˈotɾos], [laz ˈmadɾes], [loz ˈβaskos]). It stays [s] before voiceless consonants. Inside words, /s/ is [z] before voiced consonants only ([ˈmizmo]), and intervocalic /s/ inside a word stays [s] ([ˈkasa]). (4) Vowel sandhi (synalepha) is not written. Both vowels are kept, with no glide symbol and no elision: [la aˈβwela], [de el], [mi ixo] written [mi ˈixo]. (5) Resyllabification of a final consonant onto the next word is not written and never moves a stress mark: [el ˈaɣwa], [loz ˈotɾos].

Source: Hualde (2005), ch. 6, ch. 9 and ch. 12 (sandhi). Lipski (1994), Ecuador chapter, on the voicing of word-final prevocalic /s/ in highland Ecuador.

## Glides and diphthongs

In rising diphthongs and triphthongs the prevocalic glide is written [j] or [w]: [ˈtjene], [ˈbweno], [ˈaɣwa], [sjuˈðað], [ˈkwiða], [ˌbwei̯]. In falling diphthongs the postvocalic glide is written [i̯] or [u̯]: [ˈbai̯le], [ˈau̯to], [ˈpei̯ne], [ˈoi̯], [mui̯], [ɹ̝ei̯]. Hiatus with written í or ú keeps full vowels: [ˈdia], [paˈis], [ɹ̝eˈuniɾ]. The consonant written y, and initial hie-/hia-, is the fricative [ʝ], not a glide: [ˈʝo], [ma ˈʝo] written [maˈʝo], [ˈʝeɾβa]. The conjunction y is always written [i], and no glide is written across word boundaries, consistent with connected_speech (4).

Source: Hualde (2005), ch. 4 and ch. 7 (glides versus /ʝ/), whose j w / i̯ u̯ notation this follows.

## Other choices

### Highland ll versus y

This transcription keeps the traditional highland distinction. ll is the grooved fricative [ʒ]: [ˈkaʒe], [ʒaˈmaɾ], [ˈpoʒo]. y and hi+vowel are [ʝ]: [ˈmaʝo], [ˈʝeso]. Where speakers or other descriptions have yeísmo, it is not followed.

Source: Lipski (1994), Ecuador chapter, on highland [ʒ] for /ʎ/. Fontanella de Weinberg (1992) on Andean lleísmo.

### Rhotics

The trill (written rr, word-initial r, and r after n, l or s) is the assibilated [ɹ̝], per the specification: [ˈpeɹ̝o], [ɹ̝oˈsa] written [ˈɹ̝osa], [onˈɹ̝aðo]. Every other r is the tap [ɾ], including in tr, dr and coda position: [ˈtɾes], [ˈmaɾ], [ˈpweɾta]. Assibilation of coda and tr /ɾ/ is reported for the Andes but is variable, so it is not written.

Source: Lipski (1994), Ecuador chapter, on assibilated rhotics in the highlands. Hualde (2005), ch. 11.

### Seseo and coda /s/

There is no /θ/: c before e or i and z are written [s] ([ˈsjelo], [ˈkasa] for caza). Coda /s/ is never aspirated or deleted in this highland norm: [ˈestos], [ˈmaz ˈbjen]. Coastal aspiration is not used.

Source: Lipski (2011), zone list (Andean versus Pacific coast). Lipski (1994), Ecuador chapter. Penny (2002) on seseo.

### Intervocalic /d/ and final /d/

Intervocalic /d/ is always written [ð], including in -ado: [kanˈsaðo], [ˈtoðo]. Word-final /d/ is written [ð]: [paˈɾeð], [uzˈteð]. Highland Ecuador retains /d/ more than the coast, so it is never deleted.

Source: Hualde (2005), ch. 6. Lipski (1994), Ecuador chapter.

### Unstressed vowel reduction

The five vowels /a e i o u/ are always written in full. The highland reduction or devoicing of unstressed vowels, especially next to /s/ (attributed to Quechua contact), is not written: [ˈpesos], not [ˈpess]. Mid and high vowels are not merged.

Source: Lipski (1994), Ecuador chapter, on Andean vowel reduction. Hualde (2005), ch. 8, on the five-vowel system.

### Other consonants

j, and g before e or i, are [x]: [ˈxente]. f is [f], not highland [ɸ]. h is silent. x between vowels is [ks] ([ekˈsamen]), but [x] in México ([ˈmexiko]). Coda b, d, g, p, k follow spirantization inside words: [aβˈsolto], [ˈapto], [ˈaktos].

Source: Hualde (2005), ch. 6 and ch. 7. Lipski (1994), Ecuador chapter.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
