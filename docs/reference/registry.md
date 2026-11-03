# Language Registry

The registry (`registry.py`) turns a language code into a registered spec code, and it loads the `LanguageSpec` for that code from `orthography2ipa/data/` on demand. Import of the package indexes the file names in that directory and parses no JSON. `get()` parses the file of a spec the first time a caller asks for it, and the registry caches the spec from then on. The registry also finds the plugins that installed packages register. [getting_started.md](../guide/getting_started.md#finding-a-language-code) shows the tasks that use it: look up a language, and install or write a plugin.

## API

The top level of `orthography2ipa` exports each of these functions.

| Function | Returns |
| :--- | :--- |
| `get(code, strict=False)` | The `LanguageSpec` for the resolved code. It raises `KeyError` when no spec matches, and under `strict` when only the nearest-language step finds one. |
| `resolve(code)` | The registered code that `get()` would load, as a string. A code with no usable match comes back unchanged. |
| `resolves_exactly(code)` | `True` when the code names a spec without the nearest-language guess, and `False` otherwise. |
| `available_codes(include_clades=False)` | A sorted list of the registered language codes. The clade nodes are in it only with `include_clades=True`. |
| `available_families()` | A dict from each family path to the list of its language codes. |
| `ancestry_chain(code)` | The list of `parent` codes above the spec, nearest first, with the clade nodes that the chain passes through. |
| `get_syllabifier(code)` | The `SyllabifierPlugin` that answers for the code, or `None`. |
| `get_rescorers(code)` | The list of `LatticeRescorer` objects that the installed rescorer plugins contribute for the code. |
| `get_stress_plugin(code)` | The `StressPlugin` registered for the code, or `None`. |
| `who_answers(code)` | A dict with the resolved `code`, the `syllabify` class name and the `rescore` list. |

```python
import orthography2ipa
spec = orthography2ipa.get("pt-BR")                          # fetch a spec by code
codes = orthography2ipa.available_codes()                    # every registered language code
all_codes = orthography2ipa.available_codes(include_clades=True)   # adds the clade nodes
families = orthography2ipa.available_families()              # codes grouped by derived family path
families["Indo-European > Italic > Romance > Ibero-Romance"][:4]
# ['an', 'an-x-ansotano', 'an-x-belsetan', 'an-x-benasques']
orthography2ipa.ancestry_chain("pt-BR")[:5]                  # the parent chain, nearest first
# ['pt-PT-x-medieval', 'roa-x-galaicopt', 'x-clade-iberrom', 'la-x-hispania', 'x-clade-roma1334']
orthography2ipa.resolve("en-NZ")                             # the code get() would load
# 'en-GB'
```

A clade node is for classification only. It carries no phoneme data, no spec inherits data from it, and `available_codes()` leaves it out by default. The loader derives `family` from the clade nodes ([ancestry.md](../specs/ancestry.md#clade-nodes-and-the-derived-family)). `available_families()` keys each language by that full path, and `orthography2ipa list --family Romance` matches any single step of it.

## Code resolution

`get()` and `resolve()` normalise a code through these steps, in order. The first step that names a registered spec wins.

1. The alias table `_ALIASES`, which holds ISO 639-3 codes and private-use tags that `langcodes` does not round-trip.
2. `langcodes.standardize_tag(code, macro=True)`, for a code with no private-use subtag. The result goes through the alias table again.
3. An exact match against the registered spec codes. A private-use tag also matches without regard to case, so `ars-sa-x-qassim` finds `ars-SA-x-qassim`.
4. A curated default variant for a bare language tag or for a region that has only sub-regional specs.
5. The nearest registered code by language distance (`ovos_spec_tools.language.closest_lang`), so `en-NZ` gives `en-GB`. With no usable match, the code stays as it is, and `get()` raises `KeyError`.

The curated defaults steer the unmarked form of a language to its reference variety. Without them, `langcodes` sends a bare tag to the region with the most speakers, such as `pt` to `pt-BR`.

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
| `ar-SA` | `ars-SA` |

The `ar-SA` default is an editorial choice, not a claim in the spec data. Saudi Arabia has several documented varieties, Najdi and Hejazi among them, and no single standard spoken form. `ar-SA` goes to Najdi, the variety of the capital region and the most widely spoken (Ingham, *Najdi Arabic*, 1994).

### Unknown variants and strict lookup

A private-use tag that names no spec, such as `pt-x-typo`, still resolves to the nearest registered spec. `resolve()` and `get()` then emit `UnknownVariantWarning`, which names the discarded subtag and the spec chosen:

```python
import warnings, orthography2ipa
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    orthography2ipa.resolve("pt-x-typo")    # 'pt-BR'
    str(w[0].message)  # "unknown variant subtag 'typo' in 'pt-x-typo'; using 'pt-BR' instead"
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
| `nld` | `nl` | `swe` | `sv` | `dan` | `da` |
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
| The bare ISO 639-3 code of an Arabic variety, mapped to the spec keyed by that code | `arz` to `arz-EG`, `ars` to `ars-SA`, and `ajp`, which SIL retired into `apc`, to `apc-JO` |
| A key that a spec had before it took its ISO 639-3 code, mapped to that spec | `ar-EG` to `arz-EG`, `ar-SA-x-najd` to `ars-SA`, `ar-x-gulf` to `afb` |
| An individual-language code that `macro=True` standardisation would collapse into its macrolanguage, mapped to itself | `quz`, which would otherwise become `qu`, and `diq`, which would become `zza` |
| An ISO 639-3 code whose variety has its spec under another key | `pnb` to `pa-PK`, `bar` to `de-x-bavarian` |
| A private-use tag, mapped to the spec that holds the variety | `pt-PT-x-barrancos` to `ext-PT-x-barrancos`, `pt-BR-x-sao-paulo` to `pt-BR-x-sp`, `ar-x-hijazi` to `acw-SA` |

Galician has one standard spec, `gl-ES`, and the bare tag `gl` resolves to it. The variety codes `gl-x-central`, `gl-x-occidental`, `gl-x-oriental`, `gl-x-eonavia` and `gl-x-reintegrado` resolve to the `gl-ES-x-*` spec of the same variety. `_ALIASES` in `registry.py` holds the full table.

## Plugin discovery

The registry finds plugins through `importlib.metadata` entry points, with one group for each pluggable stage. Discovery runs once per stage, on the first call that needs it, and the result stays cached at module scope. A plugin that fails to load logs a `WARNING` and is skipped. A bundled plugin whose optional dependency is absent logs at `DEBUG` instead, and names the extra that would enable it.

| Group | Lookup | When several plugins claim one code |
| :--- | :--- | :--- |
| `orthography2ipa.syllabify` | `get_syllabifier(code)` | The highest `priority` wins |
| `orthography2ipa.rescore` | `get_rescorers(code)` | All of them run, lowest `priority` first, so the highest has the last word |
| `orthography2ipa.stress` | `get_stress_plugin(code)` | The highest `priority` wins |
| `orthography2ipa.normalize`, `orthography2ipa.sandhi` | by entry-point name | The spec or the caller names one, so no contest arises |

The default `priority` of each plugin base class is `50`.

Discovery alone selects only a syllabifier, because a syllabifier must not change the transcription. The engine runs a normalize, stress, rescore or sandhi plugin only when the spec or the caller names it by entry-point name ([architecture.md](../engine/architecture.md#pluggable-steps)). `get_rescorers(code)` lists what the installed rescorer plugins contribute, but `G2P` runs only the declared ones. A stress plugin runs only when the spec sets `stress.source` to `"plugin"`. If none is installed, the engine raises `MissingStressPlugin`, which `orthography2ipa.registry` defines. A named plugin that is not installed raises `MissingPlugin`.

`who_answers(code)` reports which syllabifier and which rescorers answer for a code:

```python
orthography2ipa.who_answers("pt-PT")
# {'code': 'pt-PT',
#  'syllabify': 'orthography2ipa.syllabifiers.SilabificadorSyllabifier',
#  'rescore': ['built-in (spec allophone_rules only)']}
```

### The bundled syllabifier entry point

The package declares one entry point of its own in `pyproject.toml`:

```toml
[project.entry-points."orthography2ipa.syllabify"]
silabificador = "orthography2ipa.syllabifiers:SilabificadorSyllabifier"
```

It loads only when the `silabificador` package is installed, through the `portuguese` extra. It claims the Portuguese codes: `pt`, `pt-PT`, `pt-BR`, `pt-AO` and the other national varieties. With no syllabifier installed, `get_syllabifier()` returns `None` for every code, and the engine uses the bundled vowel-group splitter.

---
[← Command line](cli.md) · [Home](../index.md) · [Public API stability →](api_stability.md)
