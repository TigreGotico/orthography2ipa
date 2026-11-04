# Transcription conventions: Proto-Peninsular Arabic (ar-x-peninsular)

Every pass of `scripts/correct_silver_ipa.py` reads this sheet. Correct it before the run. A change to the text changes the cache key, so the rows of the lect run again.

## Stress

Mark primary stress with ˈ before the stressed syllable. Every stressed word gets one mark, including monosyllabic content words. Do not mark syllable boundaries. Compute stress on the word as it is pronounced in its position. In context, written case vowels, tanwīn, tāʾ marbūṭa + vowel and enclitic pronouns count as syllables. In pausal position, compute stress on the pausal form. Weight: CV is light. CVV and CVC are heavy, and a syllable closed by the first half of a geminate is CVC. CVVC and CVCC are superheavy. Apply this cascade and stop at the first step that fits. (1) A superheavy final syllable takes stress: kiˈtaːb, kaˈtabt, ˈbajt. (2) Otherwise a heavy penult takes stress: kiˈtaːbun, muˈʕallim, kaˈtabtu. (3) Otherwise the antepenult takes stress: ˈkataba, ˈmadrasa, makˈtabatun, kiˈtaːbuhu. (4) In a disyllable with a light penult, stress the penult: ˈwalad, ˈʕalaː, ˈmaʃaː. A final CVV or final CVC is never stressed unless the word is a monosyllable. Proclitics written as part of the word (al-, wa-, fa-, bi-, li-, ka-, sa-) count for syllabification but never take stress. If the cascade lands on one, stress the first syllable of the stem instead: ʔalˈwalad, waˈkataba. Stress shifts with suffixes and with pausal truncation: madˈrasatun in context → ˈmadrasa in pause; kiˈtaːbun → kiˈtaːb. Omani iambic stress is not applied.

Source: Quantity-sensitive trochaic (Eastern) cascade, as declared in the specification. Watson 2002, p.9 (East/West line, short-vowel retention, trochaic stress; fn.9 Omani iambic stress left to the leaf) and Watson 2002 chapter on word stress (Ṣanʿānī and Cairene systems). The three-syllable window and the exclusion of proclitics follow the standard Eastern Arabic stress cascade.

## Stressed and unstressed words

Unstressed, written with no ˈ: prepositions fiː, min, ʕan, ʕalaː, ʔilaː, maʕa, ladaː, ħattaː; conjunctions ʔaw, θumma, ʔam, lakin(na), ʔinna, ʔanna, ʔan, ʔin, ʔiðaː (conditional); relative pronouns allaðiː, allatiː, allaðiːna, maː (relative); particles qad, sawfa, jaː (vocative). Every hyphen-separated clitic is also unstressed, so a hyphen-split article, preposition or pronoun suffix gets no mark. Stressed, written with ˈ: independent pronouns (ˈʔana, ˈhuwa, ˈhija, ˈnaħnu, ˈʔanta); demonstratives (ˈhaːðaː, ˈhaːðihi, ˈðaːlika); interrogatives (ˈmaːðaː, ˈʔajna, ˈkajfa, ˈman); negators (ˈlaː, ˈmaː, ˈlam, ˈlan, ˈlajsa); verbal auxiliaries, which are verbs (ˈkaːna, ˈsˤɑːra, ˈʔasˤbaħa). Attached proclitics and enclitics are part of their host and follow the stress rule above, for example biˈbajtihi. Example: fiː lˈbajti → fi lˈbajti (shortening by the connected-speech rule); ˈhuwa ˈlam ˈjaktub.

Source: Classical/MSA reading tradition for the stress status of particles, as the specification's MSA orthographic base implies; no Peninsular-specific description contradicts it at group level. Watson 2002 treats proclitics and enclitics as inside the phonological word (chapter on word stress).

## Pausal forms

Pausal forms apply at the end of the sentence and before every comma, semicolon, colon, question mark and exclamation mark. They apply nowhere else; inside a phrase every written ḥarakah is pronounced. In pause: (1) drop a final short vowel: kataba → ˈkatab, jaktubu → ˈjaktub; (2) drop tanwīn -un/-in with its vowel: kitaːbun → kiˈtaːb, bajtin → ˈbajt; (3) tanwīn -an becomes -aː: kitaːban → kiˈtaːbaː; (4) tāʾ marbūṭa becomes -a with no h or t: madrasatun → ˈmadrasa; (5) final long vowels and written sukūn stay unchanged: ˈʕalaː, ˈfiː; (6) final hamza stays: samaːʔun → saˈmaːʔ. Recompute stress on the pausal form. In context, ة carrying a written ḥarakah is -at + vowel (madˈrasatun). ة with no ḥarakah is -a in every position, following the specification's pausal tāʾ marbūṭa reading.

Source: Classical/MSA pausal rules (waqf), as in Fischer, A Grammar of Classical Arabic (sections on pause; section numbers not verified). The specification's ORTHOGRAPHIC READING BASE note (pausal tāʾ marbūṭa, MSA leaf ar) supports this. The spoken Peninsular dialects lack case endings altogether, but the input is fully diacritised, so written case vowels are kept in context.

## Connected speech

The words keep their own places; a cross-boundary process changes only the word it affects. (1) Hamzat al-waṣl: after a pause or at the start of a sentence, a waṣl-initial word starts with ʔ plus its vowel (ʔal-, ʔi-, ʔu-). Use the written vowel if there is one; otherwise ʔa- for the article, ʔu- if the stem vowel is u, and ʔi- elsewhere. Examples: ʔalˈbajtu, ʔismuhu → ˈʔismuhu. Inside a phrase, ʔ and its vowel are dropped, and the word starts with the consonant: ˈraʔaː lwalada → see (3). (2) A word-final long vowel directly before a waṣl word is written short: fiː + lbajti → fi lˈbajti; ʕalaː lʔardˤi → ʕala lˈʔardˤi. (3) A consonant-final word (sukūn, tanwīn) before a waṣl word takes a linking vowel. Use the vowel the text writes (min → mina, ʔantum → ʔantumu). If none is written, add -i: kiˈtaːbun lwalad → kiˈtaːbuni lwalad, qad ʔintahaː → qadi ntaˈhaː. (4) The article assimilates to a following sun letter (t θ d ð r z s ʃ sˤ dˤ tˤ ðˤ l n) inside its own word, in every position: ʔaʃˈʃamsu, fi ʃˈʃamsi. ج and the other moon letters do not assimilate: ʔalˈdʒamal. (5) Write no other cross-word process: no nasal or voicing assimilation, no emphasis spreading across a word boundary, no resyllabification marks.

Source: Classical/MSA waṣl and article-assimilation rules, as in Fischer, A Grammar of Classical Arabic (sections on hamzat al-waṣl and the article; section numbers not verified). The ban on cross-word emphasis spread follows Watson 2002, p.279: the domain of spread varies, Qatari crossing word boundaries per Bukshaisha 1985:217-19 but Abha not, so it is left to the leaves.

## Glides and diphthongs

Write glides as consonants j and w, never i̯ u̯ or y. Fatḥa + sukūn-marked ي/و is a diphthong written aj, aw: ˈbajt, ˈjawm, ˈlajl. Do not monophthongize to eː oː; monophthongization is leaf territory. Kasra + ي and ḍamma + و without their own vowel are long vowels iː, uː: ˈkabiːr, ˈjaktubuːn. Onset glides with a written vowel are consonants: ˈwalad, ˈjaktub. Geminate glides are doubled: ʔajˈjaːm, ˈquwwa, ʕaˈlijj (pausal).

Source: Watson 2002, ch.2 (phoneme inventory: /w j/ as consonants, diphthongs as V + glide), and the specification's ORTHOGRAPHIC READING BASE note (onset-glide digraphs يَ/وَ as /ja/, /wa/; word-final ي/و preferring the long-vowel reading). Monophthongization varies across the Gulf, Najdi and Ṣanʿānī leaves (Holes 2006; Ingham 1994), so it is not asserted at group level.

## Other choices

### qāf ق

Write ق as q in every word: ˈqaːla, ˈqalb. The majority Peninsular (Bedouin, Ṣanʿānī) reflex is ɡ (ˈɡaːl), but this node claims no group value. q is the first candidate of the root and is kept by the sedentary western, southern and Omani varieties. Leaves override.

Source: Watson 2002, p.17 (§2.1.9; Behnstedt 1985:41); Al-Balushi 2016, p.88 (Omani ħaqqūti). The specification lists [q, ɡ], and this convention takes the first.

### ǧīm ج

Write ج as dʒ: ˈdʒamal, ˈradʒul. ɟ, ɡ and j are leaf reflexes.

Source: Watson 2002, p.16 (§2.1.6). This follows the first candidate of the specification's list [dʒ, ɡ, j].

### interdentals ث ذ ظ

Write θ, ð, ðˤ: ˈθalaːθa, ˈhaːðaː, ˈðˤɑhr. Do not merge them to stops; the Hejazi merger belongs to its leaf.

Source: Watson 2002, pp.9, 14-15; Ingham 1994; Holes 2006. Omar 1975 gives the Hejazi counter-case.

### ḍād ض

Write ض as dˤ, distinct from ظ ðˤ: ˈdˤɑraba, ˈʔardˤ. Most Peninsular Bedouin varieties merge ض and ظ as ðˤ. That merger is not applied here; the specification lists dˤ as a separate emphatic, and the merger is leaf territory.

Source: The specification's emphatic set /tˤ dˤ sˤ ðˤ zˤ/. The Bedouin ḍ/ẓ merger is reported in the Peninsular literature (Ingham 1994; Holes 2006, as cited).

### emphasis spreading

Back short a to ɑ and long aː to ɑː only when the vowel is immediately adjacent (before or after) to tˤ, dˤ, sˤ, ðˤ or zˤ in the same word: ˈsˤɑbr, ˈtˤɑːlib, ˈrabɑtˤ, ˈdˤɑraba, but ˈmarisˤ is unchanged because i is not low. No whole-word spread, no spread across word boundaries, and q, r, l are not triggers.

Source: Watson 2002, §10.4 pp.273-274 and p.279 (adjacent-only as the group-wide minimum), as declared in the AR_PEN_EMPH_* rules.

### velar k

Write ك as k in all environments: ˈkalb, ˈtʃalb is not used. Gulf tʃ and Najdi ts affrication belong to the subgroups.

Source: Holes 2006 (Gulf), Ingham 1994 (Najdi), both as cited. The specification treats affrication as subgroup territory.

### segmental notation

Write long vowels with ː (aː iː uː). Write geminates as doubled letters (bb, ll), not ː. Write hamza as ʔ wherever it is written, including word-initial hamzat al-qaṭʿ: ʔakala. Write alif madda as ʔaː and alif maqṣūra as aː. Short vowels are a i u with no imāla and no raising of final -a.

Source: The specification's MSA-based grapheme conventions (leaf ar). Watson 2002, ch.2 for the /a i u/ triad retained east of the Salum–Chad line (p.9).

## Word segmentation

The engine splits a text into words at spaces, at hyphens and at punctuation. An apostrophe splits words, as punctuation does. A clitic joined to its host by a hyphen is a word of its own. Each pass gets the words of its text in this split, and writes one IPA word for each word, in the same order, separated by single spaces. A process across a word boundary changes the words on each side of the boundary; it does not join them.
