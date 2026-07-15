"""Cited-rule conformance: the Portuguese-cluster dialects and their siblings.

Each test takes ONE cited claim from a spec — its ``notes`` prose or the
``notes`` of a single ``allophone_rules``/``sandhi_rules`` entry — quotes it
with its citation, and proves the engine honours it on a real word, isolating
the rule to a single segment. Wherever the phonology allows one the assertion is
a MINIMAL PAIR: the same word under the dialect and under its parent (or its
sister dialect), so nothing but the delta can make the test pass.

Claims the engine does NOT honour are marked ``xfail(strict=True)``, the
assertion left exactly as the citation states it.

Scope note: the cited claims of pt-PT, pt-BR and most of their dialect deltas
are already proved elsewhere (test_cited_rules_romance.py, test_ep_lisbon.py,
test_ep_porto.py, test_ep_north.py, test_ep_south.py, test_ep_insular.py,
test_ep_minho_beira.py, test_ep_new_accents.py, test_br_dialects.py,
test_br_paulista.py, test_mirandese.py, test_lusophone_african.py,
test_lusophone_asian.py, test_uruguayan_portuguese.py). This file covers the
cited claims those files leave untested.
"""
import unicodedata

import pytest

from orthography2ipa.g2p import G2P


def _t(code, word):
    # NFC so a precomposed nasal glyph in an expected literal compares equal to
    # the engine's decomposed vowel + combining tilde.
    return unicodedata.normalize("NFC", G2P(code).transcribe_word(word))


def _bare(code, word):
    return _t(code, word).replace("ˈ", "").replace("ˌ", "")


# ===========================================================================
# gl — Standard Galician (RAG norm)
# ===========================================================================


def test_gl_distincion():
    """DISTINCIÓN: ⟨c⟩ before e/i and ⟨z⟩ are the interdental /θ/.

    gl notes: "(1) DISTINCIÓN (interdental /θ/): standard Galician HAS the
    phoneme /θ/ — ⟨c⟩ before e/i and ⟨z⟩ = /θ/ (as in Castilian; Portuguese has
    no interdental...). SESEO ... is a WESTERN/coastal DIALECTAL feature, NOT
    part of the RAG standard. Regueira (1996: 119) describes standard Galician
    with /θ/ and explicitly notes it does not show the dialectal seseo."

    Minimal pair on ⟨c⟩: cinco (before ⟨i⟩ → [θ]) vs casa (before ⟨a⟩ → [k]).
    Portuguese, which has no interdental at all, is the cross-language contrast.
    """
    assert _bare("gl", "cinco").startswith("θ")
    assert _bare("gl", "zapato").startswith("θ")
    assert _bare("gl", "casa").startswith("k")
    assert "θ" not in _bare("pt-PT", "cinco")


@pytest.mark.xfail(
    strict=True,
    reason="gl notes claim an apico-alveolar /s/ [s̺]; engine produces a plain "
    "unmarked [s] in casa — the apical diacritic the spec's own prose asserts is "
    "never emitted (contrast mwl/pt-PT-x-trasosmontes, which do mark it)",
)
def test_gl_apico_alveolar_s():
    """Galician /s/ is the apico-alveolar [s̺], not the Portuguese predorsal [s̻].

    gl notes: "(2) APICO-ALVEOLAR /s/ [s̺] like Castilian/Asturian (not
    Portuguese predorsal [s̻])." Sources: Freixeiro Mato (2006), Regueira (1996),
    Ferreiro (1997).
    """
    assert "s̺" in _bare("gl", "casa")


def test_gl_betacism():
    """BETACISM: ⟨b⟩ = ⟨v⟩ = /b/, unlike Portuguese.

    gl notes: "(3) BETACISM: ⟨b⟩ = ⟨v⟩ = /b/ (unlike Portuguese which preserves
    /v/ ≠ /b/)." Freixeiro Mato (2006), Regueira (1996).

    Minimal pair on the same word against pt-PT, which keeps /v/.
    """
    assert _bare("gl", "vaca").startswith("b")
    assert _bare("pt-PT", "vaca").startswith("v")


def test_gl_ll_and_enye_are_castilian_spellings_of_the_palatals():
    """⟨ll⟩ = /ʎ/ and ⟨ñ⟩ = /ɲ/ — Castilian, not Portuguese, orthography.

    gl notes: "(4) ⟨ll⟩ = /ʎ/, ⟨ñ⟩ = /ɲ/ (Castilian orthographic conventions, not
    Portuguese ⟨lh⟩/⟨nh⟩)." Freixeiro Mato (2006).
    """
    assert _bare("gl", "pollo") == "poʎo"
    assert _bare("gl", "teño") == "teɲo"


def test_gl_ch_is_the_affricate():
    """⟨ch⟩ = /tʃ/ in the standard pronunciation.

    gl notes: "(5) ⟨ch⟩ = /tʃ/ (standard pronunciation; urban registers
    increasingly /ʃ/ under Portuguese/Spanish influence)." Regueira (1996).
    """
    assert _bare("gl", "chave").startswith("tʃ")


def test_gl_x_is_the_postalveolar_fricative():
    """⟨x⟩ = /ʃ/ — the cited whole-word transcription of xeneral.

    gl notes: "(6) ⟨x⟩ = /ʃ/ — covers many words where Castilian uses
    ⟨j⟩/⟨ge,gi⟩ (e.g. 'xeneral' [ʃeneˈɾal] vs. Spanish 'general')."

    Minimal pair against es-ES, whose ⟨j⟩/soft ⟨g⟩ is the velar [x].
    """
    assert _t("gl", "xeneral") == "ʃeneˈɾal"
    assert _bare("es-ES", "general").startswith("x")


def test_gl_no_unstressed_vowel_reduction():
    """NO VOWEL REDUCTION: unstressed /a/ stays [a], not the Portuguese [ɐ].

    gl notes: "(7) NO VOWEL REDUCTION: unstressed /a/ stays [a] (not /ɐ/ as in
    Portuguese)." Regueira (1996: 119).

    Minimal pair on the same word: pt-PT reduces the final ⟨a⟩ to [ɐ] (and voices
    the intervocalic ⟨s⟩); Galician does neither.
    """
    assert _bare("gl", "casa") == "kasa"
    assert _bare("pt-PT", "casa") == "kazɐ"


@pytest.mark.xfail(
    strict=True,
    reason="gl notes cite irmán [ɐ̃] and corazón [õ]; engine produces [iˈɾmaŋ] and "
    "[koɾaˈθɔŋ] — the word-final nasal is realised as a separate velar [ŋ] and "
    "the vowel is neither nasalised nor raised, so no nasal vowel is produced",
)
def test_gl_word_final_nasal_vowels():
    """NASAL VOWELS word-finally: irmán has [ɐ̃], corazón has [õ].

    gl notes: "(9) NASAL VOWELS word-finally (irmán [ɐ̃], corazón [õ])."
    Freixeiro Mato (2006), Regueira (1996).
    """
    assert "ɐ̃" in _bare("gl", "irmán")
    assert "õ" in _bare("gl", "corazón")


def test_gl_preserves_the_diphthongs_ou_and_ei():
    """Galician preserves ⟨ou⟩ /ow/ and ⟨ei⟩ /ej/.

    gl notes: "(10) Preserves diphthongs: ou /ow/ ('cousa'), ei /ej/ ('leite')."
    Freixeiro Mato (2006).

    The contrast is central-southern EP, which monophthongises ⟨ou⟩ to [o] and
    lowers ⟨ei⟩ to [ɐj] (pt-PT-x-lisbon).
    """
    assert "ow" in _bare("gl", "cousa")
    assert "ej" in _bare("gl", "leite")
    assert "ow" not in _bare("pt-PT-x-lisbon", "ouro")


# ===========================================================================
# gl-ES — Standard Galician, RAG norms (the country-coded standard node)
# ===========================================================================


@pytest.mark.xfail(
    strict=True,
    reason="gl-ES notes claim distinción (interdental /θ/); engine produces "
    "[kinko] for cinco and [kiðaðe] for cidade — the ⟨c⟩ grapheme has no "
    "before-front-vowel branch in this spec, so soft ⟨c⟩ surfaces as [k]. The "
    "parent gl gets it right, so this is a gl-ES DATA gap, not an engine limit",
)
def test_gl_es_distincion_on_soft_c():
    """gl-ES has the interdental /θ/ for ⟨c⟩ before a front vowel.

    gl-ES notes: "Standard Galician has interdental /θ/ (distinción); seseo is
    western-dialectal (see gl-x-occidental), not standard." Regueira (1996: 119).

    Minimal pair inside the spec: ⟨z⟩ does yield [θ] (zapato), so only the soft-⟨c⟩
    branch of the same cited claim fails.
    """
    assert _bare("gl-ES", "cinco").startswith("θ")


def test_gl_es_z_is_interdental():
    """⟨z⟩ = /θ/ — the half of gl-ES's distinción claim the engine does honour.

    gl-ES notes: "Standard Galician has interdental /θ/ (distinción); seseo is
    western-dialectal ..., not standard." Regueira (1996: 119).
    """
    assert _bare("gl-ES", "zapato").startswith("θ")


def test_gl_es_has_no_voiced_sibilants():
    """No intervocalic /s/ → [z] voicing, unlike Portuguese.

    gl-ES notes: "no voiced sibilants (no intervocalic /s/→[z] voicing)".

    Minimal pair on the same words against pt-PT, which voices them.
    """
    assert "z" not in _bare("gl-ES", "casa")
    assert "z" not in _bare("gl-ES", "rosa")
    assert "z" in _bare("pt-PT", "casa")


def test_gl_es_nh_is_the_velar_nasal():
    """⟨nh⟩ is the velar nasal /ŋ/ (unha), not the Portuguese palatal /ɲ/.

    gl-ES notes: "⟨nh⟩ is the velar nasal /ŋ/ (e.g. unha), not palatal /ɲ/."
    """
    assert "ŋ" in _bare("gl-ES", "unha")
    assert "ɲ" not in _bare("gl-ES", "unha")


def test_gl_es_keeps_unstressed_a_open():
    """No unstressed vowel reduction: /a/ stays [a].

    gl-ES notes: "no unstressed vowel reduction, /a/ stays [a] (Regueira
    1996:119)".
    """
    assert _bare("gl-ES", "casa").endswith("a")


# ===========================================================================
# gl-x-occidental — Western Galician
# ===========================================================================


def test_gl_occidental_gheada_word_initial():
    """GHEADA: word-initial /ɡ/ is replaced by the voiceless fricative [h].

    gl-x-occidental notes: "KEY FEATURE — GHEADA: the defining hallmark of
    western Galician, a substitution of /ɡ/ by a voiceless fricative [h] ...
    'galego' → [haˈlɛho], 'gato' → [ˈhato]. The gheada affects: word-initial /ɡ/,
    intervocalic /ɡ/." Sources: Fernández Rei (1990), Dubert García (2006).

    Minimal pair against the sister dialect gl-x-oriental, whose notes state
    "(5) No gheada (characteristic of the western coast, absent in the east)".
    """
    assert _bare("gl-x-occidental", "gato").startswith("h")
    assert _bare("gl-x-oriental", "gato").startswith("ɡ")


def test_gl_occidental_gheada_intervocalic():
    """GHEADA also affects intervocalic /ɡ/.

    gl-x-occidental notes: "The gheada affects: word-initial /ɡ/, intervocalic
    /ɡ/." Fernández Rei (1990).
    """
    assert _bare("gl-x-occidental", "amigo") == "amiho"
    assert _bare("gl-x-oriental", "amigo").endswith("ɣo")


def test_gl_occidental_gu_digraph_keeps_the_stop():
    """The ⟨gu⟩ digraph before e/i is exempt from the gheada.

    gl-x-occidental notes: "the ⟨gu⟩ digraph before e/i typically retains /ɡ/."
    Fernández Rei (1990).

    This is the environment that isolates the gheada: guerra keeps [ɡ] where the
    bare ⟨g⟩ of gato becomes [h].
    """
    assert _bare("gl-x-occidental", "guerra").startswith("ɡ")
    assert _bare("gl-x-occidental", "gato").startswith("h")


@pytest.mark.xfail(
    strict=True,
    reason="gl-x-occidental cites galego → [haˈlɛho]; engine produces [haleho] — "
    "the gheada itself fires, but the spec carries no stress block (no stress "
    "mark is emitted at all, unlike its parent gl) and the tonic ⟨e⟩ is the "
    "close [e], not the cited open [ɛ]",
)
def test_gl_occidental_cited_galego_transcription():
    """gl-x-occidental cites galego as [haˈlɛho].

    gl-x-occidental notes: "a substitution of /ɡ/ by a voiceless fricative [h]
    ...: 'galego' → [haˈlɛho], 'gato' → [ˈhato]." Fernández Rei (1990).
    """
    assert _t("gl-x-occidental", "galego") == "haˈlɛho"


# ===========================================================================
# gl-x-oriental — Eastern Galician
# ===========================================================================


def test_gl_oriental_ch_retained_as_affricate():
    """⟨ch⟩ = /tʃ/ is retained, where /ʃ/ spreads in the west and the cities.

    gl-x-oriental notes: "(3) ⟨ch⟩ = /tʃ/ RETAINED more consistently (vs. western
    and urban Galician where /ʃ/ is spreading)." Fernández Rei (1990).
    """
    assert _bare("gl-x-oriental", "chave").startswith("tʃ")


def test_gl_oriental_no_yeismo():
    """/ʎ/ for ⟨ll⟩ is robustly preserved — no yeísmo.

    gl-x-oriental notes: "(4) /ʎ/ for ⟨ll⟩ robustly preserved (no yeísmo,
    influenced by Asturian conservatism)." Fernández Rei (1990), Beswick (2007).

    Contrast es-ES, which merges ⟨ll⟩ into /ʝ/.
    """
    assert "ʎ" in _bare("gl-x-oriental", "calle")
    assert "ʎ" not in _bare("es-ES", "calle")


# ===========================================================================
# roa-x-galaicopt — Galaico-Portuguese (~9th–14th c.)
# ===========================================================================


def test_galaicopt_medieval_four_way_sibilant_contrast():
    """The medieval 4-way sibilant contrast: /ts/ ⟨ç⟩, /dz/ ⟨z⟩, /s/ ⟨ss⟩, /z/ ⟨-s-⟩.

    roa-x-galaicopt notes: "(1) Medieval 4-way sibilant contrast: /ts/ ⟨ç⟩ vs
    /d͡z/ ⟨z⟩ vs /s/ ⟨ss⟩ vs /z/ ⟨-s-⟩." Sources: Maia (1986), Castro (2006),
    Teyssier (1982).

    The four graphemic series must stay four distinct sibilants: the affricates
    for ⟨ç/c⟩ and ⟨z⟩, and the plain fricative pair for ⟨ss⟩ and intervocalic
    ⟨-s-⟩ (which the spec writes with the apical diacritic).
    """
    ceo = _bare("roa-x-galaicopt", "ceo")          # ⟨c⟩ before e = ⟨ç⟩ series
    fazer = _bare("roa-x-galaicopt", "fazer")      # ⟨z⟩
    passo = _bare("roa-x-galaicopt", "passo")      # ⟨ss⟩
    casa = _bare("roa-x-galaicopt", "casa")        # intervocalic ⟨-s-⟩
    assert ceo.startswith("t͡s")
    assert "d͡z" in fazer
    assert "s̺" in passo and "t͡s" not in passo
    assert "z̺" in casa and "d͡z" not in casa


def test_galaicopt_preserves_b_v_distinction():
    """/b/ ≠ /v/ is preserved — no betacism.

    roa-x-galaicopt notes: "(3) /b/ ≠ /v/ preserved." Maia (1986).

    Minimal pair on the same word against its Galician descendant, whose notes
    claim "(3) BETACISM: ⟨b⟩ = ⟨v⟩ = /b/".
    """
    assert _bare("roa-x-galaicopt", "vaca").startswith("v")
    assert _bare("gl", "vaca").startswith("b")


def test_galaicopt_lh_and_nh_digraphs():
    """⟨lh⟩ = /ʎ/ and ⟨nh⟩ = /ɲ/ — the Occitan digraph convention.

    roa-x-galaicopt notes: "(2) /ʎ/ ⟨lh⟩, /ɲ/ ⟨nh⟩ digraph convention from
    Occitan." Castro (2006), Teyssier (1982).
    """
    assert _bare("roa-x-galaicopt", "filho") == "fiʎo"
    assert _bare("roa-x-galaicopt", "vinho") == "viɲo"


def test_galaicopt_initial_f_preserved():
    """Initial F- is preserved: filho, not the Castilian hijo.

    roa-x-galaicopt notes: "(4) F- preserved (filho, not hijo)." Maia (1986).

    Minimal pair against es-ES, whose own notes cite the F→H→∅ change
    ("FILIU→hijo") and which transcribes hijo with no labial at all.
    """
    assert _bare("roa-x-galaicopt", "filho").startswith("f")
    assert not _bare("es-ES", "hijo").startswith("f")


def test_galaicopt_ou_is_still_a_true_diphthong():
    """⟨ou⟩ is still a true diphthong [ow], not yet monophthongised.

    roa-x-galaicopt notes: "(5) /ou/ still a true diphthong." Teyssier (1982).

    Minimal pair against pt-PT-x-lisbon, where the central-southern standard has
    completed the monophthongisation to [o].
    """
    assert "ow" in _bare("roa-x-galaicopt", "cousa")
    assert "ow" not in _bare("pt-PT-x-lisbon", "ouro")


# ===========================================================================
# pt-PT-x-medieval — Old Portuguese (~14th–16th c.)
# ===========================================================================


def test_medieval_sibilant_deaffrication():
    """SIBILANT DEAFFRICATION: /ts/ → /s/ and /dz/ → /z/.

    pt-PT-x-medieval notes: "(1) Sibilant deaffrication: /ts/→/s/, /dz/→/z/ — the
    4-way contrast collapses to 2 (~14th–15th c.)." Sources: Williams (1962),
    Mattos e Silva (2006), Castro (2006).

    Minimal pair against the ancestor roa-x-galaicopt on the same words, which
    still has the affricates: this isolates exactly the change being claimed.
    """
    assert "t͡s" not in _bare("pt-PT-x-medieval", "ceo")
    assert "d͡z" not in _bare("pt-PT-x-medieval", "fazer")
    assert "t͡s" in _bare("roa-x-galaicopt", "ceo")
    assert "d͡z" in _bare("roa-x-galaicopt", "fazer")


def test_medieval_four_sibilants_collapse_to_two():
    """The 4-way contrast collapses to 2: passo = paço, coser = cozer.

    pt-PT-x-medieval notes: "(1) Sibilant deaffrication: /ts/→/s/, /dz/→/z/ — the
    4-way contrast collapses to 2 (~14th–15th c.)." Williams (1962).

    The collapse is what makes the medieval near-minimal pairs homophonous, where
    the ancestor kept them apart — the strongest possible proof of the merger.
    """
    assert _t("pt-PT-x-medieval", "passo") == _t("pt-PT-x-medieval", "paço")
    assert _t("pt-PT-x-medieval", "coser") == _t("pt-PT-x-medieval", "cozer")
    assert _t("roa-x-galaicopt", "passo") != _t("roa-x-galaicopt", "paço")


def test_medieval_dj_simplifies_to_zh():
    """/dʒ/ → /ʒ/ simplification: ⟨j⟩ is the plain fricative.

    pt-PT-x-medieval notes: "(4) /dʒ/→/ʒ/ simplification." Williams (1962),
    Mattos e Silva (2006).

    Minimal pair against roa-x-galaicopt, which still has the affricate [d͡ʒ].
    """
    assert _bare("pt-PT-x-medieval", "jogar").startswith("ʒ")
    assert _bare("roa-x-galaicopt", "jogar").startswith("d͡ʒ")


@pytest.mark.xfail(
    strict=True,
    reason="pt-PT-x-medieval cites the /dʒ/→/ʒ/ simplification; ⟨j⟩ does yield "
    "[ʒ] (jogar) but soft ⟨g⟩ does not — gente is transcribed [ˈɡɛnte], the "
    "grapheme ⟨g⟩ having no before-front-vowel branch in this spec. DATA gap "
    "(same shape as gl-ES's soft ⟨c⟩), not an engine limit",
)
def test_medieval_soft_g_simplifies_to_zh():
    """/dʒ/ → /ʒ/ applies to soft ⟨g⟩ as well as to ⟨j⟩.

    pt-PT-x-medieval notes: "(4) /dʒ/→/ʒ/ simplification." Williams (1962).

    The two graphemes of the historical /dʒ/ phoneme are ⟨j⟩ and ⟨g⟩ before a
    front vowel; the claim is about the phoneme, so both must simplify.
    """
    assert _bare("pt-PT-x-medieval", "gente").startswith("ʒ")


@pytest.mark.xfail(
    strict=True,
    reason="pt-PT-x-medieval claims nasal vowels are fully phonemicised; engine "
    "produces [ˈkampo] and [ˈvɛnto] — a vowel before a coda nasal stays oral and "
    "the nasal consonant surfaces separately, so no nasal vowel exists outside "
    "the ⟨ão⟩ digraph. DATA gap: the spec inherits none of pt-PT's "
    "PT_NASAL_*_RAISE coda-nasalisation rules",
)
def test_medieval_nasal_vowels_are_phonemicised():
    """NASAL VOWELS fully phonemicised.

    pt-PT-x-medieval notes: "(3) Nasal vowels fully phonemicised." Sources:
    Williams (1962), Mattos e Silva (2006), Castro (2006).

    Modern pt-PT nasalises the vowel and absorbs the coda nasal (campo → [ˈkɐ̃pu]);
    a fully phonemicised nasal-vowel system must do the same.
    """
    assert "m" not in _bare("pt-PT-x-medieval", "campo")
    assert "ɐ̃" in _bare("pt-PT-x-medieval", "campo")


# ===========================================================================
# pt-BR-x-sp — Paulistano
# ===========================================================================


@pytest.mark.xfail(
    strict=True,
    reason="pt-BR-x-sp cites então → [ĩˈtɐ̃w̃]; engine produces [ẽtɐ̃ˈw̃] — the "
    "word-initial pretonic /eN/ → [ĩ] raising is asserted in the notes but no "
    "rule or map entry implements it, and the output is identical to the pt-BR "
    "base. DATA gap",
)
def test_sp_word_initial_pretonic_en_raises_to_i():
    """Word-initial pretonic /eN/ raises to [ĩ]: então → [ĩˈtɐ̃w̃].

    pt-BR-x-sp notes: "Inherits the pt-BR base unchanged: ... word-initial
    pretonic /eN/ -> [ĩ] (então -> [ĩˈtɐ̃w̃])." Reference variety of Barbosa &
    Albano (2004, JIPA).
    """
    assert _bare("pt-BR-x-sp", "então").startswith("ĩ")


# ===========================================================================
# pt-BR-x-rj — Carioca
# ===========================================================================


def test_rj_coda_r_velar():
    """RJ_CODA_R_VELAR: a non-final coda /R/ is the velar fricative [x].

    Rule notes: "Non-final coda /R/ (pre-consonantal: porta, carta) is the velar
    fricative [x], the predominant cultured-Carioca variant (Callou 2010:138,
    Callou 1987). Onset and intervocalic rhotics are untouched (they are not in
    the coda)."

    Minimal pair against the pt-BR base, whose coda /R/ is the tap [ɾ].
    """
    assert _bare("pt-BR-x-rj", "porta") == "poxtɐ"
    assert _bare("pt-BR-x-rj", "carta") == "kaxtɐ"
    assert _bare("pt-BR", "porta") == "poɾtɐ"


def test_rj_coda_r_final_aspiration():
    """RJ_CODA_R_FINAL: a word-final coda /R/ is the aspiration [h].

    Rule notes: "Word-final coda /R/: aspiration [h] (or deletion) prevails in
    cultured Carioca speech (Callou 2010:138, citing Callou 1987). Modelled as
    aspiration rather than deletion so the segment is retained."

    Minimal pair inside the dialect: word-final [h] (mar) vs the pre-consonantal
    velar [x] of RJ_CODA_R_VELAR (porta) — two rules, two outcomes.
    """
    assert _bare("pt-BR-x-rj", "mar") == "mah"
    assert _bare("pt-BR-x-rj", "porta").count("x") == 1


# ===========================================================================
# pt-BR-x-fluminense — Fluminense
# ===========================================================================


def test_fluminense_coda_r_velar():
    """FLU_CODA_R_VELAR: a non-final coda /R/ is the velar fricative [x].

    Rule notes: "Non-final coda /R/ -> velar fricative [x] in the coastal
    prestige norm (Callou 2010:138)."

    Minimal pair against the pt-BR base, whose coda /R/ is the tap [ɾ].
    """
    assert _bare("pt-BR-x-fluminense", "porta") == "poxtɐ"
    assert _bare("pt-BR", "porta") == "poɾtɐ"


def test_fluminense_coda_r_final_aspiration():
    """FLU_CODA_R_FINAL: a word-final coda /R/ is the aspiration [h].

    Rule notes: "Word-final coda /R/ -> aspiration [h]/deletion, as in the Carioca
    norm (Callou 2010:138)."
    """
    assert _bare("pt-BR-x-fluminense", "mar") == "mah"
    assert _bare("pt-BR", "mar") == "maɾ"


# ===========================================================================
# pt-BR-x-caipira — Caipira
# ===========================================================================


@pytest.mark.xfail(
    strict=True,
    reason="pt-BR-x-caipira cites Amaral (1920) §25 'Vocaliza-se em i ... muié' "
    "and §6e 'lh não existe no dialeto'; engine produces [muˈʎeɻ] for mulher and "
    "[ˈoʎu] for olho — the palatal lateral survives intact. DATA gap: no rule or "
    "map entry vocalises /ʎ/ (contrast pt-UY, which does model exactly this)",
)
def test_caipira_palatal_lateral_vocalises_to_glide():
    """/ʎ/ vocalises to [j]: mulher → muié, olho → oio.

    pt-BR-x-caipira notes: "/ʎ/ vocalises to [j] (Amaral §25: 'Vocaliza-se em i:
    espaiado, maio, muié'; §6e: lh 'não existe no dialeto')."
    """
    assert "ʎ" not in _bare("pt-BR-x-caipira", "mulher")
    assert "j" in _bare("pt-BR-x-caipira", "mulher")


@pytest.mark.xfail(
    strict=True,
    reason="pt-BR-x-caipira cites Amaral (1920) §23a 'Cai, quando final de "
    "palavra: andá, muié, esquecê'; engine produces [ɐ̃ˈdaɻ] for andar and "
    "[koˈmeɻ] for comer — the word-final rhotic is retroflexed, not elided. DATA "
    "gap: deletion IS expressible (cf. pt-PT-x-alentejo "
    "ALE_FINAL_HIGH_VOWEL_DELETION), but no such rule is declared",
)
def test_caipira_word_final_r_elides():
    """Word-final /r/ elides: andar → andá.

    pt-BR-x-caipira notes: "Word-final /r/ elides (Amaral §23a: 'Cai, quando final
    de palavra: andá, muié, esquecê')."

    The complementary environment pins the rule: a coda /r/ that is NOT word-final
    (porta) survives as the retroflex [ɻ], so only the word-final one may go.
    """
    assert not _bare("pt-BR-x-caipira", "andar").endswith("ɻ")
    assert "ɻ" in _bare("pt-BR-x-caipira", "porta")


def test_caipira_final_vowel_raising_divergence_is_declared_not_modelled():
    """The spec's own declared omission: Amaral's unraised final vowels are NOT modelled.

    pt-BR-x-caipira notes: "NB Amaral §8 records that early-20c rural caipira did
    NOT raise final unstressed /e/->[i] or /o/->[u] ('Não se operou aqui a permuta
    de e final por i ... como não se operou a de o por u'); the spec inherits the
    modern pt-BR reduction, which now prevails, and this historical divergence is
    documented rather than modelled."

    Pinned as a passing test so the declared omission cannot silently change: the
    modern pt-BR raising is what caipira inherits.
    """
    assert _t("pt-BR-x-caipira", "gato") == "ˈɡatu"
    assert _t("pt-BR-x-caipira", "gato") == _t("pt-BR", "gato")


# ===========================================================================
# pt-MZ — Mozambican Portuguese
# ===========================================================================


def test_mz_strong_rhotic_is_the_alveolar_trill():
    """The strong rhotic ⟨r⟩/⟨rr⟩ is an alveolar trill [r], not the EP uvular [ʁ].

    pt-MZ notes: "(2) RHOTIC (Nhatuve 2019:136-137, Maputo oral Portuguese,
    READ): the strong rhotic ⟨r⟩/⟨rr⟩ is realised as an alveolar multiple vibrant
    [r]~[R] in all contexts, not the EP uvular [ʁ]", a calque of the Bantu
    changana/ronga system.

    Minimal pair against pt-PT on the same word: the uvular [ʁ] of carro is the
    only segment that differs.
    """
    assert _bare("pt-MZ", "carro") == "karu"
    assert _bare("pt-PT", "carro") == "kaʁu"
    assert "ʁ" not in _bare("pt-MZ", "rato")
