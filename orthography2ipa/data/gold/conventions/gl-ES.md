# Transcription conventions: Galician (gl-ES)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Write primary stress ˈ before the stressed syllable of every stressed word, monosyllables included: pé [ˈpɛ], mar [ˈmaɾ]. Unstressed function words (see function_words) get no mark. There is no secondary stress and there are no syllable dots. Placement follows the RAG accentuation rules. A written accent always wins: lóxico [ˈlɔʃiko], árbore [ˈaɾβoɾe], camión [kaˈmjoŋ], día [ˈdia]. Without an accent, a word ending in a vowel, ⟨-n⟩, ⟨-s⟩ or ⟨-ns⟩ is stressed on the penultimate syllable: casa [ˈkasa], cantan [ˈkantaŋ], lingua [ˈliŋɡwa]. Any other unaccented word is stressed on the last syllable. That includes words ending in a falling diphthong, with or without ⟨-s⟩: xeneral [ʃeneˈɾal], cantar [kanˈtaɾ], estou [esˈtow], partiu [paɾˈtiw], papeis [paˈpɛjs]. Rising-diphthong vowels ⟨i u⟩ + vowel count as one syllable: Galicia [ɡaˈliθja]. Verb forms with enclitics written solid keep the verb's stress: dáme [ˈdame], dígocho [ˈdiɣotʃo]. A verb before a hyphenated article clitic keeps its stress on its own: cantámo-lo [kanˈtamo] [lo]. Galician has no long vowels, no geminates and no case endings, so those parts of the topic do not apply. ⟨rr⟩ is a trill, not a geminate.

Source: RAG/ILG Normas ortográficas e morfolóxicas (2003, rev. 2012), accentuation chapter. Stress rules as implemented in Cotovia (GTM Universidade de Vigo, sil_acen.cpp). Freixeiro Mato 1998 I, chapter on stress.

## Stressed and unstressed words

Unstressed, no ˈ, close mid vowels only: definite articles o a os as and the allomorphs lo la los las, no na nos nas. Contractions of preposition + article: do da dos das, no na, ao [ao], polo pola, co coa, deste etc. Simple prepositions a de en con por para sen ata desde sobre entre contra tras cara: para [paɾa], sobre [soβɾe]. Conjunctions and relatives e ou nin que se mais pero como cando onde porque pois: o can da casa [o ˈkaŋ da ˈkasa], ti e eu [ˈti e ˈew]. Atonic pronouns me te se lle lles nos vos o a os as lo no che and their fused forms mo cho llo etc. Preverbal non: non o sei [noŋ o ˈsej]. Stressed: indefinite un unha uns unhas [ˈuŋ ˈuŋa]. Tonic pronouns eu ti el ela nós vós eles elas min si comigo contigo: nós [ˈnɔs] against clitic nos [nos]. Possessives, demonstratives, numerals and quantifiers: a miña casa [a ˈmiɲa ˈkasa]. All verb forms, auxiliaries and copula included: é [ˈɛ], hei [ˈej], ten que [ˈteŋ ke]. Adverbs, including moi [ˈmoj], tan [ˈtaŋ] and xa [ˈʃa]. Interrogative or exclamative que cando onde como quen: cando? [ˈkando]. Prepositions from participles or adjectives: segundo, durante, mediante, salvo, excepto. Non when it stands alone or is contrastive: [ˈnoŋ].

Source: Álvarez & Xove 2002, introduction on stressed and unstressed words. Freixeiro Mato 1998 I, chapter on stress (atonic words). Citation-form stress as in Regueira 2010.

## Pausal forms

Does not apply: Galician has no pausal forms, no case endings and no nunation. Final vowels and consonants are written the same at a pause as anywhere else, e.g. casa [ˈkasa] and pan [ˈpaŋ] sentence-finally. The only pause effect is on the following word. After the start of the text, a full stop, comma, semicolon, colon, dash, bracket or question/exclamation mark, a word-initial /b d ɡ/ is a stop: Bos días. [ˈbos ˈdias].

Source: Regueira 2010, introduction (post-pausal stops). Regueira 1996.

## Connected speech

Each word is written in its own place, with no joining, no elision of vowels and no syllable dots. Three things are written across boundaries.
(1) Lenition of a word-initial /b d ɡ/ (⟨b v d g gu⟩) depends on the end of the previous word. It is [β ð ɣ] after a vowel, a glide, /l/, /ɾ/ or /s/: a boca [a ˈβoka], el dixo [ˈel ˈðiʃo], dous gatos [ˈdows ˈɣatos]. It is [b d ɡ] after a nasal or a pause: con gana [koŋ ˈɡana].
(2) A word-final nasal is [ŋ] before a vowel, a glide or a pause: un home [ˈuŋ ˈɔme], pan [ˈpaŋ]. Before a consonant it takes that consonant's place:
- [m] before /p b m f/: un pé [ˈum ˈpɛ];
- [n] before /t d θ s l ɾ r n tʃ ʃ/: un dedo [ˈun ˈdeðo], en Xullo [en ˈʃuʎo];
- [ɲ] before /ʎ ɲ/;
- [ŋ] before /k ɡ/: con gana [koŋ ˈɡana].
The same assimilation applies inside words: campo [ˈkampo].
(3) A word-initial ⟨r⟩ is always [r]. A word-final ⟨r⟩ stays [ɾ] even before a vowel: mar azul [ˈmaɾ aˈθul].
Not written: voicing of coda /s/, which stays [s] (mesmo [ˈmesmo], os dedos [os ˈðeðos]); synalepha and vowel elision (de auga [de ˈawɣa]); resyllabification.

Source: Regueira 2010, introduction (a) lenition including after /l/ and (b) nasal place assimilation with velar final nasal. Freixeiro Mato 1998 I, consonant chapter. Álvarez & Xove 2002.

## Glides and diphthongs

Write glides as [j w], never i̯ u̯ or ʊ ɪ.
- Falling diphthongs ⟨ai ei oi ui au eu ou iu⟩ are vowel + [j w]: pai [ˈpaj], leite [ˈlejte], noite [ˈnojte], muito [ˈmujto], auga [ˈawɣa], eu [ˈew], cousa [ˈkowsa], viu [ˈbiw].
- Unaccented rising ⟨ia ie io ua ue uo⟩ are [j w] + vowel: historia [isˈtɔɾja], cuarto [ˈkwaɾto], lingua [ˈliŋɡwa], ambigüidade [ambiɣwiˈðaðe].
- An accent on the open vowel keeps the glide: nación [naˈθjoŋ], camión [kaˈmjoŋ].
- An accent on the high vowel marks hiatus, written as two plain vowels: día [ˈdia], rúa [ˈrua].
- Lexical hiatus words spelled ⟨-ión/-ián⟩ get [i]: Xián [ʃiˈaŋ], gorrión [goriˈoŋ], folión, mión, Brión.
- Intervocalic ⟨i⟩ is [j]: maio [ˈmajo].
- Across word boundaries, vowels are never turned into glides: e eu [e ˈew].

Source: Freixeiro Mato 1998 I, diphthong chapter (⟨iu⟩ falling). RAG Normas 2003/2012. Regueira 2010 for lexical hiatus.

## Other choices

### final nasal and ⟨nh⟩

Write a word-final nasal as a consonant [ŋ], assimilated before consonants as in connected_speech. Never write a nasal vowel or [ɐ̃]: irmán [iɾˈmaŋ], corazón [koɾaˈθoŋ]. This departs from note (9) of the specification. ⟨nh⟩ in unha, algunha, ningunha is intervocalic [ŋ]: [ˈuŋa], [alˈɣuŋa]. Unstressed /a/ is always [a].

Source: Regueira 1996, p.119-120. Regueira 2010, introduction (b).

### mid-vowel aperture

The /e ɛ o ɔ/ contrast is written only in stressed syllables, following Regueira 2010 word by word: terra [ˈtɛra], mesa [ˈmesa], porta [ˈpɔɾta], boca [ˈboka], home [ˈɔme]. All unstressed mid vowels are [e o], with no pretonic open vowels in derivatives: porteiro [poɾˈtejɾo]. Never write [ɔ] before a tautosyllabic nasal: son [ˈsoŋ], ponte [ˈponte].

Source: Regueira 2010, introduction (c) and entries. Freixeiro Mato 1998 I, vowel chapter.

### distinción, seseo, gheada, ⟨ll⟩

Standard distinción and no gheada.
- ⟨c⟩ before e/i and ⟨z⟩ are [θ]: cinco [ˈθiŋko], cazar [kaˈθaɾ].
- ⟨g⟩ is /ɡ/, as [ɡ] or [ɣ].
- ⟨ll⟩ is [ʎ]; there is no yeísmo.
- ⟨ñ⟩ is [ɲ], ⟨ch⟩ is [tʃ] and ⟨x⟩ is [ʃ]: chave [ˈtʃaβe], xente [ˈʃente].
- ⟨h⟩ is silent.
- Apical /s/ is written plain [s], with no diacritic in this broad transcription.

Source: Regueira 1996, p.119. RAG Normas 2003/2012.

### rhotics

The trill [r] is used for ⟨rr⟩, for word-initial ⟨r⟩, and for ⟨r⟩ after ⟨l n s⟩: carro [ˈkaro], honra [ˈonra]. Elsewhere ⟨r⟩ is the tap [ɾ], coda included: porta [ˈpɔɾta], cantar [kanˈtaɾ].

Source: Freixeiro Mato 1998 I, consonant chapter.

### lenition symbols

Write [β ð ɣ] with no lowering diacritic. They apply word-internally after a vowel, glide, /l ɾ s/ or other consonant, and never after a nasal: verde [ˈbeɾðe], aldea [alˈðea], ambos [ˈambos]. ⟨v⟩ is written exactly like ⟨b⟩: vaca [ˈbaka], a vaca [a ˈβaka].

Source: Regueira 2010, introduction (a). Freixeiro Mato 1998 I.

### learned ⟨x⟩ and coda clusters

Learned intervocalic ⟨x⟩ is [ks]: exame [ekˈsame]. ⟨x⟩ before a consonant is [s]: texto [ˈtesto], explicar [espliˈkaɾ]. Other coda consonants are written as spelled: acción [akˈθjoŋ].

Source: Freixeiro Mato 1998 I and Álvarez & Xove 2002 (reduced [s] before a consonant). Some careful-speech descriptions give [ks] in all positions; not followed here.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
