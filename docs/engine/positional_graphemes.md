# Positional Graphemes

The `positional_graphemes` field refines the flat `graphemes` table by context. Many letters change their sound with their position in the word or with their neighbours. A positional entry states which IPA candidates apply in one environment. The engine builds an ordered list of the positions a grapheme stands in, and it uses the first position that the spec declares.

The field serves transcription. A positional entry does not change the phoneme inventory.

## Why positions

The flat table lists every sound a letter can spell. European Portuguese ⟨s⟩ has a flat entry of `["s", "z"]`. That list does not say which candidate a given word takes. The `pt-PT` spec adds the context:

```json
"positional_graphemes": {
  "s": {
    "word_initial": ["s"],
    "intervocalic": ["z"],
    "word_final": ["ʃ"],
    "intervocalic_cross_word": ["z"]
  }
}
```

```python
from orthography2ipa import G2P

pt = G2P("pt-PT")
pt.transcribe_word("sol")     # 'ˈsɔɫ'
pt.transcribe_word("casa")    # 'ˈkazɐ'
pt.transcribe_word("gatos")   # 'ˈɡatuʃ'
pt.transcribe("os amigos")    # 'oz ɐˈmiɡuʃ'
```

Not every one of these results comes from the positional table. The coda [ʃ] of ⟨pasta⟩ comes from an allophone rule, and the [z] of ⟨os amigos⟩ comes from a sandhi rule (see [allophony.md](allophony.md)). The `intervocalic_cross_word` key in this spec is one of the positions the engine never emits, as the next section explains.

## The `GraphemePosition` values

The keys are the values of `orthography2ipa.types.GraphemePosition`. A spec JSON uses the lowercase value, such as `word_initial`.

These positions describe the word edges and the neighbours:

| Value | Environment | Example |
|---|---|---|
| `word_initial` | first grapheme of the word | Spanish ⟨r⟩ is the trill [r] |
| `word_final` | last grapheme of the word | Spanish ⟨d⟩ is [ð] |
| `intervocalic` | between two vowel graphemes of one word | Spanish ⟨b d g⟩ lenite to [β ð ɣ] |
| `before_vowel`, `after_vowel` | next to any vowel grapheme | Brazilian ⟨l⟩ stays [l] before a vowel |
| `before_consonant`, `after_consonant` | next to any consonant grapheme | Brazilian ⟨l⟩ is [w] before a consonant |
| `before_final_vowel` | before a vowel that is the last audible slot and that the spec silences | French ⟨ie⟩ stays [i] in ⟨vie⟩ |
| `before_mute_e` | the vowel of the ⟨VCe⟩ pattern | English ⟨i⟩ is [aɪ] in ⟨time⟩ |

In an abugida, a consonant letter whose inherent vowel still stands counts as a vowel for `after_vowel`. Tibetan ⟨ལག⟩ is [lak], so the ⟨ག⟩ is after a vowel and also after a consonant.

These positions read the neighbouring letter or its class:

| Value | Environment | Example |
|---|---|---|
| `before_a`, `before_e`, `before_i`, `before_o`, `before_u`, `before_y` | before that vowel letter | Spanish ⟨c⟩ is [θ] before ⟨e⟩ and ⟨i⟩ |
| `after_a`, `after_e`, `after_i`, `after_o`, `after_u` | after that vowel letter | German ⟨ch⟩ after ⟨a⟩ |
| `before_front_vowel`, `after_front_vowel` | next to a front vowel letter | Romance ⟨c g⟩ softening |
| `before_back_vowel`, `after_back_vowel` | next to a back vowel letter | German ⟨ch⟩ is [x] after a back vowel |
| `before_palatal`, `after_palatal` | next to a grapheme whose IPA is a palatal consonant | European Portuguese stressed ⟨e⟩ before ⟨lh⟩ |

The exact-letter positions also match the Cyrillic plain vowel letters ⟨а э и і о у⟩. The iotated letters ⟨е ё ю я⟩ open with a glide, so they do not match.

These positions need the stress and syllable context that only the engine computes:

| Value | Environment | Example |
|---|---|---|
| `nucleus_stressed` | nucleus of the stressed syllable | full vowel quality |
| `nucleus_unstressed` | nucleus of an unstressed syllable | Catalan unstressed ⟨a⟩ is [ə] |
| `nucleus_secondary` | nucleus of a syllable with secondary stress | English keeps the vowel full |
| `first_pretonic` | the syllable just before the stress | Russian first-pretonic [ɐ] |
| `pretonic`, `posttonic` | before or after the stressed syllable | pretonic and posttonic reduction |
| `open_syllable`, `closed_syllable` | nucleus of a syllable without or with a coda | French ⟨eu⟩ is [ø] or [œ] |
| `nucleus_stressed_open`, `nucleus_stressed_closed` | stress and aperture together | Romance mid vowels under stress |
| `nucleus_unstressed_open`, `nucleus_unstressed_closed` | no stress, with aperture | aperture that survives reduction |
| `nucleus` | any vowel grapheme | a nucleus with no stress distinction |
| `default` | every context | the fallback entry |

A vowel grapheme and a grapheme whose first IPA candidate holds a vowel both take the nucleus positions. The second case covers the Cyrillic CV units, such as ⟨дя⟩ for [dʲa].

The enum also holds `onset`, `coda`, `intervocalic_cross_word`, `consonantal` and `vocalic`. The engine never emits these five, so an entry under one of them never fires in a transcription. Only a direct call to `resolve_grapheme` reads them. The test `test_positional_graphemes_never_key_on_inert_coda` in `tests/test_data_quality.py` refuses a spec that keys on `coda`. Use `word_final` or `before_consonant` for a consonant in the coda. Use an allophone rule with `syllable_position: "coda"` for real coda phonology. Cross-word effects belong in `sandhi_rules`.

The docstrings in `orthography2ipa/types.py` carry the citations for each position. Kenstowicz (1994), *Phonology in Generative Grammar*, Hayes (2009), *Introductory Phonology*, and Zsiga (2013), *The Sounds of Language*, describe the general environments.

## Resolution order

`orthography2ipa.positional.grapheme_positions` builds the ordered list for one grapheme. The order runs from the most specific position to the least specific:

1. `before_final_vowel`.
2. The exact next letter (`before_e`), then the next letter's vowel class (`before_front_vowel` or `before_back_vowel`), then `before_palatal`.
3. `word_initial`, then `word_final` for the true last grapheme.
4. `intervocalic`.
5. The crossed aperture position (`nucleus_stressed_open` and its siblings), then `open_syllable` or `closed_syllable`.
6. `nucleus_stressed`, or `nucleus_secondary`, or `nucleus_unstressed`. Then `first_pretonic`, `pretonic` or `posttonic`.
7. `before_mute_e`.
8. `word_final` for a grapheme that only a silenced plural ⟨-s⟩ or ⟨-x⟩ follows.
9. The previous letter (`after_e`), its vowel class, `after_palatal` and `after_vowel`. After a consonant, `after_palatal` and `after_consonant`.
10. `before_vowel` or `before_consonant`.
11. `nucleus`, then `default`.

`orthography2ipa.positional.positional_candidates` walks this list and returns the candidates of the first position the spec declares. If the grapheme has a positional entry, the winning candidates rank first and the flat candidates follow them. The beam keeps the full search space this way. If no position matches, the flat table and its weights apply.

A spec can therefore declare a class rule and a narrower letter rule together. With `before_front_vowel` and `before_e` on one grapheme, ⟨e⟩ takes the `before_e` entry and every other front vowel takes the class entry. A vowel letter that a spec reads as the glide /j/ is both a front vowel and a palatal. The vowel class comes first, so `before_front_vowel` outranks `before_palatal` for that neighbour.

A plural ⟨-s⟩ makes the slot before it count as word-final at step 8, below the stress positions. So a stress rule wins over a `word_final` reduction for a stressed clitic such as Barranquenho ⟨les⟩.

## Vowel-class positions

The front and back classes state the commonest context rule of Latin-script orthographies in one entry. Romance ⟨c⟩ and ⟨g⟩ soften before any front vowel letter, accented or not. Without the classes, a spec needs one entry for each vowel letter and for each accented form of it.

`orthography2ipa.vowels` decides membership. The front class is ⟨e i y⟩, their accented forms and the front rounded letters ⟨ü ö ø œ æ⟩. The back class is ⟨a o u⟩ and their accented forms. The class reads the first letter of the neighbouring grapheme.

```python
from orthography2ipa.vowels import is_back_vowel, is_front_vowel

is_front_vowel("é")   # True
is_front_vowel("y")   # True
is_back_vowel("â")    # True
```

This Italian-style demo spec has one class entry for ⟨c⟩:

```python
from orthography2ipa import G2P
from orthography2ipa.registry import _cache
from orthography2ipa.types import LanguageSpec

demo = LanguageSpec(
    code="x-demo", name="Demo", family="Demo", family_path=(), clade=False,
    script="Latin",
    graphemes={"c": ["k"], "e": ["e"], "i": ["i"], "y": ["i"],
               "a": ["a"], "o": ["o"], "u": ["u"], "é": ["e"]},
    allophones={},
    positional_graphemes={"c": {"before_front_vowel": ["tʃ"]}},
)
_cache["x-demo"] = demo
eng = G2P("x-demo")

eng.transcribe_word("ce")   # 'tʃe'
eng.transcribe_word("cé")   # 'tʃe'
eng.transcribe_word("cy")   # 'tʃi'
eng.transcribe_word("ca")   # 'ka'
eng.transcribe_word("cu")   # 'ku'
```

## Palatal positions

`before_palatal` and `after_palatal` are the consonant-side mirror of the vowel classes. They read the primary IPA candidate of the neighbour, not its spelling. So one entry covers ⟨lh⟩ [ʎ], ⟨nh⟩ [ɲ], ⟨ch⟩ [ʃ], ⟨x⟩ and ⟨j⟩ together.

`orthography2ipa.vowels.is_palatal_consonant` decides membership. The set is ⟨ʎ ɲ ʃ ʒ j c ɟ ç ʝ ɕ ʑ ɥ⟩ and the affricates ⟨tʃ dʒ tɕ dʑ⟩, with or without a tie bar. The function reads only the first segment, so ⟨ʃː⟩ is palatal too.

```python
from orthography2ipa.vowels import is_palatal_consonant

is_palatal_consonant("ʎ")    # True
is_palatal_consonant("t͡ʃ")   # True
is_palatal_consonant("s")    # False
```

European Portuguese stressed ⟨e⟩ becomes [ɐ] before a palatal, as in ⟨velho⟩ and ⟨espelho⟩. This demo spec states the rule once:

```python
demo2 = LanguageSpec(
    code="x-demo2", name="Demo2", family="Demo", family_path=(), clade=False,
    script="Latin",
    graphemes={"e": ["e"], "t": ["t"], "lh": ["ʎ"], "nh": ["ɲ"], "ch": ["ʃ"]},
    allophones={},
    positional_graphemes={"e": {"before_palatal": ["ɐ"]}},
)
_cache["x-demo2"] = demo2
eng = G2P("x-demo2")

eng.transcribe_word("elh")   # 'ɐʎ'
eng.transcribe_word("enh")   # 'ɐɲ'
eng.transcribe_word("ech")   # 'ɐʃ'
eng.transcribe_word("et")    # 'et'
```

The class positions do nothing for a spec that does not declare them.

## Syllable aperture

`open_syllable`, `closed_syllable` and the four crossed positions key a nucleus on whether its syllable has a coda. The Romance *loi de position* is stated in this environment. It gives close-mid /e ø o/ in open syllables and open-mid /ɛ œ ɔ/ in closed ones (Fougeron & Smith 1993, Tranel 1987 ch. 4, both in the `sources` of `fr-FR`). The French spec keys ⟨eu⟩ on aperture:

```json
"eu": {"default": ["ø", "œ"], "open_syllable": ["ø", "œ"], "closed_syllable": ["œ", "ø"]}
```

```python
fr = G2P("fr-FR")
fr.transcribe_word("heureux")     # 'øʁø'
fr.transcribe_word("fleur")       # 'flœʁ'
fr.transcribe_word("chanteurs")   # 'ʃɑ̃tœʁ'
```

The engine decides aperture on the orthographic syllable from the spec's own syllabifier. A syllable is open when its last character is a vowel letter. In the last syllable of the word, the engine first strips the trailing graphemes that the spec silences. So a mute ⟨x⟩ or ⟨h⟩ does not close a syllable (*heureux*, *beuh*). A mute ⟨s⟩ after a pronounced ⟨r⟩ does not open one (*chanteurs*). A hyphen also ends the word for this test, so *peut-être* has an open first syllable.

The crossed positions outrank the aperture pair, and the aperture pair outranks the stress-only positions. So a spec that declares `nucleus_unstressed` without `nucleus_unstressed_open` keeps its reduction in every unstressed syllable. The engine syllabifies a word for aperture only when the spec declares one of these keys.

The proxy is only as good as the syllable boundary. A syllabifier that maximises onsets without phonotactics makes syllables open that are closed. Measure an aperture declaration on the [benchmark board](../evaluation/benchmarks.md) before you ship it.

## Secondary stress

A spec can declare `stress.secondary_stress`. A syllable that heads a secondary foot then takes `nucleus_secondary` and no unstressed position. It takes neither `nucleus_unstressed` nor its aperture pair, because such a syllable is not weak (Liberman & Prince 1977, Hayes 1995 ch. 3). If the spec declares nothing for `nucleus_secondary`, the grapheme falls through to its default mapping, which is the full vowel. The reduction entries then reach only the syllables with no stress. A spec without the declaration does not change.

## The engine and the standalone beam

The standalone tokenizer beam (`PhonetokTokenizer.ipa_beam` and `ipa_best`) reads the same positional entries as the engine. Both call `orthography2ipa.positional.resolve_branches`, so the two paths cannot drift apart.

```python
from orthography2ipa import get
from orthography2ipa.phonetok import PhonetokTokenizer

G2P("es-ES").transcribe_word("cena")             # 'ˈθena'
PhonetokTokenizer(get("es-ES")).ipa_best("cena")  # 'θena'
```

The beam has no stress context and no syllabification. So the stress positions and the aperture positions fire on the engine path only, and the beam adds no stress marks and no sandhi. French ⟨fleur⟩ shows the difference. The engine gives `flœʁ` from the closed syllable, and `ipa_best` gives `fløʁ` from the default entry. Every other position resolves the same on both paths.

## Reading positions from Python

`LanguageSpec.resolve_grapheme(grapheme, position=None)` returns the candidates for one position. It tries `positional_graphemes[grapheme][position]` first and then the flat `graphemes[grapheme]`. It does not fall back to a positional `default` entry. It raises `KeyError` when the grapheme is in neither table. This method is a lookup, not the engine. It reads the five positions the engine never emits, and it applies no resolution order.

```python
import orthography2ipa
from orthography2ipa.types import GraphemePosition

pt = orthography2ipa.get("pt-PT")

pt.resolve_grapheme("s")                                  # ['s', 'z']
pt.resolve_grapheme("s", GraphemePosition.WORD_INITIAL)   # ['s']
pt.resolve_grapheme("s", GraphemePosition.INTERVOCALIC)   # ['z']
pt.resolve_grapheme("s", GraphemePosition.WORD_FINAL)     # ['ʃ']
pt.resolve_grapheme("a", GraphemePosition.ONSET)          # ['a', 'ɐ']

pt.has_positional_data()                  # True
sorted(pt.positional_grapheme_keys())     # ['a', 'c', 'e', 'g', 'gu', 'l', 'm', 'n', 'o', 'qu', 'r', 's', 'z']
pt.positions_for_grapheme("s")
# (<GraphemePosition.WORD_FINAL: 'word_final'>, <GraphemePosition.WORD_INITIAL: 'word_initial'>,
#  <GraphemePosition.INTERVOCALIC: 'intervocalic'>,
#  <GraphemePosition.INTERVOCALIC_CROSS_WORD: 'intervocalic_cross_word'>)
```

The type of the field is `PositionalGrapheme2IPA`, which is `Dict[str, Dict[GraphemePosition, List[str]]]`. The loader turns the JSON keys into enum members. The dataclass default is `None`, and `__post_init__` turns it into `{}`.

## Positions in the shipped specs

Give a grapheme a positional entry only when its sound changes with context. A grapheme with one sound everywhere stays in the flat table. The `es-ES` spec states Spanish lenition and the soft ⟨c g⟩ this way:

```json
"positional_graphemes": {
  "b": {"intervocalic": ["β"]},
  "d": {"intervocalic": ["ð"], "word_final": ["ð"]},
  "g": {"before_e": ["x"], "before_i": ["x"], "intervocalic": ["ɣ"]},
  "c": {"before_e": ["θ"], "before_i": ["θ"]}
}
```

```python
es = G2P("es-ES")
es.transcribe_word("lobo")     # 'ˈloβo'
es.transcribe_word("boca")     # 'ˈboka'
es.transcribe_word("verdad")   # 'beɾˈdað'
es.transcribe_word("gente")    # 'ˈxente'
es.transcribe_word("lago")     # 'ˈlaɣo'
```

The `pt-BR` spec vocalises ⟨l⟩ in the coda with `before_consonant` and `word_final`:

```json
"l": {"before_consonant": ["w"], "word_final": ["w"], "before_vowel": ["l"], "onset": ["l"]}
```

```python
br = G2P("pt-BR")
br.transcribe_word("alto")   # 'ˈawtu'
br.transcribe_word("mal")    # 'ˈmaw'
br.transcribe_word("mala")   # 'ˈmalɐ'
```

Its `onset` entry never fires. The `before_vowel` entry does that work.

## Positional entries and allophone rules

The two layers work at different levels. `positional_graphemes` picks the phoneme a grapheme spells. `allophone_rules` pick the surface form of a phoneme that is already chosen. Some processes fit either layer, such as English /t/ flapping. Use `positional_graphemes` when the step from spelling to phoneme is ambiguous. Use `allophone_rules` when the step from phoneme to surface varies. A spec can use both. [allophony.md](allophony.md) describes the rule layer.

`distance.positional_divergence` compares the positional entries of two specs. The other metrics in [distance.md](../guide/distance.md) do not read positional entries.

---
[← Allophony](allophony.md) · [Home](../index.md) · [Data Model →](../specs/data_model.md)
