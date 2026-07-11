# Glottolog hierarchy audit — orthography2ipa

Reference: **Glottolog** (clld/glottolog-cldf, `cldf/languages.csv` + `cldf/values.csv`
`classification` parameter). 27,177 languoids; full ancestor path per glottocode.

Glottolog is used as the reference for **genetic classification only**. o2i is deliberately
**finer** (dialects, historical stages, reconstructed proto-nodes) and **richer** (contact edges:
substrate / superstrate / adstrate, which Glottolog does not model at all). Nothing below argues
for deleting o2i's dialect granularity or contact edges. Glottolog is used to **catch errors** and
**fill gaps**, not to flatten.

**Scope split**

* **Phase 1 (shipped in this PR)** — metadata only: `glottolog_code`, `family`. Transcription-neutral
  by construction (see §5).
* **Phase 2 (this document)** — hierarchy discrepancies. **No `parent` was rewired in this PR.**
  Changing `parent` changes what a spec *inherits*, therefore changes transcription, therefore
  needs a scoreboard delta + linguistic justification. Deferred, coordinated with **#159**.

---

## 1. Critical: `glottolog_code` was populated with many WRONG codes

The single biggest finding. `glottolog_code` was never parsed by `json_loader.py`
(fixed separately in #269), so these values were **never validated by anything** and had
silently rotted. Two distinct failure classes:

### 1a. Stale codes — not present in current Glottolog at all (41)

`heja1235`, `tuni1238`, `yeme1256`, `goid1235`, `prot1503`, `sahi1246`, `chur1273`, `cope1239`,
`aust1239`, `hibe1234`, `gene1240`, `rive1239`, `cuba1234`, `mexi1236`, `etru1238`, `bizk1238`,
`lapu1237`, `nava1268`, `soul1252`, `barr1235`, `earl1234`, `fran1243`, `ingv1234`, `pger1234`,
`khoi1244`, `meit1245`, `flem1244`, `osca1244`, `olds1238`, `phoe1234`, `pied1238`, `minh1237`,
`munda1424`, `logu1243`, `semi1246`, `finl1244`, `tart1246`, `anda1275`, `aqui1235`, `lepo1237`,
`prot1522`.

### 1b. Valid-but-WRONG codes — resolve to a completely unrelated language

These are the dangerous ones: the code exists, so any naive validator passes, but it points at the
wrong language entirely.

| spec | was | resolved to (WRONG) | now |
|---|---|---|---|
| `es-CO` | `colo1256` | **Tsafiki** (Barbacoan, Ecuador) | `null` (Glottolog has no Colombian Spanish node) |
| `es-UY` | `urug1238` | **Uruguayan Sign Language** | `null` |
| `nn` | `norw1261` | **Norwegian Sign** (family) | `norw1262` (Norwegian Nynorsk) |
| `pt-PT-x-medieval` | `oldp1255` | **Old Persian** | `oldp1257` (Old Portuguese) |
| `fa` | `nucl1301` | **Turkish** | `west2369` (Western Farsi) |
| `ps` | `nort2684` | **Northern Khmer** | `nucl1276` (Nuclear Pashto) |
| `la-x-archaic` | `arch1244` | **Archi** (NE Caucasian) | `oldl1238` (Old Latin) |
| `es-ES-x-canarias` | `cana1268` | **Canadian English** | `cana1269` (Canary Islands Spanish) |
| `en-CA` | `cana1269` | **Canary Islands Spanish** | `cana1268` (Canadian English) |
| `en-ZA` | `sout3113` | **Central Delta Nile Arabic** | `sout3331` (Southern African English) |
| `es-CL` | `chil1276` | **Chilasi Kohistani** | `chil1286` (Chilean Spanish) |
| `ca-x-nord`, `ca-x-occidental` | `nort3175` | **North Sea Germanic** | `ross1234` / `cata1291` |
| `ca-x-balear` | `bale1254` | **Balesi** (Surmic, Sudan) | `bale1256` (Balear) |
| `an-x-occidental` | `west2615` | **Western Apache** | `west2340` (Western Aragonese) |
| `kmb` | `namb1293` | **Nambo** (Yam, PNG) | `kimb1241` (Kimbundu) |
| `aoa` | `ango1254` | **Angor** (Senagi, PNG) | `ango1258` (Angolar) |
| `unr` | `mund1330` | **Mundurukú** (Tupian) | `mund1320` (Mundari) |
| `xtg` | `tran1292` | **Transitional Bulgarian** | `tran1282` (Transalpine Gaulish) |
| `xga` | `gala1264` | **Galambu** (Chadic) | `gala1252` (Galatian) |
| `xbr` | `brit1243` | **British Creole** | `bryt1239` (Brythonic) |
| `fax` | `fala1244` | **Falahu** | `fala1241` (Fala) |
| `ar-NG` | `shua1254` | **Shua** (Khoe) | `chad1249` (Chadian Arabic) |
| `brx-x-proto-boro-garo` | `boro1282` | **Bororo** (Brazil) | `null` |
| `en-GB-x-scotland` | `scot1243` | **Scots** (a different *language*, not Scottish English) | `null` |
| `tr` | `turk1311` | *Turkic* (the family node, not the language) | `nucl1301` (Turkish) |
| `xce` | `celt1248` | *Celtic* (family node) | `celt1247` (Celtiberian) |
| `kn` | `kann1255` | Nuclear Kannaoid (subgroup, not the language) | `nucl1305` (Kannada) |
| `bho` | `bhoj1246` | Bhojpuric (subgroup) | `bhoj1244` (Bhojpuri) |
| `co` | `cors1242` | Corsic (subgroup) | `cors1241` (Corsican) |

Note the two **transposition bugs** (`en-CA` ↔ `es-ES-x-canarias`, and `oldp1255`/`oldp1257`) —
strong evidence these were assigned by fuzzy lookup without verification.

### Coverage

|  | before | after |
|---|---|---|
| specs with `glottolog_code` | 308 / 463 | **313 / 463** |
| of which **valid** in current Glottolog | 268 | **313 (100%)** |
| of which point at the **right** language | ~225 (est.) | **313 (100%)** |
| changed | — | **146** |

60+ codes were wrong and are now either corrected or set to `null` where **Glottolog genuinely has
no node** and o2i is finer. `null` is the honest value; a wrong code is worse than no code.

> **Review correction.** A first pass over-applied the "no Glottolog node for sub-national lects"
> rule and wrongly nulled ~19 codes that were valid *and* correct — most seriously `ro-RO`
> (`roma1327`, Romanian), plus the Arabic lects (`egyp1253`, `liby1240`, `suda1236`, `najd1235`,
> `gulf1241`, `nort3139`, `stan1323`, `dari1249`) and the German ones (`bava1246`, `alem1243`).
> All restored. Three unambiguous codes that the ISO index had missed were also added
> (`az`→`nort2697`, `bo`→`tibe1272` — the spec carries the legacy `tib` ISO code —
> and `el-CY`→`cypr1249`). `es-ES-x-andalusia-{e,w}` now share `anda1279`, the single Andalusian
> node Glottolog has (as `ar-AE/BH/KW/QA` share `gulf1241`).
>
> `de-CH` is deliberately left `null`: its old code `swis1247` is *Central Alemannic* (iso `gsw`,
> the Swiss German dialect), which is a different lect from the spec's "Swiss Standard German
> (Hochdeutsch)" — that is precisely the valid-but-wrong-language error class this audit exists to
> remove, and Glottolog has no node for the standard variety.
> `ar-NG` keeps the corrected `chad1249` (Chadian Arabic, iso `shu` = Shuwa): its old `shua1254`
> is *Shua*, a **Khoe** language of Botswana (iso `shg`).

**Deliberate `null`s** (o2i finer than Glottolog): reconstructed proto-nodes (`cel`, `gem`, `sem`,
`xpa`, `xaq`, `sat-x-proto-munda`, `kha-x-proto-mon-khmer`, `brx-x-proto-boro-garo`,
`cel-x-goidelic`, `gem-x-ingvaeonic`); Vulgar-Latin regional stages (`la-x-hispania`, `la-x-gallia`,
`la-x-italia`, `la-x-galloitalic`, `la-x-balkans` — Glottolog has only one `vulg1234`);
dialects Glottolog does not enumerate (`es-CO`, `es-UY`, `da-x-copenhagen`, `nl-BE`, `sv-FI`,
`de-CH`, `en-US`, `en-GB-x-scotland`, `pt-PT-x-minho`, `ext-PT-x-barrancos`, `eu-x-lapurtera`,
`eu-x-nafarra-garaia`, `eu-x-nafarra-beherea`, `roa-x-galaicopt`, `khi`).

5 glottocodes are legitimately shared by two specs each (o2i has both a generic and a specific
spec for the same Glottolog node): `ar`/`arb`, `gl`/`gl-ES`, `nl`/`nl-NL`, `dra`/`ta-x-proto-dravidian`,
`ar-JO`/`ar-PS`.

---

## 2. `family` normalization — convention adopted

**Before:** inconsistent and mutually incompatible. Iberian Romance varieties were variously
`Romance`, `Asturleonese`, `Indo-European > Romance > Ibero-Romance`. 58 distinct tokens across
mixed depths; `Portuguese Creole`, `Tibeto-Burman`, `Niger-Congo`, `Afroasiatic` vs `Afro-Asiatic`.

**Convention adopted — up to three levels:**

```
family = "<top-level family> > <branch> > <sub-branch>"    # levels dropped when not applicable
```

| | |
|---|---|
| `pt-PT` | `Indo-European > Romance > Ibero-Romance` |
| `fr-FR` | `Indo-European > Romance > Gallo-Romance` |
| `de-DE` | `Indo-European > Germanic > West Germanic` |
| `ru` | `Indo-European > Slavic > East Slavic` |
| `arb` | `Afro-Asiatic > Semitic > Central Semitic` |
| `tr` | `Turkic` |

**This is a curated mapping ONTO Glottolog's classification path, not a verbatim slice of it.**
Glottolog has no `Romance` node reachable by a simple depth cut — Portuguese sits under
`Italic > Latino-Faliscan > Latinic > Imperial Latin > Romance > Italo-Western Romance >
Western Romance > Shifted Western Romance > Southwestern Shifted Romance > West Ibero-Romance >
Galician Romance > Macro-Portuguese`, whose intermediate names are unusable as labels. So the
generator walks each spec's real Glottolog path and picks the deepest node belonging to a
controlled vocabulary of traditional **branch** names (Romance, Germanic, Slavic, Semitic, …) and
**sub-branch** names (`West Ibero-Romance`/`Castilic`/`Galician Romance` → *Ibero-Romance*;
`Gallo-Rhaetian`/`Oil` → *Gallo-Romance*; `Italo-Dalmatian` → *Italo-Romance*; …).

The mapping is **executable and committed** as `scripts/gen_family.py` (`--check` fails if any
spec's `family` is stale), so it is auditable and reproducible rather than hand-asserted.

The branch must be picked from the path **plus the node's own name** — otherwise a spec whose
glottocode *is* the branch node gets the branch above it (`sla`/`slav1255` came out as
`Balto-Slavic` while its 28 descendants were `Slavic`; likewise `ira` → `Indo-Iranian`, and `sq`
fell back to a bare `Indo-European`).

**Depth-3 matters:** a flat depth-2 scheme would have put **167 of 463 specs** in a single
`Indo-European > Romance` bucket and destroyed the `Ibero-Romance` / `Gallo-Romance` /
`West Germanic` / `West Slavic` distinctions that already existed on `dev`. Iberian granularity is
the point of this project. The largest bucket is now `Indo-European > Romance > Ibero-Romance`
(122). **66 distinct families**, all 463 specs populated. The CLI's `--family` filter matches *any*
step of the path, so both `--family Romance` and `--family Ibero-Romance` work.

**Non-Glottolog-derivable values** (documented exception list in `MANUAL`): `Basque` (the Vasconic
set, incl. `xaq`), `Constructed` (`eo`), and the reconstructed proto-nodes with no Glottolog node
of their own (`brx-x-proto-boro-garo`, `kha-x-proto-mon-khmer`, `sat-x-proto-munda`, `xpa`).
`Isolate` (`etr`, `xib`) and `Unclassifiable` (`txr`, `xlg`) *are* Glottolog-derived — Glottolog
genuinely files Tartessian and Ancient Ligurian as unclassifiable. Romance varieties whose o2i
parent is a Vulgar Latin stage (`roa-x-galaicopt`, `it-IT-x-{abruzzo,calabria,puglia}`,
`pt-PT-x-lisbon`) are pinned, since inheriting the Latin node's `Italic` branch would mislabel them.

Normalizing `family` is also what **exposed** the wrong glottocodes in §1b: `nn` deriving
`Sign Language` and `es-CO` deriving `Barbacoan` is how they surfaced.

### 2b. Proto/grouping nodes and bogus ISO codes (review follow-up)

Grouping specs were being filled inconsistently — `sla`, `ira`, `iir`, `ber`, `xbr` got their
Glottolog family node while `cel`, `gem`, `sem`, `khi` were left null even though the nodes exist.
Filled, same convention: `cel`→`celt1248`, `gem`→`germ1287`, `sem`→`semi1276`, `khi`→`khoe1240`,
`cel-x-goidelic`→`goid1240`, `gem-x-ingvaeonic`→`nort3175`, `sem-x-west`→`west2786`,
`sem-x-central`→`cent2236`, and `roa-x-galaicopt`→**`gali1263` "Galician Romance"** (a near-exact
match for Galaico-Portuguese).

Two `iso639_3` values pointed at unrelated languages and are corrected: `etr` carried `"etr"` =
**Edolo** (a Papuan language) — Etruscan is **`ett`**; `xbr` carried `"xbr"` = **Kambera** —
Common Brythonic has no ISO 639-3 code, so it is now `null`.

## 3. Hierarchy discrepancies (Phase 2 — feeds #159, NOT fixed here)

Cycle check on the ancestry graph: **clean, no cycles** (before and after).

### 3a. `pt-PT-x-lisbon` has `parent: null` — ORPHAN BUG (highest priority)

`pt-PT-x-lisbon` is a **scored benchmark row** and it has **no parent at all**. It therefore
inherits nothing. Every other `pt-PT-x-*` dialect descends from `pt-PT`.

* o2i: `parent = null`
* Glottolog: Lisbon is not a node, but the variety is unambiguously European Portuguese.
* **Fix:** `parent = "pt-PT"`. **Inheritance-affecting → needs scoreboard proof.**

### 3b. Colonial mis-parenting — Lusophone (confirmed, #159)

All African/Asian Portuguese varieties are parented to **modern** `pt-PT`:

| spec | o2i parent | Glottolog says | recommended |
|---|---|---|---|
| `pt-AO`, `pt-MZ`, `pt-GW`, `pt-CV`, `pt-ST`, `pt-TL`, `pt-MO` | `pt-PT` | siblings of EP under `port1283`/Macro-Portuguese, not descendants of the modern Lisbon standard | a shared colonial-era EP node (e.g. `pt-PT-x-classical`, 16th–19th c.) |

The **creoles** are worse — they are parented to `pt-PT` as if they were dialects of modern EP:

| spec | o2i parent | Glottolog |
|---|---|---|
| `aoa` (Angolar), `kea` (Kabuverdianu), `pov` (Upper Guinea Crioulo), `pre` (Principense), `mzs` (Macanese), `pap` (Papiamento) | `pt-PT` | all under **Macro-Portuguese**, a *sister* branch to Portuguese proper — creoles are not descendants of the modern lexifier |

Recommended: parent creoles to the colonial-era node, and keep the modern lexifier as a
**superstrate contact edge** (which is exactly what o2i's contact-edge machinery is for, and what
Glottolog cannot express). Inheritance-affecting.

### 3c. Colonial mis-parenting — Latin American Spanish (confirmed, #159)

**`es-419` exists and has ZERO children.** All 20 LatAm national varieties parent directly to
`es-ES` (Castilian):

`es-AR`, `es-BO`, `es-CL`, `es-CO`, `es-CR`, `es-CU`, `es-DO`, `es-EC`, `es-GT`, `es-HN`, `es-MX`,
`es-NI`, `es-PA`, `es-PE`, `es-PR`, `es-PY`, `es-SV`, `es-UY`, `es-VE` (+ `es-GQ`).

Glottolog is unambiguous here: `cast1244` (Castilian) and `amer1254` (Latin American Spanish) are
**sibling dialects** under `stan1288` (Spanish). Parenting American Spanish to Castilian asserts
that e.g. Mexican Spanish descends from a *seseo*-less, `/θ/`-distinguishing variety — which is
precisely backwards, and it is the reason Andalusian/Canarian features have to be re-added by hand
downstream.

* **Fix:** point the LatAm nationals at `es-419`, and give `es-419` a parent that is *not* modern
  Castilian (Andalusian-Canarian-influenced colonial Spanish). Inheritance-affecting; this is the
  big one for #159.
* `es-419` itself currently has `parent = es-ES` — same problem, one level up.

### 3d. Sub-dialects skipping their national parent (inheritance-affecting)

| spec | o2i parent | should be |
|---|---|---|
| `es-CO-x-costa` | `es-ES` | `es-CO` |
| `es-CO-x-paisa` | `es-ES` | `es-CO` |
| `es-MX-x-costa` | `es-ES` | `es-MX` |
| `es-PE-x-lima` | `es-ES` | `es-PE` |

(The remaining `es-CO-x-*` / `es-VE-x-*` / `es-AR-x-*` specs *do* correctly parent to their national
node — so these four are inconsistencies within o2i itself, not a systematic choice.)

**Explicitly NOT bugs** (my first pass flagged them; they are correct):
`es-ES-x-medieval → la-x-hispania`, `pt-PT-x-medieval → roa-x-galaicopt`, `pt-BR → pt-PT-x-medieval`
(historical stages must descend from the historical ancestor, not the modern sibling), and
`it-IT-x-{abruzzo,calabria,puglia} → la-x-italia` (the southern *dialetti* are sister Italo-Romance
varieties, **not** descendants of Standard Italian — parenting them to Vulgar Latin is *more*
correct than parenting them to `it-IT`).

### 3e. Parent asserts descent where Glottolog has siblinghood

o2i models **diachronic descent**; Glottolog models **cladistic siblinghood** and has no time axis.
So `enm → ang`, `da/fo/is → non`, `el → grc`, `zh → ltc → och`, `ca/sc/mxi → la-x-late`,
`fy/frr/stq → ofs`, `nds → osx`, `cop → egy`, `pal → peo` all "contradict" Glottolog but are
**correct and should be kept**. Listed here only so they are not mistaken for bugs later.

The following, however, are **genuine siblinghood-as-descent errors** worth revisiting:

| spec | o2i parent | Glottolog | note |
|---|---|---|---|
| `ml` | `ta` | sisters under *Tamil-Malayalam* | Malayalam does **not** descend from Tamil |
| `bho` | `hi` | common anc. *Shaurasenic* | Bhojpuri is Magadhan, not a Hindi dialect |
| `ur` | `hi` | sisters under *Hindustani* | both should hang off a Hindustani node |
| `pa-PK` | `pa` | sisters under *Greater Panjabic* | W. vs E. Punjabi are sisters |
| `fa-AF` (Dari), `tg` (Tajik) | `fa` | sisters under *Farsic* | not descendants of Western Farsi |
| `fa-x-hazaragi` | `fa-AF` | sister of Dari | |
| `mt` | `ar` | common anc. *Arabic* | Maltese descends from **Siculo-Arabic**, not MSA |
| `acy` (Cypriot Ar.), `xaa` (Andalusi Ar.) | `arb` | sisters under *Arabic* | MSA is a sibling, not an ancestor |
| `ar-IQ-x-qeltu` | `ar-IQ` | *qeltu* and *gilit* are the two co-ordinate Mesopotamian branches | not parent/child |
| `pnt` (Pontic) | `el` | sister of Modern Greek | |
| `ext` (Extremaduran) | `es-ES` | Glottolog puts it under *Castilic*; traditional scholarship calls it Asturleonese | contested — worth a decision |
| `xlg` (Ancient Ligurian) | `ine` | Glottolog gives it **no IE ancestry at all** | contested |
| the 13 modern Indo-Aryan specs (`hi`,`bn`,`gu`,`mr`,`ne`,`or`,`pa`,`sd`,`si`,`as`,`mai`,`kok`,`ks`) | `sa` | common anc. *Indo-Aryan* | descent from Sanskrit *proper* (rather than MIA/Prakrit) is a known simplification — flag, low priority |

### 3f. Missing intermediate nodes

Glottolog has these grouping nodes; o2i has no corresponding spec, which is *why* several of the
§3e errors were forced (with no Hindustani node, Urdu had nowhere to go but Hindi):

**High value** (would directly fix a §3e error): *Spanish* (neutral, above Castilian ⇄ LatAm) —
already half-present as `es-419`; *Hindustani* (`hind1270`); *Farsic* (`fars1253`);
*Tamil-Malayalam* (`tami1294`); *Arabic* (neutral, above MSA/dialects); *Macro-Portuguese*
(above Portuguese + creoles).

**Lower value / o2i may deliberately stay coarser**: *Anglic*, *North Germanic*, *Frisian*,
*Sorbian*, *Lechitic*, *Eastern Baltic*, *Greater Panjabic*, *Shaurasenic*.
Flagged, not forced.

### 3g. Orphans (`parent: null`) — 69 total

Most are **legitimate roots**: proto/family nodes (`ine`, `sem`, `dra`, `urj`, `trk`, `jpx`, `pko`,
`nic`, `sit`, `tai`, `ccs`, `afa`, `xgn`, `poz`).

Genuine orphans that Glottolog *does* place under a family, and which have a plausible o2i parent
already in the tree:

`pt-PT-x-lisbon` (→ `pt-PT`, see §3a — **the urgent one**), `lt`/`lv` (→ Balto-Slavic),
`csb`/`dsb`/`hsb`/`szl` (→ Slavic), `sq`, `hy` (→ `ine`), `nrf`/`pcd`/`wa` (→ Gallo-Romance/`fr`),
`rup` (→ Eastern Romance), `rue` (→ `uk`), `yi` (→ Germanic/`de`), `nah`, `qu`, `so`, `xh`, `rw`,
`su`, `ny`, `ts`, `kmb`, `ff`.
All inheritance-affecting.

---

## 4. Notable missing languages (short, prioritized — NOT added here)

Well-attested in Glottolog, plausible for the project, absent from o2i:

1. **Cantonese** (`yue`, `cant1236`) — ~85M; the largest gap in the roster.
2. **Uyghur** (`ug`, `uigh1240`) — Turkic, Arabic script; o2i has 10 Turkic specs but not this one.
3. **Kurdish** (`ku` / `ckb`, `nort2641` / `cent1972`) — Iranian; o2i has 15 Iranian specs.
4. **Malagasy** (`mg`, `plat1254`) — Austronesian, Latin script, well documented.
5. **Shona** (`sn`), **Sotho–Tswana** (`st`/`tn`/`nso`), **Lingala** (`ln`), **Wolof** (`wo`) — o2i's
   Atlantic-Congo coverage (12) is thin relative to its Romance coverage (161).
6. **Cebuano** (`ceb`), **Malay/Indonesian** — large Austronesian gaps.
7. **Bosnian** (`bs`) — trivially, given `hr`/`sr` are present.
8. **Hokkien** (`nan`), **Hakka** (`hak`), **Wu** (`wuu`) — Sinitic beyond Mandarin.
9. **Yakut** (`sah`), **Navajo** (`nv`), **Maori** (`mi`), **Hawaiian** (`haw`) — good phonological
   documentation, useful typological spread.

(Romanian is **not** missing — it is present as `ro-RO`.)

---

## 5. Transcription-neutrality (Phase 1)

Both changed fields are `OWN_ONLY` in `FIELD_INHERITANCE` (`orthography2ipa/types.py`) and neither
reaches the G2P engine: `family` is read only by `registry.available_families()` and the CLI, and
`glottolog_code` is a pure catalog cross-reference. **No `parent` is rewired**, so no spec's
inheritance changes. Transcription therefore cannot move *by construction* — no scoreboard run is
required, and `benchmarks/results.json` / `docs/scoreboard.md` are left untouched (confirmed absent
from the PR's file list).

Mechanically verified against `origin/dev`, for all 424 changed spec JSONs:

* the set of differing keys is exactly `{glottolog_code, family}` — nothing else was touched, and
  no file was reflowed or reindented;
* `parent` is unchanged in every single spec;
* every non-null `glottolog_code` (313) resolves in Glottolog;
* the ancestry graph is cycle-free.

Tests: **20847 passed, 5 skipped** (on `dev` with #269 merged, i.e. with `glottolog_code` now
actually parsed by the loader). Engine untouched — data, tests and docs only.
