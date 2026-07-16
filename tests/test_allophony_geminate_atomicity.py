"""Geminate atomicity in the post-lexical allophone layer (engine-generic).

A geminate is phonologically a single long consonant. When the input spells
it doubled — and the tokenizer's shadda expansion realises it as two
identical, contiguous, same-grapheme slots — a single-segment allophone rule
triggered by material OUTSIDE the geminate must not rewrite just one half and
manufacture a heterorganic cluster the language never has.

The canonical break was Najdi velar affrication: ⟨دقّ⟩ /diɡɡ/ surfaced as
*[didzɡ] because the affrication rule (``/ɡ/ → [dz]`` after a front vowel)
fired on the first half of the geminate /ɡɡ/ — the half adjacent to the /i/ —
leaving the second half /ɡ/. Ingham (1994) and Alhoody (2020) attest that
Najdi affrication does not apply to geminates; the correct surface is [diɡɡ].

The guard is generic — it reads only the phonological neighbourhood, never a
language or script — and it does NOT block a genuine gemination process, which
is *about* the geminate and states so by conditioning on the doubled phoneme
in its own neighbour context (Tamil's paired ``TA_GEM1``/``TA_GEM2`` realise
⟨க்க⟩ as the coordinated [kː]).
"""
from __future__ import annotations

import pytest

from orthography2ipa import get
from orthography2ipa.allophony import compile_allophone_rescorer
from orthography2ipa.g2p import G2P
from orthography2ipa.phonetok import PhonetokTokenizer
from orthography2ipa.types import AllophoneRule, LanguageSpec


# ─── helpers (mirroring tests/test_allophone_rules.py) ─────────────────────

def _spec(graphemes, rules=(), *, code="xx-gem"):
    return LanguageSpec(
        code=code, name="Test", family="Test", script="Latin",
        graphemes=graphemes, allophones={}, allophone_rules=tuple(rules),
    )


def _tok_best(spec, word):
    tok = PhonetokTokenizer(spec)
    resc = compile_allophone_rescorer(spec.allophone_rules)
    return tok.ipa_best(word, rescorer=resc)


# ─── Engine-generic unit tests (synthetic language, no real data) ──────────

def test_external_rule_does_not_split_a_geminate():
    """A rule fired by an outside neighbour leaves a geminate whole.

    ``/ɡ/ → [dz]`` after a front vowel — the Najdi affrication shape. On the
    geminate ⟨gg⟩ /ɡɡ/ of /diɡɡ/ the /i/ is adjacent only to the FIRST half;
    the rule must not split the unit, so both halves stay /ɡ/.
    """
    affric = AllophoneRule(id="AFFRIC_G", phonemes=("ɡ",), surface="dz",
                           preceded_by_phoneme=("i",))
    spec = _spec({"d": ["d"], "i": ["i"], "g": ["ɡ"]}, (affric,))
    assert _tok_best(spec, "digg") == "diɡɡ"


def test_external_rule_still_fires_on_a_single_consonant():
    """The guard is scoped to geminates: a lone /ɡ/ after /i/ still affricates."""
    affric = AllophoneRule(id="AFFRIC_G", phonemes=("ɡ",), surface="dz",
                           preceded_by_phoneme=("i",))
    spec = _spec({"d": ["d"], "i": ["i"], "g": ["ɡ"]}, (affric,))
    assert _tok_best(spec, "dig") == "didz"


def test_geminate_aware_rule_may_rewrite_a_half():
    """A rule conditioned on the twin phoneme is *about* the geminate.

    Modelled on Tamil's paired gemination rules: the first half, seeing its
    twin to the right, lengthens; the second half, seeing its twin to the left,
    deletes — together the coordinated long [kː]. Because both rules name the
    twin /k/ in their neighbour context, the guard lets them fire.
    """
    gem1 = AllophoneRule(id="GEM1_k", phonemes=("k",), surface="kː",
                         followed_by_phoneme=("k",))
    gem2 = AllophoneRule(id="GEM2_k", phonemes=("k",), surface="",
                         preceded_by_phoneme=("k",))
    spec = _spec({"a": ["a"], "k": ["k"]}, (gem1, gem2))
    assert _tok_best(spec, "akka") == "akːa"


# ─── Real-data integration: the ledger probes ──────────────────────────────

@pytest.fixture(scope="module")
def najd():
    return G2P("ar-SA-x-najd")


def test_najdi_geminate_qaf_does_not_affricate(najd):
    """⟨دقّ⟩ /diɡɡ/ — the geminate blocks velar affrication (Ingham 1994).

    Before the fix the first half of /ɡɡ/ affricated to [dz] and the second
    stayed [ɡ], yielding the heterorganic *[didzɡ] Ingham does not attest.
    """
    assert najd.transcribe("دِقّ") == "ˈdiɡɡ"


def test_najdi_affrication_still_fires_on_single_velar(najd):
    """A non-geminate /k/ before a front vowel still affricates: ⟨ديك⟩ → [diːts]."""
    assert najd.transcribe("دِيك") == "ˈdiːts"


def test_najdi_geminate_after_non_front_is_unchanged(najd):
    """⟨حقّ⟩ /ħaɡɡ/ — geminate after /a/ never affricated, and still doesn't."""
    assert najd.transcribe("حَقّ") == "ˈħaɡɡ"


def test_tamil_geminate_still_lengthens():
    """The real Tamil paired rules survive the guard: ⟨அக்கா⟩ → [akːaː]."""
    assert G2P("ta").transcribe("அக்கா") == "akːaː"


def test_abugida_cv_cv_is_not_mistaken_for_a_geminate():
    """Two adjacent identical CV syllables are not a geminate.

    ⟨அங்கக⟩ /aŋɡaɡa/ has two ⟨க⟩ slots each carrying its inherent /a/ (ka, ka)
    — two syllables, not a doubled consonant. Post-nasal and intervocalic
    voicing must still apply to both, so the guard (which fires only on a bare
    consonant with no vowel) must leave this word alone.
    """
    assert G2P("ta").transcribe("அங்கக") == "aŋɡaɡa"
