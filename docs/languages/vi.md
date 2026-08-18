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
| `ipadict` | machine-generated | 70 899 | **0.0773** |
| `vox_communis` | epitran-derived | 2 475 | 0.5597 |

The two golds transcribe the same variety in incompatible notations,
and the gap between the rows is almost entirely that. `ipadict`'s
`vi_N` file is Northern Vietnamese and agrees with Kirby segment for
segment — the labial-velar finals, the ⟨anh⟩ = /ɛŋ/ rime, the
diphthongs, and Chao letters at the end of the syllable.
`vox_communis`'s Vietnamese comes from the VoxCommunis lexicon pipeline
and writes a pan-dialectal literary transcription instead: /c ɲ/ for
final ⟨ch nh⟩, a phonemic length mark the Illustration does not use,
˨˨ rather than ˧˧ for ngang, and the tone letters against the nucleus
rather than the syllable. Scoring the same output blind to tone drops
that row to about 0.33 and blind to tone and length to about 0.20,
which is where the real segmental disagreement sits.

Neither row can qualify the language. `machine-generated` and
`epitran-derived` are both below the gate (see
[../quality_tiers.md](../quality_tiers.md)); `epitran-derived` in
particular measures agreement with a competitor.

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
