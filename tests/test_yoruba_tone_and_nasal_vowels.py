"""Standard Yoruba: the three level tones and the five nasal vowels.

Yoruba writes tone on the vowel — acute for high, grave for low, nothing
for mid — and writes vowel nasalisation with a following ⟨n⟩. Both are
therefore recoverable from the spelling, and the spec is expected to emit
both. The expectations below follow the standard descriptions of the
language (Bamgboṣe, A. (1966) *A Grammar of Yoruba*, Cambridge University
Press; Akinlabi, A. (2004) "Yoruba"): three level tones with mid
unmarked in the orthography, seven oral vowels /i e ɛ a ɔ o u/, and five
nasal vowels /ĩ ɛ̃ ã ɔ̃ ũ/ with no nasal counterparts of /e/ and /o/.

Every string here is NFC-normalised before comparison because a tone mark
that follows a nasalisation tilde composes differently from one that
precedes it, and only the tilde-first order is the standard notation.
"""
import unicodedata

import pytest

from orthography2ipa.g2p import G2P


@pytest.fixture(scope="module")
def yo():
    return G2P("yo")


def nfc(s):
    return unicodedata.normalize("NFC", s)


def say(yo, word):
    return nfc(yo.transcribe_word(word))


# ── Tone is emitted, and mid is a mark of its own ─────────────────────
# The classic minimal triple on ⟨ọkọ⟩: mid-mid "hoe", mid-low "vehicle",
# low-low "spear". A transcription that drops tone collapses all three.
@pytest.mark.parametrize("word,expected", [
    ("ọkọ", "ɔ̄kɔ̄"),
    ("ọkọ̀", "ɔ̄kɔ̀"),
    ("ọ̀kọ̀", "ɔ̀kɔ̀"),
])
def test_tone_is_emitted_on_every_vowel(yo, word, expected):
    assert say(yo, word) == nfc(expected)


def test_the_three_okọ_readings_stay_distinct(yo):
    forms = {say(yo, w) for w in ("ọkọ", "ọkọ̀", "ọ̀kọ̀")}
    assert len(forms) == 3


@pytest.mark.parametrize("word,expected", [
    ("bá", "bá"), ("bà", "bà"), ("ba", "bā"),
    ("dé", "dé"), ("dè", "dè"), ("de", "dē"),
    ("ẹ́", "ɛ́"), ("ẹ̀", "ɛ̀"), ("ẹ", "ɛ̄"),
])
def test_each_tone_mark_maps_to_its_own_ipa_diacritic(yo, word, expected):
    assert say(yo, word) == nfc(expected)


def test_an_unmarked_vowel_is_mid_not_toneless(yo):
    """Mid is a specified tone, so ⟨ba⟩ is /bā/, never bare /ba/."""
    assert say(yo, "ba") != "ba"


# ── Nasal vowels ──────────────────────────────────────────────────────
# ⟨n⟩ after a nasalisable vowel, not itself before a vowel, spells
# nasalisation of that vowel and is not a consonant of its own.
@pytest.mark.parametrize("word,expected", [
    ("Abiọdun", "ābīɔ̄dũ̄"),
    ("Agbaakin", "āɡ͡bāākĩ̄"),
    ("Adediran", "ādēdīɾã̄"),
    ("Agbọnmiregun", "āɡ͡bɔ̃̄mĩ̄ɾēɡũ̄"),
])
def test_final_n_nasalises_the_vowel(yo, word, expected):
    assert say(yo, word) == nfc(expected)


@pytest.mark.parametrize("word", ["Abiọdun", "Agbaakin", "Adediran"])
def test_the_nasalising_n_is_not_a_separate_consonant(yo, word):
    assert not say(yo, word).endswith("n")


@pytest.mark.parametrize("word,expected", [
    ("ana", "ānã̄"),
    ("ẹni", "ɛ̄nĩ̄"),
    ("Aarinọla", "āāɾīnɔ̃̄lā"),
])
def test_n_before_a_vowel_stays_an_onset(yo, word, expected):
    """The before_vowel positional override: the ⟨n⟩ of ⟨ana⟩ is an onset
    consonant, so the vowel BEFORE it stays oral — /ānã̄/, not */ãnã̄/ and
    not the coda reading */ãā/. The vowel after it is nasal because a
    nasal onset nasalises what follows it."""
    out = say(yo, word)
    assert out == nfc(expected)
    decomposed = unicodedata.normalize("NFD", out)
    assert "n" in out
    assert decomposed.count("̃") == 1


@pytest.mark.parametrize("word", ["kenbu", "onta"])
def test_e_and_o_have_no_nasal_counterpart(yo, word):
    """Yoruba nasalises only /i ɛ a ɔ u/; ⟨en⟩ and ⟨on⟩ are not nasal
    vowel spellings, so the ⟨n⟩ must survive as a nasal consonant and the
    vowel before it must stay oral."""
    out = unicodedata.normalize("NFD", say(yo, word))
    assert "ŋ" in out or "n" in out
    assert "̃" not in out


# ── Notation order: tilde before tone ─────────────────────────────────
@pytest.mark.parametrize("word,expected", [
    ("ún", "ṹ"),
    ("ùn", "ũ̀"),
    ("un", "ũ̄"),
    ("ín", "ĩ́"),
    ("ọ́n", "ɔ̃́"),
    ("ẹ̀n", "ɛ̃̀"),
])
def test_nasal_and_tone_compose_in_the_standard_order(yo, word, expected):
    assert say(yo, word) == nfc(expected)


def test_tilde_precedes_the_tone_mark(yo):
    """u + tilde + acute composes to ṹ; the reverse order does not."""
    decomposed = unicodedata.normalize("NFD", say(yo, "ún"))
    assert decomposed.index("̃") < decomposed.index("́")


# ── A vowel after a nasal onset is nasal, and no ⟨n⟩ is written ────────
# Nasality is predictable after ⟨m⟩ and ⟨n⟩, so the orthography leaves it
# unwritten: ⟨mi⟩ ⟨mu⟩ ⟨mọ⟩ are /mĩ mũ mɔ̃/, and the ⟨n⟩ of ⟨inú⟩ is the
# nasal allophone of /l/, which occurs only before a nasal vowel —
# /īlṹ/ → [īnṹ] (Bamgboṣe 1969; Abraham 1958, whose dictionary writes the
# nasality out as ⟨inún⟩; editions not consulted, read via
# https://en.wikipedia.org/wiki/Yoruba_language).
@pytest.mark.parametrize("word,expected", [
    ("mi", "mĩ̄"),
    ("mu", "mũ̄"),
    ("mọ", "mɔ̃̄"),
    ("inú", "īnṹ"),
    ("ẹni", "ɛ̄nĩ̄"),
    ("ọmọ", "ɔ̄mɔ̃̄"),
])
def test_vowel_after_a_nasal_onset_is_nasalised(yo, word, expected):
    assert say(yo, word) == nfc(expected)


@pytest.mark.parametrize("word", ["mo", "me", "no", "ne"])
def test_e_and_o_stay_oral_after_a_nasal_onset(yo, word):
    """The nasalisation is bounded by the inventory: Yoruba has no
    /ẽ õ/, so ⟨mo⟩ ⟨me⟩ ⟨no⟩ ⟨ne⟩ keep an oral vowel."""
    assert "̃" not in unicodedata.normalize("NFD", say(yo, word))


@pytest.mark.parametrize("word,expected", [
    ("mí", "mĩ́"),
    ("mì", "mĩ̀"),
])
def test_nasalisation_after_a_nasal_onset_keeps_the_tone(yo, word, expected):
    """Nasalising the vowel must not lose or reorder its tone mark: the
    tilde still precedes the tone diacritic."""
    out = say(yo, word)
    assert out == nfc(expected)
    decomposed = unicodedata.normalize("NFD", out)
    assert decomposed.index("̃") < decomposed.index("́" if "í" in word else "̀")


# ── /ɛ/ stays oral after a nasal onset ─────────────────────────────────
# Phonemic /ɛ̃/ is confined to a single word in the source (ìyẹn~yẹn
# "that"), and the gold agrees: /ɛ/ after a nasal onset is nasal in only
# 3 of 55 contexts. The rule set is therefore restricted to /i a ɔ u/ and
# ⟨mẹ⟩/⟨nẹ⟩ keep an oral vowel, matching the core native numeral class
# (mẹfa, mẹta, mẹrin...).
@pytest.mark.parametrize("word,expected_first_vowel", [
    ("mẹfa", "ɛ̄"),
    ("mẹta", "ɛ̄"),
    ("mẹrin", "ɛ̄"),
])
def test_epsilon_stays_oral_after_a_nasal_onset(yo, word, expected_first_vowel):
    out = say(yo, word)
    assert expected_first_vowel in out
    assert "ɛ̃" not in out


# ── The syllabic nasal ─────────────────────────────────────────────────
# Yoruba allows only open syllables (Adesola, O., *Yoruba: A Grammar
# Sketch*, Afranaph, §2.1.2), so an ⟨n⟩ that is followed by a consonant
# cannot be a coda. It is either the nasalisation mark of the preceding
# vowel — which is why ⟨an in ọn un ẹn⟩ are read as nasal vowels — or a
# syllable nucleus of its own, a syllabic nasal that carries its own tone
# (same work, p. 2 n. 4: "Syllabic nasals can also bear tones in
# Yoruba"). The nasal-vowel reading is only available for the five vowels
# that have nasal counterparts, /ĩ ɛ̃ ã ɔ̃ ũ/ (same work, chart 3); /e/
# and /o/ have none, so ⟨en⟩ and ⟨on⟩ before a consonant can only be the
# syllabic reading. The same holds where no vowel precedes at all.
@pytest.mark.parametrize("word,expected", [
    # word-initial, nothing to nasalise
    ("nkọ", "ŋ̩̄kɔ̄"),
    ("njẹ", "ŋ̩̄dʒɛ̄"),
    ("nla", "ŋ̩̄lā"),
    # after ⟨o⟩ and ⟨e⟩, which have no nasal counterpart
    ("Aderonkẹ", "ādēɾōŋ̩̄kɛ̄"),
    ("otente", "ōtēŋ̩̄tē"),
])
def test_n_before_a_consonant_is_a_syllabic_nasal(yo, word, expected):
    assert say(yo, word) == nfc(expected)


@pytest.mark.parametrize("word", ["nkọ", "Aderonkẹ", "otente"])
def test_the_syllabic_nasal_is_a_tone_bearing_nucleus(yo, word):
    """Adding the nucleus adds a tone slot: the nasal carries the mid
    tone an unmarked orthographic vowel would carry, not a bare /n/."""
    out = unicodedata.normalize("NFD", say(yo, word))
    i = out.index("ŋ")
    assert out[i + 1:i + 3] == "̩̄"


@pytest.mark.parametrize("word,expected", [
    ("an", "ã̄"),
    ("ọn", "ɔ̃̄"),
    ("sùn", "sũ̀"),
    ("ana", "ānã̄"),
])
def test_the_nasal_vowel_and_onset_readings_are_untouched(yo, word, expected):
    """The syllabic reading must not eat the two readings that already
    work: ⟨n⟩ after a nasalisable vowel with nothing following spells
    nasalisation, and ⟨n⟩ before a vowel is an ordinary onset."""
    assert say(yo, word) == nfc(expected)
    assert "ŋ" not in say(yo, word)


@pytest.mark.parametrize("word", ["Kolonbia", "alukenbu", "ipenpeju"])
def test_the_syllabic_nasal_is_not_written_homorganic(yo, word):
    """The descriptive literature calls the syllabic nasal homorganic
    with the following consonant, but Standard Yoruba spells the labial
    variant ⟨m⟩ (⟨òrombó⟩), so an orthographic ⟨n⟩ before a labial is not
    evidence of a labial nasal. The wikipron gold agrees and transcribes
    a velar in every one of these environments — including where the
    spelling itself has ⟨m⟩ (⟨Abimbọla⟩ → ``a b í ŋ̄ b ɔ́ l á``) — so the
    spec emits one velar rather than guessing a place from the spelling.
    """
    assert "ŋ" in say(yo, word)
    assert "m" not in say(yo, word)
