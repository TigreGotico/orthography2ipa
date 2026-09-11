"""Cited claims for Old Tupi (Tupinambá) in the normalised orthography.

The spelling modelled here is the one modern editions use (Navarro 2013,
refining Lemos Barbosa 1956): ⟨y⟩ is the high central vowel, ⟨î û ŷ⟩ are
semivowels, ⟨'⟩ is the glottal stop, the tilde marks a nasal vowel and the
acute marks stress. The colonial Jesuit spelling of Anchieta is a different
orthography and is deliberately not modelled.
"""
import orthography2ipa as o2i


def segments(word):
    """Transcription without the stress mark.

    ⟨ng⟩ and the prenasalised stops are licit onsets in Old Tupi, but the
    shared syllabifier treats a velar nasal as coda-only (a calibration
    taken from Germanic), so the mark lands one segment early in every word
    whose final onset is ⟨ng⟩ or a prenasalised stop — 35 of the 375 gold
    headwords, not just ⟨atatinga⟩. The claims below are about segments,
    not about that.
    """
    return o2i.G2P("tpw").transcribe_word(word).replace("\u02c8", "")


def test_the_six_vowels_use_the_open_mid_qualities():
    """The inventory is /a ɛ i ɔ u ɨ/ with matching nasals; ⟨y⟩ is /ɨ/, a
    seventeenth-century convention Navarro's orthography keeps."""
    g = o2i.get("tpw").graphemes
    assert g["y"] == ["ɨ"]
    assert g["e"][0] == "ɛ" and g["o"][0] == "ɔ"
    assert g["ã"] == ["ã"] and g["ỹ"] == ["ɨ̃"]


def test_the_acute_accent_is_stress_only():
    """⟨á é í ó ú⟩ mark the stressed syllable and carry no segmental value,
    so they read exactly as their unaccented counterparts."""
    g = o2i.get("tpw").graphemes
    for plain, marked in (("a", "á"), ("e", "é"), ("i", "í"),
                          ("o", "ó"), ("u", "ú"), ("y", "ý")):
        assert g[marked] == g[plain]
    assert o2i.get("tpw").stress.default_position == -1


def test_b_is_a_bilabial_fricative_and_x_is_postalveolar():
    """⟨b⟩ writes /β/, not a plosive, and ⟨x⟩ writes /ʃ/."""
    assert segments("aba") == "aβa"
    assert segments("xe") == "ʃɛ"


def test_the_glottal_stop_letter_is_transcribed():
    """⟨'⟩ is a full consonant, Navarro's innovation over earlier spellings."""
    assert segments("ka'a") == "kaʔa"


def test_the_semivowel_letters_are_glides():
    """⟨î û ŷ⟩ are the non-syllabic counterparts of /i u ɨ/."""
    assert segments("aîuru") == "ajuɾu"
    assert segments("apŷaba") == "apɨ̯aβa"


def test_the_digraphs_tokenize_as_single_segments():
    """⟨ng nh gû⟩ are /ŋ ɲ ɡw/, and the maximal-munch tokenizer must prefer
    them over the letters they contain."""
    assert segments("atatinga").endswith("ŋa")
    assert segments("nhũ") == "ɲũ"
    assert segments("gûyra").startswith("ɡw")


def test_mb_and_nd_are_prenasalized_and_nasalize_the_vowel_before_them():
    """/m n/ surface as [ᵐb ⁿd] before an oral vowel, and regressive nasal
    harmony nasalises the vowel to their left."""
    assert segments("pindá") == "pĩⁿda"
    assert segments("kamby") == "kãᵐbɨ"


def test_a_vowel_nasalizes_before_a_plain_nasal_consonant():
    """The same leftward spreading applies before [m n ŋ ɲ]."""
    assert segments("angaturama") == "ãŋatuɾãma"
