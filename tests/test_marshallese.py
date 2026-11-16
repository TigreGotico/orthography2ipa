"""Marshallese (mh) — phonemic transcription pins.

Marshallese has four vowel phonemes distinguished by height alone; backness
and rounding come from the flanking consonants' secondary articulation, and
the spelling records the resulting surface quality rather than the phoneme.
Each expected string below is derived by hand from that statement in the
spec's ``notes`` — the vowel letter's row gives the height, its column gives
the articulation standing beside it, and a glide appears wherever that
articulation has no consonant to sit on. None of them is read back from the
engine.
"""
import orthography2ipa


def _tw(word):
    return orthography2ipa.G2P("mh").transcribe_word(word)


# --- Four height-only vowel phonemes ----------------------------------------
# The three columns of a height row spell one phoneme, not three: ⟨i ū u⟩ are
# all /i/ and ⟨ā a ọ⟩ are all /æ/. The surface [ɯ], [u], [ɑ], [ɒ] the letters
# name belong in `allophones`, conditioned by the neighbouring consonants.

def test_lap_big():
    """ḷap 'big' — velarised /lˠ/, so the /æ/ it precedes is written ⟨a⟩."""
    assert _tw("ḷap") == "lˠæpʲ"


def test_kuam_guam():
    """Kuaṃ 'Guam' — ⟨u⟩ is /i/ beside the rounded /kʷ/, not a rounded vowel."""
    assert _tw("Kuaṃ") == "kiɰæmˠ"


# --- Glides where no consonant carries the articulation ----------------------
# No syllable begins or ends with a bare vowel. A word-initial vowel letter
# takes its column's glide in front of it, a word-final one takes it behind,
# and two written vowels are separated by one.

def test_anij_god():
    """Anij 'God' — word-initial ⟨a⟩ is velarised-flanked, so /ɰ/ opens it."""
    assert _tw("Anij") == "ɰænʲitʲ"


def test_elej_ellis():
    """Elej — word-initial ⟨e⟩ is palatalised-flanked, so /j/ opens it."""
    assert _tw("Elej") == "jɛlʲɛtʲ"


def test_awa_hour():
    """awa 'hour' — /ɰ/ opens the word and closes it."""
    assert _tw("awa") == "ɰæwæɰ"


def test_ial_road():
    """iaļ 'road' — a written ⟨ia⟩ hiatus is separated by the PRECEDING
    vowel's column glide, not the following one: ⟨i⟩ is palatalised-flanked,
    so /j/ (not /ɰ/) opens ⟨a⟩. 38 of the WikiPron gold's ⟨ia⟩ words agree
    with this direction (``Iaab``, ``Intia``, ``Kuria`` among them)."""
    assert _tw("iaļ") == "jijælˠ"


def test_naaj_future():
    """naaj 'future'.

    A doubled vowel letter is a vowel-glide-vowel sequence, not a long
    vowel: the spec's Wikipedia source gives this word as /nʲæɰætʲ/.
    """
    assert _tw("naaj") == "nʲæɰætʲ"


# --- Both letterform families of the new orthography -------------------------
# The online dictionary writes ⟨ḷ ṃ ṇ ñ ọ⟩ with dots below; the print standard
# writes the same letters with cedillas and a macron. Text in either spelling
# has to transcribe identically.

def test_al_sun_cedilla():
    """aļ 'sun' with U+013C — the same word as ⟨aḷ⟩."""
    assert _tw("aļ") == _tw("aḷ") == "ɰælˠ"


def test_an_breeze_macron_n():
    """an̄ 'wind' with ⟨n̄⟩ (n + combining macron) — the same word as ⟨añ⟩."""
    assert _tw("an̄") == _tw("añ") == "ɰæŋ"


def test_maan_front_cedilla_m():
    """ṃaan 'front' with ⟨m̧⟩ (m + combining cedilla)."""
    assert _tw("m̧aan") == _tw("ṃaan") == "mˠæɰænʲ"
