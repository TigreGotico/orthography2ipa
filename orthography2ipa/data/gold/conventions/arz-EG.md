# Transcription conventions: Egyptian Arabic (Cairene) (arz-EG)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Write ˈ before the stressed syllable of every word of two or more syllables. Leave monosyllables unmarked (beːt, ʔalb, da). Assign stress on the whole written word, prefixes and suffixes included. Syllable weight: CV is light. CVː and CVC are heavy word-internally. A geminate closes its first syllable (mu.dar.ris). A word-final single consonant does not count, so final CVC is light and final CVː is heavy. Final CVːC and CVCC are superheavy. Apply these steps in order. (1) A final superheavy syllable is stressed: kiˈtaːb, makaˈtabʃ, kaˈtabt. (2) Otherwise a heavy penult is stressed: muˈdarris, ˈbaːbu, ˈhuwwa. (3) Otherwise stress the penult or the antepenult, whichever is separated by an even number of syllables from the nearest preceding heavy syllable, or from the start of the word if there is none: madˈrasa, mudarˈrisa, ʔinˈkasar, ˈkatabit, ˈkatabu. Stress never falls before the antepenult. Feminine nouns of the shape CaCaCa take penult stress as lexicalised: ʃaˈɡara, baˈʔara, ʕaˈʃara. Suffixation moves stress by the same steps: kaˈtabha, kataˈbuːha. Cairene keeps long vowels only in stressed syllables, so write an unstressed native long vowel short: ʃaːf → ʃafˈtu. Write a long vowel short in a non-final closed syllable: ˈʃafha. A word-final vowel is always written short (ʕala, ˈkatabu) and lengthens under stress before a suffix. There are no case endings. Epenthetic vowels are ignored when counting syllables. The spec does not encode stress; this rule follows the published descriptions.

Source: Mitchell 1956, An Introduction to Egyptian Colloquial Arabic, pronunciation/stress chapter; Watson 2002, The Phonology and Morphology of Arabic, ch. 5 (stress) and the treatment of long-vowel shortening; lexical stress of CaCaCa nouns as in Badawi & Hinds 1986.

## Stressed and unstressed words

Proclitics written attached in Arabic script belong to their host's word and are never stressed. These are the article il-, wi- 'and', bi- 'with/in', li- 'to', the imperfective b(i)-, the future ħa- and negative ma-…-ʃ. Stress is computed on the whole word: ilˈbeːt, ħaˈjiktib, maˈʃafʃ. The article assimilates to a following coronal: iʃˈʃams, irˈraːgil, inˈnuːr. It does not assimilate before ɡ, k, ʔ or the other non-coronals: ilˈɡamal, ilˈʔamar. Short separate prepositions and particles fi, min, ʕan, ʕala, ʔinn, ʔilli, ja are unstressed in connected speech. Monosyllables among them are left unmarked anyway. ʕala, ʔilli and ʔinnu get no ˈ when a noun or verb follows. Independent pronouns carry stress: ˈʔana, ˈʔinta, ˈhuwwa, ˈhijja, ˈʔihna, ˈhumma. So do the auxiliary/copula kaːn (ˈkaːnit), the postposed demonstratives da, di, dool, and the question words ˈfeːn, ˈʔeːh, ˈmiːn and ˈizzaj.

Source: Mitchell 1956 (article assimilation, proclitics, negation); Watson 2002, ch. 5 (stress domain includes clitics; negative -ʃ attracting stress, e.g. maˈkatabʃ).

## Pausal forms

Nowhere. Colloquial Cairene has no case endings and no tanwīn, and pause changes nothing. Every word is written in the same form at a sentence end, at a comma or medially. Ta marbūṭa in isolation is -a: madˈrasa, ʕarabiˈjja. Final short vowels are kept: ˈkatabu, ˈʕandaha. Adverbs with a lexicalised -an keep it everywhere: ˈʃukran, ˈʔahlan, ˈʔabadan, ˈtaʔriːban. No other tanwīn is read, even if the script shows it.

Source: Watson 2002 (Cairene lacks case and nunation; ch. on syllable structure); Mitchell 1956; Badawi & Hinds 1986 entries for -an adverbs.

## Connected speech

Write each word in its own place, changed only at its edges. (a) After a vowel-final word, the initial i of the article il- and of other i-initial clitic forms is elided. The next word then begins with the consonant: fi lˈbeːt, ʕala lˈʔardˤ, ja rˈraːgil. Before a consonant-final word or at the start of the utterance, keep the i: min ilˈbeːt. (b) Three consonants are not allowed across a boundary. When a word ends in CC and the next begins with a consonant, write an unstressed epenthetic i at the end of the first word: ˈbinti kwajˈjisa, ʔulti lu. Stress is not recounted for it. (c) In construct (iḍāfa) before a following noun, ta marbūṭa is written -it on the first word: ʕarabiˈjjit ilwalad, madˈrasit ilbanaːt. (d) Do not write cross-word voicing or place assimilation, resyllabification marks or linking symbols. Article assimilation is word-internal and is always written.

Source: Watson 2002, ch. 4 (syllable structure, CCC epenthesis with i inserted after the second consonant) and the description of article elision; Mitchell 1956 (construct -it, helping vowel).

## Glides and diphthongs

Glides are the consonants j and w, and are never written i̯ or u̯. The old diphthongs are monophthongised to the long vowels eː and oː: beːt, joːm, zeːt, loːn. A glide is written only where the lect has a consonant: ˈwalad, ˈjaʔni, ˈhuwwa, ˈhijja, ˈsajjid, ʕarabiˈjja, keˈfaːja. Geminate glides are written double. Remaining aj and aw sequences are written as a plus j or w, e.g. in learned words and before a vowel: ʔaw, ˈʔajjaːm. For و and ي after a consonant letter, follow the spec note. Read them as uː or iː, then oː or eː, then w or j, choosing whichever is the lect's form. Before a final ة, or as the first of two adjacent letters, read them as the glide: ˈbijuːt → buˈjuːt.

Source: Watson 2002 (Cairene monophthongisation aj > eː, aw > oː); Wikipedia 'Egyptian Arabic phonology' letter names (zeːn) and 'Egyptian Arabic' (keˈfæːjæ, written broad as keˈfaːja).

## Other choices

### vowel symbols and emphasis

Short vowels are i a u and long vowels are iː aː uː eː oː. Write a for the front [æ] allophone. Next to or within the spreading domain of tˤ dˤ sˤ zˤ, write a and aː as ɑ and ɑː, as the spec's allophone rule does: ˈsˤɑbaħ, ˈtˤɑːlib, ˈmɑsˤr. Do not mark emphasis on r.

Source: Spec note (AR_EG_EMPH); Watson 2002 on emphasis spread.

### qaf and interdentals

In inherited words ق is ʔ (ʔalb, ʔaˈʔuːl). In learned or Classical words it is q (ilˈqurʔaːn, ʔiqtiˈsˤɑːd). In inherited words ث is t, ذ is d and ظ/ض are dˤ (talaːta, diːb, dˤuhr). In learned words they are s, z and zˤ (sawra, zikr, zˤɑrf).

Source: Badawi & Hinds 1986 lexical reflexes; Watson 2002.

### geminates and r

Write geminates as doubled consonants, never with ː: muˈdarris, ˈʔawwil. Write the rhotic as broad r, with no tap ɾ.

Source: Watson 2002 phonemic inventory.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
