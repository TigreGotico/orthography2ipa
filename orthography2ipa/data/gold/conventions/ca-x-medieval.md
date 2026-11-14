# Transcription conventions: Old Catalan (ca-x-medieval)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark primary stress with ˈ before the stressed syllable of every stressed word, monosyllables included: [ˈflor], [ˈpa]. Mark no secondary stress and no syllable dots. Placement follows the modern IEC orthographic rules. (1) A written accent marks the stressed vowel and always wins: ⟨història⟩ [isˈtɔria], ⟨cafè⟩ [kaˈfɛ]. (2) An unaccented word ending in a vowel, vowel+⟨s⟩, ⟨-en⟩ or ⟨-in⟩ is stressed on the penult: ⟨casa⟩ [ˈkaza], ⟨dies⟩ [ˈdies], ⟨canten⟩ [ˈkanten]. (3) Every other unaccented word is stressed on the last syllable, consonant+⟨s⟩ plurals included: ⟨amor⟩ [aˈmor], ⟨camins⟩ [kaˈmins], ⟨cantar⟩ [kanˈtar]. (4) The diaeresis ⟨ï ü⟩ marks hiatus, not stress: ⟨veïna⟩ [veˈina]. (5) Adverbs in ⟨-ment⟩ take one primary stress, on ⟨-ment⟩: ⟨clarament⟩ [klaraˈment]. Accent quality: ⟨è ò⟩ = [ɛ ɔ] and ⟨é ó⟩ = [e o]. The lect has no phonemic long vowels and no case endings. Geminates ([ll], [bbl], [mm]) are consonant clusters and never move the stress.

Source: Institut d'Estudis Catalans 2016, Gramàtica de la llengua catalana, ch. 3 (l'accent); Wheeler 2005, The Phonology of Catalan, §3.1. The modern accentuation is applied to the modern orthography, as the spec notes require (medieval manuscripts are unaccented).

## Stressed and unstressed words

The following words are unstressed: they get no ˈ mark and are written with unstressed vowels. Definite and personal articles: el, la, lo, els, les, los, l', en, na. Contractions: al, als, del, dels, pel, pels. Atonic possessive determiners: mon, ton, son, ma, ta, sa, mos, mes, etc. Atonic prepositions: a, de, d', en, amb, per, per a. Conjunctions: i, o, ni, que, si, com, quan. Relative que and qui. All weak pronouns, proclitic or enclitic: em, et, es, se, en, ne, hi, ho, li, la, lo, els, les, ens, us, me, te, m', t', s', n', -lo, -la, -los, -ne, -hi. Examples: ⟨la casa⟩ [la ˈkaza], ⟨de la dona⟩ [de la ˈðɔna], ⟨que ho diu⟩ [ke o ˈdiw], ⟨menjar-lo⟩ [menˈdʒar lo]. A one-consonant elided form after an apostrophe is written as its bare consonant: ⟨l'home⟩ [l ˈɔme], ⟨d'aigua⟩ [d ˈajɣwa]. Everything else is stressed: nouns, adjectives, full verbs, all auxiliaries and copulas (⟨ha vingut⟩ [ˈa vinˈɡut], ⟨és⟩ [ˈɛs]), the indefinite article and numerals (⟨un⟩ [ˈun], ⟨una⟩ [ˈuna]), tonic pronouns (⟨ell⟩ [ˈeʎ], ⟨mi⟩ [ˈmi]), demonstratives, interrogatives, adverbs, and the disyllabic preposition and conjunction ⟨però⟩, ⟨sobre⟩, ⟨contra⟩.

Source: Institut d'Estudis Catalans 2016, §6.2 and the list of 'mots àtons'; Wheeler 2005, §3.1. Treating auxiliaries and ⟨un/una⟩ as stressed follows the IEC list, which does not include them among the atonic words.

## Pausal forms

Not applicable as a distinct category: Catalan has no pausal forms, case endings or nunation. At a pause (sentence end or comma) a word keeps its full citation form. Final obstruents are voiceless: ⟨verd⟩ [ˈvert]. Final ⟨-nt -lt -mp -nc⟩ clusters are kept: ⟨cant⟩ [ˈkant], ⟨molt⟩ [ˈmolt]. Final ⟨-r⟩ is [r]: ⟨amor⟩ [aˈmor]. Final vowels are never dropped.

Source: Wheeler 2005, §5.3 and §10.2–10.5; Moll 2006 (Gramàtica històrica catalana) for final -r and final clusters kept in Old Catalan.

## Connected speech

Every word keeps its own slot. A sandhi process only changes the segments at the edges of the words involved. Apply these, and only these, inside a phrase not broken by punctuation. (1) Spirantization: word-initial /b d ɡ/ becomes [β ð ɣ] after a word ending in a vowel, a glide, a fricative or [r ɾ]: ⟨la dona⟩ [la ˈðɔna], ⟨de bon grat⟩ [de ˈβɔŋ ˈɡrat]. /b ɡ/ also spirantize after [l], but /d/ stays [d] there: ⟨el dia⟩ [el ˈdia]. All three stay stops after a pause or a nasal: ⟨un gat⟩ [uŋ ˈɡat]. /v/ never spirantizes: ⟨la vida⟩ [la ˈviða]. (2) Sibilant voicing: final /s/ is [z] before a vowel or a voiced consonant: ⟨les ales⟩ [lez ˈales], ⟨els dies⟩ [elz ˈðies]. (3) Voicing assimilation: a final stop or affricate becomes voiced before a voiced consonant (⟨cap dia⟩ [ˈkab ˈdia]) and stays voiceless before a vowel (⟨set anys⟩ [ˈsɛt ˈaɲs]). (4) Nasal place: final /n/ becomes [m] before /p b m f v/ (⟨en Pere⟩ [em ˈpɛre]) and [ŋ] before /k ɡ/ (⟨un cop⟩ [uŋ ˈkɔp]). It stays [n] elsewhere, including before palato-alveolars. (5) Pre-consonantal cluster simplification: final ⟨-nt -lt -mp -nc⟩ lose the stop before a consonant-initial word (⟨tant bo⟩ [ˈtam ˈbɔ], ⟨molt bé⟩ [ˈmol ˈβe]) and keep it before a vowel or a pause (⟨tant és⟩ [ˈtant ˈɛs]). (6) Final ⟨-r⟩ is [ɾ] before a vowel-initial word (⟨per a⟩ [peɾ a]) and [r] elsewhere. Do not apply vowel elision or synalepha, and do not mark resyllabification: two vowels across a word boundary are both written in full (⟨la amiga⟩ [la aˈmiɣa]).

Source: Wheeler 2005, §5.2 (spirantization), §5.3 (cross-word voicing) and §10.2–10.5 (cluster simplification, nasal assimilation, phrase-level lenition); Recasens 1993 (nasal place, spirantization). Rule (5) follows the spec notes, which treat simplification before a consonant as pan-Catalan. Moll 2006 describes the medieval clusters as intact, and this is honoured before a vowel or a pause.

## Glides and diphthongs

Write non-syllabic i/u as [j w], never [i̯ u̯]. Falling diphthongs: ⟨caixa⟩ [ˈkajʃa], ⟨rei⟩ [ˈrej], ⟨pau⟩ [ˈpaw], ⟨diu⟩ [ˈdiw], ⟨bou⟩ [ˈbɔw]. Rising diphthongs, only after ⟨qu gu qü gü⟩ before a vowel: ⟨quatre⟩ [ˈkwatre], ⟨aigua⟩ [ˈajɣwa]. ⟨i⟩ is [j] between vowels and word-initially before a vowel: ⟨noia⟩ [ˈnɔja], ⟨iogurt⟩ [joˈɣurt]. Any other i/u + vowel sequence, and any vowel under a diaeresis, is a hiatus of two full vowels, written without a dot: ⟨dia⟩ [ˈdia], ⟨veïna⟩ [veˈina]. ⟨ix⟩ after a vowel letter is always [jʃ]: ⟨peix⟩ [ˈpejʃ], ⟨mateix⟩ [maˈtejʃ].

Source: Wheeler 2005, §2.5 (diphthong inventory); Moll 2006 and Veny 1982 for the conservative ⟨ix⟩ = [jʃ].

## Other choices

### Unstressed vowels

No reduction. Stressed vowels use seven qualities [a ɛ e i ɔ o u]. Unstressed vowels use five, [a e i o u]: ⟨e⟩ → [e] and ⟨o⟩ → [o]. Never write [ə], and never raise unstressed o to [u]. Examples: ⟨porta⟩ [ˈpɔrta] but ⟨portar⟩ [porˈtar]; ⟨pare⟩ [ˈpare].

Source: Moll 2006; Wheeler 2005 §2.3 (the Western block keeps the unreduced system); Recasens 1996.

### Quality of unaccented stressed e/o

Where Eastern and Western values differ, use the Western/Old-Catalan value: Latin Ē/Ĭ gives [e], not Central [ɛ]. Examples: ⟨cera⟩ [ˈsera], ⟨fred⟩ [ˈfret], ⟨verd⟩ [ˈvert]. Otherwise use the normative dictionary vowel: ⟨terra⟩ [ˈtɛra], ⟨porta⟩ [ˈpɔrta].

Source: Veny 1982 ch. 1; Moll 2006. This departs from Central Catalan as described in Recasens 1993.

### Labials /b/ and /v/

⟨v⟩ = [v] in all positions and never spirantizes: ⟨viure⟩ [ˈviwre], ⟨cava⟩ [ˈkava]. ⟨b⟩ = [b] or [β] by the spirantization rule: ⟨saber⟩ [saˈβer].

Source: Moll 2006; Wheeler 2005 §5.1.

### Palatal affricate and sibilants

⟨j⟩, ⟨g⟩ before e/i, ⟨tj⟩ and ⟨tg⟩ = [dʒ] in all positions: ⟨gent⟩ [ˈdʒent], ⟨menjar⟩ [menˈdʒar], ⟨metge⟩ [ˈmedʒe]. ⟨tx⟩ and word-final ⟨-ig⟩ = [tʃ]: ⟨maig⟩ [ˈmatʃ]. Word-initial ⟨x⟩ and ⟨x⟩ after a consonant = [ʃ]: ⟨xarxa⟩ [ˈʃarʃa]. ⟨ex-⟩ + vowel = [eɡz] (⟨exemple⟩ [eɡˈzemple]); ⟨ex-⟩ + consonant = [eks]. ⟨c⟩ before e/i, ⟨ç⟩, ⟨ss⟩ and non-intervocalic ⟨s⟩ = [s]. Intervocalic ⟨s⟩ and ⟨z⟩ = [z]. ⟨tz⟩ = [dz]. The medieval /ts/ and the apico-alveolar sibilants are not written.

Source: Moll 2006; Wheeler 2005 §5.1; spec notes (medieval affricates deliberately not modelled).

### Rhotics

Write [r] word-initially, after ⟨n l s⟩, for ⟨rr⟩, in codas and word-finally: ⟨rosa⟩ [ˈrɔza], ⟨carn⟩ [ˈkarn], ⟨flor⟩ [ˈflor]. Write [ɾ] for single ⟨r⟩ between vowels and in onset clusters: ⟨cara⟩ [ˈkaɾa], ⟨pobre⟩ [ˈpɔbbɾe]. Final ⟨-r⟩ is always pronounced, including in infinitives and in ⟨-er⟩/⟨-or⟩ endings.

Source: Moll 2006 (final -r pronounced); Wheeler 2005 §5.1 and §10.2.

### Gemination and laterals

⟨ll⟩ = [ʎ] and ⟨ny⟩ = [ɲ]. Write these as geminates: ⟨l·l⟩ and ⟨tl⟩ = [ll] (⟨col·legi⟩ [kolˈlɛdʒi]), ⟨tll⟩ = [ʎʎ], ⟨tm⟩ = [mm], ⟨tn⟩ = [nn]. /b ɡ/ before /l/ geminate and do not spirantize: ⟨poble⟩ [ˈpɔbble], ⟨segle⟩ [ˈseɡɡle]. ⟨h⟩ is silent.

Source: Wheeler 2005 §5.2; spec notes (pre-lateral gemination as pan-Catalan).

### Final-obstruent devoicing inside the word

A word-final obstruent is voiceless in citation form: ⟨fred⟩ [ˈfret], ⟨llarg⟩ [ˈʎark], ⟨cap⟩ [ˈkap]. Before a following word it may revoice only by the sandhi rules under connected_speech.

Source: Wheeler 2005 §5.3; Recasens 1993.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
