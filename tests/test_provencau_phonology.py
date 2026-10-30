"""Provençal (oc-x-provencau) — the letters that diverge from Lengadocian,
and the letters that must NOT.

The spec is a child of ``oc`` and writes only the values the Lo Congrès
graphie-phonie tables give SEPARATELY for provençal. Everything else is
inherited, so this file tests two things that are equally easy to get wrong:

* each cited divergence reaches the transcription, and
* each value the source says nothing about is still the parent's.

The second half is not decoration. ``positional_graphemes`` merges one level
deep, so a child entry REPLACES the parent's whole context dict for that
letter. A first draft of the spec wrote the word-final line alone for ⟨c⟩,
⟨d⟩, ⟨g⟩ and ⟨r⟩ and silently lost ⟨c⟩ before a front vowel, the trill of
word-initial ⟨r⟩, and the intervocalic lenition — none of which is a
Provençal feature.

Values per Lo Congrès, "Relacions grafia-fonia / Relations graphie-phonie"
(consonant table, vowel table and diphthong table), which names provençal
against each general Occitan value.
"""
import pytest

from orthography2ipa import get, transcribe


PROV = "oc-x-provencau"
LENG = "oc"


def prov(word):
    return transcribe(word, lang=PROV)


def leng(word):
    return transcribe(word, lang=LENG)


class TestSpecShape:
    """The spec is a child that overrides, not a copy."""

    def test_it_is_a_child_of_lengadocian(self):
        spec = get(PROV)
        assert spec.parent == "oc"
        assert spec.name == "Provençal (Occitan)"

    def test_it_inherits_the_whole_grapheme_table(self):
        # graphemes_base pulls the parent's 68 entries in; the file itself
        # writes only the three that diverge.
        assert len(get(PROV).graphemes) == len(get(LENG).graphemes)


class TestConsonantsThatDiverge:

    def test_v_is_not_betacised(self):
        # Betacism is Gascon and Lengadocian. Provençal keeps /v/ apart
        # from /b/, word-initially and between vowels.
        assert prov("vila") == "ˈvilɔ"
        assert leng("vila") == "ˈbilɔ"
        assert prov("vertat").startswith("v")

    @pytest.mark.parametrize("word,expect", [
        ("vertat", "veɾˈta"),    # final -t silent
        ("grand", "ˈɡɾan"),      # final -d silent
    ])
    def test_final_stops_are_silent(self, word, expect):
        assert prov(word) == expect
        assert prov(word) != leng(word)

    @pytest.mark.parametrize("word,expect", [
        ("patz", "ˈpas"),
        ("crotz", "ˈkɾus"),
    ])
    def test_final_tz_is_s(self, word, expect):
        # [s] in Provençal against the [t͡s] of the general value.
        assert prov(word) == expect

    def test_final_n_is_kept(self):
        # The direction a blanket "Provençal loses its final consonants"
        # would get backwards: the parent DROPS this ⟨-n⟩ and Provençal
        # pronounces it.
        assert prov("pichon") == "piˈtʃun"
        assert leng("pichon") == "piˈtʃu"

    def test_final_r_is_uvular(self):
        # Same direction again: kept, and as [ʀ].
        assert prov("melhor") == "meˈʎuʀ"
        assert leng("melhor") == "meˈʎu"


class TestVowelsAndDiphthongsThatDiverge:

    def test_atone_ai_is_ej(self):
        # ⟨ai⟩ is [aj] under the stress and [ej] when atone.
        assert prov("maison") == "mejˈzun"
        assert prov("paire") == "ˈpajɾe"

    def test_oi_is_wej(self):
        assert prov("coire") == "ˈkwejɾe"
        assert leng("coire") == "ˈkujɾe"


class TestWhatMustStayInherited:
    """Every case here is a value the source gives NO separate Provençal
    reading for, so the parent's value must survive the override."""

    def test_c_before_a_front_vowel_is_still_s(self):
        assert prov("cigala") == leng("cigala") == "siˈɣalɔ"

    def test_word_initial_r_is_still_a_trill(self):
        assert prov("roge") == leng("roge") == "ˈrudʒe"

    def test_intervocalic_lenition_still_applies(self):
        assert prov("aiga") == leng("aiga") == "ˈajɣɔ"
        assert prov("codonh") == leng("codonh") == "kuˈðun"

    def test_the_front_vowel_series_is_untouched(self):
        # ⟨cc⟩ before a front vowel is [t͡s] in both, so the word differs
        # only by the final ⟨-n⟩ the dialect keeps.
        assert prov("diccionari") == leng("diccionari") == "ditsjuˈnaɾi"
        assert prov("escòla") == leng("escòla") == "esˈkɔlɔ"

    def test_occitan_differs_only_by_the_final_n(self):
        # The name of the language is the compact case: same [t͡s] from the
        # inherited ⟨cc⟩ rule, plus the ⟨-n⟩ this dialect pronounces.
        assert leng("occitan") == "utsiˈta"
        assert prov("occitan") == "utsiˈtan"

    def test_final_unstressed_a_is_still_open_o(self):
        assert prov("filha") == leng("filha") == "ˈfiʎɔ"
