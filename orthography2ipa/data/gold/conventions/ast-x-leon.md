# Transcription conventions: Leonese (ast-x-leon)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Leonese has free lexical stress on one syllable per word, located as in its orthography. (1) If a vowel carries an acute accent, stress falls on that syllable: ⟨fácil⟩ /ˈfaθil/, ⟨paxarín⟩ /paʃaˈɾin/, ⟨día⟩ /ˈdia/. (2) Otherwise, words ending in a vowel, ⟨-n⟩ or ⟨-s⟩ take penultimate stress: ⟨llobu⟩ /ˈʎobu/, ⟨llingua⟩ /ˈʎinɡwa/, ⟨cantaben⟩ /kanˈtaben/. (3) Other consonant-final words take final stress: ⟨chover⟩ /tʃoˈbeɾ/, ⟨meyor⟩ /meˈʝoɾ/, ⟨llugar⟩ /ʎuˈɡaɾ/. Rising and falling diphthongs (ie, ue, ua, ou, ei, ai) count as one syllable, and silent ⟨u⟩ in ⟨qu, gu⟩ counts as nothing. Place ˈ immediately before the onset of the stressed syllable. A single intervocalic consonant, and an obstruent+liquid cluster, belong to the following syllable: ⟨palabra⟩ /paˈlabɾa/. Write ˈ on every stressed word, monosyllables included (⟨pan⟩ /ˈpan/), and on no unstressed function word (see function_words). Adverbs in ⟨-mente⟩ take primary stress on -men- and secondary ˌ on the base: /ˌfaθilˈmente/. Words with enclitics written solid keep the verb's stress: ⟨dímelo⟩ /ˈdimelo/. Long vowels: none; vowel length is not phonemic and is never written. Geminates: none; ⟨ll⟩ /ʎ/ and ⟨rr⟩ /r/ are single phonemes. Case endings: none; Leonese has no nominal case.

Source: Accentuation rules of the Propuesta de Norma Ortográfica para el Leonés (anonymous, c. 2010), section on accentuation, which follows the common Ibero-Romance (Spanish/Asturian) system. Phonological basis per Navarro Tomás (1918) Manual de pronunciación española, chapter on accent, and Hualde (2005) The Sounds of Spanish, chapter on stress. The -mente double stress follows Navarro Tomás.

## Stressed and unstressed words

Follow the Navarro Tomás list of unstressed words. Unstressed words get no ˈ mark and are written in full citation form, with no vowel reduction. UNSTRESSED: (a) Definite articles: el, la, lo/lu, los, las/les, as in ⟨el llobu⟩ /el ˈʎobu/. (b) Contractions written solid: al, del, nel, na, pol, pola, col, cola, pal, as in /pola ˈkaʎe/. (c) Prepositions: a, de, en, con, por, pa, sin, sobre, ente/entre, dende, hasta/hastra, hacia. (d) Conjunctions: y /i/, ya meaning 'and' /ʝa/, e, ou/o, nin, que, si, pero, mas, porque. (e) Relatives: que, quien, cuyu, onde, cuando, como. (f) Clitic pronouns: me, te, se, lu, la, lo, los, las, les, lle, lles, mos, nos, vos, os. These are unstressed both when free and when hyphen-joined as separate words, e.g. ⟨da-lle⟩ /ˈda/ /ʎe/. (g) Prenominal possessives without article: mi, tu, su. (h) Reduced negation nun /nun/. STRESSED: (a) All verb forms, including auxiliaries and copula: ⟨ye⟩ /ˈʝe/, ⟨hai⟩ /ˈai̯/, ⟨foi⟩ /ˈfoi̯/, ⟨tien⟩ /ˈtjen/. (b) Indefinite articles: un /ˈun/, una /ˈuna/. (c) Subject and prepositional pronouns: you /ˈʝou̯/, tú /ˈtu/, él /ˈel/, nós /ˈnos/, mí /ˈmi/. (d) Possessives after the article: el mieu /el ˈmjeu̯/. (e) Demonstratives and numerals. (f) Interrogatives and exclamatives: qué /ˈke/, ónde /ˈonde/. (g) Full negation non /ˈnon/. (h) Adverb ya meaning 'already' /ˈʝa/. (i) All nouns, adjectives and adverbs.

Source: Navarro Tomás (1918) Manual de pronunciación española, chapter on accented and unaccented words. Quilis (1993) Tratado de fonología y fonética españolas, chapter on accent. Applied to Leonese forms as listed in Morala & Egido (2009) and the Propuesta de Norma Ortográfica.

## Pausal forms

Does not apply: Leonese has no pausal forms, case endings or nunation, so every word is written in the same form at a sentence end, at a comma and sentence-internally. Final ⟨-u, -e, -i, -o⟩ are written as spelled: ⟨fiyu⟩ /ˈfiʝu/ in all positions.

Source: Menéndez Pidal (1906) El dialecto leonés. Zamora Vicente (1967) Dialectología española, chapter on Leonese. Neither describes any pausal alternation.

## Connected speech

Write no cross-word process; each word keeps its citation form, with stress or no stress as set by function_words. Specifically, none of the following is written: (a) Synalepha or vowel merger across words: ⟨la agua⟩ /la ˈaɡwa/. (b) Nasal or lateral place assimilation: ⟨en Bembibre⟩ /en bemˈbibɾe/, not [em]. (c) /s/ voicing before voiced consonants: ⟨los güevos⟩ /los ˈɡwebos/. (d) Resyllabification of final consonants. (e) Gliding of the conjunction y before a vowel, which stays /i/. Elision is written only where the spelling shows it with an apostrophe. Each piece is then its own word and is transcribed with exactly its spelled segments: ⟨d'agua⟩ → /d/ /ˈaɡwa/; ⟨l'home⟩ → /l/ /ˈome/. Contractions spelled as one word are one IPA word: ⟨nel⟩ /nel/.

Source: Broad phonemic practice of Martínez-Celdrán, Fernández-Planas & Carrera-Sabaté (2003) 'Castilian Spanish', JIPA 33(2): 255-259, which transcribes words in citation form. The spec disables the ALLA-based Asturian allophone rules, and no published source for these processes in León, Zamora or Portugal was consulted, so none is written.

## Glides and diphthongs

Write prenuclear (rising) glides as j and w, and postnuclear (falling) glides as i̯ and u̯. Rising: ⟨fierro⟩ /ˈfjero/, ⟨fuente⟩ /ˈfwente/, ⟨llingua⟩ /ˈʎinɡwa/, ⟨güevu⟩ /ˈɡwebu/. Falling, including the western Leonese diphthongs ou and ei: ⟨cousa⟩ /ˈkou̯sa/, ⟨caldeiru⟩ /kalˈdei̯ɾu/, ⟨you⟩ /ˈʝou̯/, ⟨hai⟩ /ˈai̯/. Keep the glide j strictly apart from the consonant ⟨y⟩ /ʝ/ in onsets: ⟨fiyu⟩ /ˈfiʝu/, ⟨meyor⟩ /meˈʝoɾ/. Word-final ⟨-y⟩ after a vowel is i̯. Accented ⟨í, ú⟩ next to a vowel form a hiatus with a full vowel: ⟨día⟩ /ˈdia/. ⟨ü⟩ is w. Silent ⟨u⟩ in ⟨que, qui, gue, gui⟩ is not written.

Source: Martínez-Celdrán, Fernández-Planas & Carrera-Sabaté (2003), JIPA 33(2), for the j w / i̯ u̯ split. Leonese ou/ei diphthongs per Menéndez Pidal (1906) El dialecto leonés and Zamora Vicente (1967) Dialectología española.

## Other choices

### Voiced stops and other allophones

Broad phonemic: ⟨b, v⟩ /b/, ⟨d⟩ /d/, ⟨g⟩ /ɡ/ in all positions, never [β ð ɣ]: ⟨llugar⟩ /ʎuˈɡaɾ/, ⟨vida⟩ /ˈbida/. Nasals are written as spelled, ⟨n⟩ /n/ and ⟨m⟩ /m/ (⟨cinco⟩ /ˈθinko/), with no [ŋ]. Phonetic descriptions report Spanish-type spirantization, but this spec disables allophone rules.

Source: Spec note (ast allophone rules disabled). Spirantization as described in Hualde (2005) The Sounds of Spanish is deliberately not transcribed.

### Palatals ll / y / ch / x / ñ

⟨ll⟩ /ʎ/ (⟨lluz⟩ /ˈʎuθ/), kept distinct from ⟨y⟩ /ʝ/, with no yeísmo. ⟨ch⟩ /tʃ/ (⟨chamar⟩ /tʃaˈmaɾ/). ⟨x⟩ /ʃ/ (⟨xente⟩ /ˈʃente/). The spec note calls ⟨x⟩ 'dorsopalatal'; dialectological descriptions treat it as prepalatal, and /ʃ/ is used either way. ⟨ñ⟩ /ɲ/; NW forms spelled with ⟨n⟩ (cabana) are /n/. Laciana/Alto Sil che vaqueira and -LJ- > /tʃ/ variants are written only if spelled (⟨mechor⟩ /meˈtʃoɾ/). ⟨j⟩ and ⟨ge, gi⟩ in Castilianisms are /x/.

Source: Morala & Egido (2009), pp. 10, 15-16 (per spec); Propuesta de Norma Ortográfica §§1, 2.2-2.3, 3.4-3.5; Menéndez Pidal (1906).

### Sibilants, rhotics, h

⟨c(e,i)⟩ and ⟨z⟩ are /θ/ (distinción): ⟨facer⟩ /faˈθeɾ/. ⟨s⟩ is /s/. ⟨r⟩ is the tap /ɾ/ between vowels, in codas and after obstruents. ⟨rr⟩, word-initial ⟨r⟩, and ⟨r⟩ after l, n, s are the trill /r/: ⟨ríu⟩ /ˈriu/. ⟨h⟩ is silent: ⟨home⟩ /ˈome/. ⟨f⟩ is /f/: ⟨fierro⟩ /ˈfjero/.

Source: Zamora Vicente (1967) Dialectología española, chapter on Leonese; Propuesta de Norma Ortográfica.

### Unstressed final vowels

Write vowels as spelled, with five vowels /a e i o u/ and no reduction. Final ⟨-u⟩ is /u/ and ⟨-e⟩ is /e/: ⟨llobu⟩ /ˈʎobu/, ⟨noche⟩ /ˈnotʃe/. Variable local closing of /e o/ to [i u] and metaphony are not written unless spelled.

Source: Menéndez Pidal (1906) El dialecto leonés; Zamora Vicente (1967).

### Medieval register

Only for sentences in medieval spelling, use the medieval four-way sibilant system: ⟨ç, c(e,i)⟩ /ts/; ⟨z⟩ /dz/; ⟨ss⟩ and initial or post-consonantal ⟨s⟩ /s/; single intervocalic ⟨s⟩ /z/; ⟨x⟩ /ʃ/; ⟨j, g(e,i)⟩ /ʒ/. Sentences in modern spelling use the modern values above.

Source: Menéndez Pidal (1906) El dialecto leonés; Morala & Egido (2009); spec note on 4-way sibilant contrast.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
