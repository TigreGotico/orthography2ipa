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
        assert _ipa("sv", "flicka") == "flɪkːa"

    def test_softening_before_front_vowel(self):
        assert _ipa("sv", "kista") == "ɕɪsta"   # ⟨k⟩ → [ɕ]
        assert _ipa("sv", "gäst") == "jɛst"     # ⟨g⟩ → [j] before ⟨ä⟩
        assert _ipa("sv", "sjö") == "ɧøː"

    def test_no_softening_before_back_vowel(self):
        assert _ipa("sv", "kort").startswith("k")

    def test_retroflexion(self):
        assert _ipa("sv", "barn") == "bɑːɳ"     # rn → [ɳ]
        assert _ipa("sv", "fars").endswith("ʂ")  # rs → [ʂ]

    def test_pre_r_lowering(self):
        assert _ipa("sv", "bära") == "bæːra"

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
