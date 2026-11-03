# Barranquenho (ext-PT-x-barrancos)

| Field | Value |
|:---|:---|
| Code | `ext-PT-x-barrancos` |
| Family | Indo-European > Italic > Romance > Ibero-Romance |
| Script | Latin (alphabet) |
| Quality tier | research |
| Parent | none: a language of its own, with Portuguese and Extremaduran contributors |
| Glottolog, ISO 639-3 | none |
| Sources | Navas Sánchez-Élez (2011), Clements, Amaral & Luís (2008, *BLS* 34), *Convenção Ortográfica do Barranquenho* (2025), Gonçalves, Navas & Correia (2025, *Gramática Básica de Barranquenho*), Gonçalves, Navas & Ferreira (2025, *Dicionário de Barranquenho*) |

Barranquenho is the contact vernacular of Barrancos, in the Baixo Alentejo of Portugal. About 1,600 to 2,000 people speak it, and UNESCO lists it as *definitely endangered*. The Spanish province of Huelva (Andalusia) surrounds Barrancos on three sides, and Extremadura borders it. Barranquenho is a contact language (Navas Sánchez-Élez 2011, Clements, Amaral & Luís 2008). It has an Alentejo European Portuguese base with a pervasive Extremaduran and Andalusian Spanish adstrate. Clements, Amaral & Luís call it a mixed language, and a mixed language is a dialect of neither parent. So the spec overrides several inherited European Portuguese processes.

The code is a private-use tag. Its `ext-PT-` prefix marks Barranquenho as a language of its own, spoken in Portugal, not as a lect of `pt-PT`. The prefix records that modelling decision, not a genealogy. Glottolog has no languoid for the variety and ISO 639-3 has no code, so both cross-reference fields are null. The retired spelling `pt-PT-x-barrancos` still resolves through the alias table in `orthography2ipa/registry.py`.

Every transcription on this page is real output of `orthography2ipa.transcribe(text, "ext-PT-x-barrancos")`. For the scores of the spec, see [../evaluation/generated/scoreboard.md](../evaluation/generated/scoreboard.md).

## Inheritance and the contact overrides

The spec has no `parent`, as for a creole. Its `ancestors` weight the contributors without a claim of descent:

| Ancestor | Role | Weight |
|:---|:---|---:|
| `pt-PT` | lexifier | 0.6 |
| `ext` (Extremaduran) | adstrate | 0.35 |
| `roa-x-galaicopt` | substrate | 0.05 |

The spec takes its data from `pt-PT` through `graphemes_base`, `allophones_base`, `positional_graphemes_base` and `word_exceptions_base`. The `allophone_rules` inherit by id (see [../engine/allophony.md](../engine/allophony.md#inheritance)): a child rule with the same id replaces the inherited rule in place. So without overrides, Barranquenho would inherit the Lisbon *chiado* of the coda sibilants and the dark coda /l/. Those are the European features that Barranquenho does not share, and the spec redeclares their ids:

| Inherited rule id | pt-PT surface | Barranquenho surface | Reason |
|:---|:---|:---|:---|
| `PT_CODA_S_HUSH` | coda /s/ gives [ʃ] | [h] | Andalusian aspiration, not *chiado* |
| `PT_CODA_Z_HUSH` | coda /z/ gives [ʒ] | [h] | coda sibilants merge in the aspirate |
| `PT_CODA_L_DARK` | coda /l/ gives [ɫ] | [l] | clear alveolar /l/, no velarisation |

The spec also switches off the `pt-PT` suffix and word-list rules for stressed vowel height and the rules for ⟨-em -en -ens⟩. Their notes say that no source on these endings in Barranquenho was read.

## Contact features modelled

1. The coda /s/ and /z/ aspirate to [h]. This is the most salient contact trait. All southern peninsular varieties (Extremaduran and Andalusian) share it, and no Portuguese dialect has it: `mesmo` [ˈmɛhmu], `Lisboa` [ˈlihbuɐ], `visto` [ˈbihtu]. The overridden rule `PT_CODA_S_HUSH` produces the [h] (Navas 2011, Clements et al. 2008, Convenção pp. 28-29).
2. A word-final /s/, /r/ and /l/ drop. The absolute final /s/ is silent and not written (`costas` [ˈkɔhtɐ]). A stressed final /r/ drops (*cantá*, *senhô*, *dotô*), and so does a stressed final /l/ (*Brasí*, *Natá*, *Isabé*). The positional map gives an empty value for ⟨s r l⟩ at the end of a word (Convenção pp. 31-32, Gramática pp. 19-20, Clements et al. 2008).
3. Betacism merges /v/ and /b/. The letter ⟨v⟩ gives /b/, and /v/ is not a phoneme. Spanish and Northern Portuguese share the merger (Navas 2011, Gramática p. 17). The spec lists the spirant [β] as the second allophone of /b/: `vaca` [ˈbakɐ], `ovo` [ˈobu].
4. The letter ⟨h⟩ is /h/, with [x] as a second allophone for Spanish loans (`hora` [ˈhɔɾɐ]). A word-initial ⟨r⟩ and ⟨rr⟩ are the alveolar trill /r/, not the European uvular /ʁ/ (`rato` [ˈratu]). The trigraph ⟨tch⟩ is the affricate /tʃ/ (`tchicu` [ˈtʃiku]).
5. *Seseo*: ⟨c⟩ before ⟨e i⟩, ⟨ç⟩, ⟨s⟩ and ⟨z⟩ all give alveolar sibilants, with no Castilian interdental (`cidade` [siˈdadɨ], `paçu` [ˈpasu]).
6. A vowel before a coda ⟨m n⟩ nasalises, and the nasal consonant goes. An ⟨m n⟩ between vowels is an onset and leaves the vowel oral. The details follow this list.
7. The stressed nasal diphthongs ⟨-âu⟩, ⟨-âi⟩ and ⟨-ôi⟩ give [ɐ̃w̃], [ɐ̃j] and [õj] (`pâu` [ˈpɐ̃w̃], `pãi` [ˈpɐ̃j], `bôi` [ˈbõj]).
8. The monosyllables *mal*, *tal*, *cual* and *pur* (Portuguese *por*) keep their final liquid. The Convenção (§2.6, *Nota*) reports that their lateral is pronounced in most contexts. The spec lists them in `word_exceptions` (`mal` [ˈmal], `cual` [ˈkwal]). Polysyllables still drop it. The list also holds `aqui` [ɐˈki].

The nasal vowels come from the nasal consonant. A coda ⟨m n⟩ comes before a consonant or at the end of a word. The positional map writes it as a combining tilde (U+0303) on the vowel before it. The tokenizer reads the digraphs ⟨nh lh⟩ first, so they never nasalise by mistake (`banho` [ˈbaɲu]). The rules `PT_NASAL_A_RAISE` and `PT_NASAL_O_RAISE` then raise ⟨a⟩ to [ɐ] and ⟨o⟩ to [o] before the tilde. The rule `EXT_E_RAISE_BEFORE_NASAL` raises /ɛ/ to [e] before a nasal consonant, also before an onset nasal that leaves the vowel oral (`pequenu` [pɨˈkenu]). The Convenção (p. 26, §1.8.1 *Vocalismo nasal tónico*) gives the spelling of the coda nasal vowels.

So ⟨am an⟩ give [ɐ̃], ⟨em en⟩ give [ẽ], ⟨im in⟩ give [ĩ], ⟨om on⟩ give [õ], and ⟨um un⟩ give [ũ]: `campu` [ˈkɐ̃pu], `lindo` [ˈlĩdu], `bom` and `bon` [ˈbõ], `mundo` [ˈmũdu]. An onset nasal leaves the vowel oral: `lhano` [ˈʎanu], `cama` [ˈkamɐ]. Final ⟨em en⟩ give the plain nasal vowel [ẽ], not the European diphthong: `tem` [ˈtẽ], `bem` [ˈbẽ]. The spec does not inherit `PT_NASAL_E_UNRED`, so an unstressed nasal ⟨e⟩ keeps the reduced [ɨ̃]: `onten` [ˈõtɨ̃], `lembrá` [lɨ̃ˈbɾa].

## Vowel reduction from the Alentejo base

Barranquenho keeps the inherited European reduction of unstressed vowels. The Convenção spelling itself writes the final raising: a final ⟨-o⟩ is written ⟨u⟩, for [u], and a final ⟨-e⟩ is written ⟨i⟩. So the spec keeps the inherited `pt-PT` vowel positions and does not override them. The cited sources do not quantify the differences in pretonic vowels between Barranquenho and Lisbon at the resolution of a phoneme map. So the spec leaves them inherited.

## Worked examples

The examples use the Convenção spelling, which the spec expects.

| Spelling | IPA | Features |
|:---|:---|:---|
| `mesmo` | ˈmɛhmu | coda /s/ gives [h], final ⟨-o⟩ gives [u] |
| `visto` | ˈbihtu | betacism and coda /s/ aspiration |
| `vaca` | ˈbakɐ | betacism |
| `cantá` | kɐ̃ˈta | coda ⟨n⟩ nasalises ⟨a⟩ to [ɐ̃], no written final ⟨-r⟩ |
| `campu` | ˈkɐ̃pu | coda ⟨m⟩ nasalises ⟨a⟩ to [ɐ̃] |
| `lindo` | ˈlĩdu | coda ⟨n⟩ nasalises ⟨i⟩ to [ĩ] |
| `bom` | ˈbõ | coda ⟨m⟩ nasalises ⟨o⟩ to [õ], and the ⟨m⟩ goes |
| `lhano` | ˈʎanu | an onset ⟨n⟩ between vowels leaves the vowel oral |
| `mal` | ˈmal | a monosyllable keeps its final ⟨-l⟩ (Convenção §2.6 *Nota*) |
| `Brasí` | bɾɐˈzi | no written final ⟨-l⟩ |

## Limitations

- The board rows for this spec come from silver golds at the `llm-corrected` tier and from a small `expert-human` row, and none of them gates. So they measure agreement, not correctness, and the phonology on this page rests on its citations.
- The spec does not model the apico-alveolar articulation or the fine pretonic vowels.
- Coda /s/ varies freely between the aspirate [h] and full deletion. The spec reduces that variation to [h] inside the word and to deletion at the end of the word.
- The positional layer has no position for the syllable count. So the spec cannot state the monosyllable condition on the final liquid as a rule, and it uses a closed `word_exceptions` set (*mal*, *tal*, *cual*, *pur*).
- Input in Portuguese spelling can have a written final ⟨-r⟩ or ⟨-l⟩. The spec drops the consonant, and the word then takes the default stress on the penult: `cantar` [ˈkɐ̃tɐ], `Brasil` [ˈbɾazi]. The Convenção spelling gives the right stress.

## Relation to g2p_barranquenho

A dedicated downstream engine, `g2p_barranquenho`, uses this spec as its data layer. The spec supplies the pre-lexical grapheme and positional maps and the post-lexical contact overrides, and the engine builds on them. The spec and this page keep the input contract stable. Input is Barranquenho in the 2025 Convenção spelling. A final ⟨-o⟩ is written ⟨u⟩ and a final ⟨-e⟩ is written ⟨i⟩. A deleted final ⟨-r -l -s⟩ is not written. The engine relies on that shape.

## Sources

- Navas Sánchez-Élez, María Victoria (2011). *El barranqueño: un modelo de lenguas en contacto*. Madrid: Editorial Complutense / Centro de Linguística da Universidade de Lisboa, 320 pp. ISBN 978-84-9938-099-5.
- Clements, J. Clancy, Amaral, Patrícia & Luís, Ana R. (2008). "Cultural identity and the structure of a mixed language: The case of Barranquenho". *Proceedings of the Annual Meeting of the Berkeley Linguistics Society* 34, 13-22. <https://hdl.handle.net/2022/24680>
- *Convenção Ortográfica do Barranquenho* (2025). II Congresso Barranquenho, Câmara Municipal de Barrancos.
- Gonçalves, M. F., Navas, M. V. & Correia, V. M. D. (2025). *Gramática Básica de Barranquenho*. Universidade de Évora. ISBN 978-972-778-464-6.
- Gonçalves, M. F., Navas, M. V. & Ferreira, V. (2025). *Dicionário de Barranquenho*. Universidade de Évora. ISBN 978-972-778-460-8.

---
[← Uruguayan Portuguese](pt-UY.md) · [Home](../index.md) · [Mirandese →](mwl.md)
