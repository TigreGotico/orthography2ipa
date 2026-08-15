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
    """Transcribe *word*, without the leading word-stress mark.

    These tests pin SEGMENTAL claims — which phoneme a grapheme yields in a
    given environment. Where the stress mark falls is a separate claim, pinned
    by ``tests/test_stress.py`` and by
    ``tests/test_english_stress_reduction.py``, so it is stripped here rather
    than repeated in every expected string.

    The strip is unconditional rather than scoped to one language because
    EVERY assertion in this file is segmental: the German half already
    stripped the mark call-by-call, and a per-language strip would just be
    the same rule written twice. Nothing here asserts the presence, absence
    or position of a stress mark, so nothing here can be weakened by
    removing it — a test that needs the mark belongs in the stress files.
    """
    return G2P(code).transcribe_word(word).lstrip("ˈ")


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


@pytest.mark.xfail(
    strict=True,
    reason="Cruttenden (2014): get/give/girl retain [ɡ]; engine now produces "
    "[dʒɛt], [dʒɪv], [dʒɜːɹl] — ⟨g⟩ softens to [dʒ] before every front vowel with "
    "no exception carve-out (regression from dropping the enumerated n-grams)",
)
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

    Isolated on the silent ⟨e⟩: each word ends on its final consonant, with no
    vowel or schwa contributed by the ⟨e⟩ (the preceding nucleus quality is a
    separate matter).
    """
    assert _t("en-GB", "hope").endswith("p")
    assert _t("en-GB", "mate").endswith("t")
    assert _t("en-GB", "time").endswith("m")
    assert _t("en-GB", "judge").endswith("dʒ")


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

    Carried by `grammatical_endings` — suffix morphology, matched at the
    effective word end, not a grapheme n-gram (Cruttenden 2014
    spelling-to-sound correspondence rules; Chomsky & Halle 1968 on the
    palatalization before `-ion`).
    """
    assert _t("en-GB", "nation").endswith("ʃən")
    assert _t("en-GB", "mission").endswith("ʃən")


@pytest.mark.xfail(
    strict=True,
    reason="Cruttenden (2014): -sion → [ʒən]/[ʃən]; the engine produces "
    "[vɪzɪɒn] for vision and [tɛnsɪɒn] for tension. The split is conditioned on "
    "the segment BEFORE the ending, and `grammatical_endings` carries no "
    "preceding-segment condition, so the ending is spelled out s-i-o-n",
)
def test_en_gb_sion_voiced_after_vowel():
    """-sion → [ʒən] after a vowel, [ʃən] after a consonant.

    en-GB notes: "the ⟨-sion⟩ split ([ʒən] after a vowel, [ʃən] after a
    consonant) needs a preceding-segment condition on `grammatical_endings`,
    which the ending table does not carry" (Cruttenden 2014).

    A true minimal pair on the context, not the grapheme: vision vs tension.
    """
    assert _t("en-GB", "vision").endswith("ʒən")
    assert _t("en-GB", "division").endswith("ʒən")
    assert _t("en-GB", "tension").endswith("ʃən")
    assert _t("en-GB", "pension").endswith("ʃən")


def test_en_gb_tial_cial_and_cious_tious():
    """-tial/-cial → [ʃəl]; -cious/-tious → [ʃəs].

    Same mechanism as -tion: `grammatical_endings` entries matched at the
    effective word end (Cruttenden 2014 spelling-to-sound correspondence
    rules; Wells 2008 LPD for the surface values).
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
    exactly the words the note names: ⟨gh⟩ must contribute no segment — night and
    though carry neither a [ɡ] nor an [f].
    """
    assert _t("en-GB", "night") == "naɪt"
    though = _t("en-GB", "though")
    assert "ɡ" not in though and "f" not in though


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


def test_en_gb_lot_vowel_is_rounded():
    """LOT = /ɒ/ (rounded).

    en-GB notes: "LOT = /ɒ/ (rounded); GOAT = /əʊ/." Source: Wells (1982) vol.
    1–2, Cruttenden (2014).

    Isolated on the nucleus: the ⟨o⟩ of lot and dog resolves to the rounded [ɒ].
    """
    assert _t("en-GB", "lot") == "lɒt"


@pytest.mark.parametrize("word,expected", [
    ("car", "kɑː"),        # ɑːɹ, word-final
    ("park", "pɑːk"),      # ɑːɹ, pre-consonantal
    ("father", "fæðə"),    # əɹ
    ("bird", "bɜːd"),      # ɜːɹ
    ("north", "nɔːθ"),     # ɔːɹ
    ("care", "kɛə"),       # ɛəɹ
    ("beer", "bɪə"),       # ɪəɹ
    ("fire", "faɪə"),      # aɪəɹ, word-final
    ("flour", "flaʊə"),    # aʊəɹ
    ("turn", "tɜːn"),      # ɜːɹ from ⟨ur⟩
    ("tired", "taɪəd"),    # aɪəɹ, pre-consonantal
])
def test_en_gb_non_rhotic_covers_every_rhotic_nucleus(word, expected):
    """NON-RHOTIC CODA /r/ applies to every rhotic nucleus, not just ⟨ar⟩.

    en-GB notes: "RP keeps /r/ only before a vowel, so every rhotic nucleus
    (ɑːɹ, ɜːɹ, ɔːɹ, əɹ, ɛəɹ, ɪəɹ, ʊəɹ, aɪəɹ, aʊəɹ, and bare ɹ) loses its [ɹ]
    before a consonant and word-finally."
    Wells (1982) vol. 1 §3.2.2; Cruttenden (2014) §8.7.
    """
    assert _t("en-GB", word) == expected


def test_en_gb_linking_r_survives_before_a_vowel():
    """The same spelling keeps [ɹ] when the ⟨r⟩ is prevocalic.

    The complementary environment of the deletion rule above: RP is non-rhotic,
    not r-less — /r/ survives before a vowel (Wells 1982 vol. 1 §3.2.2).
    """
    assert "ɹ" in _t("en-GB", "caring")
    assert "ɹ" in _t("en-GB", "carry")
    assert _t("en-GB", "rose").startswith("ɹ")


@pytest.mark.parametrize("word,expected", [
    ("marry", "mæɹi"),
    ("merry", "mɛɹi"),
    # unstressed second syllable: the ⟨or⟩ nucleus reduces to /ə/ and RP's
    # non-rhotic rule then deletes the coda [ɹ] — Wells 2008 LPD gives
    # ˈmɪɹə (Cruttenden 2014 §9.4 on the weak vowel of an unstressed syllable)
    ("mirror", "mɪɹə"),
    ("hurry", "hʌɹi"),
    ("sorry", "sɒɹi"),
    ("spirit", "spɪɹɪt"),
])
def test_en_gb_prevocalic_r_takes_the_checked_vowel(word, expected):
    """PREVOCALIC ⟨r⟩: the nucleus is the CHECKED vowel, not the long one.

    en-GB notes: "where the ⟨r⟩ is the onset of the next syllable the nucleus
    is the CHECKED vowel, not the long r-coloured one — marry [ˈmæɹi], merry
    [ˈmɛɹi], mirror [ˈmɪɹə], hurry [ˈhʌɹi], sorry [ˈsɒɹi]."
    Wells (1982) vol. 1 §2.2.6; Carney (1994).
    """
    assert _t("en-GB", word) == expected


def test_en_gb_prevocalic_r_shortening_needs_a_following_vowel():
    """The complementary environment: word-final ⟨rr⟩ keeps the long nucleus.

    ⟨Carr⟩ has no following vowel for the ⟨r⟩ to be an onset of, so the
    checked-vowel rule must not fire and the nucleus stays [ɑː].
    """
    assert _t("en-GB", "carr") == "kɑː"


def test_en_gb_goat_is_schwa_initial():
    """GOAT = /əʊ/ in RP.

    en-GB notes: "LOT = /ɒ/ (rounded); GOAT = /əʊ/."
    Wells (1982) vol. 1–2; Roach (2004) JIPA.
    """
    assert _t("en-GB", "boat") == "bəʊt"
    assert _t("en-GB", "toe") == "təʊ"


def test_en_gb_word_final_vowel_letters():
    """WORD-FINAL VOWEL LETTERS: ⟨a⟩ → [ə], ⟨o⟩ → [əʊ].

    en-GB notes: "unstressed word-final ⟨a⟩ is /ə/ (sofa, America, data) and
    word-final ⟨o⟩ is /əʊ/ (photo, piano, go)." Carney (1994).

    Complementary environment: the same letters keep their non-final values in
    ⟨cat⟩ and ⟨lot⟩ (pinned by test_en_gb_lot_vowel_is_rounded above).
    """
    assert _t("en-GB", "sofa") == "səʊfə" or _t("en-GB", "sofa").endswith("ə")
    assert _t("en-GB", "data").endswith("ə")
    assert _t("en-GB", "photo").endswith("əʊ")
    assert _t("en-GB", "go") == "ɡəʊ"
    assert _t("en-GB", "cat") == "kæt"


def test_en_gb_y_is_a_vowel_letter():
    """⟨y⟩ is declared a vowel letter (`vowel_graphemes`).

    en-GB notes: "⟨y⟩ is declared a vowel letter (`vowel_graphemes`): it is the
    nucleus of very, myth, happy." Carney (1994) treats ⟨y⟩ as a vowel letter
    of the English writing system.

    Falsifiable on the neighbour context it feeds: the ⟨r⟩ of ⟨very⟩ is
    prevocalic, so it is not deleted by the non-rhotic rule.
    """
    assert _t("en-GB", "very") == "vɛɹi"
    assert G2P("en-GB").spec.vowel_graphemes == ("y",)


@pytest.mark.parametrize("word,expected", [
    ("nature", "nætʃə"),
    ("picture", "pɪktʃə"),
    ("measure", "miːʒə"),
    ("pressure", "pɹɛʃə"),
    ("famous", "fæməs"),
])
def test_en_gb_ture_sure_ous_endings(word, expected):
    """SUFFIX PALATALIZATION: ⟨-ture⟩ [tʃə], ⟨-sure⟩ [ʒə], ⟨-ssure⟩ [ʃə];
    ⟨-ous⟩ [əs].

    Yod coalescence in the ⟨-ture⟩/⟨-sure⟩ suffixes and the reduced ⟨-ous⟩
    suffix vowel: Wells (2008) LPD; Cruttenden (2014) §9.7. Carried by
    `grammatical_endings`, so ⟨-ssure⟩ wins over ⟨-sure⟩ by longest match, the
    same way ⟨-ssion⟩ wins over ⟨-sion⟩.
    """
    assert _t("en-GB", word) == expected


# ── ⟨-ed⟩ / ⟨-s⟩ allomorphy and velar nasal assimilation ─────────────


@pytest.mark.parametrize("word,ending", [
    # [ɪd] after an alveolar plosive
    ("wanted", "tɪd"),
    ("ended", "dɪd"),
    # [t] after any other voiceless consonant
    ("walked", "kt"),
    ("missed", "st"),
    ("packed", "kt"),
    # [d] elsewhere
    ("played", "eɪd"),
    ("loved", "vd"),
])
def test_en_gb_ed_allomorphy(word, ending):
    """⟨-ed⟩ is [ɪd] after /t d/, [t] after other voiceless, [d] elsewhere.

    en-GB EN_GB_ED_EPENTHESIS / EN_GB_ED_SYNCOPE / EN_GB_ED_DEVOICING notes:
    "English past-tense / past-participle ⟨-ed⟩ has three regular allomorphs
    conditioned by the final segment of the stem: [ɪd] after an alveolar
    plosive (wanted, ended), [t] after any other voiceless consonant (walked,
    missed), and [d] elsewhere (played, loved). Cruttenden 2014, § 4.3;
    Wells 2008 LPD gives the same three surface values."

    All three branches are pinned together: the ending is the only thing that
    differs between them, so a rule that swallowed one branch into another
    would break at least one row.
    """
    assert _t("en-GB", word).endswith(ending)


@pytest.mark.parametrize("word,ending", [
    ("dogs", "ɡz"),
    ("beds", "dz"),
    ("films", "mz"),
])
def test_en_gb_final_s_voices_after_voiced_consonant(word, ending):
    """Word-final ⟨-s⟩ after a voiced consonant is [z].

    en-GB EN_GB_FINAL_S_VOICING notes: "Word-final ⟨-s⟩ after a voiced
    consonant is [z], not [s]: dogs, beds, films (Cruttenden 2014,
    § 4.3 on the voicing agreement of the ⟨-s⟩ ending; Wells 2008 LPD)."
    """
    assert _t("en-GB", word).endswith(ending)


@pytest.mark.parametrize("word", ["cats", "bus", "this"])
def test_en_gb_final_s_stays_voiceless(word):
    """The complementary environment of EN_GB_FINAL_S_VOICING.

    ⟨cats⟩ pins the voiceless-consonant environment; ⟨bus⟩ and ⟨this⟩ pin the
    deliberate restriction the same note states — "after a vowel the spelling
    is ambiguous between the ending (sees, boys) and a stem-final ⟨s⟩ (bus,
    gas, this, us), and telling them apart needs morphology this engine
    deliberately does not have" — so a later widening of the rule to all
    vowels would fail here rather than silently voice ⟨bus⟩.
    """
    assert _t("en-GB", word).endswith("s")


def test_en_gb_velar_nasal_assimilation_is_not_shipped():
    """EN_GB_VELAR_NASAL_ASSIMILATION was dropped in PR #856's fix round.

    The rule was unconditioned and fired across morpheme boundaries where
    broad transcription conventions keep [n] (``unkind``, ``increase``,
    ``pancake`` — the negative prefix ``un-`` and the ``in-``/``pan-``
    boundary are not the tautosyllabic, single-morpheme environment
    Cruttenden 2014, § 9.4 describes for ``think``/``bank``/``uncle``).
    Cruttenden treats the cross-boundary case as optional/casual-speech
    assimilation, not obligatory broad-transcription fact, and the rule's
    measured benchmark contribution was marginal (LOO -0.0007) — not worth
    the false positives without a citable boundary-aware condition.
    """
    assert "ŋ" not in _t("en-GB", "unkind")
    assert "ŋ" not in _t("en-GB", "increase")
    assert "ŋ" not in _t("en-GB", "pancake")


@pytest.mark.parametrize("word,expected", [
    ("fed", "fɛd"), ("ted", "tɛd"), ("bed", "bɛd"), ("led", "lɛd"),
    ("red", "ɹɛd"), ("wed", "wɛd"), ("zed", "zɛd"), ("ped", "pɛd"),
    ("sed", "sɛd"), ("shed", "ʃɛd"),
])
def test_en_gb_stem_ed_monosyllables_are_not_past_tense(word, expected):
    """The ⟨ed⟩ of a monosyllabic STEM is not the past-tense ending.

    en-GB notes: "Whether a given ⟨ed⟩ IS that ending is a lexical fact, not
    an orthographic one — Carney 1994, ch. 3 treats the ⟨ed⟩ spelling as
    ambiguous between the ending and a stem the letters simply spell — and
    this engine has no morphology to decide it." The three ⟨-ed⟩ rules
    (EPENTHESIS, SYNCOPE, DEVOICING) each require ``preceded_by_2``/
    ``preceded_by_3="any"`` — a real stem grapheme standing before the
    stem-final consonant — which is what now keeps these three-letter
    /Cɛd/ monosyllables out WITHOUT a ``word_exceptions`` carve-out: there
    is nothing before the single stem consonant to satisfy the gate.

    The complementary environment of the ⟨-ed⟩ allomorphy tests above: same
    final four letters, no syncope and no devoicing.
    """
    assert _t("en-GB", word) == expected


@pytest.mark.xfail(
    reason=(
        "Known residual, PR #856 fix round: obstruent+liquid cluster-onset "
        "monosyllables whose /Cɛd/ IS the stem (bled, bred, cred, fled, "
        "pled, shred, sled, sped) still mis-syncope, because the stem "
        "grapheme immediately before the mute <e> (a consonant) is "
        "indistinguishable, at the grapheme-class level, from a genuine "
        "polysyllabic stem's final consonant before the same ending — both "
        "read as 'consonant' two graphemes back. Unlike the plain /Cɛd/ "
        "monosyllables above, this class has no citable phonological "
        "condition to close it (deliberately not enumerated in "
        "word_exceptions — see PR body residual list)."
    ),
    strict=True,
)
@pytest.mark.parametrize("word,expected", [
    ("bled", "blɛd"), ("bred", "bɹɛd"), ("cred", "kɹɛd"),
    ("fled", "flɛd"), ("pled", "plɛd"), ("shred", "ʃɹɛd"),
    ("sled", "slɛd"), ("sped", "spɛd"),
])
def test_en_gb_cluster_onset_ed_monosyllables_are_a_known_residual(
        word, expected):
    """Documented hole, not a regression to chase: see docstring above."""
    assert _t("en-GB", word) == expected


@pytest.mark.parametrize("word,ending", [
    ("pleased", "zd"), ("breathed", "ðd"),
])
def test_en_gb_ed_devoicing_reads_the_surface_stem_not_the_declared_candidate(
        word, ending):
    """A voiced-resolving stem consonant must NOT trigger devoicing.

    en-GB EN_GB_ED_DEVOICING notes: the voicing trigger is read as the
    resolved SURFACE phoneme of the stem-final slot (``preceded_by_surface_
    phoneme_2``), not that grapheme's first declared candidate — ⟨s⟩'s and
    ⟨th⟩'s first declared candidate is voiceless ([s], [θ]), but both
    resolve voiced ([z], [ð]) intervocalically in ``pleased``/``breathed``
    before this rule ever runs (Cruttenden 2014, § 4.3).
    """
    assert _t("en-GB", word).endswith(ending)


def test_en_gb_ed_devoicing_fires_after_an_affricate_stem():
    """⟨watch⟩ ends in the affricate [tʃ] — devoicing must see it as ONE
    segment two graphemes back, not split it into [t] + [ʃ] and miss the
    match (Cruttenden 2014, § 4.3, [t] after any voiceless consonant)."""
    assert _t("en-GB", "watched").endswith("tʃt")


# ===========================================================================
# en-US / rhotic descendants — General American and friends
# ===========================================================================


@pytest.mark.parametrize("code", ["en-US", "en-CA", "en-IE",
                                  "en-GB-x-scotland"])
def test_rhotic_descendants_keep_coda_r(code):
    """A rhotic descendant re-declares the RP deletion ids with no phonemes.

    Each spec's notes state it is rhotic (Wells 1982 vol. 3 §6.1 for GA), and
    an inherited `allophone_rules` entry can only be disabled by id, so the
    claim is falsifiable exactly here: coda /r/ must survive.
    """
    assert _t(code, "car").endswith("ɹ")
    assert "ɹ" in _t(code, "park")


@pytest.mark.parametrize("code", ["en-AU", "en-ZA"])
def test_non_rhotic_descendants_inherit_the_deletion(code):
    """The complementary case: en-AU and en-ZA declare themselves non-rhotic
    and inherit RP's coda-/r/ deletion unchanged (Wells 1982 vol. 3)."""
    assert _t(code, "car") == "kɑː"


def test_en_us_lot_palm_merger():
    """LOT-PALM merger: GA has no /ɒ/.

    en-US notes: "LOT-PALM merger: /ɑː/ for both."
    Wells (1982) vol. 3 §6.1.3; Ladefoged & Johnson (2011).
    """
    assert "ɒ" not in _t("en-US", "lot")
    assert "ɒ" not in _t("en-US", "sofa")


def test_en_us_goat_is_o_initial():
    """GA GOAT is /oʊ/, not the RP /əʊ/ its parent declares.

    en-US notes: "GA GOAT is /oʊ/, not the RP /əʊ/ this spec's parent
    declares." Wells (1982) vol. 3 §6.1.4.
    """
    assert _t("en-US", "boat") == "boʊt"
    assert _t("en-US", "go") == "ɡoʊ"


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
    ⟨d⟩ devoiced; the vowel here stays short -- a closed monosyllable has no
    following vowel to trigger open-syllable lengthening, and free vowel length
    in a closed German monosyllable is not recoverable from spelling alone, a
    known engine-limit exception) vs Baden → [ˈbaːdən] (the same ⟨d⟩, now medial
    and in an open syllable, stays voiced; the vowel is long by the
    open-syllable lengthening rule -- Wiese 1996).
    """
    assert _t("de-DE", "Bad") == "bat"
    assert _t("de-DE", "Baden").startswith("baː")


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


# ---------------------------------------------------------------------------
# en-US — the General American transcription conventions
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("word,expected", [
    ("bird", "bɝd"), ("nurse", "nɝz"), ("herd", "hɝd"),
])
def test_en_us_nurse_is_r_coloured(word, expected):
    """Stressed NURSE is the r-coloured vowel ɝ, not vowel + rhotic.

    en-US rule EN_US_NURSE_RCOLOURED: "General American has TRUE r-coloured
    vowels, written with the rhotacised symbols ɝ (stressed NURSE) and ɚ
    (unstressed lettER)". Wells (1982) vol. 3 §6.1.2; Kenyon & Knott (1953);
    Ladefoged & Johnson (2011) ch. 4; Kretzschmar (2004) §2.
    """
    assert _t("en-US", word) == expected


@pytest.mark.parametrize("word,expected", [
    ("doctor", "dɑktɚ"), ("dollar", "dɑlɚ"), ("standard", "stændɚd"),
    ("aardvark", "ɑɹdvɚk"),
])
def test_en_us_letter_is_r_coloured_schwa(word, expected):
    """Unstressed lettER is ɚ — the same vowel as ɝ without the accent.

    en-US rule EN_US_LETTER_RCOLOURED. Wells (1982) vol. 3 §6.1.2;
    Kenyon & Knott (1953).

    KNOWN LIMIT, stated rather than hidden: the rule keys on the parent's
    ə + rhotic reading, so ⟨-er⟩ words whose ⟨er⟩ the weights resolve to
    the NURSE reading instead (``letter`` → lɛtɝ) come out with the
    STRESSED symbol. Conditioning the rule on ``stress="unstressed"``
    fixes those words and is the correct phonology, but was measured
    PER-NEGATIVE on the gold that has the distinction at all (ipadict
    en-US 0.3549 → 0.3652 at the 1000-word sample), because that gold
    writes ɝ in unstressed position too. The orthographic proxy is kept
    as the better-measuring of two imperfect statements.
    """
    assert _t("en-US", word) == expected


@pytest.mark.parametrize("word", ["car", "park", "see", "food", "feel",
                                  "more", "lot", "coffee", "bird",
                                  # the yod-plus-GOOSE compound and the frozen
                                  # function words: both reach the output by a
                                  # route the plain per-vowel rules cannot see,
                                  # so the invariant only has teeth with them
                                  "cue", "value", "accrue", "beauty",
                                  "be", "he", "me", "we", "she"])
def test_en_us_carries_no_length_marks(word):
    """GA is transcribed WITHOUT length marks; its RP parent keeps them.

    en-US notes: "General American is conventionally transcribed WITHOUT
    length marks: the RP length contrast this spec's parent declares is not
    part of the GA system". Wells (1982) vol. 3 §6.1.1; Kenyon & Knott
    (1953); Labov, Ash & Boberg (2006) §2.1; Kretzschmar (2004) §2.

    The complementary half is the point: en-GB must still HAVE the mark on
    the words where RP is long, so this is a dialect difference and not the
    engine having lost the ability to emit it.
    """
    assert "ː" not in _t("en-US", word)


def test_en_gb_keeps_the_length_marks_en_us_drops():
    """Minimal pair for the rule above: RP long vowels stay long."""
    assert "ː" in _t("en-GB", "car")
    assert "ː" in _t("en-GB", "see")
    assert "ː" in _t("en-GB", "food")


@pytest.mark.parametrize("word", ["water", "butter", "city", "ladder"])
def test_en_us_default_transcription_is_phonemic_not_flapped(word):
    """Flapping is allophonic, so it is NOT in the default (broad) output.

    en-US notes: "BROAD BY DECLARATION: the default transcription is
    PHONEMIC. T/D-FLAPPING and word-initial aspiration are sub-phonemic
    realisations of /t/ and /d/ ... so they are declared in `allophones` ...
    and NOT forced into the default output by `positional_graphemes`."
    Wells (1982) vol. 3 §6.1.5; Kretzschmar (2004) §2; Kenyon & Knott (1953).
    """
    assert "ɾ" not in _t("en-US", word)


def test_en_us_still_declares_the_flap_and_the_aspirate_as_allophones():
    """The complementary half: dropping them from the DEFAULT output must not
    drop the claim that GA has them. They stay in `allophones`, the field
    that states a phoneme's surface variants.

    BOTH stops are guarded. /d/ has no explicit key in en-US.json — it
    arrives through `allophones_base: en-GB` — so without this assertion the
    d-flap claim rests on an inherited table nothing in this file pins, and a
    parent edit could silently drop it while the /t/ test stayed green.
    """
    from orthography2ipa import get
    allo = get("en-US").allophones
    assert set(allo["t"]) >= {"t", "tʰ", "ɾ"}
    assert set(allo["d"]) >= {"d", "ɾ"}


@pytest.mark.parametrize("word", ["tuna", "ten", "top"])
def test_en_us_default_transcription_is_not_aspirated(word):
    """Same claim, aspiration half. Ladefoged & Johnson (2011) ch. 3 treat
    aspiration as an allophone of the voiceless stop series."""
    assert "ʰ" not in _t("en-US", word)


def test_en_us_aa_digraph_is_one_vowel():
    """⟨aa⟩ occurs in English only in loans and names, where GA reads it as
    the single low back vowel ɑ (Wells 2008 LPD) — not as two ⟨a⟩s, which
    would give the word a spurious extra syllable."""
    assert _t("en-US", "aardvark") == "ɑɹdvɚk"
    assert _t("en-US", "aachen").startswith("ɑ")
