"""Hanoi Vietnamese: rime mapping, coda allophony and tone.

Every expectation is Kirby (2011), "Vietnamese (Hanoi Vietnamese)", JIPA
41(3), 381-392 — the IPA Illustration for the variety the spec describes.
Words that appear in the Illustration's own example lists are marked; the
rest are ordinary words whose reading follows the rules stated there.
"""
import unicodedata

import pytest

from orthography2ipa.g2p import G2P
from orthography2ipa.registry import get
from orthography2ipa.vowels import is_orthographic_vowel


@pytest.fixture(scope="module")
def vi():
    return G2P("vi")


TONE_LETTERS = "˥˦˧˨˩ˀ"


def segments(ipa):
    return ipa.rstrip(TONE_LETTERS)


def tone(ipa):
    return ipa[len(segments(ipa)):]


# ── Onsets ────────────────────────────────────────────────────────────
# Kirby's initial inventory: ⟨tr⟩ and ⟨ch⟩ are "completely merged" as the
# affricate /tɕ/, ⟨s x⟩ as /s/, ⟨d gi r⟩ as /z/, ⟨g gh⟩ is the fricative
# /ɣ/ (his ⟨gà⟩ [ɣa]), and ⟨b đ⟩ are the implosives /ɓ ɗ/ (his ⟨ba⟩ [ɓa],
# ⟨da⟩ [ɗa]).
@pytest.mark.parametrize("word,onset", [
    ("ba", "ɓ"), ("đa", "ɗ"), ("ta", "t"), ("tha", "tʰ"),
    ("cha", "tɕ"), ("tra", "tɕ"), ("nha", "ɲ"), ("nga", "ŋ"),
    ("nghe", "ŋ"), ("kha", "x"), ("gà", "ɣ"), ("ghe", "ɣ"),
    ("pha", "f"), ("và", "v"), ("xa", "s"), ("sa", "s"),
    ("da", "z"), ("gia", "z"), ("ra", "z"), ("hà", "h"),
    ("ma", "m"), ("na", "n"), ("la", "l"), ("ca", "k"), ("ka", "k"),
])
def test_onsets(vi, word, onset):
    assert vi.transcribe_word(word).startswith(onset)


def test_tr_and_ch_are_the_same_onset(vi):
    assert vi.transcribe_word("tra") == vi.transcribe_word("cha")


def test_s_and_x_are_the_same_onset(vi):
    assert vi.transcribe_word("sa") == vi.transcribe_word("xa")


def test_d_gi_r_all_give_z(vi):
    assert (vi.transcribe_word("da") == vi.transcribe_word("gia")
            == vi.transcribe_word("ra"))


# ── Velar fronting: ⟨anh ach inh ich ênh êch⟩ ─────────────────────────
# Kirby's own examples: ⟨kinh⟩ [kiŋ̟], ⟨kênh⟩ [keŋ̟], ⟨canh⟩ [kɛŋ̟],
# ⟨xích⟩ [sik̟], ⟨xếch⟩ [sek̟], ⟨sách⟩ [sɛk̟]. The spec writes plain
# /ŋ k/; what is under test is the VOWEL and the velar place.
@pytest.mark.parametrize("word,expected", [
    ("kinh", "kiŋ"), ("kênh", "keŋ"), ("canh", "kɛŋ"),
    ("xích", "sik"), ("xếch", "sek"), ("sách", "sɛk"),
])
def test_velar_fronting_rimes(vi, word, expected):
    assert segments(vi.transcribe_word(word)) == expected


def test_anh_is_not_a_palatal_rime(vi):
    """⟨anh⟩ is [ɛŋ], not the literary-Vietnamese [aɲ]."""
    out = segments(vi.transcribe_word("anh"))
    assert out == "ɛŋ"
    assert "ɲ" not in out


# ── Labial-velar finals ───────────────────────────────────────────────
# Kirby: after /u o ɔ/ the velar stops are doubly articulated. His
# examples, and the minimal pairs he sets against the plain bilabials.
@pytest.mark.parametrize("word,expected", [
    ("ung", "uŋ͡m"), ("ông", "oŋ͡m"), ("ong", "ɔŋ͡m"),
    ("úc", "uk͡p"), ("ốc", "ok͡p"), ("óc", "ɔk͡p"),
])
def test_labial_velar_finals(vi, word, expected):
    assert segments(vi.transcribe_word(word)) == expected


@pytest.mark.parametrize("velar,bilabial", [
    ("xúc", "súp"), ("hồng", "hôm"), ("học", "họp"), ("xong", "xóm"),
])
def test_labial_velar_finals_differ_from_plain_bilabials(vi, velar, bilabial):
    assert segments(vi.transcribe_word(velar)) != \
        segments(vi.transcribe_word(bilabial))


def test_labial_velar_rule_needs_a_rounded_monophthong(vi):
    """Kirby states the rule over /u o ɔ/, so the diphthong /uə/ is
    outside it: ⟨uống⟩ is [uəŋ], not *[uəŋ͡m]."""
    assert segments(vi.transcribe_word("uống")) == "uəŋ"


def test_oo_is_kirbys_named_exception(vi):
    """⟨boong⟩ (< French *pont*) is one of the rare plain-velar finals
    after a rounded vowel that Kirby names, and his transcription of it,
    [ɓɔːŋ], is also where the long vowel is written."""
    assert segments(vi.transcribe_word("boong")) == "ɓɔːŋ"


# ── Long /ɛː ɔː/ before a true velar ──────────────────────────────────
# Kirby (p. 384) gives the length distinction its own minimal pairs:
# "[sɛːŋ] xẻng 'shovel'" against "[sɛŋ̟] xanh 'green'", and "[sɔːŋ] xoong
# 'saucepan'" against "[sɔŋ͡m] xong 'to finish'". ⟨eng ec⟩ and ⟨oong ooc⟩
# are the spellings quốc ngữ leaves for those long vowels, ⟨anh ach⟩ and
# ⟨ong oc⟩ being taken by the fronted and labial-velar rimes.
@pytest.mark.parametrize("word,expected", [
    ("xẻng", "sɛːŋ"), ("rẻng", "zɛːŋ"), ("méc", "mɛːk"),
    ("khẹc", "xɛːk"),
    ("xoong", "sɔːŋ"), ("boong", "ɓɔːŋ"), ("coóc", "kɔːk"),
    ("voọc", "vɔːk"),
])
def test_long_vowel_before_a_true_velar(vi, word, expected):
    assert segments(vi.transcribe_word(word)) == expected


@pytest.mark.parametrize("long_word,short_word", [
    ("xẻng", "xanh"), ("éc", "ách"), ("xoong", "xong"), ("coóc", "cóc"),
])
def test_the_length_pairs_are_two_readings(vi, long_word, short_word):
    """Kirby's pairs must not collapse: without the length mark ⟨xẻng⟩
    and ⟨xanh⟩ come out identical."""
    assert segments(vi.transcribe_word(long_word)) != \
        segments(vi.transcribe_word(short_word))


# ── Diphthongs and their coda-conditioned spellings ───────────────────
@pytest.mark.parametrize("word,expected", [
    ("thìa", "tʰiə"), ("tiêm", "tiəm"), ("tiếp", "tiəp"),
    ("liên", "liən"), ("biết", "ɓiət"), ("tiếng", "tiəŋ"),
    ("nhiều", "ɲiəw"),
    ("thua", "tʰuə"), ("buồm", "ɓuəm"), ("luôn", "luən"),
    ("buốt", "ɓuət"), ("xuống", "suəŋ"), ("thuốc", "tʰuək"),
    ("buổi", "ɓuəj"),
    ("thưa", "tʰɯə"), ("tươm", "tɯəm"), ("lươn", "lɯən"),
    ("ướt", "ɯət"), ("xương", "sɯəŋ"), ("thước", "tʰɯək"),
    ("rượu", "zɯəw"),
])
def test_falling_diphthongs(vi, word, expected):
    assert segments(vi.transcribe_word(word)) == expected


def test_open_and_closed_spellings_are_the_same_diphthong(vi):
    """⟨ia/iê⟩, ⟨ua/uô⟩ and ⟨ưa/ươ⟩ are spelling alternants of one
    vowel each; only the coda decides which is written."""
    for open_word, closed_word in (("mía", "miếng"), ("múa", "muốn"),
                                   ("mưa", "mương")):
        nucleus = segments(vi.transcribe_word(open_word))[1:]
        assert segments(vi.transcribe_word(closed_word)).startswith(
            "m" + nucleus)


# ── Short vowels ⟨ă â⟩, including the ⟨ay au ây âu⟩ spellings ─────────
@pytest.mark.parametrize("word,expected", [
    ("tắm", "tăm"), ("sắp", "săp"), ("lăn", "lăn"), ("bắt", "ɓăt"),
    ("xăng", "săŋ"), ("sắc", "săk"),
    ("tâm", "tɤ̆m"), ("lấp", "lɤ̆p"), ("bất", "ɓɤ̆t"), ("tầng", "tɤ̆ŋ"),
    # Kirby's pairs: ⟨mai⟩ [maj] against ⟨may⟩ [măj], ⟨dao⟩ [zaw]
    # against ⟨rau⟩ [zăw], ⟨mấy⟩ [mɤ̆j], ⟨râu⟩ [zɤ̆w].
    ("mai", "maj"), ("may", "măj"), ("dao", "zaw"), ("rau", "zăw"),
    ("mấy", "mɤ̆j"), ("râu", "zɤ̆w"),
])
def test_short_vowel_rimes(vi, word, expected):
    assert segments(vi.transcribe_word(word)) == expected


def test_ay_and_ai_are_a_length_contrast(vi):
    assert segments(vi.transcribe_word("may")) != \
        segments(vi.transcribe_word("mai"))


# ── The labial on-glide ───────────────────────────────────────────────
@pytest.mark.parametrize("word,expected", [
    ("hoa", "hwa"), ("oan", "wan"), ("khuya", "xwiə"),
    ("thuế", "tʰwe"), ("quốc", "kwok͡p"), ("quyển", "kwiən"),
    ("ngoài", "ŋwaj"), ("khoẻ", "xwɛ"),
])
def test_medial_glide(vi, word, expected):
    assert segments(vi.transcribe_word(word)) == expected


def test_both_tone_mark_placements_of_an_open_medial_rime(vi):
    """⟨hòa⟩ and ⟨hoà⟩ are the pre- and post-reform spellings of one
    word; both are current in running text and must read alike."""
    for old, new in (("hòa", "hoà"), ("khỏe", "khoẻ"), ("thúy", "thuý")):
        assert vi.transcribe_word(old) == vi.transcribe_word(new)


def test_gi_before_a_toned_i_is_written_with_one_i(vi):
    """⟨gì⟩ is /zi/: the digraph's ⟨i⟩ and the rime's ⟨i⟩ are one letter."""
    assert vi.transcribe_word("gì") == "zi˧˨"


def test_gi_survives_a_rime_that_opens_with_a_diacritic_vowel(vi):
    """⟨giường giờ giữ⟩ keep the /z/ onset. The digraph back-off in the
    tokenizer asks whether the next character is a written vowel, and
    ⟨ư ơ ữ⟩ answer yes only once a precomposed Latin vowel is recognised
    as one."""
    assert vi.transcribe_word("giường") == "zɯəŋ˧˨"
    assert vi.transcribe_word("giờ") == "zɤ˧˨"
    assert vi.transcribe_word("giữ") == "zɯ˧ˀ˥"


@pytest.mark.parametrize("word,expected", [
    # ⟨gi⟩ + an ⟨i⟩-initial rime, written with one ⟨i⟩. Wiktionary gives
    # [ziəŋ] / [ziət] / [ziəw] for Hà Nội.
    ("giếng", "ziəŋ˨˦"), ("giêng", "ziəŋ˧˧"), ("giết", "ziət˦˥"),
    ("giễu", "ziəw˧ˀ˥"),
    # The collapse must not let a coda split off the digraph.
    ("gìn", "zin˧˨"), ("gin", "zin˧˧"),
    # ...and must not swallow the productive ⟨gi⟩ + ⟨u⟩-rime spellings,
    # nor ⟨gia⟩, which is ⟨gi⟩ + ⟨a⟩.
    ("giúp", "zup˦˥"), ("giũ", "zu˧ˀ˥"), ("gia", "za˧˧"),
])
def test_gi_merged_rimes(vi, word, expected):
    assert vi.transcribe_word(word) == expected


def test_giu_gin_phrase(vi):
    """⟨giữ gìn⟩: two syllables, neither of them shattered."""
    assert vi.transcribe("giữ gìn") == "zɯ˧ˀ˥ zin˧˨"


@pytest.mark.parametrize("word,expected", [
    # ⟨oach⟩ takes velar fronting like every other ⟨a⟩ + palatal-letter
    # rime, and ⟨oam oap⟩ do not (the rule is stated over /ŋ k/).
    ("hoạch", "hwɛk˨ˀ˩"), ("ngoàm", "ŋwam˧˨"), ("ngoáp", "ŋwap˦˥"),
    ("oáp", "wap˦˥"),
])
def test_medial_oa_rimes_with_stop_and_nasal_codas(vi, word, expected):
    assert vi.transcribe_word(word) == expected


def test_ke_hoach_phrase(vi):
    assert vi.transcribe("kế hoạch") == "ke˨˦ hwɛk˨ˀ˩"


@pytest.mark.parametrize("word,expected", [
    # ⟨qu⟩ takes the medial, so what is left of ⟨uynh uyt⟩ is ⟨ynh ýt⟩.
    ("quỳnh", "kwiŋ˧˨"), ("huỳnh", "hwiŋ˧˨"),
    ("quýt", "kwit˦˥"), ("quỵt", "kwit˨ˀ˩"),
    ("huýt", "hwit˦˥"), ("tuýp", "twip˦˥"),
])
def test_y_rimes_after_qu(vi, word, expected):
    assert vi.transcribe_word(word) == expected


def test_a_qu_checked_rime_takes_a_checked_tone(vi):
    """⟨quýt⟩ closes with an oral stop, so its sắc is D1 (˦˥) and the
    tone letters still land after the coda, not inside the syllable."""
    out = vi.transcribe_word("quýt")
    assert segments(out) == "kwit"
    assert tone(out) == "˦˥"


def test_quoc_and_cuoc_are_spelled_apart(vi):
    """⟨quốc⟩ is ⟨qu⟩ + ⟨ôc⟩ and takes the labial-velar final; ⟨cuốc⟩ is
    ⟨c⟩ + ⟨uôc⟩, whose nucleus is the diphthong the rule excludes. The
    ipa-dict gold makes the same split."""
    assert vi.transcribe_word("quốc") == "kwok͡p˦˥"
    assert vi.transcribe_word("cuốc") == "kuək˦˥"


# ── Tone ──────────────────────────────────────────────────────────────
@pytest.mark.parametrize("word,expected_tone", [
    ("ma", "˧˧"),      # ngang  A1
    ("mà", "˧˨"),      # huyền  A2
    ("má", "˨˦"),      # sắc    B1
    ("mả", "˧˩˨"),     # hỏi    C1
    ("mã", "˧ˀ˥"),     # ngã    C2
    ("mạ", "˨ˀ˩"),     # nặng   B2
])
def test_six_tones_on_an_open_syllable(vi, word, expected_tone):
    out = vi.transcribe_word(word)
    assert segments(out) == "ma"
    assert tone(out) == expected_tone


def test_the_six_tones_are_six_distinct_readings(vi):
    forms = {vi.transcribe_word(w)
             for w in ("ma", "mà", "má", "mả", "mã", "mạ")}
    assert len(forms) == 6


def test_tone_is_written_after_the_coda(vi):
    """The tone belongs to the syllable, not to the nucleus, so the
    letters come last."""
    out = vi.transcribe_word("bánh")
    assert out == "ɓɛŋ˨˦"


@pytest.mark.parametrize("word,expected", [
    ("mát", "mat˦˥"),   # D1, the checked counterpart of sắc (Kirby's
                        # own [mat] 'cool'; ⟨mắt⟩ is the short-vowel rime)
    ("mạt", "mat˨ˀ˩"),  # D2, the checked counterpart of nặng
])
def test_checked_syllables_take_the_two_tone_paradigm(vi, word, expected):
    assert vi.transcribe_word(word) == expected


def test_checked_sac_is_not_the_open_sac(vi):
    """Kirby separates B1 from D1 on both pitch onset and trajectory."""
    assert tone(vi.transcribe_word("má")) != tone(vi.transcribe_word("mát"))


def test_a_stop_coda_licenses_no_other_tone(vi):
    """Only D1 and D2 occur on a syllable closed by an oral stop, so the
    spec declares no reading for the four impossible spellings."""
    spec = get("vi")
    for spelling in ("màt", "mảt", "mãt", "mat"):
        assert spelling[1:] not in spec.graphemes


def test_every_rime_reading_carries_exactly_one_tone(vi):
    spec = get("vi")
    for key, readings in spec.graphemes.items():
        for reading in readings:
            body = segments(reading)
            if body == reading:          # an onset: no tone, by design
                continue
            assert reading[len(body):].strip(TONE_LETTERS) == ""
            assert "˧" in reading or "˨" in reading or "˦" in reading


# ── Precomposed characters ────────────────────────────────────────────
def test_spec_keys_are_precomposed(vi):
    spec = get("vi")
    for key in spec.graphemes:
        assert key == unicodedata.normalize("NFC", key), key


def test_decomposed_input_reads_the_same(vi):
    """Text that arrives in NFD must transcribe as its NFC twin."""
    for word in ("tiếng", "người", "quốc", "giữ", "mạ"):
        assert vi.transcribe_word(unicodedata.normalize("NFD", word)) == \
            vi.transcribe_word(unicodedata.normalize("NFC", word))


@pytest.mark.parametrize("char", list("ăâêôơư") + list("ắằẳẵặấầẩẫậếềểễệ")
                         + list("ốồổỗộớờởỡợứừửữự"))
def test_precomposed_latin_vowels_are_written_vowels(char):
    """The vowel table cannot enumerate every precomposed form; a Latin
    vowel under a diacritic is still a written vowel."""
    assert is_orthographic_vowel(char)


def test_the_cyrillic_glide_is_still_not_a_vowel():
    """⟨й⟩ decomposes to ⟨и⟩ plus a breve but is excluded on purpose."""
    assert not is_orthographic_vowel("й")


# ── Whole words ───────────────────────────────────────────────────────
@pytest.mark.parametrize("word,expected", [
    ("tôi", "toj˧˧"), ("thích", "tʰik˦˥"), ("táo", "taw˨˦"),
    ("việt", "viət˨ˀ˩"), ("người", "ŋɯəj˧˨"), ("buồn", "ɓuən˧˨"),
    ("học", "hɔk͡p˨ˀ˩"), ("một", "mot˨ˀ˩"), ("nước", "nɯək˦˥"),
    ("ngữ", "ŋɯ˧ˀ˥"), ("đẹp", "ɗɛp˨ˀ˩"), ("tốt", "tot˦˥"),
])
def test_words(vi, word, expected):
    assert vi.transcribe_word(word) == expected
