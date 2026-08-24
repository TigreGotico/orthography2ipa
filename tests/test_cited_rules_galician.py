"""Cited-rule tests for standard Galician (``gl``).

Every test isolates ONE claim the ``gl`` spec makes with a citation, on a real
word, and asserts exactly the segment the citation asserts. Each rule is paired
with the counter-case the same citation predicts, so a rule that over-applies
fails here rather than in the benchmark.

Sources asserted: Regueira 2010 (*Dicionario de pronuncia da lingua galega*),
Freixeiro Mato 1998 (*Gramática da lingua galega I: Fonética e fonoloxía*),
Álvarez & Xove 2002, and the RAG/ILG *Normas ortográficas e morfolóxicas*.
"""

import pytest

from orthography2ipa.g2p import G2P


def bare(w: str) -> str:
    return G2P("gl").transcribe_word(w).replace("ˈ", "")


# ═══════════════════════════════════════════════════════════════════════════
# Lenition of /b d ɡ/ — Regueira 2010; Freixeiro Mato 1998 I
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("word,expected", [
    ("Albor", "alβoɾ"),      # /b/ after a lateral
    ("abla", "aβla"),        # /b/ in a branching onset after a vowel
    ("Pardal", "paɾðal"),    # /d/ after a rhotic
    ("Fidalgo", "fiðalɣo"),  # /ɡ/ after a lateral
    ("acerga", "aθeɾɣa"),    # /ɡ/ after a rhotic
])
def test_gl_lenition_outside_intervocalic(word, expected):
    """Galician /b d ɡ/ are the approximants [β ð ɣ] in EVERY position except
    after a pause and after a nasal — not only between vowels (Regueira 2010,
    introduction; Freixeiro Mato 1998 I; Álvarez & Xove 2002). Unlike
    Castilian, /d/ lenites after /l/ and /ɾ/ too."""
    assert bare(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("ambos", "ambos"),
    ("tango", "taŋɡo"),
    ("ninguén", "niŋɡɛŋ"),  # and open [ɛ] survives before the nasal coda
])
def test_gl_stop_after_nasal(word, expected):
    """The nasal is the one context that blocks lenition: after it the stop
    surfaces (Regueira 2010)."""
    assert bare(word) == expected


def test_gl_word_initial_stop():
    """Utterance-initially the stop surfaces (Regueira 2010)."""
    assert bare("boi").startswith("b")
    assert bare("dedo").startswith("d")
    assert bare("gato").startswith("ɡ")


@pytest.mark.parametrize("word,expected", [
    ("tiven", "tiβeŋ"),
    ("xuvenal", "ʃuβenal"),
])
def test_gl_v_spells_the_same_phoneme_as_b(word, expected):
    """⟨v⟩ is not a separate phoneme: RAG *Normas* keep it as an etymological
    spelling of /b/, so it lenites exactly like ⟨b⟩ (Regueira 2010;
    Freixeiro Mato 1998 I)."""
    assert bare(word) == expected


def test_gl_v_word_initial_is_a_stop():
    """The same phoneme, so the same word-initial stop (Regueira 1996)."""
    assert bare("vaca").startswith("b")


# ═══════════════════════════════════════════════════════════════════════════
# Nasal place assimilation — Regueira 2010; Freixeiro Mato 1998 I
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("word,expected", [
    ("Angumil", "aŋɡumil"),
    ("abanca", "aβaŋka"),
])
def test_gl_nasal_assimilates_to_a_velar(word, expected):
    """A coda nasal takes the place of the following consonant; before a velar
    it is [ŋ] (Regueira 2010; Freixeiro Mato 1998 I)."""
    assert bare(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("benvida", "bembiða"),
    ("circunvalar", "θiɾkumbalaɾ"),
])
def test_gl_nasal_assimilates_to_a_labial(word, expected):
    """The labial half of the same assimilation (Regueira 2010)."""
    assert bare(word) == expected


def test_gl_nasal_before_a_coronal_is_unchanged():
    """The counter-case: before a coronal the nasal stays [n]."""
    assert bare("antes") == "antes"


@pytest.mark.parametrize("word,expected", [
    ("Bertamiráns", "beɾtamiɾaŋs"),
    ("montóns", "montoŋs"),
])
def test_gl_final_ns_keeps_the_velar_nasal(word, expected):
    """Word-final ⟨-n⟩ is velar [ŋ] and keeps that articulation before the
    plural ⟨-s⟩, which is a suffix rather than a syllable-mate that could
    re-place it (Regueira 2010; Freixeiro Mato 1998 I)."""
    assert bare(word) == expected


def test_gl_word_internal_ns_is_not_velar():
    """The gate is the word-final ⟨s⟩: word-internal ⟨ns⟩ is untouched."""
    assert bare("consenso") == "konsenso"


# ═══════════════════════════════════════════════════════════════════════════
# No open /ɔ/ before a tautosyllabic nasal — Regueira 2010
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("word,expected", [
    ("Antón", "antoŋ"),
    ("camión", "kamjoŋ"),
    ("aberración", "aβeraθjoŋ"),
])
def test_gl_tonic_o_before_a_nasal_coda_is_close(word, expected):
    """Galician has no open /ɔ/ before a tautosyllabic nasal: a tonic ⟨o⟩/⟨ó⟩
    closed by a nasal coda is close [o] (Regueira 2010, vowel system;
    Freixeiro Mato 1998 I)."""
    assert bare(word) == expected


def test_gl_open_o_survives_before_an_onset_nasal():
    """The counter-case the citation predicts: a heterosyllabic ONSET nasal
    does not close the vowel — cómodo [ˈkɔmoðo]."""
    assert bare("cómodo") == "kɔmoðo"


def test_gl_open_o_survives_without_a_nasal():
    """And without a nasal at all: fóra [ˈfɔɾa], adiós [aˈðjɔs]."""
    assert bare("fóra") == "fɔɾa"
    assert bare("adiós") == "aðjɔs"


# ═══════════════════════════════════════════════════════════════════════════
# Diphthongs — Freixeiro Mato 1998 I; RAG/ILG Normas
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("word,expected", [
    ("camión", "kamjoŋ"),
    ("cirurxián", "θiɾuɾʃjaŋ"),
    ("adiós", "aðjɔs"),
])
def test_gl_written_accent_on_the_open_vowel_keeps_the_rising_diphthong(
        word, expected):
    """In ⟨iá ié ió uá ué uó⟩ the RAG accent marks STRESS, not hiatus: the
    high vowel stays a glide (Freixeiro Mato 1998 I, os ditongos; RAG/ILG
    *Normas*)."""
    assert bare(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("aburriu", "aβuriw"),
    ("admitiu", "aðmitiw"),
])
def test_gl_iu_is_a_falling_diphthong(word, expected):
    """⟨iu⟩ is decrescente [iw] (viu, partiu), not the rising [ju]
    (Freixeiro Mato 1998 I, os ditongos)."""
    assert bare(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("lingüístico", "liŋɡwistiko"),
    ("ambigüidade", "ambiɣwiðaðe"),
    ("bilingüe", "biliŋɡwe"),
])
def test_gl_dieresis_spells_a_pronounced_w(word, expected):
    """⟨ü⟩ is the RAG diaeresis that marks the ⟨u⟩ of ⟨güe/güi⟩ as pronounced
    (RAG/ILG *Normas*). Mapping ⟨ü⟩ itself, instead of the ⟨güe⟩/⟨güi⟩
    trigraphs, leaves the ⟨g⟩ free to take its own lenition."""
    assert bare(word) == expected


def test_gl_plain_gu_before_front_vowels_stays_a_bare_velar():
    """The counter-case: without the diaeresis the ⟨u⟩ of ⟨gue/gui⟩ is mute
    (RAG/ILG *Normas*)."""
    assert bare("guerra") == "ɡera"
    assert bare("guitarra") == "ɡitara"


# ═══════════════════════════════════════════════════════════════════════════
# Trill after a heterosyllabic /l n s/ — Freixeiro Mato 1998 I
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("word,expected", [
    ("alroto", "alroto"),
    ("bulra", "bulra"),
    ("honra", "onra"),
])
def test_gl_trill_after_heterosyllabic_l_n_s(word, expected):
    """The rhotic is the trill /r/, not the tap, after a heterosyllabic
    /l n s/ (Freixeiro Mato 1998 I, as consoantes vibrantes;
    Álvarez & Xove 2002)."""
    assert bare(word) == expected


def test_gl_tap_survives_in_a_branching_onset():
    """The counter-case: a tautosyllabic onset cluster keeps the tap."""
    assert bare("tres") == "tɾes"
    assert bare("pobre") == "poβɾe"


# ═══════════════════════════════════════════════════════════════════════════
# No approximant geminate — Regueira 2010; Freixeiro Mato 1998 I
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("word,expected", [
    ("obvio", "obβjo"),
    ("subversivo", "subβeɾsiβo"),
    ("subvención", "subβenθjoŋ"),
])
def test_gl_no_approximant_geminate(word, expected):
    """An approximant is not a possible first member of a cluster of two
    IDENTICAL voiced obstruents: ⟨bv⟩ surfaces [b]+[β], never [ββ]
    (Regueira 2010, on the distribution of the approximants; Freixeiro Mato
    1998 I). WikiPron's gold agrees — obvio [ɔbbjo], subversivo
    [subbɛɾsibo] — and offers no [ββ] variant for any of these."""
    assert bare(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("abdome", "aβðome"),
    ("adventista", "aðβentista"),
])
def test_gl_lenition_survives_a_heterorganic_cluster(word, expected):
    """The counter-case that keeps the guard narrow: lenition DOES apply
    across a cluster of two DIFFERENT voiced obstruents."""
    assert bare(word) == expected
