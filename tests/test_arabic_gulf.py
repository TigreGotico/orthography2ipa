"""Gulf Arabic dialects — research-grounded phonology (ar-x-gulf + AE/BH/KW/QA/OM).

The Gulf specs model, on the proto-parent ``ar-x-gulf`` and inherited by the
four Gulf country specs via ``graphemes_base`` / OVERLAY_BY_ID:

* Old Arabic *q → [ɡ] (grapheme ق → [ɡ] first);
* velar affrication — /k/ → [tʃ] (``GULF_K_AFFRICATION``) and /ɡ/(<*q) →
  [dʒ] (``GULF_G_AFFRICATION``) adjacent to a high front vowel /i, iː/;
* interdentals /θ ð ðˤ/ RETAINED (Bedouin-type), not merged to stops.

Omani (``ar-OM``) is genetically Peninsular (inherits ``ar-x-peninsular``
directly), keeps *q as [q], and carries only /k/-affrication
(``OM_K_AFFRICATION``) as a Bedouin/interior feature.

Sources actually read: Alshammari 2026 (JLTR 17(4):1333-1341), Al-Balushi
2016 (Macrolinguistics 4(1):80-125), Szreder & Derrick 2023 (JIPA).

Input contract: fully diacritised (tashkeel) Arabic.
"""
from orthography2ipa import get
from orthography2ipa.g2p import G2P

GULF = ("ar-AE", "ar-BH", "ar-KW", "ar-QA")


def _t(code, word):
    return G2P(code).transcribe(word)


# ─── the affrication rules exist and are inherited ──────────────────────

def test_proto_gulf_declares_the_two_affrication_rules():
    ids = [r.id for r in get("ar-x-gulf").allophone_rules]
    assert "GULF_K_AFFRICATION" in ids
    assert "GULF_G_AFFRICATION" in ids


def test_gulf_countries_inherit_affrication_rules():
    for code in GULF:
        ids = [r.id for r in get(code).allophone_rules]
        assert "GULF_K_AFFRICATION" in ids, code
        assert "GULF_G_AFFRICATION" in ids, code


def test_gulf_countries_inherit_peninsular_emphatic_spreading():
    # AR_PEN_EMPH_* comes from ar-x-peninsular, two nodes up.
    for code in GULF:
        ids = [r.id for r in get(code).allophone_rules]
        assert any(i.startswith("AR_PEN_EMPH") for i in ids), code


# ─── /q/ → [ɡ] in the Gulf (Bedouin/sedentary reflex) ───────────────────

def test_qaf_is_g_in_gulf():
    # قَلَم 'pen' — *q → [ɡ], /a/ does not trigger g-affrication
    for code in GULF:
        assert _t(code, "قَلَم") == "ɡalam", code


# ─── /k/ affrication before a high front vowel, and only there ──────────

def test_k_affricates_before_front_vowel():
    # كِتَاب 'book' — /k/ before /i/ → [tʃ]
    for code in GULF:
        out = _t(code, "كِتَاب")
        assert out.startswith("tʃ"), (code, out)


def test_k_does_not_affricate_before_back_or_low_vowel():
    # كَلْب 'dog' — /k/ before /a/ stays [k] (Mustafawi: blocked by [-high])
    for code in GULF:
        out = _t(code, "كَلْب")
        assert out.startswith("k") and "tʃ" not in out, (code, out)


# ─── /ɡ/ (< *q) affrication before a high front vowel ───────────────────

def test_g_affricates_before_front_vowel():
    # قِرْد 'monkey' — *q→[ɡ], then [ɡ] before /i/ → [dʒ]
    for code in GULF:
        out = _t(code, "قِرْد")
        assert out.startswith("dʒ"), (code, out)


# ─── interdental retention (Bedouin-type) ───────────────────────────────

def test_interdentals_retained():
    # ثَلاثَة 'three' keeps /θ/ (not merged to /t/ or /s/)
    for code in GULF + ("ar-OM",):
        assert "θ" in _t(code, "ثَلاثَة"), code
    # ذَهَب 'gold' keeps /ð/
    for code in GULF + ("ar-OM",):
        assert "ð" in _t(code, "ذَهَب"), code


# ─── per-country / per-node deltas ──────────────────────────────────────

def test_omani_is_peninsular_not_gulf():
    om = get("ar-OM")
    assert om.parent == "ar-x-peninsular"
    ids = [r.id for r in om.allophone_rules]
    # Omani carries only /k/-affrication, NOT the Gulf *q→[ɡ] g-affrication.
    assert "OM_K_AFFRICATION" in ids
    assert "GULF_G_AFFRICATION" not in ids


def test_omani_retains_qaf():
    # قَلَم and قِرْد keep [q] in sedentary Omani (no *q→[ɡ], no g-affrication)
    assert _t("ar-OM", "قَلَم") == "qalam"
    assert _t("ar-OM", "قِرْد") == "qird"


def test_omani_still_affricates_k_before_front_vowel():
    # Bedouin/interior feature present: كِتَاب → tʃitaːb
    assert _t("ar-OM", "كِتَاب").startswith("tʃ")


def test_emirati_has_english_loan_phonemes():
    # Heaviest English influence: /p/, /v/, /ŋ/ integrated (allophones delta)
    allo = get("ar-AE").allophones
    assert "ŋ" in allo


def test_bahraini_documents_the_communal_split():
    notes = get("ar-BH").notes.lower()
    assert "baḥārna" in notes or "baharna" in notes or "split" in notes


# ─── tier + provenance ──────────────────────────────────────────────────

def test_all_gulf_specs_are_research_tier_with_read_sources():
    from orthography2ipa.types import QualityTier
    for code in ("ar-x-gulf",) + GULF + ("ar-OM",):
        sp = get(code)
        assert sp.quality == QualityTier.RESEARCH, code
        ids = {s.id for s in sp.sources}
        # every Gulf spec cites at least one of the actually-read sources
        assert ids & {"alshammari2026", "albalushi2016", "szreder_derrick2023"}, code
