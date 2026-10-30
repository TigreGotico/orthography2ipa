"""Word-initial ⟨hi⟩ strengthening, the Basque digraph ⟨tx⟩, and ⟨ý⟩ coverage.

Each test states one claim from the ``es-ES`` spec notes and proves the engine
honours it on real words.  The citations live in the spec's ``notes``; this
file only points at them.
"""
import pytest

from orthography2ipa.g2p import G2P


def _t(word, code="es"):
    return G2P(code).transcribe_word(word).replace("ˈ", "").replace("ˌ", "")


# ---------------------------------------------------------------------------
# Word-initial ⟨hie-/hia-/hio-⟩ → /ʝ/, and only word-initially.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("word,expected", [
    ("hielo", "ʝelo"),
    ("hierro", "ʝero"),
    ("hierba", "ʝeɾba"),
    ("hiedra", "ʝedɾa"),
    ("hiena", "ʝena"),
    ("hiato", "ʝato"),
    ("hialino", "ʝalino"),
    ("hioides", "ʝoiðes"),
])
def test_initial_hi_strengthens_to_palatal_obstruent(word, expected):
    assert _t(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("antihielo", "antijelo"),
    ("contrahierba", "kontɾajeɾba"),
    ("isohieta", "isojeta"),
])
def test_post_vocalic_hi_stays_a_glide(word, expected):
    """The strengthening is positional: after a vowel the vocoid is [j]."""
    assert _t(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("hijo", "ixo"),
    ("hilo", "ilo"),
    ("historia", "istoɾja"),
    ("hincar", "inkaɾ"),
])
def test_initial_hi_before_a_consonant_is_a_plain_vowel(word, expected):
    """⟨hi⟩ + consonant is silent ⟨h⟩ + the vowel /i/, never /ʝ/."""
    assert _t(word) == expected


def test_ch_digraph_still_wins_over_hi():
    """⟨chi⟩ must segment as ⟨ch⟩ + ⟨i⟩, not ⟨c⟩ + ⟨hi⟩."""
    assert _t("Chiapas") == "tʃjapas"
    assert _t("achicar") == "atʃikaɾ"


# ---------------------------------------------------------------------------
# ⟨tx⟩ = /tʃ/ in Basque-origin lexis and proper names.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("word,expected", [
    ("pintxo", "pintʃo"),
    ("txapela", "tʃapela"),
    ("txakoli", "tʃakoli"),
    ("Arantxa", "aɾantʃa"),
    ("Getxo", "xetʃo"),
])
def test_basque_tx_digraph_is_an_affricate(word, expected):
    assert _t(word) == expected


@pytest.mark.parametrize("word,expected", [
    ("texto", "testo"),
    ("México", "meksiko"),
    ("extra", "estɾa"),
])
def test_tx_entry_does_not_disturb_native_x(word, expected):
    """No native Spanish word contains ⟨tx⟩, so ⟨x⟩ keeps its own values."""
    assert _t(word) == expected


# ---------------------------------------------------------------------------
# ⟨ý⟩ must not be dropped.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("word,expected", [
    ("Aýna", "aina"),
    ("Almatý", "almati"),
    ("Ýñiguez", "iɲiɡeθ"),
])
def test_accented_y_is_transcribed_not_deleted(word, expected):
    assert _t(word) == expected


# ---------------------------------------------------------------------------
# The rehilada varieties do NOT join the merger.
#
# coloma2018 p.244 prints hielo [ˈjelo] in the same word list that prints
# llama [ˈʃama] (primary_sources row coloma2018-028), so in River Plate
# Spanish the ⟨hi⟩ words keep the glide while ⟨ll⟩/⟨y⟩ are rehiladas.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("code,expected", [
    ("es-AR", "jelo"),
    ("es-EC-x-andino", "jelo"),
])
def test_rehilada_varieties_keep_the_glide(code, expected):
    assert _t("hielo", code) == expected


@pytest.mark.parametrize("code,hielo,llama", [
    ("es-AR", "jelo", "ʃama"),
    ("es-EC-x-andino", "jelo", "ʒama"),
])
def test_hi_words_are_not_merged_with_ll_in_rehilada_varieties(
        code, hielo, llama):
    """The minimal pair the citation rests on: they must NOT be the same."""
    assert _t("hielo", code) == hielo
    assert _t("llama", code) == llama
    assert _t("hielo", code) != _t("llama", code)


@pytest.mark.parametrize("code", ["es", "es-419", "es-MX", "es-CL"])
def test_non_rehilada_varieties_do_strengthen(code):
    assert _t("hielo", code) == "ʝelo"
