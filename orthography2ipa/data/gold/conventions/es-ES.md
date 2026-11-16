# Transcription conventions: Castilian Spanish (es-ES)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark primary stress with ˈ before the onset of the stressed syllable. Syllabify by onset maximisation. The legal onset clusters are stop or /f/ + /l ɾ/ (hablar [aˈβlaɾ], otro [ˈotɾo], tres [ˈtɾes]). In Spain ⟨tl⟩ is split (atlántico [atˈlantiko]). Placement follows the orthography. (1) A tilde marks the stressed vowel: café [kaˈfe], árbol [ˈaɾβol], nación [naˈθjon], día [ˈdia]. (2) With no tilde, a word ending in a vowel, ⟨n⟩ or ⟨s⟩ is stressed on the penult: casa [ˈkasa], joven [ˈxoβen], lunes [ˈlunes]. (3) With no tilde, any other final letter, including final ⟨y⟩, gives final stress: papel [paˈpel], verdad [beɾˈðað], virrey [biˈrei̯]. A diphthong or triphthong counts as one syllable, and a tilde on a high vowel makes a hiatus. Mark stress on every stressed word, monosyllables included: sol [ˈsol], pan [ˈpan], mí [ˈmi]. Unstressed function words get no mark (see function_words). Write no secondary stress. Exception: adverbs in -mente keep both lexical stresses, each written ˈ: rápidamente [ˈrapiðaˈmente], claramente [ˈklaɾaˈmente]. Enclitics written solid with the verb do not move its stress: dame [ˈdame], dímelo [ˈdimelo], diciéndole [diˈθjendole]. Spanish has no long vowels. A doubled vowel letter is a hiatus of two vowels: leer [leˈeɾ], alcohol [alkoˈol], Saavedra [saaˈβeðɾa]. Spanish has no geminate phonemes. A doubled letter is written double only where both consonants are pronounced: innato [inˈnato], acción [akˈθjon]. ⟨rr⟩ is one trill [r] and ⟨ll⟩ is one [ʝ]. Case endings do not apply: Spanish has no case morphology on nouns.

Source: RAE & ASALE 2010 Ortografía de la lengua española ch. 2 (acentuación gráfica); RAE & ASALE 2011 NGLE Fonética y fonología chs. 9–10 (acento; adverbios en -mente con dos acentos); Hualde 2005 ch. 11; Navarro Tomás 1977 §§ on acento.

## Stressed and unstressed words

This follows the Navarro Tomás / Quilis list of palabras átonas versus tónicas. UNSTRESSED (no ˈ):
- definite articles el, la, lo, los, las;
- prenominal possessives mi, tu, su, mis, tus, sus, nuestro/-a/-os/-as, vuestro/-a/-os/-as;
- all simple prepositions (a, ante, bajo, con, contra, de, desde, en, entre, hacia, hasta, para, por, sin, sobre, tras), except según [seˈɣun];
- conjunctions y, e, ni, o, u, pero, mas, que, si, porque, aunque, pues;
- relatives without tilde: que, quien, cual, cuyo, donde, cuando, como, cuanto;
- object clitics me, te, se, nos, os, lo, la, los, las, le, les, whether proclitic, enclitic in solid spelling, or a separate hyphenated word;
- the titles don, doña, san, santo, fray, sor before a name.
Examples: la casa [la ˈkasa], de Madrid [de maˈðɾið], te lo dije [te lo ˈdixe], el que viene [el ke ˈβjene].
STRESSED (ˈ):
- nouns, adjectives, lexical verbs and adverbs;
- ALL verb forms, including the auxiliaries haber, ser, estar: he comido [ˈe koˈmiðo], está cansado [esˈta kanˈsaðo];
- indefinite articles un, una, unos, unas: un libro [ˈun ˈliβɾo];
- numerals, demonstratives, postnominal or pronominal possessives (mío, tuyo, suyo);
- subject pronouns yo, tú, él, ella, nosotros, usted;
- prepositional pronouns mí, ti, sí, conmigo;
- interrogatives and exclamatives with tilde: qué, quién, cuál, cómo, cuándo, dónde, cuánto;
- según.
The tilde-bearing member of a written pair is always stressed and the bare one is unstressed: tu [tu] / tú [ˈtu], el [el] / él [ˈel], si [si] / sí [ˈsi], mi [mi] / mí [ˈmi].

Source: Navarro Tomás 1977 §§ on palabras acentuadas y inacentuadas; Quilis 1993 ch. on el acento (palabras tónicas y átonas); RAE & ASALE 2011 NGLE Fonética y fonología ch. 10; Hualde 2005 ch. 11.

## Pausal forms

Spanish has no pausal morphology. There are no case endings and no nunation (tanwīn), and final short vowels are never dropped or altered: casa [ˈkasa] in every position. The only effect of a pause is on the following word. Treat these as pause positions: the start of the sentence, and the first word after a comma, semicolon, colon, dash, parenthesis or quotation break. There, word-initial /b d ɡ/ are stops: Bueno, dame [ˈbweno ˈdame]; ..., gracias [ˈɡɾaθjas]. Elsewhere they follow the connected-speech rule. Word-final /d/ is written [ð] everywhere, at pause too: verdad [beɾˈðað], Madrid [maˈðɾið]. The spec's optional zero variant is not written. Final /s/ is never aspirated or dropped.

Source: Hualde 2005 ch. 8 (stop vs approximant allophones of /b d ɡ/ after pause); Navarro Tomás 1977 §§ on /d/ final; RAE & ASALE 2011 NGLE Fonética y fonología ch. on /d/ (Castilian [ð] as the standard final realisation).

## Connected speech

Each word stays in its own slot. A cross-boundary process changes only the segment at the edge of a word, and nothing is moved or merged. Two processes apply across word boundaries, conditioned by the last segment of the previous word.
(1) Nasal place assimilation. A coda /n/ is written [m] before /p b m/, inside words and across them: un beso [ˈum ˈbeso], en Madrid [em maˈðɾið], inmaculada [immakuˈlaða]. Elsewhere it stays [n], including before /f/ and velars: enfermo [enˈfeɾmo], tengo [ˈtenɡo], un gato [ˈun ˈɡato]. The spec's broad level writes only the bilabial allophone. Navarro Tomás describes labiodental and velar nasals here, but they are not written.
(2) Spirantisation of /b d ɡ/. Write /b d ɡ/ as approximants [β ð ɣ] everywhere except in three positions, where they are stops [b d ɡ]: after a pause (see pausal_forms), after a nasal, and for /d/ only after /l/. This applies within and across words: la boca [la ˈβoka], los dedos [los ˈðeðos], el gato [el ˈɣato], el dedo [el ˈdeðo], un dedo [ˈun ˈdeðo]. It also covers post-consonantal position: alba [ˈalβa], algo [ˈalɣo], caldo [ˈkaldo], verde [ˈbeɾðe], desde [ˈdesðe]. This is broader than the spec's note 7, which says between vowels only. The standard descriptions give the wider distribution.
NOT written:
- synalepha or glide formation across words: mi amigo [mi aˈmiɣo], agua y aceite [ˈaɣwa i aˈθei̯te];
- merger of identical vowels: la amiga [la aˈmiɣa];
- resyllabification: los otros [los ˈotɾos], with stress marks always placed by word-internal syllabification;
- voicing of /s/ or /θ/ before voiced consonants: mismo [ˈmismo], los mismos [los ˈmismos], hazme [ˈaθme];
- /s/ deletion before /r/.

Source: Hualde 2005 ch. 8 (distribution of [b d ɡ] vs [β ð ɣ]) and ch. on nasals; Navarro Tomás 1977 §§ on asimilación de las nasales, enlace and sinalefa; Quilis 1993 (nasal assimilation).

## Glides and diphthongs

Use asymmetric notation, as the spec does.
- A rising diphthong has a consonantal onglide [j w]: nación [naˈθjon], tierra [ˈtjera], cuando [ˈkwando], después [desˈpwes], Adrián [aˈðɾjan].
- A falling diphthong has a non-syllabic offglide [i̯ u̯]: aire [ˈai̯ɾe], causa [ˈkau̯sa], hoy [ˈoi̯], muy [ˈmui̯], rey [ˈrei̯], deuda [ˈdeu̯ða].
- In triphthongs the onglide is written [j w] and the offglide [i̯ u̯]: buey [ˈbwei̯], Uruguay [uɾuˈɣwai̯], estudiáis [estuˈðjai̯s].
- ⟨ui⟩ and ⟨iu⟩ inside a word are rising: ruido [ˈrwiðo], ciudad [θjuˈðað]. Word-final ⟨uy⟩ is falling: muy [ˈmui̯].
- An unstressed ⟨i u⟩ next to another vowel is always a glide unless the high vowel bears a tilde. Lexical hiatus is not marked: cliente [ˈkljente], piano [ˈpjano], riendo [ˈrjendo], suave [ˈswaβe].
- A tilde on the high vowel makes a hiatus of two full vowels: día [ˈdia], país [paˈis], búho [ˈbuo], continúo [kontiˈnuo].
- Sequences of non-high vowels (ea, eo, oa, ae, oe) are hiatus with no glide: teatro [teˈatɾo], poeta [poˈeta].
- Word-initial ⟨hie- hia- hio-⟩ is [ʝ] in every sentence position, whatever the previous word ends in: hielo [ˈʝelo], la hierba [la ˈʝeɾβa]. Word-internally after a vowel it is the glide [j]: antihielo [antiˈjelo].
- Word-initial ⟨hue- hui-⟩ is [w], with no [ɣ] strengthening: huevo [ˈweβo], hueso [ˈweso].

Source: Hualde 2005 ch. 4 (diphthongs, glides and hiatus) and ch. 10; RAE & ASALE 2011 NGLE Fonética y fonología ch. 8 (diptongos, triptongos, hiatos); Navarro Tomás 1977 §§ on diptongos; spec notes 9 and 12.

## Other choices

### rhotics

The trill [r] is written word-initially (rosa [ˈrosa]), for ⟨rr⟩ (perro [ˈpero]), and after a heterosyllabic /l n s/ (alrededor [alreðeˈðoɾ], honra [ˈonra], Israel [israˈel]). The tap [ɾ] is written everywhere else: intervocalic ⟨r⟩ (pero [ˈpeɾo]), onset clusters (tres [ˈtɾes]), and all codas, word-final included (verde [ˈbeɾðe], comer [koˈmeɾ], verdad [beɾˈðað]). The spec's example [berˈdað] writes a coda trill and a stop after it. This follows Hualde instead: coda tap, and [ð] after /ɾ/.

Source: Hualde 2005 ch. 10 (rhotics; coda neutralisation realised as tap in normal speech); RAE & ASALE 2011 NGLE Fonética y fonología ch. on vibrantes; Navarro Tomás 1977.

### sibilant and interdental

Distinción applies: ⟨z⟩ and ⟨c⟩ before e/i are [θ] (cielo [ˈθjelo], zapato [θaˈpato]), and ⟨s⟩ is [s]. Seseo is never used. The apico-alveolar quality is not marked: write plain [s], not [s̺] (casa [ˈkasa]). ⟨cc⟩ is [kθ]: lección [lekˈθjon].

Source: RAE & ASALE 2011 NGLE Fonética y fonología (distinción as the Castilian norm); Hualde 2005 ch. 9; spec notes 1–2.

### palatal and velar fricatives

⟨y⟩ as a consonant and ⟨ll⟩ are always [ʝ] (yeísmo): calle [ˈkaʝe], yo [ˈʝo]. This holds after a nasal, after /l/ and after a pause too, so no affricate [ɟʝ] is written: cónyuge [ˈkonʝuxe], el yeso [el ˈʝeso]. ⟨ch⟩ and ⟨tx⟩ are [tʃ]: noche [ˈnotʃe], pintxo [ˈpintʃo]. ⟨j⟩ and ⟨g⟩ before e/i are always [x], never [χ]: jamón [xaˈmon], gente [ˈxente].

Source: RAE & ASALE 2011 NGLE Fonética y fonología (yeísmo; /x/); Hualde 2005 ch. 9; Hualde & Ortiz de Urbina 2003 for ⟨tx⟩; spec notes 3, 5, 13.

### letter x

Intervocalic and coda ⟨x⟩ is [ks]: examen [ekˈsamen], texto [ˈteksto]. The [ɣs] variant is not written. Word-initial ⟨x⟩ is [s]: xilófono [siˈlofono]. ⟨x⟩ is [x] in the traditional spellings México [ˈmexiko], Oaxaca [oaˈxaka], Texas [ˈtexas].

Source: RAE & ASALE 2010 Ortografía ch. 1 (letra x); RAE & ASALE 2011 NGLE Fonética y fonología; Navarro Tomás 1977.

### coda obstruents

Coda voiceless stops are written as spelled: apto [ˈapto], acto [ˈakto], atlas [ˈatlas]. Coda ⟨b d g⟩ follow the spirantisation rule and are written [β ð ɣ]: absoluto [aβsoˈluto], adquirir [aðkiˈɾiɾ], digno [ˈdiɣno]. The exception is a coda after a nasal, which stays a stop. ⟨h⟩ is silent: hacer [aˈθeɾ]. ⟨b⟩ and ⟨v⟩ are the same phoneme: vino [ˈbino], la vaca [la ˈβaka].

Source: Hualde 2005 ch. 8; Navarro Tomás 1977 §§ on consonantes implosivas; spec notes 4, 6.

### vowels

Use five vowels [a e i o u] with no reduction in unstressed syllables, and no open/close allophones marked: perro [ˈpero], comer [koˈmeɾ].

Source: Hualde 2005 ch. 6; Quilis 1993; Navarro Tomás 1977 (allophonic vowel opening described but not written in broad transcription).

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
