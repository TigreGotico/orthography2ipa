"""Portuguese segmental round — cited regression tests.

Locks in the segmental fixes of the pt-segmental round, each keyed to the
arbitration word list and its literature:

* P1 — tonic mid-vowel open/close selection via lexeme-keyed ``AllophoneRule``
  (``word`` condition): Mateus & d'Andrade 2000 ch.3; Vigário 2003.
* P2 — word-final ``-em/-ém/-êm`` → [ɐ̃j̃] (EP) / [ẽj̃] (BP) and ``-am`` →
  [ɐ̃w̃] nasal diphthongs: Mateus & d'Andrade 2000 ch.4; Barbosa & Albano 2004.
* P3 — BR /t d/ affrication fed by the raised final ⟨e⟩: Barbosa & Albano 2004;
  Câmara Jr. 1970 — with the conservative-dental / non-palatalising opt-outs.
* P4 — intervocalic ⟨s⟩ voicing (MZ/CV), ⟨éu⟩ diphthong, ⟨x⟩=[s] in trouxe.
"""
import unicodedata

import pytest

from orthography2ipa.g2p import transcribe


def _t(word, lect):
    # NFC so a precomposed literal (õ, ẽ, ũ) and the engine's combining-tilde
    # output compare equal regardless of normalisation form.
    return unicodedata.normalize("NFC", transcribe(word, lect))


def _n(s):
    return unicodedata.normalize("NFC", s)


# ─── P1: tonic mid-vowel open/close (Mateus & d'Andrade 2000 ch.3; Vigário) ──

@pytest.mark.parametrize("word,expected", [
    # EP over-opened close-mids, now close [o]/[e]
    ("sobre", "ˈsobɾɨ"), ("sopa", "ˈsopɐ"), ("boa", "ˈboɐ"),
    ("como", "ˈkomu"), ("saboroso", "sɐbuˈɾozu"), ("fresco", "ˈfɾeʃku"),
    ("Porto", "ˈpoɾtu"), ("calor", "kɐˈloɾ"), ("catorze", "kɐˈtoɾzɨ"),
    # -oso masculine is close, its -osa feminine open (both EP)
    ("famoso", "fɐˈmozu"), ("famosa", "fɐˈmɔzɐ"),
])
def test_ep_mid_vowel_height(word, expected):
    assert _t(word, "pt-PT") == _n(expected)


@pytest.mark.parametrize("word,expected", [
    # BP over-closed open-mids, now open [ɔ]/[ɛ]
    ("corre", "ˈkɔʁi"), ("mora", "ˈmɔɾɐ"), ("era", "ˈɛɾɐ"),
    ("sol", "ˈsɔw"), ("nove", "ˈnɔvi"), ("dez", "ˈdɛs"),
    ("terra", "ˈtɛʁɐ"), ("serra", "ˈsɛʁɐ"),
    # -osa feminine open, its -oso masculine close (both BP)
    ("famosa", "faˈmɔzɐ"), ("famoso", "faˈmozu"),
])
def test_bp_mid_vowel_height(word, expected):
    assert _t(word, "pt-BR") == _n(expected)


def test_lexeme_pin_leaves_dialect_metaphony_intact():
    """The standard open/close pins are opted out where a dialect owns its own
    stressed mid-vowel process (Porto/Braga/Terceira diphthongisation)."""
    assert _t("Porto", "pt-PT-x-porto") == "ˈpwɔɾtu"
    assert _t("sol", "pt-PT-x-porto") == "ˈswɔɫ"


def test_lexeme_pin_only_touches_the_vowel():
    """A ``word``-keyed pin changes only the stressed vowel; l-vocalisation,
    rhotics and affrication around it still run."""
    assert _t("sol", "pt-BR") == "ˈsɔw"          # l→w kept
    assert _t("forte", "pt-BR") == "ˈfɔɾt͡ʃi"      # affrication kept
    assert _t("corre", "pt-BR") == "ˈkɔʁi"        # uvular rr kept


# ─── P2: final nasal diphthongs (Mateus & d'Andrade 2000 ch.4) ──────────────

@pytest.mark.parametrize("word,expected", [
    ("bem", "ˈbɐ̃j̃"), ("vem", "ˈvɐ̃j̃"), ("tem", "ˈtɐ̃j̃"),
    ("nem", "ˈnɐ̃j̃"), ("homem", "ˈɔmɐ̃j̃"), ("ontem", "ˈõtɐ̃j̃"),
    ("também", "tɐ̃ˈbɐ̃j̃"), ("custam", "ˈkuʃtɐ̃w̃"), ("falam", "ˈfalɐ̃w̃"),
    # -im/-om/-um keep the plain nasal monophthong
    ("sim", "ˈsĩ"), ("bom", "ˈbõ"), ("um", "ˈũ"),
    # an ⟨em⟩ before a consonant stays a monophthong
    ("tempo", "ˈtẽpu"), ("campo", "ˈkɐ̃pu"),
])
def test_ep_final_nasal_diphthong(word, expected):
    assert _t(word, "pt-PT") == _n(expected)


@pytest.mark.parametrize("word,expected", [
    # BP keeps the close-mid nucleus [ẽ] (no Lisbon centralisation)
    ("bem", "ˈbẽj̃"), ("quem", "ˈkẽj̃"), ("homem", "ˈomẽj̃"),
    ("custam", "ˈkustɐ̃w̃"), ("sim", "ˈsĩ"),
])
def test_bp_final_nasal_diphthong(word, expected):
    assert _t(word, "pt-BR") == _n(expected)


@pytest.mark.parametrize("lect,expected", [
    ("pt-CV", "ˈbẽj̃"),   # [ẽj] — mid nucleus, no centralisation
    ("pt-AO", "ˈbẽj̃"),   # Undolo 2014: no atonic centralisation
    ("pt-MZ", "ˈbẽ"),     # variable monophthong [ẽ]
])
def test_peripheral_lects_do_not_centralise_em(lect, expected):
    assert _t("bem", lect) == _n(expected)


def test_barranquenho_keeps_em_monophthong():
    """Barranquenho ⟨-em/-én⟩ is a nasal monophthong per the Convenção."""
    assert _t("quen", "ext-PT-x-barrancos") == "ˈkẽ"
    assert _t("bem", "ext-PT-x-barrancos") == "ˈbẽ"


# ─── P3: BR affrication fed by the raised final ⟨e⟩ (Barbosa & Albano 2004) ──

@pytest.mark.parametrize("word,expected", [
    ("leite", "ˈlejt͡ʃi"), ("tarde", "ˈtaɾd͡ʒi"), ("gente", "ˈʒẽt͡ʃi"),
    ("dente", "ˈdẽt͡ʃi"), ("onde", "ˈõd͡ʒi"), ("forte", "ˈfɔɾt͡ʃi"),
])
def test_bp_affrication_before_raised_final_e(word, expected):
    assert _t(word, "pt-BR") == _n(expected)


@pytest.mark.parametrize("lect", [
    "pt-BR-x-caipira", "pt-BR-x-sul", "pt-UY",
    "pt-BR-x-pr", "pt-BR-x-recife",
])
def test_conservative_lects_keep_dental_before_raised_e(lect):
    """The conservative-dental / non-palatalising varieties do NOT affricate a
    /t d/ before a raised final ⟨e⟩ (the new rule is opted out by id)."""
    assert "t͡ʃ" not in _t("leite", lect)
    assert "d͡ʒ" not in _t("tarde", lect)


def test_caipira_still_affricates_lexical_i():
    """Opting out of the final-⟨e⟩ affrication must not remove caipira's
    etymological ⟨i⟩ affrication (petisca, dia — cited silva2002)."""
    assert _t("petisca", "pt-BR-x-caipira") == "peˈt͡ʃiskɐ"
    assert "d͡ʒ" in _t("dia", "pt-BR-x-caipira")


# ─── P4: assorted confirmed bugs ────────────────────────────────────────────

@pytest.mark.parametrize("lect", ["pt-MZ", "pt-CV"])
def test_intervocalic_s_voices(lect):
    assert _t("casa", lect) == "ˈkazɐ"


def test_eu_acute_is_a_diphthong():
    """⟨éu⟩ is the falling diphthong [ɛw], not a hiatus."""
    assert _t("céu", "pt-PT") == "ˈsɛw"
    assert _t("véu", "pt-PT") == "ˈvɛw"
    assert _t("chapéu", "pt-PT") == "ʃɐˈpɛw"


def test_trouxe_x_is_s():
    """⟨x⟩ in the trazer preterite stem is [s], while lexical [ʃ] is kept."""
    assert _t("trouxe", "pt-PT") == "ˈtɾosɨ"
    assert _t("peixe", "pt-PT") == "ˈpejʃɨ"
    assert _t("luxo", "pt-PT") == "ˈluʃu"
