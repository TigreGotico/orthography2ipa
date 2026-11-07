# Vietnamese (`vi`)

**Code**: `vi` | **Family**: Austroasiatic > Vietic | **Script**: Latin (alphabet, chữ quốc ngữ) | **Quality tier**: research

The `vi` spec describes Northern (Hanoi) Vietnamese in chữ quốc ngữ. Its reference is Kirby (2011), the IPA Illustration for this variety, which the spec's `sources` cite as `kirby2011`. Quốc ngữ writes all six tones, so the tone category of a syllable comes from its spelling with no lexicon. The spec therefore emits tone.

## The unit of mapping is the rime

A quốc ngữ syllable is an onset spelling, a rime (vần) spelling and a tone diacritic on one letter inside the rime. Almost everything irregular about the orthography is in the rime, and the rime is regular as a unit. ⟨anh⟩ is /ɛŋ/ and ⟨ong⟩ is /ɔŋ͡m/ whatever onset comes before them. So the spec maps whole toned rimes.

`scripts/gen_vietnamese.py` builds that table from four small inputs: the nucleus inventory, the coda inventory, the allophony that relates them, and the tone paradigm. It writes the `graphemes` and `allophones` blocks of `vi.json`. Edit the script, never the generated blocks.

The script applies these rules, all from Kirby (2011):

| Rule | What the spec does | Examples (engine output) |
|---|---|---|
| Velar fronting | ⟨anh ach⟩, ⟨ênh êch⟩ and ⟨inh ich⟩ end in velars, not the palatals /ɲ c/ of literary Vietnamese | ⟨canh⟩ `kɛŋ˧˧`, ⟨sách⟩ `sɛk˦˥` |
| Labial-velar finals | After the rounded monophthongs /u o ɔ/, the velar codas are doubly articulated | ⟨ông⟩ `oŋ͡m˧˧`, ⟨óc⟩ `ɔk͡p˦˥` |
| Diphthong exception | The diphthong /uə/ falls outside the labial-velar rule | ⟨uống⟩ `uəŋ˨˦` |
| Short vowels | ⟨ă â⟩ and ⟨ay au ây âu⟩ spell the short /ă ɤ̆/ | ⟨may⟩ `măj˧˧` against ⟨mai⟩ `maj˧˧` |
| Long ⟨oo⟩ and ⟨e⟩ rimes | ⟨oong ooc⟩ and ⟨eng ec⟩ spell the long /ɔː ɛː/ with a plain velar | ⟨boong⟩ `ɓɔːŋ˧˧` against ⟨bong⟩ `ɓɔŋ͡m˧˧` |
| Falling diphthongs | ⟨iê/ia⟩, ⟨uô/ua⟩ and ⟨ươ/ưa⟩ are /iə uə ɯə/, and the spelling alternation tracks only the presence of a coda | ⟨giếng⟩ `ziəŋ˨˦` |
| The ⟨gi⟩ collapse | After the onset ⟨gi⟩, a rime that starts with ⟨i⟩ is written with one ⟨i⟩ | ⟨gìn⟩ `zin˧˨` |
| Merged onsets | ⟨tr ch⟩ are /tɕ/, ⟨s x⟩ are /s/, ⟨d gi r⟩ are /z/, ⟨g gh⟩ are /ɣ/, and ⟨b đ⟩ are the implosives /ɓ ɗ/ | ⟨tra⟩ and ⟨cha⟩ `tɕa˧˧`, ⟨ra⟩ `za˧˧` |

Velar fronting is phonetically pre-velar [ŋ̟ k̟]. The spec does not write that narrow detail. ⟨gia⟩ is the exception that the orthography itself makes: it spells ⟨gi⟩ plus ⟨a⟩, `za˧˧`, because the /ziə/ rime is never written after ⟨gi⟩. Southern Vietnamese keeps several of the merged onsets apart. It is a different variety, and this spec does not describe it.

## Tone

Kirby analyses eight tones. A six-tone paradigm occurs on open and sonorant-final syllables. A two-tone paradigm occurs on syllables closed by an unreleased oral stop, where only the sắc-spelled (D1) and nặng-spelled (D2) tones occur. The spec follows this analysis. A checked rime therefore carries two readings and every other rime carries six. A spelling that the tone and coda restriction forbids, such as ⟨màt⟩, has no rime entry. The engine then reads it letter by letter (`ma˧˨t`).

| Diacritic | Name | Kirby's code | Chao letters |
|:---|:---|:---|:---|
| unmarked | ngang | A1 | ˧˧ |
| ◌̀ | huyền | A2 | ˧˨ |
| ◌́ | sắc | B1 / D1 | ˨˦, and ˦˥ when checked |
| ◌̉ | hỏi | C1 | ˧˩˨ |
| ◌̃ | ngã | C2 | ˧ˀ˥ |
| ◌̣ | nặng | B2 / D2 | ˨ˀ˩ |

The tone letters come after the coda, because the tone belongs to the syllable: ⟨bánh⟩ is `ɓɛŋ˨˦`. The spec's `tone_inventory` holds the same table.

The Chao letters are notation, and the categories are the claim. Kirby writes these tones with IPA tone staves and names their contours. The numeric values above are the Hanoi values that the literature cites most often. They let the benchmark measure whether the spec finds the right tone category, not a notation gap. The spec does not write voice quality. Kirby argues that IPA diacritics cannot show when glottalisation occurs relative to pitch.

## The gold rows

Two gold sets score the spec. For the figures, see the [scoreboard](../evaluation/generated/scoreboard.md).

The `ipadict` row (`vi_N.txt`) is Northern Vietnamese from the vPhon converter, a `machine-generated` tier that can gate. It agrees with Kirby segment for segment: the labial-velar finals, the ⟨anh⟩ /ɛŋ/ rime, the diphthongs, and Chao letters at the end of the syllable.

The `vox_communis` row comes from the VoxCommunis lexicon pipeline. Its tier is `epitran-derived`, so it can neither qualify nor block a promotion. It writes a pan-dialectal literary transcription: /c ɲ/ for final ⟨ch nh⟩, a length mark that the Illustration does not use, ˨˨ for ngang, and the tone letters inside the rime. Most of its distance from the spec is therefore notation. `scripts/fold_vi_notation.py` folds each convention out of both sides and scores the row again. The spec's `audit` entry for `vox_communis` records the result as `at_ceiling_documented`, and [Notation, not phonology](../evaluation/datasets.md#notation-not-phonology-vi-pa-as) describes the conventions.

The `vox_communis` tone tier also merges two contrastive tones, which is a gold defect and not a convention. It writes ˨˨ for both ngang and huyền. Kirby (2011: 386) tabulates them as separate categories, A1 (level) and A2 (mid falling), on the minimal pair *ma* 'ghost' and *mà* 'but, yet'. The spec keeps them apart (⟨ma⟩ `ma˧˧`, ⟨mà⟩ `ma˧˨`) and pays edit distance on that row. The `vox_communis_corrected` row repairs the merge from the spelling (see [the corrected row](../evaluation/datasets.md#voxcommunis-with-the-vietnamese-tone-merge-repaired-vox_communis_corrected)). The other tone splits in that gold match the spec: sắc and nặng each split by coda, which is Kirby's D1 and D2 restriction.

The finals are the one true analytical disagreement, and the source settles it against the gold. Under "Velar fronting", Kirby (2011: 383) names the palatal reading and rejects it. The stops after /i e ɛ/ "are actually pre-velar [ŋ̟] and [k̟], with no point of alveolar contact (Henderson 1965)", with ⟨canh⟩ [kɛŋ] and ⟨sách⟩ [sɛk].

## Where the spec disagrees with the gold

Three disagreements with the `ipadict` row are deliberate.

The spec reads ⟨giếng giêng giết giễu⟩ as `ziəŋ˨˦ ziəŋ˧˧ ziət˦˥ ziəw˧ˀ˥`. The gold has /zeŋ zeŋ zet zew/, because it reads the letters after ⟨gi⟩ as rimes ⟨êng êt êu⟩ of their own. Those rimes do not occur elsewhere, and the ⟨gi⟩ collapse is not special to a bare ⟨i⟩. Wiktionary gives [ziəŋ] and [ziət] for Hà Nội, so the spec keeps the collapse.

⟨quốc⟩ is `kwok͡p˦˥` and ⟨cuốc⟩ is `kuək˦˥`. The difference is real. ⟨qu⟩ takes the medial, so ⟨ôc⟩ has a rounded monophthong as its nucleus and gets the labial-velar final. The nucleus of ⟨cuốc⟩ is the diphthong /uə/, which the rule excludes. The gold makes the same split.

⟨b đ⟩ are the implosives /ɓ ɗ/, and the merged ⟨tr ch⟩ onset is the affricate /tɕ/, both from Kirby. The `ipadict` gold writes plain ⟨b d⟩ and a plain ⟨c⟩. The `vox_communis` gold writes ⟨ɓ⟩, so the two golds disagree, and the Illustration decides.

## Known limitations

| Gap | What the spec does |
|---|---|
| Southern Vietnamese | The Southern mergers and splits (⟨d gi⟩ against ⟨r⟩, ⟨s⟩ against ⟨x⟩, ⟨tr⟩ against ⟨ch⟩, final palatals) belong to a separate variety. The spec does not model them |
| Zero-onset glottal stop | Kirby counts /ʔ/ as the onset of a syllable that starts with a vowel. The spec writes nothing there, like both golds |
| Voice quality | Not written, following Kirby's own argument |
| Pre-velar fronting | Not written: ⟨kinh⟩ is `kiŋ˧˧`, not [kiŋ̟] |
| The letters ⟨ă⟩ and ⟨â⟩ alone | Neither is a syllable, because both nuclei need a coda. A word that is only one of these letters transcribes to an empty string, with an `UnmappedGraphemeWarning` |
| Foreign spellings | Transliterated proper nouns and loans outside the quốc ngữ rime inventory have no rime to match, and the engine reads them letter by letter |

---
[← Finnish](fi.md) · [Home](../index.md) · [Standard Thai →](th.md)
