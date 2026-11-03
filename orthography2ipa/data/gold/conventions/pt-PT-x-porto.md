# Transcription conventions: Portuense Portuguese (pt-PT-x-porto)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark primary stress with ˈ before the stressed syllable of every stressed word, monosyllables included: [ˈpjɛ] pé, [ˈkɐ̃j] cão? no — write [ˈkɐ̃w] cão. Do not mark secondary stress. Stress is lexical and follows the spelling. A written acute, circumflex or grave accent (á é í ó ú â ê ô) marks the stressed syllable. If the word has no accent, stress the penult when it ends in a, e, o, am, em or ens, with or without -s: [ˈkɐzɐ] casa, [ˈfalɐ̃w] falam. Otherwise stress the final syllable, as in words ending in i, u, l, r, z, im, um, om, ã, ão, or a diphthong: [ʒuˈbaɫ] jovial, [fɐˈlaɾ] falar, [ɐˈʃi] aqui. Place ˈ before the onset of the stressed syllable, including any onglide produced by the Porto diphthongisation rule: [ˈtwɔkɨ] toque, [ˈs̺jedu] cedo. Portuguese has no phonemic long vowels, no geminates and no case endings, so those parts of the topic do not apply. Spelled double consonants are single sounds: ss is [s̺] and rr is [ʁ].

Source: Mateus & d'Andrade 2000, The Phonology of Portuguese, ch. 6 (word stress); the stress marking follows the specification's notes.

## Stressed and unstressed words

The following words are unstressed and get no ˈ. Their vowels reduce, and they are never diphthongised. Definite articles: o [u], a [ɐ], os [uʃ], as [ɐʃ]. Simple prepositions and preposition+article contractions: de [dɨ], em [ẽj], a [ɐ], por [puɾ], para [pɐɾɐ], com [kõ], sem [s̺ẽj], do [du], da [dɐ], no [nu], na [nɐ], ao [aw], à [a], pelo [pɨlu]. Conjunctions and the complementiser/relative: e [i], que [kɨ], se [s̺ɨ], mas [mɐʃ], nem [nẽj], ou [ow]. Object and reflexive clitics, including hyphenated ones, which are still separate words: me [mɨ], te [tɨ], se [s̺ɨ], lhe [ʎɨ], o [u], a [ɐ], nos [nuʃ], vos [buʃ], lhes [ʎɨʃ]. For example, dá-me is [ˈda mɨ]. The following words are stressed. Subject and tonic pronouns: eu [ˈew], tu [ˈtu], ele [ˈjelɨ], nós [ˈnwɔʃ], mim [ˈmĩ]. Indefinite articles: um [ˈũ], uma [ˈumɐ]. Demonstratives, possessives, numerals, the negator não [ˈnɐ̃w] and interrogatives. All verb forms, auxiliaries included: é [ˈjɛ], está [ɨʃˈta], foi [ˈfoj], tem [ˈtẽj], vai [ˈbaj], há [ˈa]. The Porto prothetic glide in eu (ieu) is not written.

Source: Mateus & d'Andrade 2000, ch. 6–7 (clitics and stressless function words in EP); stressed-word diphthongisation per Brissos 2018, pp. 196–201.

## Pausal forms

Not applicable: Portuguese has no pausal forms, case endings or nunation. Write each word the same way before a pause, at a comma and sentence-internally. Final unstressed vowels keep their reduced citation values at the end of a sentence too: [ɨ] in [ˈnwɔjtɨ] noite, [u] in [ˈgatu] gato, [ɐ] in [ˈkɐzɐ] casa. Do not delete final [ɨ]. Do not add the Porto paragogic -a. The only pause-sensitive item is word-final /s/, which is [ʃ] before a pause; see connected_speech.

Source: Mateus & d'Andrade 2000, ch. 2–3 (EP vowel reduction); Porto paragoge left unwritten per the specification's notes (pwl_porto).

## Connected speech

Apply exactly one cross-word process: coda-/s/ sandhi, written on the first word only. Word-final s, z or x is [ʃ] before a pause or a voiceless consonant: [uʃ ˈpjɛʃ] os pés. It is [ʒ] before a voiced consonant: [uʒ ˈdedwuʃ]? no — write [ɐʒ ˈmɐ̃jʃ] as mães. It is [z] (plain alveolar) before a vowel-initial word: [uz ˈwɔʎuʃ] os olhos, [mɐz ˈjɛ] mas é. Nothing else is written across boundaries. Do not elide vowels: de a is [dɨ ɐ], and que é is [kɨ ˈjɛ]. Do not merge vowels or insert glides. Word-final r stays [ɾ] and word-final l stays [ɫ] even before a vowel: [fɐˈlaɾ ɐ] falar a, [ˈmaɫ ɐ] mal a. Do not write lenition of b, d, g to [β ð ɣ]. Each word stays in its own slot.

Source: Mateus & d'Andrade 2000, ch. 3 (coda sibilant voicing and place across word boundaries), inherited unchanged by Porto per the specification's notes.

## Glides and diphthongs

Write glides as the plain consonant symbols j and w, never i̯ or u̯, both as onglides and as offglides. This covers the Porto tonic diphthongisation, written onglide + vowel: [ˈpjɛ] pé, [ˈtwɔkɨ] toque, [ˈs̺jedu] cedo, [ˈpwoɾtu] Porto. It covers the preserved diphthongs: ou [ow] in [ˈow̃]? no — [ˈowɾu] ouro, ei [ej] in [ˈlejtɨ] leite, and oi [oj] in [ˈkojz̺ɐ]? no — [ˈkojs̺ɐ]? write coisa as [ˈkojz̺ɐ]. Other falling diphthongs: [aj] [ɛw] [iw] [uj] [ɔj]. In nasal diphthongs, mark nasality on the vowel only: [ˈmɐ̃w] mão, [ˈtẽj] tem, [ˈpõjʃ] põe. Write an unstressed i or u next to another vowel in the same word as a glide: [iʃˈtwɔɾjɐ] história, [ˈkwɐ̃du] quando. Do not write the toward-central RD2 subtype [eɐ̯ ɔɐ̯]. Do not write the /i/→[ej] variant (maquia).

Source: Cintra 1971 (je/wo notation); Brissos 2018, pp. 196–201 (RD1 within-axis subtype adopted, written here with j w instead of his i̯ u̯).

## Other choices

### Tonic mid-vowel diphthongisation scope

Diphthongise every stressed oral monophthong e, ɛ, o, ɔ in a stressed word, as [je jɛ wo wɔ]: [ˈbjɛʎu] velho? no — velho has close e, so write [ˈbjeʎu]; café is [kɐˈfjɛ], avó is [ɐˈbwɔ], só is [ˈs̺wɔ], três is [ˈtɾjeʃ]. Do not diphthongise nasal vowels, vowels already inside a diphthong (ei, ou, oi, éu), unstressed vowels, or the cardinal vowels a, i, u. This follows Brissos rather than Cintra, who limits the rule to the close mids.

Source: Brissos 2018, pp. 196–201; Brissos & Rodrigues 2016; Cintra 1971 (close mids only) not followed on scope.

### Open vs close quality of unaccented tonic e/o

Use the lexical quality of the standard pronunciation, not a default open vowel: cedo is [ˈs̺jedu], medo is [ˈmjedu], Porto is [ˈpwoɾtu], but pé is [ˈpjɛ] and toque is [ˈtwɔkɨ]. This disagrees with the note's inherited open default, which the note itself flags as a limit.

Source: Mateus & d'Andrade 2000, ch. 2 (lexical mid-vowel quality); the specification's notes, limit (b).

### Betacism

Write both v and b as [b] in every position, as a broad symbol with no [β]: vaca is [ˈbakɐ], vinho is [ˈbiɲu], vos is [buʃ].

Source: Cintra 1971, feature 1; Segura 2013.

### Diphthong preservation and pre-palatal e

Write ou as [ow] and ei as [ej], where Lisbon has [o] and [ɐj]. In line with this, write no Lisbon-type centralisation before palatals or in -em: tem is [ˈtẽj], bem is [ˈbẽj], em is [ẽj], and lenha is [ˈljeɲɐ] rather than [ˈlɐɲɐ].

Source: Cintra 1971, feature 4; Segura 2013 (Lisbon centralisation as a southern-standard trait).

### Onset sibilants

Write every onset /s z/ as apico-alveolar [s̺ z̺], whether spelled s, ss, ç, c(e,i), z or intervocalic s: passo and paço are both [ˈpas̺u], casa is [ˈkaz̺ɐ], cedo is [ˈs̺jedu]. This disagrees with the note, which applies the apical to ss only; Cintra places Porto in the zone with only apico-alveolar sibilants. Coda sibilants stay [ʃ ʒ], and [ʂ ʐ] are not written.

Source: Cintra 1971, feature 2 (CVC reprint, pp. 11–13).

### Strong rhotic and unstressed vowels

Write word-initial r and rr as [ʁ], and the [r] trill variant is not written: rato is [ˈʁatu]. Write single r elsewhere as [ɾ]. Write unstressed vowels with the inherited EP reduction: a is [ɐ], e is [ɨ] (but [i] word-initially before s and for the conjunction e), and o is [u]. The more open Porto pretonic vowels are not written.

Source: Mateus & d'Andrade 2000, ch. 2–3; inherited per the specification's notes.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
