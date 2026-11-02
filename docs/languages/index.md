# Language pages

Most registered specs have no page of their own. The JSON spec is the source
of truth for every language, and it describes itself: its graphemes,
allophones, rules, sources and `notes`. Read it from Python or from the shell:

```python
import orthography2ipa

spec = orthography2ipa.get("fi")
spec.name, spec.family, spec.script, spec.quality
spec.notes     # linguistic notes, with the known caveats
spec.sources   # the cited references
```

```bash
orthography2ipa info fi --graphemes
```

A page exists where a language needs prose to explain why its tables look the
way they do: an irregular orthography, a contested analysis, or a family of
dialects that share one base. To decide whether a language is fit for your
use, read its `quality` tier ([../specs/quality_tiers.md](../specs/quality_tiers.md)) and
its rows on the [scoreboard](../evaluation/generated/scoreboard.md). Whether a page exists says
nothing about either.

## Pages by family

### Germanic

| Page | Covers |
| :--- | :--- |
| [comparative.md](comparative.md) | Comparative tables for the Germanic, Romance and Slavic families |
| [en-GB.md](en-GB.md) | British RP (`en-GB`) and General American (`en-US`) |
| [de-DE.md](de-DE.md) | Standard German |
| [fo.md](fo.md) | Faroese: Hammershaimb's etymological orthography and the positional rules it needs |

### Romance

| Page | Covers |
| :--- | :--- |
| [es-ES.md](es-ES.md) | Castilian Spanish |
| [ro-RO.md](ro-RO.md) | Romanian |
| [fr-FR.md](fr-FR.md) | French |
| [it-IT.md](it-IT.md) | Italian |
| [lij.md](lij.md) | Ligurian (Genoese): ⟨x⟩ as /ʒ/, ⟨o⟩ as /u/, ⟨u⟩ as /y/ |
| [an-valleys.md](an-valleys.md) | The Pyrenean-valley Aragonese varieties: Cheso, Ansotano, Belsetán, Chistabín, Tensino |

### Portuguese

`pt-PT` and `pt-BR` are the two base specs. Each regional spec is a set of
differences over one of them.

| Page | Covers |
| :--- | :--- |
| [pt-PT.md](pt-PT.md) | European Portuguese: vowel reduction, coda allophony |
| [pt-PT-dialects.md](pt-PT-dialects.md) | The European regional specs, from Alto-Minho to the Azores |
| [pt-BR.md](pt-BR.md) | Brazilian Portuguese: positional maps and post-lexical allophony |
| [pt-BR-dialects.md](pt-BR-dialects.md) | The Brazilian regional specs: Carioca, Paulistano, Caipira, Mineiro, the South, the North and the Northeast |
| [pt-AO.md](pt-AO.md) | Angolan Portuguese |
| [pt-CV.md](pt-CV.md) | Cape Verdean Portuguese, which is not the Kabuverdianu creole (`kea`) |
| [pt-MZ.md](pt-MZ.md) | Mozambican Portuguese |
| [pt-MO.md](pt-MO.md) | Macau Portuguese, which is not the Patuá creole |
| [pt-TL.md](pt-TL.md) | East Timorese Portuguese, which is not the Bidau creole |
| [pt-UY.md](pt-UY.md) | Uruguayan Portuguese of the Brazilian border |
| [ext-PT-x-barrancos.md](ext-PT-x-barrancos.md) | Barranquenho, the Portuguese and Spanish contact variety of Barrancos |

### Asturleonese

| Page | Covers |
| :--- | :--- |
| [mwl.md](mwl.md) | Mirandese and its Sendinês and Ifanês sub-dialects |

### Slavic

| Page | Covers |
| :--- | :--- |
| [ru.md](ru.md) | Russian |

### Semitic

| Page | Covers |
| :--- | :--- |
| [ar.md](ar.md) | Modern Standard Arabic: the abjad, the input contract that depends on tashkeel, emphasis spread |
| [ar-dialects.md](ar-dialects.md) | The Arabic dialect specs: Egyptian, the Arabian Peninsula, the Levant, Iraq, the Maghreb and Sudan |

### Other families

| Page | Covers |
| :--- | :--- |
| [kab.md](kab.md) | Kabyle (Berber): the Berber Latin alphabet, spirantization, emphatics |
| [egy.md](egy.md) | Ancient Egyptian: Egyptological transliteration in, the Egyptological reading out |
| [ha.md](ha.md) | Hausa (Chadic): the hooked letters, ⟨ts⟩ as /sʼ/, and the contrasts the spelling hides |
| [hi.md](hi.md) | Hindi (Indo-Aryan): Devanagari, schwa deletion |
| [as.md](as.md) | Assamese (Indo-Aryan): the Assamese script read on Assamese phonology |
| [mn.md](mn.md) | Mongolian (Khalkha) in Cyrillic |
| [eu.md](eu.md) | Basque and its dialects: the sibilant systems, aspiration, Souletin /y/ and nasal vowels |
| [fi.md](fi.md) | Finnish (Uralic) |
| [vi.md](vi.md) | Vietnamese (Hanoi): rime-level mapping and tone from the orthography |
| [th.md](th.md) | Standard Thai: tone computed from the consonant class, syllable shape, vowel length and tone mark |
| [yo.md](yo.md) | Yoruba: three level tones and the nasal vowels |
| [eo.md](eo.md) | Esperanto |

### Latin American Spanish

Every Latin American national variety has a spec, and so do the main regional
zones of Lipski's classification
([Lipski, "Geographical and Social Varieties of Spanish: An Overview"](https://johnlipski.github.io/geo.pdf)).
The ancestry and distance metrics therefore resolve for the whole family.
These specs have no page. List them with
`orthography2ipa list --family Ibero-Romance`.

| Country | Regional specs (`es-XX-x-...`) |
| :--- | :--- |
| Argentina (`es-AR`) | `cordoba`, `cuyo`, `litoral`, `norte`, `patagonia` |
| Mexico (`es-MX`) | `costa`, `norte`, `yucatan` |
| Colombia (`es-CO`) | `costa`, `llanero`, `pacifico`, `paisa`, `santander`, `valluno` |
| Peru (`es-PE`) | `amazonico`, `andino`, `lima` |
| Chile (`es-CL`) | `andino`, `chilote` |
| Venezuela (`es-VE`) | `andino`, `llanero`, `maracucho` |
| Bolivia (`es-BO`) | `andino`, `camba` |
| Ecuador (`es-EC`) | `andino`, `costa` |

## Phenomena

Use this table to find how the library handles one phonological process
across languages.

| Phenomenon | Where to read |
| :--- | :--- |
| Final devoicing | [comparative.md](comparative.md#germanic-languages), [de-DE.md](de-DE.md) |
| Softening of ⟨c⟩ and ⟨g⟩ before front vowels | [comparative.md](comparative.md#romance-languages), [../engine/positional_graphemes.md](../engine/positional_graphemes.md) |
| Unstressed vowel reduction | [pt-PT.md](pt-PT.md), [ru.md](ru.md) |
| Weak or absent reduction in African Portuguese | [pt-AO.md](pt-AO.md), [pt-MZ.md](pt-MZ.md), [pt-CV.md](pt-CV.md) |
| Coda allophony: dark /l/, coda sibilants | [pt-PT.md](pt-PT.md), [../engine/allophony.md](../engine/allophony.md) |
| Nasal vowels | [fr-FR.md](fr-FR.md), [comparative.md](comparative.md#slavic-languages), [eu.md](eu.md) |
| Apical and laminal sibilants | [eu.md](eu.md), [pt-PT-dialects.md](pt-PT-dialects.md#northern-sibilant-systems), [mwl.md](mwl.md) |
| Retroflex consonants | [hi.md](hi.md), [pt-BR-dialects.md](pt-BR-dialects.md#caipira-pt-br-x-caipira) |
| Schwa deletion and the inherent vowel | [hi.md](hi.md), [as.md](as.md) |
| Geminates | [it-IT.md](it-IT.md), [kab.md](kab.md) |
| Spirantization | [kab.md](kab.md) |
| Tone from the orthography | [vi.md](vi.md), [th.md](th.md), [yo.md](yo.md), [ha.md](ha.md) |
| Liaison and other cross-word rules | [fr-FR.md](fr-FR.md), [../engine/lattice.md](../engine/lattice.md#the-sentence-context-seam) |
| Input that depends on tashkeel | [ar.md](ar.md), [ar-dialects.md](ar-dialects.md#what-the-dialect-specs-share) |
| Arabic dialect reflexes of qāf, jīm and kāf | [ar-dialects.md](ar-dialects.md#defining-features-by-lect) |

A language with no page above is described by its spec alone. To write a
page, follow [../contributing/spec_authoring.md](../contributing/spec_authoring.md) and add the
page to a table here.

---
[← Spec diagnostics](../evaluation/generated/spec_diagnostics.md) · [Home](../index.md) · [Comparative phonology →](comparative.md)
