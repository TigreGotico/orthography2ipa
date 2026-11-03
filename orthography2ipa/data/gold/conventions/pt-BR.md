# Transcription conventions: Brazilian Portuguese (pt-BR)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Primary stress is lexical, and its position follows the orthography. Write ˈ immediately before the stressed syllable of every stressed word, monosyllables included: mar [ˈmaʁ], pé [ˈpɛ], é [ˈɛ]. Do not write secondary stress. Do not write ˈ on the unstressed function words listed under function_words. Placement: (a) a written acute or circumflex accent marks the stressed syllable: café [kaˈfɛ], lâmpada [ˈlɐ̃padɐ], você [voˈse]. (b) Without an accent mark, words ending in -a, -e, -o, -am, -em, -ens, or any of these plus -s, take penultimate stress: casa [ˈkazɐ], gato [ˈɡatu], falam [ˈfalɐ̃w̃], homem [ˈɔmẽj̃]. (c) All other unaccented words take final stress, including words ending in -r, -l, -z, -x, -i, -u, -im, -um, -om, -ão and a falling diphthong: falar [faˈlaʁ], Brasil [bɾaˈziw], aqui [aˈki], irmão [iʁˈmɐ̃w̃], papel [paˈpɛw]. A hyphenated clitic is a separate word and does not move the host's stress: dá-me → [ˈda mi]. Not applicable: Portuguese has no contrastive vowel length, no geminates and no case endings. ⟨ss⟩ and ⟨rr⟩ are digraphs for single consonants: isso [ˈisu], carro [ˈkaʁu]. Never write ː.

Source: Barbosa & Albano 2004: 227–229 (stress marking and examples); Câmara 1970, chapter on stress (acento); Cunha & Cintra 1984, accentuation rules.

## Stressed and unstressed words

Write the following words without ˈ. Use these fixed forms, which apply unstressed-vowel raising. Definite articles: o [u], a [a], os [us], as [as]. Monosyllabic prepositions: de [d͡ʒi], em [ẽj̃], a [a], com [kõ], sem [sẽj̃], por [poʁ]. Preposition–article contractions: do [du], da [da], dos [dus], das [das], no [nu], na [na], nos [nus], nas [nas], ao [aw], à [a], pelo [pelu], pela [pelɐ]. The preposition para [paɾɐ], including written pra [pɾa]. Conjunctions: e [i], ou [o], nem [nẽj̃], mas [mas], se [si]. The complementiser and relative que [ki]. Clitic object pronouns: me [mi], te [t͡ʃi], se [si], lhe [ʎi], nos [nus], vos [vus], o [u], a [a], os [us], as [as], lhes [ʎis]; enclitic -lo [lu], -la [la]. The same clitic forms apply when a hyphen separates the clitic: diga-me → [ˈd͡ʒiɡɐ mi]. Everything else carries ˈ: all verbs, including auxiliaries and copulas (é [ˈɛ], está [isˈta], tem [ˈtẽj̃], vou [ˈvo], foi [ˈfoj]); subject and tonic pronouns (eu [ˈew], ele [ˈeli], você [voˈse], nós [ˈnɔs], mim [ˈmĩ]); indefinite articles (um [ˈũ], uma [ˈumɐ]); não [ˈnɐ̃w̃]; demonstratives, possessives, quantifiers and numerals; disyllabic and longer prepositions and conjunctions other than para, pelo and pela (sobre [ˈsobɾi], como [ˈkomu], quando [ˈkwɐ̃du], porque [poʁˈke]); interrogatives (quê [ˈke], quem [ˈkẽj̃]).

Source: Câmara 1970, on atonic forms (vocábulos átonos/clíticos); Mateus & d'Andrade 2000, chapter 6 (clitics and the prosodic word); Vigário 2003, chapters 4–5 (function words as non-prosodic words, adapted to BP).

## Pausal forms

Not applicable: Portuguese has no pausal forms, case endings or nunation. A word has the same form at a comma, at the end of the sentence and in mid-sentence. Final vowels are not dropped or changed before a pause. The only boundary-sensitive choices are the cross-word rules under connected_speech, and those apply only when another word follows in the same sentence. Before a pause or punctuation, use the citation form: final /s/ is [s] and final /r/ is [ʁ]: (...) mar. → [ˈmaʁ]; (...) mas, → [mas].

Source: Barbosa & Albano 2004 (citation forms); Mateus & d'Andrade 2000, chapter on sandhi.

## Connected speech

Only two consonantal sandhi rules apply. Each word keeps its own slot, and a word changes only at its edge. (1) Word-final sibilant voicing. Final ⟨s, z, x⟩ is written [z] when the next word begins with a vowel or a voiced consonant, and [s] before a voiceless consonant or a pause: os amigos [uz aˈmiɡus], mas nada [maz ˈnadɐ], três casas [ˈtɾes ˈkazɐs], faz isso [ˈfaz ˈisu]. The same voicing applies inside words: mesmo [ˈmezmu], desde [ˈdezd͡ʒi]. (2) Word-final /r/ is written as the tap [ɾ] when the next word begins with a vowel, and as [ʁ] elsewhere: mar azul [ˈmaɾ aˈzuw], falar inglês [faˈlaɾ ĩˈɡles], but falar bem [faˈlaʁ ˈbẽj̃]. Not written: vowel elision, degemination and cross-word gliding. Write casa amarela [ˈkazɐ amaˈɾɛlɐ], not *[ˈkaz amaˈɾɛlɐ], and de agora [d͡ʒi aˈɡɔɾɐ], not *[dʒaˈɡɔɾɐ]. These vowel processes are optional and rate-dependent, and the descriptions do not agree on them. Coda /l/ stays [w] before a vowel: mal assim [ˈmaw aˈsĩ]. Nasal place assimilation is not written across words.

Source: Câmara 1970 (realisation of the archiphonemes /S/ and /R/ in external sandhi); Mateus & d'Andrade 2000, sections on sibilant voicing and external sandhi; Barbosa & Albano 2004: 228–229 (coda sibilants and rhotics).

## Glides and diphthongs

Write non-syllabic vowels as [j] and [w], never i̯ or u̯. Falling oral diphthongs: pai [ˈpaj], meu [ˈmew], céu [ˈsɛw], noite [ˈnojt͡ʃi], foi [ˈfoj], azuis [aˈzujs]. Coda ⟨l⟩ gives [w]: alto [ˈawtu], sol [ˈsɔw]. Nasal diphthongs carry a tilde on both elements: mão [ˈmɐ̃w̃], mãe [ˈmɐ̃j̃], põe [ˈpõj̃], muito [ˈmũj̃tu], and final stressed or unstressed ⟨-em/-ém/-ens⟩ is [ẽj̃]: tem [ˈtẽj̃], também [tɐ̃ˈbẽj̃], homem [ˈɔmẽj̃]. Unstressed final ⟨-am⟩ is [ɐ̃w̃]: falam [ˈfalɐ̃w̃]. Rising sequences: write ⟨qu, gu⟩ + vowel with [w] where the ⟨u⟩ is pronounced: quando [ˈkwɐ̃du], água [ˈaɡwɐ], qual [ˈkwaw]. A post-tonic unstressed ⟨i, u⟩ before a final vowel is a glide: história [isˈtɔɾjɐ], série [ˈsɛɾji], árduo [ˈaʁdwu]. Elsewhere ⟨i, u⟩ next to a vowel are syllabic: piano [piˈɐ̃nu], saúde [saˈud͡ʒi], rio [ˈʁiu]. Diphthong ⟨ou⟩ is written as the monophthong [o]: vou [ˈvo], outro [ˈotɾu], ou [o]. Diphthong ⟨ei⟩ stays [ej] in all positions: beijo [ˈbejʒu], primeiro [pɾiˈmejɾu]. Do not write the glide that is often inserted before final stressed /s/: três [ˈtɾes], mas [mas], nós [ˈnɔs].

Source: Barbosa & Albano 2004: 229–230 (vowels and diphthongs, j/w notation); Câmara 1970 (diphthongs, nasal diphthongs); Callou & Leite 2001 (ou monophthongisation as near-categorical; ei reduction and yod insertion before /s/ as variable).

## Other choices

### Final and unstressed vowels

Word-final unstressed ⟨e, es⟩ is [i, is]; ⟨o, os⟩ is [u, us]; ⟨a, as⟩ is [ɐ, ɐs]: leite [ˈlejt͡ʃi], gatos [ˈɡatus], casa [ˈkazɐ]. The exception is the monosyllabic function words, which keep [a] as listed. Pretonic ⟨e, o⟩ are [e, o], with no vowel-harmony raising: menino [meˈninu], bonito [boˈnitu], perigo [peˈɾiɡu]. Two exceptions: word-initial unstressed ⟨es-, ex-⟩ + consonant is [is]: escola [isˈkɔlɐ], estar [isˈtaʁ]; and ⟨des-⟩ is [d͡ʒis]: desligar [d͡ʒizliˈɡaʁ]. Non-final post-tonic ⟨e, o⟩ keep [e, o]: número [ˈnumeɾu], pérola [ˈpɛɾolɐ]. Stressed mid vowels follow the lexical value, [e o] against [ɛ ɔ]: avó [aˈvɔ], avô [aˈvo]. The final-vowel raising agrees with the specification's rule, and the near-close [ɪ ʊ] are never written.

Source: Câmara 1970 (vowel neutralisation by position); Barbosa & Albano 2004: 229–230; Callou & Leite 2001 (pretonic harmony as variable, hence not written).

### Palatalisation of /t d/

Write /t d/ as [t͡ʃ d͡ʒ], with the tie bar, before every [i]. This covers ⟨i⟩, final raised ⟨e⟩, the epenthetic [i], and the clitic forms de and te: tia [ˈt͡ʃiɐ], dia [ˈd͡ʒiɐ], dente [ˈdẽt͡ʃi], cidade [siˈdad͡ʒi], de [d͡ʒi]. This follows the standard (southeastern and general) pronunciation. The specification leaves affrication before raised final ⟨e⟩ to dialect files, but these conventions write it.

Source: Barbosa & Albano 2004: 228; Câmara 1970 (palatalisation of dentals before [i]).

### Rhotics

Write ⟨rr⟩, word-initial ⟨r⟩, and ⟨r⟩ after ⟨n, l, s⟩ as uvular [ʁ]: carro [ˈkaʁu], rua [ˈʁuɐ], honra [ˈõʁɐ]. Write intervocalic single ⟨r⟩ and ⟨r⟩ in onset clusters as [ɾ]: caro [ˈkaɾu], prato [ˈpɾatu]. Write all coda /r/, word-internal and word-final, infinitives included, as [ʁ], subject to the pre-vocalic tap rule under connected_speech: porta [ˈpɔʁtɐ], mar [ˈmaʁ], falar [faˈlaʁ]. The specification's note lists coda-R loss as an innovation. Infinitival -r deletion is common in speech but is not written, and [h] and [x] are not used.

Source: Barbosa & Albano 2004: 228; Callou & Leite 2001 (coda-R variants).

### Nasal vowels

Write a vowel followed by a coda ⟨m, n⟩ as a nasal vowel, without the nasal consonant: campo [ˈkɐ̃pu], tempo [ˈtẽpu], ponte [ˈpõt͡ʃi], mundo [ˈmũdu], sim [ˈsĩ]. Nasal ⟨a⟩ is [ɐ̃]: lã [ˈlɐ̃], canto [ˈkɐ̃tu]. Write a stressed vowel before an onset ⟨m, n, nh⟩ as nasalised: cama [ˈkɐ̃mɐ], banana [baˈnɐ̃nɐ], tenho [ˈtẽɲu]. Unstressed vowels before onset nasals stay oral.

Source: Barbosa & Albano 2004: 229–230; Câmara 1970 (nasal vowels as V + nasal archiphoneme).

### Palatal consonants and sibilants

⟨nh⟩ is [ɲ]: vinho [ˈviɲu]; the nasal glide [ȷ̃] is not used. ⟨lh⟩ is [ʎ]: filho [ˈfiʎu]. ⟨ch⟩, and ⟨x⟩ where it is palatal, is [ʃ]: chave [ˈʃavi]. ⟨j⟩ and ⟨g⟩ before ⟨e, i⟩ are [ʒ]. Coda sibilants are alveolar [s z], never [ʃ ʒ], as the specification's note states; carioca chiado is not written: festa [ˈfɛstɐ].

Source: Barbosa & Albano 2004: 228 (consonant chart).

### Epenthetic [i] in consonant clusters

Write an epenthetic [i] after a stop or fricative that orthographically closes a syllable (other than ⟨s, r, l⟩ and nasals). Write it also after a word-final consonant in loans: advogado [ad͡ʒivoˈɡadu], ritmo [ˈʁit͡ʃimu], pneu [piˈnew], técnico [ˈtɛkiniku], internet [ĩteʁˈnɛt͡ʃi]. The epenthetic vowel is never stressed and does not affect stress placement.

Source: Câmara 1970 (vowel epenthesis in learned clusters); Mateus & d'Andrade 2000 (syllable structure).

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
