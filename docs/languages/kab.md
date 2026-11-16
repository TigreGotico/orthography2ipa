# Kabyle (`kab`)

<!-- atlas:summary begin -->
Kabyle is a Berber language, written in the Latin script. Glottolog places it in Algeria. The `kab` spec is at the research tier. It cites 12 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `kab` |
| ISO 639-3 | [kab](https://iso639-3.sil.org/code/kab), Kabyle |
| Glottolog | [kaby1243](https://glottolog.org/resource/languoid/id/kaby1243), Kabyle |
| Wikidata | [Q35853](https://www.wikidata.org/wiki/Q35853) |
| Wikipedia | [Kabyle language](https://en.wikipedia.org/wiki/Kabyle_language) |
| Family | [Afro-Asiatic](by-family.md#afro-asiatic) > [Berber](by-family.md#afro-asiatic--berber) |
| Region | [Africa](by-region.md#africa) > [Algeria](by-region.md#algeria) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1800, living |
| Parent | [Kabyle-Atlas Berber](https://tigregotico.github.io/orthography2ipa/#ber-x-kabyle-atlas) `ber-x-kabyle-atlas` |
| Explorer | [`kab` in the data explorer](https://tigregotico.github.io/orthography2ipa/#kab) |
| Spec file | [`kab.json`](../../orthography2ipa/data/kab.json) |
<!-- atlas:header end -->

## Overview

The defining trait of Kabyle phonology is spirantization: the lax stops become fricatives, and the tense (geminate) stops keep their closure. The spec carries the stops in the grapheme table and the fricatives in the allophone layer, so the geminates never spirantize.

Kabyle is spoken in Kabylia, north-eastern Algeria, by about 5 to 7 million speakers (Kossmann & Stroomer 1997, p. 461).

The sources read are Kossmann & Stroomer, *Berber Phonology* (1997), pp. 461-475, the primary source. Karaoui, Djeradi & Djeradi (2024), pp. 123-125. Bedar, Quellec & Tifrit (2022). Wikipedia, *Kabyle language*, as a secondary check of the alphabet only.

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

<!-- atlas:lects begin -->
## Related lects

No spec names `kab` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 12 works. 10 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-kossmann_stroomer1997"></a>Kossmann, Maarten G. & Stroomer, Harry J. (1997). *Berber Phonology*. In A. S. Kaye (ed.), Phonologies of Asia and Africa, vol. 1, Eisenbrauns. Cited: pp. 461-475. [hdl.handle.net](https://hdl.handle.net/1887/4150)
2. <a id="src-karaoui2024_fricatives"></a>Karaoui, Fazia, Djeradi, Amar, Djeradi, Rachida (2024). *Acoustic Characterization of the Noise Sources for the Kabyle Fricatives Consonants (abstract, ICAECE'2023, DOI is for the edited abstracts volume)*. AIJR (ICAECE'2023 abstracts), DOI 10.21467/abstracts.163. Cited: pp. 123-125. DOI [10.21467/abstracts.163](https://doi.org/10.21467/abstracts.163) · [books.aijr.org](https://books.aijr.org/index.php/press/catalog/download/163/81/3171-1)
3. <a id="src-bedar_quellec_tifrit_2022"></a>Bedar, Amazigh, Quellec, Lucie, Tifrit, Ali (2022). *Post-sonorant occlusivization in Kabyle*. 19th Meeting of the French Phonology Network (RFP 2022), Porto, Portugal, 7-9 June 2022. [hal.science](https://hal.science/hal-03691265)
4. <a id="src-wikipedia_kabyle"></a>Wikipedia contributors (2024). *Kabyle language*. Wikipedia. [en.wikipedia.org](https://en.wikipedia.org/wiki/Kabyle_language)
5. <a id="src-dallet1982"></a>Dallet, Jean-Marie (1982). *Dictionnaire kabyle-français: parler des At Mangellat, Algérie*. SELAF, Paris. [catalogue.bnf.fr](https://catalogue.bnf.fr/ark:/12148/cb34694452r)
6. <a id="src-naitzerrad2001"></a>Naït-Zerrad, Kamal (2001). *Grammaire moderne du kabyle / tajerrumt tatrart n teqbaylit*. Karthala, Paris. [karthala.com](https://www.karthala.com/2079-grammaire-moderne-du-kabyle-9782845861725.html)
7. <a id="src-chaker1996_notation"></a>Chaker, Salem (1996). *Propositions pour la notation usuelle à base latine du berbère*. Centre de Recherche Berbère, INALCO, Paris (synthèse de l'atelier des 24-25 juin 1996). [centrederechercheberbere.fr](https://www.centrederechercheberbere.fr/tl_files/doc-pdf/notation.pdf)
8. <a id="src-mammeri1976_precis"></a>Mammeri, Mouloud (1976). *Précis de grammaire berbère (kabyle)*. Paris (rééd. Fichier TAL, 1983).
9. <a id="src-souag2019_arabic_script"></a>Souag, Lameen (2019). *Kabyle in Arabic Script: A History without Standardisation*. In: Creating Standards, De Gruyter, pp. 273-296. DOI 10.1515/9783110639063-011. Cited: 273-296. DOI [10.1515/9783110639063-011](https://doi.org/10.1515/9783110639063-011) · [shs.hal.science](https://shs.hal.science/halshs-02945641)
10. <a id="src-wang2020_syllabification"></a>Wang, Beini (2020). *Syllabification and Schwa Epenthesis in Kabyle*. McGill Working Papers in Linguistics 26.1 ('Topics in Kabyle Linguistics'), McGill University. [people.linguistics.mcgill.ca](http://people.linguistics.mcgill.ca/~mcgwpl/McGWPL/2020v26n01/2020_26_1_Wang.pdf)
11. <a id="src-mokraoui2026_native_verification"></a>MOKRAOUI, Athmane (boffire) (2026). *Native-speaker verification sessions for the Kabyle orthography2ipa spec*.
12. <a id="src-corpus_audit_2026_07_17"></a>MOKRAOUI, Athmane (boffire) (2026). *Kabyle corpus audit for cluster attestation and orthographic contamination*. [huggingface.co](https://huggingface.co/boffire)
<!-- atlas:sources end -->

### Notes on the sources

What each work supports:

- Kossmann & Stroomer (1997) is the primary source, read in full, for spirantization, lax and tense gemination, the vowels, the schwa and pharyngealization. <https://hdl.handle.net/1887/4150>
- Karaoui, Djeradi & Djeradi (2024) give the Kabyle fricative inventory, [ç ʝ] included.
- Bedar, Quellec & Tifrit (2022) give speaker judgments for Chemini Kabyle, with comparative data from Aït Mengellat, Boghni and Makouda.
- Naït-Zerrad (2001) is a lexical and morphological source for the TTS silver set, not a phonological source.
- Dallet (1982) is a lexical source for the TTS silver set, not a phonological source.
- Wikipedia, *Kabyle language*, is a secondary check of the Berber Latin alphabet table only.

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `kab` | generated | epitran-derived | CC0 1.0 | 54545 | 0.2071 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 81 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Uvular | Pharyngeal | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b bː p pː |  |  | d dː dˤ dˤː t tː tˤ tˤː |  |  | k kː ɡ ɡː | q qː |  |  |
| Affricate |  |  |  |  | d͡ʒ d͡ʒː t͡ʃ t͡ʃː |  |  |  |  |  |
| Nasal | m mː |  |  | n nː |  | ɲ | ŋ |  |  |  |
| Trill |  |  |  | r rː rˤ rˤː |  |  |  |  |  |  |
| Fricative | β | f fː v | ð ðˤ θ | s sː sˤ sˤː z zː zˤ zˤː | ʃ ʃː ʒ ʒː | ç ʝ | ɣ ɣː | ʁ ʁː χ χː | ħ ħː ʕ ʕː | h hː |
| Approximant |  |  |  |  |  | j jː |  |  |  |  |
| Lateral approximant |  |  |  | l lː |  |  |  |  |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i |  | u |
| Near-close | ɪ |  | ʊ |
| Close-mid | e |  | o |
| Mid |  | ə |  |
| Near-open | æ |  |  |
| Open | a |  | ɑ |

Sequences that the spec writes as one unit: [w] [wː].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨b⟩ | [b] |  |
| ⟨bb⟩ | [bː] |  |
| ⟨c⟩ | [ʃ] |  |
| ⟨cc⟩ | [ʃː] |  |
| ⟨d⟩ | [d] |  |
| ⟨dd⟩ | [dː] |  |
| ⟨e⟩ | [ə] |  |
| ⟨f⟩ | [f] |  |
| ⟨ff⟩ | [fː] |  |
| ⟨g⟩ | [ɡ] |  |
| ⟨gg⟩ | [ɡː] |  |
| ⟨h⟩ | [h] |  |
| ⟨hh⟩ | [hː] |  |
| ⟨i⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨jj⟩ | [ʒː] |  |
| ⟨k⟩ | [k] |  |
| ⟨kk⟩ | [kː] |  |
| ⟨l⟩ | [l] |  |
| ⟨ll⟩ | [lː] |  |
| ⟨m⟩ | [m] |  |
| ⟨mm⟩ | [mː] |  |
| ⟨n⟩ | [n] |  |
| ⟨nn⟩ | [nː] |  |
| ⟨p⟩ | [p] |  |
| ⟨pp⟩ | [pː] |  |
| ⟨q⟩ | [q] |  |
| ⟨qq⟩ | [qː] |  |
| ⟨r⟩ | [r] |  |
| ⟨rr⟩ | [rː] |  |
| ⟨s⟩ | [s] |  |
| ⟨ss⟩ | [sː] |  |
| ⟨t⟩ | [t] |  |
| ⟨tt⟩ | [tː] |  |
| ⟨u⟩ | [u] |  |
| ⟨v⟩ | [v] |  |
| ⟨w⟩ | [w] |  |
| ⟨ww⟩ | [wː] |  |
| ⟨x⟩ | [χ] |  |
| ⟨xx⟩ | [χː] |  |
| ⟨y⟩ | [j] |  |
| ⟨yy⟩ | [jː] |  |
| ⟨z⟩ | [z] |  |
| ⟨zz⟩ | [zː] |  |
| ⟨č⟩ | [t͡ʃ] |  |
| ⟨čč⟩ | [t͡ʃː] |  |
| ⟨ǧ⟩ | [d͡ʒ] |  |
| ⟨ǧǧ⟩ | [d͡ʒː] |  |
| ⟨ɛ⟩ | [ʕ] |  |
| ⟨ɛɛ⟩ | [ʕː] |  |
| ⟨ɣ⟩ | [ɣ] |  |
| ⟨ɣɣ⟩ | [ɣː] |  |
| ⟨ḍ⟩ | [dˤ] |  |
| ⟨ḍḍ⟩ | [dˤː] |  |
| ⟨ḥ⟩ | [ħ] |  |
| ⟨ḥḥ⟩ | [ħː] |  |
| ⟨ṛ⟩ | [rˤ] |  |
| ⟨ṛṛ⟩ | [rˤː] |  |
| ⟨ṣ⟩ | [sˤ] |  |
| ⟨ṣṣ⟩ | [sˤː] |  |
| ⟨ṭ⟩ | [tˤ] |  |
| ⟨ṭṭ⟩ | [tˤː] |  |
| ⟨ẓ⟩ | [zˤ] |  |
| ⟨ẓẓ⟩ | [zˤː] |  |

The spec declares no stress rule.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 26 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `KAB_BLOCK_SPIRANT_B_AFTER_M` | /b/ → [b], after [m] | ⟨'basket'⟩ [zəmbil] | [Kossmann 1997](#src-kossmann_stroomer1997), [Bedar 2022](#src-bedar_quellec_tifrit_2022), Quellec & Tifrit 2022 |
| `KAB_BLOCK_SPIRANT_D_AFTER_N` | /d/ → [d], after [n] | ⟨'where'⟩ [anda] | [Kossmann 1997](#src-kossmann_stroomer1997), [Bedar 2022](#src-bedar_quellec_tifrit_2022), Quellec & Tifrit 2022 |
| `KAB_BLOCK_SPIRANT_T_AFTER_N` | /t/ → [t], after [n] | ⟨'⟩ [anta] | [Kossmann 1997](#src-kossmann_stroomer1997), [Bedar 2022](#src-bedar_quellec_tifrit_2022), Quellec & Tifrit 2022 |
| `KAB_BLOCK_SPIRANT_T_AFTER_L_FINAL` | /t/ → [t], word-finally, after [l] | ⟨'egg'⟩ [θaməllalt] | [Bedar 2022](#src-bedar_quellec_tifrit_2022), Quellec & Tifrit 2022 |
| `KAB_BLOCK_SPIRANT_DH_EMPH_AFTER_N` | /dˤ/ → [dˤ], after [n] | - | [Kossmann 1997](#src-kossmann_stroomer1997), [Bedar 2022](#src-bedar_quellec_tifrit_2022), Quellec & Tifrit 2022 |
| `KAB_BLOCK_SPIRANT_D_AFTER_L` | /d/ → [d], after [l] | ⟨'open'⟩ [ldi] | - |
| `KAB_BLOCK_SPIRANT_T_AFTER_M` | /t/ → [t], after [m] | ⟨tasemmumt⟩ [tasemmumt] | [Bedar 2022](#src-bedar_quellec_tifrit_2022), Quellec & Tifrit 2022 |
| `KAB_BLOCK_SPIRANT_D_AFTER_M` | /d/ → [d], after [m] | ⟨'pond'⟩ [θamda] | [Bedar 2022](#src-bedar_quellec_tifrit_2022), Quellec & Tifrit 2022 |
| `KAB_BLOCK_SPIRANT_K_AFTER_CONSONANT` | /k/ → [k], after [b] [d] [dˤ] [f] [ɡ] [ɣ] [h] [ħ] and 53 more | - | [Bedar 2022](#src-bedar_quellec_tifrit_2022), Quellec & Tifrit 2022 |
| `KAB_BLOCK_SPIRANT_G_AFTER_CONSONANT` | /ɡ/ → [ɡ], after [b] [d] [dˤ] [f] [ɡ] [ɣ] [h] [ħ] and 52 more | - | [Bedar 2022](#src-bedar_quellec_tifrit_2022), Quellec & Tifrit 2022 |
| `KAB_SPIRANT_K` | /k/ → [ç] | - | [Kossmann 1997](#src-kossmann_stroomer1997), [Karaoui 2024](#src-karaoui2024_fricatives) |
| `KAB_SPIRANT_B` | /b/ → [β] | - | [Kossmann 1997](#src-kossmann_stroomer1997) |
| `KAB_SPIRANT_D` | /d/ → [ð] | ⟨'mountain'⟩ [aðrar] | [Kossmann 1997](#src-kossmann_stroomer1997) |
| `KAB_SPIRANT_T` | /t/ → [θ] | ⟨'light'⟩ [θafaθ] | [Kossmann 1997](#src-kossmann_stroomer1997) |
| `KAB_SPIRANT_G` | /ɡ/ → [ʝ] | ⟨argaz⟩ [arʝaz] | [Kossmann 1997](#src-kossmann_stroomer1997) |
| `KAB_SPIRANT_DH_EMPH` | /dˤ/ → [ðˤ] | - | [Kossmann 1997](#src-kossmann_stroomer1997) |
| `KAB_GH_UVULAR_REALIZATION` | /ɣ/ → [ʁ] | ⟨tifinaɣ⟩ [θifinɑʁ] | - |
| `KAB_GH_GEM_UVULAR_REALIZATION` | /ɣː/ → [ʁː] | - | - |
| `KAB_A_BACKING` | /a/ → [ɑ], before [rˤ] [rˤː] [sˤ] [sˤː] [dˤ] [dˤː] [tˤ] [tˤː] and 8 more | ⟨'house'⟩ [ɑχːɑm] | [Kossmann 1997](#src-kossmann_stroomer1997) |
| `KAB_A_BACKING_PRECEDING` | /a/ → [ɑ], after [rˤ] [rˤː] [sˤ] [sˤː] [dˤ] [dˤː] [tˤ] [tˤː] and 8 more | - | - |
| `KAB_A_DEFAULT` | /a/ → [æ] | - | [Kossmann 1997](#src-kossmann_stroomer1997) |
| `KAB_I_CLOSED` | /i/ → [ɪ], before a consonant cluster | - | - |
| `KAB_U_CLOSED` | /u/ → [ʊ], before a consonant cluster | - | - |
| `KAB_N_VELAR_ASSIM` | /n/ → [ŋ], before [k] [ɡ] [kː] [ɡː] [q] [qː] [χ] [ɣ] and 2 more | - | [Bedar 2022](#src-bedar_quellec_tifrit_2022), Quellec & Tifrit 2022 |
| `KAB_N_LABIAL_ASSIM` | /n/ → [m], before [b] [bː] [p] [f] [m] [mː] | - | - |
| `KAB_N_PALATAL_ASSIM` | /n/ → [ɲ], before [j] [jː] | - | - |
<!-- atlas:rules end -->

<!-- atlas:examples begin words="akli|tagut|abrid|aḍar|adrar|argaz|anda|nteddu|tamellalt|zembil" -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "kab")`. They are engine output, not reference transcriptions.

| Spelling | Engine output |
|:--|:--|
| akli | [æçli] |
| tagut | [θæʝuθ] |
| abrid | [æβrið] |
| aḍar | [ɑðˤɑr] |
| adrar | [æðrær] |
| argaz | [ærɡæz] |
| anda | [ændæ] |
| nteddu | [ntədːu] |
| tamellalt | [θæməlːælt] |
| zembil | [zəmbil] |
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Kabiye](kbp.md) · [Home](../index.md) · [Kaingang →](kgp.md)
