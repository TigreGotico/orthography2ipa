# Iraqi Arabic (ar-IQ gilit and ar-IQ-x-qeltu) — Phonology Reference

**Codes**: `ar-IQ` (Baghdad Muslim / southern **gilit**), `ar-IQ-x-qeltu` (Northern
**qəltu** — Mosul/Muslawi, Tikrit, and the Jewish and Christian communal dialects of
Baghdad)
**Family**: Semitic | **Script**: Arabic (abjad) | **Quality tier**: research

---

## The gilit/qəltu communal-dialect distinction

The **gilit/qəltu split is the defining Mesopotamian isogloss**. It is named after the
reflex of the word *"I said"*: Muslim Baghdad says **gilit**, while Mosul and the Jewish
and Christian communities of Baghdad say **qəltu**. Haim Blanc's *Communal Dialects in
Baghdad* (1964) — the foundational study, based on 1957–1962 fieldwork — showed that in
Baghdad the dialect boundary is **communal, not merely geographical**: the Muslim
majority speak a gilit (Bedouin-type) dialect, whereas the Jewish and Christian
minorities speak qəltu (sedentary) dialects that pattern with Mosul and the wider
northern Mesopotamian area (Blanc 1964, §2, §7).

`ar-IQ` models the gilit type; `ar-IQ-x-qeltu` inherits it and declares only the qəltu
deltas.

## Input contract

Like all Arabic specs, both varieties assume **fully-diacritized (tashkeel-marked)**
input. Dialectal Arabic is normally written defectively, so short vowels, gemination
(shadda) and sukūn surface only where they are actually written. Undiacritized text is
not disambiguated — this is a documented contract, not a bug.

## Inheritance structure

```
arb → ar-x-mashriqi → ar-IQ (gilit) → ar-IQ-x-qeltu (qəltu)
```

The gilit reflexes and allophone rules live on `ar-IQ`; `ar-IQ-x-qeltu` overrides the
qaf grapheme (→ /q/) and suppresses the inherited affrication rules by id, keeping the
shared interdental retention and emphatic backing.

## The defining reflex: OA qaf ق

| Variety | qaf reflex | Example (vocalised) | Source (read) |
|:---|:---|:---|:---|
| **gilit** (`ar-IQ`) | **[ɡ]** — voiced velar (Bedouin origin) | قَالَ → `ɡaːla` 'he said' | Blanc 1964 §3.26, p.26–27; Jasim 2020 §2.4 |
| **qəltu** (`ar-IQ-x-qeltu`) | **[q]** — voiceless uvular, retained | قَالَ → `qaːla` | Blanc 1964 §3.26; Jasim 2020 §2.4 |

Blanc (§3.26): *"In J and C, the reflex of OA/q/ is, in practically every instance, /q/;
in M, it is usually /g/ … JC/qal/, M/gal/ 'to say'."* Jasim (§2.4): the /q/ of Muslawi
Qəltu *"is realised as the voiced velar stop [ɡ] in Baghdadi Gilit"*. MSA-learned words
keep /q/ even in gilit (e.g. القرآن), but this is not orthographically separable.

## Other modelled features

| Feature | gilit `ar-IQ` | qəltu `ar-IQ-x-qeltu` | Source (read) |
|:---|:---|:---|:---|
| **kaf ك affrication** | → **[tʃ]** adjacent to a front vowel (`IQ_GILIT_AFFRIC_K_*`): كِيلو → `tʃiːlw`, دِيك → `diːtʃ` | **[k]** retained — /k/ and /tʃ/ are separate phonemes, no allophony | Blanc 1964 §3.25, p.25; Jasim 2020 §2.9.2 |
| **qaf-reflex /ɡ/ affrication** | /ɡ/ → **[dʒ]** before a front vowel (`IQ_GILIT_AFFRIC_G_*`): قِرْد → `dʒird` | n/a (qaf → /q/) | Blanc 1964 §3.26, p.28 |
| **Interdentals /θ ð ðˤ/** | **retained** (ثَلْج → `θaldʒ`) | **retained** (Mosul/Jewish) | Blanc 1964 §3.2; Jasim 2020 §2.4 |
| **jim ج** | **[dʒ]** (retained) | **[dʒ]** | Blanc 1964; ar-x-mashriqi default |
| **Emphatic backing (tafxim)** | /a aː/ → **[ɑ ɑː]** adjacent to /tˤ dˤ sˤ ðˤ/ (`IQ_EMPH_*`): طَالِب → `tˤɑːlib` | inherited (Muslawi tafxim) | Jasim 2020 (thesis topic); Blanc 1964 §3.3 |

The gilit kaf affrication modelled here is the **phonetically-conditioned** part (kaf
adjacent to a front vowel). The fully **lexicalised** gilit affrication — M/čan/ < kān,
M/čalb/ < kalb, where the historical trigger vowel is no longer present — is not
predictable from the orthography and is a documented **engine limit**, not captured.

## Documented sub-variety limits (not modelled)

- **Christian Baghdadi** merges the interdentals to dental stops (θ→t, ð→d, ðˤ→dˤ) while
  preserving /q/ (Blanc 1964 §3.2; Jasim 2020 §2.3). This split from Mosul/Jewish qəltu
  (which retain the interdentals) is not orthographically separable, so the
  retained-interdental majority reflex is modelled and the Christian merger documented.
- **OA /r/ → [ʁ]~[ɣ]** (uvular/velar) in many Muslawi and Jewish/Christian-Baghdadi
  instances (Blanc 1964 §3.24, *M/ras/ ~ JC/ɣas/* 'head'; Jasim 2020 §2.4). This is
  lexically conditioned and not predictable from the orthography, so it is documented
  rather than applied as a blanket rule.

## Sources

**Read for this reference** (page-cited above):

- **Blanc, H. (1964)** *Communal Dialects in Baghdad*, Harvard Middle Eastern Monographs
  X, Harvard University Press. The foundational gilit/qəltu and
  Muslim–Jewish–Christian analysis. Read via OCR full text; §3.24–3.26, §3.2–3.3.
- **Jasim, M. (2020)** *Tafxiːm in the vowels of Muslawi Qəltu and Baghdadi Gilit
  dialects of Arabic*, PhD thesis, Newcastle University. Modern acoustic study directly
  contrasting the two varieties; §2.3, §2.4, §2.9.2.

**Not obtained** (listed for completeness, no claim sourced to it): Erwin, W.M. (1963)
*A Short Reference Grammar of Iraqi Arabic*, Georgetown University Press — the standard
descriptive grammar of gilit Baghdadi, library/paywall only for this pass.
