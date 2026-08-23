"""Tatar (tt) — full-word transcription pins.

Every word is a real Tatar form. Its IPA is derived by hand from the
``tt.json`` grapheme table, never read back from the engine.
"""
import orthography2ipa


def _tw(word):
    return orthography2ipa.G2P("tt").transcribe_word(word)


# --- The three Cyrillic front vowels ----------------------------------------
# ә (U+04D9) /æ/, ө (U+04E9) /ø/ and ү (U+04AF) /y/ are Cyrillic letters with
# descenders/hooks, not the Latin ə ö ü they resemble. A spec keyed on the
# Latin lookalikes matches no Tatar text at all and drops the vowel.

def test_asa_mother():
    """әсә 'mother'."""
    assert _tw("әсә") == "æˈsæ"


def test_och_three():
    """өч 'three'."""
    assert _tw("өч") == "ˈøtʃ"


def test_ton_night():
    """төн 'night'."""
    assert _tw("төн") == "ˈtøn"


def test_kuz_eye():
    """күз 'eye'."""
    assert _tw("күз") == "ˈkyz"


def test_soz_word():
    """сүз 'word'."""
    assert _tw("сүз") == "ˈsyz"


# --- Җ: Tatar-specific fricative, distinct from Ж -----------------------

def test_can_soul():
    """җан 'soul' — Җ /ʑ/, missing outright before this fix."""
    assert _tw("җан") == "ˈʑan"


def test_yay_summer():
    """җәй 'summer'."""
    assert _tw("җәй") == "ˈʑæj"


# --- Ъ / Ь mark [ʔ]; Ё iotated (Russian loans) ------------------------------
# Gold: 106/106 ъ-words and 439/439 ь-words in the tt benchmark carry ʔ, per
# the Wikipedia "Tatar alphabet" description of both letters as [ʔ]. The
# silent reading is kept as a secondary candidate for the minority of
# orthographic-only tokens; it is not the default output.

def test_yolka_fir_tree():
    """ёлка 'fir tree' (Russian loan) — Ё is /jo/."""
    assert _tw("ёлка") == "jolˈka"


def test_palma_palm():
    """пальма 'palm tree' (Russian loan) — Ь marks [ʔ]."""
    assert _tw("пальма") == "palʔˈma"


def test_globalny_global():
    """глобаль 'global' (Russian loan) — word-final Ь marks [ʔ]."""
    assert _tw("глобаль") == "ɡloˈbalʔ"
