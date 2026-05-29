# Link audit

Audit of every URL in `orthography2ipa/data/*.json` (`sources[].url`, `sources[].wikipedia_url`, top-level `wikipedia`, top-level `urls`).

Wikipedia URLs are checked for article existence via the MediaWiki API; other URLs via an HTTP GET with a browser User-Agent. `403`/`429`/timeout/`5xx` responses are treated as inconclusive, never dead.

## Summary

| Metric | Count |
| --- | ---: |
| Total URL occurrences | 979 |
| Unique URLs | 646 |
| Valid | 601 |
| Dead | 44 |
| Inconclusive | 1 |
| Removed from JSON | 21 |
| Dead but kept (would empty a non-stub wikipedia) | 21 |
| Corrected (replaced with verified live URL) | 1 |

## Corrected links

Dead URLs replaced with a verified live equivalent.

| File | Field | Old URL | New URL | Verification |
| --- | --- | --- | --- | --- |
| `orthography2ipa/data/ar-DZ.json` | `wikipedia` | https://ar.wikipedia.org/wiki/العربية_الجزائرية | https://ar.wikipedia.org/wiki/لهجة_جزائرية | MediaWiki API: present (title='لهجة جزائرية', pageid=42352) |

## Dead links removed

| File | Field | URL | Reason | Wayback snapshot |
| --- | --- | --- | --- | --- |
| `orthography2ipa/data/aoa.json` | `urls` | https://endangeredlanguages.com/lang/2102 | HTTP 404 | no snapshot |
| `orthography2ipa/data/es-ES-x-cantabria.json` | `urls` | https://en.wikipedia.org/wiki/Cantabrian_Spanish | MediaWiki API: missing (title='Cantabrian Spanish') | no snapshot |
| `orthography2ipa/data/es-ES-x-cantabria.json` | `wikipedia` | https://en.wikipedia.org/wiki/Cantabrian_Spanish | MediaWiki API: missing (title='Cantabrian Spanish') | no snapshot |
| `orthography2ipa/data/eu-x-bizkaiera.json` | `urls` | https://glottolog.org/resource/languoid/id/bizk1238 | HTTP 404 | no snapshot |
| `orthography2ipa/data/eu-x-lapurtera.json` | `urls` | https://glottolog.org/resource/languoid/id/lapu1237 | HTTP 404 | no snapshot |
| `orthography2ipa/data/eu-x-nafarra-garaia.json` | `urls` | https://glottolog.org/resource/languoid/id/nava1268 | HTTP 404 | no snapshot |
| `orthography2ipa/data/eu-x-zuberera.json` | `urls` | https://glottolog.org/resource/languoid/id/soul1252 | HTTP 404 | no snapshot |
| `orthography2ipa/data/ff.json` | `urls` | https://en.wikipedia.org/wiki/Fula_phonology | MediaWiki API: missing (title='Fula phonology') | no snapshot |
| `orthography2ipa/data/frr.json` | `urls` | https://en.wikipedia.org/wiki/Mooring_dialect | MediaWiki API: missing (title='Mooring dialect') | no snapshot |
| `orthography2ipa/data/gem-x-ingvaeonic.json` | `urls` | https://de.wikipedia.org/wiki/Ingw%C3%A4onische_Sprachen | MediaWiki API: missing (title='Ingwäonische Sprachen') | no snapshot |
| `orthography2ipa/data/gl-x-central.json` | `urls` | https://en.wikipedia.org/wiki/Dialects_of_Galician | MediaWiki API: missing (title='Dialects of Galician') | no snapshot |
| `orthography2ipa/data/gl-x-central.json` | `wikipedia` | https://en.wikipedia.org/wiki/Dialects_of_Galician | MediaWiki API: missing (title='Dialects of Galician') | no snapshot |
| `orthography2ipa/data/lad.json` | `urls` | https://en.wikipedia.org/wiki/Judeo-Spanish_phonology | MediaWiki API: missing (title='Judeo-Spanish phonology') | no snapshot |
| `orthography2ipa/data/lij.json` | `wikipedia` | https://lij.wikipedia.org/wiki/Lengua_lìgure | MediaWiki API: missing (title='Lengua lìgure') | no snapshot |
| `orthography2ipa/data/nds.json` | `urls` | https://en.wikipedia.org/wiki/Low_German_phonology | MediaWiki API: missing (title='Low German phonology') | no snapshot |
| `orthography2ipa/data/pre.json` | `urls` | https://endangeredlanguages.com/lang/2095 | HTTP 404 | no snapshot |
| `orthography2ipa/data/pt-BR.json` | `urls` | https://pt.wikipedia.org/wiki/Fonologia_do_portugu%C3%AAs_brasileiro | MediaWiki API: missing (title='Fonologia do português brasileiro') | no snapshot |
| `orthography2ipa/data/pt-PT-x-acores.json` | `urls` | https://glottolog.org/resource/languoid/id/azor1234 | HTTP 404 | no snapshot |
| `orthography2ipa/data/pt-PT-x-alentejo.json` | `urls` | https://glottolog.org/resource/languoid/id/por1251 | HTTP 404 | no snapshot |
| `orthography2ipa/data/pt-PT-x-algarve.json` | `urls` | https://glottolog.org/resource/languoid/id/por1251 | HTTP 404 | no snapshot |
| `orthography2ipa/data/pt-PT-x-madeira.json` | `urls` | https://glottolog.org/resource/languoid/id/made1238 | HTTP 410 | no snapshot |
| `orthography2ipa/data/pt-PT-x-minho.json` | `urls` | https://glottolog.org/resource/languoid/id/por1251 | HTTP 404 | no snapshot |
| `orthography2ipa/data/pt-PT-x-trasosmontes.json` | `urls` | https://glottolog.org/resource/languoid/id/por1251 | HTTP 404 | no snapshot |
| `orthography2ipa/data/pt-ST.json` | `urls` | https://en.wikipedia.org/wiki/S%C3%A3o_Tom%C3%A9_Creole | MediaWiki API: missing (title='São Tomé Creole') | no snapshot |
| `orthography2ipa/data/pt-ST.json` | `wikipedia` | https://en.wikipedia.org/wiki/S%C3%A3o_Tom%C3%A9_Creole | MediaWiki API: missing (title='São Tomé Creole') | no snapshot |
| `orthography2ipa/data/ru-x-don.json` | `wikipedia` | https://en.wikipedia.org/wiki/Don_dialect | MediaWiki API: missing (title='Don dialect') | no snapshot |
| `orthography2ipa/data/ru-x-moscow.json` | `wikipedia` | https://en.wikipedia.org/wiki/Moscow_dialect_of_Russian | MediaWiki API: missing (title='Moscow dialect of Russian') | no snapshot |

## Dead links kept for human review

These returned a dead signal but were not auto-removed (either removing would empty the only top-level `wikipedia` entry of a non-stub language, or the link is explicitly protected). Review and either replace with the Wayback snapshot or a correct live URL.

| File | URL | Reason | Wayback snapshot |
| --- | --- | --- | --- |
| `orthography2ipa/data/ar-IQ-x-qeltu.json` | https://en.wikipedia.org/wiki/qǝltu_dialects | MediaWiki API: missing (title='qǝltu dialects') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/ast-PT-x-guadramil.json` | https://en.wikipedia.org/wiki/Guadramil | MediaWiki API: missing (title='Guadramil') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/da-x-copenhagen.json` | https://en.wikipedia.org/wiki/Copenhagen_dialect | MediaWiki API: missing (title='Copenhagen dialect') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/es-CO-x-paisa.json` | https://en.wikipedia.org/wiki/Paisa_dialect | MediaWiki API: missing (title='Paisa dialect') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/es-ES-x-murcia.json` | https://en.wikipedia.org/wiki/Murcian_dialect | MediaWiki API: missing (title='Murcian dialect') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/eu-x-bizkaiera.json` | https://en.wikipedia.org/wiki/Bizkaian_dialect | MediaWiki API: missing (title='Bizkaian dialect') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/eu-x-lapurtera.json` | https://en.wikipedia.org/wiki/Labourdian_dialect | MediaWiki API: missing (title='Labourdian dialect') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/it-IT-x-abruzzo.json` | https://en.wikipedia.org/wiki/Abruzzese_dialect | MediaWiki API: missing (title='Abruzzese dialect') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/it-IT-x-umbria.json` | https://en.wikipedia.org/wiki/Umbrian_dialect | MediaWiki API: missing (title='Umbrian dialect') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/mcm.json` | https://en.wikipedia.org/wiki/Macanese_Creole | MediaWiki API: missing (title='Macanese Creole') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/pt-BR-x-fluminense.json` | https://en.wikipedia.org/wiki/Fluminense_dialect | MediaWiki API: missing (title='Fluminense dialect') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/pt-BR-x-rj.json` | https://en.wikipedia.org/wiki/Carioca_dialect | MediaWiki API: missing (title='Carioca dialect') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/pt-MO.json` | https://en.wikipedia.org/wiki/Macanese_Creole | MediaWiki API: missing (title='Macanese Creole') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/pt-PT-x-acores.json` | https://en.wikipedia.org/wiki/Azorean_Portuguese | MediaWiki API: missing (title='Azorean Portuguese') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/pt-PT-x-alentejo.json` | https://en.wikipedia.org/wiki/European_Portuguese_phonology | MediaWiki API: missing (title='European Portuguese phonology') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/pt-PT-x-algarve.json` | https://en.wikipedia.org/wiki/Algarvian_Portuguese | MediaWiki API: missing (title='Algarvian Portuguese') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/pt-PT-x-algarve.json` | https://en.wikipedia.org/wiki/European_Portuguese_phonology | MediaWiki API: missing (title='European Portuguese phonology') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/pt-PT-x-beira.json` | https://en.wikipedia.org/wiki/Beira_Portuguese | MediaWiki API: missing (title='Beira Portuguese') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/pt-PT-x-lisbon.json` | https://en.wikipedia.org/wiki/Lisbon_dialect | MediaWiki API: missing (title='Lisbon dialect') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/pt-PT-x-madeira.json` | https://en.wikipedia.org/wiki/Madeiran_Portuguese | MediaWiki API: missing (title='Madeiran Portuguese') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/pt-PT-x-porto.json` | https://en.wikipedia.org/wiki/Porto_dialect | MediaWiki API: missing (title='Porto dialect') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/pt-PT-x-trasosmontes.json` | https://en.wikipedia.org/wiki/European_Portuguese_phonology | MediaWiki API: missing (title='European Portuguese phonology') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/ru-x-northern.json` | https://en.wikipedia.org/wiki/Northern_Russian_dialect | MediaWiki API: missing (title='Northern Russian dialect') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |
| `orthography2ipa/data/ru-x-southern.json` | https://en.wikipedia.org/wiki/Southern_Russian_dialect | MediaWiki API: missing (title='Southern Russian dialect') | NOT removed: sole/last surviving top-level wikipedia entry for a non-stub language (would break test_non_stub_has_wikipedia) | no snapshot |

## Dead links in prose notes (not auto-edited)

These dead URLs appear only inside free-text `notes` fields, so they are left untouched. Update the surrounding citation manually if desired.

| File | Field | URL | Reason |
| --- | --- | --- | --- |
| `orthography2ipa/data/ext-PT-x-barrancos.json` | `/notes` | https://github.com/NLP-Workspace/g2p-barranquenho), | HTTP 404 |

## Inconclusive (for human review)

Reachability could not be confirmed either way (403/429/timeout/5xx). **Not** removed.

| File | Field | URL | Reason |
| --- | --- | --- | --- |
| `orthography2ipa/data/cop.json` | `/wikipedia` | https://cop.wikipedia.org/wiki/ϯⲙⲉⲧⲣⲉⲙⲛ̀ⲭⲏⲙⲓ | API error: <urlopen error [Errno -2] Name or service not known> |
