"""Modern Israeli Hebrew niqqud (vowel pointing): pointed text must be fully
readable, unpointed text degrades gracefully like undiacritized Arabic.

The spec targets the MODERN (Non-Oriental) pronunciation, not Tiberian:

* Laufer, A. (1999), "Hebrew", *Handbook of the International Phonetic
  Association*, CUP, pp. 96-99 (Illustrations of the IPA; earlier version
  JIPA 20(2), 1990, 40-43) — the 5-vowel system /i e a o u/ (p. 98
  חִיל/חֵיל/חַל/חוֹל/חוּל), the Non-Oriental mergers /ʕ/→/ʔ/ and /ħ/→/χ/,
  resh as uvular [ʁ], no gemination outside Oriental speech, distinctive
  stress (ˈbereχ 'knee' vs beˈreχ 'he blessed');
* Bolozky, S. (1997), "Israeli Hebrew Phonology", in Kaye (ed.),
  *Phonologies of Asia and Africa* 1, 287-311 — begadkefat reduced to the
  three pairs b~v, k~χ, p~f; shva realised as zero or [e]; no length or
  gemination contrast.

Expectations INCLUDE the stress mark: the spec declares the milra (final,
-1) default, so the engine emits ˈ on the last syllable. Words whose real
stress is milel (segolates such as סֵפֶר) are asserted stress-stripped,
because their stress is a documented limitation, not a vowel claim.
"""
import pytest

from orthography2ipa import transcribe, get


def _no_stress(word: str) -> str:
    return transcribe(word, "he").replace("ˈ", "")


# ─── Metadata: the spec says what it models and cites the primaries ───────

def test_cites_laufer_and_bolozky():
    spec = get("he")
    ids = {s.id for s in spec.sources}
    assert "laufer1999" in ids
    assert "bolozky1997" in ids


def test_niqqud_marks_are_optional_marks():
    """Unpointed text is UNDERSPECIFIED input, like undiacritized Arabic
    (ar.json): every niqqud combining mark must be declared optional."""
    marks = set(get("he").optional_marks)
    for mark in "ְֱֲֳִֵֶַָׇֹֻּׁׂ":
        assert mark in marks, f"niqqud mark U+{ord(mark):04X} missing from optional_marks"


# ─── The five vowels (Laufer 1999 p.98: חִיל חֵיל חַל חוֹל חוּל) ─────────

def test_hiriq_male_is_i():
    """חִיל 'fear' — hiriq + yod (hiriq male) reads /i/."""
    assert transcribe("חִיל", "he") == "ˈχil"


def test_tsere_male_is_plain_e():
    """חֵיל 'army of' — Modern Hebrew reads tsere (male) as plain /e/, not
    the Non-Oriental diphthongal [ei̯] variant (Laufer 1999 p.98)."""
    assert transcribe("חֵיל", "he") == "ˈχel"


def test_patach_is_a():
    """חַל 'occurred' — patach = /a/."""
    assert transcribe("חַל", "he") == "ˈχal"


def test_holam_male_is_o():
    """חוֹל 'sand' — vav + holam (holam male) = /o/."""
    assert transcribe("חוֹל", "he") == "ˈχol"


def test_shuruq_is_u():
    """חוּל 'abroad' — vav + dagesh (shuruq) = /u/."""
    assert transcribe("חוּל", "he") == "ˈχul"


def test_qamats_equals_patach_modern():
    """Modern Hebrew merged Tiberian qamats /ɔ/ into /a/: שָׁנָה 'year' is
    /ʃaˈna/ (Bolozky 1997; Modern_Hebrew_phonology)."""
    assert transcribe("שָׁנָה", "he") == "ʃaˈna"


def test_segol_equals_tsere_modern():
    """Tsere and segol are both /e/ in Modern Hebrew: סֵפֶר 'book' = sefer
    (stress-stripped: segolates carry unpredictable milel stress)."""
    assert _no_stress("סֵפֶר") == "sefeʁ"


def test_qubuts_is_u():
    """קִבּוּץ 'kibbutz': qubuts/shuruq = /u/, and the dagesh in בּ gives
    the stop /b/ with NO gemination (Bolozky 1997: no length contrast)."""
    assert transcribe("קִבּוּץ", "he") == "kiˈbuts"


# ─── Shva na vs shva nach (Bolozky 1997) ───────────────────────────────────

def test_shva_nach_is_silent():
    """זְמַן 'time' is /zman/ — the shva under ז is not pronounced
    (Modern_Hebrew_phonology: 'zman' as the silent-shva example)."""
    assert transcribe("זְמַן", "he") == "ˈzman"


def test_shva_grapheme_offers_e_as_alternative():
    """The shva mark must keep /e/ as a ranked candidate: its realisation
    as zero or [e] is morphology/sonority-conditioned (Bolozky 1997) and
    not recoverable from the mark alone."""
    assert get("he").graphemes["ְ"] == ["", "e"]


# ─── Begadkefat: only ב כ פ still alternate (Bolozky 1997) ────────────────

def test_bet_with_dagesh_is_b_without_is_v():
    """דָּבָר 'word' /daˈvaʁ/: dagesh in ד changes nothing (d), and the
    undotted ב is the fricative /v/."""
    assert transcribe("דָּבָר", "he") == "daˈvaʁ"


def test_bet_dagesh_after_vowel_is_still_a_stop():
    """שַׁבָּת 'sabbath' /ʃaˈbat/: dagesh (historically forte) makes בּ a
    stop but does NOT geminate in Modern Hebrew (Laufer 1999: gemination
    survives only for some Oriental speakers)."""
    assert transcribe("שַׁבָּת", "he") == "ʃaˈbat"


def test_kaf_without_dagesh_is_chi():
    """לִכְתֹּב 'to write' /liχˈtov/: undotted כ = /χ/, dotted תּ = plain
    /t/ (the t~θ alternation is lost in Modern Hebrew), final undotted
    ב = /v/."""
    assert _no_stress("לִכְתֹּב") == "liχtov"


def test_pe_with_dagesh_is_p_without_is_f():
    """תַּפּוּחַ 'apple' /taˈpuaχ/ has פּ /p/; final ף is /f/ as in צָף
    'floats' (Laufer 1999 p.97 word list)."""
    assert transcribe("תַּפּוּחַ", "he") == "taˈpuaχ"
    assert transcribe("צָף", "he") == "ˈtsaf"


# ─── Shin/sin dots ─────────────────────────────────────────────────────────

def test_shin_dot_vs_sin_dot():
    """שָׁר 'sings' /ʃar/ vs שַׂר 'minister' /sar/ (Laufer 1999 p.97
    minimal-ish pair for /ʃ/ and /s/)."""
    assert transcribe("שָׁר", "he") == "ˈʃaʁ"
    assert transcribe("שַׂר", "he") == "ˈsaʁ"


def test_israel_has_sin():
    """יִשְׂרָאֵל /jisʁaˈʔel/: word-initial יִ is /ji/, שׂ is /s/."""
    assert transcribe("יִשְׂרָאֵל", "he") == "jisʁaˈʔel"


# ─── Gutturals in the Non-Oriental pronunciation (Laufer 1999) ─────────────

def test_ayin_and_aleph_are_glottal_or_silent():
    """Non-Oriental speakers merge /ʕ/ into /ʔ/ (Laufer 1999): עִבְרִית
    'Hebrew' starts /ʔ/."""
    assert transcribe("עִבְרִית", "he") == "ʔiˈvʁit"


def test_final_he_is_silent_mater():
    """Word-final ה is a silent mater for /a/: תּוֹרָה /toˈʁa/."""
    assert transcribe("תּוֹרָה", "he") == "toˈʁa"


def test_resh_is_uvular():
    """ר = /ʁ/ (Laufer 1999: 'usually a uvular approximant' for
    Non-Orientals): מָחָר 'tomorrow' /maˈχaʁ/ — also shows ח = /χ/."""
    assert transcribe("מָחָר", "he") == "maˈχaʁ"


# ─── Furtive patach (patach gnuva) ─────────────────────────────────────────

def test_furtive_patach_under_final_het():
    """רוּחַ 'wind' /ˈʁuaχ/: a word-final ח bearing patach reads the vowel
    BEFORE the consonant."""
    assert _no_stress("רוּחַ") == "ʁuaχ"


def test_furtive_patach_under_final_ayin():
    """שׁוֹמֵעַ 'hears' /ʃoˈmea/: final עַ reads /a/ with the ayin silent
    for Non-Oriental speakers."""
    assert transcribe("שׁוֹמֵעַ", "he") == "ʃoˈmea"


# ─── Consonantal glides carrying vowels ────────────────────────────────────

def test_yod_with_vowel_is_consonantal():
    """בַּיִת 'house' /ˈbajit/: a yod bearing hiriq is the onset /ji/, not
    the vowel /i/ (stress-stripped: segolate-pattern milel)."""
    assert _no_stress("בַּיִת") == "bajit"


def test_vav_with_vowel_is_consonantal():
    """מִצְוָה 'commandment' /miˈtsva/: a vav bearing qamats is /va/, not
    the mater /o/ or /u/."""
    assert transcribe("מִצְוָה", "he") == "miˈtsva"


# ─── Unicode mark-order robustness ─────────────────────────────────────────

@pytest.mark.parametrize("word,expected", [
    ("שָׁלוֹם", "ʃaˈlom"),
    ("שַׁבָּת", "ʃaˈbat"),
    ("כִּפָּה", "kiˈpa"),
])
def test_canonical_and_typed_mark_orders_agree(word, expected):
    """Real pointed text is inconsistently normalized: typed convention puts
    dagesh/shin-dot before the vowel, Unicode canonical ordering (NFC/NFD)
    puts the vowel first. Both must transcribe identically."""
    import unicodedata
    assert transcribe(word, "he") == expected
    assert transcribe(unicodedata.normalize("NFC", word), "he") == expected
    assert transcribe(unicodedata.normalize("NFD", word), "he") == expected


# ─── Unpointed text: consonants + matres lectionis stay readable ──────────

def test_unpointed_shalom_reads_matres():
    """Unpointed שלום: the medial ו is the mater /o/ (ktiv male), so the
    skeleton still reads /ʃlom/ — vowels missing elsewhere, as in
    undiacritized Arabic."""
    assert transcribe("שלום", "he") == "ˈʃlom"


def test_unpointed_medial_yod_is_i():
    """Unpointed עברית 'Hebrew': the medial-final י carries /i/."""
    assert _no_stress("עברית").endswith("it")


def test_stress_is_distinctive_and_defaults_to_milra():
    """Laufer 1999 p.98: /ˈbereχ/ 'knee' vs /beˈreχ/ 'he blessed'. Stress
    is lexical, so the spec models only the milra default (-1): the
    pointed verb בֵּרֵךְ comes out right; the segolate noun cannot."""
    assert transcribe("בֵּרֵךְ", "he") == "beˈʁeχ"
    rules = get("he").stress
    assert rules.default_position == -1
