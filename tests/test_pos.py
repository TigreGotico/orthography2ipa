"""Tests for positional grapheme system in orthography2ipa.types.

Tests the GraphemePosition enum, PositionalGrapheme2IPA type,
LanguageSpec.resolve_grapheme(), and backward compatibility.

Uses stdlib unittest — no external dependencies required.
"""
import os
import sys
import unittest
from dataclasses import FrozenInstanceError

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from orthography2ipa.types import (
    Ancestor,
    AncestorRole,
    GraphemePosition,
    LanguageSpec,
)


# ═══════════════════════════════════════════════════════════════════════════
# Helpers
# ═══════════════════════════════════════════════════════════════════════════

def make_minimal_spec():
    return LanguageSpec(
        code="xx", name="Test Language", family="TestFamily", script="Latin",
        graphemes={"a": ["a"], "b": ["b"], "s": ["s", "z"]},
        allophones={"a": ["a"], "b": ["b", "β"], "s": ["s", "z"]},
    )


def make_positional_spec():
    """Portuguese-like positional patterns."""
    return LanguageSpec(
        code="xx-pos", name="Test Positional", family="TestFamily",
        script="Latin",
        graphemes={
            "a": ["a"], "e": ["e", "ɛ"], "s": ["s", "z"], "l": ["l"],
            "t": ["t"], "r": ["ɾ"], "rr": ["ʁ"],
        },
        allophones={
            "a": ["a"], "e": ["e", "ɛ", "ɨ"],
            "s": ["s", "z", "ʃ", "ʒ"], "l": ["l", "w", "ɫ"],
            "t": ["t", "tʃ"], "ɾ": ["ɾ"], "ʁ": ["ʁ", "χ", "ʀ", "h"],
        },
        positional_graphemes={
            "s": {
                GraphemePosition.DEFAULT: ["s"],
                GraphemePosition.WORD_INITIAL: ["s"],
                GraphemePosition.INTERVOCALIC: ["z"],
                GraphemePosition.WORD_FINAL: ["ʃ"],
                GraphemePosition.INTERVOCALIC_CROSS_WORD: ["z"],
                GraphemePosition.CODA: ["ʃ", "ʒ"],
            },
            "l": {
                GraphemePosition.ONSET: ["l"],
                GraphemePosition.CODA: ["w"],
            },
            "t": {
                GraphemePosition.DEFAULT: ["t"],
                GraphemePosition.ONSET: ["t", "tʃ"],
            },
            "r": {
                GraphemePosition.WORD_INITIAL: ["ʁ"],
                GraphemePosition.INTERVOCALIC: ["ɾ"],
                GraphemePosition.CODA: ["ɾ", "ʁ"],
            },
        },
    )


def make_ancestry_positional_spec():
    return LanguageSpec(
        code="xx-complex", name="Complex Test Language",
        family="TestFamily", script="Latin",
        graphemes={"a": ["a"], "b": ["b"], "d": ["d"]},
        allophones={"a": ["a"], "b": ["b"], "d": ["d", "ð"]},
        parent="yy-parent",
        ancestors=(
            Ancestor("yy-parent", AncestorRole.PARENT, 0.80, "Primary descent"),
            Ancestor("zz-sub", AncestorRole.SUBSTRATE, 0.10, "Substrate lang"),
        ),
        positional_graphemes={
            "d": {
                GraphemePosition.WORD_INITIAL: ["d"],
                GraphemePosition.INTERVOCALIC: ["ð"],
                GraphemePosition.WORD_FINAL: ["t"],
            },
        },
    )


# ═══════════════════════════════════════════════════════════════════════════
# GraphemePosition enum
# ═══════════════════════════════════════════════════════════════════════════

class TestGraphemePosition(unittest.TestCase):

    def test_all_positions_exist(self):
        expected = {
            "default", "word_initial", "word_final",
            "intervocalic", "intervocalic_cross_word",
            "onset", "nucleus_stressed", "nucleus_unstressed", "coda",
            "pretonic", "posttonic"
        }
        actual = {p.value for p in GraphemePosition}
        self.assertEqual(actual, expected)

    def test_position_values_are_strings(self):
        for pos in GraphemePosition:
            self.assertIsInstance(pos.value, str)

    def test_position_lookup_by_value(self):
        self.assertEqual(GraphemePosition("word_initial"), GraphemePosition.WORD_INITIAL)
        self.assertEqual(GraphemePosition("coda"), GraphemePosition.CODA)

    def test_position_lookup_invalid(self):
        with self.assertRaises(ValueError):
            GraphemePosition("nonexistent")

    def test_positions_are_unique(self):
        values = [p.value for p in GraphemePosition]
        self.assertEqual(len(values), len(set(values)))

    def test_default_position_exists(self):
        self.assertEqual(GraphemePosition.DEFAULT.value, "default")


# ═══════════════════════════════════════════════════════════════════════════
# Backward compatibility
# ═══════════════════════════════════════════════════════════════════════════

class TestBackwardCompatibility(unittest.TestCase):

    def setUp(self):
        self.spec = make_minimal_spec()

    def test_no_positional_defaults_to_empty_dict(self):
        self.assertEqual(self.spec.positional_graphemes, {})

    def test_has_positional_data_false(self):
        self.assertFalse(self.spec.has_positional_data())

    def test_positional_grapheme_keys_empty(self):
        self.assertEqual(self.spec.positional_grapheme_keys(), frozenset())

    def test_positions_for_grapheme_empty(self):
        self.assertEqual(self.spec.positions_for_grapheme("s"), ())

    def test_resolve_default_falls_back(self):
        self.assertEqual(self.spec.resolve_grapheme("s"), ["s", "z"])
        self.assertEqual(self.spec.resolve_grapheme("a"), ["a"])

    def test_resolve_any_position_falls_back(self):
        self.assertEqual(
            self.spec.resolve_grapheme("s", GraphemePosition.WORD_INITIAL), ["s", "z"])
        self.assertEqual(
            self.spec.resolve_grapheme("s", GraphemePosition.CODA), ["s", "z"])

    def test_resolve_unknown_key_raises(self):
        with self.assertRaises(KeyError):
            self.spec.resolve_grapheme("xyz")

    def test_immutability(self):
        with self.assertRaises(FrozenInstanceError):
            self.spec.code = "yy"

    def test_none_positional_normalised(self):
        spec = LanguageSpec(
            code="xx", name="Test", family="TestFamily", script="Latin",
            graphemes={"a": ["a"]}, allophones={"a": ["a"]},
            positional_graphemes=None,
        )
        self.assertEqual(spec.positional_graphemes, {})


# ═══════════════════════════════════════════════════════════════════════════
# Positional grapheme resolution
# ═══════════════════════════════════════════════════════════════════════════

class TestPositionalResolution(unittest.TestCase):

    def setUp(self):
        self.spec = make_positional_spec()

    def test_has_positional_data_true(self):
        self.assertTrue(self.spec.has_positional_data())

    def test_positional_grapheme_keys(self):
        self.assertEqual(self.spec.positional_grapheme_keys(),
                         frozenset({"s", "l", "t", "r"}))

    def test_positions_for_s(self):
        positions = set(self.spec.positions_for_grapheme("s"))
        expected = {
            GraphemePosition.DEFAULT, GraphemePosition.WORD_INITIAL,
            GraphemePosition.INTERVOCALIC, GraphemePosition.WORD_FINAL,
            GraphemePosition.INTERVOCALIC_CROSS_WORD, GraphemePosition.CODA,
        }
        self.assertEqual(positions, expected)

    def test_resolve_default(self):
        self.assertEqual(self.spec.resolve_grapheme("s", GraphemePosition.DEFAULT), ["s"])

    def test_resolve_word_initial(self):
        self.assertEqual(self.spec.resolve_grapheme("s", GraphemePosition.WORD_INITIAL), ["s"])

    def test_resolve_intervocalic(self):
        self.assertEqual(self.spec.resolve_grapheme("s", GraphemePosition.INTERVOCALIC), ["z"])

    def test_resolve_word_final(self):
        self.assertEqual(self.spec.resolve_grapheme("s", GraphemePosition.WORD_FINAL), ["ʃ"])

    def test_resolve_coda(self):
        self.assertEqual(self.spec.resolve_grapheme("s", GraphemePosition.CODA), ["ʃ", "ʒ"])

    def test_resolve_cross_word(self):
        self.assertEqual(
            self.spec.resolve_grapheme("s", GraphemePosition.INTERVOCALIC_CROSS_WORD), ["z"])

    def test_resolve_l_onset(self):
        self.assertEqual(self.spec.resolve_grapheme("l", GraphemePosition.ONSET), ["l"])

    def test_resolve_l_coda(self):
        self.assertEqual(self.spec.resolve_grapheme("l", GraphemePosition.CODA), ["w"])

    def test_resolve_l_fallback_to_base(self):
        self.assertEqual(self.spec.resolve_grapheme("l", GraphemePosition.WORD_INITIAL), ["l"])

    def test_resolve_r_word_initial(self):
        self.assertEqual(self.spec.resolve_grapheme("r", GraphemePosition.WORD_INITIAL), ["ʁ"])

    def test_resolve_r_intervocalic(self):
        self.assertEqual(self.spec.resolve_grapheme("r", GraphemePosition.INTERVOCALIC), ["ɾ"])

    def test_resolve_non_positional_grapheme(self):
        self.assertEqual(self.spec.resolve_grapheme("a"), ["a"])
        self.assertEqual(self.spec.resolve_grapheme("a", GraphemePosition.CODA), ["a"])

    def test_resolve_digraph_fallback(self):
        self.assertEqual(self.spec.resolve_grapheme("rr"), ["ʁ"])

    def test_resolve_unknown_raises(self):
        with self.assertRaises(KeyError):
            self.spec.resolve_grapheme("xyz")

    def test_resolve_no_args_uses_default(self):
        self.assertEqual(self.spec.resolve_grapheme("s"), ["s"])


# ═══════════════════════════════════════════════════════════════════════════
# Positional + ancestry combined
# ═══════════════════════════════════════════════════════════════════════════

class TestPositionalWithAncestry(unittest.TestCase):

    def setUp(self):
        self.spec = make_ancestry_positional_spec()

    def test_ancestry_works(self):
        self.assertEqual(len(self.spec.get_ancestors()), 2)
        self.assertEqual(self.spec.primary_parent, "yy-parent")

    def test_positional_works(self):
        self.assertEqual(
            self.spec.resolve_grapheme("d", GraphemePosition.WORD_INITIAL), ["d"])
        self.assertEqual(
            self.spec.resolve_grapheme("d", GraphemePosition.INTERVOCALIC), ["ð"])
        self.assertEqual(
            self.spec.resolve_grapheme("d", GraphemePosition.WORD_FINAL), ["t"])

    def test_non_positional_grapheme(self):
        self.assertEqual(self.spec.resolve_grapheme("a"), ["a"])
        self.assertEqual(self.spec.resolve_grapheme("b"), ["b"])


# ═══════════════════════════════════════════════════════════════════════════
# Edge cases
# ═══════════════════════════════════════════════════════════════════════════

class TestEdgeCases(unittest.TestCase):

    def test_empty_positional_dict(self):
        spec = LanguageSpec(
            code="xx", name="Test", family="TestFamily", script="Latin",
            graphemes={"a": ["a"]}, allophones={"a": ["a"]},
            positional_graphemes={},
        )
        self.assertFalse(spec.has_positional_data())
        self.assertEqual(spec.resolve_grapheme("a"), ["a"])

    def test_positional_with_only_default(self):
        spec = LanguageSpec(
            code="xx", name="Test", family="TestFamily", script="Latin",
            graphemes={"a": ["a", "ə"]}, allophones={"a": ["a", "ə"]},
            positional_graphemes={"a": {GraphemePosition.DEFAULT: ["ɐ"]}},
        )
        self.assertEqual(spec.resolve_grapheme("a"), ["ɐ"])
        self.assertEqual(spec.resolve_grapheme("a", GraphemePosition.CODA), ["ɐ"])

    def test_positional_without_default_fallback(self):
        spec = LanguageSpec(
            code="xx", name="Test", family="TestFamily", script="Latin",
            graphemes={"a": ["a", "ə"]}, allophones={"a": ["a"]},
            positional_graphemes={"a": {GraphemePosition.CODA: ["ɐ"]}},
        )
        self.assertEqual(spec.resolve_grapheme("a", GraphemePosition.CODA), ["ɐ"])
        self.assertEqual(spec.resolve_grapheme("a", GraphemePosition.ONSET), ["a", "ə"])
        self.assertEqual(spec.resolve_grapheme("a"), ["a", "ə"])

    def test_nucleus_position(self):
        spec = LanguageSpec(
            code="xx", name="Test", family="TestFamily", script="Latin",
            graphemes={"e": ["e", "ɛ"]}, allophones={"e": ["e", "ɛ", "ɨ"]},
            positional_graphemes={"e": {GraphemePosition.NUCLEUS_UNSTRESSED: ["ɨ"]}},
        )
        self.assertEqual(spec.resolve_grapheme("e", GraphemePosition.NUCLEUS_UNSTRESSED), ["ɨ"])
        self.assertEqual(spec.resolve_grapheme("e", GraphemePosition.ONSET), ["e", "ɛ"])


# ═══════════════════════════════════════════════════════════════════════════
# Linguistic realism
# ═══════════════════════════════════════════════════════════════════════════

class TestLinguisticRealism(unittest.TestCase):

    def test_german_auslautverhaertung(self):
        spec = LanguageSpec(
            code="de-DE", name="German", family="Germanic", script="Latin",
            graphemes={"d": ["d"], "t": ["t"]},
            allophones={"d": ["d", "t"], "t": ["t", "tʰ"]},
            positional_graphemes={
                "d": {
                    GraphemePosition.DEFAULT: ["d"],
                    GraphemePosition.WORD_FINAL: ["t"],
                },
            },
        )
        self.assertEqual(spec.resolve_grapheme("d", GraphemePosition.WORD_INITIAL), ["d"])
        self.assertEqual(spec.resolve_grapheme("d", GraphemePosition.WORD_FINAL), ["t"])

    def test_spanish_lenition(self):
        spec = LanguageSpec(
            code="es-ES", name="Castilian Spanish", family="Romance",
            script="Latin",
            graphemes={"b": ["b"], "d": ["d"]},
            allophones={"b": ["b", "β"], "d": ["d", "ð"]},
            positional_graphemes={
                "b": {
                    GraphemePosition.DEFAULT: ["b"],
                    GraphemePosition.INTERVOCALIC: ["β"],
                },
                "d": {
                    GraphemePosition.DEFAULT: ["d"],
                    GraphemePosition.INTERVOCALIC: ["ð"],
                    GraphemePosition.WORD_FINAL: ["ð", "∅"],
                },
            },
        )
        self.assertEqual(spec.resolve_grapheme("b", GraphemePosition.INTERVOCALIC), ["β"])
        self.assertEqual(spec.resolve_grapheme("d", GraphemePosition.INTERVOCALIC), ["ð"])
        self.assertEqual(spec.resolve_grapheme("d", GraphemePosition.WORD_FINAL), ["ð", "∅"])

    def test_english_l_allophony(self):
        spec = LanguageSpec(
            code="pt-PT", name="European Portuguese", family="Romance", script="Latin",
            graphemes={"l": ["l"]},
            allophones={"l": ["l", "ɫ"]},
            positional_graphemes={
                "l": {
                    GraphemePosition.ONSET: ["l"],
                    GraphemePosition.CODA: ["ɫ"],
                },
            },
        )
        self.assertEqual(spec.resolve_grapheme("l", GraphemePosition.ONSET), ["l"])
        self.assertEqual(spec.resolve_grapheme("l", GraphemePosition.CODA), ["ɫ"])

    def test_portuguese_s_distribution(self):
        spec = LanguageSpec(
            code="pt-PT", name="European Portuguese", family="Romance",
            script="Latin",
            graphemes={"s": ["s", "z", "ʃ", "ʒ"]},
            allophones={"s": ["s"], "z": ["z"], "ʃ": ["ʃ"], "ʒ": ["ʒ"]},
            positional_graphemes={
                "s": {
                    GraphemePosition.WORD_INITIAL: ["s"],
                    GraphemePosition.INTERVOCALIC: ["z"],
                    GraphemePosition.CODA: ["ʃ"],
                    GraphemePosition.WORD_FINAL: ["ʃ"],
                    GraphemePosition.INTERVOCALIC_CROSS_WORD: ["z"],
                },
            },
        )
        self.assertEqual(spec.resolve_grapheme("s", GraphemePosition.WORD_INITIAL), ["s"])
        self.assertEqual(spec.resolve_grapheme("s", GraphemePosition.INTERVOCALIC), ["z"])
        self.assertEqual(spec.resolve_grapheme("s", GraphemePosition.CODA), ["ʃ"])
        self.assertEqual(
            spec.resolve_grapheme("s", GraphemePosition.INTERVOCALIC_CROSS_WORD), ["z"])

    def test_brazilian_portuguese_l_vocalization(self):
        spec = LanguageSpec(
            code="pt-BR", name="Brazilian Portuguese", family="Romance",
            script="Latin",
            graphemes={"l": ["l"]},
            allophones={"l": ["l", "w"]},
            positional_graphemes={
                "l": {
                    GraphemePosition.ONSET: ["l"],
                    GraphemePosition.CODA: ["w"],
                },
            },
        )
        self.assertEqual(spec.resolve_grapheme("l", GraphemePosition.ONSET), ["l"])
        self.assertEqual(spec.resolve_grapheme("l", GraphemePosition.CODA), ["w"])

    def test_korean_coda_neutralization(self):
        spec = LanguageSpec(
            code="ko-KR", name="Korean", family="Koreanic", script="Hangul",
            graphemes={"ㄱ": ["k"], "ㄷ": ["t"], "ㅂ": ["p"]},
            allophones={"k": ["k", "k̚"], "t": ["t", "t̚"], "p": ["p", "p̚"]},
            positional_graphemes={
                "ㄱ": {GraphemePosition.ONSET: ["k"], GraphemePosition.CODA: ["k̚"]},
                "ㄷ": {GraphemePosition.ONSET: ["t"], GraphemePosition.CODA: ["t̚"]},
                "ㅂ": {GraphemePosition.ONSET: ["p"], GraphemePosition.CODA: ["p̚"]},
            },
        )
        self.assertEqual(spec.resolve_grapheme("ㄱ", GraphemePosition.ONSET), ["k"])
        self.assertEqual(spec.resolve_grapheme("ㄱ", GraphemePosition.CODA), ["k̚"])


# ═══════════════════════════════════════════════════════════════════════════
# Ancestor tests (preserved from original)
# ═══════════════════════════════════════════════════════════════════════════

class TestAncestorRole(unittest.TestCase):
    def test_all_roles_exist(self):
        expected = {"parent", "substrate", "superstrate", "adstrate",
                    "lexifier", "creole_base"}
        self.assertEqual({r.value for r in AncestorRole}, expected)


class TestAncestor(unittest.TestCase):
    def test_repr(self):
        a = Ancestor("la", AncestorRole.PARENT, 0.85, "Latin parent")
        self.assertIn("la", repr(a))
        self.assertIn("parent", repr(a))

    def test_immutability(self):
        a = Ancestor("la", AncestorRole.PARENT, 0.85)
        with self.assertRaises(FrozenInstanceError):
            a.code = "xx"


class TestLanguageSpecAncestry(unittest.TestCase):
    def test_get_ancestors_from_parent_field(self):
        spec = LanguageSpec(
            code="xx-d", name="Test Dialect", family="TestFamily",
            script="Latin", graphemes={"a": ["a"]}, allophones={"a": ["a"]},
            parent="xx",
        )
        ancestors = spec.get_ancestors()
        self.assertEqual(len(ancestors), 1)
        self.assertEqual(ancestors[0].code, "xx")

    def test_primary_parent(self):
        spec = make_ancestry_positional_spec()
        self.assertEqual(spec.primary_parent, "yy-parent")

    def test_no_parent_no_ancestors(self):
        spec = make_minimal_spec()
        self.assertIsNone(spec.primary_parent)
        self.assertEqual(spec.get_ancestors(), ())


if __name__ == "__main__":
    unittest.main()
