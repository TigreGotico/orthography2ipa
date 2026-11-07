"""English ⟨VCe⟩ split digraph, the vowel digraphs, and the ⟨-s⟩ allomorphs.

Each test pins one orthographic regularity of English spelling against the
environment that shows it is a rule and not a word list: a minimal pair, or
the complementary environment where the same letters take the other value.

The ⟨VCe⟩ pattern (Carney 1994 on the ⟨VCe⟩ correspondences; Wells 1982
vol. 1 for the RP lexical-set values) is the productive one, so it is pinned
in all three of its inflected shapes — bare, plural, past — because the
suffix attaches outside the stem and must not reach back into its nucleus.
"""
import pytest

from orthography2ipa.g2p import G2P


def _t(code, word):
    """Transcribe *word* without the leading word-stress mark; every claim
    here is segmental (see tests/test_cited_rules_germanic.py)."""
    return G2P(code).transcribe_word(word).lstrip("ˈ")


# ─── ⟨VCe⟩: the split digraph ───────────────────────────────────────────────

@pytest.mark.parametrize("word,expected,checked,checked_expected", [
    ("name", "neɪm", "nam", "næm"),
    ("these", "θiːz", "thess", "θɛs"),   # RP is ðiːz: ⟨th⟩ ranking, not ⟨VCe⟩
    ("time", "taɪm", "tim", "tɪm"),
    ("hope", "həʊp", "hop", "hɒp"),
    ("use", "juːz", "us", "ʌs"),
])
def test_en_gb_vce_long_vowel_against_its_checked_pair(
        word, expected, checked, checked_expected):
    """The five vowel letters take their free value before ⟨Ce⟩ and their
    checked value in the closed syllable — the pair is what makes it a rule."""
    assert _t("en-GB", word) == expected
    assert _t("en-GB", checked) == checked_expected


def test_en_gb_vce_survives_inflection():
    """⟨hope⟩/⟨hopes⟩/⟨hoped⟩ state one fact about the ⟨o⟩: the inflectional
    suffix sits outside the stem."""
    assert _t("en-GB", "hope") == "həʊp"
    assert _t("en-GB", "hopes") == "həʊps"
    assert _t("en-GB", "hoped") == "həʊpt"


def test_en_gb_vce_admits_th_but_no_other_digraph():
    """⟨th⟩ is the one consonant digraph that genuinely carries ⟨VCe⟩
    (bathe, breathe, scythe). Every other one in that slot marks a CHECKED
    vowel or is not a mute ⟨e⟩ at all: ⟨ck⟩ is the doubling allograph, and
    ⟨sh⟩/⟨ch⟩ take the epenthetic ⟨-es⟩ ending."""
    assert _t("en-GB", "bathe") == "beɪð"
    assert _t("en-GB", "breathe") == "bɹiːð"
    assert _t("en-GB", "scythe") == "saɪð"
    assert _t("en-GB", "wicked") == "wɪkt"
    assert _t("en-GB", "packed") == "pækt"
    assert _t("en-GB", "wishes") == "wɪʃɪz"
    assert _t("en-GB", "wished") == "wɪʃt"


def test_en_gb_ng_keeps_its_nasal_and_is_not_a_vce_consonant():
    """⟨ng⟩ is the affricate only before a mute word-final ⟨e⟩ (plunge,
    hinge); with anything after that ⟨e⟩ the nasal stands (singer, anger).
    It is deliberately outside ⟨VCe⟩: ⟨-nge⟩ is free only after ⟨a⟩ and
    checked everywhere else, so it states no length fact."""
    assert _t("en-GB", "singer") == "sɪŋə"
    assert _t("en-GB", "anger") == "æŋə"
    assert _t("en-GB", "longer") == "lɒŋə"
    assert _t("en-GB", "hanged") == "hæŋd"
    assert _t("en-GB", "plunge") == "plʌndʒ"
    assert _t("en-GB", "hinge") == "hɪndʒ"


def test_en_gb_oi_stays_a_diphthong_except_across_the_ing_boundary():
    """⟨oi⟩ is CHOICE (oil, coin, voice); word-final ⟨-oing⟩ is ⟨-ing⟩ on
    an ⟨o⟩-final stem, so the letters sit in different morphemes."""
    assert _t("en-GB", "oil") == "ɔɪl"
    assert _t("en-GB", "voice") == "vɔɪs"
    assert _t("en-GB", "going") == "ɡəʊɪŋ"
    assert _t("en-GB", "echoing") == "ɛtʃəʊɪŋ"
    assert _t("en-GB", "shoeing") == "ʃəʊɪŋ"


def test_oing_hiatus_lands_on_each_accents_own_goat_vowel():
    """The rule restores the hiatus; the vowel is the spec's own GOAT.

    An allophone rule's surface is a literal, so the RP [əʊ] written into
    the parent cannot follow a child's inventory by itself — en-US
    re-declares the rule on [oʊ], the value its own ⟨o⟩ already carries.
    The other children share RP's [əʊ] (their ⟨hope⟩ is [həʊp]) and
    inherit unchanged."""
    assert _t("en-US", "going") == "ɡoʊɪŋ"
    assert _t("en-US", "hope") == "hoʊp"
    for accent in ("en-AU", "en-CA", "en-IE", "en-ZA", "en-GB-x-scotland"):
        assert _t(accent, "going") == "ɡəʊɪŋ"
        assert _t(accent, "hope") == "həʊp"


def test_do_family_is_goose_not_goat_and_prefixed_forms_are_not():
    """⟨do⟩ spells GOOSE under an ⟨o⟩, which no rule here predicts.

    ⟨do⟩/⟨does⟩/⟨doing⟩ are whole-word overrides, the same closed
    high-frequency class as ⟨have⟩ and ⟨come⟩. The PREFIXED forms are
    outside what a whole-word list can hold and stay wrong — pinned so
    the limit is visible rather than implied."""
    assert _t("en-GB", "do") == "duː"
    assert _t("en-GB", "doing") == "duːɪŋ"
    assert _t("en-US", "doing") == "duɪŋ"
    assert _t("en-GB", "undoing") == "ʌndəʊɪŋ"   # RP ˌʌnˈduːɪŋ
    assert _t("en-GB", "redoing") == "ɹɛdəʊɪŋ"   # RP ˌriːˈduːɪŋ


def test_es_voicing_does_not_leak_into_krio():
    """Krio inherits en-GB but has no source for an English ⟨-es⟩ voicing
    alternation, so the two voicing rules are switched off by id and Krio
    keeps its own [s]."""
    assert _t("kri", "wishes") == "wiʃes"
    assert _t("kri", "roses") == "ʁoses"
    assert _t("kri", "going") == "ɡoĩ"


def test_en_gb_gu_words_keep_the_base_reading():
    """No ⟨gue⟩ grapheme is declared: one would swallow the ⟨u⟩ that
    ⟨argue⟩ needs as a nucleus."""
    assert _t("en-GB", "argue") == "ɑːɡjuː"


def test_en_gb_oo_is_not_shortened_before_k():
    """No ⟨ook⟩ grapheme is declared. ⟨book⟩/⟨shook⟩ are [ʊ] and ⟨spooky⟩
    is [uː]; the spelling does not tell them apart, so the engine states
    the majority ⟨oo⟩ value and gets ⟨book⟩ wrong rather than encoding a
    word list as a grapheme."""
    assert _t("en-GB", "spooky") == "spuːki"
    assert _t("en-GB", "book") == "buːk"


def test_en_gb_vce_needs_a_single_consonant():
    """Two consonant graphemes between the nucleus and the ⟨e⟩ is no longer
    the split digraph: ⟨table⟩ and ⟨dense⟩ must not take the free value."""
    assert _t("en-GB", "table").startswith("tæ")
    assert _t("en-GB", "dense").startswith("dɛ")


def test_en_gb_vce_does_not_reach_an_unstressed_syllable():
    """The free value is a fact about a STRESSED nucleus; a weak final
    syllable reduces whatever its spelling (⟨climate⟩, ⟨private⟩)."""
    assert _t("en-GB", "climate") == "klɪmət"
    assert _t("en-GB", "private") == "pɹɪvət"


def test_en_us_vce_takes_the_american_goat_vowel():
    """en-US inherits the pattern but not en-GB's RP value for it."""
    assert _t("en-US", "hope") == "hoʊp"
    assert _t("en-US", "note") == "noʊt"


# ─── vowel digraphs ─────────────────────────────────────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("law", "lɔː"),
    ("cause", "kɔːz"),
    ("boy", "bɔɪ"),
    ("boil", "bɔɪl"),
    ("new", "njuː"),
    ("Europe", "juːɹəp"),
])
def test_en_gb_vowel_digraphs(word, expected):
    """⟨aw au oy oi ew eu⟩ are single vowel graphemes, not letter sequences."""
    assert _t("en-GB", word) == expected


def test_en_gb_aw_before_a_vowel_is_two_syllables():
    """⟨aw⟩ spanning a syllable boundary (⟨a-ward⟩, ⟨a-wave⟩) is not the
    THOUGHT digraph — the ⟨w⟩ is the next syllable's onset."""
    assert _t("en-GB", "awave").startswith("əw")


@pytest.mark.parametrize("word,expected", [
    ("khan", "kæn"),
    ("school", "skuːl"),
    ("scheme", "skiːm"),
])
def test_en_gb_consonant_final_digraphs(word, expected):
    """⟨kh⟩ and ⟨sch⟩ each spell one thing."""
    assert _t("en-GB", word) == expected


def test_en_gb_sc_is_a_stop_cluster_except_before_a_front_vowel():
    """⟨sc⟩ follows the same softening as ⟨c⟩ alone: /sk/ by default
    (scale, scope, scar), /s/ before ⟨e⟩ and ⟨i⟩ (scene, science)."""
    assert _t("en-GB", "scale") == "skeɪl"
    assert _t("en-GB", "scar").startswith("sk")
    assert _t("en-GB", "scene") == "siːn"


def test_en_gb_final_h_is_silent():
    """A word-final ⟨h⟩ spells nothing (oh, hurrah); word-initially it is
    the consonant."""
    assert _t("en-GB", "oh") == "ɒ"
    assert _t("en-GB", "hurrah").endswith("ə")
    assert _t("en-GB", "hat").startswith("h")


# ─── ⟨g⟩ before ⟨i⟩ ─────────────────────────────────────────────────────────

def test_en_gb_g_before_i_is_hard_by_default():
    """Soft ⟨g⟩ is nothing like as reliable as soft ⟨c⟩: before ⟨i⟩ the
    Germanic core of the vocabulary keeps the plosive."""
    for word in ("girl", "gift", "girth", "gild"):
        assert _t("en-GB", word).startswith("ɡ")
    assert "ɡ" in _t("en-GB", "begin")


def test_en_gb_soft_g_before_i_is_a_ranking_trade():
    """The other side of ranking hard ⟨ɡ⟩ first before ⟨i⟩.

    This is a TRADE, not a correction: ⟨g⟩ before ⟨i⟩ is genuinely split
    between the Germanic core (give, girl, gift — now right) and the
    Romance stratum (magic, giant, ginger — now wrong), and the ranking
    can only put one of them first. Both readings stay in the lattice for
    a rescorer; only rank 1 moves. Pinned so the cost is visible and a
    future change that claims to fix ⟨g⟩ has to say what it did here."""
    assert _t("en-GB", "magic") == "mæɡɪk"      # RP ˈmædʒɪk
    assert _t("en-GB", "giant") == "ɡiænt"      # RP ˈdʒaɪənt
    assert _t("en-GB", "ginger") == "ɡɪŋə"      # RP ˈdʒɪndʒə


def test_en_gb_double_g_is_a_plosive():
    """⟨gg⟩ is hard even before a front vowel (bigger, dagger)."""
    assert _t("en-GB", "bigger") == "bɪɡə"
    assert _t("en-GB", "dagger") == "dæɡə"


# ─── the ⟨-es⟩ allomorphs ───────────────────────────────────────────────────

def test_en_gb_es_allomorphs():
    """⟨-s⟩ after a mute ⟨e⟩: [ɪz] after a sibilant, [s] after any other
    voiceless consonant, [z] elsewhere (Cruttenden 2014, § 4.3)."""
    assert _t("en-GB", "roses") == "ɹəʊzɪz"
    assert _t("en-GB", "faces") == "feɪsɪz"
    assert _t("en-GB", "hopes") == "həʊps"
    assert _t("en-GB", "scales") == "skeɪlz"


def test_en_gb_es_allomorph_known_wrong_where_the_stem_is_wrong():
    """The ⟨-es⟩ ending is right on ⟨cases⟩ and the STEM is not.

    RP is [ˈkeɪsɪz]; the engine says [ˈkeɪzɪz]. The [ɪz] ending is this
    PR's rule doing its job — the [z] in the stem is the pre-existing
    ⟨s⟩ intervocalic entry, which states [z] categorically. Pinned as
    known-wrong so the day that entry is revisited, this moves with it
    instead of quietly staying broken."""
    assert _t("en-GB", "cases") == "keɪzɪz"


def test_en_gb_softening_reaches_y():
    """⟨y⟩ is the third front-vowel spelling the softening keys on."""
    assert _t("en-GB", "cycle").startswith("s")
    assert _t("en-GB", "cynic").startswith("s")
    assert _t("en-GB", "gym").startswith("dʒ")
    assert _t("en-GB", "cat").startswith("k")


# ─── ⟨i⟩ in hiatus and word-finally ─────────────────────────────────────────

def test_en_gb_i_in_hiatus_is_tense():
    """⟨i⟩ before another vowel is the tense /i/, not the checked /ɪ/
    (audio, medium, Sochi) — the happY/hiatus value."""
    assert _t("en-GB", "audio") == "ɔːdiəʊ"
    assert _t("en-GB", "Sochi").endswith("i")
