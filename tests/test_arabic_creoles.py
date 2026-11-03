"""Arabic-lineage contact languages: the rules that separate a Juba Arabic,
Ki-Nubi or Cypriot Maronite Arabic transcription from a mainstream Arabic one.

Three languages descend from Arabic but broke away from it hard enough to earn
their own ISO 639-3 codes and their own (Latin) orthographies:

* **Juba Arabic** (`pga`) and **Ki-Nubi** (`kcn`) — the two surviving
  Arabic-based creoles, sisters descended from one 19th-century southern-Sudanese
  pidgin (Owens 1997; Manfredi 2017). Both are cited here from their open-access,
  verifiable APiCS Online survey chapters (Manfredi & Petrollino 2013, chapter 64;
  Luffin 2013, chapter 63): a five-vowel system, wholesale loss of the Arabic
  pharyngeals and emphatics, and a *distinctive* stress realised as high pitch.

* **Cypriot Maronite Arabic** (`acy`) — 800 years isolated on Cyprus under
  Cypriot Greek, derived by Borg (1985, 2004) from a qeltu / North-Mesopotamian
  ("Syrian-Anatolian") antecedent, not from Levantine.

Every claim below is isolated on a real word and cited to the spec's own sources.
"""
import pytest

from orthography2ipa import get, transcribe


# ─── The shared clade: two creoles, one pidgin ancestor ────────────────────

def test_sudanic_creole_clade_groups_juba_and_nubi():
    """Juba Arabic and Ki-Nubi are literature-recognised sisters of one
    southern-Sudanese pidgin (Owens 1997; Manfredi 2017), so both hang from a
    single clade node whose derived family names that group."""
    for code in ("pga", "kcn"):
        assert get(code).parent == "x-clade-sudanic-creole"
        assert "Sudanic Creole Arabic" in get(code).family
    clade = get("x-clade-sudanic-creole")
    assert clade.clade is True
    # Hung under the Semitic clade (Glottolog gives the group no single code);
    # the Arabic lexifier link lives on each member's ancestors[], not by
    # inheritance, so the creoles do not pick up mainstream-Arabic allophony.
    assert clade.parent == "x-clade-semi1276"
    for code in ("pga", "kcn"):
        lexifiers = {a.code for a in get(code).ancestors if a.role.value == "lexifier"}
        assert "ar-SD" in lexifiers


# ─── Juba Arabic (pga), APiCS chapter 64 ───────────────────────────────────

def test_pga_is_a_five_vowel_system():
    """Manfredi & Petrollino (2013) give five vowel phonemes a e i o u with no
    length and no emphatic/plain split — the Arabic three-quality-plus-length
    system collapsed."""
    vowels = {v for readings in get("pga").graphemes.values() for v in readings
              if v in set("aeiou") or v in {"aː", "iː", "uː", "eː", "oː"}}
    assert vowels == {"a", "e", "i", "o", "u"}


def test_pga_has_no_pharyngeals_or_emphatics():
    """The 20-segment inventory has no pharyngeal column and no emphatic series:
    Arabic ħ ʕ and tˤ dˤ sˤ ðˤ have no reflex (Manfredi & Petrollino 2013)."""
    emitted = {ipa for readings in get("pga").allophones.values() for ipa in readings}
    assert not (emitted & {"ħ", "ʕ", "tˤ", "dˤ", "sˤ", "ðˤ", "zˤ"})


def test_pga_stress_is_distinctive_high_pitch():
    """Stress is a distinctive high pitch: sába 'seven' vs. sabá 'morning'
    (APiCS ch.64). The acute in the practical orthography pins the stressed
    vowel, so the two words stress differently."""
    assert transcribe("sába", "pga") == "ˈsaba"
    assert transcribe("sabá", "pga") == "saˈba"


def test_pga_latin_orthography_digraphs():
    """The modelled Latin orthography reads j=/dʒ/ and š/sh=/ʃ/ (APiCS ch.64):
    jol 'person', šedíd 'strong'."""
    assert get("pga").graphemes["j"] == ["dʒ"]
    assert get("pga").graphemes["š"] == ["ʃ"]
    assert transcribe("jol", "pga") == "ˈdʒol"


def test_pga_has_implosive_in_substrate_loans():
    """ɓ is an implosive from the Nilotic substrate: ɓéko 'to find'
    (Manfredi & Petrollino 2013)."""
    assert transcribe("ɓéko", "pga") == "ˈɓeko"


# ─── Ki-Nubi (kcn), APiCS chapter 63 ───────────────────────────────────────

def test_kcn_is_a_five_vowel_system_without_length():
    """Luffin (2013): five vowels i e a o u, vowel length not distinctive."""
    vowels = {v for readings in get("kcn").graphemes.values() for v in readings
              if v in set("aeiou")}
    assert vowels == {"a", "e", "i", "o", "u"}
    assert not any(len(v) > 1 and v.endswith("ː")
                   for readings in get("kcn").graphemes.values() for v in readings)


def test_kcn_lost_pharyngeals_and_emphatics():
    """The native inventory has no pharyngeals and no emphatics; Arabic kabīr →
    kebír, kalām → kalám show the pharyngeal-free, interdental-free reflexes
    (Luffin 2013; Wellens 2005)."""
    emitted = {ipa for readings in get("kcn").allophones.values() for ipa in readings}
    assert not (emitted & {"ħ", "ʕ", "tˤ", "dˤ", "sˤ", "ðˤ"})
    assert transcribe("kebír", "kcn") == "keˈbir"


def test_kcn_stress_marks_the_passive():
    """Stress is grammatically distinctive: límu 'to gather' vs. limú 'to be
    gathered' — the passive is a rightward stress shift (Luffin 2013)."""
    assert transcribe("límu", "kcn") == "ˈlimu"
    assert transcribe("limú", "kcn") == "liˈmu"


def test_kcn_marginal_loan_phonemes_are_present_but_ranked_last():
    """p, tʃ, v etc. are marginal, entering through Arabic/Swahili/English loans
    (Luffin 2013): /dʒ/ can front to [tʃ] in loans."""
    assert "tʃ" in get("kcn").allophones["dʒ"]
    assert get("kcn").graphemes["v"] == ["v"]


# ─── Cypriot Maronite Arabic (acy), Borg (1985, 2004) ──────────────────────

def test_acy_cites_borg_and_the_qeltu_ancestry():
    """Borg (1985, 2004) is the reference grammar and derives CMA from a qeltu /
    North-Mesopotamian antecedent, encoded as the ar-IQ-x-qeltu ancestry link."""
    spec = get("acy")
    ids = {s.id for s in spec.sources}
    assert {"borg1985", "borg2004"} <= ids
    codes = {a.code for a in spec.ancestors}
    assert "ar-IQ-x-qeltu" in codes
    assert "el" in codes  # Cypriot Greek adstrate


def test_acy_lost_pharyngeals_uvular_q_became_k():
    """Greek contact: pharyngeals ħ/ʕ lost, uvular q → /k/ (Borg 1985)."""
    allo = get("acy").allophones
    assert allo["q"] == ["k"]
    assert "" in allo["ʕ"]           # ʕ → ∅ (or h)
    assert set(allo["ħ"]) <= {"h", ""}


def test_acy_keeps_interdentals_and_gains_greek_p_v():
    """θ and ð are retained (reinforced by Greek θ/δ); /p/ and /v/ enter from
    Greek, which mainstream Arabic lacks (Borg 1985; Newton 1964)."""
    g = get("acy").graphemes
    assert g["θ"] == ["θ"] and g["ð"] == ["ð"]
    assert g["p"] == ["p"] and g["v"] == ["v"]


def test_acy_emphatics_deemphaticised():
    """Emphatics are weakened: the emphatic series carries a plain reflex as a
    ranked alternative (Borg 1985 deemphasisation)."""
    allo = get("acy").allophones
    assert "s" in allo["sˤ"] and "t" in allo["tˤ"] and "d" in allo["dˤ"]
