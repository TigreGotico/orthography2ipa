# Language Registry

The registry (`registry.py`) turns a language code into a registered spec code, and it loads the `LanguageSpec` for that code from `orthography2ipa/data/` on demand. Import of the package indexes the file names in that directory and parses no JSON. `get()` parses the file of a spec the first time a caller asks for it, and the registry caches the spec from then on. The registry also finds the plugins that installed packages register. [getting_started.md](../guide/getting_started.md#finding-a-language-code) shows the tasks that use it: look up a language, and install or write a plugin.

## API

The top level of `orthography2ipa` exports each of these functions.

| Function | Returns |
| :--- | :--- |
| `get(code, strict=False)` | The `LanguageSpec` for the resolved code. It raises `KeyError` when no spec matches, and under `strict` when only the nearest-language step finds one. |
| `resolve(code)` | The registered code that `get()` would load, as a string. A code with no usable match comes back in its standardised spelling, such as `qqq-ZZ` for `qqq-zz`. |
| `resolves_exactly(code)` | `True` when the code names a spec without the nearest-language guess, and `False` otherwise. |
| `available_codes(include_clades=False)` | A sorted list of the registered language codes. The clade nodes are in it only with `include_clades=True`. |
| `available_families()` | A dict from each family path to the list of its language codes. |
| `ancestry_chain(code)` | The list of `parent` codes above the spec, nearest first, with the clade nodes that the chain passes through. |
| `get_syllabifier(code)` | Deprecated. `None` for every code, because discovery finds no syllabifier. A caller passes one in `Pipeline(syllabifier=...)`. |
| `get_rescorers(code)` | Deprecated. The list of `LatticeRescorer` objects that the installed rescorer plugins contribute for the code. `G2P` does not run them. A caller passes rescorers in `Pipeline(rescore=...)`. |
| `get_stress_plugin(code)` | Deprecated. The `StressPlugin` registered for the code, or `None`. |
| `who_answers(code)` | Deprecated. A dict with the resolved `code`, `syllabify` (always `built-in`) and the `rescore` list of the installed plugins. `G2P.pipeline` holds the steps of one engine. |

```python
import orthography2ipa
spec = orthography2ipa.get("pt-BR")                          # fetch a spec by code
codes = orthography2ipa.available_codes()                    # every registered language code
all_codes = orthography2ipa.available_codes(include_clades=True)   # adds the clade nodes
families = orthography2ipa.available_families()              # codes grouped by derived family path
families["Indo-European > Italic > Romance > Ibero-Romance"][:4]
# ['an', 'an-x-ansotano', 'an-x-belsetan', 'an-x-benasque']
orthography2ipa.ancestry_chain("pt-BR")[:5]                  # the parent chain, nearest first
# ['pt-PT-x-medieval', 'roa-x-galaico-pt', 'x-clade-iberrom', 'la-x-hispania', 'x-clade-roma1334']
orthography2ipa.resolve("en-NZ")                             # the code get() would load
# 'en-GB'
```

A clade node is for classification only. It carries no phoneme data, no spec inherits data from it, and `available_codes()` leaves it out by default. The loader derives `family` from the clade nodes ([ancestry.md](../specs/ancestry.md#clade-nodes-and-the-derived-family)). `available_families()` keys each language by that full path, and `orthography2ipa list --family Romance` matches any single step of it.

## Code resolution

`get()` and `resolve()` normalise a code through these steps, in order. The first step that names a registered spec wins. The steps use [`langcodes`](https://github.com/rspeer/langcodes) for [BCP 47](https://www.rfc-editor.org/rfc/rfc5646) parsing and [`linguatag`](https://github.com/TigreGotico/linguatag) for the default regions and the language distance.

1. The alias table `_ALIASES`, which holds ISO 639-3 codes and private-use tags that `langcodes` does not round-trip.
2. An exact match against the alias keys and the registered spec codes, without regard to case, because BCP 47 tags are case-insensitive ([RFC 5646, section 2.1.1](https://www.rfc-editor.org/rfc/rfc5646#section-2.1.1)). So `MNK` finds `mnk`, and `ars-sa-x-qassim` finds `ars-SA-x-qassim`. Then `langcodes.standardize_tag(code, macro=True)`, for a code with no private-use subtag. The result goes through the alias table again.
3. An exact match against the registered spec codes. A private-use tag also matches with a script subtag dropped when that script is the language's Suppress-Script in the [IANA Language Subtag Registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry), so `pt-Latn-BR-x-sp` finds `pt-BR-x-sp`. The Suppress-Script "adds no distinguishing information to a language tag" ([RFC 5646, section 3.1.9](https://www.rfc-editor.org/rfc/rfc5646#section-3.1.9)). Only the part before `-x-` goes to `langcodes`, because `langcodes` rejects a private-use subtag longer than 8 characters, such as the alias `ar-x-levantine`.
4. For a bare language tag, the spec of its default region (`linguatag.with_default_region`), when that spec is registered. For a region that has only sub-regional specs, a curated default variant.
5. The nearest registered code by language distance (`linguatag.closest_lang`), so `en-NZ` gives `en-GB`. A private-use subtag counts for nothing in the distance, so an unknown variant ties with the sibling lects of its language. The call passes `lects="standard"`, which breaks the tie toward the standard variety: `ar-x-zzz` gives `ar`, not one of the regional Arabic lects such as `ar-x-mashriqi`. With no usable match, the code stays as it is, and `get()` raises `KeyError`.

   The search looks first among the codes of the tag's own language, because the primary language subtag names the language. So `sr-Latn-RS` gives `sr`, although `langcodes` expands `cnr` to `sr-Latn-ME`, which is nearer. The own language is the primary subtag of the tag as given. When that language has no spec, it is the language of the standardized tag, so `sh` (standardized to `sr-Latn`) gives `sr`. Arabic is the likely script of Algerian Saharan Arabic, so `aao-Arab` gives `aao`. When no own-language spec is near enough, the search takes every registered code, so `hr-Cyrl` gives `sr`, because the Croatian spec reads Latin script.

The default region of a bare tag is its motherland, the region where the language first appeared and is still spoken. `linguatag` takes it from the [CLDR likely subtags](https://github.com/unicode-org/cldr/blob/main/common/supplemental/likelySubtags.xml) and overrides CLDR where the most-populous region differs, so `pt` goes to `pt-PT` and not to `pt-BR`.

| Code | Resolves to |
| :--- | :--- |
| `de` | `de-DE` |
| `en` | `en-GB` |
| `es` | `es-ES` |
| `fr` | `fr-FR` |
| `gl` | `gl-ES` |
| `it` | `it-IT` |
| `pt` | `pt-PT` |
| `ro` | `ro-RO` |
| `ar-SA` | `ars-SA` (curated) |

The `ar-SA` default is an editorial choice, not a claim in the spec data. Saudi Arabia has several documented varieties, Najdi and Hejazi among them, and no single standard spoken form. `ar-SA` goes to Najdi, the variety of the capital region and the most widely spoken (Ingham, *Najdi Arabic: Central Arabian*, 1994, [doi:10.1075/loall.1](https://doi.org/10.1075/loall.1)).

### Unknown variants and strict lookup

A private-use tag that names no spec, such as `pt-x-typo`, still resolves to the nearest registered spec. `resolve()` and `get()` then emit `UnknownVariantWarning`, which names the discarded subtag and the spec chosen:

```python
import warnings, orthography2ipa
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    orthography2ipa.resolve("pt-x-typo")    # 'pt-PT'
    str(w[0].message)  # "unknown variant subtag 'typo' in 'pt-x-typo'; using 'pt-PT' instead"
```

To get the behaviour of the base language without the warning, ask for the base tag. `get(code, strict=True)` refuses the nearest-language guess and raises `KeyError` instead. The alias table, case folding, BCP-47 standardisation and the curated defaults still apply under `strict`, because each of them names a spec on purpose.

`resolves_exactly(code)` tells the two cases apart. It returns `True` when the code names a spec without a guess, and `False` when only the nearest-language step finds one:

```python
orthography2ipa.resolves_exactly("en")      # True: a curated default
orthography2ipa.resolves_exactly("en-NZ")   # False: only the nearest-language guess finds en-GB
```

## Code aliases

The alias table maps these ISO 639-3 codes of major languages to a spec:

| ISO 639-3 | Spec | ISO 639-3 | Spec | ISO 639-3 | Spec |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `por` | `pt-PT` | `eng` | `en-GB` | `spa` | `es-ES` |
| `fra` | `fr-FR` | `deu` | `de-DE` | `ita` | `it-IT` |
| `nld` | `nl-NL` | `swe` | `sv` | `dan` | `da` |
| `nor` | `no` | `rus` | `ru` | `ukr` | `uk` |
| `ara` | `ar` | `fas` | `fa` | `hin` | `hi` |
| `zho` | `zh` | `jpn` | `ja` | `kor` | `ko` |
| `eus` | `eu` | `cat` | `ca` | `glg` | `gl-ES` |
| `oci` | `oc` | `tur` | `tr` | `fin` | `fi` |
| `ell` | `el` | `pol` | `pl` | `ces` | `cs` |
| `ron` | `ro-RO` | `mwl` | `mwl` | `arg` | `an` |
| `lat` | `la` | `tgk` | `tg` | `prs` | `fa-AF` |

The table holds five other kinds of entry:

| Kind | Examples |
| :--- | :--- |
| The bare ISO 639-3 code of a variety, mapped to the spec keyed by that code | `arz` to `arz-EG`, `bar` to `bar-AT`, `pnb` to `pnb-PK`, and `ajp`, which SIL retired into `apc`, to `apc-JO` |
| A key that a spec had before it took its canonical key, mapped to that spec | `ar-EG` to `arz-EG`, `ar-SA-x-najd` to `ars-SA`, `de-x-bavarian` to `bar-AT`, `cbk-x-ternate` to `cbk-PH-x-ternate` |
| An individual-language code that `macro=True` standardisation would collapse into its macrolanguage, mapped to itself | `quz`, which would otherwise become `qu`, and `diq`, which would become `zza` |
| An ISO 639-3 code whose variety has its spec under another key | `twi` to `tw` |
| A private-use tag, mapped to the spec that holds the variety | `pt-PT-x-barrancos` to `ext-PT-x-barranco`, `pt-BR-x-sao-paulo` to `pt-BR-x-sp`, `ar-x-hijazi` to `acw-SA` |

Galician has one standard spec, `gl-ES`, and the bare tag `gl` resolves to it. The variety codes `gl-x-central`, `gl-x-occidental`, `gl-x-oriental`, `gl-x-eonavia` and `gl-x-reintegrado` resolve to the `gl-ES-x-*` spec of the same variety. `_ALIASES` in `registry.py` holds the full table.

Dutch has one Netherlands standard spec, `nl-NL`. The bare tag `nl`, the ISO 639-3 code `nld` and the ISO 639-2/B code `dut` resolve to it exactly. `nl-BE`, `af` and `vls` take `nl-NL` as their parent.

An old key that is the ISO 639-3 code of another language is not kept as an alias. `aja` was the key of Aja (Benin), now `ajg-BJ`, and it is the code of Aja (South Sudan), so `aja` names no spec. In the same way, `tmg` is the code of Ternateño, the extinct creole of the Moluccas, and does not name `cbk-PH-x-ternate`, the spec of Ternate Chabacano of Cavite.

## Plugin discovery

Plugin discovery is deprecated. It goes in the next major release, together with the deprecated `G2P(plugins=...)`. A caller passes each step to one engine in a `Pipeline`, and no step needs an entry point. `get_rescorers`, `get_stress_plugin`, `who_answers`, `get_declared_plugins`, the base classes `NormalizePlugin`, `RescorerPlugin` and `StressPlugin`, and the constants `STAGES`, `OUTPUT_CHANGING_STAGES` and `ENTRY_POINT_GROUPS` raise a `DeprecationWarning` that names the release that removes them.

The registry finds plugins through `importlib.metadata` entry points, with one group for each pluggable stage except `syllabify`. Discovery runs once per stage, on the first call that needs it, and the result stays cached at module scope. A plugin that fails to load logs a `WARNING` and is skipped.

| Group | Lookup | When several plugins claim one code |
| :--- | :--- | :--- |
| `orthography2ipa.rescore` | `get_rescorers(code)` | All of them run, lowest `priority` first, so the highest has the last word |
| `orthography2ipa.stress` | `get_stress_plugin(code)` | The highest `priority` wins |
| `orthography2ipa.normalize`, `orthography2ipa.sandhi` | by entry-point name | The spec or the caller names one, so no contest arises |

`RescorerPlugin`, `StressPlugin` and `SyllabifierPlugin` each have a `priority` property that defaults to `50`. `NormalizePlugin` and `SandhiPlugin` have none, because a caller names them. Nothing reads the priority of a syllabifier, for the same reason. `SyllabifierPlugin` and `SandhiPlugin` have a `language_codes` property that defaults to an empty list, and the engine does not read it.

Discovery alone selects nothing. A caller passes a syllabifier in `Pipeline(syllabifier=...)`. The engine runs a normalize, stress, rescore or sandhi plugin only when the spec or the caller names it by entry-point name ([architecture.md](../engine/architecture.md#pluggable-steps)). `get_rescorers(code)` lists what the installed rescorer plugins contribute, but `G2P` runs only the declared ones. A stress plugin runs only when the spec sets `stress.source` to `"plugin"`. If none is installed, the engine raises `MissingStressPlugin`, which `orthography2ipa.registry` defines. A named plugin that is not installed raises `MissingPlugin`.

`who_answers(code)` reports which installed rescorer plugins claim a code:

```python
orthography2ipa.who_answers("pt-PT")
# DeprecationWarning: who_answers is deprecated ...
# {'code': 'pt-PT',
#  'syllabify': 'built-in',
#  'rescore': ['built-in (spec allophone_rules only)']}
```

### The bundled syllabifier plugin

`orthography2ipa.syllabifiers.SilabificadorSyllabifier` wraps the [`silabificador`](https://github.com/TigreGotico/silabificador) package, which the `portuguese` extra installs. A caller builds it and passes it to one engine:

```python
from orthography2ipa import G2P, Pipeline
from orthography2ipa.syllabifiers import SilabificadorSyllabifier

engine = G2P("pt-PT", pipeline=Pipeline(syllabifier=SilabificadorSyllabifier()))
```

It claims the Portuguese codes: `pt`, `pt-PT`, `pt-BR`, `pt-AO` and the other national varieties, and the regional `pt-BR-x-*` specs, which read the `pt-BR` grapheme table. `language_codes` on an instance lists them. An engine that gets no syllabifier uses the bundled vowel-group splitter, whether or not the package is installed.

---
[← Command line](cli.md) · [Home](../index.md) · [Public API stability →](api_stability.md)
