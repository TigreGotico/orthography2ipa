# Transcription conventions: Classical Arabic (arb)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark primary stress with ˈ before the onset of the stressed syllable. Every content word carries exactly one ˈ, including monosyllables. Function words listed under function_words carry none.

Stress domain: the host word together with its enclitic pronouns. Leave out proclitics (wa-, fa-, bi-, li-, ka-, la-, sa-) and the article al-/ʔal-, including an assimilated article. These are written but never stressed.

Syllable weight inside the domain:
- CV is light.
- CVV (long vowel) is heavy.
- CVC is heavy, including the first half of a geminate: ʕal.la.ma.
- CVVC and CVCC are superheavy.

Rule, applied to the form as transcribed in that position:
1. If the final syllable is superheavy, stress it.
2. Otherwise stress the rightmost heavy non-final syllable.
3. If there is none, stress the first syllable of the domain.

A final CV, CVV or CVC is never stressed.

In context, case endings and nunation count as syllables. A superheavy final therefore mostly arises in pausal forms.

Examples:
- context: ˈkataba, ˈmaktabatun, ˈmadrasatun, kiˈtaːbun, jaˈquːlu, ˈʕallama, muˈʕallimun, ˈbajtun, ˈsalmaː
- with clitics: kiˈtaːbuhu, waˈkataba, ʔalˈwaladu, walˈwaladu, ʔaʃˈʃamsu
- pausal: kiˈtaːb, ʔalˈbajt, ˈkatab, kaˈtabt, maˈdiːnah

Source: The Western/philological reconstruction of Classical Arabic stress: Fischer, W. (2002), A Grammar of Classical Arabic, 3rd ed., Yale UP, Phonology chapter, section on stress. It is also summarised as the 'Classical' pattern in Watson (2002, ch. 5, stress). Medieval grammarians (Sībawayhi) do not describe word stress, so this is a modern reconstruction. The Cairene/Egyptian recitation pattern (makˈtabatun, madˈrasatun) is NOT followed.

## Stressed and unstressed words

Unstressed (no ˈ):
- the article al-
- the attached proclitics wa-, fa-, bi-, li-, ka-, la-, sa-
- separate prepositions: fiː, min, ʕan, ʕalaː, ʔilaː, ħattaː, maʕa, munðu, ladaː
- conjunctions and particles: ʔaw, ʔam, θumma, bal, ʔinna, ʔanna, ʔan, ʔin, laːkin, laːkinna, ʔiðaː, law, qad, sawfa, ʔammaː
- the negations laː, lam, lan and negative maː
- the vocative jaː
- relative pronouns: allaðiː, allatiː, allaðiːna
- pronoun suffixes (-hu, -haː, -ka, -kum, -iː, -naː …), which belong to their host's stress domain

Stressed:
- independent pronouns: ˈʔana, ˈhuwa, ˈhija, ˈnaħnu, ʔanˈtum, ˈhum
- demonstratives: ˈhaːðaː, haːˈðihi, ˈðaːlika
- interrogatives: ˈman, ˈmaːðaː, ˈkajfa, ˈʔajna, ˈmataː, and interrogative ˈmaː
- all verbs, including kaːna and lajsa as auxiliaries: ˈkaːna, ˈlajsa
- nouns, adjectives and numerals

Examples: fiː lˈbajti, ʕalaː ˈmaktabin, lam ˈjaktub, ʔinna ˈllaːha, qad ˈkataba, ˈhuwa ˈkaːna.

Source: Fischer (2002), Phonology chapter on stress and the particle chapters. Watson (2002, ch. 5) treats clitics as outside the stress domain. The stressed/unstressed split for particles is a consistency convention built on these, since the sources give no exhaustive list.

## Pausal forms

Where pause applies:
- on the last word of the sentence
- on the last word before any internal punctuation mark (comma, semicolon, colon, question mark, exclamation mark, dash)
- nowhere else

What happens in pause:
1. A final short vowel is dropped, with or without its nunation: -u, -i, -a, -un, -in → zero. Examples: kiˈtaːbun → kiˈtaːb, ˈjaktubu → ˈjaktub, kaˈtabtu → kaˈtabt, kiˈtaːbuka → kiˈtaːbuk, samaːʔun → saˈmaːʔ.
2. Accusative indefinite -an becomes -aː: kiˈtaːban → kiˈtaːbaː, hudan → ˈhudaː.
3. Tāʔ marbūṭa with any ending (-atun, -atin, -atan, -atu, -ati, -ata) becomes -ah: maˈdiːnatun → maˈdiːnah. This departs from the spec note, which gives pre-pausal [a]. The published Classical pausal form is -ah, and this convention writes -ah.
4. Pronoun suffix -hu or -hi becomes -h: kiˈtaːbuhu → kiˈtaːbuh.
5. Defective nouns in -in lose the ending: qaːdˤin → ˈqaːdˤ.
6. Long final vowels stay: ʕalaː, fiː, ˈkatabuː.

Recompute stress on the pausal form; a resulting superheavy final takes the stress.

After a pause, the next word starts afresh. A hamzat al-waṣl word there is pronounced with ʔ and its vowel, as at the start of a sentence.

Source: Wright, W. (1896–98), A Grammar of the Arabic Language, 3rd ed., vol. II, section on pause (waqf). Fischer (2002), section on pausal forms. Watson (2002, ch. 3 and ch. 5) on pausal phonology. The pausal -ah follows Wright and Fischer against the spec note's [a].

## Connected speech

Only the following processes apply. Each one changes the edges of the words it touches, and the words stay separate.

(1) Hamzat al-waṣl elision. Hamzat al-waṣl is found on the article, ibn, ism, imraʔa, imperatives of form I, and perfects, imperatives and verbal nouns of forms VII–X. After any preceding word in the same stretch without a pause, the word loses its initial ʔ and vowel:
- wa ʔalwaladu → wa lˈwaladu
- ˈqaːla ʔuktub → ˈqaːla ˈktub

Word-initially, a sentence-initial or post-pausal waṣl word keeps them: ʔalˈwaladu, ˈʔuktub, ˈʔibnu.

(2) A word-final long vowel shortens before a waṣl-elided word: fiː + ʔalbajti → fi lˈbajti, ʕalaː + ʔalʔardˤi → ʕala lˈʔardˤi.

(3) Helping vowels before a waṣl-elided word:
- A word-final consonant takes -i: lam jakun → lam jaˈkuni lˈladiː…, ʕan → ʕani, qad → qadi.
- The exception is min, which takes -a: mina lˈbajti.
- The pronoun endings -hum, -tum, -kum take -u: ʕalajˈhimu lqiˈtaːlu.
- Nunation becomes -ni: ˈnuːħuni bˈnahu.

(4) The article's l assimilates to a following coronal ('sun letter') everywhere, inside the word: ʔaʃˈʃamsu, wa ʃˈʃamsu, ʔarˈraħmaːnu, ʔadˈdiːnu.

Not written: the tajwīd assimilations of n and nunation across word boundaries (idghām, iqlāb, ikhfāʔ) and nasalisation. Write min ˈrabbihim and min ˈbaʕdi unassimilated.

Resyllabification across the boundary is not marked beyond the above, and there is no linking symbol.

Source: Wright (1896–98), vol. I, on waṣla and helping vowels. Fischer (2002), Phonology chapter on hamzat al-waṣl, auxiliary vowels and the article. Watson (2002, ch. 9) on the assimilation of the article. Tajwīd n-assimilation, described already by Sībawayhi (al-Kitāb, chapters on idghām), belongs to recitation style and is excluded.

## Glides and diphthongs

Write the consonantal glides as j and w, never i̯ u̯. Write the diphthongs as vowel plus glide, never monophthongised:
- bajtun → ˈbajtun
- jawmun → ˈjawmun
- ʕalajhi → ʕaˈlajhi

Long vowels are written iː uː aː, never ij uw: ˈfiːlun, ˈnuːrun. Geminate glides are doubled: ˈsajjidun, ˈquwwatun, ʕaraˈbijjun. A glide between vowels is a consonant: ˈdʒawwun, ʔaˈjaːmun. Wāw and yāʔ used as matres lectionis are written only as the long vowel.

Source: Spec note (7): diphthongs /aj aw/ preserved. Watson (2002, ch. 2, inventory). Fischer (2002), Phonology chapter on diphthongs.

## Other choices

### ض and other contested consonant values

Use these symbols:
- ض = ɮˤ, as the spec states (lateral emphatic): ˈɮˤaraba
- ط = tˤ
- ظ = ðˤ
- ص = sˤ
- ق = q
- ج = dʒ
- ث = θ
- ذ = ð
- ع = ʕ
- ح = ħ
- خ = x
- غ = ɣ
- ء = ʔ, always written, including word-initially: ˈʔakala

Modern [dˤ] for ض, [g] or [ɢ] for ق, and voiced [dˤ] for ط (Sībawayhi's majhūr) are not used.

Source: Spec notes (1)–(4). Sībawayhi, al-Kitāb (chapter on the makhārij). Watson (2002, ch. 2). The reconstructed voiced values of ط and ق are noted in Versteegh (2001, ch. 6) and not adopted.

### Gemination and length

Write geminate consonants as doubled symbols, never with ː: ˈʕallama, muˈħammadun. Write long vowels with ː: aː iː uː.

Source: Watson (2002, ch. 2–3); Fischer (2002), Phonology chapter.

### Emphasis spread

/a aː/ immediately before or after an emphatic consonant (tˤ, sˤ, ðˤ, ɮˤ) inside the same word is written ɑ, ɑː: ˈtˤɑːlibun, ˈsˤɑbrun, ˈɮˤɑraba, ʔalˈʔarɮˤi.

The rule has these limits:
- no further spread
- no backing across word boundaries
- no backing triggered by q, r, x, ɣ
- /i u/ stay unchanged

Source: Davis (1995), as modelled by this spec's AR_EMPHASIS rules. Watson (2002, ch. 10) on emphasis.

### Case endings and nunation in context

In non-pausal position, always write the full iʿrāb vowel and nunation, supplying them by grammar when the text is unvocalised. Examples: ʔalˈwaladu, kiˈtaːbun, fiː lˈbajti. Diptotes take no nunation: ˈʔaħmadu.

Tāʔ marbūṭa in context is -at- plus the case ending: maˈdiːnatun, maˈdiːnati lˈʕilmi.

Source: Spec notes (5), (6) and the tāʔ marbūṭa note. Wright (1896–98), vol. I, declension. Versteegh (2001, ch. 6).

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
