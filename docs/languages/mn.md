# Mongolian (Khalkha, Cyrillic script) — `mn`

The `mn` spec describes Khalkha Mongolian as written in the Cyrillic
orthography used in Mongolia since the 1940s. It is not the Traditional
Mongolian script, which the library does not cover under this tag. The
description follows Svantesson (2003), "Khalkha", in Janhunen (ed.)
*The Mongolic Languages*, which is the spec's `sources` entry.

Khalkha has no voiced obstruents. The laryngeal contrast is strong
(aspirated) against weak (plain voiceless unaspirated), so ⟨п т ц ч к⟩ are
[pʰ tʰ tsʰ tɕʰ kʰ] and ⟨б д з ж⟩ are [p t ts tɕ]. The one exception is the
weak velar ⟨г⟩, which is functionally voiced [ɡ], voiceless [k] word-finally
and before a voiceless consonant, and often fricative [ɣ] between vowels.
⟨л⟩ is a lateral fricative [ɮ] and ⟨ш⟩ an alveopalatal [ɕ]. Word-final ⟨н⟩
is /ŋ/, because the orthography writes a following vowel letter exactly when
the nasal is alveolar: ⟨хан⟩ [xaŋ] "king" against ⟨хана⟩ [xan] "wall".

The seven vowels carry pharyngeal (ATR) harmony. The historically back
rounded ⟨о у⟩ are pharyngealized [ɔ ʊ], the historically front rounded
⟨ө ү⟩ are centralized [ɵ u], and ⟨и⟩ is neutral. Long vowels are written
double, the four diphthongs in -i are written with ⟨й⟩, ⟨ий⟩ writes long
/iː/, and the historical diphthong ⟨эй⟩ has merged with /eː/. The iotated
letters ⟨е ё ю я⟩ write a glide word-initially and after a vowel but
palatalization of the preceding consonant after one, ⟨е⟩ standing in for
iotated ö and so spelling /jɵ/. An iotated letter followed by its matching
plain vowel letter — ⟨яа ёо юу юү еэ⟩ — writes one LONG nucleus, exactly as
a doubled plain vowel does: ⟨юу⟩ is [jʊː] and ⟨юү⟩ [juː], the second letter
stating length and which side of the harmony the nucleus sits on.

Both signs are palatalization of the preceding consonant: ⟨хорь⟩ [xɔrʲ],
⟨арьс⟩ [arʲs]. Before one of ⟨е ё ю я⟩ they are instead the separating signs
of the Russian-derived spelling, marking a syllable break that the iotated
letter's own glide fills, and they contribute no segment: ⟨объект⟩
[ɔpjɵkʰtʰ], ⟨томьёо⟩ [tʰɔmjɔː], ⟨харьяалах⟩ [xarjaːɮax]. Svantesson (2003)
does not treat the separating spellings, which occur in Russian loans; the
reading is taken from the WikiPron `mon_cyrl_broad` gold. Across the gold's
3563 entries, 38 words spell ⟨ь⟩ or ⟨ъ⟩ immediately before an iotated
letter: 35 show a bare glide with no palatalization mark, one is palatalized
(⟨харьяа⟩ [xarʲjaː], contradicted by its own derivative ⟨харьяалах⟩
[xarjaːɮax]), and two spell only a long vowel with no glide at all
(⟨идье⟩ [itiː], ⟨оръё⟩ [ɔriː] — both voluntative forms; the spec predicts
[itjɵ] and [ɔrjɔ] for these two, a known divergence). ⟨ь⟩ and ⟨ъ⟩ alternate
freely in this position: the gold spells four words both ways with an
identical transcription — ⟨объект⟩/⟨обьект⟩ both [ɔpjɵkʰtʰ], ⟨овъёос⟩/
⟨овьёос⟩ both [ɔw̜jɔːs], ⟨авъяас⟩/⟨авьяас⟩ both [aw̜jaːs], ⟨Пёнъян⟩/⟨Пёньян⟩
both [pʰʲɔnjaŋ] — evidence that the sign here is a harmony-conditioned
allograph rather than the Russian hard/soft contrast. The analysis holds on
⟨ь⟩ alone, without needing ⟨ъ⟩: of the 11 words that spell ⟨ь⟩ before an
iotated letter, 9 show the bare glide, 1 is palatalized (⟨харьяа⟩), and 1
spells only the long vowel (⟨идье⟩).

## Known limits

Orthographic short vowels of non-initial syllables are not phonemes but
reduced schwas, inserted where syllable structure requires one and absent
from the underlying form. Whether a given vowel letter is even in a
non-initial syllable, and whether the surrounding consonants form a
well-formed coda, needs a syllabifier the engine does not run for this
spec, so the spec does not implement the reduction: every short vowel
letter, medial or word-final, keeps its full quality (⟨хамар⟩ [xamar],
⟨хана⟩ [xana]). This also keeps a CV monosyllable's only vowel (⟨би⟩ [pi]
"I", ⟨та⟩ [tʰa] "you") — a plain word-final deletion rule would otherwise
delete it wrongly, since that vowel is in the word's initial, not a
non-initial, syllable.

Word prominence is not contrastive and the literature does not agree on
its place, so no `stress` block is declared.

## Benchmark

Scored against the WikiPron `mon_cyrl_broad` gold, which is a **mix** of
hand-typed Wiktionary IPA and `Module:mn-IPA` output rather than purely
crowd-scraped: a 40-headword sample of the raw en.wiktionary source drew
roughly three module-generated entries for every hand-typed one, so part
of this row is a reproduction test rather than an accuracy test (see
[Module-generated WikiPron rows](../benchmarks.md#module-generated-wikipron-rows)).
Mongolian Cyrillic is also a deep orthography for this purpose: the
letters record a historical, pre-reduction shape of the word rather than
its surface form, so the 0.25 deep-orthography threshold applies.

That gold is a narrow phonetic transcription and differs from this spec on
transcription depth rather than on phonology. It writes the weak velar as
[k] in every position including word-initially, marks final sonorant
devoicing ([r̥], [ɮ̥]), writes a lowered [w̜] for ⟨в⟩, marks half-length,
and spells out the epenthetic schwa. About 7% of its segments are symbols
this spec never emits for that reason, which is a floor on the achievable
PER that no rule change can recover. Adopting its word-initial [k] alone
would lower the measured PER by roughly two points, and the spec declines
to do so because the source states the opposite.
