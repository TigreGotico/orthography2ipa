"""Mainland Scandinavian (da / nb / sv) — cited word→IPA behaviour.

The three specs share one architecture, expressed entirely in spec DATA
(no engine changes):

* **Quantity.** Danish, Swedish and Norwegian all have complementary
  length in the stressed syllable: a long vowel is followed by a short
  consonant, a short vowel by a long consonant or a cluster
  (Riad 2014 for Swedish; Kristoffersen 2000 for Norwegian;
  Basbøll 2005 for Danish). This is encoded by giving doubled letters
  and consonant clusters their own grapheme keys (⟨tt⟩ → /tː/,
  ⟨st⟩ → /st/), selecting the long vowel in ``nucleus_stressed`` and
  shortening it again with ``allophone_rules`` whose
  ``followed_by_phoneme`` lists exactly those geminate/cluster phonemes.
* **Reduction.** Unstressed ⟨e⟩ is [ə] in Danish and Norwegian.
* **Softening / retroflexion.** ⟨k g sk⟩ palatalise before a front
  vowel in Swedish and Norwegian (not in Danish, where ⟨sk⟩ is [sɡ]);
  ⟨r⟩ + coronal gives the retroflex series in Swedish and Norwegian.

Danish stød and the Swedish/Norwegian tonemes are suprasegmental and are
deliberately NOT produced.
"""
from orthography2ipa import G2P


def _ipa(lang: str, word: str) -> str:
    """Transcription without the primary-stress mark."""
    return G2P(lang).transcribe_word(word).replace("ˈ", "")


class TestDanishScandinavian:
    """Danish (Grønnum 2005; Basbøll 2005; Wikipedia 'Danish phonology')."""

    def test_soft_d_intervocalic_and_final(self):
        # /d/ after a vowel is the soft-d approximant [ð]
        assert _ipa("da", "mad") == "maːð"
        assert _ipa("da", "gade") == "ɡaːðə"

    def test_silent_d_after_n_and_l(self):
        # ⟨d⟩ is silent after ⟨n⟩/⟨l⟩ — and the cluster still shortens the vowel
        assert _ipa("da", "mand") == "man"
        assert _ipa("da", "guld") == "ɡul"

    def test_silent_d_after_r(self):
        assert _ipa("da", "gård") == "ɡɔʁ"

    def test_no_aspiration_after_s(self):
        # ⟨sk⟩/⟨st⟩ → [sɡ]/[sd]: Danish does not palatalise ⟨sk⟩
        assert _ipa("da", "skole") == "sɡoːlə"
        assert _ipa("da", "stol") == "sdoːl"

    def test_unstressed_e_is_schwa(self):
        assert _ipa("da", "tale") == "taːlə"

    def test_quantity_long_before_single_consonant(self):
        assert _ipa("da", "måne") == "mɔːnə"

    def test_quantity_short_before_doubled_letter_and_no_geminates(self):
        # doubled letters signal a short vowel; Danish has no long consonants
        assert _ipa("da", "hoppe") == "hɔpə"

    def test_stod_is_not_transcribed(self):
        assert "ˀ" not in G2P("da").transcribe_word("hus")


class TestSwedishScandinavian:
    """Swedish (Riad 2014; Engstrand 1999; Wikipedia 'Swedish phonology')."""

    def test_complementary_quantity(self):
        assert _ipa("sv", "tak") == "tɑːk"      # long V + short C
        assert _ipa("sv", "tack") == "takː"     # short V + long C
        assert _ipa("sv", "katt") == "katː"

    def test_short_vowel_before_cluster(self):
        assert _ipa("sv", "flicka") == "²flɪkːa"

    def test_softening_before_front_vowel(self):
        assert _ipa("sv", "kista") == "²ɕɪsta"   # ⟨k⟩ → [ɕ]
        assert _ipa("sv", "gäst") == "jɛst"     # ⟨g⟩ → [j] before ⟨ä⟩
        assert _ipa("sv", "sjö") == "ɧøː"

    def test_no_softening_before_back_vowel(self):
        assert _ipa("sv", "kort").startswith("k")

    def test_retroflexion(self):
        # Retroflexion (rn/rd/rt/rl/rs -> ɳ ɖ ʈ ɭ ʂ) is real in Central Swedish
        # and is kept as sv-x-rikssvenska's own data (Elert 1994), but applying
        # it unconditionally in the base "sv" spec actively hurt PER against
        # the wikipron gold convention, which mostly spells the cluster out
        # rather than retroflexing it (the beat-espeak-germanic data campaign
        # measured this directly) -- so base "sv" no longer retroflexes by
        # default.
        assert _ipa("sv", "barn") == "barn"
        assert _ipa("sv-x-rikssvenska", "barn").endswith("ɳ")
        assert _ipa("sv-x-rikssvenska", "fars").endswith("ʂ")

    def test_pre_r_lowering(self):
        assert _ipa("sv", "bära") == "²bæːra"

    def test_no_final_devoicing(self):
        # Swedish keeps final /b d ɡ/ (unlike German/Catalan)
        assert _ipa("sv", "hund").endswith("d")


class TestNorwegianScandinavian:
    """Norwegian Bokmål (Kristoffersen 2000; Wikipedia 'Norwegian phonology')."""

    def test_quantity(self):
        assert _ipa("nb", "hus") == "hʉːs"
        assert _ipa("nb", "katt") == "katː"
        assert _ipa("nb", "gate") == "ɡɑːtə"    # short ⟨a⟩ = [a], long = [ɑː]

    def test_unstressed_e_is_schwa(self):
        assert _ipa("nb", "tale") == "tɑːlə"

    def test_retroflexion(self):
        assert _ipa("nb", "barn") == "bɑːɳ"
        assert _ipa("nb", "bord") == "buːɖ"

    def test_softening_before_front_vowel(self):
        assert _ipa("nb", "kjøre") == "çøːɾə"
        assert _ipa("nb", "skip") == "ʃiːp"

    def test_silent_letters(self):
        assert _ipa("nb", "hvem") == "ʋeːm"     # ⟨hv⟩ → [ʋ]
        assert _ipa("nb", "land") == "lan"      # final ⟨d⟩ silent after ⟨n⟩
        assert _ipa("nb", "kveld") == "kʋɛl"

    def test_v_is_approximant(self):
        assert _ipa("nb", "vann") == "ʋanː"

    def test_tonemes_are_not_transcribed(self):
        out = G2P("nb").transcribe_word("bønder")
        assert "²" not in out and "¹" not in out


class TestComplementaryQuantity:
    """Quantity comes from the ``consonant_cluster`` context, not from
    enumerated cluster graphemes.

    A stressed vowel is long in an open syllable and short before a
    consonant cluster or a geminate (Riad 2014; Kristoffersen 2000;
    Basbøll 2005). The minimal pairs below differ only in the coda, so
    they isolate the quantity rule itself.
    """

    def test_swedish_minimal_pair(self):
        assert _ipa("sv", "vit") == "viːt"      # single coda consonant
        assert _ipa("sv", "vitt") == "vɪtː"     # geminate shortens

    def test_norwegian_minimal_pair(self):
        assert _ipa("nb", "tak") == "tɑːk"
        assert _ipa("nb", "takk") == "takː"

    def test_danish_shortens_before_cluster(self):
        assert _ipa("da", "hus") == "huːs"      # open syllable
        assert _ipa("da", "hest") == "hɛsd"     # cluster shortens

    def test_no_enumerated_cluster_graphemes(self):
        """A cluster is a context, never a grapheme.

        ``bf``/``bk``/``dp`` are not units of any Scandinavian
        orthography; they only ever existed to stand in for the missing
        cluster context.
        """
        for lang in ("da", "sv", "nb"):
            graphemes = G2P(lang).spec.graphemes
            for fake in ("bf", "bk", "dp", "fb", "bl", "gm"):
                assert fake not in graphemes, f"{lang}: {fake!r} is not a grapheme"


class TestSwedishBeatEspeakWave:
    """Riad 2014-cited classes added by the beat-espeak Swedish wave.

    Each pin is a documented example from the rule notes; the guards
    (mer, vinter, bil) prove the conditions don't overreach.
    """

    def _t(self, word):
        from orthography2ipa import G2P
        return G2P("sv").transcribe(word)

    def test_short_before_ng_nk_sk(self):
        assert self._t("säng") == "ˈsɛŋ"
        assert self._t("lång") == "ˈlɔŋ"
        assert self._t("sjunga") == "²ɧɵŋa"
        assert self._t("fisk") == "ˈfɪsk"
        assert self._t("tänka") == "²tɛŋka"

    def test_long_kept_in_open_syllables(self):
        assert self._t("bil") == "ˈbiːl"
        assert self._t("tak") == "ˈtɑːk"
        assert self._t("hat") == "ˈhɑːt"

    def test_short_diphthong_before_j(self):
        assert self._t("aj") == "ˈaj"
        assert self._t("hej") == "ˈhɛj"
        assert self._t("maj") == "ˈmaj"
        assert self._t("nöjd") == "ˈnœjd"

    def test_pre_r_lowering_stressed_only(self):
        assert self._t("bert") == "ˈbært"
        assert self._t("ärt") == "ˈært"
        assert self._t("är") == "ˈæːr"
        assert self._t("lära") == "²læːra"
        assert self._t("herr") == "ˈhærː"
        assert self._t("mer") == "ˈmeːr"          # single r, /e/: no lowering
        assert self._t("vinter") == "ˈvɪntɛr"     # unstressed -er keeps [ɛr]

    def test_unstressed_o_reduction(self):
        assert self._t("bravo").endswith("vʊ")
        assert self._t("avokado").endswith("dʊ")
        assert self._t("afton").endswith("tɔn")   # closed syllable keeps [ɔ]
        assert self._t("dator").endswith("tɔr")

    def test_accent2_marking(self):
        assert self._t("vecka").startswith("²")
        assert self._t("tala").startswith("²")
        assert self._t("vinter").startswith("ˈ")  # accent 1: plain stress mark
        assert self._t("bil").startswith("ˈ")     # monosyllable: never accent 2


class TestProsodyMarkScoringBoundary:
    """PER strips pitch-accent digits ONLY for specs that declare them.

    Swedish declares stress.accent2_mark, so ¹/² are unscored prosody there;
    Yi (ycl) gold writes lexical tone with the same superscripts, and for it
    they are segments. Blanket-stripping cost ycl +0.076 PER (caught by the
    benchmark-regression CI gate) — this pins the boundary.
    """

    def test_prosody_marks_per_language(self):
        import importlib.util
        from pathlib import Path
        spec = importlib.util.spec_from_file_location(
            "bm", Path(__file__).parent.parent / "scripts" / "benchmark.py")
        bm = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(bm)
        assert bm._prosody_marks("sv") == "¹²"
        assert bm._prosody_marks("ycl") == ""
        assert bm._prosody_marks("de") == ""
        assert bm.normalize("²vɛkːa", True, True,
                            extra_strip="¹²") == "vɛkka"
        assert bm.normalize("a³³pʰi²¹", True, True) == "a³³pʰi²¹"
