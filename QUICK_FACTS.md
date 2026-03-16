# QUICK_FACTS.md — orthography2ipa

_Last updated: 2026-03-16_

## Package Identity

| Field | Value |
| :--- | :--- |
| **Package name** | `orthography2ipa` |
| **Current version** | `0.2.0a1` |
| **Python support** | 3.9 – 3.13 |
| **License** | Apache 2.0 |
| **PyPI** | `pip install orthography2ipa` |
| **Optional Arabic** | `pip install orthography2ipa[arabic]` |
| **Source** | `orthography2ipa/version.py` — `VERSION_STR` |

## Language Coverage

| Tier | Count |
| :--- | :--- |
| Production-quality | ~50 |
| Research-quality | ~20 |
| Stub/skeleton | ~238 |
| **Total registered** | **308+** |

## Key Public Classes

| Class | File | Description |
| :--- | :--- | :--- |
| `LanguageSpec` | `orthography2ipa/types.py` | Frozen dataclass: graphemes, allophones, positional_graphemes, ancestors |
| `PhonetokTokenizer` | `orthography2ipa/phonetok.py` | Maximal-munch tokenizer + beam-search IPA expansion |
| `ArabicG2PPlugin` | `orthography2ipa/plugins/arabic_g2p.py` | Rule-based Arabic→IPA with optional tashkeel |
| `SandhiEngine` | `orthography2ipa/sandhi.py` | Cross-word-boundary phonological rule application |
| `DialectTransform` | `orthography2ipa/transforms.py` | IPA dialect transform profile (15 Iberian Romance variants) |

## Key Public Functions

| Function | File | Description |
| :--- | :--- | :--- |
| `get(code)` | `orthography2ipa/registry.py` | Lazy-load `LanguageSpec` by BCP-47 or ISO 639 code |
| `segment_distance(a, b)` | `orthography2ipa/distance.py` | Normalized [0,1] phonological distance between two IPA phones |
| `phonological_distance(a, b)` | `orthography2ipa/distance.py` | Full `PhonologicalDistance` between two `LanguageSpec` objects |
| `apply_transform(ipa, profile)` | `orthography2ipa/transforms.py` | Apply a named dialect transform to an IPA string |
| `available_profiles()` | `orthography2ipa/transforms.py` | List all 15 registered dialect transform profile names |
| `load_json_spec(code)` | `orthography2ipa/json_loader.py` | Load a single `LanguageSpec` from JSON, resolving inheritance |

## Entry Points

| Group | Name | Class |
| :--- | :--- | :--- |
| `orthography2ipa.g2p` | `arabic` | `orthography2ipa.plugins.arabic_g2p:ArabicG2PPlugin` |

## Quick Usage

```python
from orthography2ipa import get
from orthography2ipa.phonetok import PhonetokTokenizer

# Load a language spec
spec = get("es-ES")
print(spec.graphemes["c"])          # → ['k', 's', 'θ']

# Tokenize and expand to IPA
tok = PhonetokTokenizer(spec)
paths = tok.ipa_beam("casa", beam_width=3)
print(paths[0])                     # → 'kasa'

# Phonological distance between languages
from orthography2ipa.distance import phonological_distance
spec_pt = get("pt-PT")
dist = phonological_distance(spec, spec_pt)
print(dist.jaccard)                 # → float in [0, 1]

# Dialect transforms
from orthography2ipa.transforms import apply_transform
ipa = "βiðɐ"                        # Lisbon-biased input
result = apply_transform(ipa, "transmontano")
print(result)
```

## Install Commands

```bash
# Standard install
pip install orthography2ipa

# With Arabic G2P support (ONNX)
pip install orthography2ipa[arabic]

# Editable dev install
pip install -e /path/to/orthography2ipa
```

## Test Command

```bash
pytest tests/ -v --cov=orthography2ipa --cov-report=term-missing
```
