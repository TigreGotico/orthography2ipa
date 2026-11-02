# Romanian (`ro-RO`)

**Code**: `ro-RO` | **Family**: Indo-European > Romance > Eastern Romance | **Script**: Latin (alphabet) | **Quality tier**: production

The `ro-RO` spec describes Standard Romanian (limba română standard). The registry resolves the bare tag `ro` to this spec.

## Orthographic depth and production threshold

Romanian has a shallow (phonemic) orthography, so the 0.15 PER production target applies (see [quality tiers](../specs/quality_tiers.md#the-per-threshold)). The orthography of 1993 is regular. The central vowels have their own letters: ⟨ă⟩ is /ə/, and ⟨â⟩ and ⟨î⟩ are /ɨ/. The letters ⟨c⟩ and ⟨g⟩ soften before front vowels, as in the rest of Romance.

## Phonology as encoded

Romanian has seven vowels, /a e i o u ə ɨ/. The orthography writes each central vowel with a letter of its own, so the spec reads them without ambiguity. The spec declares ⟨ă⟩ in `vowel_graphemes`, because the engine's closed inventory of Latin vowel letters does not include it. Without that declaration, a rule that tests for a neighbouring vowel would fail next to ⟨ă⟩, as in ⟨băieți⟩.

The rules `RO_SOFT_C` and `RO_SOFT_G` make ⟨c⟩ /tʃ/ and ⟨g⟩ /dʒ/ before ⟨e⟩ and ⟨i⟩. The digraphs ⟨ch⟩ and ⟨gh⟩ are graphemes of their own and keep /k/ and /ɡ/. The spec gives ⟨cer⟩ as `tʃer` and ⟨cheie⟩ as `keje`. Romanian has no intervocalic lenition, so the spec maps ⟨p t c⟩ to plain stops in every position (⟨lup⟩ gives `lup`).

The diphthongs ⟨ea⟩ /e̯a/ and ⟨oa⟩ /o̯a/ are graphemes, so ⟨soare⟩ gives `so̯are`. Two rules make ⟨i⟩ the glide [j]: `RO_I_GLIDE_INITIAL` before a vowel at the start of a word, and `RO_I_GLIDE_POSTVOCALIC` after a vowel. The plural ⟨copii⟩ gives `kopij`.

The word-final ⟨i⟩ of a plural or a second-person singular is asyllabic. The rule `RO_FINAL_I_ASYLLABIC` deletes it and palatalises the consonant before it, so ⟨lupi⟩ gives `lupʲ`. The rule `RO_FINAL_I_ASYLLABIC_LIQUID` does the same after ⟨l⟩ or ⟨r⟩, but only where the liquid is not the second member of an obstruent-liquid onset. Both rules apply only when the word keeps another vowel nucleus (Chițoran 2002, ch. 5).

Word-initial ⟨e⟩ is [je] only in a closed set. That set holds the personal pronouns ⟨eu el ea ei ele⟩ and the present and imperfect forms of ⟨a fi⟩, such as ⟨este⟩ and ⟨era⟩. These words are in `word_exceptions`, so ⟨este⟩ gives `jeste` and ⟨elev⟩ gives `elev` (DOOM3, Chițoran 2002 ch. 2).

## Stress

Romanian stress is lexical, and the standard spelling does not mark it. It has a strong default (Chițoran 2002: 75-77, tabulated in Alexei & Ulfsbjorninn 2022: 2-5). A word that ends in a consonant takes final stress (*bărbát*, *animál*). A word that ends in a falling diphthong also takes final stress (*gunói*, *biróu*). So does a word that ends in the diphthong ⟨ea⟩ [e̯a] (*cafeá*, *perdeá*, *aveá*), because that diphthong occurs only in stressed position (Alexei & Ulfsbjorninn 2022: 18). Any other word takes penultimate stress (*máre*, *feméie*, *mașínă*). The `stress` block states that default. The benchmark strips stress marks, so the block does not change the PER.

## Benchmark

Two rows can gate a promotion: `wikipron` under the bare tag `ro`, which is crowd-scraped, and `ipadict` under `ro-RO`, which is lexicon-derived. The registry and the guard test both resolve `ro` to this spec. The `vox_communis` row is epitran-derived and the `ipa_childes` row is espeak-derived. Those two rows measure agreement with another system and cannot gate. The scores are on the [scoreboard](../evaluation/generated/scoreboard.md).

## Known limitations

The stress default misses the lexically marked words. These have penultimate stress on a consonant-final word (*záhăr*, *călúgăr*), antepenultimate stress on a vowel-final word (*pépene*, *cámeră*), or final stress on a plain vowel (*macará*, *pané*). The spec lists none of them.

Inflectional endings keep the stress of the stem (Franzén & Horne 1997: 75). The engine reads the whole word, so *lupul*, *trenuri* and *caselor* take the mark one syllable late. The definite article on a noun in *-e* also writes ⟨ea⟩, so *cartea* and *mintea* take the mark on the article. The spec does not resolve homographs that differ only in stress, such as *cópii* 'copies' and *copíi* 'children'.

After ⟨c⟩ or ⟨g⟩, an ⟨i⟩ before a vowel is silent in the inherited vocabulary and syllabic in the learned layer. Examples are ⟨cioban⟩ [tʃoˈban] and ⟨Dacia⟩ [ˈdatʃi.a]. The split is lexical, not orthographic. The spec emits the syllabic reading for both, so ⟨cioban⟩ gives `tʃioban`. A caller-supplied lexicon can correct the inherited words.

The spelling before 1993 used ⟨î⟩ inside words where the standard writes ⟨â⟩. That spelling is a variant of the orthographic norm. The spec does not cover it, because orthography2ipa does not normalise its input.

The spec maps only the comma-below letters ⟨ș⟩ and ⟨ț⟩. Much Romanian text uses the cedilla letters ⟨ş⟩ (U+015F) and ⟨ţ⟩ (U+0163) in their place. The spec has no mapping for them, so the engine drops them with an `UnmappedGraphemeWarning`. So ⟨şase⟩ gives `ase` where ⟨șase⟩ gives `ʃase`. A caller must convert the cedilla letters to comma-below before transcription.

## Sources

- Mallinson, G. (1986). *Romanian*. Croom Helm Descriptive Grammars.
- Deletant, D. & Alexandrescu, I. (1983). *Teach Yourself Romanian*. Hodder & Stoughton.
- Ladefoged, P. & Maddieson, I. (1996). *The Sounds of the World's Languages*. Blackwell.
- Chițoran, I. (2002). *The Phonology of Romanian: A Constraint-based Approach*. Mouton de Gruyter.
- Alexei, S. & Ulfsbjorninn, S. (2022). Metrical exceptionality and stress shift in Romanian nouns and adjectives. *Isogloss* 8(1)/4, 1-29.
- Franzén, V. & Horne, M. (1997). Word stress in Romanian. *Lund University Working Papers* 46, 75-91.
- Academia Română (2021). *Dicționarul ortografic, ortoepic și morfologic al limbii române* (DOOM3). Univers Enciclopedic.

---
[← Spanish](es-ES.md) · [Home](../index.md) · [French →](fr-FR.md)
