# Transcription conventions: Catalan (ca)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark primary stress with ˈ before the stressed syllable of every stressed word, monosyllables included (gos [ˈɡos], pa [ˈpa]). Never mark unstressed function words (see function_words). Place stress as follows. (1) A written accent marks the stressed vowel and always wins (cançó [kənˈso], música [ˈmuzikə], està [əsˈta]). (2) An unaccented word ending in a vowel, vowel+s, -en or -in stresses the penult (casa [ˈkazə], cases [ˈkazəs], parlen [ˈparlən]). (3) Every other unaccented word stresses the last syllable, consonant+s plurals included (cantar [kənˈta], camps [ˈkams]). (4) ⟨ï ü⟩ mark hiatus, not stress (veïna [bəˈinə]). (5) A stressed vowel keeps full quality. In every unstressed syllable, /a e ɛ/ → [ə] and /o ɔ/ → [u], while /i u/ stay as they are (dona [ˈdɔnə], gosset [ɡuˈsɛt]). (6) Adverbs in -ment keep the adjective's stress as secondary stress ˌ with an unreduced vowel (clarament [ˌklaɾəˈmen]). Mark no other secondary stress. (7) A hyphen-split compound is several words, each stressed on its own (vint-i-tres → [ˈbint i ˈtɾɛs]). Catalan has no phonemic vowel length, so write no ː. It has no case endings. On geminates: write ⟨l·l⟩ as [ll] (col·legi [kulˈlɛʒi]). Write ⟨tll tl⟩ as [ʎʎ]/[ll] (ametlla [əˈmeʎʎə]). Write ⟨tz⟩ as [dz] (dotze [ˈdodzə]). Do not write the spontaneous stop gemination before /l/ (poble [ˈpɔblə], with a stop [b], not [β]).

Source: IEC 2016, Gramàtica de la llengua catalana, ch. 3 (l'accent); Wheeler 2005 §3.1 (stress) and §2.3 (Eastern reduction); IEC normative geminate ⟨l·l⟩, cross-checked against Badia i Margarit 1994.

## Stressed and unstressed words

Words on the IEC 'mots àtons' list are unstressed. Write them without ˈ and with reduced vowels. (1) Definite and personal articles: el [əl], la [lə], els [əls], les [ləs], l' [l], en [ən], na [nə]. (2) Contractions: al [əl], del [dəl], pel [pəl], als [əls], dels [dəls], pels [pəls]. (3) Atonic prepositions: a [ə], de [də], d' [d], en [ən], per [pər], amb [əm], des [dəs]. Write amb as [əmb] before a vowel. (4) Conjunctions and relatives: i [i], o [u], ni [ni], que [kə], si [si], relative qui [ki], conjunction com [kum], quan [kwən]. (5) Weak pronouns, proclitic or enclitic: em [əm], et [ət], es [əs], ens [əns], us [us], li [li], ho [u], hi [i], en [ən], el [əl], la [lə], els [əls], les [ləs], m' [m], t' [t], s' [s], n' [n]. Enclitic forms after a hyphen: -lo [lu], -la [lə], -los [lus], -les [ləs], -me [mə], -te [tə], -se [sə], -ne [nə], -nos [nus], -vos [bus], -li [li], -hi [i], -ho [u]. Elided enclitics after an apostrophe: 'l [l], 'm [m], 'n [n], 's [s], 'ns [ns]. Every other word is stressed: (1) the indefinite article and numeral un [ˈun], una [ˈunə]; (2) possessives, el meu [əl ˈmew], la meva [lə ˈmeβə], seu [ˈsew]; (3) strong pronouns, ell [ˈeʎ], jo [ˈʒɔ]; (4) negation no [ˈno]; (5) interrogatives, què [ˈkɛ], qui [ˈki], com [ˈkɔm], quan [ˈkwan], on [ˈɔn]; (6) però [pəˈɾɔ] and perquè [pərˈke]; (7) disyllabic prepositions, sense [ˈsɛnsə]; (8) all forms of haver and ser, he [ˈe], has [ˈas], ha [ˈa], hem [ˈɛm], heu [ˈɛw], han [ˈan], és [ˈes], ser [ˈse]; (9) fer [ˈfe]. Follow the dcvb close-mid vowels in he, meu, meva, teu, teva, seu, ser and fer, as the spec's word_exceptions do. The ipa_childes open-mid forms are not followed.

Source: IEC 2016 §6.2 and the 'mots àtons' list; Wheeler 2005 §2.3 (reduction of atonic words); dcvb headwords he, meu, teu, seu, ser, fer.

## Pausal forms

Not applicable: Catalan has no pausal forms, case endings or nunation. The one pause-sensitive effect is that word-final obstruents are voiceless before a pause or a sentence end (verd [ˈbɛrt], maig [ˈmatʃ], fred [ˈfɾɛt]). A comma is treated like any other word boundary (see connected_speech).

Source: Wheeler 2005 §5.3 (final-obstruent devoicing).

## Connected speech

Write these word-boundary processes. Each change goes on the word it affects, and the words stay separate. (1) Voicing. A word-final sibilant is voiced before a vowel or a voiced consonant: els homes [əlz ˈɔməs], dos dits [ˈdoz ˈðits], s'obre [z ˈɔβɾə]. Other final obstruents are voiced only before a voiced consonant, and are then written as stops: cap dia [ˈkab ˈdiə]. Before a vowel they stay voiceless: tot u [ˈtot ˈu]. Before a voiceless consonant or a pause, every final obstruent is voiceless. (2) Spirantization. /b d ɡ/ are [β ð ɣ] after any vowel or continuant, also across a word boundary: la dona [lə ˈðɔnə], el gos [əl ˈɣos], de vegades [də βəˈɣaðəs]. They stay stops after a pause or a nasal: un gos [uŋ ˈɡos]. /d/ also stays a stop after /l/: el dit [əl ˈdit]. (3) Nasal place assimilation. Word-final /n/ takes the place of the following consonant: en Pere [əm ˈpɛɾə], un camp [uŋ ˈkam], son germà [ˈsoɲ ʒəɾˈma]. The palato-alveolar is written [ɲ]. (4) Final clusters. A word-final stop in -nt, -lt, -mp or -nc is deleted, plural -s included: molt [ˈmol], camps [ˈkams], sants [ˈsans]. It is restored before a vowel-initial word: molt alt [ˈmolt ˈal], vint-i-un [ˈbint i ˈun]. (5) Final ⟨-r⟩ and enclitics. Infinitives and -r suffixes lose final ⟨-r⟩ (see other). An infinitive's r is restored as [ɾ] before a vowel-initial enclitic: fer-ho [ˈfeɾ u], dir-hi [ˈdiɾ i]. It stays silent before a consonant-initial enclitic: donar-li [duˈna li]. (6) Not written: vowel elision, vowel fusion and gliding across words, since these vary with rate. Write each word's full form: la amiga stays [lə əˈmiɣə], and o un stays [u ˈun]. Elisions that the spelling marks with an apostrophe are written as spelled.

Source: Wheeler 2005 §5.2 (spirantization), §5.3 (voicing assimilation), §10.2–§10.5 (final-rhotic loss, cluster simplification, nasal assimilation, phrase-level lenition); Recasens 1993 (nasal assimilation, spirantization, devoicing); Bonet & Lloret 1998 ch. 5 (cross-word vowel contact, which is deliberately not written).

## Glides and diphthongs

Write non-syllabic high vowels as [j w], never as [i̯ u̯]. Falling diphthongs: rei [ˈrɛj], meu [ˈmew], noia [ˈnɔjə], ciutat [sjuˈtat]. Rising diphthongs occur only after ⟨q g⟩ in ⟨qu gu qü gü⟩ + vowel: quatre [ˈkwatɾə], aigua [ˈajɣwə], pingüí [piŋˈɡwi]. Every other vowel+vowel sequence is a hiatus with no glide: piano [piˈanu], veïna [bəˈinə], Lluís [ʎuˈis]. Write the ⟨i⟩ of ⟨ix⟩ as no glide, absorbed into [ʃ] (caixa [ˈkaʃə]). Unstressed vowels before a glide reduce as usual: autor [əwˈto].

Source: Wheeler 2005 §2.5 (diphthong inventory); Wikipedia 'Catalan orthography' for ⟨ix⟩, ⟨qu gu⟩ and the diaeresis.

## Other choices

### stressed mid-vowel aperture

A written accent decides: ⟨è ò⟩ are open [ɛ ɔ], and ⟨é ó⟩ are close [e o] (cafè [kəˈfɛ], cançó [kənˈso]). For an unaccented stressed e/o, use the dcvb Central pronunciation of the word: gos [ˈɡos], tot [ˈtot], dos [ˈdos], molt [ˈmol], but cos [ˈkɔs], pont [ˈpɔn], font [ˈfɔn], tres [ˈtɾɛs]. For a word you cannot look up, write open-mid in the Mascaró contexts: before [l], [r]+coronal, trilled [r], [ɲ], [ŋ], [f] or [sk]; before a pre-stressed suffix; or before an [i]/[j] in the next syllable (premi [ˈpɾɛmi], còpia). ⟨-ent -ment⟩ is close (dent [ˈden]), and ⟨ndr⟩ is open (prendre [ˈpɾɛndɾə]). Elsewhere, fall back on the spec's open-mid prior. Mascaró 2009 §1 finds no general opening tendency outside these contexts, so this prior is only a tie-breaker.

Source: dcvb headwords; Mascaró 2009 ex. (1), (3), §1, §9; Wheeler 2005 §2.3.

### final -r

Delete final ⟨-r⟩ in infinitives and in the suffixes -ar/-er/-or/-dor/-ir, plurals included: cantar [kənˈta], fer [ˈfe], cantadors [kəntəˈðos]. Keep it in lexically listed words such as mar [ˈmar], cor [ˈkɔr], amor [əˈmor], pur [ˈpur] and per [pər]. Write a kept final rhotic as [r], but as [ɾ] before a vowel-initial word or enclitic.

Source: Wheeler 2005 §10.2; Veny 1982.

### rhotics and consonant symbols

Write the trill [r] word-initially, for ⟨rr⟩, and after n, l or s (roda [ˈrɔðə], terra [ˈtɛrə], Enric [ənˈrik]). Write the tap [ɾ] between vowels and in clusters (cara [ˈkaɾə], tres [ˈtɾɛs]). Other symbols: v = b, so [b]/[β] (vi [ˈbi]); ⟨j⟩ and ⟨ge gi⟩ = [ʒ] (jo [ˈʒɔ]); ⟨x⟩ initially and after a consonant = [ʃ]; learned ⟨x⟩ = [ks] (taxi [ˈtaksi]); ⟨ex⟩+vowel = [əɡz] (examen [əɡˈzamən]); ⟨tx⟩ = [tʃ]; ⟨tg tj⟩ = [dʒ] (metge [ˈmedʒə]); final ⟨-ig⟩ = [tʃ]; ⟨ll⟩ = [ʎ]; ⟨ny⟩ = [ɲ]; single intervocalic ⟨s⟩ = [z]; ⟨ss⟩ and ⟨ç⟩ = [s]; ⟨h⟩ is silent. Write /l/ plain [l], not [ɫ], and /s/ plain [s], not [s̺]. Write affricates without a tie bar.

Source: Wheeler 2005 §5.1; Recasens 1996; Wikipedia 'Catalan orthography'; Ladefoged & Maddieson 1996 for the symbols.

### homograph seu

Write seu as the possessive [ˈsew] unless the sentence clearly uses the noun 'cathedral, seat' or the verb form of seure. In those cases write [ˈsɛw]. This corrects, sentence by sentence, the miss that the spec's notes document.

Source: dcvb s.v. seu; spec notes on word_exceptions.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
