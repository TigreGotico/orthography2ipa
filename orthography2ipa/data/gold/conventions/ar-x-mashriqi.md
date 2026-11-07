# Transcription conventions: Proto-Mashriqi Arabic (ar-x-mashriqi)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

One primary stress per content word, marked with ˈ before the stressed syllable. The rule is the Eastern trochaic, quantity-sensitive rule in its Levantine/'Classical-type' form, applied to the pausal (caseless) form of the word.
(1) A final superheavy syllable (CVVC, CVCC, or CVːC closed by a geminate) takes stress: [kiˈtaːb], [maˈdʒaːl], [ʃaˈrafts].
(2) Otherwise a heavy penult takes stress. A heavy penult is CVV, or CVC including a syllable closed by the first half of a geminate: [ˈbaːb], [ˈmadda], [muˈʕallim], [ˈsaːkin].
(3) Otherwise stress goes on the antepenult: [ˈkatab], [ˈmadrasa], [ˈʃadʒara]. It never goes further left.
Other points:
- Case endings, tanwīn and other word-final short vowels are removed before stress is counted (see pausal_forms), so they never attract or shift stress.
- A word-final open vowel never counts as superheavy: [ˈdunja], [ˈʕala].
- Long vowels are written aː iː uː. Geminates are written as doubled consonants.
- The article and the one-consonant proclitics (wa-, fa-, bi-, li-, ka-, sa-) lie outside the stress domain: [alwaˈlad], [wabiˈlaːd].
- Monosyllabic content words also get ˈ: [ˈbajt].
The Cairene variant (penult stress in [maˈdrasa], [kataˈbitu]) and the iambic leaves (Upper Egypt, Negev) are leaf territory and are not used here.

Source: Watson 2002:9 (Eastern trochaic stress, 'katab vs Western ka'tab, including the fn. 9 caveat on iambic exceptions); Watson 2002, chapter on word stress (Levantine/Classical-type vs Cairene stress algorithms). This is also the standard handbook presentation (Versteegh 2014, ch. 'The Dialects of Arabic', as reported).

## Stressed and unstressed words

Unstressed words get no ˈ mark. These are:
- the article al- and the one-consonant proclitics wa-, fa-, bi-, li-, ka-, sa- (inside their host word);
- the prepositions fi, min, ʕan, ʕala, ʔila, maʕ, ʕind;
- the conjunctions ʔaw, θumma/tumma, ʔan, ʔanna, ʔinna, ʔiða/ʔida, law, bal, lakin;
- the negators la, ma, lam, lan, lajsa;
- the particles qad and sawf;
- the relative allaði/alladi.
Pronoun suffixes never carry their own stress; they only lengthen the host for stress counting: [kiˈtaːbuh].
Stressed words get ˈ. These are:
- independent pronouns: [ˈʔana], [ˈhuwa], [ˈʔanta];
- demonstratives: [ˈhaːda];
- interrogatives: [ˈmaːda], [ˈkajf];
- the verbs kaːn/jakuːn, which are treated as full verbs: [ˈkaːn];
- all nouns, adjectives, verbs and adverbs.

Source: Watson 2002, chapter on word stress (clitics and the article outside the stress domain, e.g. il-'walad type); the general Eastern dialect description as reported for Holes 2004 and Brustad 2000.

## Pausal forms

Every word is written in its pausal (dialect-type) form, wherever it stands in the sentence: at the end, at a comma, or inside a phrase. This follows the Eastern dialects, which lost case and mood endings altogether.
- Any short vowel at the absolute end of the written word is dropped: kitaːbun → [kiˈtaːb], kataba → [ˈkatab], jaktubu → [ˈjaktub], katabtu → [kaˈtabt].
- Tanwīn -un, -in and -an is dropped: [ˈwalad]. The one exception is the adverbial accusative, which the dialects keep as -an: [ˈʃukran], [ˈʔabadan], [ˈdʒiddan].
- Tāʾ marbūṭa is [a]: [ˈmadrasa]. When the word is the first member of a construct (iḍāfa) followed by its genitive, it is [at]: [maˈdiːnat alˈquds].
- Word-final long vowels (alif, alif maqṣūra, final ي/و) are written short: [ˈʕala], [fi], [ˈkatabu]. This departs from the specification note, which reads final ي/و as long. The departure concerns length only, following the dialect descriptions of final-vowel shortening.

Source: Watson 2002:9 and the dialect descriptions there (loss of case; Cairene simīn vs Moroccan smin, citation forms without endings); the specification note on pausal tāʾ marbūṭa; Watson 2002, chapter on syllable structure (final-vowel shortening in Cairene and Levantine).

## Connected speech

Processes inside a word are written:
- Sun-letter assimilation of the article: [aʃˈʃams], [annaːs], [addaˈris].
- Hamzat al-waṣl is written as its vowel with no ʔ: [alˈbajt], [ˈiktib].
One process across a word boundary is written: after a word that ends in a vowel, the a of the article is elided. The vowel-final word stays as it is, and the next word begins with l or the assimilated consonant: [fi lˈbajt], [ˈʕala ʃˈʃaːriʕ]. After a consonant-final word the article keeps its a: [ˈkatab alwaˈlad].
The following are not written: assimilation of place or voice across words, resyllabification, linking consonants, and liaison of tanwīn (none survives). Each word keeps its own segments.

Source: Watson 2002:9 (inherited ʔidġām aš-šamsiyya, as in the specification note); Watson 2002, chapter on phonological processes (article assimilation, elision of the article vowel).

## Glides and diphthongs

The glides are always consonants, written [j] and [w]: [ˈjawm], [walad], [ˈsajjid].
The diphthongs ay and aw are written [aj] and [aw]: [bajt], [ˈlawn]. They are not written as monophthongs. Cairene and urban Levantine [eː] and [oː] are leaf territory.
The onset digraphs يَ and وَ are read as [ja] and [wa].
Non-syllabic diacritics i̯ and u̯ are never used.
Long vowels are [iː] and [uː], not [ij] or [uw]: [kaˈbiːr], [ˈnuːr].

Source: Specification note (onset-glide digraphs يَ/وَ = /ja wa/, inherited from the MSA base); Watson 2002, chapter on phonemes (diphthong monophthongisation as a dialect-specific development).

## Other choices

### qāf ق

Always write [q], the inheritance-root default: [qalb], [alqurˈʔaːn]. The values [ʔ] (urban Mediterranean) and [ɡ] (Bedouin/Sudanic) belong to the leaves and are not used here.

Source: Watson 2002:17 §2.1.9; specification note (a).

### ǧīm ج

Always write [dʒ]: [dʒamal], [ˈdʒiddan]. Not [ɡ], [ɟ] or [ʒ].

Source: Watson 2002:16 §2.1.6; specification note (b).

### interdentals ث ذ ظ

Following the specification's stop-first default (sedentary koine), write ث as [t], ذ as [d] and ظ as [dˤ]: [ˈtalaːta], [ˈhaːda], [ˈdˤuhr]. Fricatives [θ ð ðˤ] are not used. Note that ظ and ض then share [dˤ].

Source: Watson 2002:9 (interdental preservation is a Bedouin, not group-wide, feature); specification note (c).

### ḍād and emphatics

ض is [dˤ] and is never lateral. The emphatics are [tˤ sˤ dˤ], written with ˤ. Vowels next to emphatics are written plainly as a i u, with no backing or [ɑ].

Source: Watson 2002:16 fn.; specification note (3).

### short vowels and hamza

Short vowels [a i u] are kept as written and never deleted. Do not write [e o] or [ə]: [siˈmiːn], [ˈbarra]. Hamza is written [ʔ] wherever the text writes it, including word-initial أ/إ: [ˈʔakal], [ʔiˈsim]. The exception is hamzat al-waṣl, which has no ʔ.

Source: Watson 2002:9 (Eastern retention of the a i u triad); specification note on hamza carriers.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
