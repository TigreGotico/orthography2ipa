# Assamese (`as`)

Standard eastern Assamese, written in the Bengali-derived Assamese script.
Assamese shares its script with Bengali but not its phonology, and the
spec below follows Mahanta (2012) and Roy & Mahanta (2018) rather than
the script's Bengali reading.

## Orthographic depth and production threshold

**Deep orthography, the ≤ 0.25 PER production threshold applies** (see
[quality tiers](../quality_tiers.md)). An abugida with an unwritten
inherent vowel, word-final vowel deletion, and a consonant cluster
fronting rule is not a shallow correspondence, even though the sound
changes involved are regular once identified.

## Phonology (as encoded)

- Twenty consonants, one alveolar plosive series only: the retroflex
  series written as ⟨ট ঠ ড ঢ ণ⟩ has neutralised with the dentals to
  /t tʰ d dʱ n/, so no /ʈ ɖ ɳ ɽ/ occurs. Mahanta (2012, p.218) and
  Roy & Mahanta (2018, p.2829) count this inventory as twenty and
  twenty-three consonants respectively, a difference in what each
  paper's table includes rather than a disagreement about the segments
  themselves; both tables agree on the segments the spec encodes.
- No affricates: ⟨চ ছ⟩ are /s/ and ⟨জ ঝ য⟩ are /z zʱ/ rather than the
  palatals their Bengali cognates spell.
- The Sanskrit sibilants ⟨শ ষ স⟩ merged to a velar fricative /x/,
  unique among Indo-Aryan languages, with cluster-fronting to [s]
  before a following consonant (`AS_X_BEFORE_CONSONANT`).
- The one rhotic is the approximant /ɹ/, written ⟨ৰ⟩ and ⟨ড়⟩ (the
  aspirated ⟨ঢ়⟩ gives /ɹʱ/); ⟨ৱ⟩ writes /w/. These two letters are the
  script's own point of departure from Bengali.
- Eight oral vowels /i e ɛ u ʊ o ɔ a/ with an ATR contrast; ⟨ও ো⟩ write
  /ʊ/ and ⟨এ ে⟩ write /ɛ/, not the /o/ and /e/ their Bengali cognates
  spell.
- The inherent vowel is /ɔ/ and is not pronounced on a word-final
  consonant letter, encoded through `inherent_vowel_final`. The
  deletion is skipped where the syllable being closed has no nucleus
  (a monosyllable keeps its vowel: ⟨ক⟩ stays /kɔ/) or would leave a
  complex coda the language does not allow (⟨অংক⟩ stays /ɔŋkɔ/, not
  */ɔŋk/); see Known limitations for what this floor does to a
  word-medial conjunct.

## Benchmark (full gold set, no cap)

| dataset | provenance | n | PER |
|---|---|---:|---:|
| `wikipron` | crowd-scraped | 2981 | **0.0918** |
| `vox_communis` | epitran-derived | 5328 | 0.2436 |

The qualifying row is `wikipron`. `vox_communis` is epitran-derived and
can neither qualify nor block promotion; it measures agreement with
epitran rather than with Assamese, and epitran does not model the
sibilant merger, so the two golds disagree exactly where epitran's own
phonology and Assamese's diverge.

## Known limitations

- Three gold transcription conventions are not matched: ⟨ɦ⟩ for the
  glottal fricative, ⟨ɪ ʊ⟩ as diphthong offglides where the sources
  analyse /i u/, and vox_communis's ⟨ʱ⟩ marking aspiration on voiceless
  stops. Both source tables print /h/, /i u/ and unaspirated stops
  respectively; matching the gold notation instead would put a claim
  in the spec that neither source supports.
- Regressive ATR vowel harmony (raising /ɛ ɔ ʊ/ to /e o u/ before a
  following high vowel) is described by both sources and is not
  encoded: its principal target is the unwritten inherent vowel, which
  has no slot a rule can address, and the harmony's nasal and coda
  blocking cannot be stated in the current rule language.
- Gemination of a consonant before ya-phala ⟨্য⟩ is not encoded.
- A word-medial conjunct that closes a syllable keeps its inherent
  vowel, because deletion is gated on the syllable being closed having
  a nucleus and never manufactures a complex coda: ভক্ত gives
  /bʱɔktɔ/, not */bʱɔkt/, retaining the second inherent vowel even
  though it is not word-final in the orthography the way the rule
  usually targets.

## Sources

- Mahanta, S. (2012). Assamese. *Journal of the International Phonetic
  Association*, 42(2).
- Roy, S. & Mahanta, S. (2018). A computational model for Assamese
  grapheme-to-phoneme conversion. *Interspeech 2018*.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)
