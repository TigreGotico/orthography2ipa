"""⟨ж ш ц⟩ are unpaired HARD, and ⟨ь⟩ after ⟨ж ш⟩ is separative.

Three consequences the base tables used to get wrong, each asserted here
against forms whose stress is written, so nothing below depends on the
spec's statistical stress guess.

The rules and their citations live in ``ru.json``
(``RU_HARD_BACK_je``/``RU_HARD_BACK_e``, ``RU_HARD_BACK_jo``, and the
``жь``/``шь`` entries of ``positional_graphemes``).
"""
import pytest

from orthography2ipa.g2p import G2P


@pytest.fixture(scope="module")
def ru():
    return G2P("ru")


def bare(g2p, word):
    return g2p.transcribe_word(word).replace("ˈ", "").replace("ˌ", "")


# ── ⟨е⟩ after ж ш ц: [ɛ] under stress, [ɨ] only unstressed ─────────────────

@pytest.mark.parametrize("word,ipa", [
    ("ше́ст", "ʂɛst"),
    ("же́ст", "ʐɛst"),
    ("це́нтр", "tsɛntr"),
    ("шесть", "ʂɛsʲtʲ"),
])
def test_stressed_e_after_hard_sibilant_is_mid_not_high(ru, word, ipa):
    """Раising to [ɨ] is the UNSTRESSED reflex. Under stress the vowel stays
    mid — writing [ɨ] here merges же́ст with жи́ст, a contrast Russian keeps."""
    assert bare(ru, word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("жена́", "ʐɨna"),
    ("цена́", "tsɨna"),
    ("шесто́й", "ʂɨstoj"),
])
def test_unstressed_e_after_hard_sibilant_still_raises(ru, word, ipa):
    """The fix above must not disable the raising where it is real."""
    assert bare(ru, word) == ipa


def test_i_after_hard_sibilant_is_always_back(ru):
    """⟨и⟩ backs regardless of stress — that is a different rule and it stays."""
    assert bare(ru, "жить") == "ʐɨtʲ"
    assert bare(ru, "шить") == "ʂɨtʲ"
    assert bare(ru, "цирк") == "tsɨrk"


# ── ⟨ё⟩ after ж ш ц: back [o], never the centralised [ɵ] ───────────────────

@pytest.mark.parametrize("word,ipa", [
    ("шёл", "ʂoɫ"),
    ("жёлтый", "ʐoɫtɨj"),
    ("шёпот", "ʂopət"),
    ("жёсткий", "ʐostkʲɪj"),
])
def test_o_after_hard_sibilant_is_not_centralised(ru, word, ipa):
    """[ɵ] is the allophone of /o/ next to PALATALISED consonants. ⟨ж ш ц⟩
    are never palatalised, so there is no centralising environment."""
    out = bare(ru, word)
    assert "ɵ" not in out
    assert out == ipa


@pytest.mark.parametrize("word", ["чёрный", "щёки", "лёд", "мёд"])
def test_o_after_a_genuinely_soft_consonant_stays_centralised(ru, word):
    """Negative control: the centralisation itself is not removed."""
    assert "ɵ" in bare(ru, word)


# ── separative ⟨ь⟩ after ж ш carries a stem /j/ ────────────────────────────

@pytest.mark.parametrize("word,ipa", [
    ("ружьё", "rʊʐjɵ"),
    ("мышью", "mɨʂjʊ"),
    ("рожью", "roʐjʊ"),
    ("шью", "ʂju"),
])
def test_separative_soft_sign_after_hard_sibilant_keeps_the_glide(ru, word, ipa):
    """⟨ь⟩ before an iotated vowel is the SEPARATING sign: it cannot
    palatalise an unpaired-hard ⟨ж ш⟩, but the stem /j/ it marks is still
    pronounced. Dropping it merged ружьё with a nonexistent *ружо."""
    assert bare(ru, word) == ipa


@pytest.mark.parametrize("word,ipa", [
    ("мышь", "mɨʂ"),
    ("рожь", "roʂ"),
    ("лишь", "lʲiʂ"),
])
def test_word_final_soft_sign_after_hard_sibilant_is_purely_grammatical(ru, word, ipa):
    """Word-finally the same ⟨ь⟩ is a declension marker with no phonetic
    content at all, and ⟨ж⟩ devoices there like any other obstruent."""
    out = bare(ru, word)
    assert "j" not in out
    assert out == ipa


@pytest.mark.parametrize("word,ipa", [
    ("Дажьбог", "daʐbək"),
])
def test_preconsonantal_soft_sign_after_hard_sibilant_has_no_glide_either(ru, word, ipa):
    """The glide belongs to the SEPARATIVE ⟨ь⟩, which by definition stands
    before a vowel. Before a consonant the sign is as empty as it is
    word-finally, and reading a glide there invents a syllable."""
    assert "j" not in bare(ru, word)
    assert bare(ru, word) == ipa


# ── separative ⟨ь⟩ after a PAIRED consonant carries the same stem /j/ ──────

@pytest.mark.parametrize("word,ipa", [
    ("бельё", "bʲɪlʲjɵ"),
    ("бытьё", "bɨtʲjɵ"),
    ("питьё", "pʲɪtʲjɵ"),
    ("жильё", "ʐɨlʲjɵ"),
])
def test_separative_soft_sign_after_paired_consonant_centralises_too(ru, word, ipa):
    """The centralising environment is the palatal flank, not the identity
    of the consonant. ⟨ьё⟩ after a paired consonant palatalises it and keeps
    the glide, so the vowel has soft articulations on both sides exactly as
    it does in ружьё — see RU_DEIOTA_jo_separative."""
    assert bare(ru, word) == ipa


# ── separative ⟨ь⟩ after ⟨ч⟩ (unpaired SOFT) also carries the stem /j/ ─────

@pytest.mark.parametrize("word,ipa", [
    ("чья", "tɕja"),
    ("чьи", "tɕji"),
    ("ночью", "notɕjʊ"),
    ("чьё", "tɕjɵ"),
])
def test_separative_soft_sign_after_ch_keeps_the_glide(ru, word, ipa):
    """⟨ч⟩ is unpaired SOFT (unlike ⟨ж ш⟩), but a following ⟨ь⟩+vowel is
    still the SEPARATIVE sign, not a plain palatalisation marker: it carries
    a stem /j/ that must survive on the surface, exactly as it does after
    ⟨ж ш⟩ and after paired consonants. Collapsing ``чь`` to a single
    unconditional ``tɕ`` (as the base grapheme table used to) dropped that
    glide everywhere, including before a vowel."""
    assert bare(ru, word) == ipa


def test_word_final_ch_soft_sign_has_no_glide(ru):
    """Word-finally ⟨чь⟩ has no following vowel to separate, so there is no
    glide to carry — this is the ``default`` branch of the ``чь``
    ``positional_graphemes`` entry, not the ``before_vowel`` one."""
    assert "j" not in bare(ru, "дочь")
