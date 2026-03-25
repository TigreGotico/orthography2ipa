# Language Registry

## Overview

The registry (`registry.py:68-82`) resolves language codes and lazily loads `LanguageSpec` objects from JSON data files under `orthography2ipa/data/`. Languages are loaded **lazily** — only when first requested via `get()`.

---

## API

```python
import orthography2ipa

# Fetch a spec by code
spec = orthography2ipa.get("pt-BR")

# List all registered codes
codes = orthography2ipa.available_codes()

# Group codes by family
families = orthography2ipa.available_families()
# Returns: {'Romance': ['ca', 'es', ...], 'Germanic': ['de', 'en', ...], ...}
```

---

## Supported Languages

### Romance Family

| Code | Language / Variety |
|---|---|
| `la` | Classical Latin |
| `la-x-hispania` | Hispanic Vulgar Latin |
| `la-x-gallia` | Gallo-Latin (ancestor of French/Occitan) |
| `pt` | Portuguese (European standard) |
| `pt-BR` | Brazilian Portuguese |
| `pt-AO` | Angolan Portuguese |
| `pt-PT-x-lisbon` | Lisbon Portuguese |
| `pt-PT-x-porto` | Porto Portuguese |
| `pt-PT-x-minho` | Minhoto dialect |
| `pt-PT-x-alfena` | Alfena dialect |
| `pt-PT-x-viana` | Viana do Castelo dialect |
| `pt-PT-x-aveiro` | Aveiro dialect |
| `pt-PT-x-alentejo` | Alentejo dialect |
| `pt-PT-x-algarve` | Algarve dialect |
| `pt-PT-x-acores` | Azorean Portuguese |
| `pt-PT-x-madeira` | Madeiran Portuguese |
| `pt-PT-x-trasosmontes` | Trás-os-Montes dialect |
| `pt-BR-x-sp` | São Paulo Brazilian Portuguese |
| `pt-BR-x-rj` | Rio de Janeiro Brazilian Portuguese |
| `pt-BR-x-fluminense` | Fluminense dialect |
| `pt-BR-x-mg` | Minas Gerais dialect |
| `pt-BR-x-caipira` | Caipira dialect |
| `pt-BR-x-recife` | Recife (Pernambuco) dialect |
| `pt-BR-x-bahia` | Bahian dialect |
| `pt-BR-x-ce` | Cearense dialect |
| `pt-BR-x-norte` | Northern Brazilian Portuguese |
| `pt-BR-x-sul` | Southern Brazilian Portuguese |
| `pt-BR-x-pr` | Paraná dialect |
| `pt-BR-x-brasilia` | Brasília dialect |
| `es` | Spanish (Castilian / Peninsular) |
| `es-419` | Latin American Spanish |
| `es-AR` | Rioplatense Spanish (Argentina/Uruguay) |
| `es-MX` | Mexican Spanish |
| `es-MX-x-costa` | Mexican coastal Spanish |
| `es-CU` | Cuban Spanish |
| `es-DO` | Dominican Spanish |
| `es-PR` | Puerto Rican Spanish |
| `es-VE` | Venezuelan Spanish |
| `es-CO` | Colombian Spanish |
| `es-CO-x-costa` | Colombian coastal Spanish |
| `es-CO-x-paisa` | Paisa dialect |
| `es-PE` | Peruvian Spanish |
| `es-PE-x-lima` | Lima Spanish |
| `es-BO` | Bolivian Spanish |
| `es-EC` | Ecuadorian Spanish |
| `es-CL` | Chilean Spanish |
| `es-PY` | Paraguayan Spanish |
| `es-UY` | Uruguayan Spanish |
| `es-GT` | Guatemalan Spanish |
| `es-NI` | Nicaraguan Spanish |
| `es-CR` | Costa Rican Spanish |
| `es-PA` | Panamanian Spanish |
| `es-GQ` | Equatorial Guinea Spanish |
| `es-ES-x-andalusia-w` | Western Andalusian Spanish |
| `es-ES-x-andalusia-e` | Eastern Andalusian Spanish |
| `es-ES-x-murcia` | Murcian Spanish |
| `es-ES-x-canarias` | Canarian Spanish |
| `es-ES-x-cantabria` | Cantabrian Spanish |
| `fr` | French |
| `it` | Italian |
| `ro` | Romanian |
| `ca` | Catalan |
| `ca-x-valencia` | Valencian |
| `ca-x-balear` | Balearic Catalan |
| `ca-x-nord` | Northern Catalan |
| `ca-x-occidental` | Western Catalan |
| `oc` | Occitan |
| `oc-x-aranes` | Aranese (Gascon Occitan) |
| `gl` | Galician |
| `gl-x-occidental` | Western Galician |
| `gl-x-central` | Central Galician |
| `gl-x-oriental` | Eastern Galician |
| `fax` | Fala (Galician-Portuguese isolate in Spain) |
| `ast` | Asturian |
| `ast-x-occidental` | Western Asturian |
| `ast-x-oriental` | Eastern Asturian |
| `ast-ES-x-leon` | Leonese |
| `an` | Aragonese |
| `an-x-occidental` | Western Aragonese |
| `an-x-oriental` | Eastern Aragonese |
| `ext` | Extremaduran |
| `ext-x-septentrional` | Northern Extremaduran |
| `mwl` | Mirandese |
| `mwl-x-sendim` | Sendinese Mirandese |
| `grc` | Ancient Greek |

### Contact / Transition Languages (Iberian)

| Code | Language / Variety |
|---|---|
| `ext-PT-x-barrancos` | Barranquenho (Portuguese-Spanish contact) |
| `ast-PT-x-rionor` | Rionorês (Asturian-Leonese in Portugal) |
| `ast-PT-x-guadramil` | Guadramilês |
| `mxi` | Mozarabic |
| `xaa` | Andalusi Arabic |

### Pre-Roman Iberian Peninsula

| Code | Language |
|---|---|
| `xce` | Celtiberian |
| `xib` | Iberian (non-IE) |
| `xlg` | Lusitanian |
| `txr` | Tartessian |
| `xaq` | Proto-Basque (Aquitanian) |
| `cel` | Common Celtic |
| `xcg` | Galatian Celtic |
| `phn` | Phoenician |

### Historical / Proto-Languages

| Code | Language |
|---|---|
| `ine` | Proto-Indo-European |
| `gem` | Proto-Germanic |
| `got` | Gothic |

### Germanic Family

| Code | Language |
|---|---|
| `en` | English |
| `de` | German |
| `nl` | Dutch |
| `sv` | Swedish |
| `da` | Danish |
| `no` | Norwegian (Bokmål) |

### Slavic Family

| Code | Language |
|---|---|
| `ru` | Russian |
| `uk` | Ukrainian |
| `pl` | Polish |
| `cs` | Czech |

### Semitic Family

| Code | Language |
|---|---|
| `ar` | Arabic (Modern Standard) |

### Indo-Iranian Family

| Code | Language |
|---|---|
| `fa` | Persian (Farsi) |
| `hi` | Hindi |

### Sino-Tibetan / Japonic / Koreanic

| Code | Language |
|---|---|
| `zh` | Mandarin Chinese |
| `ja` | Japanese |
| `ko` | Korean |

### Basque (Language Isolate)

| Code | Language |
|---|---|
| `eu` | Standard Basque (Batua) |
| `eu-x-bizkaiera` | Bizkaian dialect |
| `eu-x-gipuzkera` | Gipuzkoan dialect |
| `eu-x-nafarra-garaia` | High Navarrese |
| `eu-x-zuberera` | Souletin (Zuberoan) |
| `eu-x-nafarra-beherea` | Low Navarrese |

### Turkic Family

| Code | Language |
|---|---|
| `tr` | Turkish |

### Uralic Family

| Code | Language |
|---|---|
| `fi` | Finnish |

### Hellenic Family

| Code | Language |
|---|---|
| `el` | Modern Greek |

---

## Code Aliases

The following ISO 639-3 codes are automatically resolved to BCP-47:

| ISO 639-3 | BCP-47 |
|---|---|
| `por` | `pt` |
| `eng` | `en` |
| `spa` | `es` |
| `fra` | `fr` |
| `deu` | `de` |
| `ita` | `it` |
| `nld` | `nl` |
| `swe` | `sv` |
| `dan` | `da` |
| `nor` | `no` |
| `rus` | `ru` |
| `ukr` | `uk` |
| `ara` | `ar` |
| `fas` | `fa` |
| `hin` | `hi` |
| `zho` | `zh` |
| `jpn` | `ja` |
| `kor` | `ko` |
| `eus` | `eu` |
| `cat` | `ca` |
| `glg` | `gl` |
| `oci` | `oc` |
| `tur` | `tr` |
| `fin` | `fi` |
| `ell` | `el` |
| `pol` | `pl` |
| `ces` | `cs` |
| `ron` | `ro` |
| `mwl` | `mwl` |
| `arg` | `an` |
| `lat` | `la` |

---

## Language Families

```python
import orthography2ipa

families = orthography2ipa.available_families()
for family, codes in sorted(families.items()):
    print(f"{family}: {', '.join(codes[:5])}{'...' if len(codes) > 5 else ''}")
```

Expected output (partial):
```
Celtic: cel, xcg
Germanic: da, de, en, nl, no...
Hellenic: el, grc
Indo-Iranian: fa, hi
Isolate: eu, eu-x-bizkaiera, eu-x-gipuzkera...
Japonic: ja
Koreanic: ko
Proto-Indo-European: ine
Romance: an, ast, ca, ca-x-balear, ca-x-nord...
Semitic: ar, phn, xaa
Sino-Tibetan: zh
Slavic: cs, pl, ru, uk
Turkic: tr
Uralic: fi
```
