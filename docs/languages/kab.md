# Kabyle / Taqbaylit (kab) — Phonology Reference

**Code**: `kab` | **Family**: Afroasiatic (Northern Berber / Amazigh) | **Script**: Latin (Berber alphabet)
**Quality tier**: research | **Region**: Kabylia, north-eastern Algeria (~5–7 million speakers)
**Sources read**: Kossmann & Stroomer, *Berber Phonology* (1997), pp. 461–475 (**primary**); Karaoui, Djeradi & Djeradi, *Acoustic Characterization of the Noise Sources for the Kabyle Fricatives* (2024), pp. 123–125; Wikipedia, *Kabyle language* (secondary orthography cross-check, flagged).

---

## Input contract

This spec expects text in the **standardised Berber Latin alphabet** — the
*tamaziɣt* / INALCO orthography descending from Mouloud Mammeri's conventions,
the everyday spelling of the Kabyle Wikipedia, the Kabyle press, and
Naït-Zerrad's teaching grammars. **Tifinagh** (neo-Tifinagh) is a *secondary*
script for Kabyle and is **not** modelled: transliterate Tifinagh to the Latin
orthography first.

The alphabet is a 34-letter Latin system that adds the Berberist letters
⟨ɣ⟩, ⟨ɛ⟩, ⟨č⟩, ⟨ǧ⟩ and the emphatic dotted series ⟨ṛ ṣ ḍ ṭ ẓ⟩ (plus ⟨ḥ⟩).

---

## Hallmark grapheme → IPA correspondences

| Grapheme | IPA | Note |
|:---:|:---:|:---|
| `c` | /ʃ/ | voiceless postalveolar fricative |
| `č` | /t͡ʃ/ | voiceless affricate |
| `ǧ` | /d͡ʒ/ | voiced affricate |
| `j` | /ʒ/ | voiced postalveolar fricative |
| `ɣ` | /ɣ/ | voiced dorsal fricative (uvular [ʁ] realisation) |
| `x` | /χ/ | voiceless uvular fricative |
| `ḥ` | /ħ/ | voiceless pharyngeal fricative |
| `ɛ` | /ʕ/ | voiced pharyngeal fricative (Arabic *ʿayn*) |
| `q` | /q/ | voiceless uvular stop |
| `ṛ ṣ ḍ ṭ ẓ` | /rˤ sˤ dˤ tˤ zˤ/ | **emphatic (pharyngealized) series** |
| `a i u` | /a i u/ | the three phonemic vowels (wide allophony: a[a~ɑ~æ], i[e~i], u[o~u]) |
| `e` | /ə/ | the epenthetic schwa — largely predictable, mostly non-phonemic |
| `b d t k g` | /b d t k ɡ/ | plain stops — **spirantize as singletons** (see below) |
| `bb dd tt kk gg` | /bː dː tː kː ɡː/ | geminate (tense) stops — stay stops |

Vowels, schwa and the pharyngealization contrast are taken from Kossmann &
Stroomer (1997): three vowels /a i u/ with strongly context-dependent
realisation (p. 463 §23.4.1); schwa placed by syllable structure / sonority
and mostly non-phonemic (p. 463 §23.4.2); Proto-Berber pharyngealized only
⟨ḍ⟩ and ⟨ẓ⟩, the rest of the emphatics being Arabic-integrated (p. 464
§23.4.3.1).

---

## The signature feature: spirantization

Kabyle's defining phonological trait is **spirantization**: the lax
(non-geminate) stops weaken to fricatives, while the tense (geminate) stops
keep their occlusion.

> "Spirantization implies the development of **lax stops into fricatives**,
> e.g., *b* becoming *β* … It reaches its **culminating points in Riffian and
> Kabyle** … **Spirantization never affects tense consonants**."
> — Kossmann & Stroomer 1997, *Berber Phonology*, p. 466.

The spirantized values (ibid. pp. 468–469, Beni-Said Riffian table, of which
Kabyle is the co-culminating system; the velar fricatives [ç ʝ] are also
confirmed in the Kabyle fricative inventory by Karaoui et al. 2024, p. 123):

| Underlying (lax) | Surface | Example |
|:---:|:---:|:---|
| /b/ | [β] | `taqbaylit` → [θaqβajliθ] |
| /d/ | [ð] | `adrar` "mountain" → [aðrar] |
| /t/ | [θ] | `tili` "shade" → [θili] |
| /k/ | [ç] | `akli` → [açli] |
| /ɡ/ | [ʝ] | `argaz` "man" → [arʝaz] |
| /dˤ/ | [ðˤ] | `aḍar` "foot" → [aðˤar] |

The lax : tense (geminate) opposition is durational — "lax consonants are
always realized shorter than their tense counterparts" (ibid. p. 465), and
generative analyses treat the tense series as geminates. Kabyle writes the
geminate by **doubling the letter** (`bb dd tt kk gg ḍḍ`).

### How the mechanism is modelled

The spec keeps the *two-maps* separation:

1. **Grapheme map** (`graphemes`): the single letters `b d t k g` map to the
   plain stop phonemes `/b d t k ɡ/`; the doubled letters `bb dd tt kk gg`
   map to the **distinct long phonemes** `/bː dː tː kː ɡː/`.
2. **Allophone map** (`allophone_rules`): five post-lexical rewrites
   (`KAB_SPIRANT_B/D/T/K/G`, plus `KAB_SPIRANT_DH_EMPH`) spirantize the plain
   stop phonemes.

Because the geminates are a *different phoneme string* (`/bː/` ≠ `/b/`), the
spirantization rules — which target `/b d t k ɡ/` — are **automatically
gemination-conditioned** and never touch the geminates. This is visible in a
minimal contrast:

```python
import orthography2ipa
orthography2ipa.transcribe("ababbu", "kab")   # 'aβabːu'  — single b → [β], geminate bb → [bː]
orthography2ipa.transcribe("yedda",  "kab")   # 'jədːa'   — geminate dd stays [dː], not [ð]
orthography2ipa.transcribe("argaz",  "kab")   # 'arʝaz'   — g → [ʝ]
```

The context-free grapheme path (`PhonetokTokenizer.ipa_best`) deliberately
leaves the stops intact (`argaz` → `arɡaz`), proving the spirantization lives
in the allophone layer rather than the base map.

Two further post-lexical rules handle **nasal place assimilation**:
`/n/ → [ŋ]` before a dorsal and `/n/ → [m]` before a labial.

---

## Known limits (documented, not modelled)

- **Post-nasal blocking.** Spirantization is blocked when the stop is preceded
  by a homorganic nasal (clusters *nt*, *nd*; Kossmann & Stroomer 1997 p. 468).
  The allophone-rule layer cannot express a *negative* context condition, so a
  stop after a homorganic nasal is currently over-spirantized. This is a small
  residue in running text.
- **Morphophonological gemination alternations.** Geminated /ɣ/ surfaces as
  *qq*, geminated /w/ as *bb*, geminated /y/ as *gg*. These are lexical /
  morphological, not recoverable from the Latin spelling, and are not modelled.
- **Stress** is largely non-distinctive and predictable in Kabyle, and is not
  marked here.
- **Labiovelarized** *kʷ gʷ* are usually left unwritten in the standard
  orthography and are not modelled.
- **Tifinagh** input is out of scope (transliterate to Latin first).

---

## Sources

- **Kossmann, Maarten G. & Stroomer, Harry J. (1997).** *Berber Phonology.* In
  A. S. Kaye (ed.), *Phonologies of Asia and Africa*, vol. 1, pp. 461–475.
  Eisenbrauns. (Primary; read in full — spirantization, lax/tense gemination,
  vowels, schwa, pharyngealization.)
  <https://hdl.handle.net/1887/4150>
- **Karaoui, F.; Djeradi, A.; Djeradi, R. (2024).** *Acoustic Characterization
  of the Noise Sources for the Kabyle Fricatives Consonants.* ICAECE'2023
  abstracts, AIJR, pp. 123–125. (Kabyle fricative inventory incl. [ç ʝ];
  spirantization / palatalization / affrication as Kabyle features.)
- **Wikipedia, *Kabyle language*** — secondary cross-check (flagged) of the
  34-letter Berber Latin alphabet table only.
