"""Cited regression tests for the Mirandese / Asturleonese fix round.

Each class is one lead from the blind-verification arbitration (page-pinned to
Leite de Vasconcelos, *Estudos de Philologia Mirandesa* vols I–II, and the
Convenção Ortográfica da Língua Mirandesa 1999 / Primeiro Aditamento 2000),
cross-checked against the lect-specific primary sources already cited in the
specs (Macias 2003 for Rionorese; Maia 1986 for the medieval sibilants).

Lead IDs:
  P1 = mwl article/clitic ⟨l⟩ stays [l] (not palatalised [ʎ]); function words
       are prosodic clitics (Convenção §L; §Acento)
  P2 = ⟨qua/quo⟩ keeps the [w] glide; ⟨que/qui⟩ has silent u
  P3 = rionor/guadramil ⟨ç⟩/⟨c⟩+e,i/⟨z⟩ = seseo [s] (Vasconcelos EPM II p.54),
       Sanabria keeps [θ]
  P4 = rionor/guadramil native ⟨tch⟩ = [tʃ] (Macias 2003 p.26)
  P5 = mwl/ifanes ⟨ie⟩/reduced ⟨an,en⟩ nasalise before a coda nasal
  P6 = mwl predorsal ⟨ç,c⟩ [s] stays distinct from apical ⟨s,ss⟩ [s̺]
  P7 = medieval ⟨z⟩ = the affricate [d͡z] of the 4-way system (Maia 1986)
"""
import pytest
from orthography2ipa import G2P


@pytest.fixture(scope="module")
def mwl():
    return G2P("mwl")


@pytest.fixture(scope="module")
def ifanes():
    return G2P("mwl-x-ifanes")


@pytest.fixture(scope="module")
def sendim():
    return G2P("mwl-x-sendim")


@pytest.fixture(scope="module")
def medieval():
    return G2P("ast-PT-x-medieval")


@pytest.fixture(scope="module")
def rionor():
    return G2P("ast-PT-x-rionor")


@pytest.fixture(scope="module")
def guadramil():
    return G2P("ast-PT-x-guadramil")


@pytest.fixture(scope="module")
def sanabria():
    return G2P("ast-x-sanabria")


# ── P1: article/clitic ⟨l⟩ gating ────────────────────────────────────────────
class TestP1ArticleClitic:
    """Convenção §L: word-initial ⟨l⟩ palatalises to /ʎ/ in the traditional
    lexicon, but bare /l/ survives in the definite article (l/la/ls/las), the
    object clitic, loanwords and proper nouns — a closed lexical set."""

    def test_article_l_stays_l(self, mwl):
        assert mwl.transcribe("l") == "l"

    def test_article_la_stays_l_unstressed(self, mwl):
        # [lɐ], not [ˈʎɐ]: onset [l] + reduced [ɐ], no word stress (proclitic)
        assert mwl.transcribe("la") == "lɐ"

    def test_article_las_stays_l(self, mwl):
        assert mwl.transcribe("las") == "lɐs̺"

    def test_loanword_litro_stays_l(self, mwl):
        assert mwl.transcribe("litro") == "ˈlitɾu"

    def test_etymological_lh_keeps_palatal(self, mwl):
        # the traditional lexicon still palatalises: ⟨lh⟩ words are unaffected
        assert "ʎ" in mwl.transcribe("lhunes")
        assert "ʎ" in mwl.transcribe("lhuna")

    def test_ifanes_inherits_article_exceptions(self, ifanes):
        assert ifanes.transcribe("litro") == "ˈlitɾu"
        assert ifanes.transcribe("la") == "lɐ"

    def test_article_is_cliticless_in_sentence(self, mwl):
        # "Bou a l doutor l lhunes a la tarde." — l/la carry no ˈ, lhunes keeps ʎ
        out = mwl.transcribe("Bou a l doutor l lhunes a la tarde.")
        assert " l " in f" {out} "          # bare [l] article, unstressed
        assert "ʎunɨs̺" in out               # lhunes still palatal
        assert "ˈʎ " not in out              # no stressed palatal article


# ── P2: ⟨qua/quo⟩ glide retention ─────────────────────────────────────────────
class TestP2QuGlide:
    """⟨qu⟩ before a/o keeps the labiovelar glide [kw]; before e/i the u is
    silent [k] (the #519 Portuguese digraph fix, reaching the mwl/ast base)."""

    def test_mwl_quantos_keeps_glide(self, mwl):
        assert mwl.transcribe("quantos") == "ˈkwɐ̃tus̺"

    def test_medieval_quarenta_keeps_glide(self, medieval):
        assert medieval.transcribe("quarenta") == "kwaɾẽta"

    def test_medieval_quando_keeps_glide(self, medieval):
        assert medieval.transcribe("quando").startswith("kw")

    def test_silent_u_before_front_vowel(self, mwl):
        assert mwl.transcribe("quilo") == "ˈkilu"      # qu+i → [k]
        assert mwl.transcribe("queiso").startswith("ˈk") and \
            "kw" not in mwl.transcribe("queiso")        # qu+e → [k]


# ── P3: seseo in the NW-corner falares ───────────────────────────────────────
class TestP3Seseo:
    """Vasconcelos EPM II p.54: guadramilês (and the adjacent Rio de Onor
    speech) merge the predorsal sibilant with Galician [s] (seseo), not the
    Castilian interdental [θ] that the Sanabria continuum keeps."""

    def test_rionor_ç_is_s(self, rionor):
        assert rionor.transcribe("çapatos") == "sapatos"

    def test_rionor_soft_c_is_s(self, rionor):
        assert rionor.transcribe("ceu") == "sew"
        assert rionor.transcribe("cena") == "sena"

    def test_guadramil_inherits_seseo(self, guadramil):
        assert guadramil.transcribe("çapatos") == "sapatos"
        assert guadramil.transcribe("berças") == "beɾsas"

    def test_no_interdental_left(self, rionor, guadramil):
        assert "θ" not in rionor.transcribe("çapatos ceu berças")
        assert "θ" not in guadramil.transcribe("çapatos ceu berças")

    def test_sanabria_keeps_interdental(self, sanabria):
        # the eastern continuum is NOT seseante — [θ] is retained
        assert "θ" in sanabria.transcribe("çapatos")
        assert sanabria.transcribe("ceo").startswith("θ")


# ── P4: native ⟨tch⟩ affricate ───────────────────────────────────────────────
class TestP4TchAffricate:
    """Macias 2003 p.26: Rionorese writes the native PL-/CL- affricate as
    ⟨tch⟩ = [tʃ] and reserves ⟨ch⟩ = [ʃ] for Portuguese loans. 'chegar'
    (< plicare) is native, so its Rionorese spelling is 'tchegar'."""

    def test_tchegares_is_affricate(self, rionor, guadramil):
        assert rionor.transcribe("tchegares") == "tʃeɡaɾes"
        assert guadramil.transcribe("tchegares") == "tʃeɡaɾes"

    def test_tchama_word_initial_affricate(self, rionor):
        assert rionor.transcribe("Tchama").startswith("tʃ")

    def test_plain_ch_stays_fricative_for_loans(self, rionor):
        # the cited Macias distinction is preserved: ⟨ch⟩ (no t-) = [ʃ]
        assert rionor.transcribe("chegares") == "ʃeɡaɾes"


# ── P5: nasalisation before a coda nasal ─────────────────────────────────────
class TestP5Nasalisation:
    """Convenção §Nasalidade + Mateus & d'Andrade 2000 (close-mid nasals):
    the Leonese diphthong ⟨ie⟩ and the reduced unstressed ⟨an/en⟩ nasalise
    before a tautosyllabic coda nasal instead of dropping the nasal."""

    def test_bien_nasalises(self, mwl, ifanes):
        assert mwl.transcribe("bien") == "ˈbjẽ"
        assert ifanes.transcribe("bien") == "ˈbjẽ"

    def test_quien_keeps_oral_plus_n(self, mwl, ifanes):
        # the interrogative is the lexical exception: [kjɛn], not [kjẽ]
        assert mwl.transcribe("quien") == "ˈkjɛn"
        assert ifanes.transcribe("quien") == "ˈkjɛn"

    def test_sendim_monophthong_path(self, sendim):
        # Sendinês monophthongises ⟨ie⟩→[i] first, so it nasalises to [ĩ]
        assert sendim.transcribe("bien") == "ˈbĩ"
        assert sendim.transcribe("quien") == "ˈkĩ"

    def test_unstressed_an_nasalises(self, mwl):
        # the proclitic preposition reduces to [ɐ] yet still nasalises: [ɐ̃]
        assert mwl.transcribe("an") == "ɐ̃"

    def test_uo_diphthong_nasalises(self, mwl):
        assert mwl.transcribe("fuonte") == "ˈfwõtɨ"


# ── P6: predorsal vs apical sibilant contrast ────────────────────────────────
class TestP6SibilantContrast:
    """Vasconcelos EPM I p.165: Mirandese keeps ⟨ç⟩/⟨c⟩ (predorsal, plain [s])
    distinct from ⟨s,ss⟩ (apical [s̺]); the two do not merge."""

    def test_predorsal_c_is_plain_s(self, mwl):
        assert "s" in mwl.transcribe("cielo")
        assert "s̺" not in mwl.transcribe("cielo")

    def test_apical_s_is_marked(self, mwl):
        assert "s̺" in mwl.transcribe("sol")

    def test_predorsal_and_apical_distinct(self, mwl):
        # 'calece' (soft c → predorsal [s]) vs 'sol' (apical [s̺]) differ
        assert "lesɨ" in mwl.transcribe("calece")   # plain [s]
        assert "s̺" in mwl.transcribe("sol")          # apical [s̺]


# ── P7: medieval ⟨z⟩ affricate ───────────────────────────────────────────────
class TestP7MedievalZ:
    """Maia 1986: the medieval 4-way sibilant system has the voiced predorsal
    affricate /d͡z/ ⟨z⟩ parallel to /t͡s/ ⟨ç,c⟩; ⟨z⟩ does not deaffricate."""

    def test_z_word_final_affricate(self, medieval):
        assert medieval.transcribe("luz") == "lud͡z"
        assert medieval.transcribe("reluz") == "relud͡z"

    def test_z_intervocalic_affricate(self, medieval):
        assert "d͡z" in medieval.transcribe("dozena")

    def test_z_parallels_c_affricate(self, medieval):
        # ⟨ç⟩ is [t͡s]; ⟨z⟩ is its voiced counterpart [d͡z] — both affricates
        assert "t͡s" in medieval.transcribe("çapatos")
        assert "d͡z" in medieval.transcribe("luz")

    def test_mwl_z_is_plain_fricative(self, mwl):
        # Mirandese lost the affricate: ⟨z⟩ is the plain voiced /z/
        assert mwl.transcribe("luzes").count("d͡z") == 0
        assert "z" in mwl.transcribe("luzes")
