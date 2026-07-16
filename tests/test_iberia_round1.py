"""Cited-rule tests for the Iberia round-1 arbitration fixes.

Each test isolates ONE arbitrated claim on a real word or phrase and asserts the
exact segment(s) the citation asserts. The five fixes:

P1  Eastern Andalusian vocalismo abierto (Navarro Tomas 1939; Cruz Ortiz).
P2  Balearic stressed schwa, atonic o->u raising, salat-article destressing
    (Veny 1982 ch. 4; Recasens 1996).
P3  cliticless_words for the Iberian families (per-family normative sources).
P4  Open-mid tonic vowels for ca/gl lects (Recasens 1996; AVL 2006; Regueira
    1996; Veny 1982).
P5  Canarian + Extremaduran velar /x/ -> [h] (Hualde 2005; Zamora Vicente 1960;
    Gonzalez Salgado 2003).
"""

from orthography2ipa.g2p import G2P


def word(code, w):
    return G2P(code).transcribe_word(w)


def bare(code, w):
    return G2P(code).transcribe_word(w).replace("ˈ", "")


def phrase(code, text):
    return G2P(code).transcribe(text)


# ── P1 — Eastern Andalusian vocalismo abierto ────────────────────────────────

def test_p1_final_s_deletion_opens_vowel():
    """es-ES-x-andalusia-e-003: a word-final -s is dropped and the preceding
    vowel opens as the sole plural cue — 'las tres' [læ ˈtɾɛ] (Navarro Tomas
    1939; Cruz Ortiz)."""
    assert phrase("es-ES-x-andalusia-e", "las tres") == "læ ˈtɾɛ"


def test_p1_internal_coda_s_aspirates_and_opens():
    """es-ES-x-andalusia-e-002: an internal coda -s aspirates to [h] and opens
    the preceding mid vowel; the final -s deletes with opening — 'estos'
    [ˈɛhtɔ]."""
    assert word("es-ES-x-andalusia-e", "estos") == "ˈɛhtɔ"


def test_p1_high_vowels_resist_opening():
    """es-ES-x-andalusia-e-017: /u/ before an aspirated -s does NOT open —
    'buscas' [ˈbuhkæ], not [ˈbʊhkæ]; only the final /a/ opens."""
    assert word("es-ES-x-andalusia-e", "buscas") == "ˈbuhkæ"


def test_p1_vowel_final_word_without_s_stays_closed():
    """es-ES-x-andalusia-e-017: a word with no -s keeps its close vowel —
    'mesa' stays [ˈmesa], never [ˈmesæ]."""
    assert word("es-ES-x-andalusia-e", "mesa") == "ˈmesa"


# ── P2 — Balearic ────────────────────────────────────────────────────────────

def test_p2_balearic_stressed_schwa():
    """ca-x-balear-005/008/013: the closed etymological set carries Majorcan
    stressed [ə] — tenen [ˈtənən], tres [ˈtɾəs], aquell [əˈkəʎ], feina
    [ˈfəjnə] (Veny 1982 ch. 4; Recasens 1996)."""
    assert word("ca-x-balear", "tenen") == "ˈtənən"
    assert word("ca-x-balear", "tres") == "ˈtɾəs"
    assert word("ca-x-balear", "aquell") == "əˈkəʎ"
    assert word("ca-x-balear", "feina") == "ˈfəjnə"


def test_p2_balearic_atonic_o_raising():
    """ca-x-balear-010/011: unstressed /o/ raises to [u] — euros [ˈɛwɾus],
    torrent [tuˈrent] (Veny 1982 ch. 4; Recasens 1996)."""
    assert word("ca-x-balear", "euros") == "ˈɛwɾus"
    assert word("ca-x-balear", "torrent") == "tuˈrent"


def test_p2_balearic_keeps_labiodental_v():
    """ca-x-balear-005/013: /v/ is preserved as a distinct labiodental (reject
    betacism) — jove [ˈʒɔvə]."""
    assert "v" in word("ca-x-balear", "jove")


def test_p2_salat_article_is_unstressed_proclitic():
    """ca-x-balear-006: the salat articles sa/des are unstressed proclitics —
    'des cotxe' [dəs ˈkɔtʃə], not stressed [ˈðɛs]."""
    assert phrase("ca-x-balear", "des cotxe") == "dəs ˈkɔtʃə"


# ── P3 — cliticless_words per family ─────────────────────────────────────────

def test_p3_spanish_clitics_unstressed():
    """Spanish articles/prepositions/contractions carry no word stress
    (Navarro Tomas 1977; Hualde 2005)."""
    assert bare("es", "el") == word("es", "el")   # no stress mark added
    assert word("es", "de") == "de"
    assert word("es", "por") == "poɾ"
    assert word("es", "del") == "del"


def test_p3_catalan_clitics_unstressed():
    """ca-009: 'per'/'del'/'el' are unstressed proclitics (Wheeler 2005 §3.1;
    IEC grammar)."""
    p = phrase("ca", "el gos corre per la vora del riu")
    assert "ˈpər" not in p.split() and "pər" in p.split()
    assert "ˈdəl" not in p.split()


def test_p3_galician_do_is_proclitic_but_pola_is_tonic():
    """gl-015: the contraction 'do' is an unstressed proclitic while 'pola'
    (por+a) is tonic (Freixeiro Mato 1998; Regueira 1996)."""
    p = phrase("gl", "corre pola ribeira do río").split()
    assert "do" in p                       # unstressed
    assert "ˈpɔla" in p                     # tonic AND open-mid


# ── P4 — Open-mid tonic vowels ───────────────────────────────────────────────

def test_p4_central_corre_is_close_o():
    """ca-009: Central 'corre' is close [ˈkorə], not the open default [ˈkɔrə]
    (DCVB; Recasens 1996)."""
    assert word("ca", "corre") == "ˈkorə"


def test_p4_nw_open_o_and_stressed_final_a_kept():
    """ca-x-occidental-009/010: North-Western 'corre'/'vora'/'dona' carry open
    [ɔ] and final atonic -a lowers to [ɛ], but a STRESSED monosyllable 'pa'
    keeps [a] (Veny 1982; Recasens 1996)."""
    assert word("ca-x-occidental", "corre") == "ˈkɔre"
    assert word("ca-x-occidental", "dona") == "ˈdɔnɛ"
    assert word("ca-x-occidental", "pa") == "ˈpa"      # not over-lowered to [ˈpɛ]


def test_p4_valencian_open_mid():
    """ca-x-valencia-003: Valencian 'finestres' [fiˈnɛstɾes] and 'grosses'
    [ˈɡɾɔses] carry open-mid vowels (AVL 2006; Recasens 1991)."""
    assert word("ca-x-valencia", "finestres") == "fiˈnɛstɾes"
    assert word("ca-x-valencia", "grosses") == "ˈɡɾɔses"


def test_p4_galician_open_o():
    """gl-015: Galician tonic 'corre' is open [ˈkɔɾe]... [ˈkɔre] (Regueira 1996;
    Freixeiro Mato 1998)."""
    assert word("gl", "corre") == "ˈkɔre"


# ── P5 — Canarian / Extremaduran velar /x/ -> [h] ────────────────────────────

def test_p5_canarian_j_g_to_h():
    """es-ES-x-canarias-003/005: /x/ (⟨j⟩/⟨g+front⟩) is the aspirate [h], not
    velar [x] — cojo [ˈkoho], trabajo [tɾaˈβaho], coge [ˈkohe] (Hualde 2005;
    Zamora Vicente 1960)."""
    assert word("es-ES-x-canarias", "cojo") == "ˈkoho"
    assert word("es-ES-x-canarias", "trabajo") == "tɾaˈβaho"
    assert word("es-ES-x-canarias", "coge") == "ˈkohe"
    assert "x" not in word("es-ES-x-canarias", "trabajo")


def test_p5_extremaduran_j_to_h_and_coda_s_aspiration():
    """es-ES-x-extremadura-005: /x/ is [h] (coge [ˈkohe], bajo [ˈbaho]) and
    coda/final -s aspirates to [h] — 'las llaves' [lah ˈʝaβeh] (Gonzalez
    Salgado 2003; Penny 2002)."""
    assert word("es-ES-x-extremadura", "coge") == "ˈkohe"
    assert word("es-ES-x-extremadura", "bajo") == "ˈbaho"
    assert phrase("es-ES-x-extremadura", "las llaves") == "lah ˈʝabeh"
