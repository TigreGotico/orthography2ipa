"""Iraqi Arabic — the gilit/qəltu communal-dialect split.

The gilit (Muslim Baghdad / southern, Bedouin-type) vs qəltu (Northern —
Mosul, Tikrit, and the Jewish/Christian communal dialects of Baghdad)
distinction is the defining Mesopotamian isogloss, named after the reflex of
the word "I said": gilit vs qəltu (Blanc 1964, *Communal Dialects in Baghdad*).

Sources actually read for these targets:
- Blanc, H. (1964) *Communal Dialects in Baghdad*, Harvard — §3.25 (OA/k/),
  §3.26 (OA/q/), §3.2 (interdentals), §3.24 (OA/r/).
- Jasim, M. (2020) *Tafxiːm in the vowels of Muslawi Qəltu and Baghdadi Gilit*,
  Newcastle University PhD thesis — §2.4, §2.9.2.

Input is vocalised (harakat) per the Arabic input contract; the engine
transcribes orthography, so short vowels surface only when written.
"""
from __future__ import annotations

import pytest

import orthography2ipa
from orthography2ipa.g2p import G2P

GILIT = "ar-IQ"
QELTU = "ar-IQ-x-qeltu"


def _ipa(code: str, word: str) -> str:
    return G2P(code).transcribe(word)


def _spec(code: str):
    return orthography2ipa.get(code)


# ── The defining isogloss: qaf reflex ──────────────────────────────────────

def test_gilit_qaf_is_g():
    """Gilit: OA qaf ق → [ɡ] — the 'gilit' reflex (Blanc §3.26; Jasim §2.4)."""
    assert _ipa(GILIT, "قَالَ") == "ɡaːla"      # 'he said'
    assert _ipa(GILIT, "قَلْب") == "ɡalb"       # 'heart'


def test_qeltu_qaf_is_q():
    """Qəltu: OA qaf ق → [q] retained — the 'qəltu' reflex (Blanc §3.26)."""
    assert _ipa(QELTU, "قَالَ") == "qaːla"
    assert _ipa(QELTU, "قَلْب") == "qalb"


def test_qaf_split_differs_between_varieties():
    for w in ("قَالَ", "قَلْب"):
        assert _ipa(GILIT, w) != _ipa(QELTU, w)


# ── Gilit kaf affrication vs qəltu retention ───────────────────────────────

def test_gilit_kaf_affricates_before_front_vowel():
    """Gilit: kaf ك → [tʃ] adjacent to a front vowel (Blanc §3.25; Jasim §2.9.2)."""
    assert _ipa(GILIT, "كِيلو").startswith("tʃ")   # k before /iː/
    assert _ipa(GILIT, "دِيك").endswith("tʃ")       # k after /iː/


def test_qeltu_kaf_stays_k():
    """Qəltu: no kaf affrication — /k/ and /tʃ/ are separate phonemes (Jasim §2.9.2)."""
    assert _ipa(QELTU, "كِيلو").startswith("k")
    assert _ipa(QELTU, "دِيك").endswith("k")


def test_kaf_not_affricated_away_from_front_vowel():
    """The modelled affrication is the phonetically-conditioned part only; kaf
    not adjacent to a front vowel stays [k] in gilit (the lexicalised residue,
    e.g. čan < kān, is an documented engine limit)."""
    assert _ipa(GILIT, "كَلْب") == "kalb"           # k next to /a/, not front


# ── qaf-reflex /ɡ/ → [dʒ] affrication (gilit only) ─────────────────────────

def test_gilit_g_affricates_before_front_vowel():
    """Gilit: the /ɡ/ reflex of qaf → [dʒ] before a front vowel (Blanc §3.26)."""
    assert _ipa(GILIT, "قِرْد") == "dʒird"          # qaf→ɡ→dʒ / _i
    # back-vowel 'he said' must NOT affricate
    assert _ipa(GILIT, "قَالَ") == "ɡaːla"


# ── Interdental retention (both varieties, conservative Mesopotamian) ───────

@pytest.mark.parametrize("code", [GILIT, QELTU])
def test_interdentals_retained(code):
    """ث/θ/, ذ/ð/, ظ/ðˤ/ retained (Blanc §3.2; Jasim §2.4)."""
    assert "θ" in _ipa(code, "ثَلْج")               # 'snow'
    assert "ð" in _ipa(code, "ذَهَب")               # 'gold'
    assert "ðˤ" in _ipa(code, "ظَهَر")              # 'he appeared'


@pytest.mark.parametrize("code", [GILIT, QELTU])
def test_jim_is_dʒ(code):
    assert _ipa(code, "جَمَل") == "dʒamal"          # 'camel'


# ── Emphatic backing / tafxim (inherited into qəltu) ───────────────────────

@pytest.mark.parametrize("code", [GILIT, QELTU])
def test_emphatic_backs_low_vowel(code):
    """Low vowels /a aː/ → [ɑ ɑː] adjacent to an emphatic (Jasim 2020, tafxim)."""
    assert _ipa(code, "طَالِب").startswith("tˤɑː")   # 'student'
    assert "sˤɑ" in _ipa(code, "صَبَاح")            # 'morning'


# ── Per-variety spec integrity ─────────────────────────────────────────────

def test_qeltu_inherits_gilit_but_suppresses_affrication():
    q = _spec(QELTU)
    rule_ids = {r.id for r in q.allophone_rules}
    # inherited affrication rule ids are present (overridden to no-ops)
    assert "IQ_GILIT_AFFRIC_K_BEFORE" in rule_ids
    # emphatic rules inherited from gilit
    assert "IQ_EMPH_A_BEFORE" in rule_ids


def test_both_varieties_research_tier():
    from orthography2ipa.types import QualityTier
    assert _spec(GILIT).quality is QualityTier.RESEARCH
    assert _spec(QELTU).quality is QualityTier.RESEARCH
