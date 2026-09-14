"""Zazaki (Zaza, ``zza``) — a Turkish-alphabet orthography, not a Kurmanji one.

Zazaki is a Northwestern Iranian language of eastern Anatolia and a separate
branch from Kurdish: Paul places it "more closely related to Gorani and the
(Iranian) Azari dialects than to Kurdish". Its Latin orthography is derived
from the Turkish alphabet, with ⟨x⟩, ⟨q⟩ and the diacritics ⟨'⟩ and ⟨^⟩ added,
so the letters it shares with Kurmanji do not all share Kurmanji's values.

Sources actually read for these targets:
- Paul, L. (2009) "Zazaki", ch. 9 of Windfuhr (ed.) *The Iranian Languages*,
  Routledge, pp. 545-548 — §1.1, §2.1, Tables 9.1 and 9.2, §2.2.
- Werner, B. (2012) *Morphological Sketch of Southern Zazaki spoken in the area
  of Çermik, Çüngüş, Siverek and Gerger*, SIL International, pp. 5-7 — the
  "Zazaki Alphabet" letter/IPA table and its footnote 3.

The example words below are Werner's own table entries where possible.
"""
from __future__ import annotations

from orthography2ipa.g2p import G2P
from orthography2ipa.registry import get

ZZA = "zza"


def _ipa(word: str) -> str:
    return G2P(ZZA).transcribe_word(word).lstrip("ˈˌ")


# ── Turkish, not Kurmanji, vowel-letter values ─────────────────────────────

def test_a_is_the_back_open_vowel():
    """Werner's alphabet table prints ⟨A a⟩ = [ɑ]; Kurmanji reads ⟨a⟩ as [aː]."""
    assert _ipa("adır") == "ɑdɨɾ"        # 'fire'


def test_i_is_close_front_and_dotless_i_is_the_central_vowel():
    """Zazaki writes two distinct vowels where Kurmanji writes one letter.

    Paul's Table 9.1 has a close front /i/ and no lax /ɪ/; Werner singles out
    dotless ⟨ı⟩ as the letter whose value departs from Turkish, "a lax central
    vowel, while in Turkish ı represents a tense back vowel". Reading ⟨i⟩ as
    [ɪ] is the Kurmanji value and asserts a vowel Zazaki's inventory lacks.
    """
    assert _ipa("isot").startswith("i")   # 'pepper'
    assert _ipa("ıstare").startswith("ɨ")  # 'star'
    assert _ipa("isot") != _ipa("ıstare")


# ── Flap / trill ───────────────────────────────────────────────────────────

def test_single_r_is_the_flap_and_rr_the_trill():
    """Paul's Table 9.2 lists "Vibrants, flap/trill" as a two-way contrast."""
    assert _ipa("par") == "pɑɾ"           # 'last year' — Werner's flap example
    assert _ipa("zerri") == "zɛri"        # 'heart'     — Werner's trill example
    assert _ipa("perr") == "pɛr"          # 'leaf'


def test_word_initial_vibrant_is_trilled_though_written_single():
    """Werner p. 7 n. 3: "all word-initially vibrants are realized as
    (thrilled), but represented by single /r/"."""
    assert _ipa("roj") == "roʒ"           # 'day'


# ── Velarized lateral and ayin ─────────────────────────────────────────────

def test_double_l_is_the_velarized_lateral():
    """Werner marks ⟨'l⟩ word-initially and ⟨ll⟩ elsewhere as velarized."""
    assert "ɫ" in _ipa("boll")            # 'much'


def test_ayin_is_pharyngeal_not_glottal():
    """Werner's table prints ⟨' (eyn)⟩ = [ʕ]. Both the ASCII apostrophe and
    U+2018, which the source itself uses, must reach the same phoneme."""
    assert _ipa("‘ereba").startswith("ʕ")   # 'car'
    assert _ipa("'ereba") == _ipa("‘ereba")


# ── The spec is no longer a Kurmanji template ──────────────────────────────

def test_zazaki_does_not_read_the_shared_letters_the_kurmanji_way():
    """⟨a⟩ and ⟨i⟩ are the two letters whose Kurmanji values are wrong for
    Zazaki. ⟨r⟩ is deliberately not checked here: Kurmanji reads it as the
    flap too, so the two specs agreeing on it is correct, not a copy."""
    zza, ku = get(ZZA).graphemes, get("ku").graphemes
    for letter in ("a", "i"):
        assert zza[letter] != ku[letter], letter
    # digraphs Kurmanji has no use for
    assert "rr" in zza and "rr" not in ku
    assert "ll" in zza and "ll" not in ku


def test_spec_cites_a_real_grammar_not_an_encyclopedia():
    authors = {s.author for s in get(ZZA).sources}
    assert "Wikipedia contributors" not in authors
    assert any(a.startswith("Paul") for a in authors)
    assert any(a.startswith("Werner") for a in authors)
