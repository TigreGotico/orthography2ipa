# Transcription conventions: Extremaduran (ext)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Spanish lexical stress, placed by the standard orthographic rule on the spelled word. A written acute marks the stressed vowel. Otherwise, a word ending in a vowel, ⟨n⟩ or ⟨s⟩ is stressed on the penult, and any other word on the final syllable. The rule reads the spelling even where the final consonant is aspirated or lost: verdad [beɾˈða], cantas [ˈkantah], comer [koˈmeɾ]. Write ˈ before the stressed syllable of every stressed word, including stressed monosyllables: sol [ˈsol], yo [ˈʝo]. Unstressed function words get no mark. Put no secondary stress except on -mente adverbs, which take ˈ on both parts: rápidamente [ˈrapiðaˈmente]. Do not use acute accents on IPA vowels, although the spec note writes [berˈdá]. Enclitic pronouns written solid with the verb leave the verb's stress where it is: dímelo [ˈdimelo], dámelos [ˈdameloh]. Vowel length is not contrastive, so never write ː. That includes vowel lengthening or opening after a lost /s/, and two identical vowels meeting across a word boundary. Geminates are not phonemic: do not write the coda assimilations of some speakers (mismo [ˈmihmo], not [ˈmimmo]). Case endings do not apply; Extremaduran has no case morphology.

Source: Alarcos Llorach (1994), Gramática de la Lengua Española, chapter on accent (prosodia) and the orthographic accent rules; Navarro Tomás (1918), Manual de pronunciación española, §§ on accent.

## Stressed and unstressed words

Follow the standard Spanish division into tonic and atonic words. UNSTRESSED, so no ˈ: definite articles el la lo los las [el la lo loh lah]. All simple prepositions except según: a de en con por para sin sobre desde hasta, e.g. [a de en kon poɾ paɾa sin soβɾe dehðe ahta]. Conjunctions y e o u ni que pero si porque aunque mas: y [i], que [ke], pero [peɾo]. Object and reflexive clitics me te se lo la le nos os los las les. Prenominal possessives mi tu su mis tus sus nuestro: su casa [su ˈkasa]. Non-interrogative relatives and conjunctions que quien cual donde cuando como. Titles don doña. STRESSED, so ˈ: indefinite articles un una unos unas, e.g. un hombre [ˈun ˈombɾe]. Subject and prepositional pronouns yo tú él ella nosotros usted mí ti sí: para mí [paɾa ˈmi]. Postposed possessives mío tuyo suyo. Demonstratives este ese aquel esto. Interrogatives and exclamatives qué quién cuál dónde cuándo cómo cuánto. Numerals, quantifiers and según. All verb forms, including the auxiliaries haber and ser and estar: ha venido [ˈa βeˈniðo], es [ˈeh]. All adverbs, including no [ˈno], muy [ˈmuj], ya [ˈʝa]. Unstressed words keep their full vowels; do not reduce them.

Source: Navarro Tomás (1918), Manual de pronunciación española, § on palabras acentuadas e inacentuadas; Alarcos Llorach (1994), Gramática de la Lengua Española, prosody chapter (tonic vs atonic words).

## Pausal forms

Not applicable: Extremaduran has no pausal forms, case endings or nunation. A word is written the same before a pause, at a comma or in mid-sentence; final /s/ is [h] and final /d/ is lost in all these positions. The one pause-sensitive point is the initial voiced stop. After the start of the sentence, a comma or any other punctuation mark, a word-initial /b d g/ is a stop: Dios, ... [ˈdjoh]. In mid-phrase the same stop follows the lenition rule under connected_speech.

Source: Navarro Tomás (1918), Manual de pronunciación española, §§ on b, d, g after pause; Zamora Vicente (1960), Dialectología española, chapter on extremeño.

## Connected speech

Each word keeps its own segments and its own place. Only these processes are written across a boundary. (1) Spirantization of /b d g/. Write [β ð ɣ] at the start of a word whose preceding word ends in a vowel, [h], [ɾ], [r] or [j w], and also after [l] for /b g/. Write [b d g] after a pause and after a nasal, and [d] after [l]. Examples: la boca [la ˈβoka], los dedos [loh ˈðeðoh], un beso [ˈum ˈbeso], el dedo [el ˈdeðo]. The same rule applies inside words: abogado [aβoˈɣaðo], hombre [ˈombɾe]. (2) Nasal place assimilation. Write a word-final /n/ as [m] before [p b m], [ɱ] before [f], [ŋ] before [k g x h], and otherwise [n]. Examples: en Badajoz [em baðaˈhoθ], con fuerza [koɱ ˈfweɾθa], en casa [eŋ ˈkasa]. Do not write the pausal velarization of /n/. (3) Coda /s/ is [h] before vowels too, and it is not resyllabified: los otros [loh ˈotɾoh], not [lo ˈhotɾoh]. Do not write voicing to [ɦ] or total loss. (4) Word-initial ⟨r⟩ is always the trill [r], whatever precedes it: la rosa [la ˈrosa]. (5) Vowels meeting across a word boundary (synalepha) are written in full on each word. Do not elide them, turn them into glides or lengthen them: de esto [de ˈehto], la hija [la ˈhiha], lo único [lo ˈuniko]. Do not write nasalized vowels, although the spec note writes [ˈõmbɾeh].

Source: Navarro Tomás (1918), Manual de pronunciación española (b d g, nasal assimilation, sinalefa); Zamora Vicente (1960), Dialectología española, chapter on extremeño (aspiration of implosive -s); Alarcos Llorach (1994).

## Glides and diphthongs

Write non-syllabic i and u inside a word as [j] and [w], never as i̯ u̯. Rising diphthongs: tiene [ˈtjene], bueno [ˈbweno], ciudad [θjuˈða]. Falling diphthongs: aire [ˈajɾe], causa [ˈkawsa], muy [ˈmuj], hay [ˈaj], rey [ˈrej], hoy [ˈoj]. A vowel with a written accent is a full vowel in hiatus: día [ˈdi.a], written [ˈdia], and país [paˈih]. Consonantal ⟨y⟩ and ⟨ll⟩, and word-initial ⟨hi⟩ before a vowel, are the obstruent [ʝ], not [j]: yo [ˈʝo], calle [ˈkaʝe], hielo [ˈʝelo]. Initial ⟨hu⟩ before a vowel is [w]: hueso [ˈweso]. The conjunction y alone is [i]. Glides are never written across word boundaries.

Source: Navarro Tomás (1918), Manual de pronunciación española, §§ on diptongos and semiconsonantes; Alarcos Llorach (1994), Gramática de la Lengua Española, phonology chapter.

## Other choices

### Distinción vs seseo (departs from spec note 1)

Write distinción. ⟨z⟩ and ⟨c⟩ before e and i are [θ]; ⟨s⟩ is [s]. Examples: hacer [haˈθeɾ], cinco [ˈθiŋko], casa [ˈkasa], caza [ˈkaθa]. The note claims general seseo. The published dialect descriptions place seseo and ceceo only in small southern Badajoz pockets, and the note's own example hacer [ˈhaθeɾ] has [θ]. Word-final or pre-consonantal ⟨z⟩ is written [θ]: luz [ˈluθ], Badajoz [baðaˈhoθ].

Source: Zamora Vicente (1960), Dialectología española, chapter on extremeño (s/z); González Salgado (2000), Cartografía lingüística de Extremadura.

### Coda /s/

Every syllable-final /s/ is written [h], whether word-internal or word-final and whatever follows. Examples: estos hombres [ˈehtoh ˈombɾeh], mismo [ˈmihmo], los años [loh ˈaɲoh]. ⟨x⟩ before a consonant is also [h]: extraño [ehˈtɾaɲo]. Between vowels ⟨x⟩ is [ks]: taxi [ˈtaksi]. Never write deletion, [ɦ] or gemination.

Source: Zamora Vicente (1960), Dialectología española, chapter on extremeño (aspiración de -s implosiva).

### Aspiration of h < Latin F-

Write [h] for ⟨h⟩ that continues Latin F-. Examples: hacer [haˈθeɾ], hijo [ˈhiho], hambre [ˈhambɾe], harina [haˈɾina], hierro [ˈhjero], humo [ˈhumo], hoja [ˈhoha], horno [ˈhoɾno], hablar [haˈβlaɾ], higo [ˈhiɣo], hondo [ˈhondo], hacha [ˈhatʃa], hoyo [ˈhoʝo], hígado [ˈhiɣaðo], hurtar [huɾˈtaɾ]. Etymological H- and other ⟨h⟩ are silent: hombre [ˈombɾe], haber [aˈβeɾ], hora [ˈoɾa], hermano [eɾˈmano], huevo [ˈweβo], hielo [ˈʝelo]. Modern ⟨f⟩ stays [f]: fuerza [ˈfweɾθa]. This follows Zamora Vicente, who treats the aspiration as general in Extremadura, against the note's 'rural/archaic' label.

Source: Zamora Vicente (1960), Dialectología española, chapter on extremeño (h aspirada); Penny (2002), A History of the Spanish Language, § on F- > h.

### Velar fricative /x/

Write ⟨j⟩, and ⟨g⟩ before e and i, as [h], never [x]. Examples: jota [ˈhota], gente [ˈhente], ojo [ˈoho]. It merges in symbol with aspirated F- and coda /s/.

Source: Zamora Vicente (1960), Dialectología española, chapter on extremeño; spec note 7.

### Yeísmo

⟨ll⟩ and consonantal ⟨y⟩ merge as [ʝ] in every position, initial or medial, after any segment: llave [ˈʝaβe], mayo [ˈmaʝo], con llave [koɲ ˈʝaβe] is not written; write [kon ˈʝaβe]. Never write [ʎ] or [ɟʝ].

Source: Zamora Vicente (1960), Dialectología española (yeísmo in extremeño); spec note 4.

### Final /d/ and intervocalic lenition

Word-final /d/ is deleted: verdad [beɾˈða], usted [uhˈte], Madrid [maˈðɾi]. Intervocalic /d/ inside a word is kept as [ð], including in -ado and -ada: cansado [kanˈsaðo], nada [ˈnaða]. Do not write the rapid-speech forms [kanˈsao] or [ˈna].

Source: Zamora Vicente (1960), Dialectología española, chapter on extremeño; Navarro Tomás (1918), Manual de pronunciación española, § on d.

### Coda /r/ and /l/

Write coda /r/ as [ɾ] and /l/ as [l], as spelled. Do not write the r/l neutralization or the loss of infinitive -r found in colloquial extremeño: comer [koˈmeɾ], not [koˈme]; alto [ˈalto]; carne [ˈkaɾne]. Write ⟨rr⟩, initial ⟨r⟩, and ⟨r⟩ after n, l or s as the trill [r]: perro [ˈpero], honra [ˈonra]. Write ⟨r⟩ elsewhere as [ɾ]: pero [ˈpeɾo].

Source: Navarro Tomás (1918), Manual de pronunciación española (r, rr); Zamora Vicente (1960), Dialectología española, notes the colloquial neutralization, which is not adopted here.

### Symbol set

Vowels: a e i o u. Consonants: p b t d k g β ð ɣ f θ s h ʝ tʃ m ɱ n ɲ ŋ l r ɾ, plus the glides j w. ⟨ch⟩ is [tʃ]: noche [ˈnotʃe]. ⟨ñ⟩ is [ɲ]. ⟨v⟩ is the same as ⟨b⟩: vaca [ˈbaka], la vaca [la ˈβaka]. ⟨qu⟩ and hard ⟨c⟩ are [k]. ⟨gu⟩ before e and i is [g] or [ɣ].

Source: Alarcos Llorach (1994), Gramática de la Lengua Española, phonology chapter; Navarro Tomás (1918).

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
