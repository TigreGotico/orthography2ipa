"""Gawri (gwc) phonology: the committee's 1995 Perso-Arabic orthography, not
Urdu's letter values.

The reference read for these tests is Baart, Joan L. G. & Sagar, Muhammad
Zaman, *The Gawri Language of Kalam and Dir Kohistan* (SIL International,
2014), https://fli-online.org/documents/languages/gawri/gawri_introduction.pdf
-- §2.1.2 Table 2 (consonant inventory: aspiration only on voiceless stops and
affricates, no glottal stop), §2.3 "Script" (the four letters the committee
added for sounds Urdu lacks, and the vowel-diacritic rules).

The claims isolated below:

* §2.3 -- ݭ ݪ ڄ څ are the four committee additions, spelling ʂ ɬ ʈʂ t̪s;
* §2.1.2 Table 2 -- the aspirated series covers only voiceless obstruents, so
  the Urdu-looking digraphs بھ دھ ڈھ گھ جھ ڑھ spell plain (unaspirated) stops,
  not voiced aspirates;
* §2.1.2 Table 2 -- there is no glottal stop, so ع and ء are silent;
* §2.3 -- ر is the dental flap, distinct from retroflex ڑ;
* §2.3 -- word-final ہ is the vowel a, not the consonant h.
"""
from orthography2ipa import get, transcribe


def test_cites_baart_sagar():
    spec = get("gwc")
    ids = {s.id for s in spec.sources}
    assert "gwc_baart_sagar" in ids


def test_committee_letters_are_mapped():
    """The four letters the 1995 committee added for sounds Urdu lacks."""
    assert transcribe("ݭ", lang="gwc") == "ʂ"
    assert transcribe("ݪ", lang="gwc") == "ɬ"
    assert transcribe("ڄ", lang="gwc") == "ʈʂ"
    assert transcribe("څ", lang="gwc") == "t̪s"


def test_urdu_style_aspirate_digraphs_are_plain_voiced_stops():
    """بھ دھ ڈھ گھ جھ ڑھ spell plain b d̪ ɖ ɡ dʑ ɽ -- Gawri has no voiced
    aspirates (Baart & Sagar §2.1.2 Table 2)."""
    assert transcribe("بھ", lang="gwc") == "b"
    assert transcribe("دھ", lang="gwc") == "d̪"
    assert transcribe("ڈھ", lang="gwc") == "ɖ"
    assert transcribe("گھ", lang="gwc") == "ɡ"
    assert transcribe("جھ", lang="gwc") == "dʑ"
    assert transcribe("ڑھ", lang="gwc") == "ɽ"


def test_voiceless_aspirate_digraphs_survive():
    assert transcribe("ٹھ", lang="gwc") == "ʈʰ"
    assert transcribe("کھ", lang="gwc") == "kʰ"
    assert transcribe("چھ", lang="gwc") == "tɕʰ"
    assert transcribe("ڄھ", lang="gwc") == "ʈʂʰ"
    assert transcribe("څھ", lang="gwc") == "t̪sʰ"


def test_no_glottal_stop():
    """ع and ء are silent carriers, not a glottal stop (Table 2 has none)."""
    assert transcribe("عام", lang="gwc") == "aːm"
    assert transcribe("ئ", lang="gwc") == "j"


def test_dental_flap_contrasts_with_retroflex_flap():
    assert transcribe("رال", lang="gwc") == "ɾaːl"
    assert transcribe("ڑال", lang="gwc") == "ɽaːl"


def test_word_final_choti_he_is_the_vowel_a():
    out = transcribe("رہ", lang="gwc")
    assert out == "ɾa"


def test_palatal_series_uses_palatal_ipa_letters():
    """Baart & Sagar and Baart 2004 place š č ǰ in a PALATAL column, distinct
    from the retroflex column -- read as ɕ tɕ dʑ, not postalveolar ʃ tʃ dʒ."""
    assert transcribe("ش", lang="gwc") == "ɕ"
    assert transcribe("چ", lang="gwc") == "tɕ"
    assert transcribe("ج", lang="gwc") == "dʑ"
