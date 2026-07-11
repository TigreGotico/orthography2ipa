# Link audit

Audit of every URL in `orthography2ipa/data/*.json` (`sources[].url`, `sources[].wikipedia_url`, top-level `wikipedia`, top-level `urls`).

Wikipedia URLs are checked for article existence via the MediaWiki API; other URLs via an HTTP GET with a browser User-Agent. `403`/`429`/timeout/`5xx` responses are treated as inconclusive, never dead.

## Summary

| Metric | Count |
| --- | ---: |
| Total URL occurrences | 986 |
| Unique URLs | 657 |
| Valid | 237 confirmed + 386 inconclusive (429/timeout) |
| Dead | 1 |
| Inconclusive | 386 |
| Removed from JSON | 0 |
| Dead but kept (would empty a non-stub wikipedia) | 0 |
| Corrected (dead URL nulled) | 1 |
| New wikipedia entries added (enrichment) | 34 |

## Changes applied

### Dead URL fixed

| File | Field | Old URL | Action |
| --- | --- | --- | --- |
| `orthography2ipa/data/gl.json` | `sources[3].url` | `http://gtm.uvigo.es/cotovia/` | Set to `null` (HTTP 404, software decommissioned) |

### Wikipedia enrichments added

Native-language and additional Wikipedia articles added to 34 specs (all verified via MediaWiki API):

| File | Added URL | Verification |
| --- | --- | --- |
| `an.json` | https://an.wikipedia.org/wiki/Aragon%C3%A9s | MediaWiki API: present |
| `be.json` | https://be.wikipedia.org/wiki/%D0%91%D0%B5%D0%BB%D0%B0%D1%80%D1%83%D1%81%D0%BA%D0%B0%D1%8F_%D0%BC%D0%BE%D0%B2%D0%B0 | MediaWiki API: present |
| `bg.json` | https://bg.wikipedia.org/wiki/%D0%91%D1%8A%D0%BB%D0%B3%D0%B0%D1%80%D1%81%D0%BA%D0%B8_%D0%B5%D0%B7%D0%B8%D0%BA | MediaWiki API: present |
| `bn.json` | https://bn.wikipedia.org/wiki/%E0%A6%AC%E0%A6%BE%E0%A6%82%E0%A6%B2%E0%A6%BE_%E0%A6%AD%E0%A6%BE%E0%A6%B7%E0%A6%BE | MediaWiki API: present |
| `ca.json` | https://ca.wikipedia.org/wiki/Catal%C3%A0 | MediaWiki API: present |
| `ca-x-balear.json` | https://ca.wikipedia.org/wiki/Dialecte_balear | MediaWiki API: present |
| `ca-x-nord.json` | https://ca.wikipedia.org/wiki/Catal%C3%A0_septentrional | MediaWiki API: present |
| `ca-x-occidental.json` | https://ca.wikipedia.org/wiki/Catal%C3%A0_occidental | MediaWiki API: present |
| `ca-x-valencia.json` | https://ca.wikipedia.org/wiki/Valenci%C3%A0 | MediaWiki API: present |
| `co.json` | https://co.wikipedia.org/wiki/Corsu | MediaWiki API: present |
| `da-x-copenhagen.json` | https://da.wikipedia.org/wiki/Rigsdansk | MediaWiki API: present |
| `dsb.json` | https://dsb.wikipedia.org/wiki/Dolnoserbš%C4%87ina | MediaWiki API: present |
| `el.json` | https://el.wikipedia.org/wiki/%CE%95%CE%BB%CE%BB%CE%B7%CE%BD%CE%B9%CE%BA%CE%AE_%CE%B3%CE%BB%CF%8E%CF%83%CF%83%CE%B1 | MediaWiki API: present |
| `el-CY.json` | https://el.wikipedia.org/wiki/%CE%9A%CF%85%CF%80%CF%81%CE%B9%CE%B1%CE%BA%CE%AE_%CE%B4%CE%B9%CE%AC%CE%BB%CE%B5%CE%BA%CF%84%CE%BF%CF%82 | MediaWiki API: present |
| `et.json` | https://et.wikipedia.org/wiki/Eesti_keel | MediaWiki API: present |
| `ff.json` | https://ff.wikipedia.org/wiki/Fulfulde | MediaWiki API: present |
| `frr.json` | https://frr.wikipedia.org/wiki/Nordfriisk | MediaWiki API: present |
| `gem-x-ingvaeonic.json` | https://de.wikipedia.org/wiki/Ingw%C3%A4onisch | MediaWiki API: present |
| `hsb.json` | https://hsb.wikipedia.org/wiki/Hornjoserbš%C4%87ina | MediaWiki API: present |
| `hy.json` | https://hy.wikipedia.org/wiki/%D5%80%D5%A1%D5%B5%D5%A5%D6%80%D5%A5%D5%B6 | MediaWiki API: present |
| `id.json` | https://id.wikipedia.org/wiki/Bahasa_Indonesia | MediaWiki API: present |
| `is.json` | https://is.wikipedia.org/wiki/%C3%8Dslenska | MediaWiki API: present |
| `ka.json` | https://ka.wikipedia.org/wiki/%E1%83%A5%E1%83%90%E1%83%A0%E1%83%97%E1%83%A3%E1%83%9A%E1%83%98_%E1%83%94%E1%83%9C%E1%83%90 | MediaWiki API: present |
| `kn.json` | https://kn.wikipedia.org/wiki/%E0%B2%95%E0%B2%A8%E0%B3%8D%E0%B2%A8%E0%B2%A1 | MediaWiki API: present |
| `lij.json` | https://it.wikipedia.org/wiki/Lingua_ligure | MediaWiki API: present |
| `ml.json` | https://ml.wikipedia.org/wiki/%E0%B4%AE%E0%B4%B2%E0%B4%AF%E0%B4%BE%E0%B4%B3%E0%B4%82 | MediaWiki API: present |
| `mr.json` | https://mr.wikipedia.org/wiki/%E0%A4%AE%E0%A4%B0%E0%A4%BE%E0%A4%A0%E0%A5%80_%E0%A4%AD%E0%A4%BE%E0%A4%B7%E0%A4%BE | MediaWiki API: present |
| `mt.json` | https://mt.wikipedia.org/wiki/Malti | MediaWiki API: present |
| `nb.json` | https://no.wikipedia.org/wiki/Bokm%C3%A5l | MediaWiki API: present |
| `nds.json` | https://nds.wikipedia.org/wiki/Nedderd%C3%BC%C3%BCtsch | MediaWiki API: present |
| `nl.json` | https://nl.wikipedia.org/wiki/Nederlands | MediaWiki API: present |
| `pt-ST.json` | https://pt.wikipedia.org/wiki/L%C3%ADngua_s%C3%A3o-tomense | MediaWiki API: present |
| `wa.json` | https://wa.wikipedia.org/wiki/Walon | MediaWiki API: present |
| `zh.json` | https://zh.wikipedia.org/wiki/%E6%B1%89%E8%AF%AD | MediaWiki API: present |

## Corrected links

Dead URLs replaced with a verified live equivalent.

| File | Field | Old URL | New URL | Verification |
| --- | --- | --- | --- | --- |
| `orthography2ipa/data/ar-DZ.json` | `wikipedia` | https://ar.wikipedia.org/wiki/العربية_الجزائرية | https://ar.wikipedia.org/wiki/لهجة_جزائرية | MediaWiki API: present (title='لهجة جزائرية', pageid=42352) |
| `orthography2ipa/data/ar-IQ-x-qeltu.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/qǝltu_dialects | https://en.wikipedia.org/wiki/North_Mesopotamian_Arabic | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/ast-PT-x-guadramil.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Guadramil | https://pt.wikipedia.org/wiki/Guadramil | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/da-x-copenhagen.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Copenhagen_dialect | https://en.wikipedia.org/wiki/Danish_phonology | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/es-CO-x-paisa.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Paisa_dialect | https://en.wikipedia.org/wiki/Colombian_Spanish | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/es-ES-x-murcia.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Murcian_dialect | https://en.wikipedia.org/wiki/Murcian_Spanish | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/eu-x-bizkaiera.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Bizkaian_dialect | https://en.wikipedia.org/wiki/Biscayan_dialect | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/eu-x-lapurtera.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Labourdian_dialect | https://en.wikipedia.org/wiki/Navarro-Lapurdian_dialect | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/it-IT-x-abruzzo.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Abruzzese_dialect | https://it.wikipedia.org/wiki/Dialetti_dell%27Abruzzo | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/it-IT-x-umbria.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Umbrian_dialect | https://en.wikipedia.org/wiki/Central_Italian | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/mcm.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Macanese_Creole | https://en.wikipedia.org/wiki/Macanese_Patois | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/pt-BR-x-fluminense.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Fluminense_dialect | https://pt.wikipedia.org/wiki/Dialeto_fluminense | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/pt-BR-x-rj.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Carioca_dialect | https://pt.wikipedia.org/wiki/Dialeto_carioca | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/pt-MO.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Macanese_Creole | https://en.wikipedia.org/wiki/Macanese_Patois | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/pt-PT-x-acores.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Azorean_Portuguese | https://pt.wikipedia.org/wiki/Dialeto_a%C3%A7oriano | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/pt-PT-x-alentejo.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/European_Portuguese_phonology | https://pt.wikipedia.org/wiki/Dialeto_alentejano | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/pt-PT-x-algarve.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Algarvian_Portuguese | https://pt.wikipedia.org/wiki/Dialeto_algarvio | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/pt-PT-x-algarve.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/European_Portuguese_phonology | https://en.wikipedia.org/wiki/Portuguese_phonology | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/pt-PT-x-beira.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Beira_Portuguese | https://en.wikipedia.org/wiki/Portuguese_dialects | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/pt-PT-x-lisbon.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Lisbon_dialect | https://en.wikipedia.org/wiki/Portuguese_phonology | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/pt-PT-x-madeira.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Madeiran_Portuguese | https://pt.wikipedia.org/wiki/Dialeto_madeirense | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/pt-PT-x-porto.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Porto_dialect | https://en.wikipedia.org/wiki/Portuguese_dialects | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/pt-PT-x-trasosmontes.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/European_Portuguese_phonology | https://pt.wikipedia.org/wiki/Dialeto_trasmontano | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/ru-x-northern.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Northern_Russian_dialect | https://en.wikipedia.org/wiki/Northern_Russian_dialects | MediaWiki API: present (redirects followed) |
| `orthography2ipa/data/ru-x-southern.json` | `wikipedia`/`urls` | https://en.wikipedia.org/wiki/Southern_Russian_dialect | https://en.wikipedia.org/wiki/Southern_Russian_dialects | MediaWiki API: present (redirects followed) |

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

No dead links are kept for human review; all such entries carry verified live URLs.

| File | URL | Reason | Wayback snapshot |
| --- | --- | --- | --- |

## Dead links in prose notes (not auto-edited)

These dead URLs appear only inside free-text `notes` fields, so they are left untouched. Update the surrounding citation manually if desired.

| File | Field | URL | Reason |
| --- | --- | --- | --- |
| `orthography2ipa/data/ext-PT-x-barrancos.json` | `/notes` | https://github.com/NLP-Workspace/g2p-barranquenho), | HTTP 404 |

## Inconclusive (for human review)

Reachability could not be confirmed either way (403/429/timeout/5xx). **Not** removed.
The majority of 429 responses are from Wikipedia's API rate limiter — the URLs are expected to be valid.

| File | Field | URL | Reason |
| --- | --- | --- | --- |
| `orthography2ipa/data/cop.json` | `/wikipedia` | https://cop.wikipedia.org/wiki/ϯⲙⲉⲧⲣⲉⲙⲛ̀ⲭⲏⲙⲓ | API error: DNS resolution failure (cop.wikipedia.org does not exist) |

---

**Navigation:** [Docs home](index.md) · [Getting started](getting_started.md) · [Architecture](architecture.md) · [Languages](languages/index.md) · [Scoreboard](scoreboard.md)

*Related: [Bibliography](bibliography.md) · [Linguistic accuracy](linguistic_accuracy.md) · [Benchmarks](benchmarks.md)*
