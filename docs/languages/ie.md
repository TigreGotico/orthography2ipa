# Interlingue (Occidental) (`ie`)

<!-- atlas:summary begin -->
Interlingue (Occidental) is a Constructed language, written in the Latin script. The `ie` spec is at the research tier. It cites 3 sources and has 0 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `ie` |
| ISO 639-3 | [ile](https://iso639-3.sil.org/code/ile), Interlingue |
| Glottolog | [inte1260](https://glottolog.org/resource/languoid/id/inte1260), Interlingue (Occidental) |
| Wikidata | [Q35850](https://www.wikidata.org/wiki/Q35850) |
| Wikipedia | [Interlingue](https://en.wikipedia.org/wiki/Interlingue) |
| Family | [Constructed](by-family.md#constructed) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1922, living |
| Explorer | [`ie` in the data explorer](https://tigregotico.github.io/orthography2ipa/#ie) |
| Spec file | [`ie.json`](../../orthography2ipa/data/ie.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Interlingue (originally Occidental), constructed international auxiliary language published by Edgar de Wahl in 1922, renamed Interlingue in 1949. Published, fully regular phonemic orthography over the 26-letter Latin alphabet.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. No board row scores it yet, so the measured gold of that tier is still missing. It cites 3 works, from 1922 to 2026. 1 of them is a Wikipedia article. [Sources](#sources) lists them. The spec file writes all 36 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/ie.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `ie` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 2 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-dewahl1922"></a>de Wahl, Edgar (1922). *Occidental: Die Weltsprache (Radicarium directiv del lingue international Occidental)*. Kosmoglott.
2. <a id="src-interlingue_wiki"></a>Wikipedia contributors (2026). *Interlingue*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Interlingue)
3. <a id="src-janotta1929"></a>Janotta, K. (1929). *Complet grammatica de Occidental. I-esim capitul: Phonologie (B. Pronunciation, C. Accentuation)*. Cosmoglotta 64 (septembre 1929) and 65 (octobre 1929), Occidental-Union. Cited: Cosmoglotta 64: 152-154, Cosmoglotta 65: 165-166, 176. [archive.org](https://archive.org/details/Kosmoglott-Cosmoglotta_1929_n065_okt)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

No dataset on the board scores this spec. See the [dataset catalogue](../evaluation/datasets.md).
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 32 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  | d t |  |  | k ɡ |  |
| Affricate |  |  | dz ts |  |  |  |  |
| Nasal | m |  | n |  |  |  |  |
| Trill |  |  | r |  |  |  |  |
| Fricative |  | f v | s z | ʃ ʒ |  |  | h |
| Approximant |  |  |  |  | j |  |  |
| Lateral approximant |  |  | l |  |  |  |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i y | u |
| Close-mid | e ø | o |
| Open-mid | ɛ |  |
| Open | a | ɒ |

Sequences that the spec writes as one unit: [ks] [kw] [w].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨c⟩ | [k] | before front vowel [ts] |
| ⟨ch⟩ | [ʃ] |  |
| ⟨d⟩ | [d] |  |
| ⟨e⟩ | [e] |  |
| ⟨eu⟩ | [ø] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] | before front vowel [ʒ] |
| ⟨h⟩ | [h] |  |
| ⟨i⟩ | [i] | before vowel [j] |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨o⟩ | [o] |  |
| ⟨p⟩ | [p] |  |
| ⟨ph⟩ | [f] |  |
| ⟨qu⟩ | [kw] |  |
| ⟨r⟩ | [r] |  |
| ⟨rh⟩ | [r] |  |
| ⟨s⟩ | [s] | intervocalic [z] |
| ⟨t⟩ | [t] |  |
| ⟨th⟩ | [t] |  |
| ⟨u⟩ | [u] | before vowel [w] |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [v] |  |
| ⟨x⟩ | [ks] |  |
| ⟨y⟩ | [y] [j] | after consonant [y] · after vowel [j] · before vowel [j] |
| ⟨z⟩ | [dz] |  |
| ⟨á⟩ | [a] |  |
| ⟨é⟩ | [e] |  |
| ⟨í⟩ | [i] |  |
| ⟨ó⟩ | [o] |  |
| ⟨ú⟩ | [u] |  |

Stress falls on the penult by default. A written ⟨á⟩ ⟨é⟩ ⟨í⟩ ⟨ó⟩ ⟨ú⟩ marks the stressed vowel. These endings take final stress: ⟨-ac⟩ ⟨-acs⟩ ⟨-aen⟩ ⟨-aic⟩ ⟨-aics⟩ ⟨-ail⟩ ⟨-al⟩ ⟨-am⟩ ⟨-ams⟩ ⟨-an⟩ ⟨-ay⟩ ⟨-b⟩ ⟨-bc⟩ ⟨-bcs⟩ ⟨-ben⟩ ⟨-bl⟩ ⟨-bm⟩ ⟨-bms⟩ ⟨-bn⟩ ⟨-bs⟩ ⟨-cc⟩ ⟨-ccs⟩ ⟨-cen⟩ ⟨-cil⟩ ⟨-cl⟩ ⟨-cm⟩ ⟨-cms⟩ ⟨-cn⟩ ⟨-d⟩ ⟨-dc⟩ ⟨-dcs⟩ ⟨-den⟩ ⟨-dil⟩ ⟨-dl⟩ ⟨-dm⟩ ⟨-dms⟩ ⟨-dn⟩ ⟨-ds⟩ ⟨-ec⟩ ⟨-ecs⟩ ⟨-een⟩ ⟨-eil⟩ ⟨-el⟩ ⟨-em⟩ ⟨-ems⟩ ⟨-ey⟩ ⟨-f⟩ ⟨-fc⟩ ⟨-fcs⟩ ⟨-fen⟩ ⟨-fil⟩ ⟨-fl⟩ ⟨-fm⟩ ⟨-fms⟩ ⟨-fn⟩ ⟨-fs⟩ ⟨-g⟩ ⟨-gc⟩ ⟨-gcs⟩ ⟨-gen⟩ ⟨-gil⟩ ⟨-gl⟩ ⟨-gm⟩ ⟨-gms⟩ ⟨-gn⟩ ⟨-gs⟩ ⟨-h⟩ ⟨-hc⟩ ⟨-hcs⟩ ⟨-hen⟩ ⟨-hil⟩ ⟨-hl⟩ ⟨-hm⟩ ⟨-hms⟩ ⟨-hn⟩ ⟨-hs⟩ ⟨-ien⟩ ⟨-iil⟩ ⟨-in⟩ ⟨-j⟩ ⟨-jc⟩ ⟨-jcs⟩ ⟨-jen⟩ ⟨-jil⟩ ⟨-jl⟩ ⟨-jm⟩ ⟨-jms⟩ ⟨-jn⟩ ⟨-js⟩ ⟨-k⟩ ⟨-kc⟩ ⟨-kcs⟩ ⟨-ken⟩ ⟨-kil⟩ ⟨-kl⟩ ⟨-km⟩ ⟨-kms⟩ ⟨-kn⟩ ⟨-ks⟩ ⟨-lc⟩ ⟨-lcs⟩ ⟨-len⟩ ⟨-lil⟩ ⟨-ll⟩ ⟨-lm⟩ ⟨-lms⟩ ⟨-ln⟩ ⟨-ls⟩ ⟨-mc⟩ ⟨-mcs⟩ ⟨-mil⟩ ⟨-ml⟩ ⟨-mm⟩ ⟨-mms⟩ ⟨-mn⟩ ⟨-nc⟩ ⟨-ncs⟩ ⟨-nen⟩ ⟨-nil⟩ ⟨-nl⟩ ⟨-nm⟩ ⟨-nms⟩ ⟨-nn⟩ ⟨-ns⟩ ⟨-oc⟩ ⟨-ocs⟩ ⟨-oen⟩ ⟨-oil⟩ ⟨-ol⟩ ⟨-om⟩ ⟨-oms⟩ ⟨-on⟩ ⟨-oy⟩ ⟨-p⟩ ⟨-pc⟩ ⟨-pcs⟩ ⟨-pen⟩ ⟨-pil⟩ ⟨-pl⟩ ⟨-pm⟩ ⟨-pms⟩ ⟨-pn⟩ ⟨-ps⟩ ⟨-r⟩ ⟨-rc⟩ ⟨-rcs⟩ ⟨-ren⟩ ⟨-ril⟩ ⟨-rl⟩ ⟨-rm⟩ ⟨-rms⟩ ⟨-rn⟩ ⟨-rs⟩ ⟨-sc⟩ ⟨-scs⟩ ⟨-sen⟩ ⟨-sil⟩ ⟨-sl⟩ ⟨-sm⟩ ⟨-sms⟩ ⟨-sn⟩ ⟨-ss⟩ ⟨-t⟩ ⟨-tc⟩ ⟨-tcs⟩ ⟨-ten⟩ ⟨-til⟩ ⟨-tl⟩ ⟨-tm⟩ ⟨-tms⟩ ⟨-tn⟩ ⟨-ts⟩ ⟨-uc⟩ ⟨-ucs⟩ ⟨-uen⟩ ⟨-uic⟩ ⟨-uics⟩ ⟨-uil⟩ ⟨-un⟩ ⟨-uy⟩ ⟨-v⟩ ⟨-vc⟩ ⟨-vcs⟩ ⟨-ven⟩ ⟨-vil⟩ ⟨-vl⟩ ⟨-vm⟩ ⟨-vms⟩ ⟨-vn⟩ ⟨-vs⟩ ⟨-w⟩ ⟨-wc⟩ ⟨-wcs⟩ ⟨-wen⟩ ⟨-wil⟩ ⟨-wl⟩ ⟨-wm⟩ ⟨-wms⟩ ⟨-wn⟩ ⟨-ws⟩ ⟨-x⟩ ⟨-xc⟩ ⟨-xcs⟩ ⟨-xen⟩ ⟨-xil⟩ ⟨-xl⟩ ⟨-xm⟩ ⟨-xms⟩ ⟨-xn⟩ ⟨-xs⟩ ⟨-yc⟩ ⟨-ycs⟩ ⟨-yen⟩ ⟨-yil⟩ ⟨-yl⟩ ⟨-ym⟩ ⟨-yms⟩ ⟨-yn⟩ ⟨-z⟩ ⟨-zc⟩ ⟨-zcs⟩ ⟨-zen⟩ ⟨-zil⟩ ⟨-zl⟩ ⟨-zm⟩ ⟨-zms⟩ ⟨-zn⟩ ⟨-zs⟩. These endings take the penult: ⟨-aica⟩ ⟨-aicas⟩ ⟨-aicmen⟩ ⟨-aico⟩ ⟨-aicos⟩.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 4 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `IE_ART4_STRESSED_I` | /j/ → [i], stressed, before a vowel, spelled ⟨i⟩, with more context in the spec | - | [Janotta 1929](#src-janotta1929) |
| `IE_ART4_STRESSED_I_PLURAL` | /j/ → [i], stressed, before a vowel, spelled ⟨i⟩, with more context in the spec | - | [Janotta 1929](#src-janotta1929) |
| `IE_ART4_STRESSED_U` | /w/ → [u], stressed, before a vowel, spelled ⟨u⟩, with more context in the spec | - | [Janotta 1929](#src-janotta1929) |
| `IE_ART4_STRESSED_U_PLURAL` | /w/ → [u], stressed, before a vowel, spelled ⟨u⟩, with more context in the spec | - | [Janotta 1929](#src-janotta1929) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "ie")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Interlingua](ia.md) · [Home](../index.md) · [Interslavic →](isv.md)
