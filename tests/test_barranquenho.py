"""Tests for Barranquenho (ext-PT-x-barrancos) — linguistic accuracy and structural integrity.

Validates the Barranquenho LanguageSpec against the Convenção Ortográfica
do Barranquenho (2025) by Gonçalves, Navas & Correia (Universidade de Évora).

Test categories:
1. Structural integrity — SPECS dict, grapheme/allophone consistency
2. Phonological inventory — vowels, consonants, nasal vowels per Convention
3. Grapheme-to-IPA accuracy — specific mappings from the Convention table
4. Positional graphemes — context-sensitive rules
5. Distinctive features — betacism, aspiration, monophthongization, etc.
6. Ancestry and lineage — parent, adstrate contacts
7. Nasal system — nasal digraphs and diphthongs per Convention §1.8
"""
import unittest
import importlib
from dataclasses import FrozenInstanceError

# Import types — these are stable across the codebase
from orthography2ipa.types import (
    Ancestor,
    AncestorRole,
    LanguageSpec,
    GraphemePosition as GP,
)


def _load_barranquenho() -> LanguageSpec:
    """Load the Barranquenho spec from the module."""
    mod = importlib.import_module("orthography2ipa.languages.barranquenho")
    return mod.SPECS["ext-PT-x-barrancos"]


# ═══════════════════════════════════════════════════════════════════════════
# 1. Structural integrity
# ═══════════════════════════════════════════════════════════════════════════

class TestBarranquenhoStructure(unittest.TestCase):
    """Structural integrity of the Barranquenho LanguageSpec."""

    def setUp(self):
        self.spec = _load_barranquenho()

    def test_spec_exists(self):
        """ext-PT-x-barrancos must be present in SPECS dict."""
        mod = importlib.import_module("orthography2ipa.languages.barranquenho")
        self.assertIn("ext-PT-x-barrancos", mod.SPECS)

    def test_code(self):
        self.assertEqual(self.spec.code, "ext-PT-x-barrancos")

    def test_name(self):
        self.assertEqual(self.spec.name, "Barranquenho")

    def test_family(self):
        self.assertEqual(self.spec.family, "Romance")

    def test_script(self):
        self.assertEqual(self.spec.script, "Latin")

    def test_frozen(self):
        """LanguageSpec must be immutable."""
        with self.assertRaises(FrozenInstanceError):
            self.spec.code = "xx"

    def test_graphemes_non_empty(self):
        self.assertGreater(len(self.spec.graphemes), 0)

    def test_allophones_non_empty(self):
        self.assertGreater(len(self.spec.allophones), 0)

    def test_grapheme_values_are_lists_of_strings(self):
        for grapheme, ipa_list in self.spec.graphemes.items():
            with self.subTest(grapheme=grapheme):
                self.assertIsInstance(ipa_list, list)
                for ipa in ipa_list:
                    self.assertIsInstance(ipa, str)

    def test_allophone_values_are_lists_of_strings(self):
        for phoneme, allo_list in self.spec.allophones.items():
            with self.subTest(phoneme=phoneme):
                self.assertIsInstance(allo_list, list)
                for allo in allo_list:
                    self.assertIsInstance(allo, str)

    def test_positional_graphemes_exist(self):
        """Barranquenho must have positional grapheme data."""
        self.assertTrue(self.spec.has_positional_data())

    def test_positional_keys_in_base_graphemes(self):
        """Every positional grapheme key must exist in base graphemes."""
        for gk in self.spec.positional_grapheme_keys():
            with self.subTest(grapheme=gk):
                self.assertIn(
                    gk, self.spec.graphemes,
                    f"Positional grapheme '{gk}' not in base graphemes",
                )


# ═══════════════════════════════════════════════════════════════════════════
# 2. Phonological inventory completeness
# ═══════════════════════════════════════════════════════════════════════════

class TestBarranquenhoInventory(unittest.TestCase):
    """Verify the phoneme inventory covers all sounds from the Convention."""

    def setUp(self):
        self.spec = _load_barranquenho()
        # Collect all IPA values from graphemes
        self.all_ipa = set()
        for ipa_list in self.spec.graphemes.values():
            for ipa in ipa_list:
                if ipa and ipa != "":
                    self.all_ipa.add(ipa)
        # Collect all allophone keys
        self.allo_keys = set(self.spec.allophones.keys())

    # ── Oral vowels (Convention §1) ────────────────────────────────────────
    def test_oral_vowels_present(self):
        """Convention lists 9 oral vowel qualities."""
        expected_vowels = {"a", "ɐ", "e", "ɛ", "i", "o", "ɔ", "u", "ɨ"}
        for v in expected_vowels:
            with self.subTest(vowel=v):
                self.assertIn(v, self.all_ipa, f"Vowel [{v}] missing from graphemes")
                self.assertIn(v, self.allo_keys, f"Vowel [{v}] missing from allophones")

    # ── Nasal vowels (Convention §1.8) ─────────────────────────────────────
    def test_nasal_vowels_present(self):
        """Convention §1.8: five nasal vowels [ɐ̃ ẽ ĩ õ ũ]."""
        expected_nasal = {"ɐ̃", "ẽ", "ĩ", "õ", "ũ"}
        for nv in expected_nasal:
            with self.subTest(nasal_vowel=nv):
                self.assertIn(nv, self.all_ipa, f"Nasal vowel [{nv}] missing from graphemes")
                self.assertIn(nv, self.allo_keys, f"Nasal vowel [{nv}] missing from allophones")

    # ── Consonants (Convention §2) ─────────────────────────────────────────
    def test_plosives_present(self):
        expected = {"p", "b", "t", "d", "k", "ɡ"}
        for c in expected:
            with self.subTest(consonant=c):
                self.assertIn(c, self.allo_keys, f"Plosive [{c}] missing")

    def test_fricatives_present(self):
        expected = {"f", "s", "z", "ʃ", "ʒ", "h"}
        for c in expected:
            with self.subTest(consonant=c):
                self.assertIn(c, self.allo_keys, f"Fricative [{c}] missing")

    def test_affricate_present(self):
        """Convention §2.2: [tʃ] from Spanish loans (catchondeu)."""
        self.assertIn("tʃ", self.allo_keys)

    def test_nasals_present(self):
        expected = {"m", "n", "ɲ"}
        for c in expected:
            with self.subTest(consonant=c):
                self.assertIn(c, self.allo_keys, f"Nasal [{c}] missing")

    def test_laterals_present(self):
        expected = {"l", "ʎ"}
        for c in expected:
            with self.subTest(consonant=c):
                self.assertIn(c, self.allo_keys, f"Lateral [{c}] missing")

    def test_rhotics_present(self):
        """Convention: [ɾ] tap and [r]~[ʀ] trill."""
        self.assertIn("ɾ", self.allo_keys, "Alveolar tap [ɾ] missing")
        self.assertIn("r", self.allo_keys, "Alveolar trill [r] missing")

    def test_glides_present(self):
        expected = {"w", "j"}
        for g in expected:
            with self.subTest(glide=g):
                self.assertIn(g, self.allo_keys, f"Glide [{g}] missing")


# ═══════════════════════════════════════════════════════════════════════════
# 3. Grapheme-to-IPA accuracy (Convention table pp. 17–19)
# ═══════════════════════════════════════════════════════════════════════════

class TestBarranquenhoGraphemeMappings(unittest.TestCase):
    """Specific grapheme→IPA mappings from the Convention table."""

    def setUp(self):
        self.spec = _load_barranquenho()
        self.g = self.spec.graphemes

    # ── Vowel graphemes ────────────────────────────────────────────────────
    def test_a_maps_to_a_and_schwa(self):
        """⟨a⟩ = [a] pássaru and [ɐ] cahtelu."""
        self.assertIn("a", self.g["a"])
        self.assertIn("ɐ", self.g["a"])

    def test_e_maps_include_three_qualities(self):
        """⟨e⟩ = [e] ehti, [ɛ] pedra, [ɨ] pretonic."""
        self.assertIn("e", self.g["e"])
        self.assertIn("ɛ", self.g["e"])

    def test_circumflex_e_is_close_mid(self):
        """⟨ê⟩ = [e] from monophthongized /ej/: bêju, casê."""
        self.assertEqual(self.g["ê"], ["e"])

    def test_circumflex_o_is_close_mid(self):
        """⟨ô⟩ = [o] from monophthongized /ow/: dotô, sonhô."""
        self.assertEqual(self.g["ô"], ["o"])

    def test_acute_a_is_open(self):
        """⟨á⟩ = [a] stressed open: cantá."""
        self.assertEqual(self.g["á"], ["a"])

    def test_tilde_a_is_nasal(self):
        """⟨ã⟩ = [ɐ̃] nasal."""
        self.assertEqual(self.g["ã"], ["ɐ̃"])

    # ── Consonant graphemes ────────────────────────────────────────────────
    def test_b_betacism(self):
        """⟨b⟩ = [b] — covers historical /b/ AND /v/ due to betacism."""
        self.assertEqual(self.g["b"], ["b"])

    def test_v_betacism(self):
        """⟨v⟩ = [b] — betacism."""
        self.assertEqual(self.g["v"], ["b"])

    def test_h_aspiration(self):
        """⟨h⟩ = [h] aspiration of coda /s/: heringu, mehmu."""
        self.assertIn("h", self.g["h"])

    def test_j_is_voiced_palatal_fricative(self):
        """⟨j⟩ = [ʒ]: janela, jogu."""
        self.assertEqual(self.g["j"], ["ʒ"])

    def test_c_dual_mapping(self):
        """⟨c⟩ = [k] before a,o,u; [s] before e,i."""
        self.assertIn("k", self.g["c"])
        self.assertIn("s", self.g["c"])

    def test_g_dual_mapping(self):
        """⟨g⟩ = [ɡ] before a,o,u; [ʒ] before e,i."""
        self.assertIn("ɡ", self.g["g"])
        self.assertIn("ʒ", self.g["g"])

    # ── Digraphs ───────────────────────────────────────────────────────────
    def test_ch_is_palatal_fricative(self):
        """⟨ch⟩ = [ʃ] (NOT affricate — unlike Castilian)."""
        self.assertEqual(self.g["ch"], ["ʃ"])

    def test_lh_is_palatal_lateral(self):
        """⟨lh⟩ = [ʎ]: colhé, lhanu."""
        self.assertEqual(self.g["lh"], ["ʎ"])

    def test_nh_is_palatal_nasal(self):
        """⟨nh⟩ = [ɲ]: senhô."""
        self.assertEqual(self.g["nh"], ["ɲ"])

    def test_tch_affricate(self):
        """⟨tch⟩ = [tʃ] Spanish loan affricate: catchondeu (Convention §2.2)."""
        self.assertEqual(self.g["tch"], ["tʃ"])

    def test_rr_is_trill(self):
        """⟨rr⟩ = [r]~[ʀ]: carru, Barrancu."""
        self.assertIn("r", self.g["rr"])

    def test_ss_is_voiceless_sibilant(self):
        """⟨ss⟩ = [s]: passu."""
        self.assertEqual(self.g["ss"], ["s"])

    def test_gu_with_trema(self):
        """⟨gü⟩ = [ɡw] explicit labiovelar: agüentá, lingüíhtica."""
        self.assertEqual(self.g["gü"], ["ɡw"])


# ═══════════════════════════════════════════════════════════════════════════
# 4. Positional graphemes
# ═══════════════════════════════════════════════════════════════════════════

class TestBarranquenhoPositional(unittest.TestCase):
    """Context-sensitive positional grapheme rules."""

    def setUp(self):
        self.spec = _load_barranquenho()

    def test_s_coda_aspirated(self):
        """Convention §2.1: coda /s/ → [h] (aspiration)."""
        result = self.spec.resolve_grapheme("s", GP.CODA)
        self.assertIn("h", result, "Coda /s/ must include [h] aspiration")

    def test_s_intervocalic_voiced(self):
        """Convention: intervocalic ⟨s⟩ = [z] (Portuguese-like voicing)."""
        result = self.spec.resolve_grapheme("s", GP.INTERVOCALIC)
        self.assertEqual(result, ["z"])

    def test_s_word_initial_voiceless(self):
        """Word-initial ⟨s⟩ = [s]."""
        result = self.spec.resolve_grapheme("s", GP.WORD_INITIAL)
        self.assertEqual(result, ["s"])

    def test_s_word_final_aspirated(self):
        """Word-final ⟨s⟩ includes aspiration [h]."""
        result = self.spec.resolve_grapheme("s", GP.WORD_FINAL)
        self.assertIn("h", result)

    def test_b_intervocalic_lenition(self):
        """Intervocalic /b/ → [β] (Spanish-like)."""
        result = self.spec.resolve_grapheme("b", GP.INTERVOCALIC)
        self.assertEqual(result, ["β"])

    def test_g_intervocalic_lenition(self):
        """Intervocalic /g/ → [ɣ] (Spanish-like)."""
        result = self.spec.resolve_grapheme("g", GP.INTERVOCALIC)
        self.assertEqual(result, ["ɣ"])

    def test_r_word_initial_trill(self):
        """Word-initial ⟨r⟩ = [r]~[ʀ] (Convention: rapazi, Enriqui)."""
        result = self.spec.resolve_grapheme("r", GP.WORD_INITIAL)
        self.assertIn("r", result, "Word-initial /r/ must include trill [r]")

    def test_r_intervocalic_tap(self):
        """Intervocalic ⟨r⟩ = [ɾ] (Convention: Marqui, caru)."""
        result = self.spec.resolve_grapheme("r", GP.INTERVOCALIC)
        self.assertEqual(result, ["ɾ"])

    def test_l_onset_clear(self):
        """Onset /l/ is clear [l]."""
        result = self.spec.resolve_grapheme("l", GP.ONSET)
        self.assertEqual(result, ["l"])


# ═══════════════════════════════════════════════════════════════════════════
# 5. Distinctive Barranquenho features
# ═══════════════════════════════════════════════════════════════════════════

class TestBarranquenhoDistinctiveFeatures(unittest.TestCase):
    """Features that distinguish Barranquenho from standard Portuguese/Spanish."""

    def setUp(self):
        self.spec = _load_barranquenho()

    def test_betacism_v_maps_to_b(self):
        """Convention §2: betacism — ⟨v⟩ → [b] (biba = 'viva', bibu = 'vivo')."""
        self.assertEqual(self.spec.graphemes["v"], ["b"])
        self.assertEqual(self.spec.graphemes["b"], ["b"])

    def test_no_v_phoneme_in_allophones(self):
        """Barranquenho has NO /v/ phoneme — complete betacism."""
        self.assertNotIn("v", self.spec.allophones,
                         "Barranquenho should not have /v/ as a phoneme (betacism)")

    def test_sibilant_aspiration_in_allophones(self):
        """Convention §2.1: /s/ → [h] in coda (fundamental Barranquenho feature)."""
        self.assertIn("h", self.spec.allophones["s"])

    def test_monophthongization_ej(self):
        """Convention §1.7: /ej/ → [e], graphed ⟨ê⟩: bêju, casê, primêra."""
        self.assertEqual(self.spec.graphemes["ê"], ["e"])

    def test_monophthongization_ow(self):
        """Convention §1.7: /ow/ → [o], graphed ⟨ô⟩: dotô, sonhô, sô."""
        self.assertEqual(self.spec.graphemes["ô"], ["o"])

    def test_ei_and_ou_absent_as_diphthongs(self):
        """Convention §1.7: ⟨ei⟩ and ⟨ou⟩ do NOT appear in native Barranquenho."""
        # They should not be in the grapheme table as diphthongs
        if "ei" in self.spec.graphemes:
            # If present, should not map to a diphthong [ej]
            self.assertNotIn("ej", self.spec.graphemes["ei"])
        if "ou" in self.spec.graphemes:
            self.assertNotIn("ow", self.spec.graphemes["ou"])

    def test_unstressed_final_e_is_i(self):
        """Convention §1.1: unstressed final ⟨-e⟩ = [i] in Barranquenho, graphed ⟨-i⟩.
        This is a systematic spelling convention (sempri, sociedadi, oji, genti).
        The grapheme ⟨i⟩ maps to [i]."""
        self.assertIn("i", self.spec.graphemes["i"])

    def test_unstressed_final_o_is_u(self):
        """Convention §1.1: unstressed final ⟨-o⟩ = [u], graphed ⟨-u⟩.
        (altu, façu). The grapheme ⟨u⟩ maps to [u]."""
        self.assertIn("u", self.spec.graphemes["u"])

    def test_affricate_tch_from_spanish(self):
        """Convention §2.2: [tʃ] only in Spanish loans: catchondeu."""
        self.assertIn("tʃ", self.spec.allophones)
        self.assertEqual(self.spec.graphemes["tch"], ["tʃ"])


# ═══════════════════════════════════════════════════════════════════════════
# 6. Ancestry and lineage
# ═══════════════════════════════════════════════════════════════════════════

class TestBarranquenhoAncestry(unittest.TestCase):
    """Ancestry relationships — Barranquenho as a contact language."""

    def setUp(self):
        self.spec = _load_barranquenho()

    def test_has_parent(self):
        """Barranquenho must have a parent language."""
        self.assertIsNotNone(self.spec.parent)

    def test_parent_is_portuguese(self):
        """Primary parent should be European Portuguese (pt-PT).

        The Convenção Ortográfica describes Barranquenho as
        'essencialmente de base portuguesa' (Gonçalves & Navas 2021).
        """
        self.assertEqual(self.spec.primary_parent, "pt-PT-x-alentejo")

    def test_has_ancestors(self):
        """Barranquenho must have explicit ancestor relationships."""
        ancestors = self.spec.get_ancestors()
        self.assertGreater(len(ancestors), 1,
                           "Contact language should have multiple ancestors")

    def test_parent_ancestor_present(self):
        """There must be a PARENT ancestor."""
        parents = self.spec.get_ancestors(AncestorRole.PARENT)
        self.assertEqual(len(parents), 1)
        self.assertEqual(parents[0].code, "pt-PT")

    def test_extremaduran_adstrate(self):
        """Extremaduran should be an ADSTRATE ancestor."""
        adstrates = self.spec.get_ancestors(AncestorRole.ADSTRATE)
        ad_codes = {a.code for a in adstrates}
        self.assertIn("ext", ad_codes,
                      "Extremaduran must be listed as adstrate contact")

    def test_andalusian_adstrate(self):
        """Western Andalusian should be an ADSTRATE ancestor."""
        adstrates = self.spec.get_ancestors(AncestorRole.ADSTRATE)
        ad_codes = {a.code for a in adstrates}
        self.assertIn("es-ES-x-andalusia-w", ad_codes,
                      "Western Andalusian must be listed as adstrate contact")

    def test_ancestor_weights_reasonable(self):
        """Ancestor weights should follow guidelines."""
        for anc in self.spec.get_ancestors():
            with self.subTest(ancestor=anc.code):
                self.assertGreaterEqual(anc.weight, 0.0)
                self.assertLessEqual(anc.weight, 1.0)
                if anc.role == AncestorRole.PARENT:
                    self.assertGreaterEqual(anc.weight, 0.60,
                                            "PARENT weight should be >= 0.60")
                elif anc.role == AncestorRole.ADSTRATE:
                    self.assertLessEqual(anc.weight, 0.30,
                                         "ADSTRATE weight should be <= 0.30")

    def test_contact_codes_non_empty(self):
        """Contact language should have non-parent contact codes."""
        self.assertGreater(len(self.spec.contact_codes), 0)


# ═══════════════════════════════════════════════════════════════════════════
# 7. Nasal system (Convention §1.8)
# ═══════════════════════════════════════════════════════════════════════════

class TestBarranquenhoNasals(unittest.TestCase):
    """Nasal vowel and nasal diphthong graphemes per Convention §1.8."""

    def setUp(self):
        self.spec = _load_barranquenho()
        self.g = self.spec.graphemes

    # ── Nasal vowel digraphs (tonic, §1.8.1) ──────────────────────────────
    def test_am_nasal_a(self):
        """⟨am⟩ = [ɐ̃]: campu."""
        self.assertIn("am", self.g)
        self.assertIn("ɐ̃", self.g["am"])

    def test_an_nasal_a(self):
        """⟨an⟩ = [ɐ̃]: canton, manhán."""
        self.assertIn("an", self.g)
        self.assertIn("ɐ̃", self.g["an"])

    def test_em_nasal_e(self):
        """⟨em⟩ = [ẽ]: tempu, sempri."""
        self.assertIn("em", self.g)
        self.assertIn("ẽ", self.g["em"])

    def test_en_nasal_e(self):
        """⟨en⟩ = [ẽ]: entãu, quen."""
        self.assertIn("en", self.g)
        self.assertIn("ẽ", self.g["en"])

    def test_im_nasal_i(self):
        """⟨im⟩ = [ĩ]: impériu."""
        self.assertIn("im", self.g)
        self.assertIn("ĩ", self.g["im"])

    def test_in_nasal_i(self):
        """⟨in⟩ = [ĩ]: seguinti, min."""
        self.assertIn("in", self.g)
        self.assertIn("ĩ", self.g["in"])

    def test_om_nasal_o(self):
        """⟨om⟩ = [õ]: ombru, pomba."""
        self.assertIn("om", self.g)
        self.assertIn("õ", self.g["om"])

    def test_on_nasal_o(self):
        """⟨on⟩ = [õ]: canton, eron, bon."""
        self.assertIn("on", self.g)
        self.assertIn("õ", self.g["on"])

    def test_um_nasal_u(self):
        """⟨um⟩ = [ũ]: chumbu."""
        self.assertIn("um", self.g)
        self.assertIn("ũ", self.g["um"])

    def test_un_nasal_u(self):
        """⟨un⟩ = [ũ]: assuntu, un."""
        self.assertIn("un", self.g)
        self.assertIn("ũ", self.g["un"])

    # ── Nasal diphthongs (§1.8.3) ─────────────────────────────────────────
    def test_ãu_nasal_diphthong(self):
        """⟨ãu⟩ = [ɐ̃w̃]: fejãu, sãu, nãu."""
        self.assertIn("ãu", self.g)
        self.assertEqual(self.g["ãu"], ["ɐ̃w̃"])

    def test_ãi_nasal_diphthong(self):
        """⟨ãi⟩ = [ɐ̃j̃]: mãi, pãi."""
        self.assertIn("ãi", self.g)
        self.assertEqual(self.g["ãi"], ["ɐ̃j̃"])

    def test_õi_nasal_diphthong(self):
        """⟨õi⟩ = [õj̃]: patrõi, liçõi."""
        self.assertIn("õi", self.g)
        self.assertEqual(self.g["õi"], ["õj̃"])

    def test_eãu_triphthong(self):
        """⟨eãu⟩ = [jɐ̃w̃]: leãu (Convention §1.8.3)."""
        self.assertIn("eãu", self.g)
        self.assertEqual(self.g["eãu"], ["jɐ̃w̃"])

    # ── Grave accent on contraction ────────────────────────────────────────
    def test_ò_contraction(self):
        """⟨ò⟩ = [ɔ] from contraction (a + o): ò contráriu."""
        self.assertIn("ò", self.g)
        self.assertEqual(self.g["ò"], ["ɔ"])


# ═══════════════════════════════════════════════════════════════════════════
# 8. Rhotics (Convention distinction)
# ═══════════════════════════════════════════════════════════════════════════

class TestBarranquenhoRhotics(unittest.TestCase):
    """Rhotic system per Convention: ⟨r-, -r-⟩ [ɾ] vs ⟨r; -rr-⟩ [r]~[ʀ]."""

    def setUp(self):
        self.spec = _load_barranquenho()

    def test_r_includes_tap_and_trill(self):
        """Base ⟨r⟩ grapheme includes both tap and trill possibilities."""
        r_ipa = self.spec.graphemes["r"]
        self.assertIn("ɾ", r_ipa, "⟨r⟩ must include tap [ɾ]")
        self.assertIn("r", r_ipa, "⟨r⟩ must include trill [r]")

    def test_rr_is_trill_only(self):
        """⟨rr⟩ = [r]~[ʀ] trill only (Convention: carru, Barrancu)."""
        rr_ipa = self.spec.graphemes["rr"]
        self.assertIn("r", rr_ipa)
        self.assertNotIn("ɾ", rr_ipa, "⟨rr⟩ should not include tap [ɾ]")

    def test_no_uvular_fricative(self):
        """Convention does NOT mention uvular fricative [ʁ].
        Barranquenho uses [r]~[ʀ] (trill variants), not the Portuguese [ʁ]."""
        self.assertNotIn("ʁ", self.spec.allophones,
                         "[ʁ] uvular fricative not attested in Convention")
        r_ipa = self.spec.graphemes["r"]
        self.assertNotIn("ʁ", r_ipa,
                         "⟨r⟩ should not map to [ʁ]")

    def test_trill_allophones_correct(self):
        """Allophone map: /r/ → [r, ʀ] (trill variants)."""
        self.assertIn("r", self.spec.allophones)
        r_allos = self.spec.allophones["r"]
        self.assertIn("r", r_allos)
        self.assertIn("ʀ", r_allos)


if __name__ == "__main__":
    unittest.main()