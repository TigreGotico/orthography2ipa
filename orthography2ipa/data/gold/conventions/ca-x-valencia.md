# Transcription conventions: Valencian (ca-x-valencia)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark primary stress with ˈ before the stressed syllable. Syllabify onsets maximally: muntanya [munˈtaɲa], aigua [ˈajɣwa], cantar [kanˈtaɾ], germà [dʒeɾˈma]. Place the stress as follows. (1) A written accent (à è é í ò ó ú) marks the stressed vowel and always wins: història [isˈtɔɾia], café [kaˈfe]. (2) Unaccented words ending in a vowel, a vowel + ⟨s⟩, or ⟨-en/-in⟩ stress the penultimate syllable: casa [ˈkaza], cases [ˈkazes], jove [ˈdʒove], examen [eɡˈzamen]. (3) All other unaccented words stress the final syllable, including plurals in consonant + ⟨s⟩: amic [aˈmik], amics [aˈmiks], cantar [kanˈtaɾ]. (4) The diaeresis ï ü marks hiatus, not stress: veïna [veˈina]. Monosyllabic content words get ˈ: molt [ˈmolt], camp [ˈkamp], sang [ˈsaŋk]. Atonic monosyllables (see function_words) get no mark. Every polysyllable gets its mark, including polysyllabic prepositions and conjunctions: sobre [ˈsobɾe], perquè [peɾˈke]. Mark only primary stress. Adverbs in -ment take one mark, on -ment: clarament [klaɾaˈment]. Vowel quality: there is no unstressed reduction. Stressed ⟨e o⟩ are [ɛ ɔ] or [e o] as the accent shows (è ò = [ɛ ɔ], é ó = [e o]). When unaccented, their quality is lexical and taken from the Valencian entry of the DCVB/DNV: gos [ˈɡos], tot [ˈtot], molt [ˈmolt], cos [ˈkɔs], pont [ˈpɔnt], tres [ˈtɾɛs]. Unstressed ⟨e o⟩ are always [e o]. Catalan has no phonemic vowel length: never write ː on vowels. Geminates are written as two consonants across the syllable boundary: col·legi [kolˈledʒi], ametla [aˈmella], bitllet [biʎˈʎet]. Case endings do not apply to this lect.

Source: IEC 2016, Gramàtica de la llengua catalana, ch. 3 (l'accent); Wheeler 2005 §3.1 (stress), §2.3 (Western block: no reduction), §5.2 (pre-lateral gemination); Recasens 1996 (Western vowels); DCVB headwords for lexical ⟨e o⟩ quality; AVL 2006 for accepted Valencian é/ó spellings.

## Stressed and unstressed words

Atonic words carry no ˈ and keep full, unreduced vowels, because Valencian has no reduction. They are the following. Definite articles: el [el], la [la], els [els], les [les]. Personal article: en [en], na [na]. Contractions: al [al], del [del], pel [pel], als [als], dels [dels], pels [pels]. Monosyllabic prepositions: a [a], de [de], en [en], per [peɾ], amb [am] (see connected_speech for amb). Conjunctions: i [i], o [o], ni [ni], que [ke], conditional si [si]. Relative and conjunctive com, quan, on, qui when they introduce a clause or a comparison: com [kom], quan [kwan], on [on], qui [ki]. All weak pronouns, whether proclitic, hyphenated enclitic or apostrophe remnant: em [em], me [me], et [et], te [te], es [es], se [se], ens [ens], nos [nos], us [us], vos [vos], el [el], lo [lo], la [la], els [els], los [los], les [les], li [li], hi [i], ho [o], en [en], ne [ne], m [m], t [t], s [s], l [l], n [n]. Examples: cantar-lo = [kanˈtaɾ lo], m'agrada = [m aˈɣɾaða], l'home = [l ˈome]. Possessives mon, ton, son: [mon], [ton], [son]. Stressed words: the indefinite article un [ˈun], una [ˈuna]; interrogative què [ˈkɛ], qui [ˈki], com [ˈkom], quan [ˈkwan], on [ˈon] in direct or indirect questions; sí [ˈsi]; no [ˈno]; tonic pronouns jo [ˈdʒo], ell [ˈeʎ], mi [ˈmi]; demonstratives, possessives meu [ˈmew] etc., numerals, adverbs. All verb forms are stressed, including auxiliaries and the copula: ha [ˈa], han [ˈan], he [ˈe], és [ˈes], va [ˈva] in va cantar [ˈva kanˈtaɾ].

Source: IEC 2016, §6.2 and the list of mots àtons; Wheeler 2005 §2.3 (Western block: no reduction of atonic forms); AVL 2006 for the Valencian full pronoun forms (me, te, se, vos, lo, los).

## Pausal forms

No pausal forms in the Arabic sense: final short vowels, case endings and nunation do not apply to this lect. The only boundary effect is that a pause blocks sandhi. A pause is the end of the sentence and any punctuation mark inside it (comma, colon, semicolon, dash, parenthesis, quotation mark). Apostrophes and hyphens are not pauses. Before a pause, a word takes its isolation form. Final obstruents are voiceless: verd [ˈveɾt], fred [ˈfɾet], llarg [ˈʎaɾk], mig [ˈmitʃ], dos [ˈdos]. Final clusters stay intact: vint [ˈvint], molt [ˈmolt], sang [ˈsaŋk]. Final ⟨-r⟩ is pronounced: cantar [kanˈtaɾ]. After a pause, the first word starts as if utterance-initial, so /b d ɡ/ there are stops: bé [ˈbe], dona [ˈdona], gat [ˈɡat].

Source: Wheeler 2005 §5.3 (final-obstruent devoicing) and §10.2–§10.5 (phrase-level processes); Veny 1982 ch. 3 (Valencian keeps final ⟨-r⟩ and final clusters).

## Connected speech

Write sandhi inside the words it affects. Never join, drop or move words. Each spelled word keeps its own IPA word, and an apostrophe remnant is written alone: d'aigua = [d ˈajɣwa]. Inside a sentence with no punctuation between the words, apply these processes. (1) Voicing of final sibilants and affricates: they become voiced before a vowel or a voiced consonant and stay voiceless before a voiceless consonant. Examples: els homes [elz ˈomes], dos dies [ˈdoz ˈðies], s'obri [z ˈɔβɾi], mig any [ˈmidʒ ˈaɲ], dos peus [ˈdos ˈpews]. (2) Final stops: they become voiced before a voiced consonant and stay voiceless before a vowel: cap gat [ˈkab ˈɡat], cap home [ˈkap ˈome]. (3) Spirantization: /b d ɡ/ are stops after a pause or a nasal, and /d/ is also a stop after [l]. Elsewhere they are [β ð ɣ], within and across words. Examples: la boca [la ˈβoka], cada [ˈkaða], alba [ˈalβa], caldre [ˈkaldɾe], un gat [uŋ ˈɡat]. ⟨v⟩ is always [v] and never spirantizes: la vaca [la ˈvaka]. (4) Nasal place assimilation: /n/ is [m] before [p b m], [ɱ] before [f v], and [ŋ] before [k ɡ]. Examples: en Pere [em ˈpeɾe], un cotxe [uŋ ˈkotʃe], canvi [ˈkaɱvi]. (5) Final cluster simplification: a word-final stop after a nasal or lateral (⟨-nt -lt -mp -nc -ng⟩) is dropped before a consonant and kept before a vowel or pause. Examples: vint de juny [ˈvin de ˈdʒuɲ], molt bé [ˈmol ˈbe], molt alt [ˈmolt ˈalt]. amb is [am] (assimilated) before a consonant and [amb] before a vowel: amb Pere [am ˈpeɾe], amb ell [amb ˈeʎ]. Plurals (-nts, -lts) and -st are not simplified: molts dies [ˈmolts ˈðies]. Final ⟨-r⟩ stays [ɾ] before a vowel: cantar-ho [kanˈtaɾ o]. (6) Vowel contact across words: write no unwritten synalepha, elision or gliding. Each word keeps all its vowels: la illa [la ˈiʎa], que ho [ke o]. Elision is written only where the spelling has an apostrophe.

Source: Wheeler 2005 §5.2 (spirantization, /v/ vs /b/), §5.3 (cross-word voicing), §10.2–§10.5 (final-cluster simplification, nasal assimilation, lenition); Veny 1982 ch. 3 (Valencian cluster isoglosses); Bonet & Lloret 1998 ch. 5 (cross-word hiatus, which this convention does not transcribe).

## Glides and diphthongs

Write non-syllabic high vowels as [j w], never [i̯ u̯]. Falling diphthongs: ai [aj], ei [ej]/[ɛj], oi [oj]/[ɔj], ui [uj], au [aw], eu [ew]/[ɛw], iu [iw], ou [ow]/[ɔw]. Examples: mai [ˈmaj], meu [ˈmew], noia [ˈnoja], creu [ˈkɾew]. Rising diphthongs only after ⟨q g⟩ + ⟨u/ü⟩: quatre [ˈkwatɾe], aigua [ˈajɣwa], qüestió [kwestiˈo], pingüí [piŋˈɡwi]. A word-initial or intervocalic ⟨i⟩ or ⟨y⟩ before a vowel is [j]: iogurt [joˈɣuɾt], joia [ˈdʒoja]. ⟨ix⟩ after a vowel is [jʃ]: caixa [ˈkajʃa], peix [ˈpejʃ]. Word-final ⟨-ig⟩ after a vowel is [tʃ], with no glide: maig [ˈmatʃ], puig [ˈputʃ]. Post-consonantal unstressed ⟨-ia -ie -io -ua -ue -uo⟩ are hiatus with full vowels: pàtria [ˈpatɾia], aigües is the exception only through ⟨gü⟩ = [ˈajɣwes]. ⟨ï ü⟩ elsewhere mark hiatus: veïna [veˈina], raïm [raˈim].

Source: Wheeler 2005 §2.5 (diphthong inventory), §5.1 (⟨ix⟩, word-final ⟨-ig⟩); IEC 2016 ch. 3 (diaeresis and hiatus); Veny 1982 ch. 3 (Western [jʃ]).

## Other choices

### /v/ vs /b/

Keep ⟨v⟩ = [v] distinct from ⟨b⟩ = [b]/[β]: viu [ˈviw], beu [ˈbew], la vida [la ˈviða]. This follows the AVL standard and the spec. Most central Valencian speech merges the two as [b]/[β], but that merger is not transcribed.

Source: AVL 2006; Wheeler 2005 §5.1; Veny 1982 ch. 3 (betacism isogloss).

### Sibilants and voicing

Write the apico-alveolar sibilants as plain [s z] in broad transcription. Intervocalic ⟨s⟩ and all ⟨z⟩ are [z]; ⟨ss⟩, ⟨ç⟩ and ⟨c⟩+e/i are [s]: casa [ˈkaza], massa [ˈmasa], zero [ˈzeɾo]. Write the voiced sibilants and affricates of the standard, not apitxat devoicing.

Source: Recasens 1991 (Valencian sibilants); AVL 2006; Veny 1982 ch. 3 (apitxat as a regional, non-standard feature).

### Affricates and ⟨x⟩

⟨j⟩ and ⟨g⟩+e/i are [dʒ]: germà [dʒeɾˈma], jove [ˈdʒove]. ⟨tj tg⟩ are [dʒ]: metge [ˈmedʒe]. ⟨tx⟩ is [tʃ]: cotxe [ˈkotʃe]. ⟨x⟩ is [tʃ] word-initially and after a consonant: xiquet [tʃiˈket], xarxa [ˈtʃaɾtʃa]. Learned ⟨x⟩ is [ks], or [ɡz] in ex-+vowel: taxi [ˈtaksi], examen [eɡˈzamen]. ⟨h⟩ is silent.

Source: Recasens 1991; Wheeler 2005 §5.1; AVL 2006.

### Rhotics

Write [ɾ] for single ⟨r⟩ between vowels, after an obstruent and in all codas (including word-final): pare [ˈpaɾe], cantar [kanˈtaɾ], porta [ˈpɔɾta]. Write trill [r] for ⟨rr⟩, word-initial ⟨r⟩ and ⟨r⟩ after ⟨n l s⟩: terra [ˈtɛra], roda [ˈroða], honra [ˈonra].

Source: Wheeler 2005 §5.1; spec note on the Valencian coda rhotic [ɾ].

### Intervocalic /d/ and final ⟨-a⟩

Keep intervocalic /d/ as [ð] in -ada, -ador, -edor: cantada [kanˈtaða], not colloquial [kanˈtaa]. Write final unstressed ⟨-a⟩ as [a], not regional [ɔ]/[ɛ]: terra [ˈtɛra].

Source: AVL 2006 (standard oral register); Veny 1982 ch. 3 and Recasens 1996 (regional harmony and d-deletion).

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
