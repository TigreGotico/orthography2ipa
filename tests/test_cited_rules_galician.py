"""Cited-rule tests for standard Galician (``gl-ES``).

Every test isolates ONE claim the ``gl-ES`` spec makes with a citation, on a real
word, and asserts exactly the segment the citation asserts. Each rule is paired
with the counter-case the same citation predicts, so a rule that over-applies
fails here rather than in the benchmark.

Sources asserted: Regueira 2010 (*Dicionario de pronuncia da lingua galega*),
Freixeiro Mato 1998 (*Gramática da lingua galega I: Fonética e fonoloxía*),
Álvarez & Xove 2002, and the RAG/ILG *Normas ortográficas e morfolóxicas*.
"""

import pytest

from orthography2ipa import registry
from orthography2ipa.g2p import G2P


def bare(w: str) -> str:
    return G2P("gl-ES").transcribe_word(w).replace("ˈ", "")


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


# ═══════════════════════════════════════════════════════════════════════════
# Accentuation, diphthongs and hiatus — RAG/ILG Normas 2012; Regueira 2010
# ═══════════════════════════════════════════════════════════════════════════
#
# Expected values are written from the sources. Regueira 2010 marks the final
# unstressed vowels as raised (o̝ a̝ e̝), a detail the spec does not model, so
# the expected strings below drop that diacritic. Where the dictionary's vowel
# quality differs from the spec on a segment this section does not test, the
# assertion checks only the stressed syllable.

def stressed(w: str, lang: str = "gl-ES") -> str:
    return G2P(lang).transcribe_word(w)


def tail(w: str, lang: str = "gl-ES") -> str:
    """The transcription from the stress mark on."""
    out = stressed(w, lang)
    assert out.count("ˈ") == 1, out
    return out[out.index("ˈ") + 1:]


@pytest.mark.parametrize("word,expected_tail", [
    ("amei", "mej"),
    ("amou", "mow"),
    ("recibiu", "βiw"),
    ("colleu", "ʎew"),
    ("ademais", "majs"),
    ("capitais", "tajs"),
    ("papeis", "pejs"),
    ("españois", "ɲojs"),
    ("cantou", "tow"),
    ("pensei", "sej"),
])
def test_gl_unaccented_final_falling_diphthong_is_oxytone(word, expected_tail):
    """RAG/ILG Normas §2.2 (p. 24): agudas that end in a falling diphthong,
    followed or not by n or s, take no written accent. The first eight words
    are the ones §2.2 lists, so the unaccented spelling marks an oxytone."""
    assert tail(word) == expected_tail


def test_gl_grave_with_a_final_falling_diphthong_carries_the_accent():
    """The counter-case, §2.3 (p. 24): a grave with a falling diphthong in the
    last syllable is written with the accent, and the accent wins."""
    assert tail("amábeis") == "maβejs"


@pytest.mark.parametrize("word,expected", [
    ("caqui", "ˈkaki"),
    ("ianqui", "ˈjaŋki"),
])
def test_gl_qu_plus_i_is_not_a_falling_diphthong(word, expected):
    """The counter-case that keeps ⟨ui⟩ out of the oxytone endings: after
    ⟨q⟩ the ⟨u⟩ belongs to the digraph, and Regueira 2010 gives these words
    as paroxytone."""
    assert stressed(word) == expected


def test_gl_final_y_after_a_vowel_is_an_oxytone_diphthong():
    """RAG/ILG Normas §2.6 (p. 26): words ending in ⟨-y⟩ have the treatment of
    words ending in ⟨-i⟩: playboy, spray, like convoi. Regueira 2010 gives
    playboy as plejˈβɔj; the mark stands before the last syllable."""
    t = tail("playboy")
    assert t[0] == "β" and t[-1] == "j" and "a" not in t


@pytest.mark.parametrize("word,expected", [
    ("whisky", "ˈwiski"),
    ("mayo", "ˈmajo"),
])
def test_gl_y_is_a_vowel_after_a_consonant_and_a_glide_after_a_vowel(
        word, expected):
    """⟨y⟩ occurs in loans and names (RAG/ILG Normas §1, p. 16). After a
    consonant it is the vowel [i] (§2.6; whisky ˈwiski in Regueira 2010).
    Next to a vowel it is the glide, and ⟨ay⟩ is one syllable, so mayo
    divides may-o and is paroxytone."""
    assert stressed(word) == expected


def test_gl_rugby_ends_in_the_vowel_i():
    """Regueira 2010: rugby ˈruɡbi, a paroxytone with a final [i]."""
    out = stressed("rugby")
    assert out.startswith("ˈru") and out.endswith("i")


@pytest.mark.parametrize("word,expected", [
    ("areal", "aɾeˈal"),
    ("perdoar", "peɾðoˈaɾ"),
])
def test_gl_hiatus_divides_two_syllables(word, expected):
    """RAG/ILG Normas §3.2.5 (pp. 33-34): two vowels that do not form a
    diphthong belong to two syllables (are-al, perdo-amos). Regueira 2010:
    areal aɾeˈal, perdoar peɾðoˈaɾ."""
    assert stressed(word) == expected


def test_gl_bloqueo_has_a_hiatus_before_the_final_vowel():
    """Regueira 2010: bloqueo blɔˈkeo̝, so the stress falls on ⟨e⟩ and the
    final ⟨o⟩ is a syllable of its own."""
    assert tail("bloqueo") == "keo"


def test_gl_aldea_has_a_hiatus_before_the_final_vowel():
    """Regueira 2010: aldea alˈdea̝."""
    out = stressed("aldea")
    assert out.split("ˈ")[0] == "al" and out.endswith("ea")


@pytest.mark.parametrize("word,expected", [
    ("ruído", "ruˈiðo"),
    ("aínda", "aˈinda"),
    ("saía", "saˈia"),
    ("raíña", "raˈiɲa"),
    ("xesuíta", "ʃesuˈita"),
])
def test_gl_accented_high_vowel_is_its_own_nucleus(word, expected):
    """RAG/ILG Normas §2.5 (p. 25): an accented ⟨í ú⟩ next to an unstressed
    vowel marks the two as separate syllables (aínda, ruído, saía, raíña;
    §3.2.5 xesu-íta). Regueira 2010: ruído ruˈiðo̝."""
    assert stressed(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("cáustico", "ˈkawstiko"),
    ("náutico", "ˈnawtiko"),
    ("terapéutico", "teɾaˈpɛwtiko"),
    ("apóutega", "aˈpowteɣa"),
    ("Máis", "ˈmajs"),
])
def test_gl_accented_falling_diphthong_keeps_its_glide(word, expected):
    """The RAG accent on the open vowel of a falling diphthong marks stress,
    and the high vowel after it stays a glide. Regueira 2010: cáustico
    ˈkawstiko̝, náutico ˈnawtiko̝, terapéutico teɾaˈpɛwtiko̝, apóutega
    aˈpowte̝ɣa̝, máis ˈmajs."""
    assert stressed(word) == expected


def test_gl_accented_ei_keeps_its_glide():
    """Regueira 2010: béisbol ˈbejsβo̝l."""
    assert stressed("béisbol").startswith("ˈbejs")


@pytest.mark.parametrize("word,expected", [
    ("bidueiro", "biðuˈejɾo"),
    ("badueira", "baðuˈejɾa"),
    ("cueiro", "kuˈejɾo"),
])
def test_gl_uei_outside_qu_gu_is_u_plus_the_diphthong_ei(word, expected):
    """Regueira 2010 gives a hiatus [u] followed by the diphthong [ej] in 17
    of its 18 ⟨uei⟩ lemmas outside ⟨qu gu⟩: bidueiro biðuˈejɾo̝, badueira
    baðuˈejɾa̝, cueiro kuˈejɾo̝."""
    assert stressed(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("queixo", "ˈkejʃo"),
    ("arqueiro", "aɾˈkejɾo"),
])
def test_gl_qu_before_ei_stays_a_digraph(word, expected):
    """The counter-case: ⟨qu⟩ is matched first, so its ⟨u⟩ is mute.
    Regueira 2010: queixo ˈkejʃo̝, arqueiro aɾˈkejɾo̝."""
    assert stressed(word) == expected


@pytest.mark.parametrize("word,expected_tail", [
    ("queixos", "kejʃos"),
    ("arqueiros", "kejɾos"),
    ("vaqueiros", "kejɾos"),
    ("queimas", "kejmas"),
    ("nogueiras", "ejɾas"),
    ("salgueiros", "ejɾos"),
])
def test_gl_qu_gu_before_ei_in_a_plural_keeps_the_stress(word, expected_tail):
    """The ⟨-s⟩ of the plural does not move the stress: "non se acentúan as
    palabras graves rematadas en [...] vogal + s" (RAG/ILG Normas §2.3,
    p. 24), so an unaccented word in a vowel plus ⟨-s⟩ is paroxytone and the
    plural keeps the stress of the singular Regueira 2010 gives (queixo
    ˈkejʃo̝, arqueiro aɾˈkejɾo̝). The mute ⟨u⟩ of ⟨qu gu⟩ is no nucleus."""
    assert tail(word).endswith(expected_tail)
    assert len(tail(word)) - len(expected_tail) <= 1


# ═══════════════════════════════════════════════════════════════════════════
# The gl-ES accentuation reaches the Galician dialect specs
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("lang", [
    "gl-ES-x-central", "gl-ES-x-occident", "gl-ES-x-oriental",
])
@pytest.mark.parametrize("word,expected_tail", [
    ("cantou", "tow"),
    ("pensei", "sej"),
    ("bloqueo", "keo"),
])
def test_gl_accentuation_is_inherited(lang, word, expected_tail):
    """RAG/ILG Normas §2.2 and §3.2.5 hold for every variety that writes the
    RAG norm, so these specs take the gl-ES stress block through
    ``graphemes_base``."""
    assert tail(word, lang) == expected_tail


@pytest.mark.parametrize("word,expected", [
    ("casa", "ˈkasa"),
    ("mayo", "ˈmajo"),
])
def test_gl_es_marks_stress_and_reads_y(word, expected):
    """gl-ES is standard Galician: casa is a paroxytone (RAG/ILG Normas §2.3),
    and ⟨y⟩, a loan letter (§1, p. 16), is the glide next to a vowel."""
    assert stressed(word, "gl-ES") == expected


def test_eonavian_unaccented_final_diphthong_stays_paroxytone():
    """The counter-case: the Normas ortográficas del eonaviego (2025, §1.5.2,
    p. 20) write the accent on an oxytone falling diphthong (baxóu, cantéi),
    so gl-ES-x-eonavia keeps its own stress block and an unaccented cantou is
    paroxytone there."""
    assert stressed("cantou", "gl-ES-x-eonavia") == "ˈkantow"


# ═══════════════════════════════════════════════════════════════════════════
# Galician has one standard spec, gl-ES, and every Galician tag reaches it
# ═══════════════════════════════════════════════════════════════════════════

@pytest.mark.parametrize("code", ["gl", "gl-ES", "gl_ES", "gl-es", "glg"])
@pytest.mark.parametrize("word,expected", [
    ("casa", "ˈkasa"),
    ("queixo", "ˈkejʃo"),
    ("arqueiro", "aɾˈkejɾo"),
    ("bidueiro", "biðuˈejɾo"),
])
def test_every_galician_tag_reaches_the_one_standard(code, word, expected):
    """casa is a paroxytone (RAG/ILG Normas §2.3, p. 24); Regueira 2010 gives
    queixo ˈkejʃo̝, arqueiro aɾˈkejɾo̝, bidueiro biðuˈejɾo̝. The bare tag, the
    ISO 639-3 code and every spelling of the region tag name the same spec
    without nearest-language guessing."""
    assert registry.resolve(code) == "gl-ES"
    assert registry.resolves_exactly(code)
    assert stressed(word, code) == expected


@pytest.mark.parametrize("old,new", [
    ("gl-x-central", "gl-ES-x-central"),
    ("gl-x-occidental", "gl-ES-x-occident"),
    ("gl-x-oriental", "gl-ES-x-oriental"),
    ("gl-x-eonavia", "gl-ES-x-eonavia"),
    ("gl-x-reintegrado", "gl-ES-x-reintegr"),
])
def test_retired_galician_variety_codes_reach_their_spec(old, new):
    """The varieties carry the region of the standard they derive from. Their
    retired codes still name the same spec exactly, so callers that pass them
    get the same transcription."""
    assert registry.resolve(old) == new
    assert registry.resolves_exactly(old)
    for word in ("bidueira", "cantou", "xente"):
        assert stressed(word, old) == stressed(word, new)
