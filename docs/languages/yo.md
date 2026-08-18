# Yoruba: Phonology Reference

**Code**: `yo` | **Family**: Niger-Congo > Volta-Niger (Defoid) | **Script**: Latin (alphabet) | **Quality tier**: research

Yoruba is the rare tonal language whose orthography is *good to a phonemizer*. Tone is written on the vowel, vowel nasalisation is written with a following ⟨n⟩, and the two vowel qualities that a bare Latin alphabet cannot distinguish get a subdot. Almost everything a phonemic transcription needs is on the page, so the `yo` spec reads it rather than declaring it unrecoverable.

## Segments

The seven oral vowels /i e ɛ a ɔ o u/ are written ⟨i e ẹ a ọ o u⟩ and the two subdot letters ⟨ẹ ọ⟩ are the open-mid pair. ⟨ṣ⟩ is /ʃ/. The two labial-velar stops are written ⟨p⟩ = /k͡p/ and ⟨gb⟩ = /ɡ͡b/ — Yoruba has no plain /p/, so the letter ⟨p⟩ is free to carry the doubly-articulated stop. ⟨j⟩ is transcribed /dʒ/ here; the same segment is analysed as a palatal stop /ɟ/ in part of the literature, and the choice is a notation preference rather than a claim about the language. ⟨r⟩ is an alveolar tap [ɾ], not a trill (Akinlabi 2004; Bamgboṣe 1966).

## Tone

Yoruba has three level tones: high, mid and low. The orthography writes high with an acute, low with a grave, and mid with nothing at all. The spec emits all three, mid included, with the IPA level-tone diacritics ◌́ ◌̄ ◌̀.

Marking mid explicitly is the point worth spelling out. Mid is a specified tone in Yoruba, not the absence of one, and leaving unmarked vowels bare would quietly claim that a word like ⟨ọkọ⟩ "hoe" has no tone. It also collapses the classic minimal triple — ⟨ọkọ⟩ /ɔ̄kɔ̄/ "hoe", ⟨ọkọ̀⟩ /ɔ̄kɔ̀/ "vehicle", ⟨ọ̀kọ̀⟩ /ɔ̀kɔ̀/ "spear" — into one string. The spec keeps the three distinct.

## Nasal vowels

Yoruba has five nasal vowels /ĩ ɛ̃ ã ɔ̃ ũ/, written ⟨in ẹn an ọn un⟩. There are no nasal counterparts of /e/ and /o/, and that gap is directly visible in the orthography: ⟨en⟩ and ⟨on⟩ are *not* nasal-vowel spellings, and the spec leaves their ⟨n⟩ standing as a consonant.

The rule the spec applies is that an ⟨n⟩ following one of the five nasalisable vowels, and not itself followed by a vowel, spells nasalisation of that vowel and is not a segment of its own. So ⟨Abiọdun⟩ is /ābīɔ̄dũ̄/ with no final /n/. Before a vowel the same letter is an ordinary onset, which is why ⟨ana⟩ is /ānā/ and not */ãā/; the spec expresses that with a `before_vowel` positional override on each nasal digraph rather than by hoping a longest-match tokenizer gets it right.

Notation order matters here. The nasalisation tilde is written before the tone mark, so that u + tilde + acute composes to the standard ṹ rather than to a string that merely looks the same.

## What is deliberately not modelled

The syllabic nasal written ⟨n⟩ before a consonant (⟨nkọ⟩, ⟨njẹ⟩) is left as /n/. Its place of articulation is analysis-dependent — homorganic assimilation in the reference grammars, a flat [ŋ] in the transcription tradition the benchmark gold follows — and the gold itself is split for medial ⟨Vn⟩ + consonant, reading it as a nasal vowel in 367 tokens and as a syllabic [ŋ] in 148. The majority reading is what the nasal-vowel rule already produces, so the spec keeps it and does not add a rule it cannot source cleanly.

Vowel nasalisation *after* ⟨m⟩ and ⟨n⟩ — the allophony that treats [m] and [n] as the pre-nasal realisations of /b/ and /l/ — is not applied either. It holds for about two thirds of such vowels in the gold (347 of 528 after ⟨m⟩, 305 of 388 after ⟨n⟩), and the remainder are largely loanwords whose oral vowels the spec would then get wrong. Encoding the rule at that hit rate would be fitting the benchmark, not describing the language.

## Benchmark rows read two different conventions

Yoruba carries two gold rows and they disagree about what a Yoruba transcription contains.

The **wikipron** row (`yor_latn_broad`) is crowd-scraped from Wiktionary and is fully tone-marked and fully nasal-marked, which is why it rewards a spec that emits both. Its orthographic column, however, is almost entirely *untoned*: only 32 of 4937 rows (0.65%) carry a tone diacritic on the headword. Tone is therefore recoverable in Yoruba but not recoverable *from this gold's input*, and every high or low vowel in it is a floor the spec cannot reach — it reads an unmarked vowel as mid, correctly, and the gold says high or low. That floor is most of the row's remaining error.

The **vox_communis** row is epitran-derived. Its orthography is real, fully accented Yoruba, but its phone column has no tone at all and handles nasal vowels inconsistently, because that is what epitran produces. It measures agreement with epitran, not accuracy, so emitting tone necessarily moves it a long way. Rank Yoruba on the wikipron row.
