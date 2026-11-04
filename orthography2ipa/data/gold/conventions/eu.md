# Transcription conventions: Basque (Euskara) (eu)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Write no stress marks in any word, including monosyllables, compounds and inflected forms. The spec's stress exemption applies. Basque has no phonemic long vowels or geminates, so neither affects anything. Case endings and the article (-a, -ak, -an, -ari, -arekin) add syllables but never add a mark. Examples: etxea [etʃea], etxeetan [etʃeetan], liburuarekin [liβuɾuaɾekin], gizon [ɡis̻on]. Published descriptions disagree on where Batua stress falls. The central/Gipuzkoan pattern puts it on the second syllable from the left, with lexical exceptions; western varieties have pitch accent; many speakers of the standard use penultimate stress. Euskaltzaindia prescribes none, so this convention does not choose among these traditions.

Source: Spec note (stress exemption). Hualde, J.I. (1999), 'Basque accentuation', in van der Hulst (ed.), Word Prosodic Systems in the Languages of Europe. Hualde in Hualde & Ortiz de Urbina (2003), 'Segmental phonology' and accent sections (pp. 15-65).

## Stressed and unstressed words

There are no weak forms. Basque has no vowel reduction, and no stress is marked (see stress). Every function word is written in its full citation form, whether stressed or not. This covers the following: auxiliaries: da [da], dut [dut], dira [diɾa], zen [s̻en], naiz [nai̯s̻]. Conjunctions: eta [eta] (never colloquial [ta]), edo [eðo], baina [bai̯na], ala [ala]. Pronouns: ni [ni], zu [s̻u], hura [uɾa]. Particles: ere [eɾe], ba- inside bada [baða], ez [es̻]. Articles, postpositions and case markers are suffixes inside the word. The only changes to function words are the cross-word processes under connected_speech: the ez-sandhi, spirantisation and nasal assimilation.

Source: Hualde in Hualde & Ortiz de Urbina (2003), 'Segmental phonology' (pp. 15-65): five full vowels and no reduction. Hualde, Lujanbio & Zubiri (2010: 122).

## Pausal forms

Does not apply. Basque has no pausal forms, case-ending loss or nunation. A word has the same form at the end of a sentence, at a comma and inside the phrase. There is no final devoicing or vowel loss: eder [eder], etxea [etʃea], dago [daɣo]. The only effect of a pause is on the next word: a voiced stop after a pause stays a stop (see connected_speech).

Source: Hualde in Hualde & Ortiz de Urbina (2003), 'Segmental phonology' (pp. 15-65).

## Connected speech

Each word is written in its own slot, and the processes below change the segments at the edges of the words. (1) SPIRANTISATION, inside words and across word boundaries. /b d ɡ/ are written [b d ɡ] in these positions: at the start of the sentence; after a pause punctuation mark (comma, semicolon, colon, dash, parenthesis, ellipsis, quote); after a nasal; and, for /d/ only, after /l/. Everywhere else they are written [β ð ɣ]: after vowels, glides, r, sibilants and other consonants. A hyphen or apostrophe is not a pause. Examples: gabe [ɡaβe], ardo [arðo], aldi [aldi], mendi berde [mendi βerðe], etxe bat [etʃe βat], ur gaziа [ur ɣas̻ia], Gaur dator [ɡau̯r ðatoɾ]. This rule is broader than the note's 'intervocalically'. (2) NEGATIVE ez SANDHI, applied every time. ez + d → [es̻ t]: ez dut [es̻ tut]. ez + g → [es̻ k]: ez gara [es̻ kaɾa]. ez + b → [es̻ p]: ez bada [es̻ paða]. ez + z → [e ts̻]: ez zen [e ts̻en]. ez + s → [e ts̺]: ez sinetsi [e ts̺inets̺i]. ez + x → [e tʃ]: ez xamar [e tʃamar]. ez + n → [e n]: ez naiz [e nai̯s̻]. ez + l → [e l]: ez luke [e luke]. In the [e ...] cases ez loses its sibilant, and any affricate is written at the start of the next word. Before a vowel or any other consonant, ez is [es̻]. Do not extend this devoicing to other sibilant-final words: gauza bat [ɡau̯s̻a βat], ikus dezagun [ikus̺ ðes̻aɣun]. (3) NASAL ASSIMILATION. Word-final /n/ before a word beginning with /b p m/ is written [m], and the following /b/ stays a stop: gizon bat [ɡis̻om bat], egin behar [eɣim bear], gizon polita [ɡis̻om polita]. Other place assimilations ([ŋ], [ɱ], dental) are not written. (4) NOT WRITTEN: vowel elision, glide formation between words, resyllabification and liaison. Etxe ederra stays [etʃe eðera]. Ni eta zu stays [ni eta s̻u]. A word-final r keeps its trill before a vowel: ur asko [ur as̺ko].

Source: Spirantisation: Hualde in Hualde & Ortiz de Urbina (2003), 'Segmental phonology' (pp. 15-65), and Hualde, Lujanbio & Zubiri (2010: 116). ez-sandhi: Hualde (1991), Basque Phonology, chapter on the negative particle ez. Nasal assimilation: Hualde, Lujanbio & Zubiri (2010: 120).

## Glides and diphthongs

The falling diphthongs ⟨ai ei oi ui au eu⟩ are written with non-syllabic [i̯ u̯], never [j w]. This holds before a vowel too. Examples: aita [ai̯ta], hau [au̯], euskara [eu̯s̺kaɾa], oinez [oi̯nes̻], gaua [ɡau̯a], lehoia [leoi̯a]. Vowel sequences beginning with i or u (ia, ie, io, ua, ue, ea, oa) are written as two full vowels in hiatus: hiria [iɾia], familia [familia], liburua [liβuɾua], etxea [etʃea]. Vowels separated by spelled ⟨h⟩ are also written as full vowels: ahuntz [aunts̻], mahai [maai̯]. ⟨j⟩ is a consonant, not a glide (see other). The ⟨i⟩ in palatal spellings is a vowel: Iñaki [iɲaki].

Source: Spec note on tautosyllabic falling diphthongs. Hualde in Hualde & Ortiz de Urbina (2003), 'Segmental phonology' (pp. 15-65), on diphthongs and hiatus.

## Other choices

### sibilants and affricates

Keep the three-way contrast and write the affricates without a tie bar. ⟨z⟩ [s̻], ⟨s⟩ [s̺], ⟨x⟩ [ʃ], ⟨tz⟩ [ts̻], ⟨ts⟩ [ts̺], ⟨tx⟩ [tʃ]. Examples: zu [s̻u], su [s̺u], xume [ʃume], hotz [ots̻], hots [ots̺], txakur [tʃakur]. Many western speakers merge these to apical sibilants, but that merger is not written.

Source: Hualde, Lujanbio & Zubiri (2010: 119). Euskaltzaindia (1998), Arau 87 'Euskara batuaren ahoskera zaindua'. Merger described in Bedialauneta & Hualde (2023: 1098).

### h and aspiration

⟨h⟩ is silent and not written, following the majority southern/western pronunciation of Batua: hau [au̯], behar [bear], hiru [iɾu], Euskal Herria [eu̯s̺kal eria]. No aspirated stops are written.

Source: Hualde (2018: 1-3), on the loss of aspiration outside the eastern dialects. Euskaltzaindia (1998), Arau 87, which permits omitting h.

### j

⟨j⟩ is written as [x] throughout, following the most widespread southern Batua realisation: jan [xan], jende [xende], Jon [xon], joan [xoan]. The [j], [ʝ] and [ʃ] variants are not used.

Source: Hualde in Hualde & Ortiz de Urbina (2003), 'Segmental phonology' (pp. 15-65), on the dialectal realisations of j.

### rhotics

Single ⟨r⟩ is written as the tap [ɾ] intervocalically and after an obstruent: liburua [liβuɾua], gure [ɡuɾe], fruta [fɾuta]. It is written as the trill [r] in the coda, word-finally and before a consonant: eder [eder], gaur [ɡau̯r], korpus [korpus̺], berde [berðe]. It is also [r] word-initially in loans. ⟨rr⟩ is always [r]: herria [eria], zakurra [s̻akura].

Source: Spec note. Hualde in Hualde & Ortiz de Urbina (2003), 'Segmental phonology' (pp. 15-65).

### palatals

Write palatals only where they are spelled: ⟨ñ⟩ [ɲ] (andereño [andeɾeɲo]), ⟨ll⟩ [ʎ], ⟨tt⟩ [c] (pottoka [pocoka]), ⟨dd⟩ [ɟ]. Palatal stops are not spirantised. Plain ⟨n l⟩ after /i/ stay [n l] in every word: mutila [mutila], mina [mina], familia [familia], kilometro [kilometɾo]. This is because palatalisation after /i/ is lexical and variable in Batua.

Source: Spec note. Hualde in Hualde & Ortiz de Urbina (2003), §2.3.

### stops and other consonants

/t d/ are written without a dental diacritic. ⟨k⟩ [k], ⟨g⟩ [ɡ], ⟨f⟩ [f], ⟨v⟩ in loans [b]. Word-internal coda /n/ before a labial is written [m]: anbulantzia [ambulants̻ia], ganbara [ɡambaɾa].

Source: Hualde, Lujanbio & Zubiri (2010: 116, 120). Spec note.

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
