"""Tetum / Tetun Dili (``tet``) — the INL standardised orthography.

Tetun Praça / Tetun Dili is the Austronesian national language of East Timor,
heavily influenced by its Portuguese lexifier. This spec targets the official
orthography declared by Government Decree 1/2004 and curated by the Instituto
Nacional de Linguística (INL). The pinned features come from:

* Williams-van Klinken, Hajek & Nordlinger (2002), *Tetun Dili: A Grammar of
  an East Timorese Language*, Pacific Linguistics, ch. 2 — the five-vowel
  system, penultimate stress, and the Portuguese-derived palatal graphemes;
* Hull (2001), *Timor-Leste: Identity, Language and Education*.
"""
from orthography2ipa import get
from orthography2ipa.g2p import G2P
from orthography2ipa.types import GraphemePosition


def _t():
    return G2P("tet")


# --- Portuguese-derived palatal / postalveolar graphemes ---------------------

def test_portuguese_palatal_digraphs():
    """lh=/ʎ/, nh=/ɲ/ — digraphs taken over from Portuguese conventions
    (Williams-van Klinken et al. 2002 §2.1)."""
    spec = get("tet")
    assert spec.graphemes["lh"] == ["ʎ"]
    assert spec.graphemes["nh"] == ["ɲ"]


def test_x_and_j_postalveolars():
    """x=/ʃ/ and j=/dʒ/, as in Portuguese loans (Williams-van Klinken et al.
    2002 §2.1)."""
    spec = get("tet")
    assert spec.graphemes["x"] == ["ʃ"]
    assert spec.graphemes["j"] == ["dʒ"]


def test_velar_nasal_digraph():
    """ng=/ŋ/, an Austronesian velar nasal that also occurs word-initially
    (Williams-van Klinken et al. 2002 §2.1)."""
    spec = get("tet")
    assert spec.graphemes["ng"] == ["ŋ"]


# --- the glottal stop -------------------------------------------------------

def test_apostrophe_is_glottal_stop():
    """The INL orthography writes the glottal stop with an apostrophe:
    ha'u 'I' -> /haʔu/ (Williams-van Klinken et al. 2002 §2.1)."""
    assert _t().transcribe("ha'u") == "ˈhaʔu"


def test_final_k_may_glottalise():
    """Word-final -k may surface as [ʔ], an Austronesian coda feature
    (Williams-van Klinken et al. 2002 §2.2)."""
    kfin = get("tet").positional_graphemes["k"][GraphemePosition.WORD_FINAL]
    assert "ʔ" in kfin and "k" in kfin


# --- vowels and diphthongs --------------------------------------------------

def test_mid_vowel_variation():
    """e varies [e]~[ɛ] and o varies [o]~[ɔ] by stress and register
    (Williams-van Klinken et al. 2002 §2.2)."""
    spec = get("tet")
    assert spec.graphemes["e"] == ["e", "ɛ"]
    assert spec.graphemes["o"] == ["o", "ɔ"]


def test_native_diphthong_au():
    """The native diphthong au is one nucleus [aw]: hau 'I' -> /haw/
    (Williams-van Klinken et al. 2002 §2.2)."""
    assert _t().transcribe("hau") == "ˈhaw"


# --- stress -----------------------------------------------------------------

def test_penultimate_stress():
    """Stress is penultimate in the large majority of words
    (Williams-van Klinken et al. 2002 §2.5): hakerek 'write' -> /haˈkerek/."""
    assert _t().transcribe("hakerek") == "haˈkerek"


def test_penultimate_stress_labarik():
    """Penultimate stress: labarik 'child' -> /laˈbarik/
    (Williams-van Klinken et al. 2002 §2.5)."""
    assert _t().transcribe("labarik") == "laˈbarik"


# --- Portuguese-contact phoneme /v/ -----------------------------------------

def test_v_phoneme_from_portuguese():
    """/v/ enters through Portuguese loans; it is absent from the indigenous
    Austronesian inventory (Williams-van Klinken et al. 2002 §2.1)."""
    assert get("tet").graphemes["v"] == ["v"]
