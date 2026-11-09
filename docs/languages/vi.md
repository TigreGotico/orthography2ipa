# Vietnamese (`vi`)

<!-- atlas:summary begin -->
Vietnamese is an Austroasiatic language, written in the Latin script. Glottolog places it in China, Laos and Vietnam. The `vi` spec is at the research tier. It cites 2 sources and has 3 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `vi` |
| ISO 639-3 | [vie](https://iso639-3.sil.org/code/vie), Vietnamese |
| Glottolog | [viet1252](https://glottolog.org/resource/languoid/id/viet1252), Vietnamese |
| Wikidata | [Q9199](https://www.wikidata.org/wiki/Q9199) |
| Wikipedia | [Vietnamese language](https://en.wikipedia.org/wiki/Vietnamese_language) |
| Family | [Austroasiatic](by-family.md#austroasiatic) |
| Region | [Eurasia](by-region.md#eurasia) > [China](by-region.md#china), [Laos](by-region.md#laos), [Vietnam](by-region.md#vietnam) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1651, living |
| Ancestor | [Proto-Mon-Khmer (reconstructed)](https://tigregotico.github.io/orthography2ipa/#kha-x-proto-mon-khmer) `kha-x-proto-mon-khmer` |
| Explorer | [`vi` in the data explorer](https://tigregotico.github.io/orthography2ipa/#vi) |
| Spec file | [`vi.json`](../../orthography2ipa/data/vi.json) |
<!-- atlas:header end -->

## Overview

The `vi` spec describes Northern (Hanoi) Vietnamese in chữ quốc ngữ. Its reference is Kirby (2011), the IPA Illustration for this variety, which the spec's `sources` cite as `kirby2011`. Quốc ngữ writes all six tones, so the tone category of a syllable comes from its spelling with no lexicon. The spec therefore emits tone.

The page places Vietnamese in the Vietic branch.

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

<!-- atlas:lects begin -->
## Related lects

No spec names `vi` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 2 works. 1 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-kirby2011"></a>Kirby, J. P. (2011). *Vietnamese (Hanoi Vietnamese)*. Journal of the International Phonetic Association 41(3), 381-392. Cited: 381-392. [doi.org](https://doi.org/10.1017/S0025100311000181)
2. <a id="src-thompson1965"></a>Thompson, L.C. (1965). *A Vietnamese Grammar*. University of Washington Press.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `ipadict` ([open-dict-data/ipa-dict](https://github.com/open-dict-data/ipa-dict)) | `vi` | generated | machine-generated | MIT, each file its own | 70899 | 0.0777 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `vi` | generated | epitran-derived | CC0 1.0 | 2475 | 0.5596 | no |
| `vox_communis_corrected` | `vi` | generated | epitran-derived | CC0 1.0 | 2475 | 0.5596 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 818 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | p |  | t tʰ |  | k |  |
| Affricate |  |  |  | tɕ |  |  |
| Nasal | m |  | n | ɲ | ŋ |  |
| Fricative |  | f v | s z |  | x ɣ | h |
| Approximant |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u ɯ |
| Close-mid | e | o ɤ ɤ̆ |
| Open-mid | ɛ ɛː | ɔ ɔː |
| Open | a ă |  |

Sequences that the spec writes as one unit: [aj˧ˀ˥] [aj˧˧] [aj˧˨] [aj˧˩˨] [aj˨ˀ˩] [aj˨˦] [ak˦˥] [ak˨ˀ˩] [am˧ˀ˥] [am˧˧] [am˧˨] [am˧˩˨] [am˨ˀ˩] [am˨˦] [an˧ˀ˥] [an˧˧] [an˧˨] [an˧˩˨] [an˨ˀ˩] [an˨˦] [ap˦˥] [ap˨ˀ˩] [at˦˥] [at˨ˀ˩] [aw˧ˀ˥] [aw˧˧] [aw˧˨] [aw˧˩˨] [aw˨ˀ˩] [aw˨˦] [aŋ˧ˀ˥] [aŋ˧˧] [aŋ˧˨] [aŋ˧˩˨] [aŋ˨ˀ˩] [aŋ˨˦] [a˧ˀ˥] [a˧˧] [a˧˨] [a˧˩˨], and 747 more.

Tones: [◌̄] ngang (A1, level) — ˧˧; unmarked in the orthography, [◌̀] huyền (A2, mid falling) — ˧˨, [◌́] sắc (B1, rising) — ˨˦; ˦˥ on a syllable closed by an oral stop (D1), [◌̉] hỏi (C1, low falling) — ˧˩˨, [◌̃] ngã (C2, broken) — ˧ˀ˥, [◌̣] nặng (B2, low glottalized) — ˨ˀ˩; D2 on a syllable closed by an oral stop.
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a˧˧] |  |
| ⟨ai⟩ | [aj˧˧] |  |
| ⟨am⟩ | [am˧˧] |  |
| ⟨an⟩ | [an˧˧] |  |
| ⟨ang⟩ | [aŋ˧˧] |  |
| ⟨anh⟩ | [ɛŋ˧˧] |  |
| ⟨ao⟩ | [aw˧˧] |  |
| ⟨au⟩ | [ăw˧˧] |  |
| ⟨ay⟩ | [ăj˧˧] |  |
| ⟨b⟩ | [ɓ] |  |
| ⟨c⟩ | [k] |  |
| ⟨ch⟩ | [tɕ] |  |
| ⟨d⟩ | [z] |  |
| ⟨e⟩ | [ɛ˧˧] |  |
| ⟨em⟩ | [ɛm˧˧] |  |
| ⟨en⟩ | [ɛn˧˧] |  |
| ⟨eng⟩ | [ɛːŋ˧˧] |  |
| ⟨eo⟩ | [ɛw˧˧] |  |
| ⟨g⟩ | [ɣ] |  |
| ⟨gh⟩ | [ɣ] |  |
| ⟨gi⟩ | [z] [zi˧˧] |  |
| ⟨gim⟩ | [zim˧˧] |  |
| ⟨gin⟩ | [zin˧˧] |  |
| ⟨ginh⟩ | [ziŋ˧˧] |  |
| ⟨giêm⟩ | [ziəm˧˧] |  |
| ⟨giên⟩ | [ziən˧˧] |  |
| ⟨giêng⟩ | [ziəŋ˧˧] |  |
| ⟨giêu⟩ | [ziəw˧˧] |  |
| ⟨giếc⟩ | [ziək˦˥] |  |
| ⟨giếm⟩ | [ziəm˨˦] |  |
| ⟨giến⟩ | [ziən˨˦] |  |
| ⟨giếng⟩ | [ziəŋ˨˦] |  |
| ⟨giếp⟩ | [ziəp˦˥] |  |
| ⟨giết⟩ | [ziət˦˥] |  |
| ⟨giếu⟩ | [ziəw˨˦] |  |
| ⟨giềm⟩ | [ziəm˧˨] |  |
| ⟨giền⟩ | [ziən˧˨] |  |
| ⟨giềng⟩ | [ziəŋ˧˨] |  |
| ⟨giều⟩ | [ziəw˧˨] |  |
| ⟨giểm⟩ | [ziəm˧˩˨] |  |
| ⟨giển⟩ | [ziən˧˩˨] |  |
| ⟨giểng⟩ | [ziəŋ˧˩˨] |  |
| ⟨giểu⟩ | [ziəw˧˩˨] |  |
| ⟨giễm⟩ | [ziəm˧ˀ˥] |  |
| ⟨giễn⟩ | [ziən˧ˀ˥] |  |
| ⟨giễng⟩ | [ziəŋ˧ˀ˥] |  |
| ⟨giễu⟩ | [ziəw˧ˀ˥] |  |
| ⟨giệc⟩ | [ziək˨ˀ˩] |  |
| ⟨giệm⟩ | [ziəm˨ˀ˩] |  |
| ⟨giện⟩ | [ziən˨ˀ˩] |  |
| ⟨giệng⟩ | [ziəŋ˨ˀ˩] |  |
| ⟨giệp⟩ | [ziəp˨ˀ˩] |  |
| ⟨giệt⟩ | [ziət˨ˀ˩] |  |
| ⟨giệu⟩ | [ziəw˨ˀ˩] |  |
| ⟨gì⟩ | [zi˧˨] |  |
| ⟨gìm⟩ | [zim˧˨] |  |
| ⟨gìn⟩ | [zin˧˨] |  |
| ⟨gình⟩ | [ziŋ˧˨] |  |
| ⟨gí⟩ | [zi˨˦] |  |
| ⟨gích⟩ | [zik˦˥] |  |
| ⟨gím⟩ | [zim˨˦] |  |
| ⟨gín⟩ | [zin˨˦] |  |
| ⟨gính⟩ | [ziŋ˨˦] |  |
| ⟨gíp⟩ | [zip˦˥] |  |
| ⟨gít⟩ | [zit˦˥] |  |
| ⟨gĩ⟩ | [zi˧ˀ˥] |  |
| ⟨gĩm⟩ | [zim˧ˀ˥] |  |
| ⟨gĩn⟩ | [zin˧ˀ˥] |  |
| ⟨gĩnh⟩ | [ziŋ˧ˀ˥] |  |
| ⟨gỉ⟩ | [zi˧˩˨] |  |
| ⟨gỉm⟩ | [zim˧˩˨] |  |
| ⟨gỉn⟩ | [zin˧˩˨] |  |
| ⟨gỉnh⟩ | [ziŋ˧˩˨] |  |
| ⟨gị⟩ | [zi˨ˀ˩] |  |
| ⟨gịch⟩ | [zik˨ˀ˩] |  |
| ⟨gịm⟩ | [zim˨ˀ˩] |  |
| ⟨gịn⟩ | [zin˨ˀ˩] |  |
| ⟨gịnh⟩ | [ziŋ˨ˀ˩] |  |
| ⟨gịp⟩ | [zip˨ˀ˩] |  |
| ⟨gịt⟩ | [zit˨ˀ˩] |  |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i˧˧] |  |
| ⟨ia⟩ | [iə˧˧] |  |
| ⟨im⟩ | [im˧˧] |  |
| ⟨in⟩ | [in˧˧] |  |
| ⟨inh⟩ | [iŋ˧˧] |  |
| ⟨iu⟩ | [iw˧˧] |  |
| ⟨iêm⟩ | [iəm˧˧] |  |
| ⟨iên⟩ | [iən˧˧] |  |
| ⟨iêng⟩ | [iəŋ˧˧] |  |
| ⟨iêu⟩ | [iəw˧˧] |  |
| ⟨iếc⟩ | [iək˦˥] |  |
| ⟨iếm⟩ | [iəm˨˦] |  |
| ⟨iến⟩ | [iən˨˦] |  |
| ⟨iếng⟩ | [iəŋ˨˦] |  |
| ⟨iếp⟩ | [iəp˦˥] |  |
| ⟨iết⟩ | [iət˦˥] |  |
| ⟨iếu⟩ | [iəw˨˦] |  |
| ⟨iềm⟩ | [iəm˧˨] |  |
| ⟨iền⟩ | [iən˧˨] |  |
| ⟨iềng⟩ | [iəŋ˧˨] |  |
| ⟨iều⟩ | [iəw˧˨] |  |
| ⟨iểm⟩ | [iəm˧˩˨] |  |
| ⟨iển⟩ | [iən˧˩˨] |  |
| ⟨iểng⟩ | [iəŋ˧˩˨] |  |
| ⟨iểu⟩ | [iəw˧˩˨] |  |
| ⟨iễm⟩ | [iəm˧ˀ˥] |  |
| ⟨iễn⟩ | [iən˧ˀ˥] |  |
| ⟨iễng⟩ | [iəŋ˧ˀ˥] |  |
| ⟨iễu⟩ | [iəw˧ˀ˥] |  |
| ⟨iệc⟩ | [iək˨ˀ˩] |  |
| ⟨iệm⟩ | [iəm˨ˀ˩] |  |
| ⟨iện⟩ | [iən˨ˀ˩] |  |
| ⟨iệng⟩ | [iəŋ˨ˀ˩] |  |
| ⟨iệp⟩ | [iəp˨ˀ˩] |  |
| ⟨iệt⟩ | [iət˨ˀ˩] |  |
| ⟨iệu⟩ | [iəw˨ˀ˩] |  |
| ⟨k⟩ | [k] |  |
| ⟨kh⟩ | [x] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨ng⟩ | [ŋ] |  |
| ⟨ngh⟩ | [ŋ] |  |
| ⟨nh⟩ | [ɲ] |  |
| ⟨o⟩ | [ɔ˧˧] |  |
| ⟨oa⟩ | [wa˧˧] |  |
| ⟨oai⟩ | [waj˧˧] |  |
| ⟨oam⟩ | [wam˧˧] |  |
| ⟨oan⟩ | [wan˧˧] |  |
| ⟨oang⟩ | [waŋ˧˧] |  |
| ⟨oanh⟩ | [wɛŋ˧˧] |  |
| ⟨oao⟩ | [waw˧˧] |  |
| ⟨oay⟩ | [wăj˧˧] |  |
| ⟨oe⟩ | [wɛ˧˧] |  |
| ⟨oen⟩ | [wɛn˧˧] |  |
| ⟨oeo⟩ | [wɛw˧˧] |  |
| ⟨oi⟩ | [ɔj˧˧] |  |
| ⟨om⟩ | [ɔm˧˧] |  |
| ⟨on⟩ | [ɔn˧˧] |  |
| ⟨ong⟩ | [ɔŋ͡m˧˧] |  |
| ⟨oong⟩ | [ɔːŋ˧˧] |  |
| ⟨oà⟩ | [wa˧˨] |  |
| ⟨oài⟩ | [waj˧˨] |  |
| ⟨oàm⟩ | [wam˧˨] |  |
| ⟨oàn⟩ | [wan˧˨] |  |
| ⟨oàng⟩ | [waŋ˧˨] |  |
| ⟨oành⟩ | [wɛŋ˧˨] |  |
| ⟨oào⟩ | [waw˧˨] |  |
| ⟨oày⟩ | [wăj˧˨] |  |
| ⟨oá⟩ | [wa˨˦] |  |
| ⟨oác⟩ | [wak˦˥] |  |
| ⟨oách⟩ | [wɛk˦˥] |  |
| ⟨oái⟩ | [waj˨˦] |  |
| ⟨oám⟩ | [wam˨˦] |  |
| ⟨oán⟩ | [wan˨˦] |  |
| ⟨oáng⟩ | [waŋ˨˦] |  |
| ⟨oánh⟩ | [wɛŋ˨˦] |  |
| ⟨oáo⟩ | [waw˨˦] |  |
| ⟨oáp⟩ | [wap˦˥] |  |
| ⟨oát⟩ | [wat˦˥] |  |
| ⟨oáy⟩ | [wăj˨˦] |  |
| ⟨oã⟩ | [wa˧ˀ˥] |  |
| ⟨oãi⟩ | [waj˧ˀ˥] |  |
| ⟨oãm⟩ | [wam˧ˀ˥] |  |
| ⟨oãn⟩ | [wan˧ˀ˥] |  |
| ⟨oãng⟩ | [waŋ˧ˀ˥] |  |
| ⟨oãnh⟩ | [wɛŋ˧ˀ˥] |  |
| ⟨oão⟩ | [waw˧ˀ˥] |  |
| ⟨oãy⟩ | [wăj˧ˀ˥] |  |
| ⟨oè⟩ | [wɛ˧˨] |  |
| ⟨oèn⟩ | [wɛn˧˨] |  |
| ⟨oèo⟩ | [wɛw˧˨] |  |
| ⟨oé⟩ | [wɛ˨˦] |  |
| ⟨oén⟩ | [wɛn˨˦] |  |
| ⟨oéo⟩ | [wɛw˨˦] |  |
| ⟨oét⟩ | [wɛt˦˥] |  |
| ⟨oòng⟩ | [ɔːŋ˧˨] |  |
| ⟨oóc⟩ | [ɔːk˦˥] |  |
| ⟨oóng⟩ | [ɔːŋ˨˦] |  |
| ⟨oõng⟩ | [ɔːŋ˧ˀ˥] |  |
| ⟨oăm⟩ | [wăm˧˧] |  |
| ⟨oăn⟩ | [wăn˧˧] |  |
| ⟨oăng⟩ | [wăŋ˧˧] |  |
| ⟨oạ⟩ | [wa˨ˀ˩] |  |
| ⟨oạc⟩ | [wak˨ˀ˩] |  |
| ⟨oạch⟩ | [wɛk˨ˀ˩] |  |
| ⟨oại⟩ | [waj˨ˀ˩] |  |
| ⟨oạm⟩ | [wam˨ˀ˩] |  |
| ⟨oạn⟩ | [wan˨ˀ˩] |  |
| ⟨oạng⟩ | [waŋ˨ˀ˩] |  |
| ⟨oạnh⟩ | [wɛŋ˨ˀ˩] |  |
| ⟨oạo⟩ | [waw˨ˀ˩] |  |
| ⟨oạp⟩ | [wap˨ˀ˩] |  |
| ⟨oạt⟩ | [wat˨ˀ˩] |  |
| ⟨oạy⟩ | [wăj˨ˀ˩] |  |
| ⟨oả⟩ | [wa˧˩˨] |  |
| ⟨oải⟩ | [waj˧˩˨] |  |
| ⟨oảm⟩ | [wam˧˩˨] |  |
| ⟨oản⟩ | [wan˧˩˨] |  |
| ⟨oảng⟩ | [waŋ˧˩˨] |  |
| ⟨oảnh⟩ | [wɛŋ˧˩˨] |  |
| ⟨oảo⟩ | [waw˧˩˨] |  |
| ⟨oảy⟩ | [wăj˧˩˨] |  |
| ⟨oắc⟩ | [wăk˦˥] |  |
| ⟨oắm⟩ | [wăm˨˦] |  |
| ⟨oắn⟩ | [wăn˨˦] |  |
| ⟨oắng⟩ | [wăŋ˨˦] |  |
| ⟨oắp⟩ | [wăp˦˥] |  |
| ⟨oắt⟩ | [wăt˦˥] |  |
| ⟨oằm⟩ | [wăm˧˨] |  |
| ⟨oằn⟩ | [wăn˧˨] |  |
| ⟨oằng⟩ | [wăŋ˧˨] |  |
| ⟨oẳm⟩ | [wăm˧˩˨] |  |
| ⟨oẳn⟩ | [wăn˧˩˨] |  |
| ⟨oẳng⟩ | [wăŋ˧˩˨] |  |
| ⟨oẵm⟩ | [wăm˧ˀ˥] |  |
| ⟨oẵn⟩ | [wăn˧ˀ˥] |  |
| ⟨oẵng⟩ | [wăŋ˧ˀ˥] |  |
| ⟨oặc⟩ | [wăk˨ˀ˩] |  |
| ⟨oặm⟩ | [wăm˨ˀ˩] |  |
| ⟨oặn⟩ | [wăn˨ˀ˩] |  |
| ⟨oặng⟩ | [wăŋ˨ˀ˩] |  |
| ⟨oặp⟩ | [wăp˨ˀ˩] |  |
| ⟨oặt⟩ | [wăt˨ˀ˩] |  |
| ⟨oẹ⟩ | [wɛ˨ˀ˩] |  |
| ⟨oẹn⟩ | [wɛn˨ˀ˩] |  |
| ⟨oẹo⟩ | [wɛw˨ˀ˩] |  |
| ⟨oẹt⟩ | [wɛt˨ˀ˩] |  |
| ⟨oẻ⟩ | [wɛ˧˩˨] |  |
| ⟨oẻn⟩ | [wɛn˧˩˨] |  |
| ⟨oẻo⟩ | [wɛw˧˩˨] |  |
| ⟨oẽ⟩ | [wɛ˧ˀ˥] |  |
| ⟨oẽn⟩ | [wɛn˧ˀ˥] |  |
| ⟨oẽo⟩ | [wɛw˧ˀ˥] |  |
| ⟨oọc⟩ | [ɔːk˨ˀ˩] |  |
| ⟨oọng⟩ | [ɔːŋ˨ˀ˩] |  |
| ⟨oỏng⟩ | [ɔːŋ˧˩˨] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [f] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [z] |  |
| ⟨s⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [tʰ] |  |
| ⟨tr⟩ | [tɕ] |  |
| ⟨u⟩ | [u˧˧] |  |
| ⟨ua⟩ | [uə˧˧] |  |
| ⟨ui⟩ | [uj˧˧] |  |
| ⟨um⟩ | [um˧˧] |  |
| ⟨un⟩ | [un˧˧] |  |
| ⟨ung⟩ | [uŋ͡m˧˧] |  |
| ⟨uy⟩ | [wi˧˧] |  |
| ⟨uya⟩ | [wiə˧˧] |  |
| ⟨uyn⟩ | [win˧˧] |  |
| ⟨uynh⟩ | [wiŋ˧˧] |  |
| ⟨uyu⟩ | [wiw˧˧] |  |
| ⟨uyên⟩ | [wiən˧˧] |  |
| ⟨uyến⟩ | [wiən˨˦] |  |
| ⟨uyết⟩ | [wiət˦˥] |  |
| ⟨uyền⟩ | [wiən˧˨] |  |
| ⟨uyển⟩ | [wiən˧˩˨] |  |
| ⟨uyễn⟩ | [wiən˧ˀ˥] |  |
| ⟨uyện⟩ | [wiən˨ˀ˩] |  |
| ⟨uyệt⟩ | [wiət˨ˀ˩] |  |
| ⟨uân⟩ | [wɤ̆n˧˧] |  |
| ⟨uâng⟩ | [wɤ̆ŋ˧˧] |  |
| ⟨uây⟩ | [wɤ̆j˧˧] |  |
| ⟨uê⟩ | [we˧˧] |  |
| ⟨uên⟩ | [wen˧˧] |  |
| ⟨uênh⟩ | [weŋ˧˧] |  |
| ⟨uôi⟩ | [uəj˧˧] |  |
| ⟨uôm⟩ | [uəm˧˧] |  |
| ⟨uôn⟩ | [uən˧˧] |  |
| ⟨uông⟩ | [uəŋ˧˧] |  |
| ⟨uý⟩ | [wi˨˦] |  |
| ⟨uýa⟩ | [wiə˨˦] |  |
| ⟨uých⟩ | [wik˦˥] |  |
| ⟨uýn⟩ | [win˨˦] |  |
| ⟨uýnh⟩ | [wiŋ˨˦] |  |
| ⟨uýp⟩ | [wip˦˥] |  |
| ⟨uýt⟩ | [wit˦˥] |  |
| ⟨uýu⟩ | [wiw˨˦] |  |
| ⟨uơ⟩ | [wɤ˧˧] |  |
| ⟨uấn⟩ | [wɤ̆n˨˦] |  |
| ⟨uấng⟩ | [wɤ̆ŋ˨˦] |  |
| ⟨uất⟩ | [wɤ̆t˦˥] |  |
| ⟨uấy⟩ | [wɤ̆j˨˦] |  |
| ⟨uần⟩ | [wɤ̆n˧˨] |  |
| ⟨uầng⟩ | [wɤ̆ŋ˧˨] |  |
| ⟨uầy⟩ | [wɤ̆j˧˨] |  |
| ⟨uẩn⟩ | [wɤ̆n˧˩˨] |  |
| ⟨uẩng⟩ | [wɤ̆ŋ˧˩˨] |  |
| ⟨uẩy⟩ | [wɤ̆j˧˩˨] |  |
| ⟨uẫn⟩ | [wɤ̆n˧ˀ˥] |  |
| ⟨uẫng⟩ | [wɤ̆ŋ˧ˀ˥] |  |
| ⟨uẫy⟩ | [wɤ̆j˧ˀ˥] |  |
| ⟨uận⟩ | [wɤ̆n˨ˀ˩] |  |
| ⟨uậng⟩ | [wɤ̆ŋ˨ˀ˩] |  |
| ⟨uật⟩ | [wɤ̆t˨ˀ˩] |  |
| ⟨uậy⟩ | [wɤ̆j˨ˀ˩] |  |
| ⟨uế⟩ | [we˨˦] |  |
| ⟨uếch⟩ | [wek˦˥] |  |
| ⟨uến⟩ | [wen˨˦] |  |
| ⟨uếnh⟩ | [weŋ˨˦] |  |
| ⟨uết⟩ | [wet˦˥] |  |
| ⟨uề⟩ | [we˧˨] |  |
| ⟨uền⟩ | [wen˧˨] |  |
| ⟨uềnh⟩ | [weŋ˧˨] |  |
| ⟨uể⟩ | [we˧˩˨] |  |
| ⟨uển⟩ | [wen˧˩˨] |  |
| ⟨uểnh⟩ | [weŋ˧˩˨] |  |
| ⟨uễ⟩ | [we˧ˀ˥] |  |
| ⟨uễn⟩ | [wen˧ˀ˥] |  |
| ⟨uễnh⟩ | [weŋ˧ˀ˥] |  |
| ⟨uệ⟩ | [we˨ˀ˩] |  |
| ⟨uệch⟩ | [wek˨ˀ˩] |  |
| ⟨uện⟩ | [wen˨ˀ˩] |  |
| ⟨uệnh⟩ | [weŋ˨ˀ˩] |  |
| ⟨uệt⟩ | [wet˨ˀ˩] |  |
| ⟨uốc⟩ | [uək˦˥] |  |
| ⟨uối⟩ | [uəj˨˦] |  |
| ⟨uốm⟩ | [uəm˨˦] |  |
| ⟨uốn⟩ | [uən˨˦] |  |
| ⟨uống⟩ | [uəŋ˨˦] |  |
| ⟨uốt⟩ | [uət˦˥] |  |
| ⟨uồi⟩ | [uəj˧˨] |  |
| ⟨uồm⟩ | [uəm˧˨] |  |
| ⟨uồn⟩ | [uən˧˨] |  |
| ⟨uồng⟩ | [uəŋ˧˨] |  |
| ⟨uổi⟩ | [uəj˧˩˨] |  |
| ⟨uổm⟩ | [uəm˧˩˨] |  |
| ⟨uổn⟩ | [uən˧˩˨] |  |
| ⟨uổng⟩ | [uəŋ˧˩˨] |  |
| ⟨uỗi⟩ | [uəj˧ˀ˥] |  |
| ⟨uỗm⟩ | [uəm˧ˀ˥] |  |
| ⟨uỗn⟩ | [uən˧ˀ˥] |  |
| ⟨uỗng⟩ | [uəŋ˧ˀ˥] |  |
| ⟨uộc⟩ | [uək˨ˀ˩] |  |
| ⟨uội⟩ | [uəj˨ˀ˩] |  |
| ⟨uộm⟩ | [uəm˨ˀ˩] |  |
| ⟨uộn⟩ | [uən˨ˀ˩] |  |
| ⟨uộng⟩ | [uəŋ˨ˀ˩] |  |
| ⟨uột⟩ | [uət˨ˀ˩] |  |
| ⟨uớ⟩ | [wɤ˨˦] |  |
| ⟨uờ⟩ | [wɤ˧˨] |  |
| ⟨uở⟩ | [wɤ˧˩˨] |  |
| ⟨uỡ⟩ | [wɤ˧ˀ˥] |  |
| ⟨uợ⟩ | [wɤ˨ˀ˩] |  |
| ⟨uỳ⟩ | [wi˧˨] |  |
| ⟨uỳa⟩ | [wiə˧˨] |  |
| ⟨uỳn⟩ | [win˧˨] |  |
| ⟨uỳnh⟩ | [wiŋ˧˨] |  |
| ⟨uỳu⟩ | [wiw˧˨] |  |
| ⟨uỵ⟩ | [wi˨ˀ˩] |  |
| ⟨uỵa⟩ | [wiə˨ˀ˩] |  |
| ⟨uỵch⟩ | [wik˨ˀ˩] |  |
| ⟨uỵn⟩ | [win˨ˀ˩] |  |
| ⟨uỵnh⟩ | [wiŋ˨ˀ˩] |  |
| ⟨uỵp⟩ | [wip˨ˀ˩] |  |
| ⟨uỵt⟩ | [wit˨ˀ˩] |  |
| ⟨uỵu⟩ | [wiw˨ˀ˩] |  |
| ⟨uỷ⟩ | [wi˧˩˨] |  |
| ⟨uỷa⟩ | [wiə˧˩˨] |  |
| ⟨uỷn⟩ | [win˧˩˨] |  |
| ⟨uỷnh⟩ | [wiŋ˧˩˨] |  |
| ⟨uỷu⟩ | [wiw˧˩˨] |  |
| ⟨uỹ⟩ | [wi˧ˀ˥] |  |
| ⟨uỹa⟩ | [wiə˧ˀ˥] |  |
| ⟨uỹn⟩ | [win˧ˀ˥] |  |
| ⟨uỹnh⟩ | [wiŋ˧ˀ˥] |  |
| ⟨uỹu⟩ | [wiw˧ˀ˥] |  |
| ⟨v⟩ | [v] |  |
| ⟨x⟩ | [s] |  |
| ⟨y⟩ | [i˧˧] |  |
| ⟨ya⟩ | [iə˧˧] |  |
| ⟨ynh⟩ | [iŋ˧˧] |  |
| ⟨yêm⟩ | [iəm˧˧] |  |
| ⟨yên⟩ | [iən˧˧] |  |
| ⟨yêng⟩ | [iəŋ˧˧] |  |
| ⟨yêu⟩ | [iəw˧˧] |  |
| ⟨yếm⟩ | [iəm˨˦] |  |
| ⟨yến⟩ | [iən˨˦] |  |
| ⟨yếng⟩ | [iəŋ˨˦] |  |
| ⟨yết⟩ | [iət˦˥] |  |
| ⟨yếu⟩ | [iəw˨˦] |  |
| ⟨yềm⟩ | [iəm˧˨] |  |
| ⟨yền⟩ | [iən˧˨] |  |
| ⟨yềng⟩ | [iəŋ˧˨] |  |
| ⟨yều⟩ | [iəw˧˨] |  |
| ⟨yểm⟩ | [iəm˧˩˨] |  |
| ⟨yển⟩ | [iən˧˩˨] |  |
| ⟨yểng⟩ | [iəŋ˧˩˨] |  |
| ⟨yểu⟩ | [iəw˧˩˨] |  |
| ⟨yễm⟩ | [iəm˧ˀ˥] |  |
| ⟨yễn⟩ | [iən˧ˀ˥] |  |
| ⟨yễng⟩ | [iəŋ˧ˀ˥] |  |
| ⟨yễu⟩ | [iəw˧ˀ˥] |  |
| ⟨yệm⟩ | [iəm˨ˀ˩] |  |
| ⟨yện⟩ | [iən˨ˀ˩] |  |
| ⟨yệng⟩ | [iəŋ˨ˀ˩] |  |
| ⟨yệt⟩ | [iət˨ˀ˩] |  |
| ⟨yệu⟩ | [iəw˨ˀ˩] |  |
| ⟨à⟩ | [a˧˨] |  |
| ⟨ài⟩ | [aj˧˨] |  |
| ⟨àm⟩ | [am˧˨] |  |
| ⟨àn⟩ | [an˧˨] |  |
| ⟨àng⟩ | [aŋ˧˨] |  |
| ⟨ành⟩ | [ɛŋ˧˨] |  |
| ⟨ào⟩ | [aw˧˨] |  |
| ⟨àu⟩ | [ăw˧˨] |  |
| ⟨ày⟩ | [ăj˧˨] |  |
| ⟨á⟩ | [a˨˦] |  |
| ⟨ác⟩ | [ak˦˥] |  |
| ⟨ách⟩ | [ɛk˦˥] |  |
| ⟨ái⟩ | [aj˨˦] |  |
| ⟨ám⟩ | [am˨˦] |  |
| ⟨án⟩ | [an˨˦] |  |
| ⟨áng⟩ | [aŋ˨˦] |  |
| ⟨ánh⟩ | [ɛŋ˨˦] |  |
| ⟨áo⟩ | [aw˨˦] |  |
| ⟨áp⟩ | [ap˦˥] |  |
| ⟨át⟩ | [at˦˥] |  |
| ⟨áu⟩ | [ăw˨˦] |  |
| ⟨áy⟩ | [ăj˨˦] |  |
| ⟨âm⟩ | [ɤ̆m˧˧] |  |
| ⟨ân⟩ | [ɤ̆n˧˧] |  |
| ⟨âng⟩ | [ɤ̆ŋ˧˧] |  |
| ⟨âu⟩ | [ɤ̆w˧˧] |  |
| ⟨ây⟩ | [ɤ̆j˧˧] |  |
| ⟨ã⟩ | [a˧ˀ˥] |  |
| ⟨ãi⟩ | [aj˧ˀ˥] |  |
| ⟨ãm⟩ | [am˧ˀ˥] |  |
| ⟨ãn⟩ | [an˧ˀ˥] |  |
| ⟨ãng⟩ | [aŋ˧ˀ˥] |  |
| ⟨ãnh⟩ | [ɛŋ˧ˀ˥] |  |
| ⟨ão⟩ | [aw˧ˀ˥] |  |
| ⟨ãu⟩ | [ăw˧ˀ˥] |  |
| ⟨ãy⟩ | [ăj˧ˀ˥] |  |
| ⟨è⟩ | [ɛ˧˨] |  |
| ⟨èm⟩ | [ɛm˧˨] |  |
| ⟨èn⟩ | [ɛn˧˨] |  |
| ⟨èng⟩ | [ɛːŋ˧˨] |  |
| ⟨èo⟩ | [ɛw˧˨] |  |
| ⟨é⟩ | [ɛ˨˦] |  |
| ⟨éc⟩ | [ɛːk˦˥] |  |
| ⟨ém⟩ | [ɛm˨˦] |  |
| ⟨én⟩ | [ɛn˨˦] |  |
| ⟨éng⟩ | [ɛːŋ˨˦] |  |
| ⟨éo⟩ | [ɛw˨˦] |  |
| ⟨ép⟩ | [ɛp˦˥] |  |
| ⟨ét⟩ | [ɛt˦˥] |  |
| ⟨ê⟩ | [e˧˧] |  |
| ⟨êm⟩ | [em˧˧] |  |
| ⟨ên⟩ | [en˧˧] |  |
| ⟨ênh⟩ | [eŋ˧˧] |  |
| ⟨êu⟩ | [ew˧˧] |  |
| ⟨ì⟩ | [i˧˨] |  |
| ⟨ìa⟩ | [iə˧˨] |  |
| ⟨ìm⟩ | [im˧˨] |  |
| ⟨ìn⟩ | [in˧˨] |  |
| ⟨ình⟩ | [iŋ˧˨] |  |
| ⟨ìu⟩ | [iw˧˨] |  |
| ⟨í⟩ | [i˨˦] |  |
| ⟨ía⟩ | [iə˨˦] |  |
| ⟨ích⟩ | [ik˦˥] |  |
| ⟨ím⟩ | [im˨˦] |  |
| ⟨ín⟩ | [in˨˦] |  |
| ⟨ính⟩ | [iŋ˨˦] |  |
| ⟨íp⟩ | [ip˦˥] |  |
| ⟨ít⟩ | [it˦˥] |  |
| ⟨íu⟩ | [iw˨˦] |  |
| ⟨ò⟩ | [ɔ˧˨] |  |
| ⟨òa⟩ | [wa˧˨] |  |
| ⟨òe⟩ | [wɛ˧˨] |  |
| ⟨òi⟩ | [ɔj˧˨] |  |
| ⟨òm⟩ | [ɔm˧˨] |  |
| ⟨òn⟩ | [ɔn˧˨] |  |
| ⟨òng⟩ | [ɔŋ͡m˧˨] |  |
| ⟨òong⟩ | [ɔːŋ˧˨] |  |
| ⟨ó⟩ | [ɔ˨˦] |  |
| ⟨óa⟩ | [wa˨˦] |  |
| ⟨óc⟩ | [ɔk͡p˦˥] |  |
| ⟨óe⟩ | [wɛ˨˦] |  |
| ⟨ói⟩ | [ɔj˨˦] |  |
| ⟨óm⟩ | [ɔm˨˦] |  |
| ⟨ón⟩ | [ɔn˨˦] |  |
| ⟨óng⟩ | [ɔŋ͡m˨˦] |  |
| ⟨óoc⟩ | [ɔːk˦˥] |  |
| ⟨óong⟩ | [ɔːŋ˨˦] |  |
| ⟨óp⟩ | [ɔp˦˥] |  |
| ⟨ót⟩ | [ɔt˦˥] |  |
| ⟨ô⟩ | [o˧˧] |  |
| ⟨ôi⟩ | [oj˧˧] |  |
| ⟨ôm⟩ | [om˧˧] |  |
| ⟨ôn⟩ | [on˧˧] |  |
| ⟨ông⟩ | [oŋ͡m˧˧] |  |
| ⟨õ⟩ | [ɔ˧ˀ˥] |  |
| ⟨õa⟩ | [wa˧ˀ˥] |  |
| ⟨õe⟩ | [wɛ˧ˀ˥] |  |
| ⟨õi⟩ | [ɔj˧ˀ˥] |  |
| ⟨õm⟩ | [ɔm˧ˀ˥] |  |
| ⟨õn⟩ | [ɔn˧ˀ˥] |  |
| ⟨õng⟩ | [ɔŋ͡m˧ˀ˥] |  |
| ⟨õong⟩ | [ɔːŋ˧ˀ˥] |  |
| ⟨ù⟩ | [u˧˨] |  |
| ⟨ùa⟩ | [uə˧˨] |  |
| ⟨ùi⟩ | [uj˧˨] |  |
| ⟨ùm⟩ | [um˧˨] |  |
| ⟨ùn⟩ | [un˧˨] |  |
| ⟨ùng⟩ | [uŋ͡m˧˨] |  |
| ⟨ùy⟩ | [wi˧˨] |  |
| ⟨ùya⟩ | [wiə˧˨] |  |
| ⟨ùê⟩ | [we˧˨] |  |
| ⟨ùơ⟩ | [wɤ˧˨] |  |
| ⟨ú⟩ | [u˨˦] |  |
| ⟨úa⟩ | [uə˨˦] |  |
| ⟨úc⟩ | [uk͡p˦˥] |  |
| ⟨úi⟩ | [uj˨˦] |  |
| ⟨úm⟩ | [um˨˦] |  |
| ⟨ún⟩ | [un˨˦] |  |
| ⟨úng⟩ | [uŋ͡m˨˦] |  |
| ⟨úp⟩ | [up˦˥] |  |
| ⟨út⟩ | [ut˦˥] |  |
| ⟨úy⟩ | [wi˨˦] |  |
| ⟨úya⟩ | [wiə˨˦] |  |
| ⟨úê⟩ | [we˨˦] |  |
| ⟨úơ⟩ | [wɤ˨˦] |  |
| ⟨ý⟩ | [i˨˦] |  |
| ⟨ýa⟩ | [iə˨˦] |  |
| ⟨ých⟩ | [ik˦˥] |  |
| ⟨ýnh⟩ | [iŋ˨˦] |  |
| ⟨ýp⟩ | [ip˦˥] |  |
| ⟨ýt⟩ | [it˦˥] |  |
| ⟨ăm⟩ | [ăm˧˧] |  |
| ⟨ăn⟩ | [ăn˧˧] |  |
| ⟨ăng⟩ | [ăŋ˧˧] |  |
| ⟨đ⟩ | [ɗ] |  |
| ⟨ĩ⟩ | [i˧ˀ˥] |  |
| ⟨ĩa⟩ | [iə˧ˀ˥] |  |
| ⟨ĩm⟩ | [im˧ˀ˥] |  |
| ⟨ĩn⟩ | [in˧ˀ˥] |  |
| ⟨ĩnh⟩ | [iŋ˧ˀ˥] |  |
| ⟨ĩu⟩ | [iw˧ˀ˥] |  |
| ⟨ũ⟩ | [u˧ˀ˥] |  |
| ⟨ũa⟩ | [uə˧ˀ˥] |  |
| ⟨ũi⟩ | [uj˧ˀ˥] |  |
| ⟨ũm⟩ | [um˧ˀ˥] |  |
| ⟨ũn⟩ | [un˧ˀ˥] |  |
| ⟨ũng⟩ | [uŋ͡m˧ˀ˥] |  |
| ⟨ũy⟩ | [wi˧ˀ˥] |  |
| ⟨ũya⟩ | [wiə˧ˀ˥] |  |
| ⟨ũê⟩ | [we˧ˀ˥] |  |
| ⟨ũơ⟩ | [wɤ˧ˀ˥] |  |
| ⟨ơ⟩ | [ɤ˧˧] |  |
| ⟨ơi⟩ | [ɤj˧˧] |  |
| ⟨ơm⟩ | [ɤm˧˧] |  |
| ⟨ơn⟩ | [ɤn˧˧] |  |
| ⟨ư⟩ | [ɯ˧˧] |  |
| ⟨ưa⟩ | [ɯə˧˧] |  |
| ⟨ưi⟩ | [ɯj˧˧] |  |
| ⟨ưm⟩ | [ɯm˧˧] |  |
| ⟨ưn⟩ | [ɯn˧˧] |  |
| ⟨ưng⟩ | [ɯŋ˧˧] |  |
| ⟨ưu⟩ | [ɯw˧˧] |  |
| ⟨ươi⟩ | [ɯəj˧˧] |  |
| ⟨ươm⟩ | [ɯəm˧˧] |  |
| ⟨ươn⟩ | [ɯən˧˧] |  |
| ⟨ương⟩ | [ɯəŋ˧˧] |  |
| ⟨ươu⟩ | [ɯəw˧˧] |  |
| ⟨ước⟩ | [ɯək˦˥] |  |
| ⟨ưới⟩ | [ɯəj˨˦] |  |
| ⟨ướm⟩ | [ɯəm˨˦] |  |
| ⟨ướn⟩ | [ɯən˨˦] |  |
| ⟨ướng⟩ | [ɯəŋ˨˦] |  |
| ⟨ướp⟩ | [ɯəp˦˥] |  |
| ⟨ướt⟩ | [ɯət˦˥] |  |
| ⟨ướu⟩ | [ɯəw˨˦] |  |
| ⟨ười⟩ | [ɯəj˧˨] |  |
| ⟨ườm⟩ | [ɯəm˧˨] |  |
| ⟨ườn⟩ | [ɯən˧˨] |  |
| ⟨ường⟩ | [ɯəŋ˧˨] |  |
| ⟨ườu⟩ | [ɯəw˧˨] |  |
| ⟨ưởi⟩ | [ɯəj˧˩˨] |  |
| ⟨ưởm⟩ | [ɯəm˧˩˨] |  |
| ⟨ưởn⟩ | [ɯən˧˩˨] |  |
| ⟨ưởng⟩ | [ɯəŋ˧˩˨] |  |
| ⟨ưởu⟩ | [ɯəw˧˩˨] |  |
| ⟨ưỡi⟩ | [ɯəj˧ˀ˥] |  |
| ⟨ưỡm⟩ | [ɯəm˧ˀ˥] |  |
| ⟨ưỡn⟩ | [ɯən˧ˀ˥] |  |
| ⟨ưỡng⟩ | [ɯəŋ˧ˀ˥] |  |
| ⟨ưỡu⟩ | [ɯəw˧ˀ˥] |  |
| ⟨ược⟩ | [ɯək˨ˀ˩] |  |
| ⟨ượi⟩ | [ɯəj˨ˀ˩] |  |
| ⟨ượm⟩ | [ɯəm˨ˀ˩] |  |
| ⟨ượn⟩ | [ɯən˨ˀ˩] |  |
| ⟨ượng⟩ | [ɯəŋ˨ˀ˩] |  |
| ⟨ượp⟩ | [ɯəp˨ˀ˩] |  |
| ⟨ượt⟩ | [ɯət˨ˀ˩] |  |
| ⟨ượu⟩ | [ɯəw˨ˀ˩] |  |
| ⟨ạ⟩ | [a˨ˀ˩] |  |
| ⟨ạc⟩ | [ak˨ˀ˩] |  |
| ⟨ạch⟩ | [ɛk˨ˀ˩] |  |
| ⟨ại⟩ | [aj˨ˀ˩] |  |
| ⟨ạm⟩ | [am˨ˀ˩] |  |
| ⟨ạn⟩ | [an˨ˀ˩] |  |
| ⟨ạng⟩ | [aŋ˨ˀ˩] |  |
| ⟨ạnh⟩ | [ɛŋ˨ˀ˩] |  |
| ⟨ạo⟩ | [aw˨ˀ˩] |  |
| ⟨ạp⟩ | [ap˨ˀ˩] |  |
| ⟨ạt⟩ | [at˨ˀ˩] |  |
| ⟨ạu⟩ | [ăw˨ˀ˩] |  |
| ⟨ạy⟩ | [ăj˨ˀ˩] |  |
| ⟨ả⟩ | [a˧˩˨] |  |
| ⟨ải⟩ | [aj˧˩˨] |  |
| ⟨ảm⟩ | [am˧˩˨] |  |
| ⟨ản⟩ | [an˧˩˨] |  |
| ⟨ảng⟩ | [aŋ˧˩˨] |  |
| ⟨ảnh⟩ | [ɛŋ˧˩˨] |  |
| ⟨ảo⟩ | [aw˧˩˨] |  |
| ⟨ảu⟩ | [ăw˧˩˨] |  |
| ⟨ảy⟩ | [ăj˧˩˨] |  |
| ⟨ấc⟩ | [ɤ̆k˦˥] |  |
| ⟨ấm⟩ | [ɤ̆m˨˦] |  |
| ⟨ấn⟩ | [ɤ̆n˨˦] |  |
| ⟨ấng⟩ | [ɤ̆ŋ˨˦] |  |
| ⟨ấp⟩ | [ɤ̆p˦˥] |  |
| ⟨ất⟩ | [ɤ̆t˦˥] |  |
| ⟨ấu⟩ | [ɤ̆w˨˦] |  |
| ⟨ấy⟩ | [ɤ̆j˨˦] |  |
| ⟨ầm⟩ | [ɤ̆m˧˨] |  |
| ⟨ần⟩ | [ɤ̆n˧˨] |  |
| ⟨ầng⟩ | [ɤ̆ŋ˧˨] |  |
| ⟨ầu⟩ | [ɤ̆w˧˨] |  |
| ⟨ầy⟩ | [ɤ̆j˧˨] |  |
| ⟨ẩm⟩ | [ɤ̆m˧˩˨] |  |
| ⟨ẩn⟩ | [ɤ̆n˧˩˨] |  |
| ⟨ẩng⟩ | [ɤ̆ŋ˧˩˨] |  |
| ⟨ẩu⟩ | [ɤ̆w˧˩˨] |  |
| ⟨ẩy⟩ | [ɤ̆j˧˩˨] |  |
| ⟨ẫm⟩ | [ɤ̆m˧ˀ˥] |  |
| ⟨ẫn⟩ | [ɤ̆n˧ˀ˥] |  |
| ⟨ẫng⟩ | [ɤ̆ŋ˧ˀ˥] |  |
| ⟨ẫu⟩ | [ɤ̆w˧ˀ˥] |  |
| ⟨ẫy⟩ | [ɤ̆j˧ˀ˥] |  |
| ⟨ậc⟩ | [ɤ̆k˨ˀ˩] |  |
| ⟨ậm⟩ | [ɤ̆m˨ˀ˩] |  |
| ⟨ận⟩ | [ɤ̆n˨ˀ˩] |  |
| ⟨ậng⟩ | [ɤ̆ŋ˨ˀ˩] |  |
| ⟨ập⟩ | [ɤ̆p˨ˀ˩] |  |
| ⟨ật⟩ | [ɤ̆t˨ˀ˩] |  |
| ⟨ậu⟩ | [ɤ̆w˨ˀ˩] |  |
| ⟨ậy⟩ | [ɤ̆j˨ˀ˩] |  |
| ⟨ắc⟩ | [ăk˦˥] |  |
| ⟨ắm⟩ | [ăm˨˦] |  |
| ⟨ắn⟩ | [ăn˨˦] |  |
| ⟨ắng⟩ | [ăŋ˨˦] |  |
| ⟨ắp⟩ | [ăp˦˥] |  |
| ⟨ắt⟩ | [ăt˦˥] |  |
| ⟨ằm⟩ | [ăm˧˨] |  |
| ⟨ằn⟩ | [ăn˧˨] |  |
| ⟨ằng⟩ | [ăŋ˧˨] |  |
| ⟨ẳm⟩ | [ăm˧˩˨] |  |
| ⟨ẳn⟩ | [ăn˧˩˨] |  |
| ⟨ẳng⟩ | [ăŋ˧˩˨] |  |
| ⟨ẵm⟩ | [ăm˧ˀ˥] |  |
| ⟨ẵn⟩ | [ăn˧ˀ˥] |  |
| ⟨ẵng⟩ | [ăŋ˧ˀ˥] |  |
| ⟨ặc⟩ | [ăk˨ˀ˩] |  |
| ⟨ặm⟩ | [ăm˨ˀ˩] |  |
| ⟨ặn⟩ | [ăn˨ˀ˩] |  |
| ⟨ặng⟩ | [ăŋ˨ˀ˩] |  |
| ⟨ặp⟩ | [ăp˨ˀ˩] |  |
| ⟨ặt⟩ | [ăt˨ˀ˩] |  |
| ⟨ẹ⟩ | [ɛ˨ˀ˩] |  |
| ⟨ẹc⟩ | [ɛːk˨ˀ˩] |  |
| ⟨ẹm⟩ | [ɛm˨ˀ˩] |  |
| ⟨ẹn⟩ | [ɛn˨ˀ˩] |  |
| ⟨ẹng⟩ | [ɛːŋ˨ˀ˩] |  |
| ⟨ẹo⟩ | [ɛw˨ˀ˩] |  |
| ⟨ẹp⟩ | [ɛp˨ˀ˩] |  |
| ⟨ẹt⟩ | [ɛt˨ˀ˩] |  |
| ⟨ẻ⟩ | [ɛ˧˩˨] |  |
| ⟨ẻm⟩ | [ɛm˧˩˨] |  |
| ⟨ẻn⟩ | [ɛn˧˩˨] |  |
| ⟨ẻng⟩ | [ɛːŋ˧˩˨] |  |
| ⟨ẻo⟩ | [ɛw˧˩˨] |  |
| ⟨ẽ⟩ | [ɛ˧ˀ˥] |  |
| ⟨ẽm⟩ | [ɛm˧ˀ˥] |  |
| ⟨ẽn⟩ | [ɛn˧ˀ˥] |  |
| ⟨ẽng⟩ | [ɛːŋ˧ˀ˥] |  |
| ⟨ẽo⟩ | [ɛw˧ˀ˥] |  |
| ⟨ế⟩ | [e˨˦] |  |
| ⟨ếch⟩ | [ek˦˥] |  |
| ⟨ếm⟩ | [em˨˦] |  |
| ⟨ến⟩ | [en˨˦] |  |
| ⟨ếnh⟩ | [eŋ˨˦] |  |
| ⟨ếp⟩ | [ep˦˥] |  |
| ⟨ết⟩ | [et˦˥] |  |
| ⟨ếu⟩ | [ew˨˦] |  |
| ⟨ề⟩ | [e˧˨] |  |
| ⟨ềm⟩ | [em˧˨] |  |
| ⟨ền⟩ | [en˧˨] |  |
| ⟨ềnh⟩ | [eŋ˧˨] |  |
| ⟨ều⟩ | [ew˧˨] |  |
| ⟨ể⟩ | [e˧˩˨] |  |
| ⟨ểm⟩ | [em˧˩˨] |  |
| ⟨ển⟩ | [en˧˩˨] |  |
| ⟨ểnh⟩ | [eŋ˧˩˨] |  |
| ⟨ểu⟩ | [ew˧˩˨] |  |
| ⟨ễ⟩ | [e˧ˀ˥] |  |
| ⟨ễm⟩ | [em˧ˀ˥] |  |
| ⟨ễn⟩ | [en˧ˀ˥] |  |
| ⟨ễnh⟩ | [eŋ˧ˀ˥] |  |
| ⟨ễu⟩ | [ew˧ˀ˥] |  |
| ⟨ệ⟩ | [e˨ˀ˩] |  |
| ⟨ệch⟩ | [ek˨ˀ˩] |  |
| ⟨ệm⟩ | [em˨ˀ˩] |  |
| ⟨ện⟩ | [en˨ˀ˩] |  |
| ⟨ệnh⟩ | [eŋ˨ˀ˩] |  |
| ⟨ệp⟩ | [ep˨ˀ˩] |  |
| ⟨ệt⟩ | [et˨ˀ˩] |  |
| ⟨ệu⟩ | [ew˨ˀ˩] |  |
| ⟨ỉ⟩ | [i˧˩˨] |  |
| ⟨ỉa⟩ | [iə˧˩˨] |  |
| ⟨ỉm⟩ | [im˧˩˨] |  |
| ⟨ỉn⟩ | [in˧˩˨] |  |
| ⟨ỉnh⟩ | [iŋ˧˩˨] |  |
| ⟨ỉu⟩ | [iw˧˩˨] |  |
| ⟨ị⟩ | [i˨ˀ˩] |  |
| ⟨ịa⟩ | [iə˨ˀ˩] |  |
| ⟨ịch⟩ | [ik˨ˀ˩] |  |
| ⟨ịm⟩ | [im˨ˀ˩] |  |
| ⟨ịn⟩ | [in˨ˀ˩] |  |
| ⟨ịnh⟩ | [iŋ˨ˀ˩] |  |
| ⟨ịp⟩ | [ip˨ˀ˩] |  |
| ⟨ịt⟩ | [it˨ˀ˩] |  |
| ⟨ịu⟩ | [iw˨ˀ˩] |  |
| ⟨ọ⟩ | [ɔ˨ˀ˩] |  |
| ⟨ọa⟩ | [wa˨ˀ˩] |  |
| ⟨ọc⟩ | [ɔk͡p˨ˀ˩] |  |
| ⟨ọe⟩ | [wɛ˨ˀ˩] |  |
| ⟨ọi⟩ | [ɔj˨ˀ˩] |  |
| ⟨ọm⟩ | [ɔm˨ˀ˩] |  |
| ⟨ọn⟩ | [ɔn˨ˀ˩] |  |
| ⟨ọng⟩ | [ɔŋ͡m˨ˀ˩] |  |
| ⟨ọoc⟩ | [ɔːk˨ˀ˩] |  |
| ⟨ọong⟩ | [ɔːŋ˨ˀ˩] |  |
| ⟨ọp⟩ | [ɔp˨ˀ˩] |  |
| ⟨ọt⟩ | [ɔt˨ˀ˩] |  |
| ⟨ỏ⟩ | [ɔ˧˩˨] |  |
| ⟨ỏa⟩ | [wa˧˩˨] |  |
| ⟨ỏe⟩ | [wɛ˧˩˨] |  |
| ⟨ỏi⟩ | [ɔj˧˩˨] |  |
| ⟨ỏm⟩ | [ɔm˧˩˨] |  |
| ⟨ỏn⟩ | [ɔn˧˩˨] |  |
| ⟨ỏng⟩ | [ɔŋ͡m˧˩˨] |  |
| ⟨ỏong⟩ | [ɔːŋ˧˩˨] |  |
| ⟨ố⟩ | [o˨˦] |  |
| ⟨ốc⟩ | [ok͡p˦˥] |  |
| ⟨ối⟩ | [oj˨˦] |  |
| ⟨ốm⟩ | [om˨˦] |  |
| ⟨ốn⟩ | [on˨˦] |  |
| ⟨ống⟩ | [oŋ͡m˨˦] |  |
| ⟨ốp⟩ | [op˦˥] |  |
| ⟨ốt⟩ | [ot˦˥] |  |
| ⟨ồ⟩ | [o˧˨] |  |
| ⟨ồi⟩ | [oj˧˨] |  |
| ⟨ồm⟩ | [om˧˨] |  |
| ⟨ồn⟩ | [on˧˨] |  |
| ⟨ồng⟩ | [oŋ͡m˧˨] |  |
| ⟨ổ⟩ | [o˧˩˨] |  |
| ⟨ổi⟩ | [oj˧˩˨] |  |
| ⟨ổm⟩ | [om˧˩˨] |  |
| ⟨ổn⟩ | [on˧˩˨] |  |
| ⟨ổng⟩ | [oŋ͡m˧˩˨] |  |
| ⟨ỗ⟩ | [o˧ˀ˥] |  |
| ⟨ỗi⟩ | [oj˧ˀ˥] |  |
| ⟨ỗm⟩ | [om˧ˀ˥] |  |
| ⟨ỗn⟩ | [on˧ˀ˥] |  |
| ⟨ỗng⟩ | [oŋ͡m˧ˀ˥] |  |
| ⟨ộ⟩ | [o˨ˀ˩] |  |
| ⟨ộc⟩ | [ok͡p˨ˀ˩] |  |
| ⟨ội⟩ | [oj˨ˀ˩] |  |
| ⟨ộm⟩ | [om˨ˀ˩] |  |
| ⟨ộn⟩ | [on˨ˀ˩] |  |
| ⟨ộng⟩ | [oŋ͡m˨ˀ˩] |  |
| ⟨ộp⟩ | [op˨ˀ˩] |  |
| ⟨ột⟩ | [ot˨ˀ˩] |  |
| ⟨ớ⟩ | [ɤ˨˦] |  |
| ⟨ới⟩ | [ɤj˨˦] |  |
| ⟨ớm⟩ | [ɤm˨˦] |  |
| ⟨ớn⟩ | [ɤn˨˦] |  |
| ⟨ớp⟩ | [ɤp˦˥] |  |
| ⟨ớt⟩ | [ɤt˦˥] |  |
| ⟨ờ⟩ | [ɤ˧˨] |  |
| ⟨ời⟩ | [ɤj˧˨] |  |
| ⟨ờm⟩ | [ɤm˧˨] |  |
| ⟨ờn⟩ | [ɤn˧˨] |  |
| ⟨ở⟩ | [ɤ˧˩˨] |  |
| ⟨ởi⟩ | [ɤj˧˩˨] |  |
| ⟨ởm⟩ | [ɤm˧˩˨] |  |
| ⟨ởn⟩ | [ɤn˧˩˨] |  |
| ⟨ỡ⟩ | [ɤ˧ˀ˥] |  |
| ⟨ỡi⟩ | [ɤj˧ˀ˥] |  |
| ⟨ỡm⟩ | [ɤm˧ˀ˥] |  |
| ⟨ỡn⟩ | [ɤn˧ˀ˥] |  |
| ⟨ợ⟩ | [ɤ˨ˀ˩] |  |
| ⟨ợi⟩ | [ɤj˨ˀ˩] |  |
| ⟨ợm⟩ | [ɤm˨ˀ˩] |  |
| ⟨ợn⟩ | [ɤn˨ˀ˩] |  |
| ⟨ợp⟩ | [ɤp˨ˀ˩] |  |
| ⟨ợt⟩ | [ɤt˨ˀ˩] |  |
| ⟨ụ⟩ | [u˨ˀ˩] |  |
| ⟨ụa⟩ | [uə˨ˀ˩] |  |
| ⟨ục⟩ | [uk͡p˨ˀ˩] |  |
| ⟨ụi⟩ | [uj˨ˀ˩] |  |
| ⟨ụm⟩ | [um˨ˀ˩] |  |
| ⟨ụn⟩ | [un˨ˀ˩] |  |
| ⟨ụng⟩ | [uŋ͡m˨ˀ˩] |  |
| ⟨ụp⟩ | [up˨ˀ˩] |  |
| ⟨ụt⟩ | [ut˨ˀ˩] |  |
| ⟨ụy⟩ | [wi˨ˀ˩] |  |
| ⟨ụya⟩ | [wiə˨ˀ˩] |  |
| ⟨ụê⟩ | [we˨ˀ˩] |  |
| ⟨ụơ⟩ | [wɤ˨ˀ˩] |  |
| ⟨ủ⟩ | [u˧˩˨] |  |
| ⟨ủa⟩ | [uə˧˩˨] |  |
| ⟨ủi⟩ | [uj˧˩˨] |  |
| ⟨ủm⟩ | [um˧˩˨] |  |
| ⟨ủn⟩ | [un˧˩˨] |  |
| ⟨ủng⟩ | [uŋ͡m˧˩˨] |  |
| ⟨ủy⟩ | [wi˧˩˨] |  |
| ⟨ủya⟩ | [wiə˧˩˨] |  |
| ⟨ủê⟩ | [we˧˩˨] |  |
| ⟨ủơ⟩ | [wɤ˧˩˨] |  |
| ⟨ứ⟩ | [ɯ˨˦] |  |
| ⟨ứa⟩ | [ɯə˨˦] |  |
| ⟨ức⟩ | [ɯk˦˥] |  |
| ⟨ứi⟩ | [ɯj˨˦] |  |
| ⟨ứm⟩ | [ɯm˨˦] |  |
| ⟨ứn⟩ | [ɯn˨˦] |  |
| ⟨ứng⟩ | [ɯŋ˨˦] |  |
| ⟨ứt⟩ | [ɯt˦˥] |  |
| ⟨ứu⟩ | [ɯw˨˦] |  |
| ⟨ừ⟩ | [ɯ˧˨] |  |
| ⟨ừa⟩ | [ɯə˧˨] |  |
| ⟨ừi⟩ | [ɯj˧˨] |  |
| ⟨ừm⟩ | [ɯm˧˨] |  |
| ⟨ừn⟩ | [ɯn˧˨] |  |
| ⟨ừng⟩ | [ɯŋ˧˨] |  |
| ⟨ừu⟩ | [ɯw˧˨] |  |
| ⟨ử⟩ | [ɯ˧˩˨] |  |
| ⟨ửa⟩ | [ɯə˧˩˨] |  |
| ⟨ửi⟩ | [ɯj˧˩˨] |  |
| ⟨ửm⟩ | [ɯm˧˩˨] |  |
| ⟨ửn⟩ | [ɯn˧˩˨] |  |
| ⟨ửng⟩ | [ɯŋ˧˩˨] |  |
| ⟨ửu⟩ | [ɯw˧˩˨] |  |
| ⟨ữ⟩ | [ɯ˧ˀ˥] |  |
| ⟨ữa⟩ | [ɯə˧ˀ˥] |  |
| ⟨ữi⟩ | [ɯj˧ˀ˥] |  |
| ⟨ữm⟩ | [ɯm˧ˀ˥] |  |
| ⟨ữn⟩ | [ɯn˧ˀ˥] |  |
| ⟨ững⟩ | [ɯŋ˧ˀ˥] |  |
| ⟨ữu⟩ | [ɯw˧ˀ˥] |  |
| ⟨ự⟩ | [ɯ˨ˀ˩] |  |
| ⟨ựa⟩ | [ɯə˨ˀ˩] |  |
| ⟨ực⟩ | [ɯk˨ˀ˩] |  |
| ⟨ựi⟩ | [ɯj˨ˀ˩] |  |
| ⟨ựm⟩ | [ɯm˨ˀ˩] |  |
| ⟨ựn⟩ | [ɯn˨ˀ˩] |  |
| ⟨ựng⟩ | [ɯŋ˨ˀ˩] |  |
| ⟨ựt⟩ | [ɯt˨ˀ˩] |  |
| ⟨ựu⟩ | [ɯw˨ˀ˩] |  |
| ⟨ỳ⟩ | [i˧˨] |  |
| ⟨ỳa⟩ | [iə˧˨] |  |
| ⟨ỳnh⟩ | [iŋ˧˨] |  |
| ⟨ỵ⟩ | [i˨ˀ˩] |  |
| ⟨ỵa⟩ | [iə˨ˀ˩] |  |
| ⟨ỵch⟩ | [ik˨ˀ˩] |  |
| ⟨ỵnh⟩ | [iŋ˨ˀ˩] |  |
| ⟨ỵp⟩ | [ip˨ˀ˩] |  |
| ⟨ỵt⟩ | [it˨ˀ˩] |  |
| ⟨ỷ⟩ | [i˧˩˨] |  |
| ⟨ỷa⟩ | [iə˧˩˨] |  |
| ⟨ỷnh⟩ | [iŋ˧˩˨] |  |
| ⟨ỹ⟩ | [i˧ˀ˥] |  |
| ⟨ỹa⟩ | [iə˧ˀ˥] |  |
| ⟨ỹnh⟩ | [iŋ˧ˀ˥] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec has no allophone rule and no cross-word rule.
<!-- atlas:rules end -->

<!-- atlas:examples begin words="anh|bánh|bong|boong|canh|cuốc|gia|kinh|ma|mà|mai|may|quốc|uống" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "vi")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| anh | [ɛŋ˧˧] |
| bánh | [ɓɛŋ˨˦] |
| bong | [ɓɔŋ͡m˧˧] |
| boong | [ɓɔːŋ˧˧] |
| canh | [kɛŋ˧˧] |
| cuốc | [kuək˦˥] |
| gia | [za˧˧] |
| kinh | [kiŋ˧˧] |
| ma | [ma˧˧] |
| mà | [ma˧˨] |
| mai | [maj˧˧] |
| may | [măj˧˧] |
| quốc | [kwok͡p˦˥] |
| uống | [uəŋ˨˦] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Veps](vep.md) · [Home](../index.md) · [Vlax Romani →](rmy.md)
