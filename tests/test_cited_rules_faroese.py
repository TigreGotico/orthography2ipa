"""Cited-rule conformance for Faroese (fo).

Each test states one claim from the ``fo`` spec's ``notes`` prose with its
citation and pins a FULL transcription, so a rule cannot be satisfied by a
segment that happens to land in the right place inside an otherwise wrong
word. Minimal pairs pin the complementary environment wherever the phonology
gives one.

Faroese orthography is Hammershaimb's etymological norm, so almost every claim
here is about a place where the letters do not say what the sounds do.
"""
import pytest

from orthography2ipa.g2p import G2P


def _t(word):
    """Transcribe *word* without the leading word-stress mark.

    Every assertion in this file is segmental; Faroese stress is categorically
    word-initial and is pinned once, by ``test_fo_initial_stress``.
    """
    return G2P("fo").transcribe_word(word).lstrip("ˈ")


# ---------------------------------------------------------------------------
# Quantity: the stressed vowel's long and short values differ in QUALITY
# (Þráinsson, Petersen, Jacobsen & Hansen 2004; Árnason 2011)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("word,expected", [
    # ⟨a⟩: [ɛaː] open, [a] before a cluster
    ("taka", "tʰɛaːka"),
    ("hestur", "hɛstʊɹ"),
    # ⟨á⟩: [ɔaː] / [ɔ]
    ("bátur", "pɔaːtʊɹ"),
    # ⟨e⟩: [eː] / [ɛ]
    ("hesa", "heːsa"),
    # ⟨i⟩: [iː] / [ɪ]
    ("vika", "viːka"),
    # ⟨o⟩ / ⟨ó⟩: [oː] / [ɔuː], short [œ]
    ("sól", "sɔuːl"),
    ("fótur", "fɔuːtʊɹ"),
    # ⟨u⟩ / ⟨ú⟩: [uː] / [ʉuː], short [ʊ] / [ʏ]
    ("hús", "hʉuːs"),
    ("hussi", "hʊssɪ"),
    # ⟨ø⟩: [øː] / [œ]
    ("gøta", "køːta"),
])
def test_fo_stressed_vowel_quantity(word, expected):
    """QUANTITY: the long value belongs to the open stressed syllable, the
    short value to the syllable closed by a geminate or a cluster, and the two
    differ in quality, not only in length (Þráinsson et al. 2004; Árnason 2011).
    """
    assert _t(word) == expected


def test_fo_quantity_minimal_pair():
    """The same vowel letter, long in an open syllable and short before a
    geminate: ⟨gøta⟩ [øː] against ⟨gøtt⟩ [œ] (Árnason 2011)."""
    assert _t("gøta") == "køːta"
    assert _t("gøtt") == "kœʰtt"


# ---------------------------------------------------------------------------
# Stops: aspiration, not voicing (Árnason 2011)
# ---------------------------------------------------------------------------

def test_fo_no_voiced_stops():
    """STOPS: ⟨b d g⟩ are the unaspirated stops [p t k]; Faroese has no voice
    contrast in its stop series (Árnason 2011)."""
    assert _t("bátur") == "pɔaːtʊɹ"
    assert _t("dagur") == "tɛaːjʊɹ"
    assert _t("gøta") == "køːta"


def test_fo_aspiration_is_word_initial_only():
    """STOPS: ⟨p t k⟩ are aspirated in the word-initial onset and plain
    elsewhere — the medial ⟨p⟩ of ⟨pipar⟩ is [p] while its initial ⟨p⟩ is [pʰ]
    (Árnason 2011)."""
    assert _t("pipar") == "pʰiːpaɹ"


def test_fo_no_aspiration_after_s():
    """STOPS: a stop after ⟨s⟩ is never aspirated (Árnason 2011)."""
    assert _t("stampur") == "stampʊɹ"


def test_fo_preaspiration():
    """STOPS: the geminate spellings ⟨pp tt kk⟩ are preaspirated
    (Árnason 2011)."""
    assert _t("bakki") == "paʰkkɪ"
    assert _t("gøtt") == "kœʰtt"


# ---------------------------------------------------------------------------
# Palatalisation (Þráinsson, Petersen, Jacobsen & Hansen 2004)
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("word,expected", [
    ("kenna", "tʃʰɛnna"),
    ("kjøt", "tʃʰøːt"),
    ("gil", "tʃiːl"),
    ("gestur", "tʃɛstʊɹ"),
    ("gjógv", "tʃɛkv"),
    ("skip", "ʃiːp"),
    ("sjón", "ʃɔuːn"),
    ("hjá", "jɔaː"),
    # ⟨ey⟩ is a front vowel letter followed by a front glide, not one of the
    # blocking ⟨ei/oy⟩ diphthong spellings, so it still palatalises the velar.
    ("geykur", "tʃɛiːkʊɹ"),
    ("skeyt", "ʃɛiːt"),
])
def test_fo_velar_palatalisation(word, expected):
    """PALATALISATION: ⟨k g sk⟩ are [tʃʰ tʃ ʃ] before a front vowel letter and
    in the ⟨kj gj skj sj⟩ digraphs; ⟨hj⟩ is [j]
    (Þráinsson et al. 2004)."""
    assert _t(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("geit", "kaiːt"),
    ("skein", "skaiːn"),
    # ⟨í ý⟩ pattern as the back-onset diphthong [ʊi], not a front vowel, so
    # the velar survives here too even though the plain letters ⟨i y⟩ palatalise.
    ("kíkur", "kʰʊiːkʊɹ"),
    ("skína", "skʊiːna"),
])
def test_fo_diphthong_blocks_palatalisation(word, expected):
    """PALATALISATION: the inherited diphthong ⟨ei⟩ and the ⟨í ý⟩ letters do
    not trigger it — the velar survives in ⟨geit⟩, ⟨skein⟩, ⟨kíkur⟩ and
    ⟨skína⟩ where ⟨gestur⟩ and ⟨skip⟩ palatalise (Þráinsson et al. 2004)."""
    assert _t(word) == expected


# ---------------------------------------------------------------------------
# Skerping (Verschärfung) (Árnason 2011)
# ---------------------------------------------------------------------------

def test_fo_skerping():
    """SKERPING: ⟨ógv úgv⟩ are [ɛkv] and [ɪkv] — the vowel changes quality and
    a stop appears, which no letter-by-letter reading gives (Árnason 2011)."""
    assert _t("gjógv") == "tʃɛkv"
    assert _t("búgv") == "pɪkv"
    assert _t("rógva") == "ɹɛkva"


# ---------------------------------------------------------------------------
# Rhotic and ⟨ð⟩ (Lockwood 1955; Þráinsson et al. 2004)
# ---------------------------------------------------------------------------

def test_fo_rhotic_is_an_approximant():
    """RHOTIC: /r/ is the alveolar approximant [ɹ], not a trill
    (Þráinsson et al. 2004)."""
    assert _t("ár") == "ɔaːɹ"
    assert _t("bátur") == "pɔaːtʊɹ"


def test_fo_eth_is_silent_or_a_glide():
    """⟨ð⟩: silent in the coda, a glide between vowels (Lockwood 1955)."""
    assert _t("norður") == "nɔɹʊɹ"
    assert _t("maður") == "mɛaːjʊɹ"
    assert _t("ríða") == "ɹʊiːja"


# ---------------------------------------------------------------------------
# Stress
# ---------------------------------------------------------------------------

def test_fo_initial_stress():
    """STRESS: categorically word-initial; the acute-accented letters mark
    vowel quality, not stress (Þráinsson et al. 2004)."""
    assert G2P("fo").transcribe_word("bátur").startswith("ˈp")
    assert G2P("fo").transcribe_word("bróðurdóttir").startswith("ˈp")


# ---------------------------------------------------------------------------
# Guards: classes this wave does not touch must not move
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("code,word,expected", [
    ("is", "bátur", "ˈpautʰʏr"),
    ("nn", "taka", "²tɑːkɑ"),
])
def test_neighbouring_specs_unmoved(code, word, expected):
    """The fo wave is spec-only; the Scandinavian specs that share the engine
    paths it exercises (positional graphemes, allophone shortening) keep their
    answers."""
    assert G2P(code).transcribe_word(word) == expected
