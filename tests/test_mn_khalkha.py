"""Cited-rule conformance for Khalkha Mongolian (mn) in Cyrillic script.

Every claim below is stated by Svantesson (2003), "Khalkha", in Janhunen
(ed.) *The Mongolic Languages* — the spec's primary source — except the
separating use of ⟨ь⟩/⟨ъ⟩ in Russian loans, which the source does not
treat and which is read off the gold, as its own block says. Each test
isolates one claim on a real word and pins the complementary environment
with a minimal pair wherever the phonology allows.

The wikipron ``mon_cyrl_broad`` gold is a narrow phonetic transcription and
disagrees with several of these rules on transcription depth (see the spec's
notes); the tests state the phonology, never the gold's notation.
"""
import pytest

from orthography2ipa.g2p import G2P


def _t(word):
    return G2P("mn").transcribe_word(word)


# --- laryngeal series: no voiced obstruents -------------------------------
# "the weak stops and affricates are basically plain voiceless unaspirated
# sounds in all positions"; the strong stops are aspirated.

@pytest.mark.parametrize("word,expected", [
    ("бар", "par"),      # 'tiger' — Svantesson's own contrast pair
    ("дал", "taɮ"),      # 'seventy'
    ("тал", "tʰaɮ"),     # 'steppe' — strong ⟨т⟩ against weak ⟨д⟩
])
def test_weak_and_strong_stops(word, expected):
    assert _t(word) == expected


def test_no_voiced_obstruent_letters_in_inventory():
    """Khalkha has no /b d ɡ/-style voicing contrast: ⟨б д ж з⟩ are voiceless."""
    g = G2P("mn").spec.graphemes
    for letter in ("б", "д", "ж", "з"):
        assert all(ipa[0] not in "bdʒz" for ipa in g[letter]), letter


# --- lateral fricative ----------------------------------------------------
# "the laterals l ly are pronounced as lateral fricatives"

def test_lateral_is_a_fricative():
    assert _t("хэл") == "xeɮ"


# --- word-final ⟨н⟩ is /ŋ/ ------------------------------------------------
# "the sequences na no ne ... indicate n ... while the letters n g (without a
# vowel) indicate ng": xan xang [xaŋ] 'king' vs xana xan [xan] 'wall'.

def test_final_n_is_velar():
    assert _t("хан") == "xaŋ"


def test_medial_n_before_vowel_stays_alveolar():
    assert _t("хана") == "xana"


# --- non-initial short vowels are transcribed with full quality -----------
# Svantesson's non-phonemic-schwa rule scopes to NON-initial syllables and
# needs a syllabifier the engine does not run for this spec (see the spec's
# notes); word-final vowel letters are therefore transcribed with their full
# quality like every other position, never spelled as the empty string.

@pytest.mark.parametrize("word,expected", [
    ("хана", "xana"),
    ("Астана", "astʰana"),
])
def test_final_short_vowel_keeps_its_quality(word, expected):
    assert _t(word) == expected


def test_word_initial_short_vowel_survives():
    """A one-letter word keeps its vowel and must never transcribe as the
    empty string."""
    assert _t("а") == "a"
    assert _t("ө") == "ɵ"


@pytest.mark.parametrize("word,expected", [
    ("би", "pi"),   # 'I'
    ("чи", "tɕʰi"), # 'you' (informal)
    ("та", "tʰa"),  # 'you' (polite)
    ("ба", "pa"),   # 'and'
])
def test_monosyllabic_cv_words_keep_their_only_vowel(word, expected):
    """A word-final deletion rule scoped to non-initial syllables must never
    delete a CV monosyllable's only (initial-syllable) vowel — these are
    core pronouns and a conjunction, not edge cases."""
    assert _t(word) == expected


# --- vowels: centralized ⟨ө ү⟩, pharyngealized ⟨о у⟩ ----------------------

@pytest.mark.parametrize("word,expected", [
    ("хүн", "xuŋ"),      # ⟨ү⟩ = [u] (centralized front rounded)
    ("төр", "tʰɵr"),     # ⟨ө⟩ = [ɵ]
    ("ном", "nɔm"),      # ⟨о⟩ = [ɔ] (pharyngealized)
    ("ул", "ʊɮ"),        # ⟨у⟩ = [ʊ]
])
def test_vowel_qualities(word, expected):
    assert _t(word) == expected


def test_cyrillic_oe_and_ue_are_mapped():
    """⟨ө⟩ U+04E9 and ⟨ү⟩ U+04AF are Mongolian Cyrillic letters, not the
    Latin ⟨ö ü⟩ of the transliteration."""
    g = G2P("mn").spec.graphemes
    assert "ө" in g and "ү" in g
    assert "ö" not in g and "ü" not in g


# --- long vowels and diphthongs ------------------------------------------
# Each vowel occurs long, written double; four diphthongs end in i, written
# with ⟨й⟩; ⟨ий⟩ is long /iː/ and ⟨эй⟩ has merged with /eː/.

@pytest.mark.parametrize("word,expected", [
    ("уул", "ʊːɮ"),
    ("үүл", "uːɮ"),
    ("сайн", "saiŋ"),
    ("үйл", "uiɮ"),
])
def test_long_vowels_and_diphthongs(word, expected):
    assert _t(word) == expected


def test_ei_merged_with_long_e():
    assert _t("эйл") == "eːɮ"


# --- iotated letters and the two signs ------------------------------------
# The iotated letters express the glide word-initially and palatalization of
# a preceding consonant after one; ⟨е⟩ stands for iotated ö.

def test_iotated_e_is_glide_plus_centralized_vowel_initially():
    assert _t("ер") == "jɵr"


def test_iotated_letter_palatalizes_a_preceding_consonant():
    assert _t("ням") == "nʲam"


def test_soft_sign_is_palatalization():
    assert _t("хорь") == "xɔrʲ"


@pytest.mark.parametrize("word,expected", [
    ("хорь", "xɔrʲ"),      # before a consonant
    ("арьс", "arʲs"),      # before a consonant
    ("хонь", "xɔnʲ"),      # word-final
    ("хорьа", "xɔrʲa"),    # before a PLAIN vowel letter
    ("мэдьэ", "metʲe"),    # before a plain vowel letter
])
def test_soft_sign_palatalizes_the_preceding_consonant(word, expected):
    assert _t(word) == expected


# ⟨ь⟩ and ⟨ъ⟩ before an iotated vowel letter are the SEPARATING signs of the
# Russian-derived spelling: the syllable break is filled by the glide the
# iotated letter itself writes, and the sign contributes no segment of its
# own. The wikipron mon_cyrl_broad gold writes 30 of its 31 such words with
# a bare /j/ and no palatalization mark on the preceding consonant
# (⟨авъяас⟩ aw̜jaːs, ⟨объект⟩ ɔpjɵkʰtʰ, ⟨томьёо⟩ tʰɔmjɔː, ⟨харьяалах⟩
# xarjaːɮax); only ⟨харьяа⟩ marks it (xarʲjaː), against its own derivative.

@pytest.mark.parametrize("word,expected", [
    ("Вьетнам", "wjɵtʰnam"),
    ("Мьянмар", "mjammar"),
    ("Пёньян", "pʰʲɔnjaŋ"),
    ("Пёнъян", "pʰʲɔnjaŋ"),
    ("авьяас", "awjaːs"),
    ("авъяас", "awjaːs"),
    ("компьютер", "kʰɔmpʰjʊtʰʲɵr"),
    ("обьект", "ɔpjɵkʰtʰ"),
    ("объект", "ɔpjɵkʰtʰ"),
    ("овьёос", "ɔwjɔːs"),
    ("овъёос", "ɔwjɔːs"),
    ("томьёо", "tʰɔmjɔː"),
    ("харьяа", "xarjaː"),
    ("харьяалах", "xarjaːɮax"),
])
def test_separating_sign_before_an_iotated_vowel(word, expected):
    out = _t(word)
    assert out == expected
    assert "ʲʲ" not in out
    assert "jʲ" not in out


# --- an iotated letter plus its long partner is ONE long nucleus ----------
# The long counterpart of an iotated syllable is written with the matching
# plain vowel letter after it — ⟨юу⟩ ⟨юү⟩ ⟨яа⟩ ⟨ёо⟩ ⟨еэ⟩ — exactly as the
# plain long vowels are written double. The second letter states length, not
# a second nucleus, and it also states which side of the pharyngeal harmony
# the nucleus sits on: ⟨юу⟩ is back [jʊː] and ⟨юү⟩ front [juː].

@pytest.mark.parametrize("word,expected", [
    ("юу", "jʊː"),
    ("юү", "juː"),
    ("яам", "jaːm"),
    ("еэвэн", "jeːweŋ"),
])
def test_iotated_long_nucleus(word, expected):
    assert _t(word) == expected


def test_iotated_long_nucleus_is_not_two_short_vowels():
    assert _t("оюутан") == "ɔjʊːtʰaŋ"


# --- nasal place assimilation --------------------------------------------

def test_nasal_assimilates_to_a_following_velar():
    assert _t("монгол") == "mɔŋɡɔɮ"


def test_weak_velar_devoices_before_a_voiceless_consonant():
    assert _t("багш") == "pakɕ"


def test_weak_velar_devoices_before_the_weak_series_too():
    """Svantesson's own example: bügd [pukt] — the weak series ⟨б д з ж⟩ is
    also voiceless ('plain voiceless unaspirated'), so it must trigger the
    same devoicing as the strong series."""
    assert _t("бүгд") == "pukt"
