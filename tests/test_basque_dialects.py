"""Validation tests for the Basque (``eu``) dialect specs.

Basque is a language isolate. The base spec ``eu`` (Euskara Batua) has a
conservative three-way sibilant contrast; the dialect specs model the
west→east continuum of sound changes. Every feature asserted here is
grounded in a source that was read directly:

- Bedialauneta Txurruka & Hualde (2023), "Markina Basque", JIPA 53(3):
  1095-1122 (Biscayan sibilant/affricate/palatal mergers, p.1098).
- Hualde, Lujanbio & Zubiri (2010), "Goizueta Basque", JIPA 40(1):
  113-127 (Upper Navarrese sibilant retention p.119, /h/ loss, yeísmo).
- Hualde (2018), "Aspiration in Basque", PiHPH 3: 1-27 (east/west
  aspiration split).
- Egurtzegi (2013), "Phonetics and Phonology" (Souletin /y/ and the
  nasalised-vowel series shared with Roncalese, p.127).

These tests assert the modelled grapheme/allophone data and the
registration/inheritance/distance wiring. Phonological features that are
NOT recoverable from standard orthography (vowel nasality, the Souletin
aspirated/unaspirated split, Roncalese metaphony/syncope) are documented
in the spec ``notes`` and deliberately not emitted; those are checked by
asserting they are mentioned in ``notes``, not by transcription.
"""
from __future__ import annotations

import pytest

import orthography2ipa
from orthography2ipa.g2p import G2P
from orthography2ipa.distance import ancestry_similarity, phonological_distance

DIALECTS = [
    "eu-x-bizkaiera",
    "eu-x-gipuzkera",
    "eu-x-nafarra-garaia",
    "eu-x-nafarra-beherea",
    "eu-x-lapurtera",
    "eu-x-zuberera",
    "eu-x-erronkariera",
]


def _spec(code: str):
    return orthography2ipa.get(code)


# ───────────────────────────────────────────────────────────────────────
# Registration & inheritance
# ───────────────────────────────────────────────────────────────────────
class TestRegistration:
    def test_base_loads(self):
        assert _spec("eu").family == "Isolate"

    @pytest.mark.parametrize("code", DIALECTS)
    def test_dialect_loads(self, code):
        assert _spec(code).code == code

    @pytest.mark.parametrize("code", DIALECTS)
    def test_parent_is_eu(self, code):
        assert _spec(code).parent == "eu"

    @pytest.mark.parametrize("code", DIALECTS)
    def test_inherits_base_vowels(self, code):
        # Five-vowel base, inherited via graphemes_base="eu".
        g = _spec(code).graphemes
        for v in ["a", "e", "i", "o", "u"]:
            assert v in g and g[v], f"{code}: vowel {v} not inherited"

    @pytest.mark.parametrize("code", DIALECTS)
    def test_every_dialect_cites_a_read_source(self, code):
        ids = {s.id for s in _spec(code).sources}
        read = {
            "bedialauneta_hualde2023",
            "hualde_lujanbio_zubiri2010",
            "hualde2018_aspiration",
            "egurtzegi2013",
        }
        assert ids & read, f"{code}: no directly-read source cited"


# ───────────────────────────────────────────────────────────────────────
# Base inventory (eu) — the three-way sibilant contrast
# ───────────────────────────────────────────────────────────────────────
class TestBaseInventory:
    def test_three_way_fricatives(self):
        g = _spec("eu").graphemes
        assert g["z"] == ["s̻"]
        assert g["s"] == ["s̺"]
        assert g["x"] == ["ʃ"]

    def test_three_way_affricates(self):
        g = _spec("eu").graphemes
        assert g["tz"] == ["ts̻"]
        assert g["ts"] == ["ts̺"]
        assert g["tx"] == ["tʃ"]


# ───────────────────────────────────────────────────────────────────────
# Biscayan — Western mergers (Bedialauneta & Hualde 2023: 1098)
# ───────────────────────────────────────────────────────────────────────
class TestBiscayan:
    CODE = "eu-x-bizkaiera"

    def test_sibilant_merger_to_apical(self):
        g = _spec(self.CODE).graphemes
        # s and z both give apico-alveolar /s̺/ (palatalising to ʃ after i)
        assert g["s"] == ["s̺", "ʃ"]
        assert g["z"] == ["s̺", "ʃ"]

    def test_affricate_merger_to_laminal(self):
        g = _spec(self.CODE).graphemes
        assert g["ts"] == ["ts̻"]
        assert g["tz"] == ["ts̻"]

    def test_palatal_stop_merges_to_affricate(self):
        assert _spec(self.CODE).graphemes["tt"] == ["tʃ"]

    def test_transcription_has_no_laminal_sibilant(self):
        # zezen 'bull' — with the merger both z's surface as apical s̺.
        out = G2P(self.CODE).transcribe("zezen")
        assert "s̻" not in out
        assert "s̺" in out

    def test_no_aspiration(self):
        assert _spec(self.CODE).allophones.get("h") == [""]


# ───────────────────────────────────────────────────────────────────────
# Gipuzkoan — Central; base sibilants retained, no /h/
# ───────────────────────────────────────────────────────────────────────
class TestGipuzkoan:
    CODE = "eu-x-gipuzkera"

    def test_base_sibilants_retained(self):
        g = _spec(self.CODE).graphemes
        assert g["z"] == ["s̻"]
        assert g["s"] == ["s̺"]

    def test_h_absent(self):
        assert _spec(self.CODE).allophones.get("h") == [""]


# ───────────────────────────────────────────────────────────────────────
# Upper Navarrese — sibilants retained, /h/ lost, yeísmo (Goizueta 2010)
# ───────────────────────────────────────────────────────────────────────
class TestUpperNavarrese:
    CODE = "eu-x-nafarra-garaia"

    def test_no_unsourced_sibilant_merger(self):
        # The corrected spec must NOT remap the apical/laminal sibilants
        # to a single [s]; the three-way contrast is stable here. The base
        # identity mappings s̺→[s̺], s̻→[s̻] are inherited, but neither may
        # carry a plain [s] merger variant.
        allo = _spec(self.CODE).allophones
        assert "s" not in allo.get("s̺", [])
        assert "s" not in allo.get("s̻", [])
        # base three-way contrast still surfaces in the grapheme map
        g = _spec(self.CODE).graphemes
        assert g["z"] == ["s̻"] and g["s"] == ["s̺"]

    def test_h_lost(self):
        assert _spec(self.CODE).allophones.get("h") == [""]

    def test_yeismo(self):
        assert _spec(self.CODE).allophones.get("ʎ") == ["ʎ", "ʝ"]


# ───────────────────────────────────────────────────────────────────────
# Lower Navarrese — eastern aspiration (Hualde 2018)
# ───────────────────────────────────────────────────────────────────────
class TestLowerNavarrese:
    CODE = "eu-x-nafarra-beherea"

    def test_aspirated_stops(self):
        allo = _spec(self.CODE).allophones
        assert allo.get("p") == ["p", "pʰ"]
        assert allo.get("t") == ["t", "tʰ"]
        assert allo.get("k") == ["k", "kʰ"]

    def test_h_preserved(self):
        assert _spec(self.CODE).allophones.get("h") == ["h"]


# ───────────────────────────────────────────────────────────────────────
# Lapurdian — aspiration receding (Hualde 2018)
# ───────────────────────────────────────────────────────────────────────
class TestLapurdian:
    CODE = "eu-x-lapurtera"

    def test_h_variable(self):
        assert _spec(self.CODE).allophones.get("h") == ["h", ""]

    def test_french_uvular_rhotic(self):
        assert "ʁ" in _spec(self.CODE).allophones.get("r", [])


# ───────────────────────────────────────────────────────────────────────
# Souletin — /y/, aspirated stops, nasal vowels documented (2010/2018/2013)
# ───────────────────────────────────────────────────────────────────────
class TestSouletin:
    CODE = "eu-x-zuberera"

    def test_front_rounded_vowel(self):
        assert _spec(self.CODE).graphemes.get("ü") == ["y"]

    def test_u_umlaut_transcribes_to_y(self):
        assert "y" in G2P(self.CODE).transcribe("üsü")

    def test_aspirated_stops_and_h(self):
        allo = _spec(self.CODE).allophones
        assert allo.get("p") == ["p", "pʰ"]
        assert allo.get("h") == ["h"]

    def test_nasal_vowels_documented(self):
        notes = _spec(self.CODE).notes.lower()
        assert "nasalis" in notes or "nasal" in notes


# ───────────────────────────────────────────────────────────────────────
# Roncalese (new) — Eastern Navarrese, extinct
# ───────────────────────────────────────────────────────────────────────
class TestRoncalese:
    CODE = "eu-x-erronkariera"

    def test_registered_with_parent_eu(self):
        assert _spec(self.CODE).parent == "eu"

    def test_marked_extinct(self):
        assert _spec(self.CODE).timespan.end_year == 1991

    def test_eastern_aspiration(self):
        allo = _spec(self.CODE).allophones
        assert allo.get("p") == ["p", "pʰ"]
        assert allo.get("h") == ["h", ""]

    def test_documents_nasalisation_metaphony_syncope(self):
        notes = _spec(self.CODE).notes.lower()
        assert "nasal" in notes
        assert "metaphony" in notes
        assert "syncope" in notes

    def test_cites_read_sources(self):
        ids = {s.id for s in _spec(self.CODE).sources}
        assert "egurtzegi2013" in ids
        assert "hualde2018_aspiration" in ids


# ───────────────────────────────────────────────────────────────────────
# Ancestry & phonological distance
# ───────────────────────────────────────────────────────────────────────
class TestDistance:
    @pytest.mark.parametrize("code", DIALECTS)
    def test_parent_ancestry_similarity(self, code):
        assert ancestry_similarity(_spec("eu"), _spec(code)) == pytest.approx(0.9)

    def test_siblings_share_grandparent(self):
        sim = ancestry_similarity(_spec("eu-x-bizkaiera"), _spec("eu-x-zuberera"))
        assert sim == pytest.approx(0.81)

    def test_phonological_distance_nonzero_for_diverging_dialects(self):
        # Both diverge from the base; Biscayan via grapheme mergers, Souletin
        # via the added /y/ grapheme and aspiration allophones.
        d_biz = phonological_distance(_spec("eu"), _spec("eu-x-bizkaiera"))
        d_zub = phonological_distance(_spec("eu"), _spec("eu-x-zuberera"))
        assert d_biz.combined > 0.0
        assert d_zub.combined > 0.0
        # the Biscayan sibilant/affricate mergers show up as grapheme divergence
        assert d_biz.grapheme.mean_ipa_distance > 0.0
