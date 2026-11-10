# Sendinês (Mirandese meridional) (`mwl-x-sendim`)

<!-- atlas:summary begin -->
Sendinês (Mirandese meridional) is an Asturleonese variety, written in the Latin script. Glottolog places it in the Eurasia macroarea. The `mwl-x-sendim` spec is at the research tier. It cites 4 sources and has 3 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `mwl-x-sendim` |
| ISO 639-3 | [mwl](https://iso639-3.sil.org/code/mwl), Mirandese |
| Wikipedia | [Mirandese language](https://en.wikipedia.org/wiki/Mirandese_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Ibero-Romance > Asturleonese](by-family.md#indo-european--italic--romance--ibero-romance--asturleonese) |
| Region | [Eurasia](by-region.md#eurasia) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1600, living |
| Parent | [Mirandese](mwl.md) `mwl` |
| Explorer | [`mwl-x-sendim` in the data explorer](https://tigregotico.github.io/orthography2ipa/#mwl-x-sendim) |
| Spec file | [`mwl-x-sendim.json`](../../orthography2ipa/data/mwl-x-sendim.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Sendinês subdialect of Mirandese, spoken in Vila de Sendim (southern extreme of Terra de Miranda).

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 4 works, from 1900 to 2000. [Sources](#sources) lists them. The spec file writes 4 of the 72 spellings of its letter table and takes the other 68 from [Mirandese](mwl.md) `mwl`.

The [spec file](../../orthography2ipa/data/mwl-x-sendim.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `mwl-x-sendim` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 4 works. 2 of them have a DOI or a URL. The spec file holds a note on what 3 of them support.

1. <a id="src-convencao1999"></a>Ferreira, M.B. & Raposo, D. (coords.) (1999). *Convenção Ortográfica da Língua Mirandesa*. Câmara Municipal de Miranda do Douro / Centro de Linguística da Universidade de Lisboa. Cited: 62. [mirandadodouro.jfreguesia.com](http://mirandadodouro.jfreguesia.com/images/stories/PDF/convencaomirandes.pdf)
2. <a id="src-aditamento2000"></a>Ferreira, M.B. & Raposo, D. (coords.) (2000). *Primeiro Aditamento à Convenção Ortográfica da Língua Mirandesa*. Câmara Municipal de Miranda do Douro / Centro de Linguística da Universidade de Lisboa.
3. <a id="src-ferreira1995"></a>Ferreira, M.B. (1995). *Variação linguística: perspectiva dialectológica*. Universidade de Lisboa.
4. <a id="src-vasconcelos1900"></a>Vasconcelos, J. Leite de (1900). *Estudos de Philologia Mirandesa*. Imprensa Nacional, Lisboa. Cited: 178, 201, 239. [archive.org](https://archive.org/details/estudosdephilolo01vascuoft)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `mirandese_g2p` ([TigreGotico/mirandese_g2p](https://huggingface.co/datasets/TigreGotico/mirandese_g2p)) | `mwl-x-sendim` | gold | expert-human | Not stated upstream | 11 | 0.4470 | no |
| `mirandese_dict` ([TigreGotico/mirandese-ipa-dict-synthetic](https://huggingface.co/datasets/TigreGotico/mirandese-ipa-dict-synthetic)) | `mwl-x-sendim` | silver | llm-corrected | CC BY-SA 4.0 | 79 | 0.1352 | no |
| `portuguese_tts` | `mwl-x-sendim` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.1388 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 81 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar | Glottal |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k kʲ ɡ |  |
| Affricate |  |  |  | d͡z ts t͡s | d͡ʒ tʃ |  |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |  |
| Trill |  |  |  | r |  |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |  |
| Fricative | β | f | ð | s s̺ s̻ z z̺ z̻ | ʃ ʒ | ʝ | ɣ | h |
| Approximant |  |  |  |  |  | j |  |  |
| Lateral approximant |  |  |  | l ɫ |  | ʎ |  |  |

| Vowels | Front | Central | Back |
|:--|:-:|:-:|:-:|
| Close | i i̯ ĩ | ɨ ɨ̃ | u u̯ ũ |
| Near-close |  |  | ʊ̃ |
| Close-mid | e ẽ |  | o õ |
| Open-mid | ɛ |  | ɔ |
| Near-open |  | ɐ ɐ̃ |  |
| Open | a |  |  |

Sequences that the spec writes as one unit: [aj] [aw] [ej] [ew] [iu] [iw] [ja] [jo] [ju] [jɐ̃w̃] [jɪ̃] [jẽ] [kw] [oj] [uj] [uu] [w] [wa] [we] [wõ] [õj̃] [ɐ̃w̃] [ɟ͡ʝ] [ɡw] [ɡwe] [ɡwi] [ɵw].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] | nucleus stressed [a] · nucleus unstressed [ɐ] · posttonic [ɐ] · pretonic [ɐ] · word final [ɐ] |
| ⟨ai⟩ | [aj] |  |
| ⟨au⟩ | [aw] |  |
| ⟨b⟩ | [b] | after consonant [b] · intervocalic [b] [β] · word initial [b] |
| ⟨c⟩ | [k] [s] | before e [s] · before i [s] |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] | after consonant [d] · intervocalic [ð] [d] · word initial [d] |
| ⟨e⟩ | [e] | nucleus stressed [e] · nucleus unstressed [ɨ] · pretonic [ɨ] · word final [ɨ] |
| ⟨ei⟩ | [ej] |  |
| ⟨eu⟩ | [ew] |  |
| ⟨f⟩ | [f] | intervocalic [f] · word initial [f] |
| ⟨g⟩ | [ɡ] [ʒ] | before e [ʒ] · before i [ʒ] · intervocalic [ɣ] |
| ⟨gu⟩ | [ɡw] [ɡ] | before a [ɡw] · before e [ɡ] · before i [ɡ] |
| ⟨güe⟩ | [ɡwe] |  |
| ⟨güi⟩ | [ɡwi] |  |
| ⟨h⟩ | ∅ |  |
| ⟨h.⟩ | [h] |  |
| ⟨i⟩ | [i] |  |
| ⟨ia⟩ | [ja] |  |
| ⟨ie⟩ | [i] | word final [i] |
| ⟨io⟩ | [jo] | word final [iu] |
| ⟨iu⟩ | [ju] | word final [iw] |
| ⟨iê⟩ | [i] |  |
| ⟨j⟩ | [ʒ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] | onset [l] |
| ⟨lh⟩ | [ʎ] | word initial [l] |
| ⟨ll⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] |  |
| ⟨nh⟩ | [ɲ] |  |
| ⟨o⟩ | [o] | nucleus stressed [o] · nucleus unstressed [u] · posttonic [u] · pretonic [u] · word final [u] |
| ⟨oi⟩ | [oj] |  |
| ⟨ou⟩ | [ɵw] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [k] | before e [k] · before i [k] · before vowel [kw] |
| ⟨r⟩ | [ɾ] | before consonant [ɾ] · intervocalic [ɾ] · word final [ɾ] · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s̺] [z̺] | intervocalic [z̺] · word initial [s̺] |
| ⟨ss⟩ | [s̺] |  |
| ⟨t⟩ | [t] |  |
| ⟨ts⟩ | [ts] |  |
| ⟨u⟩ | [u] |  |
| ⟨ua⟩ | [wa] |  |
| ⟨ue⟩ | [we] | word final [u] |
| ⟨ui⟩ | [uj] |  |
| ⟨uo⟩ | [u] | word final [uu] |
| ⟨uô⟩ | [u] |  |
| ⟨v⟩ | [b] | after consonant [b] · intervocalic [b] [β] · word initial [b] |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ʃ] |  |
| ⟨y⟩ | [ʝ] [j] | word final [j] |
| ⟨yy⟩ | [kʲ] |  |
| ⟨z⟩ | [z] | intervocalic [z] · word final [z] · word initial [z] |
| ⟨á⟩ | [a] |  |
| ⟨ã⟩ | [ɐ̃] |  |
| ⟨ão⟩ | [ɐ̃w̃] |  |
| ⟨ç⟩ | [s] |  |
| ⟨é⟩ | [e] [ɛ] |  |
| ⟨éu⟩ | [ew] |  |
| ⟨ê⟩ | [e] |  |
| ⟨í⟩ | [i] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ó⟩ | [o] [ɔ] |  |
| ⟨õ⟩ | [õ] |  |
| ⟨õe⟩ | [õj̃] |  |
| ⟨ú⟩ | [u] |  |
| ⟨ĩ⟩ | [ĩ] |  |
| ⟨ũ⟩ | [ũ] |  |
| ⟨ḥ⟩ | [h] |  |
| ⟨ẽ⟩ | [ẽ] |  |

Stress falls on the penult by default. A written ⟨á⟩ ⟨é⟩ ⟨í⟩ ⟨ó⟩ ⟨ú⟩ ⟨ã⟩ ⟨ẽ⟩ ⟨ĩ⟩ ⟨õ⟩ ⟨ũ⟩ marks the stressed vowel. These endings take final stress: ⟨-r⟩ ⟨-l⟩ ⟨-z⟩ ⟨-ç⟩ ⟨-in⟩ ⟨-un⟩ ⟨-on⟩ ⟨-is⟩ ⟨-us⟩ ⟨-ns⟩ ⟨-ão⟩ ⟨-ie⟩.

Whole-word exceptions (11): ⟨algũa⟩ [ɐɫˈɣũŋɐ], ⟨algũas⟩ [ɐɫˈɣũŋɐs̺], ⟨bien⟩ [ˈbiɨ̃], ⟨cien⟩ [ˈsiɨ̃], ⟨l⟩ [l], ⟨non⟩ [ˈno], ⟨quien⟩ [ˈkiɨ̃], ⟨sue⟩ [ˈs̺ʊə], ⟨tue⟩ [ˈtʊə], ⟨ũa⟩ [ˈũŋɐ], ⟨ũas⟩ [ˈũŋɐs̺].

Grammatical endings: ⟨-ion⟩ [jɐ̃w̃], ⟨-on⟩ [ɐ̃w̃].
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 23 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `AST_NASAL_a` | /a/ → [ɐ̃], before a coda nasal | - | - |
| `AST_NASAL_e` | /e/ → [ẽ], before a coda nasal | - | [Vasconcelos 1900](#src-vasconcelos1900) |
| `AST_NASAL_i` | /i/ → [ĩ], before a coda nasal | - | - |
| `AST_NASAL_o` | /o/ → [õ], before a coda nasal | - | [Vasconcelos 1900](#src-vasconcelos1900) |
| `AST_NASAL_u` | /u/ → [ũ], before a coda nasal | - | - |
| `AST_NASAL_ABSORB` | /n m/ → ∅, in the coda, after a vowel, before [f] [s̺] [z̺] [s] [z] [ʃ] [ʒ] [l] and 10 more | ⟨honra⟩ [ˈõɾɐ] | [Convenção Ortográfica 1999](#src-convencao1999), [Vasconcelos 1900](#src-vasconcelos1900) |
| `MWL_NASAL_ABSORB_FINAL` | /n m/ → ∅, word-finally, in the coda, after a vowel | ⟨pan⟩ [ˈpɐ̃] | [Convenção Ortográfica 1999](#src-convencao1999), [Vasconcelos 1900](#src-vasconcelos1900) |
| `MWL_NASAL_LABIAL` | /n/ → [m], before [p] [b] [m] | - | [Vasconcelos 1900](#src-vasconcelos1900), Mateus & d'Andrade 2000 |
| `MWL_NASAL_VELAR` | /n/ → [ŋ], before [k] [ɡ] | - | [Vasconcelos 1900](#src-vasconcelos1900), Mateus & d'Andrade 2000, Ferreira et al. 2014 |
| `MWL_SPIRANT_B` | /b/ → [β], after a vowel, before a vowel | ⟨rabudo⟩ [rɐˈβudu] | [Convenção Ortográfica 1999](#src-convencao1999), [Vasconcelos 1900](#src-vasconcelos1900) |
| `MWL_NASAL_A_REDUCED` | /ɐ/ → [ɐ̃], before a coda nasal | ⟨an Miranda⟩ [ɐ̃ miˈɾandɐ] | - |
| `MWL_NASAL_E_REDUCED` | /ɨ/ → [ɨ̃], before a coda nasal, with more context in the spec | - | [Convenção Ortográfica 1999](#src-convencao1999), [Vasconcelos 1900](#src-vasconcelos1900), Ferreira et al. 2014 |
| `MWL_NASAL_E_REDUCED_FINAL` | /ɨ/ → [ɨ̃], before a coda nasal, with more context in the spec | - | [Vasconcelos 1900](#src-vasconcelos1900) |
| `MWL_NASAL_DIPHTHONG_JI` | /jɪ/ → [jɪ̃], before a coda nasal | ⟨bien⟩ [ˈbjɪ̃] | [Vasconcelos 1900](#src-vasconcelos1900) |
| `MWL_NASAL_U_LAX` | /ʊ/ → [ʊ̃], before a coda nasal | ⟨fuonte⟩ [ˈfʊ̃ntɨ] | [Vasconcelos 1900](#src-vasconcelos1900) |
| `MWL_NASAL_DIPHTHONG_JE` | /je jɛ/ → [jẽ], before a coda nasal | ⟨bien⟩ [ˈbjẽ] | [Convenção Ortográfica 1999](#src-convencao1999), [Vasconcelos 1900](#src-vasconcelos1900), Ferreira et al. 2014 |
| `MWL_NASAL_DIPHTHONG_WO` | /wo wɔ/ → [wõ], before a coda nasal | ⟨fuonte⟩ [ˈfwõntɨ] | [Convenção Ortográfica 1999](#src-convencao1999), [Vasconcelos 1900](#src-vasconcelos1900), Ferreira et al. 2014 |
| `MWL_NASAL_E_OPEN` | /ɛ/ → [ẽ], before a coda nasal | ⟨lhéngua⟩ [ˈʎẽŋɡwɐ] | [Vasconcelos 1900](#src-vasconcelos1900) |
| `MWL_S_VOICING` | /s̺/ → [z̺], before [b] [d] [ɡ] [β] [ð] [ɣ] [m] [n] and 7 more | ⟨asno⟩ [ˈaz̺nu] | [Convenção Ortográfica 1999](#src-convencao1999), [Vasconcelos 1900](#src-vasconcelos1900) |
| `MWL_L_VELAR` | /l/ → [ɫ], in the coda | ⟨caldo⟩ [ˈkaɫdu] | [Vasconcelos 1900](#src-vasconcelos1900) |
| `MWL_SPIRANT_D` | /d/ → [ð], after [s̺] [z̺] [s] [z] [ɾ] | ⟨tarde⟩ [ˈtaɾðɨ] | [Convenção Ortográfica 1999](#src-convencao1999), [Vasconcelos 1900](#src-vasconcelos1900) |
| `MWL_SPIRANT_B_AFTER_CONSONANT` | /b/ → [β], after [l] [ɫ] [ʎ] [ɾ] [r] [s̺] [z̺] [z] and 1 more | ⟨silba⟩ [ˈs̺iɫβɐ] | [Convenção Ortográfica 1999](#src-convencao1999), [Vasconcelos 1900](#src-vasconcelos1900) |
| `MWL_SPIRANT_G` | /ɡ/ → [ɣ], after [s̺] [z̺] [l] [ɫ] [ɾ] | ⟨algo⟩ [ˈaɫɣu] | [Convenção Ortográfica 1999](#src-convencao1999), [Vasconcelos 1900](#src-vasconcelos1900) |

The spec applies 8 rules across a word boundary. The contexts are regular expressions on the IPA of the two words.

| Rule | End of word | Start of next word | Change | Example | Cited |
|:--|:--|:--|:--|:--|:--|
| `MWL_FINAL_S_VOICING` | `s̺$` | `^ˈ?[bdɡβðɣmnɲlɫʎɾrʒz]` | left [z̺] | ⟨ls nius⟩ [ɫz̺ ˈnjus̺] | [Vasconcelos 1900](#src-vasconcelos1900) |
| `MWL_FINAL_C_VOICING` | `(?<!t)s$` | `^ˈ?[bdɡβðɣmnɲlɫʎɾrʒz]` | left [z] | - | [Convenção Ortográfica 1999](#src-convencao1999), [Vasconcelos 1900](#src-vasconcelos1900) |
| `MWL_ARTICLE_L_VELAR` | `^l$` | `^ˈ?[pbtdkɡfsʃʒzmnɲlʎɾrβðɣ]` | left [ɫ] | ⟨l pai⟩ [ɫ ˈpaj] | [Vasconcelos 1900](#src-vasconcelos1900) |
| `MWL_NASAL_VELAR_ONSET` | `(?:[ãẽĩõũ]\|[ɐɨɪʊə]̃)$` | `^(ˈ?)(?=[aeiouɐɨɪʊəɵáéíóú])` | right [ŋ] | ⟨bien alto⟩ [ˈbjɪ̃ ˈŋaɫtu] | [Convenção Ortográfica 1999](#src-convencao1999), [Vasconcelos 1900](#src-vasconcelos1900), Ferreira et al. 2014 |
| `MWL_SPIRANT_D_ONSET` | `(?:[sz]̺?\|ɾ\|[aeiouɐɨɪʊəɛɔɵjw])$` | `^(ˈ?)d` | right [ð] | ⟨ls dedos⟩ [ɫz̺ ˈðeðus̺] | [Vasconcelos 1900](#src-vasconcelos1900) |
| `MWL_SPIRANT_B_ONSET` | `(?:[sz]̺?\|[lɫɾ]\|[aeiouɐɨɪʊəɛɔɵjw])$` | `^(ˈ?)b` | right [β] | ⟨ls bonos⟩ [ɫz̺ ˈβonus̺] | [Vasconcelos 1900](#src-vasconcelos1900) |
| `MWL_SPIRANT_G_ONSET` | `(?:s̺\|[lɫɾ])$` | `^(ˈ?)ɡ` | right [ɣ] | ⟨l gato⟩ [ɫ ˈɣatu] | [Vasconcelos 1900](#src-vasconcelos1900) |
| `MWL_SENDIM_IEN_PROCLITIC` | `^ˈ?([bβks])iɨ̃$` | `^.` | left [ĩ] | ⟨bien feito⟩ [bĩ ˈfejtu] | [Vasconcelos 1900](#src-vasconcelos1900) |

The spec switches off 16 inherited rules: `AST_GLIDE_I_RISING`, `AST_GLIDE_U_RISING`, `AST_GLIDE_I_FALLING`, `AST_GLIDE_U_FALLING`, `AST_SPIRANT_B`, `AST_SPIRANT_D`, `AST_SPIRANT_G`, `AST_SPIRANT_G_INITIAL`, `AST_AFFRICATE_Y_INITIAL`, `AST_TRILL_AFTER_L_N_S`, `AST_NASAL_LABIAL`, `AST_NASAL_VELAR`, `AST_NASAL_FINAL`, `AST_VOICE_S`, `AST_VOICE_THETA`, `AST_VOICE_SH`.
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "mwl-x-sendim")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Sena](seh.md) · [Home](../index.md) · [Seneca →](see.md)
