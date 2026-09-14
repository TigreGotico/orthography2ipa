"""Ottoman Turkish reads vowel harmony off the consonant letters.

The Perso-Arabic script writes almost no Turkish vowels, and where it does
write one the letter is ambiguous between the two members of a harmony pair:
⟨و⟩ stands for any of /o ø u y/, ⟨ی⟩ for /i/ or /ɯ/, word-final ⟨ه⟩ for /e/ or
/a/. The orthography resolves the ambiguity elsewhere in the word — the hard
letters ⟨ح خ ص ض ط ظ ع غ ق⟩ occur in back-vowel words and the soft letters
⟨ت س ك گ ه⟩ in front-vowel words (Ottoman Turkish alphabet, Wikipedia). Reading
that signal needs a word-scope condition, which no neighbour-scope condition
can express, so these tests are also the coverage for the
``word_contains_grapheme`` rule condition.

The consonant values are the parent Turkish spec's: the tap rhotic, the
[k]~[c] and [ɡ]~[ɟ] palatal pairs, and clear versus velarized [l] (Zimmer &
Orgun, Illustrations of the IPA: Turkish; Göksel & Kerslake 2005).
"""
import pytest

from orthography2ipa.g2p import G2P

OTA = G2P("ota")


@pytest.mark.parametrize("word,expected,why", [
    # A word with no hard letter is a front-vowel word, so its kef is the
    # palatal [c] even though neither conditioning vowel is written.
    ("اكمك", "ecmc", "ekmek 'bread' — soft word, both kefs palatal; the middle vowel is unwritten and stays missing"),
    ("كرس", "cɾs", "kiris — kef palatal, both vowels unwritten"),
    ("ركاب", "ɾcab", "rikab — kef palatal in a word with no hard letter"),
    # A hard letter blocks it: qaf is the back velar letter by definition and
    # a kef standing beside one is in a back-vowel word.
    ("تقدیر", "tkdɯɾ", "takdir — qaf is hard, so ⟨ی⟩ takes its back value"),
])
def test_hard_soft_letters_select_the_velar_and_the_harmony_vowel(
        word, expected, why):
    assert OTA.transcribe(word) == expected, why


@pytest.mark.parametrize("word,expected,why", [
    # Word-final ⟨ه⟩ writes the /e ~ a/ suffix vowel; the hard letter picks /a/.
    ("بالطه", "baɫta", "balta 'axe' — tı is hard, final he is /a/"),
    ("قاصه", "kasa", "kasa — qaf and sad are hard, final he is /a/"),
    # No hard letter anywhere: the same letter is /e/.
    ("تره", "tɾe", "tere 'cress' — soft word, final he is /e/"),
    ("دانه", "dane", "dane 'grain' — soft word, final he is /e/"),
])
def test_final_he_takes_the_harmonizing_suffix_vowel(word, expected, why):
    assert OTA.transcribe(word) == expected, why


@pytest.mark.parametrize("word,expected,why", [
    # ⟨ی⟩ is /i/ by default and /ɯ/ in a hard-letter word.
    ("قیشله", "kɯʃla", "kışla 'barracks' — qaf is hard, so ⟨ی⟩ is /ɯ/ and the qaf itself stays velar"),
    ("فشقی", "fʃkɯ", "fışkı — qaf is hard, final ⟨ی⟩ is /ɯ/"),
    # ⟨و⟩ is /u/ by default and front rounded /y/ in a soft kef/gaf word.
    ("یورك", "jyɾc", "yürek 'heart' — kef is soft, so ⟨و⟩ is front rounded and the kef palatal"),
    ("كوپوك", "cypyc", "köpük 'foam' — soft word: palatal kefs and front-rounded ⟨و⟩ (the /y ~ ø/ height contrast is unrecoverable)"),
])
def test_vav_and_ye_resolve_by_harmony(word, expected, why):
    assert OTA.transcribe(word) == expected, why


@pytest.mark.parametrize("word,expected,why", [
    # A word-initial ⟨ا⟩ before a mater is a bare carrier, not a vowel, and
    # the mater it licenses becomes the nucleus rather than an onset glide.
    ("اوچ", "otʃ", "üç 'three' — carrier dropped, vav is the nucleus"),
    ("اوچر", "otʃɾ", "üçer — same carrier plus mater sequence"),
    ("ایكیشر", "iciʃɾ", "ikişer — carrier dropped, ye is the nucleus"),
])
def test_initial_carrier_before_a_mater_is_silent(word, expected, why):
    assert OTA.transcribe(word) == expected, why


def test_carrier_drop_has_a_nucleus_restore_for_every_mater_it_licenses():
    """A drop rule without a paired restore leaves a bare onset glide.

    ``OTA_CARRIER_DROP_BEFORE_MATER`` licenses both ⟨و⟩ and ⟨ی⟩, so both must
    have a nucleus-restore rule; otherwise the silenced carrier turns the
    mater into a word-initial /v/ or /j/ with no vowel at all.
    """
    from orthography2ipa import get

    rules = {r.id: r for r in get("ota").allophone_rules}
    licensed = set(rules["OTA_CARRIER_DROP_BEFORE_MATER"].followed_by_grapheme)
    restored = {g
                for rid, r in rules.items()
                if "NUCLEUS_AFTER_DROPPED_CARRIER" in rid
                for g in (r.grapheme or ())}
    assert licensed == restored


@pytest.mark.parametrize("word,expected,why", [
    # Turkish /l/ is velarized after a back vowel and clear after a front one.
    ("اشغال", "aʃɡaɫ", "işgal — velarized after /a/"),
    ("بالطه", "baɫta", "balta — velarized after /a/"),
    # Sağır kef: word-final kef after a written back vowel in a hard-letter
    # word is the velar nasal, not the stop.
    ("طوك", "tuŋ", "don — tı is hard, final kef is the nasal"),
])
def test_lateral_velarization_and_sagir_kef(word, expected, why):
    assert OTA.transcribe(word) == expected, why


def test_sagir_kef_needs_a_hard_letter_to_be_recoverable():
    """‹آلاك› /aɫaŋ/ is a back-vowel word spelt with no hard letter.

    Plain kef is ambiguous between the stop and the velar nasal, and the only
    signal the spelling gives is the hard/soft letter class. A word like this
    one carries neither, so the nasal reading is unreachable and the kef comes
    out palatal instead — a known gap, recorded here so that a later rule that
    closes it is recognised as a fix rather than a regression.
    """
    assert OTA.transcribe("آلاك") == "aɫac"


def test_consonant_values_match_the_parent_turkish_spec():
    """ota inherits tr's consonant inventory; the skeleton did not.

    The rhotic is the tap and the velar and lateral letters carry their
    palatal / velarized partners as candidates, exactly as the parent
    declares them.
    """
    from orthography2ipa import get

    ota = get("ota").graphemes
    assert ota["ر"] == ["ɾ"]
    assert ota["ل"] == ["l", "ɫ"]
    assert "c" in ota["ك"] and "ŋ" in ota["ك"]
    assert ota["گ"] == ["ɡ", "ɟ"]
    # ⟨خ⟩ reads as /h/ in the Turkish stratum, keeping /x/ as a secondary.
    assert ota["خ"][0] == "h"


#: Pairs of spellings of the same word that differ only in which codepoint
#: writes a letter Unicode encodes twice: kef as U+0643 or U+06A9, ye as
#: U+06CC, U+064A or U+0649. Ottoman was set in both the Arabic and the
#: Persian tradition, so both spellings must reach the same transcription.
CONFUSABLE_SPELLINGS = [
    ("كوچك", "کوچک", "kucuk — kef twice, Arabic kaf against Persian keheh"),
    ("كوچك", "كوچک", "the mixed spelling a real typesetter also produces"),
    ("ایكیشر", "ایکیشر", "ikiser — the carrier-drop and harmony rules must fire on either kef"),
    ("كیم", "کيم", "kim — kef and ye both swapped at once"),
    ("یل", "يل", "yil — Persian ye against Arabic yeh"),
    ("یل", "ىل", "yil — Persian ye against the dotless alef maksura"),
    ("دكیل", "دكىل", "degil — the ye alternates inside a word, not only at its edge"),
]


@pytest.mark.linguistic
@pytest.mark.parametrize("arabic,persian,why", CONFUSABLE_SPELLINGS)
def test_confusable_codepoints_transcribe_alike(arabic, persian, why):
    assert OTA.transcribe(arabic) == OTA.transcribe(persian), why


@pytest.mark.linguistic
def test_keheh_is_not_deleted():
    """A letter with no grapheme entry is dropped without an error.

    That is what made this a silent defect: ⟨کوچک⟩ came back as a plausible
    short string with all three kefs missing, and nothing said so.
    """
    assert OTA.transcribe("کوچک") != ""
    assert "c" in OTA.transcribe("کوچک")


@pytest.mark.linguistic
def test_hamza_carriers_are_read():
    """Hemze reads /ʔ/ on every carrier, not only on ⟨ئ⟩."""
    for word in ("مؤمن", "أمر", "إمام"):
        assert "ʔ" in OTA.transcribe(word), word


@pytest.mark.linguistic
def test_kashida_and_zwnj_are_declared_empty():
    """Line-shaping marks carry no sound and must not disturb the word.

    They were already dropped, but as unknown characters rather than by
    declaration, which is the same code path that loses a real letter.
    """
    plain = OTA.transcribe("آرمود")
    assert OTA.transcribe("ـآرمودـ") == plain
    assert OTA.transcribe("آر‌مود") == plain


@pytest.mark.linguistic
def test_lookalikes_from_other_traditions_stay_out():
    """Not every confusable is an Ottoman spelling.

    The Urdu he shapes, the Quranic elif wasla and the Sindhi swash kaf
    belong to traditions Ottoman was not set in, so adopting them would
    invent readings rather than recover them.
    """
    from orthography2ipa import get

    graphemes = get("ota").graphemes
    for absent in ("ہ", "ھ", "ٱ", "ڪ"):
        assert absent not in graphemes, absent
