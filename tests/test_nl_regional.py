"""Regional Standard Dutch: the ``nl-NL-x-*`` delta specs.

Each spec is a delta over ``nl-NL``. It inherits the whole standard and
states only what its region changes. The expected values come from the
sources the specs cite, never from the engine:

- Dutch Limburg (``nl-NL-x-limburg``). van der Harst & Van de Velde (2007,
  *Taal en Tongval* 59, pp. 184, 189) measure word-initial /ɣ/ in the carrier
  word *guize*: in Dutch Limburg the norm is "de stemloze velair", with 77.5%
  voiceless tokens and 5% uvular ones. Van de Velde (2016, *Onze Taal*, p. 10)
  gives 65% voiced word-initial v in the south (*vier* against *fier*).
- Polder Dutch (``nl-NL-x-polder``), a sociolect and not a region. Stroop
  (1998, *Poldernederlands*, pp. 25-27) gives the lowered diphthongs: ⟨ei ij⟩
  "aai [a:i]", ⟨ui⟩ "[ɑy]" and ⟨ou⟩ "aau [a:u]", with the examples *taaid*,
  *haus*, *Mauden*, *jaauw*, *vraauw* and *Paaul*.
- Groningen and north Drenthe (``nl-NL-x-groninge``), regional Standard
  Dutch, not the Low Saxon dialect Gronings (``gos``). Van de Velde (2016,
  p. 10) gives only 9% voiced word-initial v in the north: "Ze zeggen in het
  noorden dus meestal 'fier' als het cijfer vier is bedoeld". van der Harst &
  Van de Velde (2007, pp. 184, 189) find /ɣ/ 100% uvular and 90% voiceless
  in the north, with "de sterk geschraapte stemloze uvulair" as the norm.

A word with none of the features of its spec must come out exactly as
``nl-NL`` gives it.
A regional spec states its own value for a feature that ``nl-NL`` may still
change, so a moved parent must not move the child.
"""
import json
from pathlib import Path

import pytest

from orthography2ipa import G2P, json_loader
from orthography2ipa.registry import resolves_exactly

DATA = Path(__file__).parents[1] / "orthography2ipa" / "data"
LIMBURG = "nl-NL-x-limburg"
POLDER = "nl-NL-x-polder"
GRONINGEN = "nl-NL-x-groninge"


@pytest.fixture(scope="module")
def nl():
    return G2P("nl-NL")


@pytest.fixture(scope="module")
def limburg():
    assert resolves_exactly(LIMBURG), f"{LIMBURG} names no spec"
    return G2P(LIMBURG)


@pytest.fixture(scope="module")
def polder():
    assert resolves_exactly(POLDER), f"{POLDER} names no spec"
    return G2P(POLDER)


def _velar(ipa: str) -> str:
    """The nl-NL transcription with every dorsal fricative made velar [x]."""
    return "".join("x" if ch in "ɣχ" else ch for ch in ipa)


def test_limburg_resolves_to_its_own_spec():
    assert resolves_exactly(LIMBURG)


def test_limburg_g_of_the_carrier_word_is_the_voiceless_velar(limburg):
    # 'in de guize horen we g' (van der Harst & Van de Velde 2007, p. 179).
    assert limburg.transcribe("guize").startswith("ˈx")


@pytest.mark.parametrize("word", [
    "guize", "gaan", "goed", "gras", "liegen", "dagen", "egel", "dag", "oog",
    "bergen",
])
def test_limburg_g_is_velar_x_and_nothing_else_moves(nl, limburg, word):
    # Onset /ɣ/: voiceless velar norm (pp. 184, 189). Word-final ⟨g⟩: the
    # velar place of /ɣ/ with the final devoicing nl-NL applies. ⟨berg⟩ is
    # an nl-NL grapheme that spells the same ⟨g⟩. The words hold no ⟨ch⟩
    # and no ⟨v⟩, so every other segment is inherited.
    assert limburg.transcribe(word) == _velar(nl.transcribe(word))


@pytest.mark.parametrize("word,onset", [("vier", "v"), ("fier", "f")])
def test_limburg_keeps_word_initial_v_voiced(limburg, word, onset):
    # 'in het zuiden 65%' voiced word-initial v (Van de Velde 2016, p. 10).
    assert limburg.transcribe(word).lstrip("ˈ")[0] == onset


@pytest.mark.parametrize("word", [
    "water", "ziek", "lachen", "school", "huis", "fee", "beuk", "boot",
    "bakker", "zitten",
])
def test_limburg_words_without_g_or_v_equal_the_standard(nl, limburg, word):
    assert limburg.transcribe(word) == nl.transcribe(word)


def test_limburg_keeps_its_values_when_nl_nl_moves(tmp_path, monkeypatch):
    # An nl-NL with the uvular [χ] for ⟨g⟩ and a devoiced initial ⟨v⟩, the
    # parent values Gussenhoven (1992) and Van de Velde (2016) give for the
    # western standard. The Limburg values must not follow them.
    raw = json.loads((DATA / "nl-NL.json").read_text(encoding="utf-8"))
    pos = raw["positional_graphemes"]
    pos["g"] = {"word_final": ["χ"], "default": ["χ"]}
    pos["berg"] = {"word_final": ["bɛrχ"], "default": ["bɛrχ"]}
    pos["v"] = {"word_final": ["f"], "default": ["f"]}
    moved_file = tmp_path / "nl-NL.json"
    moved_file.write_text(json.dumps(raw, ensure_ascii=False), encoding="utf-8")
    index = dict(json_loader._index, **{"nl-NL": moved_file})
    specs = {k: v for k, v in json_loader._specs.items()
             if k not in ("nl-NL", LIMBURG)}
    monkeypatch.setattr(json_loader, "_index", index)
    monkeypatch.setattr(json_loader, "_specs", specs)

    moved = G2P("nl-NL", spec=json_loader.load_json_spec("nl-NL"))
    child = G2P(LIMBURG, spec=json_loader.load_json_spec(LIMBURG))
    assert moved.transcribe("gaan").startswith("ˈχ")
    assert moved.transcribe("vier").startswith("ˈf")
    for word in ("guize", "gaan", "liegen", "dag", "bergen"):
        assert child.transcribe(word) == _velar(moved.transcribe(word))
    assert child.transcribe("vier").startswith("ˈv")


# Stroop (1998): the nl-NL diphthong and its Polder value.
_POLDER_DIPHTHONGS = {"ɛi": "aːi", "œy": "ɑy", "ɑu": "aːu"}


def _lowered(ipa: str, standard: dict[str, str] | None = None) -> str:
    """The nl-NL transcription with each diphthong replaced by its Polder value."""
    for old, new in (standard or _POLDER_DIPHTHONGS).items():
        ipa = ipa.replace(old, new)
    return ipa


def test_polder_resolves_to_its_own_spec():
    assert resolves_exactly(POLDER)


def test_polder_is_a_sociolect_with_no_location(polder):
    # Stroop (pp. 16, 51) defines the speakers by age, sex and job, and
    # most of them grew up outside the Randstad: no point on a map.
    assert polder.spec.location is None


@pytest.mark.parametrize("word,diphthong", [
    ("tijd", "aːi"),     # taaid (p. 25)
    ("twijfelen", "aːi"),  # twaaifelen (p. 25)
    ("vrijheid", "aːi"),   # vraaihaaid (p. 25)
    ("huis", "ɑy"),      # haus (p. 26)
    ("buiten", "ɑy"),    # bauten (p. 26)
    ("Muiden", "ɑy"),    # Mauden (p. 26)
    ("jou", "aːu"),      # jaauw (p. 27)
    ("vrouw", "aːu"),    # vraauw (p. 27)
    ("Paul", "aːu"),     # Paaul (p. 27)
])
def test_polder_lowers_the_diphthong_of_stroops_examples(polder, word, diphthong):
    assert diphthong in polder.transcribe(word)


@pytest.mark.parametrize("word", [
    "tijd", "wijn", "ijs", "reis", "trein", "twijfelen", "vrijheid", "huis",
    "buiten", "uit", "ruim", "Muiden", "vrouw", "jou", "koud", "zout", "blauw",
    "gauw", "Paul", "paus", "flaauw",
])
def test_polder_changes_only_the_diphthong(nl, polder, word):
    # ⟨ei ij⟩ [a:i] (p. 25), ⟨ui⟩ [ɑy] (p. 26), ⟨ou au⟩ [a:u] (p. 27); the
    # other segments are inherited from nl-NL.
    assert polder.transcribe(word) == _lowered(nl.transcribe(word))


@pytest.mark.parametrize("word", [
    "water", "ziek", "school", "fee", "beuk", "boot", "bakker", "kraai",
    "mooi", "groei", "leeuw", "nieuw", "ruw", "gaan", "vier", "kerk",
])
def test_polder_words_without_the_diphthongs_equal_the_standard(nl, polder, word):
    # ⟨ee eu oo⟩, ⟨r⟩ and the fricatives stay as in nl-NL: Stroop gives no
    # endpoint or no majority for them (pp. 30-34).
    assert polder.transcribe(word) == nl.transcribe(word)


def test_polder_keeps_its_values_when_nl_nl_moves(polder, tmp_path, monkeypatch):
    # An nl-NL that gives the diphthongs their alternative surfaces [ɛɪ œʏ ʌu].
    # The Polder values must not follow them.
    raw = json.loads((DATA / "nl-NL.json").read_text(encoding="utf-8"))
    moved_values = {"ɛi": "ɛɪ", "œy": "œʏ", "ɑu": "ʌu"}
    for key in ("ei", "ij", "ui", "ou", "au", "ouw", "auw", "aauw"):
        raw["graphemes"][key] = [moved_values[raw["graphemes"][key][0]]]
    moved_file = tmp_path / "nl-NL.json"
    moved_file.write_text(json.dumps(raw, ensure_ascii=False), encoding="utf-8")
    index = dict(json_loader._index, **{"nl-NL": moved_file})
    specs = {k: v for k, v in json_loader._specs.items()
             if k not in ("nl-NL", POLDER)}
    monkeypatch.setattr(json_loader, "_index", index)
    monkeypatch.setattr(json_loader, "_specs", specs)

    moved = G2P("nl-NL", spec=json_loader.load_json_spec("nl-NL"))
    child = G2P(POLDER, spec=json_loader.load_json_spec(POLDER))
    for word, moved_diphthong in (("tijd", "ɛɪ"), ("huis", "œʏ"), ("vrouw", "ʌu"),
                                  ("blauw", "ʌu"), ("koud", "ʌu")):
        assert moved_diphthong in moved.transcribe(word)
        assert child.transcribe(word) == polder.transcribe(word)


@pytest.fixture(scope="module")
def groningen():
    assert resolves_exactly(GRONINGEN), f"{GRONINGEN} names no spec"
    return G2P(GRONINGEN)


def _uvular(ipa: str) -> str:
    """The nl-NL transcription with every dorsal fricative made uvular [χ]."""
    return "".join("χ" if ch in "ɣx" else ch for ch in ipa)


def _initial_f(ipa: str) -> str:
    """The nl-NL transcription with a word-initial [v] made [f]."""
    stress = ipa[0] if ipa[:1] in "ˈˌ" else ""
    body = ipa[len(stress):]
    return stress + ("f" + body[1:] if body.startswith("v") else body)


def test_groningen_resolves_to_its_own_spec():
    assert resolves_exactly(GRONINGEN)


def test_groningen_is_regional_standard_dutch_not_gronings(groningen):
    # Gronings has an ISO 639-3 code of its own, so it is keyed `gos`; this
    # spec descends from the standard and inherits its ISO code.
    assert groningen.spec.parent == "nl-NL"
    assert groningen.spec.iso639_3 == "nld"


@pytest.mark.parametrize("word,onset", [("vier", "f"), ("fier", "f")])
def test_groningen_says_fier_for_vier(groningen, word, onset):
    # "Ze zeggen in het noorden dus meestal 'fier' als het cijfer vier is
    # bedoeld" (Van de Velde 2016, p. 10).
    assert groningen.transcribe(word).lstrip("ˈ")[0] == onset


@pytest.mark.parametrize("word", [
    "vier", "vis", "vader", "van", "vuur", "voor", "vaak", "veel",
])
def test_groningen_devoices_only_the_initial_v(nl, groningen, word):
    assert groningen.transcribe(word) == _initial_f(nl.transcribe(word))


@pytest.mark.parametrize("word", ["over", "avond", "duivel", "leven"])
def test_groningen_keeps_a_word_internal_v(nl, groningen, word):
    # The source measures the word-initial ⟨v⟩ only.
    assert groningen.transcribe(word) == nl.transcribe(word)


@pytest.mark.parametrize("word", [
    "gaan", "goed", "gras", "liegen", "dagen", "egel", "dag", "oog", "bergen",
])
def test_groningen_g_is_the_voiceless_uvular(nl, groningen, word):
    # N-N: 100% uvular (Table 3) and 90% voiceless (Table 4), p. 184. The
    # words hold no ⟨ch⟩ and no ⟨v⟩, so every other segment is inherited.
    assert groningen.transcribe(word) == _uvular(nl.transcribe(word))


@pytest.mark.parametrize("word", ["zandgrond", "hoofdgebouw", "handgranaat", "Landgraaf"])
def test_groningen_devoices_a_coda_obstruent_before_the_uvular(limburg, groningen, word):
    # The inherited NL_CODA_DEVOICE_* rules devoice a coda obstruent before a
    # voiceless fricative. Limburg gets the same words with the velar [x], so
    # its output with [x] made [χ] is the expected Groningen value.
    assert groningen.transcribe(word) == _uvular(limburg.transcribe(word))


@pytest.mark.parametrize("word", [
    "water", "ziek", "lachen", "school", "huis", "fee", "beuk", "boot",
    "bakker", "zitten", "lopen",
])
def test_groningen_words_without_g_or_initial_v_equal_the_standard(nl, groningen, word):
    assert groningen.transcribe(word) == nl.transcribe(word)


def test_groningen_keeps_its_values_when_nl_nl_moves(groningen, tmp_path, monkeypatch):
    # An nl-NL with the velar [ɣ x] of the south and a devoiced ⟨v⟩ in every
    # position. The Groningen values must not follow it.
    raw = json.loads((DATA / "nl-NL.json").read_text(encoding="utf-8"))
    pos = raw["positional_graphemes"]
    pos["g"] = {"word_final": ["x"], "default": ["x"]}
    pos["berg"] = {"word_final": ["bɛrx"], "default": ["bɛrx"]}
    pos["v"] = {"word_final": ["f"], "default": ["f"]}
    moved_file = tmp_path / "nl-NL.json"
    moved_file.write_text(json.dumps(raw, ensure_ascii=False), encoding="utf-8")
    index = dict(json_loader._index, **{"nl-NL": moved_file})
    specs = {k: v for k, v in json_loader._specs.items()
             if k not in ("nl-NL", GRONINGEN)}
    monkeypatch.setattr(json_loader, "_index", index)
    monkeypatch.setattr(json_loader, "_specs", specs)

    moved = G2P("nl-NL", spec=json_loader.load_json_spec("nl-NL"))
    child = G2P(GRONINGEN, spec=json_loader.load_json_spec(GRONINGEN))
    assert moved.transcribe("gaan").startswith("ˈx")
    assert "f" in moved.transcribe("over")
    for word in ("gaan", "liegen", "dag", "bergen", "vier", "over", "geven"):
        assert child.transcribe(word) == groningen.transcribe(word)
