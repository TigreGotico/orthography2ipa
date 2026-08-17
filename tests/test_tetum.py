"""Tetum — Tetun Dili (``tet``) and Tetun Terik (``tet-x-terik``).

Tetun Dili is the Austronesian national language of Timor-Leste, written in the
orthography the Instituto Nacional de Linguística curates, and its phonology is
stratified: a small native Austronesian stock beside a very large Portuguese
loan stratum that brought phonemes, clusters and stress patterns with it. These
tests exercise BOTH strata, because a spec that only reads native words is not a
spec for the language people actually write.

The phonological claims live in the specs' own ``notes`` and ``sources``, with
the printed pages they stand on; the docstrings below name the source and point
there rather than restating the citation.
"""
from orthography2ipa import get
from orthography2ipa.g2p import G2P
from orthography2ipa.types import GraphemePosition


def _t():
    return G2P("tet")


def _terik():
    return G2P("tet-x-terik")


# ── the Portuguese-derived letters ──────────────────────────────────────────

def test_j_is_a_fricative_not_an_affricate():
    """⟨j⟩ is /ʒ/. The affricate [dʒ] is a hypercorrection under Indonesian
    spelling and belongs in the allophone list, not the grapheme table
    (Williams-van Klinken, Hajek & Nordlinger 2002)."""
    spec = get("tet")
    assert spec.graphemes["j"] == ["ʒ"]
    assert _t().transcribe("janela") == "ʒaˈnela"
    assert "dʒ" in spec.allophones["ʒ"]


def test_x_is_the_voiceless_counterpart_of_j():
    """⟨x⟩ is /ʃ/, and the merger with /s/ that less Portuguese-influenced
    speakers make is an allophone of it."""
    spec = get("tet")
    assert spec.graphemes["x"] == ["ʃ"]
    assert spec.allophones["ʃ"] == ["ʃ", "s"]


def test_both_palatal_spelling_conventions_are_read():
    """⟨nh lh⟩ and Hull's ⟨ñ ll⟩ spell the same two palatals, so text in either
    convention reads identically."""
    spec = get("tet")
    assert spec.graphemes["nh"] == spec.graphemes["ñ"] == ["ɲ"]
    assert spec.graphemes["lh"] == spec.graphemes["ll"] == ["ʎ"]
    assert _t().transcribe("milhaun") == _t().transcribe("millaun")


def test_portuguese_loan_consonants_are_present():
    """/p ɡ v z ʃ ʒ ɲ ʎ/ enter through Portuguese and are part of the maximal
    inventory the spec declares."""
    inventory = set(get("tet").phonemes)
    assert {"p", "ɡ", "v", "z", "ʃ", "ʒ", "ɲ", "ʎ"} <= inventory


def test_speaker_mergers_are_allophones_not_readings():
    """Speakers without the Portuguese stratum merge /v/-/b/, /ʒ/-/z/, /ɲ/-/n/
    and /ʎ/-/l/; each merger target is a second allophone."""
    allo = get("tet").allophones
    assert allo["v"] == ["v", "b"]
    assert "z" in allo["ʒ"] and "n" in allo["ɲ"] and "l" in allo["ʎ"]


def test_c_is_the_indonesian_loan_letter():
    """⟨c⟩ occurs only in Indonesian loans, where it spells /c/."""
    assert get("tet").graphemes["c"] == ["c"]


# ── what the inventory does NOT contain ─────────────────────────────────────

def test_no_velar_nasal_phoneme():
    """Neither source's consonant table has /ŋ/: it is a word-final variant of
    /n/, so it is positional, and ⟨ng⟩ is not a digraph of the language."""
    spec = get("tet")
    assert "ŋ" not in spec.phonemes
    assert "ng" not in spec.graphemes
    assert spec.positional_graphemes["n"][GraphemePosition.WORD_FINAL] == ["n", "ŋ"]


def test_ng_spells_a_sequence_in_loans():
    """With no ⟨ng⟩ digraph, a loan spelling reads as /nɡ/."""
    assert _t().transcribe("Inglés").startswith("i") and "ɡ" in _t().transcribe("Inglés")


def test_dili_has_no_glottal_stop_phoneme():
    """The glottal stop is a phoneme of Terik, not of Dili, while the INL
    spelling still writes it. The source names ha'u and hau as spellings of the
    same Dili word, so ⟨'⟩ reads as nothing first and keeps [ʔ] as the second
    candidate for the conservative pronunciation; Terik has only the stop."""
    assert "ʔ" not in get("tet").phonemes
    assert get("tet").graphemes["'"] == ["", "ʔ"]
    assert _t().transcribe("ha'u") == "ˈhau"
    assert "ˈhaʔu" in _t().word_candidates("ha'u", k=3)
    assert get("tet-x-terik").graphemes["'"] == ["ʔ"]
    assert "ʔ" in get("tet-x-terik").phonemes
    assert _terik().transcribe("ha'u") == "ˈhaʔu"


def test_final_k_is_not_glottalised():
    """Word-final voiceless stops are unreleased, not glottal; the [ʔ] variant
    of /k/ belongs to word-initial /kC/ clusters."""
    spec = get("tet")
    assert "k" not in spec.positional_graphemes
    assert spec.allophones["k"] == ["k", "ʔ"]
    assert _t().transcribe("labarik") == "laˈbarik"


# ── the acute accent ────────────────────────────────────────────────────────

def test_accented_vowels_are_graphemes():
    """⟨á é í ó ú⟩ are letters of the orthography. Before they were mapped the
    engine dropped them, and Timór came out /timr/."""
    spec = get("tet")
    for plain, accented in [("a", "á"), ("e", "é"), ("i", "í"),
                            ("o", "ó"), ("u", "ú")]:
        assert spec.graphemes[accented] == spec.graphemes[plain]


def test_acute_accent_marks_stress_not_quality():
    """The accent marks prominence only, so an accented vowel keeps its plain
    counterpart's readings and attracts the stress mark."""
    assert get("tet").stress.marked_vowels == ("á", "é", "í", "ó", "ú")
    assert _t().transcribe("Timór") == "tiˈmoːɾ"
    assert _t().transcribe("ne'ebé") == "neeˈbeː"


def test_antepenultimate_stress_in_portuguese_loans():
    """Antepenultimate stress reaches Tetun only through Portuguese loans, and
    the orthography always writes it with an accent."""
    assert _t().transcribe("múzika") == "ˈmuzika"
    assert _t().transcribe("úmidu") == "ˈumidu"


def test_penultimate_stress_is_the_default():
    """Most words are penultimate and carry no accent."""
    assert _t().transcribe("hakerek") == "haˈkerek"
    assert _t().transcribe("labarik") == "laˈbarik"


# ── vowel length ────────────────────────────────────────────────────────────

def test_stressed_final_syllable_is_long():
    """Vowels lengthen in stressed monosyllables and stressed final syllables."""
    assert _t().transcribe("hát") == "ˈhaːt"
    assert _t().transcribe("fó") == "ˈfoː"
    assert _t().transcribe("kabás") == "kaˈbaːs"
    assert _t().transcribe("haré") == "haˈreː"


def test_non_final_stressed_vowels_stay_short():
    """Length is conditioned on the final syllable, not on stress alone."""
    assert "ː" not in _t().transcribe("hakerek")
    assert "ː" not in _t().transcribe("múzika")


def test_diphthong_offglide_is_not_lengthened():
    """The process targets the nucleus; the second element of a diphthong is an
    offglide and stays short."""
    assert _t().transcribe("hau") == "ˈhau"
    assert _t().transcribe("koi") == "ˈkoi"


# ── diphthongs ──────────────────────────────────────────────────────────────

def test_rising_sequences_are_one_nucleus():
    """The rising sequences count as a single nucleus, so a word ending in one
    is stressed on it rather than on the following vowel."""
    assert get("tet").stress.diphthongs == ("ei", "ai", "oi", "ui", "au", "eu", "ou")
    assert _t().transcribe("kadeira") == "kaˈdeira"
    assert _t().transcribe("senoura") == "seˈnoura"


def test_nasal_vowels_are_not_borrowed():
    """Portuguese nasal vowels are unpacked into a vowel plus a nasal, so no
    nasal vowel is declared and ⟨-aun⟩ reads as a sequence."""
    assert not [p for p in get("tet").phonemes if "̃" in p]
    assert _t().transcribe("komparasaun").endswith("saun")


# ── rhotics ─────────────────────────────────────────────────────────────────

def test_trill_initially_tap_finally():
    """The orthography does not distinguish the two rhotics; the trill is
    preferred syllable-initially and the tap is usual word-finally."""
    pos = get("tet").positional_graphemes["r"]
    assert pos[GraphemePosition.WORD_INITIAL] == ["r"]
    assert pos[GraphemePosition.WORD_FINAL] == ["ɾ", "r"]
    assert _t().transcribe("fiar").endswith("ɾ")


# ── the three ⟨nh⟩ words that are not /ɲ/ ───────────────────────────────────

def test_bain_compounds_are_not_palatal():
    """Three bimorphemic lexemes built on bain 'day' have ⟨nh⟩ as /n/+/h/."""
    assert _t().transcribe("bainhira") == "bainˈhira"
    assert _t().transcribe("bainhitu") == "bainˈhitu"
    assert _t().transcribe("kompanhia") == "kompaˈɲia"


# ── Tetun Terik ─────────────────────────────────────────────────────────────

def test_terik_inventory_excludes_the_portuguese_stratum():
    """Terik has twelve consonants and five vowels; every phoneme Portuguese
    contributed to Dili is absent, and the back mid vowel is low-mid /ɔ/."""
    phonemes = set(get("tet-x-terik").phonemes)
    assert not phonemes & {"p", "ɡ", "f", "v", "z", "ʃ", "ʒ", "ɲ", "ʎ", "r"}
    assert "ɔ" in phonemes and "o" not in phonemes
    assert "ʔ" in phonemes


def test_terik_reads_o_low_mid_and_r_as_a_tap():
    """The two inventory facts that reach the grapheme table."""
    assert _terik().transcribe("loron") == "ˈlɔɾɔn"
    assert _terik().transcribe("foho") == "ˈfɔhɔ"


def test_terik_inherits_the_dili_grapheme_table():
    """Terik is unwritten as such: text in it uses Official Tetun's spelling, so
    the table is inherited and only the divergences are restated."""
    child, parent = get("tet-x-terik"), get("tet")
    assert child.graphemes["nh"] == parent.graphemes["nh"]
    assert child.graphemes["r"] != parent.graphemes["r"]


def test_terik_inherits_vowel_length_deliberately():
    """Lengthening is not among the contact-induced features Avram lists, so it
    is read as a property of Tetun and inherited — flagged in the spec's notes
    as needing a native check, since no source states it of Terik directly."""
    assert _terik().transcribe("hát") == "ˈhaːt"


def test_terik_diphthongs_carry_the_terik_vowel_values():
    """⟨o⟩ is /ɔ/ here, and the diphthong list divides the transcription as well
    as the spelling — without the ɔ-forms koi is cut kɔ|i and the mark lands on
    the offglide."""
    assert {"ɔi", "ɔu"} <= set(get("tet-x-terik").stress.diphthongs)
    assert _terik().transcribe("koi") == "ˈkɔi"
    assert _terik().transcribe("foun") == "ˈfɔun"
    assert _terik().transcribe("senoura") == "seˈnɔuɾa"


def test_terik_does_not_inherit_contact_driven_vowel_readings():
    """The open/raised variants tet declares for ⟨e⟩ and ⟨o⟩ are Portuguese
    contact effects, so Terik restates the plain readings."""
    assert get("tet-x-terik").graphemes["e"] == ["e"]
    assert get("tet-x-terik").graphemes["o"] == ["ɔ"]


def test_terik_keeps_k_initial_clusters():
    """Native /kC/ onsets survive in Terik where Dili drops or breaks them."""
    assert _terik().transcribe("ktodan") == "ˈktɔdan"
    assert _terik().transcribe("kmanek") == "ˈkmanek"
