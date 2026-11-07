# Kabyle / Taqbaylit (kab)

**Code**: `kab` | **Family**: Afro-Asiatic > Berber | **Script**: Latin (Berber alphabet)
**Quality tier**: research | **Region**: Kabylia, north-eastern Algeria (about 5 to 7 million speakers, Kossmann & Stroomer 1997, p. 461)
**Sources read**: Kossmann & Stroomer, *Berber Phonology* (1997), pp. 461-475, the primary source. Karaoui, Djeradi & Djeradi (2024), pp. 123-125. Bedar, Quellec & Tifrit (2022). Wikipedia, *Kabyle language*, as a secondary check of the alphabet only.

The defining trait of Kabyle phonology is spirantization: the lax stops become fricatives, and the tense (geminate) stops keep their closure. The spec carries the stops in the grapheme table and the fricatives in the allophone layer, so the geminates never spirantize.

## Input contract

The spec expects the standard Berber Latin alphabet: the tamaziɣt (INALCO) orthography that descends from Mouloud Mammeri's conventions. The Kabyle Wikipedia, the Kabyle press and Naït-Zerrad's teaching grammars use it. Tifinagh (neo-Tifinagh) is a secondary script for Kabyle, and the spec does not read it, so transliterate Tifinagh to the Latin orthography first.

The alphabet has 34 letters. It adds the Berberist letters ⟨ɣ ɛ č ǧ⟩ and the emphatic dotted series ⟨ṛ ṣ ḍ ṭ ẓ⟩, plus ⟨ḥ⟩, to the Latin letters.

## Letter values

| Grapheme | IPA | Note |
|:---:|:---:|:---|
| `c` | /ʃ/ | voiceless postalveolar fricative |
| `č` | /t͡ʃ/ | voiceless affricate |
| `ǧ` | /d͡ʒ/ | voiced affricate |
| `j` | /ʒ/ | voiced postalveolar fricative |
| `ɣ` | /ɣ/ | realised as the uvular [ʁ] in every position (`KAB_GH_UVULAR_REALIZATION`) |
| `x` | /χ/ | voiceless uvular fricative |
| `ḥ` | /ħ/ | voiceless pharyngeal fricative |
| `ɛ` | /ʕ/ | voiced pharyngeal fricative, the Arabic ʿayn |
| `q` | /q/ | voiceless uvular stop |
| `ṛ ṣ ḍ ṭ ẓ` | /rˤ sˤ dˤ tˤ zˤ/ | the emphatic (pharyngealized) series |
| `a i u` | /a i u/ | the three phonemic vowels |
| `e` | /ə/ | the epenthetic schwa, mostly predictable and non-phonemic |
| `b d t k g` | /b d t k ɡ/ | plain stops, which spirantize as singletons |
| `bb dd tt kk gg ḍḍ` | /bː dː tː kː ɡː dˤː/ | geminate (tense) stops, which stay stops |

Kossmann & Stroomer (1997) give three vowels /a i u/ with strongly context-dependent realisations (p. 463, §23.4.1). The schwa follows syllable structure and sonority and is mostly non-phonemic (p. 463, §23.4.2). Proto-Berber pharyngealized only ⟨ḍ⟩ and ⟨ẓ⟩, and the other emphatics came in with Arabic (p. 464, §23.4.3.1).

The vowel rules follow that context-dependence. The vowel /a/ is [æ] by default (`KAB_A_DEFAULT`) and backs to [ɑ] next to an emphatic or uvular consonant (`KAB_A_BACKING`), so axxam 'house' is [ɑχːɑm]. The vowels /i/ and /u/ lower to [ɪ ʊ] before a consonant cluster (`KAB_I_CLOSED`, `KAB_U_CLOSED`). The spec covers only part of the full vowel allophony.

## Spirantization

> "Spirantization implies the development of lax stops into fricatives, e.g., *b* becoming *β* … It reaches its culminating points in Riffian and Kabyle … Spirantization never affects tense consonants."
> Kossmann & Stroomer 1997, *Berber Phonology*, p. 466.

The spirantized values come from the Beni-Said Riffian table (ibid., pp. 468-469), and Kabyle is the other culminating system. Karaoui et al. (2024, p. 123) confirm the velar fricatives [ç ʝ] in the Kabyle fricative inventory.

| Underlying (lax) | Surface | Example |
|:---:|:---:|:---|
| /b/ | [β] | `abrid` 'path' → [æβrið] |
| /d/ | [ð] | `adrar` 'mountain' → [æðrær] |
| /t/ | [θ] | `tili` 'shade' → [θili] |
| /k/ | [ç] | `akli` → [æçli] |
| /ɡ/ | [ʝ] | `tagut` → [θæʝuθ] |
| /dˤ/ | [ðˤ] | `aḍar` 'foot' → [ɑðˤɑr] |

The lax and tense series differ in duration: "lax consonants are always realized shorter than their tense counterparts" (ibid., p. 465). Generative analyses treat the tense series as geminates, and Kabyle writes a geminate by doubling the letter.

### How the spec models it

The spec keeps the grapheme map and the allophone map apart.

1. In the grapheme map (`graphemes`), the single letters `b d t k g` map to the plain stops /b d t k ɡ/. The doubled letters map to the separate long phonemes /bː dː tː kː ɡː/.
2. In the allophone map (`allophone_rules`), the rules `KAB_SPIRANT_B`, `KAB_SPIRANT_D`, `KAB_SPIRANT_T`, `KAB_SPIRANT_K`, `KAB_SPIRANT_G` and `KAB_SPIRANT_DH_EMPH` spirantize the plain stops.

The geminates are different phoneme strings, so a rule that targets /b/ never matches /bː/. The minimal contrast shows it:

```python
>>> import orthography2ipa
>>> orthography2ipa.transcribe("ababbu", "kab")
'æβæbːu'
>>> orthography2ipa.transcribe("yedda", "kab")
'jədːæ'
>>> orthography2ipa.transcribe("tagut", "kab")
'θæʝuθ'
```

Three nasal place rules also apply: /n/ becomes [ŋ] before a dorsal (`KAB_N_VELAR_ASSIM`), [m] before a labial (`KAB_N_LABIAL_ASSIM`), and [ɲ] before /j/ (`KAB_N_PALATAL_ASSIM`).

### Where spirantization is blocked

A lax stop after certain consonants keeps its closure. The allophone layer has no negative context condition, but first-match rule order supplies one. The identity rules `KAB_BLOCK_SPIRANT_*` come before the `KAB_SPIRANT_*` rules, so a stop that matches a block rule never reaches the spirantization rule.

| Stop | Blocked after | Example | Source |
|:--|:--|:--|:--|
| /b/ | /m/, as in /nb/ → [mb] | `zembil` 'basket' → [zəmbil] | Kossmann & Stroomer 1997, p. 469, and Bedar, Quellec & Tifrit 2022 |
| /d/ | /n/, /m/, /l/ | `anda` 'where' → [ændæ], `ldi` 'open' → [ldi] | Kossmann & Stroomer 1997, pp. 468-469, and Bedar, Quellec & Tifrit 2022 |
| /t/ | /n/, /m/, and /l/ at word end | `nteddu` 'we go' → [ntədːu], `tamellalt` 'egg' → [θæməlːælt] | Kossmann & Stroomer 1997, p. 468, and Bedar, Quellec & Tifrit 2022 |
| /dˤ/ | /n/ | | Kossmann & Stroomer 1997, by analogy, and native-speaker judgment |
| /k/ | any consonant | | native-speaker judgments in the spec sources, and Bedar, Quellec & Tifrit 2022 for the sonorants |
| /ɡ/ | any consonant except /m/ | `argaz` 'man' → [ærɡæz] | native-speaker judgments in the spec sources, and Bedar, Quellec & Tifrit 2022 for the sonorants |

The blocks after /m/ for /t/ and /d/ follow the Chemini and Aït Mengellat pattern. The Boghni and Makouda pattern is not modelled as an alternative. Before /u/, /mʝ/ debuccalizes to [mh] (Bedar, Quellec & Tifrit 2022). The rule engine cannot condition a block on the following vowel, so the spec does not model it. Bedar, Quellec & Tifrit also attest /lθ lð/ → [lt ld] word-medially. The spec keeps the /t/ block after /l/ at word end only, until the medial case is confirmed.

## Known limits

- Morphophonological gemination alternations are lexical or morphological, and the Latin spelling does not show them. A geminated /ɣ/ surfaces as *qq*, a geminated /w/ as *bb*, and a geminated /y/ as *gg*.
- Sandhi across a word boundary, such as n + w → bb or pp and d + t → ts, is not modelled.
- Recent loanwords, especially French technical loans such as itiknikanen (← techniciens), can keep their stops. The spec models the native phonology without lexical exceptions.
- Stress is largely non-distinctive and predictable, and the spec does not mark it.
- The labiovelarized *kʷ gʷ* are usually unwritten in the standard orthography, and the spec does not model them.
- Tifinagh input is out of scope. Transliterate it to Latin first.

## TTS silver set

`orthography2ipa/data/gold/kabyle_tts/kab.tsv` holds phonetically diverse Kabyle sentences, each justified from the literature. It validates Kabyle TTS voices and pins the sentence-level behaviour of the spec. The [TTS silver sets](../evaluation/silver_sets.md#kabyle_tts) page describes the schema, the feature tags and the authoring steps.

## Sources

- Kossmann, Maarten G. & Stroomer, Harry J. (1997). *Berber Phonology*. In A. S. Kaye (ed.), *Phonologies of Asia and Africa*, vol. 1, pp. 461-475. Eisenbrauns. The primary source, read in full, for spirantization, lax and tense gemination, the vowels, the schwa and pharyngealization. <https://hdl.handle.net/1887/4150>
- Karaoui, F., Djeradi, A. & Djeradi, R. (2024). *Acoustic Characterization of the Noise Sources for the Kabyle Fricatives Consonants*. ICAECE'2023 abstracts, AIJR, pp. 123-125. The Kabyle fricative inventory, [ç ʝ] included.
- Bedar, A., Quellec, L. & Tifrit, A. (2022). *Post-sonorant occlusivization in Kabyle*. Speaker judgments for Chemini Kabyle, with comparative data from Aït Mengellat, Boghni and Makouda.
- Naït-Zerrad, Kamal (2001). *Grammaire moderne du kabyle / Tajerrumt tatrart n teqbaylit*. Éditions Karthala, Paris. A lexical and morphological source for the TTS silver set, not a phonological source.
- Dallet, Jean-Marie (1982). *Dictionnaire kabyle-français: parler des At Mangellat, Algérie*. SELAF, Paris. A lexical source for the TTS silver set, not a phonological source.
- Wikipedia, *Kabyle language*. A secondary check of the Berber Latin alphabet table only.

---
[← Arabic dialects](ar-dialects.md) · [Home](../index.md) · [Ancient Egyptian →](egy.md)
