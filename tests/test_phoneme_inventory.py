"""A language's sounds are not a property of its writing system.

`phonemes` states the inventory directly, so a language can have a phonology with
no orthography — which is the normal condition for most of the world's languages,
and the only honest way to model a reconstructed one.
"""
import json
from pathlib import Path

import orthography2ipa as o2i
from orthography2ipa import json_loader
from orthography2ipa.distance import _extract_phonemes, inventory_distance


def test_an_unwritten_language_can_have_a_phonology(tmp_path, monkeypatch):
    """The point of the field: no graphemes at all, yet a full inventory — and it
    can be compared with any other language.

    Before this field existed the inventory was read out of the grapheme map, so a
    language with no orthography had, by construction, no phonology. That is
    backwards, and it silently excluded most human languages.
    """
    (tmp_path / "zzu.json").write_text(json.dumps({
        "code": "zzu",
        "name": "An unwritten language",
        "family": "Isolate",
        "script": "Unwritten",
        "graphemes": {},          # nobody writes it
        "allophones": {},
        "phonemes": ["p", "t", "k", "m", "n", "a", "i", "u"],
    }), encoding="utf-8")
    monkeypatch.setattr(json_loader, "_DATA_DIR", Path(tmp_path))
    monkeypatch.setitem(json_loader._index, "zzu", tmp_path / "zzu.json")
    spec = json_loader.load_json_spec("zzu")

    assert spec.graphemes == {}
    assert _extract_phonemes(spec) == {"p", "t", "k", "m", "n", "a", "i", "u"}

    # And it is comparable — the phonological axis works with no orthography.
    result = inventory_distance(spec, o2i.get("pt-PT"))
    assert 0.0 < result.jaccard < 1.0


def test_a_reconstructed_language_declares_its_inventory():
    """Proto-Indo-European was never written. The asterisked forms in `graphemes`
    are the literature's NOTATION for the reconstruction, not an orthography
    anyone read — keeping them is right, but the inventory must not depend on
    them."""
    ine = o2i.get("ine")
    assert ine.phonemes, "a reconstructed language should declare its inventory"
    assert _extract_phonemes(ine) == set(ine.phonemes)


def test_specs_that_declare_nothing_are_unchanged():
    """The derivation from graphemes remains the fallback, so every existing spec
    keeps exactly the inventory it had."""
    for code in ("pt-PT", "es-ES", "en-GB", "fi", "ar"):
        spec = o2i.get(code)
        if spec.phonemes:
            continue
        derived = {i for v in spec.graphemes.values() if v for i in v if i}
        assert _extract_phonemes(spec) == derived


def test_declared_inventory_wins_over_the_grapheme_map():
    """When a spec says what its sounds are, that is the answer — the spelling
    does not get a vote."""
    ine = o2i.get("ine")
    from_graphemes = {i for v in ine.graphemes.values() if v for i in v if i}
    assert _extract_phonemes(ine) == set(ine.phonemes)
    # (For `ine` the two coincide, because its "orthography" was an identity map
    # invented precisely to smuggle the inventory in. That is the hack this field
    # retires.)
    assert set(ine.phonemes) == from_graphemes
