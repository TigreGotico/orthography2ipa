"""Tests for Asturian (ast) language inventories.

Validates linguistic accuracy of the Asturian module against the
official ALLA *Normes Ortográfiques* (8th ed., 2021) and standard
phonological descriptions.

Covers:
- Phoneme inventory completeness (§1.7 consonants, §1.2 vowels)
- Grapheme-to-IPA mapping accuracy
- Allophone inventory consistency
- Positional grapheme behaviour (lenition, rhotics)
- Diphthong coverage (§1.6.1)
- Dialectal variants (Western, Eastern, Leonese)
- Structural integrity (keys, ancestors, family)
- Key contrasts with Castilian Spanish
"""
import unittest
import importlib

from orthography2ipa.types import GraphemePosition as GP, LanguageSpec


# ═══════════════════════════════════════════════════════════════════════════
# Setup helpers
# ═══════════════════════════════════════════════════════════════════════════

def _load_ast_module():
    return importlib.import_module("orthography2ipa.languages.ast")


def _extract_phonemes(graphemes):
    """Extract the set of unique IPA phonemes from a grapheme map."""
    phonemes = set()
    for ipa_list in graphemes.values():
        for ipa in ipa_list:
            if ipa and ipa not in ("", "∅"):
                phonemes.add(ipa)
    return phonemes


# ═══════════════════════════════════════════════════════════════════════════
# Central Asturian: Phoneme inventory (ALLA §1.7)
# ═══════════════════════════════════════════════════════════════════════════

class TestAsturianPhonemeInventory(unittest.TestCase):
    """Validate the native phoneme inventory per ALLA Normes §1.2 and §1.7."""

    def setUp(self):
        mod = _load_ast_module()
        self.spec = mod.SPECS["ast"]
        self.graphemes = mod.GRAPHEMES_AST
        self.allophones = mod.ALLOPHONES_AST
        self.phonemes = _extract_phonemes(self.graphemes)

    # ── Vowel system (§1.2) ──────────────────────────────────────────

    def test_five_vowel_system(self):
        """Asturian has a 5-vowel system /a, e, i, o, u/ (§1.2)."""
        for vowel in ["a", "e", "i", "o", "u"]:
            self.assertIn(vowel, self.phonemes,
                          f"Missing vowel /{vowel}/ in phoneme inventory")

    def test_no_reduced_vowels(self):
        """Standard Asturian has no vowel reduction (unlike Portuguese)."""
        reduced_vowels = {"ə", "ɐ", "ɨ"}
        self.assertEqual(self.phonemes & reduced_vowels, set(),
                         "Asturian should not have reduced vowels")

    def test_accented_vowels_same_phoneme(self):
        """Accented graphemes map to same phonemes as unaccented."""
        for pair in [("a", "á"), ("e", "é"), ("i", "í"), ("o", "ó"), ("u", "ú")]:
            self.assertEqual(
                self.graphemes[pair[0]], self.graphemes[pair[1]],
                f"⟨{pair[0]}⟩ and ⟨{pair[1]}⟩ should map to same IPA"
            )

    # ── Consonant inventory (§1.7) ───────────────────────────────────

    def test_alla_consonant_phonemes(self):
        """ALLA §1.7 lists these consonant phonemes explicitly:
        /p, t, tʃ, k, b, d, ɡ, ʝ, f, θ, s, ʃ, m, n, ɲ, l, ʎ, ɾ, r/
        """
        alla_consonants = {
            "p", "t", "tʃ", "k",       # voiceless stops + affricate
            "b", "d", "ɡ",             # voiced stops
            "ʝ",                        # palatal (§1.7.7: ⟨y⟩)
            "f", "θ", "s", "ʃ",        # fricatives
            "m", "n", "ɲ",             # nasals
            "l", "ʎ",                  # laterals
            "ɾ", "r",                  # rhotics
        }
        for phoneme in alla_consonants:
            self.assertIn(phoneme, self.phonemes,
                          f"Missing ALLA-listed consonant /{phoneme}/")

    def test_no_velar_fricative_native(self):
        """Asturian does NOT have /x/ (velar fricative) as a native phoneme.
        ⟨x⟩ = /ʃ/ (postalveolar), not /x/ (velar) as in Castilian.
        ⟨j⟩ is only used in foreign words (§1.1.6).
        """
        # /x/ should NOT appear as a native mapping of ⟨g⟩
        g_values = self.graphemes.get("g", [])
        self.assertNotIn("x", g_values,
                         "⟨g⟩ should not map to /x/ in Asturian; "
                         "Asturian uses ⟨x⟩=/ʃ/ where Castilian uses /x/")

    def test_x_is_postalveolar(self):
        """⟨x⟩ = /ʃ/ (voiceless postalveolar fricative), §1.7.12."""
        self.assertEqual(self.graphemes["x"], ["ʃ"])

    def test_palatal_lateral_preserved(self):
        """⟨ll⟩ = /ʎ/ (palatal lateral), no yeísmo in standard (§1.7.17)."""
        self.assertEqual(self.graphemes["ll"], ["ʎ"])

    def test_betacism(self):
        """⟨b⟩ and ⟨v⟩ are both /b/ (§1.7.5)."""
        self.assertEqual(self.graphemes["b"], ["b"])
        self.assertEqual(self.graphemes["v"], ["b"])


# ═══════════════════════════════════════════════════════════════════════════
# Grapheme-to-IPA accuracy
# ═══════════════════════════════════════════════════════════════════════════

class TestAsturianGraphemes(unittest.TestCase):
    """Validate specific grapheme→IPA mappings per ALLA norms."""

    def setUp(self):
        mod = _load_ast_module()
        self.graphemes = mod.GRAPHEMES_AST

    def test_h_is_silent(self):
        """⟨h⟩ is silent in standard Central Asturian (§1.7.20)."""
        self.assertEqual(self.graphemes["h"], [""])

    def test_ch_affricate(self):
        """⟨ch⟩ = /tʃ/ (§1.7.3)."""
        self.assertEqual(self.graphemes["ch"], ["tʃ"])

    def test_rr_trill(self):
        """⟨rr⟩ between vowels = /r/ trill (§1.7.19)."""
        self.assertEqual(self.graphemes["rr"], ["r"])

    def test_single_r_tap(self):
        """Single ⟨r⟩ = /ɾ/ tap (§1.7.18)."""
        self.assertEqual(self.graphemes["r"], ["ɾ"])

    def test_ny_palatal_nasal(self):
        """⟨ñ⟩ = /ɲ/ (§1.7.15)."""
        self.assertEqual(self.graphemes["ñ"], ["ɲ"])

    def test_c_dual_value(self):
        """⟨c⟩ = /k/ before a,o,u and /θ/ before e,i (§1.7.4, §1.7.10)."""
        self.assertEqual(self.graphemes["c"], ["k", "θ"])

    def test_z_interdental(self):
        """⟨z⟩ = /θ/ (§1.7.10.2)."""
        self.assertEqual(self.graphemes["z"], ["θ"])

    def test_qu_velar_stop(self):
        """⟨qu⟩ = /k/ before e,i (§1.7.4.2)."""
        self.assertEqual(self.graphemes["qu"], ["k"])

    def test_gu_voiced_velar(self):
        """⟨gu⟩ = /ɡ/ before e,i (§1.7.8.2)."""
        self.assertEqual(self.graphemes["gu"], ["ɡ"])

    def test_g_only_velar_stop(self):
        """⟨g⟩ before a,o,u = /ɡ/ only (§1.7.8.1).
        In Asturian, ⟨g⟩ before e,i is handled by the ⟨gu⟩ digraph,
        NOT by a /x/ realisation as in Castilian.
        """
        self.assertEqual(self.graphemes["g"], ["ɡ"])

    def test_y_dual_value(self):
        """⟨y⟩ = /ʝ/ consonant or /i/ vowel (§1.7.7, §1.2.1.2)."""
        self.assertEqual(self.graphemes["y"], ["ʝ", "i"])

    def test_f_labial_fricative(self):
        """⟨f⟩ = /f/ (§1.7.9). Asturian preserves Latin F- (unlike Castilian)."""
        self.assertEqual(self.graphemes["f"], ["f"])

    def test_s_apicoalveolar(self):
        """⟨s⟩ = /s/ apico-alveolar (§1.7.11)."""
        self.assertEqual(self.graphemes["s"], ["s"])


# ═══════════════════════════════════════════════════════════════════════════
# Diphthong coverage (§1.6)
# ═══════════════════════════════════════════════════════════════════════════

class TestAsturianDiphthongs(unittest.TestCase):
    """Validate diphthong mappings per ALLA §1.6.1."""

    def setUp(self):
        mod = _load_ast_module()
        self.graphemes = mod.GRAPHEMES_AST

    def test_rising_diphthongs(self):
        """Rising (crecientes) diphthongs: ia, ie, io, ua, ue, uo (§1.6.1a)."""
        expected = {
            "ia": ["ja"], "ie": ["je"], "io": ["jo"],
            "ua": ["wa"], "ue": ["we"], "uo": ["wo"],
        }
        for grapheme, ipa in expected.items():
            self.assertIn(grapheme, self.graphemes,
                          f"Missing rising diphthong ⟨{grapheme}⟩")
            self.assertEqual(self.graphemes[grapheme], ipa,
                             f"⟨{grapheme}⟩ should map to {ipa}")

    def test_falling_diphthongs(self):
        """Falling (decrecientes) diphthongs: ai, ei, oi, au, eu, ou (§1.6.1b)."""
        expected = {
            "ai": ["aj"], "ei": ["ej"], "oi": ["oj"],
            "au": ["aw"], "eu": ["ew"], "ou": ["ow"],
        }
        for grapheme, ipa in expected.items():
            self.assertIn(grapheme, self.graphemes,
                          f"Missing falling diphthong ⟨{grapheme}⟩")
            self.assertEqual(self.graphemes[grapheme], ipa,
                             f"⟨{grapheme}⟩ should map to {ipa}")

    def test_mixed_diphthongs(self):
        """Mixed (mestos) diphthongs: iu, ui (§1.6.1c)."""
        self.assertEqual(self.graphemes["iu"], ["ju"])
        self.assertEqual(self.graphemes["ui"], ["wi"])

    def test_leonese_diphthong_ue(self):
        """Asturleonese hallmark: Lat. Ŏ → ue /we/."""
        self.assertEqual(self.graphemes["ue"], ["we"])

    def test_leonese_diphthong_ie(self):
        """Asturleonese hallmark: Lat. Ĕ → ie /je/."""
        self.assertEqual(self.graphemes["ie"], ["je"])


# ═══════════════════════════════════════════════════════════════════════════
# Aspiration and dialectal graphemes (§1.1.2–§1.1.5)
# ═══════════════════════════════════════════════════════════════════════════

class TestAsturianDialectalGraphemes(unittest.TestCase):
    """Validate ALLA-approved dialectal graphemes."""

    def setUp(self):
        mod = _load_ast_module()
        self.graphemes_central = mod.GRAPHEMES_AST
        self.graphemes_western = mod.GRAPHEMES_AST_W

    def test_aspiration_grapheme_h_dot(self):
        """⟨ḥ⟩ and ⟨h.⟩ represent aspiration (§1.1.2)."""
        self.assertIn("ḥ", self.graphemes_central)
        self.assertEqual(self.graphemes_central["ḥ"], ["h"])
        self.assertIn("h.", self.graphemes_central)
        self.assertEqual(self.graphemes_central["h."], ["h"])

    def test_ts_western_affricate(self):
        """⟨ts⟩ = western dialectal [ts] for /tʃ/ (§1.1.4)."""
        self.assertIn("ts", self.graphemes_central)
        self.assertEqual(self.graphemes_central["ts"], ["ts"])

    def test_yy_western_palatal(self):
        """⟨yy⟩ = western dialectal [ky] for /ʝ/ (§1.1.5)."""
        self.assertIn("yy", self.graphemes_central)
        self.assertEqual(self.graphemes_central["yy"], ["ky"])

    def test_western_che_vaqueira_ḷḷ(self):
        """⟨ḷḷ⟩ = che vaqueira (§1.1.3) — western lateral realisation."""
        self.assertIn("ḷḷ", self.graphemes_western)

    def test_western_che_vaqueira_l_dot_l(self):
        """⟨l.l⟩ = alternative notation for che vaqueira (§1.1.3)."""
        self.assertIn("l.l", self.graphemes_western)

    def test_western_h_aspirated(self):
        """Western ⟨h⟩ = [h] (aspirated from Latin F-)."""
        self.assertEqual(self.graphemes_western["h"], ["h"])

    def test_diaeresis_gue_gui(self):
        """⟨güe⟩ and ⟨güi⟩ with audible /u/ (§1.9.3)."""
        self.assertIn("güe", self.graphemes_central)
        self.assertIn("güi", self.graphemes_central)
        self.assertEqual(self.graphemes_central["güe"], ["ɡwe"])
        self.assertEqual(self.graphemes_central["güi"], ["ɡwi"])


# ═══════════════════════════════════════════════════════════════════════════
# Allophone inventory consistency
# ═══════════════════════════════════════════════════════════════════════════

class TestAsturianAllophones(unittest.TestCase):
    """Validate allophone map is consistent with grapheme inventory."""

    def setUp(self):
        mod = _load_ast_module()
        self.graphemes = mod.GRAPHEMES_AST
        self.allophones = mod.ALLOPHONES_AST

    def test_iberian_lenition_voiced_stops(self):
        """Voiced stops have spirant allophones (standard Iberian lenition)."""
        self.assertEqual(self.allophones["b"], ["b", "β"])
        self.assertEqual(self.allophones["d"], ["d", "ð"])
        self.assertEqual(self.allophones["ɡ"], ["ɡ", "ɣ"])

    def test_s_apicoalveolar_allophone(self):
        """Asturian /s/ allophone is apico-alveolar [s̺]."""
        self.assertEqual(self.allophones["s"], ["s̺"])

    def test_palatal_fricative_allophones(self):
        """⟨y⟩/ʝ/ has fricative and affricate allophones."""
        self.assertIn("ʝ", self.allophones["ʝ"])
        self.assertIn("ɟʝ", self.allophones["ʝ"])

    def test_all_grapheme_phonemes_have_allophones(self):
        """Every unique phoneme from graphemes should have an allophone entry.
        Multi-segment IPA values (diphthongs, complex onsets, consonant clusters)
        are excluded as they are composed of individual phonemes.
        """
        phonemes = _extract_phonemes(self.graphemes)
        # Known multi-segment values to exclude: diphthongs, glide+V, C+glide+V, etc.
        # A "simple" phoneme is a single IPA segment: a vowel, consonant, or
        # well-known affricate (tʃ, ts, ɟʝ). These should have allophone entries.
        # Multi-segment values like "aj", "we", "ɡwe", "ky" should not.
        known_affricates = {"tʃ", "ts", "ɟʝ", "dʒ"}
        # Consonant clusters that are NOT single phonemes (they arise from
        # dialectal graphemes like ⟨yy⟩ → [ky])
        known_clusters = {"ky"}
        for phoneme in phonemes:
            if not phoneme or phoneme == "∅":
                continue
            if phoneme in known_clusters:
                continue
            # Skip known affricates — they should be in allophones (and are tested elsewhere)
            if phoneme in known_affricates:
                if phoneme in self.allophones:
                    continue  # Already checked
            # Skip anything that looks multi-segment: contains a vowel char AND
            # another segment, or is 3+ chars and not a known affricate
            if len(phoneme) >= 3 and phoneme not in known_affricates:
                continue  # Complex onset / diphthong / cluster
            # Skip two-char sequences that are clearly diphthongs or clusters
            # (contain two "nucleus-capable" segments)
            if len(phoneme) == 2 and phoneme not in known_affricates:
                has_vowel = any(c in "aeiou" for c in phoneme)
                has_glide = any(c in "jw" for c in phoneme)
                # ky, kw, gw etc. are clusters, not single phonemes
                if not has_vowel and not has_glide:
                    # Could be e.g. "ɲ" (single char but unicode len>1)
                    # or unknown affricate — check it
                    pass
                else:
                    continue  # diphthong or glide sequence
            self.assertIn(phoneme, self.allophones,
                          f"Phoneme /{phoneme}/ from graphemes has no allophone entry")

    def test_nasal_velar_assimilation(self):
        """Coda /n/ can assimilate to [ŋ] before velars."""
        self.assertIn("ŋ", self.allophones["n"])


# ═══════════════════════════════════════════════════════════════════════════
# Positional grapheme behaviour
# ═══════════════════════════════════════════════════════════════════════════

class TestAsturianPositional(unittest.TestCase):
    """Validate positional grapheme resolution for Asturian."""

    def setUp(self):
        mod = _load_ast_module()
        self.ast = mod.SPECS["ast"]
        self.ast_w = mod.SPECS["ast-x-occidental"]

    def test_b_intervocalic_spirant(self):
        """Intervocalic /b/ → [β] (standard Iberian lenition)."""
        self.assertEqual(self.ast.resolve_grapheme("b", GP.INTERVOCALIC), ["β"])

    def test_b_default_stop(self):
        """Default /b/ → [b] (post-pause, post-nasal)."""
        self.assertEqual(self.ast.resolve_grapheme("b", GP.DEFAULT), ["b"])

    def test_d_intervocalic_spirant(self):
        """Intervocalic /d/ → [ð]."""
        self.assertEqual(self.ast.resolve_grapheme("d", GP.INTERVOCALIC), ["ð"])

    def test_g_intervocalic_spirant(self):
        """Intervocalic /ɡ/ → [ɣ]."""
        self.assertEqual(self.ast.resolve_grapheme("g", GP.INTERVOCALIC), ["ɣ"])

    def test_r_word_initial_trill(self):
        """Word-initial ⟨r⟩ = trill [r] (§1.7.19.1a)."""
        self.assertEqual(self.ast.resolve_grapheme("r", GP.WORD_INITIAL), ["r"])

    def test_r_intervocalic_tap(self):
        """Intervocalic ⟨r⟩ = tap [ɾ] (§1.7.18)."""
        self.assertEqual(self.ast.resolve_grapheme("r", GP.INTERVOCALIC), ["ɾ"])

    def test_r_coda_tap(self):
        """Coda ⟨r⟩ = tap [ɾ] (§1.7.19.1d)."""
        self.assertEqual(self.ast.resolve_grapheme("r", GP.CODA), ["ɾ"])

    def test_n_coda_velar(self):
        """Coda /n/ can be [n] or [ŋ]."""
        result = self.ast.resolve_grapheme("n", GP.CODA)
        self.assertIn("n", result)
        self.assertIn("ŋ", result)

    def test_western_f_word_initial_aspiration(self):
        """Western Asturian: word-initial /f/ → [h] (Latin F- aspiration)."""
        result = self.ast_w.resolve_grapheme("f", GP.WORD_INITIAL)
        self.assertIn("h", result)

    def test_western_f_intervocalic_retained(self):
        """Western Asturian: intervocalic /f/ retained as [f]."""
        result = self.ast_w.resolve_grapheme("f", GP.INTERVOCALIC)
        self.assertEqual(result, ["f"])


# ═══════════════════════════════════════════════════════════════════════════
# Dialectal variation: Western, Eastern, Leonese
# ═══════════════════════════════════════════════════════════════════════════

class TestAsturianDialects(unittest.TestCase):
    """Validate dialectal differences across Asturian varieties."""

    def setUp(self):
        mod = _load_ast_module()
        self.central = mod.SPECS["ast"]
        self.western = mod.SPECS["ast-x-occidental"]
        self.eastern = mod.SPECS["ast-x-oriental"]
        self.leonese = mod.SPECS["ast-ES-x-leon"]

    def test_all_dialects_registered(self):
        """All four codes should be in SPECS."""
        mod = _load_ast_module()
        for code in ["ast", "ast-x-occidental", "ast-x-oriental", "ast-ES-x-leon"]:
            self.assertIn(code, mod.SPECS, f"Missing spec for {code}")

    def test_all_asturleonese_family(self):
        """All variants belong to the Asturleonese family."""
        for spec in [self.central, self.western, self.eastern, self.leonese]:
            self.assertEqual(spec.family, "Asturleonese")

    def test_dialects_parent_chain(self):
        """Western, Eastern, Leonese all have Central as parent."""
        self.assertEqual(self.western.parent, "ast")
        self.assertEqual(self.eastern.parent, "ast")
        self.assertEqual(self.leonese.parent, "ast")

    def test_central_parent_is_latin(self):
        """Central Asturian descends from (Vulgar) Latin."""
        self.assertEqual(self.central.parent, "la")

    def test_western_has_aspiration(self):
        """Western Asturian has [h] in grapheme and allophone inventories."""
        self.assertIn("h", self.western.allophones)
        self.assertEqual(self.western.graphemes["h"], ["h"])

    def test_western_has_che_vaqueira(self):
        """Western Asturian has ⟨ḷḷ⟩ che vaqueira grapheme."""
        self.assertIn("ḷḷ", self.western.graphemes)

    def test_eastern_yeismo_tendency(self):
        """Eastern Asturian shows incipient yeísmo: /ʎ/ → [ʝ]."""
        self.assertIn("ʝ", self.eastern.allophones.get("ʎ", []))

    def test_leonese_no_yeismo(self):
        """Leonese is conservative: /ʎ/ = [ʎ] only."""
        self.assertEqual(self.leonese.allophones["ʎ"], ["ʎ"])


# ═══════════════════════════════════════════════════════════════════════════
# Structural integrity
# ═══════════════════════════════════════════════════════════════════════════

class TestAsturianStructure(unittest.TestCase):
    """Validate structural properties of all Asturian specs."""

    def setUp(self):
        mod = _load_ast_module()
        self.specs = mod.SPECS

    def test_all_specs_are_language_specs(self):
        for code, spec in self.specs.items():
            self.assertIsInstance(spec, LanguageSpec, f"{code} is not LanguageSpec")

    def test_all_specs_have_names(self):
        for code, spec in self.specs.items():
            self.assertTrue(spec.name, f"{code} has empty name")

    def test_all_specs_have_nonempty_graphemes(self):
        for code, spec in self.specs.items():
            self.assertGreater(len(spec.graphemes), 10,
                               f"{code} has too few graphemes")

    def test_all_specs_have_nonempty_allophones(self):
        for code, spec in self.specs.items():
            self.assertGreater(len(spec.allophones), 5,
                               f"{code} has too few allophones")

    def test_central_has_ancestry(self):
        """Central Asturian should have full ancestry."""
        spec = self.specs["ast"]
        self.assertGreater(len(spec.ancestors), 0,
                           "Central Asturian should have ancestors")

    def test_central_has_positional_data(self):
        """Central Asturian should have positional grapheme data."""
        spec = self.specs["ast"]
        self.assertTrue(spec.has_positional_data())

    def test_positional_keys_exist_in_graphemes(self):
        """Positional grapheme keys must exist in base graphemes."""
        for code, spec in self.specs.items():
            if not spec.has_positional_data():
                continue
            for grapheme in spec.positional_grapheme_keys():
                self.assertIn(grapheme, spec.graphemes,
                              f"Positional key '{grapheme}' not in "
                              f"{code} graphemes")


# ═══════════════════════════════════════════════════════════════════════════
# Contrasts with Castilian Spanish
# ═══════════════════════════════════════════════════════════════════════════

class TestAsturianVsCastilian(unittest.TestCase):
    """Key phonological contrasts between Asturian and Castilian Spanish.

    These tests document the distinctive features that make Asturian
    a separate language from Castilian, not merely a dialect.
    """

    def setUp(self):
        mod = _load_ast_module()
        self.ast = mod.GRAPHEMES_AST
        self.ast_allophones = mod.ALLOPHONES_AST

    def test_x_postalveolar_not_velar(self):
        """Asturian ⟨x⟩ = /ʃ/ (postalveolar); Castilian ⟨j⟩ = /x/ (velar).
        This is a fundamental phonological difference.
        """
        self.assertEqual(self.ast["x"], ["ʃ"])
        # Verify /x/ is NOT in the allophone map as a native phoneme
        self.assertNotIn("x", self.ast_allophones,
                         "/x/ should not be a native allophone in Asturian")

    def test_g_before_vowels_not_fricative(self):
        """Asturian ⟨g⟩ = /ɡ/ only (never /x/).
        In Castilian, ⟨g⟩ before e,i = /x/. In Asturian, ⟨x⟩ = /ʃ/ instead.
        """
        self.assertNotIn("x", self.ast["g"])

    def test_palatal_lateral_preserved(self):
        """Asturian preserves /ʎ/ (no yeísmo, unlike most Castilian)."""
        self.assertEqual(self.ast["ll"], ["ʎ"])
        self.assertIn("ʎ", self.ast_allophones)
        # /ʎ/ has only [ʎ] in central, no [ʝ] merge
        self.assertEqual(self.ast_allophones["ʎ"], ["ʎ"])

    def test_ts_affricate_not_in_castilian(self):
        """⟨ts⟩ affricate is unique to Asturian (western)."""
        self.assertIn("ts", self.ast)
        self.assertEqual(self.ast["ts"], ["ts"])


if __name__ == "__main__":
    unittest.main()