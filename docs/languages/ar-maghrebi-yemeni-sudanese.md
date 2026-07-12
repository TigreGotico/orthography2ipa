# Peripheral Arabic — Maghrebi, Ṣanʿānī Yemeni, and Sudanese — Phonology Reference

**Codes**: `ar-x-maghrebi` (Proto-Maghrebi node) → `ar-MA` (Moroccan Darija),
`ar-DZ` (Algerian), `ar-TN` (Tunisian), `ar-LY` (Libyan), `ar-MR` (Mauritanian
Hassaniya); `ar-YE` (Ṣanʿānī Yemeni); `ar-SD` (Sudanese, Khartoum koine)
**Family**: Afro-Asiatic > Semitic | **Script**: Arabic (abjad) | **Quality tier**: research
(`ar-MA`, `ar-YE`, `ar-SD`), skeleton (`ar-DZ`, `ar-TN`, `ar-LY`, `ar-MR`,
`ar-x-maghrebi`)

---

## Input contract

Like every Arabic spec, all varieties here assume **fully-diacritized
(tashkeel-marked)** input. Dialectal Arabic is normally written defectively, so
short vowels, gemination (shadda) and sukūn surface only where they are actually
written. Undiacritized text is not disambiguated — this is a documented contract,
not a bug. This matters most for the Maghreb, where the defining trait is
short-vowel *deletion*: the engine transcribes the vowels that are written and
lists reduction alternates in the allophone layer rather than deleting from
orthography.

## Inheritance structure

```
arb → ar-x-maghrebi → ar-MA / ar-DZ / ar-TN / ar-LY / ar-MR
arb → ar-x-peninsular → ar-YE
arb → ar-x-mashriqi → ar-SD
```

The shared sedentary-Maghrebi reflexes (jim → /ʒ/, interdental merger, qaf → /q/,
`پ`/`ڤ` for /p v/) live on the **`ar-x-maghrebi`** parent, so every country node
inherits them and declares only its deltas. `ar-YE` and `ar-SD` inherit from the
Peninsular and Mashriqi nodes respectively.

## The Maghreb: jim ج → [ʒ] and short-vowel reduction

Two features define the sedentary Maghreb.

**Jim is a fricative, not an affricate.** Across sedentary Morocco, Algeria,
Tunisia and urban Libya, ج is realized [ʒ] (voiced postalveolar fricative), never
the Mashriqi affricate [dʒ]. This reflex is declared once on `ar-x-maghrebi` and
inherited by all country nodes.

**Short vowels collapse to schwa [ə] and delete, producing heavy clusters** — the
single most salient Maghrebi trait, driven by the Amazigh (Berber) substrate.

| Feature | Reflex | Example | Source (read) |
|:---|:---|:---|:---|
| **jim ج** | **[ʒ]** (not [dʒ]) | جَمَل → `ʒamal` 'camel' | Watson 2002 p.16; Ennaji et al. 2004 p.2; Noamane 2020 p.45 |
| **short-vowel reduction** | /i u a/ → **[ə]** / Ø in weak positions | (allophone layer; clusters e.g. `kəlb`, `smən`) | Noamane 2020 p.49; Heath 2020 p.216; Watson 2002 p.13 |
| **interdentals ث ذ ظ** | **merged** to stops /t d dˤ/ | ثَلاثة → `tal…` (no /θ/) | Watson 2002 p.15; Ennaji et al. 2004 p.2 |
| **qaf ق** | **[q]** sedentary / **[ɡ]** Bedouin | قَلْب → `qalb` | Watson 2002 p.17; Ennaji et al. 2004 p.2 |

Watson (p.16): in the majority of Maghribi dialects "the phoneme does not have an
initial occlusive element and is realized as /ž/", citing Heath (1987:20–1) for
Moroccan specifically. Noamane (p.49): the Moroccan vocalic inventory is "limited
to three underlying short vowels /i, u, a/ and an epenthetic schwa /ə/" with no
long vowels; Heath (p.216): the koiné "reduce[s] all three short vowels to just
one short vowel ə", with original short vowels syncopating in weak metrical
positions.

### Country differentiation

| Variety | qaf ق | Notes | Adstrate |
|:---|:---|:---|:---|
| **Moroccan** `ar-MA` | /q/ (urban); /ɡ/ Bedouin | Most reduced; `e`/`o` from French; interdentals fully merged | French |
| **Algerian** `ar-DZ` | /q/ ~ /ɡ/ (west/Oran /ɡ/) | Intermediate; deep French integration (130 yr) | French, Berber (Kabyle) |
| **Tunisian** `ar-TN` | /q/ ~ /ɡ/ (urban Tunis /ɡ/) | Best-documented; some rural /θ/ retained | Italian/Sicilian |
| **Libyan** `ar-LY` | /q/ (Tripoli conservative) | West (Tripoli) Maghrebi vs East (Benghazi) more conservative/Egyptian-influenced | Italian |
| **Hassaniya** `ar-MR` | inherited | Westernmost Bedouin variety (Mauritania/W. Sahara) | — |

Algerian and Tunisian carry the sedentary~Bedouin qaf duality /q ~ ɡ/ as grapheme
alternates; Moroccan keeps /q/ as its urban reference reflex. The **Amazigh
(Berber)** substrate is linked on `ar-MA` as the cause of the vowel reduction and
cluster phonotactics, and **French** as the adstrate contributing /p v e o/.

## Ṣanʿānī Yemeni (`ar-YE`)

The reference variety is highland **Ṣanʿānī**, per Watson (2002). Two reflexes are
the opposite of what a "conservative peninsular" first guess suggests, and Watson
is explicit on both.

| Feature | Ṣanʿānī reflex | Example | Source (read) |
|:---|:---|:---|:---|
| **qaf ق** | **[ɡ]** — voiced velar | قَلْب → `ɡalb` | Watson 2002 p.11, §2.2 p.20 |
| **jim ج** | **[dʒ]** — palatoalveolar affricate | جَمَل → `dʒamal` | Watson 2002 p.11, §2.2 p.20 |
| **interdentals ث ذ ظ** | **retained** [θ ð ðˤ] | ثَلاثة → `θal…` | Watson 2002 §2.1.4 pp.14–15, Table 2.2 p.19 |
| **ḍād ض / ẓāʾ ظ merger** | both → **[ðˤ]** | (§2.2 merger) | Watson 2002 §2.2 p.20 |

Watson (p.20): "The original voiceless uvular stop, *q, is not realized in any
lexemes in the dialect. Even religious and Standard Arabic words are pronounced
with a voiced velar stop, /g/, as in: al-gurʔān 'the Qur'an'." The **[ɡ]-jim**
reflex often attributed to "Yemeni" belongs to Cairene and the **lower-Yemeni
Taʿizz/Hugariyyah** dialects (§2.1.6 p.16), *not* Ṣanʿānī — so `ar-YE` lists
/dʒ/ first and /ɡ/ as the Taʿizzī alternate. The ḍād/ẓāʾ merger to a single
voiced pharyngealized interdental fricative [ðˤ] loses one Classical phoneme
(§2.2 p.20).

## Sudanese (`ar-SD`)

The Khartoum/central-Sudan koine belongs to the Egypto-Sudanic group. Its marquee
feature is an archaic **palatal** jim that sets it apart from both Egyptian [ɡ]
and Levantine [ʒ].

| Feature | Sudanese reflex | Example | Source (read) |
|:---|:---|:---|:---|
| **jim ج** | **[ɟ]** — voiced palatal stop | جَمَل → `ɟamal` | Leddy-Cecere 2021 §3.1.1 |
| **qaf ق** | **[ɡ]** — voiced velar | قَلْب → `ɡalb` | Leddy-Cecere 2021 §3.1; Youssef 2021 §3.1 |
| **interdentals ث ذ ظ/ض** | **merged** to stops /t d dˤ/ (~/s z zˤ/ in loans) | ثَلْج → `talɟ` | Leddy-Cecere 2021 §3.1 |

Leddy-Cecere (§3.1.1): "the palatal articulation /ɟ/ dominates in the core Sudanic
region represented by the dialects of Khartoum and the Šukriyya … perhaps of high
salience, given its comparative rarity outside this region." The interdental
series merges with the dental stops, with a distinctive extra emphatic /ḍ/ reflex
of *ð in the Sudanic area (§3.1). Nubian/Beja/Nilotic influence is documented for
the **lexicon** (Gasim 1965), not as a phonological cause — so no substrate sound
change is modelled.

## Documented limits (not modelled)

- **Maghrebi vowel deletion** is applied as an allophone *alternate* (/i u a/ →
  [ə]/Ø), not an orthography rewrite: with vocalised input the written short vowel
  surfaces first. Fully predicting syncope from spelling is an engine limit.
- **Libyan east/west split** and **Algerian west /ɡ/** are noted in the specs but
  only the reference reflex is applied at grapheme level.
- **Ṣanʿānī imāla** and lower-Yemeni (Taʿizzī) [ɡ]-jim are documented as
  alternates rather than the primary reflex.

## Sources

**Read for this reference** (page/section-cited above):

- **Watson, J.C.E. (2002)** *The Phonology and Morphology of Arabic*, OUP. Full
  open-access PDF; printed pages 11, 13, 14–16, 19–20. Ṣanʿānī and Maghrebi
  reflexes.
- **Noamane, A. (2020)** "Consonant Gemination in Moroccan Arabic", *J. of Applied
  Language and Culture Studies* 3:37–68. Open access; pp. 45, 49 (MA vowel and
  consonant inventories).
- **Heath, J. (2020)** "Moroccan Arabic", ch. 10 in Lucas & Manfredi (eds.),
  *Arabic and Contact-Induced Change*, Language Science Press. Open access; p. 216
  (three-way short-vowel reduction to ə).
- **Ennaji, M. et al. (2004)** *A Grammar of Moroccan Arabic*, Fès. Open access;
  pp. 2–7 (28-consonant inventory: /ʒ/, no /dʒ/, no interdentals, /q/ and /ɡ/).
- **Leddy-Cecere, T.A. (2021)** "Interrogating the Egypto-Sudanic Arabic
  Connection", *Languages* 6(3):123. Open access, cited by section (§3.1, §3.1.1).
- **Youssef, I. (2021)** "Contrastive Feature Typologies of Arabic Consonant
  Reflexes", *Languages* 6(3):141. Open access, cited by section (§3.1).

**Not obtained** (listed for completeness, no claim sourced to it): Harrell (1962)
*A Short Reference Grammar of Moroccan Arabic*; Heath (2002) *Jewish and Muslim
Dialects of Moroccan Arabic*; Caubet (1993) *L'arabe marocain*; Dickins (2007)
*Sudanese Arabic: Phonematics and Syllable Structure* — the standard primary
monograph for Sudanese /ɟ/, library/paywall only for this pass.

---

**Navigation:** [← All languages](index.md) · [Docs home](../index.md) · [Benchmarks](../benchmarks.md) · [Scoreboard](../scoreboard.md)

*Related: [ar](ar.md), [ar-x-levantine](ar-x-levantine.md), [ar-IQ](ar-IQ.md), [kab](kab.md)*
