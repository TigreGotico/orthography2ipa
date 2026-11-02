# Assamese (`as`)

**Code**: `as` | **Family**: Indo-European > Indo-Iranian > Indo-Aryan | **Script**: Bengali (the Assamese alphabet, an abugida) | **Quality tier**: production

The `as` spec describes Standard eastern Assamese, written in the Assamese script, which derives from the Bengali script. Assamese shares the script with Bengali but not the phonology. The spec follows Mahanta (2012) and Roy & Mahanta (2018), not the Bengali reading of the letters.

## Orthographic depth and production threshold

Assamese has a deep orthography, so the deep threshold of 0.25 PER applies (see [quality tiers](../quality_tiers.md#the-per-threshold)). The script is an abugida with an unwritten inherent vowel. It also has word-final vowel deletion and a rule that fronts a consonant cluster. The sound changes are regular once identified, but the correspondence is not shallow.

## Phonology

The spec has one alveolar plosive series. The retroflex letters ⟨ট ঠ ড ঢ ণ⟩ have merged with the dentals as /t tʰ d dʱ n/, so no /ʈ ɖ ɳ ɽ/ occurs. Mahanta (2012, p.218) counts twenty consonants and Roy & Mahanta (2018, p.2829) count twenty-three. The difference is in what each table includes. Both tables agree on the segments that the spec encodes.

Assamese has no affricates. The spec maps ⟨চ ছ⟩ to /s/ and ⟨জ ঝ য⟩ to /z zʱ/, not to the palatals that their Bengali cognates spell.

The Sanskrit sibilants ⟨শ ষ স⟩ merged to a velar fricative /x/, which is unique among Indo-Aryan languages. Before a consonant, the cluster fronts /x/ to [s]. The allophone rule `AS_X_BEFORE_CONSONANT` states this, so the spec gives `skul` for স্কুল.

The one rhotic is the approximant /ɹ/, written ⟨ৰ⟩ and ⟨ড়⟩. The aspirated ⟨ঢ়⟩ gives /ɹʱ/, and ⟨ৱ⟩ writes /w/. The letters ⟨ৰ⟩ and ⟨ৱ⟩ are where the Assamese script differs from Bengali.

The eight oral vowels are /i e ɛ u ʊ o ɔ a/, with an ATR contrast. The spec maps ⟨ও ো⟩ to /ʊ/ and ⟨এ ে⟩ to /ɛ/, not to the /o/ and /e/ that their Bengali cognates spell.

## The inherent vowel

The inherent vowel is /ɔ/. It is not pronounced after a word-final consonant letter, and the spec encodes this through `inherent_vowel_final`. The spec gives `kɔlɔm` for কলম and `ɔxɔm` for অসম.

The deletion does not apply in two cases. If the syllable has no other nucleus, the vowel stays, so a monosyllable such as ক is `kɔ`. If the deletion would leave a complex coda that Assamese does not allow, the vowel also stays, so অংক is `ɔŋkɔ` and not `ɔŋk`.

## Benchmark

Two gold rows score the spec. For the figures, see the [scoreboard](../scoreboard.md). The `wikipron` row is crowd-scraped and is the qualifying row. The `vox_communis` row is epitran-derived, so it can neither qualify nor block a promotion. It measures agreement with epitran, not with Assamese. Epitran does not model the sibilant merger, so the two golds disagree where the phonology of epitran and of Assamese differ.

## Known limitations

The spec does not match three gold conventions. The golds write ⟨ɦ⟩ for the glottal fricative, ⟨ɪ ʊ⟩ for the offglides of diphthongs, and, in `vox_communis`, ⟨ʱ⟩ on voiceless stops. The source tables print /h/, /i u/ and unaspirated stops. To match the gold notation, the spec would have to make a claim that neither source supports.

Both sources describe regressive ATR vowel harmony, which raises /ɛ ɔ ʊ/ to /e o u/ before a high vowel. The spec does not encode it. The main target of the harmony is the unwritten inherent vowel, and no rule can address that slot. The rule language also cannot state the blocking of the harmony by nasals and codas.

The spec does not encode the gemination of a consonant before the ya-phala ⟨্য⟩.

A conjunct inside a word that closes a syllable keeps its inherent vowel. The deletion needs a nucleus in the syllable that it closes, and it never makes a complex coda. So ভক্ত gives `bʱɔktɔ` and not `bʱɔkt`, and the second inherent vowel stays.

## Sources

- Mahanta, S. (2012). Assamese. *Journal of the International Phonetic Association*, 42(2).
- Roy, S. & Mahanta, S. (2018). A computational model for Assamese grapheme-to-phoneme conversion. *Interspeech 2018*.

---
[← Hindi](hi.md) · [Home](../index.md) · [Mongolian →](mn.md)
