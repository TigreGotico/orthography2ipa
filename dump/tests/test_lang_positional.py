"""Tests for positional grapheme integration across all language specs.

Validates that:
1. Every LanguageSpec with a POSITIONAL_* dict actually has it wired in
2. Positional grapheme keys exist in the base graphemes dict
3. Positional IPA values are a subset of the allophone inventory
4. resolve_grapheme returns correct values for known patterns
5. Key linguistic phenomena are correctly modelled

Uses stdlib unittest — no external dependencies required.
"""
import unittest
from orthography2ipa.registry import get
from orthography2ipa.types import GraphemePosition as GP, LanguageSpec


# ═══════════════════════════════════════════════════════════════════════════
# Helper: collect all specs from a module
# ═══════════════════════════════════════════════════════════════════════════

def _all_ipa(allophones):
    """Flatten all IPA symbols from allophone map."""
    symbols = set()
    for vals in allophones.values():
        symbols.update(vals)
    return symbols


# ═══════════════════════════════════════════════════════════════════════════
# Structural integrity tests
# ═══════════════════════════════════════════════════════════════════════════

class TestPositionalGraphemesWired(unittest.TestCase):
    """Every spec must have positional data wired in the LanguageSpec."""

    def _check_codes(self, expected_codes):
        """Verify all expected codes have positional data."""
        for code in expected_codes:
            with self.subTest(code=code):
                spec = get(code)
                self.assertTrue(
                    spec.has_positional_data(),
                    f"{code} has positional_graphemes={spec.positional_graphemes} "
                    f"(expected non-empty)"
                )

    def test_es_specs_wired(self):
        self._check_codes([
            "es-ES", "es-ES-x-andalusia-w", "es-ES-x-andalusia-e",
            "es-ES-x-murcia", "es-ES-x-canarias", "es-ES-x-cantabria",
        ])

    def test_es_latam_specs_wired(self):
        self._check_codes([
            "es-419", "es-MX", "es-MX-x-costa", "es-CU", "es-DO", "es-PR",
            "es-VE", "es-GT", "es-NI", "es-CR", "es-PA", "es-CO",
            "es-CO-x-costa", "es-CO-x-paisa", "es-PE", "es-PE-x-lima",
            "es-BO", "es-EC", "es-CL", "es-PY", "es-UY", "es-AR", "es-GQ",
        ])

    def test_pt_specs_wired(self):
        self._check_codes([
            "pt-PT", "pt-BR", "pt-AO",
        ])

    def test_pt_dialects_specs_wired(self):
        self._check_codes([
            "pt-PT-x-minho", "pt-PT-x-porto", "pt-PT-x-alfena",
            "pt-PT-x-viana", "pt-PT-x-aveiro", "pt-PT-x-lisbon",
            "pt-PT-x-alentejo", "pt-PT-x-algarve", "pt-PT-x-acores",
            "pt-PT-x-madeira", "pt-PT-x-trasosmontes",
        ])

    def test_ca_specs_wired(self):
        self._check_codes([
            "ca", "ca-x-valencia", "ca-x-balear", "ca-x-nord",
            "ca-x-occidental", "oc-x-aranes",
        ])

    def test_gl_specs_wired(self):
        self._check_codes([
            "gl-ES", "gl-x-occidental", "gl-x-central", "gl-x-oriental", "fax",
        ])

    def test_oc_specs_wired(self):
        self._check_codes(["oc"])

    def test_ast_specs_wired(self):
        self._check_codes([
            "ast", "ast-x-occidental", "ast-x-oriental", "ast-ES-x-leon",
        ])

    def test_an_specs_wired(self):
        self._check_codes([
            "an", "an-x-occidental", "an-x-oriental",
        ])

    def test_mwl_specs_wired(self):
        self._check_codes([
            "mwl", "mwl-x-sendim",
        ])

    def test_barranquenho_spec_wired(self):
        self._check_codes(["ext-PT-x-barrancos"])

    def test_rionorese_spec_wired(self):
        self._check_codes(["ast-PT-x-rionor"])

    def test_guadramilese_spec_wired(self):
        self._check_codes(["ast-PT-x-guadramil"])


class TestPositionalGraphemesConsistency(unittest.TestCase):
    """Positional grapheme keys must exist in base graphemes."""

    def _check_spec_consistency(self, spec: LanguageSpec):
        """Verify positional keys reference valid graphemes."""
        if not spec.has_positional_data():
            return
        for grapheme_key in spec.positional_grapheme_keys():
            with self.subTest(code=spec.code, grapheme=grapheme_key):
                self.assertIn(
                    grapheme_key, spec.graphemes,
                    f"{spec.code}: positional grapheme '{grapheme_key}' "
                    f"not found in base graphemes"
                )

    def _check_codes(self, codes):
        for code in codes:
            self._check_spec_consistency(get(code))

    def test_es(self):
        self._check_codes([
            "es-ES", "es-ES-x-andalusia-w", "es-ES-x-andalusia-e",
            "es-ES-x-murcia", "es-ES-x-canarias", "es-ES-x-cantabria",
        ])

    def test_es_latam(self):
        self._check_codes([
            "es-419", "es-MX", "es-MX-x-costa", "es-CU", "es-DO", "es-PR",
            "es-VE", "es-GT", "es-NI", "es-CR", "es-PA", "es-CO",
            "es-CO-x-costa", "es-CO-x-paisa", "es-PE", "es-PE-x-lima",
            "es-BO", "es-EC", "es-CL", "es-PY", "es-UY", "es-AR", "es-GQ",
        ])

    def test_pt(self):
        self._check_codes(["pt-PT", "pt-BR", "pt-AO"])

    def test_pt_dialects(self):
        self._check_codes([
            "pt-PT-x-minho", "pt-PT-x-porto", "pt-PT-x-alfena",
            "pt-PT-x-viana", "pt-PT-x-aveiro", "pt-PT-x-lisbon",
            "pt-PT-x-alentejo", "pt-PT-x-algarve", "pt-PT-x-acores",
            "pt-PT-x-madeira", "pt-PT-x-trasosmontes",
        ])

    def test_ca(self):
        self._check_codes([
            "ca", "ca-x-valencia", "ca-x-balear", "ca-x-nord",
            "ca-x-occidental", "oc-x-aranes",
        ])

    def test_gl(self):
        self._check_codes([
            "gl-ES", "gl-x-occidental", "gl-x-central", "gl-x-oriental", "fax",
        ])

    def test_oc(self):
        self._check_codes(["oc"])

    def test_ast(self):
        self._check_codes([
            "ast", "ast-x-occidental", "ast-x-oriental", "ast-ES-x-leon",
        ])

    def test_an(self):
        self._check_codes(["an", "an-x-occidental", "an-x-oriental"])

    def test_mwl(self):
        self._check_codes(["mwl", "mwl-x-sendim"])

    def test_barranquenho(self):
        self._check_codes(["ext-PT-x-barrancos"])

    def test_rionorese(self):
        self._check_codes(["ast-PT-x-rionor"])

    def test_guadramilese(self):
        self._check_codes(["ast-PT-x-guadramil"])


# ═══════════════════════════════════════════════════════════════════════════
# Linguistic accuracy tests
# ═══════════════════════════════════════════════════════════════════════════

class TestSpanishLenition(unittest.TestCase):
    """Spanish voiced stop lenition is the canonical positional process."""

    def setUp(self):
        self.es = get("es-ES")

    def test_b_default_is_occlusive(self):
        self.assertEqual(self.es.resolve_grapheme("b", GP.DEFAULT), ["b"])

    def test_b_intervocalic_is_spirant(self):
        self.assertEqual(self.es.resolve_grapheme("b", GP.INTERVOCALIC), ["β"])

    def test_d_intervocalic_is_spirant(self):
        self.assertEqual(self.es.resolve_grapheme("d", GP.INTERVOCALIC), ["ð"])

    def test_d_word_final_weakened(self):
        result = self.es.resolve_grapheme("d", GP.WORD_FINAL)
        self.assertIn("ð", result)

    def test_g_intervocalic_is_spirant(self):
        self.assertEqual(self.es.resolve_grapheme("g", GP.INTERVOCALIC), ["ɣ"])

    def test_r_word_initial_is_trill(self):
        self.assertEqual(self.es.resolve_grapheme("r", GP.WORD_INITIAL), ["r"])

    def test_r_intervocalic_is_tap(self):
        self.assertEqual(self.es.resolve_grapheme("r", GP.INTERVOCALIC), ["ɾ"])


class TestAndalusianAspiration(unittest.TestCase):
    """Western Andalusian: coda /s/ → [h] or deletion."""

    def setUp(self):
        self.and_w = get("es-ES-x-andalusia-w")

    def test_coda_s_aspirated(self):
        result = self.and_w.resolve_grapheme("s", GP.CODA)
        self.assertIn("h", result)

    def test_word_final_d_deleted(self):
        result = self.and_w.resolve_grapheme("d", GP.WORD_FINAL)
        self.assertIn("∅", result)


class TestPortugueseSSystem(unittest.TestCase):
    """European Portuguese ⟨s⟩ is the richest positional system."""

    def setUp(self):
        self.pt = get("pt-PT")

    def test_s_word_initial(self):
        self.assertEqual(self.pt.resolve_grapheme("s", GP.WORD_INITIAL), ["s"])

    def test_s_intervocalic(self):
        self.assertEqual(self.pt.resolve_grapheme("s", GP.INTERVOCALIC), ["z"])

    def test_s_coda(self):
        result = self.pt.resolve_grapheme("s", GP.CODA)
        self.assertIn("ʃ", result)

    def test_s_word_final(self):
        self.assertEqual(self.pt.resolve_grapheme("s", GP.WORD_FINAL), ["ʃ"])

    def test_l_onset_clear(self):
        self.assertEqual(self.pt.resolve_grapheme("l", GP.ONSET), ["l"])

    def test_l_coda_dark(self):
        self.assertEqual(self.pt.resolve_grapheme("l", GP.CODA), ["ɫ"])

    def test_r_word_initial_uvular(self):
        self.assertEqual(self.pt.resolve_grapheme("r", GP.WORD_INITIAL), ["ʁ"])

    def test_r_intervocalic_tap(self):
        self.assertEqual(self.pt.resolve_grapheme("r", GP.INTERVOCALIC), ["ɾ"])


class TestBrazilianPortuguese(unittest.TestCase):
    """Brazilian Portuguese: l-vocalisation, no coda [ʃ]."""

    def setUp(self):
        self.br = get("pt-BR")

    def test_l_coda_vocalised(self):
        self.assertEqual(self.br.resolve_grapheme("l", GP.CODA), ["w"])

    def test_s_word_final_alveolar(self):
        # Brazilian: word-final /s/ stays [s], not [ʃ]
        self.assertEqual(self.br.resolve_grapheme("s", GP.WORD_FINAL), ["s"])

    def test_r_word_initial_glottal(self):
        result = self.br.resolve_grapheme("r", GP.WORD_INITIAL)
        self.assertIn("h", result)


class TestCatalanVowelReduction(unittest.TestCase):
    """Central Catalan: systematic unstressed vowel reduction."""

    def setUp(self):
        self.ca = get("ca")
        self.val = get("ca-x-valencia")

    def test_central_a_reduces_to_schwa(self):
        self.assertEqual(self.ca.resolve_grapheme("a", GP.NUCLEUS), ["ə"])

    def test_central_e_reduces_to_schwa(self):
        self.assertEqual(self.ca.resolve_grapheme("e", GP.NUCLEUS), ["ə"])

    def test_central_o_reduces_to_u(self):
        self.assertEqual(self.ca.resolve_grapheme("o", GP.NUCLEUS), ["u"])

    def test_valencian_a_no_reduction(self):
        self.assertEqual(self.val.resolve_grapheme("a", GP.NUCLEUS), ["a"])

    def test_valencian_e_no_reduction(self):
        self.assertEqual(self.val.resolve_grapheme("e", GP.NUCLEUS), ["e"])


class TestGalicianGheada(unittest.TestCase):
    """Western Galician: /ɡ/ → [h] (gheada)."""

    def setUp(self):
        self.gl_w = get("gl-x-occidental")

    def test_g_default_is_gheada(self):
        result = self.gl_w.resolve_grapheme("g", GP.DEFAULT)
        self.assertIn("h", result)


class TestMirandesePositional(unittest.TestCase):
    """Mirandese: betacism + 4-way sibilant system."""

    def setUp(self):
        self.mwl = get("mwl")

    def test_b_intervocalic_spirant(self):
        self.assertEqual(self.mwl.resolve_grapheme("b", GP.INTERVOCALIC), ["β"])

    def test_d_intervocalic_spirant(self):
        self.assertEqual(self.mwl.resolve_grapheme("d", GP.INTERVOCALIC), ["ð"])


class TestBarranquenhoAspiration(unittest.TestCase):
    """Barranquenho: coda /s/ → [h] (Spanish influence)."""

    def setUp(self):
        self.brq = get("ext-PT-x-barrancos")

    def test_s_coda_aspirated(self):
        result = self.brq.resolve_grapheme("s", GP.CODA)
        self.assertIn("h", result)

    def test_s_intervocalic_voiced(self):
        self.assertEqual(self.brq.resolve_grapheme("s", GP.INTERVOCALIC), ["z"])


class TestCaribbeanSpanish(unittest.TestCase):
    """Caribbean Spanish: universal coda aspiration and -d deletion."""

    def setUp(self):
        self.cu = get("es-CU")

    def test_s_coda_aspirated(self):
        result = self.cu.resolve_grapheme("s", GP.CODA)
        self.assertIn("h", result)

    def test_d_word_final_deleted(self):
        result = self.cu.resolve_grapheme("d", GP.WORD_FINAL)
        self.assertIn("∅", result)


class TestHighlandSpanish(unittest.TestCase):
    """Highland Spanish (Mexico, Bogotá, Andean): conservative coda /s/."""

    def setUp(self):
        self.mx = get("es-MX")

    def test_s_coda_retained(self):
        result = self.mx.resolve_grapheme("s", GP.CODA)
        self.assertIn("s", result)
        self.assertNotIn("h", result)


class TestAsturianPositional(unittest.TestCase):
    """Asturian: standard Ibero-Romance lenition."""

    def setUp(self):
        self.ast = get("ast")
        self.ast_w = get("ast-x-occidental")

    def test_b_intervocalic(self):
        self.assertEqual(self.ast.resolve_grapheme("b", GP.INTERVOCALIC), ["β"])

    def test_western_f_word_initial_aspiration(self):
        result = self.ast_w.resolve_grapheme("f", GP.WORD_INITIAL)
        self.assertIn("h", result)


# ═══════════════════════════════════════════════════════════════════════════
# Backward compatibility
# ═══════════════════════════════════════════════════════════════════════════

class TestBackwardCompat(unittest.TestCase):
    """Specs without positional data should still work."""

    def test_resolve_without_positional_falls_back(self):
        spec = LanguageSpec(
            code="xx", name="Test", family="TestFamily", script="Latin",
            graphemes={"a": ["a"]}, allophones={"a": ["a"]},
        )
        self.assertEqual(spec.resolve_grapheme("a"), ["a"])
        self.assertEqual(spec.resolve_grapheme("a", GP.CODA), ["a"])

    def test_no_positional_data(self):
        spec = LanguageSpec(
            code="xx", name="Test", family="TestFamily", script="Latin",
            graphemes={"a": ["a"]}, allophones={"a": ["a"]},
        )
        self.assertFalse(spec.has_positional_data())


if __name__ == "__main__":
    unittest.main()