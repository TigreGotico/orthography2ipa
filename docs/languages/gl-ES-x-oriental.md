# Eastern Galician (`gl-ES-x-oriental`)

<!-- atlas:summary begin -->
Eastern Galician is an Ibero-Romance variety, written in the Latin script. Its code names Spain. The `gl-ES-x-oriental` spec is at the research tier. It cites 3 sources and has 1 scored dataset.
<!-- atlas:summary end -->

<!-- atlas:header begin -->
| Field | Value |
|:--|:--|
| Code | `gl-ES-x-oriental` |
| Aliases | `gl-x-oriental` |
| ISO 639-3 | [glg](https://iso639-3.sil.org/code/glg), Galician |
| Wikipedia | [Galician language](https://en.wikipedia.org/wiki/Galician_language) |
| Family | [Indo-European](by-family.md#indo-european) > [Italic > Romance > Ibero-Romance](by-family.md#indo-european--italic--romance--ibero-romance) |
| Region | [Eurasia](by-region.md#eurasia) > [Spain](by-region.md#spain) |
| Script | [Latin](by-script.md#latin) (alphabet) |
| Tier | [research](../specs/quality_tiers.md#research) |
| Attested | from 1300, living |
| Parent | [Galician](gl-ES.md) `gl-ES` |
| Explorer | [`gl-ES-x-oriental` in the data explorer](https://tigregotico.github.io/orthography2ipa/#gl-ES-x-oriental) |
| Spec file | [`gl-ES-x-oriental.json`](../../orthography2ipa/data/gl-ES-x-oriental.json) |
<!-- atlas:header end -->

<!-- atlas:overview begin -->
## Overview

The notes of the spec file open with these words:

> Eastern Galician (galego oriental), spoken in the eastern provinces of Lugo and Ourense, bordering Asturias and Castile-León. KEY FEATURES: (1) STRONGER ASTURLEONESE CONTACT: the eastern zone was historically the zone of maximum Galician-Asturleonese overlap.

The spec is at the [research](../specs/quality_tiers.md#research) tier, which asks for a cited description, with stress and a measured gold. It cites 3 works, from 1990 to 2000. [Sources](#sources) lists them. The spec file writes 2 of the 71 spellings of its letter table and takes the other 69 from [Galician](gl-ES.md) `gl-ES`.

The [spec file](../../orthography2ipa/data/gl-ES-x-oriental.json) holds the full notes, with the caveats of the spec.
<!-- atlas:overview end -->

<!-- atlas:lects begin -->
## Related lects

No spec names `gl-ES-x-oriental` as its parent.
<!-- atlas:lects end -->

<!-- atlas:sources begin -->
## Sources

The spec cites 3 works. 0 of them have a DOI or a URL. The spec file holds a note on what each work supports.

1. <a id="src-freixeiro_mato1998"></a>Freixeiro Mato, X.R. (1998). *Gramática da Lingua Galega*. A Nosa Terra.
2. <a id="src-mateus_dandrade2000"></a>Mateus, M.H.M. & d'Andrade, E. (2000). *The Phonology of Portuguese*. Oxford University Press.
3. <a id="src-fernandez_rei1990"></a>Fernández Rei, F. (1990). *Dialectoloxía da lingua galega*. Xerais.
<!-- atlas:sources end -->

<!-- atlas:datasets begin -->
## Datasets

Every row of the board that scores this spec. PER is the phoneme error rate against the dataset. A gold row is human work, a silver row is a language model's label, and a generated row is the output of another tool. Only a row marked as gating can promote or block the spec. The [dataset catalogue](../evaluation/datasets.md) describes each set.

| Dataset | Row tag | Class | Provenance | Licence | Words | PER | Gates |
|:--|:--|:--|:--|:--|--:|--:|:--|
| `spain_romance_tts` | `gl-ES-x-oriental` | silver | llm-corrected | Apache-2.0 (this repository) | 20 | 0.0690 | no |
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
| ⟨ch⟩ | [tʃ] | intervocalic [tʃ] · word initial [tʃ] |
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
| `GL_OPEN_O` | /o/ → [ɔ], stressed, in 4 listed words | ⟨corre⟩ [ˈkɔre] | [Freixeiro 1998](#src-freixeiro_mato1998), Regueira 1996 |
| `GL_STOP_AFTER_NASAL` | /β/ → [b], after a coda nasal | ⟨ambos⟩ [ˈambos] | [Freixeiro 1998](#src-freixeiro_mato1998), Regueira 2010, Xove 2002 |
| `GL_STOP_AFTER_NASAL_D` | /ð/ → [d], after a coda nasal | - | Regueira 2010 |
| `GL_STOP_AFTER_NASAL_G` | /ɣ/ → [ɡ], after a coda nasal | ⟨tango⟩ [ˈtaŋɡo] | [Freixeiro 1998](#src-freixeiro_mato1998), Regueira 2010 |
| `GL_NASAL_VELAR` | /n/ → [ŋ], before [k] [ɡ] [ɣ] [x] | ⟨Angumil⟩ [aŋɡuˈmil] | [Freixeiro 1998](#src-freixeiro_mato1998), Regueira 2010, Xove 2002 |
| `GL_NASAL_LABIAL` | /n/ → [m], before [p] [b] [β] [m] | ⟨benvida⟩ [bemˈbiða] | [Freixeiro 1998](#src-freixeiro_mato1998), Regueira 2010 |
| `GL_NASAL_FINAL_NS` | /n/ → [ŋ], before [s], with more context in the spec | ⟨Bertamiráns⟩ [beɾtamiˈɾaŋs] | [Freixeiro 1998](#src-freixeiro_mato1998), Regueira 2010 |
| `GL_RAISE_O_BEFORE_NASAL` | /ɔ/ → [o], before a coda nasal, before [n] [m] [ŋ] [ɲ] | ⟨Antón⟩ [anˈtoŋ] | [Freixeiro 1998](#src-freixeiro_mato1998), Regueira 2010 |
| `GL_TRILL_AFTER_L_N_S` | /ɾ/ → [r], after [l] [n] [s] [ŋ] | ⟨alroto⟩ [alˈroto] | [Freixeiro 1998](#src-freixeiro_mato1998), Xove 2002 |
| `GL_STOP_BEFORE_IDENTICAL_B` | /β/ → [b], before [β] | - | [Freixeiro 1998](#src-freixeiro_mato1998), Regueira 2010 |
| `GL_STOP_BEFORE_IDENTICAL_D` | /ð/ → [d], before [ð] | - | [Freixeiro 1998](#src-freixeiro_mato1998), Regueira 2010 |
| `GL_STOP_BEFORE_IDENTICAL_G` | /ɣ/ → [ɡ], before [ɣ] | - | [Freixeiro 1998](#src-freixeiro_mato1998), Regueira 2010 |
<!-- atlas:rules end -->

<!-- atlas:examples begin -->
## Examples

The engine wrote every transcription in this section with `orthography2ipa.transcribe(text, "gl-ES-x-oriental")`. They are engine output, not reference transcriptions.

No example words are chosen for this page yet.
<!-- atlas:examples end -->

<!-- atlas:related begin -->
## Related repositories

No downstream repository of the TigreGotico organisation covers this spec. The [o2i-lexicons](https://github.com/TigreGotico/o2i-lexicons) package ships no lexicon for it.
<!-- atlas:related end -->

---
[← Eastern Egyptian Bedawi Arabic](avl-EG.md) · [Home](../index.md) · [Eastern Mari →](mhr.md)
