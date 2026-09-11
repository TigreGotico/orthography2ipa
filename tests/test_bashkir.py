"""Bashkir (ba) — full-word transcription pins.

Every word is a real Bashkir form. Its IPA is derived by hand from the
``ba.json`` grapheme table and the alphabet table of the spec's cited
Wikipedia source, never read back from the engine.
"""
import orthography2ipa


def _tw(word):
    return orthography2ipa.G2P("ba").transcribe_word(word)


# --- The three Cyrillic front vowels ----------------------------------------
# ә (U+04D9) /æ/, ө (U+04E9) /ø/ and ү (U+04AF) /y/ are Cyrillic letters with
# descenders/strokes, not the Latin ə ö ü they resemble. A spec keyed on the
# Latin lookalikes matches no Bashkir text at all and drops the vowel.

def test_asa_mother():
    """әсә 'mother'."""
    assert _tw("әсә") == "æˈsæ"


def test_os_three():
    """өс 'three'."""
    assert _tw("өс") == "ˈøs"


def test_ton_night():
    """төн 'night'."""
    assert _tw("төн") == "ˈtøn"


def test_kuth_eye():
    """күҙ 'eye' — ү plus the interdental ҙ /ð/."""
    assert _tw("күҙ") == "ˈkyð"


def test_hyth_word():
    """һүҙ 'word' — һ /h/, ү /y/, ҙ /ð/."""
    assert _tw("һүҙ") == "ˈhyð"


def test_menan_with():
    """менән 'with'."""
    assert _tw("менән") == "meˈnæn"


def test_bulma_room():
    """бүлмә 'room'."""
    assert _tw("бүлмә") == "bylˈmæ"


# --- ⟨е⟩: /je/ word-initially, /e/ elsewhere --------------------------------

def test_yer_earth():
    """ер 'earth, land' — word-initial ⟨е⟩ is iotated."""
    assert _tw("ер") == "ˈjer"


def test_belem_knowledge():
    """белем 'knowledge' — ⟨е⟩ after a consonant is the plain vowel."""
    assert _tw("белем") == "beˈlem"


def test_keshe_person():
    """кеше 'person'."""
    assert _tw("кеше") == "keˈʃe"


# --- ⟨у⟩/⟨ү⟩ as the glide /w/ after a harmonic vowel ------------------------

def test_tau_mountain():
    """тау 'mountain' — back vowel plus ⟨у⟩ is /aw/."""
    assert _tw("тау") == "ˈtaw"


def test_auyr_heavy():
    """ауыр 'heavy'."""
    assert _tw("ауыр") == "aˈwɯr"


def test_kewek_like():
    """кеүек 'like, as' — front vowel plus ⟨ү⟩ is /ew/, and the ⟨е⟩ that
    follows the glide is a plain vowel again."""
    assert _tw("кеүек") == "keˈwek"


def test_dawer_epoch():
    """дәүер 'epoch, era'."""
    assert _tw("дәүер") == "dæˈwer"


def test_qaytaryu_to_return():
    """ҡайтарыу 'to return' — ҡ /q/ and the verbal noun ending -ыу /ɯw/."""
    assert _tw("ҡайтарыу") == "qajtaˈrɯw"


# --- Russian-loan letters ---------------------------------------------------

def test_yolka_fir_tree():
    """ёлка 'fir tree' (Russian loan) — ⟨ё⟩ is /jo/."""
    assert _tw("ёлка") == "jolˈka"


def test_palma_palm():
    """пальма 'palm tree' (Russian loan) — ⟨ь⟩ is silent."""
    assert _tw("пальма") == "palˈma"


def test_global_global():
    """глобаль 'global' (Russian loan) — word-final ⟨ь⟩ is silent."""
    assert _tw("глобаль") == "ɡloˈbal"


# --- ⟨ье⟩/⟨ъе⟩: /je/, not the silent sign plus the plain vowel --------------

def test_pesa_play():
    """пьеса 'play' (Russian loan) — ⟨ье⟩ is /je/, not /e/."""
    assert _tw("пьеса") == "pjeˈsa"


def test_lyot_pours():
    """льет 'pours' (Russian loan) — ⟨ье⟩ is /je/."""
    assert _tw("льет") == "ˈljet"


def test_podyezd_entrance():
    """подъезд 'entrance, doorway' (Russian loan) — ⟨ъе⟩ is /je/."""
    assert _tw("подъезд") == "poˈdjezd"


def test_syezd_congress():
    """съезд 'congress' (Russian loan) — ⟨ъе⟩ is /je/."""
    assert _tw("съезд") == "ˈsjezd"


# --- ⟨е⟩ after a vowel is iotated too, not just word-initially --------------

def test_tiesh_must():
    """тиеш 'must, should' — ⟨ие⟩ is /ije/: ⟨е⟩ is iotated after a vowel."""
    assert _tw("тиеш") == "tiˈjeʃ"
