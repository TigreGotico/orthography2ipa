# Galician (`gl-ES`)

<!-- atlas:summary begin -->
Galician is an Ibero-Romance language, written in the Latin script. Its code names Spain. The `gl-ES` spec is at the research tier. It cites 9 sources and has 3 scored datasets.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `gl-ES` |
| Aliases | `glg` |
| ISO 639-3 | [glg](https://iso639-3.sil.org/code/glg), Galician |
| Glottolog | [gali1258](https://glottolog.org/resource/languoid/id/gali1258), Galician |
| Wikidata | [Q9307](https://www.wikidata.org/wiki/Q9307) |
| Wikipedia | [Galician language](https://en.wikipedia.org/wiki/Galician_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Ibero-Romance](by-family.md#indo-european--italic--romance--ibero-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Spain](by-region.md#spain) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Ancestor | [Galaico-Portuguese](https://tigregotico.github.io/orthography2ipa/#roa-x-galaico-pt) `roa-x-galaico-pt` |
| Child lects | 6, see [Related lects](#related-lects) |
| Explorer | [`gl-ES` in the data explorer](https://tigregotico.github.io/orthography2ipa/#gl-ES) |
| Spec file | [`gl-ES.json`](../../orthography2ipa/data/gl-ES.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Standard Galician (galego) per the Real Academia Galega (RAG) *Normas ortográficas e morfolóxicas do idioma galego* (2003, revised 2012). Spoken by ~2.4 million people in the Autonomous Community of Galicia (Spain) and diaspora communities. KEY FEATURES vs.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 9 works, from 1979 to 2012. [Sources](#sources) lists them. The spec file writes all 71 spellings of its letter table itself.

The [spec file](../../orthography2ipa/data/gl-ES.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

These specs name `gl-ES` as their parent. They are sorted by country, and a lect with no recorded country comes last.

- [A Fala (Xalimego)](fax.md) `fax`: Portugal, Spain, research tier
- [Central Galician](gl-ES-x-central.md) `gl-ES-x-central`: Spain, research tier
- [Eonavian (Galician-Asturian, gallego-asturiano)](gl-ES-x-eonavia.md) `gl-ES-x-eonavia`: Spain, research tier
- [Western Galician](gl-ES-x-occident.md) `gl-ES-x-occident`: Spain, research tier
- [Eastern Galician](gl-ES-x-oriental.md) `gl-ES-x-oriental`: Spain, research tier
- [Galician (reintegrationist orthography)](gl-ES-x-reintegr.md) `gl-ES-x-reintegr`: Spain, research tier
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 9 works. 3 of them have a DOI or a URL. The spec file holds a note on what 6 of them support.

1. <a id="src-freixeiro_mato1998"></a>Freixeiro Mato, X.R. (1998). *Gramática da Lingua Galega*. A Nosa Terra.
2. <a id="src-mateus_dandrade2000"></a>Mateus, M.H.M. & d'Andrade, E. (2000). *The Phonology of Portuguese*. Oxford University Press.
3. <a id="src-carballo_calero1979"></a>Carballo Calero, R. (1979). *Gramática elemental del gallego común (7th ed.)*. Galaxia.
4. <a id="src-regueira1996"></a>Regueira, X.L. (1996). *Galician (Illustrations of the IPA)*. Journal of the International Phonetic Association 26(2). Cited: 119-122. [cambridge.org](https://www.cambridge.org/core/journals/journal-of-the-international-phonetic-association/article/galician/12F7CB857C4D8CD3B8634FBD250580CF)
5. <a id="src-cotovia_gtm_uvigo"></a>Gamallo, P., Regueira, X.L. & others (2012). *Cotovia TTS System (GTM, Universidade de Vigo)*. GTM, Universidade de Vigo.
6. <a id="src-regueira2010"></a>Regueira, X.L. (2010). *Dicionario de pronuncia da lingua galega*. Real Academia Galega / Instituto da Lingua Galega. [ilg.usc.gal](https://ilg.usc.gal/pronuncia/)
7. <a id="src-freixeiro_mato1998_fonetica"></a>Freixeiro Mato, X.R. (1998). *Gramática da lingua galega I: Fonética e fonoloxía*. A Nosa Terra.
8. <a id="src-alvarez_xove2002"></a>Álvarez, R. & Xove, X. (2002). *Gramática da lingua galega*. Galaxia.
9. <a id="src-rag_ilg2012_normas"></a>Real Academia Galega & Instituto da Lingua Galega (2012). *Normas ortográficas e morfolóxicas do idioma galego (23ª ed.)*. Real Academia Galega. Cited: 16, 21-26, 33-34. [publicacions.academia.gal](https://publicacions.academia.gal/index.php/rag/catalog/book/252)
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `wikipron` ([CUNY-CL/wikipron](https://github.com/CUNY-CL/wikipron)) | `gl-ES` | gold | crowd-scraped | Wiktionary terms: CC BY-SA and GFDL | 8091 | 0.0799 | yes |
| `vox_communis` ([fdemelo/vox-communis-parallel-g2p](https://huggingface.co/datasets/fdemelo/vox-communis-parallel-g2p)) | `gl-ES` | generated | epitran-derived | CC0 1.0 | 47512 | 0.0653 | no |
| `spain_romance_tts` | `gl-ES` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.0986 | no |
<!-- atlas:datasets end -->

<!-- atlas:inventory begin -->
## Inventory

The spec can emit 61 segments. They come from the letter table, the positional readings, the allophones and the rules, so the charts show what the spec can write, not a phonemic analysis. A segment with a diacritic sits in the cell of its base symbol.

| Consonants | Bilabial | Labiodental | Dental | Alveolar | Postalveolar | Palatal | Velar |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Plosive | b p |  |  | d t |  |  | k ɡ |
| Affricate |  |  |  |  | tʃ |  |  |
| Nasal | m |  |  | n |  | ɲ | ŋ |
| Trill |  |  |  | r |  |  |  |
| Tap |  |  |  | ɾ |  |  |  |
| Fricative | β | f | ð θ | s s̺ z | ʃ ʒ |  | ɣ |
| Approximant |  |  |  |  |  | j |  |
| Lateral approximant |  |  |  | l |  | ʎ |  |

| Vowels | Front | Back |
|:--|:-:|:-:|
| Close | i | u |
| Close-mid | e | o |
| Open-mid | ɛ | ɔ |
| Open | a |  |

Sequences that the spec writes as one unit: [aj] [aw] [ej] [ew] [iw] [ja] [jaj] [je] [jej] [jo] [jow] [jɔ] [jɛ] [oj] [ow] [uej] [w] [wa] [waj] [we] [wi] [wo] [wow] [wɔ] [wɛ] [ɔj] [ɛw] [ɡw].
<!-- atlas:inventory end -->

<!-- atlas:spelling begin -->
## Spelling

Each letter or letter group of the spec with its readings. The first reading is the default, and the others stay in the lattice as lower-ranked candidates. The last column gives the readings that depend on the position in the word.

| Spelling | Readings | By position |
|:--|:--|:--|
| ⟨a⟩ | [a] |  |
| ⟨ai⟩ | [aj] |  |
| ⟨au⟩ | [aw] |  |
| ⟨b⟩ | [b] | default [β] · intervocalic [β] · word initial [b] |
| ⟨c⟩ | [k] [θ] | before e [θ] · before i [θ] |
| ⟨ch⟩ | [tʃ] |  |
| ⟨d⟩ | [d] | default [ð] · intervocalic [ð] · word initial [d] |
| ⟨e⟩ | [e] [ɛ] |  |
| ⟨ei⟩ | [ej] |  |
| ⟨eu⟩ | [ew] |  |
| ⟨f⟩ | [f] |  |
| ⟨g⟩ | [ɡ] | default [ɣ] · intervocalic [ɣ] · word initial [ɡ] |
| ⟨gu⟩ | [ɡ] | before a [ɡw] · before e [ɡ] · before i [ɡ] · before o [ɡw] · default [ɡ] |
| ⟨h⟩ | ∅ |  |
| ⟨i⟩ | [i] |  |
| ⟨ia⟩ | [ja] |  |
| ⟨iai⟩ | [jaj] |  |
| ⟨ie⟩ | [je] |  |
| ⟨iei⟩ | [jej] |  |
| ⟨io⟩ | [jo] |  |
| ⟨iou⟩ | [jow] |  |
| ⟨iu⟩ | [iw] |  |
| ⟨iá⟩ | [ja] |  |
| ⟨ié⟩ | [jɛ] |  |
| ⟨ió⟩ | [jɔ] |  |
| ⟨k⟩ | [k] |  |
| ⟨l⟩ | [l] | onset [l] |
| ⟨ll⟩ | [ʎ] |  |
| ⟨m⟩ | [m] |  |
| ⟨n⟩ | [n] | before consonant [n] [ŋ] · word final [ŋ] |
| ⟨nh⟩ | [ŋ] |  |
| ⟨o⟩ | [o] [ɔ] |  |
| ⟨oi⟩ | [oj] |  |
| ⟨ou⟩ | [ow] |  |
| ⟨p⟩ | [p] |  |
| ⟨q⟩ | [k] |  |
| ⟨qu⟩ | [k] |  |
| ⟨r⟩ | [ɾ] | before consonant [ɾ] · intervocalic [ɾ] · word final [ɾ] · word initial [r] |
| ⟨rr⟩ | [r] |  |
| ⟨s⟩ | [s] |  |
| ⟨ss⟩ | [s] |  |
| ⟨t⟩ | [t] |  |
| ⟨u⟩ | [u] |  |
| ⟨ua⟩ | [wa] |  |
| ⟨uai⟩ | [waj] |  |
| ⟨ue⟩ | [we] |  |
| ⟨uei⟩ | [uej] |  |
| ⟨ui⟩ | [wi] |  |
| ⟨uo⟩ | [wo] |  |
| ⟨uou⟩ | [wow] |  |
| ⟨uá⟩ | [wa] |  |
| ⟨ué⟩ | [wɛ] |  |
| ⟨uó⟩ | [wɔ] |  |
| ⟨v⟩ | [b] | default [β] · intervocalic [β] · word initial [b] |
| ⟨w⟩ | [w] |  |
| ⟨x⟩ | [ʃ] |  |
| ⟨y⟩ | [j] [i] | after consonant [i] |
| ⟨z⟩ | [θ] |  |
| ⟨á⟩ | [a] |  |
| ⟨ái⟩ | [aj] |  |
| ⟨áu⟩ | [aw] |  |
| ⟨é⟩ | [ɛ] |  |
| ⟨éi⟩ | [ej] |  |
| ⟨éu⟩ | [ɛw] |  |
| ⟨í⟩ | [i] |  |
| ⟨ñ⟩ | [ɲ] |  |
| ⟨ó⟩ | [ɔ] |  |
| ⟨ói⟩ | [ɔj] |  |
| ⟨óu⟩ | [ow] |  |
| ⟨ú⟩ | [u] |  |
| ⟨ü⟩ | [w] |  |

Stress falls on the penult by default. A written ⟨á⟩ ⟨é⟩ ⟨í⟩ ⟨ó⟩ ⟨ú⟩ marks the stressed vowel. These endings take final stress: ⟨-r⟩ ⟨-l⟩ ⟨-z⟩ ⟨-x⟩ ⟨-d⟩ ⟨-ai⟩ ⟨-ain⟩ ⟨-ais⟩ ⟨-au⟩ ⟨-aun⟩ ⟨-aus⟩ ⟨-ei⟩ ⟨-ein⟩ ⟨-eis⟩ ⟨-eu⟩ ⟨-eun⟩ ⟨-eus⟩ ⟨-iu⟩ ⟨-iun⟩ ⟨-ius⟩ ⟨-oi⟩ ⟨-oin⟩ ⟨-ois⟩ ⟨-ou⟩ ⟨-oun⟩ ⟨-ous⟩ ⟨-ay⟩ ⟨-ey⟩ ⟨-oy⟩ ⟨-uy⟩. These endings take the penult: ⟨-n⟩ ⟨-s⟩ ⟨-ns⟩.
<!-- atlas:spelling end -->

<!-- atlas:rules begin -->
## Rules

The spec applies 12 allophone rules after the letters are read. The change column is built from the rule's conditions. The example and the citation are quoted from the rule's note in the spec file. A dash means that the note holds no worked example or no dated citation.

| Rule | Change | Example | Cited |
|:--|:--|:--|:--|
| `GL_OPEN_O` | /o/ → [ɔ], stressed, in 4 listed words | ⟨corre⟩ [ˈkɔre] | [Freixeiro 1998](#src-freixeiro_mato1998), [Regueira 1996](#src-regueira1996), [Freixeiro 1998](#src-freixeiro_mato1998_fonetica) |
| `GL_STOP_AFTER_NASAL` | /β/ → [b], after a coda nasal | ⟨ambos⟩ [ˈambos] | [Freixeiro 1998](#src-freixeiro_mato1998), [Regueira 2010](#src-regueira2010), [Freixeiro 1998](#src-freixeiro_mato1998_fonetica) |
| `GL_STOP_AFTER_NASAL_D` | /ð/ → [d], after a coda nasal | - | [Regueira 2010](#src-regueira2010) |
| `GL_STOP_AFTER_NASAL_G` | /ɣ/ → [ɡ], after a coda nasal | ⟨tango⟩ [ˈtaŋɡo] | [Freixeiro 1998](#src-freixeiro_mato1998), [Regueira 2010](#src-regueira2010), [Freixeiro 1998](#src-freixeiro_mato1998_fonetica) |
| `GL_NASAL_VELAR` | /n/ → [ŋ], before [k] [ɡ] [ɣ] [x] | ⟨Angumil⟩ [aŋɡuˈmil] | [Freixeiro 1998](#src-freixeiro_mato1998), [Regueira 2010](#src-regueira2010), [Freixeiro 1998](#src-freixeiro_mato1998_fonetica) |
| `GL_NASAL_LABIAL` | /n/ → [m], before [p] [b] [β] [m] | ⟨benvida⟩ [bemˈbiða] | [Freixeiro 1998](#src-freixeiro_mato1998), [Regueira 2010](#src-regueira2010), [Freixeiro 1998](#src-freixeiro_mato1998_fonetica) |
| `GL_NASAL_FINAL_NS` | /n/ → [ŋ], before [s], with more context in the spec | ⟨Bertamiráns⟩ [beɾtamiˈɾaŋs] | [Freixeiro 1998](#src-freixeiro_mato1998), [Regueira 2010](#src-regueira2010), [Freixeiro 1998](#src-freixeiro_mato1998_fonetica) |
| `GL_RAISE_O_BEFORE_NASAL` | /ɔ/ → [o], before a coda nasal, before [n] [m] [ŋ] [ɲ] | ⟨Antón⟩ [anˈtoŋ] | [Freixeiro 1998](#src-freixeiro_mato1998), [Regueira 2010](#src-regueira2010), [Freixeiro 1998](#src-freixeiro_mato1998_fonetica) |
| `GL_TRILL_AFTER_L_N_S` | /ɾ/ → [r], after [l] [n] [s] [ŋ] | ⟨alroto⟩ [alˈroto] | [Freixeiro 1998](#src-freixeiro_mato1998), [Freixeiro 1998](#src-freixeiro_mato1998_fonetica), [Álvarez 2002](#src-alvarez_xove2002) |
| `GL_STOP_BEFORE_IDENTICAL_B` | /β/ → [b], before [β] | - | [Freixeiro 1998](#src-freixeiro_mato1998), [Regueira 2010](#src-regueira2010), [Freixeiro 1998](#src-freixeiro_mato1998_fonetica) |
| `GL_STOP_BEFORE_IDENTICAL_D` | /ð/ → [d], before [ð] | - | [Freixeiro 1998](#src-freixeiro_mato1998), [Regueira 2010](#src-regueira2010), [Freixeiro 1998](#src-freixeiro_mato1998_fonetica) |
| `GL_STOP_BEFORE_IDENTICAL_G` | /ɣ/ → [ɡ], before [ɣ] | - | [Freixeiro 1998](#src-freixeiro_mato1998), [Regueira 2010](#src-regueira2010), [Freixeiro 1998](#src-freixeiro_mato1998_fonetica) |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "gl-ES")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Galibi Carib](car.md) · [Home](../index.md) · [Galician →](gl-ES-x-reintegr.md)
