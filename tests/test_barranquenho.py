"""Barranquenho (ext-PT-x-barrancos) — contact-variety allophony.

Barranquenho is a Portuguese–Spanish contact variety (Alentejo Portuguese
base + Extremaduran/Andalusian Spanish adstrate). It inherits pt-PT via
graphemes_base/allophones_base/positional_graphemes_base, so the European
Portuguese post-lexical allophone_rules (the Lisbon 'chiado' coda sibilants
[ʃ ʒ] and the dark coda [ɫ]) are inherited by OVERLAY_BY_ID. This spec must
OVERRIDE those rules by id: coda /s z/ aspirate to [h] (Andalusian-type,
never [ʃ]/[ʒ]) and coda /l/ stays clear.

Sources: Navas Sánchez-Élez (2011), *El barranqueño: un modelo de lenguas en
contacto*; Clements, Amaral & Luís (2008), BLS 34:13–22; Convenção
Ortográfica do Barranquenho (2025).
"""

import pytest

import orthography2ipa
from orthography2ipa.g2p import G2P


@pytest.fixture(scope="module")
def barrancos():
    return orthography2ipa.get("ext-PT-x-barrancos")


@pytest.fixture(scope="module")
def g2p():
    return G2P("ext-PT-x-barrancos")


def _rule(spec, rule_id):
    for r in spec.allophone_rules:
        if r.id == rule_id:
            return r
    return None


class TestInheritedEPRulesOverridden:
    """The three inherited European Portuguese allophone rules are redeclared
    (OVERLAY_BY_ID replaces them in place) so the EP chiado / dark-l are gone."""

    def test_coda_s_rule_overridden_to_aspiration(self, barrancos):
        r = _rule(barrancos, "PT_CODA_S_HUSH")
        assert r is not None, "inherited coda-/s/ rule id must remain (redeclared)"
        assert r.phonemes == ("s",)
        assert r.syllable_position == "coda"
        assert r.surface == "h", "coda /s/ must aspirate to [h], NOT the EP chiado [ʃ]"
        assert r.surface != "ʃ"

    def test_coda_z_rule_overridden_to_aspiration(self, barrancos):
        r = _rule(barrancos, "PT_CODA_Z_HUSH")
        assert r is not None
        assert r.surface == "h", "coda /z/ must aspirate to [h], NOT [ʒ]"
        assert r.surface != "ʒ"

    def test_coda_l_dark_neutralised(self, barrancos):
        r = _rule(barrancos, "PT_CODA_L_DARK")
        assert r is not None
        assert r.surface == "l", "coda /l/ stays clear [l], NOT velarised [ɫ]"
        assert r.surface != "ɫ"

    def test_no_rule_emits_chiado_or_dark_l(self, barrancos):
        surfaces = {r.surface for r in barrancos.allophone_rules}
        assert "ʃ" not in surfaces
        assert "ʒ" not in surfaces
        assert "ɫ" not in surfaces


class TestCodaSAspiration:
    """Coda /s/ → [h] (Andalusian-type), never the EP chiado [ʃ]."""

    @pytest.mark.parametrize(
        "word,frag",
        [("mesmo", "h"), ("visto", "h"), ("festa", "h"), ("isto", "h"),
         ("bastante", "h")],
    )
    def test_internal_coda_s_aspirates(self, g2p, word, frag):
        out = g2p.transcribe(word)
        assert frag in out, f"{word} -> {out} should contain aspirate [h]"

    @pytest.mark.parametrize("word", ["mesmo", "visto", "festa", "isto", "bastante"])
    def test_no_chiado_in_coda(self, g2p, word):
        out = g2p.transcribe(word)
        assert "ʃ" not in out, f"{word} -> {out} must NOT show EP chiado [ʃ]"
        assert "ʒ" not in out


class TestBetacism:
    """/v/ merged with /b/ (betacism, shared with Spanish + Northern PT)."""

    def test_v_grapheme_maps_to_b(self, barrancos):
        assert barrancos.graphemes.get("v") == ["b"]

    def test_v_phoneme_absent(self, barrancos):
        assert barrancos.allophones.get("v") is None

    @pytest.mark.parametrize("word", ["vaca", "visto", "vida"])
    def test_v_realised_as_b(self, g2p, word):
        out = g2p.transcribe(word)
        assert "b" in out and "v" not in out, f"{word} -> {out}"


class TestFinalConsonantWeakening:
    """Word-final /r/, /l/, /s/ delete (contact feature)."""

    @pytest.mark.parametrize("word", ["cantar", "senhor", "dotor"])
    def test_final_r_deleted(self, g2p, word):
        out = g2p.transcribe(word)
        assert not out.rstrip("ˈˌ").endswith("ɾ") and not out.endswith("r"), \
            f"final -r must delete: {word} -> {out}"

    @pytest.mark.parametrize("word", ["Brasil", "Natal", "Isabel"])
    def test_final_l_deleted(self, g2p, word):
        out = g2p.transcribe(word)
        assert not out.endswith("l") and not out.endswith("ɫ"), \
            f"final -l must delete: {word} -> {out}"

    def test_no_dark_l_ever(self, g2p):
        for word in ["Brasil", "alto", "mal", "sal"]:
            assert "ɫ" not in g2p.transcribe(word)


class TestWholeWords:
    """A few whole-word transcriptions grounded in the cited sources."""

    @pytest.mark.parametrize(
        "word,expected",
        [
            ("mesmo", "ˈmɛhmu"),   # coda s -> [h]; final -o raised to [u]
            ("visto", "ˈbihtu"),   # betacism + coda-s aspiration
            ("vaca", "ˈbakɐ"),     # betacism
            ("cantar", "ˈkantɐ"),  # final -r deleted
            ("Brasil", "ˈbɾazi"),  # final -l deleted
        ],
    )
    def test_word(self, g2p, word, expected):
        assert g2p.transcribe(word) == expected


class TestSeseoNoInterdental:
    """Seseo-like: no Castilian /θ/ distinción is introduced."""

    def test_no_theta_in_inventory(self, barrancos):
        for ipas in barrancos.graphemes.values():
            if ipas:
                assert "θ" not in ipas
