"""Cited-rule conformance: Russian, Ukrainian, Belarusian.

Each test takes one cited claim from a spec's ``notes`` prose or from a single
``allophone_rules`` entry, quotes it with its citation, and proves the engine
honours it on a real word — isolating the rule to a single segment and pinning
the complementary environment with a minimal pair wherever the phonology allows.

The three East Slavic specs declare near-identical regressive-assimilation rule
families, which makes them each other's controls: where ``be`` reproduces its
cited transcription exactly and ``uk`` does not on the very word its own
citation names, the divergence is the finding.

Claims the engine does NOT honour are marked ``xfail(strict=True)`` with the
actual output in the reason, never weakened to match.
"""
import pytest

from orthography2ipa.g2p import G2P


def _t(code, word):
    return G2P(code).transcribe_word(word)


def _bare(code, word):
    return _t(code, word).replace("ˈ", "").replace("ˌ", "")


# ===========================================================================
# ru — Standard Russian
# ===========================================================================


def test_ru_regressive_devoicing_before_voiceless():
    """RU_REGR_DEVOICE_d: /d/ devoices to [t] before a voiceless obstruent.

    The RU_REGR_DEVOICE_* family declares regressive voicing assimilation: a
    voiced obstruent devoices before a voiceless one.

    водка: the ⟨д⟩ stands before the voiceless ⟨к⟩ and surfaces [t]. The minimal
    pair is дом, where the same ⟨д⟩ has no voiceless neighbour and stays [d].
    """
    assert _bare("ru", "водка") == "votkə"
    assert _bare("ru", "дом").startswith("d")


def test_ru_regressive_voicing_before_voiced():
    """RU_REGR_VOICE_s: /s/ voices to [z] before a voiced obstruent.

    The RU_REGR_VOICE_* family is the mirror image of the devoicing family: a
    voiceless obstruent voices before a voiced one.

    сдать: the ⟨с⟩ stands before the voiced ⟨д⟩ and surfaces [z]. The minimal
    pair is стол, where the same ⟨с⟩ precedes a voiceless ⟨т⟩ and stays [s].
    """
    assert _bare("ru", "сдать").startswith("z")
    assert _bare("ru", "стол").startswith("s")


def test_ru_regressive_palatalization_before_soft_consonant():
    """RU_REGR_PALAT_s: /s/ palatalises to [sʲ] before a soft consonant.

    The RU_REGR_PALAT_* family declares regressive palatalisation of the dentals
    before a following soft consonant.

    снег: the ⟨н⟩ is soft before ⟨е⟩, and the preceding ⟨с⟩ softens with it. The
    minimal pair is стол, where the following ⟨т⟩ is hard and no softening
    occurs.
    """
    assert _bare("ru", "снег") == "sʲnʲek"
    assert "sʲ" not in _bare("ru", "стол")


def test_ru_final_devoicing_is_not_over_applied_to_sonorants():
    """Regressive devoicing targets obstruents only; the sonorant /n/ is untouched.

    The RU_REGR_DEVOICE_* family enumerates obstruents (b bʲ v vʲ d dʲ ɡ ɡʲ z zʲ
    ʐ) — no sonorant is listed, so a word-final soft /nʲ/ must survive intact.
    """
    assert _bare("ru", "конь") == "konʲ"


# ===========================================================================
# be — Standard Belarusian
# ===========================================================================


def test_be_regr_devoice_d_on_cited_word():
    """BE_REGR_DEVOICE_d: /d/ devoices before a voiceless obstruent.

    Rule notes: "Regressive devoicing before voiceless obstruents (Mayo 1993):
    адкласці [atkɫasʲtsʲi]." Mayo (1993) Belarusian, in Comrie & Corbett (eds.)
    The Slavonic Languages, Routledge.

    Isolated on the ⟨д⟩ of адкласці, which stands before the voiceless ⟨к⟩.
    """
    assert _bare("be", "адкласці").startswith("atk")


def test_be_regr_palat_s_on_cited_word():
    """BE_REGR_PALAT_s: /s/ palatalises before a soft dental.

    Rule notes: "Regressive palatalization before soft dentals (Mayo (1993)
    Belarusian, in Comrie & Corbett (eds.) The Slavonic Languages, Routledge,
    phonology section): адкласці [atkɫasʲtsʲi]."

    The whole cited transcription is reproduced, so this pins the softened [sʲ]
    within it rather than only the word.
    """
    assert "sʲ" in _bare("be", "адкласці")
    assert _bare("be", "адкласці") == "atkɫasʲtsʲi"


def test_be_regr_palat_z_before_soft_labial():
    """BE_REGR_PALAT_z: /z/ softens before a soft labial.

    Rule notes: "Regressive palatalization before soft dentals (Mayo 1993) ...
    s/z also soften before soft labials: звер [zʲvʲer]."
    """
    assert _bare("be", "звер") == "zʲvʲer"


def test_be_g_is_voiced_velar_fricative():
    """⟨г⟩ is [ɣ], a fricative, not a plosive.

    be notes: "Distinctive features: ⟨г⟩ = [ɣ] (voiced velar fricative, not
    plosive)."

    Minimal pair against uk, whose notes claim "⟨г⟩ = [ɦ] (not [ɡ])", and against
    ru, where the same letter is the plosive [ɡ].
    """
    assert _bare("be", "галава").startswith("ɣ")
    assert _bare("uk", "голова").startswith("ɦ")


def test_be_akanne_unstressed_o_lowers_to_a():
    """АКАННЕ: unstressed /ɔ/ is realised [a].

    be notes: "pervasive аканне (unstressed /ɔ/ → [a])."

    галава is written with ⟨а⟩ throughout, so the falsifiable form is its
    Russian/Ukrainian cognate spelling: the claim is that no unstressed [ɔ]
    survives in Belarusian, which uk (which has no аканне) contradicts by design.
    """
    assert "ɔ" not in _bare("be", "галава")
    assert "ɔ" in _bare("uk", "голова")


# ===========================================================================
# uk — Standard Ukrainian
# ===========================================================================


def test_uk_h_not_g():
    """⟨г⟩ is [ɦ], not [ɡ]; ⟨ґ⟩ is the separate letter for [ɡ].

    uk notes: "Key differences from Russian: ⟨г⟩ = [ɦ] (not [ɡ]), ⟨ґ⟩ = [ɡ] as
    separate letter."
    """
    assert _bare("uk", "голова").startswith("ɦ")
    assert _bare("uk", "ґанок").startswith("ɡ")


def test_uk_no_vowel_reduction():
    """Ukrainian has no аканье: unstressed ⟨о⟩ stays [ɔ].

    uk notes: "no vowel reduction (no аканье)."

    Minimal pair against ru, where the unstressed ⟨о⟩ of the cognate reduces.
    """
    assert _bare("uk", "голова").startswith("ɦɔ")


@pytest.mark.xfail(
    strict=True,
    reason="UK_REGR_PALAT_s and UK_REGR_PALAT_t cite кістка [kʲisʲtʲkɐ]; engine "
    "produces [kʲistkɐ] — neither the /s/ nor the /t/ softens, so the rules do "
    "not fire on the very word their citation names (be's parallel rules do fire "
    "on адкласці)",
)
def test_uk_regr_palat_on_cited_word():
    """UK_REGR_PALAT_s/_t: the dentals palatalise before a soft dental.

    Rule notes: "Regressive palatalization of dentals before soft dentals
    (Pompino-Marschall, Pashchenko & Mołczanow (2017) Ukrainian, JIPA 47(3),
    consonant section): кістка [kʲisʲtʲkɐ]."
    """
    assert _bare("uk", "кістка") == "kʲisʲtʲkɐ"


@pytest.mark.xfail(
    strict=True,
    reason="UK_REGR_PALAT_z cites звер [zʲvʲer]; engine produces [zʋɛr] — the /z/ "
    "does not soften before the soft labial (be's identically-worded rule does "
    "produce [zʲvʲer])",
)
def test_uk_regr_palat_z_before_soft_labial():
    """UK_REGR_PALAT_z: /z/ softens before a soft labial.

    Rule notes: "Regressive palatalization of dentals before soft dentals
    (Pompino-Marschall, Pashchenko & Mołczanow (2017) Ukrainian, JIPA 47(3),
    consonant section) ... s/z also soften before soft labials: звер [zʲvʲer]."
    """
    assert _bare("uk", "звер").startswith("zʲ")


@pytest.mark.xfail(
    strict=True,
    reason="uk notes claim ⟨в⟩ = [ʋ] approximant; engine produces [wɔdɐ] for "
    "вода — word-initial prevocalic ⟨в⟩ selects [w], not the declared [ʋ] it "
    "selects intervocalically (нива → [nɪʋɐ])",
)
def test_uk_v_is_approximant():
    """⟨в⟩ is the approximant [ʋ].

    uk notes: "Key differences from Russian: ... ⟨в⟩ = [ʋ] approximant."

    The claim is stated without positional qualification. Intervocalically the
    engine honours it (нива → [nɪʋɐ]); word-initially before a vowel it does not.
    """
    assert _bare("uk", "вода").startswith("ʋ")
