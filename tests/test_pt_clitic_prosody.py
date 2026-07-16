"""Portuguese clitic prosody and stress-interaction fixes.

Covers four corrections to the pan-Portuguese prosody, all expressed in the
lect data (``stress.cliticless_words`` / ``word_exceptions``) over the generic
engine — no language logic lives in the engine:

P1  Function words (definite articles, monosyllabic prepositions and their
    preposition-article contractions, the conjunction ``e``, the complementizer
    ``que`` and the unstressed object pronoun clitics) form no prosodic word of
    their own and bear NO word stress (Vigário 2003, *The Prosodic Word in
    European Portuguese*; Cunha & Cintra, *Nova Gramática do Português
    Contemporâneo*, on átonos/clíticos). Declared per-lect in
    ``stress.cliticless_words``.

P2  The coordinating conjunction ``e`` is raised to [i] in modern Portuguese
    (EP and BP alike; and verbatim [i] in Barrancos per Navas), but keeps its
    unraised [e] in the medieval / Galician-Portuguese stages. Data:
    ``word_exceptions {"e": "i"}`` on pt-PT and pt-BR (inherited by their
    modern children), absent from pt-PT-x-medieval and roa-x-galaicopt.

P3  North-western tonic-mid diphthongisation ([e]→[je], [o]→[wo]; Brissos 2018,
    Cintra 1971) must fire only on lexically stressed ORAL mids, never on an
    unstressed proclitic. Because a clitic is now marked as bearing no stress,
    the stress-gated diphthongisation rule is withheld from it.

P4  Alentejo final-vowel apocope (Brissos 2014) must not relocate the word
    stress: ⟨fazendo⟩ → [fɐˈzẽd], keeping the original tonic, not *[ˈfɐzẽd].
"""
from __future__ import annotations

import unicodedata

import pytest

from orthography2ipa import G2P, transcribe
from orthography2ipa.stress import StressRules, apply_stress_mark


def _has_mark(s: str) -> bool:
    return "ˈ" in s or "ˌ" in s


def _n(s: str) -> str:
    # The engine emits nasality as a combining tilde; normalise both sides so
    # the literals below can be written either way.
    return unicodedata.normalize("NFC", s)


# ── P1: function words carry no word stress ──────────────────────────────────

# The generic engine already suppresses the mark on any form listed in a lect's
# ``stress.cliticless_words``; here we assert the pan-Portuguese list is present
# and active on a spread of lects (EP, BP, insular, African, historical).
CLITICS = ["o", "a", "os", "as", "de", "em", "por", "da", "na", "ao", "às",
           "e", "do", "no", "que", "me", "se", "lhe"]

P1_LECTS = ["pt-PT", "pt-BR", "pt-PT-x-lisbon", "pt-PT-x-porto",
            "pt-PT-x-braga", "pt-PT-x-alentejo", "pt-PT-x-acores",
            "pt-BR-x-sp", "pt-AO", "pt-MZ", "pt-PT-x-medieval",
            "roa-x-galaicopt", "ext-PT-x-barrancos"]


@pytest.mark.parametrize("lect", P1_LECTS)
def test_function_words_are_unstressed(lect):
    eng = G2P(lect)
    for w in CLITICS:
        out = eng.transcribe(w)
        assert not _has_mark(out), f"{lect}: clitic {w!r} got word stress: {out}"


def test_enclitic_pronoun_is_unstressed():
    # liga-me: the host ⟨liga⟩ keeps its stress, the enclitic ⟨-me⟩ takes none.
    out = transcribe("liga-me", "pt-PT")
    host, _, clitic = out.partition(" ")
    assert _has_mark(host), out
    assert not _has_mark(clitic), out


def test_indefinite_article_um_keeps_stress():
    # ⟨um⟩/⟨uns⟩ are prosodic words, not clitics, and are NOT in the list.
    assert transcribe("um", "pt-PT-x-beira") == "ˈum"
    assert transcribe("uns", "pt-PT-x-beira") == "ˈunʃ"


# ── P2: conjunction e → [i] (modern), [e] (historical) ───────────────────────

@pytest.mark.parametrize("lect", ["pt-PT", "pt-BR", "pt-PT-x-lisbon",
                                  "pt-PT-x-braga", "pt-BR-x-sp", "pt-AO",
                                  "pt-UY", "ext-PT-x-barrancos"])
def test_conjunction_e_raises_to_i_modern(lect):
    assert transcribe("e", lect) == "i", lect


@pytest.mark.parametrize("lect", ["pt-PT-x-medieval", "roa-x-galaicopt"])
def test_conjunction_e_stays_e_historical(lect):
    # Pre-raising stage: ⟨e⟩ keeps [e] (no /e/ > /i/ raising yet).
    assert transcribe("e", lect) == "e", lect


# ── P3: NW diphthongisation gated to stressed oral mids only ─────────────────

DIPHTHONGISING = ["pt-PT-x-braga", "pt-PT-x-porto"]


@pytest.mark.parametrize("lect", DIPHTHONGISING)
def test_stressed_oral_mid_still_diphthongises(lect):
    # The primary Brissos 2018 rows are all oral and lexically stressed.
    eng = G2P(lect)
    assert eng.transcribe("mês") == "ˈmjeʃ"      # close-mid front [e] → [je]
    assert eng.transcribe("avô") == "ɐˈbwo"      # close-mid back  [o] → [wo]
    assert eng.transcribe("pé") == "ˈpjɛ"        # open-mid front  [ɛ] → [jɛ]
    assert eng.transcribe("só") == "ˈswɔ"        # open-mid back   [ɔ] → [wɔ]


@pytest.mark.parametrize("lect", DIPHTHONGISING)
def test_proclitic_mid_does_not_diphthongise(lect):
    # Unstressed clitics must escape the rule (no [ˈwo]/[ˈje]/[ˈjẽ]).
    eng = G2P(lect)
    assert eng.transcribe("o") == "o"     # article, not [ˈwo]
    assert eng.transcribe("os") == "oʃ"   # not [ˈwoʃ]
    assert eng.transcribe("e") == "i"     # conjunction (raised), not [ˈje]
    assert _n(eng.transcribe("em")) == _n("ẽ")  # nasal clitic, not [ˈjẽ]


@pytest.mark.parametrize("lect", DIPHTHONGISING)
def test_stressed_nasal_mid_does_not_diphthongise(lect):
    # A genuinely stressed NASAL mid is [ẽ]/[õ], never oral [e]/[o], so it never
    # matches the oral-mid rule (bem, contente, cimento, momento).
    eng = G2P(lect)
    for w in ("bem", "contente", "cimento", "momento", "bom", "contém"):
        assert "j" not in eng.transcribe(w), (lect, w)
        assert "w" not in eng.transcribe(w), (lect, w)


# ── P4: apocope must not move the stress ─────────────────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("fazendo", "fɐˈzẽd"),
    ("falando", "fɐˈlɐ̃d"),
    ("cantando", "kɐ̃ˈtɐ̃d"),
    ("bebendo", "bɨˈbẽd"),
    ("dizendo", "diˈzẽd"),
])
def test_alentejo_apocope_keeps_tonic(word, expected):
    # Final unstressed -o is deleted; the primary stress stays on the original
    # tonic penult, it does not slide to the first syllable.
    assert _n(transcribe(word, "pt-PT-x-alentejo")) == _n(expected)


def test_apply_stress_mark_underflow_final_apocope():
    # Unit: IPA with FEWER syllables than the spelling because a final vowel was
    # apocopated (consonant-final result) → start-anchor keeps the mark on the
    # original tonic instead of dragging it forward.
    rules = StressRules(diphthongs=("ãe", "ão"))
    # orthographic fa-zen-do (3 sylls), paroxytone stress_index=1; IPA fɐzẽd.
    out = apply_stress_mark("fɐzẽd", rules, 1, syllables=["fa", "zen", "do"])
    assert _n(out) == _n("fɐˈzẽd")


def test_apply_stress_mark_underflow_digraph_overcount_is_end_anchored():
    # Guard: a vowel-final IPA with fewer syllables is an orthographic
    # over-count of a digraph (⟨linya⟩ → [ˈliɲa]), NOT an apocope — it must fall
    # through to end-anchoring and land on the penult, not the final syllable.
    rules = StressRules()
    out = apply_stress_mark("liɲa", rules, 0, syllables=["li", "ny", "a"])
    assert out == "ˈliɲa"
