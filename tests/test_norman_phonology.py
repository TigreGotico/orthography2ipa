"""Norman (Nouormand) phonology: what separates a Norman reading from a
French one.

The spec commits to ONE norm — Jèrriais in its standard dictionary
orthography — because it is the only Norman variety with a settled spelling
and a published spelling-to-sound table. Continental Norman and Dgèrnésiais
have their own standards and would each merit their own spec; their shared
inherited spellings (⟨qu⟩, ⟨ch⟩, ⟨ou⟩, the silent finals) read correctly
here, the rest approximately.

Sources for the claims below:

* the Wikipedia *Jèrriais* spelling-to-IPA tables — consonants (⟨c⟩ before
  e/i/y /s/, ⟨g⟩ before e/i /ʒ/, ⟨dg⟩ /dʒ/, ⟨tch⟩ /tʃ/, ⟨th⟩ /ð/ or /θ/,
  ⟨qu⟩ /k/, ⟨ç⟩ and ⟨ch⟩ /ʃ/, ⟨ngn⟩ /ɲ/, silent final ⟨p g h r⟩), the nine
  short/long oral vowel pairs written with a circumflex, the five nasal
  pairs spelled ⟨in un on en an⟩, and the apostrophe trigraph that writes
  real gemination;
* the Wikipedia *Norman language* article — Latin /k/ kept before /a/ north
  of the Joret line (⟨cat⟩, ⟨cose⟩, ⟨quien⟩ against French chat, chose,
  chien), the aspirate /h/ of Norse superstrate origin, and ⟨ei⟩ where
  French writes ⟨oi⟩ (⟨beire⟩, ⟨creire⟩);
* Le Maistre (1966) for the orthography itself and Liddicoat (1994) for the
  grammar, both cited by author-year in the spec.

Expectations carry no stress marks: the spec declares no lexical stress, so
the engine emits none.
"""
import pytest

from orthography2ipa import transcribe, get


# ─── Which variety, and the metadata that says so ──────────────────────────

def test_commits_to_the_jerriais_norm_and_cites_it():
    spec = get("nrf")
    ids = {s.id for s in spec.sources}
    assert {"lemaistre1966", "liddicoat1994"} <= ids
    assert "JÈRRIAIS" in spec.notes


def test_nrm_is_the_same_language_and_inherits_the_description():
    """⟨nrm⟩ is the code the Norman Wikipedia uses; ISO 639-3 gives the
    language ⟨nrf⟩. Two codes, one description — the ⟨nrm⟩ entry inherits
    rather than keeping a second copy that can drift."""
    assert get("nrm").iso639_3 == "nrf"
    assert transcribe("tchaîthe", "nrm") == transcribe("tchaîthe", "nrf")


# ─── The dental fricative no other Oïl variety has ─────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("tchaîthe", "tʃɛːð"),
    ("péthe", "peð"),
    ("abûther", "abyːðe"),
])
def test_th_is_a_dental_fricative_not_a_stop(word, expected):
    """⟨th⟩ is /ð/ — the hallmark Norman consonant. French ⟨th⟩ is /t/."""
    assert get("nrf").graphemes["th"][0] == "ð"
    assert transcribe(word, "nrf") == expected


# ─── The affricates are spelled, so ⟨ch⟩ never carries one ─────────────────

def test_ch_is_the_fricative_and_tch_the_affricate():
    """Norman writes its affricate ⟨tch⟩ and ⟨dg⟩, which frees ⟨ch⟩ for
    plain /ʃ/. Reading ⟨ch⟩ as /tʃ/ turns ⟨cache⟩ into a word Norman does
    not have."""
    assert get("nrf").graphemes["ch"] == ["ʃ"]
    assert transcribe("cache", "nrf") == "kaʃ"
    assert transcribe("ichi", "nrf") == "iʃi"
    assert transcribe("tchaîse", "nrf") == "tʃɛːz"
    assert transcribe("dgèrre", "nrf") == "dʒɛr"


# ─── Latin /k/ before /a/, kept north of the Joret line ────────────────────

@pytest.mark.parametrize("word,expected", [
    ("cat", "ka"),
    ("cose", "koz"),
    ("quien", "kjẽ"),
    ("vaque", "vak"),
])
def test_velar_kept_where_french_palatalised(word, expected):
    assert transcribe(word, "nrf") == expected


# ─── The Norse aspirate ────────────────────────────────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("habits", "habi"),
    ("hitchet", "hitʃɛ"),
    ("houme", "hum"),
])
def test_word_initial_h_is_pronounced(word, expected):
    """Norman kept an aspirate /h/ that French lost. Word-initially only —
    elsewhere ⟨h⟩ is a spelling artifact of the digraphs."""
    assert transcribe(word, "nrf") == expected
    assert transcribe("tchaîthe", "nrf") == "tʃɛːð"


# ─── ⟨ei⟩ stands where French writes ⟨oi⟩ ──────────────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("veisin", "vezẽ"),
    ("peisson", "pesõ"),
])
def test_ei_is_a_front_vowel_never_wa(word, expected):
    assert get("nrf").graphemes["ei"][0] == "e"
    assert transcribe(word, "nrf") == expected


# ─── Nasal vowels fall out of the coda-nasal rules, not digraph keys ───────

@pytest.mark.parametrize("word,expected", [
    ("grand", "ɡrɑ̃"),
    ("blianc", "bjɑ̃"),
    ("gardîn", "ɡardẽː"),
    ("coumenchier", "kumɑ̃ʃje"),
])
def test_nasal_vowels(word, expected):
    assert not {"an", "en", "in", "on", "un"} & set(get("nrf").graphemes)
    assert transcribe(word, "nrf") == expected


def test_an_onset_nasal_leaves_the_vowel_oral():
    """⟨janne⟩ has an onset /n/, so its vowel does not nasalise. A nasal
    DIGRAPH key could not see the difference; the coda-nasal rule can.

    The WikiPron gold disagrees — its only ⟨janne⟩ row is nasal, /ʒɑ̃n/ —
    and the spec follows the generalisation rather than the gold, which is
    the standing rule that a cited description outranks a transcription.
    """
    assert transcribe("janne", "nrf") == "ʒan"


# ─── Silent finals and the Oïl spelling conventions ────────────────────────

@pytest.mark.parametrize("word,expected", [
    # word-final unstressed ⟨e⟩ is mute
    ("cache", "kaʃ"),
    ("moûque", "muːk"),
    # final ⟨t d s c⟩ are mute
    ("cat", "ka"),
    ("grand", "ɡrɑ̃"),
    ("habits", "habi"),
    # the ⟨r⟩ of an infinitive is mute; in a ⟨Cr⟩ cluster it is not
    ("finir", "fini"),
    ("abattre", "abatr"),
    # ⟨-er⟩ / ⟨-ier⟩ infinitives
    ("abanonner", "abanone"),
    ("mâquier", "maːkje"),
])
def test_silent_finals(word, expected):
    assert transcribe(word, "nrf") == expected


@pytest.mark.parametrize("word,expected", [
    ("janne", "ʒan"),
    ("Jèrri", "ʒɛri"),
    ("counnétablle", "kunetabl"),
    ("faume", "fɔm"),
])
def test_doubled_letters_spell_one_consonant(word, expected):
    """A doubled consonant letter is French etymological spelling. Jèrriais
    writes its REAL geminates with the apostrophe trigraph (⟨pâl'la⟩,
    ⟨c'mench'chons⟩), so ⟨nn⟩ and ⟨rr⟩ are single consonants."""
    assert transcribe(word.lower(), "nrf") == expected


# ─── Vowel graphemes Norman reads differently from French ──────────────────

def test_au_is_open_not_the_french_close_o():
    assert get("nrf").graphemes["au"] == ["ɔ"]
    assert transcribe("faume", "nrf") == "fɔm"


def test_iau_is_the_norman_form_of_french_eau():
    """⟨iau⟩ is the Norman reflex of French ⟨eau⟩ — ⟨iau⟩ 'water',
    ⟨biauté⟩ 'beauty'."""
    assert transcribe("iau", "nrf") == "jo"


def test_ou_is_a_glide_before_a_vowel():
    assert transcribe("ouothelle", "nrf") == "woðəl"


def test_cl_clusters_palatalise():
    """Norman palatalised ⟨pl bl cl fl⟩ before a front glide: the ⟨l⟩ of
    ⟨blianc⟩ is mute and the ⟨i⟩ carries /j/. Only in a cluster — an
    intervocalic ⟨l⟩ before ⟨i⟩ is untouched."""
    assert transcribe("blianc", "nrf") == "bjɑ̃"
    assert transcribe("tolir", "nrf") == "toli"


# ─── Regression guards on the plain cases ──────────────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("carité", "karite"),
    ("abri", "abri"),
    ("litchi", "litʃi"),
    ("à", "a"),
])
def test_no_regression_on_plain_words(word, expected):
    assert transcribe(word, "nrf") == expected
