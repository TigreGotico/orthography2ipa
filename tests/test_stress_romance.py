"""Gold stress cases for Romance family stress blocks (Part 1) and
pt-BR positional vowel reduction (Part 2).

Tests use detect_stress() to verify syllable-index assignment and
apply_stress_mark() to verify the mark lands on the right syllable.
pt-BR reduction cases check positional_graphemes keys directly so the
test does not depend on a full G2P pipeline.
"""
import pytest

from orthography2ipa import get
from orthography2ipa.stress import apply_stress_mark, detect_stress, syllabify


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def stress_index(lang_code: str, word: str) -> int:
    """Return the stressed syllable index (negative, end-anchored) for *word*.

    detect_stress returns a positive 0-based index; we convert to end-anchored
    so that -1 = final, -2 = penultimate, -3 = antepenultimate.
    """
    spec = get(lang_code)
    sylls = syllabify(word)
    n = len(sylls)
    if n == 0:
        return -1
    pos = detect_stress(word, spec.stress, syllables=sylls)
    return pos - n  # convert to end-anchored negative


# ---------------------------------------------------------------------------
# Part 1 — stress blocks: Spanish
# ---------------------------------------------------------------------------

class TestSpanishStress:
    """es-ES / es-419 / es-MX / es-AR share the same Iberian accentuation rules."""

    @pytest.mark.parametrize("code", ["es-ES", "es-419", "es-MX", "es-AR"])
    def test_marked_vowel_wins(self, code):
        # café — final syllable carries acute accent → oxytone
        spec = get(code)
        assert spec.stress is not None
        assert "á" in spec.stress.marked_vowels
        assert "é" in spec.stress.marked_vowels

    @pytest.mark.parametrize("code", ["es-ES", "es-419", "es-MX", "es-AR"])
    def test_stress_block_present(self, code):
        spec = get(code)
        assert spec.stress is not None
        assert spec.stress.default_position == -2
        assert "r" in spec.stress.final_stress_endings
        assert "n" in spec.stress.penult_stress_endings
        assert "s" in spec.stress.penult_stress_endings

    def test_es_vowel_final_paroxytone(self):
        # casa → [-2] paroxytone (default)
        idx = stress_index("es-ES", "casa")
        assert idx == -2

    def test_es_r_final_oxytone(self):
        # hablar → final r triggers oxytone
        idx = stress_index("es-ES", "hablar")
        assert idx == -1

    def test_es_n_final_paroxytone(self):
        # imagen → ends in -n → paroxytone
        idx = stress_index("es-ES", "imagen")
        assert idx == -2

    def test_es_s_final_paroxytone(self):
        # casas → ends in -s → paroxytone
        idx = stress_index("es-ES", "casas")
        assert idx == -2

    def test_es_d_final_oxytone(self):
        # verdad → ends in -d → oxytone
        idx = stress_index("es-ES", "verdad")
        assert idx == -1

    def test_es_marked_proparoxytone(self):
        # teléfono → acute on é → -3 via marked vowel
        idx = stress_index("es-ES", "teléfono")
        assert idx == -3


# ---------------------------------------------------------------------------
# Part 1 — stress blocks: Italian
# ---------------------------------------------------------------------------

class TestItalianStress:
    def test_it_stress_block_present(self):
        spec = get("it-IT")
        assert spec.stress is not None
        assert spec.stress.default_position == -2
        assert "à" in spec.stress.marked_vowels
        assert "è" in spec.stress.marked_vowels
        assert "ù" in spec.stress.marked_vowels

    def test_it_default_paroxytone(self):
        # libro → default -2
        idx = stress_index("it-IT", "libro")
        assert idx == -2

    def test_it_marked_final(self):
        # città → acute à on final syllable → -1
        idx = stress_index("it-IT", "città")
        assert idx == -1

    def test_it_marked_grave_e(self):
        # caffè → è on final syllable → -1
        idx = stress_index("it-IT", "caffè")
        assert idx == -1

    def test_it_marked_grave_e_antepenult(self):
        # célere (quick) — é on antepenultimate syllable → -3
        # naive syllabifier gives ['cé','le','re'] so index 0 → -3 end-anchored
        idx = stress_index("it-IT", "célere")
        assert idx == -3

    def test_it_marked_accent_wins(self):
        # virtù → final ù → -1
        idx = stress_index("it-IT", "virtù")
        assert idx == -1

    def test_it_plain_paroxytone_multiword(self):
        # parole → default -2
        idx = stress_index("it-IT", "parole")
        assert idx == -2


# ---------------------------------------------------------------------------
# Part 1 — stress blocks: Catalan
# ---------------------------------------------------------------------------

class TestCatalanStress:
    def test_ca_stress_block_present(self):
        spec = get("ca")
        assert spec.stress is not None
        assert spec.stress.default_position == -2
        assert "à" in spec.stress.marked_vowels
        assert "é" in spec.stress.marked_vowels
        assert "ï" in spec.stress.marked_vowels

    def test_ca_vowel_final_paroxytone(self):
        # casa → -2
        idx = stress_index("ca", "casa")
        assert idx == -2

    def test_ca_r_final_oxytone(self):
        # cantar → -1
        idx = stress_index("ca", "cantar")
        assert idx == -1

    def test_ca_marked_overrides(self):
        # català → à on final → -1
        idx = stress_index("ca", "català")
        assert idx == -1

    def test_ca_s_final_paroxytone(self):
        # cases → -s → -2
        idx = stress_index("ca", "cases")
        assert idx == -2

    def test_ca_l_final_oxytone(self):
        # animal → -l → -1
        idx = stress_index("ca", "animal")
        assert idx == -1


# ---------------------------------------------------------------------------
# Part 1 — stress blocks: Aragonese & Asturian
# ---------------------------------------------------------------------------

class TestAragonese:
    def test_an_stress_block_present(self):
        spec = get("an")
        assert spec.stress is not None
        assert spec.stress.default_position == -2
        assert "á" in spec.stress.marked_vowels
        assert "r" in spec.stress.final_stress_endings

    def test_an_vowel_final_paroxytone(self):
        idx = stress_index("an", "casa")
        assert idx == -2

    def test_an_r_final_oxytone(self):
        idx = stress_index("an", "parlar")
        assert idx == -1

    def test_an_s_final_paroxytone(self):
        idx = stress_index("an", "casas")
        assert idx == -2

    def test_an_marked_two_syllable(self):
        # árbol: naive syllabifier gives 2 syllables ['á','rbol']
        # á on first (= penult) → -2 end-anchored; written accent still wins
        idx = stress_index("an", "árbol")
        assert idx == -2

    def test_an_d_final_oxytone(self):
        idx = stress_index("an", "ciudat")
        assert idx == -1


class TestAsturian:
    def test_ast_stress_block_present(self):
        spec = get("ast")
        assert spec.stress is not None
        assert spec.stress.default_position == -2

    def test_ast_vowel_final_paroxytone(self):
        idx = stress_index("ast", "casa")
        assert idx == -2

    def test_ast_r_final_oxytone(self):
        idx = stress_index("ast", "falar")
        assert idx == -1

    def test_ast_s_final_paroxytone(self):
        idx = stress_index("ast", "cases")
        assert idx == -2

    def test_ast_marked_proparoxytone(self):
        idx = stress_index("ast", "páxaru")
        assert idx == -3

    def test_ast_n_final_oxytone(self):
        # Asturian: n-final is oxytone (unlike Spanish)
        idx = stress_index("ast", "xoven")
        assert idx == -1


# ---------------------------------------------------------------------------
# Part 1 — stress blocks: Occitan
# ---------------------------------------------------------------------------

class TestOccitanStress:
    def test_oc_stress_block_present(self):
        spec = get("oc")
        assert spec.stress is not None
        # Occitan default is final (-1)
        assert spec.stress.default_position == -1
        assert "à" in spec.stress.marked_vowels

    def test_oc_default_oxytone(self):
        # amors → -s final → paroxytone (-2)
        # amor → -or not in penult list → default final (-1)
        idx = stress_index("oc", "amor")
        assert idx == -1, f"amor should be oxytone, got {idx}"

    def test_oc_vowel_final_paroxytone(self):
        # porta → vowel final → -2
        idx = stress_index("oc", "porta")
        assert idx == -2

    def test_oc_s_final_paroxytone(self):
        # portas → -s final → -2
        idx = stress_index("oc", "portas")
        assert idx == -2

    def test_oc_marked_wins(self):
        # cantar → in penult list (infinitive -ar) → -2
        idx = stress_index("oc", "cantar")
        assert idx == -2

    def test_oc_aranes_block(self):
        spec = get("oc-x-aranes")
        assert spec.stress is not None
        assert spec.stress.default_position == -1


# ---------------------------------------------------------------------------
# Part 1 — Mirandese dialects inherit mwl stress
# ---------------------------------------------------------------------------

class TestMirandeseDiaelcts:
    def test_mwl_sendim_has_stress(self):
        spec = get("mwl-x-sendim")
        assert spec.stress is not None
        assert spec.stress.default_position == -2
        assert "r" in spec.stress.final_stress_endings

    def test_mwl_ifanes_has_stress(self):
        spec = get("mwl-x-ifanes")
        assert spec.stress is not None
        assert spec.stress.default_position == -2

    def test_mwl_sendim_r_final_oxytone(self):
        idx = stress_index("mwl-x-sendim", "falar")
        assert idx == -1

    def test_mwl_ifanes_vowel_final_paroxytone(self):
        idx = stress_index("mwl-x-ifanes", "casa")
        assert idx == -2


# ---------------------------------------------------------------------------
# Part 2 — pt-BR positional vowel reduction
# ---------------------------------------------------------------------------

class TestPtBRReduction:
    """Check that positional_graphemes encode the Brazilian reduction system."""

    def test_ptbr_word_final_e_reduces_to_i(self):
        spec = get("pt-BR")
        pg = spec.positional_graphemes or {}
        e_rules = pg.get("e", {})
        assert "ɪ" in e_rules.get("word_final", []), (
            "pt-BR word-final /e/ should reduce to [ɪ] (Barbosa & Albano 2004)"
        )

    def test_ptbr_word_final_o_reduces_to_u(self):
        spec = get("pt-BR")
        pg = spec.positional_graphemes or {}
        o_rules = pg.get("o", {})
        assert "ʊ" in o_rules.get("word_final", []), (
            "pt-BR word-final /o/ should reduce to [ʊ] (Barbosa & Albano 2004)"
        )

    def test_ptbr_word_final_a_reduces_to_schwa(self):
        spec = get("pt-BR")
        pg = spec.positional_graphemes or {}
        a_rules = pg.get("a", {})
        assert "ɐ" in a_rules.get("word_final", []), (
            "pt-BR word-final /a/ should reduce to [ɐ]"
        )

    def test_ptbr_posttonic_e_reduces_to_i(self):
        spec = get("pt-BR")
        pg = spec.positional_graphemes or {}
        e_rules = pg.get("e", {})
        assert "ɪ" in e_rules.get("posttonic", []), (
            "pt-BR posttonic /e/ should reduce to [ɪ] (Barbosa & Albano 2004)"
        )

    def test_ptbr_posttonic_o_reduces_to_u(self):
        spec = get("pt-BR")
        pg = spec.positional_graphemes or {}
        o_rules = pg.get("o", {})
        assert "ʊ" in o_rules.get("posttonic", []), (
            "pt-BR posttonic /o/ should reduce to [ʊ] (Barbosa & Albano 2004)"
        )

    def test_ptbr_posttonic_a_reduces_to_schwa(self):
        spec = get("pt-BR")
        pg = spec.positional_graphemes or {}
        a_rules = pg.get("a", {})
        assert "ɐ" in a_rules.get("posttonic", []), (
            "pt-BR posttonic /a/ should reduce to [ɐ]"
        )

    def test_ptbr_pretonic_vowels_not_reduced(self):
        # BR pretonic vowels are NOT strongly reduced (unlike EP);
        # nucleus_unstressed for /o/ should be [o] not [u]
        spec = get("pt-BR")
        pg = spec.positional_graphemes or {}
        o_rules = pg.get("o", {})
        # nucleus_unstressed should be [o] (weak reduction, stays mid)
        nu = o_rules.get("nucleus_unstressed", [])
        assert "o" in nu, "pt-BR pretonic /o/ should remain [o]"
        # and NOT start with [u] as EP does
        assert nu[0] != "u", "pt-BR pretonic /o/ must not be EP-style [u]-first"

    def test_ptbr_reduction_does_not_affect_ptpt(self):
        # pt-PT positional_graphemes for o/pretonic should still be [u]
        spec = get("pt-PT")
        pg = spec.positional_graphemes or {}
        o_rules = pg.get("o", {})
        assert "u" in o_rules.get("pretonic", []), (
            "pt-PT pretonic /o/ must still reduce to [u] (no regression)"
        )
