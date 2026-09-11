# Vietnamese (`vi`)

Northern (Hanoi) Vietnamese in chữ quốc ngữ. Austroasiatic, Vietic
branch. The reference throughout is Kirby (2011), the IPA Illustration
for exactly this variety, cited in the spec's `sources` as
`kirby2011`.

Vietnamese is the library's first spec that **emits tone**. It can,
because quốc ngữ writes all six tones: the tone category of a syllable
is recoverable from its spelling with no lexicon and no ambiguity.

## The unit of mapping is the rime, not the letter

A quốc ngữ syllable is an onset spelling, a rime (vần) spelling, and a
tone diacritic sitting on one letter inside the rime. Almost everything
irregular about the orthography lives in the rime, and it is regular
*as a rime*: ⟨anh⟩ is /ɛŋ/ and ⟨ong⟩ is /ɔŋ͡m/ whatever onset precedes
them. So the spec maps whole toned rimes. `scripts/gen_vietnamese.py`
composes that table from four small inputs — the nucleus inventory, the
coda inventory, the allophony relating them, and the tone paradigm —
and writes the `graphemes` and `allophones` blocks of `vi.json`. Edit
the script, never the generated blocks.

The rules the script applies, all from Kirby (2011):

- **Velar fronting.** ⟨anh ach⟩ are /ɛŋ ɛk/, ⟨ênh êch⟩ /eŋ ek/, ⟨inh
  ich⟩ /iŋ ik/. These are velars, not the palatals /ɲ c/ of literary
  Vietnamese; phonetically they are pre-velar [ŋ̟ k̟], a narrow detail
  the spec does not write.
- **Labial-velar finals.** After the rounded vowels /u o ɔ/ the velar
  stops are doubly articulated: ⟨ung ông ong⟩ /uŋ͡m oŋ͡m ɔŋ͡m/, ⟨úc ốc
  óc⟩ /uk͡p ok͡p ɔk͡p/. The rule is stated over the rounded
  *monophthongs*, so the diphthong /uə/ falls outside it and ⟨uống⟩ is
  /uəŋ/. ⟨oo⟩ in French loans (⟨boong⟩, ⟨xoong⟩) is Kirby's named
  exception and keeps a plain velar.
- **Short vowels.** ⟨ă⟩ and ⟨â⟩ spell the short /ă ɤ̆/ — the only two
  length contrasts in the vowel system — and ⟨ay au ây âu⟩ spell them
  too, which is what separates ⟨may⟩ /măj/ from ⟨mai⟩ /maj/.
- **Diphthongs.** ⟨iê/ia⟩, ⟨uô/ua⟩ and ⟨ươ/ưa⟩ are one falling
  diphthong each — /iə uə ɯə/ — and the spelling alternation tracks
  nothing but the presence of a coda.
- **The ⟨gi⟩ collapse.** After the onset ⟨gi⟩, a rime that begins with
  ⟨i⟩ is written with a single ⟨i⟩: ⟨gi⟩ + ⟨ìn⟩ is ⟨gìn⟩ /zin/ and ⟨gi⟩
  + ⟨iếng⟩ is ⟨giếng⟩ /ziəŋ/. One rule covers both. ⟨gia⟩ is the
  exception the orthography itself makes — it spells ⟨gi⟩ + ⟨a⟩ /za/,
  and the /ziə/ rime is simply not written after ⟨gi⟩.
- **Merged onsets.** ⟨tr⟩ and ⟨ch⟩ are both /tɕ/ in modern Hanoi
  speech, ⟨s⟩ and ⟨x⟩ both /s/, and ⟨d gi r⟩ all /z/. ⟨g gh⟩ is the
  fricative /ɣ/, and ⟨b đ⟩ are the implosives /ɓ ɗ/. Southern
  Vietnamese keeps several of these distinctions; it is a different
  spec and is not described here.

## Tone

Kirby's analysis is eight tones: a six-tone paradigm on open and
sonorant-final syllables, and a two-tone paradigm on syllables closed
by an unreleased oral stop, where only the sắc-spelled (D1) and
nặng-spelled (D2) tones occur. The spec follows it, which is why a
checked rime carries two readings and every other rime carries six, and
why no reading at all exists for spellings like ⟨màt⟩ that the
tone–coda restriction forbids.

| Diacritic | Name | Kirby's code | Chao letters |
|:---|:---|:---|:---|
| unmarked | ngang | A1 | ˧˧ |
| ◌̀ | huyền | A2 | ˧˨ |
| ◌́ | sắc | B1 / D1 | ˨˦, ˦˥ when checked |
| ◌̉ | hỏi | C1 | ˧˩˨ |
| ◌̃ | ngã | C2 | ˧ˀ˥ |
| ◌̣ | nặng | B2 / D2 | ˨ˀ˩ |

The letters come after the coda, because the tone belongs to the
syllable: ⟨bánh⟩ is /ɓɛŋ˨˦/.

**The Chao letters are notation, the categories are the claim.** Kirby
transcribes these tones with IPA tone staves and names their contours;
the numeric renderings above are the widely cited Hanoi values, chosen
so the benchmark measures whether the spec derives the right tone
*category* instead of measuring a notation gap. Voice quality is not
transcribed, following Kirby's own reasoning that IPA diacritics cannot
express the temporal alignment of glottalisation against pitch.

## Benchmark (full gold set, no cap)

| dataset | provenance | n | PER |
|---|---|---:|---:|
| `ipadict` | machine-generated | 70 899 | **0.0777** |
| `vox_communis` | epitran-derived | 2 475 | 0.5596 |

The two golds transcribe the same variety in incompatible notations,
and the gap between the rows is almost entirely that. `ipadict`'s
`vi_N` file is Northern Vietnamese and agrees with Kirby segment for
segment — the labial-velar finals, the ⟨anh⟩ = /ɛŋ/ rime, the
diphthongs, and Chao letters at the end of the syllable.
`vox_communis`'s Vietnamese comes from the VoxCommunis lexicon pipeline
and writes a pan-dialectal literary transcription instead: /c ɲ/ for
final ⟨ch nh⟩, a phonemic length mark the Illustration does not use,
˨˨ rather than ˧˧ for ngang, and the tone letters against the nucleus
rather than the syllable. That row is therefore notation-dominated rather
than phonological, and `scripts/fold_vi_notation.py` puts a number on
each convention by folding it out of both sides and re-scoring:

| fold applied (cumulative, both sides) | PER |
|---|---:|
| as scored | 0.5596 |
| tone letters | 0.3277 |
| + vowel length ⟨ː⟩ | 0.1994 |
| + unreleased-stop mark ⟨◌̚⟩ | 0.1715 |
| + tie bar ⟨ŋ͡m k͡p⟩ | 0.1715 |
| + ⟨ɨ⟩ ~ ⟨ɯ⟩ for ⟨ư⟩ | 0.1449 |
| + short vowels ⟨ă ɤ̆⟩ ~ ⟨a ə⟩ | 0.0398 |
| + palatal ⟨ɲ c⟩ ~ pre-velar ⟨ŋ k⟩ finals | 0.0246 |
| + vowel height ⟨ɛ ɔ⟩ ~ ⟨e o⟩ | 0.0246 |

Under 3 of the 56 PER points are a disagreement about Vietnamese; the
rest is how the two sides spell the same analysis. Two of those folds
move nothing at all, which is itself informative: the harness's
`normalize()` already strips the tie bar, so none survives to the scorer
on either side, and the ⟨ɛ ɔ e o⟩ heights differ on only 71 of the 2 475
words — too few to move the fourth decimal. Neither is a real source of
distance, and both are listed so a later reader does not look for them
again.

Both golds do write tone — about a third of `vox_communis`'s gold
characters carry a tone mark, and about 37% of `ipadict`'s — so what
separates them is placement and scale, not omission. Placement is the
larger half: 1 905 of the 2 468 toned gold words (77.2%) put the tone
letters inside the rime, before the coda (⟨tôi⟩ `toː˨˨j`), where this
spec writes them after the syllable.

**The `vox_communis` tone tier also merges two contrastive tones**, which
is a defect rather than a convention. It writes the same letter ˨˨ for
ngang (566 of 590 words) and for huyền (401 of 406) — 967 words, 39.1% of
the row. Kirby (2011: 386) tabulates them as separate categories, A1
(level) and A2 (mid falling), on the minimal pair *ma* 'ghost' / *mà*
'but, yet'. This spec distinguishes them and is charged edit distance for
doing so. The gold's other tone splits are principled and match the spec's
analysis: sắc and nặng each split by coda (˨˦/˦˥ and ˨˩ˀ/˨˩), which is
Kirby's D1/D2 coda-tone restriction.

The finals are the one genuine analytical disagreement, and the cited
source settles it against the gold. Kirby (2011: 383), under "Velar
fronting", names the palatal reading and rejects it: the stops after
/i e ɛ/ "are actually pre-velar [ŋ̟] and [k̟], with no point of alveolar
contact (Henderson 1965)", transcribing ⟨canh⟩ [kɛŋ] and ⟨sách⟩ [sɛk].

Neither row can qualify the language, and the `vox_communis` row cannot
block it either. `epitran-derived` is in `NON_QUALIFYING_TIERS`, so
`can_gate_promotion` returns False for it and the row has no vote in
either direction — which is the right outcome for a gold that merges two
phonemic tones, and is already what the dataset-wide tier delivers.

It is worth being explicit about why this row is **not** reclassified,
because the tier names invite the mistake. `RELIABILITY_TIERS` is an
ordered tuple and `machine-generated` sits above `epitran-derived` in it,
so moving this row to `machine-generated` reads like a downgrade. It is
the opposite: gating is decided by membership of `NON_QUALIFYING_TIERS`,
not by position in the tuple, and `machine-generated` is not a member. A
row moved there would gain a gating vote. The row stays `epitran-derived`
and the finding lives in prose, here. Nothing about the Vietnamese spec
should be read off it in either direction.

## Where this disagrees with the gold

Three disagreements are deliberate and worth stating, because they cost
PER on the `ipadict` row.

⟨giếng giêng giết giễu⟩ come out /ziəŋ ziəŋ ziət ziəw/ here and
/zeŋ zeŋ zet zew/ in the gold, which reads the letters left over after
⟨gi⟩ as rimes ⟨êng êt êu⟩ of their own. Those rimes are otherwise
unattested, the ⟨gi⟩ collapse is not special to a bare ⟨i⟩, and
Wiktionary gives [ziəŋ] and [ziət] for Hà Nội, so the collapse wins.

⟨quốc⟩ is /kwok͡p/ and ⟨cuốc⟩ /kuək/. They look like they should be
homophones, and the difference is real rather than an artifact: ⟨qu⟩
takes the medial, leaving ⟨ôc⟩ with a rounded monophthong nucleus that
triggers the labial-velar final, while ⟨cuốc⟩'s nucleus is the
diphthong /uə/, which the rule excludes. The gold makes the same split.

⟨b đ⟩ are the implosives /ɓ ɗ/ and the merged ⟨tr ch⟩ onset is the
affricate /tɕ/, both per Kirby. The gold writes plain ⟨b d⟩ and a plain
⟨c⟩. `vox_communis` writes ⟨ɓ⟩, so the two golds disagree and the
Illustration decides it.

## Known limitations

- **Northern only.** The Southern mergers and splits (⟨d gi⟩ vs ⟨r⟩,
  ⟨s⟩ vs ⟨x⟩, ⟨tr⟩ vs ⟨ch⟩, final palatals) are a separate variety and
  are not modelled.
- **No zero-onset glottal stop.** Kirby counts /ʔ/ as the onset of a
  vowel-initial syllable; the spec emits nothing there, matching both
  golds.
- **Voice quality is not written**, per Kirby's own argument.
- **Pre-velar fronting is not written**: ⟨kinh⟩ is /kiŋ/, not [kiŋ̟].
- **⟨oo⟩ loses its length.** Kirby's minimal pair for the plain-velar
  exception is [bɔŋ͡m] ⟨bong⟩ against [bɔːŋ] ⟨boong⟩; the spec writes
  the plain velar but not the long vowel, so the two differ only in the
  final. Length is not contrastive anywhere else in the vowel system
  except for /a/ and /ɤ/, which ⟨ă â⟩ already spell.
- **The letter names ⟨ă⟩ and ⟨â⟩ have no reading.** Neither is a
  syllable — both nuclei require a coda — so the three `ipadict`
  entries that are just those letters transcribe empty and drop out of
  the covered count.
- **Foreign spellings** outside the quốc ngữ rime inventory
  (transliterated proper nouns, unassimilated loans) have no rime to
  match and fall back to letter-by-letter reading.

---
[← Finnish](fi.md) · [Home](../index.md) · [Standard Thai →](th.md)
