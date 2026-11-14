# Transcription conventions: Andalusi Arabic (xaa)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark primary stress with ˈ before the stressed syllable. Mark it on every stressed word, including monosyllabic content words. Write no length marks. Place stress by the first rule that applies. (1) Stress the rightmost vowel that was long in Old Arabic, now written short, unless it stands in a word-final open syllable: kitāb [kiˈteb], kātib [ˈketib], madīna [maˈdina], sīdī [ˈsiði]. (2) Otherwise stress a word-final syllable closed by a consonant or a geminate, as in the Romance-type oxytones: [usˈquf], [qunˈfud], [azzaˈhar], [alandaˈlus], [muˈqasˤsˤ]. (3) Otherwise stress the penult: [ˈbaqra], [andaˈlusi]. Geminates are written doubled. The ˈ goes before the second half of a geminate: [muˈqasˤsˤ], but [ˈʃamma]. Case endings and tanwīn do not exist in this lect (see pausal_forms), so they never count for stress. Where the source shows an anomalous mater lectionis marking stress, that marking overrides rules 1–3. This disagrees with the specification note, whose engine stresses the penult by default regardless of quantity. I follow Corriente's statement that phonemic length was replaced by stress, so that etymological long vowels mark the stressed syllable.

Source: Corriente 2013, ch. 1 (stress); Corriente, Pereira & Vicente 2015: 75–78; Vicente 2020 §3.1.1, pp. 232–234.

## Stressed and unstressed words

Unstressed (no ˈ): the article [al] (assimilated before coronals: [az], [as], [an], [at], [ad], [ar], [aʃ]); monosyllabic prepositions [bi], [li], [fi], [min], [ʕan]; conjunctions [wa], [fa], [an], [in], [aw]; the relative [allaði]; pronoun suffixes or other clitics when the text writes them as separate words ([hu], [ha], [ni], [ki]). Stressed: independent pronouns ([ˈana], [ˈanta], [ˈhu], [ˈhi], [ˈnaħna], [anˈtum], [ˈhum]); negators ([ˈlas], [ˈlam], [ˈma]); disyllabic prepositions and adverbs ([ʕaˈla], [ˈʕand]); and all verbs, including kān used as an auxiliary ([ˈken]).

Source: Corriente 2013, ch. 1 (stress) and the chapters on pronouns and particles; Vicente 2020 §3.1.1.

## Pausal forms

Does not apply as a separate rule. Andalusi Arabic lost case endings, mood vowels and tanwīn, so every word has its pausal-type shape in every position, sentence-internally as well as at commas and sentence end. Never transcribe a case vowel or nunation, even if the source is fully vocalised: al-kitābu [al kiˈteb], baytun [ˈbajt]. Tāʾ marbūṭa is [a] in the absolute state and [at] in the construct state: [maˈdina], [maˈdinat ...]. A lexicalised adverb in -an keeps the [an] only where the source spells it.

Source: Corriente 2013, ch. 1 and the morphology chapters on the loss of iʿrāb; Corriente, Pereira & Vicente 2015.

## Connected speech

Write only one cross-word process: assimilation of the article to a following coronal when the article is a separate word. Write the article as [aC] and leave the noun unchanged: al-zahar → [az zaˈhar], al-šams → [aʃ ˈʃams]. Before non-coronals write [al]: [al ˈqamar]. Write no other process across word boundaries: no elision of the article vowel (hamzat al-waṣl) after a vowel-final word, no nasal assimilation, no resyllabification, no linking marks. Each word keeps its citation shape apart from the article rule.

Source: Corriente 2013, ch. 1 (article and assimilation); Watson 2002 for the sun-letter pattern.

## Glides and diphthongs

Write consonantal glides and diphthong offglides as [j] and [w]. Never use i̯ or u̯. Write the diphthongs /aj aw/ as preserved: [ˈbajt], [ˈmawt], [ˈjawm]. Do not monophthongise them to [e o], even where some sources show sporadic monophthongs.

Source: Corriente 2013, ch. 1 (vowels and diphthongs).

## Other choices

### imāla

Write etymological /aː/ as short [e], except where it is adjacent to an emphatic /tˤ sˤ dˤ ðˤ/, to /q x ɣ ħ ʕ h ʔ/, or to /r/; there it stays [a]: [kiˈteb], [qiˈtel], [ˈbeb], [ˈken], but [ˈtˤalib], [ˈnar], [alˈqadˤi]. Do not write the Granadan strong imāla [i]. Short /a/ stays [a].

Source: Corriente 2013, ch. 1 (imāla); Vicente 2020 §3.1.1; specification note (XAA_IMALA rules).

### vowel length

Write no phonemic length. /aː iː uː/ are written [a/e i u], and their trace is the stress placement only: [maˈdina], [usˈtur].

Source: Corriente 2013, ch. 1; Corriente, Pereira & Vicente 2015: 75–78.

### interdentals, q, ḍ, ǧ

Write /θ ð ðˤ/ as interdentals: [ˈθalaθ], [ˈðahab], [ˈðˤulm]. Write /q/ as [q]. Write ḍ as [dˤ], not as lateral [ɮˤ]: [alˈqadˤi]. Write ǧ as the affricate [dʒ]: [dʒaðˈwal].

Source: Corriente, Pereira & Vicente 2015: 29, 64 via Vicente 2020, p. 228; Corriente 2013, ch. 1.

### spirantisation of d and b

Write /d/ as [d] and /b/ as [b] by default. Write [ð] only in the lexicalised items with attested ð: [ˈsiði], [ħaˈfið], [al ˈħaðð], [dʒaðˈwal]. Never write [β].

Source: Corriente, Pereira & Vicente 2015 via Vicente 2020 §3.1.1.

### hamza

Do not write OA /ʔ/. A word-initial vowel takes no [ʔ], and medial or final hamza is dropped: raʔs [ˈras], biʔr [ˈbir].

Source: Corriente 2013, ch. 1 (loss of hamza).

### s/sˤ and Romance phonemes

Follow the spelling for /s/ versus /sˤ/: sūr [ˈsur], ṣūr [ˈsˤur]. Write the Romance loan phonemes as [p], [g] and [tʃ]: [ˈtʃipp], [tʃiˈqala].

Source: Corriente, Pereira & Vicente 2015: 57; Corriente 1978 via the specification; Vicente 2020.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
