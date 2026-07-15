"""Kabuverdianu / Cape Verdean Creole (``kea``) — the ALUPEC orthography.

Kabuverdianu is a Portuguese-based creole. This spec targets ALUPEC (Alfabeto
Unificado para a Escrita da Língua Cabo-verdiana), the phonemic official
alphabet — Decreto-Lei 67/98 (trial) and Decreto-Lei 8/2009 — NOT the
etymological Portuguese-based spelling. Pinned features come from:

* Baptista (2002), *The Syntax of Cape Verdean Creole: The Sotavento
  Varieties*, John Benjamins, ch. 2 (phonological inventory);
* the ALUPEC alphabet documentation — the vowel+n nasal-vowel convention,
  the silent h, the affricates tx/dj, and the rr/r rhotic split.

In ALUPEC a nasal vowel is written vowel+n, the coda n marking nasality and
left unpronounced (bon /bõ/); the tilde is kept only in the diphthongs ãi/ãu.
"""
from orthography2ipa import get
from orthography2ipa.g2p import G2P
from orthography2ipa.types import GraphemePosition


def _t():
    return G2P("kea")


# --- affricates: creole innovations relative to Portuguese ------------------

def test_tx_affricate():
    """tx=/tʃ/: txiga 'to arrive' -> /ˈtʃiɡa/ (ALUPEC; Baptista 2002 §2)."""
    assert _t().transcribe("txiga") == "ˈtʃiɡa"


def test_dj_affricate():
    """dj=/dʒ/, retained from old Portuguese: dja 'already' -> /ˈdʒa/
    (ALUPEC; Baptista 2002 §2)."""
    assert _t().transcribe("dja") == "ˈdʒa"


# --- postalveoral fricatives ------------------------------------------------

def test_x_and_j_fricatives():
    """x=/ʃ/ and j=/ʒ/: fixi -> /ˈfiʃi/, oja 'to see' -> /ˈoʒa/
    (ALUPEC; Baptista 2002 §2)."""
    g = _t()
    assert g.transcribe("fixi") == "ˈfiʃi"
    assert g.transcribe("oja") == "ˈoʒa"


def test_silent_h():
    """ALUPEC h is silent — it has no phonetic value (ALUPEC alphabet)."""
    assert get("kea").graphemes["h"] == [""]


# --- ALUPEC vowel+n nasalisation --------------------------------------------

def test_nasal_vowel_word_final_n():
    """Coda n marks nasality and is unpronounced: bon 'good' -> /bõ/
    (ALUPEC; Baptista 2002 §2)."""
    assert _t().transcribe("bon") == "ˈbõ"


def test_nasal_vowel_before_consonant():
    """A vowel nasalises before a coda n and the n is absorbed:
    kansa 'to tire' -> /ˈkãsa/ (ALUPEC; Baptista 2002 §2)."""
    assert _t().transcribe("kansa") == "ˈkãsa"


def test_onset_n_stays_oral():
    """An onset n before a vowel does NOT nasalise: mininu 'boy' -> /miˈninu/
    (ALUPEC; Baptista 2002 §2)."""
    assert _t().transcribe("mininu") == "miˈninu"


# --- rhotic split: tap vs strong rhotic -------------------------------------

def test_intervocalic_r_is_tap():
    """Single intervocalic r is a tap /ɾ/: karu 'expensive' -> /ˈkaɾu/
    (ALUPEC; Baptista 2002 §2)."""
    assert _t().transcribe("karu") == "ˈkaɾu"


def test_rr_is_strong_rhotic():
    """rr is the strong rhotic /ʀ/: forru 'free' -> /ˈfoʀu/
    (ALUPEC; Baptista 2002 §2)."""
    assert _t().transcribe("forru") == "ˈfoʀu"


def test_word_initial_r_is_strong():
    """Word-initial r is the strong rhotic /ʀ/ (written single r in ALUPEC):
    riba 'up' -> /ˈʀiba/ (ALUPEC; Baptista 2002 §2)."""
    assert get("kea").positional_graphemes["r"][GraphemePosition.WORD_INITIAL] == ["ʀ"]
    assert _t().transcribe("riba") == "ˈʀiba"


# --- stress -----------------------------------------------------------------

def test_penultimate_stress():
    """Stress is penultimate by default: kabalu 'horse' -> /kaˈbalu/
    (Baptista 2002 §2; ALUPEC)."""
    assert _t().transcribe("kabalu") == "kaˈbalu"


def test_written_accent_overrides_stress():
    """A written accent marks a non-penultimate stressed vowel:
    karapáti 'tick' -> /kaɾaˈpati/, not penultimate (Baptista 2002 §2;
    ALUPEC)."""
    assert _t().transcribe("karapáti") == "kaɾaˈpati"


# --- lexifier ---------------------------------------------------------------

def test_portuguese_superstrate_declared():
    """European Portuguese is the lexifier / superstrate ancestor."""
    codes = {a.code: a.role for a in get("kea").ancestors}
    assert codes.get("pt-PT") == "superstrate"
