"""Tests for Mirandese (mwl) — linguistic accuracy and structural integrity.

Validates the Mirandese LanguageSpec against the Cumbençon Ourtográfica
da Lhéngua Mirandesa (1999) and phonological descriptions.

Tests cover:
1. Structural integrity (all required fields, types, ancestry chain)
2. Sibilant system (4-way contrast — hallmark feature)
3. Leonese diphthongs (iê/uô from Latin Ĕ/Ŏ)
4. L-palatalization (lh- initial)
5. Betacism (no /v/ phoneme)
6. Positional graphemes (lenition, rhotics, sibilant voicing)
7. Vowel system (7 oral + 5 nasal + centralised ɨ)
8. Consonant digraphs
9. Sendinês and Ifanês subdialect differences
10. Cross-dialectal consistency
"""
import unittest
import sys
import os

# Add working directory to path so we can import the module
sys.path.insert(0, "/home/claude")

from orthography2ipa.languages.mwl import (
    GRAPHEMES_MWL, ALLOPHONES_MWL, POSITIONAL_MWL,
    GRAPHEMES_MWL_SENDIM, ALLOPHONES_MWL_SENDIM,
    GRAPHEMES_MWL_IFANES,
    SPECS,
)
from orthography2ipa.types import GraphemePosition as GP, AncestorRole


# ═══════════════════════════════════════════════════════════════════════════
# Helper utilities
# ═══════════════════════════════════════════════════════════════════════════

def _all_ipa_from_graphemes(graphemes):
    """Collect all IPA symbols appearing in a grapheme dict."""
    symbols = set()
    for vals in graphemes.values():
        symbols.update(vals)
    symbols.discard("")  # silent h
    return symbols


def _all_ipa_from_allophones(allophones):
    """Collect all IPA symbols appearing in an allophone dict."""
    symbols = set()
    for vals in allophones.values():
        symbols.update(vals)
    return symbols


# ═══════════════════════════════════════════════════════════════════════════
# 1. Structural integrity
# ═══════════════════════════════════════════════════════════════════════════

class TestMirandeseStructuralIntegrity(unittest.TestCase):
    """Verify all specs have required fields and correct types."""

    def test_all_expected_codes_present(self):
        """SPECS must contain mwl, mwl-x-sendim, mwl-x-ifanes."""
        self.assertIn("mwl", SPECS)
        self.assertIn("mwl-x-sendim", SPECS)
        self.assertIn("mwl-x-ifanes", SPECS)

    def test_mwl_required_fields(self):
        """Standard Mirandese has all required LanguageSpec fields."""
        mwl = SPECS["mwl"]
        self.assertEqual(mwl.code, "mwl")
        self.assertEqual(mwl.name, "Mirandese")
        self.assertEqual(mwl.family, "Asturleonese")
        self.assertEqual(mwl.script, "Latin")
        self.assertIsInstance(mwl.graphemes, dict)
        self.assertIsInstance(mwl.allophones, dict)
        self.assertIsNotNone(mwl.notes)
        self.assertTrue(len(mwl.notes) > 0)

    def test_grapheme_values_are_lists_of_strings(self):
        """Every grapheme mapping must be list[str]."""
        for key, vals in GRAPHEMES_MWL.items():
            with self.subTest(grapheme=key):
                self.assertIsInstance(vals, list, f"grapheme '{key}' value is not a list")
                for v in vals:
                    self.assertIsInstance(v, str, f"grapheme '{key}' contains non-string: {v}")

    def test_allophone_values_are_lists_of_strings(self):
        """Every allophone mapping must be list[str]."""
        for key, vals in ALLOPHONES_MWL.items():
            with self.subTest(phoneme=key):
                self.assertIsInstance(vals, list, f"allophone '{key}' value is not a list")
                for v in vals:
                    self.assertIsInstance(v, str, f"allophone '{key}' contains non-string: {v}")

    def test_no_empty_grapheme_lists(self):
        """No grapheme should map to an empty list (except silent h)."""
        for key, vals in GRAPHEMES_MWL.items():
            with self.subTest(grapheme=key):
                if key != "h":
                    self.assertTrue(len(vals) > 0,
                                    f"grapheme '{key}' maps to empty list")

    def test_silent_h(self):
        """⟨h⟩ should map to empty string (silent)."""
        self.assertIn("h", GRAPHEMES_MWL)
        self.assertEqual(GRAPHEMES_MWL["h"], [""])

    def test_positional_graphemes_keys_exist_in_base(self):
        """Every positional grapheme key must exist in base graphemes."""
        for key in POSITIONAL_MWL:
            with self.subTest(grapheme=key):
                self.assertIn(key, GRAPHEMES_MWL,
                              f"positional grapheme '{key}' not in base graphemes")


# ═══════════════════════════════════════════════════════════════════════════
# 2. Ancestry chain
# ═══════════════════════════════════════════════════════════════════════════

class TestMirandeseAncestry(unittest.TestCase):
    """Verify ancestry chain is linguistically correct."""

    def setUp(self):
        self.mwl = SPECS["mwl"]

    def test_parent_is_leonese(self):
        """Mirandese descends from Leonese, not directly from Latin."""
        self.assertEqual(self.mwl.parent, "ast-ES-x-leon")

    def test_ancestors_populated(self):
        """Ancestors tuple must be non-empty."""
        self.assertTrue(len(self.mwl.ancestors) > 0)

    def test_has_parent_ancestor(self):
        """Must have at least one PARENT ancestor."""
        parent_ancestors = [a for a in self.mwl.ancestors
                            if a.role == AncestorRole.PARENT]
        self.assertTrue(len(parent_ancestors) > 0,
                        "No PARENT ancestor found")

    def test_leonese_is_primary_parent(self):
        """ast-ES-x-leon should be the primary parent ancestor."""
        parent_ancestors = [a for a in self.mwl.ancestors
                            if a.role == AncestorRole.PARENT]
        codes = [a.code for a in parent_ancestors]
        self.assertIn("ast-ES-x-leon", codes)

    def test_portuguese_adstrate(self):
        """Portuguese should be listed as an adstrate (contact language)."""
        adstrate_codes = [a.code for a in self.mwl.ancestors
                          if a.role == AncestorRole.ADSTRATE]
        # Portuguese contact is a defining feature of modern Mirandese
        self.assertTrue(
            any("pt" in code for code in adstrate_codes),
            f"Portuguese not found in adstrate codes: {adstrate_codes}"
        )

    def test_ancestry_weights_sum_reasonable(self):
        """Ancestry weights should sum to approximately 1.0."""
        total = sum(a.weight for a in self.mwl.ancestors)
        self.assertAlmostEqual(total, 1.0, delta=0.1,
                               msg=f"Ancestry weights sum to {total}, expected ~1.0")

    def test_sendim_parent_is_mwl(self):
        """Sendinês must have mwl as parent."""
        self.assertEqual(SPECS["mwl-x-sendim"].parent, "mwl")

    def test_ifanes_parent_is_mwl(self):
        """Ifanês must have mwl as parent."""
        self.assertEqual(SPECS["mwl-x-ifanes"].parent, "mwl")


# ═══════════════════════════════════════════════════════════════════════════
# 3. Four-way sibilant system
# ═══════════════════════════════════════════════════════════════════════════

class TestMirandeseSibilants(unittest.TestCase):
    """Validate the distinctive 4-way sibilant contrast.

    Per the Convenção (p.16) and Atlas Linguistique Roman:
    - Apical voiceless [s̺]: ⟨s⟩ initial/coda, ⟨ss⟩ intervocalic
    - Apical voiced [z̺]: ⟨s⟩ intervocalic
    - Predorsal voiceless [s̻]: ⟨ç⟩, ⟨c⟩ before e/i
    - Predorsal voiced [z̻]: ⟨z⟩
    """

    def test_s_grapheme_maps_to_apical(self):
        """⟨s⟩ should map to apical sibilants [s̺] and [z̺]."""
        s_ipa = GRAPHEMES_MWL["s"]
        self.assertIn("s̺", s_ipa, "⟨s⟩ must include apical voiceless [s̺]")
        self.assertIn("z̺", s_ipa, "⟨s⟩ must include apical voiced [z̺]")

    def test_ss_grapheme_maps_to_voiceless_apical(self):
        """⟨ss⟩ should map to voiceless apical [s̺] only."""
        ss_ipa = GRAPHEMES_MWL["ss"]
        self.assertEqual(ss_ipa, ["s̺"],
                         "⟨ss⟩ must map to voiceless apical [s̺] only")

    def test_c_cedilla_maps_to_predorsal(self):
        """⟨ç⟩ should map to predorsal voiceless [s̻]."""
        c_ipa = GRAPHEMES_MWL["ç"]
        self.assertEqual(c_ipa, ["s̻"],
                         "⟨ç⟩ must map to predorsal voiceless [s̻]")

    def test_z_grapheme_maps_to_predorsal_voiced(self):
        """⟨z⟩ should map to predorsal voiced [z̻]."""
        z_ipa = GRAPHEMES_MWL["z"]
        self.assertEqual(z_ipa, ["z̻"],
                         "⟨z⟩ must map to predorsal voiced [z̻]")

    def test_c_before_ei_maps_to_predorsal(self):
        """⟨c⟩ includes predorsal [s̻] (for c before e/i context)."""
        c_ipa = GRAPHEMES_MWL["c"]
        self.assertIn("s̻", c_ipa,
                      "⟨c⟩ must include predorsal [s̻] (before e/i)")

    def test_all_four_sibilants_in_allophone_inventory(self):
        """The allophone inventory must contain all four sibilant phonemes."""
        self.assertIn("s̺", ALLOPHONES_MWL, "Missing apical voiceless [s̺]")
        self.assertIn("z̺", ALLOPHONES_MWL, "Missing apical voiced [z̺]")
        self.assertIn("s̻", ALLOPHONES_MWL, "Missing predorsal voiceless [s̻]")
        self.assertIn("z̻", ALLOPHONES_MWL, "Missing predorsal voiced [z̻]")

    def test_sibilants_distinct_from_postalveolars(self):
        """Sibilants must be distinct from postalveolar ⟨x⟩=[ʃ] and ⟨j⟩=[ʒ]."""
        self.assertIn("ʃ", ALLOPHONES_MWL, "Missing postalveolar [ʃ]")
        self.assertIn("ʒ", ALLOPHONES_MWL, "Missing postalveolar [ʒ]")
        # Ensure sibilant keys are distinct
        sibilant_keys = {"s̺", "z̺", "s̻", "z̻"}
        postalveolar_keys = {"ʃ", "ʒ"}
        self.assertTrue(sibilant_keys.isdisjoint(postalveolar_keys))

    def test_positional_s_voicing(self):
        """⟨s⟩ should voice to [z̺] intervocalically per positional data."""
        self.assertIn("s", POSITIONAL_MWL)
        pos_s = POSITIONAL_MWL["s"]
        # Word-initial = voiceless
        self.assertEqual(pos_s[GP.WORD_INITIAL], ["s̺"])
        # Intervocalic = voiced
        self.assertEqual(pos_s[GP.INTERVOCALIC], ["z̺"])


# ═══════════════════════════════════════════════════════════════════════════
# 4. Leonese diphthongs
# ═══════════════════════════════════════════════════════════════════════════

class TestMirandeseLeoneseDiphthongs(unittest.TestCase):
    """Validate the hallmark Leonese diphthongs from Latin Ĕ and Ŏ."""

    def test_ie_diphthong_present(self):
        """⟨iê⟩ must map to [je] (Latin Ĕ → iê)."""
        self.assertIn("iê", GRAPHEMES_MWL)
        self.assertEqual(GRAPHEMES_MWL["iê"], ["je"])

    def test_uo_diphthong_present(self):
        """⟨uô⟩ must map to [wo] (Latin Ŏ → uô)."""
        self.assertIn("uô", GRAPHEMES_MWL)
        self.assertEqual(GRAPHEMES_MWL["uô"], ["wo"])

    def test_sendim_monophthongization_ie(self):
        """Sendinês: ⟨iê⟩ reduces to [i] (monophthongization)."""
        self.assertEqual(GRAPHEMES_MWL_SENDIM["iê"], ["i"])

    def test_sendim_monophthongization_uo(self):
        """Sendinês: ⟨uô⟩ reduces to [u] (monophthongization)."""
        self.assertEqual(GRAPHEMES_MWL_SENDIM["uô"], ["u"])

    def test_ifanes_monophthongization_ie(self):
        """Ifanês: ⟨iê⟩ reduces to [e] (different from Sendim's [i])."""
        self.assertEqual(GRAPHEMES_MWL_IFANES["iê"], ["e"])

    def test_ifanes_retains_uo(self):
        """Ifanês: ⟨uô⟩ retained as [wo] (sporadic but present)."""
        self.assertEqual(GRAPHEMES_MWL_IFANES["uô"], ["wo"])


# ═══════════════════════════════════════════════════════════════════════════
# 5. L-palatalization and laterals
# ═══════════════════════════════════════════════════════════════════════════

class TestMirandeseLPalatalization(unittest.TestCase):
    """Validate L-palatalization (Latin L- → [ʎ], written ⟨lh-⟩)."""

    def test_lh_maps_to_palatal_lateral(self):
        """⟨lh⟩ must map to palatal lateral [ʎ]."""
        self.assertIn("lh", GRAPHEMES_MWL)
        self.assertEqual(GRAPHEMES_MWL["lh"], ["ʎ"])

    def test_palatal_lateral_in_allophones(self):
        """[ʎ] must be in allophone inventory."""
        self.assertIn("ʎ", ALLOPHONES_MWL)

    def test_l_onset_is_clear(self):
        """⟨l⟩ in onset should be clear [l]."""
        self.assertEqual(
            POSITIONAL_MWL["l"][GP.ONSET], ["l"]
        )

    def test_l_coda_is_velarised(self):
        """⟨l⟩ in coda should be velarised [ɫ]."""
        self.assertIn("ɫ", POSITIONAL_MWL["l"][GP.CODA])


# ═══════════════════════════════════════════════════════════════════════════
# 6. Betacism
# ═══════════════════════════════════════════════════════════════════════════

class TestMirandeseBetacism(unittest.TestCase):
    """Validate betacism: /v/ does not exist, ⟨v⟩ → [b]."""

    def test_v_maps_to_b(self):
        """⟨v⟩ must map to [b], not [v] (betacism)."""
        self.assertIn("v", GRAPHEMES_MWL)
        self.assertEqual(GRAPHEMES_MWL["v"], ["b"])
        # /v/ must NOT be in the allophone inventory
        self.assertNotIn("v", ALLOPHONES_MWL,
                         "Mirandese has betacism: /v/ should not be in allophones")

    def test_b_has_spirant_allophone(self):
        """⟨b⟩ must have [β] spirant allophone (intervocalic)."""
        self.assertIn("β", ALLOPHONES_MWL["b"])


# ═══════════════════════════════════════════════════════════════════════════
# 7. Vowel system
# ═══════════════════════════════════════════════════════════════════════════

class TestMirandeseVowels(unittest.TestCase):
    """Validate the vowel inventory: 7 oral + 5 nasal + centralised ɨ."""

    def test_seven_oral_vowels(self):
        """Allophone inventory must include all 7 oral vowel qualities."""
        expected_oral = {"a", "ɐ", "e", "ɛ", "i", "o", "ɔ", "u", "ɨ"}
        allophone_keys = set(ALLOPHONES_MWL.keys())
        for v in expected_oral:
            with self.subTest(vowel=v):
                self.assertIn(v, allophone_keys, f"Missing oral vowel {v}")

    def test_five_nasal_vowels(self):
        """Allophone inventory must include all 5 nasal vowels."""
        expected_nasal = {"ɐ̃", "ẽ", "ĩ", "õ", "ũ"}
        allophone_keys = set(ALLOPHONES_MWL.keys())
        for v in expected_nasal:
            with self.subTest(vowel=v):
                self.assertIn(v, allophone_keys, f"Missing nasal vowel {v}")

    def test_centralised_vowel(self):
        """Centralised ɨ (unstressed) must be in allophones."""
        self.assertIn("ɨ", ALLOPHONES_MWL)

    def test_centralised_nasal_vowel(self):
        """Centralised nasal ɨ̃ (unique Mirandese) must be in allophones."""
        self.assertIn("ɨ̃", ALLOPHONES_MWL)

    def test_e_grapheme_includes_centralised(self):
        """⟨e⟩ should include [ɨ] for unstressed reduction."""
        self.assertIn("ɨ", GRAPHEMES_MWL["e"])

    def test_o_grapheme_includes_reduction(self):
        """⟨o⟩ should include [u] for unstressed reduction."""
        self.assertIn("u", GRAPHEMES_MWL["o"])

    def test_accented_vowel_quality(self):
        """Accented vowels should map to specific qualities."""
        # Acute = open
        self.assertEqual(GRAPHEMES_MWL["á"], ["a"])
        self.assertEqual(GRAPHEMES_MWL["é"], ["ɛ"])
        self.assertEqual(GRAPHEMES_MWL["ó"], ["ɔ"])
        # Circumflex = closed
        self.assertEqual(GRAPHEMES_MWL["ê"], ["e"])
        self.assertEqual(GRAPHEMES_MWL["ô"], ["o"])


# ═══════════════════════════════════════════════════════════════════════════
# 8. Consonant system
# ═══════════════════════════════════════════════════════════════════════════

class TestMirandeseConsonants(unittest.TestCase):
    """Validate consonant inventory and digraphs."""

    def test_ch_is_affricate(self):
        """⟨ch⟩ must map to affricate [tʃ], not fricative [ʃ]."""
        self.assertEqual(GRAPHEMES_MWL["ch"], ["tʃ"])

    def test_nh_is_palatal_nasal(self):
        """⟨nh⟩ must map to palatal nasal [ɲ]."""
        self.assertEqual(GRAPHEMES_MWL["nh"], ["ɲ"])

    def test_rr_is_trill(self):
        """⟨rr⟩ must map to alveolar trill [r]."""
        self.assertEqual(GRAPHEMES_MWL["rr"], ["r"])

    def test_x_is_postalveolar_fricative(self):
        """⟨x⟩ must map to voiceless postalveolar [ʃ]."""
        self.assertEqual(GRAPHEMES_MWL["x"], ["ʃ"])

    def test_y_is_semivowel(self):
        """⟨y⟩ must map to [j] (medieval Leonese tradition)."""
        self.assertIn("y", GRAPHEMES_MWL)
        self.assertEqual(GRAPHEMES_MWL["y"], ["j"])

    def test_w_for_foreign_words(self):
        """⟨w⟩ must be present for foreign words."""
        self.assertIn("w", GRAPHEMES_MWL)

    def test_j_is_voiced_postalveolar(self):
        """⟨j⟩ must map to voiced postalveolar [ʒ]."""
        self.assertEqual(GRAPHEMES_MWL["j"], ["ʒ"])

    def test_g_before_ei_context(self):
        """⟨g⟩ must include [ʒ] (for before e/i context)."""
        self.assertIn("ʒ", GRAPHEMES_MWL["g"])

    def test_affricate_in_allophones(self):
        """[tʃ] must be in allophone inventory."""
        self.assertIn("tʃ", ALLOPHONES_MWL)


# ═══════════════════════════════════════════════════════════════════════════
# 9. Diphthong inventory
# ═══════════════════════════════════════════════════════════════════════════

class TestMirandeseDiphthongs(unittest.TestCase):
    """Validate the full diphthong inventory from the Convenção."""

    def test_falling_diphthongs_present(self):
        """All falling diphthongs from Convenção p.18-19 must be present."""
        expected = {
            "ai": ["aj"], "au": ["aw"], "ei": ["ej"],
            "eu": ["ew"], "iu": ["iw"], "oi": ["oj"],
            "ou": ["ow"], "ui": ["uj"],
        }
        for digraph, ipa in expected.items():
            with self.subTest(diphthong=digraph):
                self.assertIn(digraph, GRAPHEMES_MWL,
                              f"Missing diphthong ⟨{digraph}⟩")
                self.assertEqual(GRAPHEMES_MWL[digraph], ipa)

    def test_accented_diphthongs(self):
        """Accented diphthongs éu and ói must be present."""
        self.assertIn("éu", GRAPHEMES_MWL)
        self.assertEqual(GRAPHEMES_MWL["éu"], ["ɛw"])
        self.assertIn("ói", GRAPHEMES_MWL)
        self.assertEqual(GRAPHEMES_MWL["ói"], ["ɔj"])

    def test_rising_diphthongs(self):
        """Rising diphthongs ia and ua must be present."""
        self.assertIn("ia", GRAPHEMES_MWL)
        self.assertEqual(GRAPHEMES_MWL["ia"], ["ja"])
        self.assertIn("ua", GRAPHEMES_MWL)
        self.assertEqual(GRAPHEMES_MWL["ua"], ["wa"])


# ═══════════════════════════════════════════════════════════════════════════
# 10. Nasal endings (word-final V+n)
# ═══════════════════════════════════════════════════════════════════════════

class TestMirandeseNasalEndings(unittest.TestCase):
    """Validate nasal vowel endings written as V+n word-finally."""

    def test_on_ending(self):
        """⟨on⟩ must map to [õ] (Latin -ōnis → -on)."""
        self.assertIn("on", GRAPHEMES_MWL)
        self.assertEqual(GRAPHEMES_MWL["on"], ["õ"])

    def test_an_ending(self):
        """⟨an⟩ must map to [ɐ̃]."""
        self.assertIn("an", GRAPHEMES_MWL)
        self.assertEqual(GRAPHEMES_MWL["an"], ["ɐ̃"])

    def test_en_ending(self):
        """⟨en⟩ must map to [ẽ]."""
        self.assertIn("en", GRAPHEMES_MWL)
        self.assertEqual(GRAPHEMES_MWL["en"], ["ẽ"])

    def test_in_ending(self):
        """⟨in⟩ must map to [ĩ]."""
        self.assertIn("in", GRAPHEMES_MWL)
        self.assertEqual(GRAPHEMES_MWL["in"], ["ĩ"])

    def test_un_ending(self):
        """⟨un⟩ must map to [ũ]."""
        self.assertIn("un", GRAPHEMES_MWL)
        self.assertEqual(GRAPHEMES_MWL["un"], ["ũ"])


# ═══════════════════════════════════════════════════════════════════════════
# 11. Positional grapheme lenition
# ═══════════════════════════════════════════════════════════════════════════

class TestMirandesePositionalLenition(unittest.TestCase):
    """Validate Ibero-Romance lenition patterns in positional data."""

    def test_b_default_is_occlusive(self):
        """⟨b⟩ default must be occlusive [b]."""
        self.assertEqual(POSITIONAL_MWL["b"][GP.DEFAULT], ["b"])

    def test_b_intervocalic_is_spirant(self):
        """⟨b⟩ intervocalic must be spirant [β]."""
        self.assertEqual(POSITIONAL_MWL["b"][GP.INTERVOCALIC], ["β"])

    def test_d_default_is_occlusive(self):
        """⟨d⟩ default must be occlusive [d]."""
        self.assertEqual(POSITIONAL_MWL["d"][GP.DEFAULT], ["d"])

    def test_d_intervocalic_is_spirant(self):
        """⟨d⟩ intervocalic must be spirant [ð]."""
        self.assertEqual(POSITIONAL_MWL["d"][GP.INTERVOCALIC], ["ð"])

    def test_g_default_is_occlusive(self):
        """⟨g⟩ default must be occlusive [ɡ]."""
        self.assertEqual(POSITIONAL_MWL["g"][GP.DEFAULT], ["ɡ"])

    def test_g_intervocalic_is_spirant(self):
        """⟨g⟩ intervocalic must be spirant [ɣ]."""
        self.assertEqual(POSITIONAL_MWL["g"][GP.INTERVOCALIC], ["ɣ"])

    def test_r_word_initial_is_trill(self):
        """⟨r⟩ word-initial must be trill [r]."""
        self.assertEqual(POSITIONAL_MWL["r"][GP.WORD_INITIAL], ["r"])

    def test_r_intervocalic_is_tap(self):
        """⟨r⟩ intervocalic must be tap [ɾ]."""
        self.assertEqual(POSITIONAL_MWL["r"][GP.INTERVOCALIC], ["ɾ"])


# ═══════════════════════════════════════════════════════════════════════════
# 12. Cross-dialectal consistency
# ═══════════════════════════════════════════════════════════════════════════

class TestMirandeseCrossDialectal(unittest.TestCase):
    """Verify that subdialects properly extend the base spec."""

    def test_sendim_inherits_base_graphemes(self):
        """Sendinês should inherit all base Mirandese graphemes."""
        for key in GRAPHEMES_MWL:
            # Skip overridden entries
            if key not in ("iê", "uô"):
                with self.subTest(grapheme=key):
                    self.assertIn(key, GRAPHEMES_MWL_SENDIM,
                                  f"Sendinês missing inherited grapheme ⟨{key}⟩")

    def test_sendim_inherits_base_allophones(self):
        """Sendinês should inherit all base allophone mappings."""
        for key in ALLOPHONES_MWL:
            with self.subTest(phoneme=key):
                self.assertIn(key, ALLOPHONES_MWL_SENDIM,
                              f"Sendinês missing inherited allophone '{key}'")

    def test_sendim_sibilants_same_as_base(self):
        """Sendinês should maintain the same 4-way sibilant system."""
        for sib in ["s̺", "z̺", "s̻", "z̻"]:
            with self.subTest(sibilant=sib):
                self.assertIn(sib, ALLOPHONES_MWL_SENDIM)

    def test_ifanes_differs_from_sendim_in_ie(self):
        """Ifanês reduces iê to [e], Sendim to [i] — they must differ."""
        self.assertNotEqual(
            GRAPHEMES_MWL_IFANES["iê"],
            GRAPHEMES_MWL_SENDIM["iê"],
            "Ifanês and Sendinês must differ in iê monophthongization"
        )

    def test_all_dialects_share_family(self):
        """All Mirandese varieties must have family 'Asturleonese'."""
        for code in ["mwl", "mwl-x-sendim", "mwl-x-ifanes"]:
            with self.subTest(code=code):
                self.assertEqual(SPECS[code].family, "Asturleonese")


# ═══════════════════════════════════════════════════════════════════════════
# 13. Allophone-grapheme coverage
# ═══════════════════════════════════════════════════════════════════════════

class TestMirandeseAlloGraphemeCoverage(unittest.TestCase):
    """Verify that IPA symbols in graphemes have allophone entries."""

    def test_simple_ipa_covered_by_allophones(self):
        """Every simple (single-phoneme) IPA symbol from graphemes should be
        in the allophone inventory. Composite symbols like diphthongs (aj, wo)
        and coarticulated consonants (kw, ɡw) are excluded — they decompose
        into constituent phonemes that are individually covered."""
        grapheme_ipa = _all_ipa_from_graphemes(GRAPHEMES_MWL)
        allophone_keys = set(ALLOPHONES_MWL.keys())
        allophone_ipa = _all_ipa_from_allophones(ALLOPHONES_MWL)
        all_coverage = allophone_ipa | allophone_keys

        # Composite IPA sequences (diphthongs, labialized consonants,
        # nasal diphthongs) — these are sequences of individual phonemes,
        # not single allophone entries.
        composite_ipa = {
            "aj", "aw", "ej", "ɛw", "ew", "iw", "oj", "ɔj", "ow", "uj",
            "je", "wo", "ja", "wa",
            "kw", "ɡw",
            "ɐ̃w̃",  # nasal diphthong
        }

        for symbol in grapheme_ipa:
            if symbol in composite_ipa:
                continue  # skip — composites decompose into covered parts
            with self.subTest(ipa=symbol):
                self.assertTrue(
                    symbol in all_coverage,
                    f"IPA symbol '{symbol}' from graphemes not found in "
                    f"allophone inventory"
                )

    def test_diphthong_constituents_covered(self):
        """Diphthong components should individually be in the allophone inventory.
        E.g., "aj" decomposes to 'a' and 'j', both must be in allophones."""
        allophone_keys = set(ALLOPHONES_MWL.keys())

        # Key glides and vowels that compose diphthongs
        required_glides = {"j", "w"}
        required_vowels = {"a", "e", "ɛ", "i", "o", "ɔ", "u"}

        for g in required_glides:
            with self.subTest(glide=g):
                self.assertIn(g, allophone_keys,
                              f"Glide '{g}' needed for diphthongs not in allophones")
        for v in required_vowels:
            with self.subTest(vowel=v):
                self.assertIn(v, allophone_keys,
                              f"Vowel '{v}' needed for diphthongs not in allophones")


# ═══════════════════════════════════════════════════════════════════════════
# 14. Specific linguistic phenomena (regression tests)
# ═══════════════════════════════════════════════════════════════════════════

class TestMirandeseLinguisticPhenomena(unittest.TestCase):
    """Test specific linguistic features of Mirandese."""

    def test_intervocalic_l_preserved(self):
        """Mirandese preserves Latin intervocalic -l- (unlike Portuguese).
        This is structural — ⟨l⟩ must be a valid grapheme for intervocalic use.
        Portuguese: salir → sair, malo → mau. Mirandese keeps salir, malo.
        """
        self.assertIn("l", GRAPHEMES_MWL)
        # l must map to clear [l], not be deleted
        self.assertIn("l", GRAPHEMES_MWL["l"])

    def test_intervocalic_n_preserved(self):
        """Mirandese preserves Latin intervocalic -n- (unlike Portuguese).
        Portuguese: cheno → cheio, lhana → lã. Mirandese keeps cheno, lhana.
        """
        self.assertIn("n", GRAPHEMES_MWL)
        self.assertIn("n", GRAPHEMES_MWL["n"])

    def test_ch_x_contrast(self):
        """⟨ch⟩ [tʃ] must contrast with ⟨x⟩ [ʃ]: bucho ≠ buxo."""
        ch_ipa = GRAPHEMES_MWL["ch"]
        x_ipa = GRAPHEMES_MWL["x"]
        self.assertNotEqual(ch_ipa, x_ipa,
                            "⟨ch⟩ and ⟨x⟩ must have different IPA values")
        self.assertEqual(ch_ipa, ["tʃ"])
        self.assertEqual(x_ipa, ["ʃ"])

    def test_no_theta_phoneme(self):
        """Mirandese does NOT have /θ/ (unlike Castilian). No distinción."""
        self.assertNotIn("θ", ALLOPHONES_MWL,
                         "Mirandese should not have /θ/ — no distinción")

    def test_no_yeismo(self):
        """Mirandese preserves [ʎ] — no yeísmo (ll → y merger)."""
        self.assertIn("ʎ", ALLOPHONES_MWL)
        # ʎ should NOT have [ʝ] as an allophone (no yeísmo)
        allophone_list = ALLOPHONES_MWL["ʎ"]
        self.assertNotIn("ʝ", allophone_list,
                         "Mirandese should not have yeísmo: [ʎ] → [ʝ]")


if __name__ == "__main__":
    unittest.main()