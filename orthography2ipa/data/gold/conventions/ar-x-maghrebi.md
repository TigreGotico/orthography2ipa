# Transcription conventions: Proto-Maghrebi Arabic (ar-x-maghrebi)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark primary stress with ˈ before the stressed syllable on every content word, monosyllables included. Apply the rule to the form left after vowel reduction (see other: short vowels) and after final short vowels, case endings and tanwīn have been dropped. Syllabify with initial clusters as onsets (ktəb = one syllable; mədrsa = məd.rsa). (1) If the final syllable is superheavy (CVːC, or a short vowel closed by two consonants including a geminate), stress it: kbiːr → ˈkbiːr, ʒdiːd → ˈʒdiːd, ħəbb → ˈħəbb. (2) Otherwise stress the penultimate syllable: kətbu → ˈkətbu, mədrsa → ˈmədrsa, ʒaːmʕa → ˈʒaːmʕa. (3) A word with one syllable takes the stress on that syllable: ktəb → ˈktəb. Long vowels count only through rule 1. Geminates count only as word-final codas under rule 1. Case endings never count because they have already been removed. Never place stress further back than the penult. Function words listed as unstressed under function_words get no mark.

Source: Watson 2002, ch. 5 (word stress in Arabic dialects: final superheavy, else penult) as the general dialectal algorithm. Marçais 1977 and Heath 2002 (as reported) describe Maghrebi, and especially Moroccan, stress as weak and largely non-contrastive. This rule is therefore a consistent convention of the transcription, not a claim that stress is phonemic.

## Stressed and unstressed words

Unstressed, with no ˈ mark: the article; the one-consonant proclitics b- 'with/in', l- 'to/for', w- 'and', f- 'and/so' and k- 'like', which are written inside their host word as in the script; the monosyllabic prepositions fi 'in', mən 'from', ʕla 'on', ʕand → ʕnd/ʕənd 'at'; the conjunctions w, aw 'or', bəlli/anna-type complementizers; the negators la and ma; and all suffixed pronouns. Suffixed pronouns stay inside the word, which takes its stress by the normal rule, e.g. ktaːbu → ˈktaːbu. Stressed: independent pronouns (ana → ˈana, huwa → ˈhuwa), demonstratives, the verb kaːn and other auxiliaries, and the negator laysa if present. Forms: the article is l- with no vowel and no ʔ, e.g. lktaːb. Before a sun letter it assimilates to a geminate: aʃʃams → ʃʃəms, annaːs → nnaːs. Proclitics take no vowel: bilqalam → blqləm, wa → w. Free fiː, ʕalaː and minː are written with a short final vowel: fi, ʕla, mən.

Source: Marçais 1977 (Maghrebi article l- and vowelless proclitics, as reported via Watson 2002); Watson 2002 p. 13 (short-vowel deletion producing initial clusters). Sun-letter assimilation is retained exactly as in the inherited MSA reading base, per the spec note.

## Pausal forms

Pausal forms apply everywhere, not only at a comma or at the end of a sentence, because Maghrebi has no case or mood endings. In every position, delete final short vowels, case endings, mood endings and tanwīn: kitaːbun → ktaːb, kataba → ktəb, fii lbayti → fi lbajt. Exceptions are the lexicalised adverbs ʃukran → ʃukran, abadan → ˈabadan, tˤabʕan → ˈtˤabʕan and ajdˤan → ˈajdˤan, which keep -an. Word-final tāʾ marbūṭa is always -a, whatever case vowel the input marks: madrasatun → mədrsa. It becomes -t only before a suffixed pronoun inside the same word: madrasatuhu → mədrəstu. A word-final long vowel is written short: katabuː → kətbu, samaːʔ → sma.

Source: Watson 2002 p. 13 (short-vowel loss) and Marçais 1977 (loss of case and tanwīn throughout Maghrebi), as reported. Final-vowel shortening and -a for tāʾ marbūṭa agree with the spec note's 'pausal tāʾ marbūṭa' reading.

## Connected speech

Write each word in its own place in its isolation form inside the sentence. Do not write any process across a word boundary: no assimilation of voice or place, no elision, no liaison and no resyllabification of a final consonant onto the next word. For example, mən lbiːt stays mən lbiːt, and ktəb ʒwaːb stays ˈktəb ʒwaːb. MSA hamzat al-waṣl does not arise, because the Maghrebi article and proclitics have no vowel to elide. Word-internal processes are written: sun-letter assimilation of the article (ʃʃəms) and assimilation of proclitic l-/b- inside the host as the script attaches them. Do not apply sibilant harmony (z/s→ʒ/ʃ before ʒ, e.g. zuːʒ, not ʒuːʒ) or *ǧ→d dissimilation; these are leaf-level, Moroccan and some Algerian, features.

Source: Spec note (sun-letter assimilation inherited unchanged); Guerrero 2019 §3 and Heath 2002 (as reported) for sibilant harmony and dissimilation as conditioned, non-group-wide shifts, which are kept off this node.

## Glides and diphthongs

Write glides as the consonants j and w, never as i̯ or u̯. يَ and وَ before a vowel are onsets: walad → wləd, jad → jədd. Write Classical diphthongs ay and aw as vowel plus consonantal glide, aj and aw, with no monophthongization at group level: bayt → bajt, yawm → jawm. Monophthongization to iː/uː or eː/oː is leaf territory. Long ī and ū are iː and uː (kbiːr, ʃuːf), not ij or uw. The proclitic w- 'and' stays w even before a cluster.

Source: Spec note (onset-glide digraphs يَ/وَ read /ja/, /wa/, not diphthongs). Marçais 1977 (as reported) for diphthong reflexes differing across Maghrebi: monophthongized in much of Morocco, Algeria and Tunis, retained in Ḥassāniyya and parts of the Tunisian Sahel. They are therefore not asserted group-wide.

## Other choices

### short-vowel reduction

After dropping final short vowels (see pausal_forms), process the remaining Classical short vowels a, i and u from right to left. Delete a short vowel standing in an open syllable, that is, one followed by a single consonant plus a vowel. Write every other short vowel as ə. Examples: kataba → katab → ktəb; katabuː → kətbu; madrasa → mədrsa. Long vowels are never deleted. Clusters of three consonants are legal; insert no epenthetic vowel. Then delete a word-initial ə left by hamza loss.

Source: Watson 2002 p. 13 (Maghrebi unstressed short-vowel deletion, smin vs Cairene simīn); spec note (a/i/u → ə/Ø).

### vowel length

Keep long vowels as aː, iː and uː in non-final position (ktaːb, kbiːr). Do not neutralize length as Moroccan does; that is leaf territory. Do not write imāla: aː stays aː, never eː or ɛː.

Source: Marçais 1977 (length retained in Tunisian, Algerian, Libyan and Ḥassāniyya; Moroccan neutralization), as reported; spec note (imāla is per-leaf).

### hamza

Drop ʔ, departing from the note's bare-/ʔ/ grapheme reading. After a vowel and before a consonant, lengthen the vowel: raʔs → raːs, biʔr → biːr. Between vowels, the hamza becomes a glide or is lost: suʔaːl → swaːl. Word-final hamza is lost: samaːʔ → sma. Word-initially, drop ʔ and let syncope apply: ʔakbar → kbər. The pronoun ʔana → ana is an exception.

Source: Marçais 1977 (general loss of hamza in Maghrebi), as reported. This departs from the spec's MSA-base reading of أ/إ as /ʔ/.

### consonant reflexes

ج → ʒ (never dʒ). ق → q. ث ذ → t d. ظ and ض → dˤ (the sedentary-koiné default of the spec). Emphatics tˤ sˤ dˤ. ڢ → f. Write geminates as doubled symbols (ʃʃəms, mərra), not with ː.

Source: Guerrero 2019 §2.2 and Watson 2002 p. 16 (ʒ); Watson 2002 pp. 15 and 17 with Guerrero 2021 and Souag 2005 (q and stop interdentals as defaults, overridden on leaves); van den Boogert 1989 and the Unicode Arabic chart (ڢ = fāʾ).

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
