"""Cited-rule conformance: English (RP) and German.

Each test takes one cited claim from a spec's ``notes`` prose or from a single
rule entry, quotes it with its citation, and proves the engine honours it on a
real word — isolating the rule to a single segment and pinning the complementary
environment with a minimal pair wherever the phonology allows one.

Claims the engine does NOT honour are marked ``xfail(strict=True)`` with the
actual output in the reason, never weakened to match.
"""
import pytest

from orthography2ipa.g2p import G2P


def _t(code, word):
    return G2P(code).transcribe_word(word)


# ===========================================================================
# en-GB — Received Pronunciation
# ===========================================================================


def test_en_gb_c_softening():
    """C SOFTENING: ⟨c⟩ → [s] before e/i/y, [k] elsewhere.

    en-GB notes: "C/G SOFTENING: c→[s] and g→[dʒ] before e/i/y (city, gem)."
    Source: Wells (1982) vol. 1–2, Cruttenden (2014).

    Minimal pair: city (before ⟨i⟩ → [s]) vs cat (before ⟨a⟩ → [k]).
    """
    assert _t("en-GB", "city").startswith("s")
    assert _t("en-GB", "cat").startswith("k")


def test_en_gb_g_softening():
    """G SOFTENING: ⟨g⟩ → [dʒ] before e/i/y.

    en-GB notes: "c→[s] and g→[dʒ] before e/i/y (city, gem)." Cruttenden (2014).
    """
    assert _t("en-GB", "gem").startswith("dʒ")


def test_en_gb_g_softening_exceptions():
    """The get/give/girl exception class keeps hard [ɡ] before a front vowel.

    en-GB notes: "exceptions: get, give, girl retain [ɡ]." Cruttenden (2014).

    The complementary environment for the softening rule above: same ⟨g⟩ + front
    vowel, different outcome, so this pins the carve-out and not the rule.
    """
    assert _t("en-GB", "get").startswith("ɡ")
    assert _t("en-GB", "give").startswith("ɡ")
    assert _t("en-GB", "girl").startswith("ɡ")


def test_en_gb_intervocalic_s_voices():
    """INTERVOCALIC s: [z] between vowels, [s] word-initially.

    en-GB notes: "INTERVOCALIC s: [z] between vowels (rose, nose) but [s]
    word-initially." Wells (1982).
    """
    assert _t("en-GB", "rose").endswith("z")
    assert _t("en-GB", "sit").startswith("s")


def test_en_gb_th_distinction():
    """TH DISTINCTION: [θ] in content words, [ð] in function words and intervocalically.

    en-GB notes: "TH DISTINCTION: [θ] in content words, [ð] in function words and
    intervocalically." Cruttenden (2014).

    Three-way isolation of the same ⟨th⟩ digraph: think (content word → [θ]),
    the (function word → [ð]), other (intervocalic → [ð]).
    """
    assert _t("en-GB", "think").startswith("θ")
    assert _t("en-GB", "the").startswith("ð")
    assert "ð" in _t("en-GB", "other")


def test_en_gb_x_word_initial_is_z():
    """X WORD-INITIAL: [z], vs [ks] elsewhere.

    en-GB notes: "X WORD-INITIAL: [z] (xylophone) vs [ks] elsewhere."
    Cruttenden (2014).
    """
    assert _t("en-GB", "xylophone").startswith("z")
    assert "ks" in _t("en-GB", "box")


def test_en_gb_silent_final_e():
    """SILENT FINAL E: word-final ⟨e⟩ after a consonant is not pronounced.

    en-GB notes: "SILENT FINAL E: orthographic word-final <e> after a consonant
    is not pronounced (mate, hope, time, judge)." Cruttenden (2014).
    """
    assert _t("en-GB", "hope") == "həʊp"
    assert _t("en-GB", "time") == "taɪm"
    assert _t("en-GB", "judge") == "dʒʌdʒ"


def test_en_gb_final_e_function_word_exceptions():
    """The pronounced-final-⟨e⟩ function words are carved out of the silent-e rule.

    en-GB notes: "A small closed class of function words spelled with a
    genuinely pronounced final <e> (the, be, he, me, we, she) is carved out via
    `word_exceptions`, since the blanket positional rule cannot distinguish these
    monosyllables from the regular silent-e pattern."

    The complementary environment for the silent-e rule above.
    """
    assert _t("en-GB", "be") == "biː"
    assert _t("en-GB", "he") == "hiː"
    assert _t("en-GB", "she") == "ʃiː"


def test_en_gb_non_rhotic():
    """NON-RHOTIC: /r/ is deleted before a consonant and word-finally.

    en-GB notes: "NON-RHOTIC: /r/ deleted before consonants and word-finally."
    Wells (1982) vol. 1–2.

    Minimal pair on ⟨r⟩: deleted in car (word-final) and cart (pre-consonantal),
    but kept in rose (onset).
    """
    assert _t("en-GB", "car") == "kɑː"
    assert _t("en-GB", "cart") == "kɑːt"
    assert _t("en-GB", "rose").startswith("ɹ")


def test_en_gb_tion_family_sh():
    """TION/SION FAMILY: -tion and -ssion → [ʃən].

    en-GB notes: "TION/SION FAMILY: -tion/-cian -> [ʃən], -ssion -> [ʃən]
    (mission, passion; matched via the dedicated `ssion` grapheme so
    maximal-munch tokenization picks it over `sion`)" (Cruttenden 2014
    spelling-to-sound correspondence rules).
    """
    assert _t("en-GB", "nation").endswith("ʃən")
    assert _t("en-GB", "mission").endswith("ʃən")


def test_en_gb_sion_voiced_after_vowel():
    """-sion → [ʒən] after a vowel, [ʃən] after a consonant.

    en-GB notes: "-sion -> [ʒən] after a vowel (vision, division, decision) or
    [ʃən] after a consonant (tension, pension, mansion), modelled with the `sion`
    entry in `positional_graphemes` using AFTER_VOWEL/AFTER_CONSONANT context"
    (Cruttenden 2014).

    A true minimal pair on the context, not the grapheme: vision vs tension.
    """
    assert _t("en-GB", "vision").endswith("ʒən")
    assert _t("en-GB", "division").endswith("ʒən")
    assert _t("en-GB", "tension").endswith("ʃən")
    assert _t("en-GB", "pension").endswith("ʃən")


def test_en_gb_tial_cial_and_cious_tious():
    """-tial/-cial → [ʃəl]; -cious/-tious → [ʃəs].

    en-GB notes: "-tial/-cial -> [ʃəl], -cious/-tious -> [ʃəs] (Cruttenden 2014
    spelling-to-sound correspondence rules)."
    """
    assert _t("en-GB", "special").endswith("ʃəl")
    assert _t("en-GB", "delicious").endswith("ʃəs")


def test_en_gb_gh_weight_favours_silent():
    """CANDIDATE WEIGHTS: ⟨gh⟩ = [ɡ 0.03, f 0.12, silent 0.85] — the beam picks silent.

    en-GB notes: "CANDIDATE WEIGHTS: a few ambiguous graphemes carry
    per-candidate `weights` (candidate frequencies) so the beam favours the
    corpus-dominant phoneme rather than the declared-first one — ... `gh` = [ɡ
    0.03, f 0.12, silent 0.85] (⟨gh⟩ is silent in the vast majority of words:
    night, though, high, weigh)."

    The claim is about which candidate the beam SELECTS, so it is falsifiable on
    exactly the words the note names: ⟨gh⟩ must contribute no segment.
    """
    assert _t("en-GB", "night") == "naɪt"
    assert _t("en-GB", "though") == "ðəʊ"


@pytest.mark.xfail(
    strict=True,
    reason="Wells (1982) TRAP-BATH split claims BATH words = /ɑː/; engine "
    "produces [kæsəl] for castle and [ɡɹæs] for grass — the BATH lexical set is "
    "not distinguished from TRAP, both reading ⟨a⟩ as [æ]",
)
def test_en_gb_trap_bath_split():
    """TRAP-BATH split: BATH words take /ɑː/, not the TRAP vowel /æ/.

    en-GB notes: "TRAP-BATH split: BATH words = /ɑː/ (castle, grass, dance)."
    Source: Wells (1982) vol. 1–2.

    The split is lexical, and the spec declares no BATH wordlist, so the two
    words the note names as BATH come out with the TRAP vowel.
    """
    assert "ɑː" in _t("en-GB", "castle")
    assert "ɑː" in _t("en-GB", "grass")


@pytest.mark.xfail(
    strict=True,
    reason="Wells (1982) LOT = /ɒ/ (rounded); engine produces [lɑːt] for lot and "
    "[dɔːɡ] for dog — the ⟨o⟩ candidate set never selects [ɒ]",
)
def test_en_gb_lot_vowel_is_rounded():
    """LOT = /ɒ/ (rounded).

    en-GB notes: "LOT = /ɒ/ (rounded); GOAT = /əʊ/." Source: Wells (1982) vol.
    1–2, Cruttenden (2014).

    Isolated on the nucleus: GOAT does resolve as [əʊ] (hope → [həʊp]), so the
    contrast the note draws is only half honoured.
    """
    assert _t("en-GB", "lot") == "lɒt"


# ===========================================================================
# de-DE — Standard German
# ===========================================================================


def test_de_auslautverhaertung_b():
    """AUSLAUTVERHÄRTUNG: /b/ devoices to [p] word-finally.

    de-DE notes: "AUSLAUTVERHÄRTUNG: obstruents devoiced word-finally (b→p, d→t,
    g→k, v→f)." Sources: Wiese (1996), Hall (2003), Mangold (2005).
    """
    assert _t("de-DE", "Kalb").endswith("p")


def test_de_auslautverhaertung_d_minimal_pair():
    """AUSLAUTVERHÄRTUNG: /d/ devoices to [t] word-finally, but not medially.

    de-DE notes: "obstruents devoiced word-finally (b→p, d→t, g→k, v→f)."
    Wiese (1996).

    The minimal pair that isolates the rule to its position: Bad → [bat] (final
    ⟨d⟩ devoiced) vs Baden → [badɛn] (the same ⟨d⟩, now medial, stays voiced).
    """
    assert _t("de-DE", "Bad") == "bat"
    assert _t("de-DE", "Baden").startswith("bad")


def test_de_auslautverhaertung_g():
    """AUSLAUTVERHÄRTUNG: /ɡ/ devoices to [k] word-finally.

    de-DE notes: "obstruents devoiced word-finally (b→p, d→t, g→k, v→f)."
    Hall (2003).
    """
    assert _t("de-DE", "Tag") == "tak"


def test_de_auslautverhaertung_v():
    """AUSLAUTVERHÄRTUNG: /v/ devoices to [f] word-finally.

    de-DE notes: "obstruents devoiced word-finally (b→p, d→t, g→k, v→f)."
    Mangold (2005).

    Minimal pair: brav (final ⟨v⟩ → [f]) vs viel, where the same letter is an
    onset and stays [v].
    """
    assert _t("de-DE", "brav").endswith("f")
    assert _t("de-DE", "viel").startswith("v")


def test_de_sp_st_word_initial_hushing():
    """SP/ST: [ʃp]/[ʃt] word-initially, [sp]/[st] elsewhere.

    de-DE notes: "SP/ST: [ʃp]/[ʃt] word-initially, [sp]/[st] elsewhere."
    Wiese (1996), Mangold (2005).

    Minimal pair on the ⟨sp⟩ cluster: Spiel (word-initial → [ʃp]) vs Wespe
    (medial → [sp]).
    """
    assert _t("de-DE", "Spiel").startswith("ʃp")
    assert _t("de-DE", "Stein").startswith("ʃt")
    assert "sp" in _t("de-DE", "Wespe")


def test_de_ach_laut_after_back_vowel():
    """CH: the ach-Laut [x] after back vowels a/o/u.

    de-DE notes: "CH (ich-Laut/ach-Laut): [x] after back vowels a/o/u ... [ç]
    after front vowels e/i, after consonants, and word-initially before front
    vowels." Wiese (1996), Hall (2003).
    """
    assert _t("de-DE", "Bach").endswith("x")
    assert _t("de-DE", "Buch").endswith("x")
    assert _t("de-DE", "Loch").endswith("x")


def test_de_ich_laut_after_front_vowel():
    """CH: the ich-Laut [ç] after front vowels e/i.

    de-DE notes: "[x] after back vowels a/o/u ... [ç] after front vowels e/i."
    Wiese (1996), Hall (2003).

    The complementary environment of the ach-Laut above — same digraph, one
    segment of difference, conditioned solely on the preceding nucleus.
    """
    assert _t("de-DE", "ich").endswith("ç")


def test_de_no_glottal_stop_insertion():
    """Glottal-stop insertion before vowel-initial syllables is deliberately not encoded.

    de-DE notes: "Glottal stop insertion before vowel-initial syllables (Kohler
    1990; Wikipedia German phonology) is attested but not phonemic and frequently
    absent even in careful speech outside northern varieties, and is not encoded
    in wikipron-style gold transcriptions used for benchmarking, so it is
    deliberately not inserted to avoid a spurious PER regression."

    A declared omission, pinned so it cannot appear by accident.
    """
    assert "ʔ" not in _t("de-DE", "Abend")
