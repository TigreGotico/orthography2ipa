"""Regional Standard Dutch: the ``nl-NL-x-*`` delta specs.

Each spec is a delta over ``nl-NL``. It inherits the whole standard and
states only what its region changes. The expected values come from the
sources the specs cite, never from the engine:

- Dutch Limburg (``nl-NL-x-limburg``). van der Harst & Van de Velde (2007,
  *Taal en Tongval* 59, pp. 184, 189) measure word-initial /ɣ/ in the carrier
  word *guize*: in Dutch Limburg the norm is "de stemloze velair", with 77.5%
  voiceless tokens and 5% uvular ones. Van de Velde (2016, *Onze Taal*, p. 10)
  gives 65% voiced word-initial v in the south (*vier* against *fier*).

A word with no ⟨g⟩ and no ⟨v⟩ must come out exactly as ``nl-NL`` gives it.
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


@pytest.fixture(scope="module")
def nl():
    return G2P("nl-NL")


@pytest.fixture(scope="module")
def limburg():
    assert resolves_exactly(LIMBURG), f"{LIMBURG} names no spec"
    return G2P(LIMBURG)


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
