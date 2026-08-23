"""Hausa (ha) phonology: the Boko orthography's glottalized series, its unit
labialized and palatalized velars, and the one consonant contrast the spelling
does not encode.

The reference description read for these tests is Paul Newman, "Hausa
Phonology", chapter 27 of A. S. Kaye & P. T. Daniels (eds.), *Phonologies of
Asia and Africa* (Eisenbrauns, 1996), pp. 537-552 — consonant inventory in
Table 27-1 on p. 538, segmental discussion on pp. 539-540.

The claims isolated below:

* p. 539 — the glottalized series is the implosives ⟨ɓ ɗ⟩ plus the ejectives
  ⟨ƙ⟩ and ⟨ts⟩, whose plain counterparts are /k/ and **/s/**; ⟨ts⟩ is therefore
  the ejective fricative /sʼ/, not an affricate /tsʼ/;
* p. 539 — ⟨ƴ⟩ (Niger ⟨ʼy⟩) is the glottalized palatal approximant, one
  phoneme with two spellings;
* pp. 538-539 — ⟨kw gw ƙw ky gy ƙy fy⟩ are unit phonemes contrasting with
  their plain counterparts before /a(a)/ (*gadaa* / *gwadaa* / *gyaɗaa*);
* pp. 539-540 — /r/ (apical tap or roll) and /ɽ/ (retroflex flap) contrast,
  the difference "is not indicated in orthography", and word-finally only the
  roll occurs;
* p. 539 — ⟨p⟩ is not in the inventory; /f/ is variably [f], [p] or [ɸ];
* p. 537 — the alphabet represents neither tone nor vowel length.
"""
from orthography2ipa import transcribe, get


# ─── Metadata ───────────────────────────────────────────────────────────────

def test_cites_newman_1996():
    """The chapter actually read for this spec is a declared source."""
    spec = get("ha")
    ids = {s.id for s in spec.sources}
    assert "newman1996" in ids


# ─── The glottalized series ────────────────────────────────────────────────

def test_ts_is_the_ejective_fricative_not_an_affricate():
    """⟨ts⟩ is the glottalized counterpart of /s/, so /sʼ/ — no /t/ onset.

    Newman 1996: 539 pairs ⟨ƙ⟩:/k/ with ⟨ts⟩:/s/.
    """
    out = transcribe("Katsina", lang="ha")
    assert "sʼ" in out
    assert "tsʼ" not in out


def test_implosives_and_ejective_kappa_survive():
    assert "ɓ" in transcribe("ɓarawo", lang="ha")
    assert "ɗ" in transcribe("ɗaya", lang="ha")
    assert "kʼ" in transcribe("ƙasa", lang="ha")


def test_hooked_y_and_apostrophe_y_are_one_phoneme():
    """⟨ƴ⟩ (Nigeria) and ⟨ʼy⟩ (Niger) spell the same glottalized approximant,
    so they must transcribe identically (Newman 1996: 539)."""
    assert transcribe("ƴa", lang="ha") == transcribe("ʼya", lang="ha")
    assert "j̰" in transcribe("ƴa", lang="ha")


# ─── Unit labialized / palatalized velars ──────────────────────────────────

def test_labialized_velars_are_single_segments():
    """⟨gw kw ƙw⟩ are phonemes, not consonant + /w/ (Newman 1996: 538-539)."""
    assert "ɡʷ" in transcribe("gwada", lang="ha")
    assert "kʷ" in transcribe("kwana", lang="ha")
    assert "kʷʼ" in transcribe("maƙwabci", lang="ha")


def test_palatalized_velars_are_single_segments():
    """⟨gy ky⟩ are palatalized velars, distinct both from plain /ɡ k/ + /j/
    and from the affricates ⟨c j⟩ (Newman 1996: 538 Table 27-1)."""
    out = transcribe("gyaɗa", lang="ha")
    assert "ɡʲ" in out and "ɡj" not in out
    assert "kʲ" in transcribe("kyau", lang="ha")


def test_palatalized_labial():
    assert "fʲ" in transcribe("fyace", lang="ha")


def test_plain_velar_contrasts_with_its_labialized_and_palatalized_partners():
    """Newman's minimal set before /a(a)/: gadaa / gwadaa / gyaɗaa."""
    plain = transcribe("gada", lang="ha")
    lab = transcribe("gwada", lang="ha")
    pal = transcribe("gyada", lang="ha")
    assert len({plain, lab, pal}) == 3


def test_doubled_digraph_writes_a_geminate_unit():
    """Only the first letter of a digraph is doubled to write gemination, but
    the phonemic result is a geminate of the digraph's unit, not a plain
    consonant before it: Newman 1996: 540 states "All Hausa consonants can
    be geminated" and gives /gásaššee/ 'roasted' as gasasshee — a geminate
    /ʃʃ/, written by doubling only the digraph's first letter. So ⟨kkw⟩ is
    /kʷ/ + /kʷ/, not /k/ + /kʷ/."""
    assert "kʷkʷ" in transcribe("Sakkwato", lang="ha")
    assert "ʃʃ" in transcribe("gasasshee", lang="ha")


# ─── The rhotic contrast the orthography hides ─────────────────────────────

def test_r_offers_both_rhotics_as_candidates():
    """/r/ and /ɽ/ contrast and Boko spells both ⟨r⟩ with no cue, so both
    readings must be reachable rather than one silently chosen
    (Newman 1996: 539-540)."""
    cands = get("ha")  # spec-level assertion: the grapheme carries both
    assert cands.graphemes["r"] == ["r", "ɽ"]
    readings = __import__("orthography2ipa").G2P("ha").word_candidates("sarki")
    assert "sarki" in readings and "saɽki" in readings


def test_the_flap_is_retroflex_not_an_alveolar_tap():
    """Newman 1996: 539 calls it the *retroflex flap*; /ɾ/ is a different
    segment and must not stand in for it."""
    spec = get("ha")
    assert "ɾ" not in spec.graphemes["r"]
    assert "ɾ" not in spec.allophones.get("r", [])


def test_word_final_r_is_the_roll_only():
    """"In word-final position, only r̃ occurs" (Newman 1996: 539)."""
    spec = get("ha")
    assert spec.positional_graphemes["r"]["word_final"] == ["r"]
    assert transcribe("teebur", lang="ha").endswith("r")


def test_word_final_n_is_pronounced_velar():
    """"In word final position /n/ is pronounced [ŋ]" (Newman 1996: 539).
    The statement is positional, so [ŋ] is reachable as a word-final candidate
    while /n/ stays the broad transcription both golds agree with."""
    engine = __import__("orthography2ipa").G2P("ha", expand_allophones=True)
    assert transcribe("bakin", lang="ha").endswith("n")
    assert any(r.endswith("ŋ") for r in engine.word_candidates("bakin", k=8))


def test_velar_n_never_leaves_word_final_position():
    """Newman's [ŋ] is confined to word-final /n/. Word-initial, intervocalic
    and half-geminate [ŋ] are not Hausa, so no candidate may contain them."""
    engine = __import__("orthography2ipa").G2P("ha", expand_allophones=True)
    for word in ("nasara", "hannu", "kwana", "ann"):
        for reading in engine.word_candidates(word, k=8):
            assert "ŋ" not in reading, (word, reading)


# ─── Loan ⟨p⟩ and the /f/ realizations ─────────────────────────────────────

def test_loan_p_is_transcribed_rather_than_dropped():
    """⟨p⟩ is absent from Table 27-1 but occurs in unassimilated loan
    spellings, where it is read [p] — and [p] is itself an attested
    realization of /f/ (Newman 1996: 539)."""
    out = transcribe("Paris", lang="ha")
    assert out.startswith("p")
    assert "ʔ" not in out


def test_f_records_its_attested_realizations():
    assert set(get("ha").allophones["f"]) >= {"f", "p", "ɸ"}


# ─── What the orthography cannot give ──────────────────────────────────────

def test_notes_record_the_tone_and_length_gap():
    """Boko writes neither tone nor vowel length (Newman 1996: 537), which is
    the dominant cost against a tone-marked gold and must be stated."""
    notes = get("ha").notes
    assert "tone" in notes and "length" in notes
    assert "ha.md" in notes


def test_engine_emits_no_tone_or_length_marks():
    """Nothing in the input can license them, so nothing may be invented."""
    out = transcribe("Abdulhamid", lang="ha")
    assert "ː" not in out
    assert not any(m in out for m in ("́", "̀", "̂"))
